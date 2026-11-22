# Plan v37 (22 November 2026): same answer, was there a recorded hover on the base rate? Reani et al. (2019) hover data

Status: this text is to be published under tag v37, before the analysis in section 5 is run. It is a plan for the
**counts of hover classes within answer groups, which nobody has yet seen**. It is not a plan made before any look
at the data: three looks at the real files came first, and section 7 lists them and what they already settle. An
earlier text was reviewed twice on 22 November by two outside AI systems, which were told not to open the data;
this version answers their findings. Forecasts are published as addendum v37.1 before the run.

## 1. Question

Our tutor sees only answers. Two people who give the same wrong number may differ in a way an answer cannot show.
**In a study where every number sat behind a hover button, among people with an answer of 49 to 51, how many had
no recorded hover on a base-rate button, and how many had at least one?**

## 2. Data

- Reani, Davies, Peek & Jay (2019), "Evidencing How Experience and Problem Format Affect Probabilistic Reasoning
  Through Interaction Analysis", Frontiers in Psychology 10:1548. Adults recruited on Amazon Mechanical Turk.
- **Checked against the paper's PDF on 22 November** by an AI assistant (the points below are paraphrased):
  - Study 2 kept 186 participants (section 2.3). Table 1 gives the probability-format group as 32 men and 62
    women, which is 94. The paper does not print "94".
  - Its stated exclusions (section 2.3): people who left an ad-blocker on; people who answered without looking
    at the question; and people who hovered over fewer than two pieces of information other than the question.
  - Its scoring (section 3): an answer is correct if it matches the true value rounded up or down to a whole
    percentage point. The paper gives 0.17 as the true value.
  - It says nothing about which devices were allowed.
- Task: a fire-and-alarm problem drawn as a tree. Each number is hidden under a button and shows only while the
  mouse is over it. In Study 2, probability format, the numbers are the same for everyone: base rate 10%, alarm
  given fire 50%, alarm given no fire 27%. The correct answer is 100 × (0.05 / 0.293) = 5000/293 = 17.06
  percentage points.
- **50% is printed on two buttons:** alarm given fire (the hit rate) and no alarm given fire (the miss rate). It
  is also a 50–50 guess. Only 50 is printed; 49 and 51 are not. Nothing in this plan can tell these cases apart,
  so the plan speaks of "an answer of 49 to 51" and "a 50% button", never of "the hit-rate answer".
- **Primary sample:** the authors' final analysis set for Study 2, probability format.
- **Two wider samples** are reported beside it. The authors' scripts drop people with short hover records (section
  4), and such people are part of this plan's question. The wider samples also differ from the primary one in
  how a hover is measured, so a difference between samples cannot be put down to the exclusions alone.
- **Source and handling.** The repository, github.com/manurea/mouse-interaction-bayesian-reasoning, is public and
  carries **no licence**. Bhavik emailed the authors on 21 November 2026. This plan does not rely on a reply and
  claims no permission from the authors.
  - The files stay on one team member's computer, in a folder git ignores. No file, row, answer or person-level
    value is copied, shared or published by us.
  - We report aggregates only. Here that means the cell counts of section 5, and the shares and intervals
    computed from them.
  - If the authors object at any time, the results are removed from our talk and materials, and a withdrawal
    note is published in this repository.

## 3. Definitions, fixed now

- **A hover** is one recorded hover on a button. At the primary threshold any recorded hover counts, whatever its
  duration. Sensitivity rows count a hover only if its duration is unknown or at least 250 ms, and unknown or at
  least 500 ms. A duration that is missing or unreadable is "unknown". Durations are compared exactly.
- **Base-rate buttons:** F ("Fire", 10%) and nF ("No fire", 90%). **50% buttons:** FA ("Alarm" under fire) and
  FnA ("No alarm" under fire).
- **Answer groups,** in exact arithmetic with the limits included:
  - *near 50*: the answer is from 49 to 51;
  - *near correct*: the answer is within 1 point of 5000/293, so 17 and 18 count and 16 does not. This matches
    the paper's own scoring rule;
  - *other*: everything else.
- **Hover classes.** Each person is in exactly one:
  - NEITHER: no counted hover on a 50% button and none on a base-rate button;
  - BASE_ONLY: a base-rate button, no 50% button;
  - FIFTY_ONLY: a 50% button, no base-rate button;
  - BOTH: a 50% button and a base-rate button.
- **No base-rate hover** = NEITHER + FIFTY_ONLY.
- **Eligible person:** someone with a readable answer and a hover log. A person with a readable answer and no
  hover log is counted and left out. A person with a hover log and no counted hover on those four buttons is
  classed NEITHER.
- **A readable number:** after removing spaces around it, an optional sign, digits with an optional decimal
  point, and an optional exponent of at most three digits (the forms R and JavaScript write), in at most 60
  characters. Only the characters 0 to 9 count as digits. Nothing else: no "%", no fraction, no words, no longer
  exponent, no digit from another script. Empty, NA, NaN, nan, null, NULL and None mean missing. Anything else is
  unreadable; the person or row is counted and left out.

## 4. Files, columns and samples

Repository commit bc8d0689a76b97664251a9a65ff080d47049ad8c. Column names and codes come from the stage 0
structure printout and from the authors' R scripts.

