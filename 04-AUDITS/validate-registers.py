#!/usr/bin/env python3
"""
validate-registers.py — mechanical enforcement of the evidence rules.

Exit 0 if every governed file passes. Exit 1 with a list of failures otherwise.
`--report` additionally prints the measurements this script deliberately does
not enforce.

What it governs
---------------
Every CSV under 00-CONTROLLER/, 02-SOURCES/, 03-REGISTERS/, 04-AUDITS/,
06-BACKLOG/ and 09-DECISIONS/. 01-INHERITED/ is skipped by design: inherited
material is copied, not corrected, and holding it to this repository's schema
would be the one thing the inheritance rule forbids.

Checks
------
 1. Identifier uniqueness within a file, and within a namespace across files.
    A prefix declared in 00-CONTROLLER/IDENTIFIER-NAMESPACES.csv is allocated
    by exactly one file; the SHARED-KEY prefixes that several registers key on
    are declared as such and exempt.
 2. Every namespace a register actually uses is declared in the registry.
 3. Evidence status: every claim register row carries a value from the closed
    seven-value vocabulary, and no gate verdict appears in a status column.
 4. Interpretive / editorial / publication status against their own
    vocabularies, read from 03-REGISTERS/CLAIM-STATUS.csv.
 5. The generated registers agree with their mirrors. CLAIM-STATUS.csv's
    evidence_status must equal the register's own status cell, and
    CLAIM-SOURCES.csv must decompose the register's own source_id cell — so a
    stale generated file is a failure rather than a silent divergence.
 6. Every VERIFIED row has a source_id, a locator and a retrieval_date, and
    every register carrying VERIFIED rows has those columns at all.
 7. Locator specificity. A locator must be able to re-find the thing: bare
    "see the article" and its relatives fail, and so does a locator with no
    page, line, section, verse, entry, row, hash or identifier in it.
 8. Claim-to-source joins. Every source_id component in every register
    resolves to 02-SOURCES/access-ledger.csv, and every one has a row in
    CLAIM-SOURCES.csv with a resolving independence group.
 9. Source dependency. Every dependency row's source_a_ids and source_b_ids
    resolve to ledger rows, and dependency_id is unique.
10. SUPERSEDED rows point at a replacement, and the replacement resolves.
11. HOLD rows resolve to a file in 05-HOLDS/ or name the hold that blocks them.
12. Owner decisions: closed status vocabulary, unique identifiers, and every
    D-NNN reference in the tree resolving to exactly one row.
13. Re-audit and access-ledger closed vocabularies.
14. Control plane: every top-level directory has a section in
    REPOSITORY-MAP.md; every root file has a row in CANONICAL-FILES.csv;
    PATH-MIGRATION.csv covers every tracked path.
15. Release eligibility. A branch is releasable when checks 1-14 pass, no
    OVERRIDE-LOG row is in force, and every open MIGRATION-HOLDS row is
    declared in the pull request. The script reports the state; it does not
    decide whether to release.

What it still cannot do
-----------------------
It sees whether a row was written claiming a retrieval, never whether the
retrieval happened. It cannot read a locator and tell you the passage says
what the claim says. It cannot tell an independent observation from a
correlated one beyond what 02-SOURCES/dependency.csv already declares.
**A passing validator is a floor, not a warrant**, and it must not be cited in
a pull request as evidence that the registers are sound.

CSVs in this repository mix CRLF and LF and carry embedded newlines inside
quoted cells. Everything here opens with newline='' and never rewrites a file.
"""
import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LEDGER = ROOT / "02-SOURCES" / "access-ledger.csv"
DEPS = ROOT / "02-SOURCES" / "dependency.csv"
DECISIONS = ROOT / "09-DECISIONS" / "OWNER-DECISIONS.csv"
CLAIM_SOURCES = ROOT / "03-REGISTERS" / "CLAIM-SOURCES.csv"
CLAIM_STATUS = ROOT / "03-REGISTERS" / "CLAIM-STATUS.csv"
NAMESPACES = ROOT / "00-CONTROLLER" / "IDENTIFIER-NAMESPACES.csv"
CANONICAL = ROOT / "00-CONTROLLER" / "CANONICAL-FILES.csv"
PATHMAP = ROOT / "00-CONTROLLER" / "PATH-MIGRATION.csv"
REPOMAP = ROOT / "00-CONTROLLER" / "REPOSITORY-MAP.md"
HOLDS_DIR = ROOT / "05-HOLDS"
OVERRIDES = ROOT / "04-AUDITS" / "OVERRIDE-LOG.csv"
MIGRATION_HOLDS = ROOT / "04-AUDITS" / "MIGRATION-HOLDS.csv"

