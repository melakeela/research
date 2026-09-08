# HOLD-007 — any archaeological, excavation or survey source bearing on the púr- corpus

**Raised:** 2026-09-08, by `06-BRIEFS/childrens-pilot/`.
**Blocks:** the "what the ground shows" half of any forts exhibit, children's or
adult; constitution §4J's *archaeological fortification* type; §4J's *proposed
geography* field at anything above the corpus-internal level.
**Does not block:** the children's investigation specified in
`06-BRIEFS/childrens-pilot/`, which is built around this hold rather than
despite it. Screen S-10 shows the hold to the child.
**Ledger:** no row. This is the point.

## What is needed

Any one of: an excavation report, a site report, a regional survey, an
archaeological dataset, a museum object record, or a geographic gazetteer,
bearing on fortification, retrievable and loggable in
`02-SOURCES/access-ledger.csv`.

### This hold cannot yet state its own region or its own period, and says so

An earlier draft read *"bearing on second-millennium-BCE fortification in the
relevant region."* Both halves were unsourced and are withdrawn.

- **No period.** Nothing in this repository dates the composition of the
  Rigveda. A search of every `rigveda-pur-*.csv` for `BCE`, `B.C.` and
  `millennium` returns nothing. The only chronological instrument in hand is
  Arnold's relative periodisation, and `PUR-028` holds at `HYPOTHESIS` that it
  is chronological at all.
- **No region.** `PUR4J-018` (`VERIFIED`) records that the pinned corpus carries
  no geographic content. `PUR4J-028` records the one thread that could ever
  reach a geography — `sindhu-`, a proper name for both translators in three of
  six passages — and the register declines to place it. Version 12 line 1175
  holds research against identifying the forts with one archaeological culture.

**A hold that names its own date range and region without a source has done the
identification it exists to request.** So this one does not. What it asks for is
a source; what it is *for* is stated under "Why it is needed"; and **bounding
the question — constitution §5 step 1 — is itself part of the work the hold
blocks, not a precondition this unit can supply.**

That is uncomfortable and it is the honest position: this repository currently
cannot say where or when to dig, and saying so is not the same as having no
question.

## Why it is needed

`00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4J requires *archaeological
fortification* to be distinguishable from *textual stronghold*, *poetic
formula*, *inferred geography* and *unsupported identification*.
`PUR4J-024` (`PROVISIONAL`) records that three of those five types were assigned
to no passage, for the stated reason that the unit had *"no geographic source and
no archaeological source"*. `PUR4J-018` (`VERIFIED`) records that the pinned
corpus contains no geographic content of any kind.

Without a source on this side, the corpus can say what the poem says and cannot
say anything at all about what stood anywhere.

## What was checked, and how

All 88 rows of `02-SOURCES/access-ledger.csv` were read for this unit, by
`category` and by `source_name`. The categories present are: `mcp-connector`,
`infrastructure`, `retrieval-channel`, `primary-source-repository`,
`tertiary-reference`, `paywalled-journal-archive`, `preprint-repository`,
`citation-infrastructure`, `primary-corpus`, `primary-text`,
`primary-annotation`, `metadata`, `primary-monograph`, `journal-literature`,
`primary-lexicon`, `search-index`, `secondary`, `repository-self-audit`,
`primary-comparative-dataset`, `reference-dataset`,
`classification-and-bibliography`, `primary-reference-work`, `derived-database`,
`reference-work-derivative`, `reconstruction-set`, `primary-lexical-data`,
`editorial-apparatus`, `secondary-literature`, `translation`,
`primary-text-edition`, `primary-text-archive`, `secondary-web`.

**No archaeological, excavation, survey, site, object-record or geographic
category exists, and no row of any category is one.**

## Why this is NOT typed under the negative-evidence standard

Constitution §6 types absences **in the record of the past**: what should exist,
where, the probability it was produced, the probability it survived, excavation
or sampling coverage, accessibility, and whether we could recognise it.

This is not that. This is an unrun retrieval. Typing it `NOT EXCAVATED` would
assert that the relevant ground has not been dug, which this unit has not
established and has no source for. Typing it `ABSENT DESPITE ADEQUATE SEARCH`
would assert a search that was never made.

It is a `HOLD`, and it stays a `HOLD` until somebody either retrieves a source or
does the §6 work properly and types a real absence.

## What closing it does not close

Retrieving an excavation report would produce a wall and a poem. Joining them is
a separate claim — a `material→text` bridge under museum framework §4.4, needing
its own mechanism, its own rivals and its own status. `RESEARCH-QUEUE.md` /
Version 12 line 1175 already carries a research hold against *"identification of
the ninety-nine forts with one archaeological culture"*, and §4J's own first line
warns against automatically translating *púr* into a Mature Harappan city.

**Closing this hold makes the question harder, not easier.** The children's
investigation's screen S-10 says so to the child, and any adult exhibit built on
a closed HOLD-007 must say the same.

## What this hold is not

**It is not a blocked attempt.** No retrieval was attempted in this unit. Nobody
was prevented from reaching anything, and `CLAUDE.md`'s gloss for `HOLD` —
"Blocked on source access" — describes something that has not happened here.

The status is still `HOLD` and not a typed absence, for the reason given above:
the alternative is to type an absence in the record of the past on the strength
of a search nobody ran. But the child-facing gloss must not say "we tried and
could not get there", and `01-investigation-spec.md` §0.1 was corrected under
review for saying exactly that. The gloss is now **"there is a job on our list
that nobody has done"**, which is true.

## Escalation

`D-001` and `D-043` are the standing egress-allowlist decisions. If the sources
needed here are unreachable at the proxy, they belong in that request rather than
in a new one, and the attempt is logged with status `EGRESS_BLOCKED` per
`CLAUDE.md`. No attempt was made in this unit, which performed no retrieval.