**Which number each button shows** (from the study page's own HTML, which the log stores as page text):

| Page node | Authors' letter | Our name | Shows |
|---|---|---|---|
| 1 | A | T | 100% (total) |
| 2 | B | F | 10%, "Fire" (base rate) |
| 3 | C | nF | 90%, "No fire" |
| 4 | D | FA | 50%, "Alarm" under fire |
| 5 | E | FnA | 50%, "No alarm" under fire |
| 6 | F | nFA | 27%, "Alarm" under no fire |
| 7 | G | nFnA | 73%, "No alarm" under no fire |
| question | H | Q | the question text |

The letters are assigned node by node in `cleanAITORdata.R:66-83`.

**Sample 1, primary: the authors' final analysis set.**
- People: rows of `scanDF2.csv` with `Wave` = 2 and `numerical_format` = "probability" (column `Ps`). A repeated
  `Ps` stops the run.
- Answer: `answer1` for the same `Ps` in `analysis_scanpath.csv`. It is a percentage: the authors divide it by 100
  (`FIRE_analysis.R:72-74`). `scanDF2.csv`'s own `Given_answer` is not used, because the authors overwrite it for
  people they scored correct (`FIRE_analysis.R:89-90`).
- Hover log: rows of `analysis_duration.csv` with `sid` = `Ps`, `wave` = 2, `n_format` = "prob", `event` =
  "mouseover" and `node.id` A–H; `duration` in milliseconds. A person with at least one such row has a hover log.
  Rows with any other `node.id` are counted and not used.
- That file is the authors' own cleaning of the mouse log (`cleanAITORdata.R`). As we read their script: only
  mouseover and mouseout events are kept; an event on the background is treated as leaving the button before
  it; repeated background rows are dropped; a hover's duration is the time to the next kept event. We found no
  rule for touch devices in it. We did not check this script against the data.
- The authors' exclusions, as their scripts apply them: duplicate submissions; a hard-coded list of people
  described as answering "with a thoughtless pattern", with no written criterion; anyone who took part more than
  once; hover records of two areas or fewer; anyone who never opened the question; anyone who visited fewer than
  three areas.

**Sample 2: the authors' cleaned set before their last rule.** The same, for every Study 2 probability person in
`analysis_scanpath.csv`. It includes the people the last rule drops (never opened the question, or fewer than
three areas).

**Sample 3: the raw mouse log, with none of the authors' exclusions.** File `w2_prob_aitor.csv`, one row per
browser event. It is not "everyone": a person enters only with a readable first answer.
- Person: `sid`. Rows with no readable `timestampms` are counted and dropped.
- Answer: the person's **first** event whose `formInputs/ans1` is not missing. If that value is unreadable, the
  person is counted and left out; a later answer does not rescue them. People with no such event are counted and
  left out. Later answer events are only counted.
- Hover log: every person with a readable first answer has one, even if it holds nothing but that answer event.
- Window: the person's events in order of time, then file order, up to and including that answer event. Nothing
  after it is used.
- Hover on node K: it starts at a `mouseover` on `study-button-nodeK` or `study-node-K`. It ends at the first of:
  1. a `mouseout` on node K, unless a `mouseover` on node K follows within 50 ms. In that case the hover
     continues, and the events between the two are ignored. The 50 ms allow for the step from the button to
     the number shown beside it;
  2. a `mouseover` on anything that is not node K;
  3. the answer event.

  A `mouseout` on anything else is ignored. A hover on the question is not counted.
- This rule is ours, not the authors'. The 50 ms is our choice and was fixed without looking at any timing.
- Reported twice: all eligible people, and without people who have a touch event (`mobileTouchStart`,
  `mobileTouchEnd`) in their window, because a touch screen may not log a hover.
- No join to the answer file is made. The authors join the two files by matching timestamps within 1.5 seconds.

**Stops.** The run stops, printing no count, if a sample has no readable answer, if nobody with an answer has a
hover log, or if no `answer1` value is above 1 (the column would then not be a percentage).

**Dropped from this plan:** the Study 2 frequency-format table. Stage 0 did not establish that page's numbers and
buttons, so no group can be defined for it in advance.

## 5. What is reported

**Primary result, one number with its table row.** In sample 1, at the "any recorded hover" threshold, among
eligible people with an answer near 50: the count K with no base-rate hover, out of N, with a marginal exact
(Clopper–Pearson) 95% interval. The four class counts of that row are printed beside it. The printout marks this
one row "PRIMARY".

**Secondary, all printed by the same run and all reported, whatever their direction:**
- the same row for the near-correct and other groups;
- all of it at the 250 ms and 500 ms thresholds;
- all of it for sample 2, for sample 3, and for sample 3 without people who have touch events.

**Which table governs.** The claim we make rests on the primary row alone. Every other row is a sensitivity
check. If the samples or thresholds disagree, we say so and quote them beside the primary row; we do not replace
it.

**The intervals.** Each is a marginal interval for one share. It is a model-based summary: it treats the N people
as a binomial sample of people like them, although this sample was selected by the authors' rules. It does not
cover several shares at once. The counts themselves are exact. A row with no eligible person prints no interval.

**What the report holds.** Cell counts, and one share and one interval per row. It also holds, for each sample,
how many people and rows were dropped at each step. It holds no answer value, no duration, no row and no person
identifier, and no count is crossed with a person-level field such as an ID, a code, age or gender.

**Small cells and differences between tables.** The person-level files are already public in the authors'
repository. Our tables are computed from those files and show nothing that is not already there. So we apply no
cell suppression, and we publish all tables even though subtracting one from another can isolate a few people.
We make no claim about how well the authors' data are anonymised.

**Forecasts, written before the run.** The forecasters are the team's two other members, Kahan and Jay. They get
the sheet in Appendix A and nothing else, and they write on it what they have already seen. The sheet is an
informed forecast: it tells them the problem, the sample and our rules. Bhavik and the AI assistant that wrote
this plan have seen the checks in section 7 and do not forecast. The forecasts, with names, dates and those
statements, are published as addendum v37.1. **The run does not start until that addendum is published.**

**Allowed sentence** (filled from the primary row only): "In Reani et al.'s Study 2 (percentage format; the
authors' final sample and their cleaned hover file; any recorded hover), N people with a hover log gave an answer
from 49% to 51%. K of them (X%, 95% interval lo to hi) had no recorded hover on either base-rate button (NEITHER
a, FIFTY_ONLY b). The other N − K had at least one (BASE_ONLY c, BOTH d). A recorded hover is a logged mouse
event: it does not show that a number was read or used, and a missing one does not show why." It may be followed
by: "50% is printed on two buttons, alarm given fire and no alarm given fire, and is also a 50–50 guess."

## 6. Limits written now

- Looking was not assigned at random. The counts describe these people. They do not show that pointing at the base
  rate changes answers.
- Any of the classes may turn out to be empty.
- The classes record logged mouse events. They cannot show that a number was displayed, read, copied or guessed,
  or why an event is absent.
- An answer of 50 may be the hit rate, the miss rate or a guess. The classes cannot tell which.
- The primary sample leaves out people with short hover records, by the authors' rules, and keeps touch devices.
  Its hover file is the authors' processing, which we have read but not checked.
- Sample 3's hover rule and answer field are our reading of a raw browser log, tested on made-up files only.
  Sample 3 mixes all devices and includes people the authors judged unreliable.
- A tree with hidden numbers is not an ordinary word problem.
- One study, 94 people in the primary sample, Mechanical Turk adults in 2019. Nothing here is about learning.

## 7. What was seen before publication, and what it already settles

**Our rule is that no analysis is run before its plan is published. For the facts in this section that rule was
broken.** Three looks were taken at the real files to write section 4, and they produced real findings. Listing
them does not make those findings prospective. The scripts and outputs are in Appendices G to L.

1. **Stage 0 structure check** (22 November; an AI session on Bhavik's Mac, running the script in Appendix K).
   For each of the 29 CSV files it printed: the file name and size; each column's name, type and number of
   distinct values; the list of values of any text column with at most 30 distinct values, unless the column name
   looked like an answer, a score or an ID; and how many values ID-like columns share between files.
   - By mistake it also printed the study page's text (`node/textContent`, `selectedContent`: question wording,
     button labels, HTML), the key names in the log's `key` column, and the values of a selection `offset`
     column. Section 4's button table comes from that page text.
   - The script now hides those columns (Appendix J). The printout was regenerated and the original printout was
     overwritten; it is not kept. Appendix L is the regenerated printout for the five Study 2 probability files.
   - What it shows about answers: the number of distinct values in answer columns, for example 31 distinct
     `answer1` values among the 172 rows of `w2_prob_alan.csv`, and 30 distinct `formInputs/ans1` values in the
     raw log. No answer value was printed.
   - Who saw the original printout: the AI session that made it, and the AI assistant that wrote this plan (parts
     of it). Whether Bhavik opened it is UNVERIFIED. The regenerated one: the same AI assistant.
2. **A second structure check** (22 November; the AI assistant that wrote this plan; Appendix G). Its whole output,
   with each measure as that script defined it, anywhere in the log:
   - 172 people (`sid`) in the raw log;
   - only `submit` events carry a non-empty `formInputs/ans1`, on 148 rows; 148 people have such a row, and all
     148 have exactly one;
   - 149 people have a `submit` event (with or without an answer);
   - 157 people have a mouseover on a number node; 138 have that and a `submit` event;
   - 11 people have an answer field and no mouseover on a number node; 20 have such a mouseover and no answer
     field;
   - all timestamps are numeric; and the list of 27 `node/id` codes.
3. **A loader check** (22 November; the same AI assistant; Appendix H). It ran an earlier version of the adapter
   (Appendix I) on the real files and printed only counts of people and rows. That run read every answer and
   hover into memory, but no answer value and no duration was printed or seen. The old version differed from the
   final code: it took the last answer event, not the first; it did not filter `analysis_duration.csv` for
   `event` = "mouseover"; it counted touch events anywhere in the log; and it used the old hover rule. Its whole
   output:
   - sample 1: 94 people, none without an answer, all 94 with at least one hover row of a known button code;
   - sample 2: 98 people, the same;
   - no hover row of these people had a missing duration, an unknown button code or another condition;
   - sample 3: 172 people in the log, 148 with an answer and 24 without; 11 of the 148 had no hover on any
     number; 16 had touch events.
   - Because the old parser would have crashed on an unreadable number and did not, we also know that no answer,
     duration or timestamp it read was unreadable to it.

**Who saw outputs 2 and 3:** the AI assistant that wrote the plan, and Bhavik. The two outside AI reviewers saw
the numbers quoted in the earlier texts of this plan. The forecasters are not shown them.

**What these looks already settle.**
- The sample sizes: 94, 98 and 148.
- In sample 3, at least 11 of the 148 people had no hover on any number, over all answer groups together, by the
  old measure. That is a fact about hovers crossed with having an answer. It is not a prospective result.
- Nobody in sample 3 has two answer events, so the "first answer" rule changes nothing there.
- No sample 1 hover row lacks a duration, so the "duration unknown" rule changes nothing there.
- No answer in any sample was missing, and none made the old parser fail. (The old parser accepted forms such as
  "1/2", which the final parser calls unreadable.)

**Decisions these looks informed:** the three-sample design; taking sample 3's answer from the log with no join;
classing a person with a log and no hover instead of leaving them out; reporting sample 3 with and without touch
devices.

**What has not been seen, as far as we know, by anyone on the team or by any AI working for it:** any answer
value; how many people are in any answer group; any hover duration; any person's record; any count of a hover
class within an answer group. **The prospective claim of this plan is limited to those.**

**Code versions.** The code in Appendices B to F was changed after the loader check and after each review. **This
final code has not been run on the real files.** It has been run only on made-up files (Appendices E and F). In
particular the `event` = "mouseover" filter and the new sample 3 rules meet the real files for the first time in
the run; the stops in section 4 guard against an empty table.

This plan makes no claim about prior work.

## 8. Procedure, the run record and failures

1. Done (22 November). Stage 0 and the two checks in section 7.
2. Done (22 November). Section 4 written; code written and tested on made-up files; two rounds of outside review.
3. A second AI session, which did not write the code, checks the code against this plan. Its first check, on 22
   November, found that the number reader could fail or hang on a number with a very long exponent; the
   exponent is now limited to three digits. Rereading the fix, the plan's author also limited digits to the
   characters 0 to 9. Its second check found that a failure to write the attempts log, or to hash the code files,
   could end in a Python error report instead of a line starting "STOP"; every step after the flag check is now
   inside one guard. The check is repeated on this text. Then this plan will be published under tag v37. The
   public tag carries the time.
4. Forecasts will be collected on the sheet in Appendix A and published as addendum v37.1.
5. One run, before 8 December: `python3 v37_run.py <folder> --run-after-tag`.
   - The flag guards against accidents only; it cannot check the tag.
   - The script checks the four data files' hashes before it reads anything.
   - It builds the whole report, saves it in one step to `v37_run_output.txt` with the UTC time and the hashes of
     the three code files, and only then prints it.
   - It writes a line to `v37_run_attempts.log` when an attempt starts and another when it ends, so an
     interrupted attempt is on record too. If the starting line cannot be written, it stops before it reads
     anything. If an ending line cannot be written, the STOP line or the report is still printed, and says so.
   - If the report cannot be saved, only a line starting "STOP" is printed.
   - No step can end in a Python error report: each ends in the report or in one STOP line. The one exception is
     a Ctrl-C, which is not caught; the starting line in the log is its record.
   - It refuses to run if `v37_run_output.txt` already exists.
   - Both files are published with the report.
6. **If the run fails.**
   - A run that saved or showed any count is final. It is reported whatever it shows and is not repeated. This
     holds even if the output is cut short.
   - A run that prints a line starting "STOP" has saved and shown no count. It may be retried once, after an
     addendum is published with the fix and the new code hashes.
   - A fix may change only what is needed to read the files: a column name, a code's spelling, or a number format.
     It may not change a sample, an answer window, a hover class, a threshold or the hover rule. If the files
     cannot be read without such a change, the analysis is abandoned and reported as not done.
7. Every count in section 5 is reported.

## 9. Files (SHA-256)

Code, the forecast sheet and the records of the earlier looks, in `exploratory/kept_ideas/v37/` of the team's
private working repository. Appendices A to L are byte-identical copies.

| Appendix | File | SHA-256 |
|---|---|---|
| A | `forecast_sheet_v37.txt` | `1e55897ee6e63664a7086b82e9184d5fbebdd65edc01b0d1b36ed9a21e386cd6` |
| B | `v37_hover.py` | `ab1312aa01298ab8e252ce3953813dd5cb0b874f35769067ad6c568e7cd54e92` |
| C | `v37_adapter.py` | `1536f0ca94e697a9540cbe243e4b24de66de81eef02a2e0abe783aee174a7835` |
| D | `v37_run.py` | `94253d4c1041a75cee01b0654297ac0b1f7f844869843fc455060caee523f6b2` |
| E | `test_v37.py` | `d4b29125a32d6de0c22b44c1b5256e0ba0f797e3f8072970bc1837da2c1db72c` |
| F | `test_v37_adapter.py` | `86f5ea02a5831dacbf50b1a149c95dbf13a0bdf279849195a4bfec0fd07188cb` |
| G | `preliminary_checks_2026-11-22/structure_check_2.py.txt` | `d4c74a882d1787a66884c2ead246ba37cf715c0b9f0e75f0a927717bff271c68` |
| H | `preliminary_checks_2026-11-22/loader_check.py.txt` | `6b47e3a543c4b077fbcec47528833d33365575f8076fd576321f8d6c0078376b` |
| I | `preliminary_checks_2026-11-22/v37_adapter_as_run_in_loader_check.py.txt` | `d9b4e807c6e59d608c6bb156626c4b317e277a08451b7a5cefe648271bc0902d` |
| J | `v37_structure.py` | `d075055493600c73424c4f09df45087d1c4d3a8604a195ce6168d9141e1af5f9` |
| K | `preliminary_checks_2026-11-22/v37_structure_as_run_in_stage0.py.txt` | `671d8360f4a55f561a62a8d7e2adc1ca1cd42a7aa072fe98983128131e01b480` |
| L | `preliminary_checks_2026-11-22/stage0_structure_excerpt.txt` | `691b560ce4d204f774bf4a7dd26f2c580fa7cf4b0ddfe61faeca5673874b8016` |

Data files, hashed only, from commit bc8d0689a76b97664251a9a65ff080d47049ad8c of the authors' repository. They are
not redistributed. `v37_run.py` checks these four hashes before it reads anything.

| File | SHA-256 |
|---|---|
| `scanDF2.csv` | `666ae25fa17caf10b662cd46baf08ce9de97d3b87bbc3102f5df6ac25c403220` |
| `analysis_scanpath.csv` | `c58785d07ae382d9689ab789b9e9fbc90b5f6581bc5e5f78a3c9c612624a198f` |
| `analysis_duration.csv` | `f635586aac58790c2b88e8e9f0c2d44754b86ad7b599f36ace81644303e3d115` |
| `w2_prob_aitor.csv` | `561d8f2b3c0c0b9e348421239a0b668f9967101470c40353cfdec6924121431d` |

## Appendix A. `forecast_sheet_v37.txt`

```text
FORECAST SHEET, plan v37. Fill this in before any result exists. Do not look anything up.

THE STUDY (Reani, Davies, Peek & Jay, 2019, Study 2, percentage format)
Adults recruited online saw one probability problem drawn as a tree. Every number was hidden under a button and
showed only while the mouse was over that button. The mouse was logged. The buttons:
  - Total: 100%
  - Fire: 10%            No fire: 90%               (the two BASE-RATE buttons)
  - under Fire:     Alarm: 50%     No alarm: 50%    (the two 50% BUTTONS)
  - under No fire:  Alarm: 27%     No alarm: 73%
  - Question button: it asks for the probability that there is a real fire, given that the alarm has gone off.
The correct answer is 17%.
Note that 50% is printed on two different buttons. It is also a round number that a person could type without
reading any button.

THE SAMPLE YOU ARE FORECASTING
The authors' final sample: 94 people. Before this, the authors had removed:
  - people who took part more than once, and duplicate submissions;
  - a list of people they judged to have answered "with a thoughtless pattern" (their rule is not written down);
  - people who never opened the question button, or who opened fewer than two other buttons.

OUR RULES
- A hover counts if it was recorded at all, however short.
- We look only at people whose answer was from 49 to 51.

YOUR FORECAST
1. How many of the 94 people gave an answer from 49 to 51?                                    ____ people

2. Of those people, what percentage are in each group? The four must add up to 100.
   (If your answer to question 1 is 0, leave this blank.)
   A  no hover on either 50% button, and none on either base-rate button                      ____ %
   B  a hover on a base-rate button, none on a 50% button                                     ____ %
   C  a hover on a 50% button, none on a base-rate button                                     ____ %
   D  a hover on a 50% button and on a base-rate button                                       ____ %

3. What have you already seen or heard about this study, its data or this plan?  ______________________________

Name: ____________________    Date and time: ____________________
```

## Appendix B. `v37_hover.py`

```python
"""Plan v37: who had a recorded hover on the base rate? Reani, Davies, Peek & Jay (2019) hover-to-reveal data.
CORE LOGIC ONLY. The readers for the authors' files are in v37_adapter.py and the single run is v37_run.py.

Study 2, probability format (the same numbers for everyone: base rate 10%, alarm given fire 50%, alarm given no
fire 27%; the correct answer is 5000/293 = 17.06...%). Every number is behind a hover button: F and nF show the
base rate (10% / 90%); FA and FnA both show 50% (alarm / no alarm, given fire); nFA and nFnA show 27% / 73%.

A hover counts at threshold 0 if it was recorded at all. At 250 and 500 ms it counts if its duration is unknown or
at least the threshold. Each person is in exactly one hover class:
  NEITHER     no counted hover on a 50% button (FA, FnA) and none on a base-rate button (F, nF)
  BASE_ONLY   a base-rate button, no 50% button
  FIFTY_ONLY  a 50% button, no base-rate button
  BOTH        a 50% button and a base-rate button
and in exactly one answer group (exact arithmetic, limits included):
  near_50       the answer is from 49 to 51
  near_correct  the answer is within 1 point of 5000/293 (so 17 and 18 count; 16 does not)
  other         everything else
"No base-rate hover" = NEITHER + FIFTY_ONLY. It is reported with a marginal exact (Clopper-Pearson) 95% interval,
which is a model-based summary (binomial sampling) for this selected sample. Durations are compared exactly.
"""
from fractions import Fraction as Q
from math import comb

BASE_LOCS = {"F", "nF"}
FIFTY_LOCS = {"FA", "FnA"}
FIFTY = Q(50)
BAYES = Q(100) * Q(1, 10) * Q(1, 2) / (Q(1, 10) * Q(1, 2) + Q(9, 10) * Q(27, 100))    # 5000/293
WINDOW = Q(1)
MIN_MS = (0, 250, 500)
CLASSES = ("NEITHER", "BASE_ONLY", "FIFTY_ONLY", "BOTH")
GROUPS = ("near_50", "near_correct", "other")
PRIMARY_GROUP, PRIMARY_MS = "near_50", 0


def seen(reveals, min_ms):
    """reveals: iterable of (pid, location, duration_ms or None). → {pid: set of locations with a counted hover}."""
    out = {}
    for pid, loc, dur in reveals:
        out.setdefault(pid, set())
        if min_ms == 0 or dur is None or dur >= min_ms:
            out[pid].add(loc)
    return out


def answer_group(a):
    if abs(a - FIFTY) <= WINDOW:
        return "near_50"
    if abs(a - BAYES) <= WINDOW:
        return "near_correct"
    return "other"


def hover_class(locs):
    fifty, base = bool(locs & FIFTY_LOCS), bool(locs & BASE_LOCS)
    return "BOTH" if fifty and base else "FIFTY_ONLY" if fifty else "BASE_ONLY" if base else "NEITHER"


def clopper_pearson(k, n, level=0.95):
    if n == 0:
        return (0.0, 1.0)
    a = (1 - level) / 2

    def cdf(p, kk):
        return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(kk + 1))

    def solve(f, lo, hi):
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    lo = 0.0 if k == 0 else solve(lambda p: 1 - cdf(p, k - 1) < a, 0.0, 1.0)
    hi = 1.0 if k == n else solve(lambda p: cdf(p, k) > a, 0.0, 1.0)
    return (lo, hi)


def split(answers, reveals, min_ms=0, logged=()):
    """answers: {pid: answer in points (Fraction)}. → (table[group][class] = count, people with no hover log).
    logged: people known to have a hover log; one of them with no counted hover is classed NEITHER, not left out."""
    s = seen(reveals, min_ms)
    for pid in logged:
        s.setdefault(pid, set())
    table = {g: {c: 0 for c in CLASSES} for g in GROUPS}
    no_log = 0
    for pid, a in answers.items():
        if pid not in s:
            no_log += 1
            continue
        table[answer_group(a)][hover_class(s[pid])] += 1
    return table, no_log


def no_base(row):
    return row["NEITHER"] + row["FIFTY_ONLY"]


def report(answers, reveals, logged=(), primary=False):
    """Counts per cell; for each answer group, the no-base-rate-hover count with its share and interval."""
    lines = []
    for ms in MIN_MS:
        table, no_log = split(answers, reveals, ms, logged)
        rule = "any recorded hover" if ms == 0 else f"duration unknown or at least {ms} ms"
        lines.append(f"== a hover counts if: {rule}; people with an answer but no hover log (left out): {no_log}")
        for g in GROUPS:
            row = table[g]
            n, k = sum(row.values()), no_base(row)
            tag = "PRIMARY >> " if primary and g == PRIMARY_GROUP and ms == PRIMARY_MS else "  "
            cells = "; ".join(f"{c} {row[c]}" for c in CLASSES)
            tail = " (no eligible respondents)"
            if n:
                lo, hi = clopper_pearson(k, n)
                tail = f" = {100 * k / n:.1f}% [{100 * lo:.1f}, {100 * hi:.1f}]"
            lines.append(f"{tag}{g}: N {n}; {cells}; no base-rate hover {k}/{n}{tail}")
    return "\n".join(lines)
```

## Appendix C. `v37_adapter.py`

```python
"""Plan v37: readers for the Reani et al. (2019) files. The tests (test_v37_adapter.py) use made-up files only.
Column names and codes are from stage 0. An earlier version of this file was run once on the real files as a
loader check (plan section 7); this version has not been run on them.

Three samples, all Study 2 ("wave 2"), probability format:
  final     the authors' final analysis set: people in scanDF2.csv                     (primary)
  cleaned   the authors' cleaned set before their last rule: people in analysis_scanpath.csv
  raw       the raw mouse log w2_prob_aitor.csv with none of the authors' exclusions: every person whose first
            answer event holds a readable answer

A number (parse): surrounding spaces are removed; then an optional sign, digits with an optional decimal point,
and an optional exponent of at most three digits, as R and JavaScript write numbers; at most 60 characters in
all. Only the characters 0 to 9 count as digits. Nothing else is a number: no "%", no fraction, no words, no
underscores, no longer exponent, no digit from another script. Empty, NA, NaN, nan, null, NULL and None mean missing.
Everything else is unreadable.

final / cleaned
  people    rows with Wave == 2 and numerical_format == "probability"; column Ps. A repeated Ps stops the run.
  answer    analysis_scanpath.csv, answer1 (a percentage: the authors divide it by 100, FIRE_analysis.R:72-74).
            scanDF2.csv's Given_answer is NOT used: the authors overwrite it for people they scored correct.
  hovers    analysis_duration.csv rows with sid == Ps, wave == 2, n_format == "prob", event == "mouseover" and
            node.id A..H; duration in ms (the authors' own cleaning). A person with at least one such row has a
            hover log. Rows with any other node.id are counted and not used. A duration that is missing or
            unreadable is "unknown".
  stops     the run stops, printing no count, if the sample has no readable answer, if nobody with an answer
            has a hover log, or if no answer is above 1 (answer1 would then not be a percentage).
raw
  answer    the person's FIRST event whose formInputs/ans1 is not missing (stage 0: only "submit" events carry
            it, and nobody has two). If that value is unreadable the person is counted and left out. People with
            no such event are counted and left out. Later answer events are only counted.
  window    the person's events in order of (timestampms, file order), up to and including that answer event.
  hover     on node K: starts at a mouseover on study-button-nodeK or study-node-K. It ends at the first of:
            (1) a mouseout on node K, unless a mouseover on node K follows within GRACE_MS; in that case the
                hover continues and the events between the two are ignored;
            (2) a mouseover on anything that is not node K;
            (3) the answer event.
            A mouseout on anything else is ignored. A hover on the question is not counted.
  touch     the person has a mobileTouchStart / mobileTouchEnd event in the window.
  stops     the run stops if nobody has a readable answer.

Which number each button shows (from the study page's own HTML, seen in stage 0): node 1 the total (100%),
node 2 "Fire" (10%), node 3 "No fire" (90%), node 4 "Alarm" under fire (50%), node 5 "No alarm" under fire (50%),
node 6 "Alarm" under no fire (27%), node 7 "No alarm" under no fire (73%). The authors' letters A..G are nodes 1..7
and H is the question (cleanAITORdata.R:66-83).
"""
import csv
import re
from decimal import Decimal, InvalidOperation
from fractions import Fraction as Q
from pathlib import Path

NODE = {1: "T", 2: "F", 3: "nF", 4: "FA", 5: "FnA", 6: "nFA", 7: "nFnA"}
LETTER = {"A": "T", "B": "F", "C": "nF", "D": "FA", "E": "FnA", "F": "nFA", "G": "nFnA", "H": "Q"}
RAW_IDS = {**{f"study-button-node{k}": v for k, v in NODE.items()}, **{f"study-node-{k}": v for k, v in NODE.items()},
           "question-node-inner": "Q", "tree-question-node": "Q"}
NUMBER_LOCS = frozenset(NODE.values())
HOVER_EVENTS = ("mouseover", "mouseout")
TOUCH_EVENTS = ("mobileTouchStart", "mobileTouchEnd")
WAVE, FORMAT, FORMAT_SHORT = 2, "probability", "prob"
GRACE_MS = 50
MISSING = ("", "NA", "NaN", "nan", "null", "NULL", "None")
NUMBER = re.compile(r"[+-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)([eE][+-]?[0-9]{1,3})?")


def _rows(path):
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        yield from csv.DictReader(fh)


def parse(x):
    """→ ("ok", exact Fraction) | ("missing", None) | ("bad", None). Never raises; never returns or prints the
    text it was given."""
    x = (x or "").strip()
    if x in MISSING:
        return "missing", None
    if len(x) > 60 or NUMBER.fullmatch(x) is None:
        return "bad", None
    try:
        return "ok", Q(Decimal(x))                             # at most about 1,060 digits, so this is quick
    except (InvalidOperation, ValueError, OverflowError):
        return "bad", None


def _is_wave2_prob(r):
    return parse(r.get("Wave"))[1] == WAVE and (r.get("numerical_format") or "").strip().lower() == FORMAT


def _people(path):
    ps = [r["Ps"] for r in _rows(path) if _is_wave2_prob(r)]
    if not ps:
        raise SystemExit(f"STOP: {Path(path).name} has no Study 2 probability rows (column names or codes differ)")
    if len(set(ps)) != len(ps):
        raise SystemExit(f"STOP: {Path(path).name} has a repeated person id among Study 2 probability rows")
    return set(ps)


def cleaned(folder, final_only):
    """→ (answers {pid: percent}, hovers [(pid, location, ms or None)], logged set, notes dict)."""
    folder = Path(folder)
    in_cleaned = _people(folder / "analysis_scanpath.csv")
    sample, notes = in_cleaned, {}
    if final_only:
        final = _people(folder / "scanDF2.csv")
        notes["people_in_final_file"] = len(final)
        notes["final_people_not_in_cleaned_file"] = len(final - in_cleaned)
        sample = final & in_cleaned
    answers, missing, bad = {}, 0, 0
    for r in _rows(folder / "analysis_scanpath.csv"):
        if _is_wave2_prob(r) and r["Ps"] in sample:
            status, a = parse(r.get("answer1"))
            if status == "ok":
                answers[r["Ps"]] = a
            elif status == "missing":
                missing += 1
            else:
                bad += 1
    hovers, logged = [], set()
    other_condition = other_event = unknown_code = no_duration = bad_duration = negative = 0
    for r in _rows(folder / "analysis_duration.csv"):
        if r["sid"] not in sample:
            continue
        if parse(r.get("wave"))[1] != WAVE or (r.get("n_format") or "").strip().lower() != FORMAT_SHORT:
            other_condition += 1
            continue
        if (r.get("event") or "").strip() != "mouseover":
            other_event += 1
            continue
        loc = LETTER.get((r.get("node.id") or "").strip())
        if loc is None:
            unknown_code += 1
            continue
        logged.add(r["sid"])
        status, d = parse(r.get("duration"))
        no_duration += status == "missing"
        bad_duration += status == "bad"
        negative += status == "ok" and d < 0
        hovers.append((r["sid"], loc, d))                     # d is an exact Fraction, or None for unknown
    name = "scanDF2.csv" if final_only else "analysis_scanpath.csv"
    if not answers:
        raise SystemExit(f"STOP: no readable answer for the Study 2 probability people of {name}")
    if not logged & set(answers):
        raise SystemExit(f"STOP: nobody with an answer in {name} has a hover row (event or button codes differ)")
    if max(answers.values()) <= 1:
        raise SystemExit("STOP: no answer1 value is above 1, so the column does not look like a percentage")
    notes.update({"people_in_sample": len(sample), "people_with_an_answer": len(answers),
                  "people_with_no_answer": missing, "people_with_an_unreadable_answer": bad,
                  "people_with_an_answer_and_a_hover_log": len(logged & set(answers)),
                  "hover_rows_in_another_condition": other_condition, "hover_rows_not_mouseover": other_event,
                  "hover_rows_with_an_unknown_button_code": unknown_code, "hover_rows_with_no_duration": no_duration,
                  "hover_rows_with_an_unreadable_duration": bad_duration,
                  "hover_rows_with_a_negative_duration": negative})
    return answers, hovers, logged, notes


def _raw_reveals(events, cutoff):
    """events: [(t, event, location or None)] in order, up to the answer event. → [(location, exact ms)]."""
    ev = [e for e in events if e[1] in HOVER_EVENTS]
    out, cur, start, i = [], None, None, 0
    while i < len(ev):
        t, kind, loc = ev[i]
        number = loc if loc in NUMBER_LOCS else None
        if cur is not None and kind == "mouseout" and number == cur:
            j = i + 1                                           # does a mouseover on K follow within the grace time?
            while j < len(ev) and ev[j][0] - t <= GRACE_MS and not (ev[j][1] == "mouseover" and ev[j][2] == cur):
                j += 1
            if j < len(ev) and ev[j][0] - t <= GRACE_MS:
                i = j + 1                                       # yes: the hover continues; events in between ignored
                continue
            out.append((cur, t - start))                        # no: the hover ended at this mouseout
            cur = start = None
        elif kind == "mouseover" and number != cur:
            if cur is not None:
                out.append((cur, t - start))                    # a mouseover on something that is not K
                cur = start = None
            if number is not None:
                cur, start = number, t
        i += 1                                                  # a mouseout on anything else is ignored
    if cur is not None:
        out.append((cur, cutoff - start))                       # still open at the answer event
    return out


def raw(folder):
    """→ (answers, hovers, logged, notes, touch set) for w2_prob_aitor.csv."""
    by, everyone, untimed = {}, set(), 0
    for i, r in enumerate(_rows(Path(folder) / "w2_prob_aitor.csv")):
        everyone.add(r["sid"])
        status, t = parse(r.get("timestampms"))
        if status != "ok":
            untimed += 1
            continue
        a_status, a = parse(r.get("formInputs/ans1"))
        by.setdefault(r["sid"], []).append((t, i, r["event"], RAW_IDS.get((r.get("node/id") or "").strip()),
                                           a_status, a))
    if not everyone:
        raise SystemExit("STOP: w2_prob_aitor.csv has no rows")
    answers, hovers, touch = {}, [], set()
    with_event = several = unreadable = 0
    for sid, evs in by.items():
        evs.sort(key=lambda e: (e[0], e[1]))
        carrying = [j for j, e in enumerate(evs) if e[4] != "missing"]
        if not carrying:
            continue
        with_event += 1
        several += len(carrying) > 1
        first = carrying[0]
        if evs[first][4] != "ok":
            unreadable += 1
            continue
        window = evs[:first + 1]                               # in (time, file order), the answer event included
        answers[sid] = evs[first][5]
        if any(e[2] in TOUCH_EVENTS for e in window):
            touch.add(sid)
        for loc, ms in _raw_reveals([(e[0], e[2], e[3]) for e in window], evs[first][0]):
            hovers.append((sid, loc, ms))
    if not answers:
        raise SystemExit("STOP: nobody in w2_prob_aitor.csv has a readable answer event")
    with_number = {p for p, _, _ in hovers}
    notes = {"people_in_the_log": len(everyone), "rows_without_a_readable_time": untimed,
             "people_with_an_answer_event": with_event, "people_without_an_answer_event": len(everyone) - with_event,
             "people_whose_first_answer_is_unreadable": unreadable, "people_with_a_readable_answer": len(answers),
             "people_with_more_than_one_answer_event": several,
             "people_with_an_answer_and_no_hover_on_any_number": len(set(answers) - with_number),
             "people_with_touch_events": len(touch)}
    return answers, hovers, set(answers), notes, touch
```

## Appendix D. `v37_run.py`

```python
"""The single run of plan v37. NOT RUN before plan v37 and its forecast addendum v37.1 are published.

    python3 v37_run.py <folder with the cloned repository> --run-after-tag

With the flag:
- every attempt appends a line to v37_run_attempts.log when it starts and another when it ends, beside this script.
  If the starting line cannot be written, the script stops before it reads anything. If an ending line cannot be
  written, the STOP line or the report is still printed, and says so;
- if v37_run_output.txt already exists the script stops: a completed run is final and is not repeated;
- the four data files' SHA-256 hashes are checked before anything is read;
- the whole report is built first, saved in one step to v37_run_output.txt with the UTC time and the hashes of the
  three code files, and only then printed. So a run either saves and prints every table, or prints one line
  starting "STOP" with no count and no data value. If the report cannot be saved, only that line is printed.
  Every step after the flag check is inside one guard, so none can end in a Python error report. The script's own
  STOP messages name only files and hashes; an unexpected error's own message is never shown. (A Ctrl-C is not
  caught; the STARTED line is its record.)
The report holds aggregate counts, one share and one interval per row: no answer value, no row, no person ID, no
duration. The flag only guards against accidents; the proof of order is the public tag time against the saved time.
"""
import hashlib
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import v37_adapter as A      # noqa: E402
import v37_hover as V        # noqa: E402

RUN_FLAG = "--run-after-tag"
OUTPUT_NAME, ATTEMPTS_NAME = "v37_run_output.txt", "v37_run_attempts.log"
CODE_FILES = ("v37_hover.py", "v37_adapter.py", "v37_run.py")
PAPER_N = 94                 # Study 2, probability format: Table 1 of the paper, 32 men + 62 women (plan section 2)
# Repository commit bc8d0689a76b97664251a9a65ff080d47049ad8c (plan section 4)
EXPECTED_SHA256 = {
    "scanDF2.csv": "666ae25fa17caf10b662cd46baf08ce9de97d3b87bbc3102f5df6ac25c403220",
    "analysis_scanpath.csv": "c58785d07ae382d9689ab789b9e9fbc90b5f6581bc5e5f78a3c9c612624a198f",
    "analysis_duration.csv": "f635586aac58790c2b88e8e9f0c2d44754b86ad7b599f36ace81644303e3d115",
    "w2_prob_aitor.csv": "561d8f2b3c0c0b9e348421239a0b668f9967101470c40353cfdec6924121431d",
}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_hashes(folder, expected=None):
    expected = EXPECTED_SHA256 if expected is None else expected
    bad = []
    for name, want in expected.items():
        p = Path(folder) / name
        got = sha256(p) if p.is_file() else "missing"
        if got != want:
            bad.append(f"{name}: expected {want}, found {got}")
    if bad:
        raise SystemExit("STOP: hash check failed: " + "; ".join(bad))


def section(title, answers, hovers, logged, notes, primary=False):
    return "\n".join([f"## {title}", "  " + "; ".join(f"{k}: {v}" for k, v in notes.items()),
                      V.report(answers, hovers, logged, primary)])


def reports(folder):
    out = []
    a, h, lg, n = A.cleaned(folder, final_only=True)
    n["paper_reports"] = PAPER_N
    out.append(section("SAMPLE 1: the authors' final analysis set (scanDF2.csv). Its near_50 row at 'any recorded "
                       "hover' is the primary result; every other row in this printout is secondary",
                       a, h, lg, n, primary=True))
    a, h, lg, n = A.cleaned(folder, final_only=False)
    out.append(section("SAMPLE 2: the authors' cleaned set before their last rule (analysis_scanpath.csv)",
                       a, h, lg, n))
    a, h, lg, n, touch = A.raw(folder)
    out.append(section("SAMPLE 3: raw mouse log, none of the authors' exclusions (w2_prob_aitor.csv); our own "
                       "hover rule", a, h, lg, n))
    a2 = {p: v for p, v in a.items() if p not in touch}
    h2 = [x for x in h if x[0] in a2]
    n2 = {"people_with_a_readable_answer": len(a2), "people_left_out_for_touch_events": len(a) - len(a2),
          "people_with_an_answer_and_no_hover_on_any_number": len(set(a2) - {p for p, _, _ in h2})}
    out.append(section("SAMPLE 3 without people who have touch events", a2, h2, lg & set(a2), n2))
    return "\n\n".join(out)


def _log(out_dir, stamp, outcome):
    """Append one line to the attempts log. → True if it was written, False if not. Never raises."""
    try:
        with open(Path(out_dir) / ATTEMPTS_NAME, "a", encoding="utf-8") as fh:
            fh.write(f"{stamp}\t{outcome}\n")
        return True
    except Exception:
        return False


NO_LOG = " The attempts log could not be written."


def _say(text):
    """Print, and never raise: if the screen cannot be written to there is nowhere left to report it."""
    try:
        sys.stdout.write(text + "\n")
    except Exception:
        pass


def _stop(out_dir, stamp, msg):
    """Print one line starting "STOP", whether or not the log can be written. → exit status 1."""
    logged = _log(out_dir, stamp, msg)
    _say(msg + " No count was printed." + ("" if logged else NO_LOG))
    return 1


def main(argv=None, out_dir=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2 or argv[1] != RUN_FLAG:
        _say(f"Nothing was read. The single run is: python3 v37_run.py <folder> {RUN_FLAG} (only after plan v37 "
             "and addendum v37.1 are published).")
        return 2
    out_dir = HERE if out_dir is None else Path(out_dir)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not _log(out_dir, stamp, "STARTED"):                    # an attempt that cannot be recorded reads nothing
        _say("STOP: the attempts log could not be written, so nothing was read. No count was printed.")
        return 1
    try:                                                       # every later step is inside this guard
        final = out_dir / OUTPUT_NAME
        if final.exists():
            raise SystemExit(f"STOP: {OUTPUT_NAME} already exists. A completed run is final and is not repeated.")
        check_hashes(argv[0])
        text = reports(argv[0])
        full = "\n".join(["# plan v37 run, started " + stamp + " (UTC)",
                          "# code: " + "; ".join(f"{f} {sha256(HERE / f)}" for f in CODE_FILES),
                          "# data: " + "; ".join(f"{k} {v}" for k, v in EXPECTED_SHA256.items()),
                          text, "# RUN COMPLETE"]) + "\n"
        tmp = out_dir / (OUTPUT_NAME + ".tmp")
        try:
            tmp.write_text(full, encoding="utf-8")
            os.replace(tmp, final)                             # the saved report appears whole or not at all
        except Exception as e:
            try:
                tmp.unlink()
            except OSError:
                pass
            raise SystemExit(f"STOP: the report could not be saved ({type(e).__name__}).")
    except SystemExit as e:
        return _stop(out_dir, stamp, e.code if isinstance(e.code, str) and e.code.startswith("STOP") else "STOP")
    except Exception as e:                                     # never show a traceback: it could hold a data value
        return _stop(out_dir, stamp,
                     f"STOP: unexpected {type(e).__name__}; details withheld so that no data value is printed.")
    logged = _log(out_dir, stamp, "COMPLETE")                  # the report is saved: it is printed whatever happens
    _say(full.rstrip("\n"))
    if not logged:
        _say("# NOTE:" + NO_LOG + " The saved report is the record of this completed run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Appendix E. `test_v37.py`

```python
"""Made-up rows only. No file from the authors' repository is read here."""
import unittest
from fractions import Fraction as Q
import v37_hover as V


class T(unittest.TestCase):
    def test_answer_groups_and_their_limits(self):
        self.assertEqual(V.BAYES, Q(5000, 293))                  # 17.0648...
        self.assertEqual(V.WINDOW, 1)
        for a, g in ((Q(49), "near_50"), (Q(50), "near_50"), (Q(51), "near_50"), (Q("48.999"), "other"),
                     (Q("51.001"), "other"), (Q(17), "near_correct"), (Q(18), "near_correct"), (Q(16), "other"),
                     (Q(19), "other"), (Q(5000, 293) + 1, "near_correct"), (Q(5000, 293) - 1, "near_correct"),
                     (Q(5000, 293) + 1 + Q(1, 10 ** 9), "other"), (Q(5), "other")):
            self.assertEqual(V.answer_group(a), g, a)

    def test_four_hover_classes(self):
        self.assertEqual(V.hover_class(set()), "NEITHER")
        self.assertEqual(V.hover_class({"Q", "nFA", "T"}), "NEITHER")
        self.assertEqual(V.hover_class({"F", "nFA"}), "BASE_ONLY")
        self.assertEqual(V.hover_class({"FA", "nFA"}), "FIFTY_ONLY")
        self.assertEqual(V.hover_class({"FnA"}), "FIFTY_ONLY")
        self.assertEqual(V.hover_class({"FnA", "nF"}), "BOTH")

    def test_split_and_threshold(self):
        answers = {"a": Q(50), "b": Q(50), "c": Q(50), "d": Q(17), "e": Q(5), "f": Q(50), "g": Q(50)}
        reveals = [("a", "FA", 900), ("a", "F", 100),          # both, but the base-rate hover is only 100 ms
                   ("b", "FA", 900),                             # a 50% button only
                   ("c", "Q", 900),                              # neither
                   ("g", "nF", 900),                             # base rate only
                   ("d", "F", 900), ("d", "FA", 900), ("d", "nFA", 900),
                   ("e", "FA", 900), ("e", "T", 900)]
        t0, nolog = V.split(answers, reveals, 0)
        self.assertEqual(nolog, 1)                               # f has an answer but no log
        self.assertEqual(t0["near_50"], {"NEITHER": 1, "BASE_ONLY": 1, "FIFTY_ONLY": 1, "BOTH": 1})
        self.assertEqual(V.no_base(t0["near_50"]), 2)
        self.assertEqual(t0["near_correct"]["BOTH"], 1)
        self.assertEqual(t0["other"]["FIFTY_ONLY"], 1)
        t250, _ = V.split(answers, reveals, 250)
        self.assertEqual(t250["near_50"], {"NEITHER": 1, "BASE_ONLY": 1, "FIFTY_ONLY": 2, "BOTH": 0})

    def test_duration_rules(self):
        r = [("a", "F", None), ("a", "FA", -5), ("b", "F", 0)]
        self.assertEqual(V.seen(r, 0), {"a": {"F", "FA"}, "b": {"F"}})      # any recorded hover counts at 0
        self.assertEqual(V.seen(r, 250), {"a": {"F"}, "b": set()})          # unknown counts; negative and 0 do not
        self.assertEqual(V.seen([("a", "F", 250)], 250), {"a": {"F"}})      # the threshold itself counts

    def test_logged_person_with_no_hover_is_classed_neither(self):
        t, nolog = V.split({"a": Q(50), "b": Q(50)}, [], 0, logged={"a"})
        self.assertEqual(t["near_50"], {"NEITHER": 1, "BASE_ONLY": 0, "FIFTY_ONLY": 0, "BOTH": 0})
        self.assertEqual(nolog, 1)                               # b has no log and is left out

    def test_clopper_pearson(self):
        lo, hi = V.clopper_pearson(0, 10)
        self.assertEqual(lo, 0.0); self.assertAlmostEqual(hi, 0.3085, places=3)
        lo, hi = V.clopper_pearson(10, 10)
        self.assertAlmostEqual(lo, 0.6915, places=3); self.assertEqual(hi, 1.0)
        lo, hi = V.clopper_pearson(5, 10)
        self.assertAlmostEqual(lo, 0.1871, places=3); self.assertAlmostEqual(hi, 0.8129, places=3)
        lo, hi = V.clopper_pearson(1, 1)
        self.assertAlmostEqual(lo, 0.025, places=6); self.assertEqual(hi, 1.0)
        self.assertEqual(V.clopper_pearson(0, 0), (0.0, 1.0))

    def test_report_marks_one_primary_row(self):
        out = V.report({"a": Q(50), "b": Q(17)}, [("a", "FA", 10), ("b", "F", 10)], primary=True)
        self.assertEqual(out.count("PRIMARY >>"), 1)
        first = [ln for ln in out.splitlines() if "PRIMARY" in ln][0]
        self.assertIn("near_50: N 1; NEITHER 0; BASE_ONLY 0; FIFTY_ONLY 1; BOTH 0; no base-rate hover 1/1", first)
        self.assertEqual(V.report({"a": Q(50)}, [("a", "FA", 10)]).count("PRIMARY"), 0)
        self.assertIn("other: N 0; NEITHER 0; BASE_ONLY 0; FIFTY_ONLY 0; BOTH 0; no base-rate hover 0/0", out)


if __name__ == "__main__":
    unittest.main()
```

## Appendix F. `test_v37_adapter.py`

```python
"""Made-up files only, written to a temporary folder with the real files' column names (from stage 0). No file from
the authors' repository is read here."""
import contextlib
import csv
import hashlib
import io
import tempfile
import unittest
from fractions import Fraction as Q
from pathlib import Path

import v37_adapter as A
import v37_hover as V
import v37_run as RUN


def write(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(header); w.writerows(rows)


SCAN = ["Ps", "Scanpath", "answer1", "answer2", "numerical_format", "Wave"]
DUR = ["event", "timestampms", "sid", "node.id", "n_format", "wave", "duration"]


def cleaned_files(d, extra_scan=(), extra_dur=()):
    write(d / "analysis_scanpath.csv", SCAN,
          [["p1", "HBD", "50", "NA", "probability", "2"],        # F and FA -> BOTH
           ["p2", "HD", "50", "NA", "probability", "2"],         # FA only -> FIFTY_ONLY
           ["p3", "HBDF", "17", "NA", "probability", "2"],
           ["p4", "HD", "50", "NA", "probability", "1"],         # wave 1: not in the sample
           ["p5", "HD", "5", "100", "frequency", "2"],           # frequency format: not in the sample
           ["p6", "HA", "50", "NA", "probability", "2"],         # in the cleaned set, not in the final set
           ["p7", "HB", "NA", "NA", "probability", "2"],         # no answer
           ["p8", "HB", "50%", "NA", "probability", "2"],        # unreadable answer
           ["p9", "HZ", "51", "NA", "probability", "2"],         # only an unknown button code: no hover log
           ["p10", "H", "49", "NA", "probability", "2"]]         # no hover row at all: no log
          + list(extra_scan))
    write(d / "scanDF2.csv", ["Ps", "numerical_format", "Wave", "Given_answer"],
          [["p1", "probability", "2", "0.5"], ["p2", "probability", "2", "0.5"], ["p3", "probability", "2", "0.17"],
           ["p4", "probability", "1", "0.5"], ["p7", "probability", "2", "0"], ["p99", "probability", "2", "0.5"]])
    write(d / "analysis_duration.csv", DUR,
          [["mouseover", "1", "p1", "H", "prob", "2", "900"], ["mouseover", "2", "p1", "B", "prob", "2", "100"],
           ["mouseover", "3", "p1", "D", "prob", "2", "NA"],
           ["mouseover", "4", "p2", "H", "prob", "2", "400"], ["mouseover", "5", "p2", "D", "prob", "2", "300"],
           ["mouseover", "6", "p3", "B", "prob", "2", "700"], ["mouseover", "7", "p3", "D", "prob", "2", "700"],
           ["mouseover", "8", "p3", "F", "prob", "2", "-3"],
           ["mouseover", "9", "p4", "D", "prob", "1", "700"],
           ["mouseover", "10", "p6", "A", "prob", "2", "700"], ["mouseover", "11", "p6", "Z", "prob", "2", "700"],
           ["mouseover", "12", "p9", "Z", "prob", "2", "700"],
           ["mouseout", "13", "p2", "B", "prob", "2", "700"],      # not a mouseover row: skipped
           ["mouseover", "14", "p2", "B", "freq", "2", "700"]]     # another condition: skipped
          + list(extra_dur))


RAW_HEADER = ["event", "timestampms", "sid", "node/id", "formInputs/ans1"]


def raw_file(d, extra=()):
    rows = [
        # s1: node 4 (button, then number overlay 2 ms later = one hover of 600 ms), then node 2, then submits 50
        ["mouseover", "1000", "s1", "study-button-node4", ""], ["mouseout", "1010", "s1", "study-button-node4", ""],
        ["mouseover", "1012", "s1", "study-node-4", ""], ["mouseout", "1600", "s1", "study-node-4", ""],
        ["mouseover", "1700", "s1", "tree-container", ""],
        ["mouseover", "2000", "s1", "study-button-node2", ""], ["mouseover", "2100", "s1", "line1", ""],
        ["submit", "5000", "s1", "", "50"],
        ["mouseover", "6000", "s1", "study-button-node3", ""],        # after the answer: not counted
        # s2: only the question and node 5, then 50 -> FIFTY_ONLY
        ["mouseover", "100", "s2", "tree-question-node", ""], ["mouseover", "300", "s2", "study-button-node5", ""],
        ["keydown", "350", "s2", "ans1", ""], ["submit", "900", "s2", "", "50"],
        # s3: no hover at all, answers 50 -> NEITHER (has a log, so it is classed, not left out)
        ["load", "10", "s3", "", ""], ["submit", "500", "s3", "", "50"],
        # s4: hovers but never submits -> left out
        ["mouseover", "10", "s4", "study-button-node2", ""],
        # s5: touch device, answers 17 after nodes 2, 4, 6
        ["mobileTouchStart", "5", "s5", "", ""], ["mouseover", "10", "s5", "study-button-node2", ""],
        ["mouseover", "20", "s5", "study-button-node4", ""], ["mouseover", "30", "s5", "study-button-node6", ""],
        ["submit", "90", "s5", "", "17"],
        # s6: base rate only, answers 50 -> BASE_ONLY; a row with no time is dropped and counted
        ["mouseover", "10", "s6", "study-node-3", ""], ["mouseover", "", "s6", "study-button-node4", ""],
        ["submit", "80", "s6", "", "50"],
        # s7: only untimed rows: in the log census, no answer
        ["submit", "NA", "s7", "", "50"]] + list(extra)
    write(d / "w2_prob_aitor.csv", RAW_HEADER, rows)


class Parse(unittest.TestCase):
    def test_parse_never_raises_and_rejects_odd_text(self):
        self.assertEqual(A.parse("50"), ("ok", Q(50)))
        self.assertEqual(A.parse(" 17.5 "), ("ok", Q(35, 2)))
        self.assertEqual(A.parse("5E+1"), ("ok", Q(50)))
        self.assertEqual(A.parse("1e+05"), ("ok", Q(100000)))       # as R writes 100000
        self.assertEqual(A.parse("1e999")[0], "ok")                 # three exponent digits is the limit
        for x in ("1e1000", "1e999999999", "1e99999999999999999999", "1e-1000", "9" * 61):
            self.assertEqual(A.parse(x), ("bad", None))             # quick, and never an error
        for x, v in ((".5", Q(1, 2)), ("5.", Q(5)), ("+3", Q(3)), ("-2.50", Q(-5, 2))):
            self.assertEqual(A.parse(x), ("ok", v))
        for x in ("", "  ", "NA", None, "null", "NaN", "nan", "NULL", "None"):
            self.assertEqual(A.parse(x), ("missing", None))
        for x in ("50%", "1/2", "inf", "-Infinity", "sNaN", "fifty", "5 0", "0x32", "1_000", "5,0", "e5", ".",
                  "1" * 61, "\u0665", "\uff11\uff12", "5\u0660"):   # digits of other scripts are not read
            self.assertEqual(A.parse(x), ("bad", None), x)


class Cleaned(unittest.TestCase):
    def test_final_and_cleaned_samples(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); cleaned_files(d)
            a, h, lg, n = A.cleaned(d, final_only=True)
            self.assertEqual(set(a), {"p1", "p2", "p3"})
            self.assertEqual(a["p1"], Q(50))
            self.assertEqual(n["people_in_final_file"], 5)                     # p1, p2, p3, p7, p99
            self.assertEqual(n["final_people_not_in_cleaned_file"], 1)         # p99
            self.assertEqual(n["people_in_sample"], 4)
            self.assertEqual(n["people_with_no_answer"], 1)                    # p7, counted inside this sample
            self.assertEqual(n["people_with_an_unreadable_answer"], 0)
            self.assertEqual(n["hover_rows_with_no_duration"], 1)
            self.assertEqual(n["hover_rows_with_a_negative_duration"], 1)
            self.assertEqual(n["hover_rows_not_mouseover"], 1)
            self.assertEqual(n["hover_rows_in_another_condition"], 1)
            t, nolog = V.split(a, h, 0, lg)
            self.assertEqual(nolog, 0)
            self.assertEqual(t["near_50"], {"NEITHER": 0, "BASE_ONLY": 0, "FIFTY_ONLY": 1, "BOTH": 1})
            self.assertEqual(t["near_correct"]["BOTH"], 1)
            t250, _ = V.split(a, h, 250, lg)                  # p1's base-rate hover lasted 100 ms
            self.assertEqual(t250["near_50"], {"NEITHER": 0, "BASE_ONLY": 0, "FIFTY_ONLY": 2, "BOTH": 0})

    def test_cleaned_sample_log_presence_and_answers(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); cleaned_files(d)
            a, h, lg, n = A.cleaned(d, final_only=False)
            self.assertEqual(set(a), {"p1", "p2", "p3", "p6", "p9", "p10"})
            self.assertEqual(n["people_in_sample"], 8)
            self.assertEqual(n["people_with_no_answer"], 1); self.assertEqual(n["people_with_an_unreadable_answer"], 1)
            self.assertEqual(n["hover_rows_with_an_unknown_button_code"], 2)
            self.assertNotIn("p9", lg)                        # a row with a code outside A..H is not a hover log
            self.assertEqual(n["people_with_an_answer_and_a_hover_log"], 4)
            t, nolog = V.split(a, h, 0, lg)
            self.assertEqual(nolog, 2)                        # p9 and p10 have no usable hover row
            self.assertEqual(t["near_50"], {"NEITHER": 1, "BASE_ONLY": 0, "FIFTY_ONLY": 1, "BOTH": 1})   # p6: total only
            self.assertTrue(all(d is None or isinstance(d, Q) for _, _, d in h))      # durations stay exact

    def test_stops_when_nothing_matches_or_an_id_repeats(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            write(d / "analysis_scanpath.csv", ["Ps", "answer1", "numerical_format", "Wave"],
                  [["p", "50", "frequency", "2"]])
            with self.assertRaises(SystemExit):
                A.cleaned(d, final_only=False)
            cleaned_files(d, extra_scan=[["p1", "HB", "17", "NA", "probability", "2"]])
            with self.assertRaises(SystemExit) as cm:
                A.cleaned(d, final_only=False)
            self.assertNotIn("p1", str(cm.exception.code))    # the message names no person


class Stops(unittest.TestCase):
    def test_stops_instead_of_printing_empty_tables(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); cleaned_files(d)
            write(d / "analysis_duration.csv", DUR, [["hover", "1", "p1", "D", "prob", "2", "900"]])
            with self.assertRaises(SystemExit) as cm:          # the event label differs: nobody has a hover log
                A.cleaned(d, final_only=True)
            self.assertTrue(str(cm.exception.code).startswith("STOP"))
            cleaned_files(d)
            write(d / "analysis_scanpath.csv", SCAN, [["p1", "HBD", "0.5", "NA", "probability", "2"],
                                                      ["p2", "HD", "0.17", "NA", "probability", "2"]])
            with self.assertRaises(SystemExit):                # answers on a 0-1 scale
                A.cleaned(d, final_only=True)
            write(d / "analysis_scanpath.csv", SCAN, [["p1", "HBD", "50%", "NA", "probability", "2"]])
            with self.assertRaises(SystemExit):                # no readable answer
                A.cleaned(d, final_only=True)
            write(d / "w2_prob_aitor.csv", RAW_HEADER, [["submit", "5", "s", "", "50%"]])
            with self.assertRaises(SystemExit):
                A.raw(d)


class Raw(unittest.TestCase):
    def test_raw_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); raw_file(d)
            a, h, lg, n, touch = A.raw(d)
            self.assertEqual(set(a), {"s1", "s2", "s3", "s5", "s6"})
            self.assertEqual(n["people_in_the_log"], 7)
            self.assertEqual(n["rows_without_a_readable_time"], 2)
            self.assertEqual(n["people_without_an_answer_event"], 2)                  # s4 and s7
            self.assertEqual(n["people_with_an_answer_event"], 5)
            self.assertEqual(n["people_whose_first_answer_is_unreadable"], 0)
            self.assertEqual(n["people_with_a_readable_answer"], 5)
            self.assertEqual(n["people_with_an_answer_and_no_hover_on_any_number"], 1)
            self.assertEqual(n["people_with_more_than_one_answer_event"], 0)
            self.assertEqual(touch, {"s5"})
            s1 = [(loc, ms) for p, loc, ms in h if p == "s1"]
            self.assertEqual(s1, [("FA", 600.0), ("F", 100.0)])            # nF after the answer is not there
            t, nolog = V.split(a, h, 0, lg)
            self.assertEqual(nolog, 0)
            self.assertEqual(t["near_50"], {"NEITHER": 1, "BASE_ONLY": 1, "FIFTY_ONLY": 1, "BOTH": 1})
            self.assertEqual(t["near_correct"]["BOTH"], 1)
            t250, _ = V.split(a, h, 250, lg)                                # s1's base-rate hover lasted 100 ms
            self.assertEqual(t250["near_50"]["FIFTY_ONLY"], 2)

    def test_first_answer_wins_and_later_hovers_do_not_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            raw_file(d, extra=[["mouseover", "100", "t1", "study-button-node4", ""], ["submit", "500", "t1", "", "50"],
                               ["mouseover", "600", "t1", "study-button-node2", ""],
                               ["submit", "1000", "t1", "", "17"]])
            a, h, lg, n, _ = A.raw(d)
            self.assertEqual(a["t1"], Q(50))
            self.assertEqual({loc for p, loc, _ in h if p == "t1"}, {"FA"})
            self.assertEqual(n["people_with_more_than_one_answer_event"], 1)

    def test_unreadable_first_answer_leaves_the_person_out(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            raw_file(d, extra=[["mouseover", "100", "w1", "study-button-node4", ""], ["submit", "200", "w1", "", "50%"],
                               ["mouseover", "300", "w1", "study-button-node2", ""], ["submit", "400", "w1", "", "50"],
                               ["submit", "10", "w2", "", "fifty"]])
            a, h, lg, n, _ = A.raw(d)
            self.assertNotIn("w1", a); self.assertNotIn("w2", a)          # a later readable answer does not rescue
            self.assertFalse([x for x in h if x[0] in ("w1", "w2")])
            self.assertEqual(n["people_whose_first_answer_is_unreadable"], 2)
            self.assertEqual(n["people_with_more_than_one_answer_event"], 1)
            self.assertEqual(n["people_with_an_answer_event"], 7)
            self.assertEqual(n["people_without_an_answer_event"], 2)      # still only s4 and s7

    def test_tied_timestamps_follow_file_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            raw_file(d, extra=[["mouseover", "1000", "u1", "study-button-node4", ""],
                               ["mouseover", "2000", "u1", "study-button-node6", ""],     # same time, before submit
                               ["submit", "2000", "u1", "", "50"],
                               ["mouseover", "2000", "u1", "study-button-node2", ""]])    # same time, after submit
            a, h, lg, n, _ = A.raw(d)
            self.assertEqual({loc for p, loc, _ in h if p == "u1"}, {"FA", "nFA"})        # F is after the answer
            self.assertEqual(V.hover_class(V.seen(h, 0)["u1"]), "FIFTY_ONLY")

    def test_touch_after_the_answer_does_not_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            raw_file(d, extra=[["submit", "10", "v1", "", "50"], ["mobileTouchStart", "20", "v1", "", ""]])
            self.assertNotIn("v1", A.raw(d)[4])

    def test_hover_rule(self):
        R, o, x = A._raw_reveals, "mouseover", "mouseout"
        # ends at the mouseout on K when nothing on K follows within the grace time
        self.assertEqual(R([(Q(100), o, "FA"), (Q(250), x, "FA")], Q(400)), [("FA", 150.0)])
        # runs to the answer when nothing ends it; other event types do not end it
        self.assertEqual(R([(Q(100), o, "FA"), (Q(150), "keydown", None)], Q(400)), [("FA", 300.0)])
        # a mouseover on the question ends it and starts nothing
        self.assertEqual(R([(Q(100), o, "Q"), (Q(200), o, "F"), (Q(260), o, "Q")], Q(400)), [("F", 60.0)])
        # two separate looks at K are two hovers, not one long one
        self.assertEqual(R([(Q(100), o, "FA"), (Q(200), x, "FA"), (Q(5000), o, "FA"), (Q(5100), x, "FA")], Q(6000)),
                         [("FA", 100.0), ("FA", 100.0)])
        # a mouseout on something else does not end a hover on K
        self.assertEqual(R([(Q(100), o, "Q"), (Q(200), o, "F"), (Q(201), x, "Q"), (Q(900), x, "F")], Q(1000)),
                         [("F", 700.0)])
        self.assertEqual(R([(Q(200), o, "F"), (Q(300), x, None), (Q(900), x, "F")], Q(1000)), [("F", 700.0)])
        # within the grace time other events are ignored: a 1 ms visit to the question does not split the hover
        self.assertEqual(R([(Q(0), o, "F"), (Q(249), x, "F"), (Q(250), o, "Q"), (Q(251), o, "F"), (Q(252), x, "F")],
                           Q(300)), [("F", 252)])
        # the step from the button to its number may cross the background
        self.assertEqual(R([(Q(1000), o, "FA"), (Q(1010), x, "FA"), (Q(1011), o, None), (Q(1012), o, "FA"),
                            (Q(1600), x, "FA"), (Q(1700), o, None)], Q(5000)), [("FA", 600)])
        # another number during the grace time, and no return to K: K ends at its mouseout, the other starts
        self.assertEqual(R([(Q(0), o, "F"), (Q(100), x, "F"), (Q(120), o, "FA")], Q(300)),
                         [("F", 100), ("FA", 180)])
        # durations are exact fractions, not floats
        self.assertIsInstance(R([(Q(1, 3), o, "F")], Q(1))[0][1], Q)
        # the grace time: back on K within 50 ms continues; after 51 ms it is a new hover
        self.assertEqual(R([(Q(0), o, "F"), (Q(100), x, "F"), (Q(150), o, "F"), (Q(400), x, "F")], Q(900)),
                         [("F", 400.0)])
        self.assertEqual(R([(Q(0), o, "F"), (Q(100), x, "F"), (Q(151), o, "F"), (Q(400), x, "F")], Q(900)),
                         [("F", 100.0), ("F", 249.0)])
        # a mouseover on another number ends K and starts the other
        self.assertEqual(R([(Q(0), o, "F"), (Q(100), o, "FA")], Q(300)), [("F", 100.0), ("FA", 200.0)])
        # a hover of zero length is still a recorded hover
        self.assertEqual(R([(Q(100), o, "F")], Q(100)), [("F", 0.0)])

    def test_button_map(self):
        self.assertEqual(A.RAW_IDS["study-node-2"], "F"); self.assertEqual(A.RAW_IDS["study-button-node4"], "FA")
        self.assertEqual([A.LETTER[x] for x in "ABCDEFGH"], ["T", "F", "nF", "FA", "FnA", "nFA", "nFnA", "Q"])
        self.assertEqual({A.NODE[2], A.NODE[3]}, V.BASE_LOCS); self.assertEqual({A.NODE[4], A.NODE[5]}, V.FIFTY_LOCS)
        self.assertNotIn("Q", A.NUMBER_LOCS); self.assertEqual(len(A.NUMBER_LOCS), 7)


class Run(unittest.TestCase):
    def run_main(self, argv, out_dir=None):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = RUN.main(argv, out_dir)
        return code, buf.getvalue()

    def test_reads_nothing_without_the_flag(self):
        with tempfile.TemporaryDirectory() as out:
            for argv in (["some/folder"], [], ["some/folder", "--other"]):
                code, text = self.run_main(argv, out)
                self.assertEqual(code, 2); self.assertTrue(text.startswith("Nothing was read."))
            self.assertEqual(list(Path(out).iterdir()), [])                  # no log, no output file

    def test_hash_check_stops_on_other_files(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
            d = Path(tmp); cleaned_files(d); raw_file(d)
            with self.assertRaises(SystemExit):
                RUN.check_hashes(d)                                          # made-up files are not the real ones
            code, text = self.run_main([str(d), RUN.RUN_FLAG], out)          # so the flagged run stops before reading
            self.assertEqual(code, 1); self.assertTrue(text.startswith("STOP: hash check failed"))
            self.assertNotIn("RUN COMPLETE", text); self.assertNotIn("near_50", text)
            self.assertFalse((Path(out) / RUN.OUTPUT_NAME).exists())
            log = (Path(out) / RUN.ATTEMPTS_NAME).read_text().splitlines()
            self.assertTrue(log[0].endswith("STARTED")); self.assertIn("STOP: hash check failed", log[1])

    def test_full_made_up_run_saves_once_and_is_final(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
            d = Path(tmp); cleaned_files(d); raw_file(d)
            ok = {n: hashlib.sha256((d / n).read_bytes()).hexdigest() for n in RUN.EXPECTED_SHA256}
            old, old_reports = RUN.EXPECTED_SHA256, RUN.reports
            try:
                RUN.EXPECTED_SHA256 = ok

                def boom(folder):
                    raise ValueError("secret value 50")
                RUN.reports = boom
                code, text = self.run_main([str(d), RUN.RUN_FLAG], out)
                self.assertEqual(code, 1); self.assertIn("STOP: unexpected ValueError", text)
                self.assertNotIn("secret", text); self.assertNotIn("RUN COMPLETE", text)
                self.assertFalse((Path(out) / RUN.OUTPUT_NAME).exists())     # a STOP saves no report
                RUN.reports = old_reports
                code, text = self.run_main([str(d), RUN.RUN_FLAG], out)      # a full made-up run
                self.assertEqual(code, 0); self.assertTrue(text.rstrip().endswith("# RUN COMPLETE"))
                saved = (Path(out) / RUN.OUTPUT_NAME).read_text()
                self.assertEqual(saved, text)                                # what is printed is what is saved
                self.assertTrue(saved.startswith("# plan v37 run, started 20"))
                for f in RUN.CODE_FILES:
                    self.assertIn(f + " " + RUN.sha256(RUN.HERE / f), saved)
                self.assertFalse((Path(out) / (RUN.OUTPUT_NAME + ".tmp")).exists())
                code, text = self.run_main([str(d), RUN.RUN_FLAG], out)      # a second run is refused
                self.assertEqual(code, 1); self.assertIn("already exists", text); self.assertNotIn("near_50", text)
                log = (Path(out) / RUN.ATTEMPTS_NAME).read_text().splitlines()
                self.assertEqual(len(log), 6)                                # a start line and an end line each
                self.assertEqual([ln.split("\t")[1] for ln in log[0::2]], ["STARTED"] * 3)
                self.assertIn("unexpected ValueError", log[1]); self.assertTrue(log[3].endswith("COMPLETE"))
                self.assertIn("already exists", log[5])
            finally:
                RUN.EXPECTED_SHA256, RUN.reports = old, old_reports

    def test_a_report_that_cannot_be_saved_is_not_printed(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
            d = Path(tmp); cleaned_files(d); raw_file(d)
            ok = {n: hashlib.sha256((d / n).read_bytes()).hexdigest() for n in RUN.EXPECTED_SHA256}
            (Path(out) / (RUN.OUTPUT_NAME + ".tmp")).mkdir()                 # a folder in the way: the save fails
            old = RUN.EXPECTED_SHA256
            try:
                RUN.EXPECTED_SHA256 = ok
                code, text = self.run_main([str(d), RUN.RUN_FLAG], out)
            finally:
                RUN.EXPECTED_SHA256 = old
            self.assertEqual(code, 1); self.assertTrue(text.startswith("STOP: the report could not be saved"))
            self.assertNotIn("near_50", text); self.assertNotIn("RUN COMPLETE", text)
            self.assertFalse((Path(out) / RUN.OUTPUT_NAME).exists())
            log = (Path(out) / RUN.ATTEMPTS_NAME).read_text().splitlines()
            self.assertEqual(len(log), 2); self.assertIn("could not be saved", log[1])

    def test_a_log_that_cannot_be_started_means_nothing_is_read(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
            d = Path(tmp); cleaned_files(d); raw_file(d)
            (Path(out) / RUN.ATTEMPTS_NAME).mkdir()                          # a folder in the way: no line can be added
            called, old = [], RUN.check_hashes
            try:
                RUN.check_hashes = lambda *a, **k: called.append(1)
                code, text = self.run_main([str(d), RUN.RUN_FLAG], out)
            finally:
                RUN.check_hashes = old
            self.assertEqual(code, 1); self.assertEqual(called, [])          # stopped before the hash check
            self.assertTrue(text.startswith("STOP: the attempts log could not be written, so nothing was read."))
            self.assertEqual(len(text.splitlines()), 1); self.assertFalse((Path(out) / RUN.OUTPUT_NAME).exists())

    def test_a_log_or_hash_failure_later_never_hides_the_stop_line_or_the_report(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
            d = Path(tmp); cleaned_files(d); raw_file(d)
            ok = {n: hashlib.sha256((d / n).read_bytes()).hexdigest() for n in RUN.EXPECTED_SHA256}
            old = RUN.EXPECTED_SHA256, RUN._log, RUN.CODE_FILES, RUN.reports
            try:
                RUN.EXPECTED_SHA256 = ok
                RUN.CODE_FILES = ("no_such_file.py",)                        # hashing the code fails
                code, text = self.run_main([str(d), RUN.RUN_FLAG], out)
                self.assertEqual(code, 1); self.assertTrue(text.startswith("STOP: unexpected FileNotFoundError"))
                self.assertEqual(len(text.splitlines()), 1); self.assertNotIn("no_such_file", text)
                self.assertFalse((Path(out) / RUN.OUTPUT_NAME).exists())
                RUN.CODE_FILES = old[2]
                RUN._log = lambda out_dir, stamp, outcome: outcome == "STARTED"      # every later log write fails

                def boom(folder):
                    raise ValueError("secret value 50")
                RUN.reports = boom
                code, text = self.run_main([str(d), RUN.RUN_FLAG], out)
                self.assertEqual(code, 1); self.assertTrue(text.startswith("STOP: unexpected ValueError"))
                self.assertTrue(text.rstrip().endswith(RUN.NO_LOG.strip())); self.assertNotIn("secret", text)
                self.assertEqual(len(text.splitlines()), 1); self.assertFalse((Path(out) / RUN.OUTPUT_NAME).exists())
                RUN.reports = old[3]
                code, text = self.run_main([str(d), RUN.RUN_FLAG], out)      # a full made-up run, ending line fails
                saved = (Path(out) / RUN.OUTPUT_NAME).read_text()
                self.assertEqual(code, 0); self.assertTrue(text.startswith(saved))   # saved, and printed in full
                self.assertTrue(saved.rstrip().endswith("# RUN COMPLETE"))
                self.assertEqual(text[len(saved):].strip(),
                                 "# NOTE:" + RUN.NO_LOG + " The saved report is the record of this completed run.")
            finally:
                RUN.EXPECTED_SHA256, RUN._log, RUN.CODE_FILES, RUN.reports = old

    def test_a_screen_that_cannot_be_written_to_never_raises(self):
        class Broken:
            def write(self, text):
                raise OSError("closed")

            def flush(self):
                pass
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
            d = Path(tmp); cleaned_files(d); raw_file(d)
            with contextlib.redirect_stdout(Broken()):
                self.assertEqual(RUN.main([str(d)], out), 2)                 # no flag
                self.assertEqual(RUN.main([str(d), RUN.RUN_FLAG], out), 1)   # flag, made-up files: hash check stops
            self.assertFalse((Path(out) / RUN.OUTPUT_NAME).exists())

    def test_report_on_made_up_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp); cleaned_files(d); raw_file(d)
            out = RUN.reports(d)
            self.assertEqual(out.count("## SAMPLE"), 4)
            self.assertEqual(out.count("PRIMARY >>"), 1)
            self.assertLess(out.index("PRIMARY >>"), out.index("## SAMPLE 2"))
            for pid in ("s1", "p1", "p99"):
                self.assertNotIn(pid, out)                                   # no person ID in the printout
            self.assertIn("people_left_out_for_touch_events: 1", out)
            self.assertIn("(no eligible respondents)", out)


if __name__ == "__main__":
    unittest.main()
```

## Appendix G. `preliminary_checks_2026-11-22/structure_check_2.py.txt`

```python
# Run once on 22 November 2026 by an AI assistant (Claude), from inside the cloned repository folder.
# STRUCTURE ONLY: which event types carry a typed-answer field, and how many people have each kind of event.
# Prints event names, node-id codes and counts of people. No answer value, no ID, no duration, no timestamp.
import csv, collections
for fn in ("w2_prob_aitor.csv",):
    ev_rows=collections.Counter(); ev_ans=collections.Counter(); sid_ans=set(); sid_submit=set(); sid_hover=set(); sids=set()
    nodes=set(); ts_ok=True; ans_events_per_sid=collections.Counter()
    with open(fn,newline='',encoding='utf-8',errors='replace') as fh:
        rd=csv.DictReader(fh)
        for r in rd:
            s=r['sid']; sids.add(s); e=r['event']; ev_rows[e]+=1; nodes.add(r['node/id'])
            if (r.get('formInputs/ans1') or '').strip()!='':
                ev_ans[e]+=1; sid_ans.add(s); ans_events_per_sid[s]+=1
            if e=='submit': sid_submit.add(s)
            if e=='mouseover' and r['node/id'].startswith(('study-button-node','study-node-')): sid_hover.add(s)
            try: float(r['timestampms'])
            except ValueError: ts_ok=False
    print(fn, "people (sid):", len(sids))
    print(" event types carrying a non-empty formInputs/ans1 (rows):", dict(ev_ans))
    print(" people with at least one such row:", len(sid_ans), "| people with exactly one:", sum(1 for v in ans_events_per_sid.values() if v==1))
    print(" people with a submit event:", len(sid_submit), "| with a mouseover on a study node:", len(sid_hover), "| with both:", len(sid_submit&sid_hover))
    print(" people with an answer field but no hover:", len(sid_ans-sid_hover), "| hover but no answer field:", len(sid_hover-sid_ans))
    print(" all timestamps numeric:", ts_ok)
    print(" node/id codes:", sorted(nodes))

# OUTPUT, complete:
# w2_prob_aitor.csv people (sid): 172
#  event types carrying a non-empty formInputs/ans1 (rows): {'submit': 148}
#  people with at least one such row: 148 | people with exactly one: 148
#  people with a submit event: 149 | with a mouseover on a study node: 157 | with both: 138
#  people with an answer field but no hover: 11 | hover but no answer field: 20
#  all timestamps numeric: True
#  node/id codes: ['', 'ans1', 'line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'pageJumboHeader', 'question-node-inner', 'study-button-node1', 'study-button-node2', 'study-button-node3', 'study-button-node4', 'study-button-node5', 'study-button-node6', 'study-button-node7', 'study-node-1', 'study-node-2', 'study-node-3', 'study-node-4', 'study-node-5', 'study-node-6', 'study-node-7', 'tree-container', 'tree-question-node', 'tree-submit-button']
```

## Appendix H. `preliminary_checks_2026-11-22/loader_check.py.txt`

```python
# Run once on 22 November 2026 by an AI assistant (Claude), from exploratory/kept_ideas/v37/, with the adapter
# version saved beside this file (v37_adapter_as_run_in_loader_check.py.txt, SHA-256 starting d9b4e807).
# LOADER CHECK ONLY: sample sizes and row counts. No answer group, no split, no answer value is computed or printed.
# Note: the adapter did read every answer and hover into memory to produce these counts.
import v37_adapter as A
F='../../../data/realdata/reani_hover/repo'
for name, fin in (("final", True), ("cleaned", False)):
    a, r, lg, n = A.cleaned(F, final_only=fin)
    print(name, n, "| people with at least one hover row:", len({p for p,_,_ in r}))
a, r, lg, n, touch = A.raw(F)
print("raw", n)

# OUTPUT, complete:
# final {'people': 94, 'rows_without_an_answer': 0, 'people_in_cleaned_set': 98, 'hover_rows_of_these_people_in_another_condition': 0, 'hover_rows_with_an_unknown_button_code': 0, 'hover_rows_with_no_duration': 0, 'final_people_missing_from_cleaned_file': 0} | people with at least one hover row: 94
# cleaned {'people': 98, 'rows_without_an_answer': 0, 'people_in_cleaned_set': 98, 'hover_rows_of_these_people_in_another_condition': 0, 'hover_rows_with_an_unknown_button_code': 0, 'hover_rows_with_no_duration': 0} | people with at least one hover row: 98
# raw {'people_in_the_log': 172, 'people': 148, 'people_in_the_log_without_an_answer': 24, 'people_with_an_answer_and_no_reveal_at_all': 11, 'people_with_touch_events': 16}
```

## Appendix I. `preliminary_checks_2026-11-22/v37_adapter_as_run_in_loader_check.py.txt`

```python
"""Plan v37 (DRAFT): readers for the Reani et al. (2019) files. TESTED ON MADE-UP FILES ONLY (test_v37_adapter.py).
Column names and codes are from stage 0 (stage0_structure.txt, stage0_scripts_notes.md); no data row was opened.

Three samples, all Study 2 ("wave 2"), probability format (10% / 50% / 27% for everyone):
  final     the authors' final analysis set: people in scanDF2.csv                     (primary)
  cleaned   the authors' cleaned set before their last rule: people in analysis_scanpath.csv
  raw       everyone in the raw mouse log w2_prob_aitor.csv who submitted an answer; no exclusion by anyone

final / cleaned
  answers   analysis_scanpath.csv: Ps, Wave == 2, numerical_format == "probability", answer1 (a percentage)
            (scanDF2.csv's Given_answer is NOT used: the authors overwrite it for people they scored correct)
  reveals   analysis_duration.csv: sid (= Ps), node.id in A..H, duration in ms (the authors' own cleaning)
raw
  answer    the value of formInputs/ans1 on the person's last event that carries one (stage 0: only "submit"
            events carry it). People with none are counted and left out.
  reveals   mouseover events on study-button-nodeK or study-node-K, at or before that answer event. A reveal of K
            starts at such a mouseover and ends at the first later mouseover or mouseout on anything that is not K
            (or at the answer event). Consecutive events on K are one reveal.
  touch     whether the person has any mobileTouchStart / mobileTouchEnd event (hovering may not be logged there).

Which number each button shows, from the study page's own HTML (seen in stage 0): node 1 the total (100%),
node 2 "Fire" (10%), node 3 "No fire" (90%), node 4 "Alarm" under fire (50%), node 5 "No alarm" under fire (50%),
node 6 "Alarm" under no fire (27%), node 7 "No alarm" under no fire (73%). The authors' letters A..G are nodes 1..7
and H is the question (cleanAITORdata.R:66-83).
"""
import csv
from fractions import Fraction as Q
from pathlib import Path

NODE = {1: "T", 2: "F", 3: "nF", 4: "FA", 5: "FnA", 6: "nFA", 7: "nFnA"}
LETTER = {"A": "T", "B": "F", "C": "nF", "D": "FA", "E": "FnA", "F": "nFA", "G": "nFnA", "H": "Q"}
RAW_IDS = {**{f"study-button-node{k}": v for k, v in NODE.items()}, **{f"study-node-{k}": v for k, v in NODE.items()},
           "question-node-inner": "Q", "tree-question-node": "Q"}
HOVER_EVENTS = ("mouseover", "mouseout")
TOUCH_EVENTS = ("mobileTouchStart", "mobileTouchEnd")
WAVE, FORMAT, FORMAT_SHORT = 2, "probability", "prob"


def _rows(path):
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        yield from csv.DictReader(fh)


def _num(x):
    x = (x or "").strip()
    if x in ("", "NA", "NaN", "null"):
        return None
    try:
        return Q(x)
    except (ValueError, ZeroDivisionError):
        return Q(float(x))


def _is_wave2_prob(r):
    w = _num(r.get("Wave"))
    return w == WAVE and (r.get("numerical_format") or "").strip().lower() == FORMAT


def cleaned(folder, final_only):
    """→ (answers {pid: percent}, reveals [(pid, location, ms or None)], logged set, notes dict)."""
    folder = Path(folder)
    people, no_answer = {}, 0
    for r in _rows(folder / "analysis_scanpath.csv"):
        if _is_wave2_prob(r):
            a = _num(r.get("answer1"))
            if a is None:
                no_answer += 1
            else:
                people[r["Ps"]] = a
    if not people:
        raise SystemExit("analysis_scanpath.csv: no Study 2 probability rows (column names or codes differ)")
    in_cleaned = len(people)
    if final_only:
        keep = {r["Ps"] for r in _rows(folder / "scanDF2.csv") if _is_wave2_prob(r)}
        if not keep:
            raise SystemExit("scanDF2.csv: no Study 2 probability rows (column names or codes differ)")
        missing = len(keep - set(people))
        people = {p: a for p, a in people.items() if p in keep}
    reveals, other_condition, unknown_code = [], 0, 0
    for r in _rows(folder / "analysis_duration.csv"):
        if r["sid"] not in people:
            continue
        if _num(r.get("wave")) != WAVE or (r.get("n_format") or "").strip().lower() != FORMAT_SHORT:
            other_condition += 1
            continue
        loc = LETTER.get((r.get("node.id") or "").strip())
        if loc is None:
            unknown_code += 1
            continue
        d = _num(r.get("duration"))
        reveals.append((r["sid"], loc, None if d is None else float(d)))
    notes = {"people": len(people), "rows_without_an_answer": no_answer, "people_in_cleaned_set": in_cleaned,
             "hover_rows_of_these_people_in_another_condition": other_condition,
             "hover_rows_with_an_unknown_button_code": unknown_code,
             "hover_rows_with_no_duration": sum(d is None for _, _, d in reveals)}
    if final_only:
        notes["final_people_missing_from_cleaned_file"] = missing
    return people, reveals, set(), notes


def _raw_reveals(events, cutoff):
    """events: [(t, event, location or None)] in time order, up to the answer event. → [(location, ms)]."""
    out, cur, start, pending = [], None, None, None

    def close(t_end):
        nonlocal cur, start, pending
        if cur is not None:
            end = pending if pending is not None else t_end
            out.append((cur, float(end - start)))
        cur, start, pending = None, None, None

    for t, ev, loc in events:
        if ev not in HOVER_EVENTS:
            continue
        number = loc if loc not in (None, "Q") else None
        if cur is not None and number == cur:
            pending = t if ev == "mouseout" else None          # still on K: a mouseout may be followed by K again
            continue
        close(t)                                               # an event on something that is not K ends the reveal
        if ev == "mouseover" and number is not None:
            cur, start, pending = number, t, None
    close(cutoff)
    return out


def raw(folder):
    """→ (answers, reveals, logged, notes, touch set). Everyone in w2_prob_aitor.csv with an answer in the log."""
    by = {}
    for i, r in enumerate(_rows(Path(folder) / "w2_prob_aitor.csv")):
        t = _num(r.get("timestampms"))
        if t is None:
            continue
        by.setdefault(r["sid"], []).append((t, i, r["event"], RAW_IDS.get((r.get("node/id") or "").strip()),
                                           _num(r.get("formInputs/ans1"))))
    if not by:
        raise SystemExit("w2_prob_aitor.csv: no rows")
    answers, reveals, touch = {}, [], set()
    for sid, evs in by.items():
        evs.sort(key=lambda e: (e[0], e[1]))
        with_answer = [e for e in evs if e[4] is not None]
        if not with_answer:
            continue
        cutoff = with_answer[-1][0]
        answers[sid] = with_answer[-1][4]
        if any(e[2] in TOUCH_EVENTS for e in evs):
            touch.add(sid)
        for loc, ms in _raw_reveals([(t, ev, loc) for t, _, ev, loc, _ in evs if t <= cutoff], cutoff):
            reveals.append((sid, loc, ms))
    with_reveal = {p for p, _, _ in reveals}
    notes = {"people_in_the_log": len(by), "people": len(answers),
             "people_in_the_log_without_an_answer": len(by) - len(answers),
             "people_with_an_answer_and_no_reveal_at_all": len(set(answers) - with_reveal),
             "people_with_touch_events": len(touch)}
    return answers, reveals, set(answers), notes, touch
```

## Appendix J. `v37_structure.py`

```python
"""Plan v37, STAGE 0: structure check of the Reani et al. (2019) hover data. Run BEFORE the plan is published.

  python3 v37_structure.py <folder with the cloned repository>

Prints ONLY structure: file names and sizes; for each CSV its column names, row count, and the number of distinct
values per column. For text columns with at most 30 distinct values it also prints the distinct values (these are
codes such as button names), EXCEPT columns whose name suggests an answer, a score, a person identifier, page text,
typed keys or a time (22 Nov: page-text and key columns added after stage 0 printed the study page's wording). It never prints a row, an
answer value, a duration, or a count per value. It also reports, for every pair of CSV files, which column names they
share and how many values of each shared low-cardinality-free id-like column overlap.
"""
import csv
import re
import sys
from pathlib import Path

HIDE = re.compile(r"answer|resp|estim|guess|numer|denom|result|correct|score|value|input|prob|freq"
                  r"|text|content|key|offset|coord|scanpath|codex|date|time", re.I)
IDLIKE = re.compile(r"(^|_)(id|sid|pid|user|participant|subject|worker|session|episode)", re.I)
MAX_SHOW = 30


def scan(path):
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        rd = csv.reader(fh)
        try:
            header = next(rd)
        except StopIteration:
            return None
        sets = [set() for _ in header]
        numeric = [True] * len(header)
        n = 0
        for row in rd:
            n += 1
            for i, v in enumerate(row[:len(header)]):
                if len(sets[i]) <= 200000:
                    sets[i].add(v)
                if numeric[i] and v not in ("", "NA"):
                    try:
                        float(v)
                    except ValueError:
                        numeric[i] = False
    return header, n, sets, numeric


def main(folder):
    folder = Path(folder)
    files = sorted(p for p in folder.iterdir() if p.is_file())
    print("FILES")
    for p in files:
        print(f"  {p.name}  {p.stat().st_size} bytes")
    idsets = {}
    for p in files:
        if p.suffix.lower() != ".csv":
            continue
        r = scan(p)
        if r is None:
            print(f"\n{p.name}: empty"); continue
        header, n, sets, numeric = r
        print(f"\n{p.name}: {n} rows, {len(header)} columns")
        for name, s, num in zip(header, sets, numeric):
            line = f"  {name!r}: {'number' if num else 'text'}, {len(s)} distinct"
            if not num and len(s) <= MAX_SHOW and not HIDE.search(name) and not IDLIKE.search(name):
                line += " -> " + ", ".join(" ".join(v.split())[:60] for v in sorted(s))     # one line, short
            print(line)
            if IDLIKE.search(name):
                idsets[(p.name, name)] = s
    print("\nID-LIKE COLUMNS: overlap of distinct values between files")
    keys = sorted(idsets)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if a[0] != b[0]:
                both = len(idsets[a] & idsets[b])
                if both:
                    print(f"  {a[0]}[{a[1]}] ({len(idsets[a])}) & {b[0]}[{b[1]}] ({len(idsets[b])}): {both} shared")


if __name__ == "__main__":
    main(sys.argv[1])
```

## Appendix K. `preliminary_checks_2026-11-22/v37_structure_as_run_in_stage0.py.txt`

```python
"""Plan v37, STAGE 0: structure check of the Reani et al. (2019) hover data. Run BEFORE the plan is published.

  python3 v37_structure.py <folder with the cloned repository>

Prints ONLY structure: file names and sizes; for each CSV its column names, row count, and the number of distinct
values per column. For text columns with at most 30 distinct values it also prints the distinct values (these are
codes such as button names), EXCEPT columns whose name suggests an answer, a score or a person identifier. It never prints a row, an
answer value, a duration, or a count per value. It also reports, for every pair of CSV files, which column names they
share and how many values of each shared low-cardinality-free id-like column overlap.
"""
import csv
import re
import sys
from pathlib import Path

HIDE = re.compile(r"answer|resp|estim|guess|numer|denom|result|correct|score|value|input|prob|freq", re.I)
IDLIKE = re.compile(r"(^|_)(id|sid|pid|user|participant|subject|worker|session|episode)", re.I)
MAX_SHOW = 30


def scan(path):
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        rd = csv.reader(fh)
        try:
            header = next(rd)
        except StopIteration:
            return None
        sets = [set() for _ in header]
        numeric = [True] * len(header)
        n = 0
        for row in rd:
            n += 1
            for i, v in enumerate(row[:len(header)]):
                if len(sets[i]) <= 200000:
                    sets[i].add(v)
                if numeric[i] and v not in ("", "NA"):
                    try:
                        float(v)
                    except ValueError:
                        numeric[i] = False
    return header, n, sets, numeric


def main(folder):
    folder = Path(folder)
    files = sorted(p for p in folder.iterdir() if p.is_file())
    print("FILES")
    for p in files:
        print(f"  {p.name}  {p.stat().st_size} bytes")
    idsets = {}
    for p in files:
        if p.suffix.lower() != ".csv":
            continue
        r = scan(p)
        if r is None:
            print(f"\n{p.name}: empty"); continue
        header, n, sets, numeric = r
        print(f"\n{p.name}: {n} rows, {len(header)} columns")
        for name, s, num in zip(header, sets, numeric):
            line = f"  {name!r}: {'number' if num else 'text'}, {len(s)} distinct"
            if not num and len(s) <= MAX_SHOW and not HIDE.search(name) and not IDLIKE.search(name):
                line += " -> " + ", ".join(sorted(s))
            print(line)
            if IDLIKE.search(name):
                idsets[(p.name, name)] = s
    print("\nID-LIKE COLUMNS: overlap of distinct values between files")
    keys = sorted(idsets)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if a[0] != b[0]:
                both = len(idsets[a] & idsets[b])
                if both:
                    print(f"  {a[0]}[{a[1]}] ({len(idsets[a])}) & {b[0]}[{b[1]}] ({len(idsets[b])}): {both} shared")


if __name__ == "__main__":
    main(sys.argv[1])
```

## Appendix L. `preliminary_checks_2026-11-22/stage0_structure_excerpt.txt`

```text
EXCERPT of the regenerated stage 0 printout (stage0_structure.txt, SHA-256 da6f069ccfe0bd7efeb8396ab0128a9616051567002f35844e36f1194a85b9bb).
Only the five Study 2 probability files this plan touches, and the ID-overlap lines between them. The full printout has
the same kind of lines for 24 other CSV files.

analysis_duration.csv: 10036 rows, 7 columns
  'event': text, 1 distinct -> mouseover
  'timestampms': number, 10036 distinct
  'sid': text, 360 distinct
  'node.id': text, 8 distinct -> A, B, C, D, E, F, G, H
  'n_format': text, 2 distinct -> freq, prob
  'wave': number, 2 distinct
  'duration': number, 3654 distinct

analysis_scanpath.csv: 360 rows, 44 columns
  'Ps': text, 360 distinct
  'Scanpath': text, 359 distinct
  'Scanpath_complex': text, 360 distinct
  'id': number, 154 distinct
  'PID': number, 143 distinct
  'date.time': number, 360 distinct
  'age': number, 49 distinct
  'gender': text, 2 distinct -> f, m
  'education': number, 4 distinct
  'alarm': number, 5 distinct
  'fire': number, 5 distinct
  'fractions': number, 6 distinct
  'percent': number, 6 distinct
  'tip': number, 6 distinct
  'shirt': number, 6 distinct
  'newspaper': number, 6 distinct
  'prob1': number, 6 distinct
  'prob2': number, 6 distinct
  'howoften': number, 6 distinct
  'input1': number, 35 distinct
  'input2': number, 56 distinct
  'input3': number, 54 distinct
  'input4': number, 22 distinct
  'input5': number, 37 distinct
  'input6': number, 27 distinct
  'sub_n1': number, 21 distinct
  'sub_n2': number, 15 distinct
  'numeracy': number, 29 distinct
  'baserate': number, 51 distinct
  'baserate_avg': number, 2 distinct
  'true_positive': number, 60 distinct
  'true_positive_avg': number, 2 distinct
  'false_alarm': number, 62 distinct
  'false_alarm_avg': number, 2 distinct
  'correct_answer': number, 112 distinct
  'given_answer': number, 47 distinct
  'numerical_format': text, 2 distinct
  'condition': number, 2 distinct
  'correctness': number, 2 distinct
  'bias_error': number, 152 distinct
  'answer1': number, 61 distinct
  'answer2': number, 35 distinct
  'amazon_codex': text, 360 distinct
  'Wave': number, 2 distinct

scanDF2.csv: 342 rows, 23 columns
  'Ps': text, 342 distinct
  'Scanpath': text, 341 distinct
  'Scanpath_complex': text, 342 distinct
  'age': number, 48 distinct
  'gender': text, 2 distinct -> f, m
  'alarm': number, 5 distinct
  'fire': number, 5 distinct
  'numeracy': number, 29 distinct
  'baserate': number, 48 distinct
  'baserate_avg': number, 2 distinct
  'true_positive': number, 56 distinct
  'true_positive_avg': number, 2 distinct
  'false_alarm': number, 57 distinct
  'false_alarm_avg': number, 2 distinct
  'numerical_format': text, 2 distinct
  'correctness': text, 2 distinct
  'Wave': number, 2 distinct
  'Correct_answer': number, 107 distinct
  'Given_answer': number, 59 distinct
  'Correct_answer_belief': number, 179 distinct
  'Bias_GC': number, 139 distinct
  'Bias_belief': number, 118 distinct
  'Numeracy_cat': text, 3 distinct

w2_prob_aitor.csv: 38974 rows, 55 columns
  '_id/$oid': text, 38974 distinct
  'event': text, 20 distinct -> change, contextmenu, dblclick, keydown, keypress, keyup, load, mobileTouchEnd, mobileTouchStart, mousedown, mouseout, mouseover, mouseup, mousewheel, scroll, select, selectextra, submit, windowqueryblur, windowqueryfocus
  'screen/sizeWidth': number, 57 distinct
  'screen/sizeHeight': number, 104 distinct
  'screen/resolutionWidth': number, 26 distinct
  'screen/resolutionHeight': number, 28 distinct
  'screen/htmlSizeWidth': number, 68 distinct
  'screen/htmlSizeHeight': number, 93 distinct
  'screen/usableSizeWidth': number, 65 distinct
  'screen/usableSizeHeight': number, 93 distinct
  'client/appName': text, 4 distinct -> , Chrome, Firefox, Safari
  'client/version': number, 21 distinct
  'client/platform': text, 10 distinct -> , Linux armv7l, Linux armv8l, Linux i686, Linux x86_64, MacIntel, Win32, Win64, iPad, iPhone
  'client/os': text, 7 distinct -> , Linux, Mac/iOS, UNIX, Windows 10, Windows 7, Windows XP
  'episodeCount': number, 8 distinct
  'timestampms': number, 32347 distinct
  'sessionstartms': number, 174 distinct
  'timezoneOffset': number, 10 distinct
  'sid': text, 172 distinct
  'url': text, 1 distinct -> http://www.when2go-study.co.uk/show_tree
  'urlFull': text, 1 distinct -> http://www.when2go-study.co.uk/show_tree
  'mouse/coordX': number, 1390 distinct
  'mouse/coordY': number, 1028 distinct
  'mouse/offsetX': number, 1500 distinct
  'mouse/offsetY': number, 1039 distinct
  'node/dom': text, 59 distinct
  'node/id': text, 27 distinct -> , ans1, line1, line2, line3, line4, line5, line6, pageJumboHeader, question-node-inner, study-button-node1, study-button-node2, study-button-node3, study-button-node4, study-button-node5, study-button-node6, study-button-node7, study-node-1, study-node-2, study-node-3, study-node-4, study-node-5, study-node-6, study-node-7, tree-container, tree-question-node, tree-submit-button
  'node/inheritedId': text, 3 distinct -> , False, True
  'node/class/0': text, 11 distinct -> , btn, container, gr__when2go-study_co_uk, jumbotron, primary-title, row, study-button-inner, study-button-number, study-button-question, tree-line
  'node/type': text, 13 distinct -> , BODY, DIV, FONT, FOOTER, FORM, H3, HR, HTML, INPUT, LABEL, P, TD
  'node/textContent': text, 26 distinct
  'mouse/but': text, 3 distinct -> , l, r
  'delta': text, 2 distinct -> , False
  'scrolly': number, 67 distinct
  'node/name': text, 3 distinct -> , answer1, next
  'node/class/1': text, 3 distinct -> , btn-primary, hasGoogleVoiceExt
  'node/class/2': text, 2 distinct -> , nextButton
  'node/textValue': text, 280 distinct
  'key': text, 30 distinct
  'type': text, 2 distinct -> , number
  'formInputs/ans1': number, 30 distinct
  'formInputs/tree-submit-button': text, 3 distinct
  'selectionTool': text, 3 distinct -> , mouse, touch
  'selectedContent': text, 22 distinct
  'coord': number, 25 distinct
  'offset': text, 25 distinct
  'but': text, 2 distinct -> , l
  'client/name': text, 3 distinct -> , Edge, Opera
  'mobileTouch/numberOfTouches': number, 4 distinct
  'mobileTouch/isCtrlKey': text, 2 distinct
  'mobileTouch/isShiftKey': text, 2 distinct
  'mobileTouch/isAltKey': text, 2 distinct
  'mobileTouch/isMetaKey': text, 2 distinct
  'scrollx': number, 92 distinct
  'formInputs/undefined': number, 1 distinct

w2_prob_alan.csv: 172 rows, 41 columns
  'id': number, 172 distinct
  'PID': number, 132 distinct
  'ucivit_id': text, 39 distinct
  'date/time': text, 172 distinct
  'age': number, 42 distinct
  'gender': text, 2 distinct -> f, m
  'education': number, 4 distinct
  'alarm': number, 5 distinct
  'fire': number, 5 distinct
  'fractions': number, 6 distinct
  'percent': number, 6 distinct
  'tip': number, 6 distinct
  'shirt': number, 6 distinct
  'newspaper': number, 6 distinct
  'prob1': number, 6 distinct
  'prob2': number, 6 distinct
  'howoften': number, 5 distinct
  'input1': number, 37 distinct
  'input2': number, 47 distinct
  'input3': number, 41 distinct
  'input4': number, 1 distinct
  'input5': number, 1 distinct
  'input6': number, 1 distinct
  'sub_n1': number, 21 distinct
  'sub_n2': number, 13 distinct
  'numeracy': number, 29 distinct
  'baserate': number, 36 distinct
  'baserate_avg': number, 1 distinct
  'true_positive': number, 45 distinct
  'true_positive_avg': number, 1 distinct
  'false_alarm': number, 40 distinct
  'false_alarm_avg': number, 1 distinct
  'correct_answer': number, 1 distinct
  'given_answer': number, 31 distinct
  'numerical_format': text, 1 distinct
  'condition': number, 1 distinct
  'correctness': number, 2 distinct
  'bias_error': number, 31 distinct
  'answer1': number, 31 distinct
  'answer2': number, 1 distinct
  'amazon_codex': text, 172 distinct

ID-LIKE COLUMNS: overlap of distinct values between these files
  analysis_duration.csv[sid] (360) & w2_prob_aitor.csv[sid] (172): 102 shared
  analysis_duration.csv[sid] (360) & w2_prob_alan.csv[ucivit_id] (39): 14 shared
  analysis_scanpath.csv[PID] (143) & w2_prob_aitor.csv[episodeCount] (8): 7 shared
  analysis_scanpath.csv[PID] (143) & w2_prob_alan.csv[PID] (132): 115 shared
  analysis_scanpath.csv[PID] (143) & w2_prob_alan.csv[id] (172): 143 shared
  analysis_scanpath.csv[id] (154) & w2_prob_aitor.csv[episodeCount] (8): 7 shared
  analysis_scanpath.csv[id] (154) & w2_prob_alan.csv[PID] (132): 117 shared
  analysis_scanpath.csv[id] (154) & w2_prob_alan.csv[id] (172): 154 shared
  w2_prob_aitor.csv[episodeCount] (8) & w2_prob_alan.csv[PID] (132): 5 shared
  w2_prob_aitor.csv[episodeCount] (8) & w2_prob_alan.csv[id] (172): 8 shared
  w2_prob_aitor.csv[sid] (172) & w2_prob_alan.csv[ucivit_id] (39): 37 shared
```
