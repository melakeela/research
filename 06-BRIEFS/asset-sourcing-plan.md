# Asset sourcing plan — the 392 slots, by rights basis

**Written:** 2026-09-08
**Unit type:** sourcing plan. It states, for each of the six asset classes,
what a usable asset is, whether an openly licensed route exists, what rights
basis each route gives, and what has to be commissioned instead. It is not
public copy and it commissions nothing.
**Register:** `03-REGISTERS/asset-sourcing.csv`, claims `AS-001` to `AS-022`
**Ledger:** `SRC-089` to `SRC-099`
**Hold:** `05-HOLDS/HOLD-007-asset-sourcing-egress.md`
**Bias failure logged:** `BF-003`
**Subject:** `01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, whose
392 slots across 96 pages remain, as that workbook left them, uniformly
`Source / commission route = To research` and `Status = Needed`.

---

## 0. The finding, before the detail

The inherited workbook's own reading of its asset register is that "the
critical path is not asset production, it is rights"
(`01-INHERITED/curatorial-audit-v1.1/SCHEMA.md` §4). Retrieval does not
support that.

**238 of the 392 slots — 61 per cent — have no third-party rights question at
all.** They are things this project makes: diagrams, legends, mobile
alternatives, downloadable tables, atmosphere assets, social cards, the
datasets themselves. Their cost is production and, for the diagrams,
sequencing behind verification. No licence is involved because no one else's
work is.

Of the remaining 154, **115 need a licence and a route exists or may exist** —
and for two collections the route was verified today, from the rightsholders'
own repositories, at `AS-004` and `AS-009`. Six of those 115, the archival site
photography, are better described as *unmeasured* than as sourced: the archives
that would answer were unreachable (`AS-017`).

**Thirty-two slots, plus seven of mixed character, cannot be licensed from
anyone, because the thing they name does not exist and will not exist until
this project makes it.** Not "no open licence has been found." No licence
is possible. That is §5 of this brief, ten of those slots are MVP slots, and
it is the cost the project has not carried.

So the critical path is rights for about a quarter of the register, production
for most of it, and for a tenth of it something the register has no column
for: fieldwork, correspondence with institutions, and a recording that would
have to be performed before it could be licensed.

---

## 1. What was probed, and what that constrains

Forty-two hosts, 2026-09-08T22:14–22:18Z (`SRC-089`). Every one answered 403
at the proxy CONNECT except `raw.githubusercontent.com` and
`media.githubusercontent.com`.

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

## 2. The five rights bases actually found

The register's single `Documentary standard` string — *"Verified source,
licence, credit, alt text, claim supported, date/place, manipulation
disclosure"* — is applied identically to all 392 slots. Retrieval found five
distinct rights positions underneath it, and they are not interchangeable.

| Basis | Verified instance | What it permits | What it does not |
|---|---|---|---|
| **CC0 over metadata, images excluded** | Met (`AS-004`, `AS-005`), Tate (`AS-011`) | Any use of the catalogue record, commercial included, no fee, no permission; attribution requested not required | Nothing about the image. The Met's CC0 image offer is real but is exercised on a separate host under a separate page |
| **CC0 over metadata *and* image files** | Cleveland (`AS-009`) — up to 30,000 works, web, print and full-size permalinks in the dataset | The image itself, commercially, without attribution | Only what the collection holds, which is unmeasured (`AS-010`) |
| **Per-record licensing** | Art Institute of Chicago (`AS-012`) | Whatever each record's `info.license_text` says | Bulk clearance. The README states the per-record notice does **not** cover images and media |
| **Public domain, no conditions** | Natural Earth (`AS-014`) | Everything, including modification and commercial print; crediting explicitly unnecessary | Supplies base geography only — no site, object or landscape imagery |
| **No licence is possible** | §5 below (`AS-015`, `AS-016`, `AS-019`) | — | — |

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
artefact points the same way as the history the custody pages are about. A
sourcing policy of "use what is openly licensed" would, followed mechanically,
illustrate ancient South Asia entirely out of the collections that removed it.
That is a curatorial decision, and §8 refers it to the owner rather than
letting the licence situation make it silently.

---

## 3. The classes, by rights basis

Slot arithmetic per class is from the workbook's own `Required asset set`
strings, counted in `04-AUDITS/` and reconciled to its stated totals:
392 slots, 96 pages, 15 MVP pages, 62 MVP slots.

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

**Open route.** None by default, and the reason is structural: a modern
translation is a new copyrightable work whatever the age of the text it
translates (`AS-021`). The age of the Tirukkuṟaḷ buys nothing.

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

**One limit on it, recorded because the first reading of it was wrong.** The
`Excavation` column is blank on all but two of those 1,005 records. That is
*not* evidence that the findspots are lost. The column is populated in exactly
one department — Egyptian Art, 59.2% — and overwhelmingly with `MMA
excavations` season strings: it records the Met's own digging, not findspot in
general (`SRC-099`, `AS-022`, superseding `AS-007`; logged as `BF-003`). The
surviving claim is about the dataset and is enough for the production
decision: **a Met CC0 image cannot be captioned with a findspot from the open
data, so it can illustrate a collection and its history but not a site.**

**Commissioning.** 14 of the 35 slots. See §5.

### 3.5 Language/script — 6 pages, 24 slots

*Manuscript/inscription image; glyph diagram; language map; pronunciation
audio where licensed.* MVP: `veli` (4), `the-languages-we-lost` (12).

**Usable asset.** An inscription photographed legibly enough to read; a glyph
diagram; a language map; audio.

**Open route.** Glyph diagrams and language maps are house work over a public
domain base (`AS-014`), 12 of 24 slots. Inscription images are the manuscript
problem again. Pronunciation audio has no route at all — see §5.

**Commissioning.** Inscription photography at 6 slots, and the audio question,
which is not a production task.

### 3.6 Place/ecology — 6 pages, 24 slots

*Site/landscape photography; material macro; ecological map; present-context
image.* MVP: `keeladi` (7), `the-water-city` (9). The only class needing
physical presence somewhere.

**Usable asset.** Photography of a named site as it now is; macro photography
of material; an ecological map; an image of the site's present context —
which for Keeladi means a working excavation and the people around it.

**Open route.** The ecological map, from Natural Earth, verified (`AS-014`).
That is 6 of 24 slots.

**What is honestly unknown.** Whether openly licensed site photography exists
is **not measured** (`AS-017`). Wikimedia Commons, `upload.wikimedia.org`,
Flickr Commons, Openverse, ASI and the Tamil Nadu department were all blocked.
Typed `NOT ACCESSIBLE`, deliberately not `ABSENT DESPITE ADEQUATE SEARCH`: the
search was not adequate, because the environment prevented it. Commons very
plausibly holds usable Keeladi and Indus-site photography. Nothing here says
otherwise, and a commissioning decision taken today on the assumption that it
does not would be taken on an absence this survey did not establish.

**Commissioning.** Present-context imagery is fieldwork under any licence
regime — nobody else's photograph is of the site *now*, and a present-context
image of a working excavation raises consent questions about the people in it
before it raises rights questions about the frame.

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
without a third party:

| Class | Slots needing no third party | Needing a licence | Impossible to licence | % self-sufficient |
|---|---:|---:|---:|---:|
| Data/interactive | 70 | 0 | 0 | **100%** |
| Generic essay set | 150 | 50 | 0 | 75% |
| Language/script | 12 | 6 | 6 | 50% |
| Place/ecology | 6 | 6 *(unmeasured)* | 12 | 25% |
| Custody/institutional | 0 | 14 (+7 mixed) | 14 | 0% |
| Text/social-history | 0 | 39 | 0 | 0% |
| **Total** | **238** | **115 (+7)** | **32** | **61%** |

Read together the two tables say something the workbook's uniform
`To research` conceals. The class gating the most MVP pages, Generic essay
set, is among the *most* tractable, because three of its four slots are house
work. The classes that will actually delay a launch are Custody/institutional
and Text/social-history — 4 MVP pages, 16 MVP slots, and zero self-sufficient
slots between them. Those two are `custody` (14), `the-archive` (15), `kural`
(10) and `the-other-laws` (13).

**A ranking by pages unblocked would put them fifth and sixth. They are the
critical path.**

---

## 5. Where nothing openly licensed exists — the uncosted commissioning

Three gaps, and none is a search failure. In each, the licence does not exist
because the *object* does not exist.

**5.1 Institutional correspondence and access-status evidence — 14 slots, 7
pages, 2 of them MVP (`AS-015`).** These are records of a transaction between
this project and a holding institution: a request made, an answer given or
withheld. No institution publishes them because there is nothing to publish
until someone asks. Typed `NOT PRODUCED`. The cost is not a licence fee but
staff time, correspondence and, where an FOI or RTI route is used, a
statutory clock. And a request has an outcome the project does not control: a
refusal is itself the asset, and publishing one is where the "no unsupported
allegation" constraint becomes testable rather than notional. This is the
single largest uncosted item in the register and it sits under two MVP pages.

**5.2 Pronunciation audio for a reconstructed language stage — 6 slots, 2 of
them MVP (`AS-016`).** No licence can exist for this, because a reconstruction
has no speakers to record. The workbook's hedge, *"pronunciation audio where
licensed"*, defers a question that has no licensing answer. Any such audio is
a newly made performance of a modern reconstruction, and it raises an
attestation-gradient problem before a rights one: a recording sounds like
evidence in a way a starred form on a page does not, and the register's own
constraint holds that a reconstructed proto-language and an attested language
are not the same kind of thing. If the speaker is a member of a living
community, it is additionally a consent question, which under `CLAUDE.md` is
an owner escalation and not a production task at all.

**5.3 Material macro and present-context imagery — 12 slots, 6 pages, 2 of
them MVP; and 6 further site-photography slots that are unmeasured rather than
impossible (`AS-017`).** The measurement gap and the real gap must not be
merged, so they are counted apart. *Present-context* imagery is fieldwork by
definition — no existing photograph is of Keeladi as it is now — and material
macro means physical access to material. Those 12 are a photographer
commission at named sites in Tamil Nadu, with permissions from the excavating
authority and consent from people in frame, and no allowlist entry touches
them. The other 6, archival site photography, may well be openly licensed on
Wikimedia Commons; Commons was unreachable, so they are counted in the
licence column of §4 and flagged there as unmeasured.

**Totals: 32 slots that cannot be licensed from anyone, plus the 7
accession/custody-document slots that are partly institutional and partly
open-data.** Ten of the 32 are MVP. The register carries no cost, no lead
time and no owner for any of them, and its uniform `Source / commission route`
`= To research` is what allowed 392 slots with three different economics —
production, licensing, and acquisition-by-request — to be scheduled as one
kind of work.

---

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
Asia entirely from the collections that removed it. Referred to the owner
(§8), not resolved here.

A second, smaller one: the Met census is the most concrete thing in this brief
and got the most space, which is proportional to its evidentiary weight but
also to the fact that it was the retrievable one. The 1,005-record count is
directional, not exact — the keyword filter over-collects (`Indus` matches
river-named objects) and under-collects (blank `Culture`, region-only
cataloguing) — and `04-AUDITS/met-openaccess-census.py` states its own limits
in its docstring.

**Preferred-counter-narrative challenge.** Did this accept a claim too easily
because it is anti-colonial or institutionally critical?

Yes, and it was caught before publication. `AS-007` measured the Met's
`Excavation` field as blank on 1,003 of 1,005 South Asian records and was
about to report it, next to `Credit Line` values naming private collectors and
dealers, as findspots gone missing. The measurement was accepted at the point
where it fitted an expected story. One question — what does this column do
elsewhere in the same file — dissolved it: the column is populated only in
Egyptian Art and overwhelmingly with the Met's own excavation seasons
(`SRC-099`). `AS-007` is `SUPERSEDED`, not deleted; `AS-022` claims only what
survives; `BF-003` records the failure and its control: *measure an absence
across the whole dataset, broken down by the producer's own organisational
units, before reading it as evidence about the world.*

`AS-008` is in the same family and was re-read under that control. It claims
only that the `Credit Line` field carries those names, and asserts nothing
about any named collector — which is the correct standing for a field this
project has read but not yet investigated.

---

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
