# HOLD-010 — Arnold's per-pāda assignments have never been checked against Arnold

**Raised by:** domain A, 2026-09-07
**Blocks:** `DA-I-001` beyond `PROVISIONAL`; the promotion of `PUR-028`
in either direction; and the diagnosis of `DA-M-007`, the five
book-by-stratum cells that are exactly zero.
**Ledger:** `SRC-026`, `SRC-083`, `SRC-023`, `SRC-069`

## The distinction this hold exists to keep

**Arnold's criteria and letters are retrieved.** `SRC-026` records a
successful retrieval on 2026-09-07T00:50Z of the archive.org OCR of
*Vedic Metre in its Historical Development* (item
`vedicmetreinitsh00arnouoft`), including Appendix IV §265 at printed
p. 269, which is where `PUR-011` gets the five stratum letters and the
meaning of the lower-case flag. `PUR-011` is properly `VERIFIED` and
`DA-D-002` confirms it.

**Arnold's per-pāda assignment list is not retrieved.** The only
per-pāda assignments in this repository are Gunkel and Ryan's
`strata.json`. No line of that file has ever been compared with Arnold.

## Why it matters more after this unit than before

`DA-M-007` finds five book-by-stratum cells that are exactly zero. Books
3, 4 and 7 contain no Archaic pāda at all; book 6 contains no Strophic;
books 4 and 8 contain no Cretic. Those five books hold 17,377 pādas,
43.6% of the coded corpus. A zero cell is not a small count — it is the
classification declining to give a book a period.

There are three explanations and the file cannot distinguish them:

1. Arnold found period and book to coincide in those cases. A finding.
2. Arnold used book membership as a criterion. An assumption inside the
   instrument, which would make `DA-M-005`'s Cramér's V of 0.463 partly
   circular by construction.
3. The transcription imposed it — for instance by assigning a stratum
   per collection where Arnold assigned per hymn or per stanza. An
   artefact.

`DA-M-008` sharpens the same point: 9.1% of coded pādas carry Arnold's
lower-case flag, but it runs from 0.0% in book 9 to 23.6% in book 3 and
22.4% in book 1. Whether that spread is Arnold's or the transcriber's is
the same question.

## What is needed

The OCR text already retrieved once, at `SRC-026`, plus enough of
Arnold's tables to spot-check. A sample of a few hundred pādas across
the five zero cells would settle explanation 3 outright, and would
strongly indicate between 1 and 2.

## What was tried

`archive.org` refused at CONNECT in this session (`SRC-069`). The
earlier session's downloaded files were session-local and were not
committed, so the OCR is not in the repository either. This is the
concrete cost of the "uncommitted work does not survive a session
restart" rule being applied to retrieved source text as well as to
registers.

## What is *not* claimed

That `strata.json` is unfaithful. Nothing here suggests it is. What is
claimed is only that its fidelity is **unchecked**, and that a
programme whose entire relative chronology descends from one file ought
to have checked it. `DA-D-001` states the consequence: no VERIFIED claim
falls if the check fails, and the register's chronological capacity does.

## Release

`D-044`: `archive.org` on the egress allowlist, or the Arnold OCR
supplied as a file.
