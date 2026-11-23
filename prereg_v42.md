# Plan v42 (23 November 2026): can a chatbot-written Bayes problem be fixed without changing its base rate or its answer?

Status: final (draft 4 after two outside reviews). Written 23 November 2026 and published byte-identical under tag
v42 before the run. The code was tested on made-up sets only and has not been run on any real set.
**No learners and no human data: this is arithmetic on the number sets that plan v23 locked.**

## 1. Question

Report v41 found that 54 of the 59 number sets in three chatbot replies have a collision: one whole-percent answer
fits two of our tutor's six wrong methods, or a wrong method and the correct answer. Within its cap of a 40-point
change to one number, 25 of the 54 could be fixed, with a median smallest fix of 19 points. Every such change alters
the exact correct answer.

A teacher often wants to keep the case they meant to teach: how common the condition is (the base rate) and the
answer. **For each set with a collision, can the collision be removed by changing the hit rate and the false-alarm
rate together, while the base rate and the exact correct answer stay the same?**

## 2. What the arithmetic fixes in advance (derived; written before this plan's author inspected any locked chatbot number set)

Write b, h and f for the base rate, hit rate and false-alarm rate as proportions, with 0 < b < 1 and 0 < f < h < 1,
and P for the correct answer. Elsewhere in this plan they are given in percentage points. "The window" is the tutor's
matching rule: within 1 + 10^-7 points.

- The posterior odds are b/(1 − b) × h/f. So with b fixed, P stays exactly the same if and only if h/f stays the
  same. In the two exact-answer searches (the primary and secondary A), every candidate keeps h'/f' = h/f.
- Along that line three of the seven answers do not move at all: the correct answer P, "base rate only" (b) and
  "equal priors" (h/(h + f)). The other four move with the scale: hit rate, 100% − false alarm, joint occurrence
  (b × h) and likelihood subtraction (h − f).
- **Prediction 1.** If some whole-percent answer fits two of the three answers that cannot move (P with b, P with
  equal priors, or b with equal priors; the two values need not be equal), no exact-answer candidate can remove it.
- **Prediction 2.** Joint occurrence minus subtraction is k × (b·h − (h − f)) when (h, f) is scaled by k. So the two
  are equal on the whole line exactly when f = h(1 − b), and such a set cannot be fixed by an exact-answer candidate.
- **Prediction 3.** If b is at most 1 point plus the window (b ≤ 2.0000001 points), the answer 1% fits both "base rate
  only" and joint occurrence (which lies between 0 and b) whatever h and f are. No search that keeps b can remove
  this, secondary B included.
- **Prediction 4.** If b is at least 99 points minus the window (b ≥ 97.9999999 points), then b < P < 100 because
  h > f, and the answer 99% fits both b and P whatever h and f are. No search that keeps b can remove this, secondary
  B included. In the exact-answer searches it is a case of prediction 1.
- **These predictions are sufficient, not exhaustive.** A set can also fail because its ratio has no other pair on the
  grid within 1 to 99 (if h/f = u/v in lowest terms, the whole-percent pairs are (ku, kv) with ku ≤ 99, and the
  original may be the only one), or because every candidate collides for another reason. A failure on the
  whole-percent grid can depend on that grid; secondary A uses half points.
- The script counts the sets each prediction marks and their union, and checks that no marked set is fixed. Any
  exception is reported as an error in this section, not hidden.

## 3. Definitions (fixed now)

- **Number sets.** Arm 1 of `extract_final.csv` (locked in addendum v23.1), read and counted exactly as plan v41
  does, with v41's own functions loaded unchanged from the hash-checked file. Distinct sets are counted within each
  reply, as in v41. The sets searched are those with a collision. Every included Arm 1 row must lie in
  0 < b < 100 and 0 < f < h < 100; otherwise the run stops and names the chatbot and slot.
- **Collision.** Plan v41's primary measure, imported unchanged: report v23's Q1 or Q3 under the window for
  whole-percent answers.
- **Candidate (primary).** The same base rate b, and a new hit rate h' and false-alarm rate f' that are whole
  percents from 1 to 99, with h' > f', h'/f' = h/f exactly, and (h', f') different from (h, f).
- **A fix** is a candidate with no Q1 and no Q3. **Its size** is the larger of |h' − h| and |f' − f|, in points.
  **The smallest fix** of a set is the fix of smallest size; among fixes of equal size, the one whose exact correct
  answer changes least (zero in the exact-answer searches), then the smaller h', then the smaller f'. Each set
  contributes at most one smallest fix to each search.
