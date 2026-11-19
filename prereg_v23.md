# Plan v23: do chatbots write Bayes practice problems that can tell mistakes apart, and are their answer keys right?

Status: published as tag v23, 19 November 2026. Written 19 November 2026 after three rounds of outside review. No chatbot had been asked for any problem when this was published. The scoring code is reproduced in full in Appendices A to C; their SHA-256 hashes are in section 9.

No chatbot may be asked for problems until all of the following are published together as tag v23 in github.com/bhavikjain026/contrast-preregistrations:
- this plan;
- `v23.py`, `test_v23.py` and `parity_v20.py`, with the SHA-256 hashes in section 9;
- the completed checklist in section 12.

The analysis runs once, and the result is reported whatever it shows, including if it arrives after the 8 December stage freeze. Addendum v23.1, published before the run, contains only data hashes and a log of deviations. It changes no definition.

## 1. Why

Teachers and students now ask chatbots for practice problems. Our tutor diagnoses a student's wrong method from typed answers. That only works if the problem's numbers let different wrong methods give different answers.

Plan v20 counted published problems from six research papers. Its collision test fired on 21 of 23 distinct number sets.

v23 asks two questions of problems written by chatbots:
- Do they leave the tutor answers it cannot attribute?
- Is the chatbot's own answer key right?

Both describe the problems, not students. Neither says how often students make these mistakes, or how anyone reasoned.

## 2. Questions

**Q1, primary (Arm 1 only).** For each chatbot: of its distinct included number sets, what share admit at least one whole-percent answer, from 0 to 100, that fits two different wrong methods? Such an answer leaves the tutor with more than one candidate, so it has to ask again.

Fit uses the frozen tutor's own rule (section 6). As in the tutor, the correct answer is just one more candidate. An answer that fits the correct answer and two wrong methods still counts.

Q1 and v20's M2 are not nested; each can fire without the other:
- On 10/12/4, typing 11 fits 10 and 12, so Q1 fires and M2 does not.
- On 50/80/20, the correct answer, hit rate, 1 − false alarm and equal priors are all 80, so both fire.

**Q1x.** Q1 recomputed while ignoring the base rate / joint occurrence pair. Whenever 0 < b ≤ 2, typing 1 fits both of those methods, so low base rates collide almost automatically.

**Q2, co-headline secondary.** For each chatbot and arm: of its included problems with a scored key, what share has a key more than 1 percentage point from the correct answer? This is a discrepancy measure.

Also reported:
- the share more than 10% off in relative terms and more than 0.5 point off, so a key rounded to the nearest percentage point (or finer) is never flagged for rounding alone;
- the count of keys outside 0 to 100;
- the largest discrepancy.

**Q3, secondary.**
- The share where some whole-percent answer fits both the correct answer and a wrong method.
- Counts for all 15 pairs of wrong methods, including pairs with zero.
- The count with hit + false alarm = 100.
- v20's own M1, M2 and M1 or M2, compared with v20's 21 of 23 only.

**Q4, Arm 2 compliance.** The share of Arm 2's distinct included sets where the smallest of the 21 gaps among the seven exact values (the correct answer and six wrong methods) is at least 3 points. This is the rule Arm 2's request states. Subtraction is used as computed, even if negative.

## 3. Before generation: roster, terms, tiers, settings (filled in before publishing)

**Roster.** ChatGPT, Gemini and Claude, each in Arm 1 and Arm 2: six scheduled chats.

Every scheduled chat ends with one disposition:
- ran;
- `unavailable:<reason>`, after two technical failures;
- `dropped:<reason>`, if the terms forbid a planned use.

Every disposition is reported.

**Terms.** For each product, Bhavik reads the terms for his account and records the date, the clause relied on and the decision for each use:
1. saving replies privately;
2. giving them to separate Claude Code sessions to split and extract;
3. publishing counts and our extracted numbers.

No problem text or screenshot is ever shown publicly.

**Terms read (19 November 2026), confirmed by Bhavik:**
- **OpenAI Terms of Use** (openai.com/policies/terms-of-use, effective 1 January 2026; the rest-of-world address serves the same text, and this version applies in India): under 'Ownership of content', the user owns Output and OpenAI assigns its rights in it; under 'What you cannot do', no using Output to develop competing models, no automatic or programmatic extraction of data or Output, and no presenting Output as human-generated. Nothing on benchmarking. The Sharing & Publication Policy (updated 14 November 2022) asks that shared AI content be clearly marked as AI-generated.
- **Anthropic Consumer Terms** (anthropic.com/legal/consumer-terms, effective 8 Oct 2025, section 4): Anthropic assigns "all of our right, title, and interest—if any—in Outputs". Section 3 bars using the Services to develop competing products or to train models. Nothing found on benchmarking or on pasting output elsewhere.
- **Google Terms of Service** (policies.google.com/terms, effective 30 July 2026): "Google won't claim ownership over" content you generate. Among the "Don't abuse our services" items: "using AI-generated content from our services to develop machine learning models or related AI technology". Nothing found on benchmarking or on pasting output elsewhere. The Generative AI Prohibited Use Policy (last modified 17 December 2024) adds nothing on ownership, other tools or benchmarking, and bars passing generated content off as solely human-made; the only Gemini-specific additional terms (Agentic Calling, 24 September 2026) cover phone calls only. (The older Generative AI Additional Terms no longer apply.)
- **Decision (Bhavik, 19 November 2026):** the terms read permit uses 1–3 for all three products. We will not use any output to train or develop a model.
- **Our reading of OpenAI's extraction clause:** it concerns extracting data or Output from the Services by automated means. Every request is typed by hand in the app and every reply copied by hand; splitting and extracting a saved text file afterwards does not access the Services. **Labelling:** every published count names the chatbot, model shown and date, and says the problems were AI-generated.
- **Documents read for this decision (19 November 2026):**
  - OpenAI Terms of Use, https://openai.com/policies/terms-of-use/ (same text at https://openai.com/policies/row-terms-of-use/), read 19 November 2026;
  - OpenAI Sharing & Publication Policy, https://openai.com/policies/sharing-publication-policy/, read 19 November 2026;
  - Google Generative AI Prohibited Use Policy, https://policies.google.com/terms/generative-ai/use-policy, read 19 November 2026;
  - Google list of service-specific additional terms, https://policies.google.com/terms/service-specific, read 19 November 2026;
  - Gemini Apps Agentic Calling Additional Terms of Service, https://policies.google.com/terms/generative-ai/gemini-agentic-calling, read 19 November 2026;
  - Anthropic Consumer Terms, https://www.anthropic.com/legal/consumer-terms, read 19 November 2026 (still effective 8 October 2025; nothing new since).

