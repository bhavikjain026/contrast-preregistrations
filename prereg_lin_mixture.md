# Pre-registration v10: diagnosing base-rate neglect from 8 answers with a pooled mixture model

**Status: FINAL. Approved by the team lead on 2026-11-17 and released as v10** in the public pre-registration
repository (github.com/bhavikjain026/contrast-preregistrations, file `prereg_lin_mixture.md`), **before any Lin Exp1 or
Exp2 answer was read for this work.** The run code is hashed (§9). The script refuses every real file until its frozen
record names the public v10 tag, which is added only after publication. Changes from here on are dated addenda,
published before the run they affect. The trial's final addendum becomes v11 (team lead, 2026-11-16;
`analysis/decisions_log.md`). Work is on branch `finals-mixture-2026-11-16`; the private file keeps its drafting
name `analysis/prereg_lin_mixture_DRAFT.md`.
Development numbers: `logs/mixture_stengard_dev_14102.json` (Slurm job 14102, commit 3e0af76). All are
**out-of-sample by person** (§10).
**Every Stengård model number in this plan is labelled "development, chosen among 80 variants"** (§10 lists the 80).
Stengård numbers that come from a check rather than a model (format count, order test) are labelled "development
check"; they involved no choice among variants.
Each design fact carries its source:
- **[paper]**;
- **[repo]** (README / file list);
- **[design columns]**: our extraction, no answer column read (§2.1);
- **[verification check]**: the team's separate check of 16 Nov, not confirmed by us.

## 1. Question and claim
Can a tutor tell from **8 answers** whether a learner neglects the base rate, with honest probabilities and an option to
say "not sure yet"?
To our knowledge, combining a pooled mixture of noisy weighted log-odds rules, simulation-based label probabilities and
an abstention rule tuned on one data set and certified with an exact bound on independent test people, for
two-hypothesis Bayes problems, has not been done before. The
parts are not new:
- strategy mixtures for updating data: El-Gamal & Grether (1995);
- people who neglect vs use the base rate: Stengård et al. (2022);
- risk control by multiple testing: Learn then Test (Angelopoulos et al., 2021);
- adaptive diagnosis of latent classes: CD-CAT (Cheng, 2009);
- nearest recent work: Xu & Yu (2026, arXiv 2611.14557), conformal misconception sets with a marginal guarantee. Our
  Exp2 certification is marginal too (an average over people like those in Exp2).

**Prior work.**
- The mixture model follows **El-Gamal & Grether (1995)**, who fitted a population mixture of updating rules (Bayes,
  representativeness, conservatism) with an error rate to people's choices.
- Per-person use of the inputs (base rate, hit rate, false-alarm rate) was estimated **offline**, from each person's
  full set of answers, by **Cohen & Staub (2015)** and **Stengård et al. (2022)**.
- What we add is the online question: how well a person's label can be predicted from 8 answers, with a calibrated
  option to say "not sure yet".

## 2. Data sets and roles
| Role | Data | People | Status |
|---|---|---|---|
| Development | Stengård et al. 2022, symbolic (data_11 + data_12) | 182 | All model choices; analysed by us before |
| **Primary test** | Lin et al., **Experiment 2, self-paced block** | 83 | **Never analysed by us**; design columns only (§2.1) |
| Calibration of the abstention threshold + secondary test | Lin et al., **Experiment 1** | 177 | **Previously analysed by us** (§3) |
| Secondary | Lin Exp2, time-limited block | 83 (20–54 answers each) | Reported separately; never pooled with the primary |
| Exploratory only | Enke & Graeber 2023 | ~500 [verification check] | Never a primary or secondary test (§2.2); responses never downloaded |

### 2.1 Lin Experiment 2
- File: `data/Exp2/Exp_2.csv` in github.com/LinYitong1/belief-update **[repo]**, at repository commit
  **f8b7c037ab56cd47b5455955bea0145b8ad0084c** (2026-11-07). File fingerprint, recorded before the tag:
  - **SHA-256 bcdd9b0ceb2f9192e79910492429970bb6e566eaae3b03aed861f9253d7d7a6b**;
  - git blob c5b6fce79f4aca0e7801ee25bec77728bdbd272b; 841,217 bytes.

  Downloaded 2026-11-16 to a git-ignored folder. Only the size, the line count (8,597 lines = header + 8,596 rows)
  and the header line were looked at. **The run refuses to start if either fingerprint differs.**
- The README describes Exp2 as "a follow-up experiment examining how time pressure influences probability
  judgements" and cites "Lin, Sanborn & Chater, submitted to JEP: General" **[repo]**.
- Exp2 is not in preprint v1 **[paper]**. There is no licence file **[verification check]**.
- **How we looked (2026-11-16):**
  - the file was streamed once;
  - only subject_id, format, block_type, block_num, n_trial, trial_in_block, practice, is_check_trial, br, hr and far
    were kept;
  - `inputvalue` (the answer), `correctAnswer`, the response-time columns and `invalid_input` were dropped in memory and
    never stored, printed or summarised.
  - Design-only file: `data/realdata/lin2026_exp2_design/design_only.csv` (git-ignored), SHA-256 fcacdc29…461879.
