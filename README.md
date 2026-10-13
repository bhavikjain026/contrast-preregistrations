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
| *(not yet published)* volunteer pilot, visit 1 — original | `analysis/prereg_pilot_visit1.md` @ `3139e5350917cb55caa2d5459240fc71967c2e46` | 2026-10-13 15:11:39 +05:30 | `26292ca897eb39df42b74eb716888e4ffc0dc314cf4f0c7dcf7a94588f3d1538` |
| *(not yet published)* volunteer pilot, visit 1 — with addendum A1 (current) | `analysis/prereg_pilot_visit1.md` @ `c14f3aa7d122db71b5e406254267018b03b0ed62` | 2026-10-13 20:21:02 +05:30 | `804a7d056aec00ef8d07a72d4a53f6b2edae40ca30e4be73b4fdd98d759d3181` |

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
- **Volunteer pilot, visit 1.** Only its SHA-256 is published now. The file itself will be added after the pilot,
  byte-identical, so it can be checked against the hash above. It is withheld for now because it mentions one
  participant's already-known result. **This hash is published here before any pilot data from participants P02–P08
  exists.** The pilot uses two independent raters; one team member's codes on one visit are flagged non-independent.
  Addendum A1 (13 Oct 2026, also before any P02–P08 data existed) adds one secondary measure — how many learners
  who neglect the base rate would get the base-rate lesson, and how many lessons would be wasted — because a
  majority guess never assigns that lesson; the primary measures are unchanged. Its hash is listed above; the
  file (with the addendum) will be published after the pilot.

## Releases

`v1` — first publication (13 Oct 2026): two selection-policy files and the pilot pre-registration's hash.
`v2` — adds the Lin et al. (2026) replication pre-registration (13 Oct 2026), before its analysis.
`v3` — adds the eight-answer comparison pre-registration on Lin et al. (2026) (13 Oct 2026), before its run.
`v4` — eight-answer pre-registration with addendum A1 (prompt definition sentence), before the model run.
`v5` — adds the hash of the pilot pre-registration with addendum A1 (file still to follow after the pilot).
