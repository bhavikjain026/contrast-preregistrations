# Addendum v23.1: replies and extraction locked before the run

Written 20 November 2026. Published under tag v23.1 **before** `v23.py` is run on any extracted data (plan v23, section 5, step 5, and section 11). Plan v23 (tag v23) and the pipeline (tag v23-pipeline) are unchanged. This addendum records what happened and locks every file by its SHA-256.

No one has run `v23.py`, a collision check or a Bayes calculation on the extracted data.

## 1. Generation (plan section 4)

**Timing.** Tag v23 was created at 23:25 IST on Thursday 19 November 2026, and tag v23-pipeline at 23:43 IST. The sitting ran from 23:49 to 23:59 IST the same evening, in one sitting of about 10 minutes. The first reply was saved at 23:51:35 and the last at 23:59:30 (file times).

**Order and attempts.** The six chats ran in the planned order: ChatGPT, Gemini and Claude on Arm 1, then the same three on Arm 2. Each ran once, with no technical failure, so every disposition is "ran" and every used file is `_attempt1`.

**Requests.** The two requests were copied from the published plan into `arm1_request.txt` and `arm2_request.txt`, then pasted by hand. Their hashes are in section 6.

**Copying.** Bhavik copied each reply with the app's own copy button and saved it with `save_reply.sh`, which writes the clipboard unchanged (`pbpaste`) and appends the file's SHA-256 to `hashes.txt` at once.

**Apps, tiers and chat type:**

| Chatbot | App | Tier | Chat type |
|---|---|---|---|
| ChatGPT | ChatGPT Mac app | Plus (paid) | Temporary chat, shown as "Unpersonalized" |
| Gemini | Gemini Mac app | "Gemini Pro" (account shows "Pro") | Temporary chat |
| Claude | claude.ai in Chrome | Max (paid) | Incognito chat, no project |

**Shown in the screenshots:**

| Chatbot | Model shown | Notices | Tools the app used on its own |
|---|---|---|---|
| ChatGPT | No model name; the selector reads "Medium". Arm 2 showed "Thinking". | none seen | Arm 2: the reply included an interactive illustration made by the app. Arm 1: none seen. |
| Gemini | "Hydrogen", "Medium". Arm 2 showed a status line while working. | none seen | none seen |
| Claude | "Sonnet 5.5", "Medium", "Auto" | none seen | none seen |

## 2. Deviations and other things to report

1. **Model selection (plan section 3).** The plan asked for the default model. Each app opened on the model Bhavik had last used, and for each reply he changed the selection to the model shown above. Whether that is each app's default was not checked. Every count is therefore reported with the model shown, as plan section 8 already requires.
2. **Session C read one file outside its folder.** It was a saved copy of its own earlier tool output, a numbered listing of the replies it had been given. It held nothing beyond those replies.
3. **Sessions A and B wrote helper files outside their folders.** These were scripts in their scratch folders, plus session A's copy of its keys file from before the format fix. They were writes, not reads. Copies are kept in `ab_tools/` and hashed in section 6.
4. **One format fix in session A's keys file.** `agree.py` stopped because one key was written as a fraction with a decimal point inside it, which the format does not allow. Session A was told only the error and the allowed format. It rewrote that single row in the allowed format with the same value, and reported that it had checked the value was equal and that no other row had changed. The first file is kept as `keys_A_try1.csv`. Session B was told nothing.
5. **Who saw what.** Bhavik saw the full replies while copying them, as the plan expects. To have them saved, he also sent the twelve sitting screenshots to Claude in a separate chat; parts of the problems and answers are visible in them. The `agree.py` output for the one unresolved key, which shows both sessions' values, was also seen in that chat. Nobody in either place checked, extracted or computed anything from them. Kahan and Jay took no part.

## 3. Step 1, split

`split_build.py` printed **ALL OK** for all six replies on the first attempt. Each reply has 20 occurrences, labelled 1 to 20 with no repeats. There are no unscored occurrences and no missing labels.

