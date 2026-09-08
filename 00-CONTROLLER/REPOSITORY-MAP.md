# Repository map

What each folder is for, what may go in it, what it takes in, what it puts
out, and who writes it. One function, one folder, one authority.

`00-CONTROLLER/CANONICAL-FILES.csv` carries the same determination at file
level and is machine-read by the validator. Where this document and that
register disagree, the register governs — it is generated from a classification
the build asserts is complete, and prose drifts.

## The rule this map exists to enforce

A file may not enter this repository without a folder whose authority covers
it. `04-AUDITS/build-canonical-files.py` fails if any tracked path is
unclassified, so "where does this go" is answered before a file is written,
not after.

## The folders

### `00-CONTROLLER/` — governance

| | |
|---|---|
| **Authority** | The methodology constitution as the owner wrote it; `CLAUDE.md` for operating rules; `CONTROLLER-RECONCILIATION.md` where those two differ |
| **Allowed** | The constitution, the reconciliation, the programme structure, the repository map, and the control-plane registers: path migration, canonical files, contradictions, status dimensions, override log, migration holds |
| **Not allowed** | Claims, sources, measurements, research findings of any kind |
| **Inputs** | Owner instructions; the reconciliation's rulings; audits of this repository |
| **Outputs** | The rules everything else runs under, and the enumerations the validator enforces |
| **Writer** | The director session. `METHODOLOGY-CONSTITUTION.md` is the owner's and is committed unchanged |

`RESEARCH-CONSTITUTION.md` sits here but is not an authority: it is a verbatim
copy of the inherited handoff's §11, kept at `INHERITED-UNVERIFIED`.
Reconciliation C-8.

### `01-INHERITED/` — preserved prior-thread material

| | |
|---|---|
| **Authority** | The inheritance rule in `CLAUDE.md`. Nothing here has evidentiary standing |
| **Allowed** | Handoffs, prior-thread audits, running lists, recovered documents — as received |
| **Not allowed** | Editing, correcting or renumbering what is preserved. Citing anything here as evidence |
| **Inputs** | Prior chat threads and supplied archives |
| **Outputs** | A claim inventory. Everything extracted from it enters `03-REGISTERS/` as `INHERITED-UNVERIFIED` |
| **Writer** | Nobody writes here. Material is deposited and left alone |

The `D-01`–`D-20` spelling in the handoff stays. `HD-01`–`HD-20` is how this
repository refers to those decisions in its own voice.

### `02-SOURCES/` — what was opened and when

| | |
|---|---|
| **Authority** | `access-ledger.csv` for retrieval events; `dependency.csv` for source dependence |
| **Allowed** | The ledger, the dependency register, retrieval manifests, corpus pins and hashes |
| **Not allowed** | Claims. A ledger row records that a source was opened, never what it shows |
| **Inputs** | Retrieval attempts, including the failed ones and the egress-blocked ones |
| **Outputs** | `SRC-` identifiers that every `VERIFIED` claim must resolve to |
| **Writer** | `retriever`; `source-genealogist` for dependency |

`SOURCE-DEPENDENCY.json` is not created. If a JSON consumer appears it is
generated from the CSV, never hand-maintained beside it. D-013.

### `03-REGISTERS/` — claims, measurements and their sources

| | |
|---|---|
| **Authority** | `CLAUDE.md` register format; `claim-sources.csv` for the claim-to-source relation |
| **Allowed** | Claim registers with an `evidence_status`; measurement and occurrence tables without one; the eligibility registers; the cross-domain bridge register; the generated claim/source join |
| **Not allowed** | Prose findings, briefs, public copy that is not marked draft, and any register whose rows have no identifier |
| **Inputs** | Measurements from `04-AUDITS/` scripts; ledger rows from `02-SOURCES/` |
| **Outputs** | The claims the rest of the project may cite, each with a status and a locator |
| **Writer** | `corpus-analyst` for measurements; the director session for interpretations; generators for `inherited-claims.csv` and `claim-sources.csv` |

A claim register and a data table are different things. A data table's rows are
evidence for a claim stated elsewhere and must not be counted as claims;
`claim-sources.csv` marks which is which in `register_class`.

### `04-AUDITS/` — method, measurement and adversarial control

| | |
|---|---|
| **Authority** | Constitution §9 for the required audit registers; `PROGRAMME.md` for when each runs |
| **Allowed** | Reproducible measurement scripts and their method notes; the bias-failure log; the re-audit queue; the archive-and-power audit; contradictions in the evidence; the validator and the generators |
| **Not allowed** | Claims presented as findings. A script's output is a measurement until a register says otherwise |
| **Inputs** | Pinned corpora named in `02-SOURCES/` manifests |
| **Outputs** | Measurements, method failures, and the mechanical verdict on the whole tree |
| **Writer** | `corpus-analyst`, `historiography-auditor`, `adversarial-reviewer` |

