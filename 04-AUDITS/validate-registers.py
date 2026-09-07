#!/usr/bin/env python3
"""
validate-registers.py — mechanical enforcement of the evidence rules.

Exit 0 if every governed file passes. Exit 1 with a list of failures
otherwise. Run in CI on every push and pull request; the local pre-push hook
runs the same script as early feedback.

What it governs is not hard-coded. 00-CONTROLLER/CANONICAL-FILES.csv assigns
every tracked path an authority and a `validated` mode:

  GATED     a defect here fails the build
  REPORTED  a defect here is printed and counted, but does not fail — used
            only where failing would demand rewriting research to satisfy a
            schema, which is not a repair. Each one is carried by a row in
            00-CONTROLLER/MIGRATION-HOLDS.csv saying why.
  NOT-VALIDATED  prose, scripts and inherited material

Checks, in the order they run:

  1  Control plane. Every tracked path is classified and every classified
     path exists. Every tracked path appears in PATH-MIGRATION.csv. The
     registers that say what is authoritative cannot themselves drift.
  2  Identifiers. Unique within a file, and unique across the repository
     within each prefix's namespace, so two files cannot both issue E-4.
  3  Status vocabularies. One enumeration per dimension, from
     STATUS-DIMENSIONS.md. evidence_status is the evidence gate; gate
     verdicts are no longer admitted into it.
  4  Retrieval. A VERIFIED row carries source_id, locator and
     retrieval_date.
  5  Locators. Specific enough to re-find. "See the article" is not a
     locator; an identifier used as one must resolve.
  6  Sources. Every source identifier resolves to the access ledger,
     whatever the row's status — not only VERIFIED rows, which is what the
     previous version checked.
  7  Claim/source join. claim-sources.csv is authoritative for the relation;
     the inline source_id cell is a projection of it and must agree exactly.
  8  Source dependency. Dependency rows resolve to the ledger.
  9  Supersession. A SUPERSEDED row names a replacement and the replacement
     resolves.
 10  Cross-references. Every D- resolves to an owner decision; every HOLD-
     resolves to a file in 05-HOLDS/.
 11  Release eligibility. Nothing may be publication_status PUBLISHED that
     is not release-eligible. The eligible set is reported either way.
 12  Governed Markdown. Every hold in 05-HOLDS/ is referenced by something
     outside it; every DECISIONS-NEEDED.md section is a register row whose
     detail_ref points back at it.
 13  Override log. Rows are well-formed, scoped and dated.

Weakening this file to make failing rows pass is not an available move. The
repair for a failing row is the row, or a recorded owner decision.

CSVs in this repository mix CRLF and LF and carry embedded newlines inside
quoted cells. Everything here opens with newline='' and never rewrites a file.
"""
import argparse
import csv
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gatevocab  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CONTROLLER = ROOT / "00-CONTROLLER"
CANONICAL = CONTROLLER / "CANONICAL-FILES.csv"
PATHMAP = CONTROLLER / "PATH-MIGRATION.csv"
OVERRIDES = CONTROLLER / "OVERRIDE-LOG.csv"
HOLDSREG = CONTROLLER / "MIGRATION-HOLDS.csv"
LEDGER = ROOT / "02-SOURCES" / "access-ledger.csv"
DEPENDENCY = ROOT / "02-SOURCES" / "dependency.csv"
DECISIONS = ROOT / "09-DECISIONS" / "OWNER-DECISIONS.csv"
JOIN = ROOT / "03-REGISTERS" / "claim-sources.csv"
HOLDS_DIR = ROOT / "05-HOLDS"

# --- vocabularies, from 00-CONTROLLER/STATUS-DIMENSIONS.md -----------------
EVIDENCE_STATUS = {"VERIFIED", "PROVISIONAL", "HYPOTHESIS", "INHERITED-UNVERIFIED",
                   "REJECTED", "SUPERSEDED", "HOLD"}
INTERPRETIVE_STATUS = {"UNASSIGNED", "MEASUREMENT-ONLY", "PROPOSED", "CONTESTED",
                       "ACCEPTED", "WITHDRAWN"}
EDITORIAL_STATUS = {"UNASSIGNED", "DRAFT", "IN-REVIEW", "CHANGES-REQUIRED",
                    "APPROVED", "RETIRED"}
