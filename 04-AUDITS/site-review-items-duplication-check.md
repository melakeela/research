# Site-review LS-/COR- items against the handoff register — duplication check

**Run:** 2026-09-07
**Inputs:** `03-REGISTERS/inherited-claims.csv` rows `IH-001`–`IH-369`
(extracted from `01-INHERITED/claude-project-handoff.md`) and rows
`IH-370`–`IH-438` (extracted from
`01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md`, Version 12)
**Method:** `04-AUDITS/site-review-items-extraction.py` for extraction; keyword
cross-match on 26 subject terms across the claim and notes columns, plus an
exact-title collision test.

## Result

**No LS- or COR- item duplicates a claim already registered from the handoff.**
Zero exact title collisions. All 69 rows are new to the register.

This is a difference in kind, not merely in wording. The handoff rows are
**assertions** — corrections, counts, rulings, admitted limitations, each one a
proposition that can be tested and promoted or rejected. The LS-/COR- rows are
**coverage commitments** — questions the running list proposes to investigate.
A coverage row cannot duplicate a claim row, because it asserts nothing about
the world; it asserts only what the running list undertakes to examine.

Registering them together is still correct: both are `INHERITED-UNVERIFIED`
material from prior threads, and both need a retrieval event before anything
built on them can be promoted. But the two groups must not be counted as one
population when reporting register coverage.

## Subject-matter adjacencies

Eight subject areas are addressed by both groups. None is a duplication; each is
a case where an existing handoff claim is **testable by** a scheduled item. These
pairings are the register's most useful product from this extraction, because
they say which research packet would discharge which inherited correction.

| Subject | Handoff claims | Scheduled items | Relationship |
|---|---|---|---|
| Brahui continuity vs. migration | IH-031, IH-034, IH-135, IH-156, IH-236 | LS-46, LS-47, LS-48, LS-51 | **Strongest pairing.** IH-031 records a correction about inverted burden of proof; IH-034 records the counter-asymmetry on Para-Munda. LS-46 "Brahui: Four Histories, Not One" and LS-47 "Continuity Versus Migration" are the programme that would test both. Running them is how IH-031/IH-034 leave `INHERITED-UNVERIFIED`. |
| Brāhmī, script and dating | IH-023, IH-069, IH-098, IH-102, IH-103 | LS-12, LS-13 | IH-023 is a specific correction on the morphology of the word *brāhmī*; LS-13 "Brāhmī Before Aśoka?" is a site-by-site dating question. Adjacent, not the same claim. |
| Substrate vocabulary | IH-022, IH-037, IH-045, IH-137, IH-231 | LS-29, LS-34, LS-51 | IH-037 records that every Witzel position on the platform is second-hand. LS-29 "The Words Whose Languages Vanished" is the lemma-level work that would replace second-hand sourcing with primary. |
| Meluhha / Gulf trade | IH-052, IH-131, IH-174, IH-190, IH-197 | COR-05, COR-06 | IH-052 is a file-packaging defect that merely contains the word; the substantive pairing is IH-131/IH-174/IH-190/IH-197 with COR-06 "Meluhha–Magan–Dilmun". |
| Genetics and ancestry | IH-024, IH-025, IH-030, IH-112, IH-119 | LS-33, LS-46, LS-49 | IH-024 (secondary-summary error) and IH-025 (admixture dates are lower bounds) are exactly the controls LS-49 "Genes Do Not Speak" is scoped to enforce. |
| Tolkāppiyam | IH-248, IH-324 | LS-07, LS-09 | IH-248 records that direct access to Tolkāppiyam is nowhere logged — a source-access gap. LS-07 "Before Tolkāppiyam" cannot start until that access exists. **This is a dependency, and it is not yet on the holds list.** |
| Retroflexion | IH-062, IH-103 | LS-18 | IH-062 is about romanising the name *Veḷi* and is a spurious keyword match. IH-103 is the real adjacency. |
| Forts / *pur* | IH-020, IH-054 | COR-16 | Weak. The repository's own `03-REGISTERS/rigveda-pur-family.csv` is the live work here, and it pairs with RV-01/RV-02 rather than COR-16. |

## Items deliberately not registered

`RV-01` ("The 99 Forts Database") and `RV-02` ("Fort Text Versus Fort
Archaeology") appear in the same Version 12 table as COR-11–COR-13, at
`MELAKEELASITEREVIEWRUNNINGLIST.md` L1214–L1215. The task scoped this extraction
to `LS-` and `COR-` items, so they are excluded.

They should not stay excluded. Both bear directly on
`03-REGISTERS/rigveda-pur-family.csv` and `05-HOLDS/HOLD-001-purandhi-etymology.md`,
which are live work in this repository — RV-01 is a specification for a dataset
the repository has already begun. Registering the `RV-` series is recommended as
a follow-up.

## What would change this result

If the handoff register is later re-read and found to contain rows that are
themselves coverage commitments rather than assertions, the "difference in kind"
argument weakens for those rows and they must be re-checked against the LS-/COR-
set individually. A scan for such rows returned 144 keyword hits, all of which
proved on inspection to be claim rows carrying a work-item cross-reference in
the notes column, not standalone coverage items. That inspection was by sample,
not exhaustive.