Choices session C reported:
- **The Claude replies state the question once, in a line at the top, rather than in each problem.** Under step 1 that line belongs to the log, so the 40 Claude stems contain the rates but no question sentence. No rule was changed. Sessions A and B each noted this independently and included those slots, because section 5 lists no exclusion for a missing question.
- **ChatGPT Arm 2.** The worked example for problem 1 went to the key for `1#1`. The text describing the interactive illustration and the reply's own validation went to the log.

## 4. Steps 2 and 3, stems

`agree.py stems` compared 120 slots: **120 agree, 0 unresolved.**

- Included: 119.
- Excluded: 1, `excluded:out_of_range`. This is Claude Arm 1, slot 20, where one stated rate is 100%.
- Missing: 0.

## 5. Step 4, keys

Each session marked all 120 keys `scored`. `agree.py keys` compared the 119 included slots: **118 agree, 1 unresolved.**

The unresolved key is ChatGPT Arm 2, slot 1. That block gives the answer twice, in a table and in a later worked example, and the two sessions recorded different forms of it. As the plan requires, no person chose between them. This key is reported as unscored (`unresolved`) in Q2. Its stem still counts for Q1, Q1x, Q3 and Q4.

## 6. Locked files

All paths are relative to `exploratory/v23/v23_run/` in the tutor repo, which stays private. No reply, stem, key or screenshot is published.

**Generation**

| File | SHA-256 |
|---|---|
| `arm1_request.txt` | `cf2802a8abfb7acdd1c592586e8110336881a56c64af753f4363200397cfc68b` |
| `arm2_request.txt` | `dffcd1fbba2bf5c9a1783411a8dc6853279983e6818cee63daee9dabc39d1edb` |
| `hashes.txt` | `f8b362c22b6f65aee98248cf5d7663a264efcc19ee179631f905afa1f29cd05e` |
| `manifest.csv` | `609b65c355d06272215001b60138a8f824dbee97f13a49ca3aad1131382919e3` |
| `record.md` | `a446f506f3f1895ef43b2e33f1340f775e576da8194c666e3afdf2db9b1b6bf0` |
| `record_note.md` | `df67c36ca0e0847ab56c3585f76e25b9a53486b6c96097fd375eef3048a5e783` |
| `replies/ChatGPT_arm1_attempt1.txt` | `e2ca33aa0dc9782463c6b8a7a79a00a6689baea47c780408c54d810272a18e91` |
| `replies/ChatGPT_arm2_attempt1.txt` | `3e38f67f7aee72af0e35035dcc880519e2164d7aa5aac8468a5d0ffcd277a8b7` |
| `replies/Claude_arm1_attempt1.txt` | `9b4829eeca292a0fd7dd444d44226057fa862bfb8328902f3fdb07201009959e` |
| `replies/Claude_arm2_attempt1.txt` | `70b147a8017dfbf0d721a6091ad89c95087bc0c5a8a99e3855c41b4952cc21dd` |
| `replies/Gemini_arm1_attempt1.txt` | `2ba1ef2abe7595799e02b1a25c4a5fbf4f2f200c8c88ba29885a903a37569d15` |
| `replies/Gemini_arm2_attempt1.txt` | `9b608616bdd34f85357ce21b9b276ff026dc3d90cecb3bf2c930fc3977d58b4e` |
| `save_reply.sh` | `40df6346005d520eb2c4c7a33150d147e55c4260e59e6609c8ca067e85c29ee7` |
| `screenshots/Screenshot_2026-11-19_at_11.49.57PM.png` | `e87223c315158aa3e24fb529a86e2331f12a64347e027b31f847896f9b380d53` |
| `screenshots/Screenshot_2026-11-19_at_11.51.01PM.png` | `b67d75eec76448e37dd46a85f761bd16bb34f5db2357811a458e167eb3d48879` |
| `screenshots/Screenshot_2026-11-19_at_11.52.08PM.png` | `6c274ca5bc23f677bee83d312e7935627d8f9bdf68fb4cb3c0d935ddb5d6e9b4` |
| `screenshots/Screenshot_2026-11-19_at_11.52.44PM.png` | `69730dc326d9db2e451a198b9b077a1265c3fe3783de05907d96d9d5f98f0ca3` |
| `screenshots/Screenshot_2026-11-19_at_11.53.39PM.png` | `620bb7a33eab635a493bd6f6aec7026b377b9a51f8130ab95e0430daf67aabfd` |
| `screenshots/Screenshot_2026-11-19_at_11.54.05PM.png` | `9bd7560fe364e9f0c48d176cbe7d1fb74c97ceaa2753695f0fbe3d25691c6640` |
| `screenshots/Screenshot_2026-11-19_at_11.54.49PM.png` | `c75912e2081b502864447b5cd01342885c89136198452fc5432a5440eb1f2725` |
| `screenshots/Screenshot_2026-11-19_at_11.56.07PM.png` | `7b8f59c812806a131887d24fb961331df434c1cd419d99679d37cf44242ae81a` |
| `screenshots/Screenshot_2026-11-19_at_11.56.43PM.png` | `e5b0ccf2bf00d7b39b7b750f193372dfcdcc9e784e7322c5bf3da112459cd3e2` |
| `screenshots/Screenshot_2026-11-19_at_11.57.29PM.png` | `a82f4a1f9cb10fca3783159221af3035f1d05090c50b20074bf16e829c55ab1a` |
| `screenshots/Screenshot_2026-11-19_at_11.58.04PM.png` | `b615c33d018ff73286ce966b1272403492c7ec45bb622783d7f167647185aa82` |
| `screenshots/Screenshot_2026-11-19_at_11.59.13PM.png` | `68f4eda843422d9508db2e408378c890761f900650af95816586eaa8abdc71df` |