GOVERNED_DIRS = ("00-CONTROLLER", "02-SOURCES", "03-REGISTERS", "04-AUDITS",
                 "06-BACKLOG", "09-DECISIONS")
SKIP_DIRS = {"01-INHERITED", ".git", "node_modules", "__pycache__"}
GENERATED = {"03-REGISTERS/CLAIM-SOURCES.csv", "03-REGISTERS/CLAIM-STATUS.csv"}

# An alias table keys on more than its id column by design: DECISION-ID-MAP is
# keyed on (old_id, old_file) because D-004, D-005 and D-006 each existed in
# two files before the 2026-09-07 merge. Repeats there are the point.
ALIAS_TABLES = {"09-DECISIONS/DECISION-ID-MAP.csv"}

# Files that ALLOCATE source ids rather than cite them. The ledger's source_id
# column is its own primary key, not a citation, so the join check must not
# ask it to appear in CLAIM-SOURCES.csv.
SOURCE_ALLOCATORS = {"02-SOURCES/access-ledger.csv"}

# Only these files' `status` column is an EVIDENCE status. Every other
# governed register with a status column has its own closed vocabulary and is
# checked in check_column_vocabularies() instead.
def is_claim_register(r):
    return r.startswith("03-REGISTERS/") and r not in GENERATED

# --------------------------------------------------------------- vocabularies

EVIDENCE_STATUS = {
    "VERIFIED", "PROVISIONAL", "HYPOTHESIS", "INHERITED-UNVERIFIED",
    "REJECTED", "SUPERSEDED", "HOLD", "NOT-ESTABLISHED",
}
# Gate verdicts are a different dimension and must never appear in a status
# column. Listing them here is what makes check 3 able to say so by name.
GATE_VERDICTS = {
    "ELIGIBLE", "NOT-ELIGIBLE", "NOT-ELIGIBLE-SOURCE-BLOCKED",
    "NOT-ELIGIBLE-GATE-FAILED", "CANNOT-GATE", "NOT-A-HYPOTHESIS", "DEFERRED",
}
INTERPRETIVE_STATUS = GATE_VERDICTS | {"NOT-RECORDED"}
EDITORIAL_STATUS = {"DRAFT", "IN-REVIEW", "CHANGES-REQUIRED",
                    "REVIEWED-ACCEPTED", "RETIRED", "NOT-RECORDED"}
PUBLICATION_STATUS = {"PROPOSED", "PUBLISHED", "WITHDRAWN", "NOT-RECORDED"}
DECISION_STATUS = {"OPEN", "BLOCKED", "TAKEN-PENDING-REVIEW", "RESOLVED",
                   "SUPERSEDED"}
REAUDIT_STATUS = {"OPEN", "CLOSED", "RESOLVED"}
REAUDIT_PRIORITY = {"HIGH", "MEDIUM", "LOW"}
ACCESS_STATUS_CLASS = {"PROBE-VERIFIED", "RETRIEVED", "PROBE-INCONCLUSIVE",
                       "EGRESS-BLOCKED", "HELD", "NOT-ATTEMPTED", "SUPERSEDED"}
CONTRADICTION_STATUS = {"OPEN", "PARTLY-RESOLVED", "RESOLVED", "SUPERSEDED"}
MIGRATION_HOLD_STATUS = {"OPEN", "RESOLVED", "SUPERSEDED"}

REQUIRED_FOR_VERIFIED = ("source_id", "locator", "retrieval_date")

# A locator has to be able to re-find the thing. These are the cells that
# cannot: AGENTS.md and CLAUDE.md both single out the vague locator as the
# failure mode this repository exists to prevent.
VAGUE_LOCATOR = re.compile(
    r"^(see (the )?(article|source|paper|book|file|above|below)|ibid\.?|"
    r"passim|n/?a|tbd|tbc|unknown|various|-{1,2}|\.|"
    r"not tested in this unit of work)$", re.I)
