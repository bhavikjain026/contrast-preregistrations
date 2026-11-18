# Plan (v15 CANDIDATE): does naming a rule predict a person's answers to other problems?

Status: **v15 CANDIDATE, not published, not approved.** Built on 18 November 2026 from DRAFT v2 (SHA-256
cc144e0a2d97c5a07076cd1675ea83c9a15af34a57c3bc6804688e70faf95bd6). It replaces draft v1 ("what do adults do when the
base rate goes from 1% to 97%?") of the same day, which was never published. To be published with the next free tag
(expected v15) before anything below is run. Nothing below has been run. Every change from DRAFT v2 is listed in
section 7.

Why draft v1 was dropped. An outside review on 18 November found three faults in it. (1) Its branch "FOLLOWS"
(a large move) also fits a person who copies the base rate or multiplies base rate by hit rate, so the name
claimed understanding that the data cannot show. (2) Its one test used only people who were not flat in BOTH
showings. Choosing people by their later answers can make agreement look perfect while half of all people
change. (3) Agreement between two labels is not what a tutor needs. A tutor needs to predict the next answer
from what it has seen so far.

Sources used for sections 2 and 3 (no answer column opened, printed, summarised or computed on): the published v10
plan (`prereg_lin_mixture.md`, SHA-256 05ef4c94…88f31) and, for the record of past runs, the published v2 and v3 plans,
`results.md` (entries of 2026-10-13 and 2026-11-16/17), the code of the v2 run (`src/lin2026_replication.py`,
`src/stengard_analysis.py`, read for definitions only) and the field names, never the values, of the stored outputs.

## 1. Question

Our tutor names a rule from a learner's numeric answers (for example "you answered with the hit rate").
If a named rule describes a person, it should predict that person's answers to OTHER problems.

Primary question: from the same 8 answers, which predicts a person's answers to other problems better:
(P2) the rule that fits those 8 answers best, or (P1) simply assuming the person will give the same numbers again?

## 2. Data, and what has already been seen

- Data: the two samples used in v10 (Lin and co-authors; Experiment 1, 177 adults, our 2026-10-13 copy, SHA-256
  09215735…965b233; Experiment 2, 83 adults, self-paced block, SHA-256 bcdd9b0c…7a6b). v10 excluded no one from these
  blocks; neither does this plan. Missing answers follow v10's rule (section 3). The time-limited block is not used.
- Design (from the v10 plan and our design-column checks): 27 problems, a 3 x 3 x 3 grid of base rate {1, 40, 97}%,
  hit rate {53, 72, 90}%, false-alarm rate {11, 31, 42}%, all varying within person. Each problem was shown twice, in
  an order that differs by person: 54 trials per person in Experiment 1 and 54 rows per person in the Experiment 2
  self-paced block. Showing 1 of a problem is its earlier presentation (by `n_trial` in Experiment 1, by
  `trial_in_block` in Experiment 2), showing 2 the later one (v10 §6). Both experiments had two formats between
  people (Experiment 1: probability 100, frequency 77; Experiment 2: probability 49, frequency 34).
- Not documented in our sources: the cover story, the wording in the frequency format, how far apart the two
  showings are, whether feedback was given, and how Experiment 2 answers were entered. No analysis below depends on
  these. If the preprint settles them, that is added as a dated addendum.
- **Already computed by the team on these people:**
  - **v2 (2026-10-13; Experiment 1, 177; all 54 answers).** Base-rate, false-alarm and (exploratory) hit-neglect
    labels, and a **per-person method label**: for a set of trials, the one of the same seven rules as section 3
    that matches the most answers within 1 point (a tie broken by the smaller mean absolute difference; a remaining
    tie is its own "unresolved" category). This label was computed on random halves of the 27 problems (100 splits)
    and on showing 1 against showing 2, and only its agreement was scored: split-half 71.6%, kappa 0.65;
    showing 1 against showing 2 65.0%, kappa 0.57 (base-rate neglect label: 87.8% / 0.73 and 82.5% / 0.63). Only
    these summaries were stored, no per-person label. Whole-data groups: base-rate neglect 61, false-alarm neglect 57,
    unresponsive 4, close to correct 11.
  - **v3 (2026-10-13; Experiment 1, 177).** From **the same 8 inputs as this plan**, four methods (the tutor's pair
    check, the learner profile, Qwen2.5-14B, a majority guess) labelled each person "ignores the base rate" or not,
    and each label was scored against a reference label computed from **the person's answers to the other 19
    problems** (tutor check 87.3% correct when it committed, coverage 44.6%; profile 67.2%; majority 63.3%). Only
    summaries were stored.
  - **v10 (2026-11-17; Experiment 1 and Experiment 2, both blocks).** From the same 8 inputs, a fitted model and a
    one-feature rule predicted each person's base-rate-neglect label from showing 2 (all 27 second-showing answers,
    which include the target problems of section 3); primary skill on Experiment 2, 0.671. The model was fitted on
    all Experiment 1 answers (both showings), so every Experiment 1 target answer has entered a fit. Also stored: the
    flat / not-flat label from each showing, the model's predictions and, per person, the mean first-showing move on
    the four input pairs (`simple_feature`).
  - **Has anything scored whether a rule label predicts a person's other answers?** At the level of a label, yes.
    v2 scored whether the seven-rule label from one half of a person's problems agrees with the label from the
    other half (and from showing 1 against showing 2). v3 and v10 scored whether a label made from these same 8
    inputs matches a label made from the person's other answers. **No earlier run predicted the answer values
    themselves, measured an error in points, or compared a named rule with "same numbers again" (P1).** So test A
    is not a repeat of an earlier test, but it is close to v2's split-half method label, and its reading must be
    stated next to that result.
  - The Round 1 abstract (October 2026) reported v2 and v3 figures.
