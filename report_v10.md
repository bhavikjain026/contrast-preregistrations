# Report v10: diagnosing base-rate neglect from 8 answers (Lin et al. 2026, Experiment 2)

**Plan:** v10 (tag v10, `prereg_lin_mixture.md`, SHA-256 05ef4c94…), published on 17 November 2026 before any Lin
answer was read for it. **Run once** for the primary on 17 November 2026 (Exp2 stage, frozen code
`src/mixture_lin.py` 54a85b70…). **Real adults** from the open data of Lin et al. (2026); only derived numbers are
reported here.

Every number below is copied from the stage output `mixture_lin_exp2_14236.json` (SHA-256 in section 6) or, for the
Exp1 stage, from `mixture_lin_exp1_14227.json`. The output files are not published, because they hold per-person
predictions.

## 1. Primary (plan section 8)

Lin Experiment 2, self-paced block, 83 people, none left out.

- **Log-loss skill of the Exp1-fitted model's mapped predictions against the Exp1 base rate: 0.671, 95% percentile
  interval [0.550, 0.763]** (20,000 resamples).
- **Success**, under the plan's rule: the lower end is above 0.
- **Robust to the interval method:** BCa interval [0.492, 0.745]; studentized interval for the mean per-person loss
  difference 0.419 [0.324, 0.474]. Both exclude 0.

## 2. Secondary (all reported, none confirmatory)

- **Accuracy** (threshold 0.5, everyone labelled): 0.964 (80 of 83, derived) against 0.699 for always choosing the
  majority label (58 of 83, derived); difference +0.265 [0.181, 0.361].
- **Raw predictions, no map:** skill 0.774 [0.556, 0.912].
- **Simple one-feature baseline (secondary 3b):** skill 0.687 [0.552, 0.777]. Paired log-loss difference, simple
  minus primary, −0.010 [−0.035, 0.015]. **The interval includes zero, so under the plan's wording: the mixture model
  shows no demonstrated advantage over a one-feature rule at 8 answers.**
- **Ceiling** (first against second showing): agreement 0.940 [0.880, 0.988], κ 0.855 [0.712, 0.970]. The model's
  accuracy is above this "ceiling", so it is not a hard bound.
- **Spike model:** mapped skill 0.592 [0.439, 0.715], raw 0.621 [0.383, 0.795].
- **Within Exp2, 5-fold:** raw 0.741 [0.507, 0.915].
- **Abstention at λ̂ = 0.97** (tuned on Exp1): 59 of 83 committed (coverage 71.1%), 1 wrong. Wrong commits as a
  share of all people 1.2% (one-sided 95% upper bound 5.6%), of committed people 1.7% (upper 7.8%): **certified at
  10% on both**, for people like those in Exp2. Accuracy on committed 98.3%. Never labelled 28.9%.
- **Time-limited block** (separate, never pooled): 61 labelled, 22 left out by the plan's truth rule. Mapped skill
  0.478 [0.309, 0.632]; simple-baseline difference +0.058 [−0.031, 0.178]; 35 of 61 committed, 1 wrong: certified
  on the share of all people, not on the share of committed people (upper bound 12.9%).
- **Exp1 stage** (people analysed before, secondary 4): out-of-fold mapped skill 0.316 [0.197, 0.423], in sample and
  optimistic; λ̂ 0.97 with 10 wrong commits of 177, the largest number that passes.
- **Exp1 version check:** the GitHub version of the Exp1 file gave identical results.

## 3. What it does not show

- It predicts a label of base-rate neglect, judged against the same people's later answers. It is not a diagnosis of
  why a person answers as they do, and not a learning result.
- The primary interval is conditional on the frozen fitted model; it does not cover refitting on other Exp1 samples.
- A one-feature rule did as well, so the result supports "8 answers predict neglect", not "our mixture model is
  needed".

## 4. Deviations and disclosures

- **History rewrite (17 November 2026).** The Exp1-stage output stored 177 platform-style participant codes from our
  copy of the Lin data. They were replaced by E1-001…E1-177, and the private history was rewritten. The registered
  script and the plan were unchanged.
- **Interval reported in one place with 1,000 resamples.** The Exp1 version check printed [0.541, 0.755] for the
  same skill, from the 1,000-resample per-block report. The registered primary interval is [0.550, 0.763], from
  20,000 resamples.

## 5. Seen before the run

As disclosed in plan section 3: Lin Experiment 1 had been analysed before. Experiment 2 had not.

## 6. Files

| File | SHA-256 |
|---|---|
| `mixture_lin_exp2_14236.json` (not published: per-person predictions) | `c0e762437f0daa445ea1579ae614ece276fe1b8d3cdd76299aadd693ba9f0141` |
| `mixture_lin_exp1_14227.json` (not published: per-person predictions) | `fb396d8fd1d0ca41e305680d209504b91e7d5382764e7321bf60244c66686da5` |
| `src/mixture_lin.py` | `54a85b7091b0e99e04963e4d930904bb6f8d2ef848f0aa69ed1be2b49e708023` |

Written 20 November 2026, from the saved outputs of the single runs.
