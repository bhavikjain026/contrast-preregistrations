Copied unchanged from prereg_v23.md (tag v23), section 5, step 1.

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
