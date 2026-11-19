# Plan v20: can published Bayes problems tell common mistakes apart?

Written 19 November 2026, before any published problem's numbers are checked against the rules. To be published
byte-identical under tag v20 before items are extracted. **No learners and no human data: this checks only the
numbers printed in published problems.**

## 1. Question

Our tutor works because one answer can fit two mistakes, and a second question can split them. That matters only if
the problems people actually use have such collisions. **In Bayes problems published in research and teaching
material, how often does an answer from a common wrong method (a) look right, or (b) fit two different wrong
methods?**

This is not a claim that any study was flawed. Gigerenzer and Hoffrage (1995), whose strategy names we use, saw that
one judgement can come from several algorithms, and used written protocols to tell them apart. We measure what the
answer alone can show.

## 2. Methods compared

The correct answer is b·h / (b·h + (1 − b)·f). The six wrong methods are those of the frozen tutor:
- hit rate, h;
- base rate only, b;
- false-alarm complement, 1 − f;
- likelihood subtraction, h − f;
- joint occurrence, b·h;
- equal priors, h / (h + f).

The values come from the frozen `bayes_strategies.predictions`, checked by SHA-256.

A student using a method is taken to type its answer rounded to a whole percent, exact halves rounded up (72.5 is
typed as 73; computed as floor(value + 0.5) with a tiny tolerance for stored decimals). That typed answer **fits** a
method if it is within 1 percentage point of that method's value (the tutor's tolerance).

## 3. Sources, fixed now

Every problem in these sources that states, or fixes through natural frequencies, a base rate, a hit rate and a
false-alarm rate for two hypotheses and asks for the probability of the hypothesis given a positive result:

1. Gigerenzer & Hoffrage (1995), *Psychological Review* 102, 684–704.
2. Sedlmeier & Gigerenzer (2001), *Journal of Experimental Psychology: General* 130, 380–400.
3. Domurat, Kowalczuk, Idzikowska, Borzymowska & Nowak-Przygodzka (2015), *Frontiers in Psychology* 6:1194.
4. Weber, Binder & Krauss (2018), *Frontiers in Psychology* 9:1833.
5. Bruckmaier, Binder, Krauss & Kufner (2019), *Frontiers in Psychology* 10:632.
6. Eichler, Böcherer-Linder & Vogel (2020), *Frontiers in Psychology* 11:1897.
7. OpenStax, *Introductory Statistics 2e* and *Statistics*: every worked example and exercise applying Bayes' theorem
   with all three rates.
8. **Order flow, kept separate (kind "orderflow").** These are problems updating the probability of a high value
   after a buy order, with informed and noise traders:
   - the numerical examples in Glosten & Milgrom (1985), *Journal of Financial Economics* 14, 71–100;
   - the free preview of tradermath's lesson "Adverse selection and the spread".

**Rules for what counts:**
- **Inaccessible sources.** A source that cannot be opened is recorded as "not accessible", with zero items. This is
  decided before any of its numbers are read.
- **Exclusions.** A problem is excluded, with the reason recorded, if it:
  - lacks one of the three rates;
  - has more than two hypotheses;
  - asks for a different quantity.
- **Natural frequencies.** These are converted exactly; for example, 10 of 1,000 becomes 0.01.
- **Repeats.** The same three numbers in several places count once in the primary measure, and once per source in
  the per-source table.
- **Lin et al. (2026) is excluded,** under the team's data-handling rules.

## 4. Fixed by arithmetic before any item is checked

- **Equal priors.** Any item with b = 0.5 has Bayes equal to h / (h + f) exactly, so equal priors is marked right (M1)
  by arithmetic.
- **Symmetric order flow.** Any order-flow item with h + f = 1 (symmetric informed and noise flow) has
  hit rate = false-alarm complement = equal priors exactly. So it collides under M2 by arithmetic. If its prior is
  also 0.5, the hit rate equals the correct answer, so M1 holds too.

The report counts these cases and labels them "by arithmetic": standard and order-flow items with b = 0.5 (and how
many show M1), and order-flow items with h + f = 1 (and how many show M2 and M1). Order-flow items with h + f ≠ 1 are
reported on their own. Order-flow items are reported separately and are not part of the primary measure.

## 5. What is reported

Per item, at the 1-point tolerance:
- **M1:** a wrong method's typed answer fits the correct answer, so it would be marked right.
- **M2:** one wrong method's typed answer fits another wrong method, so one answer has two possible causes.
- **Alone:** how many of the seven methods give an answer that fits no other method.

**Primary.** Among unique standard number sets: the share with any collision (M1 or M2), with an exact 95% interval.

**Described, no pass or fail:**
- M1 and M2 separately;
- which methods pass as right, and which pairs collide;
- per source;
- the same at a 0.5-point tolerance (the same whole percent), as a sensitivity check;
- the order-flow items;
- every item's numbers and outcome.

**Reading.** No threshold. The only slide sentence allowed has this form: "Of N published Bayes problems from [these
sources], X let a common wrong method look right to within a point, and Y let one answer fit two different wrong
methods. Order-flow problems: Z of W, most by arithmetic."

## 6. Limits written in advance

- **Six wrong methods only.** People use others.
- **Typing assumption.** Learners are assumed to type whole percents, and the 1-point tolerance is our choice. The
  0.5-point sensitivity is reported.
- **Not a judgement on the studies.** A collision says what one answer alone cannot show. It says nothing about the
  studies, which may have used written working, as Gigerenzer and Hoffrage did.
- **Small sample.** The sources are our selection, fixed before checking. The number of items will be small, and
  the interval says so.

## 7. Seen before writing this plan (disclosed)

- **Earlier plans:** all plans v10–v18, addendum v17.1, and their results.
- **Read for prior art:** a research agent read Gigerenzer & Hoffrage (1995) in full, and another saw the
  tradermath preview's symmetric 50/50 example. No collision was computed on any of their items. The classic
  mammography numbers (1%, 80%, 9.6%) were already known to us.
- **The checker** has been run only on made-up items, to test that it works: seven made-up rows by the author, and four by the
  independent checker (60/75/30 twice, 50/72.5/30 and an order-flow 30/75/25), which found the two faults fixed in this
  version (section 4 counts missing; repeats counted twice per source). No published numbers were used.

## 8. Files and procedure

| File | SHA-256 |
|---|---|
| `v20.py` | `c71003c8602d912409bc5ea07941d8e93796716c6f607470b8c5436c84232db3` |
| `test_v20.py` | `b6f33b9f5b21e5b0e5a6a83204110b88f225c96e5d25463dce8f81722d528297` |
| `items_v20_template.csv` | `e1c6a34afac6a543b3b20f0fcdc22b097aab1e414f4e5f03646219a32b19da10` |
| `src/bayes_strategies.py` | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `src/topic_engine.py` | `3072e0419b3dafc1a31a86d784e3b770d89018d940493c97708cb9b9bc1b492a` |

1. **Publish.** Publish this plan byte-identical under tag v20 (plan text only).
2. **Extract.** One extractor fills `items_v20.csv` from the sources in section 3. Each row carries the source, the
   location (page or section), the three numbers, the kind, and a short verbatim quote of the numbers. Excluded
   problems and inaccessible sources go in a separate log with reasons. The extractor computes no method values.
   Bhavik checks every row against its source.
3. **Lock.** Publish addendum v20.1 with the SHA-256 of `items_v20.csv` and of the exclusion log, before step 4.
4. **Run once.** Run `python3 v20.py <repo root> items_v20.csv`. Report every number in section 5. Any change after
   publication is a dated, published addendum.