- Design **[design columns]**:
  - 83 people, 8,596 rows, no practice or check rows; probability format 49, frequency 34;
  - one self-paced and one time-limited block per person; self-paced first 39, time-limited first 44;
  - **self-paced block:** 54 rows for everyone = 27 triples × 2 showings, on the Exp1 grid: base {0.01, 0.40, 0.97},
    hit {0.53, 0.72, 0.90}, FA {0.11, 0.31, 0.42}. **Base, hit and FA all vary within person**;
  - time-limited block: 20–54 rows per person (24 complete). Missing trials are absent rows.
- Entry mode: **not documented for Exp2** (team decision, 2026-11-16). Exp2 is unpublished, so nothing describes how
  answers were entered. The answer column has the same name as in Exp1 (`inputvalue`), but that is not taken as
  evidence of typed entry.

### 2.2 Enke & Graeber (2023): exploratory only
Source: NBER WP 26518 (rev. January 2021), §4.1.1 and Figure 19 **[paper, WP]**. The QJE version is paywalled to us.
- Signals are **symmetric**: "We only implemented symmetric signal structures such that P(red|A) = P(blue|B)". So
  FA = 1 − hit.
- Base rate {10, 30, 50, 70, 90}%, q ∈ {70, 90}, 1 or 3 balls drawn, six tasks per person, typed field 0–100
  **[paper, WP]**. The verification check reports base rates 1–99% and 6–12 tasks **[verification check]**.
- So separate hit and FA weights are not identifiable, and there are too few tasks for 8 answers plus a truth label.
- **Exploratory only, clearly labelled:** on single-ball trials, the **base-rate weight** and **one evidence weight**
  on log(q / (1 − q)), with the primary (spike-free) model family. The weights are described, with no accuracy claim.

## 3. Disclosure: Lin Experiment 1 was analysed before
We ran two pre-registered, run-once studies on Lin Exp1 on 2026-10-13 (`results.md`):
1. label stability: base-rate split-half κ 0.73;
2. same 8 answers: learner profile 67.2% vs majority guess 63.3%; 65 / 177 labelled neglect by a 38-trial reference.

Exp1 is therefore not blind. Here it calibrates the abstention threshold and is a secondary test.

### 3.1 Which Exp1 file
- **The calibration (and every Exp1 number in §8) uses our copy analysed on 2026-10-13:**
  `data/realdata/lin2026/df.csv`, **SHA-256 092157357ca7baa79cf0714fd04fd3d49648fa6932cbabd5834d3de64965b233**.
  The run refuses to start if it differs.
- **It differs from the current GitHub version** (`data/Exp1/df.csv` at commit f8b7c037…, SHA-256
  ed5f60a9716471cd43058b904a2939a6a99ddd3232d53d8096de03221a9e9e00, git blob 5baa1ad1…).
- **The differences were not examined.** On 2026-11-16 we compared only file size, row count and column headers:

  | | our 2026-10-13 copy | GitHub version |
  |---|---|---|
  | Size | 991,251 bytes | 513,331 bytes |
  | Lines (header + rows) | 9,559 | 9,559 |
  | Columns | file_id, format, rt, inputvalue, br, hr, far, brr, error, correctAnswer, n_trial, **subject_id**, **id_source**, subject | the same without **subject_id** and **id_source** |
  | Line ends | LF | CRLF |

  The GitHub version has `subject` as its only person column, so the script reads people from `subject` there.
- A pre-specified secondary check repeats the calibration on the GitHub version (§8, item 10).

## 4. Blind format check (one per Lin test set, before unblinding)
- Before any outcome, the script counts **how many responses are whole numbers** (a whole percent; frequency format: a
  whole number out of 100), and reports that count and share.
- **Answer-scale guard** (same step, for each file: Exp1, Exp2, and the GitHub version of Exp1). The script also
  reports the **smallest and largest answer** and the **share of answers above 1**. **This reads the range of the
  answers only.**
  - **If the largest answer is 1 or less, or under half the answers are above 1,** the run stops.
  - A dated addendum is then published before any analysis.
  - Later stages refuse to start on that file.
- **Pre-flight data check** (same step; **validity only**: whether each answer is usable, never its value beyond the
  §6.1 range rule). For each file (Exp1, Exp2, the GitHub version of Exp1), for each Exp2 block separately, and within
  each **response format** separately, the script reports:
  - the share of the expected answers (people × 54) that the missing-answer rule (§6.1) would drop, **split by
    reason**: row absent; blank or not a number; outside 0–100; `invalid_input` flag (an answer is counted under the
    first reason that applies, in that order);
  - the **number of people who would fail the 18-pair rule** (§6.1).

  **Stop rule, for Exp1 (both versions) and the Exp2 self-paced block:** if **more than 10% of people** would be left
  out, or **more than 10% of answers in any format** are outside 0–100, the run stops before any analysis and a
  dated addendum is published first; later stages refuse that file. **The time-limited block is reported only**
  (missing trials are expected there).
- Nothing else is computed in this step.
- The **primary model has no spikes**, so this check does not affect the primary endpoint.
- It decides only whether the **secondary spike model** is run on that data set. The pass mark is **at least 95% of
  responses whole numbers**.
  - **Lin Exp1:** entry is documented as a fill-in "___ %" **[paper]**, with an `inputvalue` column **[repo]**. The
    spike model runs if the check passes.
  - **Lin Exp2:** entry is **not documented** (unpublished; §2.1). **The spike model runs on Exp2 only if the blind
    whole-number check passes;** the check alone decides.
  - If the check fails, the spike comparison on that data set is reported as "not run (format)".
