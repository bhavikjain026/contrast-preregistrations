# Addendum 2 to plan v14

Published as tag v14.2 on 22 November 2026. Written 22 November 2026, before either human coder has received a coding
sheet and before any human code of these replies exists. It changes when one coder's sheet is sent and adds one interim
description. It changes no code, rubric, item, sheet, script or registered number.

## 1. Why
Plan section 6 says that two team members other than the team lead code the replies. They are Kahan Dadbhawala and
Jay Singh. Jay cannot code before 4 December 2026 because of his
university examinations. Kahan has finished his visit-1 pilot coding (section 2). Under addendum v14.1, section 6, neither
sheet could be sent until Jay's pilot coding was also locked, or until 4 December. This addendum lets Kahan start now and lets the team lead prepare the analysis on
his codes while Jay's are awaited. The registered result is unchanged (section 4).

## 2. When each sheet is sent (replaces addendum v14.1, section 6)
- Plan section 6 says a coder's coding here starts "when their pilot coding is locked, or on 4 December 2026 if it is not
  locked by then". Addendum v14.1 read this as both coders together. From now it is read for each coder separately:
  **each coder's sheet is sent when that coder's visit-1 pilot coding is locked, or on 4 December 2026, whichever comes first.**
- **Kahan's visit-1 pilot coding is locked as of 22 November 2026.** He has coded all four visit-1 packets he was sent
  (P01, P06, P07 and P08). Those packets, as he returned them, are fixed by the SHA-256 in section 6. His pilot codes are
  not changed after he receives his sheet. Any change would be a dated entry in the pilot's coding log and would be
  reported with the pilot.
- **Kahan receives `coding_sheet_coder_A.xlsx`; Jay receives `coding_sheet_coder_B.xlsx`**, both exactly as fixed in
  addendum v14.1, section 8. Kahan's sheet is sent after this addendum is public. Jay's is sent when his visit-1 pilot
  coding is locked, or on 4 December 2026, whichever comes first.
- The date each sheet is sent and handed in is recorded.

## 3. Who may see what (adds to addendum v14.1, section 7)
- **Jay** sees nothing from Kahan's sheet (codes, notes or calculations), nor the interim output of section 4, nor anything
  computed from them, until Jay has handed in his own sheet.
- **Kahan** does not see the interim output until the disagreements between his codes and Jay's are settled.
- The two coders are asked not to discuss these replies or their codes with each other until both have handed in.
- Disagreements are settled by discussion between the two coders, as plan section 6 says. The team lead takes no part
  (addendum v14.1, section 7).
- **The team lead will see the interim output** before the codes are settled. This is disclosed here. The team lead
  already takes no part in settling and changes no analysis file before the registered run.

## 4. The interim description from one coder (new; not a registered result)
- When Kahan hands in his sheet, the team lead records its SHA-256 and the date. `run_v14_interim.py` (section 6) then:
  checks every fixed input against its published hash; converts the sheet with `sheet_to_codes.py`, unchanged; runs
  `analyse_v14.py` version 3, unchanged, once, with the label "INTERIM: one coder (Kahan, sheet A), codes not settled";
  and saves the output with its hash and an attempts log.
- If `sheet_to_codes.py` refuses the sheet because it breaks the sheet's own rules (addendum v14.1, section 5), nothing is
  analysed. The converter's error messages go back to Kahan. Each names the rule broken. Those about one row give the
  row, its reply ID and what is in it; one checks that there are 198 coded rows, and one that the header row is
  unchanged. None holds reply text. He corrects the sheet, and the corrected sheet is the one handed in. Both versions
  are kept with their hashes.
- If the analysis script fails for any other reason, the error is recorded and a dated addendum comes before any second run.
- **What the interim output is:** the plan section 7 tables computed on one coder's unsettled codes. It has no agreement
  figure, because agreement (raw and Cohen's kappa) needs both coders. It can differ from the registered result.
- **What it is not used for:** it is not the registered result. It is not quoted in any slide, talk, page or message, and
  no wording about the audit is chosen from it. Our own rule for the stage wording (section 5) already says no number
  is said before the registered run.
- **Release:** the interim output stays private until Jay has handed in his sheet and the disagreements are settled. It
  is then published with the registered report, beside the registered result, whatever either shows, with the
  differences between them stated.
- **The registered result is unchanged:** `analyse_v14.py` version 3 run once on the settled codes of both coders
  (addendum v14.1, sections 4 and 5), with agreement reported as plan section 6 says.

## 5. Fixed before the interim run
- On 20 November 2026, before any human code existed, the team wrote down the rule that picks how the audit's result is
  described on stage, and the wording for each outcome. That file is fixed now by its SHA-256 (section 6), unchanged
  since 20 November. It is kept private until both coders have handed in their sheets, because it describes how the
  items were built, which the coders are not told. It is published with the registered report.

## 6. Files (SHA-256)
New:
- `run_v14_interim.py`: f4a0f482d51bca5e6b8d4c693f25a24c431dba8f2730cd81f6a507c8d0235b51
- `test_run_v14_interim.py` (13 checks, made-up codes only): fd9d76c43589ed012ed6850d3dea1134059f2be62bec2e2cadef0ec35fd4537f
- Stage wording file (`v14_endings_DRAFT.md`, 20 November 2026, private until both sheets are handed in):
  f4783b3a4b529cee33c79df92c52c9562d5d1b860a0d32e3422763bd943cf2dd

Kahan's visit-1 pilot packets, as returned (private: they hold volunteers' working):
- `pilot_P01_visit1_packet_kahan.xlsx`: 6fac09e337e6e62dd159be249cedc3f595a57efd5ea921119264e267776762a2
- `pilot_P06_visit1_packet_kahan.xlsx`: a06bbf8d5cf17d554955ce3a12066b3c88900f15cc2c02dba66c3c98f71e9873
- `pilot_P07_visit1_packet_kahan.xlsx`: 09272c5fc2a2c79b2046cd517078430798f6d3b608bb94c932e81085f8b55fa1
- `pilot_P08_visit1_packet_kahan.xlsx`: 87e385a8915d9d86ae702b1a5a1469eaf7a19a02e6f21fd5ae2cdde7f58d5d64

Unchanged, as in addendum v14.1, section 8, and plan section 11: `analyse_v14.py` version 3 (1ae10bdf...),
`sheet_to_codes.py` (900f96e0...), `test_analyse_v14.py` (f8d2ba09...), `coding_sheet_coder_A.xlsx` (585d267e...),
`coding_sheet_coder_B.xlsx` (5a29e904...), `KEY_lead_only.csv` (78437144...) and `items.csv` (0c61ddb3...).
Before it runs, `run_v14_interim.py` checks the full hashes of the five of these it uses: `analyse_v14.py`,
`sheet_to_codes.py`, `KEY_lead_only.csv`, the blank `coding_sheet_coder_A.xlsx` and `items.csv`.

## 7. Disclosed
- This addendum was written after the team lead had seen the AI coder's tables (addendum v14.1, section 4). It changes
  only the timing of one sheet and adds a description that cannot change the registered result.
- Kahan codes these replies up to about two weeks before Jay. The two coders therefore code at different times.
- The interim script and this addendum were written by an AI assistant working for the team. The script was tested on
  made-up codes only.