# Something that lets a reader land on the same place. Two shapes qualify,
# because this repository has two kinds of source. A printed or numbered
# source is located by a number, a section mark, an identifier or a hash. A
# retrieved dataset is located by a file and the column, key, field, row set
# or expression within it — "rv_tokens_vedaweb.tsv, book column" re-finds its
# measurement exactly, and demanding a digit of it would be demanding the
# wrong thing.
SPECIFIC_LOCATOR = re.compile(
    r"\d|[A-Z]{2,}-\d|§|\bsha256\b|\bhash\b|\bHEAD\b|\bcommit\b"
    r"|\.(csv|tsv|json|xml|txt|md|xlsx|py|html)\b|/"
    r"|\b(column|columns|field|fields|key|keys|entry|entries|row|rows|"
    r"regexe?s?|expression|grouped|cross-tabulation|deduplicated|intersected|"
    r"filtered)\b|\bname=", re.I)

# A relative locator - "same file; <operation>" - points at the source named by
# the row above it. It re-finds the measurement only if the reader keeps the
# row order, so it qualifies as specific but is reported: it is the locator
# form that breaks first when a register is sorted or a row is moved.
RELATIVE_LOCATOR = re.compile(
    r"^same (file|extraction|dataset|source|corpus)\b\s*[;,]\s*\S", re.I)

SUPERSEDE_TARGET = re.compile(r"\b[A-Z][A-Z0-9-]{1,12}-\d{1,5}\b")
HOLD_REF = re.compile(r"\bHOLD-\d{3}\b")
DECISION_REF = re.compile(r"\bD-\d{3}\b")

failures = []
notes = []


def fail(msg):
    failures.append(msg)


def note(msg):
    notes.append(msg)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def rel(path):
    return str(Path(path).relative_to(ROOT))


def governed_csvs():
    for d in GOVERNED_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.csv")):
            if any(p in SKIP_DIRS for p in path.parts):
                continue
            yield path


def id_column(fields):
    return next((c for c in fields if c and (c.endswith("_id") or c == "id")),
                None)


# ------------------------------------------------------------------ 1, 2. ids

def load_namespaces():
    if not NAMESPACES.exists():
        fail(f"identifier registry missing: {rel(NAMESPACES)}")
        return {}
    ns = {}
    for row in read_csv(NAMESPACES):
        prefix = (row.get("prefix") or "").strip()
        if prefix:
            ns[prefix] = row
    return ns


def split_id(value):
    """('DE-M-030') -> ('DE-M', 30). Returns (None, None) if not an id."""
    m = re.match(r"^([A-Z][A-Z0-9-]*?)-(\d+)$", value)
    return (m.group(1), int(m.group(2))) if m else (None, None)


def check_identifiers(namespaces):
    seen_by_prefix = defaultdict(lambda: defaultdict(set))  # prefix -> file -> ids
    for path in governed_csvs():
        r = rel(path)
        rows = read_csv(path)
        if not rows:
            continue
        idc = id_column(list(rows[0]))
        if not idc:
            continue
        alias = r in ALIAS_TABLES
        local = set()
        for n, row in enumerate(rows, start=2):
            value = (row.get(idc) or "").strip()
            if not value:
                continue
            if value in local and not alias:
                fail(f"{r}:{n}: duplicate {idc} {value}")
            local.add(value)
            prefix, _ = split_id(value)
            if prefix and not alias and r not in GENERATED:
                seen_by_prefix[prefix][r].add(value)

    for prefix, by_file in sorted(seen_by_prefix.items()):
        decl = namespaces.get(prefix)
        if decl is None:
            fail(f"{prefix}-* is allocated in "
                 f"{', '.join(sorted(by_file))} but is not declared in "
                 f"{rel(NAMESPACES)}")
            continue
        rule = (decl.get("cross_file_rule") or "").strip()
        if rule == "SHARED-KEY" or len(by_file) == 1:
            continue
        allocator = (decl.get("allocator_file") or "").strip()
        shared = {x.strip() for x in
                  (decl.get("shared_key_files") or "").split(";") if x.strip()}
        extra = sorted(f for f in by_file if f != allocator and f not in shared)
        if extra:
            fail(f"{prefix}-* is declared {rule} allocated by "
                 f"{allocator or '(none)'} but also appears as an id column in "
                 f"{', '.join(extra)}")


# ------------------------------------------------- 3-8. claims, status, joins

