"""Plan v23, section 5, steps 3 and 4: mechanical agreement (written before any chatbot was asked).

  python3 agree.py stems RUN_DIR stems_A.csv stems_B.csv      -> RUN_DIR/stems_final.csv, stems_agreement.txt
  python3 agree.py keys  RUN_DIR keys_A.csv  keys_B.csv       -> RUN_DIR/extract_final.csv, keys_agreement.txt

No person decides anything here. Where A and B agree, their value stands; where they disagree on any field,
the slot is excluded:unresolved (stems) or the key is unresolved (keys). Numbers are compared as exact
rationals, so "0.5" and "1/2" agree; the value written out is A's text. Nothing is rounded. This file does
not load the v23 scoring script and computes nothing about the problems: no Bayes value, no collision, no error.

stems_<X>.csv columns: chatbot,arm,slot,status,b,h,f,note
  one row per slot 1..20 for every group that ran (manifest.csv); none for groups that did not
  status: included | missing | excluded:<reason>, reason one of REASONS below
  b, h, f: exact percentages (a decimal such as 0.00004 or a fraction such as 100/2500000; no % sign),
           strictly between 0 and 100, only when included; otherwise empty
  missing exactly when the group's stem file has no occurrence <slot>#1
  note: free text (source sentence for an exclusion or an allowed subtraction); never compared
keys_<X>.csv columns: chatbot,arm,slot,key_status,key,note
  one row per slot 1..20 for every group that ran
  key_status: scored | none | range | nonnumeric | unresolved;  key: exact percentage only when scored
  (any value, including outside 0 to 100, as plan section 5 says)
"""
import csv
import hashlib
import os
import sys
from fractions import Fraction as Q

ROSTER = [(c, a) for a in ("1", "2") for c in ("ChatGPT", "Gemini", "Claude")]
SLOTS = [str(s) for s in range(1, 21)]
REASONS = ("missing_number", "unconvertible", "more_than_two_hypotheses", "more_than_one_result",
           "sequential_tests", "other_question", "inconsistent", "out_of_range", "derived", "overall_accuracy")
KEY_STATUSES = ("scored", "none", "range", "nonnumeric", "unresolved")
STEM_COLS = ["chatbot", "arm", "slot", "status", "b", "h", "f", "note"]
KEY_COLS = ["chatbot", "arm", "slot", "key_status", "key", "note"]
FINAL_STEM_COLS = ["chatbot", "arm", "slot", "status", "b", "h", "f"]
EXTRACT_COLS = ["chatbot", "arm", "slot", "status", "b", "h", "f", "key", "key_status"]


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def exact(text, where):
    t = text.strip()
    if not t or any(ch in t for ch in "%eE "):
        raise SystemExit(f"{where}: not an exact number: {text!r}")
    try:
        return Q(t)
    except (ValueError, ZeroDivisionError):
        raise SystemExit(f"{where}: not an exact number: {text!r}")


def read_csv(path, cols):
    with open(path, newline="", encoding="utf-8") as fh:
        raw = list(csv.reader(fh))
    if not raw or raw[0] != cols:
        raise SystemExit(f"{path}: header must be exactly {','.join(cols)}")
    rows = []
    for i, cells in enumerate(raw[1:], start=2):
        if not any(c.strip() for c in cells):
            continue
        if len(cells) != len(cols):
            raise SystemExit(f"{path} line {i}: expected {len(cols)} fields, found {len(cells)}")
        rows.append((i, dict(zip(cols, (c.strip() for c in cells)))))
    return rows


def read_manifest(run):
    rows = read_csv(os.path.join(run, "manifest.csv"), ["chatbot", "arm", "disposition", "used_file"])
    m = {(r["chatbot"], r["arm"]): r["disposition"] for _, r in rows}
    if sorted(m) != sorted(ROSTER) or len(rows) != 6:
        raise SystemExit("manifest.csv must list the six roster groups once each")
    return m


def first_occurrences(run, c, a):
    """Labels n (1..20) that have occurrence n#1 in the group's stem file."""
    p = os.path.join(run, "stems", f"{c}_arm{a}.txt")
    with open(p, encoding="utf-8") as fh:
        ids = {ln[4:-4] for ln in fh.read().split("\n") if ln.startswith("=== ") and ln.endswith(" ===")}
    return {n for n in SLOTS if f"{n}#1" in ids}


def by_slot(path, rows, ran):
    out = {}
    for i, r in rows:
        where = f"{path} line {i}"
        g = (r["chatbot"], r["arm"])
        if g not in ran:
            raise SystemExit(f"{where}: {g} is not a group that ran")
        if r["slot"] not in SLOTS:
            raise SystemExit(f"{where}: slot must be 1..20")
        k = g + (r["slot"],)
        if k in out:
            raise SystemExit(f"{where}: duplicate slot")
        out[k] = (where, r)
    for g in ran:
        for s in SLOTS:
            if g + (s,) not in out:
                raise SystemExit(f"{path}: {g} slot {s} is missing (write all 20 rows for each group that ran)")
    return out


