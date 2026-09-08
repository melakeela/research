# Domain A retrieval manifest — 2026-09-07

Backing record for ledger rows `SRC-089` through `SRC-104`.

Domain A is Rigvedic chronology and transmission. The unit was commissioned to
examine, rather than use, the dependency `DEP-001` already records: that every
chronological claim in this repository rests on Arnold's metrical strata, and
that VedaWeb's `strata.json` and Arnold 1905 are one source, not two. The
retrieval question was therefore narrow and answerable: **is any instrument of
Rigvedic relative chronology retrievable in this session that is not Arnold?**

The answer is yes, and four of them were already inside the corpus this
repository has had pinned since 2026-09-07.

## What was retrieved

### The corpus, for the third time

`VedaWebProject/vedaweb-data` at `d3eb8af7324338161520d2d35eae8f7e985a19a5`
(`SRC-089`). Every checksum in `02-SOURCES/vedaweb-manifest-2026-09-07.md` that
was re-checked matched, and `04-AUDITS/rv-token-extract.py` reproduced 164,758
tokens. This is a third retrieval event of one target, not a third source:
`DEP-020` already records the second, and `DEP-029` below records this one.

### `info/stanza_properties.json` — the find of the unit

A per-stanza layer of **presumed late additions**, compiled by Dieter Gunkel
(Richmond) and Salvatore Scarlata (Zürich), carrying the judgements of five
scholars in five separate columns (`SRC-090`):

| Column | Work | Codes | Stanzas |
|---|---|---|---|
| `grassmann` | Grassmann 1876–7, *Rig-veda. Übersetzt* | `G` | 1,094 |
| `oldenberg` | Oldenberg 1888 *Prolegomena*; 1909 and 1912 *Noten* | `O` 424 / `o` 275 | 699 |
| `arnold` | Arnold **1897**, "Sketch of the Historical Grammar of the Rig and Atharva Vedas", JAOS 18: 203–353 | `C1` 732 / `C2` 576 | 1,308 |
| `wuest` | Wüst 1928, *Stilgeschichte und Chronologie des Ṛgveda* | `W` 418 / `w` 291 | 709 |
| `witzel` | Witzel 1995, "Ṛgvedic History: Poets, Chieftains and Polities" | `Z` 441 / `z` 248 | 689 |

2,350 stanzas of 10,552 carry at least one mark. (The file has 2,372 keys; 22 are empty objects. Recorded as 2,372 on 2026-09-07 and corrected the same day after adversarial review.)

The layer has been in the pinned clone throughout and has never been opened in
this repository. It is not `strata.json` and it is not derived from it.

### The legend for that layer

`resources/help/lateAdditions.md` in `VedaWebProject/vedaweb` at
`f6f840084e5c4d80444dec323fcd94d74e5b1bfc` (`SRC-091`). It states the code
semantics in full, and they are not guessable from the data:

> The abbrevations are case sensitive: Lowercase is used to indicate that the
> author was unsure, e.g. "O" = Oldenberg thought it was certainly an Addition
> vs. "o" = Oldenberg thought it may/might be an Addition. In his "Sketch,"
> Arnold distinguishes between two phases of Additions, C1 and C2.

The same legend is served to readers at `vedaweb.uni-koeln.de`, which is
`EGRESS_BLOCKED` in this session (`SRC-035`, `SRC-104`). The platform's own
source repository, reached over the git lane, was the only channel that
delivered it.

### Hellwig 2020 in full text

`papers/2020lt4hala/paper/hellwig-linguistic-markers-2020.pdf` inside
`OliverHellwig/sanskrit` (`SRC-093`, `SRC-094`): Oliver Hellwig, "Dating and
Stratifying a Historical Corpus with a Bayesian Mixture Model", LT4HALA 2020.
Ten pages, read in full. It carries three things this unit needed and could not
get any other way:

1. Oldenberg's arrangement rule stated with locators — hymns in each book are
   arranged by number of stanzas, and hymns violating the rule are the youngest
   layer, the "appendices" (Oldenberg 1888, 191–197, 265).
