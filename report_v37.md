# Report v37: same answer, was there a recorded hover on the base rate? (Reani et al. 2019 hover data)

**Plan:** v37 (tag v37, `prereg_v37.md`, SHA-256 `83f7949eeaf6524dea2add9f8f8e0789a938f7ccc197e0b038867cc5a254d7c7`), published on 22 November 2026 at 09:44:07 UTC. **Addendum v37.1** (tag v37.1, the forecast and four disclosures) was published at 10:02:54 UTC.

**Run once** on 22 November 2026 at 10:03:02 UTC, on macOS with Python 3.14.7. The code was `v37_run.py` with `v37_adapter.py` and `v37_hover.py`, whose hashes are in the output's first lines and match plan section 9. Exit status 0.

**Data.** Reani, Davies, Peek & Jay (2019), Frontiers in Psychology 10:1548. The repository is `manurea/mouse-interaction-bayesian-reasoning` at commit `bc8d0689a76b97664251a9a65ff080d47049ad8c`. It has no licence. The files stayed on the team lead's computer, nothing from them is redistributed, and this report gives counts only.

**Sources of the numbers.** Every number below is copied from the run's output, published unchanged as `report_v37_output.txt`, except where marked "derived", which means arithmetic on printed counts. The attempts log is published as `report_v37_attempts.log`. It holds one STARTED line and one COMPLETE line.

## 1. Primary result (plan section 5)

Sample 1 is the authors' final sample. The row is people with an answer from 49% to 51%, counting any recorded hover:

| N | NEITHER | BASE_ONLY | FIFTY_ONLY | BOTH | No base-rate hover |
|---|---|---|---|---|---|
| 48 | 0 | 0 | 0 | 48 | **0 of 48 (0.0%, 95% interval 0.0 to 7.4)** |

**The plan's allowed sentence, filled in:**

> "In Reani et al.'s Study 2 (percentage format; the authors' final sample and their cleaned hover file; any recorded hover), 48 people with a hover log gave an answer from 49% to 51%. 0 of them (0.0%, 95% interval 0.0 to 7.4) had no recorded hover on either base-rate button (NEITHER 0, FIFTY_ONLY 0). The other 48 had at least one (BASE_ONLY 0, BOTH 48). A recorded hover is a logged mouse event: it does not show that a number was read or used, and a missing one does not show why."

It may be followed by: "50% is printed on two buttons, alarm given fire and no alarm given fire, and is also a 50–50 guess."

## 2. Secondary rows, all reported (plan section 5)

"No base-rate hover" is NEITHER plus FIFTY_ONLY. Each cell gives that count out of N, for answers near 50% / near the correct 17% / all other answers.

| Sample | Any recorded hover | At least 250 ms | At least 500 ms |
|---|---|---|---|
| 1. The authors' final sample (94) | 0/48 · 0/2 · 0/44 | 0/48 · 0/2 · 0/44 | 1/48 · 0/2 · 1/44 |
| 2. The authors' cleaned set, before their last rule (98) | 0/49 · 0/2 · 0/47 | 0/49 · 0/2 · 0/47 | 1/49 · 0/2 · 1/47 |
| 3. The raw mouse log, none of the authors' exclusions (148 with an answer) | 5/67 · 0/2 · 15/79 | 9/67 · 0/2 · 20/79 | 14/67 · 0/2 · 27/79 |
| 3 without people with touch events (132) | 3/61 · 0/2 · 10/69 | 7/61 · 0/2 · 15/69 | 11/61 · 0/2 · 22/69 |

- **Sample 3 near 50%, any recorded hover:** NEITHER 2, BASE_ONLY 1, FIFTY_ONLY 3, BOTH 61. That is 5 of 67 (7.5%, 2.5 to 16.6) with no base-rate hover.
- **Sample 3 near 50%, at 500 ms:** 14 of 67 (20.9%, 11.9 to 32.6).
- Every class count, share and interval for each row is in the output.

**Which table governs (plan section 5).** The claim rests on the primary row alone, and every other row is a sensitivity check. **The samples disagree.**

