# Plan v25: answers that fit Bayes and also fit a shortcut, in real answers

**Status:** final text, written on 20 November 2026 after two rounds of outside review (six reviews), for release as tag v25 in the public pre-registration repository. Drafts 1 to 3 were never published. Its code and tests (Appendix A and Appendix B) have been run on made-up rows only. Nothing has been run on the study file.

**What kind of analysis this is:** a pre-specified exploratory description of data we have partly examined before. Tagging it fixes every choice before its code reads the data. It is not a confirmatory test: our own October analysis of these answers first pointed at the task this plan studies, and we chose the measures knowing some of its summary output (section 3). It reports counts. It has no interval, no test and no comparison between counts.

## 1. Question

In one published study, every adult answered the same four Bayes problems. On task 504, the Bayes answer is 75%, and "100% minus the false-alarm rate" also gives 75%. An answer of 75% there cannot show how a person got it.

Among the people whose answer on task 504 matches 75%:

- how many also matched the answer that 100% − f gives on task 402 (90%), and on both task 402 and task 501 (90% and 60%)?
- how many matched the Bayes answer on both task 402 and task 502, where no other listed rule comes within 1 point of it?

The same counts are printed for everyone else, as context.

## 2. Data

- Woike, Hertwig & Gigerenzer (2023), Cognitive Psychology 143, 101564, Study 4a. Harvard Dataverse, doi:10.7910/DVN/FYMODJ, file `Study4a.xlsx`, CC0 licence.
- SHA-256 of our copy: `0376fcfb346b277f320a6ffe3a82a781c56fe9764b05d1710e29bf873ebb0811`.
- From the paper (section 5.1, read 20 November 2026):
  - 545 participants, recruited on Amazon Mechanical Turk;
  - each saw the same four number sets (tasks 402, 501, 502 and 504);
  - the assignment of number sets to story texts, and the order of tasks, were varied systematically between participants.

  The released file does not give the order or the story.
- The file is read with the unchanged `load()` function of `src/realdata_woike.py`, imported, not copied. Answers are in the 0–1 scale and are multiplied by 100 once.
- **Why Study 4a only.** It contains the task 504 coincidence, which our October analysis first noted (section 3), and other tasks on which to score the same rule.
  - In Study 4c each person answered one task.
  - In Study 4b the one candidate task is 0.1 / 99.9 / 20, with a Bayes answer of 0.5%. Our window around that value includes 0%, so it cannot tell an answer of 0% from a Bayes-window match.

  The results concern the selected Study 4a tasks. They do not estimate how common such tasks are.

## 3. What we already knew (disclosure)

We are not blind to this file. We believe we are blind to the link this plan measures.

**How the task numbers were read.** On 20 November 2026 a script read only the task ID, base rate, hit rate and false-alarm rate columns of the three Study 4 files. The answer column was not loaded.

**Our October analysis** (`src/realdata_woike.py`, commit 10e70f6, planned in the lab log before the download, run on 11 October 2026, not publicly registered). For Study 4a it printed:

- **Answers within 1 point of correct:** 102 in total, of which 78 also fit one of our six rules.
- **Answers more than 1 point from correct, per task:** 532, 514, 534 and 498 of 545, for tasks 402, 501, 502 and 504. By subtraction, 13, 31, 11 and 47 answers were within 1 point of correct.
- **Wrong answers that fit exactly one rule, over all four tasks:** hit rate 622, base rate 329, 100 − f 146, joint 66, subtraction 50, equal priors 30.
- **Wrong answers that fit one, several or none of our rules, per task:**

  | Task | One | Several | None |
  |---|---|---|---|
  | 402 | 201 of 532 | 213 of 532 | 118 of 532 |
  | 501 | 388 of 514 | 60 of 514 | 66 of 514 |
  | 502 | 252 of 534 | 160 of 534 | 122 of 534 |
  | 504 | 402 of 498 | 0 of 498 | 96 of 498 |

- **Within a person** (people with at least two wrong answers that fit a rule): one rule fitted all of them for 133 of 488 people (27.3%; 14.7% when answers were shuffled between people). Consecutive such answers, in task ID order, shared a rule in 586 of 1,149 pairs (51.0%; 36.6% shuffled).

**Do October's definitions match this plan's?** Checked on 20 November by reading the code, without the data.

- October called an answer correct if it was within 1 + 10⁻⁷ points of the file's Correct column, in floating point. That column was within 4.3 × 10⁻⁸ points of Bayes.
- This plan uses the exact fractions and the same window. The two can differ only for an answer that sits within about 10⁻⁷ points of a window's edge.
- `src/realdata_woike.py` is unchanged since commit 10e70f6, and it is the file hashed in section 9.

So we treat the October numbers below as this plan's numbers. The run prints both side by side (section 6).

**What those numbers already settle:**

- **Group sizes.** Group F (section 5) has 47 people and group N has 498. These are not results.
- **Whole-file Bayes totals.** In F and N together, 13 people match Bayes on task 402 and 11 on task 502. So N's counts follow from F's.
- **A ceiling on count 3.** At most 11 of the 47 in F can match Bayes on both, and at least 23 of the 47 match it on neither. In N, at least 474 of 498 match it on neither. A small count 3 is forced by these totals. We will not read it as evidence about how task 504 was answered.
- **An exact total.** On tasks 402, 501 and 502, 100 − f gives 90, 60 and 50. On each, the correct answer and our other five rules are more than 2 points away. So every such answer was counted in October as a wrong answer that fits only 100 − f, and (90 on 402) + (60 on 501) + (50 on 502) = 146 in the whole file. At most 73 people in the file can match both 90 on 402 and 60 on 501.
- **A ceiling on the reference answers.** 60, 70 and 80 on task 402 fit none of our six rules and are not correct. So they were all in task 402's "None" column: at most 118 in the whole file, taken together.
- **Nothing more inside F.** Apart from the ceiling on count 3, none of these limits is below 47.

**Where the idea came from. It is not independent of the answers.** Our lab log entry of 11 October 2026, written from that analysis, already says: "in 4a, 78 of 102 'correct' answers also equal a wrong strategy (task 501: base 50%, so equal priors = Bayes; task 504: 1 − FA = Bayes = 75%) — a right answer there does not show the right method." So the study and the task were first singled out in October, from the answers, together with the counts above. What was chosen later, and with what knowledge:

