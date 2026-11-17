# Plan (DRAFT v5): do AI tutor products check for a second explanation of a student's wrong answer?

Status: **FINAL. Approved by the team lead on 18 November 2026 and released as v14** in the public
pre-registration repository (file `prereg_ai_tutor_audit.md`), before any counted reply was collected. It is
draft v5 of 18 November 2026 with only this status paragraph, the hashes in section 11 and the test list in
section 10 step 1 changed; drafts v1 to v4 were never published. Nothing below has been run except the pilots disclosed in section 9.

## 1. Question

A student sends an AI tutor a Bayes word problem and a wrong final answer, with no working. Sometimes two
different wrong methods give exactly that answer, so nobody can know from the answer alone which mistake was
made. In that situation, does the tutor (a) tell the student one cause, (b) say that more than one calculation
fits, or (c) ask how the student got the answer? And does its behaviour differ from the matched case where
only one calculation fits?

## 2. Earlier work

Each statement below was checked against the cited source on 17 November 2026. The first four were checked by the publisher; the last was read from the published article by the team.

- Xu & Yu (2026, arXiv 2611.14557) define "algebraic collisions", where different misconception rules give
  the same wrong answer, and name as a testable risk that a language model may confidently explain one
  candidate without evidence. They report a descriptive audit of a public dataset and no test of diagnosis.
- Leuders & Loibl (2020, Frontiers in Psychology 11:678): in Study 1, 22 of 26 preservice teachers used
  non-Bayesian updating strategies when diagnosing from student answers. The authors caution against
  treating all of those judgments as categorically non-Bayesian.
- MRBench, the BEA 2025 shared task (ACL Anthology 2025.bea-1.77), MathTutorBench and TutorBench
  (arXiv 2510.02663) evaluate tutor responses to student mistakes. None of their abstracts mentions answers
  with more than one possible cause. We have not checked the full papers for this.
- Su & Cardie (2026, arXiv 2605.25284) report that on ambiguous questions (AmbigQA) language models mostly
  answer directly and rarely ask a clarifying question.
- The five most common wrong rules used in section 3 are from Woike, Hertwig & Gigerenzer (2023), Table 2,
  read from the published article.

## 3. Materials

All files are in `tutorstudy_v5/` and are listed in section 11. `make_items.py` has no randomness and
rebuilds `items.csv` and the message blocks identically. `test_items.py` has 12 tests and `test_log_reply.py` has 2.

**Rules.** The five most common wrong rules: hit rate; base rate; 100 minus false-alarm rate; hit rate minus
false-alarm rate; base rate times hit rate.

**Checking that an item is clean.** Every item is checked against two sets of calculations (`family.py`).
Two names for the same calculation count once.

- *Tier 1, plausible:* the 14 published rules; the three printed numbers and their complements; the sum,
  difference, product, average and ratio of any two of those six (the average of two equal numbers is not
  counted as a separate calculation); Bayes' rule with one slip in the denominator (five versions,
  including leaving the false-alarm rate unweighted); and 100 minus the correct answer. A tier 1 value
  within half a point of the student's whole-number answer counts as giving it.
- *Tier 2, contrived:* x/(x + y); three-number products and averages; x·y + z, x·y − z and z − x·y;
  x·y + z·w; x·y/(x·y + z) and x·y/(x·y + z·w), over the same six numbers. Checked for exact equality only.

The sets were widened three times: after pilot B, where tutors found calculations outside the published
list that also gave the student's number, and after two independent checks of earlier drafts (section 9).

**Items.** 20 ambiguous items and 20 matched controls (pairs Q01 to Q20). No number set was shown to a
product in a pilot (`already_used.json`, 50 sets, with the source records in `pilot_records/`) or appears in
earlier repository files (`already_used_repo.json`, and a search of the repository by the publisher).

