# Plan v18: the ambiguous start, computed exactly

Written 19 November 2026, before anything below is computed for any learner in the plan. To be published
byte-identical under tag v18 before it is run. **This is a computation with simulated learners. No human data is
read, used or produced.**

## 1. Question

The live demo uses the tutor's **ambiguous start**: the first problem has two or more wrong rules giving the same
whole-percent answer (60/75/30: subtraction 75 − 30 and joint occurrence 60% × 75% both give 45). Plans v16 and v17
used the default start, where no first answer can fit two rules (addendum v17.1, A2–A3). No registered result yet
covers the demo's situation.

**When a learner who uses one rule gives a first answer that fits two or more wrong rules, including their own, how
often does the frozen tutor then name another rule?** Also: how often does it name their rule, or none, and how often
does it name another rule over all ambiguous-start sessions?

## 2. The tutor, exactly as frozen

Same files and hashes as plans v16 and v17 (section 8). Default settings except `start="ambiguous"`, an existing
setting: `confirm=2`, collision filter off (the tutor refuses the filter with this start).

Learners:
- the seven of v16 (six wrong rules and the correct method), each applying its rule to every problem;
- 30 switchers (one wrong rule on the first problem, a different one on the second);
- the three rules the tutor does not know from plan v17: b·h / (b·h + f), (b + h) / 2, and b·h + (1 − b)·f.

An answer is the learner's value rounded to a whole percent, plus integer noise drawn uniformly from −k to +k
(k = 0, 1, 2), clipped to 0–100, typed with a `%` sign. The two answers' noise draws are independent.

## 3. Method: exact, not sampled

Every outcome is summed exactly over three things.
- **First problems:** every first problem the tutor can draw (488 in the ambiguous start), weighted as
  `Session.pick_first` draws them: a story uniformly among the six, then a problem uniformly within that story.
- **Noise:** every pair of noise draws (25 at ±2).
- **Follow-ups:** every follow-up the tutor can choose. `tutor.follow_up` shuffles the five other stories (its only
  use of randomness) and takes the first one where its search finds a problem. The search within a story is
  deterministic: it ranks candidates and keeps the top one. So each story where the search succeeds is equally
  likely. We call `follow_up` itself once per story, with a stand-in random generator that puts that story first.

Fractions are exact, so the results have no sampling error. They are exact **for this model of learners and noise
only**.

**Checks against 7,000 real ambiguous-start sessions** (1,000 per single-rule learner at ±2; seeds 0–999; noise
from each session's own fixed stream):
1. **Per session.** The follow-up shown must be one of the computed candidates. The real verdict must equal the
   computed outcome for that follow-up and those answers. Both counts are expected to be 0.
2. **The follow-up choice.** The number of sessions whose follow-up was the first candidate in story order is
   compared with its expected number under equal likelihood (the sum of 1/number of candidates), with a z value.
3. **Outcome frequencies.** For each learner and outcome, the exact probability is compared with the 99% exact
   interval of the observed share. With about 30 cells, about 0.3 are expected outside by chance.

A non-zero count in check 1, or a clear failure in checks 2–3, is reported first. No v18 number is then quoted on a
slide until it is explained. Because checks 1 and 3 use the tutor's own functions, they test the session path, the
weights and the method, not the tutor's logic.

**Method check against v16.** The same code computes the default start exactly. v16's sampled results at ±2 (wrong
rule named 0.4%, interval 0.3–0.6%; correct learner accused 0 of 2,000, interval 0–0.2%) should contain the exact
values. Whether they do is reported; a value outside is reported as a disagreement to explain, not hidden.

## 4. Facts from the tutor's code, computed before this plan with no learner (published here)

**Census.** We looked at every ambiguous first problem and every whole-percent first answer that fits two or more
wrong rules: 1,688 cases. For each, we listed every follow-up the tutor can choose and the smallest gap between the
surviving wrong rules' answers on it.
- **Follow-ups:** 8,034 in total. Every case has four or five.
- **Smallest gap anywhere:** 2.5 points. The tutor guarantees only more than 2.
- **When "another rule" is possible:** a learner can be named as another surviving rule at noise ±k only if their
  own rule's answer and that rule's answer are at most k + 1.5 points apart (k noise, 0.5 rounding, 1 tolerance).
  This is necessary, not sufficient.
  - Follow-ups whose smallest survivor gap is within that reach: 41 at ±1, 1,391 at ±2. These are upper bounds,
    since in a three-way tie the smallest gap need not involve the learner's rule.
