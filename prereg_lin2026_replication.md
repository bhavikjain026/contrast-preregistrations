# PRE-REGISTRATION — replication of label stability on Lin et al. (2026)

Written 2026-10-13, committed and published BEFORE any answer in the dataset is analysed (only its structure was read:
counts, units, design). SHA-256 of this file is recorded in the project log and in the public pre-registration repo.
A one-off exception to the team's analysis freeze, approved by the team lead.

## 1. Data
Lin et al. (2026), "Integrating Heuristics and Mental Sampling in Belief Updating", doi 10.31234/osf.io/wgpb2_v1; file
`data/df.csv` from github.com/LinYitong1/belief-update (downloaded 2026-10-13, SHA-256
092157357ca7baa79cf0714fd04fd3d49648fa6932cbabd5834d3de64965b233). No licence stated: the file is never committed or
shared; only derived numbers are reported, with the citation.
Structure (checked, no answers analysed): 177 people × 54 trials, no missing answers; base rate {1, 40, 97}%, hit rate
{53, 72, 90}%, false-alarm rate {11, 31, 42}% in a full 3 × 3 × 3 design (the three vary independently); every person
answers all 27 triples twice, in a person-specific random order; answers are percents (0–100); presentation format is
between people (probability 100, frequency 77). All seven methods (correct + six wrong) are more than 2 points apart on
only 5 of the 27 triples.

## 2. Method (same functions as the registered Stengård analyses; answers divided by 100)
- **Canonical order:** each person's trials are sorted by triple, then by presentation (slots 1–27 = first
  presentations, 28–54 = second presentations), so all people share one design and the functions of
  `src/stengard_sensitivity.py` apply unchanged. Pairs = trials differing in exactly one number (across presentations
  too); slope = Σ(Δanswer·Δcorrect)/Σ(Δcorrect²).
- **Labels:** base-rate neglect = |base slope| < 0.2 AND hit or false-alarm slope ≥ 0.2 (the registered definition,
  `groups()`); false-alarm neglect = the registered `groups()` definition; **hit neglect = |hit slope| < 0.2 AND base or
  false-alarm slope ≥ 0.2 — EXPLORATORY (new definition, not registered on Stengård)**; commonest named method =
  best match over the 7 methods within 1 point on the trials of a half (tie → lower mean error, still tied →
  "unresolved", its own category), as `src/stengard_splithalf_labels.py`.
- **(a) Split-half:** 100 random 27 / 27 splits of the 54 slots (rng seed 0); per split, each label from each half;
  agreement and Cohen's κ, averaged over splits; 95% CI from 1,000 resamples of people with per-split labels fixed
  (seed 0).
- **(b) Test-retest:** the same labels from slots 1–27 (first presentations) vs 28–54 (second presentations); agreement
  and κ; 95% CI from 1,000 resamples of people.
- **(c)** (a) and (b) for the false-alarm-neglect label and the (exploratory) hit-neglect label.
- **(d) Matched comparison:** commonest-method κ on the same 100 splits and on test-retest; difference base-rate κ −
  method κ with a 95% CI from the same resamples of people.
- **Primary: all 177 people. Secondary: each format separately.** No exclusions; people giving the same answer on all
  54 trials are counted and reported.

## 3. Predictions (fixed now; results reported whatever they show)
1. Base-rate split-half κ ≥ data_12's 0.56, with the 95% CI lower bound > 0.40 (the extreme base rates give a stronger
   base-rate signal than the Stengård grid).
2. Test-retest κ ≥ split-half κ for the base-rate label (identical triples allow memory and consistency).
3. False-alarm κ < base-rate κ (narrow false-alarm range, as on Stengård: 0.26 vs 0.56).
4. Method κ < base-rate κ.
**Interpretation fixed now:** because only 5 of the 27 triples separate all methods, a lower method κ than base-rate κ
on this dataset will NOT be interpreted as number-use labels being more stable than formula (method) labels; it is
reported as design-limited. (On Stengård, measured the same way, the two were about equal.)

## 4. Procedure (one run)
1. Script `src/lin2026_replication.py`. Dry run on Stengård `data_12.mat` (already-used data, NOT part of this
   replication): it must reproduce exactly the registered split-half figures — base-rate neglect 79.9% / κ 0.56 (S3),
   false-alarm κ 0.26 (S7), commonest-method κ 0.54 (SH1). If any differs, stop and fix before freezing.
2. Freeze the script's SHA-256 (recorded in the project log); the Lin run refuses to start if the script differs.
3. Run once on Lin; report every number above, including any prediction that fails.
