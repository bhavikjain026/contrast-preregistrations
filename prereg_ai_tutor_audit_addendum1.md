# Addendum 1 to plan v14

Published as tag v14.1 on 19 November 2026, after collection and before any human coding. Written 18 November 2026;
revised 19 November 2026, after an independent check of the draft and the analysis script found one error in the
script and seven unclear points (sections 1, 4, 5, 6 and 7).

## 1. Collection, as it happened
- All 200 chats were sent on 18 November 2026 between 19:10 and 22:11 IST by AI agents (model identifier claude-opus-5-5,
  method "agent") in the team lead's browser, following sending_instructions.md. No chat was typed by hand.
- Counted replies: 198 of 200. Missing (failed twice, as section 5 step 6 says): gemini_normal messages 23 and 26.
  Two further messages (gemini_guided 34 and 37) failed once and were counted on the second attempt.
- Before collection the ChatGPT product switcher read "Codex"; it was set to "ChatGPT" at the team lead's request.
  Every ChatGPT chat then showed Temporary chat, Unpersonalized, Medium and Plus.
- Claude's page footer showed "Auto". This is the app's tool-permission mode, not a model setting; the model label was
  Sonnet 5.5 with effort Medium in every Claude chat.
- Gemini's Guided learning was found under "+ > More tools > Guided learning", not directly under "Upload & tools".
  The mode was confirmed by the "Learn" chip, as planned.
- In one log (gemini_guided block 1) a sending agent edited the notes field of one entry once, to replace a
  placeholder with a character count. No reply text or status was changed.
- Order (deviation from section 5 step 5). Every arm finished block K before any arm started block K+1, and each
  tutoring-mode arm started after its product's normal arm had finished, as planned. The three normal-mode arms
  ran at the same time, which section 5 allows for different products, but they did not start in the planned order
  (chatgpt_normal, gemini_normal, claude_normal): in every block claude_normal's first reply was logged first,
  25, 30, 58 and 39 seconds before chatgpt_normal's in blocks 1 to 4. gemini_normal's first reply was logged after
  chatgpt_normal's in every block. Times are the logged times of first replies, not of sending.
- Reply text was copied from the page's text. For ChatGPT, rendered maths often copies with a few dozen characters
  fewer than the page element holds; each gap is logged. Screenshots (988 files) back up every reply.

## 2. One change to how coding is recorded
Section 6 says the coder records, for every named calculation, whether it is the pair's generating rule. To avoid
telling the coders how each item was built, the coders do not record that. Instead each coder picks each named
calculation from a fixed list (hit rate; base rate; 100 minus false-alarm rate; hit rate minus false-alarm rate; base rate
times hit rate; hit rate / (hit rate + false-alarm rate); false-alarm rate; the correct Bayes answer; other, described in
Notes) and marks it FITS or DOES-NOT-FIT. The sheet has three slots for calculations. If a reply names more than
three, the coder fills the three slots and lists the rest in Notes; the analysis reads the three slots only.
Whether a named calculation is the generating rule (and, on ambiguous items, which of the two routes it is) is then
filled in mechanically by the analysis script, which the team lead runs, from the coder's list choice and items.csv,
with no further judgement by anyone. A calculation coded "other" never counts as the generating rule or a route.
Nothing else about coding changes.

## 3. Coding packet
Each coder receives one workbook with the rubric of section 6 copied word for word and all 198 replies, each with a
random ID, the student's message and the reply, and nothing else, in an order shuffled separately for each coder
(seed 20261118). The key linking IDs to arms is held by the team lead only. On 19 November two lines of the sheets'
Read-me were reworded to match section 2 (who fills in the generating rule; what to do with more than three
calculations) and the sheets were rebuilt from the same seed; the IDs, the orders, the key and every cell of the
Coding tab are unchanged. Neither coder had received a sheet before then.

## 4. The blind AI coder was run before the human coders (disclosed)
On 18 November 2026, at the team lead's request and before either human coder started, the blind AI coder of section 6
(model identifier claude-opus-5-5, four separate runs of about 50 replies each) coded all 198 replies from the rubric,
the student's message and the reply only. This went against our own brief for that coder (ai_coder_brief.md, which
says "Run only after BOTH human coders have handed in their sheets"); plan section 6 itself does not say when it runs.
The section 7 tables were computed on these codes with version 1 of analyse_v14.py (SHA-256
622e6228f8b3bb8a67f2311b63b6e0f5a1ce457c912812794a7ba93ce560a0bf, written and fingerprinted before any code existed).
The file of version 1 was not kept; only its hash was recorded. The team lead has seen those tables. One exact interval in
them had a wrong upper end, because of the error described in section 5. As section 6
says, the AI codes are not used for any result; the registered result is the analysis script run once on the settled
human codes. The AI codes give free-text calculations, not list choices, so no generating-rule or route table has
been computed on them. The human coders have not been told the AI codes or the tables, and will not be until they
have handed in their sheets.