2. The list of the 31 appendix hymns (Oldenberg 1888, 197–202, 222–223),
   printed in Hellwig's footnote 6.
3. Hellwig's own model result on the ten books, and his own qualification of
   it: the appendix effect is driven by a handful of hymns, and the family-book
   appendices are not marked late by the model at all — some are marked early.

This is Hellwig reporting Oldenberg. `DEP-027` records that it is not Oldenberg
retrieved.

### The Aṣṭādhyāyī

`ashtadhyayi-com/data` at `24109f7` (`SRC-098`), `sutraani/data.txt`: one record
per sūtra with Devanagari text, transliteration, padaccheda and anuvṛtti. It
makes the `chandasi` question countable. It is a community edition with no
stated critical apparatus, so counts over it are counts over that file.

### Retrieved, logged, not used as instruments here

- `UniversalDependencies/UD_Sanskrit-Vedic` (`SRC-096`) — 4,000 sentences across
  five texts. A sample, too small for a per-book Rigvedic distribution.
- `sanskrit-texts/rigveda` (`SRC-097`) — Hellwig's morpho-lexical and Hettrich's
  verb-argument annotation of the whole Rigveda. A second, author-independent
  morphological annotation of the same text. Aligning it token-by-token to the
  Zürich layer is a unit of work in itself and was not attempted.
- The DCS transcription of Arnold's *lexical* criteria, Arnold 1905 pp. 29–43
  (`SRC-095`). Same author and same book as `SRC-023`/`SRC-026`; a different
  part of it. Recorded as `DEP-028`, not as an independent instrument.

## What could not be retrieved

Twelve hosts were probed and all twelve refused at CONNECT with HTTP 403
(`SRC-104`): archive.org, gretil, titus, dsal, jstor, arxiv.org, doi.org,
api.crossref.org, zora.uzh.ch, aclanthology.org, openalex.org. `WebFetch`
returned `EGRESS_BLOCKED` for archive.org and zora.uzh.ch. The egress policy in
this session is GitHub-only over the git proxy lane.

The three consequences are exact:

- **Arnold 1905 itself was not read in this session.** `PUR-011` was verified
  against the archive.org scan in an earlier session, when that host answered;
  it is not re-verifiable now. `HOLD-009`.
- **Oldenberg 1888 itself was not read.** What this unit has is Gunkel and
  Scarlata's transcription of his marks (`SRC-090`) and Hellwig's report of his
  rule and his appendix list (`SRC-094`). `HOLD-010`.
- **Hellwig, Scarlata and Widmer 2021 was reached in abstract only**, through
  the Consensus connector (`SRC-099`). The ZORA open-access copy and the JAOS
  copy were both refused. `HOLD-011`.

## The connectors, one by one

The instruction was to use the MCP literature connectors and record what each
returned. All five were called.

| Connector | Result |
|---|---|
| Consensus (`SRC-099`) | **Worked.** Returned the Hellwig, Scarlata and Widmer 2021 abstract verbatim, plus Klein 2008 on Arnold's standing. The only connector that reached the target paper at all. |
| Scholar Gateway (`SRC-100`) | Worked, wrong corpus. Ten Wiley passages, none the target. Two are useful as standing evidence: TPS 12141 uses Arnold's "Popular Rigveda" as a live chronological label in 2018. |
| Scholar Feed (`SRC-101`) | Worked, arXiv cs.CL only. Three relevant computational papers, no philology. |
| alphaXiv (`SRC-102`) | Worked, arXiv only. Overlaps Scholar Feed. |
| Scite (`SRC-103`) | **Failed.** Monthly free-tier quota (25 calls) exhausted; resets 2026-10-01. Identical to its state on 2026-09-06 (`SRC-002`). |

The pattern is worth stating plainly, because it shapes what this repository can
verify: the connectors that answered cover computer science and Wiley journals.
The philological journal literature of Indology — JAOS, ZDMG, IIJ, *Language* —
is reachable through none of them, and the open-access repository that holds the
one article this unit most needed is blocked at the proxy.
