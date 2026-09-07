# HOLD-007 — the five scholars' code letters have no key

**Raised by:** domain A, 2026-09-07
**Blocks:** any statement about **what** Grassmann, Oldenberg, Arnold,
Wüst or Witzel meant by marking a stanza. Does not block `DA-M-009` to
`DA-M-015`, which treat the markings as set membership only.
**Ledger:** `SRC-072`

## What is held

`info/stanza_properties.json` marks 2,372 stanzas with one or more of:

| Field | Code values | Work named in the TEI |
|---|---|---|
| `grassmann` | `G` | Grassmann, *Rig-veda, übersetzt und mit kritischen erläuternden Anmerkungen versehen*, Brockhaus, Leipzig 1876–7 |
| `oldenberg` | `O`, `o` | Oldenberg, *Prolegomena* 1888; *Noten* 1909, 1912 |
| `arnold` | `C1`, `C2` | Arnold, "Sketch of the Historical Grammar of the Rig and Atharva Vedas", *JAOS* 18: 203–353, 1897 |
| `wuest` | `W`, `w` | Wüst, *Stilgeschichte und Chronologie des Ṛgveda*, DMG, Leipzig 1928 |
| `witzel` | `Z`, `z` | Witzel, "R̥gvedic History: Poets, Chieftains and Polities", in Erdosy (ed.), *The Indo-Aryans of Ancient South Asia*, De Gruyter, Berlin 1995 |

The repository gives no key. Nothing in it says what `C1` is as against
`C2`, or whether upper and lower case carry the same distinction here
that they carry in `strata.json` (there, per `PUR-011`, lower case means
the period is indicated by metrical variations alone). It does not even
say that a marking means "late": that is the natural reading of a file
called *stanza properties* whose five sources are all works on
chronology and style, and it is a reading, not a fact.

Every claim in this unit is therefore written to survive the key being
anything. `DA-M-009` to `DA-M-015` measure set membership, set overlap
and cross-tabulation against Arnold's codes. None of them says what a
mark means.

## What is needed

Either an explicit key from the VedaWeb project, or the five works
themselves, which would let the marks be reconstructed from the source.
The four in `HOLD-006` are two of the five; Grassmann 1876–7 and Witzel
1995 are the others.

## A pointer that does not resolve

The `stanza_properties` `publicationStmt` carries
`<ptr target="http://digitalcommons.unl.edu/zeabook/55"/>`. That is a
University of Nebraska–Lincoln e-book series and has no evident relation
to any of the six works in its own `sourceDesc`. It was not followed —
the host is blocked in any case — and it is recorded as an unexplained
pointer rather than as a lead.

## What is *not* claimed

That the file is unreliable. Its compilers are named (Gunkel, Scarlata),
its licence is stated, and its sources are given in full bibliographic
form. What is missing is one paragraph of documentation.
