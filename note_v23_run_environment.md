# Note on v23: where the run happened and who ran the steps

Written 20 November 2026, after report v23 (tag v23-report). It adds to the record without changing any file or number.

- **Where `v23.py` ran.** Claude, the chat assistant in Bhavik's Claude desktop app, ran it at 00:25:24 IST on 20 November 2026. The run used the app's link to Bhavik's Mac: a Linux virtual machine that the Claude app runs on that Mac, with the tutor repo folder mounted into it. That machine's Python is 3.10.12, which is the version printed in `report_v23_output.txt`. Before the run, Claude checked that `v23.py` and `extract_final.csv` had the hashes locked in plan v23 and addendum v23.1. It ran the script once. `extract_final.csv` was read only on the Mac. Only the printed counts went back to the chat.
- **Other steps Claude carried out the same way, on the Mac:**
  - hashing files;
  - writing `manifest.csv` and `record.md`, from Bhavik's screenshots and his answers;
  - writing `record_note.md`;
  - building the lock table in addendum v23.1.

  Claude read no reply, stem or key file in doing these steps.
- **Everything else, as recorded.** Bhavik ran the sitting, copied the replies and ran `split_build.py` and `agree.py`. Claude Code sessions C, A and B did the splitting and extraction. A separate Claude Code session published every tag.
