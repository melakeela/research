# Research Queue

The only backlog. One programme at a time, top down. Nothing here is a
finding; every row is work not yet done.

Seeded from `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` §4 (domains A–V)
and §11 (packets R20–R21). Ordering below the first item is owner decision
**D-008** in `09-DECISIONS/OWNER-DECISIONS.csv`.

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
   `D-035`.
5. **Controller amendment** — methodology installed, reconciled against
   the controller, decisions register and this queue seeded. Merged as
   PR #6.

## Now

6. **Domain E, comparative half — Dravidian, Munda and unidentified
   substrate claims.** *(This change.)* The lexical and comparative
   counterpart to item 4, run from CDIAL, DEDR and Munda data retrieved
   through the git proxy lane. Registers, audits, hypothesis gate,
   bridges, draft copy and `HOLD-004` are in place; both §8 adversarial
   tests are logged in `04-AUDITS/domain-e-method-comparative.md` §5.

   Five of §4.E's eleven distinctions were measurable from retrieved
   sources and four were not, and the split follows the retrieval
   channel rather than the evidence. Step 13 ran against
   `melakeela/site` and returned one substantive finding (`IC-E-001`,
   `IC-E-002`) and two passes.

   Item 4 and this item are two separate runs of the same domain, from
   different evidence classes and different sessions. Their method notes,
   registers and holds are kept apart deliberately; `DEP-014` to
   `DEP-018` record where their ledger rows are the same source probed
   twice.

## Blocked on inputs

Items **7** and **8** are reserved for the prompt-pack intake and the
`MELAKEELAWHOMADETHEPAST.md` register intake, which are on
`claude/prompt-pack-inventory-reconcile-iz1phs` (PR #14) and are not on this
branch. The reservation is deliberate: both branches were cut from the same
base and both appended to this list, so the numbers were allocated once,
across both, rather than twice from the same free position. Whichever merges
first, the other's items keep the numbers stated here. The reassignment is
recorded under "Item numbering" at the end of this file.

9. **Backlog reconciliation** — `06-BACKLOG/BACKLOG-COVERAGE.csv`, one row
   per item 1–89 with a destination, deliverable, hold or reasoned
   rejection. `RESEARCH HOLD`: the "MelaKeela.com v2 — Master Research,
   Product & Institutional Backlog" is not in this repository and cannot be
   reconstructed by inference. See `DECISIONS-NEEDED.md` D-014.
10. **Packets R1–R19.** Named in the site review running list; their
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
| E | Dravidian, Munda and unidentified substrate claims | Symmetry between an attested family and a hypothetical donor; "unknown" used as positive evidence — *both halves run 2026-09-07: corpus-internal (item 4) and comparative (item 6). Distinctions 4, 8, 9 and 10 remain on `HOLD-002`, `HOLD-003` and `HOLD-004`.*
| F | *kīnāśa* and agricultural vocabulary | Accepting the etymology, or dismissing it as resemblance, without the lemma work |
| G | BMAC/Oxus and pre-split Indo-Iranian contact | Reading "Proto-Indo-Iranian" as pre-contact or purely inherited |
| H | Rigvedic and Old Avestan social worlds | A violent-Indic versus peaceful-Iranian binary; genre mistaken for society |
| I | Rigvedic society, patronage and canonization | Sanitizing patronage as timeless spirituality |
| J | The Rigvedic forts | Translating *pur* into a Mature Harappan city; one famous count standing for the corpus |
| K | Indus writing and institutional discontinuity | Concluding that populations vanished because institutions and archives did |
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

- **Retrieve the substrate literature.** `HOLD-004`. Witzel 1999,
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
  `RA-006` is programme-wide: every domain where one side of an
  argument sits in retrievable data and the other in unretrievable
  literature.

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

## Item numbering

This list is append-only and its numbers are identifiers, not positions. Two
branches cut from the same base each appended to it, so the free numbers were
allocated once across both rather than twice from the same position. Old
number to new, with the branch that holds the item:

| Old | New | Item | Branch |
|---|---|---|---|
| 5 | 5 | Controller amendment | `main` (PR #6), moved from **Now** to **Done** by PR #10 |
| — | 6 | Domain E, comparative half | `claude/domain-e-research-queue-z83m9b` (PR #10) |
| — | 7 | Prompt-pack intake | `claude/prompt-pack-inventory-reconcile-iz1phs` (PR #14) |
| — | 8 | Register intake for Who Made the Past | `claude/prompt-pack-inventory-reconcile-iz1phs` (PR #14) |
| 6 | 9 | Backlog reconciliation | `main` |
| 7 | 10 | Packets R1–R19 | `main` |

A reference to a queue item number in a file written before 2026-09-07 is
read through this table. No item was removed; nothing above item 5 moved.