- **Which ties occur:**
  - The commonest is hit rate = false-alarm complement = equal priors, which happens whenever hit + false alarm =
    100%: 648 of the 1,688 cases.
  - The demo's tie (joint occurrence and subtraction) is 105.
  - These counts are over cases, not weighted by how often the tutor draws them.

**Range.** Every wrong rule's answer on every problem in the tutor's pools lies between 3% and 95%, and the hit rate
always exceeds the false-alarm rate. So at noise up to ±2 no wrong-rule learner's answer is ever clipped, and
subtraction is never negative.

**Derived from these before any learner runs**, for single-rule learners in event E (section 5):
- **No other endings are possible.** SAID-CORRECT and NO-KNOWN-STRATEGY cannot occur: the first answer fits the
  learner's rule, and the correct answer is more than 2 points from every wrong one, so it cannot also fit.
  NO-FOLLOW-UP cannot occur either: every census case has a follow-up. So every session in E ends as NAMED-RIGHT,
  NAMED-OTHER or POSSIBLE-SLIP.
- **Noise 0:** the tutor names the learner's rule every time. Their answer fits their rule, and every other
  survivor is more than 2 points away. Noise 0 is described, not primary.
- **Noise ±2, the learner's own rule:** the second answer fits the learner's rule for 3 of 5 noise draws if that
  rule's answer on the follow-up is a whole percent, and 2 of 5 if not. It cannot fit two survivors at once. So:
  - for base rate, hit rate, false-alarm complement and subtraction, whose answers are always whole percents on the
    tutor's 5% grid, **NAMED-RIGHT is exactly 60%**;
  - for joint occurrence and equal priors it lies between 40% and 60%.

  NAMED-RIGHT is fixed by arithmetic and is never called accuracy.
- **NAMED-OTHER is not fixed in advance.** It is the part of the remaining 40–60% where the second answer lands on
  another survivor rather than on nothing. It can be above 0 only through the close follow-ups above. It is the
  number this plan exists to measure.

## 5. What is reported

**Event E**: the learner's first answer fits two or more wrong rules, one of them the learner's own.

**Primary.** Ambiguous start, noise ±2, the six wrong-rule learners at weight 1/6 each. Among sessions in E, the
shares **NAMED-OTHER**, NAMED-RIGHT and POSSIBLE-SLIP, pooled: Σ P(outcome and E) / Σ P(E). Beside it: the
unweighted mean of the six per-learner shares, and P(E). The headline is NAMED-OTHER, always quoted with NAMED-RIGHT
and the no-name share, and with the arithmetic in section 4.

**Co-headline.** Over **all** ambiguous-start sessions of the six wrong-rule learners at ±2, in E or not, the share
naming a rule other than the learner's. This catches noisy first answers that fit only a rule the learner does not
use, which fall outside E. It is quoted beside v16's 0.4% (default start).

**Demo problem.** The same shares, exact, for the demo's first problem 60/75/30 (trading) alone:
- for the subtraction and joint-occurrence learners, at every noise level;
- for every single-rule learner at ±2;
- over all the follow-ups the tutor can choose for it.

These are quoted whenever that problem is on screen.

**Described, no pass or fail:**
- the primary at noise 0 and ±1;
- the primary split by tie group;
- for both starts, every learner's outcome shares at every noise level, including SAID-CORRECT,
  NO-KNOWN-STRATEGY, ACCUSED for the correct learner, and MISLABEL (any rule named) for switchers and unknown rules;
- the checks in section 3.

**Reading, fixed now.** There is no comparison arm and no threshold.
- **No comparison arm.** One fixed second problem with whole-percent answers far apart would score 60% right and 0%
  other for single-rule learners. That is a real cost of the adaptive follow-up under a 1-point window, not a quirk.
  But plan v17 showed it fails learners who retype their first number. A comparison here would only repeat v17's
  arithmetic.
