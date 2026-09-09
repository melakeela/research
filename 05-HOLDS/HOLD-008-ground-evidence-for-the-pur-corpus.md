# HOLD-008 — any archaeological source at all, for the *púr-* corpus

**Raised:** 2026-09-09
**Blocks:** the ground half of `06-BRIEFS/childrens-pilot/` (screen `CP-3.5`,
and the second of the three sentences at `CP-4.1`). Release decision `D-056`.
**Does not block:** anything else in the *púr-* registers, none of which claims
anything about the ground.
**Ledger:** *no row exists.* That is the hold.

## What is needed

At least one retrieved, ledger-logged archaeological source bearing on
fortification in the region and period the *púr-* passages are usually placed
in. Any one of: an excavation report with a stratigraphic sequence; a site
chronology with dated contexts; a radiocarbon series with laboratory numbers
and calibration stated; a survey coverage report.

## Why the absence is a HOLD and not a typed absence

`CLAUDE.md`'s negative-evidence standard governs arguing **from** absence about
the past. Nothing here argues from absence about the past.

None of the eight types applies, and the reason is the same for all eight:
**every one of them is a finding about the record, and no search of the record
was run.**

- not `ABSENT DESPITE ADEQUATE SEARCH` — no search was run at all, so the
  adequacy condition is not merely unmet, it is unassessed;
- not `NOT ACCESSIBLE` — nothing was requested and nothing was refused; there is
  no `EGRESS_BLOCKED` row and no refusal on file;
- not `NOT EXCAVATED`, `NOT PUBLISHED`, `NOT PRODUCED`, `NOT PRESERVED`,
  `NOT RECOGNIZED` or `DOCUMENTED DESTRUCTION` — each of these asserts something
  about what exists or once existed in the world, and this repository holds no
  evidence bearing on any of them either way.

**An earlier draft of this hold argued the point differently and worse**, by
asserting that *"people have excavated, extensively"* and *"reports exist"*.
Those may well be true, and this repository holds no source for either, so
using them as premises would have made the typing decision rest on exactly the
kind of unevidenced background assumption the standard exists to catch. The
argument above needs no such premise: an untyped gap is untyped because nobody
looked, and that is a fact about us.

What is true is narrower and entirely about us:
**`02-SOURCES/access-ledger.csv` contains 98 data rows — `SRC-001` to
`SRC-098`, derived with `csv.DictReader` and not from the file's 99 lines — and
not one of them is archaeological.** Every source behind every *púr-* register
row is a text, a translation, a dictionary, a metrical study, or a lexical
database.

That statement is checkable, and screen `CP-3.5` is built so that a child
checks it against the real ledger rather than being told it.

## What must not be inferred from this hold

- **Not** that no archaeology bears on the question. It may bear on it heavily;
  nobody here has looked.
- **Not** that the *púr-* passages describe nothing that stood anywhere.
  `PUR4J-I-03`'s own `what_it_does_not_establish` field is explicit: 48 of 103
  passages present a fort as an object in the narrative, and the unit that
  produced them *"has no evidence bearing on whether any of them stood
  anywhere."*
- **Not** that filling this hold would produce a match. Version 12 line 1175
  holds the identification of the forts with one archaeological culture, and
  constitution §4J forbids the automatic step from *pur* to a Mature Harappan
  city. A retrieved excavation report would be evidence about the ground; the
  bridge from it to any passage is a separate claim under §4.4 and would need
  its own mechanism, its own rivals and its own status.

## What discharging it would take

Named as `U-1` in `06-BRIEFS/childrens-pilot/VERIFYING-UNITS.csv`. In outline:

1. Bound the question first (constitution §5 step 1). "Archaeology of the
   Rigvedic forts" is not a bounded question and cannot be retrieved against.
   Chronology and geography gates run **before** any site is named, and the
   gate may return `NOT-ELIGIBLE`: the corpus states no place (`PUR4J-018`) and
   the museum holds no absolute date for it (`DE-M-027`), so a request for
   "the right sites" has, today, no criterion.
2. That is the real shape of `U-1`, and it is why the hold is written rather
   than a retrieval simply being scheduled. **The chronology and geography
   problems are upstream of the archaeology, not downstream of it.** `U-2` and
   `U-3` are prior work, not parallel work.
3. Retrieval, logged, with `EGRESS_BLOCKED` rows where the proxy refuses and
   the domains collected for the pull request, per `CLAUDE.md`.

## Falsifier for this hold's own framing

If a search of the ledger's history shows an archaeological source was
retrieved in an earlier session and dropped, this is not a hold but a
`SUPERSEDED` row and a recovery task. A full-tree search of the tracked files
for excavation-source rows was run for
`06-BRIEFS/childrens-pilot/INVESTIGATION-SPEC.md` and found none; that search
covered the working tree at `main`, not the full history.