- For reference, Stengård symbolic (development check): typed **[paper]**; all 8,190 answers are whole numbers.

## 5. Assumption: no order or position effects
The replay asks a fixed set of 8 answers regardless of when they were given. **We assume answers do not depend on
position or on earlier problems.** On the only development files that keep order (Stengård pictorial, 40 people × 90
trials; `logs/mixture_order_local-20261116.json`) there was **no evidence of order effects** (development check):
- drift −0.0006 per 10 trials, permutation p 0.36;
- second − first presentation |error| −0.004, p 0.51;
- base-rate slope, second − first half −0.009, p 0.81.

With 40 people this cannot show that order effects are absent. Exploratory on Exp2: results by block order (39 vs 44).

**Limitation (replay).** The test replays answers people already gave; no one is asked anew. Replay assumes **a
person's answer to a question does not depend on which questions came before it**. In a live tutor, the questions
before would be only the ones the tutor chose to ask; in the data, they were the full experimental sequence. If
earlier questions change later answers (learning, fatigue, anchoring on a previous number), the replayed results may
differ from what a live tutor would get.

## 6. What is asked and what it is graded against (Lin)
- **Ask only from each person's FIRST showing of the 27 combinations.** The 8 answers are the first-showing answers to
  the 1% vs 97% base-rate pairs at hit/FA (72, 42), (53, 31), (90, 42), (72, 31), asked in that order (the same 8 as on
  2026-10-13).
- **Truth = the neglect label from all 27 answers of the SECOND showing:** |base slope| < 0.2 over the 27 base-rate
  pairs of the second showing (9 hit/FA cells × 3 base-rate pairs). The slope is Σ Δanswer·Δcorrect / Σ Δcorrect².
  Every policy and baseline is graded against this same truth.
- **Ceiling (reported first):** agreement between the label from showing 1 (27 answers) and the label from showing 2,
  as % agreement with CI and κ. No 8-answer policy can be expected to do much better.
- **Which showing is which:** within a block, showing 1 of a triple is its earlier presentation by `trial_in_block`
  (Exp1, one block: by `n_trial`), and showing 2 the later one. *(Added 2026-11-16 while writing the script:)* a
  triple with only one row in a block counts as its showing 1 (in a time-limited block, missing trials are the ones
  not reached). A triple not on the Lin grid, or shown more than twice, stops the run (design violation).
- The primary endpoint uses the Exp2 self-paced block only. The Exp2 time-limited block is a **secondary** analysis
  under the same rules (§6.1), reported separately.

### 6.1 Rules fixed in advance (all Lin sets)
- **Missing answers.** An answer is missing if:
  - its row is absent;
  - the value is blank or not a number;
  - the value is outside 0–100;
  - or the data's own `invalid_input` flag is true.

  Missing answers are left out of the likelihood; nothing is imputed. No person is excluded for missing asked
  answers:
  - the 8-answer prediction uses whichever of the 8 asked answers are present;
  - the abstention policy skips a missing item and goes on to the next;
  - a person with none of the 8 present gets the population prediction Σ_k π_k q_k.
- **Missing answers, truth side.** A truth label is computed only from base-rate pairs with both answers present, and
  needs **at least 18 of the 27 pairs**. A person below 18 has no truth label and is left out of every endpoint. The
  ceiling also needs at least 18 pairs in showing 1. The number of people left out is reported for each data set.
- **Ties.**
  - Truth label: neglect if |slope| < 0.2, strictly. A slope of exactly 0.2 (float64, answers as proportions) is
    "uses the base rate"; *(added 2026-11-16)* a slope within 10⁻¹² of 0.2 (float rounding) counts as exactly 0.2.
    The slope is always defined, because the paired correct answers differ.
  - Predictions: neglect if p ≥ 0.5.
  - Majority guess: neglect if the prevalence is ≥ 0.5.
  - Abstention commits: neglect if p ≥ 0.5.
- **Intervals.**
  - Every CI except the risk intervals and the primary endpoint: percentile bootstrap over people, **1,000
    resamples, seed 0**
    (numpy `default_rng(0)`), with the same resampled people for every metric of a data set. Ratios (skill, κ) are
    recomputed in each resample.
  - Committed-wrong risk: exact Clopper–Pearson 95% (two-sided), plus the one-sided exact 95% upper bound (§8,
    item 6).
  - The primary endpoint and its two sensitivity intervals: **20,000 resamples**, same seed rule (§8).
  - The cross-fitting folds use seed 0.
- **Answer scale check** *(added 2026-11-16; design columns only, before any answer is used)*: `correctAnswer` must
  equal 100 × the Bayes answer for (br, hr, far) within 0.5 on at least 95% of rows, i.e. answers are on the 0–100
  scale. Otherwise the run stops with no analysis, and a dated addendum is published before anything else.
- **Answers 0 and 100** are kept. The rule part reads them as the intervals [0, 0.5)% and (99.5, 100]%. Non-whole
  answers are rounded to the nearest whole percent for the rule part.
- **Development labels were built differently:** Stengård has no repeats. There the 8 answers are the 10% vs 90%
  pairs at the 4 rule-chosen cells, and the truth comes from the other 37 answers (62 base pairs). Development and
  test numbers are therefore not on the same footing.

