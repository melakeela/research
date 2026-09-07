# Migration report — 2026-09-07

What the control-plane reconciliation changed in the data, row by class, and
how each change was checked. Written so a reviewer can disprove it rather
than take it.

Reproduce every figure here by running, from the repository root:

```
python3 04-AUDITS/migrate-status-dimensions.py   # idempotent; reports what it did
python3 04-AUDITS/build-claim-sources.py
python3 04-AUDITS/validate-registers.py
python3 04-AUDITS/test-validate-registers.py
```

## Validation, before and after

| | Failures | Warnings |
|---|---|---|
| `main` at `aa40d3a` | **53** | not implemented |
| this branch | **0** | **7**, each a `MIGRATION-HOLDS.csv` row |

The 53 were 52 source-reference failures (cells holding several identifiers,
which the validator read as one) and 1 status-vocabulary failure (a status
cell carrying prose). The cross-repository audit of the same date reported
43; it was written against an earlier tree, before further registers landed.
Recorded as CR-012.

The after figure is not comparable to the before figure in scope: the old
validator checked five things over `03-REGISTERS/*.csv`, the new one checks
twelve over every file `CANONICAL-FILES.csv` marks `GATED` or `REPORTED`.
The honest comparison is that the new validator, run against `main`, would
report more than 53, not fewer.

## Status split

`status` → `evidence_status` in 8 claim registers, with
`interpretive_status`, `editorial_status`, `publication_status`,
`status_reason` and `superseded_by` appended.

| Register | Rows |
|---|---|
| `03-REGISTERS/inherited-claims.csv` | 369 |
| `03-REGISTERS/domain-e-measurements.csv` | 30 |
| `03-REGISTERS/rigveda-pur-family.csv` | 28 |
| `03-REGISTERS/domain-e-claims.csv` | 26 |
| `03-REGISTERS/domain-m-brahui-position.csv` | 26 |
| `03-REGISTERS/domain-e-hypothesis-eligibility.csv` | 11 |
| `03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv` | 10 |
| `03-REGISTERS/domain-e-interpretations.csv` | 10 |
| **total** | **510** |

**Nothing was promoted.** All 510 rows carry `UNASSIGNED` in all three new
dimensions. `UNASSIGNED` asserts nothing; it is not a weak `PROPOSED` or a
provisional `DRAFT`. Release eligibility is consequently 0 of 510, which is
the truthful state: no claim in this repository has been through the
adversarial-review loop that `editorial_status: APPROVED` would record.

**One cell was decomposed**, not rewritten:

> `domain-e-hypothesis-eligibility.csv` row 12 (E-11)
> was `VERIFIED as a measurement; not a claim about origins`
> is `evidence_status=VERIFIED`, `interpretive_status=MEASUREMENT-ONLY`,
> `status_reason` = the original string, verbatim.

The cell already said `VERIFIED`; it was unparseable, not unstated. Nothing
was added to it and nothing was dropped.

**Every other original cell is byte-identical to its pre-migration value.**
Checked by reading `git show aa40d3a:<file>` and the current file into
dictionaries and comparing every column of every row. One mismatch, the one
above. The check is not a claim about the script's intent; it is a
comparison of the two files.

### Gate verdicts

`gate_verdict` added to the two eligibility registers, 21 rows, parsed from
the leading term of `eligible_for_extended_analysis`, whose prose is
untouched. The two registers were written in different vocabularies for the
same column — one in `ELIGIBLE` / `NOT-ELIGIBLE-SOURCE-BLOCKED` terms, one
answering the column heading `YES` / `NO` — and the synonym table that reads
both into one is in the migration script, listed line by line, longest-prefix
first so `NO - FOR LACK OF SOURCES` cannot be swallowed by bare `NO`. That
the two disagree is CR-006 and MH-003; parsing them is not merging them.

Gate verdicts were previously admitted into the claim status vocabulary by
the validator itself. They no longer are (CR-016).

### Other status columns

- `04-AUDITS/REAUDIT-QUEUE.csv`: 11 decompositions. Case normalised on 4
  cells; `OPEN - blocked on X` split into `status=OPEN` plus `blocked_by=X`
  on 4 rows, with the original preserved in `status_reason`; two priority
  cells with prose appended split into `priority` plus `priority_reason`.
  The declared token never changed — a row that said `OPEN` still says
  `OPEN`.
- `09-DECISIONS/OWNER-DECISIONS.csv`: 1 cell, `open` → `OPEN`. Case only.
  `TAKEN-PENDING-REVIEW` was **not** removed; three live rows assert it, so
  the declared vocabulary in `09-DECISIONS/README.md` was corrected instead
  (CR-005).
