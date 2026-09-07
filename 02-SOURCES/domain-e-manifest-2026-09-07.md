# Domain E retrieval manifest — 2026-09-07

Backing record for ledger rows `SRC-048` through `SRC-063`.

## 1. The egress regression this session

The session of 2026-09-07 that produced `SRC-025`, `SRC-027`–`SRC-031`
and `SRC-033` recorded `archive.org`, `indianculture.gov.in`,
`gretil.sub.uni-goettingen.de`, `en.wikipedia.org`, `arxiv.org`,
`doi.org` and `titus.uni-frankfurt.de` as **reachable**. In the present
session they are not. Every one of them is refused at the egress
gateway, on **both** available channels — `curl` through the container
proxy and the `WebFetch` service, which are separate paths.

This is not a correction of the earlier probes. Those probes returned
HTTP 200 with byte counts, and one of them (`SRC-026`) produced a
1,054,774-byte file whose sha256 is recorded. The earlier reachability
was real. The environment's network policy has narrowed between the two
sessions. Both readings stand for their own date; neither supersedes the
other. What is superseded is the *inference* that these domains are
available to future units of work.

The task for this unit named GRETIL, archive.org and TITUS specifically
as places to look for a DEDR or other Dravidian etymological source.
All three were probed. All three are blocked. That result is logged as
`SRC-048`–`SRC-050` rather than passed over.

Reachable in this session: `github.com` through the session git proxy's
anonymous read lane, `raw.githubusercontent.com`, and
`api.github.com` **only** for repository-scoped endpoints on
`melakeela/research`. `api.github.com/search/*` is refused with
*"sessions are bound to their configured repositories."*

## 2. What was retrieved instead

The git proxy's anonymous lane serves arbitrary public repositories,
which the GitHub REST API in this session does not. That single open
channel carried three retrievals.

### 2.1 VedaWeb Rigveda data — re-retrieval and verification

`VedaWebProject/vedaweb-data`, `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1`.

| Field | Value |
|---|---|
| HEAD | `d3eb8af7324338161520d2d35eae8f7e985a19a5` |
| Commit date | 2025-06-13T07:07:10+00:00 |
| Local path | `/home/user/vedawebproject/vedaweb-data` (session-local) |
| Licence | CC-BY-4.0 |

The clone was made fresh because the container of the earlier session
was reclaimed. Three files were re-hashed against
`02-SOURCES/vedaweb-manifest-2026-09-07.md` and match exactly:

| file | sha256 | manifest |
|---|---|---|
| `rigveda/versions/aufrecht.csv` | `7b99eb3d…af21c10` | match |
| `rigveda/info/strata.json` | `484e657e…6e0ed75` | match |
| `rigveda/TEI/vedaweb_corpus.tei` | `7ba145d9…97a15b` | match |

The manifest is therefore reproducible from the commit SHA alone, which
is what it was written to guarantee.

### 2.2 JAMBU — `moli-mandala/data`

The CLDF database behind Jambu, a historical-linguistic database for
South Asian languages (Arora et al., arXiv:2306.02514).

| Field | Value |
|---|---|
| HEAD | `dbae3102fe779aa60f5ef03108f7918ab2ede006` |
| Commit date | 2026-08-30T04:37:14-07:00 |
| Local path | `/tmp/jambu` (session-local) |
| Working tree | 3,049 files, 654 MB |

`cldf/forms.csv` is a 112 MB Git-LFS pointer and was **not** fetched;
git-lfs is absent from this container. Nothing below depends on it. The
per-source raw tables under `data/` are ordinary files and are complete.

| sha256 | bytes | path |
|---|---|---|
| `1d91f819b9af2c530ba6688a089a775d4bd6bcaa7c8e30e90dacdcce3758943e` | 5251799 | `data/dedr/dedr.csv` |
| `2f561c446d3c73f434f71dc2ec5e7b4cf827779f645a8570501baa5d0afcb529` | 5435150 | `data/dedr/dedr_new.csv` |
| `95beb73b1f9c36d42ecb671df4d8bb01eea27641dffa802ca8c33e5343ceafa9` | 67311 | `data/dedr/pdr.csv` |
| `6b9049af82b82a3b8c42dcd637341ac1a48978d46de2c287c7f1316140c2ed71` | 82802 | `data/dedr/params.csv` |
| `11e8963f8b1ea757b80829fe60dcf5e4d2d9fa899273b45d534d97511d449ea6` | 42562 | `data/munda/forms.csv` |
| `6130838e68cb2bef8ceb98b69014dccbaff64d5b558cff295fc81c6956fd9310` | 16287 | `data/munda/params.csv` |
| `b634f283a3fe67ba082c5999e16e9fe13419ae8fbc4bf9b67a8ca161acf5aed2` | 34895 | `data/munda/rau_2019.csv` |
| `a44be9f9f5d8a5981a79e3391c8d9e0281c923b781af0029fdd605ea7b774054` | 8316306 | `data/cdial/cdial.csv` |
| `f375be2b786375e14ea94df551dffe1f31ed98cccc0f6f71cb6b15870809a8c6` | 2460557 | `data/cdial/params.csv` |
| `ce9f9e458ebe6f549bdd4c6ad5d15fe2759ae816be184ff55c09fedd923aa013` | 84946 | `data/cdial-dravidian-mention-audit.csv` |
| `5bf5cd616f36e2bda5824f19be4c8a35fc2ebf43770e8255908af1eb14e01577` | 26922 | `cldf/languages.csv` |
| `f80c32a5c5f9a41a5378b03086bb379097650ee90e532f7f77b9346e1b76ff9d` | 219632 | `cldf/references.csv` |