**Step 1, split (session C)**

| File | SHA-256 |
|---|---|
| `c_tools/split.py` | `11db2f5bc0feecf7a4c7f615e40b30ee9d2696052e246fc653e38efea65c0ad7` |
| `keys/ChatGPT_arm1.txt` | `1aa701ee9c5910fbee1626ea36f2cd4c79e2c4c625fa4b9238d16d8ccd8220b7` |
| `keys/ChatGPT_arm2.txt` | `9169858a9e8f0608bf17f9cf7c42e1f77b3e5bddb255077aa489d6f38d064ffa` |
| `keys/Claude_arm1.txt` | `a23d17d178019f73101b62abb5a4c95bc4ef4940fd4a3cb722fb84ce914b6dda` |
| `keys/Claude_arm2.txt` | `b92727068a900a9b83aefd685560927413fd815e5a9caa42e5a3201c1af66dc5` |
| `keys/Gemini_arm1.txt` | `c3d5cf4e1536ea28a7c3a0cd749dab61211797e938b3e4b1a478063fa5238b71` |
| `keys/Gemini_arm2.txt` | `16e5127c5833e88f2ab73eaa2c7b4b5c6e3087596179b19b5aa4e55ec5fdce3a` |
| `log/ChatGPT_arm1.txt` | `a98842ad86062bea0ac2cb60d8fa442f035fe2effbe5097ca417cf47a06394dc` |
| `log/ChatGPT_arm2.txt` | `1852cb2253497a464a3a015649d2c257365efc295899a9c51164aad761bc497e` |
| `log/Claude_arm1.txt` | `d42c4d877ddaf845d79a63a69fdecf0ee87f9f53aedb2e8ce91de377c7f6300e` |
| `log/Claude_arm2.txt` | `9058e63388d10ce616c01c799a1e09834d3888faa6b56e5713099bc9504d6f3a` |
| `log/Gemini_arm1.txt` | `de502e3ecb1b2acb1bcc063e237e7d15c3f150e36eebb8537dd908b7f6d0db2c` |
| `log/Gemini_arm2.txt` | `8fa8762c00d21c7ecae8ebfa9a75e8da074d101e8a24642398e6f04b4ca4d592` |
| `split/ChatGPT_arm1.jsonl` | `97d1ecbcc5443119ebe798e6859fa772aa9e2e2b8c670ea4fdee00bd862a0231` |
| `split/ChatGPT_arm2.jsonl` | `f31a77dc3b6cf28d1ad68d3e1925c95b5cdfbe14de4617e695af93649acb896a` |
| `split/Claude_arm1.jsonl` | `0c4d1ab6492a7afa6baaad952cc30fa6084c7dfdac3ad4a81fab7fd7ceed1c90` |
| `split/Claude_arm2.jsonl` | `001db8a39b26d096d5e0af664d8774a7e1b269afac442e407be11827c2164444` |
| `split/Gemini_arm1.jsonl` | `2fdd3f32ec6dd64324dd89987a50384669de35d61030b99759665a7527ca49d3` |
| `split/Gemini_arm2.jsonl` | `4041b9100457c7dd40efdfaa4c00e3aa6e0ec52a7346e2c553bf75e517eea2a8` |
| `split_check.txt` | `279bf9d04fa6344d2975b6772e7e2f7ed87c714a6ee6297d7623c9a6c1191fc4` |
| `stems/ChatGPT_arm1.txt` | `615a086deaf4e35500e017eb201138d431bfd4e942010285eacd64065fe1b98e` |
| `stems/ChatGPT_arm2.txt` | `ba09aee874d42883bd4f36ba834b905b299c4e5eb4d66cff65859d99d2d0e4ef` |
| `stems/Claude_arm1.txt` | `f2919febb72eb96dc9de97b191327c354441e7a26c02aff91f047327a6e59d4b` |
| `stems/Claude_arm2.txt` | `e696a87df70024ed88cd51c53e8a4a84fd13974540d639dafccadfb5254fd895` |
| `stems/Gemini_arm1.txt` | `7a9f2c4bd55503ebcdda4fe691ebaab3def9afb657f56fa995f893c280d17db7` |
| `stems/Gemini_arm2.txt` | `77a279274056fd69aff64fbedab8f1f3e2976e92edd0bdbea92217c7a5bca125` |