def ledger_ids():
    if not LEDGER.exists():
        fail(f"ledger missing: {rel(LEDGER)}")
        return set()
    ids = set()
    for row in read_csv(LEDGER):
        sid = (row.get("source_id") or row.get("id") or "").strip()
        if sid:
            ids.add(sid)
    return ids


def hold_ids():
    if not HOLDS_DIR.exists():
        return set()
    out = set()
    for f in HOLDS_DIR.glob("HOLD-*.md"):
        m = re.match(r"^(HOLD-\d{3})", f.name)
        if m:
            out.add(m.group(1))
    return out


EXPLICIT_NONE = {"-", "--", "n/a", "N/A", "NA", "NONE", "none"}
RANGE = re.compile(r"^(?P<pre>[A-Z]+-)(?P<lo>\d+)\s+to\s+(?:(?P=pre))?(?P<hi>\d+)$")


def source_components(cell):
    """The ledger ids a source_id cell names, expanding a declared span."""
    out = []
    for part in (p.strip() for p in (cell or "").split(";")):
        if not part or part in EXPLICIT_NONE:
            continue
        m = RANGE.match(part)
        if m:
            lo, hi, w = int(m.group("lo")), int(m.group("hi")), len(m.group("lo"))
            if lo <= hi and hi - lo < 100:
                out.extend(f"{m.group('pre')}{i:0{w}d}" for i in range(lo, hi + 1))
                continue
        out.append(part)
    return out


def check_claim_registers(ledger, holds):
    """Checks 3, 6, 7, 8, 10, 11 over every register with a status column."""
    join = defaultdict(set)
    if CLAIM_SOURCES.exists():
        for row in read_csv(CLAIM_SOURCES):
            join[(row["register"], row["claim_id"])].add(row["source_id"])
    else:
        fail(f"generated join missing: {rel(CLAIM_SOURCES)} — run "
             f"04-AUDITS/claim-sources-build.py")

    for path in governed_csvs():
        r = rel(path)
        if r in GENERATED:
            continue
        rows = read_csv(path)
        if not rows:
            continue
        fields = list(rows[0])
        idc = id_column(fields)
        has_status = "status" in fields
        has_source = "source_id" in fields

        for n, row in enumerate(rows, start=2):
            cid = (row.get(idc) or "").strip() if idc else ""
            status = (row.get("status") or "").strip() if has_status else ""

            # 3. evidence status vocabulary, and no gate verdict in it
            if has_status and status and is_claim_register(r):
                if status in GATE_VERDICTS:
                    fail(f"{r}:{n}: '{status}' is a gate verdict, not an "
                         f"evidence status — it belongs in "
                         f"eligible_for_extended_analysis, not in status")
                elif status not in EVIDENCE_STATUS:
                    fail(f"{r}:{n}: status '{status[:60]}' not in the evidence "
                         f"vocabulary")

            # 6. VERIFIED needs the three columns, and values in them
            if status == "VERIFIED":
                missing = [c for c in REQUIRED_FOR_VERIFIED if c not in fields]
                if missing:
                    fail(f"{r}:{n}: VERIFIED row in a register with no "
                         f"{'/'.join(missing)} column — the retrieval behind it "
                         f"cannot be checked")
                for col in REQUIRED_FOR_VERIFIED:
                    if col in fields and not (row.get(col) or "").strip():
                        fail(f"{r}:{n}: VERIFIED row missing {col}")

            # 7. locator specificity. Enforced on the rows that assert a
            # retrieval; reported on the rest, because a HYPOTHESIS row
            # writing "not tested in this unit of work" in the locator cell is
            # being honest, not vague.
            loc = (row.get("locator") or "").strip()
            if loc:
                relative = RELATIVE_LOCATOR.match(loc) is not None
                if relative:
                    note(f"{r}:{n}: {cid} uses a relative locator "
                         f"('{loc[:45]}') — it resolves only against the row "
                         f"above it and breaks if the register is re-sorted")
                bad = (VAGUE_LOCATOR.match(loc) is not None
                       or (SPECIFIC_LOCATOR.search(loc) is None
                           and not relative))
                if bad and status in ("VERIFIED", "PROVISIONAL"):
                    fail(f"{r}:{n}: {status} row locator '{loc[:70]}' cannot "
                         f"re-find anything — no page, line, section, entry, "
                         f"file-and-column, identifier or hash")
                elif bad:
                    note(f"{r}:{n}: {status or 'unstatused'} row uses the "
                         f"locator cell for a statement rather than a locator: "
                         f"'{loc[:60]}'")

            # 8. every source component resolves, and is in the join
            if has_source and r not in SOURCE_ALLOCATORS:
                comps = source_components(row.get("source_id"))
                for sid in comps:
                    if ledger and sid not in ledger:
                        fail(f"{r}:{n}: source_id {sid} not in access ledger")
                if comps and CLAIM_SOURCES.exists() and cid:
                    joined = join.get((r, cid), set())
                    missing = [s for s in comps if s not in joined]
                    if missing:
                        fail(f"{r}:{n}: {', '.join(missing)} in the source_id "
                             f"cell has no row in {rel(CLAIM_SOURCES)} — the "
                             f"join is stale; re-run claim-sources-build.py")

            # 10. SUPERSEDED points at a replacement that resolves
            if status == "SUPERSEDED":
                trail = " ".join((row.get(c) or "") for c in
                                 ("superseded_by", "notes", "supports_page")
                                 if c in fields)
                targets = [t for t in SUPERSEDE_TARGET.findall(trail)
                           if t != cid]
                if not targets:
                    fail(f"{r}:{n}: SUPERSEDED row {cid} names no replacement")

            # 11. HOLD names a hold that exists.
            #
            # Citing a hold that does not exist is a failure. NOT citing one is
            # a note, not a failure: CLAUDE.md requires a HOLD claim to be
            # recorded in 05-HOLDS/ and six files are, but no register carries
            # a column linking a held row to the hold that blocks it. That is
            # a schema gap rather than a defect in the row, and filling it
            # means choosing a hold for someone else's row. MH-009, RA-019.
            if status == "HOLD":
                trail = " ".join((row.get(c) or "") for c in fields)
                refs = set(HOLD_REF.findall(trail))
                if not refs:
                    note(f"{r}:{n}: HOLD row {cid} names no HOLD- file "
                         f"(MH-009)")
                for h in sorted(refs - holds):
                    fail(f"{r}:{n}: HOLD row {cid} cites {h}, which has no "
                         f"file in 05-HOLDS/")


