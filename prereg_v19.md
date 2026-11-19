# Plan v19: a fixed second question with a repeat check, against the adaptive follow-up

Written 19 November 2026, before anything below is run. To be published byte-identical under tag v19 before it is run.
**This is a simulation. No human data is read, used or produced.**

**About the tag.** Tag v19 was reserved earlier for a "markets mode" plan. That plan was never published or run, and it
was dropped on 18–19 November after review. No public tag, registry entry or file has used the name v19, so this plan
takes it.

## 1. Question

**What v17 found.** In plan v17 (scripted learners, noise ±2, the six wrong-rule learners pooled):
- one fixed second problem named the right rule in 34.3% of sessions, against 32.4% for the tutor's adaptive
  follow-up;
- it named a wrong rule in 0.0%, against 0.4%;
- the adaptive follow-up's one clear advantage was with learners who type their first number again (repeaters): the
  fixed arm named a rule for 12.0% of them at ±2, and the adaptive arm for none, by design.

**The rival.** An outside review (ChatGPT, 19 November, after seeing v17) proposed the cheapest rival: keep the fixed
second problem, but give no name when the second answer repeats the first.

**This plan estimates, against that guarded fixed question:**
- how often each arm names the right rule;
- how often each names a wrong rule;
- how many correct names the repeat check withdraws.

It is an estimation study. The primary results are two separate paired differences, each with its interval. They are
not combined into one verdict.

## 2. Arms

All arms share the first problem and the first answer. Both come from a scripted session run through the frozen tutor.

- **adaptive:** the frozen tutor's own follow-up (default settings, two problems), exactly as in v17.
- **fixed:** v17's fixed second problem (base 90%, hit 60%, false alarm 20%, classroom story), with the tutor's naming
  rule applied outside the session, exactly as in v17. With two answers its verdict is either "named" or "possible
  slip". A second answer that fits only the correct method is a "possible slip".
- **guarded (new, primary):** the fixed arm, except when the fixed verdict is "named" or "possible slip" and the second
  typed whole percent equals the first. Then no rule is named, and the verdict is recorded as "repeat, no name".
  - Sessions that ended after the first answer are unchanged.
  - Every row keeps the fixed arm's original verdict and named rule, so a withdrawn name and a relabelled "possible
    slip" are counted separately.
- **guarded1 (new, secondary):** the same, but a second answer within 1 point of the first counts as a repeat. This
  treats "copy the first number" as one more rule, with the tutor's 1-point tolerance.

**Notes:**
- Every typed answer the arms use must be a whole percent from 0 to 100; the script stops otherwise.
- v17's random arm is not re-run. It used its own random stream (a new generator built from each session's key), so
  leaving it out changes no other session.

**Why the adaptive arm gets no repeat check.** It would withdraw no adaptive name.
- In `src/tutor.py`, with the default two problems, the follow-up must move every surviving wrong rule's answer by at
  least 10 points. The fallback to smaller moves exists only when there are two or more earlier problems. If no
  problem qualifies, the verdict is "possible slip" and nothing is named.
- A name also needs both typed answers within 1 point of that rule's answers.
- So the two typed answers of any adaptive name differ by at least 8 points.
- Check C (section 4) verifies this, and check C2 that no adaptive session showed more than two problems.
- A repeat check would only relabel some adaptive "possible slip" verdicts, which changes neither measure.

## 3. Learners and sessions

**Stage 1: v17's own sessions, re-run.** These use v17's own code (`sim_v17.py`, unchanged and checked by hash), with
the same seeds, learner codes, noise draws and order.
- **Part 1:** seven one-rule learners (the six wrong-rule learners plus the correct learner), at noise 0, 1 and 2,
  with 2,000 sessions each (session numbers 0–1999).
- **Part 2:** the unknown rules, switchers, repeater, guessers and rounded learners.
- Stage 1 checks the re-run against v17 (section 4) and gives in-sample secondary results.

**Stage 2: fresh sessions** (run after stage 1, in the same process):
- **Fresh Part 1:** the same seven learners and noise levels, with session numbers 2000–3999. v17 never used these,
  so every first problem, noise draw and session seed is new. **The primary results come from these sessions.**
