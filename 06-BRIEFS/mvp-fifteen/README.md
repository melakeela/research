# MVP fifteen — page briefs

**Written:** 2026-09-08
**Unit type:** page briefs. One per page in the curatorial audit's MVP set.
Fifteen briefs, `01-index.md` to `15-the-archive.md`, in the workbook's rank
order. This README is the index and the shared-gate reference; it is not a
sixteenth brief.
**Built by:** `04-AUDITS/mvp-fifteen-briefs-build.py`.
**Inputs:** `13-PRODUCT-ARCHITECTURE/museum-framework.md` (every design
proposition `HYPOTHESIS`, per its own §14.4);
`01-INHERITED/curatorial-audit-v1.1/` (`INHERITED-UNVERIFIED` without
exception); `03-REGISTERS/` scanned for `supports_page`;
`02-SOURCES/access-ledger.csv` for retrieval capability.

**No retrieval was performed for this unit.** No row was added to
`02-SOURCES/access-ledger.csv`; no claim moved status; no domain was requested.
A brief is a statement of what a page would have to be and what it would have
to rest on. **None of it is public copy**, and no sentence in it may be lifted
onto a page.

---

## 1. The fifteen

| # | Slug | Environment / posture | Decision | Risk | Lowest status of its evidence |
|---:|---|---|---|---|---|
| 1 | [`index`](01-index.md) | Nocturnal Veḷi — *not yet known* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |
| 2 | [`enter`](02-enter.md) | Tamil Retrofuture — *known against an official account* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |
| 3 | [`artifact-atlas`](03-artifact-atlas.md) | Living Signal Field — *known by relation* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 4 | [`veli`](04-veli.md) | Nocturnal Veḷi — *not yet known* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 5 | [`tinai`](05-tinai.md) | Living Tiṇai — *known through place and material* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 6 | [`the-ledger`](06-the-ledger.md) | Reading Room — *known by argument from sources* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 7 | [`keeladi`](07-keeladi.md) | Living Tiṇai — *known through place and material* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 8 | [`before-the-indus`](08-before-the-indus.md) | Nocturnal Veḷi — *not yet known* | `Hold` | `Critical` | `INHERITED-UNVERIFIED` |
| 9 | [`the-water-city`](09-the-water-city.md) | Living Tiṇai — *known through place and material* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 10 | [`kural`](10-kural.md) | Tamil Retrofuture — *known against an official account* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |
| 11 | [`sound-changes`](11-sound-changes.md) | Living Signal Field — *known by relation* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |
| 12 | [`the-languages-we-lost`](12-the-languages-we-lost.md) | Nocturnal Veḷi — *not yet known* | `Keep` | `Low` | `INHERITED-UNVERIFIED` |
| 13 | [`the-other-laws`](13-the-other-laws.md) | Tamil Retrofuture — *known against an official account* | `Split` | `Low` | `INHERITED-UNVERIFIED` |
| 14 | [`custody`](14-custody.md) | Extraction / Collection — *known but withheld* | `Keep` | `Medium` | `INHERITED-UNVERIFIED` |
| 15 | [`the-archive`](15-the-archive.md) | Extraction / Collection — *known but withheld* | `Revise` | `Medium` | `INHERITED-UNVERIFIED` |

---

## 2. The finding that applies to all fifteen

**No page in the MVP set has a single register row behind it.**

A scan of every register in `03-REGISTERS/` carrying a `supports_page` column
(14 files) returns **zero rows naming any of the fifteen slugs**. The
`supports_page` values actually in use are *forts (proposed)*, *substrate
(proposed)*, *geography (proposed)*, `what-varna-meant.html`,
`the-northwest-cousin.html`, `the-killed.html`, `brahui`, *atlas layer* and
*method*. `03-REGISTERS/inherited-claims.csv` holds 369 rows, all
`INHERITED-UNVERIFIED`, and **all 369 have an empty `supports_page`**.

Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the
atlas entry or exhibit it feeds, and *"evidence that supports nothing is not
collected."* Read the other way round, which is the way that matters here: on the
repository's own accounting, **the launch set is supported by nothing**.

Three consequences, and they are the shape of the whole unit:

1. **The lowest status is the same on every page.** Nothing bearing on any of the
   fifteen stands above `INHERITED-UNVERIFIED`. Where each brief names inherited
   rows, they are rows that *bear on* the page, not rows that support it.
2. **No public copy may be drafted for any of them.** Method step 14 draws public
   copy from accepted claims. There are none. Each brief therefore states its
   page's QUESTION and leaves the other six step-14 slots open with the reason.
