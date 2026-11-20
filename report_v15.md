# Report v15: does naming a rule predict a person's answers to other problems? (Lin et al. 2026)

**Plan:** v15 (tag v15, `prereg_next_answer.md`, SHA-256 0be6e73e…7fa31), published on 18 November 2026 at 17:07 IST,
before the analysis code was written. **Run once** on 18 November 2026 with
`python3 -P src/next_answer.py real … --run-once` (code `src/next_answer.py`, SHA-256 27a7e52c…; written after the
plan and tested on made-up answers only). **Real adults** from the open data of Lin et al. (2026): Experiment 1
(177) and the self-paced block of Experiment 2 (83). Only derived numbers are reported.

Every number below is copied from the run's output `next_answer_results.json` (aggregates only; SHA-256 in section
6), except where marked "derived", which means arithmetic on printed numbers.

## 1. Who was analysed

260 people: Experiment 1 probability format 100, frequency 77; Experiment 2 probability 49, frequency 34. Nobody was
left out of any comparison. Two people had an exact tie between two rules (both 100% minus false alarm and equal
priors).

## 2. Primary (plan section 4A)

Mean error over each person's 10 to 20 target answers, in percentage points:
- **P1, "same numbers again":** 14.521.
- **P2, "named rule":** 14.083.
- **P2 minus P1: −0.439, 95% interval [−1.654, 0.786]** (10,000 resamples of people, seed 20261118).

**Reading fixed in the plan: the interval includes 0, so there is no evidence either way.** These data do not show
that naming a rule from 8 answers predicts a person's other answers better or worse than repeating their own
average answers.

## 3. Described, no pass or fail (plan section 4B and 4C)

- **Other predictors:** P0 (the average of other people) 22.372 [21.461, 23.295]; P3 (a rule only when it fits at
  least 6 of the 8 inputs within 2 points, otherwise P1) 12.288 [11.195, 13.391]; sham P1 27.522 [25.885, 29.162];
  sham P2 27.741 [25.908, 29.571].
- **By experiment:** Experiment 1, P1 16.017 and P2 16.490; Experiment 2, P1 11.331 and P2 8.950.
- **P2 better than P1** for 142 people, tied for 11, worse for 107 (54.6% better).
- **Rules P2 picked:** hit rate 61, base rate × hit rate 48, base rate 43, Bayes 42, hit rate − false alarm 30,
  equal priors 22, 100% − false alarm 12, tie 2.
- **P3 gave a rule to 97 people.** Among them, P2 error 4.570 against P1 10.557 (P2 better for 75, tied 11, worse
  11). For the other 163 people (derived from the totals): P2 about 19.7 against P1 about 16.9. This split is chosen
  by how well a rule fits the person's inputs, so it describes when naming helps; it is not a test.
- **Secondary targets at a 40% base rate:** P1 15.828, P2 14.458, P3 12.356, P0 16.849.
- **Move table (4C):** 260 people had a group in both showings; raw agreement 0.750, kappa 0.620. The plan states
  in advance that the "large positive move" group includes people who answer correctly, people who copy the base
  rate, and people who multiply base rate by hit rate, so no verdict is drawn from it.

Full tables by experiment and format are in the output file.

## 4. What it does not show (plan section 5)

- A rule that predicts well is a better description of the answers, not proof of what the person did.
- P1 uses two numbers from the person; P2 chooses one of seven fixed rules. The comparison is "which is more useful
  at the same cost of 8 answers", not a comparison of equally flexible models.
- At base rates of 1% and 97% the correct answer and "copy the base rate" are within about 7 points on every input
  and target problem, so test A cannot tell those two rules apart. The 40% targets can.
- Inputs and targets come from the same session and the same kind of problem. Nothing here shows transfer to our
  tutor's problems or to other topics, and nothing here is about learning.
- Both samples had been analysed before (plan section 2), and the idea came after those results. Only test A has a
  fixed reading.

## 5. Deviations and disclosures

- **One rule decided before the run but not in the plan:** if two rules tie exactly, P3 checks the average of their
  values. It was recorded in the lab log before the run. It affects at most the 2 people with tied rules.
- The run was made on 18 November 2026 and logged privately the same day; it was not published until now, at the
  team lead's instruction at the time. Its output has not changed (same SHA-256 as logged then).

## 6. Files

| File | SHA-256 |
|---|---|
| `next_answer_results.json` (not published: Lin et al. give no data licence) | `1fd527908a6c5f75e578d76a74ef8ba7f2bce1a1f6994930f7c95e514bf5b8bf` |
| `src/next_answer.py` | `27a7e52c6894d923f153775913abb1656405cfb579eaa5356c9ae3fc902f4a04` |

Written 20 November 2026, from the saved output of the single run.