PUBLICATION_STATUS = {"UNASSIGNED", "PRIVATE", "PREVIEW", "PUBLISHED",
                      "WITHDRAWN", "ARCHIVED"}
GATE_VERDICT = gatevocab.GATE_VERDICT
DECISION_STATUS = {"OPEN", "BLOCKED", "TAKEN-PENDING-REVIEW", "RESOLVED", "SUPERSEDED"}
REAUDIT_STATUS = {"OPEN", "IN-PROGRESS", "CLOSED"}
PRIORITY = {"HIGH", "MEDIUM", "LOW"}
EVIDENCE_ROLE = {"SOLE", "CONTRIBUTING", "UNASSIGNED"}

# An override signature this short matches half the failure lines in the tree.
# "-" appears in every path; a one-token waiver is a blanket waiver.
MIN_OVERRIDE_SIGNATURE = 24

DIMENSIONS = {
    "evidence_status": EVIDENCE_STATUS,
    "interpretive_status": INTERPRETIVE_STATUS,
    "editorial_status": EDITORIAL_STATUS,
    "publication_status": PUBLICATION_STATUS,
    "gate_verdict": GATE_VERDICT,
}
# Files whose `status` column is a different dimension entirely.
FILE_STATUS_VOCAB = {
    "09-DECISIONS/OWNER-DECISIONS.csv": ("status", DECISION_STATUS),
    "04-AUDITS/REAUDIT-QUEUE.csv": ("status", REAUDIT_STATUS),
    "06-BACKLOG/BACKLOG-COVERAGE.csv": ("status", set()),   # owner's; may be blank
}

REQUIRED_FOR_VERIFIED = ("source_id", "locator", "retrieval_date")

# Registers whose row key is not the first *_id column alone. DECISION-ID-MAP
# is keyed by (old_id, old_file) by design: D-004 existed in two files and a
# bare reference to it is ambiguous without knowing which was meant. An
# identifier that moved twice also keeps one row per number it held.
COMPOSITE_KEY = {
    "09-DECISIONS/DECISION-ID-MAP.csv": ("old_id", "old_file", "new_id"),
}

# Registers exempt from cross-register identifier uniqueness. Both exist to
# carry identifiers issued elsewhere, so repeating them is their function.
ALIAS_REGISTERS = {
    "09-DECISIONS/DECISION-ID-MAP.csv",     # holds D- identifiers from the register
    "03-REGISTERS/claim-sources.csv",       # its claim_id column names other files' rows
}

# A locator has to let a reader re-find the passage. These do not.
VAGUE_LOCATOR = re.compile(
    r"^(see the (article|source|paper|book)|passim|various|throughout|"
    r"n/?a|tbd|unknown|the (article|source|paper)|as above|ibid\.?)$", re.I)
BARE_IDENTIFIER = re.compile(r"^[A-Z]{1,6}(-[A-Z]{1,3})?-\d{1,4}[A-Za-z-]*$")

failures, warnings, notes = [], [], []
# {"path:line": "MH-nnn"} — exact coordinates an open migration hold covers.
# Narrow by construction: a whole-file or prefix waiver is not expressible.
waived_at = {}


def fail(msg):
    """Record a failure, unless an open migration hold names its exact row.

    A waiver here is not a pass. It downgrades one named coordinate to a
    warning that prints the hold on every run, and it can only be created by
    committing a row to MIGRATION-HOLDS.csv that says what could not be
    migrated and what it is blocked on. There is no file-level or pattern
    waiver: `path:line`, or nothing.
    """
    coord = msg.split(":")[0:2]
    key = ":".join(coord)
    hold = waived_at.get(key)
    if hold:
        warnings.append(f"{msg}  [held unmigrated by {hold}]")
    else:
        failures.append(msg)


def warn(msg):
    warnings.append(msg)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


RANGE = re.compile(r"^(?P<prefix>[A-Z]+)-(?P<lo>\d+)\s*(?:to|-|–|—)\s*(?:(?P=prefix)-)?(?P<hi>\d+)$")
NO_SOURCE = {"-", "--", "n/a", "na", "none", ""}


