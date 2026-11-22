# Plan v41: can each chatbot-written Bayes problem be fixed by changing one number?

Written on 22 November 2026, before the check below is run on any chatbot-written number set. To be published byte-identical under tag v41 before it is run. **No learners and no human data: this is arithmetic on the number sets that plan v23 locked.**

## 1. Question

Report v23 asked three chatbots, once each on 19 November 2026, to write 20 Bayes practice problems.

- **Arm 1, the plain request.** In 18 of 20, 20 of 20 and 16 of 19 distinct number sets, one whole-percent answer fits two of our tutor's six wrong methods (Q1). In 1, 3 and 2 sets, one fits the correct answer and a wrong method (Q3).
- **Arm 2, the request that stated our rule** (every two methods at least 3 points apart). All 60 sets were clean on both measures.

**For each Arm 1 number set with a collision, what is the smallest change to one of its three numbers that removes every collision?**

## 2. Definitions (fixed now)

- **Number sets.** The included rows of `extract_final.csv` (locked in addendum v23.1; SHA-256 in section 6), read with v23's own `load` function. Each distinct exact set (b, h, f) counts once within its reply, as in report v23.
- **Collision (primary).** Report v23's own exact measures, imported unchanged from `v23.py`: Q1, some whole-percent answer fits two wrong methods; or Q3, some whole-percent answer fits the correct answer and a wrong method. "Fits" is the tutor's own rule, within 1 + 10⁻⁷ points.
- **A fix.** Change one of base rate, hit rate or false-alarm rate by a whole number of percentage points (1 to 40) from its value, in exact arithmetic. Every number must stay strictly between 0 and 100, and the hit rate must stay above the false-alarm rate. The result must have no Q1 and no Q3.
- **The smallest fix for a number** is the smallest such change, with minus tried before plus at each size. **The smallest fix for a set** is the smallest over its three numbers; ties are all counted.
- This is plan v22's search space and order. The success test is stricter than v22's, because it uses v23's measures.
- **Secondary.** Plan v22's own collision check and fix search, imported unchanged from `v22.py`, on the same sets. This allows comparison with report v22 only.

## 3. What is reported (no threshold, no pass or fail)

The script prints hashes and counts only. **No number set is printed**, because the sets come from chatbot replies and chatbot output stays out of public files.

- **For each chatbot and arm:**
  - D, Q1, Q3 and v23's legacy count, as a check against report v23;
  - the number of sets with a collision, and how many can be fixed by changing one number;
  - how many have a smallest fix of at most 1, 2, 3, 5, 10, 20 and 40 points;
  - the median and largest smallest fix, and which number gives a smallest fix;
  - the median and largest change in the correct answer at the first smallest fix;
  - the secondary counts.
- **Primary.** Arm 1, summed over the three replies: sets with a collision, sets fixable by changing one number, and the median and largest smallest fix. The sum is of three single replies; it is not a sample, and no interval is given.

**The only slide sentence allowed has this form:** "Asked once on 19 November 2026, three chatbots wrote practice problems; in N of their 59 number sets, one typed answer could mean two different mistakes, or a mistake and the right answer. X of those N could be fixed by changing one number, by at most Y points (median Z). Arithmetic, not tested on people." It may add the registered v23 fact: "Told our rule, the same chatbots wrote 60 of 60 clean sets."

## 4. Forecast (written before the run)

The author of this plan forecasts that **about 28** of the Arm 1 sets with a collision can be fixed by changing one number, **with 15 to 40 as the range** expected. This is a guess from report v22 (12 of 21, with a weaker success test) and from report v24's grids, not a calculation on these sets. It decides nothing.

## 5. Limits written in advance

- **The rules.** It covers only the tutor's six wrong methods and its 1-point window, with answers typed as whole percents.
- **What a fix does.** It changes the problem, and usually its correct answer; the size of that change is reported. A fix says nothing about whether the original problem was a bad teaching choice, and nothing about the wording around the numbers.
- **No students are involved.** A fix is a property of the numbers. It is not evidence that students would then be diagnosed correctly.
- **The search space.** It searches whole-point steps from the given value of one number. Finer changes and two-number changes are not searched.
- **One reply per chatbot.** The counts describe three replies asked once. They say nothing about how a next reply would vary.

## 6. Seen before writing this plan (disclosed)

- **Report v23 and its output; report v24 and its output.** Earlier sessions, run by AI assistants working for the team, read the number sets of `extract_final.csv` while building and checking v23 and v24.
- **No fix has been computed on any v23 set, as far as our records show.** The team's Collision Checker page computes v22-style fixes. We have no record of it being used on these sets, but we cannot rule that out.
- **Tests.** `test_v41.py` uses made-up sets only. In its made-up mode, `v41.py` refuses the real file.

## 7. Files and procedure

| File | SHA-256 |
|---|---|
| `v41.py` | `26738d145e856b1e37ac31015e474f9d52ff33b16cfd1630a8e21fa87a8081ae` |
| `test_v41.py` (11 tests, made-up sets) | `817fd2ed1d142af1ceaf85ab3b9d4b97cf93e618c2f4fa1a3952a019e89f1eb9` |
| `extract_final.csv` (locked in addendum v23.1) | `bbeea3ea18d34e7020c42ead5d343527c235873958204461deb180d79a08787a` |
| `v23.py` (plan v23) | `f31694bb53e4dc56c558e44ffe409641e5efe7d3aaa9d174ff767d171946aec5` |
| `v22.py` (plan v22) | `4a9a8740f40623c96df080bed40561df02c2944257f36d4ee5a9042b1f14a3b5` |
| `v20.py` (plan v20) | `c71003c8602d912409bc5ea07941d8e93796716c6f607470b8c5436c84232db3` |
| `src/bayes_strategies.py` (frozen tutor) | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `src/topic_engine.py` (frozen tutor) | `3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a` |

1. `v41.py` checks every hash above, except its own and the tests', before it reads anything. It refuses to run if its output file already exists.
2. It also stops if any of D, Q1, Q3 or the legacy count differs from report v23, or if v22's and v23's legacy checks disagree on any set.
3. It is run once, after this tag is public, with the flag `--run-after-tag`. It saves its output in one step, then prints it.
4. Report v41 publishes the output unchanged and gives every number in it, whatever it shows.
5. If the run stops with a line starting "STOP", the cause is reported. Any fix to our own code is a dated, published addendum with new hashes, before the next start.
