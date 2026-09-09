# HOLD-008 — the Indus corpus and its literature are unretrieved

**Opened:** 2026-09-09
**Domain:** K (Indus writing and institutional discontinuity); packet R20
**Ledger rows:** `SRC-099`, `SRC-108`–`SRC-114`
**Blocks:** §4.K's seals, sealings, tablets, proposed functions,
durability, distribution, post-urban survival, whether the script had
become unreadable, and institutional rupture — that is, everything in the
domain except the Rigvedic half.

## What is needed

| Work | Why it is load-bearing | Where it might be | Ledger |
|---|---|---|---|
| Mahadevan, *The Indus Script: Texts, Concordance and Tables*, ASI Memoirs 1977 | the foundational corpus publication; the source of every object count, sign frequency and find-spot table quoted at second hand anywhere in this repository or on the platform | archive.org item located but refused | `SRC-109` |
| Wells 2015 sign list, and ICIT (Wells and Fuls) | the second and third sign lists; the only route to checking the crosswalk measured at `DK-M-013` | epigraphica.de, tu-berlin.de; access also by request to the administrator | `SRC-110` |
| CISI, Joshi and Parpola 1987; Shah and Parpola 1991; Parpola et al. 2010 | the corpus the one retrievable dataset digitises; carries the find-spot, material and museum data that dataset drops | print; not located online | `DEP-029` |
| Mukhopadhyay 2023, *Humanities and Social Sciences Communications* | the find-spot argument for the administrative reading — seals near gates and workshops, sealings on storage locks, Kanmer pendants — cited on `melakeela/site` and unreachable here | nature.com, refused | `SRC-113` |
| ASI excavation reports and *Indian Archaeology — A Review* | stratigraphy, context and dating for every object class in §4.K | asi.nic.in, refused | `SRC-111` |
| Rao et al. 2009 (*Science*) and Farmer, Sproat and Witzel 2004 (*EJVS*) | the two poles of the is-it-writing dispute, `DK-H-001` and `DK-H-011` | pnas.org, arxiv.org, ejvs — all refused | `SRC-114` |
| Any cuneiform corpus | to search for a Mesopotamian mention of Meluhhan writing or scribes — `DK-A-013`, the most answerable open question in the domain | not probed by name this session; every comparable host refused | `SRC-099` |

## Why it is blocked

Sixteen hosts were probed on 2026-09-08/09 and every one was refused at
the egress gateway with `CONNECT tunnel failed, response 403`:
`harappa.com`, `archive.org`, `asi.nic.in`, `epigraphica.de`,
`www.user.tu-berlin.de`, `arxiv.org` and its API, `pnas.org`,
`nature.com`, `researchgate.net`, `zenodo.org`, `persee.fr`, `doi.org`,
`api.openalex.org`, `api.crossref.org`. `WebFetch` refuses the same hosts,
so it is not a second channel. Every literature connector is
quota-exhausted or unauthenticated (`SRC-108`).

The one open channel is the git proxy's anonymous lane, which reached
three GitHub datasets (`SRC-102`, `SRC-104`, `SRC-105`) and the Rigveda
(`SRC-106`).

## What this hold does and does not permit

**Permits.** Measuring the retrieved digitization and saying exactly what
it is; measuring the Rigvedic side in full; typing the absences; gating
the hypotheses as source-blocked; naming what each blocked source would
decide.

**Forbids.** Any claim about Indus find-spot distribution, object-class
proportions, stratigraphy, chronology, post-urban survival or seal
function. Any statement of the form "the Indus corpus contains N objects"
or "the longest text is N signs". Any characterisation of what Parpola,
Mahadevan, Wells, Fuls, Rao, Farmer or Mukhopadhyay argued. Any
comparison between the Rigvedic measurements and the Indus material.

**Specifically forbids the conclusion the shape of this session invites.**
The Rigvedic half of this domain was measurable and the Indus half was
not. A unit that reports a rich Rigvedic result against an empty Indus
column, and then explains the emptiness historically, has converted its
own network policy into a finding. `04-AUDITS/domain-k-method.md` §5
carries this as the first item of the prestige-bias challenge and
`APA-K-004` audits it as a property of this record.

## What would close it

Any one of: an allowlist covering `archive.org` and `nature.com`; a
reachable cuneiform corpus; an ICIT access grant; or a Codex-side
retrieval of Mahadevan 1977 with its tables. Partial closure is useful
here — Mahadevan 1977 alone would settle `RA-022` and `IC-K-001`.
