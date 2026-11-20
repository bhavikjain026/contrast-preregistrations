# Report v25: answers on the other tasks among adults who matched 75% on task 504

Team Contrast · 20 November 2026 · Plan: v25 (tag v25, commit `be3f062`), in this repository.

This is the single run of plan v25 (tag v25), on Study 4a of Woike, Hertwig and Gigerenzer (2023). The full standard output is published unchanged as `report_v25_output.txt`, and the status line as `report_v25_status.txt`.

**Sources of the numbers.** The scoring tables come from `report_v25_output.txt`. The plan supplies the task values and the rule descriptions. The run record, the code review, the recount and the later inspection of stored values are identified separately below. A number marked "derived" is arithmetic on numbers from the named source.

It is a pre-specified exploratory description of data we had partly examined before (plan section 3). It reports counts. It has no interval, no test and no comparison between counts.

All counts use the primary window, within 1 + 10⁻⁷ percentage points, unless stated.

## The sentences fixed in the plan, with the run's numbers

> Counting an answer as a match when it is within 1 percentage point: in Study 4a of Woike, Hertwig and Gigerenzer (2023), 47 of 545 adults matched 75% on a problem where Bayes' rule and "100% minus the false-alarm rate" both give 75%. On a second problem, "100% minus the false-alarm rate" gives 90%, and none of the other 14 rules listed by Woike et al. does. 1 of the 47 matched 90% there; 0, 0 and 1 matched 60%, 70% and 80%, which no listed rule gives there. 1 matched 90% there and also 60% on a third problem, where three other listed rules also give 60%. 7 matched the Bayes answer on both the second problem and a fourth, where no other listed rule comes within 1 point of it. At most 11 could have, because 13 of all 545 adults matched it on the second problem and 11 on the fourth. These counts describe answers, not the methods behind them.

## Primary counts, within group F

Group F is the 47 people whose answer on task 504 matched 75%. On that task, Bayes' rule and 100% minus the false-alarm rate both give 75%, so a match there does not identify the method.

| | Count | Of | Share |
|---|---|---|---|
| 1. Matched 90% on task 402 | 1 | 47 | 2.1% |
| 2. Matched 90% on task 402 and 60% on task 501 | 1 | 47 | 2.1% |
| 3. Matched Bayes on tasks 402 and 502 | 7 | 47 | 14.9% |
| Reference: matched 60% on task 402 | 0 | 47 | 0.0% |
| Reference: matched 70% on task 402 | 0 | 47 | 0.0% |
| Reference: matched 80% on task 402 | 1 | 47 | 2.1% |

- The one person in count 1 is also the one person in count 2 (derived: count 2 is a subset of count 1, and both are 1).
- In F, 10 matched 60% on task 501, where three other listed rules also give that answer.
- Before the run, the whole-file counts were known to cap count 3 at 11. Count 3 was 7 of 47.

## The same counts for everyone else, and the single targets

Group N is the other 498 people. It is printed as context. The plan draws no conclusion from any difference between F and N.

| | F (47) | N (498) | Whole file (545) |
|---|---|---|---|
| Matched 90% on task 402 | 1 | 4 | 5 |
| Matched 90% on 402 and 60% on 501 | 1 | 1 | 2 |
| Matched Bayes on 402 and 502 | 7 | 1 | 8 |
| Matched 60% on task 402 | 0 | 14 | 14 |
| Matched 70% on task 402 | 0 | 2 | 2 |
| Matched 80% on task 402 | 1 | 3 | 4 |
| Matched 60% on task 501 | 10 | 74 | 84 |
| Matched Bayes on task 402 | 11 | 2 | 13 |
| Matched Bayes on task 502 | 9 | 2 | 11 |
| Gave the same answer four times | 0 | 3 | 3 |

The output also gives each count as a percentage of its group.

## S by D

S is the number of the two 100 − f targets matched (90% on task 402, 60% on task 501). D is the number of the two Bayes targets matched, 300/7 on task 402 and 1900/109 on task 502. Task 502 is not in S, as fixed in plan section 5: there 100 − f gives 50%, which is also the listed "50% rule" and the stated false-alarm rate. Its 50% count enters the check against plan section 3 below, and nothing else.

Group F:

| | D = 0 | D = 1 | D = 2 | Total |
|---|---|---|---|---|
| S = 0 | 24 | 6 | 7 | 37 |
| S = 1 | 9 | 0 | 0 | 9 |
| S = 2 | 1 | 0 | 0 (impossible by definition) | 1 |
| Total | 34 | 6 | 7 | 47 |

