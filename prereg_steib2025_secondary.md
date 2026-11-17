# Plan v13: secondary analysis of the Steib et al. (2025) open trial data — analysis plan posted before analysis

**Status: FINAL. Approved by the team lead on 2026-11-17 and released as v13** in the public pre-registration
repository (file `prereg_steib2025_secondary.md`), before the analysis was run. Written 2026-11-17 before any score or
label of the data file was read (only the sheet name, the header row, the description row and the file size were
looked at); five changes decided from published metadata were made the same day, also before any outcome was read.
(Tag v11 is reserved for the trial's final addendum.)

The trial's main results are already published, so this is **an analysis plan posted before our analysis**, not a
pre-registration of the trial.

## 1. Source and licence
Steib, N., Büchter, T., Eichler, A., Binder, K., Krauss, S., Böcherer-Linder, K., Vogel, M., & Hilbert, S. (2025).
How to teach Bayesian reasoning: An empirical study comparing four different probability training courses.
*Learning and Instruction*, 95, 102032. https://doi.org/10.1016/j.learninstruc.2024.102032. Open access, CC BY 4.0.
Data: the article's supplementary file `1-s2.0-S0959475224001592-mmc6.xlsx` (CC BY 4.0), stored outside GitHub
(`data/realdata/steib2025/`, git-ignored), **SHA-256 b5e06520ddd15c8bf72de0ebe4c83e25328dfc57d72ddb22a173c238e8a14f84**.
All credit for the trial, the tasks, the scoring and the strategy labels belongs to the authors. We use their data
under CC BY 4.0; we change nothing in it and publish no row of it.

## 2. What is known about the file (structure only)
- One sheet (`Tabelle1`), 515 students; row 2 is a description row (dropped, as in the authors' R script).
- Columns used: `subject` (Jura = law, Medizin = medicine), `group` (1 double tree, 2 unit square, 3 natural
  frequencies, 4 school tree, 5 control), and for each task the 0/1 score (`…_Dummy`) and the authors' strategy label
  (`…_Strategy`): pre-test d1, d1\*, d2, d3; post-test d4, d5, d1, d1\*, t1; follow-up d6, d7, d1, d1\*, d4, t2.
  ID, grade, gender, age, semester, notes and sums are **not used and not written anywhere**.
- Strategy labels (as listed for us): correct; guessing; PPV- or NPV-prefixed Fisherian, Joint occurence, Base-rate
  only, Likelihood-substr., Pre-Bayes, Evidence only; and PPV-Likelihood.
- There are **no typed answers**, so our engine cannot be run on this file; every label is the authors'.
- d1 and d1\* are asked at all three time points.
- **Task inputs** (base rate / hit rate / false-alarm rate, %) are published in the paper (Table 1 and Supplement A.1);
  each reproduces the answer key in the file's description row (checked by the script, which stops if one does not):

  | Task | Law: inputs → key | Medicine: inputs → key |
  |---|---|---|
  | d1 | 50 / 85 / 10 → 89.47 | 6 / 97 / 2 → 75.58 |
  | d2 | 41 / 10 / 3 → 69.85 | 6 / 80 / 10 → 33.80 |
  | d3 | 10 / 93 / 50 → 17.13 | 5 / 96 / 2 → 71.64 |

- **Collisions**, computed from these published numbers only (our six wrong methods; "within 1 point" inclusive):

  | Task | Wrong method within 1 point of the correct answer | Wrong methods within 1 point of each other |
  |---|---|---|
  | law d1 | equal priors h/(h+f) = 89.47 = correct; false-alarm complement 1 − f = 90.0 (0.53 from correct, just outside the authors' ±0.5 rule) | false-alarm complement ~ equal priors 0.53 |
  | law d2 | none | none |
  | law d3 | none | base rate only ~ joint occurrence 0.7 |
  | medicine d1 | none | base rate only ~ joint occurrence 0.18; false-alarm complement ~ equal priors 0.02; hit rate ~ equal priors 0.98; hit rate ~ false-alarm complement 1.0 |
  | medicine d2 | none | none |
  | medicine d3 | none | base rate only ~ joint occurrence 0.2; false-alarm complement ~ equal priors 0.04 |

  So on law d1 "ignore the base rate" in the equal-priors form is scored correct. On the NPV task d1\*, the law key
  (85.71; printed 85.72) also equals the value from ignoring the base rate, (1 − f) / ((1 − f) + (1 − h)); the medicine
  key (99.80) does not (97.03).

## 3. Definitions
- **Wrong answer:** score 0. Score missing = not answered: left out of that task's denominators, counted and reported.
- **Label normalisation (spelling only):** case, spaces and hyphens are ignored when matching a label to the list
  (e.g. "Joint occurrence" = "Joint occurence"). A label not on the list is kept under its own name as
  "unlisted: …", reported, and never dropped or merged.
- **Known-error label:** any PPV- or NPV-prefixed method label. Not known-error: correct, guessing, unlisted, empty.
- **The four shared methods:** Fisherian (= our hit-rate method), Joint occurence (= joint occurrence), Base-rate
  only, Likelihood-substr. (= likelihood subtraction). Our other two methods (false-alarm complement, equal priors)
  have no label of their own here.
- **Training arms:** groups 1–4 pooled. **Control:** group 5.
- **Reporting order:** every analysis by subject (law, medicine) first, pooled second.
- **Intervals:** exact Clopper–Pearson 95% intervals for every share. Differences of two independent shares: Newcombe's
  hybrid score interval (method 10). Bootstrap where stated: 10,000 resamples of students, seed 0, percentile.
  Shuffles: 10,000, seed 0. **No p-values except the one contrast in §4.3.**

## 4. Analyses

### 4.1 How common each wrong method is at pre-test
For each PPV task (d1, d2, d3), for the three PPV tasks with answers pooled, and for the NPV task d1\* separately:
among wrong answers, the share with each label (incl. guessing, empty and unlisted), and the share covered by the
four shared methods. **This share is a lower bound for our six methods:** answers from our other two methods may sit
under other labels (e.g. guessing, Pre-Bayes, Evidence only), and on law d1 equal-priors answers are scored correct
(§2). Because Base-rate only and Joint occurence nearly coincide on medicine d1 and d3 (§2) and the authors' tie rule
is unknown, the share of those two labels **combined** is also reported. In the pooled-answers figure one student
contributes up to three answers; the exact interval treats answers as independent and is therefore too narrow — it is
reported as descriptive.

### 4.2 Consistency within a person at pre-test
**Primary:** the share of students wrong on at least two of d1, d2, d3 whose wrong-task labels are all the **same
known-error label** (denominator: all students wrong on at least two of d1, d2, d3), with an exact interval. Compared
with the share expected if labels were shuffled between students of the same subject, using the same definition:
within each subject and task, the labels of that task's wrong answers are permuted among the students wrong on it
(who is wrong stays fixed), 10,000 times; we report the mean and the 2.5–97.5% range of the shuffled share.
**Secondary:** the same with any label (incl. guessing and empty) counting, same denominator and shuffle, with a count
of which label the consistent students share (also given for the primary). **Sensitivity:** the primary with
Base-rate only and Joint occurence treated as one label (§4.1). No p-value.

### 4.3 Change over time on d1 — the one pre-specified contrast
Tables of the d1 label at pre-test → post-test, pre-test → follow-up, and pre → post → follow-up, as counts, for the
four training groups pooled and for the control group.
**Pre-specified contrast (the only test):** among students with a known-error label on d1 at pre-test and a follow-up
d1 score, the share correct on d1 at follow-up, **training minus control**, pooled over subjects, with a Newcombe
interval and a two-sided Fisher exact p-value. The same difference by subject is reported with its interval and no
p-value. Also, for the control group, the share whose follow-up d1 label equals their pre-test d1 label (exact
interval); denominator: control students with a known-error d1 label at pre-test and a d1 label at follow-up.
**Caution written in advance:** on law d1 "correct at follow-up" includes any student who ignores the base rate in the
equal-priors way (§2), so the medicine figure is the cleaner one. Students without a follow-up d1 score
are counted and reported, not imputed.

### 4.4 A collision prediction, stated before looking
Prediction: at pre-test, law students' share correct on d1 will exceed their share correct on d2 and d3, and this gap
will be larger than the same gap for medical students, whose d1 has a 6% base rate.
- Reported: share correct on d1, d2 and d3 for law and for medicine (students with all three scores), the gap
  d1 − mean(d2, d3) for each subject (also d1 − d2 and d1 − d3), and the **difference of gaps (law − medicine)** with a
  bootstrap interval (students resampled within subject).
- No wrong method lies within 1 point of the correct answer on d2 or d3 in either subject (§2), so **d2 and d3 are
  clean comparison tasks in both subjects.**
- **Suggestive only:** item difficulty can also explain a gap; d1, d2 and d3 differ in more than the base rate.
- A pooled re-analysis (Woike, Hertwig & Gigerenzer, 2023) reportedly found this method in only about 1% of answers,
  so **a small or zero gap is the likely outcome.** We report the result either way.

### 4.5 Descriptive only
Pre-test label (d1, d1\*, d2, d3) by training group, as counts, by subject and pooled, also with Base-rate only and
Joint occurence combined (§4.1). No tests.

## 5. Checks reported with the results (not exclusions)
Number of students (the run stops unless it is 515); students by subject and group; scores missing; score 1 with a
label other than correct; score 0 labelled correct; score present with no label; every unlisted label with its count.

## 6. Limits
- The labels are the authors'; their matching rule is not yet known to us (we have asked the lead author). "guessing"
  probably means that no known method matched.
- Each label comes from a single answer.
- No group received teaching aimed at an individual's error, so **nothing here can show that targeted teaching works.**
- Completers only; German law and medical students; not our tutor and not our problems.
- Base-rate only and Joint occurence give nearly the same answer on medicine d1 (0.18 points) and d3 (0.2), and
  0.7 points apart on law d3; the authors' rule for such ties is unknown, so the split between those two labels may
  be arbitrary there (hence the combined figures).
- On law d1 the equal-priors way of ignoring the base rate is scored correct, and on law d1\* ignoring the base rate
  gives the correct NPV; those answers are invisible in the labels.

## 7. Procedure
1. Script `steib2025/steib_analysis.py` tested on MADE_UP data in the same layout (`steib2025/make_fake_steib.py`,
   identical header; `steib2025/test_steib_analysis.py`, 22 tests). SHA-256 of the script:
   **3edea828f11f74657176d29006e1f58b0aea20667eeee53a886d37e47254edbb**, recorded in `steib2025/frozen.json`.
2. The script refuses the real file unless its code matches the frozen record, the record names the public v13 tag,
   and the data SHA-256 matches; in made-up mode it refuses the real file.
3. After this plan is approved and published byte-identical with tag v13: one run (`jobs/steib2025_cpu.sbatch`), the
   output (derived numbers only) logged in `results.md`, and every result reported whatever it shows.
4. Any change after publication is a dated, published addendum before any rerun.
