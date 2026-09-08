# Repository map

**Written:** 2026-09-08 · **Class:** control plane. Not research.
**Standing:** this file is authoritative for *what each folder is for*. It is
not authoritative for any claim about the past, and it promotes nothing.
Where it describes a folder's contents it describes the tree at the commit
that carries it; `04-AUDITS/path-migration-build.py` regenerates the machine
-readable half (`PATH-MIGRATION.csv`) so the two cannot drift silently.

Governing documents, in the order they win:
`00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` (method) ·
`00-CONTROLLER/CONTROLLER-RECONCILIATION.md` (which governs where the two
disagree) · `CLAUDE.md` (operating controller) · this file (folder authority).
This file adds no evidence rule. Every constraint below cites the document it
comes from.

---

## 0. Why this file exists

The 2026-09-07 cross-repository audit found that the repository contains
several overlapping operating systems rather than one, that folder numbering
had become a namespace (`06-` twice, `13-` carried in from a rejected archive
scheme, `07`/`08`/`10`/`11`/`12` absent), and that no document said which
folder was authoritative for what. Nothing here renumbers or moves anything —
the audit's own instruction is that the enumeration comes before the move.
What this file does is give every folder one authority, one allowed-content
rule, and one responsible writer, so that a later structural migration is a
mechanical operation rather than an editorial one.

**Numbering is not meaning.** A folder's number records when it was created,
not its rank, its stage, or its dependency order. A gap in the numbering is
not a missing folder and must not be filled to make the sequence look
complete. Reconciliation §4 already ruled that the archive scheme's `11-`–
`19-` numbering "does not survive"; `13-PRODUCT-ARCHITECTURE/` was created
against that ruling and is recorded as a misapplied number in
`CONTRADICTION-REGISTER.csv`, not corrected in place.

## 1. Reading the table

- **Authority** — the one question this folder is the last word on. If two
  folders answer the same question, one of them is wrong and the conflict has
  a row in `00-CONTROLLER/CONTRADICTION-REGISTER.csv`.
- **Allowed contents** — what may be added. Anything else is misfiled.
- **Inputs** — what the folder legitimately reads from.
- **Outputs** — what other folders may read from it.
- **Responsible writer** — the agent role in `.claude/agents/` that writes
  here, from `00-CONTROLLER/PROGRAMME.md`'s lane table. `director` is the
  coordinating session. A role named here does not make anything true: an
  agent is a Claude subagent, and its output is model-generated until a named
  human reviews it (`AI-AGENT-ROSTER.md`).

---

## 2. The folders

### `00-CONTROLLER/` — control plane

| | |
|---|---|
| **Authority** | Method, controller reconciliation, folder authority, path migration, canonical-file selection, control-plane contradictions. |
| **Allowed contents** | The methodology constitution (committed unchanged); the reconciliation; the programme's operating structure; this map; `PATH-MIGRATION.csv`; `CANONICAL-FILES.csv`; `CONTRADICTION-REGISTER.csv`. No claim rows. No source rows. |
| **Inputs** | The owner's constitution; `CLAUDE.md`; the cross-repository audit; the tree itself, read mechanically. |
| **Outputs** | Rules other folders run under; the crosswalk any future move uses. |
| **Responsible writer** | director. |
| **Not allowed** | Evidence claims, retrieval events, product specifications, public copy. |

`RESEARCH-CONSTITUTION.md` sits here for historical reasons and is **not** a
controller: it is a verbatim copy of §11 of the inherited handoff, marked
`INHERITED-UNVERIFIED` on its own first line, and nothing cites it as
governing (reconciliation C-8). `CANONICAL-FILES.csv` records it as
`INHERITED`.

### `01-INHERITED/` — inherited intake

| | |
|---|---|
| **Authority** | What prior threads said, preserved exactly. Authoritative for *the record of what was claimed*, never for whether it is true. |
| **Allowed contents** | Handoffs, running lists, curatorial audits, reconciliations *of* inherited material, as received. Additions only; no corrections in place. |
| **Inputs** | Material supplied by the owner from outside this repository. |
| **Outputs** | Claims for `03-REGISTERS/inherited-claims.csv`, all at `INHERITED-UNVERIFIED`. |
| **Responsible writer** | director, on intake only. |
| **Not allowed** | Citation as evidence. `AGENTS.md` §6: nothing here may be cited as evidence; it is a claim inventory. Promotion out of it requires a logged retrieval (`CLAUDE.md`, the inheritance rule). |

Files here keep their original identifier spellings, including the handoff's
own `D-01`–`D-20` series, which this repository writes as `HD-01`–`HD-20`
everywhere it speaks in its own voice (reconciliation C-4).

### `02-SOURCES/` — source authority