- **Study and task, for this plan.** On 20 November 2026 the drafting assistant picked Study 4a and task 504 from the task numbers, at 11:21 UTC, and re-read the October table at 11:24 UTC (session record). That order does not make the choice blind: the team had held the October entry for six weeks.
- **The rule, 100 − f.** It is the rule that coincides with Bayes on task 504. No other choice was available.
- **The window.** The tutor's 1-point window, used in every plan since October.
- **The measures** (S, D, the reference answers, counts within F). Written on 20 November after re-reading the October summary above, and revised after six outside reviews that saw the counts disclosed in the drafts. The October counts led us to remove an interpretation they had already ruled out, to drop a minimum group size, and to state the ceiling on count 3.

**Not computed, and to our knowledge not seen:** any table that links a task-504 answer of 75 to the same person's other answers. The October within-person counts used only wrong answers. So they included task-504 answers from people in N, but never a 75.

**Stored, but not in the October report.** The October log file (`logs/realdata_woike.json`) also stores, for each task, how many wrong answers fit only each rule. For tasks 402 and 501 that includes the number of people in the whole file who matched 90 and 60. Those two numbers cap counts 1 and 2 from above. They were not printed in the October report (`analysis/realdata_woike.md`) and have not been read for this plan. Bhavik stated on 20 November 2026 that he has never opened that log file.

**Checked for this plan:**

- **No list or histogram of answers.** Bhavik confirmed on 20 November 2026 that, to his knowledge, nobody on the team has printed or looked at a list or histogram of Study 4a answer values. The stored October outputs hold counts and shares only.
- **No public plan analysed these answers.** We searched every file in every commit of the public repository, up to tag v24-report, for the paper, the dataset and the study names. Five plans mention them, and none analyses the answers:
  - `prereg_ai_tutor_audit.md` (v14) takes five rules from the paper's Table 2;
  - `prereg_pighin_p37nz.md` reuses the 1-point tolerance "as for Woike";
  - `prereg_steib2025_secondary.md` cites the paper once;
  - `prereg_selection_policies_v1.md` and `_v2.md` describe the files' structure and state "no answers read".
- **Another idea dropped unread.** On 11 October a per-person "base-rate sensitivity" analysis of Studies 4a and 4b was judged impossible from the task numbers and task IDs alone, and was never run.

**What we have read of the paper.** The drafting assistant read pages 3 to 8 on 20 November (Table 2, Figures 5 and 6, and the start of Study 4), the sample and method paragraphs of Studies 4a to 4c, and the appendix list of studies. It has not read the Study 4 results, which report response times and self-reported strategies, and will not before the run. Bhavik stated on 20 November 2026 that he has read none of the paper himself. The October lab log cites Table 2 and the matching rule on page 6; those entries were written in AI-assisted sessions, and we have no record of what else was read then. So we cannot rule out that an earlier session saw the Study 4 results.

## 4. The four tasks

Shown as percentages, rounded to two decimals where needed. With b, h and f as proportions: Bayes = bh / (bh + (1 − b)f); joint = bh; subtraction = h − f; equal priors = h / (h + f).

| Task | Base / hit / false alarm | Bayes | Hit rate | Base rate | Joint | Subtraction | 100 − f | Equal priors |
|---|---|---|---|---|---|---|---|---|
| 402 | 20 / 30 / 10 | 42.86 | 30 | 20 | 6 | 20 | 90 | 75 |
| 501 | 50 / 80 / 40 | 66.67 | 80 | 50 | 40 | 40 | 60 | 66.67 |
| 502 | 10 / 95 / 50 | 17.43 | 95 | 10 | 9.5 | 45 | 50 | 65.52 |
| 504 | 60 / 50 / 25 | 75 | 50 | 60 | 30 | 25 | 75 | 66.67 |

- **Exact targets.** The two Bayes targets that do not terminate are scored as exact fractions: 300/7 on task 402 and 1900/109 on task 502. The table's 66.67 and 65.52 are 200/3 and 1900/29; they are not scored.
- **Task 504.** Among the listed rules, only Bayes and 100 − f are within 1 point of 75. Hit rate plus false-alarm rate is also 75; it is not a listed rule.
- **Task 501.** Equal priors gives the Bayes answer. This plan does not analyse that.
- **Tasks 402 and 502.** The nearest of our six rules is 12.86 and 7.43 points from Bayes. The nearest other listed rule is 7.14 points away on task 402 (the 50% rule) and 2.93 on task 502 (b(h + f), which gives 14.5). No other listed rule is within 1 point of Bayes on either task.

## 5. Definitions

- **Listed rules.** The 15 rules in Woike et al.'s Table 2. **Our six rules** are the six wrong rules in section 4. No other phrase is used for either set.
- **Match.** An answer x matches a target v if |x − v| ≤ w + 10⁻⁷ percentage points, inclusive, with v the exact target. The primary window is w = 1.
- **Group F.** People whose answer on task 504 matches 75.
- **Group N.** Everyone else in the file.
- **The 100 − f targets on the other tasks:** 90 on task 402 and 60 on task 501. S is the number of these two that a person matches: 0, 1 or 2.
  - 90 on task 402 matches no other listed rule.
  - 60 on task 501 does. Three other listed rules give 60 there: b(h + f), (h + f)/2 and bh + (1 − b)f. So a 60 on task 501 by itself says little.
  - Task 502 does not enter S. There, 100 − f is 50, which is also the listed "50% rule" and the stated false-alarm rate.
- **The Bayes targets on the other tasks:** 300/7 on task 402 and 1900/109 on task 502. D is the number of these two that a person matches: 0, 1 or 2.
- **Reference answers on task 402:** 60, 70 and 80. None is within 1 point of any listed rule on that task. 70 and 80 are 100 minus the hit rate and 100 minus the base rate, the same form as 100 − f. 60 is also the sum of the three numbers shown. They show how often people in F give other round numbers on that task. They are reference points for count 1 only, and they do not estimate a chance rate. Count 2 has no reference: on task 501, four listed rules give 60.
- **Same answer four times.** The largest of a person's four answers minus the smallest is at most w + 10⁻⁷.

No person can have S = 2 and D = 2, because both need a different answer on task 402. That cell is printed as "0 (impossible by definition)".

## 6. What is reported

Everything is a count with its denominator, reported whatever it shows, including zeros. At the primary window each count also has its percentage of the group, to one decimal place.

