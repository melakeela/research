# HOLD-007 — the WATER sources the backlog names by name are unretrieved

**Opened:** 2026-09-08
**Domain:** product architecture — the WATER Living World (backlog items 27 and 38)
**Ledger rows:** `SRC-091`, `SRC-095`, `SRC-096`
**Blocks:** the filling of every one of the seven slots specified in
`13-PRODUCT-ARCHITECTURE/water-living-world.md`, including the half of slot 6
that concerns the past — the Indus absences cannot be typed without excavation
coverage (`APA-W-001`). What it does **not** block is the half of slot 6 that
records this repository's own reach, and it does not block the specification
itself, which is written to be checkable against an empty register.
*(Corrected from "five of the seven" after adversarial review; the unit
carried three different counts of the same quantity. `BF-025`.)*

## What is needed

Backlog item 27 names six candidate materials and one scholar. This hold
records what could not be reached for each.

| Work | Why it is load-bearing | Where it might be | Probe |
|---|---|---|---|
| Bhavani Raman, "Urban nature and Chennai's water archive", *Seminar* 744, 2021 | Item 27 names Raman's Chennai water work by name. It is the only named modern-system source in the backlog, and it is about the *archive* of Chennai water — which is the MODERN SYSTEM slot's archive-audit requirement (§4.5) rather than only its content. | india-seminar.com | `SRC-096` — `EGRESS_BLOCKED` at the gateway. Nothing was read. |
| Raman's other water and coastal-property work (the Stanford "Muddy Waters: Coastal Property in India" material; her EPW pieces; the digital-humanities work on colonial Chennai maps and Tamil hydrological lexicon) | Same slot. The DH work on a Tamil hydrological lexicon annotated onto colonial maps also bears on the TEXT AND LANGUAGE slot (§4.3). | EPW; academia.edu; institutional pages | Named only in a WebSearch result listing (`SRC-097`). Hosts untested or index pages, not texts. Discovery, not retrieval. |
| Excavation reports for Dholavira — R. S. Bisht's ASI reports and the ASI *Indian Archaeology: A Review* volumes | The MATERIAL EVIDENCE slot (§4.2) requires findspot, context and report locator for every water feature. Every reachable secondary account of Dholavira's reservoirs depends on these, and the dependency is currently unmeasured. | ASI publications; archive.org | Not reachable. `SRC-095` re-confirms the publisher and bibliographic lanes are refused; ASI reports are in no lane probed in this session. |
| Sengupta et al. 2019/2020, "Did the Harappan settlement of Dholavira (India) collapse during the onset of Meghalayan stage drought?", *J. Quaternary Science* 35(3) 382–395, `10.1002/jqs.3178` | The ECOLOGICAL CHANGE slot (§4.4). Its dating is what would let the environmental record and the settlement record be placed on one timeline without asserting that one caused the other. | Wiley | **Partly reachable.** `SRC-090` returned chunks 1 and 20 with the DOI. The article itself, its figures, its calibration curve and its supplementary material were not obtained; `SRC-095` shows the DOI cannot be dereferenced. |
| Singh et al. 2020, "Hydrology and water resources management in ancient India", *HESS* 24, `10.5194/hess-24-4691-2020` | The most-cited reachable synthesis (44 citations at `SRC-089`), and the one most likely to be leaned on. Its **abstract**, which is all we hold, states that *"The Mauryan Empire (~322–185 BCE) is credited as the first 'hydraulic civilization'"* — and *civilization* is on `CLAUDE.md`'s ten-category audit list, so the phrase is one slot 3 requirement 3 of the specification requires be audited, not repeated. | Copernicus, open access | `SRC-095` — `CONNECT` 403 on both doi.org and hess.copernicus.org. Abstract only, via `SRC-089`, where the quoted phrase is now located. |
| Houdas 2024, doctoral corpus of 597 Indus hydraulic structures across twelve sites | The only reachable candidate for a *systematic* material inventory rather than a site-by-site account, and therefore the one source that could tell us whether the Indus hydraulic literature is twelve sites or two. | French institutional repository | Abstract only, via `SRC-089`. Not probed further; no lane. |
| Mosse 1997, "The Symbolic Making of a Common Property Resource", *Development and Change* | The South Indian tank material, and the historiographical slot: it is an argument *against* the ahistorical "community management" reading of Tamil tank systems that a Living World is otherwise likely to reproduce. | Wiley | Abstract only, via `SRC-089`. Not returned by `SRC-090`. |
| Any Tamil-language edition of the Sangam corpus with a hydrological lexicon | The TEXT AND LANGUAGE slot (§4.3) cannot be filled from English summaries. The translation standard requires original script, transliteration, grammatical form, edition and exact locator. | GRETIL, TITUS, Tamil digital libraries | Not reached. GRETIL and TITUS are refused (`SRC-080`, `SRC-082`); no Tamil corpus lane has ever been opened in this repository. |

## Why it is blocked

Three separate causes, and they are not the same problem:

1. **Egress.** `doi.org`, `api.crossref.org`, `api.openalex.org`,
   `hess.copernicus.org` and `india-seminar.com` are all refused at the
   gateway (`SRC-095`, `SRC-096`). A DOI recovered from a connector cannot be
   resolved to the article. This reverses the 2026-09-07 reading, recorded at
   D-001, that every domain except JSTOR now answers.
2. **Subscription.** Scite is spent for the month (`SRC-091`). That is the
   instrument method step 5 would use, so the dependency structure of the
   Indus hydraulic literature cannot be measured in this session — only
   asserted, which the standing constraint forbids.
3. **Corpus coverage, which is not a block but reads like one.** The two
   working lanes are Consensus and Scholar Gateway. Scholar Gateway is
   Wiley. Consensus returns abstracts without DOIs. Neither reaches ASI
   reports, Tamil-language scholarship, Indian university presses, EPW or
   *Seminar*. **The material this repository can reach on WATER is
   disproportionately Anglophone, Northern-published and
   engineering-framed** — which is an archive-audit finding about us
   (method step 6), and is recorded as one in
   `04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv`, not treated as a fact about the
   past.

## What this hold does and does not permit

**Permits.** Specifying the seven slots and their evidence requirements;
recording which candidate materials have a reachable source and which do
not; naming these works as leads with the standing of the probe that found
them; and stating that the burden is undischarged in this record.

**Forbids.** Any register row characterising what Bisht, Raman or the ASI
reports say. Any WATER claim promoted above `INHERITED-UNVERIFIED` on the
strength of an abstract. Any statement that the Dholavira reservoirs are
dated, or that the 4.2 ka event caused anything at Dholavira, until the
Sengupta article is read rather than excerpted. Any use of a Consensus or
Scholar Gateway return as though it were an independent second source for a
claim the other one also carries — both are indexes over the same
publication record, and their agreement measures nothing.

## What would close it

For (1), D-001 with `india-seminar.com`, `doi.org` and
`hess.copernicus.org` added. For (2), D-003's paid-tier half. For (3),
nothing an allowlist can fix: a lane to Indian and Tamil-language
scholarship has to be opened deliberately, and until it is, the coverage
skew is stated on the face of every WATER unit rather than left to be
inferred.
