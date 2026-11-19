# Plan v22: can each published Bayes problem be fixed by changing one number?

Written 19 November 2026, before the check below is run on any published number set. To be published byte-identical
under tag v22 before it is run. **No learners and no human data: this is arithmetic on the item file that addendum
v20.1 locked.**

## 1. Question

Plan v20 found that in 21 of the 23 distinct number sets printed in six published sources, a common wrong method's
typed answer either fits the correct answer (M1) or fits another wrong method (M2), within 1 point.

**For each of those number sets, what is the smallest change to one of its three numbers that removes every such
collision?**

## 2. Definitions (fixed now)

- **Items.** The standard rows of `items_v20.csv` (locked in addendum v20.1; SHA-256 in section 6), each
  unique number set counted once, exactly as in v20.
- **Collision.** v20's own `audit` function and definitions, at the 1-point tolerance, with v20's six wrong methods,
  imported unchanged from `v20.py` (SHA-256 in section 6).
- **A fix.** Change one of base rate, hit rate or false-alarm rate by a whole number of percentage points (1 to 40),
  starting from its printed value. The result must keep every number strictly between 0 and 100 and the hit rate above
  the false-alarm rate. It must leave no M1 and no M2.
- **The smallest fix for a number.** The smallest such change. Minus is tried before plus at each size.
- **The smallest fix for a set.** The smallest over its three numbers. Ties are all reported.

## 3. What is reported (no threshold, no pass or fail)

- **For every number set:** its numbers, sources and collisions, and every number's smallest fix, with the correct
  answer before and after.
- **Primary.** Of the number sets with a collision, how many can be fixed by changing one number, and how many have a
  smallest fix of at most 1, 2, 3, 5, 10, 20 and 40 points.
- **Also:** the median and largest smallest fix, and which number gives a smallest fix (counted once per tie).

**The only slide sentence allowed has this form:** "Of the N published number sets with a collision, X could be fixed
by changing one number by at most Y points (median Z)." It must say "arithmetic, not tested on people."

## 4. Limits written in advance

- **The rules.** It covers only the six wrong methods, the 1-point window and the whole-percent typing rule of v20.
- **What a fix does.** It changes the problem, and usually its correct answer. It does not say the original problem
  was a bad teaching choice.
- **No students involved.** A fix is a property of the numbers, not evidence that students would then be diagnosed
  correctly.
- **The search space.** Whole-point steps from the printed value; finer or two-number changes are not searched.

## 5. Seen before writing this plan (disclosed)

- **Plan v20, addendum v20.1 and the full v20 report,** including every set's collisions.
- **No fix computed on any published set.** The same fix search has been run only on sets that are not among the 23,
  in two places:
  - in the team's Collision Checker page, which uses the identical algorithm. It was checked against v20's Python code
    on 18,919 made-up cases with every v20 number set excluded, with no mismatch;
  - on our demo problem (60/75/30, smallest fix: false-alarm rate 30 → 32) and made-up market-maker examples.
- **Tests.** `test_v22.py` uses made-up sets only.

## 6. Files and procedure

| File | SHA-256 |
|---|---|
| `v22.py` | `4a9a8740f40623c96df080bed40561df02c2944257f36d4ee5a9042b1f14a3b5` |
| `test_v22.py` | `1895b71b1d557e6fa0f8720c4fee846dd33035b89d398f39a07de9acbb3b875f` |
| `v20.py` | `c71003c8602d912409bc5ea07941d8e93796716c6f607470b8c5436c84232db3` |
| `items_v20.csv` | `5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236` |
| `src/bayes_strategies.py` | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `src/topic_engine.py` | `3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a` |

1. **Publish.** Publish this plan byte-identical under tag v22 (plan text only).
2. **Run once.** Run `python3 v22.py <repo root> <folder with v20.py> items_v20.csv`. Report every number in
   section 3.
3. **Changes.** Any change after publication is a dated, published addendum.