**Primary: three counts within group F** (denominator: the size of F in the run; it was 47 in October):

1. matched 90 on task 402;
2. matched 90 on task 402 and 60 on task 501 (S = 2);
3. matched Bayes on tasks 402 and 502 (D = 2).

**Reference, printed beside count 1, within group F:** the numbers who matched 60, 70 and 80 on task 402.

**Also printed:**

- the same counts for group N, as context, and for the whole file;
- for F, N and the whole file, the number matching each single target: 60 on task 501, Bayes on task 402 and Bayes on task 502;
- the S-by-D table for F and for N, with row and column totals;
- for F, N and the whole file, the number who gave the same answer four times;
- the sizes of F and N;
- for each task, how many answers are whole numbers of percent.

**If the run disagrees with section 3.** The script does not stop. It first prints the run's values next to section 3's: the sizes of F and N, the whole-file numbers matching Bayes on task 402 and on task 502, and the whole-file total of answers matching 90 on 402, 60 on 501 and 50 on 502. The report then uses the run's numbers everywhere, including section 8. The ceiling on count 3 is the smaller of the run's two whole-file Bayes numbers.

**No interval, test or comparison.** We describe the people in this file. No count gets an interval. No pair of counts, within F or between F and N, gets a test or a verbal comparison.

**One secondary check, counts only:** everything above again with w = 0.1, which is close to the rule Woike et al. used (their p. 6). F, N, S, D, the reference answers and "same answer" are all rebuilt at that width. No percentages are printed. If people typed whole numbers, no answer can match Bayes on task 402 or 502 at this width, because no whole number is within 0.1 of 42.857 or 17.431; the whole-number counts show whether that is so.

## 7. Rules

- One run. No other outcome, subgroup, task or study.
- The script prints the failed check and exits with an error, and nothing else is reported, unless:
  - the SHA-256 of the data file and of the three loader files match sections 2 and 9;
  - the loader accepts the header row, which it does only if it is exactly PersonID, TaskID, b, h, f, Correct, Estimate, in that order;
  - no row is marked excluded by the loader, and every row has exactly those seven fields;
  - TaskID takes only the values 402, 501, 502 and 504;
  - on every row, b, h and f equal the section 4 values for that task, within 10⁻⁹;
  - there are 545 people, each with exactly one row for each of the four tasks;
  - every Estimate is a finite number with 0 ≤ Estimate ≤ 1.
- Before printing, the script checks its own arithmetic: count 2 is not above count 1; each S-by-D table adds up to its group size; the impossible cell is 0; F and N add up to the whole file. If a check fails, it stops.
- From now until the tag, the only permitted read of the study file is to compute its SHA-256. Reading code and running the tests on made-up rows are allowed.
- The standard output is published unchanged.
- If a bug is found after the run, the first output stays published. We publish the bug, the fix and the corrected output beside it, marked as a deviation.

## 8. What we will and will not say (written in advance)

**The sentences we will use, with the run's numbers filled in:**

> Counting an answer as a match when it is within 1 percentage point: in Study 4a of Woike, Hertwig and Gigerenzer (2023), [size of F] of 545 adults matched 75% on a problem where Bayes' rule and "100% minus the false-alarm rate" both give 75%. On a second problem, "100% minus the false-alarm rate" gives 90%, and none of the other 14 rules listed by Woike et al. does. [count 1] of the [size of F] matched 90% there; [reference a], [reference b] and [reference c] matched 60%, 70% and 80%, which no listed rule gives there. [count 2] matched 90% there and also 60% on a third problem, where three other listed rules also give 60%. [count 3] matched the Bayes answer on both the second problem and a fourth, where no other listed rule comes within 1 point of it. At most [ceiling] could have, because [whole-file Bayes count, task 402] of all 545 adults matched it on the second problem and [whole-file Bayes count, task 502] on the fourth. These counts describe answers, not the methods behind them.

On a slide we may print only the numbers and their labels from section 6, with these sentences in the notes.

**Labels.** We use no word such as "many", "few", "most", "more", "fewer" or "only", and we state no comparison between any two counts. The numbers stand alone.

**We will not say:**

- that any person used 100 − f on task 504. Someone could use Bayes there and something else elsewhere, or 100 − f there and nowhere else. We can count answers; we cannot see methods.
- that a small count 3 shows anything. Section 3 already limits it.
- that a difference between F and N shows anything about method. Anyone who answers 100 − f on every task is in F by construction, and N mixes every other kind of answer.
- that the reference answers are a chance rate.
- anything about learning, about any tutor, or about our tutor.

**Other explanations that the design cannot rule out:**

- **Arithmetic difficulty.** Bayes on task 504 is 30/40. On tasks 402 and 502 it is 3/7 and 19/109.
- **Round numbers.** 75, 90 and 60 are round; 42.86 and 17.43 are not. The reference answers address this only in part.
- **Window width.** If people typed whole numbers, a 1-point window holds three of them around 75, 90 and 60, but only two around 42.86 (42 and 43) and 17.43 (17 and 18).
- **Other routes to the same numbers.** On task 504, hit rate plus false-alarm rate is also 75. On task 501, three other listed rules give 60.
- **Different rules on different tasks.** People can give answers that fit different rules on different tasks.
- **Story and order.** They varied between participants and are not in the file.

**Scope.** One study of 545 adults recruited online, four tasks, no feedback. The 1-point window is ours. No Study 4a task has a hit rate equal to Bayes, so this says nothing about that rule.

**Credit.** Right answers produced by a wrong rule were named "false corrects" by Tatsuoka, Birenbaum, Tatsuoka & Baillie (1980). Woike et al. (2023, p. 6) note that when rules' predictions overlapped, a matching answer was counted for each of them.

## 9. Code and tests

The full text of both files is in Appendix A and Appendix B, byte for byte.

- `v25.py`, SHA-256 `ef58b8057ca0740a4073ada9b826100a73ecba635eb3a69c29cd2c716f13d79c`. Standard library, plus the imported `load()`.
  - It reads nothing unless it is started with the flag `--run-after-tag`.
  - Each answer is the exact value of the stored number, times 100, as a fraction. Targets and windows are exact fractions.
  - The loader is imported only inside the run, after the hash checks.
  - It prints the Python, numpy and scipy versions. The loader's module imports numpy and scipy; no count uses them.
