# Report v24: answer collisions on a screening grid, and without 100% − false alarm

This is the single run of plan v24 (tag v24). The full output is published unchanged as `report_v24_output.txt`. Every number below comes from it, except where marked "derived", which means subtraction of two printed counts. All results use the tutor window (1 + 10⁻⁷ points) unless stated. The grids and the window are our design choices (plan sections 3 and 7).

## Primary result 1: grid G1

G1 is the grid we chose: every whole-percent combination with base rate 1–20%, hit rate 70–99% and false-alarm rate 1–20%, which is 12,000 sets, each counted once. With six methods:

> **In 11,441 of 12,000 G1 sets (95.3%), at least one whole-percent answer fits two of our six wrong methods.** Leaving out the base rate / joint occurrence pair, the figure is 10,880 of 12,000 (90.7%).

G1 is an arithmetic description of that grid. It is not a model of what chatbots, textbooks or students choose, and it is not an expected rate for any reply.

## Primary result 2: each chatbot's v23 Arm 1 sets, with six methods and with five (no 100% − false alarm)

| Chatbot (one reply) | Q1, six | Q1, five | Q1x, six | Q1x, five |
|---|---|---|---|---|
| ChatGPT | 18 of 20 | 17 of 20 | 18 of 20 | 9 of 20 |
| Gemini | 20 of 20 | 19 of 20 | 20 of 20 | 14 of 20 |
| Claude | 16 of 19 | 16 of 19 | 15 of 19 | 10 of 19 |

- **Q1.** Leaving out 100% − false alarm cost ChatGPT one Q1 set, Gemini one and Claude none.
- **Q1x.** Of the sets that counted for Q1x with six methods, ChatGPT lost 9 of 18 (50%), Gemini 6 of 20 (30%) and Claude 5 of 15 (33%). Derived: six-method Q1x minus five-method Q1x.

## Checks and run record

- **Check against report v23.** For each chatbot, the recomputed tuple (D, Q1, Q1x, Q3) at six methods matches report v23's published one: MATCH for all three. v20's 54 standard rows give 23 distinct sets, as v20 reported.
- **Run record.** The run started at 01:29:42 and finished at 01:31:29 IST on 20 November 2026, with exit status 0 and empty standard error (`report_v24_status.txt`). It ran on Bhavik's Mac, in the Claude app's Linux virtual machine (Python 3.10.12), as v23 did ([note on v23](note_v23_run_environment.md)). Both input hashes were verified before scoring, as printed on the output's first line.
- **Launch history.** An earlier attempt to launch the run in the background never started `v24.py`, and no output file was created. The foreground launch was the only scoring run.

| File | SHA-256 |
|---|---|
| `v24.py` (plan v24, section 6) | `1a0ff3953e72f78eb98be4c2001c86b42b6ddb69ee2fb3b71efe55c4ebee252b` |
| `report_v24_output.txt` (standard output) | `baf9c1db09ae77c607cfb7cb7506c0deea01cd98c57f92d2ec91fcd1ab7365cd` |
| `report_v24_status.txt` (status line) | `40f062ebc93d3bef12f15050ca57bf54eec8571a521ed4c0ad53799c0f5896d7` |

## Secondary diagnostics (pre-registered in plan v24; all printed in the output)

**Wider grids and v20**, at the tutor window:

| Set | Q1, six | Q1x, six | Q1, five | Q1x, five |
|---|---|---|---|---|
| G1 (12,000) | 95.3% | 90.7% | 73.7% | 26.3% |
| G2: b 1–50, h 50–99, f 1–50 (124,950) | 61.6% | 48.0% | 45.4% | 22.6% |
| G3: every whole-percent set from 1% to 99% with h > f (480,249) | 56.2% | 48.9% | 44.0% | 31.7% |
| v20 published problems (23) | 20 of 23 | 15 of 23 | 19 of 23 | 9 of 23 |

**Where the remaining five-method collisions come from.** Some five-method Q1 sets collide only through the base rate / joint occurrence pair. That was 8 of 17 sets for ChatGPT, 5 of 19 for Gemini and 6 of 16 for Claude. Derived: five-method Q1 minus five-method Q1x.

**v23 Arm 1 and v20 sets that lie on the G1 grid**, with six methods:

| Set | On the G1 grid | Q1 among them |
|---|---|---|
| ChatGPT | 13 of 20 | 13 of 13 |
| Gemini | 15 of 20 | 15 of 15 |
| Claude | 9 of 19 | 8 of 9 |
| v20 | 3 of 23 | 3 of 3 |

Six of v20's 23 sets lie within G1's bounds once fractional inputs count.

**The half-point window, a sensitivity check that is not the tutor's rule:**

| Set | Q1, six methods (tutor window → half point) | Q1x, five methods (tutor window → half point) |
|---|---|---|
| G1 | 95.3% → 51.6% | 26.3% → 3.3% (400 of 12,000) |
| ChatGPT | 18/20 → 16/20 | 9/20 → 6/20 |
| Gemini | 20/20 → 19/20 | 14/20 → 4/20 |
| Claude | 16/19 → 14/19 | 10/19 → 7/19 |

The size of the window matters a lot, especially once 100% − false alarm is not counted.

**A wrong answer with two explanations (Q1w), six methods.** On G1, Q1w equals Q1 (11,441 of 12,000). So every G1 set that collides has a colliding answer outside the correct-answer window, and a tutor that checks correctness first could still face ambiguity if given such an answer. Elsewhere, Q1w is slightly below Q1:

| Set | Q1w | Q1 |
|---|---|---|
| Claude | 15 of 19 | 16 of 19 |
| v20 | 18 of 23 | 20 of 23 |
| G2 | 60.5% | 61.6% |
| G3 | 55.3% | 56.2% |

**Three-point separation (Q4), all seven values.**
- On G1, no set passed: 0 of 12,000. On G2, 15.9% passed, and on G3, 16.1%.
- Q4 is report v23's Arm 2 rule: the 21 gaps among the same seven values must each be at least 3 points. The plan's tests confirm the code is identical.
- Report v23 found that every Arm 2 set met that rule. Any such set is therefore not one of G1's whole-percent points. If its inputs are whole percents, at least one of them lies outside G1's ranges. Fractional inputs could still lie within G1's ranges.
- v24 did not check where the Arm 2 sets lie. Doing so would need a new plan.

**Clean sets, six methods.** These have neither Q1 nor Q3 (a whole-percent answer fitting both the correct answer and a wrong method). On G1, 502 of 12,000 (4.2%) were clean, compared with 5,696 of 12,000 (47.5%) at the half-point window.

## What this does and does not show

**Shows** (primary):
- On our grid G1, at the tutor window, 95.3% of sets admit a whole-percent answer that fits two of our six wrong methods. Leaving out the base rate / joint occurrence pair, 90.7% do.
- For each chatbot's v23 reply, leaving out 100% − false alarm changes Q1 by at most one set. It reduces Q1x by 50% for ChatGPT, 30% for Gemini and 33% for Claude.

**Does not show:**
- that chatbots or textbook authors pick numbers from these grids, or with equal weights;
- that a grid fraction is an expected rate for any reply, or what students meet;
- that the grids explain v23;
- whether collisions vary with base rate in a way that would explain the chatbots' numbers;
- that any tutor misdiagnosed anyone, or how often students use any method.

There are no student answers, diagnoses or learning outcomes in this run.
