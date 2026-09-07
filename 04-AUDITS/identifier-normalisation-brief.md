# Identifier normalisation brief

**Date:** 2026-09-07
**Tree audited:** `181ccf2` (`main` at the time of writing). This branch adds
this brief and one row — `D-036` — to `09-DECISIONS/OWNER-DECISIONS.csv`. Every
count below is against `181ccf2`, so the `D-` span in §2.1 reads 001–035; with
this branch applied it reads 001–036. Nothing else the brief audits is changed.
**Class:** report. **Nothing in this repository is renumbered by this brief.**

## 0. What this document is, and what standing it has

This is not a register and it makes no claim about the world. Every statement
below is a statement about files in this repository at the commit named above,
and each is re-derivable by a command given in §8. Where a count appears it is
a count of matches in the tree, not a finding about anything outside it. No
row here is promoted, demoted or given an evidence status; the evidence-status
vocabulary in `CLAUDE.md` governs claims about the past, and this brief makes
none.

It was commissioned to describe parallel identifier series on `main`, what each
holds, and what normalising them would cost in broken references, and to set
out the live case of the question whether the constitution's twelve mandated
registers accumulate under their mandated names or split per domain. It states
the consequences of each option and does not choose.

---

## 1. The premise as commissioned, against the tree

The commissioning brief states that `main` carries three parallel series from
concurrently-running branches. Two of the three do not exist, and the third is
not a parallel pair. The underlying tension is real; it sits somewhere else,
and §3 locates it.

| As commissioned | On `main` at `181ccf2` |
|---|---|
| `BF-` alongside `BF-E-` | No `BF-E-` identifier exists. `grep -r "BF-E"` over the tree returns nothing, and `git log --all -S"BF-E"` returns no commit that ever added or removed such a string on any branch. `BF-001` to `BF-006` is one series in one file, `04-AUDITS/BIAS-FAILURE-LOG.csv`. |
| `RA-` alongside `RA-E-` | No `RA-E-` identifier exists, on the same two tests. `RA-001` to `RA-005` is one series in `04-AUDITS/REAUDIT-QUEUE.csv`. |
| `HYPOTHESIS-ELIGIBILITY.csv` and `domain-e-hypothesis-eligibility.csv`, "same eleven distinctions, different evidence" | Only the second file exists. `HYPOTHESIS-ELIGIBILITY.csv` has never existed on any branch; it is a **mandated name that no file yet occupies** (constitution §9, placement `03-REGISTERS/` under reconciliation C-3). There is therefore no second body of evidence and no divergence between two eligibility registers — there is one register, holding the eleven §4.E distinctions as `E-1` to `E-11`. |
| "This is the live case of D-037" | `D-037` is not allocated. `09-DECISIONS/OWNER-DECISIONS.csv` runs `D-001` to `D-035` with no gaps. The next free identifier is **`D-036`**, and the decision is registered there by this brief. |

The last row is itself an instance of the failure this brief is about. `D-037`
was a number carried in from outside the register, and `CLAUDE.md` says
explicitly: allocate the next free `D-` from the CSV, never from the highest
number you happen to see in a document. Had the number been taken at face
value, `D-036` would have been skipped and a gap left in the authoritative
namespace — the same mechanism that produced the `D-004`/`D-005`/`D-006`
collision on 2026-09-07, when two branches each took "the next free number"
from a different file. **`D-037` in the commissioning brief resolves to
`D-036` in this repository.** No row is added to
`09-DECISIONS/DECISION-ID-MAP.csv` for it: that map resolves identifiers that
once stood in repository files, and `D-037` never did.