- `test_v25.py`, SHA-256 `3811cd51c40d9e2b670e0ffabc9c0218bc98cd379b6cb5eb49a809725fd34150`. 14 tests, on made-up rows only. No test imports the loader or reads the study file. They check:
  - the section 4 targets, as exact fractions;
  - every target and reference answer against all 15 listed rules, including the statements in sections 4 and 5;
  - the window at its edges, on both sides and at both widths, including 43.86 on task 402, which is within 1 point of the rounded 42.86 and not of the exact 300/7;
  - that no answer on task 402 can match both 90 and Bayes;
  - S, D, the reference answers and "same answer" on hand-built people, including four answers whose neighbours are close but whose range is too wide;
  - all counts and both tables on a made-up file of 545 people, at both widths, including people who leave F at the narrow width and an empty group;
  - each stop in section 7.
- The three files the loader depends on, by SHA-256:
  - `src/realdata_woike.py`: `4874dd3dc4dce7205584a234829809ca5550633880495ff7573b6d2c94bc4402`
  - `src/census.py`: `20712f082c7e2bc1f6c8fde6c900da2b08c9bf2d4e6f33130bc4bdf72bb6b059`
  - `src/bayes_strategies.py`: `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e`

  Importing them opens no data file (checked on 20 November).
- Before the tag, a second session that did not write the code reads `v25.py` and `test_v25.py` and runs the tests. It does not open the study file.
- The run records the tag, date, time, machine and Python version.

## 10. Who does what, and when

- Bhavik's time on this is capped at 4 hours. Kahan and Jay are not involved.
- If the code check or the tests are not passing when the cap is reached, the analysis is not run, and we say so.
- Tag and single run: by 26 November 2026. Report: by 28 November, well before the 8 December freeze.

## 11. What changed, and why

**From draft 1 to draft 2:**

1. The primary result became counts within group F. The difference between F and N was dropped, because N cannot contain anyone who answers 100 − f throughout.
2. An interpretation that our October counts already ruled out was removed.
3. The disclosure was rewritten. Draft 1 said the plan was blind to its own outcomes.
4. The target 60 on task 501 was flagged as shared with three other listed rules.
5. The bootstrap, the minimum group size and the equal-priors side analysis were dropped. Labels became literal. The loader was pinned by hash.

**From draft 2 to draft 3:**

6. **The origin of the idea is disclosed.** Our October lab log had already singled out task 504, from the answers.
7. **All intervals and the one allowed comparison are gone.** Counts 1 and 4 came from the same people and excluded each other, so separate intervals were the wrong model.
8. **The placebo was replaced.** Swapping 60 and 90 between tasks was not a matched control, because four listed rules give 60 on task 501 and none gives 90. There are now three reference answers on task 402, for count 1 only.
9. **The fixed sentence was rewritten.** It no longer says "both others", "no shortcut comes near it" or a hard-coded 47, and it states the ceiling on count 3.
10. **"Listed rules" is defined,** and every target was checked against all 15.
11. **The disclosure gained** the exact total of 146, the whole-file Bayes totals, the ceiling on the reference answers, a check that October's definitions match, and what we have read of the paper.
12. **The plan says what happens if the run disagrees with section 3,** if a bug is found, and if time runs out.
13. **The code spec was completed:** validation checks, exact arithmetic, the narrow window, empty groups.
14. **Not taken:** a formal paired test in place of the comparison, since we make no comparison; an extra comparison group; and written confirmations from Kahan and Jay, who are kept out of this to protect their blind coding.

**From draft 3 to this text:**

15. Bhavik answered the two open disclosure questions (the October log file, and the paper).
16. The code gained a flag without which it reads nothing, and a test for it.
17. The code and tests were appended.

## Appendix A: `v25.py`

