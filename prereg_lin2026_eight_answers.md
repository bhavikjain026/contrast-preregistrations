# PRE-REGISTRATION — from the same 8 answers, which method diagnoses base-rate neglect best? (Lin et al. 2026)

Written 2026-10-13, committed and published before this analysis is run (a one-off exception to the team's analysis
freeze). Data: Lin et al. (2026), doi 10.31234/osf.io/wgpb2_v1, file SHA-256 0921573…965b233 (no licence stated: never
committed; derived numbers only). These answers were already used once, today, for a different pre-registered analysis
(label stability, `prereg_lin2026_replication.md`): its results (split-half and test-retest agreement of labels) are
known; no method below was run on these data before this file was committed.

## 1. The 8 trials (fixed from the design only)
Base-rate contrast pairs: same hit and false-alarm rate, base rate 1% vs 97%. Rule (as the tutor's opening pairs):
largest change in the correct answer first, never hit ≈ 1 − false alarm (within 1 point). Chosen (hit, false alarm):
**(72, 42), (53, 31), (90, 42), (72, 31)** % — correct answer changes ≈ 96 points in each. Each person's FIRST presentation
of these 8 triples is used (their own trial order).

## 2. Reference label (no leakage)
From the person's answers on the other 19 triples, both presentations (38 trials) — the 8 chosen triples are excluded
entirely, including their repeat presentations. Base-rate slope over the one-number-changed base-rate pairs within those
38 trials (Σ Δanswer·Δcorrect / Σ Δcorrect², `src/stengard_sensitivity.py`); **reference = "neglects" if |slope| < 0.2,
else "uses"** (the base-rate flag used for the tutor comparisons K1 / R-c).

## 3. Methods (each sees only the 8 answers and their numbers)
- **(a) Tutor check:** the frozen `opening_block.base_screen` (study-freeze-v2 logic, 1-point tolerance) on each of the 4
  pairs; "base-rate neglect likely" → neglects, "uses the base rate (likely)" → uses, otherwise no commitment from that
  pair; person label = the majority of the committed pair verdicts; a tie or no committed pair → **not sure**.
- **(b) Learner profile:** `learner_profile.fit` (least squares, intercept + base + hit + false alarm) on the 8 answers;
  base word "ignores it" → neglects; "under-uses it" / "uses it fully" / "uses it the wrong way" → uses; "not sure yet",
  "not measurable yet" or no fit → **not sure**.
- **(c) Language model:** Qwen2.5-14B-Instruct (bf16, one 2g.48gb GPU slice), greedy decoding (temperature 0), one call
  per person with a frozen prompt (`src/lin2026_eight.py`, PROMPT; SHA-256 recorded before the run): a short fixed
  instruction, the 8 problems (base rate, hit rate, false-alarm rate in percent, in a fixed order: pair by pair, 1% then
  97%) with the person's answers, and the fixed question "Does this person ignore the base rate? Answer yes / no / not
  sure". Reply parsed: starts with "yes" → neglects, "no" → uses, "not sure" or anything else → **not sure**.
- **(d) Majority guess:** always the more common reference label (in-sample baseline).

## 4. Measures (all people; reported whatever they show)
- **PRIMARY: accuracy** = share of people whose label equals the reference, **"not sure" counted wrong**.
- Secondary: coverage (share committed) and accuracy on committed cases; paired differences in accuracy (b − a, c − b,
  c − a, each − d). 95% CIs from 1,000 resamples of people (seed 0). By format (probability / frequency) as secondary.

## 5. Predictions (fixed now)
1. Profile (b) accuracy > tutor check (a) accuracy (paired CI above 0): the profile commits more often.
2. Tutor check (a): accuracy on committed cases ≥ 80%, coverage < 60% (as with one pair on Stengård: 82%, 43%).
3. Language model (c): accuracy below the profile (b). (Weak basis: the model has no explicit rule for "ignoring".)
4. No prediction about the majority guess (the reference prevalence on these trials is unknown before running).

## 6. Procedure (one run)
Dry run on synthetic people (known strategies on this design; stub model) and on Stengård data_12 (already used; base
1% / 97% replaced by the grid's 10% / 90%; methods (a), (b), (d) only) → freeze the script and prompt SHA-256 → one GPU
job (model replies for all 177 people; shown to the team lead before submitting) → one analysis run.
