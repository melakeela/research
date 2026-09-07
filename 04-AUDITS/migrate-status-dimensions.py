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

# The exact prose-to-verdict mapping applied on 2026-09-07, written out rather
# than recomputed, so that re-running the migration from aa40d3a reproduces the
# committed column without re-introducing an inference rule.
HISTORICAL_PARSE = {
    "YES": "ELIGIBLE",
    "NO": "NOT-ELIGIBLE",
    "NO - FOR LACK OF SOURCES, NOT FOR LACK OF MERIT": "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "NO - FOR LACK OF SOURCES": "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "NO, pending sources": "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "YES, when the Brahui literature is retrievable": "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "DEFERRED - domain K and packet R20": "DEFERRED",
}

ROOT = Path(__file__).resolve().parents[1]

NEEDS_A_SOURCE = ("VERIFIED", "PROVISIONAL")

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


SUPERSEDED_BY = re.compile(r"SUPERSEDED\s+BY\s+([A-Z]+-[0-9A-Za-z-]+)", re.I)

report = {"renamed": [], "decomposed": [], "superseded": [], "gate": [], "holds": []}


REGISTER_CAN_CARRY_RETRIEVAL = True   # set per register by migrate_claim_register


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
    # A decomposition is only safe where the leading term is a standing the
    # register can actually carry. It is NOT safe merely because a vocabulary
    # word appears first: E-11 opened with VERIFIED in a register that has no
    # source_id, locator or retrieval_date column, so decomposing it produced a
    # VERIFIED row whose retrieval no check could ever reach. That is a
    # promotion in machine standing, and it is refused here. The caller records
    # a migration hold instead.
    # Same predicate the validator gates on. Guarding only VERIFIED meant the
    # script would recreate exactly the PROVISIONAL rows the validator now
    # fails, and the self-test asserted that as correct.
    if term in NEEDS_A_SOURCE and not REGISTER_CAN_CARRY_RETRIEVAL:
        return None
    interpretive = "UNASSIGNED"
    return term, interpretive


def migrate_claim_register(rel):
    path = ROOT / rel
    fields, rows = csvdialect.read(path)
    if "evidence_status" in fields:
        return False                      # already migrated
    if "status" not in fields:
        return False
    global REGISTER_CAN_CARRY_RETRIEVAL
    REGISTER_CAN_CARRY_RETRIEVAL = all(
        c in fields for c in ("source_id", "locator", "retrieval_date"))
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
        # The one-time parse that populated this column on 2026-09-07. It is
        # NOT re-derived: gate_verdict is authored now, because inferring it
        # from prose moved hypotheses across the gate by rewording. This branch
        # is dead on a migrated tree and is kept so the migration is
        # reproducible from aa40d3a.
        verdict = HISTORICAL_PARSE.get(cell.strip(), "UNASSIGNED")
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


SPLIT_QUALIFIER = re.compile(r"\s*[—–-]\s+")   # em dash, en dash, or ' - '


def decompose_token(cell):
    """Split 'OPEN - blocked on X' into ('OPEN', 'blocked on X').

    The declared token is preserved exactly as written, only upper-cased.
    A row that said OPEN still says OPEN: the qualifier moves to its own
    column instead of being promoted into a different status.
    """
    cell = (cell or "").strip()
    if not cell:
        return "", ""
    parts = SPLIT_QUALIFIER.split(cell, 1)
    token = parts[0].strip().upper()
    rest = parts[1].strip() if len(parts) > 1 else ""
    return token, rest


def migrate_reaudit_queue():
    """Decompose REAUDIT-QUEUE.csv status and priority.

    Both columns held a mixture of cases and composite values: OPEN, open,
    'OPEN - blocked on HOLD-005', MEDIUM, medium, and 'HIGH — it affects how
    every future unit plans its retrievals.' No mechanical filter over the
    re-audit queue was possible. Case is normalised, the qualifier is moved
    to blocked_by or priority_reason, and the declared token is unchanged.
    """
    rel = "04-AUDITS/REAUDIT-QUEUE.csv"
    path = ROOT / rel
    fields, rows = csvdialect.read(path)
    if "blocked_by" in fields:
        return False
    out_fields = list(fields) + ["blocked_by", "priority_reason", "status_reason"]
    for n, row in enumerate(rows, start=2):
        original_status = (row.get("status") or "").strip()
        token, rest = decompose_token(original_status)
        row["status"] = token
        # 'blocked on X' is a dependency; anything else is a qualification.
        m = re.match(r"blocked on\s+(.*)$", rest, re.I)
        row["blocked_by"] = m.group(1).strip() if m else ""
        row["status_reason"] = original_status if rest else ""
        if original_status != token:
            report["decomposed"].append(
                f"{rel}:{n}: status {original_status!r} -> {token}"
                + (f", blocked_by={row['blocked_by']!r}" if row["blocked_by"] else "")
                + (", original preserved in status_reason" if rest else " (case only)"))

        original_priority = (row.get("priority") or "").strip()
        ptoken, prest = decompose_token(original_priority)
        row["priority"] = ptoken
        row["priority_reason"] = prest
        if original_priority != ptoken:
            report["decomposed"].append(
                f"{rel}:{n}: priority {original_priority[:40]!r} -> {ptoken}"
                + (", qualification moved to priority_reason" if prest else " (case only)"))
    csvdialect.write(path, out_fields, rows)
    return True


def migrate_owner_decisions():
    """Normalise the one lower-case decision status. Case only; no re-typing."""
    rel = "09-DECISIONS/OWNER-DECISIONS.csv"
    path = ROOT / rel
    fields, rows = csvdialect.read(path)
    changed = False
    for n, row in enumerate(rows, start=2):
        v = (row.get("status") or "").strip()
        if v and v != v.upper():
            row["status"] = v.upper()
            changed = True
            report["decomposed"].append(f"{rel}:{n}: status {v!r} -> {v.upper()} (case only)")
    if changed:
        csvdialect.write(path, fields, rows)
    return changed


def selftest():
    """Exercise the decomposition rules directly.

    No row in the tree now reaches the refusal branch — E-11 is restored and
    held — so without this the guard that stops a VERIFIED promotion is code
    that nothing runs. Adversarial review made that point about the first
    version of this repair and it is a fair one.
    """
    global REGISTER_CAN_CARRY_RETRIEVAL
    cases = [
        (True, "VERIFIED as a measurement; not a claim about origins", ("VERIFIED", "UNASSIGNED")),
        (False, "VERIFIED as a measurement; not a claim about origins", None),
        (False, "PROVISIONAL, on one source", None),
        (True, "PROVISIONAL, on one source", ("PROVISIONAL", "UNASSIGNED")),
        (True, "not a status at all", None),
    ]
    for can_carry, cell, expected in cases:
        REGISTER_CAN_CARRY_RETRIEVAL = can_carry
        got = decompose(cell)
        assert got == expected, (can_carry, cell, got, expected)
    REGISTER_CAN_CARRY_RETRIEVAL = True
    print("selftest: decomposition rules hold "
          f"({len(cases)} cases, including the refusal of a VERIFIED opening "
          "in a register that cannot record a retrieval)")


def main():
    selftest()
    migrate_reaudit_queue()
    migrate_owner_decisions()
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