- **Secondary A (half-point rates).** The same, with h' and f' on half-point steps from 0.5 to 99.5.
- **Secondary B (correct answer within 0.5 percentage points).** Keep b; let h' and f' be any whole percents from 1
  to 99 with h' > f', (h', f') different from (h, f), and an exact correct answer within 0.5 points of P, inclusive.
  One rate or both may change. Two answers within 0.5 points can still round to different whole percents, and equal
  priors may move by more than 0.5 points. Predictions 1 and 2 do not apply to B; predictions 3 and 4 do.
- **Secondary C (published problems).** The primary, A and B searches on the published number sets of plan v20 that
  have a collision under the same measure (items locked in addendum v20.1; each must lie in the same domain, or the
  run stops and names the item).

## 4. What is reported (no threshold, no pass or fail)

Counts only. **No chatbot number set is printed**, because chatbot output stays out of public files. Published v20
sets are listed with their primary smallest fix, as report v20's output lists them.

- For each chatbot, and summed over Arm 1: sets with a collision; sets marked by predictions 1, 2, 3 and 4, by
  their union, and (for B) by 3 or 4; the exceptions, each set counted once; for the primary and secondaries A and B:
  sets with at least one candidate, sets fixed, and, among sets not fixed and not marked, those with no candidate
  at all and those whose candidates all collide; smallest fix of at most 1, 2, 3, 5, 10, 20 and 40 points; the median
  and largest smallest fix. For B, also the median and largest change in the correct answer at the smallest fix.
- The same for secondary C.
- Beside it, from report v41 and not recomputed: within a 40-point one-number change, 25 of 54, median 19 points.

**The only slide sentence allowed has this form:** "Among the 54 colliding sets in these three chatbot replies, X
could be fixed with whole-percent rates while keeping the base rate and the exact answer, by changing the hit and
false-alarm rates together. Among the fixed sets, the median size of the smallest fix was M points. The predictions
we wrote in advance ruled out an exact fix for Y sets. Arithmetic, not tested on people."
If X is 0, the sentence with M is left out. Y is the union of predictions 1 to 4, and the sentence with Y is used
only if the run reports zero exceptions. Other sets can also fail.

## 5. Limits written in advance, and earlier work

- Only the tutor's six wrong methods and its window, with whole-percent answers.
- Keeping b and P keeps the "case" only in two numbers. A fix changes how good the test in the story is; the wording
  of the story may no longer fit (for example a hit rate below the story's believable range). The script does not
  judge wording.
- A failure on the whole-percent grid can depend on the grid; secondary A shows the effect of half points.
- One reply per chatbot, asked once. Nothing here says how a next reply would vary.
- No students: a fix is a property of the numbers, not evidence that students would be diagnosed correctly.
- **Earlier work.** Choosing a problem's numbers so that common strategies give different answers is not new:
  Woike, Hertwig & Gigerenzer (2023, Cognitive Psychology) describe rules giving the same answer on Bayes items and
  chose numbers to avoid it in one study; Eichler, Böcherer-Linder & Vogel (2020, Frontiers in Psychology) chose task
  numbers so that students' strategies could be identified; Sedlmeier & Gigerenzer (2001, Journal of Experimental
  Psychology: General) checked wrong strategies' answers against their scoring window. We claim only the count
  reported here, not the idea, and we found no earlier work doing this repair with the base rate and the exact
  answer both held fixed. We do not claim to be first.

## 6. Seen before writing this plan (disclosed)

- **The author of this plan** is the AI assistant (Claude) that works for the team. It has read reports v23, v24 and
  v41 and their counts, not the locked chatbot number sets. Earlier AI sessions working for the team read those
  sets while building v23 and v24.
- The idea came from an outside AI (ChatGPT) on 23 November 2026, after it read report v41.
- **Outside review, two rounds, both by Gemini on 23 November 2026.** Round 1 received draft 2 and two spreadsheet
  files sent by mistake, which it says it did not open; it did not receive the code. It checked the algebra and the
  test arithmetic by hand. Round 2 received draft 3 and the four code files, and none of the locked inputs. It ran
  13 of the then 16 tests on Python 3.14.7 (the other 3 need files it did not have), and showed by changing the code
  in memory that no test caught a broken half-point search. Draft 4 takes in both rounds: predictions 3 and 4 with
  exact cutoffs, the causes of failure, the domain checks, a test that the half-point search finds 70 / 17.5 on
  10 / 80 / 20, a tie rule and its test, a forced-exception test, hash checks of each input separately, loading
  v41.py and v23.py from their checked paths, and an attempts log that allows only one start.
