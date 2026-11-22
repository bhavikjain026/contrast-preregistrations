# Plan v39: does an added checking layer put labels that do not hold on scripted learners it has never seen?

**Status:** final text, written on 22 November 2026, for release as tag v39 in the public pre-registration repository. It is published before the battery that counts exists.

**What kind of analysis this is:** a benchmark on scripted, made-up learners written by an outside AI. There are no people and no participant data. There is one run, with a stop rule fixed here. A pass or a fail says nothing about human learners.

## 1. Question

Our tutor for Bayes word problems is frozen. It reads one or two typed answers and says "correct", names one of six wrong rules, or says it cannot tell.

We have written a layer that sits around it, called the wrapper here. The wrapper never changes the tutor's verdict. In a session it either adds a label about the learner or holds back and adds none.

On a battery of scripted learners written by someone who has never seen the wrapper's rules:

- does every label the wrapper gives hold for the learner who received it?
- in the sessions of learners for whom a true label exists, does at least half end in a label that holds?

The same counts are printed for the frozen tutor alone, as context.

## 2. Why the rules are sealed

The battery has to be written by someone who cannot read the rules. So the wrapper's rules, its code and the prompt for the battery are fixed here by their SHA-256 and are not published yet. They are published with the report, and anyone can then check them against the hashes below.

This plan describes the scoring and the stop rule in general words. The exact definitions are in the sealed spec.

## 3. What is fixed, by hash

| File | SHA-256 |
|---|---|
| `wrapper_spec_v39.md`, the rules, the session steps, the scoring and the stop rule | `60d320e8b8bef70f88de0aa413fc332790a72f9c681d6aeb74ca0b106591cd12` |
| `wrapper_v39.py`, the rules as code | `6f7a052b4f4ee5d045ee474fca62cea67fe051d5c65259e7a70c3cbc14ab0d65` |
| `harness_v39.py`, which runs a battery and scores it | `dfa78fd5e7cb8909def497f5a4caa77607a17bd26040f42f4ab1b9f076b83ce3` |
| `v39_run.py`, the single run | `b252823fe04554be6df5b16b878c484823296c4be28e40f7051e5c10d950e280` |
| `v39_intake.py`, the check of a battery's files | `18c43d22caa767371758da6e9dd5980ac31fe603128981f29b294941b9cd23a0` |
| `test_wrapper_v39.py`, 15 tests on made-up learners | `316c1410c03833730af86ad11f04ce7db010048fe52fbd700fbb6027b38be610` |
| `v39_battery_prompt_confirm.txt`, the prompt for the battery that counts | `bfb93204bcee633b28bed8e52eceb6e39877018ca611463b7cb40b2675b52aba` |
| `v39_stop_rule_prompt.txt`, the page given to the two reviewers of the stop rule | `eee29616849c0d8275ca9b0e6b219b8198b4755e7500ded8f44ad26675e53362` |
| `stop_rule_decision_2026-11-22.md`, their two answers | `9222a84a03f67622b311a6fea46caa6d6c366688dfbd47cee351b6e0476cff2a` |

The frozen tutor, in our private repository at commit `a7361004c5b32cd268936254d8a92e175e0f686f`, with no change under `src/`:

| File | SHA-256 |
|---|---|
| `src/tutor.py` | `73f4374a50dcc49c8732ed85ad484f32eedce7efddf0c48818812f7f8740ba0c` |
| `src/score_quiz.py` | `80f3b2bcc52c4492243c39b1ee1dabdafb42dfa0ea3af317f6e66a7ee84b97b3` |
| `src/bayes_strategies.py` | `4d43af92ecb0e3bf8f74be1a213340010d92372762337f22a425817c3ac6b96e` |
| `src/screening_quiz.py` | `a86c27da98dea87c310575c813378012f3c7e0934cd6c45c31b329c01df96a10` |

`v39_run.py` checks the spec, the wrapper, the harness, the intake check and these four before it loads anything.

The practice set (section 4):

