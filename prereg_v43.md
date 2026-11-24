# Plan v43 (25 November 2026): does every answer get a certificate that an independent checker accepts?

Status: final text for release as tag v43 (draft 8, after seven rounds of outside review; the first five each said STOP, the
sixth and seventh said FIX; section 8 says what changed), published before the registered run and before the engine is frozen. **No learners and no human data: this is arithmetic on problems generated from the lists in section 4, plus
one problem written by someone outside the team.** The acceptance rules are fixed here, as prose in section 3 and as
the checker file whose SHA-256 is in section 9. The engine, its tests and the run script are frozen later, by
addendum v43.1, which publishes the hash of a manifest of every file before the single run.

## 1. Question

The team has built a separate tool, World or Trade, beside the frozen tutor. A problem is a list of stated facts
about chances ("the alarm catches 80% of real cases"), and a question ("how likely is a case to be real, given that
both alarms fire?"). For any exact answer (a fraction between 0 and 1) to a supported problem (section 3), the tool
returns one of four things:

- **a world**: a table of whole counts in which every stated fact holds and the answer is exactly right;
- **a trade**: bets at the stated rates, plus one bet against the answer, that never lose and win whenever the
  question's condition happens;
- **"the facts contradict each other"**, with bets on the facts alone that win in every case;
- **"the condition can never happen under these facts"**, with a table showing the facts can hold and bets
  showing the condition then has no chance.

It also returns the range of answers the facts allow, and, for a stated price and one extra fact (the reply to a
question a person chose to ask), whether that reply settles a buy-or-pass decision.

Every one of these comes with a certificate that can be checked with plain sums. **On the cases written down in
section 4, does every certificate pass the independent checker, and do the results stated in section 2 hold?**

This plan does not change plan v39. Plan v39 says the team enters the frozen tutor alone; its checking layer stays
withdrawn. World or Trade does not read, wrap or relabel the tutor's verdicts, and it names no method. Whether it is
shown at the final at all, and how, will be stated in a dated public note before the final.

## 2. What the arithmetic fixes in advance (derived; proofs sketched here, checked in section 4)

All inputs are exact rational numbers, so every linear programme below has rational solutions and every certificate
is a table of fractions. Write a world as a probability table x over the states (every combination of the yes/no
events). A rate fact
"P(E | C) = r" holds when P(E and C) = r·P(C); "at least r" and "at most r" use ≥ and ≤. A fact whose condition has
chance 0 holds automatically. The question is P(T | K), and only worlds with P(K) > 0 count.

**Result 1 (one of the two, never both).** For a problem whose facts can hold together and whose condition K can
happen, and any answer q: either some world makes q exactly right, or a trade against q exists, and never both. This
is de Finetti's theorem (1937) in the form of a linear programme (Hailperin 1965); the R package Pinference (Porta
Mana 2025) computes the same bounds. *Why never both:* in a world where the facts hold, the facts' bets (with the
allowed signs of section 3) have expected payoff at most 0 and the bet against q has expected payoff 0, but a trade
pays at least L > 0 whenever K happens, so its expected payoff is at least L·P(K) > 0. *Why one of the two:* the set
of worlds is a polytope. Worlds where K has chance 0 add nothing to P(T and K) or P(K), so the answers the facts
allow run between the smallest and largest ratio over the polytope's corners with P(K) > 0; a rational q in that range,
an end included, has a rational world. If q is outside it, the gap is positive and linear-programming duality (Farkas's
lemma) gives bets that pay at least a positive amount whenever K happens: the trade. A tie at an end is a world, not a
trade.
- For one-alarm Bayes problems (base rate b, hit rate h, false-alarm rate f, 0 < f < h < 1, 0 < b < 1) the facts
  force one answer, P* = bh / (bh + (1 − b)f). So the tool returns a world exactly when q = P*, and otherwise a trade
  that locks exactly |q − P*| whenever the alarm fires.

**Result 2 (ignorance adds up in log-odds).** Suppose every fact is either the base rate b of "real" or a rate
conditional on "real" or on "not real", and K involves only the alarms. Then the worlds split into a part for real
cases and a part for sound cases, chosen independently. Write T and F for the chances of K among real and among
sound cases; T ranges over an interval [Tmin, Tmax] and F over [Fmin, Fmax], independently. The odds of "real"
given K are b/(1 − b) × T/F. So the answer's range in log-odds is the prior log-odds plus
[log(Tmin/Fmax), log(Tmax/Fmin)]. Its width is log(Tmax/Tmin) + log(Fmax/Fmin): one share from the real cases and
one from the sound cases. Learning T exactly removes exactly the first share, and learning F removes exactly the
second. These statements assume 0 < b < 1. The statements about widths apply when Tmin, Tmax, Fmin and Fmax are all
positive; when Tmin = 0 or Fmin = 0 (and both maxima are positive) the range reaches 0 or 1, and only the end
statements hold. If Fmax = 0 the answer is 1 wherever K can happen; if Tmax = 0 it is 0; if both are 0, K cannot
happen.
- For k alarms that all fire, with each alarm's catch rate h_i and false-alarm rate f_i stated and nothing about how
  they overlap, T and F range over the Fréchet bounds: [max(0, Σh_i − (k − 1)), min h_i] and
  [max(0, Σf_i − (k − 1)), min f_i]. Both ends are reached: nesting the alarm events gives the upper bound, and
  arranging their complements to be disjoint, or to cover every case, gives the lower one. At a corner with T > 0 and
  F = 0 the answer is 1, and with T = 0 and F > 0 it is 0; T = F = 0 means the condition has no chance there, and if
  it is forced to have none, the tool reports "cannot happen".
