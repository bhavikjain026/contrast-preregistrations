# Addendum v39.1 to plan v39: the battery that counts, its intake, and three departures from the plan

Written on 22 November 2026. To be published under tag v39.1 **before** `v39_run.py` is run. Plan v39 (tag v39) is unchanged. No sealed file has changed. Nobody has run the wrapper, the harness or the tutor on this battery.

This is a benchmark on scripted, made-up learners. There are no people and no participant data.

## 1. The battery that counts

| File | Bytes | SHA-256 |
|---|---:|---|
| `battery_v39_confirm.py` | 31,961 | `ef7ae20fce439d682df5acf4c212d601e89bd27ebc006e2534ed2d76338299ed` |
| `battery_v39_confirm_truth.json` | 38,344 | `ead82a8ac7b485dc1df1c0f59180e9fe650abfec80bef77b32e047d81b89b2f6` |

Both hashes equal the ones the battery's author reported in its own reply.

The battery was written after tag v39 was public. That tag was pushed at 08:13:41 UTC on 22 November 2026.

## 2. Intake

`v39_intake.py` (the sealed version, hash in plan section 3) was run on the folder once, by the author of the rules, with Python 3.10.12 on Linux. This is everything it printed:

```
sha256 battery_v39_confirm.py         ef7ae20fce439d682df5acf4c212d601e89bd27ebc006e2534ed2d76338299ed bytes 31961
sha256 battery_v39_confirm_truth.json ead82a8ac7b485dc1df1c0f59180e9fe650abfec80bef77b32e047d81b89b2f6 bytes 38344
modules imported: ['math', 'random'] | outside the allowed list: [] | banned names used: []
self-test: exit status 0 | last line is 'shapes OK': True
learners: 61 | all are classes: True | names all different: True | every learner has the six methods: True | one well-formed truth record per learner: True
INTAKE PASSED
```

Intake is run again on the machine that makes the run, just before the run. Its output must equal the block above, or the run is not started.

## 3. Departures from plan v39

Plan section 5 was not followed in three ways. Each is stated here before the run.

**3.1 Three AIs were asked, where the plan says one.** The team lead gave the sealed prompt to three outside AIs. He then had to choose which reply is the battery.

- The battery in section 1 is the one he chose. His ground does not depend on what the learners are: it was the first reply, or the only one, to arrive as the two files with their hashes, which is what the sealed prompt asks for.
- He chose before intake was run, and before anyone had run the wrapper on any of the three.
- The author of the rules recommended this choice, and had already read this battery when recommending it (see 3.2).
- The other two replies do not count. They are not run under plan v39, and nothing from them will be reported as its result. The author of the rules has not opened them and will not open them before the run. As pasted, their SHA-256 values are `1d9cf9ca92d04a6cf287b0d8a096bd840120143a2d20a4aeda60671509830b54` (73,319 bytes) and `fcdd8361743c1632e911d94bfbb8b9da3fe9d96426010e6599223623776bcacf` (101,301 bytes).

**3.2 The battery was pasted into the chat with the author of the rules.** The plan says the two files are saved straight into a folder and are not pasted into any such chat. All three replies were pasted there.

- The author of the rules has read the battery that counts in full, with its truth file, before the run.
- The team lead received the author's covering reply, which describes some of the learners, and passed it on.
- So the promise that nobody reads the learners before the run was not kept.

**3.3 The files were not saved straight into the folder.** They were recovered from the pasted text and then saved. The recovered files are byte-for-byte what the battery's author wrote, as far as the hashes can show: both equal the hashes in its reply.

## 4. What this changes and what it does not

- **The rules could not be fitted to this battery.** The spec, the wrapper, the harness, the intake check and the four tutor files were fixed by hash in tag v39 before the battery existed. `v39_run.py` checks all eight before it loads anything and stops if one differs.
- **The choice among three replies is a real weakness.** A reader has only our word for the ground in 3.1. The two hashes there let anyone check later that the other replies were not swapped.
- **One allowance in the plan is now weaker.** Plan section 6 lets us fix a fault in our own code after a stop, as a disclosed deviation. Such a fix would now be written by someone who has read the battery. So it is narrowed: a fix may only make the code do what the sealed spec already says, the spec itself is not changed, the second reader checks the fix against the spec before new hashes are published, and the report says the fix was made after the battery was read.
- **The forecast is not renewed.** Plan section 9 was written before the battery existed and stands as written. The author of the rules has since read the battery. No new forecast is made, and nothing the author says about this battery before the run counts as one.
- **Freshness of the chat.** The battery's author stated in its reply that it had seen none of the material listed in plan section 5 before its session. The team lead confirms that the chat was a fresh one. We cannot show this independently.
- The report will name the AI that wrote the battery and say whether it is of the same model family as the author of the rules.

## 5. The run

One command, once, as in plan section 6:

`python3 -B v39_run.py <battery folder> ef7ae20fce439d682df5acf4c212d601e89bd27ebc006e2534ed2d76338299ed ead82a8ac7b485dc1df1c0f59180e9fe650abfec80bef77b32e047d81b89b2f6 --run-after-tag`

The stop rule of plan section 8 applies unchanged. There is one attempt. The result is reported whatever it shows, with this addendum's departures listed again.