```python
"""Plan v25: answers that fit Bayes and also fit a shortcut, in real answers (Woike et al. 2023, Study 4a).

A pre-specified exploratory description. One run. Counts only: no interval, no test, no comparison.
Standard library only, plus the unchanged loader `load()` imported from src/realdata_woike.py inside main().
Nothing in this file reads the study file except main(), and main() checks four SHA-256 hashes first.

    python3 v25.py --run-after-tag        # the single registered run; without the flag it reads nothing and exits
"""
import hashlib
import math
import platform
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
DATA_NAME = "Study4a.xlsx"
DATA_FILE = ROOT / "data" / "realdata" / "woike" / DATA_NAME
EXPECTED_SHA256 = {
    "data/realdata/woike/Study4a.xlsx": "0376fcfb346b277f320a6ffe3a82a781c56fe9764b05d1710e29bf873ebb0811",
    "src/realdata_woike.py": "4874dd3dc4dce7205584a234829809ca5550633880495ff7573b6d2c94bc4402",
    "src/census.py": "20712f082c7e2bc1f6c8fde6c900da2b08c9bf2d4e6f33130bc4bdf72bb6b059",
    "src/bayes_strategies.py": "4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e",
}
COLUMNS = ["PersonID", "TaskID", "b", "h", "f", "Correct", "Estimate"]
N_PEOPLE = 545
# Task numbers in percent (plan section 4): base rate, hit rate, false-alarm rate.
TASKS = {402: (20, 30, 10), 501: (50, 80, 40), 502: (10, 95, 50), 504: (60, 50, 25)}
EPS = F(1, 10 ** 7)                      # slack added to every window, in points
WINDOWS = (F(1), F(1, 10))               # primary, then the narrow secondary check
PARAM_TOL = 1e-9                         # task numbers in the file vs TASKS, as proportions
OCTOBER = {"F": 47, "N": 498, "bayes_402": 13, "bayes_502": 11, "sum_90_60_50": 146}   # plan section 3


class Stop(Exception):
    """A failed check. The run prints the message and exits non-zero."""


def bayes(task):
    b, h, f = (F(x) for x in TASKS[task])
    return 100 * b * h / (b * h + (100 - b) * f)


def comp(task):
    return F(100 - TASKS[task][2])


# Exact targets, in percentage points (plan section 5).
T_F = (504, F(75))                                   # group F: matches 75 on task 504
T_S = ((402, F(90)), (501, F(60)))                   # 100 - f on tasks 402 and 501
T_D = ((402, bayes(402)), (502, bayes(502)))         # Bayes on tasks 402 and 502: 300/7 and 1900/109
T_REF = ((402, F(60)), (402, F(70)), (402, F(80)))   # reference answers on task 402
T_CHECK_502 = (502, F(50))                           # only to reconcile the October total of 146
assert bayes(504) == comp(504) == T_F[1]
assert comp(402) == T_S[0][1] and comp(501) == T_S[1][1] and comp(502) == T_CHECK_502[1]
assert T_D[0][1] == F(300, 7) and T_D[1][1] == F(1900, 109)


def matches(x, v, w):
    """Inclusive window: |x - v| <= w + 10^-7 points, in exact arithmetic."""
    return abs(x - v) <= w + EPS


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_hashes(root=ROOT, expected=EXPECTED_SHA256):
    bad = []
    for rel, want in expected.items():
        p = Path(root) / rel
        got = sha256(p) if p.is_file() else "missing"
        if got != want:
            bad.append(f"{rel}: expected {want}, found {got}")
    if bad:
        raise Stop("hash check failed: " + "; ".join(bad))


def validate(rows):
    """Rows from load() -> {person: {task: answer in points, as an exact Fraction}}. Raises Stop on any failed check."""
    people = {}
    for i, r in enumerate(rows):
        if "excluded" in r:
            raise Stop(f"row {i}: the loader marked it excluded ({r['excluded']})")
        if sorted(r) != sorted(COLUMNS):
            raise Stop(f"row {i}: fields {sorted(r)} differ from {sorted(COLUMNS)}")
        try:
            task = int(float(str(r["TaskID"])))
        except ValueError:
            raise Stop(f"row {i}: TaskID {r['TaskID']!r} is not a number")
        if task not in TASKS or float(str(r["TaskID"])) != task:
            raise Stop(f"row {i}: TaskID {r['TaskID']!r} is not one of {sorted(TASKS)}")
        for name, want in zip(("b", "h", "f"), TASKS[task]):
            got = r[name]
            if isinstance(got, bool) or not isinstance(got, (int, float)) or not math.isfinite(got) \
                    or abs(got - want / 100) > PARAM_TOL:
                raise Stop(f"row {i}: task {task} has {name} = {got!r}, expected {want / 100}")
        est = r["Estimate"]
        if isinstance(est, bool) or not isinstance(est, (int, float)) or not math.isfinite(est) or not 0 <= est <= 1:
            raise Stop(f"row {i}: Estimate {est!r} is not a finite number between 0 and 1")
        person = str(r["PersonID"])
        if person in ("", "None"):
            raise Stop(f"row {i}: missing PersonID")
        answers = people.setdefault(person, {})
        if task in answers:
            raise Stop(f"person {person}: more than one answer on task {task}")
        answers[task] = F(est) * 100          # exact value of the stored number, times 100, once
    if len(people) != N_PEOPLE:
        raise Stop(f"{len(people)} people, expected {N_PEOPLE}")
    for person, answers in people.items():
        if sorted(answers) != sorted(TASKS):
            raise Stop(f"person {person}: answers on tasks {sorted(answers)}, expected {sorted(TASKS)}")
    return people


def describe(answers, w):
    """One person's flags at window w (plan section 5)."""
    s_hits = [matches(answers[t], v, w) for t, v in T_S]
    d_hits = [matches(answers[t], v, w) for t, v in T_D]
    xs = list(answers.values())
    return {
        "in_F": matches(answers[T_F[0]], T_F[1], w),
        "m90_402": s_hits[0], "m60_501": s_hits[1], "S": sum(s_hits),
        "bayes_402": d_hits[0], "bayes_502": d_hits[1], "D": sum(d_hits),
        "ref60_402": matches(answers[402], T_REF[0][1], w),
        "ref70_402": matches(answers[402], T_REF[1][1], w),
        "ref80_402": matches(answers[402], T_REF[2][1], w),
        "m50_502": matches(answers[T_CHECK_502[0]], T_CHECK_502[1], w),
        "same4": max(xs) - min(xs) <= w + EPS,
    }


FLAGS = ("m90_402", "m60_501", "bayes_402", "bayes_502", "ref60_402", "ref70_402", "ref80_402", "m50_502", "same4")


def summarise(members):
    """Counts for one group (a list of describe() dicts)."""
    out = {"n": len(members)}
    for k in FLAGS:
        out[k] = sum(m[k] for m in members)
    out["S2"] = sum(m["S"] == 2 for m in members)
    out["D2"] = sum(m["D"] == 2 for m in members)
    out["table"] = {(s, d): sum(m["S"] == s and m["D"] == d for m in members) for s in range(3) for d in range(3)}
    return out


def analyse(people, w):
    flags = [describe(a, w) for a in people.values()]
    res = {"F": summarise([m for m in flags if m["in_F"]]),
           "N": summarise([m for m in flags if not m["in_F"]]),
           "ALL": summarise(flags)}
    for g in ("F", "N", "ALL"):
        c = res[g]
        if c["S2"] > c["m90_402"] or c["S2"] > c["m60_501"] or c["D2"] > min(c["bayes_402"], c["bayes_502"]):
            raise Stop(f"internal check failed: joint count exceeds a single count in group {g}")
        if sum(c["table"].values()) != c["n"]:
            raise Stop(f"internal check failed: S-by-D table does not add up to the group size in group {g}")
        if c["table"][(2, 2)] != 0:
            raise Stop(f"internal check failed: the impossible cell is not zero in group {g}")
        if c["m90_402"] + c["bayes_402"] + c["ref60_402"] + c["ref70_402"] + c["ref80_402"] > c["n"]:
            raise Stop(f"internal check failed: exclusive task-402 answers exceed the group size in group {g}")
    for k in FLAGS + ("S2", "D2"):
        if res["F"][k] + res["N"][k] != res["ALL"][k]:
            raise Stop(f"internal check failed: F and N do not add up to the whole file for {k}")
    if res["F"]["n"] + res["N"]["n"] != N_PEOPLE:
        raise Stop("internal check failed: F and N do not add up to 545")
    return res


def whole_numbers(people):
    """Per task: how many answers are whole numbers of percent (within 10^-7 points)."""
    return {t: sum(abs(a[t] - round(a[t])) <= EPS for a in people.values()) for t in sorted(TASKS)}


def cell(k, n, pct):
    if not pct:
        return f"{k} of {n}"
    return f"{k} of {n} ({100 * k / n:.1f}%)" if n else f"{k} of {n} (no percentage: empty group)"


LABELS = (
    ("m90_402", "count 1: matched 90 on task 402"),
    ("S2", "count 2: matched 90 on task 402 and 60 on task 501 (S = 2)"),
    ("D2", "count 3: matched Bayes on tasks 402 and 502 (D = 2)"),
    ("ref60_402", "reference a: matched 60 on task 402"),
    ("ref70_402", "reference b: matched 70 on task 402"),
    ("ref80_402", "reference c: matched 80 on task 402"),
    ("m60_501", "single target: matched 60 on task 501"),
    ("bayes_402", "single target: matched Bayes (300/7) on task 402"),
    ("bayes_502", "single target: matched Bayes (1900/109) on task 502"),
    ("same4", "gave the same answer four times"),
)


def render_window(res, w, pct):
    L = [f"== window {float(w)} + 10^-7 points" + (" (primary)" if pct else " (secondary check: counts only)")]
    L.append(f"   group sizes: F {res['F']['n']} of {N_PEOPLE}; N {res['N']['n']} of {N_PEOPLE}")
    for g, name in (("F", "group F (matched 75 on task 504)"), ("N", "group N (everyone else; context only)"),
                    ("ALL", "whole file (F and N together)")):
        c = res[g]
        L.append(f"   {name}:")
        for k, label in LABELS:
            L.append(f"      {label}: {cell(c[k], c['n'], pct)}")
        if g != "ALL":
            L.append("      S-by-D table, rows S = 0, 1, 2; columns D = 0, 1, 2; then row totals:")
            for s in range(3):
                row = [c["table"][(s, d)] for d in range(3)]
                shown = [str(x) for x in row]
                if s == 2:
                    shown[2] = "0 (impossible by definition)"
                L.append(f"         S = {s}: " + " | ".join(shown) + f" | total {sum(row)}")
            L.append("         column totals: " + " | ".join(str(sum(c["table"][(s, d)] for s in range(3)))
                                                               for d in range(3)) + f" | total {c['n']}")
    return L


def render(people):
    L = []
    primary = analyse(people, WINDOWS[0])
    a = primary["ALL"]
    run = {"F": primary["F"]["n"], "N": primary["N"]["n"], "bayes_402": a["bayes_402"], "bayes_502": a["bayes_502"],
           "sum_90_60_50": a["m90_402"] + a["m60_501"] + a["m50_502"]}
    L.append("== comparison with plan section 3 (October values), primary window; the run's values are used throughout")
    for k, label in (("F", "size of F"), ("N", "size of N"), ("bayes_402", "whole file, matched Bayes on task 402"),
                     ("bayes_502", "whole file, matched Bayes on task 502"),
                     ("sum_90_60_50", "whole file, matched 90 on 402 + 60 on 501 + 50 on 502")):
        L.append(f"   {label}: run {run[k]}; section 3 {OCTOBER[k]}; " + ("AGREES" if run[k] == OCTOBER[k] else "DIFFERS"))
    L.append(f"   ceiling on count 3 (the smaller whole-file Bayes count): {min(run['bayes_402'], run['bayes_502'])}")
    L += render_window(primary, WINDOWS[0], True)
    L += render_window(analyse(people, WINDOWS[1]), WINDOWS[1], False)
    wn = whole_numbers(people)
    L.append("== answers that are whole numbers of percent (within 10^-7 points), per task: "
             + "; ".join(f"task {t}: {wn[t]} of {N_PEOPLE}" for t in sorted(wn)))
    L.append("Counts describe answers, not the methods behind them. One study, four tasks, no feedback. "
             "No interval, test or comparison is computed.")
    return L


RUN_FLAG = "--run-after-tag"


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv != [RUN_FLAG]:
        print(f"Nothing was read. The single registered run is: python3 v25.py {RUN_FLAG} (only after the plan is tagged).")
        return 2
    try:
        check_hashes()
        sys.path.insert(0, str(SRC))
        from realdata_woike import COLUMNS as LOADER_COLUMNS, load   # the loader stops by itself on a wrong header row
        if LOADER_COLUMNS != COLUMNS:
            raise Stop(f"the loader's column list {LOADER_COLUMNS} differs from {COLUMNS}")
        people = validate(load(DATA_NAME))
        lines = render(people)
    except Stop as e:
        print(f"STOP: {e}")
        return 1
    print("# v25 inputs verified: " + "; ".join(f"{k} {v}" for k, v in EXPECTED_SHA256.items()))
    print("\n".join(lines))
    import numpy
    import scipy
    print(f"# environment: python {platform.python_version()}; numpy {numpy.__version__}; scipy {scipy.__version__} "
          "(numpy and scipy are imported by the loader's module and are not used in any count)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Appendix B: `test_v25.py`

```python
"""Tests for v25.py. Made-up rows only: no test reads the study file or imports the loader.

    python3 exploratory/v25/test_v25.py
"""
import hashlib
import sys
import tempfile
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import v25  # noqa: E402
from v25 import (EPS, N_PEOPLE, TASKS, WINDOWS, Stop, analyse, bayes, check_hashes, comp, describe, matches,  # noqa: E402
                 render, validate, whole_numbers)