## 7. Model (final; `src/mixture_strategies.py`, `src/mixture_eval.py`)
**Primary model: no spikes.**
- K person types. Each answer (a whole percent) comes from one of two parts:
  - a noisy weighted log-odds rule: logit(answer) ~ N(b0 + b1·logit(base) + b2·log(hit/FA), σ²), read at whole-percent
    resolution;
  - a lapse (uniform 0–100).
- EM fit. Pseudo-counts 1. σ ≥ 0.05. 8 seeded restarts; the best by log-likelihood is kept.
- P(neglect | answers) = Σ_k P(type k | answers) · q_k. q_k = the share of 2,000 SIMULATED type-k people labelled
  neglect on the 27 second-showing trials. Predictions are clipped to [0.01, 0.99].

**Selection rule (fixed; applied once to Stengård; never to test data).**
- Candidates: {one evidence weight, separate hit and FA weights} × **K ∈ {1, …, 20}**.
- Choose the lowest 5-fold cross-validated (by person, seed 0) 8-answer log-loss on all 182 Stengård people.
- Ties within 0.001 go to fewer parameters (smaller K, then one evidence weight).
- **K hit the top of the grid twice:** K ≤ 6 picked K = 6 (job 14067), and K ≤ 10 picked K = 10 with spikes and 9
  without (job 14071).
- The grid was then extended once to K = 1–20 (team decision); its pick is final.

  **Result: one evidence weight, K = 14** (interior of the grid; development, chosen among 80 variants).

**Secondary comparison: spike model.** The same plus 7 exact-hit spikes (one per engine method). It is chosen by the
same rule among spike configurations (**one evidence weight, K = 17**; development, chosen among 80 variants), and runs on a Lin set only if the blind check
(§4) allows it.

### 7.1 How the model is fitted and used on Lin (design change of 2026-11-16, team lead)
**Why it changed.**
- On 2026-10-13 the Exp1 test–retest agreement of the neglect label was **κ 0.63** (`results.md`), so labels change
  between showings.
- The model assumes each person has one stable type. In development it was very confident: **78 of 182 people got
  exactly the 0.01 clip**, and 94 fell in the 0–0.1 bin of the nested calibration table (mean p 0.015; development,
  chosen among 80 variants; clip count from job 14181).
- Log-loss punishes confident errors heavily. So against a second-showing truth, the primary endpoint is exposed to
  overconfidence.
- K = 14 was chosen with about **146 training people** per fold (Stengård). A 5-fold fit inside Exp2 would have about
  **66**.

**The design (structure fixed: K = 14, one evidence weight, no spikes; the spike model K = 17).**
1. **Primary fit:** the primary model is fitted **once on all Exp1 people** (our 2026-10-13 copy, §3.1; both showings;
   **no labels** in the fit). EM seed 5, q seed 500, 8 restarts, 2,000 simulated people per type. It is **applied
   unchanged to Exp2 people**. **No Exp2 answer enters the fit.** Each Exp2 person is predicted from their 8
   first-showing answers only.
