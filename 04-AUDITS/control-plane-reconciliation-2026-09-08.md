# Control-plane reconciliation — method note

**Written:** 2026-09-08
**Branch:** `claude/control-plane-reconciliation-vbrc08`, cut from `main` at
`1756b08`
**Unit type:** control plane. **No research finding is created, changed,
promoted or demoted by this unit.**
**Commissioned by:** the 2026-09-07 cross-repository audit of
`melakeela/research@aa40d3a` and `melakeela/site@e6b6b67`.

## 0. What standing this unit has

Every statement here is a statement about files, and each is re-derivable by
a command given in §6. Where a count appears it is a count of rows or matches
in a tree, not a finding about the past. Nothing in this unit carries an
evidence status, because it makes no claim that could carry one.

Two things follow, and both were binding constraints on the work:

1. **No register row's meaning was changed.** Where a value could not be
   migrated without changing what a row says, the row was left alone and a
   row was written to `04-AUDITS/MIGRATION-HOLDS.csv`. There are nine.
2. **Nothing was rewritten to make the validator pass.** Where the repaired
   validator found a real defect in another unit's rows, the finding is
   recorded and queued (`RA-019`), not fixed by guessing.

## 1. The one retrieval

`SRC-089`. `melakeela/site` cloned read-only at
`e6b6b67a62563f701922b67b7adf4ee1119ab094`; `SITE-INVENTORY.md` present,
sha256 `d9676f9e…`; 133 `.html` files at the repository root and 133 in the
whole tree, so no HTML sits below the root; `assets/data/page-evidence.json`
parses and its `pages` object holds 68 entries.

This is the retrieval that outcome 9 rests on. Before it, the claim that the
site inventory "now exists elsewhere" was the audit's assertion, and this
repository promotes nothing on an assertion. **Nothing in `melakeela/site`
was changed, and no site code was written anywhere.**

The 133/68 figures are measured here. The Artifact Atlas counts in `CR-021`
(175 in the title, 158 array rows, 153 unique names) are **not** re-measured
and are attributed to the audit in the row itself.

## 2. Before and after

Three runs, because "before" is ambiguous and the ambiguity is the point.

| Run | Result |
|---|---|
| **Old validator, tree at `main`** | `all checks pass` |
| **Old validator, this branch's tree** | `all checks pass` |
| **New validator, tree at `main`** | **143 failures** |

The first two are the finding. The old validator passed both trees not
because both were clean but because it asked five questions of one directory:
status vocabulary, three columns present on `VERIFIED` rows, `source_id`
resolution, in-file id uniqueness, and `D-NNN` resolution. `02-SOURCES/`,
`04-AUDITS/`, `06-BACKLOG/` and `09-DECISIONS/` were unchecked except as
lookup tables.

The third decomposes as:

| Failures | What |
|---|---|
| 88 | `access-ledger.csv` had no closed retrieval class column — one repair, every row |
| 33 | an identifier namespace in use and undeclared, because no registry existed |
| 15 | a closed-vocabulary violation in an existing register (`REAUDIT-QUEUE` ×14, `OWNER-DECISIONS` ×1) |
| 3 | a control-plane file absent |
| 2 | the claim/source join and the status register absent |
| 1 | `dependency.csv` prose cells that cannot resolve to a ledger id |
| 1 | other |

Most of that is "the file the check reads did not exist yet", which is what a
first run of a wider validator looks like. The 15 vocabulary violations and
the dependency failure are defects that were live on `main`.

**After, on this branch: `all checks pass`, with 24 reported notes.** The
notes are the things the validator can see and deliberately does not fail:
12 relative locators, 7 `HOLD` rows naming no hold file, 3 `HYPOTHESIS` rows
using the locator cell for a statement, `DEP-007`'s one-sided dependency, and
`MH-009`.

## 3. What the repaired validator now checks

Fifteen checks over every CSV in six directories, against five on one.
`01-INHERITED/` stays exempt: holding inherited material to this repository's
schema is the thing the inheritance rule forbids.

Two checks are softer than they look, and the reasons are the interesting
part:

- **Locator specificity** is enforced on `VERIFIED` and `PROVISIONAL` rows
  and reported on the rest. A locator qualifies by naming a number, section,
  identifier or hash, *or* by naming a file and the column, key, entry, row
  set or expression within it. `rv_tokens_vedaweb.tsv, book column` re-finds
  its measurement exactly; demanding a digit of it would be demanding the
  wrong thing, and the first draft of this check failed 25 rows on that
  mistake. A `HYPOTHESIS` row writing `not tested in this unit of work` is
  being honest, not vague.
- **A `HOLD` row naming no hold file** is reported, not failed. Seven rows
  are in that position. No register carries a column for the link, which is a
  schema gap and not a defect in the rows.

