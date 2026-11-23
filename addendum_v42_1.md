# Addendum v42.1 to plan v42: the first attempt stopped on a published item; what changes before the second start

Written 23 November 2026, after the first attempt stopped and before any output of plan v42 existed. To be published
byte-identical under tag v42.1 before the next start. **No learners and no human data.**

## 1. What happened

Plan v42 was published under tag v42 (commit `c4d4ae5`) at 15:50:12 UTC on 23 November 2026. Its single run started
at 15:50:22 UTC and stopped at 15:50:26 UTC with this line:

> STOP: items_v20.csv, item Table 2: Active feminist / Bank teller (S1 Gigerenzer & Hoffrage 1995): outside 0 < b < 100, 0 < f < h < 100. No report was saved.

- The attempts log, `v42_run_attempts.log` (SHA-256 `168cfef2c3c8efe0fa682e51ca2c183ca3d7363a7a85c9e8898cdaa78eff12e2`), holds one
  STARTED line and one STOPPED line. It is kept unchanged and will be published with report v42.
- No output was saved. Before the stop the script had passed its hash checks, its check of the chatbot rows and its
  check that the Arm 1 counts are those of report v41 (59 sets, 54 with a collision). That check comes after the
  searches on the chatbot sets, so those searches had run in memory. Their counts were not printed or saved, and
  nobody saw them.

## 2. Why

The stop was the domain check of plan section 3 doing what it was written to do. The rule itself was wrong for one
published problem. The bank-teller item of Gigerenzer & Hoffrage (1995), as locked in plan v20, has base rate 5%, hit
rate 0.4% and false-alarm rate 2.105%: **its hit rate is below its false-alarm rate.** Report v20 includes it and its
output lists it (it is one of the three sets where a wrong method looks right). Plan v42's searches are defined for a
hit rate above the false-alarm rate, and prediction 4 uses that too. After the stop, the author of the plan read the
locked item file (published problems only) and found no other standard row outside the plan's domain. The chatbot rows had already passed.

## 3. What changes

- **Secondary C** leaves out any published set whose three rates all lie strictly between 0 and 100 but whose hit
  rate is at or below its false-alarm rate. Each such set is listed in the output by its numbers, source and item,
  with whether it has a collision under v41's measure. It is counted among report v20's 23 distinct sets, so the
  check against 23 still covers it. Any other row outside the domain still stops the run.
- **The attempts log.** The second start writes a new log, `v42_1_run_attempts.log`, created exclusively as before.
  Before it does, the script checks that the first log exists and has the SHA-256 above; otherwise it stops and
  reads nothing.
- **Two notes from the code check before the first run, fixed too.** If `v23.load` refuses the extract, the run now
  stops with a STOP line and a STOPPED log entry, and withholds the loader's message because it could quote a row.
  If the COMPLETE line cannot be written after the output is saved, the script says so instead of printing STOP.
- **Tests.** `test_v42.py` has 29 tests: the 26 of plan v42 (one changed: an out-of-domain item is now a hit rate of
  150%, which still stops), and three new ones: a published set with the hit rate below the false-alarm rate is left
  out, listed and counted; the first attempt's log must be the recorded one; a refusal by `v23.load` stops without
  quoting.

**Nothing else changes:** not the question, the predictions, the primary or secondary searches A and B, the
chatbot sets, the counts reported for them, the slide sentence or the limits. The primary result does not use the
published items.

## 4. Files (SHA-256)

| File | SHA-256 |
|---|---|
| `v42.py` (addendum v42.1) | `b4f0c703049453f342c57d806dd49a107d838ca2a8fe752d6c794cfb42494dfa` |
| `test_v42.py` (addendum v42.1, 29 tests, made-up sets only) | `4cce836eb29c1596bba78a5c7fca7af8b4ae684686ec8aec532eb02389220767` |
| `v42.py` as listed in plan v42, section 7, kept as `v42_as_in_plan_v42.py` | `3def31952cc5d350efcaf02a8564df5837acf5eebe52386e9172d718ae9b5bb6` |
| `test_v42.py` as listed in plan v42, section 7, kept as `test_v42_as_in_plan_v42.py` | `2d1069cfa52ff736166c7115f3137cfc92a544a6242bdd587d5b606b6c9228de` |
| `v42_run_attempts.log` (the first attempt) | `168cfef2c3c8efe0fa682e51ca2c183ca3d7363a7a85c9e8898cdaa78eff12e2` |

Every other file and hash is as in plan v42, section 7. The command is the same as in plan v42, section 7.4.
Report v42 publishes the output, both attempts logs and this addendum's history, whatever they show.
