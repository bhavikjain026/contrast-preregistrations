# Report v23: chatbot-written Bayes problems (result of the single run)

Plan v23 (tag v23), pipeline (tag v23-pipeline), addendum v23.1 (tag v23.1). `v23.py` (SHA-256 `f31694bb…46aec5`) was run once, at 00:25 IST on 20 November 2026, on `extract_final.csv` (`bbeea3ea…08787a`). The full output is `v23_result.txt` (`eb3e687b…484ef6`). Nothing was re-run, and this report changes no number in that output.

**Scope.** Each request was asked once, on 19 November 2026, in the app and tier shown, with the model the app displayed. Bhavik selected that model himself; whether it was the app's default was not checked (addendum v23.1, section 2.1). All problems were AI-generated. Each count describes **one reply** per chatbot and arm. Counts are not pooled or ranked.

**Intervals.** The bracketed intervals are exact Clopper–Pearson 95% intervals, printed by `v23.py` as the plan requires. They are nominal only: the 20 problems in one reply are not independent draws, and one reply says nothing about how the next reply would vary.

**Distinct sets.** In every cell, the number of distinct (b, h, f) sets D equals the number of usable problems (`v23_result.txt`): 20, 20 and 19 in Arm 1, and 20, 20 and 20 in Arm 2.

## Arm 1: the plain request

| Chatbot (app, tier, model shown) | Labels filled | Usable = D | Q1: some whole-percent answer fits two wrong methods | Q1x: same, ignoring base rate / joint occurrence | Q2: keys more than 1 point off | Largest key error | Q3: some answer fits the correct answer and a wrong method |
|---|---|---|---|---|---|---|---|
| ChatGPT (Mac app, Plus; no model name shown, "Medium") | 20 of 20 | 20 | 18 of 20 (68.3–98.8) | 18 of 20 | 0 of 20 | 0.005 pt | 1 of 20 |
| Gemini (Mac app, "Gemini Pro"; "Hydrogen", "Medium") | 20 of 20 | 20 | 20 of 20 (83.2–100) | 20 of 20 | 0 of 20 | 0.000 pt (to 4 decimals) | 3 of 20 |
| Claude (claude.ai, Max; "Sonnet 5.5", "Medium", "Auto") | 20 of 20 | 19 (1 excluded: a stated rate of 100%) | 16 of 19 (60.4–96.6) | 15 of 19 | 0 of 19 | 0.044 pt | 2 of 19 |

**Which pairs collide.** A number set can count in several rows, so pair counts overlap and must not be added.

| Pair | ChatGPT | Gemini | Claude |
|---|---|---|---|
| equal priors with 100% − false alarm | 18 | 20 | 15 |
| base rate with joint occurrence | 15 | 19 | 14 |
| equal priors with hit rate | 8 | 8 | 9 |
| 100% − false alarm with hit rate | 8 | 8 | 9 |

- **One pair is in every Q1x set.** In each reply, the count for equal priors with 100% − false alarm equals Q1x (18, 20 and 15), so that pair is present in every number set Q1x counts.
- **Why that pair collides.** The algebra is exact. The gap between the two methods is 100 · f(1 − h − f)/(h + f) points, where h and f are proportions. A small false-alarm rate makes it small, and h + f = 1 makes it zero. When the gap is at most 1 point, some whole percent always fits both. For example, the gap is about 1.1 points at h = 80%, f = 10%, and about 0.3 points at h = 90%, f = 5%.
- **Exact ties.** h + f = 100 in 6, 4 and 6 sets. In those sets, the hit rate, 100% − false alarm and equal priors give exactly the same number.

**The plan's fixed sentence (section 8), with "a student could type" meaning that such an answer exists, not that a student typed it:**

