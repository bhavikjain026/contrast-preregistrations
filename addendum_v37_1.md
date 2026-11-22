# Addendum v37.1 to plan v37: the forecast, written before the run, and four disclosures

Written on 22 November 2026. To be published under tag v37.1 **before** `v37_run.py` is run (plan v37, sections 5 and 8). Plan v37 (tag v37) is unchanged. Nobody has run `v37_run.py` with its flag, and no count of hover classes within answer groups exists yet.

## 1. The forecast

Jay Singh, a team member, filled in the forecast sheet of plan v37, Appendix A (`forecast_sheet_v37.txt`, SHA-256 `1e55897ee6e63664a7086b82e9184d5fbebdd65edc01b0d1b36ed9a21e386cd6`). His sheet is reproduced below as it was received. He dated it 22/11/2026, 3:26 PM IST (09:56 UTC). That is after tag v37 was pushed (09:44:07 UTC), and before any result.

| | Jay Singh's forecast |
|---|---|
| 1. People of the 94 with an answer from 49 to 51 | 70 |
| 2A. Of those: no hover on a 50% button and none on a base-rate button | 40% |
| 2B. A hover on a base-rate button, none on a 50% button | 40% |
| 2C. A hover on a 50% button, none on a base-rate button | 10% |
| 2D. A hover on a 50% button and on a base-rate button | 10% |
| 3. What he had already seen or heard about the study, its data or this plan | "Nothing" |

- **In the plan's terms**, 2A is NEITHER, 2B is BASE_ONLY, 2C is FIFTY_ONLY and 2D is BOTH.
- **The primary row of plan section 5** counts people with no base-rate hover, NEITHER plus FIFTY_ONLY. In this forecast that is 2A plus 2C, which is 50% (derived).
- **The saved sheet** is `forecast_v37_jay_singh.txt`, SHA-256 `f229713d9dab06553f7d397808b6d2cc217a38f81e10144c801d88e43f618a26`. It is kept in the team's private working repository, in `exploratory/v37_forecasts/`, beside a receipt log.
- **Report v37** will show this forecast beside the counts. No score is computed, and the forecast decides nothing.

## 2. Disclosures

**2.1 One forecaster, not two.** Plan section 5 names the forecasters as Kahan and Jay. Only Jay's forecast was collected before this addendum. Bhavik decided to go ahead without waiting for Kahan's, and a forecast written after the run would not count.

**2.2 The forecaster was given more than the sheet.** Plan section 5 says the forecasters "get the sheet in Appendix A and nothing else". The forecasters said they did not understand the sheet. The AI assistant that wrote the plan then wrote explanations, and Bhavik forwarded some or all of them:

- a note on how to fill in the sheet;
- a plain-words version of the sheet;
- a short message, and a step-by-step version of it;
- an explanation of the buttons, with a worked example over 1,000 days of how the correct answer, 17%, comes about.

None of them gave any count or result from the data. **One sentence in them goes beyond the sheet.** The plain-words version said "A wrong answer many people give is 50%", and the short message said "Lots of people wrongly answer 50%". The sheet itself says only that 50% is printed on two buttons and is a round number. From the shares the published paper reports, the author of the plan had worked out that about half of the people in Study 2 gave the hit-rate answer. These sentences may have moved the forecast for question 1 upward. Bhavik has not confirmed which of the explanations Jay saw.

**2.3 How the forecast was received.** Bhavik pasted Jay's sheet into the chat with the AI assistant that wrote the plan. That assistant saved it unchanged. It has seen the earlier looks listed in plan section 7, and it does not forecast.

**2.4 A third check before publication.** Plan section 8, step 3, describes two checks of the code by a second AI session. There was a third. It found that plan section 3, and the adapter's own docstring, listed five words meaning "missing", while the code treats seven as missing: "nan" and "NULL" as well. The code was not changed. Plan section 3 and the docstring were changed to list all seven, one test was extended, and the check was repeated before tag v37. So the published plan already carries the fix. This note completes the record of section 8, step 3.

## 3. The run

One run, as in plan section 8, step 5:

`python3 v37_run.py <folder with the cloned repository> --run-after-tag`

Everything in plan v37 applies unchanged: the samples, the thresholds, the hover rule, the primary row, the allowed sentence and the rules for a failed run.