- Consequence for teaching: the fact that removes the larger share of the log-odds width is the one about the class
  whose overlap is less pinned down. In our two-alarm example (base 10%, each alarm 80% and 20%), the real-case
  overlap lies in [60%, 80%] (ratio 4/3) and the sound-case overlap in [0%, 20%] (unbounded ratio), so the second
  removes the larger share. Whether it settles a given decision also depends on the price, and on which replies one
  counts; section 4 reports both, as counts of evenly spaced replies.

**Result 3 (sign or spread: a second alarm either moves you in a known direction, or leaves you less sure).**
Stated: the base rate b of "real", with 0 < b < 1, and P(A | real) = a and P(A | sound) = c for a first alarm A, with a, c > 0; so
after A alone the facts force p1 = ba / (ba + (1 − b)c). A second alarm B has its own rates stated, and nothing links
it to A. Let T = P(A and B | real) and F = P(A and B | sound). As in result 2, T ranges over [Tl, Tu] and F over
[Fl, Fu], independently; for two alarms these are the Fréchet bounds Tl = max(0, a + h2 − 1), Tu = min(a, h2),
Fl = max(0, c + f2 − 1), Fu = min(c, f2). Then, except in the degenerate case where c·T = a·F in every world (B tells
nothing), exactly one of the following holds:
- **Sure up**, if c·Tl ≥ a·Fu: in every world that fits the facts, B firing gives an answer of at least p1 and B
  staying quiet gives at most p1.
- **Sure down**, if a·Fl ≥ c·Tu: the reverse.
- **Spread (dilation)** otherwise, that is when c·Tl < a·Fu and a·Fl < c·Tu: whatever B shows, the range of answers
  strictly contains p1 (Seidenfeld and Wasserman 1993).
*Proof sketch.* In a world (T, F), B firing gives the answer bT / (bT + (1 − b)F) and B quiet gives
b(a − T) / (b(a − T) + (1 − b)(c − F)). Cross-multiplying, the first is at least p1 exactly when c·T ≥ a·F, and that is
also exactly when the second is at most p1. Since T and F vary independently, c·T ≥ a·F holds in every world exactly
when c·Tl ≥ a·Fu. In the spread case the worlds (Tl, Fu) and (Tu, Fl) put each answer on both sides of p1, and the strict
inequalities give both results of B a positive chance in those worlds. Only worlds in which a result of B has a
positive chance count for that result; at a corner where it has none, that corner does not count. For example, with
b = 1/2, h1 = 4/5, h2 = 1 and f1 = f2 = 1/5, B always fires on real cases, so the answer after a quiet result is 0
whenever a quiet result can happen; here c·Tl = a·Fu, B is a sure confirmation, and nothing spreads.
In words: compare the share of A's real hits that B also catches, which lies between Tl/a and Tu/a, with the share
of A's false alarms that B repeats, which lies between Fl/c and Fu/c. If the smallest possible first share is at least
the largest possible second share, B can only confirm; if the largest first share is at most the smallest second share,
B can only disconfirm; otherwise each range's lower end is strictly below the other range's upper end, and whatever B
shows, you end up less sure. (The condition 0 < b < 1 matters: with b = 0 every answer is 0 whatever the shares say.)
- **For two alarms with c + f2 ≤ 1** (so Fl = 0 and Fu = min(c, f2)), and 0 < b < 1, 0 < a ≤ 1, 0 < c, 0 < h2 ≤ 1,
  0 < f2, B is never a sure disconfirmation, and it is a sure confirmation exactly when
  min(c, f2) ≤ c × max(0, 1 − (1 − h2)/a); otherwise it spreads. When h2 < 1 the right side is below c, so the test
  reads f2 ≤ c × max(0, 1 − (1 − h2)/a). When h2 = 1 the right side is c and B is always a sure confirmation: for
  example b = 1/2, a = 4/5, c = 1/5, h2 = 1, f2 = 3/10 (draft 2 wrote f2 in place of min(c, f2) and so wrongly called
  this case spread; the second outside review found it). In particular, if
  0 < c ≤ f2, c + f2 ≤ 1, 0 < a ≤ 1 and 0 < h2 < 1, B spreads whatever b, a and h2 are (a = 1 included).
