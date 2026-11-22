# Report v41: can each chatbot-written Bayes problem be fixed by changing one number?

**Plan:** v41 (tag v41, `prereg_v41.md`, SHA-256 `77c8cd579f083a351bc988786d142d5917cb26fd8298feca91b724ec60a409c6`), published on 22 November 2026 at 09:31:24 UTC, before the run. **Run once** on 22 November 2026, 09:31:31 to 09:31:37 UTC, with `v41.py` (SHA-256 `26738d145e856b1e37ac31015e474f9d52ff33b16cfd1630a8e21fa87a8081ae`), on macOS with Python 3.14.7. Exit status 0.

**Arithmetic only: no learners and no human data.** The number sets are the ones plan v23 locked (`extract_final.csv`, SHA-256 `bbeea3ea…08787a`). They come from one reply by each of three chatbots, asked once on 19 November 2026.

**Sources of the numbers.** Every number below is copied from the run's output, published unchanged as `report_v41_output.txt`, except where marked "derived", which means arithmetic on printed counts. No number set is printed, here or in the output.

## 1. Check against report v23

For each chatbot and arm, the run recomputed D, Q1, Q3 and v23's legacy count, and all six matched report v23. v22's collision check and v23's legacy check agreed on every set.

## 2. Primary result (plan section 3)

A collision is report v23's own measure: some whole-percent answer fits two wrong methods (Q1), or fits the correct answer and a wrong method (Q3). A fix changes one number by 1 to 40 whole points and leaves no Q1 and no Q3.

| Arm 1 (plain request) | Sets | With a collision | Fixable by changing one number | Smallest fix: median, largest | Fix of at most 10 points |
|---|---|---|---|---|---|
| ChatGPT | 20 | 18 | 10 | 19.5, 36 points | 2 |
| Gemini | 20 | 20 | 7 | 12, 37 points | 1 |
| Claude | 19 | 16 | 8 | 19, 34 points | 2 |
| **Sum of the three replies** | **59** | **54** | **25** | **19, 37 points** | **5** |

- **The sum is of three single replies.** It is not a sample, so it has no interval.
- **Fixes are rarely small.** Of the 54, 2 can be fixed by at most 5 points and 5 by at most 10 points. 29 cannot be fixed by changing one number by up to 40 points (derived: 54 − 25).
- **Which number fixes it.** Mostly the hit rate: 8 of ChatGPT's fixes, 7 of Gemini's and 7 of Claude's. The false-alarm rate gave 2 (ChatGPT), and the base rate 1 (Claude). Ties are counted for each.
- **A fix moves the correct answer.** At the first smallest fix, the median change was 5.73, 3.80 and 6.09 points, and the largest was 10.50, 12.11 and 11.67 points.

**The plan's slide sentence, with the run's numbers:**

> "Asked once on 19 November 2026, three chatbots wrote practice problems; in 54 of their 59 number sets, one typed answer could mean two different mistakes, or a mistake and the right answer. 25 of those 54 could be fixed by changing one number, by at most 37 points (median 19). Arithmetic, not tested on people. Told our rule, the same chatbots wrote 60 of 60 clean sets."

The last sentence is report v23's Arm 2 result, which this run re-checked: Q1, Q3 and the legacy count were 0 in all 60 Arm 2 sets.

## 3. Secondary: plan v22's check and search, unchanged

| Arm 1 | With a collision (v20's measure) | Fixable (v22's success test) | Smallest fix: median, largest |
|---|---|---|---|
| ChatGPT | 18 | 13 | 17, 36 points |
| Gemini | 20 | 11 | 19, 40 points |
| Claude | 15 | 7 | 16, 27 points |

- **Derived:** 31 of 53 by v22's test, against 25 of 54 by v23's.
- **The two counts differ because v22's test is weaker.** It looks only at each wrong method's own typed answer, so a set it counts as fixed can still have a whole-percent answer that fits two methods. This is why plan v41 uses v23's measures as primary.

## 4. The forecast

Plan section 4 forecast about 28 fixable sets, with 15 to 40 expected. The result was 25, inside that range. The forecast did not say how large the fixes would be.

## 5. What this does not show (plan section 5)

- **Only the tutor's six wrong methods and its 1-point window** are covered, with answers typed as whole percents.
- **A fix changes the problem and its correct answer.** It says nothing about the wording, or about whether the original problem was a bad teaching choice.
- **No students are involved.** A fix is a property of the numbers, not evidence that students would then be diagnosed correctly.
- **Only one number at a time**, in whole-point steps, is searched.
- **One reply per chatbot**, asked once.

## 6. Deviations

None. Every input hash matched the plan before the run, and the run was made once.

## 7. Notes on wording in earlier files (no number changes)

- **Plan v41, section 2** says the hash of `extract_final.csv` is "in section 6". It is in section 7.
- **Report v13, section 6** says "All six PPV answer keys were reproduced from the published inputs", and gives the data checks as zero counts. Both are recorded in the run's log entry of 18 November 2026, from the same run. They are not explicit fields in `report_v13_output.json`, which report v13 names as the source of its numbers. The facts are unchanged.
- **Found by:** Claude Code, while checking report v13 and plan v41 before publication.

## 8. Files

| File | SHA-256 |
|---|---|
| `report_v41_output.txt` (the run's output, unchanged) | `d84bfbb2e297ed2a059a5de6d2cb92e2eb75d23c26c45745eb7b94cd1adb217d` |
| `v41.py` | `26738d145e856b1e37ac31015e474f9d52ff33b16cfd1630a8e21fa87a8081ae` |
| `test_v41.py` | `817fd2ed1d142af1ceaf85ab3b9d4b97cf93e618c2f4fa1a3952a019e89f1eb9` |