def split_sources(cell):
    """Split a source cell into individual identifiers.

    Three shapes occur in the tree and all three are handled here rather than
    by editing research rows:
      - a ';'-delimited list, which is the normal case
      - a lone '-' or 'none', which means no source and is not an identifier
      - a range, 'SRC-053 to SRC-058', which is expanded to its members. A
        range is the same defect as a list — several identifiers in one
        opaque cell — and expanding it is arithmetic, not interpretation.
    """
    out = []
    for part in (cell or "").replace(",", ";").split(";"):
        part = part.strip()
        if part.lower() in NO_SOURCE:
            continue
        m = RANGE.match(part)
        if m and int(m.group("hi")) > int(m.group("lo")):
            width = len(m.group("lo"))
            out += [f"{m.group('prefix')}-{i:0{width}d}"
                    for i in range(int(m.group("lo")), int(m.group("hi")) + 1)]
        else:
            out.append(part)
    return out


def id_column(fields):
    return next((c for c in fields if c.endswith("_id") and c != "source_id"), None)


# --------------------------------------------------------------------------
def load_governed():
    """Read CANONICAL-FILES.csv into {relpath: (mode, prefix, role)}."""
    if not CANONICAL.exists():
        fail("00-CONTROLLER/CANONICAL-FILES.csv is missing; nothing can be governed")
        return {}
    out = {}
    for row in read_csv(CANONICAL):
        out[row["path"]] = (row.get("validated", ""), row.get("id_prefix", ""),
                            row.get("role", ""))
    return out


def check_control_plane(governed):
    tracked = set(p for p in subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True
    ).stdout.split() if not p.endswith(".gitkeep"))

    for rel in sorted(tracked - set(governed)):
        fail(f"00-CONTROLLER/CANONICAL-FILES.csv: {rel} is tracked but has no authority row")
    for rel in sorted(set(governed) - tracked):
        fail(f"00-CONTROLLER/CANONICAL-FILES.csv: row for {rel}, which is not tracked")

    if PATHMAP.exists():
        mapped = {r["current_path"] for r in read_csv(PATHMAP)}
        for rel in sorted(tracked - mapped):
            fail(f"00-CONTROLLER/PATH-MIGRATION.csv: {rel} has no crosswalk row")
        for r in read_csv(PATHMAP):
            if r.get("move_status") != "NOT-MOVED" and not r.get("references_enumerated"):
                fail(f"PATH-MIGRATION.csv: {r['path_id']} is moved with no references enumerated")
    else:
        fail("00-CONTROLLER/PATH-MIGRATION.csv is missing")


def ledger_ids():
    if not LEDGER.exists():
        fail(f"ledger missing: {LEDGER.relative_to(ROOT)}")
        return set()
    return {(r.get("source_id") or "").strip() for r in read_csv(LEDGER)
            if (r.get("source_id") or "").strip()}


def decision_ids():
    if not DECISIONS.exists():
        fail("09-DECISIONS/OWNER-DECISIONS.csv is missing")
        return set()
    counts = {}
    for row in read_csv(DECISIONS):
        did = (row.get("decision_id") or "").strip()
        if did:
            counts[did] = counts.get(did, 0) + 1
    for did, n in sorted(counts.items()):
        if n > 1:
            fail(f"OWNER-DECISIONS.csv: {did} appears {n} times")
    return set(counts)


def all_register_ids(governed):
    """Every identifier issued anywhere, for resolving identifier-shaped locators."""
    ids = set()
    for rel in governed:
        p = ROOT / rel
        if p.suffix != ".csv" or not p.is_file():
            continue
        try:
            rows = read_csv(p)
        except (OSError, csv.Error):
            continue
        if not rows:
            continue
        col = id_column(rows[0].keys())
        if col:
            ids |= {(r.get(col) or "").strip() for r in rows if (r.get(col) or "").strip()}
    return ids