2. **Recalibration map:** logit(p') = a + t · logit(p), with **t ≥ 0**, fitted by maximum likelihood on the **Exp1
   out-of-fold predictions** (5-fold cross-fitting inside Exp1, seed 0) against the Exp1 second-showing truth. The
   frozen map is applied to the Exp2 predictions, then p' is clipped to [0.01, 0.99] as before. a and t are reported.
3. **Abstention** uses the **raw** probabilities: λ̂ comes from Learn then Test on the Exp1 out-of-fold predictions
   (§8, item 6) and is applied to the Exp1-fitted model's predictions on Exp2. **Calibration (map and λ̂) used
   cross-fitted models; the final model is fitted on all Exp1 people.**
4. **Within-Exp2 5-fold fit** (the earlier primary): fit on the other four folds' Exp2 answers from the same block,
   both showings, no labels. Now a **pre-specified secondary** (§8, item 11).
5. **Spike model (secondary):** the same steps with its own fit, map and Exp1 data, if both blind checks allow it (§4).

## 8. Endpoints
**Single primary endpoint (Lin Exp2, self-paced block, 83 people):**
- **Log-loss skill at 8 answers of p'** (the Exp1-fitted primary model's predictions through the Exp1 recalibration
  map, §7.1) **vs the Exp1 base rate:** skill = 1 − mean LL(p') / mean LL(base rate).
- **Base rate** = the neglect prevalence in Exp1 (second-showing truth, our 2026-10-13 copy), clipped to [0.01, 0.99];
  the same number for every Exp2 person.
- 95% CI: percentile person bootstrap, **20,000 resamples**, seed 0 (numpy `default_rng(0)`), ratio recomputed in
  each resample.
- **Success = lower end of the two-sided 95% interval above 0.** This is a **one-sided test at the 2.5% level.**
  Otherwise we say "no evidence that 8 answers beat the base rate"; we do not say "as good as".
- **What the interval covers:** it is **conditional on the frozen fitted procedure** (the Exp1-fitted model and map).
  It reflects variation across test people, **not** retraining the model on other Exp1 samples.
- **Sensitivity intervals (pre-specified secondaries, same 20,000 resamples and seed):**
  - a **paired BCa interval for the skill** (bias correction from the bootstrap, acceleration from the jackknife over
    people);
  - a **studentized (bootstrap-t) interval for the mean per-person loss difference** (base-rate loss minus model loss).

  For each we report whether it excludes zero. **If either disagrees with the primary interval** (on whether the lower
  end is above 0), **we describe the primary result as not robust to the interval method.**

**Secondary (all reported, none confirmatory):**
1. Accuracy of the primary model (threshold 0.5, every person labelled, coverage 100%) vs the majority guess, for p'
   and for raw p.
2. The ceiling (§6).
3. The spike model's skill (if run, §4), Exp1-fitted with its own map (§7.1).
3a. **The skill of the raw p** (no map) vs the same Exp1 base rate; **the map's a and t.**
3b. **Simple baseline:** a logistic regression of the Exp1 truth label on **one feature**, the mean of (answer at 97%
    base rate − answer at 1% base rate) over the asked cells that have both answers (answers as proportions). Fitted
    by maximum likelihood on Exp1 people, applied unchanged to Exp2; predictions clipped to [0.01, 0.99]. A person with
    no complete pair gets the Exp1 prevalence. Reported: its log-loss skill vs the Exp1 base rate, and the paired
    per-person log-loss difference from the primary model (simple − primary) with a 1,000-resample bootstrap interval.
    **If that interval includes zero, we will say the mixture model shows no demonstrated advantage over a one-feature
    rule at 8 answers.**
4. The same endpoints on **Lin Exp1** (previously analysed).
5. The same endpoints on the **Lin Exp2 time-limited block**, under the rules of §6.1, reported separately and never
   pooled with the primary.
6. **Abstention (Learn then Test)**:
   - **policy:** ask the 8 first-showing items in order; from the 2nd answer on, stop when max(p, 1 − p) ≥ λ and
     commit to the more likely label; otherwise say "not sure yet";
   - **one loss per person** for the whole policy: 1 = committed to a wrong label;
   - **(a) The error rate controlled** is the **share of ALL learners** (committed or not) who get a committed wrong
     label: (number committed and wrong) ÷ (number of learners). People told "not sure yet" count in the denominator
     with loss 0. The **share of committed learners** who are wrong, (committed and wrong) ÷ (committed), is **not
     controlled**. On Exp2 **both** are reported, each with its exact 95% Clopper–Pearson interval;
   - **(b) Threshold grid and multiple-testing rule:**
     - grid: λ = 0.99, 0.98, …, 0.50 (50 values, steps of 0.01);
     - for each λ, H0: risk(λ) > α, tested with the exact binomial p-value P(Binomial(n, α) ≤ number of wrong
       commits);
     - **fixed-sequence testing:** test in the order 0.99 → 0.50 and stop at the first λ with p > δ;
     - λ̂ = the last λ that passed (the lowest passing λ, so the largest coverage). Fixed-sequence testing needs no
       further multiplicity correction: each test is run only if all earlier ones passed;
   - **λ̂ is tuned on Exp1 with the Learn then Test procedure.** No formal Learn then Test guarantee is claimed for
     the Exp1 stage: the Exp1 errors come from cross-fitted models with overlapping training data, and the final
     model is refitted on all Exp1 people, so **no exact guarantee is claimed for the deployed rule**;
   - λ̂ is **tuned on Lin Exp1 people (n = 177)** with **α = 0.10, δ = 0.05**, on the **raw out-of-fold** probabilities
     (5-fold cross-fitted models inside Exp1). It is then used unchanged on the **Exp1-fitted model's raw
     predictions** for Exp2 (§7.1: calibration used cross-fitted models; the final model is fitted on all Exp1
     people);
   - **(c) Largest number of wrong commits that still passes on Exp1:** a λ passes if its wrong commits k satisfy
     P(Binomial(n, 0.10) ≤ k) ≤ 0.05 (the tuning rule).
     - With n = 177 this is **k ≤ 10** (10 wrong of 177 = 5.6%; p = 0.029; 11 wrong gives p = 0.053 and fails).
     - If people are left out by the truth rule (§6.1), the same formula is applied to the n that remains, and that
       k is reported.
     - At least 29 people are needed for any λ to pass (0 wrong: 0.9^29 = 0.047);
   - **(d) If no threshold passes** (λ = 0.99 already has p > δ):
     - **no λ passes:** the tutor commits to no one, every person gets "not sure yet", and coverage is 0%;
     - this is reported as "no threshold passed the Exp1 tuning at α = 0.10, δ = 0.05";
     - no fallback threshold is chosen. The Exp2 risk–coverage table is still reported, as description only;
   - **What is certified, and where: on Exp2.** There the model and the threshold are frozen before any Exp2 answer is
     used, and the people are independent of the tuning. We report the **one-sided exact 95% upper bound**
     (Clopper–Pearson) on:
     - **(a) wrong commits as a share of all learners**, and
     - **(b) wrong commits as a share of committed learners**,

     each with the two-sided exact 95% interval, coverage and accuracy on committed next to it.
     **"Certified at 10%" means that upper bound is at or below 10%.** For (a) with 83 people that allows **at most 3
     wrong commits** (3 of 83: bound 9.1%; 4 of 83: 10.7%). The certificate **applies to people like those in Exp2**
     and is an average over learners, not a promise about any one learner. We also report whether the point estimate
     is at or below α = 10%;
   - also reported on Exp2: mean items asked, the risk–coverage table and AURC. **Committed accuracy is never shown
     without coverage;**
   - **(e) Coverage on Lin may be lower than in development** (73.1% on Stengård; development, chosen among 80
     variants). Reasons:
     - λ̂ is tuned on one set of 177 people with an exact test, which is stricter than the cross-fold λ of
       development;
     - the 8 asked items, base rates (1% and 97%) and truth label differ from Stengård (§6);
     - Exp2 people may differ from Exp1 people.

     A lower coverage is reported as found, not treated as a failure;
   - tuning-size uncertainty: n = 177; the minimum n for any λ to pass (29); λ̂ with its bootstrap 2.5 / 50 /
     97.5% quantiles; the Clopper–Pearson interval of the calibration risk.
7. Calibration table of the primary model.
8. **Questions asked before committing (Exp2, at λ̂ from Exp1):**
   - among committed people, the number of answers used (2–8): mean, median and the count at each number;
   - the mean has a 95% person-bootstrap CI (§6.1).
9. **Share of people never labelled (Exp2, at λ̂ from Exp1):**
   - the people still "not sure yet" after all 8 answers, as a share of all learners (= 1 − coverage);
   - with an exact 95% Clopper–Pearson interval;
   - 100% if no threshold passed (d).
10. **Exp1 version check (after the primary run):**
    - **the whole Exp1 stage** (§7.1: out-of-fold predictions, recalibration map, λ̂, final fit on all people) is
      repeated on the **current GitHub version** of the Exp1 file (§3.1), after its own blind check and scale guard;
    - reported: **both thresholds and both maps** (our 2026-10-13 copy and the GitHub version) with their calibration n;
    - **both Exp2 results:** the skill of p' and of raw p, and the abstention check (item 6, both error rates,
      coverage, items, never labelled), on Exp2 self-paced and time-limited, for each Exp1 version;
    - **the primary result uses our 2026-10-13 copy;** this check never replaces it.
