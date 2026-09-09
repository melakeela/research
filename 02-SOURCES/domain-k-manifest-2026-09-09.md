# Domain K retrieval manifest — 2026-09-09

Backing record for ledger rows `SRC-099` through `SRC-116` and dependency
rows `DEP-029` through `DEP-033`.

## 1. What was asked for, and what answered

The task named four things to probe: Mahadevan's concordance, the Wells
sign list, ASI excavation reports, and any machine-readable sign corpus
on GitHub, with the outcome logged either way. All four were probed.
Three are blocked and one answered.

| Target | Ledger row | Outcome |
|---|---|---|
| Mahadevan 1977 concordance (archive.org) | `SRC-109` | refused, gateway 403 |
| Wells sign list / ICIT (epigraphica.de, tu-berlin) | `SRC-110` | refused, gateway 403; and access is by request to the administrator in any case |
| ASI publications and excavation reports (asi.nic.in) | `SRC-111` | refused, gateway 403 |
| Machine-readable sign corpus on GitHub | `SRC-102`, `SRC-103` | **retrieved** |

Two further GitHub datasets were retrieved and are logged with what they
can and cannot carry: `SRC-104` (a decipherment claim) and `SRC-105` (327
seal photographs and a spreadsheet of 135 rows scraped from harappa.com
captions, locating 38 of them even to a site). This manifest's first
reading said `SRC-105` had no provenance table; the file is `.xlsx` and
its README says csv. `BF-027`.

## 2. The channel picture on 2026-09-09

Reachable: the session git proxy's anonymous read lane for public GitHub
repositories (`SRC-101`), and `raw.githubusercontent.com`.

Refused at the gateway, on `curl` and on `WebFetch` alike: `harappa.com`,
`archive.org`, `asi.nic.in`, `epigraphica.de`, `www.user.tu-berlin.de`,
`arxiv.org` and its API, `pnas.org`, `nature.com`, `researchgate.net`,
`zenodo.org`, `persee.fr`, `doi.org`, `api.openalex.org`,
`api.crossref.org` (`SRC-099`, `SRC-113`).

Refused or unauthenticated on the connector lane: Scite (monthly limit,
resets 2026-10-01), Scholar Feed, Consensus, alphaXiv, Scholar Gateway
(`SRC-108`).

Repository-scoped only: the GitHub REST API, which now refuses
`/search/*` **and** `/repos/{owner}/{repo}` for repositories outside
`melakeela/research` (`SRC-100`). This is a narrowing since `SRC-057`.
Repository names therefore had to be discovered by WebSearch
(`SRC-115`) and then fetched over the git lane. WebSearch is logged as a
discovery channel; nothing it asserted is entered as a claim.

`codeload.github.com` answers 403, so the tarball route is not an
alternative to the git protocol.

## 3. The shape of the asymmetry, stated before any analysis

The Rigvedic side of this domain is retrievable at full text, with
morphological annotation, in a corpus this repository has already pinned
four times (`SRC-106`, `SRC-107`).

The Indus side is retrievable only as one annotator's partial
digitization of a print corpus that cannot be opened here (`SRC-102`,
`DEP-029`), covering 179 objects from one site.

No excavation report, no find-spot table, no museum catalogue and no
peer-reviewed article on Indus writing was read in this session.

That asymmetry is not a finding about the ancient world. It is a fact
about this session's network policy, and it runs in the direction that
would flatter a Rigveda-centred account of the evidence if it were left
unstated. It is stated here, it is carried into
`04-AUDITS/domain-k-method.md` §5 as the first item of the
prestige-bias challenge, and it is the reason `HOLD-008` exists.

## 4. Pinned artefacts

| Clone | Commit | Verification |
|---|---|---|
| `mayig/indus-valley-script-corpus` | `ad2f1e218a34b8c33c57de0d6cb8d99272765bbb` (2025-04-16) | 179 corpus JSON + 397 feature JSON; concatenated sha256 `96d0174e29cc74b07b6e60bb9d278ee9f7bc206475c778892deb7127e7b30f11` |
| `ramnerd/IVC_script_decoded` | `982d621384ce8a0230f9925d39e84b07de82dd47` (2026-08-10) | `dataset/dataset_IVC.csv`, 556 rows, no header, no artefact ids |
| `akksshhaay/Indus-Seal-Dataset` | `536a7e2218ab06255ca2863f032431453afc6d92` (2021-02-02) | 329 files: 327 JPEGs, a README, and `ExhaustiveDatabaseOfSeals.xlsx` with 135 data rows, 38 carrying a location and 18 a date (`DK-M-022`–`DK-M-024`, `BF-027`) |
| `VedaWebProject/vedaweb-data` | `d3eb8af7324338161520d2d35eae8f7e985a19a5` (2025-06-13) | identical to the commit pinned at `SRC-019`/`SRC-047`/`SRC-069`/`SRC-085`; `lubotsky.csv` sha256 `14f89279…05bee`, `aufrecht.csv` sha256 `7b99eb3d…af21c10` |

Derived: `rv_tokens.tsv`, 164,758 tokens, sha256
`e6a33556744952772c14f59bdb7ef82d2a5ed9f4dd298c06cf148064150fc5e4`,
produced by `04-AUDITS/rv-token-extract.py` from the VedaWeb TEI. The
token total matches the total reported for the same commit in the
pur- family and várṇa- units, so the extraction reproduces across
sessions.

Clones live outside the working tree and are not committed; they are
re-creatable from the commit hashes above.

## 5. Domains requested and refused

For the PR's "Domains requested" list: `www.harappa.com`,
`archive.org`, `ia801604.us.archive.org`, `asi.nic.in`,
`www.epigraphica.de`, `www.user.tu-berlin.de`, `arxiv.org`,
`export.arxiv.org`, `www.pnas.org`, `www.nature.com`,
`www.researchgate.net`, `zenodo.org`, `www.persee.fr`, `doi.org`,
`api.openalex.org`, `api.crossref.org`, `codeload.github.com`,
`api.github.com` (non-repository-scoped paths), `mcp.scholarfeed.org`,
`mcp.consensus.app`, `connector.scholargateway.ai`, `api.alphaxiv.org`,
`api.scite.ai`.
