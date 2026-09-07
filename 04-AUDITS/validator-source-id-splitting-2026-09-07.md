# Validator fix: compound `source_id` cells were never actually checked

**Written:** 2026-09-07
**Subject:** `04-AUDITS/validate-registers.py` check 3, and one status cell in
`03-REGISTERS/domain-e-hypothesis-eligibility.csv`.
**Found by:** the push gate blocking this branch's first commit with 53
failures, none of which this branch caused.

## What was wrong

`validate-registers.py` check 3 read the whole `source_id` cell as one string
and asked whether that string was in the access ledger:

```python
sid = (row.get("source_id") or "").strip()
if sid and ledger and sid not in ledger:
    fail(...)
```

Every register in this repository cites several sources per claim, joined with
`; ` — `"SRC-019; SRC-022; SRC-023"` — because the source-independence rule
requires a claim to name every source behind it. A ledger id is `SRC-0NN`, so a
compound cell could never match, **whatever it contained**.

The effect was not a strict check. It was **no check at all** on exactly the
rows the rule exists for: 52 of the 53 failures were well-formed rows citing
sources that are all present in the ledger, and a genuinely bad id hidden in a
compound cell would have been indistinguishable from them. Single-source cells
were checked correctly, so the bug was invisible in any register that cited one
source per claim.

## The fix

Split the cell on `;` and resolve each component:

```python
for one in (p.strip() for p in sid.split(";")):
    if one and one not in ledger:
        fail(f"{rel}:{n}: source_id {one} not in access ledger")
```

**This makes the validator stricter, not weaker.** Before, `"SRC-019; SRC-999"`
and `"SRC-019; SRC-022"` both failed with an undifferentiated message; a reader
clearing the noise would have cleared the real error with it. After, the first
fails naming `SRC-999` and the second passes. `CLAUDE.md` forbids weakening the
validator to get past it; this is the opposite operation, and it is recorded
here rather than folded silently into a research commit.

Verified against the tree at the time of the fix: with splitting on, every
`source_id` component in every register resolves to a ledger row.

## The one failure that was not the bug

`03-REGISTERS/domain-e-hypothesis-eligibility.csv`, row `E-11`, carried

    status = "VERIFIED as a measurement; not a claim about origins"

`CLAUDE.md` — "Every claim carries exactly one status." A status cell is a term
from the vocabulary; a qualifier on it is prose and belongs in prose. The status
is now `VERIFIED` and the qualifier opens the row's existing `reason` cell,
which already argued the same point at length. **Nothing about the row's
standing changed** — it was and remains a verified measurement that is not a
claim about origins, and the `reason` cell still says so in the row's own words.

This is another unit's register, touched here only because the push gate is
repository-wide and this row blocks every branch, not because this branch has a
view on domain E.

## Why this was not visible earlier

The gate is a `PreToolUse` hook on `Bash`, so it fires **before** the command
runs — a blocked push means the commit in the same command never happened
either. A session that pushes only at the end of its work meets all of this at
once, at the point where it is most tempting to set the override variable and
move on. `CLAUDE.md`'s instruction to commit and push after every unit of work
is what surfaced it here at the first unit instead of the last.