# --------------------------------------------------------------------------
def check_file(rel, mode, prefix, ledger, known_ids):
    """Checks 2-6 and 9 over one governed CSV."""
    report = fail if mode == "GATED" else warn
    path = ROOT / rel
    try:
        rows = read_csv(path)
    except (OSError, csv.Error) as exc:
        fail(f"{rel}: unreadable ({exc})")
        return
    if not rows:
        return
    fields = list(rows[0].keys())
    idcol = id_column(fields)

    keycols = COMPOSITE_KEY.get(rel) or ((idcol,) if idcol else ())
    prefixes = tuple(p for p in prefix.split("|") if p)
    seen = set()
    for n, row in enumerate(rows, start=2):
        # --- 2. identifiers
        if keycols:
            key = tuple((row.get(c) or "").strip() for c in keycols)
            if any(key):
                if key in seen:
                    report(f"{rel}:{n}: duplicate {'+'.join(keycols)} {'+'.join(key)}")
                seen.add(key)
        if idcol and prefixes:
            rid = (row.get(idcol) or "").strip()
            if rid and not rid.startswith(prefixes):
                report(f"{rel}:{n}: {idcol} {rid} uses none of this register's "
                       f"declared prefixes {list(prefixes)}")

        # --- 3. status vocabularies
        for col, vocab in DIMENSIONS.items():
            if col in fields:
                v = (row.get(col) or "").strip()
                if col == "evidence_status" and not v:
                    report(f"{rel}:{n}: evidence_status is empty; no claim is unstatused")
                if v and v not in vocab:
                    report(f"{rel}:{n}: {col} '{v[:60]}' not in its vocabulary")
        if rel in FILE_STATUS_VOCAB:
            col, vocab = FILE_STATUS_VOCAB[rel]
            v = (row.get(col) or "").strip()
            if v and vocab and v not in vocab:
                report(f"{rel}:{n}: {col} '{v[:60]}' not in the {rel} vocabulary")
        if "priority" in fields:
            v = (row.get("priority") or "").strip()
            if v and v not in PRIORITY:
                report(f"{rel}:{n}: priority '{v[:40]}' not in {sorted(PRIORITY)}")

        # --- 3b. the parsed gate verdict must still agree with its prose
        if "gate_verdict" in fields and "eligible_for_extended_analysis" in fields:
            declared = (row.get("gate_verdict") or "").strip()
            derived = gatevocab.parse(row.get("eligible_for_extended_analysis"))
            if declared != derived:
                report(f"{rel}:{n}: gate_verdict {declared!r} does not match "
                       f"{derived!r}, which is what its eligibility prose says; "
                       f"the parse is not a one-time act")

        status = (row.get("evidence_status") or "").strip()

        # --- 4. retrieval
        if status == "VERIFIED":
            absent = [c for c in REQUIRED_FOR_VERIFIED if c not in fields]
            if absent:
                # Without these columns the retrieval check is structurally
                # unreachable: the row can claim VERIFIED and no check can
                # ever trace it. A register that cannot carry a retrieval
                # cannot carry a VERIFIED row.
                report(f"{rel}:{n}: VERIFIED row in a register with no "
                       f"{', '.join(absent)} column; the retrieval that would "
                       f"back it cannot be recorded here, so VERIFIED is "
                       f"untraceable in this file")
            for col in REQUIRED_FOR_VERIFIED:
                if col in fields and not (row.get(col) or "").strip():
                    report(f"{rel}:{n}: VERIFIED row missing {col}")

        # --- 5. locator quality
        if "locator" in fields:
            loc = (row.get("locator") or "").strip()
            if loc and VAGUE_LOCATOR.match(loc):
                report(f"{rel}:{n}: locator '{loc}' is not specific enough to re-find")
            elif loc and BARE_IDENTIFIER.match(loc) and loc not in known_ids:
                report(f"{rel}:{n}: locator '{loc}' looks like an identifier but "
                       f"resolves to no register row")

        # --- 6. sources resolve, whatever the status
        for sid in split_sources(row.get("source_id")):
            if ledger and sid not in ledger:
                report(f"{rel}:{n}: source_id {sid} is not in the access ledger")

        # --- 9. supersession
        if status == "SUPERSEDED":
            target = (row.get("superseded_by") or "").strip()
            if not target:
                report(f"{rel}:{n}: SUPERSEDED row names no replacement in superseded_by")
            elif target not in known_ids:
                report(f"{rel}:{n}: superseded_by {target} resolves to no register row")


