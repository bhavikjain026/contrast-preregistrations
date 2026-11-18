# Addendum v17.1 to plan v17: facts derived before the run, and added described tables

Written 19 November 2026. **To be published under tag v17.1 before plan v17 is run.** If plan v17 has already been run
when this is read, this addendum is void as a registration and its tables may be shown only as described,
after-the-run checks, labelled that way. **This is a simulation. No human data is read, used or produced.** Nothing
here changes a verdict, a primary or a stopping rule of plan v17.

## Why

After plan v17 was fixed, an outside review (a general-purpose AI assistant given the plan's text and no data) pointed
out that the direction of verdict 1 follows from arithmetic. We checked each point below against the frozen tutor's
code, without running any learner, and found them correct. We state them before the run so that the result is read
as what it is.

## A. Facts about plan v17, derived from the code before the run

**A1. Verdict 1's direction is fixed by design.**
- The fixed problem (90/60/20) gives whole-percent answers for all six wrong rules (40, 54, 60, 75, 80, 90), at least
  5 points apart. At noise up to ±2, a single-rule learner's second answer on it fits the learner's own rule exactly
  when the noise draw is −1, 0 or +1, and never fits another rule (that would need a gap of 3 or less). So **the fixed
  arm can never name a wrong rule** at noise 0, ±1 or ±2.
- Both arms share the second noise draw (plan v17, section 3). On a whole-percent target the adaptive answer fits
  for the same draws; on a fractional target (such as 3.75%) for a subset of them; and an adaptive session can end
  without a follow-up. So, except where an answer is clipped at 0% or 100%, **in every paired session the adaptive arm
  names the right rule only if the fixed arm does**.
- Consequence: of verdict 1's four outcomes, "adaptive better" and "trade-off" cannot occur (barring clipping). The
  run measures only the size of the fixed problem's advantage, which comes mainly from its whole-percent, widely
  spaced answers under a 1-point window, not from a better choice of question. Any "fixed better" result is always
  described that way: "largely because its answers are whole percents".
- The run checks both facts (A1 checks in `addendum_v17_1.py`).

**A2. The ambiguous-first-answer breakdown is empty by design.** With the default start, every first problem's seven
answers are at least 3 points apart (`screening_quiz.qualifies`, `MIN_GAP = 0.03`), so no first answer can fit two
wrong rules within 1 point. The breakdown in plan v17, section 5 will report 0 sessions. Its example ("like 45% on
60/75/30") was wrong: that problem is not in the default start's pool.

**A3. Plans v16 and v17 do not simulate the demo's start.** The live demo uses the tutor's ambiguous start, where the
first problem has two wrong rules giving the same answer (60/75/30, both 45). Plans v16 and v17 use the default start,
where no first problem has such a tie. Their results say nothing about the ambiguous start, and any slide showing
them says "default start".

**A4. Sessions share first problems.** A session's first problem depends only on its seed i, so the six wrong-rule
learners' sessions with the same i share a first problem (and so do Part 2's sessions with that i). The 12,000 paired
sessions are 2,000 groups of six. Plan v17's bootstrap resamples within each rule and ignores this.

## B. Added described tables (no pass or fail)

Computed by `addendum_v17_1.py` from the same `rows_v17.json`, after `report_v17.py`:

1. **A1 checks**: per noise level, paired sessions right-named in the adaptive arm but not the fixed arm (expected
   only with clipping) and fixed-arm wrong names (expected 0); Part 1 rows with an ambiguous first answer (expected
   0). Any other value is reported as a fault in this addendum's reasoning.
2. **Seed bootstrap** (A4): verdict 1's two differences at ±2 with a 95% interval from resampling seeds, all six
   rules' sessions of a seed together (10,000 times, seed 20261120). If this interval and plan v17's disagree on
   whether 0 is included, both are reported and the verdict is described as sensitive to the resampling.
3. **Told "correct"**: for every Part 2 kind, arm and noise level, the share of sessions told "correct" on the first
   answer. A learner using a wrong method who is told "correct" is a failure plan v17 did not count.
4. **Verdict 2 without repeated problems**: verdict 2 recomputed with sessions whose first problem is the fixed
   problem left out (identified from Part 1 rows with the same seed). Plan v17's verdict 2 stands; this is reported
   beside it.

## C. Seen before writing this addendum

Plan v17 as published, the frozen tutor's code, two outside reviews of the plan's text, and nothing from any run of
plan v17.

## D. Files

| File | SHA-256 |
|---|---|
| `addendum_v17_1.py` | `ff3826458eec1920d964bb15f07ee02c37aee71962dc871afb172b489bb09141` |

Run once, after `report_v17.py`: `python3 addendum_v17_1.py rows_v17.json > addendum_v17_1.txt`. The script imports
`report_v17.py` from plan v17 unchanged. `python3 addendum_v17_1.py --selftest` checks its two helpers on made-up rows.