- **Example.** Base 10%, A catches 80% and false-alarms on 20%; after A alone the answer is 4/13, about 30.8%. If B also
  catches 80%, the cut-off is 0.75 × 20% = 15%. With B false-alarming on 20%, B spreads: 25% to 100% if it fires, 0% to
  100% if it is quiet. With B false-alarming on 14%, B is a sure confirmation: 10/31 (32.3%) to 100% if it fires,
  0% to 10/37 (27.0%) if it is quiet.

**Result 4 (one interval of open replies).** Fix a price c and a candidate fact "P(E | C) = r", and suppose the
stated facts force P(C) to be at least some d > 0 (the step's condition bound, section 3; without it, worlds with
P(C) = 0 satisfy every reply and the step is not supported). Call a reply r *attainable* if, with the fact added, the
facts can hold and K has a chance, and *open* if, in addition, some world makes c exactly fair. The attainable replies
form one interval, possibly without its ends, and so do the open replies: they are images of convex sets of worlds
under the map x ↦ P(E | C), which is linear-fractional with a positive denominator. Every attainable reply that is
not open settles the decision: buy if all its worlds have P(T | K) > c, pass if all have P(T | K) < c.

**Result 5 (the extremes are enough, when they are attainable).** With L(r) and U(r) the ends of the range after an
attainable reply r: {r : L(r) ≤ t} is the same kind of image of {worlds: P(T | K) ≤ t}, so it is an interval for
every t, and L is quasi-convex on the attainable replies; likewise U is quasi-concave. So if both extreme replies are
attainable, the largest L(r) and the smallest U(r) are reached at one of them, and a fact can settle "buy" for some
reply exactly when it does so at one of its two extreme replies. If an extreme reply is not attainable, the statement
holds only for the limit, which need not be reached. For example, with the single fact P(A | K) = 1/2, the question
P(A | K) and a price of 1/4, every reply r = P(A) strictly between 0 and 1 settles buy, while r = 0 and r = 1 cannot
occur.

None of results 1, 4 and 5 is new mathematics. Results 2 and 3 follow from standard facts (Fréchet bounds, the
independence of the two classes' unknowns, and Seidenfeld and Wasserman's link between dilation and independence); we
found them stated in this form nowhere, but the search was short and we do not claim to be first.

## 3. Definitions (fixed now)

