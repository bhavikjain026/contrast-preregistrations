
---

## 2026-10-12 — PLAN, CONFIRMATORY (recorded before any engine run): our engine vs human error codes, OSF p37nz
**Source:** Pighin, S., Tentori, K., & Filimon, F. "The impact of problem domain on Bayesian inferences: A systematic
investigation", OSF project p37nz (data, 2023-06-13) and pre-registrations 2da5k (Study 1), ckwde (Study 2), cfmvk
(Study 3). **No licence stated** → default copyright: raw data and stimuli stay on scratch
(`/scratch/bhavik.jain.ug26/data/osf_p37nz/`), never in git; only derived numbers here; cite the source.
Deadline: if not done and checked by 2026-10-22, it stays out of the abstract (abstract not edited here).
**What was looked at before this plan** (structure only, no engine run, no comparison with codes): coding sheets,
supplementary doc, pre-registered stimuli PDFs, column types, answer denominators.
**Data.** Between-subjects, one answer per person (IDs unique). Study 1 (open question): 762 people; Study 3 (open
question): 729. **Study 2 is excluded**: multiple choice, the "answer" is the chosen option, which IS the code — there
is nothing for the engine to infer. Answer = Numerator / Denominator ("how many of these … out of …"), in points.
**Problem numbers** (from the pre-registered stimuli; identical across domains and evidence types):

| Value combination | Base rate | Hit rate | False alarm | Correct |
|---|---|---|---|---|
| VC1 | 7 / 1000 | 6 / 7 | 50 / 993 | 6 / 56 = 10.7% |
| VC2 | 10 / 1000 | 8 / 10 | 79 / 990 | 8 / 87 = 9.2% |
| VC3 | 13 / 100 | 9 / 13 | 20 / 87 | 9 / 29 = 31.0% |

Mapping of the files' value column (checked with answer denominators unique to one combination, NOT with codes):
Study 1 Values 1/2/3 → VC1/VC2/VC3 (unique-denominator answers 72/5/0, 0/45/0, 0/5/71); Study 3 Value 1 → VC2,
Value 2 → VC3 (0/65/0, 2/8/113) — the Study 3 codebook's "2 / 3" are the combination numbers.
**Exclusions:** missing or non-numeric numerator/denominator, denominator 0, numerator > denominator (answer > 100%):
Study 1 5, Study 3 4 (the last rule). Counts reported.
**Engine labelling** (frozen `src/bayes_strategies.py` formulas, same 1-point tolerance as the Woike analysis,
`TOL = 1.0` point + 1e-7): correct if within 1 point of the correct answer (checked first, as for Woike); otherwise
the set of the six wrong strategies within 1 point → exactly one = that strategy; two or more = **ambiguous**; none =
**no match**.
**Mapping of our methods to their error codes (fixed now):**

| Their code | Their label | Our engine |
|---|---|---|
| 0 | no error (correct) | correct (Bayes) |
| 1 | Sensitivity | hit_rate |
| 2 | Base-rate only | base_rate_only |
| 3 | Evidence only | **no match in our six** (≈ positives / total, (TP+FP)/N) — unrepresentable |
| 4 | Joint occurrence | joint_occurrence |
| 5 | Specificity | false_alarm_complement (1 − FA = specificity) — the files do not define code 5; if the authors also coded answers equal to the false-positive rate as "Specificity", those will show as disagreements (reported) |
| 6 | Other | likelihood_subtraction, equal_priors (no code of theirs), and engine "no match" |

Ambiguous engine sets: if all members map to the same code, that code; otherwise "ambiguous" (its own category).
Separability on these numbers (from the formulas, before any answer): VC1 and VC2 — base rate only vs joint
occurrence within 1 point; VC1 — FA complement vs equal priors within 1 point. Such answers will be ambiguous.
**Metrics** (pooled Studies 1 + 3, and per study; 95% CIs from 1,000 bootstrap resamples of people, seed 0):
- **Agreement %**: engine code = their ERRtype, over all included answers (ambiguous and their code 3 count as
  disagreement); also reported excluding their code 3 (unrepresentable).
- **Cohen's kappa** on the same pairs (engine categories 0, 1, 2, 4, 5, 6, ambiguous vs their 0–6).
- **Per-code confusion table** (their code × engine label), with each code's agreement.
- **Coverage**: share of included answers the engine labels with exactly one method (correct or one of the six);
  ambiguous and no match are not covered. Agreement also reported within covered answers.
- Descriptive: among their code 3, how many equal (TP+FP)/N within 1 point; among their code 5, how many equal 1 − FA
  vs FA; among ambiguous answers, whether their code is one of the set's codes.