W1, W01 = WINDOWS


def rows_for(people):
    """people: list of {task: answer as a proportion}. -> rows shaped like the loader's output."""
    out = []
    for i, answers in enumerate(people):
        for task, est in answers.items():
            b, h, f = (x / 100 for x in TASKS[task])
            out.append({"PersonID": str(1000 + i), "TaskID": str(task), "b": b, "h": h, "f": f,
                        "Correct": float(bayes(task) / 100), "Estimate": est})
    return out


def person(a402, a501, a502, a504):
    return {402: a402, 501: a501, 502: a502, 504: a504}


SHORTCUT = person(0.90, 0.60, 0.50, 0.75)          # 100 - f on every task
BAYESIAN = person(0.4286, 0.6667, 0.1743, 0.75)    # Bayes on every task, typed to two decimals
SAME75 = person(0.75, 0.75, 0.75, 0.75)            # the same answer four times
FIFTY = person(0.50, 0.50, 0.50, 0.50)             # 50 everywhere: group N
NEAR75 = person(0.10, 0.10, 0.10, 0.755)           # in F at 1 point, not at 0.1
REF60 = person(0.60, 0.90, 0.20, 0.75)             # reference answer 60 on task 402
REF70 = person(0.70, 0.30, 0.20, 0.30)
REF80 = person(0.80, 0.30, 0.20, 0.30)