### 2.3 DravLex — `lexibank/dravlex`

CLDF of Kolipakam, Dunn, Jordan and Verkerk 2018, a 20-variety /
100-concept cognate-coded Dravidian wordlist. CC-BY-4.0.

| Field | Value |
|---|---|
| HEAD | `37578075e5ccb09c43022f7f1282125e748de84d` |
| Commit date | 2025-06-11T20:45:58+12:00 |
| Local path | `/tmp/dravlex` (session-local) |

## 3. Provenance of the DEDR text, stated exactly

This matters more than the checksums, because it caps what any count
taken from it can claim.

`cldf/references.csv` row `dedr` names the source as **Burrow and
Emeneau, *A Dravidian Etymological Dictionary*, 2nd edition, Clarendon
Press, Oxford, 1984**, and gives its URL as
`https://dsal.uchicago.edu/dictionaries/burrow/` — the Digital
Dictionaries of South Asia digitization. That row also records
`Editor = Aryaman Arora`, `OCR = No`, `Provenance = data/dedr/dedr_new.csv`.

So the chain is:

    Burrow & Emeneau 1984 (print)
      → DSAL digitization (dsal.uchicago.edu — EGRESS_BLOCKED here)
        → JAMBU re-parse and edit by Arora (data/dedr/*.csv — retrieved)

**We do not have DEDR. We have a reachable derivative of DEDR at two
removes, and the intermediate stage is the very domain the egress policy
refuses.** No claim resting on it may be entered as `VERIFIED` against
"DEDR" as such. Counts over the retrieved table are `VERIFIED` as counts
*over the retrieved table*; anything asserted about the printed
dictionary is `PROVISIONAL` at best. The distinction is kept in every
row of `03-REGISTERS/domain-e-measurements.csv`.

The same applies to CDIAL: `data/cdial/params.csv` is a digitization of
Turner, *A Comparative Dictionary of the Indo-Aryan Languages* (Oxford,
1962–66), reached at the same remove.

## 4. What each retrieved layer can and cannot support

| Layer | File | Supports | Does **not** support |
|---|---|---|---|
| DEDR reflexes | `data/dedr/dedr.csv` | attested Dravidian forms by language, under a DEDR entry number | Proto-Dravidian: DEDR states no reconstructions |
| PDr reconstructions | `data/dedr/pdr.csv` | reconstructed Proto-Dravidian, attributed to Krishnamurti | attestation; these are starred forms |
| Munda reflexes | `data/munda/forms.csv` | attested Munda forms in 12 languages | Proto-Munda; and nothing about the northwest |
| Rau 2019 | `data/munda/rau_2019.csv` | reconstructed Proto-Munda etyma with per-language reflex sources | pre-Proto-Munda; Rau's own reconstruction only |
| MKCD / Pinnow columns | `data/munda/rau_2019.csv`, `params.csv` | deeper Austroasiatic comparanda (Shorto; Pinnow) | Munda in South Asia's northwest |
| CDIAL | `data/cdial/params.csv` | Turner's Indo-Aryan entries with his own etymological brackets and first-attestation tags | independent confirmation of Turner's attributions |
| CDIAL→DEDR audit | `data/cdial-dravidian-mention-audit.csv` | which CDIAL Dravidian mentions JAMBU's editor could resolve to a DEDR entry | any editorial judgement beyond Arora's |
| DravLex | `/tmp/dravlex/cldf/` | cognate-coded attested Dravidian, 20 varieties × 100 concepts | Proto-Dravidian forms; it codes cognacy, not reconstruction |
| VedaWeb Zürich | TEI `source="zurich"` token layer | lemma and morphology per Rigvedic token | etymology of any kind |
| Arnold strata | `rigveda/info/strata.json` | one metrical stratum code per pāda | absolute dates; and it is Arnold 1905 alone (`DEP-001`) |

**No source retrieved in this session speaks to Para-Munda, to the
Kubhā-Vipāś prefixing language, or to Masica's Language X.** Those are
proposals in the secondary literature, and that literature —
Witzel 1999, Kuiper 1991, Masica 1979 — remains unretrieved. This is
recorded as a hold, not glossed over.
