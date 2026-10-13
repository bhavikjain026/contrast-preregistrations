# PRE-REGISTRATION (CONFIRMATORY) — question-selection policies on fixed held-out items

Written 2026-10-13, committed BEFORE any analysis code exists and before any response in the confirmatory file is read.
Its SHA-256 is recorded in results.md in the same commit. Any change after this commit is a new version with its own
hash, recorded before the run, and the change is reported next to the result.

## 0. Why a new sample (audit of the 46 "outside the tuning half")
The 46 people in `data_12.mat` outside the seed-0 tuning half (array positions 0, 1, 3, 6, 7, 12, 14, 21, 22, 24, 26,
29, 31, 32, 33, 37, 38, 40, 41, 45, 46, 47, 48, 49, 51, 54, 56, 58, 59, 60, 61, 62, 63, 66, 69, 71, 76, 77, 78, 79,
80, 81, 83, 84, 87, 88; `subject_index` = position + 1) are NOT unused. Every one of them was used, identically, by:

| # | Analysis (script → log) | Date | How the 46 were used |
|---|---|---|---|
| 1 | `src/stengard_analysis.py` → `stengard_analysis.json` (analyses 1–4: coverage, per-person best method, split-half prediction, pool-based selection) | 2026-10-09 | all 91 |
| 2 | `src/stengard_sensitivity.py` → `stengard_sensitivity.json` (slopes, groups, split-half κ, pairs needed) | 2026-10-09 | all 91 |
| 3 | `src/stengard_base_only.py` → `stengard_base_only.json` (base-rate neglect from few problems) | 2026-10-09 | all 91 |
| 4 | `src/stengard_learner_model.py` → `stengard_learner_model.json` (A prediction, B groups, C selection EIG vs contrast vs random, D calibration) | 2026-10-09 | **the 46 = its test half** |
| 5 | `src/stengard_early_label.py` → `stengard_early_label.json` (early label vs disjoint reference) | 2026-10-12 | all 91 |
| 6 | `src/stengard_hier.py` → `stengard_hier.json` (10-fold empirical Bayes over all 91; 91-person 23/22 prediction) | 2026-10-12 | all 91 (part (b) used the 45 only) |

Not used by: `src/stengard_profile_size.py` (tuning 45 only) and `stengard_hier.py` part (b) (same 45). Abstract
figures that include the 46: S1, S2, S3, S5, S6, S7, S9, S10, S11, K1–K10 (all from analyses 1–6).
Analysis 4C already compared selection policies on exactly these 46. They cannot be a confirmatory sample.

**Woike et al. 2023 (Study 4a–c), structure only** (from the 2026-10-11 feasibility entry in results.md; no answers
read): 4a = 4 tasks per person, base rate varies but hit and FA move together (r = 1.00) and no two tasks share a
number; 4b = 2 tasks per person; 4c = 1 task per person. A per-person base-rate label needs ≥ 3 unknowns plus held-out
items, and a selection policy needs a pool to choose from. **Not enough items per person — not usable.**

**Confirmatory sample chosen: Stengård et al. 2022, `data_11.mat`** (symbolic × NATURAL-FREQUENCY format; 91 people who
are different from `data_12`'s, per the paper's between-participant format assignment). Never analysed: only its file
structure was read (2026-10-09 description; 2026-10-13 structure check: 91 people × 45 items, the same 45-item grid
in the same order for everyone, base rates 10/30/50/70/90%, 45 non-missing responses per person; no response value
looked at). Raw data stay on scratch (no licence; derived numbers only).
**Caveat fixed now:** natural frequencies are known to reduce base-rate neglect, so the format differs from both our
tutor (percentages) and the tuning data (`data_12`). A result here is about this format; base-rate neglect may be
rare, which lowers the majority-guess baseline's informativeness and the power (see 7).

## 1. Items: one fixed held-out test set, the same for every policy and every person
From the 45-item grid (base {10,30,50,70,90} × hit {50,70,90} × FA {10,30,50}), chosen from the design only:
- **Test set T = the 15 items with hit 70%** (5 base × 3 FA). Never shown to any policy.
- **Pool = the 30 items with hit 50% or 90%.** Policies choose only from the pool.
T contains 30 base-rate one-number-changed pairs (10 per FA level) for the reference label.

