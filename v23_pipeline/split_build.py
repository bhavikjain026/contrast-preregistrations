"""Plan v23, section 5, step 1: the deterministic split check (written before any chatbot was asked).

  python3 split_build.py RUN_DIR

RUN_DIR (v23_run/) must contain:
  manifest.csv            chatbot,arm,disposition,used_file   one row per roster group (six rows)
                          disposition: ran | unavailable:<reason> | dropped:<reason>; used_file only when ran
  hashes.txt              `shasum -a 256` lines written at generation; every used file must be listed there
  replies/<used_file>     the saved reply, exactly as copied
  split/<chatbot>_arm<k>.jsonl   written by session C, one JSON object per line:
      {"line": n, "part": i, "dest": "stem"|"key"|"log", "id": "7#1"|null, "q": true|false, "text": "..."}
      line  = 1-based line number in the reply file (lines split on "\\n", a trailing "\\r" removed)
      part  = 1, 2, ... when C cuts one line into consecutive pieces; the pieces, in part order, must rebuild
              the line exactly (nothing added, dropped or changed)
      dest  = stem (problem text up to and including its question sentence), key (everything after the
              question for that occurrence), log (preamble, closing text, anything not part of an occurrence)
      id    = occurrence ID <label>#<n> for stem and key pieces; null for log pieces
      q     = true on exactly one stem piece per occurrence: the piece that ends with its question sentence

Checks (any failure: exit 1, C redoes the split, the failure is logged):
  * every used file is byte-for-byte the file whose SHA-256 is in hashes.txt;
  * every non-blank line appears exactly once, rebuilt exactly from its pieces; pieces only for real lines;
  * IDs well formed; for each label, occurrences numbered 1, 2, ... in order of first appearance;
  * every occurrence has stem text and exactly one q piece, which is its last stem piece;
  * key pieces belong to an occurrence that has a stem;
  * after the question sentence, no stem text contains "answer", "=", "≈" or "%": no stem piece of an
    occurrence comes after its q piece, and in the q piece the text after its last "?" contains none of
    them. A q piece with no "?" may not contain "answer", "=" or "≈" at all, nor end with "%".
It also logs every occurrence that is not a scored slot (any label other than 1..20, and any <n>#2 or later)
and every label 1..20 with no occurrence. On success it writes stems/<group>.txt, keys/<group>.txt, log/<group>.txt and split_check.txt,
and prints every output file's SHA-256. It reads no numbers and computes nothing about the problems.
"""
import csv
import hashlib
import json
import os
import re
import sys

ROSTER = [(c, a) for a in ("1", "2") for c in ("ChatGPT", "Gemini", "Claude")]
ID_RE = re.compile(r"^([^#\s]+)#([1-9][0-9]*)$")
FORBIDDEN = ("answer", "=", "≈", "%")


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def group_name(c, a):
    return f"{c}_arm{a}"


def read_manifest(run):
    with open(os.path.join(run, "manifest.csv"), newline="", encoding="utf-8") as fh:
        raw = list(csv.reader(fh))
    if not raw or raw[0] != ["chatbot", "arm", "disposition", "used_file"]:
        raise SystemExit("manifest.csv: header must be exactly chatbot,arm,disposition,used_file")
    rows = {}
    for i, cells in enumerate(raw[1:], start=2):
        if len(cells) != 4:
            raise SystemExit(f"manifest.csv line {i}: expected 4 fields")
        c, a, d, u = (x.strip() for x in cells)
        if (c, a) not in ROSTER:
            raise SystemExit(f"manifest.csv line {i}: {c} arm {a} is not in the roster")
        if (c, a) in rows:
            raise SystemExit(f"manifest.csv line {i}: duplicate group")
        if d == "ran":
            if not u:
                raise SystemExit(f"manifest.csv line {i}: a group that ran needs used_file")
        elif any(d.startswith(p) and len(d) > len(p) for p in ("unavailable:", "dropped:")):
            if u:
                raise SystemExit(f"manifest.csv line {i}: no used_file for a group that did not run")
        else:
            raise SystemExit(f"manifest.csv line {i}: invalid disposition {d!r}")
        rows[(c, a)] = (d, u)
    missing = [g for g in ROSTER if g not in rows]
    if missing:
        raise SystemExit(f"manifest.csv: missing groups {missing}")
    return rows