- **In the authors' final and cleaned samples,** nobody who answered about 50% lacked a recorded base-rate hover, counting any recorded hover or hovers of at least 250 ms. At 500 ms, one person in each did: 1 of 48 and 1 of 49.
- **In the raw log, before the authors' exclusions,** some did: 5 of 67 counting any recorded hover, and more as the minimum hover length rises.
- **One known reason.** The paper's stated exclusions include people who answered without looking at the question, and people who hovered over fewer than two pieces of information other than the question (plan section 2). That rule favours people who hovered. Plan section 2 also notes that the samples differ in more than the exclusions, so a difference cannot be put down to them alone.

## 3. Dropped people and rows (plan section 5)

- **Sample 1:** 94 people, all in the cleaned file and all with a readable answer and a hover log. No hover row was dropped for another condition, a non-mouseover event, an unknown button code, or a missing, unreadable or negative duration.
- **Sample 2:** the same for all 98 people.
- **Sample 3:**
  - 172 people are in the log; 148 have an answer event and 24 do not;
  - no answer was unreadable, and nobody had more than one answer event;
  - 11 of the 148 had an answer and no hover on any number;
  - 16 had touch events, so the version without touch events has 132 people;
  - no row lacked a readable time.

## 4. The forecast (addendum v37.1)

Jay Singh's forecast, written before the run, beside the result. No score is computed, and the forecast decides nothing.

| | Forecast | Result (sample 1, any recorded hover) |
|---|---|---|
| People of the 94 with an answer from 49 to 51 | 70 | 48 |
| Of those: no hover on either kind of button (NEITHER) | 40% | 0 of 48 |
| A base-rate hover only (BASE_ONLY) | 40% | 0 of 48 |
| A 50% hover only (FIFTY_ONLY) | 10% | 0 of 48 |
| Both kinds (BOTH) | 10% | 48 of 48 |
| No base-rate hover (the primary row) | 50% (derived) | 0% |

- Addendum v37.1 (section 2.2) discloses that explanations Bhavik forwarded, some or all of them, said that many people wrongly answer 50%. Which of them Jay saw is not confirmed. If he saw that sentence, it may have raised his forecast of 70.
- Only one forecast was collected.

## 5. What this does not show (plan section 6)

- **A recorded hover is a logged mouse event.** It does not show that a number was read or used. A missing hover does not show why.
- **Hovering was not randomised.** So this says nothing about whether pointing a learner to the base rate would change the answer.
- **The final sample was selected by the authors' rules,** including one that favours people who hovered. The intervals treat the people in a row as a binomial sample, which they are not.
- **It is one problem,** drawn as a tree, with the numbers hidden under buttons. Hiding numbers may change how people read.
- **What was known before the run.** Plan section 7 lists three earlier looks at the files. They settled the sample sizes. They also settled that at least 11 of the 148 people in sample 3 had no hover on any number, over all answer groups together. That fact is not a prospective result.

## 6. Deviations

- **None in the run.** Every hash matched before the run, and it was made once.
- **Before the run,** addendum v37.1 disclosed four departures: one forecaster, not two; explanations given beyond the sheet; how the forecast was received; and a third pre-publish check that plan section 8 does not list.
- **Permission.** The authors' repository has no licence. Bhavik emailed the authors on 21 November 2026, and the team has no record of a reply as of this report. As plan section 2 says, the plan does not rely on a reply and claims no permission from the authors. Also as plan section 2 says: if the authors object at any time, the results are removed from our talk and materials, and a withdrawal note is published in this repository.

## 7. Files

| File | SHA-256 |
|---|---|
| `report_v37_output.txt` (the run's output, unchanged) | `9f1782d320a06be49a6b3fd9293a44b0ff174ef2dc93aa8c570ad0cabb8c1b3b` |
| `report_v37_attempts.log` (the attempts log, unchanged) | `bcced3ef7faf0b666efabdef7faa11a9e291039439ff931a074dec10dd8b4589` |
