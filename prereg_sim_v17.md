# Plan v17: does the adaptive follow-up earn its keep, and what does the tutor name for learners it does not model?

Written 19 November 2026, after the v16 result and before anything below is run. Revised before publication after an
independent check and two outside reviews (section 7). To be published byte-identical under tag v17 before it is run. **This is a simulation. No human data is read, used or produced.**

## 1. Questions

1. **Follow-up value.** The tutor picks its second problem from the first answer (an adaptive follow-up). Does that
   name the learner's rule more often, or wrongly less often, than giving everyone one fixed second problem, or a
   random one?
2. **Learners the tutor does not model.** How often does the tutor name one of its six rules for a learner who uses a
   rule it does not know, switches rule between the two answers, repeats their first number, guesses, or rounds to the
   nearest 5%? A name is then a mislabel (section 4).

## 2. The tutor, exactly as frozen

Same files and hashes as plan v16 (section 7 below). Default settings only: `tutor.Session(code, seed=i,
data_dir=<one new temporary folder for the whole run>)`, classic flow, normal start, `confirm=2`, collision filter
off. Every session has its own learner code (a running number), so no session is a returning learner. Answers are
whole percents typed with a `%` sign (so a typed 1% is read as 1%, never as the bare "1" that the tutor reads as
100%); noise is an integer drawn uniformly from −k to +k (each of the 2k + 1 values equally likely), added to the rule's
answer rounded to a whole percent, then clipped to 0–100, as in v16.

## 3. Part 1: follow-up value

- Learners: the seven of v16 (six wrong rules and the correct method), each applying its rule to every problem.
  Noise k = 0, 1, 2. For each learner type and noise level, sessions i = 0 to 1,999 (42,000 sessions).
- Each session's first problem and first answer are the tutor's own (seed i). Its two noise draws are fixed before the
  session, so the second answer differs between arms only because the second problem differs.
- Three arms for the second problem:
  - **adaptive**: the tutor's own follow-up (the real session);
  - **fixed**: one problem for everyone, chosen before any learner by this rule: among all 1,869 problems in the
    tutor's six story pools, the one whose seven rule answers have the largest smallest gap (ties: story order, then
    base, hit and false-alarm rate). It is base 90%, hit 60%, false alarm 20% (classroom story); its answers are at
    least 5 points apart;
  - **random**: a problem drawn uniformly from those 1,869 (its own fixed random stream per session), redrawn while
    its numbers equal the first problem's (the adaptive follow-up is never the first problem either).
