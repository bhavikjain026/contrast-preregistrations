# Report v19: a guarded fixed second question against the adaptive follow-up (simulation)

**Plan:** v19 (tag v19, `prereg_v19.md`), published before the run. **Run once** on 19 November 2026 with
`python3 v19.py <repo root> <folder with sim_v17.py and report_v17.py> rows_v19.json`, on macOS with Python 3.14.7.
**Simulated, scripted learners only. Nothing here is about real people.**

Every number below is copied from `report_v19_output.txt` (SHA-256 in section 6).

## 1. Stage 1: reproduction of v17 and fixed checks (plan section 4)

All 17 checks printed **MATCH**, including v17's right-name count (3,885) and wrong-name count (48) for the adaptive
arm at ±2, and the fixed arm's shares at noise 0, ±1 and ±2. Check F (row-by-row identity with v17's own rows) was
**not run**, because `rows_v17.json` was not supplied; the output says so. So v17's printed numbers were reproduced,
but row-level identity with v17's run is unverified.

## 2. Primary (plan section 5)

Fresh sessions 2000–3999, noise ±2, the six one-rule learners pooled, 12,000 paired sessions.

- **Adaptive (the tutor):** right rule named 32.2% [31.4, 33.1]; wrong rule 0.4% [0.3, 0.5] (43 sessions).
- **Guarded fixed question:** right rule 32.0% [31.1, 32.8]; wrong rule 0.0% [0.0, 0.0]. The guard withdrew 6.5%
  [5.7, 7.3] of the fixed question's right names.
- **Right names, adaptive minus guarded:** +0.24 points [−0.08, +0.57]. Discordant sessions 229 and 200. **Unresolved.**
- **Wrong names, adaptive minus guarded:** +0.36 points [+0.26, +0.47]. Discordant 43 and 0. **Adaptive worse.**
- Exact McNemar p, beside the intervals only: 0.176 and 2.27 × 10⁻¹³.

**Template (plan section 5):** "In our simulation of six scripted one-rule learners at noise ±2 (12,000 fresh paired
sessions), the adaptive follow-up named the right rule in 32.2% of sessions and the guarded fixed question in 32.0%
(the guard withdrew 6.5% of the fixed question's right names); a wrong rule in 0.4% and 0.0%. Adaptive minus guarded
was +0.24 points [−0.08, +0.57] on right names and +0.36 points [+0.26, +0.47] on wrong names."

**Determination sentence (plan section 5):** "On these one-rule learners, the guarded fixed question made fewer wrong
names; right names was unresolved (+0.24 points [−0.08, +0.57])."

The script printed this sentence without the bracketed figures; the plan's form includes them, and is given here.
Under the plan, the unresolved right-name result is not a win for either arm.

## 3. Secondary

- **guarded1, fresh sessions:** right names +3.43 points [+3.00, +3.88], adaptive better; wrong names +0.36
  [+0.26, +0.47], adaptive worse. A trade-off.
- **guarded, v17's own sessions (in sample):** right +0.49 [+0.16, +0.83], adaptive better; wrong +0.40
  [+0.29, +0.52], adaptive worse.
- **guarded1, v17's own sessions:** right +3.57 [+3.13, +3.99]; wrong +0.40 [+0.29, +0.52]. A trade-off.

## 4. Co-reported and described

In the output, without determinations: the cost of each guard at noise 0, ±1 and ±2 and per rule; every arm's
outcome shares in both stages; the correct learner (accused in 0 of 2,000 sessions in every arm and stage); the
repeaters (named without new evidence: adaptive 0%, fixed 23.1% at noise 0 and 12.0% at ±2, both guards 0%); the
noisy repeaters; every other v17 Part 2 learner; and the rounded correct learner.

## 5. What it does not show

As written in the plan: a rival chosen after seeing v17; scripted learners only; a narrow headline (six one-rule
learners at ±2); intervals that describe the scripted session generator, not people.

## 6. Deviations and files

- No deviation from the procedure. Check F could not run (above), as the plan allowed for a missing `rows_v17.json`.
- The script, test file, `sim_v17.py`, `report_v17.py` and the frozen tutor files matched plan section 8 (checked on
  20 November 2026).
- `rows_v19.json` (213 MB, per-session rows of simulated learners) is kept privately; its size is the only reason.

| File | SHA-256 |
|---|---|
| `report_v19_output.txt` (printed output, unchanged) | `44b5e1fcd1cc85fc02064baf4cc99eff79d4c1cacdb45086933957c3af506512` |
| `v19.py` | `648befc2bcf9ca8aa38c8d9d5ffb257c7b08ee4599ef179a35475d82c4f425f2` |

Written 20 November 2026, from the saved output of the single run.