def made_up_file():
    people = [SHORTCUT] * 10 + [BAYESIAN] * 5 + [SAME75] * 3 + [NEAR75] * 2 + [REF60] * 4 + [REF70] * 6 + [REF80] * 7
    return people + [FIFTY] * (N_PEOPLE - len(people))


# ---------------------------------------------------------------- targets (plan section 4)
def test_targets_are_exact_fractions():
    assert bayes(402) == F(300, 7) and bayes(501) == F(200, 3) and bayes(502) == F(1900, 109) and bayes(504) == 75
    assert [comp(t) for t in (402, 501, 502, 504)] == [90, 60, 50, 75]
    assert v25.T_F == (504, F(75))
    assert v25.T_S == ((402, F(90)), (501, F(60)))
    assert v25.T_D == ((402, F(300, 7)), (502, F(1900, 109)))
    assert v25.T_REF == ((402, F(60)), (402, F(70)), (402, F(80)))


def listed_rules(task):
    """The 15 rules of Woike et al. (2023), Table 2, in percentage points."""
    b, h, f = (F(x, 100) for x in TASKS[task])
    r = {"h": h, "b": b, "1-f": 1 - f, "h-f": h - f, "b*h": b * h, "0.5": F(1, 2), "b*(h+f)": b * (h + f),
         "Bayes": b * h / (b * h + (1 - b) * f), "f": f, "(h+f)/2": (h + f) / 2, "0.5*b": b / 2,
         "b*h/((1-b)*f)": b * h / ((1 - b) * f), "h/(h+f)": h / (h + f), "b*h+(1-b)*f": b * h + (1 - b) * f, "h-b": h - b}
    assert len(r) == 15
    return {k: 100 * x for k, x in r.items()}


def within1(task, target):
    return sorted(k for k, x in listed_rules(task).items() if abs(x - target) <= 1)


def test_targets_against_all_fifteen_listed_rules():
    assert within1(504, 75) == ["1-f", "Bayes"]                       # group F's answer
    assert within1(402, 90) == ["1-f"]                                # count 1's target is clean
    assert within1(501, 60) == sorted(["1-f", "b*(h+f)", "(h+f)/2", "b*h+(1-b)*f"])   # count 2's second target is not
    for ref in (60, 70, 80):
        assert within1(402, ref) == []                                # reference answers fit no listed rule
    assert within1(402, bayes(402)) == ["Bayes"] and within1(502, bayes(502)) == ["Bayes"]
    near402 = min(abs(x - bayes(402)) for k, x in listed_rules(402).items() if k != "Bayes")
    near502 = min(abs(x - bayes(502)) for k, x in listed_rules(502).items() if k != "Bayes")
    assert near402 == F(50) - F(300, 7) and round(float(near402), 2) == 7.14      # the 50% rule
    assert near502 == F(1900, 109) - F(145, 10) and round(float(near502), 2) == 2.93   # b*(h+f)
    assert 20 + 30 + 10 == 60 and 100 - 30 == 70 and 100 - 20 == 80   # what the reference answers also are


# ---------------------------------------------------------------- the window
def test_window_edges_both_signs_both_widths():
    for w in (W1, W01):
        for v in (F(75), F(300, 7)):
            assert matches(v + w, v, w) and matches(v - w, v, w)                  # exactly at the edge: inclusive
            assert matches(v + w + EPS, v, w) and matches(v - w - EPS, v, w)      # the 10^-7 slack is inclusive too
            assert not matches(v + w + 2 * EPS, v, w) and not matches(v - w - 2 * EPS, v, w)
    assert not matches(F(4386, 100), F(300, 7), W1)        # 43.86 is 1.0029 from the exact 300/7: no match
    assert matches(F(4386, 100), F(4286, 100), W1)         # though it is 1.00 from the rounded 42.86
    assert matches(F(0.76) * 100, F(75), W1) and matches(F(0.74) * 100, F(75), W1)   # stored binary values
    assert matches(F(0.9) * 100, F(90), W01) and not matches(F(0.89) * 100, F(90), W01)


def test_s2_and_d2_cannot_both_hold():
    for w in (W1, W01):
        for k in range(0, 10001):                                 # every answer on task 402 from 0 to 100 in steps of 0.01
            x = F(k, 100)
            assert not (matches(x, F(90), w) and matches(x, F(300, 7), w))


# ---------------------------------------------------------------- one person
def pts(p):
    return {t: F(a) * 100 for t, a in p.items()}


def test_describe_hand_built_people():
    d = describe(pts(SHORTCUT), W1)
    assert d["in_F"] and d["S"] == 2 and d["D"] == 0 and d["m50_502"] and not d["same4"]
    d = describe(pts(BAYESIAN), W1)
    assert d["in_F"] and d["S"] == 0 and d["D"] == 2 and d["bayes_402"] and d["bayes_502"]
    d = describe(pts(BAYESIAN), W01)
    assert d["in_F"] and d["D"] == 2                              # two-decimal Bayes answers still match at 0.1
    d = describe(pts(SAME75), W1)
    assert d["in_F"] and d["same4"] and d["S"] == 0 and d["D"] == 0 and not d["ref60_402"]
    d = describe(pts(FIFTY), W1)
    assert not d["in_F"] and d["same4"] and d["m50_502"] and d["S"] == 0
    assert describe(pts(NEAR75), W1)["in_F"] and not describe(pts(NEAR75), W01)["in_F"]
    assert describe(pts(REF60), W1)["ref60_402"] and describe(pts(REF70), W1)["ref70_402"]
    assert describe(pts(REF80), W1)["ref80_402"] and not describe(pts(REF80), W1)["ref70_402"]
    assert describe(pts(person(0.43, 0.3, 0.17, 0.3)), W1)["D"] == 2      # whole numbers 43 and 17 match at 1 point
    assert describe(pts(person(0.43, 0.3, 0.17, 0.3)), W01)["D"] == 0     # and cannot match at 0.1


def test_same_answer_uses_the_full_range():
    chain = person(0.74, 0.75, 0.76, 0.77)                         # neighbours 1 apart, range 3
    assert not describe(pts(chain), W1)["same4"]
    tight = person(0.75, 0.755, 0.76, 0.752)                       # range exactly 1
    assert describe(pts(tight), W1)["same4"] and not describe(pts(tight), W01)["same4"]