- **Part 3, noisy repeaters (new):**
  - on the first problem, the answer of one of the six wrong rules (drawn at random per session), with noise k = 0 or
    2;
  - on the second problem, that typed number moved by −2, −1, +1 or +2 (equally likely), clipped to 0–100;
  - 2,000 sessions per noise level.

The guarded arms reuse the fixed arm's two typed answers. The rival was chosen after seeing v17, which is why the
primary uses fresh sessions. Intervals describe uncertainty under the scripted session generator only.

**Known before the run (from the code and from v17):**

1. **The fixed problem names no wrong rule for a one-rule learner.** On the fixed problem the six wrong-rule answers
   are 40, 54, 60, 75, 80 and 90, at least 5 points apart. In `sim_v17.py` a one-rule learner types its rule's answer
   rounded to a whole percent, plus a whole-number noise drawn uniformly from −k to +k (k ≤ 2), clipped to 0–100. Noise
   is added to the final answer, not to the problem's numbers. So its second answer is within 2 points of its own
   rule's answer and at least 3 points from every other rule. No other rule can fit within 1 point. Therefore the
   fixed, guarded and guarded1 arms name exactly **zero** wrong rules for the six wrong-rule learners at noise 0, 1
   and 2, in both stages. This does not extend to switchers, unknown rules or guessers.
2. **The wrong-name difference is essentially known.** It equals the adaptive arm's own wrong-name share. That was 48
   of 12,000 sessions at ±2 in v17 (stage 1), and it is expected to be similar on the fresh sessions. Its interval will
   almost surely lie above 0.
3. **The right-name difference is the open question.**
   - Adaptive minus guarded on right names = (adaptive minus fixed) + (share of fixed right names the guard withdraws).
   - From v17's rounded shares, adaptive minus fixed was about −1.9 points.
   - So the adaptive arm leads on right names only if the guard withdraws more than about 1.9 points, and the interval
     excludes 0 only if it withdraws clearly more.
   - Those figures are rounded and from v17's sessions; the results use exact counts.
4. **Repeaters.** In `sim_v17.py` the repeater's second answer is its first typed answer, copied exactly, with no new
   noise. So both guarded arms name no rule for any v17 repeater. This is a design property, checked in section 4
   (check E), not a finding. The noisy repeaters of Part 3 are not caught by construction by the exact guard.
5. **Who loses a correct name.** A one-rule learner who types the same whole percent on both problems. On the fixed
   problem that means hit 60, base 90, complement 80, subtraction 40, joint 54 or equal priors 75.
   - This happens when the first problem shares the relevant number, or when rounding and noise land both answers on
     the same integer.
   - guarded1 withdraws at least as many correct names as guarded.

## 4. Checks before any guarded result

The script prints all of these first. **If any check fails, it prints no guarded result and stops.**

**Exact checks** (stage 1 unless stated):
- **A.** The adaptive arm at ±2, six wrong-rule learners pooled: right rule named in exactly **3,885** sessions, and a
  wrong rule in **48**. (v17: 48 of 3,933 names were wrong.)
- **B.** Fixed, guarded and guarded1: **0** wrong names for the six wrong-rule learners at any noise level, in both
  stages (section 3, point 1).
- **C.** Adaptive names whose two typed answers differ by less than 8 points: **0**, in both stages (section 2).
- **C2.** Adaptive sessions that showed more than two problems: **0**.
- **E.** Repeaters named by guarded or guarded1, at both noise levels: **0** (section 3, point 4).

**Share checks.** These must equal v17's report to one decimal (six wrong-rule learners pooled):
- noise 0: right names, adaptive 100.0%, fixed 100.0%;
- ±1: right names, adaptive 89.2%, fixed 94.5%;
- ±2: right names, fixed 34.3%; wrong names, fixed 0.0%;
- repeaters named: adaptive 0.0% at noise 0 and at ±2; fixed 23.1% at noise 0 and 12.0% at ±2.

**Per-session check.** `rows_v17.json` was not located on the team's Mac when this plan was written.
- If it is found before the run, its path and SHA-256 are recorded in the run report and it is passed to the script.
- Every v17 adaptive and fixed session must then have the same verdict and named rule, with no session missing or
  extra.