def read_hashes(run):
    out = set()
    with open(os.path.join(run, "hashes.txt"), encoding="utf-8") as fh:
        for line in fh:
            parts = line.split()
            if parts and re.fullmatch(r"[0-9a-f]{64}", parts[0]):
                out.add(parts[0])
    return out


def reply_lines(path):
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    return [ln[:-1] if ln.endswith("\r") else ln for ln in text.split("\n")]


def check_group(lines, records):
    """-> (errors, occurrences in order, pieces sorted). Pure function, used by the tests."""
    errs = []
    pieces = []
    for n, r in enumerate(records, start=1):
        where = f"record {n}"
        if not isinstance(r, dict) or set(r) - {"line", "part", "dest", "id", "q", "text"} or \
                not {"line", "part", "dest", "id", "text"} <= set(r):
            errs.append(f"{where}: needs exactly line, part, dest, id, text (and optional q)")
            continue
        q = r.get("q", False)
        if not (type(r["line"]) is int and type(r["part"]) is int and isinstance(r["text"], str)
                and type(q) is bool):
            errs.append(f"{where}: line and part must be integers, text a string, q true or false")
            continue
        if r["dest"] not in ("stem", "key", "log"):
            errs.append(f"{where}: dest must be stem, key or log")
            continue
        if r["dest"] == "log":
            if r["id"] is not None or q:
                errs.append(f"{where}: a log piece has id null and q false")
                continue
        else:
            if not isinstance(r["id"], str) or not ID_RE.match(r["id"]):
                errs.append(f"{where}: id must look like 7#1")
                continue
            if q and r["dest"] != "stem":
                errs.append(f"{where}: only a stem piece can be the q piece")
                continue
        if not 1 <= r["line"] <= len(lines):
            errs.append(f"{where}: line {r['line']} does not exist (the reply has {len(lines)} lines)")
            continue
        pieces.append(dict(r, q=q))
    if errs:
        return errs, [], []
    by_line = {}
    for p in pieces:
        by_line.setdefault(p["line"], []).append(p)
    for ln, ps in sorted(by_line.items()):
        parts = sorted(p["part"] for p in ps)
        if parts != list(range(1, len(ps) + 1)):
            errs.append(f"line {ln}: parts must be 1..{len(ps)} once each, found {parts}")
            continue
        rebuilt = "".join(p["text"] for p in sorted(ps, key=lambda p: p["part"]))
        if rebuilt != lines[ln - 1]:
            errs.append(f"line {ln}: the pieces do not rebuild the line exactly")
    for ln, text in enumerate(lines, start=1):
        if text.strip() and ln not in by_line:
            errs.append(f"line {ln}: non-blank line not assigned to stem, key or log")
    pieces.sort(key=lambda p: (p["line"], p["part"]))
    order, seen = [], set()
    for p in pieces:
        if p["dest"] == "log" or p["id"] in seen:
            continue
        seen.add(p["id"])
        order.append(p["id"])
    count = {}
    for oid in order:
        label, k = ID_RE.match(oid).groups()
        count[label] = count.get(label, 0) + 1
        if int(k) != count[label]:
            errs.append(f"{oid}: occurrences of label {label} must be numbered 1, 2, ... in order of appearance")
    for oid in order:
        st = [p for p in pieces if p["id"] == oid and p["dest"] == "stem"]
        if not st:
            errs.append(f"{oid}: key text without any stem text")
            continue
        qs = [p for p in st if p["q"]]
        if len(qs) != 1:
            errs.append(f"{oid}: needs exactly one q piece, found {len(qs)}")
            continue
        if qs[0] is not st[-1]:
            errs.append(f"{oid}: stem text continues after the question sentence")
        t = qs[0]["text"]
        if "?" in t:
            after = t[t.rindex("?") + 1:]
            bad = [w for w in FORBIDDEN if w in after.lower()]
            if bad:
                errs.append(f"{oid}: after the question mark the stem contains {bad}")
        else:
            bad = [w for w in ("answer", "=", "≈") if w in t.lower()]
            if bad or t.rstrip().endswith("%"):
                errs.append(f"{oid}: question piece without '?' contains {bad or ['a final %']}")
    return errs, order, pieces


