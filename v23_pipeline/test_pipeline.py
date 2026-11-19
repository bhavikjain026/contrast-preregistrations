"""Tests for split_build.py and agree.py, on made-up text only (no chatbot output). Run: python3 -m pytest -q"""
import csv
import hashlib
import json
import os
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import agree  # noqa: E402
import split_build as sb  # noqa: E402

REPLY = """Here are some problems.

1. A condition affects 2% of people. A test is positive for 90% of those with it and 5% of those without. What is the probability of the condition given a positive test? Answer: about 26.9%
2. In a town, 10% have it. Sensitivity is 80%, specificity 90%.
What is P(condition | positive)?
Solution: 0.08/(0.08+0.09) = 47.1%

Good luck!"""


def recs():
    return [
        {"line": 1, "part": 1, "dest": "log", "id": None, "text": "Here are some problems."},
        {"line": 3, "part": 1, "dest": "stem", "id": "1#1", "q": True,
         "text": "1. A condition affects 2% of people. A test is positive for 90% of those with it and 5% of "
                 "those without. What is the probability of the condition given a positive test?"},
        {"line": 3, "part": 2, "dest": "key", "id": "1#1", "text": " Answer: about 26.9%"},
        {"line": 4, "part": 1, "dest": "stem", "id": "2#1", "text": "2. In a town, 10% have it. Sensitivity is 80%, specificity 90%."},
        {"line": 5, "part": 1, "dest": "stem", "id": "2#1", "q": True, "text": "What is P(condition | positive)?"},
        {"line": 6, "part": 1, "dest": "key", "id": "2#1", "text": "Solution: 0.08/(0.08+0.09) = 47.1%"},
        {"line": 8, "part": 1, "dest": "log", "id": None, "text": "Good luck!"},
    ]


def lines():
    return REPLY.split("\n")


def test_good_split_passes():
    errs, order, pieces = sb.check_group(lines(), recs())
    assert errs == [] and order == ["1#1", "2#1"]
    stem = sb.render("t", order, pieces, "stem")
    assert "Answer" not in stem and "47.1" not in stem and "=== 2#1 ===\n2. In a town" in stem
    key = sb.render("t", order, pieces, "key")
    assert "=== 1#1 ===\n Answer: about 26.9%" in key


@pytest.mark.parametrize("mutate, msg", [
    (lambda r: r.pop(6), "not assigned"),                                        # a line dropped
    (lambda r: r.append(dict(r[0], part=2)), "rebuild"),                          # a line twice
    (lambda r: r[2].update(text=" Answer: about 26.9"), "rebuild"),              # text changed
    (lambda r: r[1].update(text=r[1]["text"] + " Answer: about 26.9%") or r.pop(2), "question mark"),  # leak
    (lambda r: r[4].update(q=False), "exactly one q"),
    (lambda r: r[3].update(q=True), "exactly one q"),
    (lambda r: r[1].update(id="1#2") or r[2].update(id="1#2"), "numbered 1, 2"),
    (lambda r: r[2].update(id="9#1"), "without any stem"),
    (lambda r: r[0].update(id="1#1"), "log piece"),
    (lambda r: r[5].update(q=True), "only a stem piece"),
    (lambda r: r[0].update(line=99), "does not exist"),
    (lambda r: r[0].update(dest="answer"), "dest must be"),
    (lambda r: r[1].update(id="1"), "id must look like"),
])
def test_bad_splits_fail(mutate, msg):
    r = recs()
    mutate(r)
    errs, _, _ = sb.check_group(lines(), r)
    assert any(msg in e for e in errs), errs


def test_stem_after_question_fails():
    r = recs()
    r[4]["q"] = False
    r[3]["q"] = True
    errs, _, _ = sb.check_group(lines(), r)
    assert any("continues after the question" in e for e in errs)


def test_no_question_mark_rules():
    ls = ["Find P(D|+) when 5% have it.", "Find P(D|+). Answer: 45%", "Find P(D|+). It is 45%"]
    ok = [{"line": 1, "part": 1, "dest": "stem", "id": "1#1", "q": True, "text": ls[0]},
          {"line": 2, "part": 1, "dest": "stem", "id": "2#1", "q": True, "text": ls[1]},
          {"line": 3, "part": 1, "dest": "stem", "id": "3#1", "q": True, "text": ls[2]}]
    errs, _, _ = sb.check_group(ls, ok)
    assert not any("1#1" in e for e in errs)
    assert any("2#1" in e for e in errs) and any("3#1" in e for e in errs)