3. **Almost every asset in the register is embargoed.** Framework §3.12: *"a
   derived asset may not be commissioned or published while the claim it depicts
   is `INHERITED-UNVERIFIED` or `HOLD`."* Eight of the fifteen asset sets contain
   a `claim-specific diagram`; all eight are blocked. This is the framework
   resolving `SCHEMA.md` §4's finding 3 — 50 claim-specific diagrams scheduled by
   MVP priority, which is driven by low risk, i.e. by the pages least examined.
   Under §3.12 the diagram schedule is a function of the verification schedule
   and cannot invert it.

**And the workbook's `Risk` column is not a measure of truth.** `method-limits.csv`
states it: *"Risk means verification priority, not falsehood"*, and *"a visible
bibliography does not prove claim-level support or source quality."* Two of the
starkest cases sit in this set — `artifact-atlas`, rated `Low` on 88
bibliography entries against 8 words of prose, and `the-archive`, rated `Medium`
with 1 source entry under 5 tables.

---

## 3. What can actually be verified in this session

Of the fifteen units of work named in the briefs, **three have a live retrieval
route** with the access this session has, and they are the ones to run first:

| Unit | Page | Route | Ceiling |
|---|---|---|---|
| **MVP-U4** | `veli` | DEDR/JAMBU (`SRC-060`, `SRC-061`), Proto-Dravidian (`SRC-062`), DravLex (`SRC-067`) | `PROVISIONAL` — single digitisation lineage (§3.2) |
| **MVP-U12** | `the-languages-we-lost` | Glottolog CLDF and languoid tree (`SRC-050`, `SRC-051`) | `PROVISIONAL` — one aggregating classification |
| **MVP-U11** (lexical half only) | `sound-changes` | same Dravidian lexical lane | `PROVISIONAL`; epigraphic half blocked |

Two more need no retrieval at all and are executable immediately: **MVP-U1**
(threshold claim decomposition, `index`) and **MVP-U6** (re-deriving the ledger
rule in-repository, `the-ledger`), plus the structural half of **MVP-U14**
(creating the Obligations, Consent and Community Authority registers).

**The rest are blocked, and the block is documented rather than assumed.**
`SRC-052` characterises the session's egress as `github.com` and
`raw.githubusercontent.com` only; `SRC-080` to `SRC-083` record GRETIL, the
Internet Archive, TITUS, sacred-texts and wisdomlib refused on re-probe at
2026-09-07T15:10Z. `SRC-027` records `indianculture.gov.in` reachable earlier the
same day, which the later characterisation supersedes — so re-probing is the
first action of any unit that needs it, not an assumption in any brief.

**Two things escalate rather than block.** `IH-215` names an outreach to Dr. G.
Sundar of the Roja Muthiah Research Library as *"the most important single
verification task in the file"* and records that nothing has been sent to any of
the nine outreach roles. Institutional access is one of `CLAUDE.md`'s five
escalation categories: that is an owner action, not a `HOLD` row. The same
applies to the audited archive `veli-site(3).zip` itself, which is not in this
repository and has no ledger row — which is why every figure in the workbook is
`INHERITED-UNVERIFIED` rather than merely unchecked.

**`05-HOLDS/` rows are owed** for: the deployed build and the audited archive
(`enter`, `artifact-atlas`); the Tolkāppiyam *Poruḷatikāram* (`tinai`); Kenoyer
et al. 1983 and Chattopadhyaya 1996 (`before-the-indus`); the Keeladi report
chain (`keeladi`); the Indus excavation literature (`the-water-city`); a citable
Tirukkuṟaḷ edition if the git lane does not serve one (`kural`); a Tamil-Brahmi
epigraphic corpus (`sound-changes`); the isolate comparative literature
(`the-languages-we-lost`); Aktor and Davis (`the-other-laws`).

---

## 4. The shared gates

Every brief's §5 lists what its page needs **beyond** these. These apply to all
fifteen and are not repeated in the briefs.

### The workbook's release gates (`summary.csv`, `INHERITED-UNVERIFIED`)

1. Claim-level citation review
2. Cross-page consistency review
3. Image rights and provenance
4. Specialist/community review where relevant
5. Browser, accessibility and mobile testing
6. Prototype approval before migration
7. Confirm production domain and deployment allowlist

### The workbook's *Not completed* list (`method-limits.csv`)

Full primary-source re-performance · legal opinion · community consultation ·
image-rights clearance · discipline-specific peer review. The sheet is explicit
that *"these are publication gates, not optional polish."*

### Framework and constitution gates

