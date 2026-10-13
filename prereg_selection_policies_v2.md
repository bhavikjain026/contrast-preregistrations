# PRE-REGISTRATION v2 (CONFIRMATORY) — question-selection policies on fixed held-out items, + replication of three headline figures

v1 committed 2026-10-13 in 6cd03cb (SHA-256 0fabe8ff…6bd526). **v2 written 2026-10-13, before any analysis code exists
and before any response value in the confirmatory file is read.** SHA-256 of this file is recorded in results.md in the
same commit. Changes from v1 (team request, 2026-10-13): (i) the accuracy reference is defined exactly (section 2);
(ii) secondary hypotheses replicating three abstract figures (section 6b); (iii) natural-frequency limit with predicted
direction (section 8); (iv) "best fixed" chosen by a seeded random search instead of greedy selection (greedy cannot score
sets below 5 items, where the profile cannot be fitted). Nothing else changed.

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

**Woike et al. 2023 (Study 4a–c), structure only** (2026-10-11 feasibility entry in results.md; no answers read):
4a = 4 tasks per person, base rate varies but hit and FA move together (r = 1.00), no two tasks share a number;
4b = 2 tasks per person; 4c = 1 task per person. **Not enough items per person — not usable.**

**Confirmatory sample: Stengård et al. 2022, `data_11.mat`** (symbolic × NATURAL-FREQUENCY format; 91 people different
from `data_12`'s — the paper assigns format between participants). Never analysed: only its file structure was read
(91 people × 45 items, the same 45-item grid in the same order for everyone, base rates 10/30/50/70/90%, 45 non-missing
responses per person; no response value looked at). Raw data stay on scratch (no licence; derived numbers only).

## 1. Items: one fixed held-out test set, the same for every policy and every person
From the 45-item grid (base {10,30,50,70,90} × hit {50,70,90} × FA {10,30,50}), chosen from the design only:
- **Test set T = the 15 items with hit 70%** (5 base × 3 FA). Never available to any policy.
- **Pool = the 30 items with hit 50% or 90%.** Policies choose only from the pool.

## 2. Reference label — exactly what each policy's answers are compared against
For each person, ONE reference label, computed once, from that person's answers to the 15 items of T ONLY, and identical
for every policy and every budget:
- base-rate slope s_T = Σ(Δanswer·Δcorrect) / Σ(Δcorrect²) over the **30 base-rate pairs inside T** (two T items that
  differ only in base rate: same hit 70% and same FA; 10 pairs per FA level), Δ = later − earlier item, correct =
  Bayes(base, hit, FA), answers as proportions (the formula of `src/stengard_sensitivity.py`, applied to T's pairs);
- **reference = "neglect" if |s_T| < 0.2, else "not neglect".**
A policy's label is computed only from its k pool answers (section 3). Because T and the pool are disjoint, no answer
is used both to label and to score. "Accuracy" = share of people whose policy label equals their reference label, with
"abstain" (not sure yet / no fit) counted as NOT equal.

## 3. Classifier (identical for all policies)
The tutor's learner profile, `src/learner_profile.fit` as on main at this commit (intercept + base + hit + FA weights;
use = learner weight ÷ correct-learner weight; word only if 2·SE ≤ 0.3). Label from the k answers: base word
"ignores it" → neglect; "under-uses it" / "uses it fully" / "uses it the wrong way" → not neglect; "not sure yet" /
"not measurable yet" / no fit → **abstain**.

## 4. Policies, equal budgets
Each policy gives the classifier the person's real answers to **k distinct pool items**. Budgets **k = 6, 8, 12, 16**;
**PRIMARY k = 8.** (k = 4 excluded: 4 answers fit 4 parameters exactly, SE = 0, a known artefact.)
- **contrast** — the tutor's pairs-first order (`stengard_early_label.designed_pairs`: base, FA, hit one-number-changed
  pairs, each by descending |Δcorrect|), using only pairs with both items in the pool; first k distinct items. Same list
  for everyone.
- **random** — k pool items uniformly without replacement; 100 draws per person (seeded per person and k); a person's
  score = mean over draws.
- **best fixed** — for each k, the k-item pool set with the highest overall accuracy (section 2 reference, section 3
  classifier) on the TUNING file `data_12.mat` (all 91), chosen among the contrast set and 2,000 random k-sets (seed 0;
  ties → first in that list). Written to `logs/confirm_bestfixed.json` in the dry run; its SHA-256 is recorded and the
  script refuses the confirmatory run if the file differs.