11. **Within-Exp2 5-fold fit** (§7.1, item 4) on each Exp2 block: skill of raw p and of p' (the same Exp1 map), each
    against the Exp1 base rate and against the within-Exp2 training base rate (the other folds' prevalence).

**Exploratory:**
- block order (39 vs 44);
- format;
- the frozen learner profile on the same 8 answers (coverage always reported with accuracy);
- a Stengård-fitted population applied unchanged (transfer);
- Enke & Graeber weights (§2.2).

## 9. Procedure and safeguards
**Order of work (fixed). No Lin answer is read before the v10 tag is public.**
1. **Write `src/mixture_lin.py`** to implement §4, §6, §6.1, §7 and §8 exactly. *(Done 2026-11-16; revised the same
   day for §7.1.)*
2. **Test it only on made-up data in the Lin file layout:** SYNTHETIC CSVs with the same columns as
   `data/Exp1/df.csv` and `data/Exp2/Exp_2.csv`. The made-up data includes missing answers, `invalid_input` flags,
   0 / 100 answers, a slope of exactly 0.2 and non-whole answers. No real Lin file is opened by the tests.
3. **Hash** the script and the model files (SHA-256) and write them into a frozen record. *(Done 2026-11-16; re-done
   2026-11-17 after the §7.1 change and after the statistical review, below.)*
4. **Freeze and publish v10** (this plan + the hashes) in the public pre-registration repository; the tag must be
   public before step 5. *(Done 2026-11-17.)*
5. **Blind whole-number check and answer-scale guard** on Exp1 and on Exp2 (§4): counts and the answer range only.
6. **Exp1 run** (our 2026-10-13 copy): 5-fold cross-fitting inside Exp1 → recalibration map and λ̂; the final model
   fitted on all Exp1 people; the Exp1 secondary endpoints.
7. **Exp2 run, once:** the Exp1-fitted model and map applied unchanged; primary endpoint first, then the secondaries
   (self-paced, then time-limited; the within-Exp2 5-fold fit last).
8. **Exp1 version check** (§8, item 10): blind check and scale guard on the GitHub version of Exp1, then its
   calibration and both thresholds applied to Exp2.

**Frozen code (step 3; done 2026-11-16, re-done 2026-11-17 after the §7.1 change and again after the statistical
review, and after the pre-flight check).** Record `logs/mixture_lin_frozen.json`, written at commit cceb0ed9… (the
earlier hashings, commits 2ab90a46…, ea1094db… and a9d2ae2a…, are kept in the record as superseded); only
`src/mixture_lin.py` changed each time;
the list is every module under `src/` that the run imports (checked when hashing). SHA-256:

| File | SHA-256 |
|---|---|
| src/mixture_lin.py | 54a85b7091b0e99e04963e4d930904bb6f8d2ef848f0aa69ed1be2b49e708023 |
| src/mixture_strategies.py | df8336f85e66f4d5e9e3eddd832bacd6f8a93c02eae3149e5bcd5cc716b12660 |
| src/mixture_eval.py | ca8e785e928f14a0cb0e0e4a9ed0ee0481244ce31053b35e7833eb1a7b546690 |
| src/stengard_sensitivity.py | 3193d49746176af35fc656faf0ccaabb60fc02fb3ad981c367192a860b6193a9 |
| src/stengard_analysis.py | a07123908756f328d1184a70d7126a462678b5931854fa3f83706a413ecc4daa |
| src/bayes_strategies.py | 4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e |
| src/topic_engine.py | 3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a |

Also recorded (not checked by the script): jobs/mixture_lin_cpu.sbatch 03da799b…, tools/make_fake_lin.py 2e91f0fc…,
tests/test_mixture_lin.py, the Python environment list (logs/venv_stengard_freeze.txt 76dd4ebd…; Python 3.12.9,
numpy 2.5.3, scipy 1.18.1). The record's `v10_public_url` stays empty until the tag is public; until then the script
refuses every real file.

Safeguards:
- The script refuses to run unless the SHA-256s of it and the model files match the frozen record.
- It refuses any data file whose fingerprint differs from §2.1 / §3.1.
- The Exp2 run refuses to start without the Exp1 λ̂ output.
- Each run is a Slurm job writing its own output file (`logs/<name>_<SLURM_JOB_ID>.json`, never overwritten).
- **Each output stores every person's** id, truth label, raw and mapped prediction, simple-baseline prediction, commit
  decision (committed or not, and the label) and number of answers used (plus the within-Exp2 and spike predictions
  where run), so every reported number can be recomputed. These files stay in the private repository.
- Changes after publication: a dated addendum, published before the run it affects.

## 10. Development record (Stengård; REAL participants unless marked SYNTHETIC)
**Label for every model number in this section: development, chosen among 80 variants.** Checks that involved no
choice among variants are marked "development check"; synthetic numbers are marked SYNTHETIC.

**All performance numbers are out-of-sample by person:**
- top level: 5-fold CV by person for each configuration;
- **nested:** the §7 rule is applied inside each outer fold to an inner 5-fold CV of the outer-training people only;
- abstention: λ calibrated on the other folds' people and applied to the held-out fold;
- the training base rate for the skill score comes from the other folds.

**Model variants tried in development:**
- **80 distinct configurations:** 2 rule-feature kinds × spikes on/off × K = 1–20, from 5 development runs.
  - **Used:** job 14102 (all 80); job 14071 (40, K ≤ 10); job 14067 (12, K ≤ 6, spikes on).
  - **Not used:** job 14068 (failed, K = 1 only); job 14069 (cancelled); an interrupted login-node run (4).
- All earlier configurations are a subset of the 80. The selection rule (lowest CV log-loss) was the only rule used;
  clipping, restarts, σ floor and simulation size were fixed from the start and never tuned.

**Nested estimates, 182 people (development, chosen among 80 variants).** 55 / 182 labelled neglect (30.2%); training base-rate log-loss 0.615.

| | **Primary: no spikes** (rule → evidence, K 14) | Secondary: spikes (rule → evidence, K 17) |
|---|---|---|
| Chosen in the 5 outer folds | evidence K17, K19, K16, K18, K16 | separate K20, evidence K15, separate K19, evidence K20, evidence K19 |
| **Log-loss skill vs training base rate [95% CI]** | **0.573 [0.478, 0.657]** | 0.462 [0.333, 0.560] |
| Log-loss (model) | 0.262 | 0.331 |
| Accuracy, coverage 100% (majority 0.698) | 0.901 (+0.203 [+0.126, +0.280]) | 0.863 (+0.165 [+0.088, +0.242]) |
| AURC | 0.025 | 0.043 |
| By file, log-loss diff vs majority | data_11 −0.333, data_12 −0.350 | data_11 −0.268, data_12 −0.278 |

- The configuration chosen at top level (no spikes, evidence, K 14) scores skill 0.574 in plain CV, matching the
  nested 0.573. Choosing among 80 variants added little optimism.

Calibration (nested; development, chosen among 80 variants; bin: n, mean p → observed):

| bin | 0–0.1 | 0.1–0.3 | 0.3–0.5 | 0.5–0.7 | 0.7–0.9 | 0.9–1 |
|---|---|---|---|---|---|---|
| primary | 94: 0.01 → 0.00 | 12: 0.21 → 0.25 | 17: 0.42 → 0.24 | 24: 0.61 → 0.79 | 32: 0.79 → 0.81 | 3: 0.92 → 1.00 |

**Abstention, cross-fold (λ from the other folds; α 0.10, δ 0.05; development, chosen among 80 variants):**

| | primary (no spikes) | spikes |
|---|---|---|
| λ per fold | 0.82, 0.76, 0.82, 0.82, 0.82 | 0.80, 0.81, 0.80, 0.81, 0.83 |
| Held-out risk (committed and wrong) [Clopper–Pearson 95%] | 6.6% [3.5, 11.2] | 6.6% [3.5, 11.2] |
| **Coverage / accuracy on committed** | **73.1% / 91.0%** | 68.1% / 90.3% |
| Items asked (mean of 8) | 4.2 | 4.5 |
| Committed labels (neglect / uses) | 21 / 112 | 15 / 109 |

**Other checks:**
- **h/f** (development, chosen among 80 variants; held-out log-likelihood of all answers per person, separate − one evidence weight, at the chosen K): no
  spikes K 14: +2.37 [0.81, 3.97]; spikes K 17: +1.17 [0.01, 2.30]. Separate weights predict raw answers better, but
  the rule, which targets the 8-answer label, chose the single evidence weight.
- Frozen learner profile on the same 8 answers (development check; the profile is frozen, no variants): **coverage 75.3% / accuracy on committed 91.2%**; 68.7% with not sure
  counted wrong.
- **Recalibration step (development check, NOT a new variant choice;** job 14181, `src/mixture_recal_dev.py`,
  `logs/mixture_recal_dev_14181.json`). The map of §7.1 fitted on the out-of-fold predictions of the training people
  in each outer fold (inner 5-fold CV, seed 1) and applied to the held-out fold; skill vs the training base rate:

  | | raw p | p' (mapped) | map t per outer fold (a) | at the 0.01 / 0.99 clip, raw → mapped |
  |---|---|---|---|---|
  | nested (job 14102's per-fold choices) | 0.573 [0.478, 0.657] (reproduces job 14102) | 0.561 [0.441, 0.667] | 1.18, 1.41, 1.18, 1.32, 1.24 (a −0.23 to 0.42) | 78 → 83 of 182 |
  | final configuration (evidence, K 14) in every fold | 0.574 [0.472, 0.658] | 0.564 [0.443, 0.662] | 1.05, 1.24, 0.97, 1.06, 1.13 (a −0.02 to 0.26) | 79 → 52 of 182 |

  On Stengård the map mostly **sharpened** (t > 1) and lowered skill by about 0.01. There the truth is built from the
  same session's other 37 answers. On Lin the truth is the second showing, which agrees less with the first (κ 0.63),
  so the map may soften there; it is fitted on Exp1 and only then used.
- **Ceiling:** cannot be computed on Stengård (no repeats). It is reported first on Lin (§6).
- **SYNTHETIC** (job 14066; `logs/mixture_synthetic_14066.json`, `logs/mixture_recovery_14066.json`):
  - planted types: 4 / 5 recovered on the Stengård design, 5 / 5 on the Lin design;
  - strategy confusion ≥ 99.7% on both 8-item sets, so nothing needs merging;
  - parameter recovery: r 0.57–0.96;
  - model recovery by BIC: structure 91.7%, K 77.1%. The CV-log-loss rule itself was not put through model recovery.

## 11. What this means (plain words)
- On new Stengård people, the spike-free model's 8-answer predictions were far better than guessing the base rate
  (development, chosen among 80 variants).
- Lin differs: more extreme base rates (1% and 97%), a different truth (second showing) and a different population.
  The development numbers are not a forecast for Lin.
- The ceiling (§6) shows how much any 8-answer method can achieve there.
- On Lin the model learns from Exp1 people only and is then tested on new people (Exp2), like a tutor trained on one
  class and used with the next. The map adjusts how confident the predictions are, softening or sharpening them,
  using what Exp1 showed; the baseline is what we would guess knowing only how common neglect was in Exp1.
- On Stengård the map sharpened rather than softened (t > 1) and cost a little skill (§10). There the truth comes from
  the same session's other answers; on Lin it comes from a second showing, which agrees less (κ 0.63).

## 12. Open items (all closed before publication)
1. ~~Whether Exp2 typed entry counts as documented.~~ Decided 2026-11-16: not documented. The spike model runs on
   Exp2 only if the blind whole-number check passes (§4).
2. ~~Script written and tested on made-up data; code hashed.~~ Done 2026-11-16, re-done after the §7.1 change (§9).
3. ~~Independent statistical review (2026-11-17).~~ Folded into this plan before publication (wording of §8 items 6
   and the primary endpoint; 20,000 resamples; sensitivity intervals; simple baseline; per-person output; §9).
4. ~~Pre-flight data check, baseline wording, README citation (2026-11-17).~~ Added before publication (§4, §8, §9).
5. ~~Approval of this text.~~ Approved 2026-11-17; published as v10. Next: §9 steps 5–8, each only when the team lead
   says so.

## References
- Angelopoulos, A. N., Bates, S., Candès, E. J., Jordan, M. I., & Lei, L. (2021). Learn then Test: Calibrating
  predictive algorithms to achieve risk control. arXiv 2110.01052.
- Cheng, Y. (2009). When cognitive diagnosis meets computerized adaptive testing: CD-CAT. *Psychometrika*, 74(4),
  619–632. doi 10.1007/s11336-009-9123-2.
- Cohen, A. L., & Staub, A. (2015). Within-subject consistency and between-subject variability in Bayesian reasoning
  strategies. *Cognitive Psychology*, 81, 26–47. doi 10.1016/j.cogpsych.2015.08.001.
- El-Gamal, M. A., & Grether, D. M. (1995). Are people Bayesian? Uncovering behavioral strategies. *JASA*, 90(432),
  1137–1145. doi 10.2307/2291506.
- Enke, B., & Graeber, T. (2023). Cognitive uncertainty. *QJE*, 138(4), 2021–2067. doi 10.1093/qje/qjad025; NBER WP
  26518 (rev. Jan 2021); data doi 10.7910/DVN/IQ47ZB.
- Lin, Y., Zhu, J.-Q., Spicer, J., Li, Y.-X., Chater, N., & Sanborn, A. N. (2026). Integrating heuristics and mental
  sampling in belief updating. PsyArXiv, doi 10.31234/osf.io/wgpb2_v1. Data/code: github.com/LinYitong1/belief-update.
- Lin, Y., Sanborn, A. N., & Chater, N. Integrating heuristics and mental sampling in belief updating. Manuscript
  submitted to *Journal of Experimental Psychology: General* (the citation the data repository's README asks for).
- Stengård, E., Juslin, P., Hahn, U., & van den Berg, R. (2022). On the generality and cognitive basis of base-rate
  neglect. *Cognition*, 226, 105160. doi 10.1016/j.cognition.2022.105160.
- Xu, C., & Yu, X. (2026). Probe before you preach: Conformal ambiguity sets and neuro-symbolic counterfactual probing
  for diagnosing algebraic misconceptions in middle school mathematics. arXiv 2611.14557.
