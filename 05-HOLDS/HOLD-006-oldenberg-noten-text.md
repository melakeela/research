# HOLD-006 — Oldenberg's *Noten* are indexed here but unread

**Raised by:** domain A, 2026-09-07
**Blocks:** any claim about *what Oldenberg said* on a Rigvedic stanza,
and the resolution of `DA-I-002` — whether the four non-Arnold
stratifications converge because they share a criterion or because they
are independent.
**Ledger:** `SRC-073`, `SRC-085`, `SRC-069`

## What is held

`DA-M-016` and `DA-M-017` are VERIFIED and stay VERIFIED. They say that
Oldenberg wrote a textual note on 5,574 of the 10,552 stanzas, and that
his attention is close to flat across Arnold's five strata. Both are
facts about a **page concordance**, not about the notes.

What is held is everything one step further in: what Oldenberg judged,
on what grounds, and with what relation to Arnold's later periods.
`DA-I-002` cannot be resolved without it, and `DEP-022` — Oldenberg and
Wüst as one instrument at φ = 0.904 — cannot be diagnosed without it
either. Whether Wüst 1928 took Oldenberg's list over or reached it
independently is a question about two books, and neither is open here.

## What is needed

| Work | Where the corpus points |
|---|---|
| Oldenberg, *Ṛgveda: textkritische und exegetische Noten* I (1909) | `https://digi.ub.uni-heidelberg.de/diglit/oldenberg1909bd1/<page>` |
| Oldenberg, *Ṛgveda: textkritische und exegetische Noten* II (1912) | `https://digi.ub.uni-heidelberg.de/diglit/oldenberg1909bd2/<page>` |
| Oldenberg, *Die Hymnen des Ṛigveda. Metrische und textgeschichtliche Prolegomena* (1888) | not pointed at by the corpus; `archive.org` |
| Wüst, *Stilgeschichte und Chronologie des Ṛgveda* (1928) | not pointed at by the corpus |

The page numbers are already in hand. `external-resources/Oldenberg/Oldenberg_Band_1.csv`
and `_Band_2.csv` give 6,064 (stanza, page) pairs, so any specific stanza
could be looked up directly the moment the host is reachable.

## What was tried

`digi.ub.uni-heidelberg.de` was not probed individually; it falls under
the `SRC-069` sweep, in which every host except `github.com` and
`raw.githubusercontent.com` refused at CONNECT. `archive.org` was probed
and refused.

An English translation of the *Prolegomena* exists — Paranjape and
Mehendale, Motilal Banarsidass, Delhi 2005 — and the Consensus connector
returned its publisher description (`SRC-084`). A publisher description
is not the book.

## What is *not* claimed

That Oldenberg's notes are lost, rare or suppressed. They are digitised,
open, and the corpus links to them by page. This is `NOT ACCESSIBLE`
under the negative-evidence typology and nothing else. The absence is
entirely a property of this session's network policy.

## Release

`D-001` and `D-044`: add `digi.ub.uni-heidelberg.de` and `archive.org`
to the egress allowlist.