def check_generated_mirrors():
    """Check 5: the generated registers must agree with what they mirror."""
    if not CLAIM_STATUS.exists():
        fail(f"generated status register missing: {rel(CLAIM_STATUS)} — run "
             f"04-AUDITS/claim-status-build.py")
        return
    status_rows = read_csv(CLAIM_STATUS)
    by_key = {(r["register"], r["claim_id"]): r for r in status_rows}

    for row in status_rows:
        for col, vocab in (("evidence_status", EVIDENCE_STATUS),
                           ("interpretive_status", INTERPRETIVE_STATUS),
                           ("editorial_status", EDITORIAL_STATUS),
                           ("publication_status", PUBLICATION_STATUS)):
            v = (row.get(col) or "").strip()
            if v not in vocab:
                fail(f"{rel(CLAIM_STATUS)}: {row['claim_id']} {col} "
                     f"'{v[:50]}' not in vocabulary")

    seen = set()
    for path in governed_csvs():
        r = rel(path)
        if r in GENERATED or not r.startswith("03-REGISTERS/"):
            continue
        rows = read_csv(path)
        if not rows or "status" not in rows[0]:
            continue
        idc = id_column(list(rows[0]))
        for n, row in enumerate(rows, start=2):
            cid = (row.get(idc) or "").strip() if idc else ""
            mirrored = (row.get("status") or "").strip()
            key = (r, cid)
            seen.add(key)
            got = by_key.get(key)
            if got is None:
                fail(f"{r}:{n}: {cid} has no row in {rel(CLAIM_STATUS)} — "
                     f"re-run claim-status-build.py")
                continue
            evidence = got["evidence_status"]
            expected = mirrored if mirrored in EVIDENCE_STATUS else "NOT-ESTABLISHED"
            if evidence != expected:
                fail(f"{r}:{n}: {cid} status '{mirrored}' but "
                     f"{rel(CLAIM_STATUS)} evidence_status '{evidence}' — the "
                     f"gate and its mirror disagree")
    for key in sorted(set(by_key) - seen):
        fail(f"{rel(CLAIM_STATUS)}: {key[1]} in {key[0]} has no matching "
             f"register row — the generated file is stale")