Three bugs of my own were found and fixed while building the checks, before
they could become findings about anyone else's work: the ledger's `source_id`
column is its own primary key and not a citation; the generated registers
re-use every prefix and must be exempt from the namespace rule; and
`DECISION-ID-MAP.csv` is keyed on `(old_id, old_file)`, so repeats are the
point of it.

## 4. The two adversarial tests

Constitution §8 requires both before a unit is called finished. A control
plane makes no claim about the past, so the tests apply to the control
plane's own asymmetries. Both found something.

### Prestige-bias challenge

*Did this privilege a claim because it is canonical, institutionally
prestigious, repeatedly cited or nationally useful?*

The prestigious document here is the **commissioning audit itself**. It is
long, confident, specific, and it was right about most of what it found — and
it is a model-written report whose own counts were never re-derived in this
repository. The first draft of `PATH-MIGRATION.csv` took its
old-path → new-path map as the destination rather than as a proposal.

Corrected: every `proposed_path` cell reads `PROPOSED-NOT-ADOPTED (D-046)`;
17 tracked paths carry `NO-PROPOSAL-RECORDED` because the audit's map does
not cover them, which is recorded as a gap in the map rather than filled in;
and the three figures this unit needed from the audit (133 routes, 68
page-evidence entries, `SITE-INVENTORY.md` present) were re-measured under
`SRC-089` rather than carried. The Atlas counts, which were *not*
re-measured, say so in `CR-021`.

A second instance: the audit recommends a specific folder structure
(`governance/ programme/ evidence/ assurance/ archive/`). It is a good
structure. Adopting it would still have been a structural decision taken by
an assistant on a model-written recommendation, so it is `D-046` and nothing
moved.

### Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is corrective?*

The attractive corrective story here is **"the gate was fake, and now it is
real."** It is half true and the second half is not.

Removing the text override is a real repair, and it was tested against seven
bypass shapes. But the hook still cannot see a push from another git client,
from the GitHub web UI or REST API, or from any session that is not this one.
CI can see those, and CI does not block anything until the check is required
in branch protection — a repository setting that only the owner can apply.
So `D-050` is recorded `BLOCKED`, the hook's own header says it is early
feedback and not the gate, and `CR-016` is `PARTLY-RESOLVED` rather than
`RESOLVED`.

A second instance, and the sharper one: the corrective story about the
registers is **"98 of 183 `VERIFIED` claims are single-sourced, so 98 rows
are overstated."** The measurement is real (`MH-008`). The inference is not
available to this unit. Several of those rows are counts over one retrieved
corpus and are legitimately verified *as counts over that corpus*; demoting
them mechanically would be rewriting research findings to satisfy a tool,
which is exactly the move the repository forbids. So the validator reports
the number and enforces nothing, and `D-051` asks the question.

Neither test produced a `BF-` row: no method failure occurred, because both
corrections were made inside this unit before anything was committed on the
wrong basis. Both are recorded here rather than in
`04-AUDITS/BIAS-FAILURE-LOG.csv`, which logs failures that reached a
deliverable.

## 5. What this unit did not do

- **It did not move anything.** All 147 tracked paths are `NOT-MOVED`.
- **It did not renumber anything.** `06-` is still allocated twice and `13-`
  still carries a number the reconciliation rejected; both are `CR-` rows.
- **It did not choose between `HYP-E-*` and `E-*`**, or between `D-036` and
  `D-039`. Choosing retires the other's rows.
- **It did not repopulate the 95 backlog coverage cells.** Mapping 133 routes
  onto 89 titles is an editorial taxonomy.
- **It did not demote, promote or delete a single claim row.**
- **It did not touch `01-INHERITED/`**, or edit any dated report to make it
  describe the present. `identifier-normalisation-brief.md` and the two
  validator notes are classed `HISTORICAL` in `CANONICAL-FILES.csv` instead.
- **It did not write site code, or change `melakeela/site` in any way.**

## 6. Re-deriving everything here

```
python3 04-AUDITS/claim-sources-build.py      # 7,698 join rows, 23 registers
python3 04-AUDITS/claim-status-build.py       # 714 claim rows, 14 registers
python3 04-AUDITS/path-migration-build.py     # 147 tracked paths
python3 04-AUDITS/backlog-coverage-build.py   # 95 backlog rows
git diff --quiet                              # all four are idempotent
python3 04-AUDITS/validate-registers.py --report
```

The old validator, for the two "before" runs:

```
git show origin/main:04-AUDITS/validate-registers.py > 04-AUDITS/_old.py
python3 04-AUDITS/_old.py && rm 04-AUDITS/_old.py
```

The hook, against every bypass shape, is exercised by feeding it a payload on
stdin with the validator deliberately failing; the seven shapes and four
override cases are listed in the commit that removed the bypass.