def check_identifier_namespaces(governed):
    """No two registers issue the same identifier.

    Uniqueness was per-file, so two registers could both issue E-4 and
    nothing noticed. The docstring claimed otherwise; this implements it.
    """
    issued = {}
    for rel, (mode, prefix, _role) in sorted(governed.items()):
        if mode == "NOT-VALIDATED" or not rel.endswith(".csv") or rel in ALIAS_REGISTERS:
            continue
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            rows = read_csv(path)
        except (OSError, csv.Error):
            continue
        if not rows:
            continue
        idcol = id_column(rows[0].keys())
        if not idcol:
            continue
        for n, row in enumerate(rows, start=2):
            rid = (row.get(idcol) or "").strip()
            if not rid:
                continue
            if rid in issued and issued[rid][0] != rel:
                fail(f"{rel}:{n}: identifier {rid} is also issued by "
                     f"{issued[rid][0]}:{issued[rid][1]}; an identifier names "
                     f"one row in this repository, not one row per file")
            issued.setdefault(rid, (rel, n))


def check_independence(governed):
    """Report claims whose cited sources collapse to one observation.

    The join computes independence_group and, until now, nothing read it.
    CLAUDE.md: two citations tracing to the same author, excavation report or
    dataset count as one. This is a note rather than a failure because
    02-SOURCES/dependency.csv records in prose that some collapses were
    assessed and cleared (DEP-006 on DME-008 and DME-009), and nothing in the
    data distinguishes assessed from unassessed. Naming them is what makes
    that gap visible instead of latent.
    """
    if not JOIN.exists():
        return
    per_claim = {}
    for r in read_csv(JOIN):
        if r.get("register_class") != "CLAIM":
            continue
        per_claim.setdefault((r["register"], r["claim_id"]), []).append(
            (r["source_id"], r["independence_group"]))
    collapsed = []
    for (rel, cid), pairs in sorted(per_claim.items()):
        if len(pairs) < 2:
            continue
        if len({g for _s, g in pairs}) < len(pairs):
            collapsed.append((rel, cid, len(pairs), len({g for _s, g in pairs})))
    verified = set()
    for rel in {c[0] for c in collapsed}:
        try:
            rows = read_csv(ROOT / rel)
        except (OSError, csv.Error):
            continue
        idcol = id_column(rows[0].keys()) if rows else None
        for row in rows:
            if (row.get("evidence_status") or "").strip() == "VERIFIED":
                verified.add((rel, (row.get(idcol) or "").strip()))
    hits = [c for c in collapsed if (c[0], c[1]) in verified]
    if hits:
        notes.append(
            f"independence: {len(hits)} VERIFIED claim(s) cite sources the "
            f"dependency register collapses into fewer independent observations")
        for rel, cid, cited, groups in hits:
            notes.append(f"  {rel} {cid}: {cited} sources, {groups} independent")
        notes.append("  assessed-and-cleared is not distinguishable from "
                     "unassessed in the data; RA-012 tracks that gap")


def check_join(governed, ledger):
    """7. The join is authoritative; the inline cell must agree with it exactly."""
    if not JOIN.exists():
        fail("03-REGISTERS/claim-sources.csv is missing; the claim/source relation "
             "has no authority")
        return
    join = read_csv(JOIN)
    by_claim = {}
    for n, r in enumerate(join, start=2):
        sid = (r.get("source_id") or "").strip()
        role = (r.get("evidence_role") or "").strip()
        if role and role not in EVIDENCE_ROLE:
            fail(f"03-REGISTERS/claim-sources.csv:{n}: evidence_role {role!r} "
                 f"not in {sorted(EVIDENCE_ROLE)}")
        loc = (r.get("locator") or "").strip()
        if loc and VAGUE_LOCATOR.match(loc):
            fail(f"03-REGISTERS/claim-sources.csv:{n}: locator {loc!r} is not "
                 f"specific enough to re-find")
        if ";" in sid or "," in sid:
            fail(f"03-REGISTERS/claim-sources.csv:{n}: source_id {sid!r} holds more "
                 f"than one identifier; the join exists to prevent exactly this")
        if ledger and sid and sid not in ledger:
            fail(f"03-REGISTERS/claim-sources.csv:{n}: source_id {sid} not in the ledger")
        by_claim.setdefault((r.get("register"), (r.get("claim_id") or "").strip()),
                            set()).add(sid)

    for rel, (mode, _prefix, _role) in sorted(governed.items()):
        if mode == "NOT-VALIDATED" or not rel.endswith(".csv") or rel == "03-REGISTERS/claim-sources.csv":
            continue
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            rows = read_csv(path)
        except (OSError, csv.Error):
            continue
        if not rows or "source_id" not in rows[0].keys():
            continue
        idcol = id_column(rows[0].keys())
        if not idcol:
            continue
        for n, row in enumerate(rows, start=2):
            cid = (row.get(idcol) or "").strip()
            if not cid:
                continue
            inline = set(split_sources(row.get("source_id")))
            joined = by_claim.pop((rel, cid), set())
            # Compared even when the inline cell is empty. Skipping that case
            # left the mirror one-directional: blanking a claim's source cell
            # while the join still held its rows passed silently.
            if inline != joined:
                fail(f"{rel}:{n}: claim {cid} cites {sorted(inline)} inline but the "
                     f"join register holds {sorted(joined)}; regenerate with "
                     f"04-AUDITS/build-claim-sources.py")

    # Join rows whose claim exists in no register are orphans: a relation to
    # something that is not there.
    for (jrel, jcid), sids in sorted(by_claim.items()):
        fail(f"03-REGISTERS/claim-sources.csv: {len(sids)} row(s) join {jcid} in "
             f"{jrel}, which holds no such row")


