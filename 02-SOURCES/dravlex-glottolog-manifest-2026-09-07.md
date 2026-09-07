# DravLex and Glottolog retrieval — 2026-09-07

Backing record for ledger rows `SRC-049`, `SRC-050`, `SRC-051`, and for the
egress characterisation `SRC-052`. Used by the domain M Brahui unit:
`03-REGISTERS/domain-m-brahui-position.csv`.

## Why these three and not the sources the question is actually about

Every archive, publisher and bibliographic API was refused at the egress
gateway at the time of retrieval (`SRC-052`, and the second status update
under `D-001`). Only `github.com` and `raw.githubusercontent.com` answered.
These three are what a Dravidian comparative question can be run on from
GitHub alone. They are **not** substitutes for Krishnamurti 2003 or DEDR,
which remain unread — see `HOLD-004` and `HOLD-002`.

## SRC-049 — DravLex (Kolipakam et al. 2018), CLDF derivation

| Field | Value |
|---|---|
| Repository | `lexibank/dravlex` |
| HEAD commit | `37578075e5ccb09c43022f7f1282125e748de84d` |
| Channel | `raw.githubusercontent.com`; HEAD pinned by `git ls-remote` |
| Retrieval (UTC) | 2026-09-07T03:12Z |
| Licence | CC-BY-4.0 |
| Local path | session scratch, not committed |

| File | sha256 |
|---|---|
| `cldf/forms.csv` | `c1b2c7f02cdddd6cfab67373d7eb50b6e27ddb592070b83de3a128899d055fde` |
| `cldf/cognates.csv` | `1eb8b6ddc6d07106c509ba38e601a2e18a65a1779336e8b6d47fb0996aff4c48` |
| `cldf/languages.csv` | `0f1d0c473f18eed7d90d69f832a2a421776d18f2f869c0d1f6351b634fad4a7b` |
| `cldf/parameters.csv` | `a8749d271220e54619c735d541d77b46ce12d756e3d7067d222f3de8abb98573` |
| `cldf/sources.bib` | `6b42dbfb9c437d240f518ead736a31b84349a21a357de3164cfd130c945f1edf` |
| `cldf/cldf-metadata.json` | `efb124cabded73d010ba8f409f6c891083789613985bb8f28fabce8627979da3` |

Shape: 2,127 forms, 20 varieties, 100 concepts, 778 expert-coded cognate
sets, 0 judgements flagged as doubtful, 141 forms flagged as loans.
Cognate-set identifiers are globally unique — none spans two concepts —
which is why the analysis keys on `Cognacy` directly.

**Underlying sources, from `cldf/sources.bib`.** Burrow and Emeneau 1961
(*DED*, first edition); Andronov 1964; **Krishnamurti 2003**; Buck 1949;
Kolipakam fieldnotes 2018. The third of these is the source whose
classification the dataset is used to test in `DMB-018`, which is why
`DEP-008` records the dependency and `DMB-021` caps the reading.

`04-AUDITS/north-dravidian-cognate-sharing.py` re-fetches `forms.csv` and
`cognates.csv` from this commit and verifies both hashes before counting
anything, so the measurement is reproducible without this scratch copy.

## SRC-050 — Glottolog CLDF languages table

| Field | Value |
|---|---|
| Repository | `glottolog/glottolog-cldf` |
| HEAD commit | `072ca0d0410039fb8b779be8fc165bac575d2cda` |
| File | `cldf/languages.csv` |
| sha256 | `1a50a393bc81568b656f9522be18aa4f80f38e94309ba6c863d583234adfbb89` |
| Retrieval (UTC) | 2026-09-07T03:10Z |

Coordinates present for all twenty DravLex glottocodes. One point per
languoid — an editorial simplification of a speech area, not a measured
centroid, and not dated. The twenty coordinates are transcribed into
`04-AUDITS/brahui-loo-geography.py`, which is therefore self-contained.

## SRC-051 — Glottolog languoid tree and reference bibliography

| Field | Value |
|---|---|
| Repository | `glottolog/glottolog` |
| HEAD commit | `8fdbc6f1347328f0bdb3333f7cf8a6fffe586ced` |
| Command | `git clone --depth 1 --filter=blob:none`, then `git sparse-checkout set languoids/tree/drav1251 references` |
| Retrieval (UTC) | 2026-09-07T03:07Z |