| | |
|---|---|
| **Authority** | Retrieval events, source identity (`SRC-`), and declared dependence between sources (`DEP-`). Nothing else may allocate a `SRC-`. |
| **Allowed contents** | `access-ledger.csv`; `dependency.csv`; retrieval manifests and notes. |
| **Inputs** | Actual retrieval attempts, with timestamps, and the egress proxy's answer. |
| **Outputs** | The set every `source_id` in every register must resolve into; the graph `independence_group` is computed from. |
| **Responsible writer** | retriever; source-genealogist for `dependency.csv`. |
| **Not allowed** | Claims about the past. A ledger row records that a probe happened and what it returned, not that anything is true. `D-042` records that reachability is a timestamped probe, not a standing property. |

### `03-REGISTERS/` — claim authority

| | |
|---|---|
| **Authority** | Claims, measurements, occurrences, hypothesis eligibility, cross-domain bridges, and — since 2026-09-08 — the claim→source join (`CLAIM-SOURCES.csv`) and the separated status dimensions (`CLAIM-STATUS.csv`). |
| **Allowed contents** | CSV registers, one row per claim/observation; the method note for a register lives in `04-AUDITS/`. Draft public copy in the step-14 shape may sit here as `*-draft-copy.md`, marked as draft. |
| **Inputs** | `02-SOURCES/` for every `source_id`; scripts in `04-AUDITS/` that regenerate derived tables. |
| **Outputs** | Everything downstream: briefs, audits, public copy, the evidence gate. |
| **Responsible writer** | corpus-analyst (measurements), chronology-gate (eligibility), director (interpretations), museum-translator (draft copy only after review). |
| **Not allowed** | A row with no status; a status outside the vocabulary; a `VERIFIED` row with no resolving `source_id`, locator and retrieval date. |

**One evidence gate.** `CLAIM-STATUS.csv.evidence_status` is the single
gate; the register's own `status` column is its mirror and the validator
fails any disagreement between them. The other three dimensions
(`interpretive_status`, `editorial_status`, `publication_status`) are
addressable but never gate anything on their own.

### `04-AUDITS/` — assurance

| | |
|---|---|
| **Authority** | Method notes, reproducibility scripts, bias-failure log (`BF-`), re-audit queue (`RA-`), archive-and-power audit (`APA-`), internal evidence contradictions (`IC-`), migration holds (`MH-`), the override log, and the validator. |
| **Allowed contents** | Audit CSVs, method notes, the scripts that regenerate derived registers, dated review reports. |
| **Inputs** | `02-SOURCES/`, `03-REGISTERS/`, and the tree read mechanically. |
| **Outputs** | Findings, not claims. A finding here does not change a register row; it queues the row for re-audit. |
| **Responsible writer** | adversarial-reviewer (reports, never edits), historiography-auditor, corpus-analyst (scripts), director (validator, override log). |
| **Not allowed** | Editing a register to make the validator pass. `CLAUDE.md`: correction history is preserved; a `REJECTED` row is never deleted. |

A dated report here (`*-2026-09-07.md`, `identifier-normalisation-brief.md`,
`VALIDATOR-FINDINGS-*.md`) describes the tree at the commit it names and is
**not** a statement about the current tree. `CANONICAL-FILES.csv` marks each
as `HISTORICAL`.

### `05-HOLDS/` — assurance (blocked evidence)

| | |
|---|---|
| **Authority** | Which claims are blocked on an unavailable source, and what would unblock each. |
| **Allowed contents** | One markdown file per `HOLD-NNN`. |
| **Inputs** | A failed retrieval logged in `02-SOURCES/access-ledger.csv`. |
| **Outputs** | The `HOLD` evidence status a register row carries. |
| **Responsible writer** | retriever. |
| **Not allowed** | A hold used as an argument. An unreachable source makes a claim `HOLD`, not `PROVISIONAL`. |

### `06-BACKLOG/` — programme

| | |
|---|---|
| **Authority** | The recovered v2 backlog titles (`BL-`), the six programmes (`PROG-`), and coverage against them. |
| **Allowed contents** | `BACKLOG-v2-ITEMS.md` (titles, `INHERITED-UNVERIFIED`); `BACKLOG-COVERAGE.csv`, generated by `04-AUDITS/backlog-coverage-build.py`; the inherited expansion prompt. |
| **Inputs** | The recovered titles; `03-REGISTERS/` for prior research; `melakeela/site` for route coverage, once `D-052` says who owns that mapping. |
| **Outputs** | What is asked for, not what is true. |
| **Responsible writer** | director. |
| **Not allowed** | Hand-editing the generated CSV; filling a scope column from a title. `D-014` is why the seven scope columns are empty. |

### `06-BRIEFS/` — programme (duplicate number)

| | |
|---|---|
| **Authority** | Reconciliation and corpus briefs: derived analysis that writes no register row. |
| **Allowed contents** | Briefs that state their own class and promote nothing. |
| **Inputs** | `03-REGISTERS/`, `01-INHERITED/`, the constitution. |
| **Outputs** | Findings and specifications for a register, never register rows. |
| **Responsible writer** | director; museum-translator for page briefs after review. |
| **Not allowed** | Anything that reads as a register. |