- **No threshold.** We have no principled threshold for an acceptable NAMED-OTHER.
- **The slide sentence.** The numbers are reported as they are. The only sentence we will put on a slide has this
  form: "Scripted one-rule learners, answers off by up to 2 points, exact computation, not people: when a first
  answer fitted two wrong rules including the learner's, the tutor then named the other one in Y%, named none in Z%,
  and named the learner's in X% (arithmetic caps this at 60%). Over all such sessions it named a wrong rule in W%."

## 6. Limits written in advance

- **Scripted learners.** The learners are scripted and the noise is assumed. "Exact" removes sampling error, not
  model error. Equal weight for the six rules is a convention, not how common the rules are.
- **The tutor's draw.** The weighting follows the tutor's random draw of first problems, but the demo always shows
  60/75/30. Hence the separate demo report.
- **NAMED-RIGHT** is fixed by arithmetic (section 4).
- **Nothing about people.** Nothing here is evidence about real students, their working, or learning.

## 7. Seen before writing this plan (disclosed)

- **Earlier plans:** everything disclosed in plans v16 and v17 and addendum v17.1, and the full v16 result.
- **Plan v17's output** was read after the first draft of this plan and before publication. It covers the default
  start only and says nothing about the ambiguous start. The revisions after reading it are listed below; none uses
  a v17 number.
- **Tutor facts:** the census and range in section 4, both tutor-only with no learner.
- **Smoke test:** to check that the script runs, the exact computation was run once for a learner outside this plan
  (always types 50%), and one real ambiguous-start session was started without answering.
- **Outside reviews.**
  - *The design:* two general-purpose AI assistants reviewed the idea, given no data. One proposed the ambiguous
    start, the census and no comparison arm; the other proposed exact enumeration. We dropped a proposed 1%
    threshold (no principled value) and widened exact enumeration from the demo problem to every first problem.
  - *The first draft:* two more reviews (the same kinds of assistant). From them we added the pooled-versus-mean
    statement, the co-headline over all sessions, the demo-problem report, checks 2 and 3, the switchers and unknown
    rules, and the facts that within E only three outcomes are possible and that NAMED-RIGHT is exactly 60% for four
    rules. We verified, rather than assumed, that no answer is clipped and that the search within a story is
    deterministic.

## 8. Files and procedure

| File | SHA-256 |
|---|---|
| `v18.py` | `9720a893a2446aa84d90b26cda72adf5c21a246e171edbbe9571c0d78f11fccb` |
| `test_v18.py` | `ae04cd5c4e2a5061bdc2ccec7cfa678a72d97905b0ca9f3c92a4995d856be146` |
| census output (`census_v18.json`, private) | `c226d64e896acd83d779edc2423f13e84f0b518d13979f5456ead0267f82f2aa` |
| `src/tutor.py` | `73f4374a50dcc49c8732ed85ad484f32eedce7efddf0c48818812f7f8740ba0c` |
| `src/bayes_strategies.py` | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `src/topic_engine.py` | `3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a` |
| `src/remediation.py` | `938df557de2ae5c71bc21b2a8f7a77c411b71e66bf92f3da3d9d61888bf52dc5` |
| `src/score_quiz.py` | `80f3b2bcc52c4492243c39b1ee1dabdafb42dfa0ea3af317f6e66a7ee84b97b3` |
| `src/screening_quiz.py` | `a86c27da98dea87c310575c813378012f3c7e0934cd6c45c31b329c01df96a10` |

1. The tests check the helpers on made-up values and one tutor-only fact: the demo's follow-up 5/75/5 is a
   candidate. They compute no outcome for any learner in this plan.
2. Publish this plan byte-identical under tag v18 (plan text only, as for v16 and v17). Record its SHA-256.
3. Run `python3 v18.py census <repo root at a736100> census_v18.json` and confirm its SHA-256 matches the table.
   Then run `python3 v18.py run <repo root at a736100> v18_out.json > v18_report.txt` once. The script stops if any
   frozen file differs.
4. Report every number in section 5. Any change after publication is a dated, published addendum.