### The Dravidian tree as retrieved

```
drav1251  Dravidian
├── cent2227  Central Dravidian      subrefs: Krishnamurti 2003
├── nort2698  North Dravidian        subrefs: Krishnamurti 2003
│   ├── brah1256  Brahui  (language)
│   └── kuru1300  Kurux-Malto (family)  subrefs: Kobayashi & Tirkey 2017:11-14
│       ├── kuru1301  Kurukh          subrefs: Kobayashi & Tirkey 2017:9-10
│       └── malt1248  Malto           subrefs: Kobayashi & Tirkey 2017:11-14
├── sout3133  South Dravidian        subrefs: Krishnamurti 2003
└── unun9890  Unclassified Dravidian
```

Two things this shape settles, both used in the register:

1. Brahui is a **primary branch** of North Dravidian, sister to the whole
   Kurux–Malto unit, not a member of it (`DMB-009`). So the quantity
   diagnostic of the top node is what Brahui shares with Kurukh *and* Malto
   together, and it is measured separately from the lower node.
2. **Three of Glottolog's four Dravidian subgroups cite Krishnamurti 2003
   and nothing else.** The only node with a second, independent source is
   Kurux–Malto. Glottolog is therefore not independent corroboration of
   North Dravidian; it is one book re-encoded (`DEP-008`, `DMB-021`).

### Bibliography entries resolved

| Key | Citation |
|---|---|
| `hh:hv:Krishnamurti:Dravidian` | Krishnamurti, Bhadriraju. *The Dravidian Languages*. Cambridge: CUP, 2003. Cambridge Language Surveys, xxvii+545. ISBN 9780521771115, OCLC 57417931 |
| `hh:gtd:Kobayashi:Kurux` | Kobayashi, Masato and Bablu Tirkey. *The Kurux Language: Grammar, Texts, and Lexicon*. Leiden: Brill, 2017. Brill's Studies in South and Southwest Asian Languages 8, xvii+791 |
| `hh:v:McAlpin:Brahui` | McAlpin, David. "Is Brahui Really Dravidian?" *Proceedings of the Sixth Annual Meeting of the Berkeley Linguistics Society*, Berkeley: University of California, 1980, 66–73 |
| `hh:hv:McAlpin:Elamo-Dravidian:1974` | McAlpin, David. "Toward Proto-Elamo-Dravidian." *Language*, 1974, 89–101 |
| `hh:hv:McAlpin:Elamo-Dravidian:1975` | McAlpin, David. "Elamite and Dravidian: Further Evidence of Relationship." *Current Anthropology*, 1975, 105–115 |
| `asjp2010:1072` | Bray, Denys de. *The Brahui Language, Part II The Brahui Problem, Part III Etymological Vocabulary*. Delhi: Gian Publishing House, 1986 |
| `hh:sv:Emeneau:Brahui` | Emeneau, Murray Barnson. *Brahui and Dravidian Comparative Grammar*. Berkeley: University of California Press, 1962. UCPL 27, xi+91 |
| `hh:s:Elfenbein:Brahui` | Elfenbein, Josef. "Brahui." In Sanford B. Steever (ed.), *The Dravidian Languages*, London/New York: Routledge, 1998, 388–414 |
| `hh:v:Andronov:Brahui` | Andronov, M. S. "Historico-comparative notes on the Dravidian heritage of Brahui." *Indian Linguistics* 63, 2002, 1–11 |

**These are bibliographic records. Not one of these works was read.** Every
host that could serve them is blocked (`SRC-052`). `DMB-023` and `DMB-024`
are `PROVISIONAL` for exactly this reason, and no inference from a title to
a conclusion is licensed anywhere in this unit.

### A negative, typed

A regex over the `title` field of all thirty-plus files in
`references/bibtex/` returns **zero** entries naming *North Dravidian*,
*Northern Dravidian*, *Proto-North Dravidian*, *Kurukh and Malto* or
*Kurux-Malto*, against dozens naming Brahui, Kurux or Malto individually.
Within this bibliography — large and curated specifically for classification
— that is **ABSENT DESPITE ADEQUATE SEARCH** (`DMB-025`). It is not an
absence claim about the scholarly literature, which was not searchable.