def render(title, order, pieces, dest):
    out = [title]
    for oid in order:
        ps = [p for p in pieces if p["id"] == oid and p["dest"] == dest]
        if not ps:
            continue
        out.append(f"=== {oid} ===")
        buf, last = [], None
        for p in ps:
            if last == p["line"]:
                buf[-1] += p["text"]
            else:
                buf.append(p["text"])
            last = p["line"]
        out.extend(buf)
    return "\n".join(out) + "\n"


def main(run):
    manifest = read_manifest(run)
    hashes = read_hashes(run)
    report, failed, written = [], False, []
    for d in ("stems", "keys", "log"):
        os.makedirs(os.path.join(run, d), exist_ok=True)
    for (c, a) in ROSTER:
        g = group_name(c, a)
        disp, used = manifest[(c, a)]
        if disp != "ran":
            report.append(f"{g}: {disp} (no split)")
            continue
        rp = os.path.join(run, "replies", used)
        h = sha(rp)
        if h not in hashes:
            report.append(f"{g}: FAIL {used} has SHA-256 {h}, which is not in hashes.txt")
            failed = True
            continue
        lines = reply_lines(rp)
        sp = os.path.join(run, "split", g + ".jsonl")
        try:
            with open(sp, encoding="utf-8") as fh:
                records = [json.loads(x) for x in fh if x.strip()]
        except (OSError, ValueError) as e:
            report.append(f"{g}: FAIL cannot read {sp}: {e}")
            failed = True
            continue
        errs, order, pieces = check_group(lines, records)
        if errs:
            failed = True
            report.append(f"{g}: FAIL ({len(errs)} problems)")
            report.extend("  " + e for e in errs)
            continue
        nonblank = sum(1 for t in lines if t.strip())
        cnt = {d: len({p["line"] for p in pieces if p["dest"] == d}) for d in ("stem", "key", "log")}
        report.append(f"{g}: OK  {used} sha256 {h}; {nonblank} non-blank lines; {len(order)} occurrences; "
                      f"lines touching stem {cnt['stem']}, key {cnt['key']}, log {cnt['log']}")
        slots = {f"{n}#1" for n in range(1, 21)}
        unscored = [o for o in order if o not in slots]
        absent = [str(n) for n in range(1, 21) if f"{n}#1" not in order]
        report.append(f"  not scored (logged): {', '.join(unscored) or 'none'}; labels 1-20 with no occurrence: "
                      f"{', '.join(absent) or 'none'}")
        for dest, folder in (("stem", "stems"), ("key", "keys")):
            p = os.path.join(run, folder, g + ".txt")
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(render(f"# {c}, arm {a}: {folder} (occurrence IDs from session C)", order, pieces, dest))
            written.append(p)
        p = os.path.join(run, "log", g + ".txt")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(f"# {c}, arm {a}: text outside any occurrence\n")
            for x in pieces:
                if x["dest"] == "log":
                    fh.write(f"[line {x['line']} part {x['part']}] {x['text']}\n")
        written.append(p)
    verdict = "FAIL: session C redoes the split for the failed groups" if failed else "ALL OK"
    report.append(verdict)
    if not failed:
        report.append("SHA-256 of outputs:")
        report.extend(f"  {sha(p)}  {os.path.relpath(p, run)}" for p in written)
    text = "\n".join(report) + "\n"
    with open(os.path.join(run, "split_check.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text, end="")
    print(f"  {sha(os.path.join(run, 'split_check.txt'))}  split_check.txt")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    sys.exit(main(sys.argv[1]))