`INTERNAL-CONTRADICTIONS.csv` here is for contradictions **in the evidence**.
Contradictions in the control plane — controllers, statuses, counts,
identifiers, route inventories, decisions — go to
`00-CONTROLLER/CONTRADICTION-REGISTER.csv`. Two registers, two subjects, no
overlap.

### `05-HOLDS/` — claims blocked on source access

| | |
|---|---|
| **Authority** | `CLAUDE.md`: a `HOLD` row names what is needed and work continues |
| **Allowed** | One file per hold, naming the source, what it would settle, and what unblocks it |
| **Not allowed** | Holds on anything but source access. A row that cannot be migrated goes to `MIGRATION-HOLDS.csv`; a decision that blocks goes to `DECISIONS-NEEDED.md` |
| **Inputs** | Failed retrievals, egress blocks, paywalls |
| **Outputs** | `HOLD-` identifiers that a claim's `evidence_status` can point at |
| **Writer** | `retriever` |

### `06-BACKLOG/` — the 89-item backlog and its coverage

| | |
|---|---|
| **Authority** | Constitution §10 for the column set; the generator for the rows |
| **Allowed** | Recovered titles, the coverage table, the expansion prompt as inherited material |
| **Not allowed** | Hand-editing the coverage CSV; inferring an item's scope from its title |
| **Inputs** | The original backlog text (absent, D-014); a route inventory (absent, in the other repository) |
| **Outputs** | One row per `BL-` and `PROG-` item |
| **Writer** | `04-AUDITS/backlog-coverage-build.py` |

### `06-BRIEFS/` — research briefs

| | |
|---|---|
| **Authority** | Constitution step 14, at brief level (reconciliation C-9) |
| **Allowed** | Briefs drafted from accepted claims, each naming every `claim_id` it rests on and the weakest status among them |
| **Not allowed** | Production HTML, CSS or JavaScript. The site is `melakeela/site` |
| **Inputs** | Claims that passed adversarial review |
| **Outputs** | Page briefs and public copy drafts |
| **Writer** | `museum-translator`, and only after review |

**This folder shares stage number 06 with `06-BACKLOG/`.** That is a real
namespace defect, recorded as CR-007. The repair is that numbering leaves the
folder names — `programme/backlog/` and `programme/briefs/` — not that a spare
number is invented. Nothing moves until `PATH-MIGRATION.csv` is acted on.

### `09-DECISIONS/` — owner decisions

| | |
|---|---|
| **Authority** | `OWNER-DECISIONS.csv` for the `D-` namespace and for every decision's status |
| **Allowed** | The register, the identifier alias map, the directory guide |
| **Not allowed** | Allocating a `D-` number from anywhere but this register. Removing a row, ever |
| **Inputs** | Escalations from research in progress; standing product and scope questions |
| **Outputs** | `D-` identifiers; the status of each decision |
| **Writer** | The director session |

`DECISIONS-NEEDED.md` at the root holds the prose case for the subset that
blocks. It allocates nothing and the CSV governs on conflict.

### `13-PRODUCT-ARCHITECTURE/` — product and museum specification

| | |
|---|---|
| **Authority** | None settled. D-012 asks whether specifications belong in this repository at all |
| **Allowed** | Specifications, on the standing rule that no specification may cite a claim above its register status |
| **Not allowed** | Site code; treating a specification's counts as current facts |
| **Inputs** | Accepted claims; owner product decisions |
| **Outputs** | Requirements and acceptance criteria |
| **Writer** | The director session |

**The folder number is a defect.** It carries the constitution §15 archive
expansion scheme into the repository, which reconciliation §4 rules does not
survive. CR-008.

### `.claude/` and `.github/` — tooling

| | |
|---|---|
| **Authority** | `PROGRAMME.md` for agent lanes; `AI-AGENT-ROSTER.md` for what the agents are and are not |
| **Allowed** | Agent definitions, hook wiring, the local pre-push hook, CI workflows |
| **Not allowed** | Describing the local hook as the gate. It is early feedback in one client |
| **Inputs** | The validator |
| **Outputs** | A mechanical verdict, on every push and pull request in CI |
| **Writer** | The director session |

## Numbering

The numbers do not identify functions. `06` names two folders; `07`, `08`,
`10`, `11` and `12` name none; `13` carries a numbering the reconciliation
rejected. Do not fill the gaps — a folder is created when a function and an
authority are defined, and `PATH-MIGRATION.csv` proposes the unnumbered
structure that removes the question. Numbering leaves folder names; stable
identifiers stay in records, where they belong.

## What is not here

- **No route registry.** No file in this repository maps the public site's
  routes. `supports_page` values are mostly marked proposed and are not an
  inventory. CR-017.
- **No actor register.** People, institutions and communities named in prose
  have no register recording role class and engagement state, which is how a
  citation can read as a relationship. Being named is not being engaged.
- **No rights, consent or community-authority registers.** Specified in the
  constitution; not built.
