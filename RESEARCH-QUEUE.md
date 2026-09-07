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
   `D-032`.
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

6. **Domain M — the six competing models, run under the fourteen-step
   method** (the rest of domain **M**) —
   `03-REGISTERS/domain-m-measurements.csv` (22 rows),
   `domain-m-interpretations.csv` (12), `domain-m-model-gates.csv` (the six
   §4.M models, each gated at step 7), `domain-m-balochi-chronology.csv`
   (6 dated statements, each with what it actually dates). Method and both
   adversarial tests: `04-AUDITS/domain-m-six-models-method.md`; script
   `domain-m-dedr-north-dravidian.py`. Method failures `BF-007`, `BF-008`,
   `BF-009`; re-audits `RA-006`, `RA-007`, `RA-008`; decisions `D-038` to
   `D-041`.

   The MCP literature connectors were authorised and what each returned is
   logged (`SRC-053`–`SRC-057`). One of them named a GitHub-hosted database
   carrying a re-encoding of **DEDR**, and GitHub is the one host the
   session proxy answers on — so a Dravidian etymological dictionary was
   read here for the first time (`SRC-059`). North Dravidian was
   re-measured on it, with a permutation test holding entry size and
   per-language attestation both fixed: Kurux–Malto 176 exclusive
   etymologies against a null of 0.71; the Brahui attachment **7** against
   a null of 0.00; Brahui's pairwise sharing with each of Kurux and Malto
   at chance. And 260 of Brahui's 269 DEDR etymologies reach outside North
   Dravidian, so its Dravidian membership does not rest on that node.

   **All six §4.M models read `CANNOT-GATE`, none `FAIL`** — nothing
   retrieved dates Brahui in either direction, so the chronological
   criterion cannot be applied at all. No model received analytical space.
   `HOLD-005` opened on the Balochi and Indo-Aryan contact strata:
   Korn 2005 is the work that would answer them and was not read.
   `HOLD-002` and `HOLD-004` are narrowed, not lifted; Krishnamurti 2003
   is in no reachable connector's corpus.

## Now

7. **Controller amendment.** Install the methodology, reconcile it against
   the controller, seed the decisions register and this queue. *(This
   change.)* No research begins until it is reviewed.

## Blocked on inputs

8. **Backlog reconciliation** — `06-BACKLOG/BACKLOG-COVERAGE.csv`, one row
   per item 1–89 with a destination, deliverable, hold or reasoned
   rejection. `RESEARCH HOLD`: the "MelaKeela.com v2 — Master Research,
   Product & Institutional Backlog" is not in this repository and cannot be
   reconstructed by inference. See `DECISIONS-NEEDED.md` D-014.
9. **Packets R1–R19.** Named in the site review running list; their
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
| E | Dravidian, Munda and unidentified substrate claims | Symmetry between an attested family and a hypothetical donor; "unknown" used as positive evidence — *corpus-internal half run 2026-09-07; comparative half on HOLD-002/003* |
| F | *kīnāśa* and agricultural vocabulary | Accepting the etymology, or dismissing it as resemblance, without the lemma work |
| G | BMAC/Oxus and pre-split Indo-Iranian contact | Reading "Proto-Indo-Iranian" as pre-contact or purely inherited |
| H | Rigvedic and Old Avestan social worlds | A violent-Indic versus peaceful-Iranian binary; genre mistaken for society |
| I | Rigvedic society, patronage and canonization | Sanitizing patronage as timeless spirituality |
| J | The Rigvedic forts | Translating *pur* into a Mature Harappan city; one famous count standing for the corpus |
| K | Indus writing and institutional discontinuity | Concluding that populations vanished because institutions and archives did |
| L | Avestan writing | Reading a Sasanian-era alphabet as transparent evidence of Gāthic pronunciation |
| M | Brahui, Kurukh and Malto | Medieval migration treated as documented fact; living people used as linguistic fossils — *six-models unit run 2026-09-07; North Dravidian re-measured on DEDR and still neither validated nor refuted; all six models `CANNOT-GATE`; contact strata on `HOLD-005`, Krishnamurti 2003 on `HOLD-004`* |
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
- Anything touching `melakeela/site`.
