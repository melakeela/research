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
     A source_id cell may name several sources separated by ";" — the
     source-independence rule requires a claim to cite every source behind
     it — and EACH one must resolve. A cell was previously matched whole
     against the ledger, so any multi-source cell failed no matter what it
     contained; splitting makes the check do its job per component.
  4. Every claim_id is unique within its file.
  4a. A VERIFIED row in a register that has no source_id, locator or
     retrieval_date COLUMN is a failure. Checks 2 and 3 are guarded by
     "if col in fields", so without this a register lacking those columns
     passed both silently and its VERIFIED rows were unverifiable by
     construction.
  5. Every D- reference in the tree resolves to exactly one row in
     09-DECISIONS/OWNER-DECISIONS.csv.

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
            missing_cols = [c for c in REQUIRED_FOR_VERIFIED if c not in fields]
            if missing_cols:
                # A register with no source_id/locator/retrieval_date column at
                # all used to pass silently: the per-column check below is
                # guarded by "if col in fields", so checks 2 and 3 were no-ops
                # on it and a VERIFIED row there was structurally uncheckable.
                fail(f"{rel}:{n}: VERIFIED row in a register with no "
                     f"{'/'.join(missing_cols)} column — the retrieval behind "
                     f"it cannot be checked")
            for col in REQUIRED_FOR_VERIFIED:
                if col in fields and not (row.get(col) or "").strip():
                    fail(f"{rel}:{n}: VERIFIED row missing {col}")
            sid = (row.get("source_id") or "").strip()
            if sid and ledger:
                for one in (p.strip() for p in sid.split(";")):
                    if one and one not in ledger:
                        fail(f"{rel}:{n}: source_id {one} not in access ledger")


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