## 2. Reference label (the "truth" each policy is scored against)
Per person, from T only: base-rate slope = Σ(Δanswer·Δcorrect) / Σ(Δcorrect²) over T's 30 base pairs (the sensitivity
analysis's formula). **Neglect = |slope| < 0.2.** No other threshold is reported as primary.

## 3. Classifier (identical for all policies)
The tutor's learner profile, `src/learner_profile.fit` as on main at this commit (intercept + base + hit + FA weights;
use = learner weight ÷ correct-learner weight; word only if 2·SE ≤ 0.3). Label from the k answers: base word
"ignores it" → neglect; "under-uses it" / "uses it fully" / "uses it the wrong way" → not neglect; "not sure yet" /
"not measurable yet" / no fit → **abstain**.

## 4. Policies, equal budgets
Each policy picks **k distinct pool items** per person; the person's real answers on those items are given to the
classifier. Budgets **k = 6, 8, 12, 16**; **PRIMARY k = 8.** (k = 4 is excluded: 4 answers fit 4 parameters exactly,
SE = 0, a known artefact.)
- **contrast** — the tutor's pairs-first order (interleaved base, FA, hit one-number-changed pairs, largest |Δcorrect|
  first, as `stengard_early_label.py`), restricted to the pool; first k distinct items. Same list for everyone.
- **random** — k pool items uniformly without replacement; 100 draws per person (seed 0); a person's score = mean over
  draws.
- **best fixed** — the single k-item pool set with the highest overall accuracy on the TUNING data `data_12.mat` (all
  91, same T / pool split and reference rule), found by greedy forward selection (ties → lowest item index). Computed
  and written to a log (with its hash) BEFORE `data_11.mat` is opened; then applied unchanged to everyone.
Non-adaptive by design: no policy uses the person's answers to choose items (an adaptive policy would be a new plan).

## 5. Metrics
- **PRIMARY: overall accuracy** at k = 8 = share of the 91 whose label equals the reference; **abstain counts as
  wrong** (so abstaining cannot help).
- Secondary: coverage (share labelled), accuracy among labelled, Cohen's κ (labelled only), at every k; held-out
  prediction error = mean |profile prediction − answer| on T's 15 items (points), at every k (people with no fit:
  person's mean answer as the prediction, counted); majority-guess baseline = always the more common reference label
  (reported, not tested).
- CIs: 1,000 bootstrap resamples of people (seed 0), paired (the same resample for all policies).

## 6. Hypotheses and decision rules (fixed now)
- **H1 (primary):** contrast > random on overall accuracy at k = 8. Supported if the paired Δ contrast − random has a
  95% CI entirely above 0; contradicted if entirely below; otherwise inconclusive.
- **H2 (primary, second):** contrast is not worse than best fixed by more than 5 points at k = 8 (non-inferiority).
  Supported if the lower 95% bound of Δ contrast − best fixed is > −5 points.
- Both are reported whatever the outcome; no correction is applied to H1/H2 beyond reporting both. All other numbers
  (other k, secondary metrics) are descriptive.
- Expectation stated now (from earlier, NON-independent data, so not evidence): on `data_12`, pairs-first − random
  overall accuracy for the profile was +12 [+4, +20] at 8 answers and +4 [−4, +11] at 16 (2026-10-12); a 91-person
  paired CI is roughly ±8 points wide, so **H1 may well come out inconclusive.** That outcome will be reported as such.

## 7. Procedure (one run)
1. Write `src/confirm_selection.py` (+ tests on synthetic people with known strategies; no real data in tests).
2. Dry run on `data_12.mat` (already-used data; labelled NOT confirmatory) to check the code end to end, and compute +
   log the best-fixed sets. Record script hash and best-fixed log hash in results.md and commit.
3. **One run on `data_11.mat`.** No code or parameter change after step 2's commit. Report everything above, including
   failures and inconclusive results, as "CONFIRMATORY, pre-registered (this file, hash in results.md)".
Exclusions: none planned (all 45 answers present). Any person the code cannot process is reported by count, never
dropped silently.