def test_blank_lines_need_no_pieces_and_crlf():
    ls = ["a?", "", "   ", "b"]
    r = [{"line": 1, "part": 1, "dest": "stem", "id": "1#1", "q": True, "text": "a?"},
         {"line": 4, "part": 1, "dest": "key", "id": "1#1", "text": "b"}]
    assert sb.check_group(ls, r)[0] == []


def make_run(tmp, reply=REPLY, records=None, hashed=True):
    run = tmp / "v23_run"
    for d in ("replies", "split"):
        (run / d).mkdir(parents=True, exist_ok=True)
    (run / "replies" / "ChatGPT_arm1_attempt1.txt").write_text(reply, encoding="utf-8")
    h = hashlib.sha256(reply.encode()).hexdigest()
    (run / "hashes.txt").write_text((f"{h}  replies/ChatGPT_arm1_attempt1.txt\n" if hashed else ""), encoding="utf-8")
    rows = [["chatbot", "arm", "disposition", "used_file"], ["ChatGPT", "1", "ran", "ChatGPT_arm1_attempt1.txt"]]
    rows += [[c, a, "unavailable:test", ""] for (c, a) in sb.ROSTER if (c, a) != ("ChatGPT", "1")]
    with open(run / "manifest.csv", "w", newline="") as fh:
        csv.writer(fh).writerows(rows)
    with open(run / "split" / "ChatGPT_arm1.jsonl", "w", encoding="utf-8") as fh:
        for r in (records or recs()):
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return run


def test_main_ok_and_hash_guard(tmp_path, capsys):
    run = make_run(tmp_path)
    assert sb.main(str(run)) == 0
    rep = (run / "split_check.txt").read_text()
    assert (run / "stems" / "ChatGPT_arm1.txt").exists() and "ALL OK" in rep
    assert "not scored (logged): none; labels 1-20 with no occurrence: 3, 4," in rep
    run2 = make_run(tmp_path / "x", hashed=False)
    assert sb.main(str(run2)) == 1


def stems_csv(path, rows):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(agree.STEM_COLS)
        w.writerows(rows)


def stem_rows(slot1=("included", "2", "90", "5"), slot2=("included", "10", "80", "10")):
    out = [["ChatGPT", "1", "1", *slot1, ""], ["ChatGPT", "1", "2", *slot2, ""]]
    out += [["ChatGPT", "1", str(s), "missing", "", "", "", ""] for s in range(3, 21)]
    return out


def keys_csv(path, k1=("scored", "26.9"), k2=("scored", "47.1")):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(agree.KEY_COLS)
        w.writerow(["ChatGPT", "1", "1", *k1, ""])
        w.writerow(["ChatGPT", "1", "2", *k2, ""])
        for s in range(3, 21):
            w.writerow(["ChatGPT", "1", str(s), "none", "", ""])


def read(path):
    with open(path, newline="") as fh:
        return list(csv.reader(fh))


def test_agreement_end_to_end(tmp_path):
    run = make_run(tmp_path)
    assert sb.main(str(run)) == 0
    stems_csv(tmp_path / "A.csv", stem_rows())
    stems_csv(tmp_path / "B.csv", stem_rows(slot2=("included", "20/2", "80", "10.0")))
    agree.stems(str(run), str(tmp_path / "A.csv"), str(tmp_path / "B.csv"))
    fin = read(run / "stems_final.csv")
    assert len(fin) == 121 and fin[2] == ["ChatGPT", "1", "2", "included", "10", "80", "10"]
    assert fin[21][3] == "unavailable:test"
    keys_csv(tmp_path / "kA.csv")
    keys_csv(tmp_path / "kB.csv", k2=("scored", "47.10"))
    agree.keys(str(run), str(tmp_path / "kA.csv"), str(tmp_path / "kB.csv"))
    ex = read(run / "extract_final.csv")
    assert ex[0] == agree.EXTRACT_COLS and len(ex) == 121
    assert ex[1] == ["ChatGPT", "1", "1", "included", "2", "90", "5", "26.9", "scored"]
    assert ex[2][7:] == ["47.1", "scored"] and ex[3] == ["ChatGPT", "1", "3", "missing", "", "", "", "", ""]


