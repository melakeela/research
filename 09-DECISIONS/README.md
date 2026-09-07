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
  lands), or `RESOLVED`. A resolved row is kept, never deleted: the reasoning
  it records is why the resolution holds.
- `detail_ref` — the prose section, e.g. `DECISIONS-NEEDED.md D-014`. Empty
  means this row is the whole record.

## `DECISION-ID-MAP.csv`

```
old_id,old_file,new_id,changed,decision,note
```

One row per identifier as it stood before the 2026-09-07 merge, keyed by the
file it appeared in — because `D-004`, `D-005` and `D-006` each existed in
both files and a bare reference to one of them in an older document is
ambiguous without knowing which file was meant. `changed` is `yes` for the
three that moved and `no` for the twenty-eight that did not.

Rows are never removed. A `D-` reference in any file written before
2026-09-07 is resolved through this map.