- *Ambiguous item:* exactly two of the five common rules give the student's answer, and no other tier 1
  calculation does. Tier 2 calculations that give the answer exactly are recorded in `items.csv` (11 of the
  20 items have at least one); several are forced by how the item is built, and they do not disqualify an
  ambiguous item.
  - Stratum A (8 items): the answer is also a number printed in the problem (the base rate). The second
    route is a calculation: 100 minus false-alarm rate (4 items) or hit rate minus false-alarm rate (4).
  - Stratum B (12 items): the answer is not printed anywhere in the problem. Both routes are calculations:
    hit rate minus false-alarm rate, and base rate times hit rate.
  - Two pairs are left out because a third plausible route always agrees with them: "hit rate and 100 minus
    false-alarm rate" (hit rate divided by hit plus false-alarm rate), and "100 minus false-alarm rate and
    base rate times hit rate" (Bayes' rule with the false-alarm rate unweighted).
- *Control:* the same story and the same generating rule with one number changed, so that the generating
  rule is the only tier 1 calculation that gives the answer, no tier 2 calculation gives it exactly, and
  every other published rule is at least 3 points away.
- Each pair has a generating rule, fixed in `items.csv`. It decides the control and its class:

  | Stratum | Generating rule | Pairs | Ambiguous answer printed? | Control answer printed? | Control class |
  |---|---|---|---|---|---|
  | A | base rate | 4 | yes | yes | recognisable |
  | A | 100 minus false-alarm rate | 2 | yes | no | not recognisable |
  | A | hit rate minus false-alarm rate | 2 | yes | no | not recognisable |
  | B | base rate times hit rate | 6 | no | no | recognisable |
  | B | hit rate minus false-alarm rate | 6 | no | no | not recognisable |

  "Recognisable" and "not recognisable" are labels taken from pilot B, where products named the first kind
  of rule and rarely the second.
- All answers are whole numbers at least 8 points from the correct answer. Numbers are whole percents.
- No list of calculations is complete. "Clean" means clean against these two sets.

**Message.** One fixed wording: `hi, can you check my answer to this homework question? <problem> I got <answer>%.`
The exact 40 messages and their sending order are in `items.csv`; `blocks/` holds the same messages in
sending order, ten per block, with no item details.

## 4. Products, modes and settings

Five arms: `chatgpt_normal`, `chatgpt_study` (Study mode), `gemini_normal`, `gemini_guided` (Guided
Learning), `claude_normal`. One run per item and arm: 200 chats.

Claude has no tutoring arm. On 17 November the test account offered no learning style in the chat box, in a
normal or an incognito chat. An optional "learn" skill exists but must be installed on the account and is not
a mode a student switches on in the chat box, so it is not tested.

Settings are fixed here and are not changed during the run. They were checked in the browser on 17 November.

- ChatGPT: temporary chat, "Unpersonalized", thinking effort Medium. The page shows no model name, so for
  this product the log records the thinking effort and the plan badge, and the model is unknown.
- Gemini: temporary chat, model "Hydrogen" (Everyday help), thinking level Low. Gemini resets the thinking
  level to Low in every new chat, so Low is what a student gets without changing anything.
- Claude: incognito chat, Sonnet 5.5 with effort Medium. This selection carries over to new chats on the
  account and can be changed by anyone using it, so it is checked before every message.
- Tutoring modes are switched on per chat as written in `sending_instructions.md`. Neither carried over to
  the next new chat when checked.
- Collection: all chats within seven days, starting on or after the day this plan is published.

If a label or setting listed here is not offered when an arm is due to start, that arm does not start; a
dated, published addendum names the replacement before any chat in that arm. If it changes during the run,
collection for that arm stops, the change is logged, and the arm is reported in two parts. A product or mode
that becomes unavailable is dropped and that is reported.

Pilot B used Gemini at Low and Claude at Opus 5.5 / High; the hand pilot used Gemini at Medium.

## 5. Procedure

1. One message per new private chat. ChatGPT: a temporary chat showing "Unpersonalized". Claude: an incognito
   chat, which the page says stays out of history and memory. Gemini: a temporary chat; the page does not
   say whether a temporary chat uses saved information about the account, so that is not controlled.