def validate_stems(path, run, ran):
    rows = by_slot(path, read_csv(path, STEM_COLS), ran)
    firsts = {g: first_occurrences(run, *g) for g in ran}
    for (c, a, s), (where, r) in rows.items():
        st = r["status"]
        if st == "included":
            r["_v"] = []
            for col in ("b", "h", "f"):
                v = exact(r[col], f"{where} {col}")
                if not 0 < v < 100:
                    raise SystemExit(f"{where}: {col} must be strictly between 0 and 100 (else exclude: out_of_range)")
                r["_v"].append(v)
        elif st == "missing" or (st.startswith("excluded:") and st[9:] in REASONS):
            if any(r[col] for col in ("b", "h", "f")):
                raise SystemExit(f"{where}: b, h, f must be empty unless included")
        else:
            raise SystemExit(f"{where}: status must be included, missing or excluded:<one of {', '.join(REASONS)}>")
        if (st == "missing") != (s not in firsts[(c, a)]):
            raise SystemExit(f"{where}: 'missing' must be used exactly when the stem file has no occurrence {s}#1")
    return rows


def validate_keys(path, ran):
    rows = by_slot(path, read_csv(path, KEY_COLS), ran)
    for _, (where, r) in rows.items():
        if r["key_status"] not in KEY_STATUSES:
            raise SystemExit(f"{where}: key_status must be one of {', '.join(KEY_STATUSES)}")
        if r["key_status"] == "scored":
            r["_k"] = exact(r["key"], f"{where} key")
        elif r["key"]:
            raise SystemExit(f"{where}: key must be empty unless key_status is scored")
    return rows


def write(path, cols, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(cols)
        w.writerows(rows)


def stems(run, pa, pb):
    man = read_manifest(run)
    ran = [g for g in ROSTER if man[g] == "ran"]
    A, B = validate_stems(pa, run, ran), validate_stems(pb, run, ran)
    out, log, n_agree, n_unres = [], [], 0, 0
    for g in ROSTER:
        for s in SLOTS:
            if g not in ran:
                out.append([*g, s, man[g], "", "", ""])
                continue
            ra, rb = A[g + (s,)][1], B[g + (s,)][1]
            same = ra["status"] == rb["status"] and ra.get("_v") == rb.get("_v")
            if same:
                n_agree += 1
                out.append([*g, s, ra["status"], ra["b"], ra["h"], ra["f"]])
                if ra["status"] == "included" and [ra[c] for c in "bhf"] != [rb[c] for c in "bhf"]:
                    log.append(f"{g[0]} arm {g[1]} slot {s}: equal values written differently, A's text kept")
            else:
                n_unres += 1
                out.append([*g, s, "excluded:unresolved", "", "", ""])
                log.append(f"{g[0]} arm {g[1]} slot {s}: A {ra['status']} {ra['b']}|{ra['h']}|{ra['f']}  "
                           f"B {rb['status']} {rb['b']}|{rb['h']}|{rb['f']}  -> excluded:unresolved")
    fp = os.path.join(run, "stems_final.csv")
    write(fp, FINAL_STEM_COLS, out)
    head = [f"stems_A {sha(pa)}", f"stems_B {sha(pb)}",
            f"slots compared {n_agree + n_unres}: agree {n_agree}, unresolved {n_unres}"]
    finish(run, "stems_agreement.txt", head + log, fp)


def keys(run, pa, pb):
    man = read_manifest(run)
    ran = [g for g in ROSTER if man[g] == "ran"]
    fs = os.path.join(run, "stems_final.csv")
    final = {(r["chatbot"], r["arm"], r["slot"]): r for _, r in read_csv(fs, FINAL_STEM_COLS)}
    if sorted(final) != sorted(g + (s,) for g in ROSTER for s in SLOTS):
        raise SystemExit("stems_final.csv must have 120 rows, one per group and slot")
    A, B = validate_keys(pa, ran), validate_keys(pb, ran)
    out, log, n = [], [], {"agree": 0, "unresolved": 0}
    for g in ROSTER:
        for s in SLOTS:
            r = final[g + (s,)]
            if r["status"] != "included":
                out.append([*g, s, r["status"], "", "", "", "", ""])
                continue
            ka, kb = A[g + (s,)][1], B[g + (s,)][1]
            if ka["key_status"] == kb["key_status"] and ka.get("_k") == kb.get("_k"):
                n["agree"] += 1
                out.append([*g, s, "included", r["b"], r["h"], r["f"], ka["key"], ka["key_status"]])
            else:
                n["unresolved"] += 1
                out.append([*g, s, "included", r["b"], r["h"], r["f"], "", "unresolved"])
                log.append(f"{g[0]} arm {g[1]} slot {s}: A {ka['key_status']} {ka['key']}  "
                           f"B {kb['key_status']} {kb['key']}  -> unresolved")
    fp = os.path.join(run, "extract_final.csv")
    write(fp, EXTRACT_COLS, out)
    head = [f"stems_final {sha(fs)}", f"keys_A {sha(pa)}", f"keys_B {sha(pb)}",
            f"included slots compared {n['agree'] + n['unresolved']}: agree {n['agree']}, unresolved {n['unresolved']}"]
    finish(run, "keys_agreement.txt", head + log, fp)


def finish(run, name, lines, product):
    p = os.path.join(run, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"  {sha(product)}  {os.path.basename(product)}")
    print(f"  {sha(p)}  {name}")


if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] not in ("stems", "keys"):
        raise SystemExit(__doc__)
    {"stems": stems, "keys": keys}[sys.argv[1]](*sys.argv[2:])