# ------------------------------------------------------------ 9. dependencies

def check_dependencies(ledger):
    if not DEPS.exists():
        fail(f"dependency register missing: {rel(DEPS)}")
        return
    rows = read_csv(DEPS)
    if rows and "source_a_ids" not in rows[0]:
        fail(f"{rel(DEPS)}: no source_a_ids/source_b_ids columns — the prose "
             f"cells cannot be resolved to ledger rows")
        return
    for n, row in enumerate(rows, start=2):
        did = (row.get("dependency_id") or "").strip()
        for col in ("source_a_ids", "source_b_ids"):
            cell = (row.get(col) or "").strip()
            ids = [x.strip() for x in cell.split(";") if x.strip()]
            if not ids:
                note(f"{rel(DEPS)}:{n}: {did} has an empty {col} — a "
                     f"dependency with one side contributes no edge (MH-007)")
                continue
            for sid in ids:
                if ledger and sid not in ledger:
                    fail(f"{rel(DEPS)}:{n}: {col} {sid} not in access ledger")
            prose = (row.get(col.replace("_ids", "")) or "")
            for sid in re.findall(r"\bSRC-\d{3}\b", prose):
                if sid not in ids:
                    fail(f"{rel(DEPS)}:{n}: {sid} appears in {col[:-4]} prose "
                         f"but not in {col}")


# --------------------------------------------------- 12, 13. closed vocabularies

def check_decisions():
    if not DECISIONS.exists():
        fail(f"decisions register missing: {rel(DECISIONS)}")
        return set()
    counts = Counter()
    for n, row in enumerate(read_csv(DECISIONS), start=2):
        did = (row.get("decision_id") or "").strip()
        if did:
            counts[did] += 1
        st = (row.get("status") or "").strip()
        if st not in DECISION_STATUS:
            fail(f"{rel(DECISIONS)}:{n}: {did} status '{st}' not in "
                 f"{sorted(DECISION_STATUS)}")
        if st == "SUPERSEDED" and not SUPERSEDE_TARGET.search(
                row.get("notes") or ""):
            fail(f"{rel(DECISIONS)}:{n}: {did} is SUPERSEDED and names no "
                 f"superseding decision")
    for did, k in counts.items():
        if k > 1:
            fail(f"{rel(DECISIONS)}: {did} appears {k} times")
    return set(counts)


def check_column_vocabularies():
    checks = [
        (ROOT / "04-AUDITS" / "REAUDIT-QUEUE.csv", "reaudit_id",
         [("status", REAUDIT_STATUS), ("priority", REAUDIT_PRIORITY)]),
        (LEDGER, "source_id", [("access_status_class", ACCESS_STATUS_CLASS)]),
        (ROOT / "00-CONTROLLER" / "CONTRADICTION-REGISTER.csv",
         "contradiction_id", [("status", CONTRADICTION_STATUS)]),
        (MIGRATION_HOLDS, "hold_id", [("status", MIGRATION_HOLD_STATUS)]),
    ]
    for path, idc, cols in checks:
        if not path.exists():
            fail(f"governed register missing: {rel(path)}")
            continue
        rows = read_csv(path)
        for n, row in enumerate(rows, start=2):
            for col, vocab in cols:
                if col not in row:
                    fail(f"{rel(path)}: no {col} column")
                    break
                v = (row.get(col) or "").strip()
                if v not in vocab:
                    fail(f"{rel(path)}:{n}: {row.get(idc, '?')} {col} "
                         f"'{v[:50]}' not in {sorted(vocab)}")


def check_decision_refs(known):
    for path in ROOT.rglob("*"):
        if any(p in SKIP_DIRS for p in path.parts):
            continue
        if path.suffix not in {".md", ".csv"} or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for ref in sorted(set(DECISION_REF.findall(text))):
            if ref not in known:
                fail(f"{rel(path)}: reference {ref} has no OWNER-DECISIONS row")


# ------------------------------------------------------------ 14. control plane

