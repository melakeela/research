#!/usr/bin/env python3
"""
build-path-migration.py — generate 00-CONTROLLER/PATH-MIGRATION.csv.

The migration map is not the hard part. Knowing what breaks when a path
moves is. This script enumerates, for every tracked path in the repository,
every other file that mentions it, and writes that count into the row. No
path may be moved until its `references_enumerated` cell is populated and
its referencing files have been updated in the same commit.

Nothing is moved here, and this script never moves anything. `move_status`
is NOT-MOVED on every row it writes. The proposed destinations come from
the cross-repository audit of 2026-09-07; the numbering disappears from
folder names and the functional name survives.

The old path is never freed. Every row is a permanent crosswalk entry: a
reference written against the old path resolves through this file, which is
why rows are added and never deleted, exactly as the decision-ID map works.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import csvdialect  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "00-CONTROLLER" / "PATH-MIGRATION.csv"

FIELDS = ["path_id", "current_path", "proposed_path", "move_status",
          "references_enumerated", "referenced_by", "rename_class",
          "blocking_reason", "notes"]

# Prefix rules, longest match first. Destination follows the audit's map:
# numbering leaves the folder names, function stays.
RULES = [
    ("00-CONTROLLER/METHODOLOGY-CONSTITUTION.md", "governance/research-method.md", "MERGE-NOT-COPY"),
    ("00-CONTROLLER/CONTROLLER-RECONCILIATION.md", "governance/history/controller-conflicts.md", "SPLIT"),
    ("00-CONTROLLER/RESEARCH-CONSTITUTION.md", "archive/inherited/controllers/research-constitution.md", "MOVE"),
    ("00-CONTROLLER/PROGRAMME.md", "programme/README.md", "MOVE"),
    ("00-CONTROLLER/REPOSITORY-MAP.md", "governance/authority-matrix.md", "MOVE"),
    ("00-CONTROLLER/PATH-MIGRATION.csv", "governance/path-aliases.csv", "MOVE"),
    ("00-CONTROLLER/CANONICAL-FILES.csv", "governance/canonical-files.csv", "MOVE"),
    ("00-CONTROLLER/CONTRADICTION-REGISTER.csv", "governance/contradictions.csv", "MOVE"),
    ("00-CONTROLLER/OVERRIDE-LOG.csv", "assurance/waivers/override-log.csv", "MOVE"),
    ("00-CONTROLLER/STATUS-DIMENSIONS.md", "governance/status-dimensions.md", "MOVE"),
    ("00-CONTROLLER/MIGRATION-HOLDS.csv", "assurance/holds/migration-holds.csv", "MOVE"),
    ("01-INHERITED/", "archive/inherited/", "MOVE"),
    ("02-SOURCES/access-ledger.csv", "evidence/sources/access-events.csv", "MOVE"),
    ("02-SOURCES/dependency.csv", "evidence/sources/dependencies.csv", "MOVE"),
    ("02-SOURCES/", "evidence/sources/manifests/", "MOVE"),
    ("03-REGISTERS/", "evidence/registers/", "MOVE"),
    ("04-AUDITS/validate-registers.py", "assurance/audits/validate-registers.py", "MOVE"),
    ("05-HOLDS/", "assurance/holds/", "MOVE"),
    ("06-BACKLOG/", "programme/backlog/", "MOVE"),
    ("06-BRIEFS/", "programme/briefs/", "MOVE"),
    ("09-DECISIONS/OWNER-DECISIONS.csv", "governance/decisions.csv", "MOVE"),
    ("09-DECISIONS/DECISION-ID-MAP.csv", "governance/decision-aliases.csv", "MOVE"),
    ("09-DECISIONS/", "governance/", "MOVE"),
    ("13-PRODUCT-ARCHITECTURE/", "programme/product/", "MOVE"),
    (".claude/", ".claude/", "STAY"),
    (".gitignore", ".gitignore", "STAY"),
    (".mcp.json", ".mcp.json", "STAY"),
    (".github/", ".github/", "STAY"),
    ("DECISIONS-NEEDED.md", "governance/open-decisions.md", "GENERATE-FROM-REGISTER"),
    ("RESEARCH-QUEUE.md", "programme/queue.md", "MOVE"),
    ("AI-AGENT-ROSTER.md", "governance/ai-roles.md", "MOVE"),
    ("README-TEAM.md", "governance/ai-roles.md", "MOVE"),
    ("CLAUDE.md", "CLAUDE.md", "STAY"),
    ("AGENTS.md", "AGENTS.md", "STAY"),
    ("README.md", "README.md", "STAY"),
]

# Scripts under 04-AUDITS/ divide by what they are, not by where they sit.
METHOD_SCRIPT = re.compile(r"04-AUDITS/(?!validate-registers|build-|migrate-|csvdialect).*\.(py|md)$")


def destination(rel):
    if METHOD_SCRIPT.match(rel) and not rel.endswith(".csv"):
        if any(k in rel for k in ("method", "brief", "FINDINGS", "identifier")):
            return "assurance/audits/" + Path(rel).name, "MOVE"
        return "evidence/methods/" + Path(rel).name, "MOVE"
    for prefix, dest, cls in RULES:
        if rel == prefix:
            return dest, cls
        if prefix.endswith("/") and rel.startswith(prefix):
            return dest + rel[len(prefix):], cls
    if rel.startswith("04-AUDITS/"):
        return "assurance/audits/" + rel[len("04-AUDITS/"):], "MOVE"
    return "", "UNASSIGNED"


def main():
    tracked = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.split()
    tracked = [p for p in tracked if not p.endswith(".gitkeep")]

    # Index the searchable text once.
    searchable = {}
    for rel in tracked:
        p = ROOT / rel
        if p.suffix.lower() in {".md", ".csv", ".py", ".sh", ".json", ".yml", ".yaml", ".txt"}:
            try:
                searchable[rel] = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                pass

    rows = []
    for n, rel in enumerate(sorted(tracked), start=1):
        dest, cls = destination(rel)
        name = Path(rel).name
        refs = []
        for other, text in searchable.items():
            if other == rel:
                continue
            # A full path mention is unambiguous. A bare filename is counted
            # too, because a reference that says only "BACKLOG-COVERAGE.csv"
            # still breaks when the file moves.
            if rel in text or (len(name) > 6 and re.search(r"(?<![\w/.-])" + re.escape(name), text)):
                refs.append(other)
        blocking = ""
        if cls == "UNASSIGNED":
            blocking = "no destination assigned; function not yet defined in REPOSITORY-MAP.md"
        elif refs:
            blocking = (f"{len(refs)} referencing file(s) must be updated in the same "
                        f"commit as the move")
        rows.append({
            "path_id": "PM-%03d" % n,
            "current_path": rel,
            "proposed_path": dest,
            "move_status": "NOT-MOVED",
            "references_enumerated": str(len(refs)),
            "referenced_by": " | ".join(sorted(refs)),
            "rename_class": cls,
            "blocking_reason": blocking,
            "notes": "",
        })

    csvdialect.write(OUT, FIELDS, rows,
                     quoting=__import__("csv").QUOTE_ALL, lineterminator="\n")
    unassigned = [r for r in rows if r["rename_class"] == "UNASSIGNED"]
    heavy = sorted(rows, key=lambda r: -int(r["references_enumerated"]))[:8]
    print(f"path-migration: {len(rows)} paths, all NOT-MOVED")
    print(f"  total references enumerated: {sum(int(r['references_enumerated']) for r in rows)}")
    print(f"  paths with no assigned destination: {len(unassigned)}")
    for r in unassigned:
        print(f"    {r['current_path']}")
    print("  most-referenced paths (these move last):")
    for r in heavy:
        print(f"    {r['references_enumerated']:>3}  {r['current_path']}")


if __name__ == "__main__":
    main()
