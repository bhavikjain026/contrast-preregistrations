# Addendum v12.1 to pre-registration v12 (Contrast-Lite v2, stage 1 on Stengård et al., 2022)

**Status: FINAL. Approved by the team lead on 2026-11-17 and released as v12.1** in the public pre-registration
repository (file `prereg_contrast_lite_stage1_addendum_v12_1.md`), **before the rerun**. Date: 2026-11-17.

## What happened
- v12 was published on 2026-11-17 (`prereg_contrast_lite_stage1.md`, SHA-256 e9a5ad2c…4ee958c, tag v12), and the
  single run was started (Slurm job 14272).
- **The job stopped at the answer-scale guard after reading only one file's largest answer**: "data_11.mat: answers
  not on the 0–100 scale (max 0.99)".
- **No verdict, reference or outcome was computed.** No output file was written.
- **Cause:** v12 §2 assumed the files store answers as percentages, taken from the Stengård readme ("the response is
  specified as a percentage"). The files actually store proportions. Our own structure check of October 2026 had
  recorded this; it should have been checked before v12 was written.

## The one change: answer-scale rule
- **Fixed in advance and decided from each file's stored minimum and maximum answer only:**
  - if the maximum is ≤ 1 (and the minimum ≥ 0), answers are multiplied by 100;
  - if the maximum is ≤ 100 (and the minimum ≥ 0), answers are used as stored;
  - anything else stops the run before any analysis.
- **Ranges and branches** (stored minimum and maximum only, read on 2026-11-17 after the stop):

  | File | Stored min | Stored max | Branch |
  |---|---|---|---|
  | data_11.mat (symbolic) | 0.01 | 0.99 | × 100 |
  | data_12.mat (symbolic) | 0.01 | 0.99 | × 100 |
  | data_21.mat (pictorial) | 0.0111 | 0.9928 | × 100 |
  | data_22.mat (pictorial) | 0.0091 | 0.9987 | × 100 |

  The run records each file's range and branch in its output.
- **Where the conversion applies:**
  - **Percent scale:** the kit's pair scores (stage 1) and the reference slope (§5) use the percent answers. The × 100
    is rounded to 10 decimals, so the same answers stored as proportions or as percentages give identical numbers.
  - **Development scale:** the v10 base-rate label in secondary 4 is computed exactly as in development, on the
    scale that code expects. That is the rule of `src/mixture_stengard.load_symbolic`: per person, stored answers ÷ 100
    if their maximum is > 1, otherwise as stored, i.e. proportions here. It never receives the percent answers.
  - **The two paths do not mix scales.** Each person carries two separate answer arrays, one per path.
- **Checks on made-up data** (`contrast_lite/test_stengard_stage1.py`, 18 tests, all pass):
  - the same answers stored as proportions and as percentages give exactly identical selected pairs, verdicts,
    references, v10 labels and outcomes;
  - the kit path is on percent and the v10 path on proportions;
  - the v10 labels equal those computed by the development loader itself;
  - the stop branches (maximum > 100, minimum < 0) stop the run.
- The script now also refuses the real files until its frozen record names the public tag of this addendum.
- The script imports no repository module outside the hashed list. It does not import `src/mixture_stengard`, which
  only the test file uses. This was checked by loading every module during a full made-up run.

## New script hash
`contrast_lite/stengard_stage1.py` SHA-256 **3e7ee8bd64c8aac2258377ef37186c263dcf41ca215d8e03e89fa3b8c32d59cf**
(was 4711c886…; recorded at commit 2eff50d9, record `contrast_lite/stage1_frozen.json`). The kit and every other
hashed file are unchanged:
- `contrast_lite.py` 0ecc3552…;
- `question_bank.json` 7dbcf6c8…;
- the v10 model files as listed in v12.

## Everything else in v12 is unchanged
The data, the kit and its settings, the item selection, the reference, the handling of undecided references, every
outcome, the formats (symbolic primary, pictorial separately, pooled secondary), the limitations, and the statement
that there is no success criterion. The check still runs once, and is reported whatever it shows.
