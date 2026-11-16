# Pre-registration v12: Contrast-Lite v2, stage 1 on Stengård et al. (2022) — a small exploratory development check

**Status: FINAL. Approved by the team lead on 2026-11-17 and released as v12** in the public pre-registration
repository (github.com/bhavikjain026/contrast-preregistrations, file `prereg_contrast_lite_stage1.md`), **before any
Stengård answer was read for this check and before the rule was run on any real data.** Changes from here on are
dated addenda. v11 stays reserved for the trial's final addendum. The private file keeps its drafting name
`contrast_lite/prereg_contrast_lite_DRAFT.md`.

## 1. What this check can and cannot show
- **There is no success criterion.** Whatever the result, it will be described as an exploratory stage-1 check on
  development data, and it will not be cited as evidence that the kit's method labels are correct.
- **It cannot test the kit's labels.**
  - The kit names a method only after stage 1 has agreed on all three inputs (base rate, hit rate, false-alarm rate)
    over 12 distinct questions, and then a formula fit.
  - No dataset we hold has that design (`contrast_lite/design_check.md`).
  - So **only stage 1 is checked, for the base rate and the false-alarm rate.** No method label is formed, and there
    is **no formula gate** (team decision, 2026-11-17).
- **Both inputs reuse the same 4 questions.** Stengård has exactly 4 items that pass the kit's question rules: a
  2 × 2 square. Its two base-rate pairs and its two false-alarm pairs are made of those 4 items. The kit itself
  requires 12 distinct questions; this deviation is stated here.
- **Stengård is development data.**
  - The symbolic groups were the v10 development set (all model choices) and were used earlier for tutor development.
  - The pictorial groups had their answers read for the v10 order check.
  - This is therefore an **exploratory development check, not a test**. The team has seen these data; the kit was not
    tuned on them.
- **The two questions of a pair were not asked back to back.** The kit asks them one after the other. In Stengård the
  items were scattered among 45 problems, in an order that differed by person. A learner may notice a change, and
  answer consistently, more readily when the two questions are adjacent. So agreement here may understate what the
  kit would see.

## 2. Data
- Stengård et al. (2022), OSF 3vkad, all four groups: **222 people** (data_11 91, data_12 91, data_21 20, data_22 20).
  Everyone saw the same 45 (b, h, f) items; pictorial people saw each item twice.
- Answers are on the 0–100 scale (percent; pictorial number-line positions as stored). No missing answers, per the
  October structure check. If any answer is missing, the affected pair or slope is not computed.
- **First showings** only, for all groups. A pictorial item's first showing is its earlier position in the file (the
  v10 assumption: file order = presentation order). Second showings are used only in secondary 4.

## 3. The kit, frozen as shipped
`contrast_lite/build_contrast_lite_v2.py` (as pasted by the team lead, 2026-11-17) writes `contrast_lite/contrast_lite_v2/`.
Checked on 2026-11-17:

| File | SHA-256 |
|---|---|
| contrast_lite.py | 0ecc3552ba79a6c6dd18f23cddcf2eff19cae36a50e57abd1b720610d1f0a7a7 |
| simulate.py | 95429c62acdaba917f586adf4d76fe03c7f2ef65a4616d7cf5d7f395334ffcaf |
| test_contrast_lite.py | 8c70688812c8436f8e2dda15be8465fd7840f840a4e5d9b182fd71d001fe45b3 |
| question_bank.json | 7dbcf6c8af5651164666f9f5b01bc79d74a38196117a915a1673f262edb7e5ef |

- The kit's 9 tests pass.
- `simulate.py` reproduces the reference ("Bayes | 95.92% | 0/9592", "switch 30% | 3.26% | 9/326") and selects the
  shipped settings.
- **Settings exactly as shipped (`DEFAULT`):** flat 0.30, moves 0.36. The fit setting, 14, is not used (no gate).
  **No tuning on real data. The kit is not changed after this result, whatever it shows.**
- **The kit's own definitions are used:**
  - **Pair score** (`contrast_scores`): (answer to the second question − answer to the first) ÷ (correct answer of
    the second − correct answer of the first). In each pair the varied input increases from the first question to
    the second, as in the kit's own bank.
  - **Pair code** (the classification line in `decide`): "flat" if |score| ≤ 0.30; "moves" if score ≥ 0.36;
    otherwise undecided.
  - **Pair agreement** (`decide`): an input gets a verdict only if both of its pairs have the same code and it is not
    undecided; otherwise "not sure yet".
  - `decide` itself cannot be called for one input alone. The analysis script copies these lines, and a test checks
    that they give the same codes as `decide` on constructed scores.

## 4. Item selection (metadata only, deterministic)
- **Rule:** questions that pass the kit's `valid_question`; one-input pairs whose correct answer moves ≥ 15 points
  (as in `check_bank`); per input, the two passing pairs with the largest move that share no item, ties to the lower
  (b, h, f).