## 5. Missing replies, and the analysis script
**Missing replies (decided after the AI preview, before any human code).** The plan does not say how a pair with a
missing reply enters a contrast. The two missing replies are gemini_normal Q04-A (stratum A, ambiguous) and Q13-K
(stratum B, control). Rule: a pair enters an arm's contrast only if both of its replies exist in that arm; for pooled
values, each pair is averaged over the arms in which it is complete. So the gemini_normal primary contrast uses 11 of
12 pairs. The key count (replies naming one cause on ambiguous items) uses every available ambiguous reply, with its
own denominator. The contrast computed from all available replies is reported beside it as a sensitivity check. On
the AI preview codes the two ways give the same values.

**Version 2** (SHA-256 2fdd35a6edb345177a8a12d95306c9109a50ef0057e842777a321aa18cd8355b, 18 November) added the
missing-reply rule and the generating-rule column of section 2. An independent check on 19 November found that it
computed the upper end of the exact (Clopper-Pearson) interval as the 97.5th percentile of Beta(k, n - k) instead of
Beta(k + 1, n - k). The lower end, and the interval when k = n, were right. Version 2 was never run on human codes.

**Version 3** (19 November) is the version that will be run. It
- fixes the upper end of the exact interval;
- adds the section 7 secondaries that version 2 did not compute. Controls, by class (recognisable, not recognisable;
  per arm and all arms, as counts): the generating rule is named; the code is ASKS-HOW; the code is
  PRESUMES-THEN-CHECKS (section 7's "how often the reply asks how" is reported both ways); at least one named
  calculation is marked DOES-NOT-FIT. On ambiguous items whose reply names one cause (per arm and stratum, as counts):
  the generating rule only, the other route only, both, or neither of the two routes was named;
- reads the codes file written by sheet_to_codes.py, which copies a sheet's choices without judgement and refuses a
  sheet that breaks its rules (a missing code, a calculation not on the list, a calculation without a Fits entry, or
  other than 198 rows);
- does not compute our own engine's output on the 40 items (section 7). That is produced separately by the frozen
  engine and reported as description, true by construction.

Version 3 and the converter were tested on made-up codes only (test_analyse_v14.py, 30 checks, including published
Clopper-Pearson values). Version 3 has not been run on the AI codes, and its new tables have not been seen on any
real codes. These files will not be changed before the human codes are run. If an error is found, the fix will be
a further dated addendum, published before the run.

## 6. When human coding starts
Section 6 says the human coding of these replies starts when the coders' pilot coding is locked, or on 4 December
2026 if it is not locked by then. On 19 November only P01 visit 1 is locked for both coders; P06, P07 and P08 have
not been coded. The sheets are therefore sent to the coders only when both coders' visit-1 pilot coding is locked,
or on 4 December 2026, whichever comes first. The date each sheet is sent is recorded.

## 7. Who has seen what, and release
- Team lead: has seen the AI coder's tables (section 4), one reply in a screenshot during collection, and the logs.
  The lead will not train the human coders on examples from these replies, will not take part in settling their
  disagreements, and will not change the analysis files before the human codes are run (except as section 5 says).
- Human coders: see only the rubric, the fixed list and the 198 replies with random IDs.
- Every original file is kept: each coder's sheet as handed in, the settled codes, and the AI codes, with SHA-256 and dates.
- Release. Plan section 10 says the 40 messages, the builder, the tests and the pilot records are published with
  the results. With the results we will publish those, and also the coding sheets as sent, every set of codes
  (each coder's, the settled codes and the AI codes), the key linking IDs to arms, the analysis script, the
  converter, the tests and the counts. Section 10 does not list the reply texts. They, the screenshots, and the
  products' replies from the pilots of section 9 (which are not in the pilot records; those hold item details and
  student messages only) are published only after the products' terms for reuse of outputs have been checked,
  account details, links and personal information have been removed, and each product maker has been sent a short
  factual notice.

## 8. Files (SHA-256)
- analyse_v14.py, version 3: 1ae10bdfcd67319cf6cc6f4a9346a54e10e86e9ffdb37fe3c9f6f67e36ccd88d
- sheet_to_codes.py: 900f96e04ee59f35829dce805efadc74b41cd1bfe96a529fb1dd50599152e0f2
- test_analyse_v14.py: f8d2ba09c344fb4c68b5ec99043d3bf035a9b2a4c9ad561d8d76d74d9def4cfb
- build_packet.py (19 November): a5b4c7a25ccd3eb0c5fcd03e2cacee0aee8f5790a97047baf4a586b0b7e9adee
- coding_sheet_coder_A.xlsx, as it will be sent: 585d267e8b5edfa914e73cb7b243bb6b472f9802739ea33c95fab189bba6d500
- coding_sheet_coder_B.xlsx, as it will be sent: 5a29e9045acafbda63b239f536c022f196676cd66fa3fd227d703ba2c34f4e0d
- KEY_lead_only.csv (held privately until release): 784371443a21b4e22e40484b487c9deddfe7772a6546930a82fa28b97388c1a2
- AI codes (ai_codes_all.json): 7de9230d940c32b993837df3eb883a7f988db6d6e953f057fa5cd85992f933cb
- ai_coder_brief.md: 230cfd942655eaa31dd9b856f056ff728191cacb9515df483f8dd099d3387287
