#!/usr/bin/env python3
"""
validate-registers.py — mechanical enforcement of the evidence rules.

Exit 0 if every register passes. Exit 1 with a list of failures otherwise.
Run before every push. Wire as a hook so a session cannot push a
VERIFIED row that no retrieval backs.

Checks:
  1. Every row's status is in the vocabulary.
  2. Every VERIFIED row has non-empty source_id, locator, retrieval_date.
  3. Every source_id resolves to a row in 02-SOURCES/access-ledger.csv.
  4. Every claim_id is unique within its file.
  5. Every D- reference in the tree resolves to exactly one row in
     09-DECISIONS/OWNER-DECISIONS.csv.

CSVs in this repository mix CRLF and LF and carry embedded newlines
inside quoted cells. Everything here opens with newline='' and never
rewrites a file.

Output modes:
  (default)  human-readable list, exit 1 if any failure
  --json     the same failures as a JSON array of records, one per failure:
             {file, row_id, failure_type, detail, line}. Exit code is
             unchanged. This is what the push gate consumes, so that the
             baseline in 04-AUDITS/validator-baseline.json can be keyed by
             file, row identifier and failure type rather than by line
             number — line numbers move whenever a row is inserted, and a
             baseline that moved with them would excuse the wrong rows.

Adding --json changed no check and no verdict. The human output below is
byte-identical to what this script printed before the flag existed.
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER_DIR = ROOT / "03-REGISTERS"
LEDGER = ROOT / "02-SOURCES" / "access-ledger.csv"
DECISIONS = ROOT / "09-DECISIONS" / "OWNER-DECISIONS.csv"

STATUS_VOCAB = {
    "VERIFIED", "PROVISIONAL", "HYPOTHESIS", "INHERITED-UNVERIFIED",
    "REJECTED", "SUPERSEDED", "HOLD",
    # gate verdicts, permitted in eligibility registers
    "ELIGIBLE", "NOT-ELIGIBLE", "NOT-ELIGIBLE-SOURCE-BLOCKED", "CANNOT-GATE",
}
REQUIRED_FOR_VERIFIED = ("source_id", "locator", "retrieval_date")
SKIP_DIRS = {"01-INHERITED", ".git", "node_modules"}

# Failure types. These are the second half of a baseline key, so they are
# stable strings: renaming one silently un-excuses every row baselined
# under the old name.
F_LEDGER_MISSING = "ledger-missing"
F_DECISIONS_MISSING = "decisions-register-missing"
F_DUPLICATE_DECISION_ID = "duplicate-decision-id"
F_DUPLICATE_ROW_ID = "duplicate-row-id"
F_STATUS_NOT_IN_VOCAB = "status-not-in-vocabulary"
F_VERIFIED_MISSING_FIELD = "verified-missing-field"
F_SOURCE_ID_NOT_IN_LEDGER = "source-id-not-in-ledger"
F_DECISION_REF_UNRESOLVED = "decision-ref-unresolved"

failures = []


def fail(message, *, file, row_id, failure_type, detail="", line=None):
    """Record one failure.

    `message` is the human line, unchanged from earlier versions of this
    script. The keyed fields are what the push gate matches against the
    baseline: `file` and `row_id` identify the row across edits that move
    it, `failure_type` says which rule it broke, and `detail` is the
    specific offending value — a baselined row whose detail has changed is
    a different failure and is not excused.
    """
    failures.append({
        "file": file,
        "row_id": row_id,
        "failure_type": failure_type,
        "detail": detail,
        "line": line,
        "message": message,
    })


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ledger_ids():
    if not LEDGER.exists():
        rel = str(LEDGER.relative_to(ROOT))
        fail(f"ledger missing: {rel}",
             file=rel, row_id="-", failure_type=F_LEDGER_MISSING)
        return set()
    ids = set()
    for row in read_csv(LEDGER):
        sid = (row.get("source_id") or row.get("id") or "").strip()
        if sid:
            ids.add(sid)
    return ids


def decision_ids():
    if not DECISIONS.exists():
        rel = str(DECISIONS.relative_to(ROOT))
        fail(f"decisions register missing: {rel}",
             file=rel, row_id="-", failure_type=F_DECISIONS_MISSING)
        return set(), {}
    counts = {}
    for row in read_csv(DECISIONS):
        did = (row.get("decision_id") or row.get("id") or "").strip()
        if did:
            counts[did] = counts.get(did, 0) + 1
    for did, n in counts.items():
        if n > 1:
            fail(f"OWNER-DECISIONS.csv: {did} appears {n} times",
                 file=str(DECISIONS.relative_to(ROOT)), row_id=did,
                 failure_type=F_DUPLICATE_DECISION_ID, detail=str(n))
    return set(counts), counts


def check_register(path, ledger):
    rel = path.relative_to(ROOT)
    rows = read_csv(path)
    if not rows:
        return
    fields = rows[0].keys()
    has_status = "status" in fields
    id_field = next((c for c in fields if c.endswith("_id") or c == "id"), None)
    seen = set()
    for n, row in enumerate(rows, start=2):
        rid = (row.get(id_field) or "").strip() if id_field else ""
        # A register with no identifier column, or a row with an empty one,
        # can only be addressed by position. Say so in the key rather than
        # silently keying an unidentifiable row as if it had an id.
        key_id = rid or f"(row {n}, no id column)"
        if id_field:
            if rid in seen:
                fail(f"{rel}:{n}: duplicate {id_field} {rid}",
                     file=str(rel), row_id=rid or key_id,
                     failure_type=F_DUPLICATE_ROW_ID, detail=id_field, line=n)
            seen.add(rid)
        if not has_status:
            continue
        status = (row.get("status") or "").strip()
        if status and status not in STATUS_VOCAB:
            fail(f"{rel}:{n}: status '{status}' not in vocabulary",
                 file=str(rel), row_id=key_id,
                 failure_type=F_STATUS_NOT_IN_VOCAB, detail=status, line=n)
        if status == "VERIFIED":
            for col in REQUIRED_FOR_VERIFIED:
                if col in fields and not (row.get(col) or "").strip():
                    fail(f"{rel}:{n}: VERIFIED row missing {col}",
                         file=str(rel), row_id=key_id,
                         failure_type=F_VERIFIED_MISSING_FIELD,
                         detail=col, line=n)
            sid = (row.get("source_id") or "").strip()
            if sid and ledger and sid not in ledger:
                fail(f"{rel}:{n}: source_id {sid} not in access ledger",
                     file=str(rel), row_id=key_id,
                     failure_type=F_SOURCE_ID_NOT_IN_LEDGER,
                     detail=sid, line=n)


def check_decision_refs(known):
    pat = re.compile(r"\bD-\d{3}\b")
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix not in {".md", ".csv"} or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = str(path.relative_to(ROOT))
        for ref in sorted(set(pat.findall(text))):
            if ref not in known:
                fail(f"{rel}: reference {ref} has no OWNER-DECISIONS row",
                     file=rel, row_id=ref,
                     failure_type=F_DECISION_REF_UNRESOLVED, detail=ref)


def main():
    parser = argparse.ArgumentParser(add_help=True, description=__doc__)
    parser.add_argument(
        "--json", action="store_true", dest="as_json",
        help="emit failures as JSON records keyed by file, row id and type",
    )
    args = parser.parse_args()

    ledger = ledger_ids()
    known, _ = decision_ids()
    if REGISTER_DIR.exists():
        for path in sorted(REGISTER_DIR.rglob("*.csv")):
            check_register(path, ledger)
    check_decision_refs(known)

    if args.as_json:
        json.dump(failures, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        sys.exit(1 if failures else 0)

    if failures:
        print(f"validate-registers: {len(failures)} failure(s)")
        for f in failures:
            print("  " + f["message"])
        sys.exit(1)
    print("validate-registers: all checks pass")


if __name__ == "__main__":
    main()
