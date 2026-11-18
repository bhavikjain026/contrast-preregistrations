# Plan v16: how often does the frozen tutor name the wrong rule when answers are a few points off?

Written 19 November 2026, before the simulation is run. To be published byte-identical under tag v16 before it is
run. **This is a simulation. No human data is read, used or produced.**

## 1. Question

The tutor matches a typed answer to a rule when the two are within 1 percentage point, and names a rule only when the
first answer and the follow-up answer both fit it. A real student who uses a rule may still slip by a point or two.
How often does the tutor then name a different rule than the one the learner used, name none, or tell a learner who
used the correct method that they used a wrong rule?

## 2. The tutor, exactly as frozen

- Code: `src/tutor.py` and the files it imports for the classic flow, checked by SHA-256 before anything runs
  (section 7). The tutor is not changed.
- Session: `tutor.Session(code, seed=i, data_dir=<one new temporary folder for the whole run>)`, with a learner code
  used by exactly one session (`SIM-<config>-<rule>-<k>-<i>`), so no session is a returning learner; classic flow (`profile_mode` off), normal
  start, two consistent answers needed to name a rule (`confirm=2`). The first problem is the tutor's own draw for
  seed `i`.
- Two configurations, both reported:
  - **A**, the frozen defaults: `collision_filter` off. **Primary.**
  - **B**, the demo's setting: `collision_filter` on (follow-ups only from collision-free problems).

## 3. Simulated learners

- Seven learner types: one for each of the tutor's six wrong rules (hit_rate, base_rate_only, joint_occurrence,
  likelihood_subtraction, false_alarm_complement, equal_priors) and one that uses the correct method (bayes).
- A learner answers every diagnostic problem (the first problem and the follow-up, if asked) with its rule's value,
  in percent, rounded to a whole number (Python `round`), plus noise, clipped to 0–100, and typed with a `%` sign.
  (The tutor reads a bare number of 1 or less as a proportion, so `1` would mean 100%; the `%` sign avoids this.)
- Noise levels k = 0, 1, 2, 3: for k > 0, an integer drawn uniformly from −k to +k, independently for each answer.
  k = 0 means rounding only.
- Sessions: for each configuration, learner type and noise level, 2,000 sessions with seeds `i` = 0 to 1,999. Noise
  comes from `random.Random(20261119 XOR crc32("<config>|<rule>|<k>|<i>"))`. In total 2 × 7 × 4 × 2,000 = 112,000
  sessions.
- After the diagnosis (the rule is named, or the session ends without a name) the learner quits. Lessons and
  practice are not simulated.

## 4. Outcomes and what is reported

Each session gets one outcome:

- **NAMED-RIGHT**: the tutor named the learner's own rule.
- **NAMED-WRONG**: the tutor named a different wrong rule.
- **ACCUSED**: the learner used the correct method and the tutor named a wrong rule.
- **SAID-CORRECT**: the tutor said the first answer was correct.
- **NO-NAME**: anything else (possible slip, no known strategy, cannot tell from one answer).

**Primary.** Configuration A, noise ±2, the six wrong-rule learners pooled (12,000 sessions): the share NAMED-WRONG,
with an exact (Clopper-Pearson) 95% interval.

**Co-primary.** Configuration A, noise ±2, the correct learner (2,000 sessions): the share ACCUSED, with an exact
95% interval.

**Described, with no pass or fail:** for each configuration, learner type and noise level, the share of each
outcome and of sessions with a follow-up; NAMED-WRONG pooled over the six rules at each noise level, with exact
intervals; and which rule was named instead, as counts.

There is no success criterion. Every number is reported whatever it shows. In the talk we will quote the primary
and co-primary shares with their intervals, the noise level, and the word "simulation".

## 5. Limits written in advance

- Simulated learners apply one rule to every problem. Real people often do not (our v15 result; Lin et al. 2026,
  p. 28).
- Uniform noise of ±k points is an assumption, not a measured model of real slips. Real slips may be larger,
  one-sided, or come from a different rule on one problem.
- The sessions are not a sample of real problems a student would meet; they are the tutor's own draws for 2,000
  seeds. Sessions sharing a seed share their first problem.
- A high NAMED-RIGHT share says the matching works on these scripted learners. It is not evidence that the tutor's
  label matches what a real person did, or that anyone learns.

## 6. Seen before writing this plan (disclosed)

- A timing check on 19 November: 30 sessions (seeds 0–29) of a joint_occurrence learner with no noise in
  configuration A. All 30 named joint_occurrence after two answers. It took 0.04 seconds.
- Demo runs of the collision path (first problem 60/75/30, follow-up 5/75/5): second answers 4 and 4.75 named joint
  occurrence; 4.76 and 5 named none; 70 named likelihood subtraction.
- Other single-rule simulated learners run on this tutor and looked at before this plan: the demo's scripted paths
  and their golden transcripts (a hit-rate learner and a likelihood-subtraction learner, classic flow); the older
  demos `analysis/tutor_demo_hit_rate.txt` and `analysis/tutor_demo_profile.txt`; and the rehearsal runs of
  19 November on the collision path, including first answers 4, 5, 20, 4.75 and 4.76 (each "no known strategy"),
  first answer 70 (one candidate, follow-up 5/75/15), and 45 then 20 (no rule named).
- None of these is a run of noisy learners across seeds. No session with noise added to a rule's answer has been run.

## 7. Files and procedure

| File | SHA-256 |
|---|---|
| `sim_noise.py` | `422b905c08a185852e5432ca493550b1a18e576b48f7940b376670af757327f7` |
| `report_v16.py` | `9e72e84ee73ab28227c901b342f18fed865c64726af352536e5515b34aa3fce4` |
| `test_sim_v16.py` | `494d5d9784d56b60303ff276c12957383eedd461a9693e640dad61166e6b1637` |
| `src/tutor.py` | `73f4374a50dcc49c8732ed85ad484f32eedce7efddf0c48818812f7f8740ba0c` |
| `src/bayes_strategies.py` | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `src/topic_engine.py` | `3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a` |
| `src/remediation.py` | `938df557de2ae5c71bc21b2a8f7a77c411b71e66bf92f3da3d9d61888bf52dc5` |
| `src/score_quiz.py` | `80f3b2bcc52c4492243c39b1ee1dabdafb42dfa0ea3af317f6e66a7ee84b97b3` |
| `src/screening_quiz.py` | `a86c27da98dea87c310575c813378012f3c7e0934cd6c45c31b329c01df96a10` |

1. The tests (`test_sim_v16.py`) check the noise, the outcome classes and the exact interval on made-up values
   only. They run no simulated session.
2. Publish this plan byte-identical under tag v16. Record its SHA-256.
3. Run `python3 sim_noise.py <repo root> sessions_v16.json` once, then `python3 report_v16.py sessions_v16.json`.
   The script stops if any frozen file differs from section 7.
4. Report every number in section 4. Any change after publication is a dated, published addendum.
