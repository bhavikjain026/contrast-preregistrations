# v23 after the sitting: the runbook

Run every command from `exploratory/v23/` in the tutor repo. Nothing here is ever committed or pushed from the tutor repo. Kahan and Jay take no part.

Folders:
- **`v23_run/`**: replies, hashes and all outputs.
- **`pipeline/`**: these scripts and prompts.
- **`~/v23_C`, `~/v23_A`, `~/v23_B`**: one folder per Claude Code session. They sit outside the repo, so each session sees only what it is given.

Two rules for every step:
- **Hash first.** Each file a session hands back is hashed into `v23_run/hashes_extraction.txt` before anything else is done with it.
- **Log redos.** If a step fails and is redone, keep the failed output under a new name ending `_try1`, and so on. Every redo is reported in v23.1.

## 0. Right after the sitting

Write `v23_run/manifest.csv` with six rows:

```
chatbot,arm,disposition,used_file
ChatGPT,1,ran,ChatGPT_arm1_attempt1.txt
Gemini,1,ran,Gemini_arm1_attempt1.txt
Claude,1,ran,Claude_arm1_attempt1.txt
ChatGPT,2,ran,ChatGPT_arm2_attempt1.txt
Gemini,2,ran,Gemini_arm2_attempt1.txt
Claude,2,ran,Claude_arm2_attempt1.txt
```

- **After one technical failure,** used_file is `_attempt2.txt`.
- **After two failures,** the disposition is `unavailable:<reason>` and used_file is empty.

Then hash the manifest and record:

```
shasum -a 256 v23_run/manifest.csv v23_run/record.md >> v23_run/hashes_extraction.txt
```

## 1. Session C: split

```
mkdir -p ~/v23_C/replies
cp pipeline/step1_v23.md ~/v23_C/
cp v23_run/replies/<each used_file> ~/v23_C/replies/
cd ~/v23_C && claude
```

1. Paste `pipeline/prompt_C_split.txt` into the new session.
2. When C finishes, go back to `exploratory/v23/` and run:

```
mkdir -p v23_run/split && cp ~/v23_C/split/*.jsonl v23_run/split/
shasum -a 256 v23_run/split/*.jsonl >> v23_run/hashes_extraction.txt
python3 pipeline/split_build.py v23_run
```

- **If it prints ALL OK,** go to step 2. `split_check.txt`, `stems/`, `keys/` and `log/` are now in `v23_run/`.
- **If it prints FAIL:**
  1. rename `split_check.txt` to `split_check_try1.txt`;
  2. paste only the FAIL lines into session C;
  3. when it is done, repeat the copy, hash and check commands above.

## 2. Sessions A and B: stems (separate sessions, in parallel)

```
for X in A B; do mkdir -p ~/v23_$X/stems; cp pipeline/section5_v23.md ~/v23_$X/; cp v23_run/stems/*.txt ~/v23_$X/stems/; done
```

Open two Terminal windows:

```
cd ~/v23_A && claude
cd ~/v23_B && claude
```

1. In each window, paste its own prompt: `pipeline/prompt_A_stems.txt` or `pipeline/prompt_B_stems.txt`.
2. When **each** finishes, hash its file at once:

```
shasum -a 256 ~/v23_A/stems_A.csv >> v23_run/hashes_extraction.txt
shasum -a 256 ~/v23_B/stems_B.csv >> v23_run/hashes_extraction.txt
```

Never show one session the other's file, or anything about it.

## 3. Stem agreement (mechanical)

```
cp ~/v23_A/stems_A.csv ~/v23_B/stems_B.csv v23_run/
python3 pipeline/agree.py stems v23_run v23_run/stems_A.csv v23_run/stems_B.csv
shasum -a 256 v23_run/stems_final.csv v23_run/stems_agreement.txt >> v23_run/hashes_extraction.txt
```

- **If agree.py stops on a format error,** paste the error into that session only. When it has fixed the file, rename the old file to `_try1`, hash the new one, and run the commands again.
- **A disagreement is not an error.** The script turns it into `excluded:unresolved` by itself.

## 4. Keys: only after stems_final.csv is hashed

```
for X in A B; do mkdir -p ~/v23_$X/keys; cp v23_run/keys/*.txt ~/v23_$X/keys/; done
```

1. In each **same** session, paste `pipeline/prompt_A_keys.txt` or `pipeline/prompt_B_keys.txt`. If a window was closed, run `cd ~/v23_A && claude --continue`.
2. When each finishes, hash it:

```
shasum -a 256 ~/v23_A/keys_A.csv >> v23_run/hashes_extraction.txt
shasum -a 256 ~/v23_B/keys_B.csv >> v23_run/hashes_extraction.txt
cp ~/v23_A/keys_A.csv ~/v23_B/keys_B.csv v23_run/
python3 pipeline/agree.py keys v23_run v23_run/keys_A.csv v23_run/keys_B.csv
shasum -a 256 v23_run/extract_final.csv v23_run/keys_agreement.txt >> v23_run/hashes_extraction.txt
```

## 5. Stop

1. Send me `v23_run/hashes.txt`, `v23_run/hashes_extraction.txt` and `split_check.txt`. From `stems_agreement.txt` and `keys_agreement.txt`, send only the count and hash lines at the top. Do not send the per-slot lines, replies, stems, keys or extract files.
2. I will write addendum v23.1.
3. Nobody runs `v23.py`, the Collision Checker or any Bayes calculation on these files until v23.1 is published. After that, `v23.py` runs exactly once.
