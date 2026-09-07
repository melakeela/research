# Owner decisions

## Which file is authoritative

`OWNER-DECISIONS.csv` is authoritative for the `D-` identifier namespace and
for each decision's `status`. **Every owner decision has a row here**, whether
or not it blocks anything.

`DECISIONS-NEEDED.md`, at the repository root, holds the prose case for the
subset that blocks work in progress: the argument, the options table, the
evidence the decision turns on. It allocates no identifiers of its own and it
does not duplicate the register. Where the two disagree on wording or status,
the CSV governs.

The routing rule in `CLAUDE.md` is unchanged — a blocking escalation is still
written up in `DECISIONS-NEEDED.md`, a standing product or scope decision
still is not. What changed on 2026-09-07 is that both draw their identifiers
from one place.

## Allocating an identifier

Take the next free `D-` **from this CSV**, not from the highest number visible
in whatever document you are writing. That is how the D-004 to D-006 collision
happened: two branches on the same day each took "the next free number" from a
different file.

For a decision that blocks, write the CSV row first, then the
`DECISIONS-NEEDED.md` section, and point `detail_ref` at it.

## `OWNER-DECISIONS.csv`

```
decision_id,decision,constitution_ref,options,blocks,why_owner,status,
raised_date,owner_answer,answer_date,notes,detail_ref
```

- `constitution_ref` — where the decision comes from. A
  `METHODOLOGY-CONSTITUTION.md` section where there is one; otherwise the
  document or rule that raised it.
- `status` — `OPEN`, `BLOCKED` (cannot be answered until something else
  lands), `TAKEN-PENDING-REVIEW` (a branch proceeded on an answer the owner
  has not confirmed), `RESOLVED`, or `SUPERSEDED` (pointing at the row that
  replaced it). A resolved row is kept, never deleted: the reasoning it
  records is why the resolution holds.

  This list said three values until 2026-09-07 while the register carried
  four, `TAKEN-PENDING-REVIEW` among them on live rows. The register
  governs, so the list was corrected rather than the rows. `SUPERSEDED` is
  added for the duplicate-decision case below. The validator enforces this
  vocabulary; a sixth value cannot be introduced by writing it into a cell.
- `detail_ref` — the prose section, e.g. `DECISIONS-NEEDED.md D-014`. Empty
  means this row is the whole record.

## `DECISION-ID-MAP.csv`

```
old_id,old_file,new_id,changed,decision,note
```

One row per identifier as it stood before the 2026-09-07 merge, keyed by the
file it appeared in — because `D-004`, `D-005` and `D-006` each existed in
both files and a bare reference to one of them in an older document is
ambiguous without knowing which file was meant.

The map is in three blocks. The first, 34 rows, is the `D-0NN` namespace: 31
rows carry `changed = no` and 3 carry `changed = yes` for the sections that
became `D-032` to `D-034`.

The second block, 20 rows, is the **inherited handoff series**. That is a
separate defect, found on 2026-09-07 and fixed in the same pass. Section 4 of
`01-INHERITED/claude-project-handoff.md` numbers its own owner decisions
`D-01` to `D-20`, allocated in prior chat threads with no knowledge of this
repository. Two-digit `D-13` and three-digit `D-013` are different decisions —
the deck being a starting point rather than a source, against the dependency
store — and nothing in the text distinguished them.

Those twenty are now written **`HD-01` to `HD-20`** wherever this repository
speaks in its own voice: `03-REGISTERS/inherited-claims.csv` and
`04-AUDITS/inherited-claims-extraction.py`, which generates it, and
`00-CONTROLLER/CONTROLLER-RECONCILIATION.md`. They are *not* renumbered into
the `D-0NN` space and they get no `OWNER-DECISIONS.csv` row: they are prior
decisions of record, `INHERITED-UNVERIFIED` like everything else that came in
through `01-INHERITED/`, and giving them rows in the authoritative register
would promote them by clerical act — which the inheritance rule forbids. If
the owner re-affirms one, it is allocated a fresh `D-` from this CSV then.

The third block holds reassignments made **after** the 2026-09-07 merge, when
a branch that allocated an identifier correctly against the register it
branched from found that number taken by the time it merged. Ten rows so far,
all dated 2026-09-07. Two come from `main`: `D-035` to `D-037`, for the branch
that raised the `MELA-KEELA-WHO-MADE-THE-PAST.md` section-numbering
discrepancy while `D-035` and `D-036` were being taken on `main`; and `D-037`
to `D-036`, which is not a renumbering but a disambiguation — the
identifier-normalisation brief names `D-037` as a number it declined, and that
name now also belongs to a live row. Eight come from
`claude/domain-e-research-queue-z83m9b` (PR #10), which was cut before the
renumbering and then merged `main` twice: `D-015` to `D-043`, `D-016` to
`D-038`, `D-017` to `D-039`, `D-018` to `D-040`, `D-019` to `D-041`, and
`D-032` and `D-036` to `D-042`, with a further row carrying that branch's
`D-037` to `D-043` after `main` took `D-037` on the second merge. Rows in this
block chain: an identifier that moved twice keeps one row, whose `new_id` is
where it landed, and a second row is added under the number it was holding
when the collision happened, so that a reference written at either point
resolves.

This block will keep growing while branches run concurrently. Allocating from
the register at branch time is still correct; what the block records is that
the register moved underneath a branch, and which row a pre-merge reference
resolves to. The old identifier is never freed and never reused.

Two files keep the old `D-NN` spelling and are deliberately not edited:
`01-INHERITED/claude-project-handoff.md` and
`00-CONTROLLER/RESEARCH-CONSTITUTION.md`, which is a verbatim copy of the
handoff's §11. Inherited material is not rewritten; the map is what resolves
their references.

Rows are never removed. A `D-` reference in any file written before
2026-09-07 is resolved through this map — three-digit against the first
block, two-digit against the second. A three-digit reference in a file or a
pull request written on a branch that predates its merge is resolved against
the third.

`old_id` is deliberately **not** unique here: `D-004` appeared in two files
and an identifier that moved twice keeps a row under each number it held.
The row key is `old_id` + `old_file` + `new_id`, and the validator is told
so; a duplicate-identifier failure on this file would be a false positive.

## One decision, two identifiers

`D-036` and `D-039` ask the same question — whether the mandated registers
accumulate under their mandated names or are re-created per domain — and
carry different statuses, `OPEN` and `TAKEN-PENDING-REVIEW`. Neither row is
edited or deleted. The owner answers them together; whichever is chosen, the
other becomes `SUPERSEDED` pointing at it. Recorded as
`00-CONTROLLER/CONTRADICTION-REGISTER.csv` CR-010.

Both rows are non-blocking, so neither gets a `DECISIONS-NEEDED.md` section,
and **no third identifier is allocated for the duplication itself** — the
answer to two identifiers for one decision is not a third one.
