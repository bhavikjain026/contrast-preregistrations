# Plan v24: are the v23 collisions a property of the numbers, and do they depend on "100% − false alarm"?

Status: published as tag v24, 20 November 2026, before `v24.py` is run on any real set. The plan collects no new responses or problems. The script enumerates three fixed grids deterministically and re-scores two locked files.

## 1. Why

**What v23 found.** Report v23 (tag v23-report) found that one reply each from ChatGPT, Gemini and Claude gave number sets where one whole-percent answer fits two of our tutor's six wrong methods: 18 of 20, 20 of 20 and 16 of 19 sets. Every Q1x set included the pair equal priors / 100% − false alarm.

**What the reviewers asked.** Two outside reviewers raised the questions a judge will ask:
1. Is this just the arithmetic of typical numbers?
2. Does the headline depend on counting 100% − false alarm as a mistake?

**The algebra behind question 1.** Write H and F for the hit and false-alarm rates as proportions. The signed gap between 100% − false alarm and equal priors is 100 · F(1 − H − F)/(H + F) points. That gap is zero when H + F = 1. It is small when false alarms are rare **and the hit rate is high**: for example, about 1.1 points at H = 0.8, F = 0.1. A rare false-alarm rate is not enough by itself. With H = 2F the gap is 100(1 − 3F)/3 points, about 33 points for small F. Report v23 said that "a low false-alarm rate by itself pushes" the two together. That was wrong, and it is corrected in the erratum published with this plan.

**When these checks were chosen.** We chose them after seeing v23. We fix them here, before anyone sees a v24 result.

## 2. Questions

- **A. Grids.** Across every whole-percent number set in three fixed grids, counted once each, how often do Q1, Q1x, Q1w, Q3, "clean" and Q4 happen?
- **B. Five methods, v23 Arm 1.** For each chatbot separately, the same measures are computed with six methods and with five, that is, without 100% − false alarm. The six-method values are checked against report v23. We also report how many of each chatbot's sets lie within each grid's bounds and on each grid, and how many of the on-grid sets have Q1 and Q1x.
- **C. v20 published problems.** The same measures are computed for the locked v20 standard problems, with six and with five methods, along with the same grid coverage.

**Windows.** For each method set, Q1, Q1x, Q1w, Q3 and "clean" are computed at two windows:
- the tutor's own window, 1 + 10⁻⁷ points, which is primary;
- a nearest-whole-percent window of half a point, where ties fit both neighbours. This is a sensitivity check, not the tutor's rule.

Q4 is computed once for each scoreable set, from all seven values.

**Primary line, fixed now.** The headline of report v24 will be these two results, whatever they show:
1. **Question 1:** the number and fraction of distinct sets in G1 for which one whole-percent answer from 0% to 100% fits at least two of the six wrong methods at the tutor window. That is Q1, with Q1x beside it.
2. **Question 2:** for each chatbot's Arm 1 sets separately, Q1 and Q1x at the tutor window with six methods and with five methods, side by side.

Everything else is a pre-registered secondary diagnostic. That covers G2, G3, the half-point window, Q1w, Q3, clean, Q4, pair counts, v20 and coverage. All of it is printed and reported, but none of it can replace the primary line as a headline.

## 3. Sets

**A. Grids.** Every whole-percent (b, h, f) in the bounds with h > f is counted, each set once.

| Grid | b | h | f | Sets |
|---|---|---|---|---:|
| G1, screening (primary) | 1–20 | 70–99 | 1–20 | 12,000 |
| G2, broad | 1–50 | 50–99 | 1–50 | 124,950 |
| G3, every whole-percent set from 1% to 99% with h > f | 1–99 | 1–99 | 1–99 | 480,249 |

- **G1** is meant to represent a low-base-rate, high-hit-rate screening problem. Its bounds are our design choice; no outside source fixes them.
- **G2 and G3** widen the bounds so that the effect of that choice can be seen. They change several bounds at once, so if the results differ, the grids cannot say which bound caused the difference.
- **What the grids leave out.** They contain no fractional inputs, no 0% or 100%, no input below 1% or above 99%, and no tests with h ≤ f. Each set has equal weight. They describe the arithmetic of the grid, not what anyone chooses.
- **The grids overlap.** G1 lies inside G2, and both lie inside G3.

**B. v23 Arm 1.**
- **Source.** The sets come from `extract_final.csv`, SHA-256 `bbeea3ea18d34e7020c42ead5d343527c235873958204461deb180d79a08787a`, locked in addendum v23.1. Only included Arm 1 rows are used, made distinct within each chatbot. The chatbots are not pooled.
- **Check against report v23.** For each chatbot, one line compares the tuple (D, Q1, Q1x, Q3), at six methods and the tutor window, with report v23's published tuple: (20, 18, 18, 1) for ChatGPT, (20, 20, 20, 3) for Gemini and (19, 16, 15, 2) for Claude. It is marked MATCH or MISMATCH. A mismatch is published unchanged, and no claim that relies on reproducing that tuple is made.
- **Why Arm 2 is not used.** The question concerns Arm 1. Report v23 also showed that every Arm 2 set met all 21 gaps of at least 3 points. Collisions under any subset of methods were therefore already impossible there.

**C. v20.**
- **Source.** The sets come from `items_v20.csv`, SHA-256 `5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236`, locked in addendum v20.1. Only rows of kind `standard` are used, converted exactly to percentages and made distinct by exact value.
- **Counts printed.** The script prints the raw count of standard rows and the distinct count, beside v20's previously reported 23. If they differ, both are reported.

