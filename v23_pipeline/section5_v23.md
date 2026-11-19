Copied unchanged from prereg_v23.md (tag v23), section 5.

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