| File | SHA-256 |
|---|---|
| practice battery 1, code | `9051da5075605b04d327fb14c1a737b8cda3f6c741b60ac5be174642cf1fa979` |
| practice battery 1, truth file | `9dcd2606adf40745fc1210149af83168d2918eb1cf409ea31423d65b8434e383` |
| practice battery 2, code | `e14aa009472c5a91465a3c4421002181b99bc9f6e829f5b1f693a7e75533f944` |
| practice battery 2, truth file | `ddeaf4facec03c7557027f97c88157990f4e43e4c1889f09b2163d4afe4fa831` |
| practice battery 3, code | `1cc40797d9592af3d5c8cff84a02b76dde3002eb09a0954cd100e59ec63584e2` |
| practice battery 3, truth file | `2228dc0f0c3d890dc51c1655a96d01845579b688c9a6b081510be3ca3deaf3b2` |
| practice output 1 | `0daee521d2e8066467bfbcd6f5127f129f73bfe8d948a34ef7bf85ed96ef97b7` |
| practice output 2 | `e783bfd1757f9f21521a22ecaaffccdd4e7f95ad1fccdb723a89bc142c8794c5` |
| practice output 3 | `166f2a2cc59aef4fb807a1e3fdc98062fd1c832bc68c69be59d8d246688898e7` |

## 4. What we already knew (disclosure)

We are not blind in several ways. Each is listed here.

- **A practice set was read.** Three outside AIs each wrote a battery from an earlier version of the prompt: 164 scripted learners in all. They were pasted into the session in which the wrapper's rules had been written, so the author of the rules read them. They are a practice set and count for nothing.
- **Details were settled after reading them.** The rules themselves were last changed before the practice batteries arrived. That version was fixed by hash when they arrived, and no rule was changed afterwards. But several details the rules left open were settled after reading them, and so was the whole scoring method in section 7. The sealed spec lists each one.
- **The code has run on the practice set.** Its three outputs are fixed by hash above. They are not results and no number from them will be quoted as one.
- **One change was tried and dropped.** After the stop rule was decided, one general change to the rules was written down, run once on the practice set, found to do worse there, and dropped. No other version was tried. The sealed spec records it.
- **Earlier checks do not count.** Before the practice set, the author of the rules tested them twice on learners the same author had scripted. Both times the count of wrong labels was zero, and the first count turned out to be wrong once outside reviewers added learners. Nothing from those checks is evidence.
- **How the stop rule was chosen.** After the practice run, two outside AI reviewers were given the same page and asked to choose a stop rule. They were told beforehand that if they disagreed the stricter rule would be used. One chose the rule in section 8. The other wrote a rule with thresholds. The rule in section 8 is the stricter one. The practice set would have failed it.
- **A second reader stopped publication three times.** A separate AI session that did not write the code checked it against the sealed spec before each attempt to publish this plan.
  - The first check found two faults. One could put the same problem to a learner twice. The other was in how the scoring decides that a learner has a true label. Both were fixed and the practice outputs were made again.
  - The second check found that the first fault was not fully closed for a problem the tutor itself had posed and the learner had left blank. It saw no repeat in 4,984 made-up sessions, but the code could not rule one out. It also found that a battery could end the run in an error report. Both were fixed, and the practice outputs did not change.
  - The third check found that the ban added after the second could be passed by code written to hide a name. The claim was withdrawn. The run no longer depends on the ban: any interrupt now ends in a STOP line. The practice outputs did not change.
  - The hashes above are the corrected ones. The sealed spec records each fault.
- **Who wrote this.** The rules, the code and this plan were written by an AI assistant working for the team. The team lead approved each step.

## 5. The battery that counts