**Tiers, fixed now:**
- ChatGPT: Plus (paid)
- Gemini: paid Google AI plan (exact plan name recorded at generation)
- Claude: Max (paid)

**Settings:**
- the default model;
- a new chat;
- no custom instructions, files or projects;
- memory and personalisation off where the app allows it;
- no search, research, code or tools turned on by us.

**Record for each chat:**
- the model name shown;
- any fallback or model-switch notice;
- any tool the app used on its own, as shown;
- the date and start and end time (IST);
- a screenshot of the model selector.

Write "unknown" for anything that can't be observed.

## 4. Generation

**Order and timing.** Arm 1 runs for ChatGPT, then Gemini, then Claude. Arm 2 then runs for the same three, each in a fresh chat. All six chats happen in one sitting that starts within 24 hours of publication and lasts at most three hours.

**Arm 1, verbatim:**

> Write 20 numbered practice problems for students learning Bayes' theorem. For each, state the base rate, the probability of a positive result when the condition is present, and the probability of a positive result when it is absent. Ask for the probability that the condition is present given a positive result. Give a numerical answer to each problem.

**Arm 2, verbatim:**

> Write 20 numbered practice problems for students learning Bayes' theorem. For each, state the base rate, the probability of a positive result when the condition is present, and the probability of a positive result when it is absent. Ask for the probability that the condition is present given a positive result. Choose the three numbers so that the correct answer and these six common wrong answers are all at least 3 percentage points apart from each other: the hit rate; the base rate; the base rate times the hit rate; the hit rate minus the false-alarm rate; 100% minus the false-alarm rate; and the hit rate divided by the sum of the hit rate and the false-alarm rate. Give a numerical answer to each problem.

**Attempts.**
- **A technical failure** is an error message, or no new text for 5 minutes, before the first problem appears.
- **After one technical failure,** open a new chat and try once more. Save `<chatbot>_arm<k>_attempt1.txt` and `_attempt2.txt`.
- **After a second failure,** the chat is `unavailable` and is not replaced.
- **Once any problem has appeared,** the reply stands whatever happens next. A refusal, a short list, a stall or a truncation all stand.
- **A refusal is a disposition of "ran"** with zero problems produced. It is not "unavailable".

**Saving.** Each attempt is copied exactly as shown into `v23_run/replies/` by Bhavik. Its SHA-256 goes in `hashes.txt` before anything else is done. Bhavik copies replies but never extracts, splits or adjudicates.

## 5. Splitting and extraction (by sessions that never see a raw reply's answers while reading stems)

**Step 1, split.** A Claude Code session C receives only the used attempt for each chat, plus this step.

C does three things:
1. It gives every problem occurrence an ID (label plus occurrence number, for example `7#1` or `7#2`). It then writes a stem file and a key file keyed by that ID.
2. The stem file holds each occurrence's text up to and including its question sentence, with every rate kept. The key file holds everything after the question for that occurrence (working, answer, units) and nothing else.
3. Preamble and closing text go to a log.

C extracts no numbers and scores nothing.

A deterministic script then checks the split:
- every non-blank line of the reply appears exactly once, in the stem file, the key file or the log;
- no stem line contains "answer", "=", "≈" or "%" after the question sentence.

A failure means C redoes the split, and the failure is logged.

**Step 2, stems.** Two separate Claude Code sessions, A and B, each receive only the stem files and this section. Each writes a full stem file, one row per slot 1 to 20, and it is hashed before either sees the other's.

**Stem rules:**
- The slot for label n is occurrence `n#1`. Any other occurrence is logged and not scored. A label with no occurrence is `missing`.
- A percentage is taken as written.
- A bare decimal in [0, 1] is a probability, multiplied by 100, unless the text says percent.
- "1 in N" and "k of N" are stored as exact fractions of 100, for example `100/2500000`.
- A denominator found by one subtraction of stated counts (healthy = total − ill) is allowed and logged. Anything else derived is excluded.
- Specificity or a true-negative rate gives f = 100 − value. A miss or false-negative rate gives h = 100 − value.
- "Overall accuracy" without conditional rates is excluded.
- Nothing is rounded.

**Exclusions, each logged with the source sentence:**
- a missing or unconvertible number;
- more than two hypotheses, more than one test result, or sequential tests;
- a question for something other than P(condition | positive);
- inconsistent numbers;
- a value outside (0, 100).

**Step 3, stem agreement (mechanical).** Where A and B agree, their value stands. Where they disagree on any field, the slot is `excluded:unresolved`. No person decides. The result, `stems_final.csv`, is hashed.

**Step 4, keys.** Only after `stems_final.csv` is hashed do A and B receive the key files. Each extracts the key for occurrence `n#1`:
- the last answer explicitly marked final, or else the last numeric answer;
- several forms of the same number are allowed, and the most precise one is used;
- if the forms disagree by more than rounding, the key is `unresolved`.

**Key conversion rules:**
- A percentage is taken as written.
- A bare decimal in [0, 1] is ×100.
- A bare fraction without a percent sign (for example 9/59) is a probability, ×100 (900/59).
- A leading "≈", "about", "approximately" or "roughly" is ignored, and the number is scored.
- A range is `range`. Words only is `nonnumeric`. No answer is `none`.