- This plan was written after the v10 result and after an outside review. It is a follow-up on known data.

## 3. Definitions

- **Answers** are in percentage points, 0 to 100, as v10 used them: the value of the answer column (`inputvalue`),
  as stored, in both formats. In the frequency format the answer is a number out of 100 (v10 §4), so it is read as
  the same number of percentage points. No answer is rescaled, rounded or corrected. Rule values are not rounded.
- **Missing answers (v10 §6.1, in words).** An answer is missing if its row is absent, its value is blank or not a
  number, its value is outside 0 to 100, or the data's own `invalid_input` flag is true. Missing answers are left
  out; nothing is filled in; no person is excluded because of them. In this plan:
  - each predictor uses whichever of the 8 inputs are present (P1 at 1% uses the present 1% inputs; at 97% the
    present 97% inputs; P2's and P3's fits use the present inputs);
  - a person with no present input at 1%, or none at 97%, has no P1 (and no sham P1 as a donor); a person with no
    present input has no P2 or P3; a person with no present target has no score. Such people are left out of the
    comparisons that need them, and the numbers left out are reported;
  - a person's error is the mean over that person's present targets.
- **Inputs** (what a predictor may use): the person's 8 first-showing answers to the four pairs v10 used:
  (hit, false alarm) = (72, 42), (53, 31), (90, 42), (72, 31), each at base rates 1% and 97%.
- **Targets** (what is predicted): the same person's answers, in both showings, to the 10 problems at base rates
  1% and 97% in the five OTHER (hit, false alarm) cells: (53, 11), (53, 42), (72, 11), (90, 11), (90, 31).
  That is up to 20 answers per person. No target problem is an input problem. (The second showings of the four
  input pairs are neither inputs nor targets.)
- **Secondary targets**: the person's answers to the 9 problems at base rate 40%, both showings (up to 18).
- **The seven rules**: correct (Bayes); hit rate; base rate; 100 minus false-alarm rate; hit rate minus
  false-alarm rate; base rate times hit rate; hit rate / (hit rate + false-alarm rate). (The same seven as v2 and the
  tutor.)

Predictors. All use only the 8 inputs of the person being predicted (except P0).

- **P0, nobody in particular.** The mean answer to that problem and showing among all OTHER people in the same
  experiment and format (present answers only).
- **P1, same numbers again.** Predicted answer at base rate 1% = the mean of the person's present input answers
  at 1%. At 97% = the mean of their present input answers at 97%. For the secondary targets at 40%: the point on
  the straight line between those two means (at 39/96 of the way).
- **P2, named rule.** The rule among the seven with the smallest mean absolute difference from the person's present
  inputs. The prediction is that rule's value on the target problem. If two or more rules tie (mean absolute
  differences within 10⁻⁹ points of each other), the prediction is the mean of their values.
- **P3, named rule or no name** (secondary; a simple stand-in for the tutor's policy, not the tutor itself, which uses
  a 1-point tolerance and a follow-up problem). If P2's rule is within 2 points of at least 6 of the 8 inputs (a
  missing input counts as not within), predict with that rule. Otherwise predict with P1. Report how many people get
  a rule.
- **Sham person** (control). P1 and P2 computed from ANOTHER person's inputs and scored on the person's own targets:
  within each experiment × format group (in the order Experiment 1 probability, Experiment 1 frequency, Experiment 2
  probability, Experiment 2 frequency), people are re-paired by a random permutation from numpy
  `default_rng(20261118)`, redrawn until nobody is paired with themselves.

Score. For each person and predictor: the mean absolute error over that person's present target answers, in points.

## 4. What is reported

**A. The primary test.** The paired difference "P2 error minus P1 error", averaged over all people with both scores
(Experiments 1 and 2 together; at most 260), with a two-sided 95% percentile interval from resampling people 10,000
times (numpy `default_rng(20261118)`). Reading, fixed now:
- interval entirely below 0: naming a rule predicts answers to other problems better than "same numbers again";
- interval entirely above 0: naming a rule predicts worse. Then these data give no support for naming a rule
  from numeric answers, and we will say so;
- interval includes 0: no evidence either way, reported as such.

**B. Around the primary test (description, no pass or fail).**
- Mean error of P0, P1, P2, P3 and the two sham versions, each with a percentile interval from the same 10,000
  resamples; each experiment and each format separately as well as together.
