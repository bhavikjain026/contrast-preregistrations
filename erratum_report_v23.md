# Erratum to report v23 (tag v23-report)

Written 20 November 2026 and published with plan v24. This erratum corrects one sentence of explanation. It does not amend any definition or any count in report v23.

**Report v23 said**, under "Does not show": "The algebra above shows that a low false-alarm rate by itself pushes equal priors and 100% − false alarm together."

**That is wrong as stated.** Write H and F for the hit and false-alarm rates as proportions, with H + F > 0. The signed gap is

  (100% − false alarm) − (equal priors) = 100 · F(1 − H − F)/(H + F) points.

- **When the gap is small.** With the hit rate held fixed, the gap shrinks to zero as the false-alarm rate falls. For a sensitive test with few false alarms, it is small: about 1.1 points at H = 0.8, F = 0.1, and about 0.3 points at H = 0.9, F = 0.05.
- **When it is zero.** When H + F = 1.
- **When a small false-alarm rate is not enough.** If the hit rate also falls, the gap need not shrink. With H = 2F, the gap is 100(1 − 3F)/3 points, which tends to about 33 points as F falls.
- **A small gap is not a collision.** It does not by itself mean that one whole-percent answer fits both methods. That depends on the tutor's window and on where the two values fall.

**The corrected sentence:** "The algebra above shows that, for a sensitive test, few false alarms push equal priors and 100% − false alarm close together; a low false-alarm rate alone does not."

Two outside reviewers, Gemini and ChatGPT ("Astra"), pointed this out while reviewing plan v24. The quoted sentence was checked against report_v23.md at tag v23-report.
