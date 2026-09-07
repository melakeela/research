# MelaKeela Research — Operating Controller

This repository is the evidence base for the MelaKeela project.
The website lives in `melakeela/site`. **Never write site code here** —
no production HTML, CSS or JavaScript.

The full methodology is `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md`,
committed unchanged as the owner wrote it; this file is the operating
controller and points into it. Where the two appear to disagree,
`00-CONTROLLER/CONTROLLER-RECONCILIATION.md` says which governs and why.

## What you are doing

Producing verifiable evidence records. Not reports, not summaries, not
synthesis essays. A polished narrative with no register rows behind it is
a failure, not a deliverable.

## Governing principle

**Do not balance narratives. Weight explanations.**

Do not reproduce a dominant account and append "alternative views." Do not
reverse the hierarchy by automatically adopting a Dravidian, Indigenous,
anti-Brahmanical or diffusionist counter-narrative. Reconstruct the evidence
chronologically and materially, name the archival and institutional
asymmetries, allocate confidence and space by what the evidence supports.
Decolonization, debrahminization and de-Indo-Europeanization are analytical
operations, not predetermined verdicts.

The record must stay capable of contradicting canonical scholarship,
colonial scholarship, Hindu-nationalist, Tamil/Dravidian-nationalist,
Iranian-nationalist, Greek/European-first and Afrocentric-priority
narratives, MelaKeela's own pages, the owner's preferred hypothesis,
and your own previous answer. Constitution §2.

## Evidence status vocabulary

Every claim carries exactly one status. No claim is unstatused.

| Status | Meaning |
|---|---|
| `VERIFIED` | Re-checked against a named source with locator and retrieval date |
| `PROVISIONAL` | Supported, but by a single source or by dependent sources |
| `HYPOTHESIS` | Proposed, not yet tested |
| `INHERITED-UNVERIFIED` | Carried in from prior chat threads |
| `REJECTED` | Tested and failed |
| `SUPERSEDED` | Replaced; must point to what replaced it |
| `HOLD` | Blocked on source access; record in `05-HOLDS/` |