- It is commissioned by the team lead only after this tag is public, from the sealed prompt, in a fresh chat with an AI that has seen none of the following: this plan, the spec, any review of them, the practice batteries, or the page given to the stop-rule reviewers.
- The prompt asks for at least 48 scripted learners. Each is a small program, so its true behaviour can be read from its code. Each has a short truth record written by its author.
- The two files are saved straight into a folder. They are not pasted into any chat with the author of the rules, and nobody on the team reads the learners before the run.
- `v39_intake.py` is run on that folder. It prints the two hashes, the list of modules the file imports, whether the file's own self-test passes, and counts. It prints no learner's name, code or truth record.
- The battery is code, and it is run as it is. The intake check screens for imports and names that an honest author would not need. It is a screen for accidents and not a sandbox, and the run does not depend on it.
- If intake fails, that battery is rejected unread. Another is commissioned in a different fresh chat, and the rejection is reported.
- Addendum v39.1 publishes the two hashes and the intake output before the run.

## 6. The run

- One command, once: `python3 -B v39_run.py <battery folder> <hash of the battery> <hash of its truth file> --run-after-tag`. Python 3, standard library only.
- Each learner meets, once, each of the 56 problems the frozen tutor may ask first. There are no random numbers of ours; the tutor's seed is fixed at 0.
- Every start first appends a line to an attempts log. The script refuses to run if its output file exists. It checks every hash, and reads the battery's text with the intake check, before the battery is loaded. It builds the whole report, saves it in one step, and only then prints it.
- On any error or interrupt, from the keyboard or from the battery's own code, it prints one line starting "STOP", saves no report and prints no count. If that happens, the cause is reported. A fault in our own code is fixed as a disclosed deviation, with new hashes published in an addendum before the next start. If the cause is the battery itself, that battery is rejected as at intake and replaced. The attempts log is published with the report.

## 7. Scoring, in general words

Truth is taken from each learner's own code.

- **A label holds.** Every label points to one way of answering. The learner is asked all 828 problems of the tutor's pool. The label holds when their answers are within 5 points of that way of answering on at least 90% of the problems they answer. Otherwise it does not hold, even when the label's sentence was true of the session.
- **A learner with a true label.** On at least 90% of problems their answers are within 1 point of the correct value, or within 1 point of what they themselves draw when asked to show their working. The exact test has further conditions, which are in the sealed spec.
- **The tutor alone.** Its "correct" verdicts and named rules are judged by the same test.
- **The truth records.** They are free text. After the run an outside AI reads them against the labels as a cross-check. That is reported as a description and is not the score.

## 8. Stop rule

The wrapper is shown only if both of these are true on the battery that counts:

1. Every label it gives holds for the learner who received it. This includes the label it gives after the tutor has said "correct".
2. At least half of all sessions of learners with a true label end in a label that holds. If there are no such sessions, the wrapper cannot pass.

If either fails, the team enters the frozen tutor alone, with its published record. There is one attempt. A failure ends the wrapper's bid for this final, and no second battery is run.

## 9. Forecast

The author of the rules expects the wrapper to fail condition 1. The reason is in the sealed spec. It is written here before the battery exists.

## 10. What is reported, whatever happens

- Counts and denominators for each kind of label: how many were given and how many do not hold.
- How many different learners received a label that does not hold.
- The share in condition 2, with its numerator and denominator.
- For the frozen tutor alone on the same battery: how many verdicts it gave and how many do not hold.
- How many of the tutor's "correct" verdicts that do not hold the wrapper confirmed, and how many it declined to confirm.
- The second reviewer's four thresholds, each with the number it would be compared with. They decide nothing.
- The disclosures of section 4, again.

## 11. What this cannot show

- These are programs, not people. Nothing here is about learning, and nothing shows how a person would read a label.
- A pass would not show the wrapper is safe with people. A fail on a single label would not show how much the wrapper helps or harms on balance; section 10 is there for that.
- The battery is one AI's idea of how learners behave.
- The practice batteries came from the same family of prompt, and the author of the rules read them. The battery that counts may resemble them.

## 12. Deviations and what follows

- Nothing in the sealed files changes after this tag, except as section 6 allows.
- Any departure from this plan is listed in the report.
- Report v39 is published with the sealed spec, the code and the two prompts. The batteries, the reviewers' answers and anything that quotes them stay private, because they are AI-written text; their hashes are public.
- The report is published only after the two team members who are coding plan v14 blind have handed in their sheets, because it shows what the wrapper said.