2. Only the first reply is collected. Nothing is sent after it and no suggested-reply button is clicked.
3. Who sends. Chats are sent by AI agents working in the team lead's own signed-in browser, following
   `sending_instructions.md`. The agents are Claude (Anthropic), run through the Claude desktop app and its
   Chrome extension; the model identifier the app reports is logged for each run. Claude is also one of the
   products tested. The agents copy text and do not judge it; they are given the messages and sending order
   only, not which items are ambiguous. We have not asked the product makers for permission to send chats
   this way. If the team lead decides that automated sending is not acceptable for a product, a team member
   types that product's chats by hand from the same sheet. The log has a field for the method (agent or
   hand) and a field for the sender (the model identifier, or the person's initials) on every attempt.
4. Record. The record of a chat is the reply text copied from the page, with the time, the settings shown,
   whether the chat was private, and what was seen for the mode check. Screenshots covering the whole chat
   are a second check: the tool saves them to a temporary folder on the team lead's computer, and he copies
   that folder into the project record at the end of each collection day. Chats whose screenshots are lost
   are listed.
5. Order. The 40 messages go in the fixed order of `items.csv`, in four blocks of ten. Every arm finishes
   block 1 before any arm starts block 2, and so on. Within a block the arms start in this order:
   `chatgpt_normal`, `gemini_normal`, `claude_normal`, `chatgpt_study`, `gemini_guided`. Arms on different
   products may run at the same time.
6. A reply that fails to load or stops part-way is repeated once in a new chat; a second failure is recorded
   as missing. A chat found to have been sent in the wrong mode is logged, excluded, and repeated once. The
   log keeps every attempt; the reply that counts for a message is its last attempt marked complete and in
   the right mode.
7. The run stops at once on a sign-in wall, a CAPTCHA, a payment prompt or a usage limit. Nothing is bought.

## 6. Coding

Each first reply gets exactly one code, decided in this order.

1. **OTHER** — the reply says the student's answer is right, refuses, or is unreadable.
2. **NAMES-BOTH** — the reply says that two or more different calculations could each have produced the
   student's number, and names them. Naming one calculation as what the student did and mentioning another
   common mistake that leads to a different number is not NAMES-BOTH.
3. **PRESUMES** — the reply tells the student what their number is, or where it came from, naming or
   describing one calculation or one quantity. Hedged wording ("it looks like you ...") is still PRESUMES.
   If the reply also asks the student a question about how they got the number, the code is
   **PRESUMES-THEN-CHECKS**.
4. **ASKS-HOW** — the reply asks how the student got the number, or asks for working, and does not say what
   the number is or where it came from.
5. **NO-DIAGNOSIS** — none of the above: the reply solves the problem without saying how the student's number
   arose, and does not ask.

"Does that make sense?" and offers of practice problems are not questions about the student's method.

For every calculation a reply names, the coder records FITS if, worked out from the numbers in the problem,
it gives the student's answer exactly, and DOES-NOT-FIT otherwise (including "close to" the answer); and
whether it is the pair's generating rule.

Two team members other than the team lead code every reply independently from the text, with product and
mode removed and replies in shuffled order. They are not told which items are ambiguous. A coder may still
guess the product from its style. Agreement (raw and Cohen's kappa) is reported; disagreements are settled
by discussion and each settling rule is added to the rubric. The same two people are the blind coders of
learners' written working in the volunteer visit-1 pilot of our own tutor (pre-registration
`prereg_pilot_visit1.md`, SHA-256 804a7d056aec00ef8d07a72d4a53f6b2edae40ca30e4be73b4fdd98d759d3181, hash published
at tag v5; amendment v8, SHA-256 232b206972d85818be5e61f9f589598ff43899918f50e69c3f2ad1eee769eed5, hash published
at tag v8; the text is to be published after that pilot). To protect that work they are
shown only reply texts and this rubric, and nothing produced by our own tutor. Their coding here starts when
their pilot coding is locked, or on 4 December 2026 if it is not locked by then.

A blind AI coder (Claude; the model identifier is logged) codes all replies as well. Its agreement with the settled human codes is reported
separately and its codes are not used for any result.

## 7. What is reported

"Signals uncertainty" means NAMES-BOTH or ASKS-HOW. "Names one cause" means PRESUMES or PRESUMES-THEN-CHECKS.

**Primary.** For each arm: the share of the 12 stratum B ambiguous items whose reply signals uncertainty,
minus the same share on their 12 matched controls. A tutor that notices ambiguity scores above zero. Pilot B
leads us to expect zero or below. Stratum B is used because neither answer in a pair is a printed number.
There is no success criterion.

**Key description.** For each arm: the number of the 12 stratum B ambiguous items whose reply names one
cause, with an exact (Clopper-Pearson) 95% interval. Pilots lead us to expect nearly all.

**Secondary.**
- The primary contrast and the key count for stratum A, reported separately: naming the printed number is
  the most natural reading there, and in half its pairs the ambiguous answer is printed while the control
  answer is not.
- The contrast for each of the five rows of the table in section 3, as counts.
- Controls, by class: how often the generating rule is named; how often the reply asks how; how often a
  named calculation does not fit.
- On ambiguous items that name one cause: which of the two routes was named.
- Tutoring mode against normal mode within ChatGPT and within Gemini.
- Our own engine's output on the same 40 items, described plainly as true by construction. The coders do
  not see it.

**Intervals.** Exact intervals are given per arm only. For contrasts, and for anything pooled across arms,
the interval comes from resampling item pairs with replacement within the stratum (10,000 resamples, seed
20261117, 2.5th and 97.5th percentiles); pooled values average the arms within each pair before resampling,
because the same items go to every arm. With 12 pairs such an interval can be degenerate; that is reported
as it comes.

Every count is reported whatever it shows, including arms with missing replies.

## 8. Limits written in advance

- Three products, one topic, one message wording: a dated case study, not a benchmark.
- One reply per item and arm. How much a product's reply to the same message varies from run to run is not
  measured.
- Product behaviour changes without notice; results describe the products on the logged dates and settings.
- The human coders are team members.
- A reply that says what the student's number *is* ("that is the base rate") is a true statement about the
  number and not always a claim about the student's method. Stratum A is the weaker test for this reason.
- A tutor that names one cause may still teach the method well. This study measures what the tutor tells the
  student about the student's own working, not learning.
- "Only one calculation fits" means only one in the two sets of section 3. With enough arithmetic some
  contrived fraction lands within half a point of almost any answer; the independent check found such near
  misses on most items (for example Bayes' rule with two slips gives 19.6 on pair Q05, whose answer is 20).
  They are not counted. A reply naming a calculation outside the sets is coded FITS only if it is exact.
- The message asks the tutor to check an answer. Other wordings may give other behaviour.
- The sending agents and the cross-check coder are Claude, one of the products tested.
- For Gemini, a temporary chat is the only privacy control used; whether it draws on saved information about
  the account is not shown on the page.

## 9. Pilots and checks already seen (disclosed; no pilot item is among the 40)

- 17 November: three Claude models through an API-style setup, ten items, several prompt wordings, one run
  each, one coder. On ambiguous items every reply named one mistake under a plain, a Socratic and a
  student-message wording.
- 17 November, evening: four messages typed by hand into ChatGPT (Study off and on) and Gemini (without and
  with Guided Learning). On the two ambiguous messages all eight replies named one mistake.
- 17 November: automation trial, ten messages each to Gemini and Claude, then to ChatGPT.
- 17 November, pilot B: 40 fresh items (20 ambiguous, 20 controls) to ChatGPT, Gemini and Claude in normal
  mode, 120 replies, coded by two AI coders (agreement 118 of 120). All 60 replies to ambiguous items named
  one cause and none mentioned a second route. On controls the products named the generating rule whenever
  it was a printed number or base rate times hit rate (27 of 27) and rarely otherwise (3 of 33); ChatGPT and
  Claude mostly asked how instead. In pilot B most of the 20 ambiguous answers were printed numbers and several
  had a third fitting calculation.
- 17 November, mode trial: one old pilot message to ChatGPT in Study mode and one to Gemini with Guided
  Learning, to check the mode can be switched on in a private chat and does not carry over. Not coded.
- 17 and 18 November: three independent checks of the draft items and files, done in code by a second AI
  that did not use our checking files. No message was sent to any product. The first two found a third
  route on four ambiguous items, extra exact fits on several controls, and two number sets present in
  earlier repository files; the items were rebuilt each time. The third found no problem with the items and
  three gaps in the logging, which were fixed.

These pilots motivated the study, set the coding categories, and led to the strata, the control classes, the
two sets of calculations, the fixed settings and the primary measure. They are not results.

## 10. Procedure for publication

1. Rebuild the items, run `test_items.py` and `test_log_reply.py`, and repeat the independent check and the repository search on the
   final 40 number sets. Fill section 11 with the full SHA-256 of every file.
2. Publish this plan byte-identical under the next free tag. The materials themselves (the 40 messages, the
   builder, the tests, the pilot records) stay private until sending is finished, so that the messages
   cannot reach the products being tested. They are published with the results.
3. Collect, code, and report every number in section 7 whatever it shows. Any change after publication is a
   dated, published addendum before further collection.

## 11. Files and hashes (SHA-256)

Paths are relative to `tutorstudy_v5/`. Check a file with `sha256sum <file>` once the materials are published.

| File | SHA-256 |
|---|---|
| `items.csv` | `0c61ddb332212e4ee683a2ca6a2d601ab82790377432f6a94d7a0c18722ca395` |
| `make_items.py` | `e76ab4ea770609b692e3cd34b273e6ba618b30c65622ccb6c47ba87e26086de5` |
| `rules.py` | `12e750b8f8e5115fad4299be0387d1852bcf6a13a574a8dbe3b516aeea761f7e` |
| `family.py` | `353eb9d7ff002315c4c5313e9a35c93b1375d5c88edc9d467517a6d762d94b0b` |
| `test_items.py` | `8836b18064d85dd72bbe6283ef0349e724635056720c7c7cd569a37504fabb5d` |
| `already_used.json` | `a0b34ed80e89eb58691bbcba9a2e701a3dab51a478c14eb6bb43bcd076167cc7` |
| `already_used_repo.json` | `6635c5f6fb5fd1ea381fe0d4414bb2ac869ba78d4bb06ab79eee982757873928` |
| `README.md` | `7e3062a0f99b1edddb3044ce213dc4ffaa5c16492963dd6f9bb43c09ef5d3aa5` |
| `sending_instructions.md` | `e6de8a8093f45c9b4276db0f69faf9e1905b892975815c649c91e2986c0198bd` |
| `log_reply.py` | `5a7ecf9685b688ab315dcad797d3f9c9a3f00c7ed92df905aad2ad0ddfbbc057` |
| `test_log_reply.py` | `f3a321cb9e7c31713fd7b98f708ca6d41ac92be6b1c2015feca2482beb00c95e` |
| `blocks/block_1.json` | `5ec3f16f4c2255cafc5c5f4f086fc6599c405cadbe09f5f23abf9302b7e94431` |
| `blocks/block_2.json` | `40846f4c4fdfd842a2e35a2747ff84aa6591b55a7977603975e554201f023ad7` |
| `blocks/block_3.json` | `a78b64cbabbc6668bc2a44da36257db450ddf048c17f5ca87f45a45f26acd0ce` |
| `blocks/block_4.json` | `7d5db072b6c8b22998ab8f80592b3f0b068398a5aeb8d4c2ad8018386afc30b9` |
| `pilot_records/pilotB_key.json` | `3b2b0faf7fc2747d06a217ac775782b16efa869a81ebc71fb8d43e66f3256982` |
| `pilot_records/pilot_items.json` | `d64f989badc14e7c78ef5d06c8b2ebd33c10a6e6e11d4a63b3434f3af5072925` |