Non-adaptive: no policy uses the person's answers to choose items.

## 5. Metrics
- **PRIMARY: overall accuracy at k = 8** (section 2; abstain = wrong).
- Secondary, at every k: coverage (share labelled), accuracy among labelled, Cohen's κ (labelled only), held-out
  prediction error on T (mean |profile prediction − answer| over T's 15 items, points; no fit → person's mean pool
  answer), majority-guess baseline (always the more common reference label; reported, not tested).
- CIs: 1,000 bootstrap resamples of people (seed 0), paired (same resample for all policies).

## 6. Hypotheses and decision rules (fixed now)
### 6a. Primary (selection policies, data_11, n = 91)
- **H1:** contrast > random on overall accuracy at k = 8. Supported if the paired Δ (contrast − random) 95% CI is
  entirely above 0; contradicted if entirely below; otherwise inconclusive.
- **H2:** contrast not worse than best fixed by more than 5 points at k = 8: supported if the lower 95% bound of
  Δ (contrast − best fixed) > −5 points; otherwise not supported.
### 6b. Secondary — replication of three abstract figures on the new 91 (each with the SAME procedure as the original
script, applied unchanged to data_11; the original value from data_12 in brackets)
- **R-a (split-half, as `stengard_sensitivity.py`):** 100 random splits of the 45 problems (23 / 22, seed 0); per half,
  slopes from pairs inside the half; label = "base-rate neglect" group (|base slope| < 0.2 AND hit or FA slope ≥ 0.2);
  agreement between halves and κ, each averaged over splits [data_12: 80%, κ 0.56]. CI: 1,000 resamples of people with
  the per-split labels fixed. **Ha:** κ's 95% CI lower bound > 0.40 (at least moderate stability). Also reported:
  whether the CI includes 0.56.
- **R-b (profile vs named methods, as `stengard_profile_size.py`, designed order, size 16):** per person, the first 16
  problems of the designed (pairs-first, full 45-item grid) order fit (i) the per-person linear profile and (ii) the
  best-matching named method (7 candidates incl. Bayes, 1-point matches, tie → lower error); mean absolute error on the
  person's other 29 answers [data_12, 45 tuning people: 10.0 vs 11.9, Δ −1.94 [−3.99, −0.04]]. All 91 people.
  **Hb:** Δ (profile − named) 95% CI entirely below 0.
- **R-c (first base-rate pair, as `stengard_early_label.py`, k = 1 pair check):** the tutor's pair check
  (`opening_block.base_screen`) on the first base-rate pair of the pairs-first order (2 problems); % committed (labelled)
  and % of committed matching the reference = base-slope label (|slope| < 0.2) from all base pairs with both problems
  outside those 2 (the other 43 answers) [data_12: 43%, 82%]. **Hc:** accuracy among committed has a 95% CI lower bound
  above the majority-guess accuracy on the same committed people (point value).
No multiplicity correction; all results (H1, H2, Ha–Hc) are reported whatever the outcome. Other k and secondary
metrics are descriptive.

## 7. Procedure (one run)
1. Write `src/confirm_selection.py` + tests on synthetic people (no real data in tests). Commit.
2. **Dry run on `data_12.mat`** (already-used data; NOT confirmatory): checks the code end to end; writes
   `logs/confirm_bestfixed.json` (best-fixed sets) and `logs/confirm_dryrun_data12.json`. Record both hashes and the
   script's hash in results.md; shown to the team; commit.
3. **One run on `data_11.mat`.** No code or parameter change after step 2's commit (the script checks its own hash and
   the best-fixed hash against the recorded values). Report everything above as "CONFIRMATORY, pre-registered".
Exclusions: none planned. Any person the code cannot process is reported by count, never dropped silently.

## 8. Known limit: natural-frequency format (direction predicted now)
`data_11` presented the numbers as natural frequencies; our tutor and `data_12` use percentages. The paper reports, for
these same files, lower error with natural frequencies (mean absolute error 18.0 vs 23.2 across conditions) and more
people best fitted by the Bayesian model (46 of 91 vs 31 of 91 in the symbolic conditions). Predicted direction on
data_11 vs data_12: **fewer people labelled base-rate neglect** (reference and R-a groups), **lower prediction errors**
in R-b for both methods, and therefore a **higher majority-guess baseline** and fewer neglect cases for κ to work with —
so κ (R-a, policies) is expected to be **lower or less precise** even if agreement is as high or higher. Any result
holds for natural-frequency presentation; it does not show the same for the tutor's percentage problems.
