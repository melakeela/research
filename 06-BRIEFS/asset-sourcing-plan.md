# Asset sourcing plan — the 392 slots, by rights basis

**Written:** 2026-09-08
**Unit type:** sourcing plan. It states, for each of the six asset classes,
what a usable asset is, whether an openly licensed route exists, what rights
basis each route gives, and what has to be commissioned instead. It is not
public copy and it commissions nothing.
**Register:** `03-REGISTERS/asset-sourcing.csv`, claims `AS-001` to `AS-022`
**Ledger:** `SRC-089` to `SRC-099`
**Hold:** `05-HOLDS/HOLD-007-asset-sourcing-egress.md`
**Bias failures logged:** `BF-024`, `BF-025`
**Adversarial review:** run before the PR was opened; fourteen findings, all
repaired in place. Four of them were disqualifying and two of them changed
this brief's headline number. What changed is recorded at §10 rather than
quietly corrected.
**Subject:** `01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, whose
392 slots across 96 pages remain, as that workbook left them, uniformly
`Source / commission route = To research` and `Status = Needed`.

---

## 0. The finding, before the detail

The inherited workbook's own reading of its asset register is that "the
critical path is not asset production, it is rights"
(`01-INHERITED/curatorial-audit-v1.1/SCHEMA.md` §4). Retrieval does not
support that.

**238 of the 392 slots — 61 per cent — need no third party.** They are things
this project makes: diagrams, legends, mobile alternatives, downloadable
tables, atmosphere assets, social cards, the datasets themselves. Their cost
is production and, for the diagrams, sequencing behind verification.[^1]

**140 need someone else's work, and not one of them could be measured.** Every
archive, image repository and museum API that would answer was unreachable
(`SRC-089`). What *was* verified — from the rightsholders' own repositories —
is the rights position five programmes take (`AS-004`, `AS-009`, `AS-011`,
`AS-012`, `AS-014`). What is not known, for any of the 140, is whether the
material exists. **That, and not any impossibility, is what the project has
not costed:** a third of the register carries no cost, no lead time and no
owner, and cannot acquire one from this environment.

**Seven slots must be created because the record does not exist under any
access conditions** — institutional correspondence, two of them MVP. That
number was 32 in the first version of this brief. The reduction is not a
softening; it is `BF-025`, and §10 says what happened.

So the critical path is production for most of the register, unmeasurable
rights for a third of it, and for seven slots something the register has no
column for. The three economics are set out at §4 and derived by
`04-AUDITS/asset-slot-decomposition.py`, whose partition is written out in the
script so it can be argued with.

[^1]: "No third party" means no one else's *permission*. 26 of those 238 — the
    map slots — sit on Natural Earth, which is someone else's work in the
    public domain: no licence is required, and §6's asset record still demands
    `owner_or_custodian`, `source` and `attribution` for every one of them.

## 1. What was probed, and what that constrains

Forty-two hosts, 2026-09-08T22:14–22:18Z (`SRC-089`, whose `probe_call` says
"40" and lists 42; the list is authoritative). Every one answered 403 at the
proxy CONNECT. Separately, `github.com`, `raw.githubusercontent.com` and
`media.githubusercontent.com` — which are not in that list of 42 — answer.

Blocked: every museum open-access API (Met, Rijksmuseum, Smithsonian,
Europeana, V&A, Art Institute, Wellcome), every IIIF endpoint, Wikimedia
Commons and `upload.wikimedia.org`, Flickr Commons, Openverse, the
Archaeological Survey of India, the Tamil Nadu State Department of
Archaeology, Tamil Digital Library, Project Madurai, Tamil Virtual Academy,
Roja Muthiah Research Library, Cambridge Digital Library, Bodleian, the
British Library and its Endangered Archives Programme, ELAR, PARADISEC,
Natural Earth's own site, the Archaeology Data Service — and
`creativecommons.org`, so a licence deed cannot be read from its issuer in
this environment.

`WebFetch` travels the same policy and is blocked identically. `WebSearch`
does not and answers, but under `CLAUDE.md`'s blocked-domains rule a search
snippet is not a substitute for a source, so nothing here is promoted on one.
Two rows (`AS-013`, `AS-018`) are `PROVISIONAL` for exactly that reason
(`AS-003`).

**What survives that.** GitHub is not an empty channel for this problem.
Several museum open-access programmes publish their datasets and their licence
texts there, and `media.githubusercontent.com` serves Git-LFS objects in full.
So the *rights* analysis in this brief rests on primary retrieval — licence
text read from the rightsholder's own repository — even though not one image
was fetched. **The plan is sourced. The assets are not.** `HOLD-007`.

That division is worth holding onto, because the two failures have different
remedies. An allowlist entry fixes the second. Nothing fixes the first for the
classes in §5.

---

## 2. The rights bases actually found

The register's single `Documentary standard` string — *"Verified source,
licence, credit, alt text, claim supported, date/place, manipulation
disclosure"* — is applied identically to all 392 slots. Retrieval found four
distinct rights positions underneath it, plus two states that are not rights
positions at all and are listed because the register does not distinguish
them either.

| Basis | Verified instance | What it permits | What it does not |
|---|---|---|---|
| **CC0 over metadata, images excluded** | Met (`AS-004`, `AS-005`), Tate (`AS-011`) | Any use of the catalogue record, commercial included, no fee, no permission; attribution requested not required | Nothing about the image. The Met's CC0 image offer is real but is exercised on a separate host under a separate page |
| **CC0 over metadata *and* image files** | Cleveland (`AS-009`) — up to 30,000 works, web, print and full-size permalinks in the dataset | The image itself, commercially, without attribution | Only what the collection holds, which is unmeasured (`AS-010`) |
| **Per-record licensing** | Art Institute of Chicago (`AS-012`) | Whatever each record's `info.license_text` says | Bulk clearance. The README states the per-record notice does **not** cover images and media |
| **Public domain, no conditions** | Natural Earth (`AS-014`) | Everything, including modification and commercial print; crediting explicitly unnecessary | Supplies base geography only — no site, object or landscape imagery |
| **No licence is possible** | §5.1 (`AS-015`) — 7 slots, and only these | — | — |
| **Not measurable from here** | §5.2 (`AS-016`, `AS-017`, `AS-023`) and every one of the 140 licence-needing slots | — | Nothing, either way. This is the state of most of the register, and it is a fact about the environment |

Two conditions recur across the CC0 programmes and are the only live
obligations they impose: do not misrepresent the dataset or its source, and do
not use the institution's trademarks or imply its endorsement. Both bind this
project directly, because a museum page that criticises an institution while
displaying that institution's data is precisely where implied endorsement gets
read in.

**A caution about what "openly licensed" is measuring here.** Every collection
whose rights position was verified is Euro-American: the Met, Cleveland, Tate,
the Art Institute, the Smithsonian. Not one South Asian institution's rights
position was retrieved. Indian and Tamil archives *were* in the probe set and
were blocked, so this is a channel artefact rather than a search bias — but the
artefact points the same way as the history the custody pages are about.

A sourcing policy of "use what is openly licensed" would, followed
mechanically, illustrate ancient South Asia entirely out of collections in
Europe and North America. How the objects in them got there is a provenance
question this project has not investigated for a single object, and this brief
does not answer it — `AS-008` and `AS-022` both decline to, and the framing
here must decline to as well. What can be said without any provenance research
is that the *distribution* is itself the subject of the custody pages, and
that arriving at it by default, because those happened to be the reachable
licences, is a curatorial decision taken by accident. §8 refers it to the
owner rather than letting the licence situation make it silently.

---

## 3. The classes, by rights basis

Slot arithmetic per class is from the workbook's own `Required asset set`
strings, derived by `04-AUDITS/asset-slot-decomposition.py` (`SRC-101`) and
reconciled to the workbook's stated totals: 392 slots, 96 pages, 15 MVP pages,
62 MVP slots. The script asserts both reconciliations and fails if either
breaks, so every number below is re-runnable rather than stated.

### 3.1 Generic essay set — 50 pages, 200 slots (51% of the register)

*Opening atmosphere asset; claim-specific diagram; source facsimile; social
card.* MVP: `index` (1), `enter` (2), `tinai` (5), `the-ledger` (6),
`before-the-indus` (8).

**Usable asset.** Three of the four slots are house design work: an atmosphere
asset that carries the page's environment, a diagram that is *correct about a
contested claim*, and a social card. The fourth, source facsimile, is a real
manuscript or print image with a rights position — class 3's problem appearing
inside class 1.

**Open route.** For the facsimile only, and it is the general
manuscript-image problem: Cleveland's CC0 covers images but its holdings are
unmeasured; the Met's covers metadata only; Cambridge, the Bodleian and the
British Library are the natural IIIF routes and all were blocked.

**Commissioning.** 150 of the 200 slots, and none of it is licensing. The 50
diagrams are the real cost and the real hazard: each is downstream of the
verification that establishes what it depicts (`AS-019`). Commissioning one
before its claims leave `INHERITED-UNVERIFIED` produces an illustration of an
unverified claim, and the workbook schedules these by MVP priority, which is
driven by *low* risk — that is, by the pages least closely examined. The
sequencing is inverted and the inherited workbook says so itself.

### 3.2 Data/interactive — 14 pages, 70 slots

*Verified dataset; accessible SVG/map; legend; mobile alternative;
downloadable table.* MVP: `artifact-atlas` (3), `sound-changes` (11).

**Usable asset.** Not an asset. One accessible component, built once, fed
fourteen times, over datasets this project produces.

**Open route.** Natural Earth for base geography: public domain, verified from
`LICENSE.md`, no permission needed, crediting explicitly unnecessary
(`AS-014`). It is the only input in this entire survey that is unencumbered,
reachable and usable today.

**Commissioning.** Engineering, not acquisition (`AS-020`). The class's
exposure is evidentiary rather than legal, and it is sharp: `verified dataset`
means the dataset must be *verified*, and `artifact-atlas`'s site count is
already recorded as contradicted inside this repository. A beautifully
accessible SVG of a contradicted number is a worse outcome than no page.

### 3.3 Text/social-history — 13 pages, 39 slots

*Primary-text facsimile; translation excerpt rights; editorial illustration or
print ephemera.* MVP: `kural` (10), `the-other-laws` (13).

**Usable asset.** A facsimile of the text as an object, a licensed excerpt of
a modern translation, and period print material.

**Open route.** None was found, and none could be looked for. The working
assumption is that a modern translation is a separate copyrightable work whose
term runs from its own publication, so that the age of the Tirukkuṟaḷ buys
nothing — but that is a proposition of copyright law, it is
jurisdiction-dependent, and this repository has retrieved no statute, no case
and no rightsholder statement bearing on it. It is `AS-026`, at `HYPOTHESIS`,
and it should not be relied on for a licensing decision until a jurisdiction
and a source are named. An earlier version of this brief stated it as
`VERIFIED` with no legal source at all (review finding F3).

**Commissioning.** Two routes avoid the negotiation and both cost work rather
than money. Use an out-of-copyright translation — which imports its period's
interpretive assumptions and must be audited under the translation standard
before a single word of it reaches a page, on a text whose colonial-era
English renderings are themselves contested. Or produce the translation
in-house, which is research output, not asset production, and belongs in a
register before it belongs in a slot. Zero of 39 slots have no external
dependency; this is the least self-sufficient class in the register.

### 3.4 Custody/institutional — 7 pages, 35 slots

*Collection record; accession/custody document; object image rights;
institutional correspondence; access-status evidence.* MVP: `custody` (14),
`the-archive` (15). Every one of the seven pages is Critical or High risk.

**Usable asset.** Two of the five slots are documents about an object's
institutional life; two are records of this project's own dealings with the
institution holding it; one is an image.

**Open route, and it is better than expected.** The collection record slot is
*retrievable today*. The Met's CC0 dataset was streamed in full — 484,956
rows, 317 MB — and contains 1,005 records that are both public-domain-flagged
and dated 1300 CE or earlier with South Asian descriptive fields: 944 in Asian
Art, 47 in Ancient Near Eastern Art, including 28 catalogued `Indus`, 32
`Baluchistan`, 16 `India (Tamil Nadu)`, and 11 seals (`AS-006`). `Credit Line`
is populated throughout and names the acquisition chain (`AS-008`). For a page
about custody, the openly licensed metadata is not decoration; it is the
evidence.

**Two limits on it, and both were got wrong before they were got right.**

First, `Credit Line` being populated on all 1,005 records is not a finding
about South Asian material. It is populated on 484,304 of 484,956 records
museum-wide — 99.9%, a mandatory display field (`SRC-100`, `AS-008`). What is
usable is not its presence but its *values*, which are acquisition-chain
statements. This brief asserts nothing about any collector named in them; a
credit line is a lead for a provenance investigation that has not been done.

Second, on findspot. The `Excavation` column is blank on all but two of the
1,005 — and the two are Egyptian Art rows, keyword false positives inside the
subset. But `Excavation` is one of *eleven* geography columns, and the first
version of this brief read one column's scope as a fact about the whole
schema. Measured across all eleven (`SRC-100`, `AS-022`): 56 records (5.6%)
carry any geographic value — `Region` 49, `Subregion` 24, `Geography Type` 10
— and the ten `Geography Type` values here are `Made in`, `Original from` and
`Attributed to`, production-place relations, not findspot relations, though
the same column reads `From` 26,755 times and `Excavated in` 3,716 times
elsewhere in the museum.

So the production rule survives in a narrower and better-founded form: **a Met
CC0 image can be captioned with a collection and its history, with a
region-level "made in" attribution for about one record in twenty, and with a
findspot for none of them.** What is now excluded is the stronger and false
claim that the dataset has no such field at all. (`AS-007` → `AS-022`;
`BF-024`; review findings F1 and F2.)

**Commissioning.** 14 of the 35 slots. See §5.

### 3.5 Language/script — 6 pages, 24 slots

*Manuscript/inscription image; glyph diagram; language map; pronunciation
audio where licensed.* MVP: `veli` (4), `the-languages-we-lost` (12).

**Usable asset.** An inscription photographed legibly enough to read; a glyph
diagram; a language map; audio.

**Open route.** Glyph diagrams and language maps are house work over a public
domain base (`AS-014`), 12 of 24 slots. Inscription images are the manuscript
problem again. Pronunciation audio: the workbook writes *"where licensed"* and
does not say *reconstructed*, and for Burushaski, Kusunda and Nihali —
living or recently living languages with archive recordings — a licensed route
plausibly exists. ELAR and PARADISEC were blocked, so it is unmeasured, not
absent (`AS-016`, §5.2).

**Commissioning.** Nothing established. Inscription photography and audio are
both `NOT ACCESSIBLE`, and whether either needs commissioning cannot be
decided until they can be searched.

### 3.6 Place/ecology — 6 pages, 24 slots

*Site/landscape photography; material macro; ecological map; present-context
image.* MVP: `keeladi` (7), `the-water-city` (9). The only class needing
physical presence somewhere.

**Usable asset.** Photography of a named site as it now is; macro photography
of material; an ecological map; an image of the site's present context —
which for Keeladi means a working excavation and the people around it.

**Open route.** The ecological map, from Natural Earth, verified (`AS-014`).
That is 6 of 24 slots.

**What is honestly unknown — all 18 of the other slots** (`AS-017`). Wikimedia
Commons, `upload.wikimedia.org`, Flickr Commons, Openverse, the ASI and the
Tamil Nadu department were all blocked, so site photography, material macro
*and* present-context imagery are alike `NOT ACCESSIBLE`, deliberately not
`ABSENT DESPITE ADEQUATE SEARCH`: the search was not adequate, because the
environment prevented it.

The first version of this brief typed site photography that way and, in the
same paragraph, called material macro and present-context imagery impossible —
on identical evidence. That is `BF-025`. Material macro plausibly sits in the
CC0 image corpora `AS-009` records as unmeasured. A recent openly licensed
photograph would satisfy present-context.

**Commissioning.** Possibly all 18, possibly none of them. What is certain is
only this: *if* fieldwork is commissioned, a present-context image of a
working excavation raises consent questions about the people in frame before
it raises rights questions about the frame. That is why the decision is the
owner's (§8) and why it should not be taken before the class can be searched.

---

## 4. The ranking, and why the requested ranking is the wrong instrument

Ranked by MVP pages gated, as asked:

| Rank | Class | MVP pages | MVP slots | Total slots | Earliest MVP rank gated |
|---:|---|---:|---:|---:|---:|
| 1 | Generic essay set | **5** | 20 | 200 | 1 (`index`) |
| 2 | Data/interactive | 2 | 10 | 70 | 3 (`artifact-atlas`) |
| 3 | Custody/institutional | 2 | 10 | 35 | 14 (`custody`) |
| 4 | Language/script | 2 | 8 | 24 | 4 (`veli`) |
| 5 | Place/ecology | 2 | 8 | 24 | 7 (`keeladi`) |
| 6 | Text/social-history | 2 | 6 | 39 | 10 (`kural`) |

Five classes tie at two pages, so the ranking barely ranks. It also misleads
in a specific way: every MVP page belongs to exactly one class, so **no class
can be deferred without cutting pages from the MVP**. The first nine MVP
pages already draw on four of the six classes. There is no ordering of these
six that gets a coherent launch set out earlier than any other.

The decision-useful ranking is by how much of each class can be produced
without a third party. Derived by `04-AUDITS/asset-slot-decomposition.py`;
`must create` is the record that does not exist under any access conditions,
and `licence` never means "material exists", only "someone else's work is
needed and this environment could not check".

| Class | No third party | Licence needed | Mixed | Must create | % self-sufficient |
|---|---:|---:|---:|---:|---:|
| Data/interactive | 70 | 0 | 0 | 0 | **100%** |
| Generic essay set | 150 | 50 | 0 | 0 | 75% |
| Language/script | 12 | 12 | 0 | 0 | 50% |
| Place/ecology | 6 | 18 | 0 | 0 | 25% |
| Custody/institutional | 0 | 21 | 7 | 7 | 0% |
| Text/social-history | 0 | 39 | 0 | 0 | 0% |
| **Total** | **238** | **140** | **7** | **7** | **61%** |

Over the 62 MVP slots the same partition is 31 / 27 / 2 / 2.

Read together the two tables say something the workbook's uniform
`To research` conceals. The class gating the most MVP pages, Generic essay
set, is among the *most* tractable, because three of its four slots are house
work. The classes that will delay a launch are Custody/institutional and
Text/social-history — 4 MVP pages, 16 MVP slots, and zero self-sufficient
slots between them.

**One qualification the first version of this brief did not make.** "Zero
self-sufficient" is a measure of third-party *dependence*, and it is being
used here as a proxy for *schedule risk*. For Custody/institutional the proxy
partly fails: the 7 collection-record slots and part of the 7
access-status-evidence slots are satisfiable **today**, from a CC0 dataset
already downloaded (§3.4, `AS-006`, `AS-023`). A dependence that has already
been discharged is not a delay. The claim that survives without qualification
is about Text/social-history, where all 39 slots depend on third parties and
none has been exercised.

**A ranking by MVP pages unblocked would put those two classes fifth and
sixth.**

## 5. Where a licence route cannot exist, and where it merely cannot be checked

The brief you are reading had, in its first version, a dramatic section here:
32 slots that "cannot be licensed from anyone." Adversarial review found that
25 of the 32 were typed impossible on the same blocked evidence that had, two
paragraphs earlier, been correctly called *unmeasured*. The strict standard
had been applied where it shrank the finding and the loose one where it
produced it. That is `BF-025`. The honest section is smaller and is below.

### 5.1 The one gap no search could close — 7 slots, 2 of them MVP

**Institutional correspondence** (`AS-015`). A record of a transaction between
this project and a holding institution: a request not yet made, an answer not
yet given. Nobody publishes it because there is nothing to publish until
someone asks. Typed `NOT PRODUCED`. Cost is staff time, correspondence, and
where an FOI or RTI route is used, a statutory clock — and the outcome is not
ours to control, since a refusal *is* the asset, and publishing one is where
the "no unsupported allegation" constraint stops being notional.

This rests on reading an ambiguous workbook string as meaning *this* project's
correspondence. On a reading where a published FOI disclosure log would serve,
the type would be `NOT ACCESSIBLE` like everything below, and the number would
be zero. The reading is stated in `AS-015` so it can be contested.

### 5.2 The gaps that are unmeasured, not impossible — 25 slots

Each of these was typed impossible in the first version and is now
`NOT ACCESSIBLE`. None of them can be costed until the allowlist opens,
which is precisely the point: **the project cannot presently decide whether
to commission them.**

- **Access-status evidence — 7 slots** (`AS-023`). Partly pre-exists, and the
  proof is in a dataset already downloaded: the Met's CC0 data carries
  `Gallery Number`, populated on 290 of the 1,005 records (28.9%) against a
  10.2% museum-wide baseline. A page arguing about what an institution keeps
  out of sight can source part of that argument from the institution's own
  open data today. What it does not cover is an institution's access
  *decision* about a specific request — which is §5.1.
- **Pronunciation audio — 6 slots** (`AS-016`). The workbook writes
  "pronunciation audio where licensed" and does not say *reconstructed*; the
  first version of this brief silently added that word, which made the slot
  impossible by construction. The languages these pages serve — Burushaski,
  Kusunda, Nihali — are living or recently living, and spoken-language
  archives hold recordings. Those archives were blocked. Two real cautions
  survive and neither is a rights question: audio of a *modern reconstruction*
  sounds like evidence in a way a starred form does not, which is an
  attestation-gradient problem; and a newly made recording by a community
  member is a consent question, and therefore an owner escalation.
- **Site photography, material macro and present-context imagery — 12 slots**
  (`AS-017`). Every candidate route was blocked. Material macro plausibly sits
  in exactly the CC0 image corpora `AS-009` records as unmeasured; a recent
  openly licensed photograph would satisfy present-context. Fieldwork may
  still be the right answer for all 18 externally dependent Place/ecology
  slots — but it would be a choice made under measured uncertainty rather than
  a necessity, and today the uncertainty is not measured.

### 5.3 What is actually uncosted

Not 32 slots, and not 7. **140.** Every slot needing someone else's work
carries no cost, no lead time and no owner, and none of them could be checked
from here. The workbook's uniform `Source / commission route = To research` is
what allowed 392 slots with four different economics — production, licensing,
acquisition-by-request, and fieldwork — to be scheduled as one kind of work,
and replacing that with a *smaller* uniform claim about impossibility would
have repeated the error in the opposite direction.

## 6. The asset record

Nothing enters a prototype without this, complete, or a placeholder that is
visibly a placeholder. Every field is mandatory; `unknown` is a permitted
value and a blank is not, because a blank cannot be distinguished from a field
nobody filled in.

| Field | Requirement |
|---|---|
| `asset_id` | Unique; the reference used by the page brief and the register |
| `owner_or_custodian` | Who holds it now. *Preservation is not authorship* — the custodian is not the maker (constitution §4V) |
| `maker_or_origin` | Who made the object or took the image, where known; `unknown` where not |
| `source` | Where this copy came from, specifically enough to re-fetch: repository, accession or catalogue number, URL, retrieval date |
| `source_id` | Resolves to a row in `02-SOURCES/access-ledger.csv`. No ledger row, no asset |
| `licence` | Named instrument and version (`CC0 1.0`, `CC BY 4.0`, `public domain`, `all rights reserved — permission granted`, `unknown`) |
| `licence_evidence` | Where the licence was read. A licence read from a third party's description is `PROVISIONAL`, not `VERIFIED` (`AS-003`) |
| `attribution` | The exact credit string to render, verbatim. "Requested, not required" is recorded as such and still rendered |
| `reuse_terms` | Commercial, derivative, share-alike, territory, and any condition — including no-misrepresentation and no-implied-endorsement clauses, which the CC0 museum programmes all carry |
| `depicts_claim` | The claim this asset is being used to support, by `claim_id`. An asset supporting no claim is not collected |
| `caption_limit` | What the source's own record supports. `AS-022` is the worked example: a Met CC0 record supports a collection caption and not a findspot caption |
| `manipulation` | Every change from the source file: crop, colour, composite, upscale, reconstruction |
| `alt_text` | Written from the claim, not from the picture |
| `consent` | For any identifiable living person or community-held knowledge: who consented, to what, when, and how it is withdrawn |
| `status` | `VERIFIED` · `PROVISIONAL` · `PLACEHOLDER` · `HOLD` · `REJECTED` |

**The placeholder rule.** A placeholder is permitted in a prototype and is
never silent. It renders as a visibly non-photographic block, it carries the
words *placeholder — not a sourced asset* in the visible layer and not only in
the alt text, and it names the class and slot it stands in for. It never
carries a caption that would be true of the real asset. Its register row
exists, with `status = PLACEHOLDER` and `licence = n/a — placeholder`, so that
the count of unsourced slots is queryable at any moment. A prototype where the
placeholders cannot be counted is not a prototype of a museum that publishes
its evidence standard.

**On generated imagery.** Not covered above, deliberately. An atmosphere asset
or a diagram may be produced by any tool; a *depiction of the past* may not be
produced by one and shown as though it were evidence, and `manipulation` is
where that distinction gets recorded. Where the line sits is a curatorial
decision, and §8 refers it.

---

## 7. Adversarial tests

**Prestige-bias challenge.** Did this privilege a claim because it is
canonical, institutionally prestigious or repeatedly cited?

Partly, and it is recorded rather than corrected, because the correction is
not available in this environment. Every verified rights position in this
brief belongs to a Euro-American museum. Indian and Tamil institutions were
probed and blocked (`SRC-089`), so the asymmetry is a channel artefact — but
the brief must not present "these five collections have open licences" as
"open licensing is available for this subject matter," and §2 states the
consequence: a mechanical open-licence policy would illustrate ancient South
Asia entirely from collections in Europe and North America. An earlier draft
wrote "the collections that removed it," which asserts as settled background a
provenance conclusion no retrieval here supports — and which `AS-011` makes
false for Tate, recorded as holding no relevant material at all. Referred to
the owner (§8), not resolved here.

A second, smaller one: the Met census is the most concrete thing in this brief
and got the most space, which is proportional to its evidentiary weight but
also to the fact that it was the retrievable one. The 1,005-record count is
directional, not exact — the keyword filter over-collects (`Indus` matches
river-named objects) and under-collects (blank `Culture`, region-only
cataloguing) — and `04-AUDITS/met-openaccess-census.py` states its own limits
in its docstring.

**Preferred-counter-narrative challenge.** Did this accept a claim too easily
because it is anti-colonial or institutionally critical?

Three times, and the self-assessment in the first version of this brief was
itself an instance of it — it reported the test as having caught one failure
and closed, when it had caught the first and stopped looking.

1. **`AS-007`.** The Met's `Excavation` field measured blank on 1,003 of 1,005
   South Asian records, about to be reported next to `Credit Line` values
   naming private collectors as findspots gone missing. One question — what
   does this column do elsewhere in the same file — dissolved it (`SRC-099`).
   Caught in-session, before the first commit.
2. **`AS-008`, which the first version claimed had been "re-read under that
   control" when no baseline had been computed at all.** `Credit Line` is
   populated on 99.9% of the museum; its presence on the subset is a
   cataloguing convention, not a finding (`SRC-100`). A control reported as
   run but not run is worse than an absent control, and it is the more serious
   half of `BF-024`. Caught by adversarial review (F2), queued as `RA-022`.
3. **The whole of §5**, which is `BF-025`: 25 slots typed impossible on the
   same blocked evidence that had been correctly called unmeasured two
   paragraphs earlier, producing a dramatic 32-slot "uncosted liability" that
   went into an owner decision. The honest figure is 7, and even that rests on
   an interpretation stated in `AS-015` so it can be contested.

The pattern in all three is the same and is worth naming precisely, because
"anti-colonial bias" is too coarse for it: **the strict standard went where it
would have shrunk the finding, and the loose one where it produced it.** The
controls now written into `BF-024` and `BF-025` are addressed at that, not at
a subject matter.

A fourth, of a different kind: `AS-019` and `AS-021` carried rights
conclusions at `VERIFIED` on a ledger row (`SRC-086`) about an unrelated
string search — one of them a proposition of copyright law with no legal
source whatever. They are now split into the counts they establish and the
reasoning they do not (`AS-025`, `AS-026`, at `HYPOTHESIS`). The register
validator passed them, because it checks that a `source_id` *resolves* and not
that it is the *right* row; that gap is not closable mechanically and is
recorded here as a known limit of the check.

## 8. What goes to the owner

One new decision, `D-053`, with a prose section in `DECISIONS-NEEDED.md`: the
commissioning cost in §5 is money, staff time and a fieldwork trip that the
project has not budgeted, and the sourcing-asymmetry question in §2 and §7 is
a curatorial position, not a production choice. Both are owner calls under
`CLAUDE.md`'s escalation rules — the first as payment and institutional
access, the second because it decides what the institution's own pages look
like they are made of.

Not escalated: the egress allowlist, which is already `D-001` and which
`HOLD-007` extends with a prioritised host list.

---

## 9. What would change this plan

- **Any allowlist entry.** `openaccess-api.clevelandart.org` would convert
  `AS-009` from a verified licence over an unmeasured collection into a
  measurable one. `commons.wikimedia.org` would convert `AS-017` from
  `NOT ACCESSIBLE` into a number and could close all six of the unmeasured
  site-photography slots — but none of the 12 in §5.3, which no archive can
  supply.
- **A Cleveland census finding substantial ancient South Asian holdings.**
  It would make CC0 *image files*, not merely metadata, a real route, and
  would move Custody/institutional off 0% self-sufficiency.
- **A finding that Cleveland's South Asian holdings are thin.** Equally
  possible and equally consequential in the other direction, and the reason
  §3.4 does not assume the first.
- **An out-of-copyright Tirukkuṟaḷ translation surviving a translation-standard
  audit.** It would remove the one unbounded external negotiation in the
  register (`AS-021`). It would also import a colonial-era reading into an
  MVP page, which is why it is an audit and not a shortcut.
- **A decision that `before-the-indus` leaves the MVP** (already open as
  `D-032`). It is the one MVP page at Critical risk, and it carries 4 Generic
  essay set slots including a claim-specific diagram that cannot be drawn
  until its claims are verified.
- **Any claim promoted out of `INHERITED-UNVERIFIED`.** The 50 claim-specific
  diagrams are gated on verification, not on rights or budget. Every promotion
  unblocks a diagram; no amount of asset funding unblocks one.
- **A named jurisdiction and a retrieved legal source for `AS-026`.** The
  entire Text/social-history route analysis rests on a proposition at
  `HYPOTHESIS`. If it is wrong in the jurisdiction that governs, 39 slots
  change character.

---

## 10. What adversarial review changed

Run before the PR was opened, as the repository requires. Fourteen findings.
Recorded here rather than folded in silently, because a brief whose headline
number moved by a factor of four should say so.

| Finding | What it changed |
|---|---|
| **F1** | `AS-022` claimed the Met data "carries no findspot field" on the strength of **one** column. The schema has eleven. Re-measured (`SRC-100`): 5.6% carry geography, and the production rule survives in a narrower form. `AS-022` rewritten. |
| **F2** | `AS-008` reported a 99.9%-populated field as a finding, and both this brief and `BF-024` stated the control had been applied to it. It had not. `AS-008` restated against its baseline; `RA-022` queued. |
| **F3** | `AS-019` and `AS-021` cited a ledger row about an unrelated string search, and carried rights conclusions at `VERIFIED`. Split into `AS-019`/`AS-021` (counts, `VERIFIED`, `SRC-101`) and `AS-025`/`AS-026` (reasoning, `HYPOTHESIS`). |
| **F4** | The largest block of "impossible" slots had no register row at all — prose only. Superseded by the retyping under F7; `AS-023` and `AS-024` added. |
| **F5** | `BF-003` was allocated by eye and collided with an existing 2026-09-07 row. Renumbered `BF-024`. Validator check 6 added — which then caught the same error again, on `RA-002`, now `RA-022`. |
| **F6** | The 238/115/32 decomposition appeared in three documents in three values, one of which did not sum to 392. Now derived once by `04-AUDITS/asset-slot-decomposition.py` and quoted from there. |
| **F7** | 25 slots typed impossible on evidence the brief elsewhere called unmeasured. `AS-015` narrowed, `AS-016` de-narrowed to the workbook's own wording, `AS-017` widened, `AS-023` added. `BF-025`. |
| **F8** | §2's table put the diagram slots in "no licence is possible" while §4 put them in the self-sufficient 238. §2 corrected. |
| **F9** | §4 used third-party dependence as a proxy for schedule risk, contradicting §3.4's own finding that the collection-record route is already exercised. Qualified. |
| **F10** | "the collections that removed it" asserted a provenance conclusion no retrieval supports, and is false for Tate on this brief's own evidence. Restated. |
| **F11** | "no third-party rights question at all" was false for the 26 map slots on Natural Earth. Footnoted. |
| **F12** | Two derivations were claimed against artefacts that did not exist. Both scripts now committed. |
| **F13** | `SRC-089` said "40 hosts" and listed 42; `AS-001` and §1 disagreed about which hosts answered. Reconciled. |
| **F14** | `supports_page = "(none)"` on two rows; an unsupported claim in `HOLD-007` that an allowlist entry yields 1,005 images. Both fixed. |

The reviewer's recommendation was **do not open the PR**. Every finding above
is repaired; the reviewer has not re-read the repairs, and this brief has not
been through a second independent review.
