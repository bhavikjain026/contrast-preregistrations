# Report v20: can published Bayes problems tell common mistakes apart?

**Plan:** v20 (tag v20, `prereg_v20.md`), with addendum v20.1 (tag v20.1), which locked the item file and the
exclusion log before the run. **Run once** on 19 November 2026 with `python3 v20.py <repo root> items_v20.csv`.
**No learners and no human data: only the numbers printed in published problems.**

Every number below is copied from `report_v20_output.txt` (SHA-256 in section 6), except where marked "derived",
which means arithmetic on printed numbers.

## 1. What was checked

54 rows from six sources, 23 unique standard number sets (base rate, hit rate, false-alarm rate). Sources S1–S6 of
plan section 3 gave items. **OpenStax (S7) gave none:** neither book applies Bayes' theorem with all three rates.
**Order flow (S8) gave none:** Glosten & Milgrom (1985) give the prior only as a symbol, and the free preview of the
tradermath lesson gives the informed share only as a symbol. So the order-flow part of the plan has 0 items. The
exclusion log has 46 rows, each with its reason.

## 2. Result (plan section 5)

**Primary.** Among the 23 unique standard number sets, **21 (91.3%, exact 95% interval 72.0 to 98.9)** have a
collision at the 1-point window: a wrong method's typed answer fits the correct answer (M1), or fits another wrong
method (M2).

**Described, no pass or fail:**
- **M1, a wrong method looks right:** 3 of 23 (13.0%, 2.8 to 33.6). Methods that pass as right: base rate only 1,
  hit rate 1, joint occurrence 2, likelihood subtraction 1. These are three number sets (derived; in percent): 0.024 / 15 / 12
  (base rate and joint occurrence; correct answer 0.03), 5 / 0.4 / 2.105 (hit rate and joint occurrence; correct
  0.99) and 25 / 80 / 40 (subtraction; correct 40.00). Two of the three have a correct answer below 1%.
- **M2, one typed answer fits two wrong methods:** 20 of 23 (87.0%, 66.4 to 97.2). The most common pairs are base
  rate only with joint occurrence (14 sets) and equal priors with false-alarm complement (13).
- **Same whole percent (0.5-point sensitivity):** any collision 18 of 23 (78.3%, 56.3 to 92.5); M1 2 of 23; M2 17
  of 23.
- **By arithmetic (plan section 4):** no standard item has a base rate of 0.5.
- **Per source** (repeats within a source counted once): S1 16 of 17, S2 4 of 4, S3 2 of 2, S4 2 of 2, S5 3 of 3,
  S6 1 of 2.
- **Every item** is listed in the output with its source, location, numbers, correct answer and collisions.

**The sentence the plan allows:** "Of 23 published Bayes number sets from six research sources, 3 let a common wrong
method look right to within a point, and 20 let one answer fit two different wrong methods. Order-flow problems: 0 of
0; none of the order-flow sources printed all three numbers."

## 3. What it does not show (plan section 6)

- Six wrong methods only; people use others.
- Whole-percent typing and the 1-point window are our assumptions; the 0.5-point result is above.
- **Not a judgement on the studies.** A collision says what one answer alone cannot show. Several of these studies
  used written working, as Gigerenzer and Hoffrage did.
- The sources are our selection, fixed before checking, and the sample is small; the intervals are wide.

## 4. Things addendum v20.1 said the report must say

1. **Mammography appears as four number sets** (false alarm 9.69%, 9.6%, 95 of 990, and 10%), because the plan counts
   exact number sets.
2. **The S1 copy is a manuscript-format PDF,** not the journal version. Its p. 4 value of 9.69% may be a typo in that
   copy (the same page computes with .096). It was recorded as printed.
3. **One row was added at the row check:** the economics row of Bruckmaier et al. (2019), 0.25 / 0.8 / 0.4. It is
   the set 25 / 80 / 40 above, one of the three M1 sets.
4. **Rows with a rate equal to 1 were excluded** (AIDS and heroin in Gigerenzer & Hoffrage Table 2; five heroin
   versions in Weber et al.). Plan section 3 did not name this exclusion.

## 5. Deviations

- **Plan section 8 step 2 says Bhavik checks every row.** He did not. At his request Claude, the AI assistant that
  also did the extraction, checked the rows instead, so the check is not independent (`row_check_v20.md`).
- Otherwise none. The script, the item file and the exclusion log matched their published SHA-256 values (checked on
  20 November 2026).

## 6. Files

| File | SHA-256 |
|---|---|
| `report_v20_output.txt` (printed output, unchanged) | `31d6d9be58427bbede642c4857e60ff7cfa34de2b61b229a90b3370ef281d86d` |
| `v20.py` | `c71003c8602d912409bc5ea07941d8e93796716c6f607470b8c5436c84232db3` |
| `items_v20.csv` | `5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236` |
| `exclusions_v20.csv` | `9d3cb48a3d1d5bb1f605b5dc79a52c7b9c919112cb5584aed98cef64f1271a29` |

The item file and exclusion log are not published, because they quote short passages of the source papers. Their
hashes were published in addendum v20.1.

Written 20 November 2026, from the saved output of the single run.
