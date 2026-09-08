#!/usr/bin/env python3
"""
claim-status-build.py — generate 03-REGISTERS/CLAIM-STATUS.csv.

The problem this fixes
----------------------
One column named `status` was carrying at least four different questions:

  * has a retrieval happened that backs this row      (evidence)
  * did this hypothesis pass the chronology/geography
    gate, and may it have analytical space            (interpretation)
  * has anyone tried to break this row                (editorial)
  * is this row's content public                      (publication)

Where two of those were needed at once the cell grew prose — `"VERIFIED as a
measurement; not a claim about origins"`, `"OPEN - blocked on HOLD-005"` — and
a closed vocabulary stopped being closed. A cell that carries prose cannot be
filtered, cannot gate, and cannot be rendered.

The repair is one column per question, in a register that is generated rather
than authored, so the migration is reproducible and reversible.

**The evidence gate stays single and unambiguous.** `evidence_status` is
copied from the register's own `status` cell, unchanged, with no promotion of
any kind: a row that was `PROVISIONAL` is `PROVISIONAL` here. It is the only
dimension that gates anything. The other three are addressable and gate
nothing on their own.

Nothing is invented. Where a dimension is not recorded anywhere in the tree it
reads `NOT-RECORDED`, which is a finding and not a default — the fact that no
register records per-claim editorial state is exactly the sort of thing that
should be visible rather than filled in.

Where a value cannot be migrated without changing what the row means, the row
is left alone, `migration_state` reads `HELD`, and a row is written to
`04-AUDITS/MIGRATION-HOLDS.csv`.

Regenerate from the repository root:

    python3 04-AUDITS/claim-status-build.py

Do not hand-edit 03-REGISTERS/CLAIM-STATUS.csv; the next run overwrites it.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "03-REGISTERS" / "CLAIM-STATUS.csv"

SCAN_DIRS = ("03-REGISTERS",)
GENERATED = {"03-REGISTERS/CLAIM-SOURCES.csv", "03-REGISTERS/CLAIM-STATUS.csv"}

# ---------------------------------------------------------------- vocabularies

# The evidence gate. CLAUDE.md's seven, plus NOT-ESTABLISHED for a row whose
# register records no evidence status at all.
EVIDENCE_STATUS = {
    "VERIFIED", "PROVISIONAL", "HYPOTHESIS", "INHERITED-UNVERIFIED",
    "REJECTED", "SUPERSEDED", "HOLD", "NOT-ESTABLISHED",
}

# The gate verdict of constitution step 7. Never an evidence status: a
# hypothesis can be ELIGIBLE and rest on nothing retrieved.
INTERPRETIVE_STATUS = {
    "ELIGIBLE", "NOT-ELIGIBLE", "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "NOT-ELIGIBLE-GATE-FAILED", "CANNOT-GATE", "NOT-A-HYPOTHESIS",
    "DEFERRED", "NOT-RECORDED",
}

# Whether anyone has tried to break the row. No register currently records
# this per claim, so every row reads NOT-RECORDED and that is the finding.
EDITORIAL_STATUS = {
    "DRAFT", "IN-REVIEW", "CHANGES-REQUIRED", "REVIEWED-ACCEPTED",
    "RETIRED", "NOT-RECORDED",
}

# Whether the row's content is public. Read only from an explicit marker in
# supports_page; never inferred from the existence of a page.
PUBLICATION_STATUS = {
    "PROPOSED", "PUBLISHED", "WITHDRAWN", "NOT-RECORDED",
}

# Prefixes that a gate cell may open with, longest first, so that
# "NOT-ELIGIBLE-SOURCE-BLOCKED" is not truncated to "NOT-ELIGIBLE".
GATE_PREFIXES = sorted(
    (v for v in INTERPRETIVE_STATUS if v != "NOT-RECORDED"),
    key=len, reverse=True,
)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _match(cell, token):
    """True if `cell` opens with `token` at a token boundary."""
    if not cell.startswith(token):
        return False
    rest = cell[len(token):]
    return rest == "" or not (rest[0].isalnum() or rest[0] == "-")


def parse_gate(cell):
    """Split a gate cell into (verdict, qualifier).

    The eligibility registers write a closed verdict followed by a qualifier:
    'NOT-A-HYPOTHESIS in the sense this register gates - a reconstruction'.
    The verdict is taken only at a token boundary, so NOT-ELIGIBLE never
    swallows NOT-ELIGIBLE-SOURCE-BLOCKED. **The qualifier is everything after
    the verdict, verbatim** apart from leading whitespace and a leading dash or
    comma: no word of it is consumed as a separator, because dropping the
    leading 'in' or 'for' of a qualifier changes what the row says.

    A cell that does not open with a known verdict is not guessed at: it
    returns (None, cell) and the caller holds the row unchanged.
    """
    cell = (cell or "").strip()
    if not cell:
        return "NOT-RECORDED", ""
    for verdict in GATE_PREFIXES:
        if _match(cell, verdict):
            return verdict, cell[len(verdict):].lstrip(" \u2014-,;:").strip()
    for word, verdict in (("YES", "ELIGIBLE"), ("NO", "NOT-ELIGIBLE")):
        if _match(cell, word):
            return verdict, cell[len(word):].lstrip(" \u2014-,;:").strip()
    return None, cell


def main():
    out_rows = []
    holds = []
    n_held = 0
    for d in SCAN_DIRS:
        for path in sorted((ROOT / d).rglob("*.csv")):
            rel = str(path.relative_to(ROOT))
            if rel in GENERATED:
                continue
            rows = read_csv(path)
            if not rows:
                continue
            fields = list(rows[0])
            if "status" not in fields:
                continue
            id_field = next(
                (c for c in fields if c and (c.endswith("_id") or c == "id")),
                None)
            gate_field = ("eligible_for_extended_analysis"
                          if "eligible_for_extended_analysis" in fields else None)
            for line, row in enumerate(rows, start=2):
                claim_id = (row.get(id_field) or "").strip() if id_field else ""
                raw = (row.get("status") or "").strip()
                reasons = []
                migration_state = "MIGRATED"
                hold_ref = ""

                # ---- evidence_status: copied, never promoted -------------
                if raw in EVIDENCE_STATUS:
                    evidence = raw
                elif not raw:
                    evidence = "NOT-ESTABLISHED"
                    reasons.append("register records no status for this row")
                else:
                    evidence = "NOT-ESTABLISHED"
                    migration_state = "HELD"
                    hold_ref = f"MH-STATUS-{rel}#{claim_id}"
                    reasons.append(
                        f"status cell {raw!r} is not a closed evidence value "
                        "and was not reinterpreted")
                    holds.append((rel, line, claim_id, raw,
                                  "status cell is outside the evidence "
                                  "vocabulary"))
                    n_held += 1

                # ---- interpretive_status ---------------------------------
                interpretive = "NOT-RECORDED"
                if gate_field:
                    verdict, qualifier = parse_gate(row.get(gate_field))
                    if verdict is None:
                        migration_state = "HELD"
                        hold_ref = hold_ref or f"MH-GATE-{rel}#{claim_id}"
                        reasons.append(
                            f"gate cell {qualifier!r} does not open with a "
                            "known verdict and was not reinterpreted")
                        holds.append((rel, line, claim_id, qualifier,
                                      "gate cell does not open with a known "
                                      "verdict"))
                        n_held += 1
                    else:
                        interpretive = verdict
                        if qualifier:
                            reasons.append(f"gate qualifier: {qualifier}")

                # ---- editorial_status ------------------------------------
                # No register records per-claim review state. That absence is
                # the finding; it is not filled in from a method note, because
                # a method note reviews a unit and not a row.
                editorial = "NOT-RECORDED"

                # ---- publication_status ----------------------------------
                supports = (row.get("supports_page") or "").strip()
                if "(proposed)" in supports.lower():
                    publication = "PROPOSED"
                else:
                    publication = "NOT-RECORDED"
                    if supports:
                        reasons.append(
                            f"supports_page names {supports!r} without a "
                            "publication marker; publication state is not "
                            "inferred from a page existing")

                # ---- superseded_by ---------------------------------------
                superseded_by = ""
                if evidence == "SUPERSEDED":
                    notes = " ".join(
                        (row.get(c) or "") for c in ("notes", "supports_page")
                        if c in fields)
                    superseded_by = notes.strip()
                    if not superseded_by:
                        reasons.append(
                            "SUPERSEDED with no replacement named in the row")

                out_rows.append({
                    "claim_id": claim_id,
                    "register": rel,
                    "register_line": line,
                    "evidence_status": evidence,
                    "interpretive_status": interpretive,
                    "editorial_status": editorial,
                    "publication_status": publication,
                    "status_reason": " | ".join(reasons),
                    "superseded_by": superseded_by,
                    "migrated_from_status_cell": raw,
                    "migration_state": migration_state,
                    "migration_hold": hold_ref,
                })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0]), quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(out_rows)

    registers = len({r["register"] for r in out_rows})
    print(f"claim-status-build: {len(out_rows)} claim rows from {registers} "
          f"registers -> {OUT.relative_to(ROOT)}")
    from collections import Counter
    for col in ("evidence_status", "interpretive_status", "editorial_status",
                "publication_status"):
        c = Counter(r[col] for r in out_rows)
        print(f"  {col}: " + ", ".join(f"{k}={v}" for k, v in c.most_common()))
    if holds:
        print(f"  rows held, left unchanged: {n_held}")
        for rel, line, cid, cell, why in holds:
            print(f"    {rel}:{line} {cid}: {why} ({cell[:60]!r})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
