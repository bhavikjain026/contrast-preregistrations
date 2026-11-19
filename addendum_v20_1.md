# Addendum v20.1: item files locked before the run

Written 19 November 2026. To be published under tag v20.1 **before** `v20.py` is run on any published item (plan v20, section 8, step 3). Plan v20 is unchanged except where stated below.

## 1. Locked files

| File | Rows | SHA-256 |
|---|---:|---|
| `items_v20.csv` | 54 (23 unique standard number sets; 0 order-flow) | `5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236` |
| `exclusions_v20.csv` | 46 | `9d3cb48a3d1d5bb1f605b5dc79a52c7b9c919112cb5584aed98cef64f1271a29` |

These replace the first extraction files (`items_v20.csv` 092689fb…, `exclusions_v20.csv` de9a6a97…), which were never run.

Per source, rows in `items_v20.csv`:

| Source | Rows |
|---|---:|
| S1 Gigerenzer & Hoffrage 1995 | 22 |
| S2 Sedlmeier & Gigerenzer 2001 | 18 |
| S3 Domurat et al. 2015 | 3 |
| S4 Weber et al. 2018 | 2 |
| S5 Bruckmaier et al. 2019 | 6 |
| S6 Eichler et al. 2020 | 3 |
| S7 OpenStax | 0 (no problem uses all three rates) |
| S8 Order flow | 0 (no numerical prior in Glosten & Milgrom; the tradermath lesson is paywalled after a symbolic preview) |

## 2. Departures from plan v20, disclosed

1. **Who checked the rows.** Section 8 says Bhavik checks every row against its source. At his request, Claude, the AI assistant, did the check. The extraction agent was also Claude, so the check is not independent of the extraction. The method and result for every row are in `row_check_v20.md`.

2. **Changes made at the check.** Four rows were added for Bruckmaier et al. (2019). These are the study's own tasks: their numbers appear only in the Figure 4 stimuli, and Figure 4 shows a Bayesian question for the economics context. The two exclusion lines for those tasks were replaced by one line saying the wording table (Table 3) is not accessible.
   - The two mammography rows repeat number sets already present.
   - The two economics rows add one new number set (b = 0.25, h = 0.8, f = 0.4).
   - This follows section 3's rule that a problem counts if its rates are "fixed through natural frequencies". It is consistent with Eichler et al. Figure 5, which was already included.

3. **Rates of exactly 1 excluded.** The published checker requires each rate to be strictly between 0 and 1, but section 3 did not list this exclusion. Excluded on this ground:
   - AIDS (hit rate 100 of 100) and heroin (10 of 10), both in Gigerenzer & Hoffrage Table 2;
   - five heroin versions in Weber et al. (2018).

4. **Copy of source 1.** Gigerenzer & Hoffrage (1995) was read from a manuscript-format copy (pages.ucsd.edu), not the journal PDF. Locations are manuscript pages.
   - On p. 4 the false-alarm rate is printed as 9.69%. Table 1 and the relative-frequency version print 9.6%, and p. 4 itself computes with .096.
   - The 9.69% is recorded as printed, and it forms its own number set.

5. **Rounded counts.** Table 2's footnote 4 says large odd totals were rounded, for example 9,950 to 10,000. Rates are recorded from the printed counts.

6. **How sources were read.** The extraction used Bhavik's Chrome. A web-fetch summary misread one figure (60% for 80%); no row relies on it, and the figure was checked by eye.

7. **What was computed before this lock.** No wrong method's value and no collision (M1 or M2) was computed for any published item. The one exception was a transcription check on Gigerenzer & Hoffrage Table 2: the correct Bayes answer was computed from our numbers for its 13 rows. All 13 matched the paper's printed p(H|D) column to two decimals.

## 3. What the report must add

These lines describe the data and are not new tests:

- **Mammography appears as four number sets** in the primary measure: false-alarm rates of 9.69%, 9.6%, 95/990 (also printed as 950/9,900) and 10%. The report says so beside the primary result.
- **The economics row (Bruckmaier, 0.25 / 0.8 / 0.4) was added at the row check.** Its outcome is shown in the per-item listing, so its effect on the primary measure is visible.
- **Order flow: 0 items.** So the slide sentence's order-flow clause reads "Order-flow problems: none in these sources had numerical rates". It does not report "Z of W".

## 4. Procedure, unchanged

Run once: `python3 v20.py <repo root> items_v20.csv` on the locked file above. Report every number in plan section 5, whatever it shows. Any change after this is a dated, published addendum.
