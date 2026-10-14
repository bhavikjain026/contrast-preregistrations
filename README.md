# Pre-registrations — contrast-based diagnosis of conditional-probability reasoning

This repository holds pre-registrations for analyses by a Plaksha University team (Perceptron Hackathon 2026,
Problem 8), so that the claim "pre-registered" can be checked. It contains only pre-registration text: no data,
no participant text, no code.

## Files

| File | Original path and commit (private project repository) | Commit date | SHA-256 |
|---|---|---|---|
| `prereg_selection_policies_v1.md` | `analysis/prereg_selection_policies.md` @ `6cd03cbb9355a81855d20290d712188d51c54bd6` | 2026-10-13 09:00:01 +05:30 | `0fabe8ff3efba8e69ac5df157c0365fe07c561d0dbbce151d26adb23ab6bd526` |
| `prereg_selection_policies_v2.md` | `analysis/prereg_selection_policies.md` @ `827c6704ca90d740ee3a4f0090a2896e6d24a3a4` | 2026-10-13 09:08:33 +05:30 | `e826495de08615f8a3171ea99d3f4430df8a6d5c6598ce3bd9e53e6905022303` |
| `prereg_lin2026_replication.md` | `analysis/prereg_lin2026_replication.md` @ `a5bd1b991e9d61b95c59a706a2ded7c5749a21e0` | 2026-10-13 17:48:38 +05:30 | `1fe875c0685bd4f2685d7b3d598d186ac5d68a1638d19db8fa1072f881fbdf1d` |
| `prereg_lin2026_eight_answers.md` — original (tag v3) | `analysis/prereg_lin2026_eight_answers.md` @ `a20f85d4fd9c82fa4d3c6c94154db8f9d21a0286` | 2026-10-13 20:01:14 +05:30 | `806d14f2724346c1fa65aa4a9d4a61bbb8951c2e52433371277c22b93436e507` |
| `prereg_lin2026_eight_answers.md` — with addendum A1 (current; tag v4) | `analysis/prereg_lin2026_eight_answers.md` @ `8c8db73f8f368d119e11b4eaa3c079eaf24be024` | 2026-10-13 20:09:34 +05:30 | `d3c5f8d98eb0b9acc0dd0bae11fc3a6bd3d5bfd5da01654dedf221b6b375c4f3` |
| `prereg_pighin_p37nz.md` | `results.md` lines 2180–2234, the lines added by commit `31918143afc81d54adca069ba1b074410909747e` (the plan section) | 2026-10-12 17:30:50 +05:30 | `f1a6f3028e2bd1ff644233c0b7912097e7b8679e387715166fe4fd146cde5314` |
| `prereg_trial.md` | `analysis/prereg_trial.md` @ `36b4cd34a06b7b1830d8c120605f6101e652997e` | 2026-10-13 20:55:29 +05:30 | `2e19e77dd6eaeab3594b9d9fdb5a0285e0d03c3a40d121cabc62755cd06d0217` |
| `prereg_trial_addendum_A1.md` (addendum to `prereg_trial.md`) | `analysis/prereg_trial_addendum_A1.md` @ `e54b65ee6d18126a3fe2f41412ae66c50a689e07` | 2026-10-14 18:54:45 +05:30 | `09c3956c7197ba2fbc55f559667f5d70e9746257a5c9cc71879507ff847ff4b0` |
| *(not yet published)* volunteer pilot, visit 1 — original | `analysis/prereg_pilot_visit1.md` @ `3139e5350917cb55caa2d5459240fc71967c2e46` | 2026-10-13 15:11:39 +05:30 | `26292ca897eb39df42b74eb716888e4ffc0dc314cf4f0c7dcf7a94588f3d1538` |
| *(not yet published)* volunteer pilot, visit 1 — with addendum A1 (current) | `analysis/prereg_pilot_visit1.md` @ `c14f3aa7d122db71b5e406254267018b03b0ed62` | 2026-10-13 20:21:02 +05:30 | `804a7d056aec00ef8d07a72d4a53f6b2edae40ca30e4be73b4fdd98d759d3181` |
| *(not yet published)* volunteer pilot, visit 1 — amendment v8 (tie-break for the A1 figures) | `analysis/prereg_pilot_visit1_amendment_v8.md` @ `e472579429873ae14f5fb3c6f02b126861da7cc2` | 2026-10-14 19:28:04 +05:30 | `232b206972d85818be5e61f9f589598ff43899918f50e69c3f2ad1eee769eed5` |
| *(not yet published)* randomised pilot — addendum A2 (addendum to `prereg_trial.md`) | `analysis/prereg_trial_addendum_A2.md` @ `d11c19f71012c702985607f8dba2c7bab5bc36a0` | 2026-10-14 22:06:27 +05:30 | `1502bb7fd0b621d600aba3ec48392fd14e5df83d582e043d3f48717b3ec943c1` |

