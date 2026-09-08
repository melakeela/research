#!/usr/bin/env python3
"""
path-migration-build.py — generate 00-CONTROLLER/PATH-MIGRATION.csv.

CLAUDE.md and the reconciliation both forbid moving a file before the
references to it are known. This script is the enumeration. It walks every
git-tracked path, counts every inbound textual reference to that path from
every other tracked file, and writes one row per path.

**It moves nothing.** Every row's `migration_state` is `NOT-MOVED`; the
`proposed_path` column records the destination the 2026-09-07 cross-repository
audit proposed, so that the crosswalk exists before any move does, and
`proposed_path_status` says that the proposal is not adopted. A move becomes
possible only when an owner decision adopts the target structure (D-046) and
the `inbound_references` count for the path is zero or every referring file is
edited in the same commit.

Reference counting is deliberately generous: a path is counted as referenced
if its full repository-relative path OR its basename appears in another
tracked file. Basename matches over-count (a common basename such as
`README.md` matches everywhere), so the row carries both numbers separately
and the validator reads `inbound_refs_fullpath`, which is the one that is
exact.

Regenerate from the repository root:

    python3 04-AUDITS/path-migration-build.py

Do not hand-edit 00-CONTROLLER/PATH-MIGRATION.csv; the next run overwrites it.
"""
import csv
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "00-CONTROLLER" / "PATH-MIGRATION.csv"

# The destination each current path was proposed for by the 2026-09-07
# cross-repository audit ("Old path -> proposed path migration map"). Keys are
# matched as directory prefixes or exact paths, longest key first. A path with
# no entry gets NO-PROPOSAL-RECORDED, which is a finding, not an omission: the
# audit's map does not cover every current path.
PROPOSED = {
    "00-CONTROLLER/METHODOLOGY-CONSTITUTION.md": "governance/research-method.md",
    "00-CONTROLLER/CONTROLLER-RECONCILIATION.md": "governance/history/controller-conflicts.md",
    "00-CONTROLLER/PROGRAMME.md": "programme/README.md",
    "00-CONTROLLER/RESEARCH-CONSTITUTION.md": "archive/inherited/controllers/research-constitution.md",
    "01-INHERITED/": "archive/inherited/",
    "02-SOURCES/access-ledger.csv": "evidence/sources/access-events.csv",
    "02-SOURCES/dependency.csv": "evidence/sources/dependencies.csv",
    "02-SOURCES/": "evidence/sources/",
    "03-REGISTERS/": "evidence/registers/",
    "04-AUDITS/": "assurance/audits/",
    "05-HOLDS/": "assurance/holds/",
    "06-BACKLOG/": "programme/backlog/",
    "06-BRIEFS/": "programme/briefs/",
    "09-DECISIONS/OWNER-DECISIONS.csv": "governance/decisions.csv",
    "09-DECISIONS/DECISION-ID-MAP.csv": "governance/decision-aliases.csv",
    "09-DECISIONS/": "governance/",
    "13-PRODUCT-ARCHITECTURE/": "programme/product/",
    "DECISIONS-NEEDED.md": "governance/open-decisions.md",
    "RESEARCH-QUEUE.md": "programme/queue.md",
    "README-TEAM.md": "governance/ai-roles.md",
    "AI-AGENT-ROSTER.md": "governance/ai-roles.md",
}

# Which folder each path belongs to for the authority column. Mirrors
# 00-CONTROLLER/REPOSITORY-MAP.md; the validator checks the two agree.
AUTHORITY = {
    "00-CONTROLLER": "control-plane",
    "01-INHERITED": "inherited-intake",
    "02-SOURCES": "source-authority",
    "03-REGISTERS": "claim-authority",
    "04-AUDITS": "assurance",
    "05-HOLDS": "assurance",
    "06-BACKLOG": "programme",
    "06-BRIEFS": "programme",
    "09-DECISIONS": "decision-authority",
    "13-PRODUCT-ARCHITECTURE": "programme",
    ".claude": "tool-adapter",
    ".github": "tool-adapter",
}

TEXT_SUFFIXES = {".md", ".csv", ".py", ".sh", ".json", ".txt", ".yml", ".yaml"}


def tracked_paths():
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    )
    return [p for p in out.stdout.splitlines() if p]


def proposal_for(path):
    for key in sorted(PROPOSED, key=len, reverse=True):
        if key.endswith("/"):
            if path.startswith(key):
                return PROPOSED[key] + path[len(key):]
        elif path == key:
            return PROPOSED[key]
    return "NO-PROPOSAL-RECORDED"


def authority_for(path):
    top = path.split("/")[0]
    if "/" not in path:
        return "repository-root"
    return AUTHORITY.get(top, "UNASSIGNED")


def main():
    paths = tracked_paths()
    texts = {}
    for p in paths:
        fp = ROOT / p
        if fp.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            texts[p] = fp.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

    full_refs = defaultdict(list)
    base_refs = defaultdict(int)
    for target in paths:
        base = target.split("/")[-1]
        for src, body in texts.items():
            if src == target:
                continue
            if target in body:
                full_refs[target].append(src)
            elif base in body:
                base_refs[target] += 1

    rows = []
    for p in sorted(paths):
        referrers = sorted(full_refs.get(p, []))
        rows.append({
            "current_path": p,
            "authority": authority_for(p),
            "migration_state": "NOT-MOVED",
            "proposed_path": proposal_for(p),
            "proposed_path_status": "PROPOSED-NOT-ADOPTED (D-046)",
            "inbound_refs_fullpath": len(referrers),
            "inbound_refs_basename_only": base_refs.get(p, 0),
            "referring_files": "; ".join(referrers),
            "move_precondition": (
                "D-046 adopts the target structure, and all "
                f"{len(referrers)} full-path reference(s) are rewritten in the "
                "same commit"
                if referrers else
                "D-046 adopts the target structure; no full-path reference to "
                "rewrite"
            ),
            "old_path_crosswalk": p,
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    print(f"path-migration-build: {len(rows)} paths -> {OUT.relative_to(ROOT)}")
    unassigned = [r["current_path"] for r in rows if r["authority"] == "UNASSIGNED"]
    if unassigned:
        print("  paths with no folder authority:", ", ".join(unassigned))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