| | Gate | Source |
|---|---|---|
| **F1** | Source Mode is reachable from the page | §1.7 — mandatory in all seven postures |
| **F2** | Every displayed claim is a Claim Object with a **computed** status; no editor can type `VERIFIED` and the CMS has no status dropdown | §3.1–§3.2 |
| **F3** | The posture is recorded in the Editorial Register with `derived_posture`, `assigned_posture` and, where they differ, a non-empty `override_reason` | §1.5, §11.5 — **this register does not exist** |
| **F4** | No derived asset is commissioned or published while the claim it depicts is `INHERITED-UNVERIFIED` or `HOLD` | §3.12 |
| **F5** | Both adversarial tests are run **as a pair** and logged whether or not they found anything, with the asymmetry statement | §3.11, §11.2, constitution §8 |
| **F6** | Every absence argument is typed under the negative-evidence standard | constitution §6 |
| **F7** | Every consequential ancient word carries a Translation Block | constitution §7, §3.8 |
| **F8** | Proportionality: allocated space is compared against evidential weight at review | §3.10, method step 9 |
| **F9** | Falsifiers are recorded for every load-bearing claim | §3.9, method step 12 |
| **F10** | Step 13 has been run — MelaKeela checked against itself for contradictions, outdated claims, duplicate pages and terminology drift | method step 13 |

### The repository-level gate

**R1.** At least one claim with `supports_page` naming the slug, at a status
above `INHERITED-UNVERIFIED`. **No page in the set passes R1 today.**

---

## 5. Open owner decisions that block pages in this set

None of these is a research question and none can be closed by retrieval. They
are listed with the pages they block, not re-argued; the argument is in
`DECISIONS-NEEDED.md` and the authoritative status is in
`09-DECISIONS/OWNER-DECISIONS.csv`.

| Decision | Question | Blocks |
|---|---|---|
| **D-032** | Does `before-the-indus` launch, or come out of the MVP set? | `before-the-indus`; and the release's shape — see §6 |
| **D-033** | Which build is authoritative; is `rakhigarhi` live? | `enter`, `artifact-atlas`, `the-water-city` |
| **D-034** | The page count and the atlas site count | `index`, `enter`, `artifact-atlas` |
| **D-004** (`OWNER-DECISIONS.csv`) | What Veḷi principally is | `index`, `veli` |
| **D-006** (`OWNER-DECISIONS.csv`) | Keezhadi or an inscription as the children's pilot | `keeladi`, and Field Mode for `tinai` and `the-water-city` |
| **D-010** (`OWNER-DECISIONS.csv`) | Which institutional claims may presently be published | `keeladi`, `custody`, `the-archive`, `the-other-laws` |
| **D-015** | Is Reading Room a seventh peer posture or demoted to Source Mode? | `the-ledger` |
| **D-016** | May Reconnection surfaces publish before community-led work exists? | `custody`, `the-languages-we-lost` |
| **D-025** | Are refused and unanswered obligations published individually, in aggregate, or only with notice? | `custody`, `the-archive` |
| **D-029** | Does the institution assert fair dealing, and in which jurisdiction? | `kural`, `the-other-laws` |

**This unit raises no new `D-` identifier.** Everything it found was already
carried by an existing decision, which is the correct outcome: `CLAUDE.md`
allocates a new identifier from `OWNER-DECISIONS.csv`, never from the highest
number visible in a document, and a brief that manufactures decisions inflates
the namespace it is meant to read from.

---

## 6. The `before-the-indus` conflict, recorded and not resolved

`before-the-indus` is **MVP rank 8** in `mvp.csv`, `MVP = Yes` in
`page-audit.csv` and `Priority = MVP` in `asset-register.csv` — and in the same
sheets it is `Decision = Hold`, `Risk = Critical`, with the release dependency
*"Withhold from MVP until load-bearing claims receive claim-level citations and
specialist/editorial review."* It is the only one of the fifteen in this state
and the only Critical-risk page in the launch set.

It is already carried as **D-032** in `DECISIONS-NEEDED.md`, with a row in
`09-DECISIONS/OWNER-DECISIONS.csv`, raised 2026-09-07 and renumbered from D-004
the same day (`09-DECISIONS/DECISION-ID-MAP.csv`). Category: *two consequential
positions both remaining viable / publication approval*.

**This unit records the conflict and takes no position on it.** The full record,
including what each arm changes and what neither changes, is in
`08-before-the-indus.md` §7. Nothing elsewhere in these briefs assumes an
outcome: `09-the-water-city.md` notes that the *Meluhha and Indus* exhibit
sequence loses a second member under one arm, and states it conditionally.

---

*Written 2026-09-08. Every design statement here is `HYPOTHESIS`; everything drawn
from the curatorial audit is `INHERITED-UNVERIFIED`. Nothing in this directory is
public copy, and nothing in it promotes a claim — promotion requires a retrieval
event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