def test_disagreements_are_mechanical(tmp_path):
    run = make_run(tmp_path)
    sb.main(str(run))
    stems_csv(tmp_path / "A.csv", stem_rows())
    stems_csv(tmp_path / "B.csv", stem_rows(slot1=("included", "2", "90", "6"),
                                            slot2=("excluded:derived", "", "", "")))
    agree.stems(str(run), str(tmp_path / "A.csv"), str(tmp_path / "B.csv"))
    fin = read(run / "stems_final.csv")
    assert fin[1][3] == "excluded:unresolved" and fin[2][3] == "excluded:unresolved"
    stems_csv(tmp_path / "B.csv", stem_rows())
    agree.stems(str(run), str(tmp_path / "A.csv"), str(tmp_path / "B.csv"))
    keys_csv(tmp_path / "kA.csv")
    keys_csv(tmp_path / "kB.csv", k1=("range", ""), k2=("scored", "47.2"))
    agree.keys(str(run), str(tmp_path / "kA.csv"), str(tmp_path / "kB.csv"))
    ex = read(run / "extract_final.csv")
    assert ex[1][3:] == ["included", "2", "90", "5", "", "unresolved"]
    assert ex[2][7:] == ["", "unresolved"]


@pytest.mark.parametrize("slot1, msg", [
    (("included", "2%", "90", "5"), "exact number"),
    (("included", "0", "90", "5"), "strictly between"),
    (("included", "2", "90", "1e-1"), "exact number"),
    (("excluded:unresolved", "", "", ""), "status must be"),
    (("excluded:derived", "2", "", ""), "must be empty"),
    (("missing", "", "", ""), "missing"),
])
def test_stem_validation(tmp_path, slot1, msg):
    run = make_run(tmp_path)
    sb.main(str(run))
    stems_csv(tmp_path / "A.csv", stem_rows(slot1=slot1))
    stems_csv(tmp_path / "B.csv", stem_rows())
    with pytest.raises(SystemExit, match=msg):
        agree.stems(str(run), str(tmp_path / "A.csv"), str(tmp_path / "B.csv"))


def test_slot3_cannot_be_included_without_occurrence(tmp_path):
    run = make_run(tmp_path)
    sb.main(str(run))
    rows = stem_rows()
    rows[2] = ["ChatGPT", "1", "3", "excluded:missing_number", "", "", "", ""]
    stems_csv(tmp_path / "A.csv", rows)
    with pytest.raises(SystemExit, match="exactly when"):
        agree.validate_stems(str(tmp_path / "A.csv"), str(run), [("ChatGPT", "1")])


def test_rows_for_all_slots_and_only_ran_groups(tmp_path):
    run = make_run(tmp_path)
    sb.main(str(run))
    stems_csv(tmp_path / "A.csv", stem_rows()[:-1])
    with pytest.raises(SystemExit, match="slot 20 is missing"):
        agree.validate_stems(str(tmp_path / "A.csv"), str(run), [("ChatGPT", "1")])
    stems_csv(tmp_path / "A.csv", stem_rows() + [["Gemini", "1", "1", "missing", "", "", "", ""]])
    with pytest.raises(SystemExit, match="not a group that ran"):
        agree.validate_stems(str(tmp_path / "A.csv"), str(run), [("ChatGPT", "1")])


def test_key_validation(tmp_path):
    run = make_run(tmp_path)
    sb.main(str(run))
    keys_csv(tmp_path / "kA.csv", k1=("none", "26"))
    with pytest.raises(SystemExit, match="empty unless"):
        agree.validate_keys(str(tmp_path / "kA.csv"), [("ChatGPT", "1")])
    keys_csv(tmp_path / "kA.csv", k1=("scored", "-5"), k2=("scored", "140"))
    agree.validate_keys(str(tmp_path / "kA.csv"), [("ChatGPT", "1")])   # outside 0..100 is scored as given


def test_no_v23_import():
    for f in ("agree.py", "split_build.py"):
        src = open(os.path.join(HERE, f), encoding="utf-8").read()
        assert "import v23" not in src and "from v23" not in src