# ---------------------------------------------------------------- a whole made-up file
def test_analyse_counts_on_a_made_up_file():
    people = validate(rows_for(made_up_file()))
    r = analyse(people, W1)
    f, n, a = r["F"], r["N"], r["ALL"]
    assert f["n"] == 10 + 5 + 3 + 2 + 4 and n["n"] == N_PEOPLE - f["n"] and a["n"] == N_PEOPLE
    assert f["m90_402"] == 10 and f["S2"] == 10 and f["D2"] == 5 and f["m60_501"] == 10
    assert f["ref60_402"] == 4 and f["ref70_402"] == 0 and f["ref80_402"] == 0 and f["same4"] == 3
    assert n["ref70_402"] == 6 and n["ref80_402"] == 7 and n["m90_402"] == 0 and n["same4"] == N_PEOPLE - 37
    assert a["bayes_402"] == 5 and a["bayes_502"] == 5 and a["m50_502"] == 10 + (N_PEOPLE - 37)
    assert f["table"][(2, 0)] == 10 and f["table"][(0, 2)] == 5 and f["table"][(0, 0)] == 9 and f["table"][(2, 2)] == 0
    assert sum(f["table"].values()) == f["n"] and sum(n["table"].values()) == n["n"]
    narrow = analyse(people, W01)
    assert narrow["F"]["n"] == f["n"] - 2                          # the two 75.5 answers leave F at 0.1
    assert narrow["F"]["D2"] == 5 and narrow["F"]["S2"] == 10


def test_render_runs_and_reports_the_run_not_october():
    people = validate(rows_for(made_up_file()))
    text = "\n".join(render(people))
    assert "size of F: run 24; section 3 47; DIFFERS" in text
    assert "ceiling on count 3 (the smaller whole-file Bayes count): 5" in text
    assert "count 1: matched 90 on task 402: 10 of 24 (41.7%)" in text
    assert "count 2: matched 90 on task 402 and 60 on task 501 (S = 2): 10 of 24 (41.7%)" in text
    assert "0 (impossible by definition)" in text
    assert "(secondary check: counts only)" in text and "count 1: matched 90 on task 402: 10 of 22\n" in text
    assert "task 504: 543 of 545" in text                          # two answers of 75.5 are not whole numbers
    for banned in ("interval", "p-value", "significant", "more often"):
        assert banned not in text.replace("No interval, test or comparison is computed.", "")


def test_empty_group_prints_without_a_percentage():
    people = validate(rows_for([NEAR75] * 3 + [FIFTY] * (N_PEOPLE - 3)))
    assert analyse(people, W01)["F"]["n"] == 0
    text = "\n".join(render(people))
    assert "count 1: matched 90 on task 402: 0 of 0\n" in text     # narrow window: counts only, no division
    assert v25.cell(0, 0, True) == "0 of 0 (no percentage: empty group)"


def test_whole_numbers():
    people = validate(rows_for([BAYESIAN] * 5 + [FIFTY] * (N_PEOPLE - 5)))
    assert whole_numbers(people) == {402: N_PEOPLE - 5, 501: N_PEOPLE - 5, 502: N_PEOPLE - 5, 504: N_PEOPLE}


# ---------------------------------------------------------------- every stop
def stops(rows, fragment):
    try:
        validate(rows)
    except Stop as e:
        assert fragment in str(e), str(e)
        return True
    raise AssertionError(f"validate() did not stop; expected: {fragment}")


def test_validate_stops():
    good = rows_for(made_up_file())
    assert len(validate(good)) == N_PEOPLE
    assert stops(good[:-4], "people, expected 545")
    assert stops(good[:-1], "answers on tasks")
    assert stops(good + [dict(good[0])], "more than one answer")
    for bad, fragment in ((1.2, "between 0 and 1"), (-0.01, "between 0 and 1"), (float("nan"), "finite"),
                          (float("inf"), "finite"), (True, "finite"), ("0.5", "finite"), (None, "finite")):
        assert stops([dict(good[0], Estimate=bad)] + good[1:], fragment)
    assert stops([dict(good[0], TaskID="601")] + good[1:], "not one of")
    assert stops([dict(good[0], TaskID="402.5")] + good[1:], "not one of")
    assert stops([dict(good[0], TaskID="abc")] + good[1:], "not a number")
    assert stops([dict(good[0], b=0.25)] + good[1:], "expected")
    assert stops([dict(good[0], extra=1)] + good[1:], "fields")
    assert stops([dict(good[0], excluded="missing value")] + good[1:], "excluded")
    assert stops([dict(good[0], PersonID="")] + good[1:], "missing PersonID")
    assert len(validate([dict(r, TaskID=r["TaskID"] + ".0") for r in good])) == N_PEOPLE    # "402.0" is task 402
    assert len(validate([dict(good[0], Estimate=0), dict(good[1], Estimate=1)] + good[2:])) == N_PEOPLE   # 0 and 1 allowed


def test_hash_check_stops_on_any_difference():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "a.txt"
        p.write_bytes(b"made-up bytes")
        good = hashlib.sha256(b"made-up bytes").hexdigest()
        check_hashes(d, {"a.txt": good})
        for expected in ({"a.txt": "0" * 64}, {"missing.txt": good}):
            try:
                check_hashes(d, expected)
            except Stop as e:
                assert "hash check failed" in str(e)
            else:
                raise AssertionError("check_hashes() did not stop")


def test_main_without_the_flag_reads_nothing():
    for argv in ([], ["--run"], ["--run-after-tag", "extra"]):
        assert v25.main(argv) == 2
    assert "realdata_woike" not in sys.modules


def test_importing_v25_reads_nothing():
    assert "realdata_woike" not in sys.modules and "numpy" not in sys.modules and "scipy" not in sys.modules
    assert sorted(v25.EXPECTED_SHA256) == ["data/realdata/woike/Study4a.xlsx", "src/bayes_strategies.py",
                                           "src/census.py", "src/realdata_woike.py"]
    assert v25.OCTOBER == {"F": 47, "N": 498, "bayes_402": 13, "bayes_502": 11, "sum_90_60_50": 146}


if __name__ == "__main__":
    tests = [(k, f) for k, f in sorted(globals().items()) if k.startswith("test_") and callable(f)]
    for name, fn in tests:
        fn()
        print("ok", name)
    print(f"{len(tests)} tests passed")
```