- `02-SOURCES/access-ledger.csv`: `superseded_by` added and populated on 7
  rows from supersession sentences in `access_status`. `access_status`
  itself was **not** re-typed — see MH-002 below.

## Claim/source relation

`03-REGISTERS/claim-sources.csv`, generated: **4,569 join rows** over 1,272
distinct claim and data rows, of which **4,492 come from cells that held more
than one source identifier**. Claim identifiers and claim rows are unchanged;
no claim row was duplicated to carry a second source.

Two cell shapes beyond the semicolon list were found and handled as
arithmetic, not interpretation: a lone `-` meaning no source, and a range
(`SRC-053 to SRC-058`) expanded to its members. The same splitter is used by
the validator and by the generator, so they cannot disagree about what a cell
says.

`independence_group` is computed from `02-SOURCES/dependency.csv` by
union-find over the 9 dependency rows that collapse two observations into
one; the 11 rows whose `effect_on_status` opens with "No effect" are not
merged, because the same source probed twice is a fact about retrieval, not a
collapse of independence. **4 groups hold more than one source**:

- `IG-SRC-019`: SRC-019, SRC-023, SRC-026
- `IG-SRC-021`: SRC-021, SRC-022
- `IG-SRC-037`: SRC-037, SRC-049, SRC-051
- `IG-SRC-056`: SRC-056, SRC-061, SRC-065, SRC-068

This is the first time the registers state, mechanically, where two cited
sources are one independent observation — the thing `CLAUDE.md`'s
source-independence constraint turns on and that no flat cell could express.

### On the retained inline cell

The join is authoritative. The inline `source_id` cell is retained, and the
validator fails if the set of identifiers in a claim row's cell is not
exactly the set of join rows for that claim. It is one authority with a
mechanically enforced mirror, not two hand-maintained stores: the join is
generated from the cells, and a defect suite case proves the validator
catches them disagreeing.

The alternative — emptying the cell — was rejected. It would have edited 118
research rows to satisfy a schema, and `VERIFIED` rows are required to carry
a non-empty source reference.

## Migration holds

Seven rows in `00-CONTROLLER/MIGRATION-HOLDS.csv`. Each is a place where the
schema wanted something and the meaning of a row would have had to change to
give it. Each is surfaced by the validator on every run, so that "recorded"
does not become "buried".

| | Target | Why not migrated |
|---|---|---|
| MH-001 | `CROSS-DOMAIN-BRIDGES.csv` `verdict`, 8 rows | Eight different findings, not eight spellings of one. An enum would decide by clerical act whether a bridge was refused on principle or merely not established. |
| MH-002 | `access-ledger.csv` `access_status`, 55 rows | `VERIFIED` labels the standing of the probe record, not a retrieval. SRC-002 is `VERIFIED` with `retrieval_capable: NO` — a verified record of a failure. Re-typing would assert 50 retrievals that did not happen. |
| MH-003 | The two eligibility registers | 10 rows against 11, different namespaces, no crosswalk. Merging means choosing between two gate verdicts, which is analysis. |
| MH-004 | `BACKLOG-COVERAGE.csv`, 95 rows × 2 columns | The route inventory is in `melakeela/site`. Filling from the frozen 96-page audit was already considered and rejected in `06-BACKLOG/README.md`. |
| MH-005 | Reconciliation `C-1`–`C-9` | Renaming to `RCF-` is right but touches 14 files; a reference migration does not belong inside a schema migration. |
| MH-006 | All 115 paths | 1,024 enumerated references. Path moves are a separate mechanical commit after this passes review. |
| MH-007 | `museum-framework.md` 96-page counts | Relabelling means re-reading each argument against a site this session cannot see. |

## What was checked, and how

| Check | Result |
|---|---|
| Every pre-migration cell preserved | 510 rows compared column by column against `aa40d3a`; 1 intended mismatch |
| Migration is idempotent | Re-run on the migrated tree produces no diff |
| Generators reproduce their output | `inherited-claims-extraction.py` reproduces the migrated register byte-for-byte; CI re-runs all four generators and fails on any diff |
| CSV dialect preserved | Round-trip of all registers is byte-identical; the one exception was a stray LF line inside an otherwise-CRLF file |
| Validator catches defects | 15 injected defects, 15 caught (`test-validate-registers.py`) |
| Push gate cannot be bypassed | Denies on the removed marker, the echo-marker trick, `env git push`, `/usr/bin/git push`, `sh -c 'git push'`, an unparseable payload and a missing validator; allows only on an unexpired override row matching the exact failure |

## What was not touched

No file in `melakeela/site`. No production HTML, CSS or JavaScript. No
research finding rewritten, no claim promoted, no `REJECTED` row deleted, no
register row removed. Research is not frozen: the queue, the domain
registers and the holds are all live, and the only thing this pass asks of
future work is that it use the columns that now exist.
