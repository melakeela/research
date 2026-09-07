#!/usr/bin/env python3
"""
migrate-status-dimensions.py — split the overloaded `status` column.

One column named `status` was carrying five different things: what the
evidence supports, whether an interpretation has been accepted, whether a
draft has been reviewed, whether anything is published, and free prose
qualifying any of those. Filtering, gating and public rendering all need
them apart. This script separates them once, mechanically, and records
what it did.

The evidence gate stays single and unambiguous: `evidence_status` is the
seven-value CLAUDE.md vocabulary and nothing else, and it is the only
column the retrieval gate reads. The other dimensions cannot promote a
claim; a row that is APPROVED editorially and PROVISIONAL evidentially is
still PROVISIONAL.

Migration rules, in full:

  1. `status` is renamed `evidence_status` in place. The column keeps its
     position so the diff shows a rename, not a reordering.
  2. `interpretive_status`, `editorial_status` and `publication_status` are
     appended and set to UNASSIGNED on every existing row. Nothing is
     promoted: no row acquires a standing it did not already have, and
     UNASSIGNED asserts nothing.
  3. `status_reason` and `superseded_by` are appended. `status_reason`
     carries the qualification that used to be jammed into the status cell.
     `superseded_by` carries the replacement a SUPERSEDED row points at.
  4. A status cell that is not a bare vocabulary term is decomposed, never
     rewritten: the vocabulary term goes to `evidence_status`, the
     qualifying clause selects an `interpretive_status`, and the original
     cell is preserved verbatim in `status_reason`. Every such row is
     listed in the migration report for review.
  5. A cell that cannot be decomposed without a judgement call is left
     alone and recorded as a migration hold. This script never guesses.
  6. The eligibility registers gain `gate_verdict`, read from the leading
     term of `eligible_for_extended_analysis`. That column keeps its prose
     unchanged; the gate verdict is a parse of it, not a replacement.

Idempotent: running it on an already-migrated tree changes nothing.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import csvdialect  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

EVIDENCE_STATUS = {
    "VERIFIED", "PROVISIONAL", "HYPOTHESIS", "INHERITED-UNVERIFIED",
    "REJECTED", "SUPERSEDED", "HOLD",
}

# Registers whose `status` column is the claim evidence gate.
CLAIM_REGISTERS = [
    "03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv",
    "03-REGISTERS/domain-e-claims.csv",
    "03-REGISTERS/domain-e-hypothesis-eligibility.csv",
    "03-REGISTERS/domain-e-interpretations.csv",
    "03-REGISTERS/domain-e-measurements.csv",
    "03-REGISTERS/domain-m-brahui-position.csv",
    "03-REGISTERS/inherited-claims.csv",
    "03-REGISTERS/rigveda-pur-family.csv",
]

ELIGIBILITY_REGISTERS = [
    "03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv",
    "03-REGISTERS/domain-e-hypothesis-eligibility.csv",
]

NEW_DIMENSIONS = ("interpretive_status", "editorial_status", "publication_status")
NEW_QUALIFIERS = ("status_reason", "superseded_by")

# Longest-first: NOT-ELIGIBLE-SOURCE-BLOCKED must be tried before NOT-ELIGIBLE.
GATE_TERMS = [
    "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "NOT-ELIGIBLE-GATE-FAILED",
    "NOT-A-HYPOTHESIS",
    "NOT-ELIGIBLE",
    "CANNOT-GATE",
    "DEFERRED",
    "ELIGIBLE",
]

# The two eligibility registers were written in different vocabularies for the
# same column. 03-REGISTERS/domain-e-hypothesis-eligibility.csv opens the cell
# with a gate term; 03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv answers the column
# heading ("eligible for extended analysis?") with YES or NO. That the two
# disagree on vocabulary is itself a defect and is recorded in the
# contradiction register; here they are read into one gate_verdict.
#
# Each entry maps a prose opening to the gate term asserting the SAME
# proposition — YES means eligible, NO for lack of sources means the gate was
# not reached because the sources are blocked. Nothing is reclassified: the
# prose column keeps every word, and the mapping is longest-prefix so that
# "NO - FOR LACK OF SOURCES" cannot be swallowed by bare "NO".
GATE_SYNONYMS = [
    ("NO - FOR LACK OF SOURCES, NOT FOR LACK OF MERIT", "NOT-ELIGIBLE-SOURCE-BLOCKED"),
    ("NO - FOR LACK OF SOURCES", "NOT-ELIGIBLE-SOURCE-BLOCKED"),
    ("NO, PENDING SOURCES", "NOT-ELIGIBLE-SOURCE-BLOCKED"),
    ("YES, WHEN THE BRAHUI LITERATURE IS RETRIEVABLE", "NOT-ELIGIBLE-SOURCE-BLOCKED"),
    ("YES", "ELIGIBLE"),
    ("NO", "NOT-ELIGIBLE"),
]

SUPERSEDED_BY = re.compile(r"SUPERSEDED\s+BY\s+([A-Z]+-[0-9A-Za-z-]+)", re.I)

report = {"renamed": [], "decomposed": [], "superseded": [], "gate": [], "holds": []}


def decompose(cell):
    """Split a non-vocabulary status cell. Returns (evidence, interpretive) or None.

    Only the one shape actually present in the tree is handled: a vocabulary
    term followed by a qualifying clause. Anything else returns None and
    becomes a migration hold rather than a guess.
    """
    head = re.split(r"[;,]", cell, 1)[0].strip()
    term = head.split()[0].strip() if head.split() else ""
    if term not in EVIDENCE_STATUS:
        return None
    rest = cell[len(term):].strip(" ;,")
    # "as a measurement" is the only qualifier in the tree; it says the row is
    # a measurement and not an interpretation, which is what MEASUREMENT-ONLY
    # means. Anything else is left UNASSIGNED rather than invented.
    interpretive = "MEASUREMENT-ONLY" if re.search(r"\bas a measurement\b", rest, re.I) else "UNASSIGNED"
    return term, interpretive


def migrate_claim_register(rel):
    path = ROOT / rel
    fields, rows = csvdialect.read(path)
    if "evidence_status" in fields:
        return False                      # already migrated
    if "status" not in fields:
        return False
    out_fields = ["evidence_status" if f == "status" else f for f in fields]
    for extra in NEW_DIMENSIONS + NEW_QUALIFIERS:
        if extra not in out_fields:
            out_fields.append(extra)
    report["renamed"].append(rel)

    for n, row in enumerate(rows, start=2):
        cell = (row.get("status") or "").strip()
        interpretive = "UNASSIGNED"
        reason = ""
        if cell and cell not in EVIDENCE_STATUS:
            split = decompose(cell)
            if split is None:
                report["holds"].append(
                    f"{rel}:{n}: status cell {cell!r} could not be decomposed "
                    f"without a judgement call; left unchanged"
                )
            else:
                cell, interpretive = split
                reason = (row.get("status") or "").strip()   # original, verbatim
                report["decomposed"].append(
                    f"{rel}:{n}: {reason!r} -> evidence_status={cell}, "
                    f"interpretive_status={interpretive}, status_reason preserved verbatim"
                )
        row["evidence_status"] = cell
        row["interpretive_status"] = interpretive
        row["editorial_status"] = "UNASSIGNED"
        row["publication_status"] = "UNASSIGNED"
        row["status_reason"] = reason
        if cell == "SUPERSEDED":
            hay = " ".join((row.get(c) or "") for c in ("notes", "reason", "claim"))
            m = SUPERSEDED_BY.search(hay)
            if m:
                row["superseded_by"] = m.group(1)
                report["superseded"].append(f"{rel}:{n}: superseded_by={m.group(1)} (read from notes)")
            else:
                row["superseded_by"] = ""
                report["holds"].append(
                    f"{rel}:{n}: SUPERSEDED row names no replacement in its own text; "
                    f"superseded_by left empty"
                )
        else:
            row.setdefault("superseded_by", "")
            row["superseded_by"] = row.get("superseded_by") or ""
    csvdialect.write(path, out_fields, rows)
    return True


def migrate_gate_verdict(rel):
    path = ROOT / rel
    fields, rows = csvdialect.read(path)
    if "gate_verdict" in fields or "eligible_for_extended_analysis" not in fields:
        return False
    out_fields = list(fields)
    out_fields.insert(
        out_fields.index("eligible_for_extended_analysis"), "gate_verdict"
    )
    for n, row in enumerate(rows, start=2):
        cell = (row.get("eligible_for_extended_analysis") or "").strip()
        verdict = "UNASSIGNED"
        upper = cell.upper()
        for term in GATE_TERMS:
            if upper.startswith(term):
                verdict = term
                break
        else:
            for prose, term in GATE_SYNONYMS:   # longest-prefix, see GATE_SYNONYMS
                if upper.startswith(prose):
                    verdict = term
                    break
        if verdict == "UNASSIGNED" and cell:
            report["holds"].append(
                f"{rel}:{n}: eligibility cell {cell[:60]!r} opens with no "
                f"recognised gate term; gate_verdict left UNASSIGNED"
            )
        else:
            report["gate"].append(f"{rel}:{n}: gate_verdict={verdict}")
        row["gate_verdict"] = verdict
    csvdialect.write(path, out_fields, rows)
    return True


def migrate_access_ledger():
    """Add a machine-readable supersession pointer to the access ledger.

    `access_status` itself is NOT re-typed. Its VERIFIED and PROVISIONAL
    values label the standing of the probe record, not a retrieval outcome
    (SRC-002 is `VERIFIED` and `retrieval_capable: NO`), so mapping them
    onto a retrieval vocabulary would change what 55 rows assert. That
    re-typing is left to the owner; see the contradiction register.
    """
    rel = "02-SOURCES/access-ledger.csv"
    path = ROOT / rel
    fields, rows = csvdialect.read(path)
    if "superseded_by" in fields:
        return False
    out_fields = list(fields) + ["superseded_by"]
    for n, row in enumerate(rows, start=2):
        cell = (row.get("access_status") or "").strip()
        target = ""
        if cell.upper().startswith("SUPERSEDED"):
            m = re.search(r"\b(SRC-\d+)\b", cell)
            if m:
                target = m.group(1)
                report["superseded"].append(f"{rel}:{n}: superseded_by={target} (read from access_status)")
            else:
                report["holds"].append(
                    f"{rel}:{n}: access_status {cell[:60]!r} declares supersession "
                    f"but names no replacement source"
                )
        row["superseded_by"] = target
    csvdialect.write(path, out_fields, rows)
    return True


def main():
    for rel in CLAIM_REGISTERS:
        migrate_claim_register(rel)
    for rel in ELIGIBILITY_REGISTERS:
        migrate_gate_verdict(rel)
    migrate_access_ledger()

    print("migrate-status-dimensions")
    for key in ("renamed", "decomposed", "superseded", "holds"):
        print(f"\n{key} ({len(report[key])}):")
        for line in report[key]:
            print("  " + line)
    print(f"\ngate_verdict rows written: {len(report['gate'])}")


if __name__ == "__main__":
    main()