> **Note added 2026-09-07, on merging `main` into
> `claude/domain-e-research-queue-z83m9b` (PR #10).** The paragraph above and
> the table row it follows are preserved as written and still describe
> `181ccf2` correctly. They are no longer a description of the current tree.
> That branch had independently allocated `D-036` to a domain E egress ruling
> and `D-037` to `D-041` to five further decisions; on merge, its `D-036` was
> reassigned to `D-042` — the next free identifier above `main`'s highest — and
> `main`'s `D-036` is unchanged. On the second merge of `main`, dated the same
> day, the branch's `D-037` moved in turn: `main` had merged PR #17, which
> allocated `D-037` to the question of which section of
> `MELA-KEELA-WHO-MADE-THE-PAST.md` carries the racialization-of-"Aryan"
> programme. The egress-allowlist question is therefore now `D-043` —
> `D-038` to `D-042` stand above `main`'s highest but are held by this
> branch's own rows — and `main`'s `D-037` is unchanged.
> `09-DECISIONS/OWNER-DECISIONS.csv` now runs `D-001` to `D-043`, and
> **`D-037` is allocated**, to the section-numbering question on `main`.
> Every `D-037` in this brief means the number as it stood in the
> commissioning brief, which is an identifier outside this repository and is
> still resolved by §1 as `D-036`; it does **not** refer to the register row
> now at `D-037`. `main` has since added the `DECISION-ID-MAP.csv` row that
> §1 said was unnecessary, keyed to this file, because the brief itself now
> names the number: a bare `D-037` here resolves to `D-036`. The
> reassignments of the branch's `D-036` to `D-042` and of its `D-037` to
> `D-043` are recorded in the same map, keyed by branch.

### 1.1 Why the two series are single, and what that already settles

`BIAS-FAILURE-LOG.csv` and `REAUDIT-QUEUE.csv` are not accidentally single.
Both carry rows from two different research domains, allocated on different
days by different units of work:

- `BF-001` to `BF-004` — domain E (Rigvedic retroflexion, hydronyms, Dravidian
  and Para-Munda gating, the stratification null).
- `BF-005` to `BF-006` — domain M (Brahui leave-one-out geography, North
  Dravidian subgrouping and the independence assumption).
- `RA-001` to `RA-003` — raised by `BF-002`, `BF-004` and by ledger row
  `SRC-045`.
- `RA-004` to `RA-005` — raised by `BF-005` and `BF-006`.

The two blocks are not separable in place. `BF-001` to `BF-004` are cited from
domain M files (`domain-m-brahui-position.csv`, `domain-m-method.md`,
`brahui-loo-geography.py`, `north-dravidian-cognate-sharing.py`), and
`BF-005`/`BF-006` are cited from `REAUDIT-QUEUE.csv` and `RESEARCH-QUEUE.md`.
The cross-domain citation is the point of the register: `BF-006`'s future
control ("any measurement over two or more languages states whether it assumes
independence") is a control on all later work, not on domain M's work. A
per-domain bias log could not have expressed it.

---

## 2. Complete identifier inventory

### 2.1 Series this repository allocates in its own voice

| Series | Span | Allocated in | Cited in | Occurrences |
|---|---|---|---|---|
| `SRC-` | 001–050 | `02-SOURCES/access-ledger.csv` | 28 files | 3527 |
| `DEP-` | 001–009 | `02-SOURCES/dependency.csv` | 9 files | 36 |
| `IH-` | 001–369 | `03-REGISTERS/inherited-claims.csv` | 16 files | 584 |
| `DME-` | 001–026 | `03-REGISTERS/domain-e-claims.csv` | 8 files | 132 |
| `DMB-` | 001–026 | `03-REGISTERS/domain-m-brahui-position.csv` | 11 files | 149 |
| `PUR-` | 001–028 | `03-REGISTERS/rigveda-pur-family.csv` | 11 files | 118 |
| `PUR-OCC-` | 001–106 | `03-REGISTERS/rigveda-pur-family-occurrences.csv` | 2 files | 108 |
| `HYD-` | 001–469 | `03-REGISTERS/domain-e-hydronyms.csv` | 1 file | 469 |
| `RES-` | 001–253 | `03-REGISTERS/domain-e-retroflex-residue.csv` | 2 files | 254 |
| `E-` | 1–11 | `03-REGISTERS/domain-e-hypothesis-eligibility.csv` | 5 files | 58 |
| `BF-` | 001–006 | `04-AUDITS/BIAS-FAILURE-LOG.csv` | 8 files | 36 |
| `RA-` | 001–005 | `04-AUDITS/REAUDIT-QUEUE.csv` | 6 files | 18 |
| `HOLD-` | 001–004 | `05-HOLDS/` (one file per hold) | 21 files | 59 |
| `BL-` | 01–89 | `06-BACKLOG/BACKLOG-COVERAGE.csv` | 2 files | 93 |
| `PROG-` | 01–06 | `06-BACKLOG/BACKLOG-COVERAGE.csv` | 2 files | 10 |
| `C-` | 1–9 | `00-CONTROLLER/CONTROLLER-RECONCILIATION.md` (§3 conflicts) | 4 files | see §3.2 |
| `D-` | 001–035 (001–036 with this branch applied) | `09-DECISIONS/OWNER-DECISIONS.csv` | 20 files | 355 |
| `HD-` | 01–20 | `09-DECISIONS/DECISION-ID-MAP.csv` (renaming of the inherited `D-NN`) | 7 files | 120 |

### 2.2 Series inherited, not allocated here

These come in through `01-INHERITED/` and through the curatorial audit. They
are read where they stand or resolved through `DECISION-ID-MAP.csv`. None is a
namespace this repository may extend.

| Series | Span | Origin | What it holds |
|---|---|---|---|
| `D-` (two-digit) | 01–20 | `01-INHERITED/claude-project-handoff.md` §4 | Prior-thread owner decisions. Renamed `HD-01`–`HD-20` wherever this repository speaks in its own voice; the two inherited files keep the old spelling by design. |
| `C-` (zero-padded) | 01–41 | handoff | Corrections logged in prior threads. |
| `V-` | 01–25 | handoff | Verified-in-thread rows. |
| `P-` | 01–26 | handoff | Page-level items. |
| `S-` | 01–14 | handoff | Source items. |
| `H-` | 01–12 | handoff | Hypotheses. |
| `R-` | 01–27 | handoff | Rejected propositions. |
| `X-` | 01–19 | handoff, carried into the curatorial audit `SCHEMA.md` | Internal contradictions. Present in this repository only as tags in the `notes` column of `IH-250`–`IH-268`, not as an allocated namespace. |
| `Q-` | 04 | handoff | Single stray reference. |
| `VELI-` | 00–13 | handoff | Names of prior documents, not claims. |
| `LS-` | 01–51 | `01-INHERITED/site-review/` | Running-list items. |
| `AS-` | 01–08 | site-review | Asset items. |
| `COR-` | 01–18 | site-review | Corrections. |
| `RV-` | 01–02 | site-review | Two derived specifications. `06-BRIEFS/rv01-reconciliation.md` is this repository's brief *against* `RV-01`; it does not extend the series. |

Everything in §2.2 sits at `INHERITED-UNVERIFIED` in
`03-REGISTERS/inherited-claims.csv` and carries no evidentiary standing here.

---

## 3. Where parallelism actually exists

Four kinds, in descending order of how well the repository already handles them.

### 3.1 Resolved and mapped — the `D-` namespace

Two defects, both found and fixed on 2026-09-07, both recorded rather than
silently corrected:

1. `DECISIONS-NEEDED.md` and `OWNER-DECISIONS.csv` were allocating `D-` numbers
   independently, and `D-004`, `D-005` and `D-006` each named two different
   decisions. The CSV block kept its numbers because `D-004`–`D-011` maps
   one-to-one onto constitution §14 bullets 1–8; the three prose sections
   became `D-032`–`D-034`.
2. The inherited handoff's own `D-01`–`D-20` collided by appearance with this
   repository's `D-0NN`. They were renamed `HD-` in the repository's own files
   and left unedited in the two inherited ones.

`09-DECISIONS/DECISION-ID-MAP.csv` carries 54 rows, keyed by *old identifier
plus the file it appeared in*, because a bare `D-004` in a pre-2026-09-07
document is ambiguous without knowing which file was meant. Rows are never
removed. This is the working model for how a collision is retired in this
repository, and §5 should be read against it: the cost of the fix was three
renumbered prose sections and one map file, and it was paid because the
alternative was a permanently ambiguous authoritative namespace.

### 3.2 Live and unmapped — the `C-` series

**This is the one genuine unresolved identifier collision on `main`.** Two
series share the prefix `C-` and are distinguished only by a leading zero:

| | Unpadded `C-1` … `C-9` | Zero-padded `C-01` … `C-41` |
|---|---|---|
| Holds | The nine conflicts between `CLAUDE.md` and the methodology constitution, with their resolutions | The 41 corrections logged in prior chat threads |
| Allocated in | `00-CONTROLLER/CONTROLLER-RECONCILIATION.md` §3 | `01-INHERITED/claude-project-handoff.md` |
| Standing | This repository's own reasoning; `C-1` and `C-3` are cited from `CLAUDE.md` itself | `INHERITED-UNVERIFIED` (`03-REGISTERS/inherited-claims.csv`, 180 occurrences) |
| Also cited in | `06-BRIEFS/rv01-reconciliation.md` (C-1…C-7, C-9), `13-PRODUCT-ARCHITECTURE/museum-framework.md` (C-1…C-5) | `00-CONTROLLER/RESEARCH-CONSTITUTION.md` (25), `02-SOURCES/dependency.csv` (C-05), `03-REGISTERS/domain-e-claims.csv` and `rigveda-pur-family.csv` (C-04, C-05), `04-AUDITS/rigveda-pur-family-method.md` (C-04, C-05) |

`00-CONTROLLER/CONTROLLER-RECONCILIATION.md` cites **both**: its §C-8 text
refers to the inherited `C-06`, `C-16`, `C-17` and `C-38` while the document's
own headings are `C-1` to `C-9`. A reader who normalises the padding — or a
script that does — merges two unrelated series. Nothing in the repository
currently states the rule that the leading zero is load-bearing.

Two further points make this less alarming than it reads, and they belong in
the record rather than in a fix:

- The ranges do not yet overlap in a way that produces a *silent* wrong
  resolution for most references: `C-10` and above can only be inherited, and
  the padded/unpadded distinction is consistently observed in every file
  checked. The exposure is `C-01`–`C-09` against `C-1`–`C-9`, nine pairs.
- `C-04` and `C-05` are the two inherited corrections most cited by live
  research files (the stem-search over-count and its companion), and both are
  cited in padded form in every one of those files.

The exposure is therefore real but bounded, and it is a *documentation* gap
before it is a renumbering problem. Recording the rule costs nothing and
breaks nothing; renumbering either series would break the reference counts in
the table above.

### 3.3 File-name parallelism — mandated names against domain-scoped names

This is the tension the commissioning brief was pointing at, in its actual
form. The constitution §9 mandates twelve persistent files by bare name;
reconciliation C-3 assigns each a home. Present state:

| # | Mandated name | Home (C-3) | State on `main` |
|---|---|---|---|
| 1 | `METHODOLOGY-CONSTITUTION.md` | `00-CONTROLLER/` | **Exists, mandated name.** |
| 2 | `RESEARCH-INHERITANCE.md` | `01-INHERITED/` | Absent. Function split across `01-INHERITED/claude-project-handoff.md` and `03-REGISTERS/inherited-claims.csv` (369 rows). |
| 3 | `RESEARCH-QUESTION-REGISTER.csv` | `03-REGISTERS/` | Absent, no substitute. |
| 4 | `HYPOTHESIS-ELIGIBILITY.csv` | `03-REGISTERS/` | **Absent under the mandated name.** `domain-e-hypothesis-eligibility.csv` holds 11 rows carrying all 17 mandated columns, in order, with no extras and none missing. Domain M has no eligibility register at all. |
| 5 | `SOURCE-DEPENDENCY.json` | `02-SOURCES/` | Absent pending `D-013`; `dependency.csv` holds 9 rows. |
| 6 | `ARCHIVE-AND-POWER-AUDIT.csv` | `04-AUDITS/` | Absent. |
| 7 | `CROSS-DOMAIN-BRIDGES.csv` | `03-REGISTERS/` | Absent. |
| 8 | `INTERNAL-CONTRADICTIONS.csv` | `04-AUDITS/` | Absent. Nearest is the inherited `X-01`–`X-19` tagging inside `inherited-claims.csv` notes. |
| 9 | `BIAS-FAILURE-LOG.csv` | `04-AUDITS/` | **Exists, mandated name, accumulating across domains E and M.** |
| 10 | `OWNER-DECISIONS.csv` | `09-DECISIONS/` | **Exists, mandated name, accumulating** — 35 rows from every source. |
| 11 | `BACKLOG-COVERAGE.csv` | `06-BACKLOG/` | **Exists, mandated name, accumulating** — 95 rows. |
| 12 | `REAUDIT-QUEUE.csv` | `04-AUDITS/` | **Exists, mandated name, accumulating across domains E and M.** |

**Five of the twelve exist. Four of those five carry the mandated name and all
four accumulate across domains. The fifth is domain-scoped. Seven are absent.**

The single observation that matters most for `D-036`: the split tracks
*directory*, not intent. Every file in `04-AUDITS/`, `06-BACKLOG/` and
`09-DECISIONS/` that answers to a mandated name carries that name and
accumulates. Every file in `03-REGISTERS/` is domain-scoped — seven of seven:
`domain-e-claims`, `domain-e-hydronyms`, `domain-e-hypothesis-eligibility`,
`domain-e-retroflex-residue`, `domain-m-brahui-position`, `inherited-claims`,
`rigveda-pur-family` (plus its occurrences table). The eligibility register was
named by its neighbours, not by a decision. No document states a convention;
the convention is emergent, and it is emergent per directory.

That is worth stating plainly because it means the question is not "which
convention did the repository choose" — it chose neither — but "does the
directory-shaped default get ratified or overridden".

### 3.4 Value-vocabulary drift from concurrent branches

Not identifier parallelism, but the same cause — two branches writing the same
file without seeing each other — and cheaper to fix, so it is recorded here
rather than left to be found again:

| File | Rows | Drift |
|---|---|---|
| `04-AUDITS/REAUDIT-QUEUE.csv` | `RA-001`–`RA-003` vs `RA-004`–`RA-005` | `priority` and `status` uppercase (`MEDIUM`, `HIGH`, `OPEN`) in the first block, lowercase (`medium`, `high`, `open`) in the second. `RA-001` and `RA-003` additionally put prose in the `priority` cell ("HIGH — it affects how every future unit plans its retrievals"), which the other three do not. |
| `04-AUDITS/BIAS-FAILURE-LOG.csv` | `BF-001`–`BF-004` vs `BF-005`–`BF-006` | First block unquoted CSV fields, second block fully quoted. Both parse; a naive `cut -d,` does not. |
| `09-DECISIONS/OWNER-DECISIONS.csv` | `D-035` vs the other 34 | `status` is `open`, against `OPEN` for every other row. `09-DECISIONS/README.md` specifies `OPEN`, `BLOCKED`, `RESOLVED`. |

Three rows are affected in total. This is a filter and sort hazard — any
consumer grouping by `status` sees `open` and `OPEN` as two values — and
correcting it changes no identifier and breaks no reference. It is not
corrected here because this brief is a report; it is queued as fact for
whichever unit next touches those files.

---

## 4. What normalising would cost, counted

Every count is of matches in the tree at `181ccf2`. "Broken references" means
references that would resolve to nothing, or to the wrong thing, if the
operation were performed and nothing else were updated.

### 4.1 Renaming `domain-e-hypothesis-eligibility.csv` to `HYPOTHESIS-ELIGIBILITY.csv`

| | Cost |
|---|---|
| Filename references | **14 occurrences across 7 files** — `RESEARCH-QUEUE.md`, `04-AUDITS/domain-e-method.md`, `04-AUDITS/BIAS-FAILURE-LOG.csv` (`BF-003`'s `affected_claims` cell), `06-BACKLOG/BACKLOG-COVERAGE.csv`, `04-AUDITS/backlog-coverage-build.py`, and this file. |
| Identifier references | **Zero.** `E-1` to `E-11` are already globally unique in the tree; nothing else allocates a bare `E-` series. A merged file keeps them unchanged, and a domain M block would begin at a fresh prefix. |
| Column schema | Zero. The file already carries the 17 mandated columns exactly. |
| Loss of information | The domain scope currently carried by the filename would have to move into a column. There is no `domain` column in the mandated 17, so it would go into `reason` or be added as an 18th — the constitution says the file "must include" those columns, not that it may include no others. |

Consolidation is cheap because a filename appears in prose and a script; an
identifier appears in evidence rows.

### 4.2 Splitting `BIAS-FAILURE-LOG.csv` per domain

| | Cost |
|---|---|
| Filename references | 11 occurrences across 6 files. |
| Identifier references | **36 occurrences across 8 files would need re-checking, and `BF-005`/`BF-006` would have to be renumbered into a domain-M series — 20 occurrences across 5 files.** Cross-domain citations break by construction: `domain-m-brahui-position.csv` and `domain-m-method.md` cite `BF-002`; `REAUDIT-QUEUE.csv` and `RESEARCH-QUEUE.md` cite `BF-005` and `BF-006`. |
| Loss of function | The `future_control` column becomes unenforceable across domains. `BF-006`'s control on independence assumptions, and `BF-001`'s on mechanical classifiers, are controls on *all* later work; in a per-domain file they are controls on one domain and the next domain re-derives them or does not. Constitution §9 says in terms: record the Dravidian/Para-Munda failure, "but do not let it become the only example considered". A per-domain log is the arrangement in which it does. |
| Loss to the re-audit chain | `REAUDIT-QUEUE.csv`'s `raised_by` column points at `BF-` identifiers across the split; every such pointer becomes cross-file. |

### 4.3 Splitting `REAUDIT-QUEUE.csv` per domain

| | Cost |
|---|---|
| Filename references | 8 occurrences across 6 files. |
| Identifier references | 18 occurrences across 6 files; `RA-004`/`RA-005` renumber, 10 occurrences across 4 files. |
| Loss of function | `RA-003` targets `02-SOURCES/access-ledger.csv` and is raised by a ledger row, not by a domain. `RA-005` targets `inherited-claims.csv` rows and is raised by two domain-M failures. Neither belongs to a domain; a per-domain scheme has no home for them. |

### 4.4 Splitting `OWNER-DECISIONS.csv` or `BACKLOG-COVERAGE.csv`

Not costed in detail — no unit of work has proposed it and both are explicitly
single-namespace by controller rule (`CLAUDE.md`, "One identifier namespace")
and by constitution §10 ("one row for every item 1–89"). Recorded here only so
the inventory is complete: `D-` is cited 355 times across 20 files and `BL-` 93
times across 2.

### 4.5 Normalising the `C-` collision

| Operation | Cost |
|---|---|
| Renumber the reconciliation's `C-1`–`C-9` to a new prefix | The nine conflicts are cited from `CLAUDE.md` (C-1, C-3), `06-BRIEFS/rv01-reconciliation.md` (8 refs), `13-PRODUCT-ARCHITECTURE/museum-framework.md` (5 refs) and `README.md`. The controller itself would need editing. |
| Renumber the inherited `C-01`–`C-41` | **Not available.** They are inherited text. `01-INHERITED/claude-project-handoff.md` and `00-CONTROLLER/RESEARCH-CONSTITUTION.md` are not edited, by the same rule that left `D-01`–`D-20` in place; 180 occurrences in `inherited-claims.csv` and 155 in the script that generates it would have to be regenerated under a new prefix, exactly as the `HD-` rename did. |
| Document the padding rule and add a `DECISION-ID-MAP`-style resolution note | Zero broken references. |

The `HD-` precedent shows the middle option is *possible* — that is precisely
what was done for the handoff's `D-NN`. It was done there because the
collision was in the **authoritative decision namespace**, where an ambiguous
reference changes what an owner is being asked. The `C-` collision is between a
controller-reasoning series and an inherited-correction series, neither of
which allocates anything an owner acts on. That is a difference in stakes, not
in kind, and it is the owner's to weigh.

### 4.6 The general shape

Consolidation costs filenames. Splitting costs identifiers. Filenames live in
prose and scripts and are cheap to update and cheap to get wrong visibly.
Identifiers live in evidence rows, in `affected_claims`, `raised_by`,
`source_dependencies` and `supports_page` cells, and a stale one resolves
silently to nothing. The asymmetry is roughly an order of magnitude in this
tree — 14 filename references against 36 identifier references for the
eligibility/bias pair alone — and it is structural, not incidental.

---

## 5. The live decision: `D-036`

**Question.** Do the constitution's twelve mandated registers accumulate under
their mandated names, with domain scope carried in a column, or does each
domain get its own file with the mandated columns?

Registered at `D-036` in `09-DECISIONS/OWNER-DECISIONS.csv`. Referred to as
`D-037` in the commissioning brief; see §1. **This brief states the
consequences and does not choose.**

### Option A — accumulate under the mandated names

Domain scope becomes a column. `domain-e-hypothesis-eligibility.csv` becomes
`03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv` with a domain column; the seven
absent files are created under their mandated names when the work that fills
them begins.

*Consequences.*

- Ratifies what four of the five existing mandated files already do. No
  existing behaviour is reversed.
- Cross-domain controls stay enforceable: one bias log, one re-audit queue, one
  bridges register, one contradictions register. A control written in domain E
  binds domain M without being restated.
- Costs 14 filename references, one time, to move the eligibility register.
- The constitution's literal instruction is followed. §9 names twelve files;
  under Option A there are twelve files.
- Reviewability degrades as the registers grow. `inherited-claims.csv` at 369
  rows and `domain-e-hydronyms.csv` at 469 are already past the size at which a
  diff is read row by row. A twenty-two-domain programme (§4A–V) accumulating
  into one eligibility register would produce a file no reviewer reads whole,
  and Codex reviews the PR.
- Concurrent branches would collide in the same file on every unit of work.
  The `RA-`/`BF-` drift in §3.4 is what that collision looks like when it does
  *not* conflict textually; when it does, it is a merge conflict on every
  parallel domain unit. This is the strongest argument against Option A and it
  is a practical one, not a methodological one.
- Requires an 18th column on `HYPOTHESIS-ELIGIBILITY.csv` and equivalents
  elsewhere. §9 says "must include", which permits additions, but the addition
  is a deviation to log.

### Option B — one file per domain, mandated columns

`domain-e-hypothesis-eligibility.csv`, `domain-m-hypothesis-eligibility.csv`,
and so on; the mandated name names a *format*, not a file.

*Consequences.*

- Ratifies what `03-REGISTERS/` already does — seven of seven files are
  domain-scoped — and what the eligibility register already is.
- Concurrent domain branches never touch the same file. No merge conflicts, no
  value drift of the §3.4 kind between domains.
- Diffs stay reviewable. A domain unit's PR touches its own registers.
- **Breaks the cross-domain function of the audit registers.** Costed at §4.2
  and §4.3: 36 and 18 identifier occurrences to re-check, `BF-005`/`BF-006` and
  `RA-004`/`RA-005` to renumber, and `future_control` reduced from a
  programme-wide control to a domain-local note. Constitution §9's instruction
  not to let one failure become the only example considered is not
  implementable in this arrangement without a second, aggregating file — which
  is Option C.
- Homeless rows have no home. `RA-003` targets the access ledger; `RA-005`
  targets inherited claims; `BF-003`'s failure is about a class of reasoning,
  not a domain. Each needs an arbitrary domain assignment or a residual file.
- Deviates from the constitution's literal twelve-file instruction and needs
  logging as such, in the same class as `D-013`.
- The file count grows as domains × registers. Twenty-two domains against the
  four register-shaped mandated files is a directory of up to 88 files, most of
  them short.

### Option C — split the claim-shaped registers, accumulate the audit-shaped ones

The de facto arrangement on `main`, ratified and made explicit: registers that
hold *evidence about a subject* are domain-scoped (`03-REGISTERS/`); registers
that hold *findings about the method* accumulate under their mandated names
(`04-AUDITS/`, `09-DECISIONS/`, `06-BACKLOG/`). The open question under Option
C is which side `HYPOTHESIS-ELIGIBILITY.csv`, `CROSS-DOMAIN-BRIDGES.csv` and
`RESEARCH-QUESTION-REGISTER.csv` fall on.

*Consequences.*

- Zero cost to adopt for eleven of the twelve; the repository is already doing
  it. Only the eligibility register's placement is genuinely open, at 14
  filename references either way.
- Keeps the cross-domain controls that Option B loses and the reviewable
  per-domain diffs that Option A loses.
- `CROSS-DOMAIN-BRIDGES.csv` is named for a function that is cross-domain by
  definition and would accumulate; `INTERNAL-CONTRADICTIONS.csv` records
  contradictions *between* domains and would accumulate;
  `ARCHIVE-AND-POWER-AUDIT.csv` audits archives, which are not domain-shaped,
  and would accumulate. Under Option C all three are settled by their function
  without a further decision.
- `HYPOTHESIS-ELIGIBILITY.csv` is the hard case and does not resolve on the
  claim/method axis. Gating is a judgement about a hypothesis (claim-shaped,
  argues for split) whose outputs are compared across domains and whose
  `proportional_space` verdicts govern how pages are written (method-shaped,
  argues for accumulation). Either answer is defensible; the decision does not
  disappear under Option C, it narrows to one file.
- Requires the rule to be written down, or the emergent directory convention of
  §3.3 keeps being re-derived by each branch — which is how the `D-004`
  collision happened.

### What the decision does not turn on

- **Column schemas.** All three options keep the mandated columns. The
  eligibility register already carries all 17.
- **Evidence status.** No option promotes or demotes any claim. Renumbering is
  clerical; the inheritance rule is untouched either way.
- **The seven absent files.** They are absent because the work that fills them
  has not been done, not because of a naming dispute. `D-036` decides what they
  are called when they arrive; it does not schedule them.

---

## 6. Out of scope, and deliberately not done

- **Nothing is renumbered.** No `BF-`, `RA-`, `E-`, `C-`, `D-` or any other
  identifier changes value in this brief. Merged identifiers are cited across
  the repository and renumbering them is a decision, not housekeeping.
- **No file is renamed or created** beyond this brief.
- **The §3.4 value drift is recorded, not corrected.** Correcting three cells
  would be within any unit's scope but outside a report's.
- **No row is added to `DECISION-ID-MAP.csv`.** That map resolves identifiers
  that stood in repository files. `D-037` never did; §1 is its resolution.
- **One repository-state change accompanies this brief:** the `D-036` row in
  `09-DECISIONS/OWNER-DECISIONS.csv`. It allocates a new identifier from the
  authoritative CSV, as `CLAUDE.md` requires of any owner decision taken in
  this repository, and it records the three options with no `owner_answer`. It
  renumbers nothing.

## 7. What would change this brief

- **Any file arriving under a mandated name in `03-REGISTERS/`, or any second
  domain-scoped file in `04-AUDITS/`.** Either would break the
  directory-shaped pattern of §3.3, which is the observation Option C rests on.
- **A domain-M hypothesis-eligibility register.** Its filename would settle the
  emergent convention by act before `D-036` is answered — which is the outcome
  this brief exists to prevent.
- **A `C-` reference in a new file that is ambiguous between the two series.**
  That would move §3.2 from a bounded documentation gap to a live defect, and
  the `HD-` precedent would become the model rather than a comparison.
- **A second aggregating register under Option B**, which collapses Option B
  into Option C.
- **Recovery of the full 89-item backlog text (`D-014`)**, which may name
  registers this inventory does not know about.
- **Any count in §2 or §4 failing to reproduce** under the commands in §8.

## 8. Reproducing every count

```sh
# §1 — the two series that do not exist
grep -rn "BF-E\|RA-E" --exclude-dir=.git .          # no output
git log --all -S"BF-E" --oneline                    # no output
git log --all --name-only --pretty=format: | sort -u | grep -i eligib

# §2 — span and citation count for one series (substitute the prefix)
grep -rhoE '\bBF-[0-9]+\b' --include='*.csv' --include='*.md' --include='*.py' . | sort -u
grep -rlE '\bBF-[0-9]+\b' --include='*.csv' --include='*.md' --include='*.py' . | wc -l

# §3.2 — the two C- series, told apart by padding
grep -rhoE '(^|[^A-Za-z-])C-[0-9]{1,2}\b' 00-CONTROLLER/CONTROLLER-RECONCILIATION.md | sort -u
grep -rhoE '(^|[^A-Za-z-])C-[0-9]{2}\b'   01-INHERITED/claude-project-handoff.md | sort -u

# §3.3 — mandated columns present in the eligibility register
head -1 03-REGISTERS/domain-e-hypothesis-eligibility.csv | tr ',' '\n' | nl

# §3.4 — the value drift
cut -d, -f6,7 04-AUDITS/REAUDIT-QUEUE.csv
grep -c '"open"' 09-DECISIONS/OWNER-DECISIONS.csv

# §4 — filename reference cost
grep -roh 'domain-e-hypothesis-eligibility.csv' --include='*.md' --include='*.csv' --include='*.py' . | wc -l
grep -rl  'domain-e-hypothesis-eligibility.csv' --include='*.md' --include='*.csv' --include='*.py' . | wc -l
```

Counts in this brief include this file's own references where the pattern
matches it, and §4.1 says so explicitly for the one case where it materially
affects the number.