- **Supported problems.** Up to 6 yes/no events (the checker reads up to 10; the run's own families use up to 5),
  written in the format `wot_check.py` describes, which the checker validates field by field.
  Facts of two kinds: a rate fact "P(E | C) is exactly / at least / at most r", and "E and E2 are equally likely given
  C". E, C, T and K are built from the events with not, and, or. Every number is exact: a whole number, or a string
  such as "1/10" or "0.25". A JSON floating-point number is refused.
- **A world** is a table of whole counts, at least 0, with a positive total. It is valid for answer q when every fact
  holds in it, K has a positive count, and count(T and K) = q × count(K).
- **Bets.** A rate fact is the bet that pays (1 if E, else 0) − r when C is true and nothing otherwise; a "same" fact
  pays (1 if E) − (1 if E2) when C is true. A stake is how many of the bet one holds. Allowed stakes: any sign for
  "exactly" and "same"; at least 0 for "at most"; at most 0 for "at least". Quoting q is the bet that pays
  (1 if T) − q when K is true; "buy" holds +1 of it, "sell" holds −1.
- **A trade** is valid for answer q when it comes with a witness (a table in which every fact holds and K has a
  positive count, so a trade is never given when the facts contradict or K cannot happen), its stakes have allowed
  signs, it locks L > 0, and in every state its total payoff is at least 0, and at least L where K is true. **A tie is
  not a profit**: L = 0 is not a trade.
- **"The facts contradict each other"** is valid when allowed stakes on the facts alone pay at least L > 0 in every
  state. **"The condition can never happen"** is valid when a table satisfies every fact, and allowed stakes on the
  facts pay at least 1 in every state where K is true and at least 0 elsewhere.
- **The range** [low, high] is valid when a world gives low, a world gives high, and allowed stakes make
  (1 if T and K) − low × (1 if K) plus the facts' payoff at least 0 in every state, and likewise for high × (1 if K) −
  (1 if T and K).
- **A step** adds one rate fact "P(E | C) = r" (the reply) and a price c. Every step, whatever its verdict, needs a
  condition bound: allowed stakes on the original facts showing that every world of the original facts gives C a
  chance of at least some d > 0. Its verdict is *buy* (a valid trade, with witness, buying the contract at exactly c, on the extended problem), *pass* (a
  valid trade selling the contract at exactly c, that is, a certified profit from selling it), *open* (a valid world
  of the extended problem with answer exactly c; a tie at an end of the range is open), or *cannot occur* (a valid
  "contradict" or "cannot happen" certificate for the extended problem, besides the condition bound). If the
  original facts are consistent but allow C a chance of 0, the step is not supported and gets no verdict: the checker
  refuses every verdict for it. If the original facts contradict each other, there is no world at all, so the
  condition bound holds for any d (the contradiction's stakes, divided by what they lock, prove it), no reply can
  occur, and every step's verdict is *cannot occur*.
- The order of checks for an answer is: facts contradict; condition cannot happen; then world or trade.
- **The checker** is `wot_check.py` (hash in section 9). It implements exactly the rules above, uses no solver and
  no floating point, and does not import the engine. Before publication, Claude Code compares it with this text; any
  disagreement found later is reported in report v43 as a failure of this plan.

## 4. The cases and what is reported

Every family is generated by the run script from these lists; nothing is sampled except F6, from the fixed seed.
Percentages are exact.

- **F1. One-alarm problems (result 1).** Base, hit and false-alarm rates each in {5%, 15%, …, 95%} (odd multiples of
  5), with hit rate above false-alarm rate: 10 × 45 = 450 problems. Answers 0%, 5%, …, 100%: 9,450 cases. For each
  problem, the range certificate.
  - Prediction 1: a world exactly when the answer equals P*. Prediction 2: every trade locks exactly |q − P*|.
    Prediction 3: every range is the single point P*.
- **F2. Two to four alarms that all fire (result 2).** k = 2: base in {2, 15, 35, 55, 75}%, each catch rate in
  {55, 70, 85, 99}%, each false-alarm rate in {1, 12, 30, 48}%: 1,280 problems. k = 3: base in {15, 55}%, catch rates
  in {60, 90}%, false-alarm rates in {5, 40}%: 128. k = 4: base 30%, catch rates in {70, 95}%, false-alarm rates in
  {10, 30}%: 256.
  - Prediction 4: every range certificate equals the closed form of result 2.
  - Prediction 5 (k = 2 only): adding the real-case overlap at its smallest, middle and largest value (leaving out
    0), the range is [bT/(bT + (1 − b)Fmax), bT/(bT + (1 − b)Fmin)]; adding the sound-case overlap likewise gives
    [bTmin/(bTmin + (1 − b)F), bTmax/(bTmax + (1 − b)F)].
- **F3. Dilation (result 3).** Base in {3, 25, 50, 75}%, h1 and h2 in {52, 68, 84, 99}%, f1 and f2 in
  {2, 17, 33, 49}%: 1,024 problems; for each, range certificates for "alarm 2 fires" and "alarm 2 is quiet".
  - Prediction 6: the comparison of result 3 classifies every problem as the certificates do: dilation exactly when
    it says spread; when it says sure up, the range after a firing starts at p1 or above and the range after a quiet
    result ends at p1 or below; when it says sure down, the reverse.
  - Prediction 7: every problem with f1 ≤ f2 shows dilation for both results of alarm 2 (on this grid f1 + f2 ≤ 1
    always holds).
  - Reported: the number with dilation.
- **F4. The fact step (results 4 and 5).** Two alarms, each catching 80% of real cases and firing on 20% of sound
  ones, both firing; base in {5, 10, 30, 50}%; prices 30, 45, 55, 70, 85 and 95 cents for a contract paying 100 cents
  if the case is real. Three candidate facts: how often both fire on real cases; on sound cases; and on all cases,
  with no labels. Each fact at 401 evenly spaced values across its certified range under the stated facts, ends
  included. Every step gets a verdict and a certificate, and every reply that does not "cannot occur" also gets a
  certified range.
  - Reported, for each base, price and fact: how many of the 401 values settle (buy, pass), how many are open and
    how many cannot occur.
    **These are counts of evenly spaced values, not chances.**
  - Prediction 8: the open values form one unbroken run, for every base, price and fact; any other verdict inside the
    run, "cannot occur" or an invalid certificate included, breaks it. Prediction 9: when both extreme values are
    attainable, the largest lower end and the smallest upper end are reached at an extreme value. Each extreme value
    must have a checked certificate: a checked "cannot occur" step, or a checked step with a checked range. If either
    has neither, that is a violation, whatever the other shows. A case is reported as not applicable only when both
    are checked and at least one cannot occur. If a base and fact has no certified range of replies or no condition
    bound, its steps are all recorded as missing, and each of its prices counts as a violation of predictions 8 and 9.
- **F5. Fixed examples: a regression family.** Every F5 example was run before this plan was published (section 8),
  so F5 checks that nothing changed, not anything new. The 0/0 trap (base 10%; each alarm catches 40% of real cases
  but never both; each fires on 20% of sound cases; answer 75%): a trade locking 75 cents. The same with "never both on sound cases" added: "cannot happen".
  P(A) = 60%, P(B) = 60%, P(A and B) = 10%: "contradict". 25 / 60 / 20 with answer 75%: a trade locking 25 cents.
  The two-alarm example with answer 20%: a trade locking 5 cents; with answer 64%: a world.
  A learner's three prices for one case, 31% now, 60% if a second alarm fires and 35% if it stays quiet ("more
  confident either way"): "contradict".
- **F6. Random problems.** 1,000 problems on the events real, A and B, drawn with Python's `random.Random(20261125)`
  in this order for each problem: the number of facts (1 to 5, equally likely); for each fact an event and a
  condition from the list real, not real, A, B, A and B, A or B, A and not B, not A, real and A, B or not real (the
  condition also from "always"), a rate from 0, 1/20, …, 1 and a relation chosen from (exactly, exactly, at least, at
  most), so exactly with chance 1/2; then the question's event and condition from the same lists; then the answer
  from 0, 1/20, …, 1. Reported: how many of each kind.
- **F7. One problem from outside the team** (section 5): its range (if any), its answers and its steps.
- **For every family:** the number of requests and how many got a certificate that the checker accepts. The run
  writes each request in a ledger before it asks the engine, and records for each one: certified, missing, invalid,
  or not for its request. The ledger keeps its own copies of each problem and request; the engine works on separate
  copies, and each certificate is bound to, and checked against, the ledger's copies. No call to the engine is made on
  a live object outside the ledger; the condition bound of F4 is computed on a copy. A certificate counts only if it
  answers the request that asked for it (the same answer, the same range question, or the same price and extra fact).

## 5. The problem from outside the team

One person outside the team (not Bhavik, Kahan or Jay, and not an AI) writes one supported problem, in words and in
the file format that `wot_check.py` describes, with any answers and any (price, extra fact) steps they choose. The
order is fixed:
1. They write the file and send only its SHA-256 to Bhavik, by email.
2. Addendum v43.1 publishes the hash of the manifest, which lists the hashes of the engine, its tests, the run script
   and this outside file.
3. Only then do they send the file. Its hash must match, or the run stops.
4. The run is made once. Afterwards they receive the certificates for their problem and check them by hand or with
   `wot_check.py`. Report v43 says whether they could, and whether they agree.

The team does not see the file before step 3. The run refuses duplicate keys, floating-point numbers, more than 6
events, event names that are not plain letters, digits or _, unknown fields, labels that are not text, and step replies that are not "exactly r". If the file lies outside the supported class, the
run stops and reports that, and it counts as a failure of the engine's claim to handle what someone else writes. A step
whose condition the stated facts, if consistent, allow a chance of 0 gets no verdict (section 3), and also counts as
such a failure. If the stated facts contradict each other, every step gets "cannot occur" (section 3).

## 6. Pass or fail, and what may be said

- **The engine passes plan v43** only if: every request in the ledger (section 4) has a certificate that the checker
  accepts and that answers that request, so a single missing certificate fails the run; predictions 1 to 3 hold with no violation; every F5 example has the stated kind and, where one is
  stated, the stated amount; the F4 counts for base 10% at 55 cents and base 50% at 85 cents equal those seen before
  this plan (section 8); and the outside problem is in the supported class and runs with no change to the engine,
  with a valid certificate for every answer and step it asks for. The run prints this verdict itself, as a line
  "SECTION 6 VERDICT: PASS" or "FAIL" with the reasons.
- **Predictions 4 to 9 test the mathematics, not the engine.** A violated prediction can come from the case
  generator, the closed form's code, the engine or the checker, or from the result itself. Report v43 lists every
  violation; one is called a counterexample to the stated result only after the instance has been checked by hand and
  found to meet the result's hypotheses. A result with a violation is not stated again until that is settled.
- **If the engine fails,** World or Trade is not described as verified anywhere, and report v43 says which check
  failed.
- **The only sentence allowed if it passes:** "In N requests written down before the run, every one got a
  certificate (a count table or a set of bets) that a separate checker accepted. Arithmetic, not tested on people."
  N is the number of requests in the run's ledger for F1 to F7: answers, ranges and steps each count once.
  Results 2 and 3 may be stated as results only if predictions 4 to 7 hold.
- Never claimed from this plan: that anyone learned anything, that the method is ours, or anything about real
  markets or real tests.

## 7. Limits written in advance, and earlier work

- Arithmetic only. Nothing here says whether the tool helps a learner. That needs a separate study with people, a
  published plan and ethics approval.
- The families are ours. F7 is one problem from one person.
- In a step, "pass" means a certified profit from selling the stated contract at the price; "buy", from buying it; a
  tie at an end of the range, where some world makes the price exactly fair, is "open". Steps are supported only when
  the stated facts keep the reply's condition from having chance 0.
- Results 2 and 3 cover alarms whose rates are stated within "real" and "sound" separately. Facts that link the two
  classes, such as a pooled count, are covered by the engine but not by the closed forms.
- **Earlier work.** De Finetti (1937) and Hailperin (1965, 1996) on coherence and probability bounds; Walley (1991)
  on lower and upper previsions (not opened by us); the R package Pinference (Porta Mana, version 0.2.6, 2025), which
  computes the bounds of result 1 and lists teaching among its uses, and whose printed examples our engine's tests
  reproduce; Seidenfeld and Wasserman (1993, Annals of Statistics) and Wasserman and Seidenfeld (1994) on dilation;
  Pedersen and Wheeler (2014, Erkenntnis), who tie dilation to departures from independence; Gong and Meng
  (arXiv 1712.08946), on dilation, sure loss and Simpson's paradox; Obradović (2023, arXiv 2204.00180) on Fréchet
  bounds for two diagnostic tests; Obradović and Ziegler (2026, arXiv 2611.20209), who show that a diagnostic test
  checked against an imperfect reference can induce dilation; Wellman (1990) on qualitative, sign-only influences in
  probabilistic networks; and, on two diagnostic tests in sequence, Vacek (1985), Gardner and colleagues (2000) and
  Marshall (1989), the last cited by a 2024 review (Diagnostic and Prognostic Research) for showing that a second
  positive test need not raise the predictive value when the tests are correlated (Marshall not opened by us); Andrews and Sarkar (2026, arXiv 2609.02797), who
  compute sure-loss profits against language models' forecasts. We found no tutor that answers a learner with a world
  or a trade; the search was small and is weak evidence.

## 8. Seen before writing this plan (disclosed)

- **The author** is the AI assistant (Claude) working for the team. It built an exploratory engine and ran it on
  problems that are not in section 4: one-alarm problems with rates on 10-point steps (3,564 cases by the current
  engine, 32,076 by an earlier sketch); 48 random two- and three-alarm problems for result 2; 243 grid problems
  (base 10, 30 or 50%; catch rates 60, 80 or 90%; false-alarm rates 5, 20 or 40%) and 150 random ones for result 3,
  where 165 of the 243 showed dilation, an earlier form of result 3's condition agreed with the engine on all 243 and
  on the 150 random ones, and the sufficient condition held in all 162 grid problems with f1 ≤ f2 and in all 1,021 random problems that
  met it (60 of them rechecked by the engine); and 24 random problem-fact-price cases for results 4 and 5.
- **Result 3 in its present form** was checked on 1,500 random problems (seed 2511; all five rates from 1% to 99% in
  any order): it held in all 1,500 (1,140 spread, 168 sure up, 192 sure down).
- **The "more confident either way" example of F5** was seen, with a check on 1,499 random problems (seed 77) that no
  binary signal raised the lowest possible answer on both of its results (it never did).
- **Testing the tests.** Before draft 1, 21 bugs were planted one at a time in copies of the engine and the checker;
  the first round caught 17, and four checker tests were added. The review then found four more that survived. For
  draft 2 the list has 40 planted bugs across the engine, the checker and the run script (section 9). The first run of
  this list was not valid: one test file failed in every copy because a file was not copied, which made three bugs
  look caught. The script now first checks that the unchanged files pass every test in a fresh folder. The next run
  caught 38 of 40; two test fixtures were corrected so that each fails only on its own target, and all 40 were then
  caught. For draft 3 the list has 47 (section 9); a planted bug whose tests time out now counts as missed, not caught;
  and four planted bugs were rewritten to match the rewritten input checks. The first draft 3 run caught 43 of 47. The
  four tests that missed were made to reach their target (a "cannot occur" fixture now carries a valid condition bound;
  a float is placed in a field nothing else checks; the manifest test no longer fails first on another check; the
  poisoned-checker test now reaches the parsing of the manifest), and the next run caught all 47, none timed out. For
  draft 4 the list has 53, one new planted bug for each draft 4 fix. The first draft 4 run caught 52 of 53: once labels
  had to be text, every float in the outside file was refused by some other check too, so removing the loader's own
  float refusal went unnoticed. The test now requires the loader's "floating-point" message, and the next run caught
  all 53, none timed out. For draft 5 the list has 57: four new planted bugs, one for each draft 5 fix, and the
  prediction 9 bug rewritten to match the stricter check. Its first run caught all 57, none timed out. Draft 6
  changes only tests and two text labels; the same 57 were run again. That run also caught all 57, none timed out.
  For draft 7 the list has 58: one new planted bug, removing the copy of the condition bound given to each step.
  Its first run caught all 58, none timed out. For draft 8 the list has 59: one new planted bug, removing the
  loader's own check of event names. Its first run caught all 59, none timed out.
- **Seen F4 counts, used as regression in section 6.** Base 10%, price 55 cents: overlap on real cases settles 0 of
  401 values, on sound cases 365, with no labels 329. Base 50%, price 85 cents: 0, 330 and 165. An outside AI
  (ChatGPT) reproduced 0, 365, 329 and 165 by its own arithmetic on 24 November 2026.
- The F5 examples, the two-alarm example's range (25% to 100%) and its after-alarm-1 value (4/13) were all seen.
- The idea of answering with a world or a trade, and of asking which one fact settles a decision, was discussed with
  ChatGPT and Gemini, which gave ideas and criticism. They saw no file of this plan.
- **Outside review, one round, by ChatGPT on 24 and 25 November 2026.** It received draft 1 of this plan and of the
  checker, engine, tests and run script, and no learner data. It answered STOP: the checker accepted a trade when the
  condition could not happen, and could certify both "buy" and "pass" for a reply that contradicts the facts. It also
  found zero-chance corners in result 3's old wording, unattainable extreme replies in results 4 and 5, weak input
  validation, four planted bugs the tests missed, unbound certificates and unchecked numbers in the run script, the
  runner's own hash inside the runner, and F5 examples run by the `--made-up` mode. It ran only `--made-up`, which in
  draft 1 executed the F5 examples. Draft 2 takes in every point: the trade witness, the step's condition bound and
  "cannot occur" certificate, schema and input checks, a manifest in place of hashes inside the runner, certificates
  bound to their requests, certified numbers for every prediction, a printed section 6 verdict, F5 declared a
  regression family with its own made-up stand-ins, and new tests for each missed bug.
- **Outside review, second round, by ChatGPT on 25 November 2026**, of draft 2, in the same chat. It answered STOP,
  with three blockers: result 3's simplified cutoff was false when h2 = 1 (its counterexample is now in result 3; the
  corrected cutoff agrees with the general rule on all 76,000 grid cases with rates in steps of 1/20 and c + f2 ≤ 1,
  an algebra check of ours, while the draft 2 cutoff disagreed on 1,800, all with h2 = 1); the checker accepted a
  verdict for a step whose condition can have chance 0, which the engine called unsupported (the checker now needs
  the condition bound for every verdict, "cannot occur" included); and the run could print PASS with a certificate
  missing (it now keeps a ledger of requests, and a missing certificate fails it). Its smaller points were all taken
  in: a certificates file holding a single record was refused; timeouts in the planted-bug run counted as caught; the
  closed form of result 2 failed when a class can never set the condition off; "not applicable" in prediction 9 could
  hide a missing certificate; the checker was imported before the manifest was checked; the outside file's shapes
  were checked loosely; and the made-up families were kept apart by name rather than by content (they are now checked
  to share no request with the registered ones). It ran only the tests and `--made-up`.
- **Outside review, third round, by ChatGPT on 25 November 2026**, of draft 3, in the same chat. It answered STOP,
  with two new problems: the ledger shared its request objects with the engine, so an engine that changed its own
  inputs could rewrite what had been asked (its fault test turned an open step into "buy" and still printed PASS);
  and for original facts that contradict each other the checker accepted a "cannot occur" step while the engine gave
  none. Draft 4 keeps the ledger's own copies (section 4) and defines every such step as "cannot occur" (section 3).
  It also asked for 0 < b < 1 in result 3's own hypotheses and the spread condition in words; prediction 9's
  "not applicable" to need checked certificates at both ends; labels to be text; and the made-up separation to compare
  the actual requests. The run now compares every request of the made-up run, with labels, fact order and the
  spelling of events ignored, against every registered base problem, and counts a match when the request has the
  same events and question and all the base's facts (or exactly them, where the family adds none).
- **Outside review, fourth round, on 25 November 2026**, of draft 4: ChatGPT in the same chat answered STOP, and a
  second reviewer (Astra) answered FIX after a static reading of seven of the nine files. ChatGPT ran every test and
  the made-up run. It found two engine calls outside the ledger's copies: the F4 condition bound was computed on the
  live problem, and an unused F7 call parsed the live outside problem. In its fault tests an engine that changed those
  inputs changed what was later recorded, and the run still printed PASS. Draft 5 computes the bound on a copy, removes
  the F7 call, and adds a test that marks every problem any engine function receives and requires that no mark ever
  reaches the ledger. Both reviewers also found that a base and fact with no certified range of replies was not
  counted against prediction 9, and the second found that prediction 9 trusted an unchecked end when ranges were
  present; both are fixed and tested. Smaller points taken in: the proof of result 3 says "in the spread case"; a
  test now changes only the problem, not the reply; forged inner certificates are refused for contradictory facts;
  stale draft labels in two file headers.
- **Outside review, fifth round, on 25 November 2026**, of draft 5: ChatGPT (same chat) and Astra both answered STOP.
  Both confirmed the runner fixes (ChatGPT replayed both of its earlier faults, ran the 95 unit tests and the made-up
  run, and caught the new planted bugs itself). Their STOP came mainly from the plan file they were sent, which was the
  draft 4 plan by mistake; the draft 5 plan already held the changes they looked for (status line, result 3's proof,
  the F4 setup-failure rule, the round-four disclosure and the count of 57). They also found real gaps in the tests,
  fixed in draft 6: the marking test did not mark the Problem objects passed to two engine functions, nor a step's reply
  and condition bound, and compared only some ledger fields (it now marks every argument and, in its first run,
  compares the complete ledger); the setup-failure test now requires exactly one violation of predictions 8 and 9 per
  price; a forged trade in the contradictory-facts test now pays everywhere, so only the invalid witness refuses it,
  for both buy and pass; and a docstring and a file header were brought up to date.
- **Outside review, sixth round, on 25 November 2026**, of draft 6: Astra answered PASS, reading the files
  without running them; ChatGPT (same chat) answered FIX, after running the 95 unit tests, the 57 planted bugs (57 caught) and the made-up run. ChatGPT found one real gap: removing the copy
  of the condition bound handed to each step was caught by no test. It cannot change a recorded request, since the
  ledger keeps its own copies, but a shared bound could carry one step's changes into the next. Fixed in draft 7:
  the marking test's second run now records whether any argument the runner hands the engine already carries a
  mark, and requires that none does; it also wraps the two Problem methods the runner calls directly, which the
  wrapper list had left out; and the bug is planted as number 58. Smaller points: the fifth-round note above now
  says "invalid witness" (the forged trade has a witness, but it is invalid); and, from Astra, the outside
  instructions now state the rule for event names.
- **Outside review, seventh round, on 25 November 2026**, of draft 7. ChatGPT (same chat) answered FIX: it confirmed
  the plan's SHA-256 and line 3, the checker's hash, every sixth-round fix, 58 of 58 planted bugs caught, the 95 unit
  tests and the made-up run, and found one new gap: the checker's name rule ends in `$`, which in Python also matches
  just before a final newline, so the checker and the outside loader accepted an unused event named "B" followed
  by a newline. The checker is fixed by this plan and is not changed; it cannot be misled by such a name, since a
  name with a newline never matches a word in any expression. Fixed in draft 8: the loader for the outside file now
  requires every event name to match the rule in full, with a test and planted bug 59. A second reviewer, in a fresh
  Gemini chat, answered STOP only because two of the nine files were missing from its upload and it could not run
  code; its static check of the other seven found no problem. Sent all nine files of draft 7 again, it answered PASS
  from reading alone (it could not run code or compute hashes), finding every sixth-round point fixed and no new
  problem. It noted that the marking test marks only positional arguments, which is enough because the runner
  passes every engine argument by position.
- No team member other than Bhavik has seen any of this. Kahan and Jay are coding plan v14 blind; nothing here
  touches plan v14.

## 9. Files and procedure

| File | SHA-256 |
|---|---|
| `wot_check.py` (the checker; fixed by this plan) | `9c5b10c969792c436dda866fe478783f15166ff1f1dfa6fa5aaaebc85f07b072` |
| `v43_manifest.json`, listing `wot_check.py`, `wot_engine.py`, `test_wot_engine.py`, `test_wot_check.py`, `test_the_tests.py`, `v43_run.py`, `test_v43_run.py` and the outside file | in addendum v43.1, before the run |

1. Addendum v43.1 publishes the manifest's SHA-256. The manifest must give the checker hash above. Before launch, the
   person running it checks every file against the manifest and runs the three test files and `test_the_tests.py` on
   the Python used for the run; `test_the_tests.py` plants a fixed list of 59 bugs in copies of the engine, the
   checker and the run script, and must report that the tests caught every one, with none timed out.
2. The run is made on the Mac, once, after the v43.1 tag is public, with
   `python3 -B v43_run.py --run-after-tag <manifest SHA-256 from addendum v43.1> <outside file>`. It first creates
   `v43_run_attempts.log` exclusively, so a second start is refused; then it checks the manifest against the given
   hash, every listed file against the manifest, and the outside file's bytes against the manifest, and parses those
   same bytes; it records STARTED, then COMPLETE with the SHA-256 of both outputs, or STOPPED with the reason.
3. It writes `v43_run_output.txt` (the counts and the section 6 verdict) and `v43_certificates.jsonl` (one line per request in the ledger:
   the request, the problem, the certificate and its status), each through a temporary file and a rename. The COMPLETE line is the marker that both
   files are whole. Report v43 publishes the output and the attempts log unchanged, whatever they show, and says where
   the certificates file can be checked with `wot_check.py`.
4. Any change to our code after v43.1 is a dated, published addendum with new hashes and a new attempts log, before
   any further start.