- Without it, the report says that identity with v17 is checked only by counts and shares, not row by row. A
  one-decimal share still allows a window of about a dozen sessions.

**Environment.** The run report records the Python version, operating system and scipy version.

**On any failure:**
- the failed output is published as it stands, and that run is not used;
- any correction, and how the run will be repeated, goes in a dated, published addendum before it is executed;
- the failed output is kept.

## 5. What is reported

**Primary** (stage 2, fresh sessions 2000–3999, noise ±2, the six wrong-rule learners pooled, 12,000 paired
sessions). Two separate determinations for adaptive minus guarded:
1. **right names:** the share of all sessions that name the right rule;
2. **wrong names:** the share of all sessions that name a wrong rule.

How each is reported:
- **Denominator:** every session, including those that ended after the first answer.
- **Shares and difference:** each arm's share in percent, and the difference in percentage points.
- **Interval:** a 95% percentile interval, computed separately for each measure, by resampling whole sessions within
  each rule (10,000 times, seed 20261120, v17's code).
- **Beside the interval:** the discordant counts and an exact McNemar p. These do not change the determination.

**Determination rule:**
- On each measure, the adaptive arm is **better**, **worse** or **unresolved**.
- It is better or worse only if the whole interval lies on one side of 0, comparing unrounded endpoints.
- An interval that includes or touches 0 is unresolved.
- An unresolved right-name result is never reported as a win for either arm.
- v17's four-way label is also printed, for continuity only.

**Secondary:**
- the same two determinations for guarded1 on fresh sessions;
- guarded and guarded1 on v17's own sessions (stage 1, in-sample).

**Co-reported, for both guards and both stages:**
- **The cost of the guard** at noise 0, ±1 and ±2, and per rule at ±2:
  - right names withdrawn;
  - wrong names withdrawn (expected 0);
  - "possible slip" relabelled as a repeat.
- **The share of the fixed arm's right names** that the guard withdraws, at ±2.

**Described (no determination):**
- **Every arm's outcome shares** at each noise level, in both stages, including wrong names per name issued (wrong
  names ÷ all names; "0/0" means undefined).
- **The correct learner:** accused, and told correct.
- **Repeaters (v17) and noisy repeaters (Part 3):** names given without new evidence, in all four arms.
- **Every other v17 Part 2 learner:** the mislabel share in all four arms, as v17 defined it. For switchers, guessers
  and unknown rules, any name is a mislabel, because no single listed rule produced both answers.
- **The rounded correct learner,** in all four arms.

**Fixed reporting template, used for every outcome:**