def check_dependency(ledger):
    """8. Dependency rows resolve to the ledger."""
    if not DEPENDENCY.exists():
        fail("02-SOURCES/dependency.csv is missing")
        return
    seen = set()
    for n, row in enumerate(read_csv(DEPENDENCY), start=2):
        did = (row.get("dependency_id") or "").strip()
        if did in seen:
            fail(f"02-SOURCES/dependency.csv:{n}: duplicate dependency_id {did}")
        seen.add(did)
        for col in ("source_a", "source_b"):
            sid = (row.get(col) or "").strip()
            if sid and ledger and sid not in ledger:
                fail(f"02-SOURCES/dependency.csv:{n}: {col} {sid} is not in the ledger")
        if not (row.get("effect_on_status") or "").strip():
            fail(f"02-SOURCES/dependency.csv:{n}: {did} states no effect on status; "
                 f"a dependency that changes nothing has not been assessed")


def check_cross_references(known_decisions):
    """10. D- and HOLD- references resolve."""
    holds = {p.name.split("-")[0] + "-" + p.name.split("-")[1]
             for p in HOLDS_DIR.glob("HOLD-*.md")} if HOLDS_DIR.exists() else set()
    dpat, hpat = re.compile(r"\bD-\d{3}\b"), re.compile(r"\bHOLD-\d{3}\b")
    skip = {"01-INHERITED", ".git"}
    for path in ROOT.rglob("*"):
        if any(part in skip for part in path.parts):
            continue
        if path.suffix not in {".md", ".csv"} or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = path.relative_to(ROOT)
        for ref in sorted(set(dpat.findall(text))):
            if ref not in known_decisions:
                fail(f"{rel}: reference {ref} has no OWNER-DECISIONS row")
        for ref in sorted(set(hpat.findall(text))):
            if holds and ref not in holds:
                fail(f"{rel}: reference {ref} has no file in 05-HOLDS/")


def check_markdown_gated():
    """Real checks for the governed files that are not CSVs.

    Marking a .md file GATED and then only reading CSVs would be an
    overstatement of the same kind this pass exists to remove. These are the
    two invariants those files actually carry.
    """
    # Every hold file is referenced by something. A hold nobody is waiting on
    # is either finished or forgotten, and neither should sit silently.
    if HOLDS_DIR.exists():
        text = ""
        for path in ROOT.rglob("*"):
            if "05-HOLDS" in path.parts or ".git" in path.parts:
                continue
            if path.suffix in {".md", ".csv"} and path.is_file():
                text += path.read_text(encoding="utf-8", errors="replace")
        for hold in sorted(HOLDS_DIR.glob("HOLD-*.md")):
            hid = "-".join(hold.name.split("-")[:2])
            if hid not in text:
                fail(f"05-HOLDS/{hold.name}: {hid} is referenced by nothing outside "
                     f"05-HOLDS/; a hold nobody is waiting on is finished or forgotten")

    # DECISIONS-NEEDED.md holds prose for blocking decisions and allocates no
    # identifiers. Every section it heads must be a register row that points
    # back at it, which is the CLAUDE.md routing rule made mechanical.
    needed = ROOT / "DECISIONS-NEEDED.md"
    if needed.exists() and DECISIONS.exists():
        back = {(r.get("decision_id") or "").strip()
                for r in read_csv(DECISIONS)
                if (r.get("detail_ref") or "").startswith("DECISIONS-NEEDED.md")}
        for m in re.finditer(r"^#{1,3}\s+(D-\d{3})\b", needed.read_text(encoding="utf-8"),
                             re.M):
            did = m.group(1)
            if did not in back:
                fail(f"DECISIONS-NEEDED.md: section {did} has no OWNER-DECISIONS row "
                     f"whose detail_ref points back at it; the register is "
                     f"authoritative and the prose allocates nothing")