**The `06-` number is allocated twice.** That is a defect, recorded as
`CR-001` in `CONTRADICTION-REGISTER.csv`. It is not repaired here, because a
rename is a move and moves wait for `D-046`.

### `09-DECISIONS/` — decision authority

| | |
|---|---|
| **Authority** | The `D-` namespace and every decision's `status`. `OWNER-DECISIONS.csv` is the last word; `DECISIONS-NEEDED.md` holds the argument and allocates nothing (`CLAUDE.md`, "One identifier namespace"). |
| **Allowed contents** | `OWNER-DECISIONS.csv`; `DECISION-ID-MAP.csv` (rows never removed); the README that states both rules. |
| **Inputs** | Escalations from research in progress; standing product and scope questions. |
| **Outputs** | `detail_ref` targets in `DECISIONS-NEEDED.md`; the set every `D-NNN` reference in the tree must resolve into. |
| **Responsible writer** | director. |
| **Not allowed** | Allocating a number from the highest one visible in a document; a row for an inherited `HD-` decision, which would promote it by clerical act. |

### `13-PRODUCT-ARCHITECTURE/` — programme (misapplied number)

| | |
|---|---|
| **Authority** | The museum/data/product specification. Specification, not research and not site code. |
| **Allowed contents** | Specifications whose every design claim carries a status, and which cite no claim above its register status (reconciliation C-5, rule S-1). |
| **Inputs** | Constitution §12/§13; `03-REGISTERS/` at each claim's actual status; `01-INHERITED/curatorial-audit-v1.1/` marked `INHERITED-UNVERIFIED` at the point of use. |
| **Outputs** | Requirements for `melakeela/site`. |
| **Responsible writer** | director; rights-steward for governance, rights and consent sections. |
| **Not allowed** | HTML, CSS, JavaScript. Whether this folder belongs in this repository at all is `D-012`. |

The `13-` number comes from the archive expansion scheme that reconciliation
§4 rejected. Recorded as `CR-002`; not renumbered here.

### Repository root

| | |
|---|---|
| **Authority** | Orientation and tool adapters only. |
| **Allowed contents** | `README.md` (orientation), `CLAUDE.md` (Claude adapter), `AGENTS.md` (Codex adapter), `AI-AGENT-ROSTER.md`, `DECISIONS-NEEDED.md`, `RESEARCH-QUEUE.md`, `CORRECTIONS-PENDING.md`, `.gitignore`, `.mcp.json`. |
| **Inputs** | Everything below. |
| **Outputs** | Instructions, not evidence. |
| **Responsible writer** | director. |
| **Not allowed** | New root files without a row in `CANONICAL-FILES.csv` naming the function they are authoritative for. |

### `.claude/` and `.github/` — tool adapters

| | |
|---|---|
| **Authority** | None over research. Tool wiring only. |
| **Allowed contents** | `.claude/agents/` role prompts; `.claude/hooks/`; `.claude/settings.json`; `.github/workflows/` for CI. |
| **Inputs** | The rules, which they enforce or restate; they never originate one. |
| **Outputs** | Enforcement. |
| **Responsible writer** | director. |
| **Not allowed** | A rule that exists only here. A constraint in an agent file must trace to `CLAUDE.md`, the constitution, the reconciliation, the inherited handoff, or a `BF-` row (`AI-AGENT-ROSTER.md`). |

---

## 3. Folders proposed but not created

| Proposed | Source | State |
|---|---|---|
| `07-PRODUCT-SPECS/` | reconciliation C-5 | Conditional on `D-012`. Not created. |
| `governance/`, `programme/`, `evidence/`, `assurance/`, `archive/` | 2026-09-07 audit, "minimal canonical structure" | Proposed target of the migration. Not created; `PATH-MIGRATION.csv` carries the crosswalk. Adoption is `D-046`. |
| `08-`, `10-`, `11-`, `12-` | nothing | No governing document assigns these a function. They are gaps in a numbering that carries no meaning. **Do not create a folder to fill a number.** |

## 4. Cross-repository boundary

`melakeela/site` holds implementation and the public projection; this
repository holds claims, sources, decisions, specifications and assurance.
**No site code is written here** (`CLAUDE.md`; reconciliation §4).

The site's route inventory is `SITE-INVENTORY.md` in that repository, not in
this one. It was read on 2026-09-08 at `e6b6b67` and logged as `SRC-089`; the
statements in this repository that called it simply absent are corrected, and
`CR-006` records the residue. Who owns the route→backlog mapping, and whether
`BACKLOG-COVERAGE.csv`'s 95 site-coverage cells are repopulated from it, is
`D-052` — it is an editorial taxonomy, not an audit finding, and this branch
does not guess it.
