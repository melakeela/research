# HOLD-007 — Oldenberg 1888 is used here only at second hand

**Raised** 2026-09-07, domain A.
**Caps** RCI-007, RCI-010, RCI-011 and DEP-021.

## What is needed

Hermann Oldenberg, *Die Hymnen des Ṛigveda. Metrische und textgeschichtliche
Prolegomena*, Berlin 1888 — pages 191–197 and 265 for the arrangement rule,
197–202 and 222–223 for the list of appendices.

## What this session has instead

Two derivatives, and they agree:

1. **Hellwig 2020**, LT4HALA, §5.4 and footnote 6 (`SRC-074`), which states
   the rule and lists the 31 appendix hymns. Read in full from a PDF inside
   the DCS repository.
2. **The `oldenberg` column of VedaWeb's `stanza_properties.json`**
   (`SRC-070`), Gunkel and Scarlata's transcription of the *Prolegomena*
   together with the 1909 and 1912 *Noten*.

All 31 hymns in Hellwig's list are marked in every stanza in the VedaWeb
column (`RCI-007`, output `m7-oldenberg-cross-check.tsv`). Two independent
transcriptions agreeing is a reproducibility check, and it is worth
something; it is not the source.

## Why it is blocked

archive.org, which holds the *Prolegomena*, refused at CONNECT with HTTP 403
(`SRC-084`).

## What turns on it

Less than `HOLD-006`, because the arrangement rule was **tested against the
corpus rather than accepted on Oldenberg's authority** (`RCI-010`): 216
descents against 56 ascents within maximal addressee runs, Monte Carlo
p < 0.01 in every book. That test does not depend on Hellwig having reported
Oldenberg correctly, only on the rule being worth testing.

What does depend on the second-hand reading is the appendix *list*, and with
it `RCI-011`. If Hellwig's footnote 6 misreports the list, `RCI-011`'s
comparison of rule-breaking hymns against Grassmann's marks would need
re-running against the corrected list.

## Negative-evidence typing

`NOT ACCESSIBLE`.

## What would clear it

`archive.org` on the environment egress allowlist (`D-043`, `D-045`).