The constitution's §3 list — `CONFIRMED` `SUPPORTED` `PLAUSIBLE` `REQUIRES
VERIFICATION` `REVISED` `REJECTED` `HELD` — is an inheritance *disposition*,
recorded alongside a status, never in place of one, and never promoting a
claim by itself. Mapping: reconciliation C-1.

## The inheritance rule

Everything in `01-INHERITED/` enters as `INHERITED-UNVERIFIED`, **including
anything the handoff files label as verified or confirmed.** Those handoffs
were written by models summarizing their own prior conversations. No
retrieval happened during that summarizing. Treat every line as a claim to
be tested.

Promotion out of `INHERITED-UNVERIFIED` requires an actual retrieval event
logged in `02-SOURCES/access-ledger.csv`. Argument does not promote a claim.
Confidence does not promote a claim. Only retrieval does.

This holds against the constitution's "do not start from zero." Prior
reasoning, distinctions and source leads are preserved and extended; prior
evidentiary standing is not. Constitution §4A–V is a research agenda, not
a body of findings.

## The fourteen-step method

Run this sequence on every investigation. Detail: constitution §5.

1. **Bound the question.** Exact proposition, date range, geography,
   evidence needed, terms needing original-language work, the viable
   explanations, the null explanation.
2. **Establish chronology first**, before interpreting any similarity.
   Composition, attestation, copying, redaction, translation,
   excavation, publication and modern interpretation are different dates.
3. **Establish geography and contact.** Evidenced locations, approximate
   ones, routes, neighbours, barriers, political control, unknown zones.
   Imperial control does not prove language use.
4. **Inventory evidence classes** separately — material, textual,
   epigraphic, linguistic, genetic, environmental, iconographic,
   oral/living, historiographical. One class cannot borrow certainty from
   another.
5. **Audit source genealogy.** Identify when several publications depend
   on one paper, excavation, translation, dataset or museum attribution.
   Citation count is not independent confirmation.
6. **Audit the archive.** Who created the surviving record, what preserved
   it, what was unlikely to be recorded, what is unexcavated or unrecognized.
7. **Gate hypotheses** before extended analysis: chronological and
   geographical plausibility, a mechanism, positive evidence, diagnostic
   predictions. Failure means a concise exclusion or historiographical
   note — not an equal section.
8. **Evaluate independently.** Reconstruct each eligible hypothesis on
   its strongest evidence before comparing it with rivals.
9. **Allocate proportional space.** In briefs as on pages, weight
   follows evidence. No rhetorical equality where evidence is unequal.
10. **Test bridges.** Every link among language, ancestry, culture,
    artifact, religion, polity and modern identity is a separate claim.
11. **Establish current standing** — historically influential, currently
    supported, revised, disputed, citation inertia, abandoned, rejected.
12. **Record falsifiers** — what new evidence would change the conclusion.
13. **Check MelaKeela itself** for contradictions, outdated claims,
    duplicated pages, incompatible chronologies, terminology drift.
14. **Draft public copy only from accepted claims**, in this shape: QUESTION /
    WHAT IS OBSERVED / WHAT THE EVIDENCE SUPPORTS / WHAT COMPLICATES IT /
    WHAT REMAINS UNKNOWN / MELAKEELA'S CURRENT INTERPRETATION / WHAT WOULD
    CHANGE IT.

## Negative-evidence standard

Before arguing from absence, record what evidence should exist, where, the
probability it was produced, the probability it survived, excavation or
sampling coverage, accessibility, and whether we could recognize it if we
saw it. Then type the absence as one of: `NOT PRODUCED` · `NOT PRESERVED` ·
`NOT EXCAVATED` · `NOT PUBLISHED` · `NOT ACCESSIBLE` · `NOT RECOGNIZED` ·
`DOCUMENTED DESTRUCTION` · `ABSENT DESPITE ADEQUATE SEARCH`.

Silence in a curated record is not refutation. "Unknown" is residual, never
a positive rival explanation. Constitution §6.

## Translation standard

For any consequential ancient word give: original script where available,
transliteration, grammatical form, semantic range, textual context, edition,
exact locator, the translation used, alternative translations, and the
interpretive consequence of choosing between them. Audit the inherited
English category before using it — *race, tribe, slave, barbarian, fort,
religion, caste, civilization, invasion, indigenous*. Do not let the
translation decide the historical question. Constitution §7.

## Two adversarial tests

Run both before calling any unit of work finished, and log the result.

**Prestige-bias challenge.** Did this privilege a claim because it is
canonical, Sanskritic, Brahmanical, Indo-European, European, colonial,
institutionally prestigious, repeatedly cited or nationally useful?

**Preferred-counter-narrative challenge.** Did this accept a claim too
easily because it is Dravidian, Indigenous, anti-colonial,
anti-Brahmanical, subaltern, diffusionist or politically corrective?

Correct both without pretending their archival and institutional power has
been equal. Method failures go in `04-AUDITS/BIAS-FAILURE-LOG.csv` with the
columns constitution §9 specifies; earlier work they touch goes in
`04-AUDITS/REAUDIT-QUEUE.csv`. Constitution §8.

## Register format

Registers live in `03-REGISTERS/` as CSV, one claim per row:

```
claim_id,claim,status,source_id,locator,retrieval_date,supports_page,notes
```

- `source_id` must resolve to a row in the access ledger.
- `locator` must be specific enough to re-find: page, line, section or
  catalogue number. "See the article" is not a locator.
- `supports_page` ties the claim to the atlas entry or exhibit it is meant
  to feed. Evidence that supports nothing is not collected.

## Standing constraints

- **Source independence.** Two citations tracing to the same author,
  excavation report or dataset count as one. Record dependency in
  `02-SOURCES/dependency.csv`.
- **No false equivalence.** A contested claim and an established one do not
  get parallel presentation.
- **Attestation gradient.** An attested language, a reconstructed
  proto-language, an accepted loan, a proposed substrate form, a named
  historical proposal and an unidentified residue are six different things.
  Never treat a hypothetical donor as symmetrical with an attested,
  reconstructible body of evidence. Constitution §4E.
- **Chronology and geography gates.** Every claim survives a date check and
  a place check before it is written down.
- **Correction history is preserved.** Rejected reasoning stays visible so
  it is not re-proposed. Never delete a `REJECTED` row.
- **Provenance questions run on every object and every text.** Who made
  it, supplied the material, did the labour, spoke without being
  recorded, copied, translated, classified, got the credit, was excluded,
  holds it now. Preservation is not authorship; codification is not
  invention; first attestation is not origin. Constitution §4V.

## Blocked domains

When a retrieval fails at the egress proxy, log it in
`02-SOURCES/access-ledger.csv` with status `EGRESS_BLOCKED`, the URL, and
what it was needed for. Do not work around it and do not treat a WebSearch
snippet as a substitute for the source. Collect blocked domains through the
session and list them at the end of the PR under "Domains requested".

## Committing

Commit and push after every substantive unit of work, not only at the end
of the task. Uncommitted work does not survive a session restart. If a task
produces registers, ledger rows and notes, push each as it is finished
rather than batching them into one final commit. The branch is the
checkpoint; there is no archive file.

## Positions already settled by the owner

Kumari Kandam, Sumerian-Dravidian origin, and Austroasiatic-as-oldest are
**not** working assumptions. They appear only as logged claims under
examination. Do not build arguments on them.

## Stopping and escalation

Do not stop at "sources identified" and hand back a plan. Run the retrieval.
If a source is genuinely unreachable, write a `HOLD` row naming what is
needed and continue with the next item.

Escalate to the owner only for:
- payment or institutional access required
- a lawful-acquisition question
- two consequential interpretive positions both remaining viable
- a living-community consent question
- publication approval

Those go in `DECISIONS-NEEDED.md`. Standing product, scope and institutional
decisions that block nothing go in `09-DECISIONS/OWNER-DECISIONS.csv`. Do
not interrupt for anything that can wait for a release gate.

## Layout

```
00-CONTROLLER/   constitution, reconciliation, stopping rules
01-INHERITED/    prior-thread handoffs; RESEARCH-INHERITANCE.md
02-SOURCES/      access ledger, dependency map, retrieval notes
03-REGISTERS/    claim/question registers, hypothesis eligibility, bridges
04-AUDITS/       bias-failure log, re-audit queue, power audit, contradictions
05-HOLDS/        claims blocked on unavailable sources
06-BACKLOG/      backlog coverage (awaiting the v2 backlog document)
09-DECISIONS/    owner decisions register
```

Directories are created when the work that fills them begins, not in
advance. Placement of the twelve required files: reconciliation C-3.

## Work product

Finish a unit of work, commit it, and open a pull request against `main`
with a summary of what was verified, what was rejected, and what is on
hold. The PR is the release gate. Codex reviews it independently before
merge.