**Steps 2 and 3, stems**

| File | SHA-256 |
|---|---|
| `stems_A.csv` | `437ab82717a60f519040a4a30830543855c4c38ed681ba9e7f131374b491f7e6` |
| `stems_B.csv` | `027819615e1143dc2c05dc3aa0ef517ba55015ca628ae52322a6a39878611281` |
| `stems_agreement.txt` | `21a339e7a949c9aa335749253a0f30c20846e98692d24ece26ede94fffe24f25` |
| `stems_final.csv` | `53cb1948528a37ef7711bc471c8725e6a0b45bb6684a08f638b4b90c16743c0d` |

**Step 4, keys**

| File | SHA-256 |
|---|---|
| `extract_final.csv` | `bbeea3ea18d34e7020c42ead5d343527c235873958204461deb180d79a08787a` |
| `keys_A.csv` | `b9b61543eda9ebafa18b43a3fa7f0e2a9d01d68ab99dd21824fe4548de64a8e8` |
| `keys_A_try1.csv` | `b9e3ac02011afa6e87b7dbf1fa407ebbef82070a25cda1fdab403bbf669b2cdd` |
| `keys_B.csv` | `431ea77fa72201ff3f0a3945dd0215f76199fd48fb06a6ca01980976c0869d93` |
| `keys_agreement.txt` | `1f29a15baf25aac299db2f90b1c0079ac35c2ed6035826e344c64f958383c121` |

**Helper files written by sessions A and B (copied from their scratch folders)**

| File | SHA-256 |
|---|---|
| `ab_tools/extract_A.py` | `45b08ed03996483d044c9a3ab2f0be64f894ce69e33959f6c81441fa86bbde8b` |
| `ab_tools/keys_A.before.csv` | `b9e3ac02011afa6e87b7dbf1fa407ebbef82070a25cda1fdab403bbf669b2cdd` |
| `ab_tools/keys_A.py` | `e852c44f35828d66072dd1dda415c06a19dac64ccba58f85c20ae2e4fb0ccb8b` |
| `ab_tools/write_keys_B.py` | `5c7e33629434432ede6078c1d3b9591c15f47d89f07fe23abbdb75f55425b0c9` |
| `ab_tools/write_stems_B.py` | `a1edbc35116a1644054de38ce332efc72e270670a749040e6c5346aee022c1fe` |

`hashes_extraction.txt`, the running log of hashes taken during extraction, is superseded by this table. Every hash it records matches a file listed here.

## 7. Next

1. Publish this addendum under tag v23.1.
2. Then run `python3 v23.py extract_final.csv` **once**, with `v23.py` at the hash in plan v23, section 9. Save the full output and hash it.
3. Report the result in the order of plan section 7, whatever it shows.