- **Two test fixtures come from the team's own materials:** 60 / 75 / 30 is the set our collision demo uses, and
  10 / 80 / 20 is the example in the frozen tutor's own description of an ambiguous start. Both are made-up numbers,
  not chatbot sets.
- No forecast is made: the author has seen v41's counts, and no team member who has not is free to forecast now.

## 7. Files and procedure

| File | SHA-256 |
|---|---|
| `v42.py` | `3def31952cc5d350efcaf02a8564df5837acf5eebe52386e9172d718ae9b5bb6` |
| `test_v42.py` (26 tests, made-up sets only) | `2d1069cfa52ff736166c7115f3137cfc92a544a6242bdd587d5b606b6c9228de` |
| `v41.py` (plan v41, loaded unchanged) | `26738d145e856b1e37ac31015e474f9d52ff33b16cfd1630a8e21fa87a8081ae` |
| `v23.py` (plan v23) | `f31694bb53e4dc56c558e44ffe409641e5efe7d3aaa9d174ff767d171946aec5` |
| `v22.py` (plan v22) | `4a9a8740f40623c96df080bed40561df02c2944257f36d4ee5a9042b1f14a3b5` |
| `v20.py` (plan v20) | `c71003c8602d912409bc5ea07941d8e93796716c6f607470b8c5436c84232db3` |
| `extract_final.csv` (addendum v23.1) | `bbeea3ea18d34e7020c42ead5d343527c235873958204461deb180d79a08787a` |
| `items_v20.csv` (addendum v20.1) | `5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236` |
| `src/bayes_strategies.py`, `src/topic_engine.py` (frozen tutor) | as in plan v41, checked through v41.py's own table |

The tests use made-up sets only. They cover: collisions between two answers that cannot move, equal (50 / 80 / 20,
80 / 60 / 15) and unequal but sharing one answer (49 / 80 / 20); exact joint-occurrence and subtraction ties that
survive every allowed rescaling (25 / 80 / 60, 60 / 75 / 30); low and high base rates (predictions 3 and 4) with
their exact cutoffs; a repair that keeps the unrounded answer, with literal expectations (10 / 80 / 20: answer 400/13,
primary fix 68 / 17 of size 12, half-point fix 70 / 17.5 of size 10); a near tie that moves into and out of the window
as the rates are rescaled (25 / 40 / 28, then 80 / 56 and 10 / 7); a ratio with no other whole-percent pair and one
half-point pair that collides (25 / 80 / 59); secondary B's window at exactly 0.5 points and just outside, and its tie
rule (10 / 80 / 30: 79 / 30 wins over 79 / 29); a forced wrong prediction counted once; a grid check with guards
against empty candidate lists or flags that are never set; and the script's refusals, each with its own reason.

1. Before launch, the person running it checks `v42.py` and `test_v42.py` against the SHA-256 values in this plan
   as published at tag v42, and runs `test_v42.py` on the Python used for the run.
2. `v42.py` checks every other hash above before it parses or analyses any input, loads `v41.py` and `v23.py` from the
   checked paths, and stops if v41's own counts (59 Arm 1 sets, 54 with a collision) or report v20's 23 distinct
   published sets are not reproduced, or if any input row lies outside the domain of section 3.
3. With `--run-after-tag` it first creates `v42_run_attempts.log` exclusively, so a second or competing launch cannot
   start. It records STARTED, then COMPLETE with the output's SHA-256 or STOPPED with the reason. The log is never
   deleted; an interrupted attempt stays recorded and blocks any further start.
4. It is run once, after this tag is public, with
   `python3 -B v42.py <repo root> v20_lock v22_run exploratory/v23 exploratory/v41 exploratory/v23/v23_run/extract_final.csv v20_lock/items_v20.csv --run-after-tag`.
   It saves its output in one step, then prints it. Report v42 publishes the output and the attempts log unchanged,
   whatever they show.
5. If the run stops, the cause is reported. Any fix to our own code after publication is a dated, published
   addendum with new hashes, and its own new attempts log, before the next start.
