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
     A source_id cell may carry several identifiers separated by ';'
     — a corpus measurement routinely rests on the clone, the lemma
     layer, the strata layer and the derived table, and recording all
     four is right. Each is resolved separately; the cell passes only
     if every identifier in it resolves.
  4. Every claim_id is unique within its file.
  5. Every D- reference in the tree resolves to exactly one row in
     09-DECISIONS/OWNER-DECISIONS.csv, either directly or by following
     09-DECISIONS/DECISION-ID-MAP.csv from an old identifier to the row
     it landed on. CLAUDE.md: "a D- reference in an older file is
     resolved through that map." Identifiers that were renumbered or
     folded are never reused, so the map is the only thing that keeps
     an older file's reference readable. Chains are followed to their
     end; a map row pointing at a number with no register row still
     fails, as does a reference in neither place.

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
ID_MAP = ROOT / "09-DECISIONS" / "DECISION-ID-MAP.csv"

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


def split_source_ids(cell):
    """A source_id cell holds one or more identifiers separated by ';'.

    Returns each identifier separately so a claim resting on four
    sources records all four in one row and still resolves. Empty
    cells and empty segments yield nothing.
    """
    return [part.strip() for part in (cell or "").split(";") if part.strip()]


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
            for col in REQUIRED_FOR_VERIFIED:
                if col in fields and not (row.get(col) or "").strip():
                    fail(f"{rel}:{n}: VERIFIED row missing {col}")
            for sid in split_source_ids(row.get("source_id")):
                if ledger and sid not in ledger:
                    fail(f"{rel}:{n}: source_id {sid} not in access ledger")


def resolvable_ids(known):
    """Identifiers a D- reference may legitimately name.

    A register row resolves directly. An identifier that was renumbered
    on merge, or folded into another row, resolves through
    DECISION-ID-MAP.csv to the row it landed on — following the chain,
    because the map records identifiers that moved more than once. An
    old identifier is never freed and never reused, so this widens what
    resolves without letting an unallocated number pass.
    """
    if not ID_MAP.exists():
        return set(known)
    edges = {}
    for row in read_csv(ID_MAP):
        old = (row.get("old_id") or "").strip()
        new = (row.get("new_id") or "").strip()
        if old and new and old != new:
            edges.setdefault(old, set()).add(new)

    resolvable = set(known)
    for old in edges:
        if old in resolvable:
            continue
        seen, frontier = {old}, set(edges[old])
        while frontier:
            nxt = frontier.pop()
            if nxt in known:
                resolvable.add(old)
                break
            if nxt in seen:
                continue
            seen.add(nxt)
            frontier |= edges.get(nxt, set())
    return resolvable


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
                fail(f"{path.relative_to(ROOT)}: reference {ref} has no OWNER-DECISIONS "
                 f"row and no DECISION-ID-MAP path to one")


def main():
    ledger = ledger_ids()
    known, _ = decision_ids()
    known = resolvable_ids(known)
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