Before the run, at least 23 of the 47 were known to have D = 0 (derived from plan section 3: the whole file has 13 + 11 = 24 Bayes matches across the two tasks, which caps the number of people who matched either one at 24).

Group N:

| | D = 0 | D = 1 | D = 2 | Total |
|---|---|---|---|---|
| S = 0 | 418 | 2 | 1 | 421 |
| S = 1 | 76 | 0 | 0 | 76 |
| S = 2 | 1 | 0 | 0 (impossible by definition) | 1 |
| Total | 495 | 2 | 1 | 498 |

## Values recorded in plan section 3

The table gives the registered values and the values recorded in plan section 3, from our October analysis.

| | Run | Plan section 3 |
|---|---|---|
| Size of F | 47 | 47 |
| Size of N | 498 | 498 |
| Whole file, matched Bayes on task 402 | 13 | 13 |
| Whole file, matched Bayes on task 502 | 11 | 11 |
| Sum of task-response counts for 90% on 402, 60% on 501 and 50% on 502 | 146 | 146 |

## Secondary window of 0.1 + 10⁻⁷ percentage points

- At this window, F contains 47 people. Counts 1 and 2 are 1 and 1. The reference counts are 0, 0 and 1. Count 3 is 0 of 47, and in the whole file the Bayes single-target counts are 0 on both tasks.
- The Bayes targets are about 42.86% and 17.43%. Every recorded answer is within 10⁻⁷ points of an integer percent (545 of 545 on each task). The secondary window therefore excludes every recorded answer at those targets. The zero follows from the precision of the answers and the window. It does not show who attempted Bayes.
- The output gives the secondary counts for F, N and the whole file, and both secondary S-by-D tables.

## Run record

- **Order.** Tag v25 was pushed at 17:56:28 IST on 20 November 2026 (commit `be3f062`). The run started at 17:57:41 IST, 73 seconds later (derived from the run record), and finished within the same second, with exit status 0 and empty standard error.
- **Machine.** Bhavik's Mac, in the Claude app's Linux virtual machine, as for v23 and v24. Python 3.10.12, numpy 2.2.6 and scipy 1.15.3, as printed on the output's environment line. The loader's module imports numpy and scipy; no count uses them. The status record gives the run's date, time, machine and tag.
- **Checks before scoring.** The four input hashes were verified, as printed on the output's first line. No stop in plan section 7 was triggered.
- **Code check before the tag.** A second session that did not write the code read it against the plan and reported that all nine points it was asked to check held. It ran the 14 tests on Python 3.14.7. It noted two possible input errors (a wrong header row, or a non-numeric task ID) that would stop the run in a different way from the plan's other checks, and described where the run's metadata would be recorded. The two input errors did not occur.
- **Deviations from the plan.** None in the registered run. After seeing the result, we ran two unplanned checks that read `Study4a.xlsx`: a recount by a second implementation, and a summary check of the 18 stored values behind one difference in that recount. Both are described next.

| File | SHA-256 |
|---|---|
| `Study4a.xlsx` (input, verified by the run) | `0376fcfb346b277f320a6ffe3a82a781c56fe9764b05d1710e29bf873ebb0811` |
| `src/realdata_woike.py` (loader, verified by the run) | `4874dd3dc4dce7205584a234829809ca5550633880495ff7573b6d2c94bc4402` |
| `src/census.py` (imported by the loader, verified by the run) | `20712f082c7e2bc1f6c8fde6c900da2b08c9bf2d4e6f33130bc4bdf72bb6b059` |
| `src/bayes_strategies.py` (imported by the loader, verified by the run) | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `v25.py` (plan v25, Appendix A) | `ef58b8057ca0740a4073ada9b826100a73ecba635eb3a69c29cd2c716f13d79c` |
| `report_v25_output.txt` (standard output) | `445943996c4b3affc1a23dc1ecc1f1410b7501269494cef1e37e24f1af291817` |
| `report_v25_status.txt` (status line) | `e7367efa39149dc4fb6771a10f04acc1d26b8389c11cb71e1a77eff9d4903bc7` |

## Two checks made after the result was seen

We made these checks because the result was not the one we hoped for. We would not otherwise have made them, so we report both and what they found. They recount the same responses; they are not a second study. The registered output above is unchanged, and the result stands whatever the checks found.