- **On Stengård (checked with the kit's code):** exactly 4 items pass, and the rule gives:
  - **base rate:** (10/50/10 → 30/50/10), correct answer +32.5; (10/50/30 → 30/50/30), +26.0;
  - **false-alarm rate:** (10/50/10 → 10/50/30), −20.1; (30/50/10 → 30/50/30), −26.5;
  - **hit rate:** none.

## 5. Reference (answers the rule does not use)
- Each person's first-showing answers to the **other 41 items**.
- **Per input:** the pooled slope Σ Δanswer·Δcorrect / Σ Δcorrect² over every one-input pair of that input among the
  41 items. Each pair runs from the lower to the higher value of the input. This is the v10 slope, used for all
  pairs, not only those passing the kit's rules.
- **Reference code:** the kit's pair code applied to the slope: "flat" if |slope| ≤ 0.30, "moves" if slope ≥ 0.36,
  otherwise **undecided**. "None" if the person has no usable pair for that input (not expected: no answers are
  missing).
- **Handling an undecided reference, fixed in advance:**
  - the agreement figure is computed **among people whose reference is decided**;
  - the number of people with a verdict whose reference is undecided is reported separately;
  - a **stricter figure** is also reported, counting undecided references as disagreements: the denominator is every
    person with a verdict and a reference that is not "none".

## 6. Outcomes
**Primary: the symbolic groups** (data_11 + data_12, **182 people**; typed percentages, the kit's own format). For
each input separately (base rate; false-alarm rate):
1. **The share of people whose two pairs agree** (the input gets a verdict), with an exact two-sided 95%
   Clopper–Pearson interval.
2. Among people with a verdict and a **decided** reference: **agreement with the reference** (same code), with an
   exact two-sided 95% interval and a one-sided exact 95% upper bound on disagreement (the kit's
   `upper_error_bound`). Next to it:
   - the number with a verdict but an undecided reference;
   - the stricter figure, with undecided counted as disagreement, with its interval and bound (§5).

**Reported separately: the pictorial groups** (data_21 + data_22, **40 people**; number-line answers, not the kit's
format). The same outcomes as the primary, never pooled into the primary.

**Secondary:**
1. **Pooled, all 222 people:** the same outcomes.
2. For each of symbolic, pictorial and pooled: the share with verdicts for both inputs, with an exact interval.
3. Verdict counts by input ("flat", "moves", "not sure yet"), and the reference codes within each verdict.
4. The base-rate verdict cross-tabulated against the v10 base-rate label as defined on Stengård in development
   (neglect if |base slope| < 0.2 over the 37 answers v10 did not ask), computed the same way for every group on
   first showings. Reported as a table, with no test.
   **This cross-table is not independent of the verdict.** Three of the 4 square items (10/50/10, 30/50/10 and
   30/50/30) are among the 37 answers used for the v10 label; the fourth, 10/50/30, is one of v10's 8 asked items
   (checked from item metadata, 2026-11-17). The table is therefore descriptive only.
5. Pictorial groups only (40 people): test–retest of each input's verdict, from the second showing of the same 4
   items. Reported as agreement among people with a verdict on both showings, with an exact interval.

All intervals are exact binomial; no resampling.

## 7. Procedure
1. Write the analysis script in `contrast_lite/`. It imports the frozen kit and never edits it. Test it on made-up
   data only. *(Done 2026-11-17: `contrast_lite/stengard_stage1.py`; 14 tests in
   `contrast_lite/test_stengard_stage1.py` on made-up files in the Stengård layout from
   `contrast_lite/make_fake_stengard.py`. One test checks the copied pair-code line against the kit's `decide` on 516
   scores.)*
2. Hash the script and the kit (record `contrast_lite/stage1_frozen.json`; table below). Then freeze and publish this
   plan as v12 before any Stengård answer is read for it. The script refuses the real files until the record names
   the public v12 tag, and it checks the SHA-256 of each Stengård file.
   **Hashed 2026-11-17** at commit e7db4c95… (every repository module the script imports, checked when hashing,
   plus the kit's question bank):

   | File | SHA-256 |
   |---|---|
   | contrast_lite/stengard_stage1.py | 4711c88683218ed29519ab983a2613beb03011bf4c2731bd9071e82db5ff1b38 |
   | contrast_lite/contrast_lite_v2/contrast_lite.py | 0ecc3552ba79a6c6dd18f23cddcf2eff19cae36a50e57abd1b720610d1f0a7a7 |
   | contrast_lite/contrast_lite_v2/question_bank.json | 7dbcf6c8af5651164666f9f5b01bc79d74a38196117a915a1673f262edb7e5ef |
   | src/mixture_eval.py | ca8e785e928f14a0cb0e0e4a9ed0ee0481244ce31053b35e7833eb1a7b546690 |
   | src/mixture_strategies.py | df8336f85e66f4d5e9e3eddd832bacd6f8a93c02eae3149e5bcd5cc716b12660 |
   | src/stengard_sensitivity.py | 3193d49746176af35fc656faf0ccaabb60fc02fb3ad981c367192a860b6193a9 |
   | src/stengard_analysis.py | a07123908756f328d1184a70d7126a462678b5931854fa3f83706a413ecc4daa |
   | src/bayes_strategies.py | 4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e |
   | src/topic_engine.py | 3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a |

   Stengård files (SHA-256): data_11 ab0ec9a9…4d51, data_12 72f3e8bd…e916, data_21 1a8f79ca…4523,
   data_22 36f9ea5a…910d.
3. Run once, as a Slurm job. The output stores per-person verdicts and reference codes under anonymous row-order IDs.
   Raw data never goes to GitHub.
4. Report whatever it shows. The kit is not changed afterwards on the basis of this result.

## References
- Stengård, E., Juslin, P., Hahn, U., & van den Berg, R. (2022). On the generality and cognitive basis of base-rate
  neglect. *Cognition*, 226, 105160. doi 10.1016/j.cognition.2022.105160.