> "Asked once on 19 November 2026, ChatGPT (Mac app, Plus, no model name shown, 'Medium') filled 20 of the 20 requested labels; 20 problems were usable. In 18 of 20 distinct number sets, a student could type one answer that fits two of our tutor's six wrong methods, so the tutor would have to ask again; ignoring the base rate / joint occurrence pair, 18 of 20. Of 20 problems, 20 had a scoreable answer key, and 0 of those 20 were more than 1 point from the correct answer."

> "Asked once on 19 November 2026, Gemini (Mac app, 'Gemini Pro', 'Hydrogen', 'Medium') filled 20 of the 20 requested labels; 20 problems were usable. In 20 of 20 distinct number sets, a student could type one answer that fits two of our tutor's six wrong methods, so the tutor would have to ask again; ignoring the base rate / joint occurrence pair, 20 of 20. Of 20 problems, 20 had a scoreable answer key, and 0 of those 20 were more than 1 point from the correct answer."

> "Asked once on 19 November 2026, Claude (claude.ai, Max, 'Sonnet 5.5', 'Medium', 'Auto') filled 20 of the 20 requested labels; 19 problems were usable. In 16 of 19 distinct number sets, a student could type one answer that fits two of our tutor's six wrong methods, so the tutor would have to ask again; ignoring the base rate / joint occurrence pair, 15 of 19. Of 19 problems, 19 had a scoreable answer key, and 0 of those 19 were more than 1 point from the correct answer."

**Legacy v20 measure, for comparison with v20 only.** M1 counts a set where some wrong method's own typed answer fits the correct value. M2 counts a set where it fits another wrong method's value. M1 or M2 is 18 of 20, 20 of 20 and 15 of 19. Plan v20 reported this same measure as 21 of 23 on published textbook and paper problems. That was a different collection, gathered differently, so the two are not compared statistically.

## Arm 2: the request that names the six wrong answers and asks for 3-point gaps

| Chatbot | Usable = D | Q4: all 21 gaps at least 3 points | Q2: keys more than 1 point off | Largest key error |
|---|---|---|---|---|
| ChatGPT | 20 | 20 of 20 | 0 of 19 (1 unresolved key) | 0.049 pt |
| Gemini | 20 | 20 of 20 | 0 of 20 | 0.000 pt (to 4 decimals) |
| Claude | 20 | 20 of 20 | 0 of 20 | 0.048 pt |

**Fixed sentence:** "Asked to keep all seven answers at least 3 points apart, it did so in 20 of 20 distinct number sets." This holds for ChatGPT, Gemini and Claude alike.

**Why Q1 and Q3 are 0 in Arm 2.** These zeros are a consequence of Q4, not separate findings. If one whole percent fits two values, the values are at most 2 + 2 × 10⁻⁷ points apart. A minimum gap of 3 therefore rules out both.

## What this does and does not show

**Shows**, for these three chatbots, asked once each on 19 November 2026:
- **Plain request:** most number sets allowed at least one whole-percent answer that fits two of the tutor's six wrong methods. That was 18 of 20 for ChatGPT, 20 of 20 for Gemini and 16 of 19 for Claude.
- **Answer keys:** every scored key was within 0.05 points of the exact answer. One ChatGPT key in Arm 2 was unresolved and is not scored.
- **The request naming the six methods:** each reply met every requested gap, 20 of 20 for each.

**Does not show:**
- that any student typed a colliding answer, or used any of these methods;
- variation between replies, prompts, settings, models or dates;
- that chatbots in general, or one chatbot more than another, write such problems;
- that the colliding sets are a chatbot habit rather than a property of typical rates. The algebra above shows that a low false-alarm rate by itself pushes equal priors and 100% − false alarm together. How often random typical rates collide was not measured.
- whether the Arm 2 problems are realistic or teach well. Arm 2 states the scoring rule in the request, so it shows compliance with a stated rule, not unprompted good design.

**Depends on our choice of methods.** Every Q1x set includes the pair equal priors / 100% − false alarm, so the size of Q1x depends on counting 100% − false alarm as a wrong method. How many sets would still collide without it was not computed, and doing so needs a new plan. How common that method is among students is not measured here.