def check_release_eligibility(governed):
    """11. Nothing is published that has not earned it."""
    eligible = blocked = published = 0
    for rel, (mode, _p, _r) in sorted(governed.items()):
        if mode == "NOT-VALIDATED" or not rel.endswith(".csv"):
            continue
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            rows = read_csv(path)
        except (OSError, csv.Error):
            continue
        if not rows or "evidence_status" not in rows[0].keys():
            continue
        idcol = id_column(rows[0].keys())
        for n, row in enumerate(rows, start=2):
            ev = (row.get("evidence_status") or "").strip()
            ed = (row.get("editorial_status") or "").strip()
            pub = (row.get("publication_status") or "").strip()
            ok = ev in {"VERIFIED", "PROVISIONAL"} and ed == "APPROVED"
            if ok:
                eligible += 1
            else:
                blocked += 1
            if pub == "PUBLISHED":
                published += 1
                if not ok:
                    fail(f"{rel}:{n}: {row.get(idcol)} is publication_status PUBLISHED "
                         f"but not release-eligible (evidence_status={ev or 'empty'}, "
                         f"editorial_status={ed or 'empty'})")
    notes.append(f"release eligibility: {eligible} eligible, {blocked} not eligible, "
                 f"{published} marked PUBLISHED")
    if eligible == 0:
        notes.append("  no claim has passed editorial review yet; editorial_status is "
                     "UNASSIGNED across the tree, which is the truthful value after a "
                     "migration that promoted nothing")


def load_migration_waivers():
    """Read the exact coordinates open holds cover. Must run before any check."""
    if not HOLDSREG.exists():
        return
    for row in read_csv(HOLDSREG):
        if (row.get("disposition") or "").strip().upper() != "OPEN":
            continue
        for coord in (row.get("waives_validation_at") or "").split(";"):
            coord = coord.strip()
            if coord:
                waived_at[coord] = row["hold_id"]


def check_migration_holds():
    """Every open migration hold is surfaced on every run.

    A row that could not be migrated without changing its meaning was left
    unchanged. That is the right call, and it is also the kind of thing a
    repository quietly forgets. Printing them each run is what stops
    'recorded' from becoming 'buried'.
    """
    if not HOLDSREG.exists():
        fail("00-CONTROLLER/MIGRATION-HOLDS.csv is missing")
        return
    for row in read_csv(HOLDSREG):
        if (row.get("disposition") or "").strip().upper() == "OPEN":
            warn(f"{row['hold_id']}: {row['target']} — not migrated; "
                 f"blocked on {row['blocked_on'][:90]}")