- For the fixed and random arms the tutor's own naming rule is applied outside the session: a rule is named only if
  it fits both answers within 1 point (the tutor's `diagnose`, tolerance 1 point, with the first answer as prior). As
  a check of that code, the same outside rule is applied to every adaptive session that had a follow-up, and the
  number of sessions where it disagrees with the tutor is reported (expected 0).
- Outcomes as in v16: NAMED-RIGHT, NAMED-WRONG, ACCUSED, SAID-CORRECT, NO-NAME.
- Also recorded per session: how many of the six wrong rules fit the first answer within 1 point (2 or more: an
  ambiguous first answer, like 45% on 60/75/30), and, per arm, whether both answers fit the learner's own rule within
  1 point. That last share is the **ceiling**: no second problem can name the right rule in a session where it is
  false, because the tutor names a rule only if both answers fit it.

## 4. Part 2: learners the tutor does not model

Each learner below runs in the **adaptive** arm (the real session) and in the **fixed** arm (same first problem and
first answer, then the fixed problem of section 3, with the tutor's naming rule applied outside the session).

- **Three rules the tutor does not know**, chosen for this test, not from data: "forgets the complement",
  b·h / (b·h + f); "averages base rate and hit rate", (b + h) / 2; and "total positive rate", b·h + (1 − b)·f.
  Noise k = 0 to 3; 2,000 sessions per rule and noise level.
- **Switchers**: one wrong rule on the first problem and a different wrong rule on the second, for all 30 ordered pairs
  of the six rules. Noise k = 0 to 3; 400 sessions per pair and noise level.
- **Repeater**: on the first problem, the answer of one of the six wrong rules (drawn at random per session), with
  noise k = 0 or 2; on the second problem, the same typed number again. 2,000 sessions per noise level. This is the
  learner the tutor's rule "every surviving rule's answer moves at least 10 points" is meant to catch.
  **In the adaptive arm the result is fixed by design, not found:** every wrong rule that fits the first answer within
  1 point gives, on the adaptive follow-up, an answer at least 10 points from its first-problem answer; a repeated
  number is within 1 point of the first-problem answer, so it is at least 9 points from that rule's follow-up answer,
  fits no surviving rule, and no rule can be named. The run checks that the code behaves this way (expected 0). The
  quantity actually measured is the fixed arm's.
- **Uniform guesser**: every answer a whole number drawn uniformly from 0 to 100; 2,000 sessions.
- **Anchor guesser**: for each problem independently, one of the base rate, hit rate, false-alarm rate, 100 minus the
  false-alarm rate, or 50%, drawn uniformly; 2,000 sessions. The draws are recorded.
- **Rounded correct learner**: the correct answer rounded to the nearest multiple of 5%; 2,000 sessions.
- **Rounded wrong-rule learners**: each of the six wrong rules, its answer rounded to the nearest multiple of 5%, no
  other noise; 2,000 sessions per rule. (Rounding uses Python's `round`: an exact half goes to the even multiple.)
- A **mislabel** is any named rule, with these exceptions where the name describes what the learner did: for the
  anchor guesser, when both draws were the same anchor, that anchor is a rule's answer (base rate, hit rate or 100
  minus the false-alarm rate) and that rule was named; for a rounded wrong-rule learner, naming its own rule. For the
  rounded correct learner a named rule is an accusation.
- **For the repeater, two measures.** Primary: **named without new evidence**, any rule named, because the second
  answer was the first number typed again and so cannot confirm anything. Secondary: a rule other than the one whose
  answer it typed on the first problem.
- In total 24,000 + 48,000 + 4,000 + 2,000 + 2,000 + 2,000 + 12,000 = 94,000 sessions, each in both arms.

## 5. What is reported

All shares use **all simulated sessions** of the group as the denominator. Shares among sessions that reached a second
problem are reported as a secondary breakdown: for Part 1, right and wrong rule named per arm and noise level; for
Part 2, the mislabel share per kind, arm and noise level.

**Primary 1.** Noise ±2, the six wrong-rule learners pooled (12,000 paired sessions): the share NAMED-RIGHT in the
adaptive arm minus the fixed arm, with a 95% interval from resampling whole sessions within each rule (10,000 times,
seed 20261120). The discordant session counts (right in one arm only) and an exact McNemar p are reported with it.
**Co-primary 1:** the same difference for NAMED-WRONG. Also co-reported: both differences for adaptive minus random. Noise 0 is
not the primary: there both arms must name the learner's rule every time (the fixed problem's rule answers are at
least 5 points apart, and v16 found 100% for the adaptive arm), so it cannot tell the arms apart. Sensitivity: both
differences with sessions whose first problem is the fixed problem left out (their number is reported). Breakdown,
fixed now: both differences separately for ambiguous first answers (2 or more wrong rules fit) and the rest.

**Primary 2.** For each kind of learner in section 4 separately (each unknown rule, switchers, uniform guesser,
anchor guesser, each rounded wrong-rule learner; noise 0 and ±2 where they exist), the share of sessions with a
mislabel in the adaptive arm, with exact (Clopper-Pearson) 95% intervals, and for the rounded wrong-rule learners the
share naming their own rule; for the rounded correct learner, the shares accused, told correct and given no name. The
repeater is reported under verdict 2. No headline rate pooled across kinds of learner is computed.

**Repeater comparison (verdict 2).** At noise 0 and at ±2 separately, on the same 2,000 paired sessions: the share
named without new evidence in the adaptive arm and in the fixed arm, with exact intervals, the discordant counts and
an exact two-sided McNemar p. The secondary measure (section 4) is reported beside it.

**Described, no pass or fail:** the adaptive-minus-fixed and adaptive-minus-random differences for NAMED-RIGHT and
NAMED-WRONG at noise 0 and ±1; each arm's outcome shares (including SAID-CORRECT); per arm and noise level the
ceiling (section 3), NAMED-RIGHT as a share of the ceiling (never quoted as the headline, which is always the share
of all sessions), and wrong names per name issued, NAMED-WRONG / (NAMED-RIGHT
+ NAMED-WRONG); per rule NAMED-RIGHT at every noise level in each arm; the correct learner's ACCUSED and SAID-CORRECT shares per arm; for Part 2, every kind, arm and noise
level: mislabel share, follow-up share and which rule was named; for switchers in each arm, whether the named rule was
their first, their second or neither. The count of sessions whose first problem is the fixed problem is reported over
all 42,000 Part 1 sessions; the ±2 count shows as the drop in paired sessions in the sensitivity line.

**Reading, fixed now, for these simulated learners. Two separate verdicts; neither can rescue the other.**

- **Verdict 1, learners who use one rule, noise ±2.** For right rule named (adaptive minus fixed), the adaptive
  follow-up is better on that measure if the interval lies entirely above 0 and worse if entirely below 0. For wrong
  rule named (adaptive minus fixed), it is better if the interval lies entirely below 0 and worse if entirely above 0.
  An interval that includes 0 shows no difference on that measure. Verdict 1 is exactly one of four outcomes:
  (1) **adaptive better**: better on at least one measure, worse on neither; (2) **fixed better**: worse on at least
  one measure, better on neither; (3) **trade-off**: better on one, worse on the other, and we will say which;
  (4) **no clear difference**: both intervals include 0. The verdict is always quoted with both differences in points
  and their intervals, so a small difference is never presented without its size. The report script prints the
  outcome from the intervals.
- **Verdict 2, repeaters, at noise 0 and at ±2 separately.** We will say the adaptive follow-up protects against
  learners who repeat their first number at that noise level only if the fixed arm names without new evidence in more
  paired sessions than the adaptive arm and the exact two-sided McNemar p is below 0.05. Because the adaptive result
  is 0 by design (section 4), this is a check of a design property and a measure of what one fixed problem would
  allow, not a discovery; it is always described that way. If the adaptive arm names a rule for any repeater, that is
  reported as a fault in the code, not as a verdict.
- We will not combine the two verdicts into one claim that the adaptive search is "essential". Each is reported and
  quoted on its own.
- Primary 2 has no fixed reading; each share is reported as the mislabel rate for that kind of learner.

Every number is reported whatever it shows, and always with the word "simulation".

## 6. Limits written in advance

- All learners are scripted. The unknown rules, switchers, repeater, guessers and rounding are our choices, not
  measured human behaviour; their shares say nothing about how common they are in real students.
- The fixed problem is the best single problem by one design rule (largest smallest gap), chosen without running
  any learner. We did not search for the fixed problem that does best in simulation; one chosen that way, or two fixed
  problems, could do better.
- The ceiling (section 3) shows how much of any low right-rule rate comes from the 1-point tolerance and the noise
  rather than from the choice of second problem. It is an upper bound, not an exact count.
- The fixed problem's six wrong-rule answers are all whole percents (40, 54, 60, 75, 80, 90). A noisy whole-percent
  answer at ±2 fits a whole-percent rule answer within 1 point for 3 of the 5 noise values, but a fractional rule answer
  (such as 3.75%) for only 2 of 5. This can favour the fixed arm on right-rule-named for a reason unrelated to how well
  it separates rules; the ceiling is reported per arm so that its size is visible.
- Uniform noise is an assumption, as in v16.
- Nothing here is evidence about real students' answers, about agreement with their working, or about learning.

## 7. Seen before writing this plan (disclosed)

- Everything listed in plan v16, section 6, and the full v16 result (published at tag v16): at noise ±2 the tutor
  named a wrong rule in 52 of 12,000 sessions and accused 0 of 2,000 correct learners; the right rule was named in
  18–37% of sessions per rule.
- The fixed problem was computed from the tutor's own pools and rule predictions only (section 3); no learner was
  run to choose it.
- No session of Part 1's fixed or random arms, and no session of Part 2, has been run.
- Before publication this plan was read by an independent checker and by outside reviews (two general-purpose AI
  assistants, given the design but no data from this run, since none exists). Changes made because of them: the
  primary moved from noise 0 (decided in advance) to ±2; the repeater, anchor guesser and rounded correct learner were
  added; each kind of learner is reported separately; two separate verdicts replace one combined rule; verdict 1 has
  four named outcomes; the repeater's primary is "named without new evidence" (a draft that excused naming the first
  problem's rule was found to hide the failure the 10-point rule exists to prevent), and the adaptive repeater result
  is declared fixed by design; verdict 2 uses a paired exact McNemar test instead of non-overlapping intervals; the
  bootstrap resamples within each rule; the random arm never repeats the first problem; the ceiling, wrong names per
  name issued and the ambiguous-first-answer breakdown are reported; a third unknown rule and the rounded wrong-rule
  learners were added.
- Suggestions considered and not adopted: choosing the fixed problem by simulated naming rate (it would need a tuning
  run; the learner-free rule is kept and its limit stated in section 6); minimum differences that matter (we have no
  principled values; sizes are always quoted instead); more sessions; a learner whose rule depends on the base rate
  (left for a later plan).

## 8. Files and procedure

| File | SHA-256 |
|---|---|
| `sim_v17.py` | `e63eb511125438c4a3234b0fffd14dd45f970d11addbbbc7dbb4d081ec0542ce` |
| `report_v17.py` | `53be819ffb8fec54d6c62073560a92ec5963ff8a87389f8c271b37fc1de50f97` |
| `test_sim_v17.py` | `271149f6f1decff5eb7271cc361fda8a6c3fc76fe2d742ea55c5b36622aaaa10` |
| `src/tutor.py` | `73f4374a50dcc49c8732ed85ad484f32eedce7efddf0c48818812f7f8740ba0c` |
| `src/bayes_strategies.py` | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `src/topic_engine.py` | `3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a` |
| `src/remediation.py` | `938df557de2ae5c71bc21b2a8f7a77c411b71e66bf92f3da3d9d61888bf52dc5` |
| `src/score_quiz.py` | `80f3b2bcc52c4492243c39b1ee1dabdafb42dfa0ea3af317f6e66a7ee84b97b3` |
| `src/screening_quiz.py` | `a86c27da98dea87c310575c813378012f3c7e0934cd6c45c31b329c01df96a10` |

1. The tests check the helpers on made-up values only; they run no simulated session. The report script was also
   run once on a small file of made-up rows, to check that it prints every table.
2. Publish this plan byte-identical under tag v17. Record its SHA-256.
3. Run `python3 sim_v17.py <repo root at a736100> rows_v17.json` once, then `python3 report_v17.py rows_v17.json`. The
   script stops if any frozen file differs.
4. Report every number in section 5. Any change after publication is a dated, published addendum.