- Share of people for whom P2 beats P1 (ties counted separately).
- Which rule P2 picked, as a count per rule, and P2's and P1's error within each group.
- For P3: how many people get a rule; among them, P2 error against P1 error.
- The same table for the secondary targets (base rate 40%).

**C. The move table (description only; replaces draft v1's test).** For all nine pairs (base rate 1% against
97%), both showings: move = answer at 97% minus answer at 1% (a pair is used only if both answers are present).
Four groups, named by what is seen: LARGE POSITIVE MOVE (at least half the correct move of that pair); SMALL POSITIVE
MOVE (more than 5 points, less than half); FLAT (minus 5 to plus 5, ends included); NEGATIVE MOVE (below minus 5). A
person's group in a showing is the most frequent group among their used pairs; a tie for most frequent is MIXED; a
person with no used pair has no group (counted).
Reported: the share of people in each group; the full 5-by-5 table of first-showing group against
second-showing group for EVERYONE with a group in both showings; raw agreement and kappa over everyone; agreement
within each group.
Stated in advance: LARGE POSITIVE MOVE includes people who answer correctly, people who copy the base rate,
and people who multiply base rate by hit rate. It is not a sign of understanding. No verdict is drawn from
this table.

Every number is reported whatever it shows.

## 5. Limits written in advance

- A rule that predicts well is a better description of the answers. It is not proof of what the person did.
- P1 uses two numbers taken from the person; P2 chooses one of seven fixed rules. The comparison is "which is
  more useful at the same cost of 8 answers", not a comparison of equally flexible models.
- P2 picks its rule by the smallest mean absolute difference; v2's method label and the tutor pick by matches within
  1 point. The two can name different rules for the same answers.
- Inputs and targets come from the same session and the same kind of problem. Nothing here shows transfer to
  our tutor's word problems, to new people's first answers, or to other topics.
- The showings may be mixed in one sequence, so targets are not known to come after inputs.
- Both samples have been analysed before (section 2), including label-level versions of this question, and the idea
  came after those results. Only test A has a fixed reading.
- Nothing here is evidence that any tutor or lesson helps anyone learn.
- At base rates of 1% and 97% the correct rule and "copy the base rate" give nearly the same numbers (within about 7 points
  on every input and target problem). So test A cannot tell those two rules apart. It mainly tests whether a person's
  answers follow the hit rate and the false-alarm rate in the way a named rule says. The secondary targets at a 40%
  base rate can tell them apart.

## 6. Procedure

1. Check sections 2 and 3 against design documents and the record of past runs. Do not open answer columns to
   do this. List every fix. *(Done in this candidate; section 7.)*
2. Write the analysis code and commit it before it is run on real answers. Test it on made-up answers only,
   including one made-up person per rule (P2 must recover each rule, from exact and from whole-number answers),
   one who types the same number always, and people with missing inputs and targets.
3. Publish this plan byte-identical under the next free tag. Record its SHA-256.
4. Run once. Report every number in section 4. Any later change is a dated, published addendum.

## 7. Changes from DRAFT v2

1. §2: v2's "per-person method labels" defined as v2 computed them (most matches within 1 point among the same seven
   rules; tie rule), with their agreement results; v3 and v10 added as label-level predictions from the same 8 inputs;
   the plain answer to "has this been scored before" stated; v10's Experiment 1 fit (all answers) and the abstract noted.
2. §2: file fingerprints; "v10's exclusions" made explicit (none); showing 1 / showing 2 defined as in v10; Experiment 2
   formats and the undocumented Experiment 2 entry mode added.
3. §3: "answers as v10 used them" defined for both formats (the stored value, 0 to 100; frequency format = out of 100).
4. §3: v10's missing-answer rule written out in words, with what each predictor does when inputs or targets are
   missing and who is left out (counted).
5. §3: the second showings of the input pairs stated to be neither inputs nor targets.
6. §3: P2's exact-tie rule given a numeric tolerance (10⁻⁹ points).
7. §3: P3 described as a stand-in for the tutor's policy, not "the tutor's actual policy" (the tutor uses a 1-point
   tolerance and a follow-up); a missing input counts as not within 2 points.
8. §3: the sham re-pairing made exact (groups, order, generator, redraw rule) and scored on the person's own targets.
9. §4A: denominator (people with both scores), interval type and generator named.
10. §4B: interval type stated; ties in "P2 beats P1" counted separately.
11. §4C: a pair needs both answers; a person with no used pair has no group; the 5-by-5 table covers everyone with a
    group in both showings.
12. §5: limit added on P2's selection rule differing from v2's and the tutor's.
13. §6: tests on made-up data extended to whole-number answers and missing answers.
14. §5: limit added: at base rates of 1% and 97% the correct rule and "copy the base rate" differ by at most 6.6 points
    on the input and target problems (design numbers, `analysis/next_answer/check_base_vs_bayes.py`), so test A cannot
    tell them apart; the 40% secondary targets can.