def check_overrides():
    """12. Override rows are well-formed. Returns the currently active ones."""
    active = []
    if not OVERRIDES.exists():
        fail("00-CONTROLLER/OVERRIDE-LOG.csv is missing; the gate has no waiver record")
        return active
    required = ("override_id", "reason", "actor", "raised_date", "expiry_date",
                "affected_validation_failures")
    today = date.today()
    for n, row in enumerate(read_csv(OVERRIDES), start=2):
        missing = [c for c in required if not (row.get(c) or "").strip()]
        if missing:
            fail(f"00-CONTROLLER/OVERRIDE-LOG.csv:{n}: override row missing {missing}")
            continue
        # Parsed, not string-compared. "never" sorts after any ISO date, so a
        # lexical comparison made it a permanent waiver.
        try:
            expiry = date.fromisoformat(row["expiry_date"].strip())
        except ValueError:
            fail(f"00-CONTROLLER/OVERRIDE-LOG.csv:{n}: expiry_date "
                 f"{row['expiry_date'].strip()!r} is not an ISO date (YYYY-MM-DD); "
                 f"an override without a real expiry never expires")
            continue
        try:
            raised = date.fromisoformat(row["raised_date"].strip())
        except ValueError:
            fail(f"00-CONTROLLER/OVERRIDE-LOG.csv:{n}: raised_date "
                 f"{row['raised_date'].strip()!r} is not an ISO date")
            continue
        if expiry < raised:
            fail(f"00-CONTROLLER/OVERRIDE-LOG.csv:{n}: expiry_date precedes raised_date")
            continue
        if (expiry - raised).days > 90:
            fail(f"00-CONTROLLER/OVERRIDE-LOG.csv:{n}: override runs "
                 f"{(expiry - raised).days} days; an emergency waiver is bounded, "
                 f"90 days at most, and is renewed by a new row that says why")
            continue
        # A short signature matches half the failure lines in the tree: every
        # one contains a path, so "-" alone waives everything. A waiver names
        # the failure it waives.
        bad = [sig.strip() for sig in row["affected_validation_failures"].split(";")
               if 0 < len(sig.strip()) < MIN_OVERRIDE_SIGNATURE]
        if bad:
            fail(f"00-CONTROLLER/OVERRIDE-LOG.csv:{n}: waiver signature(s) {bad} "
                 f"shorter than {MIN_OVERRIDE_SIGNATURE} characters; a signature "
                 f"this general waives failures nobody has read")
            continue
        if expiry >= today:
            active.append(row)
    return active


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", help="write a markdown report to this path")
    ap.add_argument("--list-active-overrides", action="store_true")
    args = ap.parse_args()

    load_migration_waivers()
    governed = load_governed()
    check_control_plane(governed)
    ledger = ledger_ids()
    known_decisions = decision_ids()
    known_ids = all_register_ids(governed)

    for rel, (mode, prefix, _role) in sorted(governed.items()):
        if mode == "NOT-VALIDATED" or not rel.endswith(".csv"):
            continue
        if rel == "03-REGISTERS/claim-sources.csv":
            continue                      # check_join owns this file entirely
        if (ROOT / rel).is_file():
            check_file(rel, mode, prefix, ledger, known_ids)

    check_identifier_namespaces(governed)
    check_join(governed, ledger)
    check_independence(governed)
    check_dependency(ledger)
    check_cross_references(known_decisions)
    check_markdown_gated()
    check_release_eligibility(governed)
    check_migration_holds()
    active = check_overrides()

    if args.list_active_overrides:
        for row in active:
            print(f"{row['override_id']}\t{row['expiry_date']}\t"
                  f"{row['affected_validation_failures']}")
        return

    for line in notes:
        print(line)
    if warnings:
        print(f"\nvalidate-registers: {len(warnings)} warning(s) "
              f"(REPORTED files; each carries a MIGRATION-HOLDS row)")
        for w in warnings:
            print("  " + w)
    if failures:
        print(f"\nvalidate-registers: {len(failures)} failure(s)")
        for f in failures:
            print("  " + f)
    else:
        print("\nvalidate-registers: all checks pass")

    if args.report:
        Path(args.report).write_text(render_report(len(failures), len(warnings)),
                                     encoding="utf-8")
    sys.exit(1 if failures else 0)


def render_report(nfail, nwarn):
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip()
    lines = [
        "# Validation report", "",
        "Generated by `04-AUDITS/validate-registers.py --report`. Do not hand-edit:",
        "a findings document written by hand goes stale and is then read as current,",
        "which is what happened to `VALIDATOR-FINDINGS-2026-09-07.md` (CR-012).", "",
        f"- Commit: `{head}`",
        f"- Date: {date.today().isoformat()}",
        f"- Failures: **{nfail}**",
        f"- Warnings: **{nwarn}** (REPORTED files; each carries a MIGRATION-HOLDS row)",
        "",
    ]
    lines += ["## Notes", ""] + [f"- {n.strip()}" for n in notes] + [""]
    if warnings:
        lines += ["## Warnings", "", "```"] + warnings + ["```", ""]
    if failures:
        lines += ["## Failures", "", "```"] + failures + ["```", ""]
    else:
        lines += ["## Failures", "", "None.", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    main()
