# Report v22: can each published Bayes problem be fixed by changing one number?

**Plan:** v22 (tag v22, `prereg_v22.md`), published before the run. **Run once** on 19 November 2026 with
`python3 v22.py <repo root> <folder with v20.py> items_v20.csv`. **Arithmetic only: no learners, no human data.**

Every number below is copied from `report_v22_output.txt` (SHA-256 in section 5). Nothing here was computed after the
run except where marked "derived", which means arithmetic on printed numbers.

## 1. Result (plan section 3)

**Primary.** Of the 23 unique number sets, 2 have no collision and 21 have one. Of those 21:

- **12 can be fixed by changing one number;** 9 cannot be fixed that way within 40 points.
- Smallest fix of at most 1 point: 2. At most 2: 3. At most 3: 6. At most 5: 8. At most 10: 11. At most 20: 12. At
  most 40: 12.
- **Median smallest fix 3.5 points, largest 13 points.** The median is over the 12 sets that can be fixed (derived:
  their smallest fixes are 1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 9 and 13).
- Which number gives a smallest fix, ties counted for each: base rate 7, hit rate 6, false-alarm rate 3.

**Every number set**, with its collisions, every smallest fix and the correct answer before and after, is listed in
the output file.

**The sentence the plan allows:** "Of the 21 published number sets with a collision, 12 could be fixed by changing
one number by at most 13 points (median 3.5). Arithmetic, not tested on people."

## 2. What it does not show (plan section 4)

- Only the six wrong methods, the 1-point window and the whole-percent typing rule of v20.
- A fix changes the problem and usually its correct answer, sometimes a lot (for example the base rate 1% → 4%
  takes the correct answer from 10.00 to 31.43 on 1 / 55 / 5). It does not say the original problem was a bad
  teaching choice.
- A fix is a property of the numbers. It is not evidence that students would then be diagnosed correctly.
- Only whole-point changes to one number were searched.

## 3. Deviations

None. The script, its test file, `v20.py`, the item file and the frozen tutor files matched the SHA-256 values in plan
section 6 (checked on 20 November 2026).

## 4. Seen before the run

As disclosed in plan section 5. No fix had been computed on any of the 23 published sets before the run.

## 5. Files

| File | SHA-256 |
|---|---|
| `report_v22_output.txt` (the run's printed output, unchanged) | `5d7711664c27ce4315bcdacb03b310610d700b5df020056a658ad933f6a76f51` |
| `v22.py` | `4a9a8740f40623c96df080bed40561df02c2944257f36d4ee5a9042b1f14a3b5` |
| `items_v20.csv` (locked in addendum v20.1; not published, see report v20) | `5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236` |

Written 20 November 2026, from the saved output of the single run.
