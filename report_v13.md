# Report v13: secondary analysis of the Steib et al. (2025) open trial data

**Plan:** v13 (tag v13, `prereg_steib2025_secondary.md`, SHA-256 `b8cf04968110f23a9737d8535387ba294dc34c5aa69045fae9332e86c0bdc866`), published on 17 November 2026 before the analysis was run. **Run once** on 18 November 2026, 01:42:56 to 01:43:11 by the cluster's clock (job 14418 on the university cluster, exit status 0), with `steib2025/steib_analysis.py` (SHA-256 `3edea828f11f74657176d29006e1f58b0aea20667eeee53a886d37e47254edbb`, the frozen record's hash).

**Data.** Steib, N., Büchter, T., Eichler, A., Binder, K., Krauss, S., Böcherer-Linder, K., Vogel, M., & Hilbert, S. (2025). How to teach Bayesian reasoning: An empirical study comparing four different probability training courses. *Learning and Instruction*, 95, 102032. https://doi.org/10.1016/j.learninstruc.2024.102032. Data: the article's supplementary file, CC BY 4.0, SHA-256 `b5e06520ddd15c8bf72de0ebe4c83e25328dfc57d72ddb22a173c238e8a14f84`. **515 real students** (law and medicine). All credit for the trial, the tasks, the scoring and the strategy labels belongs to the authors. No row of the data is published here.

**Sources of the numbers.** Every number below is copied from the run's output, published unchanged as `report_v13_output.json`. The count tables of plan sections 4.3 and 4.5 are published as `report_v13_tables.md`, formatted from that output with no new computation. Every label is the authors'. Intervals are exact Clopper–Pearson 95% intervals unless stated.

**Published late.** The run was on 18 November. This report was published on 22 November, four days later. No number was changed or recomputed, and nothing was re-run.

## 1. How common each wrong method is at pre-test (plan 4.1)

Pooled over subjects, among the 1,306 wrong answers to the three PPV tasks (one student can give up to three, so these intervals are descriptive):

- **"Guessing" was the commonest label:** 769 of 1,306 (58.9%, 56.2 to 61.6).
- **The four methods shared with our tutor** (Fisherian, which is our hit-rate method, joint occurrence, base rate only and likelihood subtraction) covered 475 of 1,306 (36.4%, 33.8 to 39.0). This is a lower bound for our six methods.
- The commonest named method was Fisherian: 215 of 1,306 (16.5%).

Every task, by subject and pooled, is in the output (`analysis_1_pre_test_label_shares`).

## 2. Consistency within a person at pre-test (plan 4.2)

Denominator: students wrong on at least two of the three PPV pre-test tasks. The shuffle permutes each task's labels among the students wrong on it, within subject, 10,000 times.

| | Law | Medicine | Pooled |
|---|---|---|---|
| **Primary:** the same known-error label on every task they got wrong | 9 of 246 (3.7%, 1.7 to 6.8) | 10 of 194 (5.2%, 2.5 to 9.3) | **19 of 440 (4.3%, 2.6 to 6.7)** |
| Shuffled: mean (2.5 to 97.5%) | 0.7% (0.0 to 1.6) | 1.3% (0.0 to 3.1) | 1.0% (0.2 to 1.8) |
| Secondary: the same label of any kind, "guessing" included | 86 of 246 (35.0%) | 90 of 194 (46.4%) | 176 of 440 (40.0%, 35.4 to 44.7) |
| Sensitivity: primary with base rate only and joint occurrence as one label | 13 of 246 (5.3%) | 11 of 194 (5.7%) | 24 of 440 (5.5%, 3.5 to 8.0) |

- Among the 19 pooled students in the primary row, the shared label was Fisherian for 13, joint occurrence for 4, base rate only for 1 and likelihood subtraction for 1.
- Of the 176 in the secondary row, 157 shared "guessing".
- The plan sets no threshold and reports no p-value here.

## 3. Change over time on task d1 (plan 4.3)

**The one pre-specified test.** Among students with a known-error label on d1 at pre-test and a follow-up d1 score, the share correct on d1 at follow-up:

| | Training (groups 1 to 4) | Control (group 5) | Difference, training minus control |
|---|---|---|---|
| **Pooled** | 37 of 130 (28.5%, 20.9 to 37.0) | 4 of 27 (14.8%, 4.2 to 33.7) | **+13.6 points (Newcombe 95% interval −5.4 to +25.8); two-sided Fisher exact p = 0.227** |
| Law | 8 of 72 (11.1%) | 0 of 15 (0.0%) | +11.1 points (−10.0 to +20.4) |
| Medicine | 29 of 58 (50.0%) | 4 of 12 (33.3%) | +16.7 points (−13.6 to +39.8) |

- The interval for the pooled difference includes zero.
- **Control students who kept the same d1 label at follow-up:** pooled 6 of 27 (22.2%, 8.6 to 42.3); law 4 of 15; medicine 2 of 12.
- **No student was left out** for a missing follow-up d1 score.
- **Caution written in the plan:** on law d1, ignoring the base rate in the equal-priors way gives the correct answer, so "correct at follow-up" there includes such students. The medicine figure is the cleaner one.
- The full label tables (pre to post, pre to follow-up, and all three) are in `report_v13_tables.md`.

## 4. A collision prediction, stated before looking (plan 4.4)

On law d1 the equal-priors answer (hit rate over hit rate plus false-alarm rate, which ignores the base rate) equals the correct answer, 89.47%. No wrong method is within 1 point of the correct answer on d2 or d3 in either subject.

| | n | Correct on d1 | Correct on d2 | Correct on d3 | Gap: d1 minus mean of d2 and d3 |
|---|---|---|---|---|---|
| Law | 255 | 22 (8.6%) | 5 (2.0%) | 10 (3.9%) | +5.7 points (bootstrap 95% interval +2.7 to +9.0) |
| Medicine | 260 | 46 (17.7%) | 64 (24.6%) | 92 (35.4%) | −12.3 points (−16.5 to −8.3) |

- **Difference of gaps, law minus medicine: +18.0 points** (bootstrap 95% interval +12.9 to +23.4).
- **The prediction held:** the law gap is positive, and larger than the medicine gap.
- **The plan's expectation did not.** The plan said "a small or zero gap is the likely outcome", because a pooled re-analysis found this method in about 1% of answers.
- **Suggestive only, as the plan says.** Item difficulty can also explain a gap, and d1, d2 and d3 differ in more than the base rate.

## 5. Descriptive: pre-test label by training group (plan 4.5)

Counts by subject and pooled are in `report_v13_tables.md`. No tests.

## 6. Checks (plan section 5)

- 515 students: law 51 per group and medicine 52 per group, in each of the five groups.
- Over all tasks and time points: no score missing; no score of 1 with a label other than correct; no score of 0 labelled correct; no score without a label.
- No label outside the plan's list.
- All six PPV answer keys were reproduced from the published inputs. The law d1\* (NPV) key equals the value from ignoring the base rate; the medicine d1\* key does not.

## 7. What this does not show

- **Targeting is not tested.** No group received teaching aimed at a student's own error, so nothing here shows that targeted teaching works.
- **The labels are the authors', each from a single answer.** Their matching rule is not known to us.
- **The population is narrow:** completers only, German law and medical students, not our tutor and not our problems.
- **Base rate only and joint occurrence nearly coincide** on medicine d1 and d3, so the split between those two labels may be arbitrary there.

## 8. Deviations and the run record

- **An environment test failed, and it was not part of the plan.** Job 14417, a separate test that loaded modules and imported packages with no data, failed after 1 second with exit code 127. The most likely cause is that `sbatch --wrap` runs with `/bin/sh`, where the `module` command is not defined; this is not proven.
- **The run's dependency on that test was removed** with the team lead's approval. The job file and its SHA-256 (`3c168cea…`) were unchanged, and so was the commit (`3f3e114`).
- **Queue settings were lowered.** Before the run, the job's time limit was reduced from 30 to 10 minutes and its memory from 4 to 2 GB, so that it could start sooner. These were changes to the job record only.
- **The report was published four days after the run** (see above).

## 9. Files

| File | SHA-256 |
|---|---|
| `report_v13_output.json` (the run's output, unchanged) | `1dd6f391f3240d242af3827d0a0ef70fdf92efb2b44d655280a0110d0ae6f32f` |
| `report_v13_tables.md` (count tables, formatted from the output) | `0ed463cd6d9de618b73f34d330b0ccb5f7f87d558a6b207a530b596299eda9fb` |
| `steib2025/steib_analysis.py` (the frozen script; not published here) | `3edea828f11f74657176d29006e1f58b0aea20667eeee53a886d37e47254edbb` |
