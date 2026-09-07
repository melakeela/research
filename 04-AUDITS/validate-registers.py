#!/usr/bin/env python3
"""
validate-registers.py — mechanical enforcement of the evidence rules.

Exit 0 if every register passes. Exit 1 with a list of failures otherwise.
Run before every push. Wire as a hook so a session cannot push a
VERIFIED row that no retrieval backs.

Checks:
  1. Every row's status is in the vocabulary.
  2. Every VERIFIED row has non-empty source_id, locator, retrieval_date.
  3. Every identifier in a VERIFIED row's source_id resolves to a row in
     02-SOURCES/access-ledger.csv.
  4. Every claim_id is unique within its file.
  5. Every D- reference in the tree resolves to exactly one row in
     09-DECISIONS/OWNER-DECISIONS.csv.

On check 3 and multi-source cells. A claim that rests on four retrievals
records four identifiers in one cell, semicolon-separated -- a corpus
measurement routinely rests on the repository clone, the lemma layer, the
strata layer and the derived token table at once, and splitting one claim
across four rows would break the one-claim-per-row rule instead. Reading
such a cell as a single identifier made it fail wholesale, which meant the
identifiers inside it were never checked at all. Splitting on ';' and
resolving each one is therefore STRICTER than what it replaces, not looser:
every identifier is now resolved individually, and a cell containing one
good identifier and one bad one now fails on the bad one instead of failing
uninformatively on both. Owner decision D-042; the disagreement it settles
is recorded at 04-AUDITS/VALIDATOR-FINDINGS-2026-09-07.md class 1.

CSVs in this repository mix CRLF and LF and carry embedded newlines
inside quoted cells. Everything here opens with newline='' and never
rewrites a file.
"""
import csv
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

failures = []


def fail(msg):
    failures.append(msg)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ledger_ids():
    if not LEDGER.exists():
        fail(f"ledger missing: {LEDGER.relative_to(ROOT)}")
        return set()
    ids = set()
    for row in read_csv(LEDGER):
        sid = (row.get("source_id") or row.get("id") or "").strip()
        if sid:
            ids.add(sid)
    return ids


def decision_ids():
    if not DECISIONS.exists():
        fail(f"decisions register missing: {DECISIONS.relative_to(ROOT)}")
        return set(), {}
    counts = {}
    for row in read_csv(DECISIONS):
        did = (row.get("decision_id") or row.get("id") or "").strip()
        if did:
            counts[did] = counts.get(did, 0) + 1
    for did, n in counts.items():
        if n > 1:
            fail(f"OWNER-DECISIONS.csv: {did} appears {n} times")
    return set(counts), counts


def source_ids(cell):
    """
    Every identifier in a source_id cell.

    One claim may rest on several retrievals; the registers record them in
    one cell, semicolon-separated. Each is resolved separately. See the
    module docstring for why this is stricter than reading the cell whole.
    """
    return [part.strip() for part in (cell or "").split(";") if part.strip()]


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
        if id_field:
            rid = (row.get(id_field) or "").strip()
            if rid in seen:
                fail(f"{rel}:{n}: duplicate {id_field} {rid}")
            seen.add(rid)
        if not has_status:
            continue
        status = (row.get("status") or "").strip()
        if status and status not in STATUS_VOCAB:
            fail(f"{rel}:{n}: status '{status}' not in vocabulary")
        if status == "VERIFIED":
            for col in REQUIRED_FOR_VERIFIED:
                if col in fields and not (row.get(col) or "").strip():
                    fail(f"{rel}:{n}: VERIFIED row missing {col}")
            for sid in source_ids(row.get("source_id")):
                if ledger and sid not in ledger:
                    fail(f"{rel}:{n}: source_id {sid} not in access ledger")


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
        for ref in sorted(set(pat.findall(text))):
            if ref not in known:
                fail(f"{path.relative_to(ROOT)}: reference {ref} has no OWNER-DECISIONS row")


def main():
    ledger = ledger_ids()
    known, _ = decision_ids()
    if REGISTER_DIR.exists():
        for path in sorted(REGISTER_DIR.rglob("*.csv")):
            check_register(path, ledger)
    check_decision_refs(known)

    if failures:
        print(f"validate-registers: {len(failures)} failure(s)")
        for f in failures:
            print("  " + f)
        sys.exit(1)
    print("validate-registers: all checks pass")


if __name__ == "__main__":
    main()