def check_control_plane():
    if not REPOMAP.exists():
        fail(f"control plane missing: {rel(REPOMAP)}")
        return
    mapped = REPOMAP.read_text(encoding="utf-8")
    for d in sorted(p.name for p in ROOT.iterdir()
                    if p.is_dir() and p.name not in SKIP_DIRS
                    and not p.name.startswith(".git")):
        if f"`{d}/`" not in mapped:
            fail(f"{rel(REPOMAP)}: directory {d}/ has no section — every "
                 f"folder needs one authority")

    if not CANONICAL.exists():
        fail(f"control plane missing: {rel(CANONICAL)}")
    else:
        listed = CANONICAL.read_text(encoding="utf-8")
        for f in sorted(p.name for p in ROOT.iterdir()
                        if p.is_file() and p.suffix == ".md"):
            if f not in listed and f not in mapped:
                fail(f"{rel(CANONICAL)}: root file {f} names no function it is "
                     f"authoritative for")

    if not PATHMAP.exists():
        fail(f"control plane missing: {rel(PATHMAP)}")
        return
    covered = {r["current_path"] for r in read_csv(PATHMAP)}
    import subprocess
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT,
                                 capture_output=True, text=True,
                                 check=True).stdout.split()
    except Exception:
        return
    for p in sorted(set(tracked) - covered):
        fail(f"{rel(PATHMAP)}: tracked path {p} is not covered — re-run "
             f"04-AUDITS/path-migration-build.py")


# --------------------------------------------------- 15. release eligibility

def release_state():
    """Returns (releasable, lines). Reports; does not decide."""
    lines = []
    releasable = True

    if OVERRIDES.exists():
        from datetime import date
        today = date.today().isoformat()
        live = [r for r in read_csv(OVERRIDES)
                if (r.get("expiry") or "").strip() >= today]
        if live:
            releasable = False
            lines.append(f"{len(live)} override(s) in force: "
                         + ", ".join(r.get("override_id", "?") for r in live))
        else:
            lines.append("no override in force")
    else:
        lines.append("no override log")

    if MIGRATION_HOLDS.exists():
        open_holds = [r for r in read_csv(MIGRATION_HOLDS)
                      if (r.get("status") or "").strip() == "OPEN"]
        lines.append(f"{len(open_holds)} open migration hold(s): "
                     + ", ".join(r["hold_id"] for r in open_holds))
        lines.append("  each must be named in the pull request; they do not "
                     "block release on their own")
    return releasable, lines


def report():
    print("\n-- report: measured, not enforced " + "-" * 42)
    if CLAIM_SOURCES.exists() and CLAIM_STATUS.exists():
        groups = defaultdict(set)
        for row in read_csv(CLAIM_SOURCES):
            groups[(row["register"], row["claim_id"])].add(
                row["independence_group"])
        st = read_csv(CLAIM_STATUS)
        print(f"claims: {len(st)}")
        for col in ("evidence_status", "interpretive_status",
                    "editorial_status", "publication_status"):
            c = Counter(r[col] for r in st)
            print(f"  {col}: "
                  + ", ".join(f"{k}={v}" for k, v in c.most_common()))
        ver = [r for r in st if r["evidence_status"] == "VERIFIED"]
        one = sum(1 for r in ver
                  if len(groups.get((r["register"], r["claim_id"]), set())) <= 1)
        print(f"VERIFIED claims resting on one independence group: "
              f"{one} of {len(ver)}")
        print("  not enforced: demoting them mechanically would rewrite "
              "research findings to satisfy a tool. D-051, MH-008.")
    ok, lines = release_state()
    print("release eligibility: " + ("CLEAR" if ok else "BLOCKED"))
    for line in lines:
        print("  " + line)
    for n in notes:
        print("note: " + n)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report", action="store_true",
                    help="also print what is measured but not enforced")
    args = ap.parse_args()

    namespaces = load_namespaces()
    ledger = ledger_ids()
    holds = hold_ids()

    check_identifiers(namespaces)
    check_claim_registers(ledger, holds)
    check_generated_mirrors()
    check_dependencies(ledger)
    known = check_decisions()
    check_column_vocabularies()
    check_decision_refs(known)
    check_control_plane()

    if failures:
        print(f"validate-registers: {len(failures)} failure(s)")
        for f in failures:
            print("  " + f)
        if args.report:
            report()
        sys.exit(1)

    print("validate-registers: all checks pass")
    releasable, _ = release_state()
    if not releasable:
        print("  release eligibility: BLOCKED by a live override "
              "(04-AUDITS/OVERRIDE-LOG.csv)")
    if args.report:
        report()


if __name__ == "__main__":
    main()