Each published file is byte-identical to the version committed at the listed commit. Check with
`sha256sum <file>`.

## What this repository does and does not prove

- **Selection-policy pre-registration (v1, v2).** Version 2 adds the replication hypotheses on the second data file,
  written before its analysis code. Both versions were committed privately on 13 Oct 2026 (hashes above) and published
  here on 13 Oct 2026. **This repository proves the files have not changed since publication here, not when they were
  written.** The private commit hashes are listed for reference; they cannot be opened from outside.
- **Replication on Lin et al. (2026)** (doi 10.31234/osf.io/wgpb2_v1). Committed privately and published here on
  13 Oct 2026, **before any answer in that dataset was analysed** (only its structure — counts, units, design — had been
  read). As above, this repository proves the file has not changed since publication here.
- **Eight-answer comparison on Lin et al. (2026).** Committed privately and published here on 13 Oct 2026, before
  this analysis was run. The same dataset had been used once earlier that day for the label-stability
  replication above; this file says so.
  Addendum A1 (published as v4, before the model run): one sentence defining "ignoring the base rate" was added
  to the model prompt so that all methods use the same definition; the original version stays in tag v3.
- **Engine vs Pighin, Tentori & Filimon's error codes** (OSF p37nz). This plan was not a separate file: it is the
  section appended to the project log by the listed commit, published here byte-identical to those added lines.
  The plan was committed at 17:30:50 on 12 Oct 2026; the analysis script and its results were first committed 4
  minutes later (17:34:39). The commits show the plan's text predates the results commit; they do not show
  whether code had been run before the plan was committed. Published here on 13 Oct 2026.
- **Randomised pilot (targeted vs general practice).** Written and approved before any participant; the trial
  starts only after Plaksha University ethics approval. Published here on 13 Oct 2026. Exact test items, the
  allocation-list hash, the frozen tutor tag and the ethics reference follow as dated addenda before the first
  participant.
  Addendum A1 (14 Oct 2026, v7.1, before any participant) corrects the low end of the stated power range: 50% of
  30 people is 7.5 per arm, where the minimum detectable d is about 1.37 (corrected range 0.89–1.37). Nothing
  else changes.
  Addendum A2 (14 Oct 2026, v9, before any participant) fixes choices v7 left open, found in a synthetic dry run of
  the whole pipeline (frozen pretest and test forms, practice and tie rules, scoring, allocation custody). Only its
  SHA-256 is published now; the full text will be published after the last delayed test, because it describes
  the delayed-test problems.
- **Volunteer pilot, visit 1.** Only its SHA-256 is published now. The file itself will be added after the pilot,
  byte-identical, so it can be checked against the hash above. It is withheld for now because it mentions one
  participant's already-known result. **This hash is published here before any pilot data from participants P02–P08
  exists.** The pilot uses two independent raters; one team member's codes on one visit are flagged non-independent.
  Addendum A1 (13 Oct 2026, also before any P02–P08 data existed) adds one secondary measure — how many learners
  who neglect the base rate would get the base-rate lesson, and how many lessons would be wasted — because a
  majority guess never assigns that lesson; the primary measures are unchanged. Its hash is listed above; the
  file (with the addendum) will be published after the pilot.
  Amendment v8 (14 Oct 2026, before the visit-1 analysis was run, when the only rater codes were those for P01
  from 12 Oct, already described in the pre-registration) fixes how the A1 figures are reported if the raters’
  majority status is tied: under both tie-breaks, with the script’s default (‘uses’) labelled. Nothing else
  changes. Its hash is listed above; the file will be published after the pilot.

## Releases

`v1` — first publication (13 Oct 2026): two selection-policy files and the pilot pre-registration's hash.
`v2` — adds the Lin et al. (2026) replication pre-registration (13 Oct 2026), before its analysis.
`v3` — adds the eight-answer comparison pre-registration on Lin et al. (2026) (13 Oct 2026), before its run.
`v4` — eight-answer pre-registration with addendum A1 (prompt definition sentence), before the model run.
`v5` — adds the hash of the pilot pre-registration with addendum A1 (file still to follow after the pilot).
`v6` — adds the Pighin et al. (OSF p37nz) comparison plan (committed 12 Oct 2026), byte-identical to the added lines.
`v7` — adds the randomised pilot pre-registration (13 Oct 2026), before any participant.
`v7.1` — addendum A1 to the randomised pilot pre-registration (power low end corrected; 14 Oct 2026).
`v8` — adds the hash of pilot amendment v8 (tie-break reporting for the A1 figures; 14 Oct 2026).
`v9` — adds the hash of addendum A2 to the randomised pilot pre-registration (14 Oct 2026; text after the last delayed test).