**Input check.** `v24.py` reads each input file once and checks its SHA-256 before anything is scored, so the bytes checked are the bytes parsed. If either hash differs, nothing is scored.

## 4. Definitions (as coded in `v24.py`)

**Values.** These are exactly v23's: the correct answer and the six wrong methods, in points, in exact rational arithmetic. Subtraction is kept raw. A set whose formulas would divide by zero is counted as unscoreable and printed. Unscoreable sets are left out of every rate's denominator, and a group with none scoreable prints "N/A". The count D for the v23 check still includes them.

**Shared answer.** u and v share an answer at window w if some whole percent k in 0–100 has |k − u| ≤ w and |k − v| ≤ w. This is computed directly, and the tests check it against the loop over k = 0–100, including for negative values and values above 100.

**Measures,** for a method set M (six methods, or five without `false_alarm_complement`):

| Measure | Meaning |
|---|---|
| Q1 | some pair of methods in M shares an answer |
| Q1x | the same, ignoring the base rate / joint occurrence pair |
| Q1w | some k fits two methods in M and does **not** fit the correct answer at the same window. The base rate / joint occurrence pair counts. At the tutor window, this is a wrong answer with two explanations, which a tutor that checks correctness first would still face. At the half-point window, the correctness window also narrows to half a point. |
| Q3 | the correct answer shares an answer with some method in M |
| clean | neither Q1 nor Q3 |
| Q4 | all 21 gaps among the seven exact values are at least 3 points (v23's Arm 2 rule; it does not depend on M or the window) |

With six methods at the tutor window, Q1, Q1x and Q3 are exactly v23's, and Q4 is v23's Arm 2 rule. The tests check this against `v23.py` itself. "Clean" uses Q1, not Q1x, so the base rate / joint occurrence pair alone makes a set not clean. Q4 always uses all seven values, even when five methods are scored. Every measure is named with its method set and window when reported.

**Pair counts.** For six methods, at both windows, we print the number of distinct sets in which each of the 15 pairs shares an answer. A set can count under several pairs, so these counts show which pairs are present. They do not show which pairs a result depends on.

**Coverage.**
- *Within bounds:* b, h and f lie inside a grid's bounds with h > f. Fractional values are allowed.
- *On the grid:* within bounds, and every input is a whole percent.

## 5. Reporting

**What `v24.py` prints:**
- for each chatbot (B), for v20 (C) and for each grid (A): the set count, every measure for both method sets at both windows, both pair-count lines and Q4;
- for each chatbot and for v20: the coverage of each grid, and Q1 and Q1x (six methods, tutor window) among its on-grid sets, printed as "no eligible sets" when there are none;
- the v23 check line and the v20 count line.

All of it is reported, whatever it shows. The headline is the primary line in section 2. The run's standard output, standard error and exit status are saved and hashed, including if the run fails.

**Not done:**
- no intervals for the grids, because they are complete enumerations;
- no significance test;
- no pooling or ranking of chatbots;
- no other grid, window or method set.

**Display.** The grid results and the chatbot counts are shown in separate, labelled panels, each with its denominator. One panel is "one reply per chatbot (observed)"; the other is "every whole-percent set in the grid (arithmetic)". Neither panel is an expected count for the other, and neither is a null model.

**We will say:**
- "Of all N whole-percent sets in grid G1 (base rate 1–20%, hit rate 70–99%, false alarm 1–20%), X let one whole-percent answer fit two of our six wrong methods." The other grids are given alongside.
- "Without counting 100% − false alarm as a mistake, the counts were a of D₁ (ChatGPT), b of D₂ (Gemini) and c of D₃ (Claude)." The denominators are the ones the script prints. The same form is used for v20 and the grids. Q1x is always given beside Q1, because the base rate / joint occurrence pair can keep Q1 positive by itself.

**We will not say:**
- that chatbots or textbook authors choose numbers from these grids;
- that a grid fraction is what students meet;
- that the grids explain v23;
- anything about how often students use any method.

## 6. Code, tests and hashes

| File | SHA-256 |
|---|---|
| `v24.py` | `1a0ff3953e72f78eb98be4c2001c86b42b6ddb69ee2fb3b71efe55c4ebee252b` |
| `test_v24.py` | `9b12feb0a61099d5179b7016fe55dbabc86cc62cee9e9dd25d3d62def075d56e` |
| `v23.py` (needed by the tests only; tag v23) | `f31694bb53e4dc56c558e44ffe409641e5efe7d3aaa9d174ff767d171946aec5` |

**Tests.** Run with `python3 -m pytest -q -p no:cacheprovider test_v24.py`: 36 tests pass (20 November). They use only made-up numbers, and no whole-percent grid point is scored. They cover:
- `v23.py`'s own hash, checked before it is imported;
- `share()` against the loop over k at both windows, at the edges and on 3,000 random pairs;
- predictions equal to v23's, including sets with h < f, h = f, and inputs below 1%;
- every measure against a brute-force oracle, for both method sets and both windows, on 400 sets;
- the six-method measures equal to v23's, on 400 sets;
- a set that flips from colliding to clean when 100% − false alarm is dropped;
- Q1x ignoring only the low pair;
- a Q1 that is not Q1w, and a Q1w with Q3 true through a different answer;
- Q4, against v23's Arm 2 rule and against an independent sorted-gap check;
- the grid sizes, the bounds and grid tests (including h = f and h < f), and empty input;
- exact totals against the oracle, and all 15 pair counts at both windows against the brute-force loop;
- unscoreable sets, which are left out of denominators and never shown as clean;
- a non-empty coverage line on a made-up box outside every v24 grid;
- the parsers on made-up files (duplicates, unresolved keys, the same set under two chatbots, ignored arms and kinds);
- a check that a bad second hash stops the run before anything is scored;
- the full printed report on made-up files.

**Disclosure.** An earlier draft's tests scored one whole-percent set, (30, 80, 20), which lies in G2 and G3. Two tests used it. One checked that it collides with six methods and with five. The other included it in a two-set tally, which computed Q1, Q1x and Q3 for both method sets at both windows, and the six-method pair counts at the tutor window. No collision total over a study grid or a locked file was computed. The present tests use (30.1, 80.1, 19.9) instead.

**Run time.** About 4 seconds on 20,000 made-up sets. That projects to about 2 minutes for all 617,199 grid visits. The grids overlap, so some sets are visited more than once.

## 7. Known limits, stated in advance

- **The grids are our design choice.** Whole-percent inputs, equal weight, bounds between 1% and 99% and h > f are all choices, not a model of how anyone writes problems.
- **Two grids are being chosen.** Whole-percent *answers* come from the tutor's rule; whole-percent *inputs* are our grid choice.
- **Dropping one method is one sensitivity check.** The remaining five methods and the 1-point window are still ours.
- **The half-point window is not the tutor's rule.**
- **v23 is one reply per chatbot, and v20 is one collection of published problems.** Neither is a sample from a defined population.

## 8. Review before publication

**Who reviewed it.** On 20 November 2026, Gemini and ChatGPT ("Astra") reviewed two drafts of this plan. Neither ran it, and neither computed any of its results.

**Round 1 changes:**
- both input hashes are now checked before any scoring;
- the gap-formula statement is corrected, together with an erratum for report v23;
- the grid bounds are described as design choices, and G3 is renamed;
- the within-bounds and on-grid counts are split, and Q1 among on-grid sets is added;
- Q1w, "clean" and Q4 are added, and half-window pair counts are added;
- the v23 and v20 checks against earlier published counts are added;
- the side-by-side display rule is replaced with separate panels;
- the tests are rewritten, and the earlier fixture is disclosed.

**Round 2 changes:**
- unscoreable sets are left out of rate denominators;
- the primary line is fixed in section 2;
- Q1x is added to coverage;
- the Q1w, clean and Q4 wording is made precise;
- `v23.py` is checked before it is imported;
- all 15 pair counts and Q4 are checked independently, and fixtures with h < f, h = f and inputs below 1% are added;
- coverage is tested on a non-empty made-up box;
- the erratum states the gap's direction, and that a small gap does not by itself mean a shared answer.

**Left for a possible later plan, not added here:** structured or "human-like" grids, such as multiples of 5% or the h + f = 100 diagonal; fractional or below-1% inputs; and dropping other methods.

## 9. Timeline

1. Publish v24 (tag v24), together with the erratum to report v23.
2. Run `python3 v24.py <extract_final.csv> <items_v20.csv>` once, on Bhavik's Mac, in the same place as v23. Save the output and hash it.
3. Publish report v24 with the output unchanged, whatever it shows.
4. Only then change a slide.

## Appendix A — v24.py

```python
"""Plan v24 (written and tested BEFORE it is run on any real set; published with the plan).

  python3 v24.py V23_EXTRACT V20_ITEMS          prints the report

Three questions about the collisions report v23 found. All arithmetic: no people, and no chatbot is asked.
  A. How often do number sets collide on three fixed grids of whole-percent inputs (every point counted once)?
  B. What if 100% - false alarm is not counted as a wrong method (five methods instead of six)?
  C. The v20 published problems (locked item file), re-scored with v23's exact measures.
Each is computed with the tutor's window (1 + 1e-7 points, primary) and with a nearest-whole-percent window
(half a point, ties fit both neighbours; sensitivity only). Exact rational arithmetic (fractions.Fraction).
Both input files are checked by SHA-256 before anything is scored, and the checked bytes are the bytes parsed.
"""
import csv
import hashlib
import io
import math
import sys
from fractions import Fraction as Q
from itertools import combinations

V23_EXTRACT_SHA256 = "bbeea3ea18d34e7020c42ead5d343527c235873958204461deb180d79a08787a"   # addendum v23.1
V20_ITEMS_SHA256 = "5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236"     # addendum v20.1
# Report v23 (tag v23-report), Arm 1, six methods, tutor window: (D, Q1, Q1x, Q3). Printed beside the recomputation.
PUBLISHED_V23 = {"ChatGPT": (20, 18, 18, 1), "Gemini": (20, 20, 20, 3), "Claude": (19, 16, 15, 2)}
V20_REPORTED_DISTINCT = 23

SIX = ("hit_rate", "base_rate_only", "joint_occurrence", "likelihood_subtraction", "false_alarm_complement",
       "equal_priors")
FIVE = tuple(m for m in SIX if m != "false_alarm_complement")
METHOD_SETS = (("six methods", SIX), ("five methods (no 100% - f)", FIVE))
LOWPAIR = ("base_rate_only", "joint_occurrence")
HUNDRED = Q(100)
TUTOR = Q(1) + Q(1, 10 ** 7)
WINDOWS = (("tutor window, 1 + 10^-7 points", TUTOR),
           ("nearest whole percent (half-point window, ties fit both)", Q(1, 2)))
BOXES = (("G1 screening", (1, 20), (70, 99), (1, 20)),
         ("G2 broad", (1, 50), (50, 99), (1, 50)),
         ("G3 every whole-percent set from 1% to 99% with h > f", (1, 99), (1, 99), (1, 99)))
CHATBOTS = ("ChatGPT", "Gemini", "Claude")
MEASURES = ("Q1", "Q1x", "Q1w", "Q3", "clean")


def predictions(b, h, f):
    """Exact percentages in -> exact values in points. Identical to v23.predictions."""
    B, H, F = b / HUNDRED, h / HUNDRED, f / HUNDRED
    return {"bayes": HUNDRED * B * H / (B * H + (1 - B) * F),
            "hit_rate": HUNDRED * H, "base_rate_only": HUNDRED * B, "joint_occurrence": HUNDRED * B * H,
            "likelihood_subtraction": HUNDRED * (H - F), "false_alarm_complement": HUNDRED * (1 - F),
            "equal_priors": HUNDRED * H / (H + F)}


def span(u, v, w):
    """Whole percents k in 0..100 with |k - u| <= w and |k - v| <= w, as (lo, hi); empty if lo > hi."""
    return max(0, math.ceil(max(u, v) - w)), min(100, math.floor(min(u, v) + w))


def share(u, v, w):
    lo, hi = span(u, v, w)
    return lo <= hi


def measures(pr, methods, w):
    """-> ({measure: bool}, colliding pairs) for one set, a method set and a window.
    Q1: some k fits two methods.  Q1x: the same, ignoring the base rate / joint occurrence pair.
    Q1w: some k fits two methods and does NOT fit the correct answer (a wrong answer with two explanations).
    Q3: some k fits the correct answer and a method.  clean: neither Q1 nor Q3."""
    pairs = [p for p in combinations(sorted(methods), 2) if share(pr[p[0]], pr[p[1]], w)]
    q1 = bool(pairs)
    q1x = any(p != LOWPAIR for p in pairs)
    q1w = False
    for a, b in pairs:
        lo, hi = span(pr[a], pr[b], w)
        if any(abs(Q(k) - pr["bayes"]) > w for k in range(lo, hi + 1)):
            q1w = True
            break
    q3 = any(share(pr["bayes"], pr[m], w) for m in methods)
    return {"Q1": q1, "Q1x": q1x, "Q1w": q1w, "Q3": q3, "clean": not (q1 or q3)}, pairs


def q4(pr):
    """All 21 gaps among the seven exact values are at least 3 points (v23's Arm 2 rule)."""
    return min(abs(pr[a] - pr[b]) for a, b in combinations(pr, 2)) >= 3


def read_locked(path, digest):
    with open(path, "rb") as fh:
        data = fh.read()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SystemExit(f"{path}: SHA-256 is not the locked file; nothing was scored")
    return data.decode("utf-8")


def parse_v23(text):
    """Included Arm 1 rows -> {chatbot: (raw included row count, sorted distinct exact (b, h, f))}."""
    raw = {c: 0 for c in CHATBOTS}
    out = {c: set() for c in CHATBOTS}
    for r in csv.DictReader(io.StringIO(text, newline="")):
        if r["arm"] == "1" and r["status"] == "included":
            raw[r["chatbot"]] += 1
            out[r["chatbot"]].add((Q(r["b"]), Q(r["h"]), Q(r["f"])))
    return {c: (raw[c], sorted(out[c])) for c in CHATBOTS}


def parse_v20(text):
    """Standard rows (probabilities as text) -> (raw standard row count, sorted distinct exact (b, h, f) in %)."""
    rows = [r for r in csv.DictReader(io.StringIO(text, newline="")) if r["kind"] == "standard"]
    return len(rows), sorted({(HUNDRED * Q(r["base"]), HUNDRED * Q(r["hit"]), HUNDRED * Q(r["false_alarm"]))
                              for r in rows})


def grid(box):
    _, (b0, b1), (h0, h1), (f0, f1) = box
    for b in range(b0, b1 + 1):
        for h in range(h0, h1 + 1):
            for f in range(f0, f1 + 1):
                if h > f:
                    yield Q(b), Q(h), Q(f)


def within_bounds(t, box):
    """Exact b, h, f inside the box's bounds with h > f (fractional values allowed)."""
    _, (b0, b1), (h0, h1), (f0, f1) = box
    b, h, f = t
    return b0 <= b <= b1 and h0 <= h <= h1 and f0 <= f <= f1 and h > f


def on_grid(t, box):
    """Within bounds AND every input a whole percent: one of the box's enumerated points."""
    return within_bounds(t, box) and all(x.denominator == 1 for x in t)


def empty_tally():
    return {"n": 0, "unscoreable": 0, "q4": 0,
            "counts": {(m, w): dict.fromkeys(MEASURES, 0) for m, _ in METHOD_SETS for w, _ in WINDOWS},
            "pairs": {w: {} for w, _ in WINDOWS}}


def tally(triples):
    t = empty_tally()
    for tri in triples:
        t["n"] += 1
        try:
            pr = predictions(*tri)
        except ZeroDivisionError:
            t["unscoreable"] += 1
            continue
        t["q4"] += q4(pr)
        for mname, methods in METHOD_SETS:
            for wname, w in WINDOWS:
                res, pairs = measures(pr, methods, w)
                c = t["counts"][(mname, wname)]
                for k in MEASURES:
                    c[k] += res[k]
                if methods is SIX:
                    for p in pairs:
                        t["pairs"][wname][p] = t["pairs"][wname].get(p, 0) + 1
    return t


def pct(k, n):
    return f"{k}/{n} ({100 * k / n:.1f}%)" if n else f"{k}/0 (no sets)"


def rate(k, n):
    return pct(k, n) if n else "N/A (no scoreable sets)"


def block(title, t):
    n, u = t["n"], t["unscoreable"]
    s = n - u
    lines = [f"== {title}: {n} distinct number sets; {u} unscoreable; {s} scoreable (rates are out of the scoreable sets)"]
    for (mname, wname), c in t["counts"].items():
        lines.append(f"   {mname}, {wname}: " + "; ".join(f"{k} {rate(c[k], s)}" for k in MEASURES))
    for wname, _ in WINDOWS:
        lines.append(f"   pairs, six methods, {wname} (a set can count under several pairs): " +
                     "; ".join(f"{a}/{b} {t['pairs'][wname].get((a, b), 0)}" for a, b in combinations(sorted(SIX), 2)))
    lines.append(f"   all 21 gaps at least 3 points (Q4, all seven values): {rate(t['q4'], s)}")
    return lines


def coverage(sets):
    """For each box: within bounds, on the grid, and Q1 and Q1x (six methods, tutor window) among on-grid sets.
    On-grid sets have whole-percent inputs from 1% to 99%, so every one is scoreable."""
    lines = []
    for bx in BOXES:
        wb = [s for s in sets if within_bounds(s, bx)]
        og = [s for s in sets if on_grid(s, bx)]
        res = [measures(predictions(*s), SIX, TUTOR)[0] for s in og]
        tail = (f"Q1 {pct(sum(r['Q1'] for r in res), len(og))}, Q1x {pct(sum(r['Q1x'] for r in res), len(og))}"
                if og else "no eligible sets")
        lines.append(f"   {bx[0]}: within bounds (fractional inputs included) {pct(len(wb), len(sets))}; "
                     f"on the grid {pct(len(og), len(sets))}; among on-grid sets (six methods, tutor window): {tail}")
    return lines


def main(v23_path, v20_path):
    v23_text = read_locked(v23_path, V23_EXTRACT_SHA256)      # both checked before anything is scored
    v20_text = read_locked(v20_path, V20_ITEMS_SHA256)
    out = [f"# v24 inputs verified: v23 extract {V23_EXTRACT_SHA256}; v20 items {V20_ITEMS_SHA256}"]
    v23 = parse_v23(v23_text)
    for c in CHATBOTS:
        raw, sets = v23[c]
        t = tally(sets)
        out += block(f"B. v23 Arm 1, {c} ({raw} included rows)", t)
        six = t["counts"][("six methods", WINDOWS[0][0])]
        got = (t["n"], six["Q1"], six["Q1x"], six["Q3"])
        out.append(f"   check against report v23, six methods, tutor window (D, Q1, Q1x, Q3): recomputed {got}; "
                   f"published {PUBLISHED_V23[c]}; "
                   + ("MATCH" if got == PUBLISHED_V23[c] else "MISMATCH"))
        out += coverage(sets)
    raw, v20 = parse_v20(v20_text)
    t = tally(v20)
    out += block(f"C. v20 published standard problems ({raw} standard rows; v20 previously reported "
                 f"{V20_REPORTED_DISTINCT} distinct standard sets)", t)
    out += coverage(v20)
    for bx in BOXES:
        _, (b0, b1), (h0, h1), (f0, f1) = bx
        out += block(f"A. {bx[0]} grid: whole-percent b {b0}-{b1}, h {h0}-{h1}, f {f0}-{f1}, h > f", tally(grid(bx)))
    out.append("Grids count every whole-percent point once: a description of the arithmetic on that grid, not a model of "
               "what people or chatbots choose, and not an expected count for any reply. v23 counts are one reply per "
               "chatbot and are not pooled.")
    print("\n".join(out))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
```

## Appendix B — test_v24.py

```python
"""Tests for v24.py on made-up numbers only. No whole-percent grid point is scored here, and no v23, v20 or grid
result is computed. Needs v23.py (tag v23) beside this file. Run: python3 -m pytest -q -p no:cacheprovider"""
import csv
import hashlib
import io
import itertools
import os
import random
import re
import sys
from fractions import Fraction as Q

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
V23_PY_SHA256 = "f31694bb53e4dc56c558e44ffe409641e5efe7d3aaa9d174ff767d171946aec5"
with open(os.path.join(HERE, "v23.py"), "rb") as _fh:        # checked BEFORE v23 is imported
    if hashlib.sha256(_fh.read()).hexdigest() != V23_PY_SHA256:
        raise RuntimeError("v23.py beside this file is not the published file (tag v23)")

sys.path.insert(0, HERE)
import v23  # noqa: E402
import v24  # noqa: E402

FIT, HALF = v24.TUTOR, v24.WINDOWS[1][1]
SYM = (Q(301, 10), Q(801, 10), Q(199, 10))        # h + f = 100, not a grid point


def made_up(rng):
    """Non-whole made-up percentages (never a v24 grid point), with h > f."""
    b = Q(rng.randint(1, 9899), 100) + Q(1, 7)
    f = Q(rng.randint(1, 9000), 100) + Q(1, 11)
    h = f + Q(rng.randint(1, int((Q(99) - f) * 100) - 1), 100) + Q(1, 13)
    return b, min(h, Q(9999, 100)), f


def oracle(pr, methods, w):
    """Brute force over k = 0..100."""
    fit = {k: {m for m in ("bayes",) + tuple(methods) if abs(Q(k) - pr[m]) <= w} for k in range(101)}
    wrong = {k: s - {"bayes"} for k, s in fit.items()}
    q1 = any(len(s) >= 2 for s in wrong.values())
    q1x = any(len(s) >= 2 and s != set(v24.LOWPAIR) for s in wrong.values())
    q1w = any(len(wrong[k]) >= 2 and "bayes" not in fit[k] for k in fit)
    q3 = any("bayes" in fit[k] and wrong[k] for k in fit)
    return {"Q1": q1, "Q1x": q1x, "Q1w": q1w, "Q3": q3, "clean": not (q1 or q3)}


def test_constants():
    assert v24.V23_EXTRACT_SHA256 == "bbeea3ea18d34e7020c42ead5d343527c235873958204461deb180d79a08787a"
    assert v24.V20_ITEMS_SHA256 == "5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236"
    assert v24.PUBLISHED_V23 == {"ChatGPT": (20, 18, 18, 1), "Gemini": (20, 20, 20, 3), "Claude": (19, 16, 15, 2)}
    assert FIT == v23.FIT and HALF == Q(1, 2)
    assert v24.FIVE == ("hit_rate", "base_rate_only", "joint_occurrence", "likelihood_subtraction", "equal_priors")


ODD = [(Q(101, 10), Q(201, 10), Q(301, 10)),     # h < f: raw subtraction negative
       (Q(3, 10), Q(997, 10), Q(7, 10)),          # b and f below 1%
       (Q(501, 10), Q(401, 10), Q(401, 10))]      # h = f


def test_v23_source_hash_was_checked():
    with open(os.path.join(HERE, "v23.py"), "rb") as fh:
        assert hashlib.sha256(fh.read()).hexdigest() == V23_PY_SHA256


def test_predictions_equal_v23():
    rng = random.Random(1)
    for t in [made_up(rng) for _ in range(300)] + ODD:
        assert v24.predictions(*t) == v23.predictions(*t)


def brute_share(u, v, w):
    return any(abs(Q(k) - u) <= w and abs(Q(k) - v) <= w for k in range(101))


@pytest.mark.parametrize("u, v, w", [
    (Q(5), Q(7), FIT), (Q(5), Q(7) + Q(1, 10 ** 6), FIT), (Q(-1), Q(0), FIT), (Q(-3, 2), Q(-1, 2), FIT),
    (Q(-2), Q(-2), FIT), (Q(101), Q(100), FIT), (Q(203, 2), Q(203, 2), FIT), (Q(1023, 10), Q(100), FIT),
    (Q(1, 2), Q(3, 2), HALF), (Q(1, 2), Q(16, 10), HALF), (Q(447, 5), Q(448, 5), HALF), (Q(179, 2), Q(181, 2), HALF),
    (Q(0), Q(0), HALF), (Q(-6, 10), Q(-7, 10), HALF)])
def test_share_edges(u, v, w):
    assert v24.share(u, v, w) == brute_share(u, v, w)


def test_share_random_equals_brute():
    rng = random.Random(2)
    for _ in range(3000):
        u = Q(rng.randint(-3000, 13000), rng.choice([1, 7, 100, 999]))
        v = u + Q(rng.randint(-400, 400), rng.choice([100, 97, 1000]))
        for w in (FIT, HALF):
            assert v24.share(u, v, w) == brute_share(u, v, w)


def test_measures_equal_oracle_both_method_sets_and_windows():
    rng = random.Random(3)
    for _ in range(400):
        pr = v24.predictions(*made_up(rng))
        for _, methods in v24.METHOD_SETS:
            for _, w in v24.WINDOWS:
                assert v24.measures(pr, methods, w)[0] == oracle(pr, methods, w)


def test_six_methods_tutor_window_equals_v23():
    rng = random.Random(4)
    for t in [made_up(rng) for _ in range(400)] + ODD:
        pr = v24.predictions(*t)
        res, pairs = v24.measures(pr, v24.SIX, FIT)
        amb, vpairs, _ = v23.tutor_ambiguity(pr)
        assert res["Q1"] == amb and sorted(pairs) == vpairs
        assert res["Q1x"] == any(p != ("base_rate_only", "joint_occurrence") for p in vpairs)
        assert res["Q3"] == bool(v23.wrong_looks_right(pr))


def base_pr(**kw):
    pr = {"bayes": Q(50), "hit_rate": Q(90), "base_rate_only": Q(2), "joint_occurrence": Q(30),
          "likelihood_subtraction": Q(70), "false_alarm_complement": Q(80), "equal_priors": Q(60)}
    pr.update(kw)
    return pr


def test_flip_when_false_alarm_complement_is_dropped():
    pr = base_pr(false_alarm_complement=Q(605, 10))         # shares 60/61 with equal priors only
    six, p6 = v24.measures(pr, v24.SIX, FIT)
    five, p5 = v24.measures(pr, v24.FIVE, FIT)
    assert six["Q1"] and six["Q1x"] and six["Q1w"] and not six["clean"]
    assert not five["Q1"] and not five["Q1x"] and not five["Q1w"] and five["clean"]
    assert p6 == [("equal_priors", "false_alarm_complement")] and p5 == []
    pr = base_pr(false_alarm_complement=Q(51))              # fits the correct answer only
    assert v24.measures(pr, v24.SIX, FIT)[0]["Q3"] and not v24.measures(pr, v24.FIVE, FIT)[0]["Q3"]


def test_q1x_ignores_only_the_low_pair_and_q1w():
    pr = base_pr(joint_occurrence=Q(18, 10))
    res, pairs = v24.measures(pr, v24.SIX, FIT)
    assert res["Q1"] and not res["Q1x"] and pairs == [("base_rate_only", "joint_occurrence")] and res["Q1w"]
    pr = base_pr(base_rate_only=Q(49), joint_occurrence=Q(51))   # their only shared k (50) is the correct answer
    res, _ = v24.measures(pr, v24.SIX, FIT)
    assert res["Q1"] and res["Q3"] and not res["Q1w"] and not res["clean"]
    pr = base_pr(bayes=Q(49), base_rate_only=Q(50), joint_occurrence=Q(50))   # 50 fits all three; 51 misses Bayes
    res, _ = v24.measures(pr, v24.SIX, FIT)
    assert res["Q1"] and res["Q3"] and res["Q1w"]
    half = v24.measures(pr, v24.SIX, HALF)[0]                    # at half a point the correctness window is also
    assert half["Q1w"] and not half["Q3"]                         # half a point: 50 no longer fits Bayes (49)


def test_symmetric_set_keeps_colliding_without_complement():
    pr = v24.predictions(*SYM)
    assert pr["hit_rate"] == pr["false_alarm_complement"] == pr["equal_priors"]
    assert v24.measures(pr, v24.FIVE, FIT)[0]["Q1x"]           # hit rate and equal priors still coincide


def independent_q4(pr):
    v = sorted(pr.values())
    return all(b - a >= 3 for a, b in zip(v, v[1:]))


def test_q4_equals_v23_arm2_rule_and_independent_check():
    rng = random.Random(6)
    for t in [made_up(rng) for _ in range(300)] + ODD:
        pr = v24.predictions(*t)
        assert v24.q4(pr) == (v23.arm2_min_gap(pr) >= 3) == independent_q4(pr)


def test_q4():
    assert not v24.q4(v24.predictions(*SYM))
    pr = {"bayes": Q(10), "hit_rate": Q(13), "base_rate_only": Q(16), "joint_occurrence": Q(19),
          "likelihood_subtraction": Q(22), "false_alarm_complement": Q(25), "equal_priors": Q(28)}
    assert v24.q4(pr) and not v24.q4(dict(pr, equal_priors=Q(2799, 100)))


def test_grid_sizes():
    assert [sum(1 for _ in v24.grid(bx)) for bx in v24.BOXES] == [12000, 124950, 480249]


def test_within_bounds_and_on_grid():
    g1, g2 = v24.BOXES[0], v24.BOXES[1]
    t = (Q(1), Q(80), Q(96, 10))
    assert v24.within_bounds(t, g1) and not v24.on_grid(t, g1)
    assert not v24.within_bounds((Q(1, 2), Q(80), Q(101, 10)), g1)
    assert not v24.within_bounds((Q(101, 10), Q(691, 10), Q(101, 10)), g1)
    assert not v24.within_bounds((Q(101, 10), Q(50), Q(50)), g2)      # h == f
    assert not v24.within_bounds((Q(101, 10), Q(50), Q(503, 10)), g2)  # h < f


def test_empty_tally_and_block():
    t = v24.tally([])
    assert t["n"] == 0 and all(v == 0 for c in t["counts"].values() for v in c.values())
    lines = v24.block("empty", t)
    assert len(lines) == 1 + 4 + 2 + 1 and "N/A (no scoreable sets)" in lines[1]
    assert v24.pct(0, 0) == "0/0 (no sets)" and v24.pct(1, 3) == "1/3 (33.3%)"


def test_unscoreable_sets_are_not_counted_as_clean():
    t = v24.tally([(Q(0), Q(1, 3), Q(0)), (Q(0), Q(1, 5), Q(0))])
    lines = v24.block("all unscoreable", t)
    assert "2 distinct number sets; 2 unscoreable; 0 scoreable" in lines[0]
    assert all("N/A (no scoreable sets)" in l and not re.search(r"\d%\)", l) for l in lines[1:5])
    assert "Q4, all seven values): N/A (no scoreable sets)" in lines[-1]
    t = v24.tally([(Q(0), Q(1, 3), Q(0)), SYM])
    assert "1/1 (100.0%)" in v24.block("mixed", t)[1]           # SYM collides; denominator is 1, not 2


def test_tally_exact_counts_against_oracle():
    rng = random.Random(5)
    sets = [made_up(rng) for _ in range(60)] + [SYM]
    t = v24.tally(sets)
    assert t["n"] == 61
    for mname, methods in v24.METHOD_SETS:
        for wname, w in v24.WINDOWS:
            exp = dict.fromkeys(v24.MEASURES, 0)
            for s in sets:
                for k, v in oracle(v24.predictions(*s), methods, w).items():
                    exp[k] += v
            assert t["counts"][(mname, wname)] == exp
    for wname, w in v24.WINDOWS:
        for a, b in itertools.combinations(sorted(v24.SIX), 2):
            exp = sum(brute_share(v24.predictions(*s)[a], v24.predictions(*s)[b], w) for s in sets)
            assert t["pairs"][wname].get((a, b), 0) == exp
    assert t["q4"] == sum(independent_q4(v24.predictions(*s)) for s in sets)


def test_coverage_non_empty_on_a_made_up_box(monkeypatch):
    tiny = ("T tiny", (1, 2), (100, 100), (1, 1))                 # h = 100: outside every v24 grid
    monkeypatch.setattr(v24, "BOXES", (tiny,))
    sets = [(Q(2), Q(100), Q(1)), (Q(3, 2), Q(100), Q(1)), (Q(5), Q(50), Q(1))]
    assert v24.on_grid(sets[0], tiny) and not v24.on_grid(sets[1], tiny) and v24.within_bounds(sets[1], tiny)
    exp = oracle(v24.predictions(*sets[0]), v24.SIX, FIT)
    line = v24.coverage(sets)[0]
    assert "within bounds (fractional inputs included) 2/3 (66.7%); on the grid 1/3 (33.3%)" in line
    assert f"Q1 {v24.pct(int(exp['Q1']), 1)}, Q1x {v24.pct(int(exp['Q1x']), 1)}" in line


def test_tally_counts_unscoreable():
    t = v24.tally([(Q(0), Q(1, 3), Q(0))])
    assert t["n"] == 1 and t["unscoreable"] == 1


def write_v23(rows):
    s = io.StringIO()
    w = csv.writer(s, lineterminator="\n")
    w.writerow(v23.COLUMNS)
    w.writerows(rows)
    return s.getvalue()


def test_parse_v23():
    text = write_v23([
        ["ChatGPT", "1", "1", "included", "1/2", "80", "10", "5", "scored"],
        ["ChatGPT", "1", "2", "included", "0.5", "80", "10.0", "", "unresolved"],       # same set as slot 1
        ["ChatGPT", "1", "3", "included", "7/3", "61", "9", "", "unresolved"],          # distinct, unresolved key
        ["ChatGPT", "2", "1", "included", "3", "80", "10", "5", "scored"],              # arm 2: ignored
        ["Gemini", "1", "1", "included", "1/2", "80", "10", "5", "scored"],             # same set, other chatbot
        ["Claude", "1", "1", "excluded:out_of_range", "", "", "", "", ""]])
    got = v24.parse_v23(text)
    assert got["ChatGPT"] == (3, [(Q(1, 2), Q(80), Q(10)), (Q(7, 3), Q(61), Q(9))])
    assert got["Gemini"] == (1, [(Q(1, 2), Q(80), Q(10))]) and got["Claude"] == (0, [])


def test_parse_v20():
    s = io.StringIO()
    w = csv.writer(s, lineterminator="\n")
    w.writerow(["source", "item_id", "location", "base", "hit", "false_alarm", "kind", "quote"])
    w.writerow(["S1", "a", "p1", "0.01", "0.8", "0.096", "standard", "x"])
    w.writerow(["S1", "b", "p2", "0.010", "0.80", "0.0960", "standard", "x"])
    w.writerow(["S2", "c", "p3", "1/3", "0.9", "0.05", "standard", "x"])
    w.writerow(["S8", "d", "p4", "0.5", "0.6", "0.4", "orderflow", "x"])
    raw, sets = v24.parse_v20(s.getvalue())
    assert raw == 3 and sets == [(Q(1), Q(80), Q(96, 10)), (Q(100, 3), Q(90), Q(5))]


def test_main_checks_both_hashes_before_scoring(tmp_path, monkeypatch, capsys):
    a, b = tmp_path / "a.csv", tmp_path / "b.csv"
    a.write_text(write_v23([["ChatGPT", "1", "1", "included", "1/2", "80", "10", "5", "scored"]]))
    b.write_text("source,item_id,location,base,hit,false_alarm,kind,quote\n")
    monkeypatch.setattr(v24, "V23_EXTRACT_SHA256", hashlib.sha256(a.read_bytes()).hexdigest())
    called = []
    monkeypatch.setattr(v24, "tally", lambda *x: called.append(1))
    with pytest.raises(SystemExit, match="nothing was scored"):
        v24.main(str(a), str(b))
    assert called == [] and capsys.readouterr().out == ""


def test_main_full_report_on_made_up_files(tmp_path, monkeypatch, capsys):
    a, b = tmp_path / "a.csv", tmp_path / "b.csv"
    a.write_text(write_v23([["ChatGPT", "1", "1", "included", "301/10", "801/10", "199/10", "5", "scored"]]))
    b.write_text("source,item_id,location,base,hit,false_alarm,kind,quote\nS1,a,p,0.0101,0.801,0.0961,standard,x\n")
    monkeypatch.setattr(v24, "V23_EXTRACT_SHA256", hashlib.sha256(a.read_bytes()).hexdigest())
    monkeypatch.setattr(v24, "V20_ITEMS_SHA256", hashlib.sha256(b.read_bytes()).hexdigest())
    monkeypatch.setattr(v24, "BOXES", (("T tiny", (1, 2), (100, 100), (1, 1)),))   # h = 100: outside every v24 grid
    v24.main(str(a), str(b))
    out = capsys.readouterr().out
    assert "B. v23 Arm 1, ChatGPT (1 included rows): 1 distinct number sets" in out
    assert "MISMATCH" in out and "B. v23 Arm 1, Gemini (0 included rows): 0 distinct number sets" in out
    assert "1 standard rows; v20 previously reported 23 distinct standard sets" in out
    assert "A. T tiny grid: whole-percent b 1-2, h 100-100, f 1-1, h > f: 2 distinct number sets" in out
    assert "no eligible sets" in out
```
