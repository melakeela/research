# Research Queue

The only backlog. One programme at a time, top down. Nothing here is a
finding; every row is work not yet done.

Seeded from `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4 (domains A–V)
and §11 (packets R20–R21), plus one domain that has no entry in either
(`WMP-9`, below). Ordering below the first item is owner decision **D-008** in
`09-DECISIONS/OWNER-DECISIONS.csv`.

## Done

1. **Source access audit** — `02-SOURCES/access-ledger.csv`, 18 rows.
   Egress and connector reach probed; blockers escalated as `D-001` and
   `D-003` in `DECISIONS-NEEDED.md`.
2. **Inheritance intake** — `03-REGISTERS/inherited-claims.csv`, 369 rows,
   all at `INHERITED-UNVERIFIED`. Inventory only; nothing verified.
3. **The púr- family in the Rigveda** (part of domain **J**) —
   `03-REGISTERS/rigveda-pur-family.csv` (28 claims) and
   `rigveda-pur-family-occurrences.csv` (106 occurrences); method in
   `04-AUDITS/rigveda-pur-family-method.md`. `HOLD-001` open on the
   `púraṃdhi-` etymology.
4. **Domain E — Dravidian, Munda and unidentified substrate claims**,
   corpus-internal half only. `03-REGISTERS/domain-e-claims.csv` (26
   claims: 19 VERIFIED, 4 PROVISIONAL, 2 HYPOTHESIS, 1 HOLD),
   `domain-e-hypothesis-eligibility.csv` (the eleven §4.E distinctions,
   each gated), `domain-e-retroflex-residue.csv` (253 lemmas),
   `domain-e-hydronyms.csv` (469 occurrences). Method and both
   adversarial tests: `04-AUDITS/domain-e-method.md`. The comparative
   half is on `HOLD-002` and `HOLD-003`: every Dravidian, Munda and
   Austroasiatic source was refused at the egress gateway. Escalated as
   `D-042`.
5. **Domain M — the Brahui geographic measurement, challenged by the owner**
   (part of domain **M**) — `03-REGISTERS/domain-m-brahui-position.csv`
   (26 claims: 20 VERIFIED, 5 PROVISIONAL, 1 SUPERSEDED; the owner's two
   objections are DMB-004 and DMB-005, recorded as raised). Method and
   both adversarial tests:
   `04-AUDITS/domain-m-method.md`; scripts `brahui-loo-geography.py` and
   `north-dravidian-cognate-sharing.py`. Method failures `BF-005` and
   `BF-006`; re-audits `RA-004`, `RA-005`; provenance question `D-035`.
   The challenged measurement was **not in this repository** and had to be
   reconstructed (`DMB-003`). The comparative half is on `HOLD-004`:
   Krishnamurti 2003, the book every retrievable assertion of North
   Dravidian traces to, has never been read here. **None of the six §4.M
   models is closed by this unit and none was allowed to be.**
6. **Controller amendment** — methodology installed, reconciled against
   the controller, decisions register and this queue seeded. Merged as
   PR #6.

## Now

7. **Domain E, comparative half — Dravidian, Munda and unidentified
   substrate claims.** *(This change.)* The lexical and comparative
   counterpart to item 4, run from CDIAL, DEDR and Munda data retrieved
   through the git proxy lane. Registers, audits, hypothesis gate,
   bridges, draft copy and `HOLD-005` are in place; both §8 adversarial
   tests are logged in `04-AUDITS/domain-e-method-comparative.md` §5.

   Five of §4.E's eleven distinctions were measurable from retrieved
   sources and four were not, and the split follows the retrieval
   channel rather than the evidence. Step 13 ran against
   `melakeela/site` and returned one substantive finding (`IC-E-001`,
   `IC-E-002`) and two passes.

   Item 4 and this item are two separate runs of the same domain, from
   different evidence classes and different sessions. Their method notes,
   registers and holds are kept apart deliberately; `DEP-016` to
   `DEP-020` record where their ledger rows are the same source probed
   twice.

12. **Domain K — Indus writing and institutional discontinuity**, Rigvedic
    half complete, Indus half held. Registers, absence typing, hypothesis
    gate, bridges, archive audit, translation blocks, method note with both
    §8 tests and a step-14 brief are in place;
    `04-AUDITS/domain-k-method.md` §5 carries the adversarial tests and
    §7 records that method steps 2 and 3 could not be run at all, because
    no absolute chronology for either side was retrievable.

    The four targets the task named were probed and logged either way:
    Mahadevan's concordance, the Wells sign list and the ASI reports are
    refused at the gateway; a machine-readable sign corpus on GitHub
    answered. That corpus is `SRC-102`/`SRC-103` and it is 179 Mohenjo-daro
    unicorn seals with three fields each.

    Thirteen absences are typed and ten of them license nothing. Only the
    three Rigvedic lexical absences are `ABSENT DESPITE ADEQUATE SEARCH`,
    and even those are refused the bridge to the society at `BR-K-006`.
    The domain's headline absence — no unambiguous Rigvedic description of
    Indus writing — is typed `NOT RECOGNISED` and licenses the least of
    all.

    `D-055` asks the owner for four hosts. `D-056` asks whether to write to
    the ICIT administrator.

## Blocked on inputs

Items **8** and **9** are reserved for the prompt-pack intake and the
`MELAKEELAWHOMADETHEPAST.md` register intake, which are on
`claude/prompt-pack-inventory-reconcile-iz1phs` (PR #14) and are not on this
branch. The reservation is deliberate: both branches were cut from the same
base and both appended to this list, so the numbers were allocated once,
across both, rather than twice from the same free position. Whichever merges
first, the other's items keep the numbers stated here. The reassignment is
recorded under "Item numbering" at the end of this file.

10. **Backlog reconciliation** — `06-BACKLOG/BACKLOG-COVERAGE.csv`, one row
    per item 1–89 with a destination, deliverable, hold or reasoned
    rejection. `RESEARCH HOLD`: the "MelaKeela.com v2 — Master Research,
    Product & Institutional Backlog" is not in this repository and cannot be
    reconstructed by inference. See `DECISIONS-NEEDED.md` D-014.
11. **Packets R1–R19.** Named in the site review running list; their
    definitions live in the prompt-pack (`MELA-KEELA-CLAUDE-FULL-SEQUENCE.md`,
    `MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md`,
    `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md`), which is also absent.
    `RESEARCH HOLD` on the same grounds.

## Research domains — constitution §4

Twenty-two domains carried in as **accumulated provisional work**, not as
findings. Each enters at `INHERITED-UNVERIFIED`; each disposition
(`CONFIRMED` … `HELD`) is recorded beside a status, never in place of one.
The trap column is the constitution's own warning for that domain — the
thing the investigation is most likely to get wrong.

| # | Domain | The named trap |
|---|---|---|
| A | Rigvedic chronology and transmission | Neither "a perfect audio recording" nor "Pāṇini rewrote it" |
| B | Early Rigvedic, Old Avestan and Classical Sanskrit | Family-tree labels predetermining an anonymized comparison; unequal archives read as equal samples |
| C | The Sanskrit sound system is historically composite | Projecting the later alphabet back as one pristine PIE design; reading the 5×5 grid as 25 inherited phonemes |
| D | Proto-Dravidian and Tamil phonology | Treating either analytical system as an imperfect version of the other |
| E | Dravidian, Munda and unidentified substrate claims | Symmetry between an attested family and a hypothetical donor; "unknown" used as positive evidence — *both halves run 2026-09-07: corpus-internal (item 4) and comparative (item 6). Distinctions 4, 8, 9 and 10 remain on `HOLD-002`, `HOLD-003` and `HOLD-005`.*
| F | *kīnāśa* and agricultural vocabulary | Accepting the etymology, or dismissing it as resemblance, without the lemma work |
| G | BMAC/Oxus and pre-split Indo-Iranian contact | Reading "Proto-Indo-Iranian" as pre-contact or purely inherited |
| H | Rigvedic and Old Avestan social worlds | A violent-Indic versus peaceful-Iranian binary; genre mistaken for society |
| I | Rigvedic society, patronage and canonization | Sanitizing patronage as timeless spirituality |
| J | The Rigvedic forts | Translating *pur* into a Mature Harappan city; one famous count standing for the corpus — *corpus built 2026-09-07 at the stanza unit, 103 passages, all fifteen enumerated items addressed and the five-way typology assigned. 99 is stated in 6 passages and is not the modal count; 100 is, in 8. Poet lineage rests on Geldner alone (`HOLD-006`); proposed geography is `NOT PRODUCED` — the pinned corpus carries no geographic content. See `06-BRIEFS/pur-4j-corpus.md`.* |
| K | Indus writing and institutional discontinuity | Concluding that populations vanished because institutions and archives did — *run 2026-09-09 and split by the egress boundary. The Rigvedic half is measured in full: 22 later writing and sealing stems absent, a gloss scan of the whole lexicon returning no writing or sealing word, and `akṣára-` denoting a syllable of chanted speech in all eight occurrences. The Indus half reached one volunteer digitisation — 179 unicorn seals from one site, no find-spot — so seals as a class, sealings, tablets, function, distribution and post-urban survival have no evidence here at all. `HOLD-008`; six of eleven hypotheses gated source-blocked and two more rejected. See `06-BRIEFS/domain-k-brief.md`.* |
| L | Avestan writing | Reading a Sasanian-era alphabet as transparent evidence of Gāthic pronunciation |
| M | Brahui, Kurukh and Malto | Medieval migration treated as documented fact; living people used as linguistic fossils |
| N | Grammatical ontologies | Typological similarity read as descent or contact without a mechanism |
| O | Pāli, Prakrit and vernacular Indo-Aryan | Prakrit as corrupted Sanskrit; one pure language decaying |
| P | South Asian linguistic convergence | Modern areal distribution converted automatically into prehistoric substrate |
| Q | Greek–South Asian contact | Starting at Alexander; "Greek invention" from first surviving text, "Indian influence" from similarity plus contact |
| R | Materials and corridors | Assigning language to artifacts; museums repeating one attribution counted as confirmation |
| S | Meluhha, Marhaši, Magan, Dilmun and extraction | Collapsing Marhaši into Meluhha; "moored ships" read as captured fleets |
| T | Hormuz and modern comparison | "Modern ruler = Sargon"; undated contemporary claims |
| U | Sacrifice, renunciation and appropriation | A peaceful-Indigenous versus violent-migrant race story |
| V | Ancient subalterns and intellectual provenance | Preservation read as authorship; codification as invention; first attestation as origin |

## A domain with no constitution §4 entry

`MELA-KEELA-WHO-MADE-THE-PAST.md` §9 treats the racialization of *Aryan* as a
research programme. It has no letter in constitution §4 and no packet in §11, so
none of the rows above guards it. This one does. It is a guard and not a start:
nothing here authorizes retrieval on the subject, no claim about it exists in
any register, and no analytical space has been allocated to it.

| # | Domain | The named trap |
|---|---|---|
| WMP-9 | The racialization of "Aryan" | Reading *ārya-* as though it already carried what nineteenth-century race science later made of it; running the transmission backwards, so that a racial category appears to have arrived in philology from outside rather than to have been built out of it; and scoring "Aryan invasion" against "no Aryan invasion" as two evidentiary hypotheses when each is a political position first |

The identifier is `WMP-9`, not a letter: letters in the table above are
constitution §4 domains and this is not one. It is named for its source
document and section so that a later reconciliation can find it.

**A Sanskrit self-designation is not a nineteenth-century racial category.**
*ārya-* is a word in Sanskrit texts, with a textual range and a grammar, and
its form here is cited unaccented because no edition has been opened for it.
"Aryan" is a term of nineteenth-century European classification. The trap is
treating either as a translation of the other: reading the Rigveda as though its
self-designation already denoted a race, or reading the nineteenth-century
category as a neutral technical term the texts licensed. Under the translation
standard the word cannot cross into English without the full block — script,
transliteration, grammatical form, semantic range, textual context, edition,
exact locator, the translation used, the alternatives, and the interpretive
consequence of choosing between them — and *race* is one of the inherited
English categories that standard names for audit before use. Constitution §7.

**The direction of transmission runs from philology into race science, and
getting the direction backwards is the trap.** That direction is §9's framing,
carried here as `INHERITED-UNVERIFIED`; it is a claim to be evidenced
publication by publication, not something this row establishes. The trap it
names is narrating the racial category as a political corruption that arrived
from outside an otherwise clean discipline. The
opposite move is the same failure inverted: treating the philology as nothing
but race science, so that the linguistic results are discarded along with the
ideology. Both are chronology failures before they are political ones, and
chronology is answerable here — who published what, in what year, citing whom,
with what institutional position — by the ordinary means of step 2. Every link
between a linguistic result, a racial classification and a political
institution is a separate claim and is tested as one; step 10.

**Both invasion framings are political positions before they are evidentiary
ones.** "Aryan invasion" and "no Aryan invasion" each have an institutional and
national history, and each is argued for reasons that are not only evidentiary.
The governing principle applies at full strength: weight explanations, do not
balance narratives. Neither framing earns space by being the counterweight to
the other, and the record stays capable of contradicting the colonial
scholarship that built the first and the Hindu-nationalist and
Tamil/Dravidian-nationalist accounts that turn on the second — as it stays
capable of contradicting MelaKeela's own pages and the owner's preferred
hypothesis. Constitution §2. Two consequences follow and are stated because
they are what the trap catches: rejecting the racial category does not settle
the migration question, and evidence bearing on migration does not rehabilitate
the racial category. They are different claims with different evidence.

**Provenance and standing.** `MELA-KEELA-WHO-MADE-THE-PAST.md` is not in this
repository — `01-INHERITED/site-review/RUNNING-LIST-RECONCILIATION.md` records
its absence and adds it to what `D-014` requests. §9 is therefore held here as
the owner stated it in the instruction that commissioned this row, not as
retrieved text, and it carries the standing everything unretrieved carries:
`INHERITED-UNVERIFIED`. Nothing above is promoted by having been written down.
The repository's own record numbers this material differently: the running list
maps supplied section 9 to feature `AS-04` "Lives Without Names" and puts
"Admired, Then Racialized" at sections 11 and 10
(`01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md` L842–843,
`INHERITED-UNVERIFIED`). Either the standalone document numbers its sections
differently from the running list, or one of the two is wrong. Raised as `D-037`
in `09-DECISIONS/OWNER-DECISIONS.csv`; it blocks nothing, because the trap is
stated from content the owner supplied directly and does not depend on which
number carries it.

The nearest existing statement in this repository on the same programme is the
running list's direction that the Aryan reception history requires branching,
sourced connections through philology, racialization and political
institutions, that Nazism is not presented as an inevitable consequence of
discovering linguistic kinship, and that its documented racial ideology is not
sanitized (same file, L856, `INHERITED-UNVERIFIED`). That is a neighbouring
direction, not the trap statement, and it is cited rather than absorbed.

§9's learning constraints — the three things a children's interface may not do —
are recorded separately, at `13-PRODUCT-ARCHITECTURE/museum-framework.md`
§10.4.7. They bind the product regardless of subject and are not scoped to this
domain.

## New packets — constitution §11

- **R20 — THE MISSING RECORD.** Indus seals and writing, Rigvedic silence,
  post-Harappan institutional discontinuity, Old Avestan oral composition,
  the later Avestan alphabet, and what eventual writing can and cannot
  recover. Overlaps domains **K** and **L**; run as one investigation, not
  three. The negative-evidence standard governs the "silence" component —
  no absence argument without a typed classification.
- **R21 — SACRIFICE, RENUNCIATION AND APPROPRIATION.** Early Vedic
  sacrifice, patronage and violence; śramaṇa traditions; ahiṃsā,
  non-possession, meditation, yoga, karma, rebirth, liberation; Brahmanical
  incorporation; modern political and commercial appropriation. Overlaps
  domain **U** — same work, and U is the fuller statement of it.

A packet need not produce a page. It may produce corrections, extensions,
shared datasets, a new investigation, Atlas layers, comparative instruments
or research holds. Constitution §11.

## Opened by domain E

- **Retrieve the substrate literature.** `HOLD-005`. Witzel 1999,
  Kuiper 1991, Masica 1979, Krishnamurti 2003, Rau 2019, Shorto 2006.
  Four of the eleven distinctions in §4.E cannot be gated without them,
  and the blockage is one-sided: it falls entirely on the hypotheses
  with the least attested support.
- **Adjudicate the DEDR digitizations.** `IC-E-001`. Two independent
  digitizations of Burrow and Emeneau disagree on 10.3% of
  entry-language assignments and neither can be checked against print
  while `dsal.uchicago.edu` is blocked. Every DEDR-derived count on the
  platform carries that error bar, including
  `the-northwest-cousin.html`'s published Brahui figure.
- **Domain M is now load-bearing.** `DE-M-025` shows Dravidian's whole
  northwestern geographic position rests on Brahui. The Brahui dating
  question stops being one domain's detail.
- **Six re-audits** in `04-AUDITS/REAUDIT-QUEUE.csv`, of which
  `RA-008` is programme-wide: every domain where one side of an
  argument sits in retrievable data and the other in unretrievable
  literature.

## Opened by the WATER Living World specification

`13-PRODUCT-ARCHITECTURE/water-living-world.md`, 2026-09-08. None of these is
an owner decision; they are research-programme scheduling.

- **Open a Tamil corpus lane.** The emptiest slot of the seven, and the one
  no allowlist change fixes. This repository's reachable corpora are Vedic
  (`SRC-019` to `SRC-024`, `SRC-069` to `SRC-085`) and comparative-lexical
  (`SRC-060` to `SRC-067`). There is no Tamil text lane at all, so slot 3 of
  a WATER world — and every claim in backlog item 14, *Tamil textual corpus
  parity* — is unfillable at the standard the translation rule sets. GRETIL
  and TITUS are refused (`SRC-080`, `SRC-082`); what a Tamil lane would be
  has not been investigated. `WLW-005`.
- **Measure the source genealogy of the Indus hydraulic literature.**
  `WLW-002`. Every reachable account of Dholavira's water engineering appears
  to depend on excavations we cannot read, and *appears to* is the problem:
  the dependency is asserted, not measured, because Scite refused for quota
  (`SRC-091`, D-003). Method step 5 is the whole point of the exercise and it
  has not been run on this literature.
- **Type the WATER absences, which needs no retrieval.** Excavated area
  against total site area for the Indus water sites; the recognition criterion
  for an elite water work; the eight-type classification for each. This is
  `06-BRIEFS/mvp-fifteen/09-the-water-city.md` §6's MVP-U9 and it is the one
  unit of WATER work that is not blocked on anything.
- **Re-audit the reachability readings across the repository.** `SRC-095`
  reverses the 2026-09-07 conclusion recorded at D-001 that "every domain
  except JSTOR now answers": `doi.org`, `api.crossref.org` and
  `api.openalex.org` all refuse again. Reachability is a timestamped probe,
  not a property — which is what D-042 asks — and any unit that relied on the
  2026-09-07 reading should be re-checked rather than assumed.

## Opened by domain K

- **Retrieve the Indus corpus and its literature.** `HOLD-008`. Mahadevan
  1977, CISI, the Wells sign list and ICIT, Mukhopadhyay 2023, the ASI
  reports, Rao et al. 2009 and Farmer, Sproat and Witzel 2004. Six of the
  eleven hypotheses in the domain are gated on them, and so is every
  question §4.K asks about seals, sealings, tablets, function,
  distribution and post-urban survival.
- **Search a cuneiform corpus for Meluhhan writing.** `DK-A-013`. The most
  answerable open question in the domain: it is a text search over a
  published corpus and it failed here only on egress. Belongs with domain
  **S**.
- **The platform's Indus corpus figures have never been verified here.**
  `RA-022`, `IC-K-001`, `IC-K-002`. Two pages give different figures for
  the longest Indus text, ten and seventeen, and the corpus figures are
  sourced through journalism rather than the concordance.
- **The administrative reading of the seals.** `RA-023`. The platform
  states a trade bureaucracy as its leading argument, citing an article on
  a blocked host. `DK-H-003` and `DK-H-004` are gated together and must be
  re-gated together.
- **`RA-024` is programme-wide, and is the second instance of the
  pattern.** After `RA-008`: in this domain the reachable evidence and the
  unreachable evidence fall on opposite sides of the question, and the
  reachable side is the Sanskritic, textual, canonical one. Every unit
  should state which side of its question its sources sit on.

## Standing sequencing rules

- One programme at a time. Do not open parallel programmes until one has
  passed a Codex review.
- Chronology (Step 2) and geography (Step 3) before any comparison.
- Hypothesis gating (Step 7) before extended analysis, so that space is
  never allocated to a hypothesis that has not cleared the gate.
- Both adversarial tests (§8) before a unit is called finished.
- The first programme previously queued — the Meluhha-to-Keezhadi spine —
  is domain **S** plus part of **R**. It is not a separate item.

## Not yet

- Product and institutional specification (§12) — pending **D-012**.
- The language-movement Artifact Atlas specification (§13).
- Page and exhibit briefs.

  *Recorded against that item, not as an exception to it:* fifteen page briefs
  were produced out of position on 2026-09-08, on the owner's instruction, and
  are in `06-BRIEFS/mvp-fifteen/`. **The placement is not settled.** No owner
  decision was allocated for it and none is claimed: an instruction to carry out
  work is not a standing decision that the work may precede its queue position,
  and `DECISIONS-NEEDED.md` **D-032** still reads *"Nothing in this repository
  acts on the MVP set until this is answered."* The briefs describe what each of
  the fifteen pages would need; they schedule no launch, approve no page, order
  no work and assume no answer to D-032. Their standing, including the reading
  under which the unit should have waited and under which this note is itself to
  be reverted, is written up in `06-BRIEFS/mvp-fifteen/README.md` §0. The other
  81 pages are untouched.
- Anything touching `melakeela/site`.

## Item numbering

This list is append-only and its numbers are identifiers, not positions. Two
branches cut from the same base each appended to it, so the free numbers were
allocated once across both rather than twice from the same position. Old
number to new, with the branch that holds the item:

| Old | New | Item | Branch |
|---|---|---|---|
| — | 5 | Domain M, the Brahui geographic measurement | `main` (PR #16) |
| 5 | 6 | Controller amendment | `main` (PR #6), moved from **Now** to **Done** by PR #10 |
| — | 6 → 7 | Domain E, comparative half | `claude/domain-e-research-queue-z83m9b` (PR #10) |
| — | 7 → 8 | Prompt-pack intake | `claude/prompt-pack-inventory-reconcile-iz1phs` (PR #14) |
| — | 8 → 9 | Register intake for Who Made the Past | `claude/prompt-pack-inventory-reconcile-iz1phs` (PR #14) |
| 6 → 7 | 10 | Backlog reconciliation | `main` |
| 7 → 8 | 11 | Packets R1–R19 | `main` |

The second column's arrows record the one further shift made on 2026-09-07
when `main` merged PR #16, whose domain M unit took item 5 and moved the
controller amendment to 6. `main` keeps the numbers it has published; the two
branches' items move up behind them, once, across both.
