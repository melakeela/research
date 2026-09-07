# Domain A retrieval manifest — 2026-09-07

Backing record for ledger rows `SRC-069` through `SRC-085`.

Domain A is *Rigvedic chronology and transmission*, constitution §4.A. This
unit was commissioned to examine the programme's dependence on Arnold's
metrical strata rather than to use it, and to test whether any instrument
independent of Arnold is retrievable.

## 1. Retrieval channel

Only `github.com` and `raw.githubusercontent.com` answered. Fifteen other
hosts, including every archive and every bibliographic API, refused at
CONNECT. This is the third session in a row under this policy (`SRC-045`,
`SRC-052`, `SRC-069`) and it is the reason Arnold 1905 itself is still
unread here.

The five literature MCP connectors are reached through the Anthropic MCP
proxy and not through the egress lane, so three of them worked even though
the proxy's own status endpoint had logged a 403 at CONNECT for their
backends at session start. What each returned is in §4.

## 2. Corpus retrieval event

| Field | Value |
|---|---|
| Repository | `VedaWebProject/vedaweb-data` |
| Command | `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/VedaWebProject/vedaweb-data` |
| HEAD commit | `d3eb8af7324338161520d2d35eae8f7e985a19a5` |
| Commit date | 2025-06-13T07:07:10+00:00 |
| Retrieval date (UTC) | 2026-09-07T14:14Z |
| Local path | `/home/user/vedawebproject/vedaweb-data` (session-local, not committed) |

Six files were re-checksummed against `02-SOURCES/vedaweb-manifest-2026-09-07.md`
and all six reproduce exactly:

| sha256 | path |
|---|---|
| `7b99eb3da956b54bc45a0c77ba825b22599aec35cde794a3a3fe21fedaf21c10` | `versions/aufrecht.csv` |
| `484e657e32ab7304aece763c072a1fa75d4042ffc4513d1426ba248776e0ed75` | `info/strata.json` |
| `7ba145d984d5a669318e144fbd1b7154adf982827a5385f323ea7ef4e797a15b` | `TEI/vedaweb_corpus.tei` |
| `14f892794f32da89d1a6304b27209ebdfec9273f46e317f8811c32dd21105bee` | `versions/lubotsky.csv` |
| `2b4ba84dd5ca3d271e40c1cb5c64111bf7412376dac2915d627068d555dd6c11` | `versions/padapatha.csv` |
| `236269da756609ef371df54bfe0734c6fc6177060a4cbcdc1fa9dc047c3a8c4b` | `TEI/rv_book_02.tei` |

## 3. What was retrieved that earlier units had not used

Four files in the pinned corpus had never been opened in this repository
before. They are the reason this unit has anything independent of Arnold
to work with.

| File | Ledger | What it is | What it can support |
|---|---|---|---|
| `info/stanza_properties.json` | `SRC-072` | 2,372 stanzas carrying markings by **five** scholars — Grassmann 1876-7, Oldenberg 1888/1909/1912, Arnold 1897, Wüst 1928, Witzel 1995 — compiled by Gunkel and Scarlata | Four stratifications not by Arnold, two of them published **before** Arnold |
| `versions/vnh.csv` | `SRC-071` | the metrically restored text, Thomson and Slocum after van Nooten and Holland | the direct measurement of how far later sandhi has moved the transmitted text off its metrical form |
| `external-resources/Oldenberg/*.csv` | `SRC-073` | page concordance to Oldenberg's *Noten*, 6,064 rows | which stanzas Oldenberg wrote a textual note on — an attention map, not an opinion |
| `info/addressees.json` | `SRC-076` | hymn addressee and collection group | the arrangement analysis |

Three mark-key gaps are open and are held, not guessed:

- the code letters in `stanza_properties.json` (`G`, `O`/`o`, `C1`/`C2`,
  `W`/`w`, `Z`/`z`) have no key in the repository — `HOLD-007`;
- the eight editorial mark characters in `vnh.csv` have no key —
  `HOLD-008`;
- the *Noten* themselves are at Heidelberg, which is blocked — `HOLD-006`.

One provenance anomaly is recorded and not followed: the
`stanza_properties` `publicationStmt` carries
`<ptr target="http://digitalcommons.unl.edu/zeabook/55"/>`, a University of
Nebraska e-book series unrelated to any of the six works named in its own
`sourceDesc`.

## 4. What each MCP literature connector returned

| Connector | Ledger | Result |
|---|---|---|
| **Consensus** | `SRC-077` | **Worked and was decisive.** Returned the full abstract of Hellwig et al. 2021 *Reassessing Rigvedic Strata* (JAOS) — the paper this unit was told to establish the scope of — plus Ryan 2021 on Vedic diphthongs (JAOS), Hellwig 2020 on Bayesian dating, Pincott 1884 and 1887 (JRAS) on the arrangement of the hymns, Candotti 2011 on the *chandasi* rules quoting Renou 1941, Scharf 2005/2008 on Pāṇini and the Vedic subjunctive, Deshpande 2002 on the *padapāṭha*s and *prātiśākhya*s, Scarlata et al. 2024 and 2025. Abstracts only; author lists truncated to "et al."; one call refused for rate limiting. |
| **Scholar Gateway** | `SRC-078` | Worked; returned nothing on the question. 15 passages across 12 articles, every one a Wiley title. No article on Rigvedic stratification, Arnold or Oldenberg. A corpus-coverage limit, not an absence of literature. |
| **Scholar Feed** | `SRC-079` | Worked; arXiv cs.CL only. Four computational papers on Rigvedic chronology, none philological. |
| **alphaXiv** | `SRC-081` | Worked; arXiv only; overlapped Scholar Feed. |
| **Scite** | `SRC-080` | **Refused.** Monthly MCP quota (25 calls) exhausted, resets 2026-10-01. The one connector that reads full text and citation context is the one unavailable, so Hellwig et al. 2021 could not be read beyond its abstract. |

The pattern is worth stating plainly, because it shapes what this unit
could do: **every connector that reaches this domain's literature returns
abstracts, and the only connector that returns full text is out of quota.**
Domain A's evidence is in JAOS, the *Indo-Iranian Journal*, ZDMG,
*Indogermanische Forschungen* and JRAS. Three of the five connectors index
arXiv or Wiley and cannot see any of it.

## 5. Scripts

| Script | What it does |
|---|---|
| `04-AUDITS/domain-a-build.py` | aligns the pāda, stanza and hymn layers of the pinned corpus into three TSVs |
| `04-AUDITS/domain-a-measure.py` | ten measurement blocks: corpus shape, Arnold against book order, the five stratifications, Oldenberg's attention map, arrangement, saṃhitāpāṭha against the restored text, padapāṭha, the structural zeros, restoration by book and stratum, the eight dates |
| `04-AUDITS/domain-a-morphology.py` | the Zürich annotation used as its own instrument: seventeen inflectional categories by book and by stratum |

All three are deterministic and take the pinned commit as their only input.

## 6. Domains requested

Added to what `D-001` asks for: `digi.ub.uni-heidelberg.de` (the digitised
Oldenberg *Noten* the corpus itself points at). `archive.org` is requested
again, for Arnold 1905.