- **Who and how.** On 20 November 2026 we prompted a separate AI coding session (Codex) to write its own recount from the plan's text, excluding its appendices, before seeing the registered output or our code. It is a second implementation by an AI session the team ran, not an audit by an outside researcher. It read the spreadsheet's raw XML itself, without our loader, and took every answer from its exact stored text. It ran once on Bhavik's Mac with Python 3.14.7. Its code and output were hashed before it opened the registered output.
- **What it covered.** Group sizes, target matches, repeated-answer counts and all S-by-D cells and margins, at both windows. The team reports that the scoring check passed. All of the plan's validity checks on the rows also passed: the header, the task IDs, the base rate (b), hit rate (h) and false-alarm rate (f) for each task, 545 people with one row per task, and every answer a finite number between 0 and 1.
- **October log.** The October log reports 5, 84 and 57 under its own rule classification for tasks 402, 501 and 502. The recount reports target matches of 5 at 90% on task 402, 84 at 60% on task 501 and 57 at 50% on task 502. The registered total of 146 counts task responses; one person can contribute on several tasks.
- **Order of events.** The recount confirmed that tag v25 points at commit `be3f062` and that the run started after the tag was pushed.
- **The whole-percent diagnostic.** The registered program counted an answer as a whole percent if it was within 10⁻⁷ points of one, as its output line says, and counted 545 on each task. The plan's text does not state a tolerance for this count. Using exact stored decimals, the recount counted 541, 545, 541 and 535 in task order 402, 501, 502 and 504.
- **The second check: the 18 stored values.** To settle the difference, we ran a further script once, on the stored text of the 18 affected entries (derived from the recount: 4 + 0 + 4 + 10). It printed summary figures and no answer value. It was run inline from the assistant's session and saved as a file afterwards, from the session record (`inspect_18_stored_values.py`). Each entry is a 19-character decimal between 1 × 10⁻¹⁵ and 4 × 10⁻¹⁵ points from a whole percent, and each reads as the same binary floating-point number as that whole percent. This is consistent with storage rounding. No target-match count depends on these entries. The smallest distance between a whole percent and the edge of any target window is 10⁻⁷ points (derived from the plan's windows: for example, 74 sits 10⁻⁷ points inside the window around 75), and 4 × 10⁻¹⁵ points is smaller than that.
- **Files.** These are kept in the tutor repository under `exploratory/v25_check/` and are not published, so readers cannot check the hashes now. We can show them on request.

  | File | SHA-256 |
  |---|---|
  | `check_v25.py` (recount code) | `fbb7f56da2eaa02923a4639b53a3cd8a6a6488210fe5e24d1b719f6b46bb1098` |
  | `check_output.txt` (recount output) | `26d006d919543f938375c19bcb9a6aaedca3ea846d57d363dfaf8311f75f128f` |
  | `check_report.txt` (recount report) | `f70c5c9e3d36dc4d2d3576598be60f0e33c025be7ed773feb83e697494243e7d` |
  | `inspect_18_stored_values.py` (second check) | `53f5644d159d72a1b2a7ae3cbff9cc51a5694a912218bf8eabc805a809f8623d` |
  | `inspect_18_output.txt` (its output) | `3f4786b2dfac9bc0ff780910d6897fe2b2bad228f928f9593e18ff9537e07f5d` |

## What this does not show

- That anyone used 100 − f on task 504. A person could use it there and nowhere else. We count answers; we cannot see methods.
- That anyone in F used Bayes on task 504. In F, 7 matched Bayes on both of tasks 402 and 502, 6 on one of them, and 34 on neither.
- Anything from a difference between F and N. N cannot contain anyone who answers 100 − f on every task, and it mixes every other kind of answer.
- A chance rate. The reference answers are other round numbers on one task, not a baseline.

## Limits specified in the plan

- **Arithmetic difficulty.** Bayes on task 504 is 30/40. On tasks 402 and 502 it is 3/7 and 19/109.
- **Round numbers and whole numbers.** The primary window includes 74%, 75% and 76% around the shared target. It includes 42% and 43% on task 402 and 17% and 18% on task 502 around the Bayes targets.
- **Other routes to the same numbers.** On task 504, hit rate plus false-alarm rate is also 75%. On task 501, three other listed rules give 60%.
- **Different rules on different tasks.** People can give answers that fit different rules on different tasks.
- **Story and order.** They varied between participants and are not in the file.
- **Scope.** One study of 545 adults recruited online, four tasks, no feedback. The 1-point window is ours. No task in it has a hit rate equal to Bayes, so this says nothing about that rule.