> "In our simulation of six scripted one-rule learners at noise ±2 (12,000 fresh paired sessions), the adaptive
> follow-up named the right rule in A% of sessions and the guarded fixed question in G% (the guard withdrew W% of the
> fixed question's right names); a wrong rule in B% and H%. Adaptive minus guarded was D points [interval] on right
> names and E points [interval] on wrong names."

Then exactly one of these sentences:
- **Right names better for adaptive, wrong names worse:** "Adapting named more right rules by D points but more wrong
  rules by E points."
- **Both worse for adaptive:** "On these one-rule learners, the guarded fixed question beat adapting on both right
  names and wrong names."
- **Right names unresolved, wrong names worse:** "On these one-rule learners, the guarded fixed question made fewer
  wrong names; right names was unresolved (D points [interval])."
- **Any other case:** "Right names was [better/worse/unresolved] for adapting (D points [interval]) and wrong names
  was [better/worse/unresolved] (E points [interval])."

The headline belongs to the exact guard (guarded), whatever guarded1 shows. It always says "simulation" and "one-rule
learners", and it is reported whatever it shows. Part 2 and Part 3 results are reported next to the headline, never
left out.

## 6. Limits written in advance

- **Scripted learners only.** All learners are scripted, as in v17.
- **A rival chosen after seeing v17.** Its primary uses fresh sessions; its stage 1 results are in-sample.
- **A narrow headline.** The primary covers only the six one-rule learners at ±2. Switchers, unknown rules, guessers,
  rounded learners, repeaters and noise 0 and ±1 are reported but carry no determination.
- **Near-copies.** v17's repeater copies exactly. Part 3 adds near-copies (±1 or ±2), which the exact guard does not
  catch and guarded1 catches only at ±1.
- **One rival.** Others are not tested, such as two fixed questions or a fixed question chosen by simulation.
- **The fixed problem.** It is v17's, chosen by v17's learner-free rule (largest smallest gap between rule answers).
  Its whole-percent answers, at least 5 points apart, guarantee it no wrong names at bounded noise up to ±2. That is a
  property of this one problem, not of fixed questions in general.
- **Code availability.** The code is identified by SHA-256 below. Under the team's publication rule, only the plan
  text goes to the preregistration repository.
- **No claims about people.** Nothing here concerns real students, agreement with their working, or learning.

## 7. Seen before writing this plan (disclosed)

**Earlier results we saw:**
- All plans v10–v18 and addendum v17.1, with their full results, including v17's whole report: per-rule right-name
  shares and every number in sections 1 and 4. v17 reports nothing about how often a one-rule learner types the same
  number on both problems.
- Plan v20 and its result (numbers printed in published Bayes problems). v20 ran first only because it was ready
  first. It is a different question, and no choice in this plan used its result.

**Code we read:** `sim_v17.py`, `report_v17.py` and the follow-up rule in `src/tutor.py`, to state sections 2 and 3.

**Outside reviews of drafts of this plan:**
- **ChatGPT**, which also proposed the rival. Changes made because of it:
  - two separate measures;
  - the zero-wrong-name argument;
  - the adaptive arm's immunity, checked;
  - the original verdict kept in every row;
  - typed answers validated;
  - exact reproduction checks;
  - stated interval rules;
  - a fixed procedure for a failed reproduction.
- **Gemini.** Changes made because of it:
  - the fresh-session primary;
  - noisy repeaters;
  - every check now stops the run;
  - check C at less than 8 points, plus check C2;
  - the noise and repeater assumptions stated from the code;
  - separate determinations instead of a four-way verdict;
  - the scoped reporting template;
  - the environment recorded;
  - the added limits and these disclosures.
- **Suggestions considered and not adopted:**
  - publishing the code itself in the preregistration repository (the team's rule is plan text only; hashes are given);
  - a minimum effect size that matters (we have no principled value; sizes are always quoted).

**Nothing guarded computed yet.** No guarded outcome has been computed for any simulated session. The only runs of
`v19.py` code were its tests, on made-up values, made-up rows and a made-up stand-in for the tutor (`test_v19.py`).

## 8. Files and procedure

| File | SHA-256 |
|---|---|
| `v19.py` | `648befc2bcf9ca8aa38c8d9d5ffb257c7b08ee4599ef179a35475d82c4f425f2` |
| `test_v19.py` | `46a4bcefc58816dfa77e1ec30252448ef294f33ade4ef7b1ba50d36ab855942d` |
| `sim_v17.py` | `e63eb511125438c4a3234b0fffd14dd45f970d11addbbbc7dbb4d081ec0542ce` |
| `report_v17.py` | `53be819ffb8fec54d6c62073560a92ec5963ff8a87389f8c271b37fc1de50f97` |
| `src/tutor.py` | `73f4374a50dcc49c8732ed85ad484f32eedce7efddf0c48818812f7f8740ba0c` |
| `src/bayes_strategies.py` | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `src/topic_engine.py` | `3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a` |
| `src/remediation.py` | `938df557de2ae5c71bc21b2a8f7a77c411b71e66bf92f3da3d9d61888bf52dc5` |
| `src/score_quiz.py` | `80f3b2bcc52c4492243c39b1ee1dabdafb42dfa0ea3af317f6e66a7ee84b97b3` |
| `src/screening_quiz.py` | `a86c27da98dea87c310575c813378012f3c7e0934cd6c45c31b329c01df96a10` |

1. **Publish.** Publish this plan byte-identical under tag v19 (plan text only). Record its SHA-256.
2. **Run once.** Run `python3 v19.py <repo root> <folder with sim_v17.py and report_v17.py> rows_v19.json
   [--v17-rows rows_v17.json]`. The script stops if any frozen file or v17 file differs, or if any section 4 check
   fails.
3. **Report.** Report section 4 first, then every number in section 5. Any change after publication is a dated,
   published addendum.