Where A and B disagree, the key is `unresolved`. An unresolved or missing key never removes the stem. Only `scored` keys enter Q2. A numeric key outside 0 to 100 is scored as given.

**Step 5, lock.** These are hashed in addendum v23.1:
- every attempt file;
- the split files and the check output;
- both stem files and `stems_final.csv`;
- both key files;
- `extract_final.csv`.

No one runs `v23.py`, a collision check or a Bayes calculation on extracted data before v23.1 is published. Kahan and Jay take no part, which keeps them clear of the v14 blinding.

## 6. Definitions (as coded in `v23.py`)

**Values.** b, h and f are exact percentages; B, H and F are the same values as fractions. All new measures use exact rational arithmetic.
- Correct answer: 100·BH / (BH + (1 − B)F).
- The six wrong methods, in points: 100H; 100B; 100BH; 100(H − F); 100(1 − F); 100H/(H + F).
- Subtraction is kept raw and can be negative.

**Fit (the frozen tutor's rule).** A whole percent k fits a value v if |k − v| ≤ 1 + 10⁻⁷ points. This is `topic_engine.matches` (|pred − answer| ≤ tol + 1e−9) with `screening_quiz.TOL` = 0.01, converted to points. k runs from 0 to 100, the range the tutor accepts.

**How the tutor treats the correct answer.** It is one more candidate: the tutor says "correct" only when the correct answer is the only fit (`tutor.py`, `_after_first`). So Q1 does not remove answers that also fit the correct answer.

**The four measures:**
- **Q1:** some k fits two different wrong methods.
- **Q3 wrong-looks-right:** some k fits the correct answer and a wrong method.
- **Q4:** the smallest of the 21 exact gaps is at least 3.
- **Distinct set:** exact equality of (b, h, f) within one chatbot and arm. Q1, Q1x, Q3 and Q4 use distinct sets; Q2 uses every included slot.

**Legacy v20 measures.** v20's float path: each exact input rounded once to a float probability, the frozen tutor's formulas in float, then v20's `audit()` copied unchanged.
- M1: a wrong method's own typed answer (halves up) fits the correct value, within 1 + 1e−9.
- M2: a wrong method's own typed answer fits another wrong method's value.

`parity_v20.py` checks the registered v20 code and item file by SHA-256. It then checks, item by item, that the float values equal the frozen tutor's and that M1 and M2 match the registered code on all 23 v20 sets, giving 21 of 23.

**Required tests.** `test_v23.py` must pass (27 tests) before publication. They include:
- the 11 case;
- the tutor's fit boundary, including the 5.0001 / 19.9996 / 16.9996 case that the tutor itself would accept;
- the correct answer treated as a candidate (50/80/20);
- negative subtraction fitting 0;
- strict Q2 cutoffs, including equality at the 0.5-point floor;
- Arm 2 gaps;
- exactly 15 pairs, each listed once;
- rejection of malformed rows, bad statuses, `nan`, `15%`, duplicate or missing slots, and absent roster groups;
- whole-group dispositions;
- a 10³⁰⁹ key reported without a crash;
- identical legacy results for identical float inputs.

## 7. Reporting

**For each chatbot and arm, in this order:**
1. Disposition. R of 20 requested labels filled, I included, exclusions by reason, missing, D distinct sets.
2. Q1 (primary for Arm 1 only) K of D, then Q1x.
3. Q2: J of E scored keys more than 1 point off, U unscored by reason, the relative and out-of-range counts, the largest discrepancy.
4. Q3 and the 15-pair table. Then the legacy v20 measures.
5. For Arm 2, Q4 of D.

**Ties to v20.** v20's 21 of 23 appears only beside the legacy measure.

**Intervals.** Exact Clopper–Pearson intervals appear in the repository report only, labelled nominal. The items in one reply are not independent, and one reply per arm says nothing about variation between replies. Slides show counts with their denominators and no intervals.

**Not done:**
- no ranking of chatbots;
- no significance test;
- no pooling;
- no extra runs.

**If the result is unflattering, it is still the headline.** For example: few ambiguous sets, accurate keys, or many unscoreable problems.

## 8. What we will and won't say

**We will say** (adding "after one retry for a technical failure" where that happened):

> "Asked once on [date], [app, tier, model shown, any tool it used on its own] filled R of the 20 requested labels; I problems were usable. In K of D distinct number sets, a student could type one answer that fits two of our tutor's six wrong methods, so the tutor would have to ask again; ignoring the base rate / joint occurrence pair, K′ of D. Of I problems, E had a scoreable answer key, and J of those E were more than 1 point from the correct answer."

For Arm 2: "Asked to keep all seven answers at least 3 points apart, it did so in Q4 of D distinct number sets."

**We will not say:**
- that chatbots in general write bad problems;
- that one chatbot beats another;
- that a chatbot "can" or "can't" do this in general;
- anything about other prompts, settings, models or dates;
- anything about students or how anyone reasoned.

## 9. Code and hashes

| File | SHA-256 |
|---|---|
| `v23.py` | `f31694bb53e4dc56c558e44ffe409641e5efe7d3aaa9d174ff767d171946aec5` |
| `test_v23.py` | `f016fc7b7e705a8bbc037b2bb3569cc170026177f404b199c5c1441b11429ddc` |
| `parity_v20.py` | `f4eb4adc7110549dac1e1c42eabbeef517abd7767e9d2298aa7561b1f490f78b` |

`parity_v20.py` pins the registered v20 code (`c71003c8…`, as listed in published plan v22, section 6) and the locked v20 item file (`5f337517…`, addendum v20.1).

## 10. Known limits, stated in advance

- **One request per arm, one reply, one day.**
- **Consumer apps may route to other models,** and Bhavik's accounts may differ from fresh ones.
- **The six wrong methods and the fit window are ours.** Q1 counts whole-percent answers only, although the tutor also accepts decimals.
- **Low base rates make the base rate and joint occurrence collide almost automatically.** That is why Q1x sits in the same sentence.
- **Bhavik sees the full replies while copying them.** He does no splitting, extraction or adjudication.
- **Claude Code sessions split and extract all replies, including Claude's own.** This is a possible conflict, mitigated by two locked extractions and mechanical agreement.
- **Q2 is judged against our extracted numbers.** Where the text is ambiguous, the rules decide, and that is logged.

## 11. Timeline

1. Publish v23.
2. Generate within 24 hours.
3. Split and check.
4. Extract, agree and lock the stems.
5. Extract and agree the keys.
6. Publish addendum v23.1.
7. Run once.
8. Report.

Only results finished before the 8 December freeze are used at the final. The report is published whenever it is finished.

## 12. Pre-publication checklist

- [x] `test_v23.py` passes: 27 of 27 (19 Nov, on the sandbox and on the Mac copy).
- [x] `parity_v20.py` passes (19 Nov): both pinned hashes match; float values equal the frozen tutor's on every item; M1 and M2 agree with the registered v20 code on all 54 item rows; 21 of 23 standard sets.
- [x] The frozen tutor's rules were checked against its code (kiosk-2026-11-20 copy of `src/`, frozen hashes unchanged):
  - fit is |pred − answer| ≤ 0.01 + 1e−9 (`topic_engine.matches`, `screening_quiz.TOL`);
  - the correct answer is a candidate, and "correct" is said only when it is the only fit (`tutor.py`, `_after_first`);
  - answers below 0 or above 100 are asked again (checked on the demo path);
  - negative predictions are compared like any other value.
- [x] The tutor's own `diagnose()` (frozen `src/`, tolerance 0.01) agrees with `v23.fitting` on 13 test problems × 101 whole-percent answers: 1,313 comparisons, 0 disagreements (19 Nov). The cases include the 1 + 1e-7 boundary, 50/80/20 and negative subtraction.
- [x] Tiers and terms filled in (Bhavik, 19 November 2026); roster final: six groups, none dropped.
- [x] The hashes in section 9 are current.

## Appendix A — v23.py

```python
"""Plan v23 scoring (written and tested BEFORE any chatbot is asked; published with the plan).

  python3 v23.py extract_final.csv        prints the report

extract_final.csv: one row per slot 1..20 for every (chatbot, arm) in the run. Columns:
  chatbot, arm (1 or 2), slot (1..20), status, b, h, f, key, key_status
  status:     included | missing | excluded:<reason>        (missing = no problem under that label)
  b, h, f:    exact converted percentages as written by the extraction rules: a decimal ("0.00004") or a
              fraction ("100/2500000"); never rounded. Empty unless status is included.
  key:        the stated answer in percent, exact as above; empty if key_status is not scored.
  key_status: scored | none | range | nonnumeric | unresolved   (only "scored" enters Q2)
New measures use exact rational arithmetic (fractions.Fraction) and the frozen tutor's own matching rule:
an answer fits a value when |answer - value| <= 0.01 + 1e-9 in probability units (topic_engine.matches with
screening_quiz.TOL = 0.01, EPS = 1e-9), i.e. within 1 + 1e-7 percentage points. As in the tutor, the correct answer
is one of the candidates: an answer that fits the correct answer AND a wrong method is still ambiguous (the tutor
asks a follow-up unless the correct answer is the ONLY fit; tutor.py _after_first).
The legacy v20 measures use v20's float code on float inputs, copied unchanged, for comparison with v20 only.
No learner, no human data: arithmetic on numbers only.
"""
import csv
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations

WRONG = ("hit_rate", "base_rate_only", "joint_occurrence", "likelihood_subtraction",
         "false_alarm_complement", "equal_priors")
ALL = ("bayes",) + WRONG
STATUSES_KEY = ("scored", "none", "range", "nonnumeric", "unresolved")
ROSTER = [(c, a) for a in ("1", "2") for c in ("ChatGPT", "Gemini", "Claude")]
COLUMNS = ["chatbot", "arm", "slot", "status", "b", "h", "f", "key", "key_status"]
ONE, HUNDRED = Q(1), Q(100)
FIT = ONE + Q(1, 10 ** 7)      # the tutor: 0.01 + 1e-9 in probability units = 1 + 1e-7 points


def predictions(b, h, f):
    """b, h, f: exact percentages (Fraction). -> {method: exact value in percentage points}."""
    B, H, F = b / HUNDRED, h / HUNDRED, f / HUNDRED
    return {"bayes": HUNDRED * B * H / (B * H + (1 - B) * F),
            "hit_rate": HUNDRED * H, "base_rate_only": HUNDRED * B, "joint_occurrence": HUNDRED * B * H,
            "likelihood_subtraction": HUNDRED * (H - F), "false_alarm_complement": HUNDRED * (1 - F),
            "equal_priors": HUNDRED * H / (H + F)}


def fitting(k, pr):
    """Methods whose exact value fits whole-percent answer k under the tutor's rule (within 1 + 1e-7 points)."""
    return {m for m, v in pr.items() if abs(Q(k) - v) <= FIT}


def tutor_ambiguity(pr):
    """PRIMARY (Q1). Whole-percent answers k = 0..100 that fit two or more different wrong methods (k may also fit
    the correct answer; the tutor then still has several candidates and asks a follow-up).
    -> (ambiguous?, sorted colliding pairs, sorted witness answers k)"""
    pairs, ks = set(), set()
    for k in range(0, 101):
        w = sorted(fitting(k, pr) & set(WRONG))
        if len(w) >= 2:
            ks.add(k)
            pairs.update(combinations(w, 2))
    return bool(pairs), sorted(pairs), sorted(ks)


def wrong_looks_right(pr):
    """Q3. Wrong methods sharing a whole-percent answer k = 0..100 with the correct answer. -> sorted methods"""
    out = set()
    for k in range(0, 101):
        s = fitting(k, pr)
        if "bayes" in s:
            out |= s & set(WRONG)
    return sorted(out)


def arm2_min_gap(pr):
    """Arm 2 compliance: the smallest of the 21 absolute gaps among the seven exact values (subtraction raw).
    The request asked for every gap to be at least 3 points."""
    return min(abs(pr[a] - pr[b]) for a, b in combinations(ALL, 2))


# ---- legacy v20 (copied unchanged from v20.audit: floats, EPS, halves up; for comparison with v20 only) ----
EPS = 1e-9


def typed_of(v):
    return math.floor(v + 0.5 + EPS)


def float_predictions(b, h, f):
    """v20's float path: each exact percentage rounded once to a float probability, then the frozen tutor's own
    formulas (bayes_strategies.SPEC) in float, times 100 (as v20.main)."""
    B, H, F = float(b / HUNDRED), float(h / HUNDRED), float(f / HUNDRED)
    v = {"bayes": B * H / (B * H + (1 - B) * F), "hit_rate": H, "base_rate_only": B, "joint_occurrence": B * H,
         "likelihood_subtraction": H - F, "false_alarm_complement": 1 - F, "equal_priors": H / (H + F)}
    return {m: 100 * x for m, x in v.items()}


def legacy_v20(fp):
    """v20.audit copied unchanged, on float values in points: M1, a wrong method's own typed answer fits the correct
    value; M2, a wrong method's own typed answer fits another wrong method's value."""
    typed = {m: typed_of(v) for m, v in fp.items()}
    fits = {m: {o for o in fp if abs(typed[m] - fp[o]) <= 1.0 + EPS} for m in fp}
    m1 = sorted(m for m in WRONG if "bayes" in fits[m])
    m2 = sorted({tuple(sorted((a, o))) for a in WRONG for o in fits[a] if o in WRONG and o != a})
    return m1, m2


# ---- Q2 ----
def key_flags(key, pr):
    """-> (abs error, absolute flag: > 1 point, relative flag: > 10% of the correct answer AND > 0.5 point,
           out-of-range flag: key < 0 or > 100). Exact."""
    t = pr["bayes"]
    err = abs(key - t)
    rel = t > 0 and err > Q(1, 10) * t and err > Q(1, 2)
    return err, err > ONE, rel, key < 0 or key > HUNDRED


def cp(k, n):
    """Exact Clopper-Pearson 95% bounds by bisection. Nominal only: items in one reply are not independent."""
    if n == 0:
        return (math.nan, math.nan)
    pmf = lambda p, j: math.comb(n, j) * p ** j * (1 - p) ** (n - j)
    tail_ge = lambda p: sum(pmf(p, j) for j in range(k, n + 1))
    tail_le = lambda p: sum(pmf(p, j) for j in range(0, k + 1))

    def solve(fn, increasing):
        lo, hi = 0.0, 1.0
        for _ in range(100):
            mid = (lo + hi) / 2
            if (fn(mid) < 0.025) == increasing:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    return (0.0 if k == 0 else solve(tail_ge, True)), (1.0 if k == n else solve(tail_le, False))


def frac(k, n):
    if n == 0:
        return "0/0 (NA)"
    lo, hi = cp(k, n)
    return f"{k}/{n} ({100 * k / n:.1f}%; nominal 95% interval {100 * lo:.1f} to {100 * hi:.1f})"


# ---- input ----
def exact(text, where):
    try:
        v = Q(text.strip())
    except (ValueError, ZeroDivisionError):
        raise SystemExit(f"{where}: not an exact number: {text!r}")
    return v


def load(path, roster=ROSTER):
    with open(path, newline="", encoding="utf-8") as fh:
        raw = list(csv.reader(fh))
    if not raw or raw[0] != COLUMNS:
        raise SystemExit(f"header must be exactly {COLUMNS}")
    rows = []
    for i, cells in enumerate(raw[1:], start=2):
        if len(cells) != len(COLUMNS):
            raise SystemExit(f"line {i}: expected {len(COLUMNS)} fields, found {len(cells)}")
        rows.append(dict(zip(COLUMNS, cells)))
    seen = set()
    for i, r in enumerate(rows, start=2):
        where = f"line {i} ({r['chatbot']}, arm {r['arm']}, slot {r['slot']})"
        if (r["chatbot"], r["arm"]) not in roster:
            raise SystemExit(f"{where}: chatbot/arm not in the roster {roster}")
        if r["slot"] not in {str(x) for x in range(1, 21)}:
            raise SystemExit(f"{where}: slot must be 1..20")
        key = (r["chatbot"], r["arm"], r["slot"])
        if key in seen:
            raise SystemExit(f"{where}: duplicate slot")
        seen.add(key)
        st = r["status"]
        ok = st in ("included", "missing") or any(st.startswith(p) and len(st) > len(p)
                                                  for p in ("excluded:", "unavailable:", "dropped:"))
        if not ok:
            raise SystemExit(f"{where}: invalid status {st!r}")
        if st == "included":
            for c in ("b", "h", "f"):
                r[c] = exact(r[c], where)
                if not 0 < r[c] < 100:
                    raise SystemExit(f"{where}: {c} must be strictly between 0 and 100")
            if r["key_status"] not in STATUSES_KEY:
                raise SystemExit(f"{where}: invalid key_status {r['key_status']!r}")
            if r["key_status"] == "scored":
                r["key"] = exact(r["key"], where)
            elif r["key"].strip():
                raise SystemExit(f"{where}: key given but key_status is {r['key_status']}")
        elif any(r[c].strip() for c in ("b", "h", "f", "key", "key_status")):
            raise SystemExit(f"{where}: a row that is not included must have empty b, h, f, key and key_status")
    groups = defaultdict(list)
    for r in rows:
        groups[(r["chatbot"], r["arm"])].append(r)
    for g in roster:
        rs = groups.get(g, [])
        if len(rs) != 20:
            raise SystemExit(f"{g}: expected 20 slot rows, found {len(rs)} (record unavailable or dropped groups too)")
        whole = [r["status"] for r in rs if r["status"].startswith(("unavailable:", "dropped:"))]
        if whole and len(whole) != 20:
            raise SystemExit(f"{g}: 'unavailable' and 'dropped' apply to all 20 slots of a group or none")
    return rows


# ---- report ----
def summarise(rs):
    inc = [r for r in rs if r["status"] == "included"]
    R = sum(r["status"] == "included" or r["status"].startswith("excluded:") for r in rs)
    disposition = next((r["status"] for r in rs if r["status"].startswith(("unavailable:", "dropped:"))), "ran")
    triples = {}
    for r in inc:
        triples.setdefault((r["b"], r["h"], r["f"]), r)
    D = len(triples)
    s = dict(disposition=disposition, R=R, I=len(inc), excluded=Counter(r["status"] for r in rs if r["status"].startswith("excluded:")),
             missing=sum(r["status"] == "missing" for r in rs), D=D, K=0, Kx=0, W=0, L1=0, L2=0, L12=0, SYM=0,
             pairs=Counter({p: 0 for p in combinations(sorted(WRONG), 2)}), A2pass=0, A2gaps=[])
    for t in triples:
        pr = predictions(*t)
        amb, pairs, _ = tutor_ambiguity(pr)
        s["K"] += amb
        s["Kx"] += any(p != ("base_rate_only", "joint_occurrence") for p in pairs)
        s["pairs"].update(pairs)
        s["W"] += bool(wrong_looks_right(pr))
        m1, m2 = legacy_v20(float_predictions(*t))
        s["L1"] += bool(m1); s["L2"] += bool(m2); s["L12"] += bool(m1 or m2)
        s["SYM"] += (t[1] + t[2] == HUNDRED)
        g = arm2_min_gap(pr)
        s["A2gaps"].append(g); s["A2pass"] += g >= 3
    sc = [r for r in inc if r["key_status"] == "scored"]
    flags = [key_flags(r["key"], predictions(r["b"], r["h"], r["f"])) for r in sc]
    s.update(E=len(sc), U=len(inc) - len(sc), J=sum(f[1] for f in flags), Jrel=sum(f[2] for f in flags),
             OOR=sum(f[3] for f in flags), maxerr=max((f[0] for f in flags), default=None),
             unscored=Counter(r["key_status"] for r in inc if r["key_status"] != "scored"))
    return s


def largest(s):
    """Exact error printed to 4 decimals without converting to float (keys like 1e309 must not crash)."""
    if s["maxerr"] is None:
        return "NA"
    x = s["maxerr"]
    n = (x.numerator * 10000 + x.denominator // 2) // x.denominator
    return f"{n // 10000}.{n % 10000:04d}"


def report(rows):
    out = []
    groups = defaultdict(list)
    for r in rows:
        groups[(r["chatbot"], r["arm"])].append(r)
    for (bot, arm), rs in sorted(groups.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        s = summarise(rs)
        role = "Arm 1 (plain request)" if arm == "1" else "Arm 2 (request states the 3-point rule)"
        out.append(f"== {bot}, {role}; disposition: {s['disposition']}")
        out.append(f"produced R = {s['R']}; included I = {s['I']}; excluded {dict(s['excluded'])}; "
                   f"missing {s['missing']}; distinct triples D = {s['D']}")
        out.append(f"Q1{' (PRIMARY)' if arm == '1' else ''} possible ambiguity (a whole-percent answer fits two of our six wrong methods): "
                   f"K = {frac(s['K'], s['D'])}")
        out.append(f"   same, ignoring the base rate / joint occurrence pair: {frac(s['Kx'], s['D'])}")
        out.append(f"Q2 answer keys: scored E = {s['E']}, unscored U = {s['U']} {dict(s['unscored'])}; "
                   f"more than 1 point from the correct answer J = {frac(s['J'], s['E'])}")
        out.append(f"   more than 10% relative and more than 0.5 point: {frac(s['Jrel'], s['E'])}; "
                   f"outside 0-100: {s['OOR']}; largest error "
                   f"{largest(s)} points")
        out.append(f"Q3 a whole-percent answer fits the correct answer and a wrong method: {frac(s['W'], s['D'])}")
        out.append(f"   hit + false alarm = 100: {s['SYM']}/{s['D']}")
        out.append("   colliding pairs (triples with that pair; a triple can count in several rows): "
                   + "; ".join(f"{a}/{b} {n}" for (a, b), n in sorted(s["pairs"].items())))
        out.append(f"   legacy v20 (compare with v20's 21/23 only): M1 {frac(s['L1'], s['D'])}; "
                   f"M2 {frac(s['L2'], s['D'])}; M1 or M2 {frac(s['L12'], s['D'])}")
        if arm == "2":
            out.append(f"Arm 2 compliance (all 21 gaps among the seven values at least 3 points): "
                       f"{frac(s['A2pass'], s['D'])}")
    out.append("Intervals are nominal: the items in one reply are not independent draws.")
    return "\n".join(out)


if __name__ == "__main__":
    print(report(load(sys.argv[1])))
```

## Appendix B — test_v23.py

```python
"""Tests for v23.py. Made-up numbers only. All must pass before v23 is published."""
import csv, os, tempfile
from fractions import Fraction as Q
import pytest
import v23

P = lambda b, h, f: v23.predictions(Q(str(b)), Q(str(h)), Q(str(f)))


R1 = [("X", "1")]


def write(rows, extra_line=None):
    d = tempfile.mkdtemp(); p = os.path.join(d, "x.csv")
    with open(p, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(v23.COLUMNS)
        for r in rows:
            w.writerow([r.get(c, "") for c in v23.COLUMNS])
        if extra_line is not None:
            fh.write(extra_line + "\n")
    return p


def L(path, roster=R1):
    return v23.load(path, roster)


def group(slots, bot="X", arm="1"):
    """slots: {slot: dict(...)}; all other slots 1..20 are missing."""
    return [dict(chatbot=bot, arm=arm, slot=str(s), **slots.get(s, dict(status="missing"))) for s in range(1, 21)]


def inc(b, h, f, key="", ks=None):
    return dict(status="included", b=str(b), h=str(h), f=str(f), key=str(key), key_status=ks or ("scored" if key != "" else "none"))


def test_formula_units():
    pr = P(1, 90, 5)
    assert pr["bayes"] == 100 * Q(9, 1000) / (Q(9, 1000) + Q(99, 100) * Q(5, 100))      # 15.38%, not 0.18%
    assert pr["joint_occurrence"] == Q(9, 10) and pr["false_alarm_complement"] == 95


def test_eleven_case():
    pr = P(10, 12, 4)                       # values 12, 10, 1.2, 8, 96, 75; correct 25
    assert pr["bayes"] == 25
    amb, pairs, ks = v23.tutor_ambiguity(pr)
    assert amb and ("base_rate_only", "hit_rate") in pairs and 11 in ks           # 11 fits 10 and 12
    assert ("base_rate_only", "likelihood_subtraction") in pairs and 9 in ks       # 9 fits 8 and 10
    assert v23.legacy_v20(v23.float_predictions(Q(10), Q(12), Q(4))) == ([], [])  # v20's M2 misses both


def test_demo_problem():
    amb, pairs, _ = v23.tutor_ambiguity(P(60, 75, 30))
    assert ("joint_occurrence", "likelihood_subtraction") in pairs


def test_clean_problem():
    pr = P(20, 40, 10)
    assert v23.tutor_ambiguity(pr) == (False, [], []) and v23.wrong_looks_right(pr) == []


def test_fit_rule_matches_the_tutor():
    # the frozen tutor accepts |answer - value| <= 0.01 + 1e-9 (probability units) = 1 + 1e-7 points
    assert "m" in v23.fitting(11, {"m": Q(10)})                                    # exactly 1 point fits
    assert "m" in v23.fitting(2, {"m": Q("0.9999999996")})                         # 1.0000000004 fits, as in the tutor
    assert "m" in v23.fitting(2, {"m": Q("0.9999999")})                            # 1.0000001 fits (the boundary)
    assert "m" not in v23.fitting(2, {"m": Q("0.99999985")})                       # 1.00000015 does not
    amb, pairs, _ = v23.tutor_ambiguity(P("5.0001", "19.9996", "16.9996"))       # joint 0.9999999996, subtraction 3
    assert ("joint_occurrence", "likelihood_subtraction") in pairs                 # the tutor would accept 2 for both
    amb, pairs, _ = v23.tutor_ambiguity(P(5, "19.999997", "16.999997"))           # joint 0.99999985, subtraction 3
    assert ("joint_occurrence", "likelihood_subtraction") not in pairs


def test_correct_answer_is_a_candidate_like_in_the_tutor():
    pr = P(50, 80, 20)                      # correct = hit = 1-f = equal priors = 80; others 50, 40, 60
    amb, pairs, ks = v23.tutor_ambiguity(pr)  # 80 fits correct AND three wrong methods: the tutor asks a follow-up
    assert amb and ks == [79, 80, 81] and ("false_alarm_complement", "hit_rate") in pairs
    assert v23.wrong_looks_right(pr) == ["equal_priors", "false_alarm_complement", "hit_rate"]


def test_negative_subtraction_near_zero():
    pr = P("0.5", 5, "5.5")                 # subtraction -0.5 fits the answer 0, like any value in the tutor
    assert pr["likelihood_subtraction"] == Q(-1, 2)
    amb, pairs, ks = v23.tutor_ambiguity(pr)
    assert ("base_rate_only", "likelihood_subtraction") in pairs and 0 in ks
    assert set(v23.wrong_looks_right(pr)) == {"base_rate_only", "joint_occurrence", "likelihood_subtraction"}


def test_key_flags():
    pr = P(10, 12, 4)
    f = lambda k: v23.key_flags(Q(k), pr)[1:3]
    assert f("26") == (False, False)
    assert f("26.0000000005") == (True, False)
    assert f("27.5") == (True, False)          # exactly 10% relative is not more than 10%
    assert f("27.50000001") == (True, True)
    assert v23.key_flags(Q(120), pr)[3] is True  # out of range is scored and counted
    small = P("0.2", 80, 10)                   # correct 1.578%: a correctly rounded key of 2 is not flagged
    assert v23.key_flags(Q(2), small)[1:3] == (False, False)
    one = P(1, 50, 50)                         # correct 1%: 0.5 point off is not more than 0.5 point
    assert v23.key_flags(Q("1.5"), one)[2] is False and v23.key_flags(Q("1.500001"), one)[2] is True


def test_arm2_gap():
    assert abs(float(v23.arm2_min_gap(P(10, 50, 5))) - 2.6315789) < 1e-6
    assert v23.arm2_min_gap(P(20, 40, 10)) == 10


def test_typed_halves_up():
    assert v23.typed_of(72.5) == 73 and v23.typed_of(3.75) == 4


def test_clopper_pearson():
    lo, hi = v23.cp(0, 20); assert lo == 0 and abs(hi - (1 - 0.025 ** (1 / 20))) < 1e-6
    lo, hi = v23.cp(10, 20); assert abs(lo - 0.27196) < 1e-4 and abs(hi - 0.72804) < 1e-4
    assert v23.frac(0, 0) == "0/0 (NA)"


def test_denominators():
    rows = group({1: inc(10, 12, 4, 25), 2: inc(10, 12, 4, 30), 3: inc(10, 12, 4)})
    s = v23.summarise(L(write(rows)))
    assert (s["R"], s["I"], s["D"], s["K"], s["E"], s["J"], s["U"]) == (3, 3, 1, 1, 2, 1, 1)
    assert s["pairs"][("base_rate_only", "hit_rate")] == 1 and s["pairs"][("base_rate_only", "likelihood_subtraction")] == 1
    assert len(s["pairs"]) == 15 and all(a < b for a, b in s["pairs"])          # each unordered pair once


def test_report_measures():
    rows = group({1: inc(1, 80, 20, 4), 2: inc("0.5", 60, 10, 3)})
    s = v23.summarise(L(write(rows)))
    assert (s["K"], s["Kx"], s["W"], s["SYM"]) == (2, 1, 0, 1)
    out = v23.report(L(write(rows)))
    assert "produced R = 2" in out and "Q1 (PRIMARY)" in out and out.count("hit_rate/base_rate_only") == 0


def test_refusal_counts_as_zero_produced():
    s = v23.summarise(L(write(group({}))))
    assert (s["R"], s["I"], s["D"]) == (0, 0, 0)


@pytest.mark.parametrize("bad", [
    dict(status="Included", b="10", h="12", f="4", key="25", key_status="scored"),
    dict(status="included", b="0", h="12", f="4", key="25", key_status="scored"),
    dict(status="included", b="10", h="12", f="4", key="nan", key_status="scored"),
    dict(status="included", b="10", h="12", f="4", key="15%", key_status="scored"),
    dict(status="included", b="10", h="12", f="4", key="25", key_status="maybe"),
    dict(status="missing", b="10", h="", f="", key="", key_status=""),
    dict(status="missing", b="", h="", f="", key="", key_status="bogus"),
    dict(status="excluded:", b="", h="", f="", key="", key_status=""),
])
def test_validation_rejects(bad):
    with pytest.raises(SystemExit):
        L(write(group({1: bad})))


def test_malformed_rows_and_roster():
    with pytest.raises(SystemExit):                                   # a row with an extra field
        L(write(group({})[:19], extra_line="X,1,20,missing,,,,,,orphan"))
    with pytest.raises(SystemExit):                                   # a scheduled group is absent
        L(write(group({})), roster=[("X", "1"), ("X", "2")])
    rows = [dict(r, status="unavailable:two technical errors") for r in group({})]
    s = v23.summarise(L(write(rows)))
    assert s["disposition"] == "unavailable:two technical errors" and s["R"] == 0
    rows[0]["status"] = "missing"
    with pytest.raises(SystemExit):                                   # unavailable must cover the whole group
        L(write(rows))


def test_huge_key_does_not_crash():
    out = v23.report(L(write(group({1: inc(10, 12, 4, "1e309")}))))
    assert "outside 0-100: 1" in out


def test_legacy_uses_float_inputs():
    a = v23.legacy_v20(v23.float_predictions(Q(14), Q(80), Q("67.500000001")))
    b = v23.legacy_v20(v23.float_predictions(Q(14), Q(80), Q("67.500000001000002")))
    assert a == b                                                     # same float inputs, same v20 output


def test_duplicate_and_bad_slots():
    rows = group({1: inc(20, 40, 10, 50)}) + [dict(chatbot="X", arm="1", slot="1", **inc(20, 40, 10, 50))]
    with pytest.raises(SystemExit):
        L(write(rows))
    rows = group({}); rows[0]["slot"] = "21"
    with pytest.raises(SystemExit):
        L(write(rows))
    with pytest.raises(SystemExit):
        L(write(group({})[:19]))                        # only 19 slots


def test_exact_inputs_keep_rare_rates():
    pr = v23.predictions(Q("100/2500000"), Q(90), Q(5))  # 1 in 2,500,000 is not rounded to zero
    assert pr["base_rate_only"] == Q(1, 25000)
```

## Appendix C — parity_v20.py

```python
"""Pre-publication check: v23.legacy_v20 must give exactly the same M1 methods and M2 pairs as the registered
v20 code on every v20 item, and the same 21/23 count. Run on the Mac before tagging v23:

  python3 parity_v20.py <tutor repo root> <path to the registered v20.py> <path to items_v20.csv>
Exits non-zero on any disagreement. Prints one line per item.
"""
import hashlib
import importlib.util
import sys
from fractions import Fraction as Q
from pathlib import Path

import v23

# Registered inputs, pinned. ITEMS is the locked v20 item file (addendum v20.1). V20_CODE must be copied from the
# registered record: published plan v22 (tag v22), section 6, lists this hash for v20.py.
ITEMS_SHA256 = "5f337517afcb5e94a3639b9c65d6b492642a34937ec9628f695b32559fdd1236"
V20_CODE_SHA256 = "c71003c8602d912409bc5ea07941d8e93796716c6f607470b8c5436c84232db3"   # as recorded in published plan v22, section 6

root, v20_path, items = Path(sys.argv[1]).resolve(), sys.argv[2], sys.argv[3]
for path, want in ((v20_path, V20_CODE_SHA256), (items, ITEMS_SHA256)):
    got = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    if got != want:
        sys.exit(f"{path}: SHA-256 {got} is not the registered {want}")
spec = importlib.util.spec_from_file_location("v20_registered", v20_path)
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)
V.check_files(root)
sys.path.insert(0, str(root / "src"))
import bayes_strategies as B  # noqa: E402

rows = V.load(items)
bad, unique = 0, {}
for r in rows:
    p = B.Problem(r["base"], r["hit"], r["false_alarm"])
    pr_reg = {m: 100 * v for m, v in B.predictions(p).items()}
    passes, pairs, _ = V.audit(pr_reg, B.CORRECT, list(B.WRONG), V.TOL)
    fp = v23.float_predictions(Q(repr(r["base"])) * 100, Q(repr(r["hit"])) * 100, Q(repr(r["false_alarm"])) * 100)
    assert all(fp[m] == pr_reg[m] for m in fp), f"float values differ from the frozen tutor's on {r['item_id']}"
    m1, m2 = v23.legacy_v20(fp)
    same = (sorted(passes) == m1) and (sorted(tuple(x) for x in pairs) == m2)
    bad += not same
    unique.setdefault((r["base"], r["hit"], r["false_alarm"], r["kind"]), bool(m1 or m2))
    print(f"{'OK ' if same else 'BAD'} {r['source']} {r['item_id']}: registered {passes} {pairs} | v23 {m1} {m2}")
std = [v for k, v in unique.items() if k[3] == "standard"]
print(f"standard unique sets with any collision (v23.legacy_v20): {sum(std)}/{len(std)}  (registered v20: 21/23)")
sys.exit(1 if bad or (sum(std), len(std)) != (21, 23) else 0)
```
