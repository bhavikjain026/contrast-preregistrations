# Addendum A1 to the randomised-pilot pre-registration (approved by the team lead; published as v7.1)

Pre-registration: `prereg_trial.md`, published as v7 (SHA-256 2e19e77dd6eaeab3594b9d9fdb5a0285e0d03c3a40d121cabc62755cd06d0217).
Date: 2026-10-14. Before any participant (no participant has been approached; ethics approval pending).

**Correction (§2, power).** The published text says: "if 50–80% of 30–40 people have a gap (8–16 per arm), it is
d ≈ 0.89–1.31". The low end of that scenario is wrong: 50% of 30 people is 15 with a gap, i.e. **7.5 per arm**, not 8.
With the same registered formula (`src/power_ancova.py`, `mde(n, 0.5)`: 80% power, two-sided α 0.05, ANCOVA with
pre–post r 0.5), the minimum detectable effect is **d ≈ 1.37 at 7.5 per arm** (1.43 at 7, 1.31 at 8). The corrected
statement is: **if 50–80% of 30–40 people have a gap (7.5–16 per arm), the minimum detectable d is about 0.89–1.37.**

**Nothing else changes.** Primary outcome, primary population (the gap stratum), analysis, secondary outcomes,
allocation, exclusions and the analysis script (SHA-256 09ef600e…c4b3c3) are unchanged; this correction only states
the power of the planned design more accurately. The effect estimate and its CI remain the main result.
