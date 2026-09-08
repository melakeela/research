#!/usr/bin/env python3
"""
claim-sources-build.py — generate 03-REGISTERS/CLAIM-SOURCES.csv.

The problem this fixes
----------------------
Every register in this repository cites several sources per row, joined with
"; " in one `source_id` cell — `"SRC-019; SRC-022; SRC-023"`. That cell is
opaque: it cannot be joined on, it cannot carry a per-source locator, it
cannot say what each source *does* for the claim, and it cannot say which of
the sources are independent of each other. Two of the three failure modes the
validator was blind to in 2026-09-07 came out of that cell.

The repair is a normalised many-to-many join: one row per (register row,
source), with the evidence role the source plays and the independence group it
belongs to. `03-REGISTERS/CLAIM-SOURCES.csv` is the authority for
claim→source. The register's own `source_id` cell is retained **unchanged** as
a human-readable mirror, and `validate-registers.py` fails any disagreement
between the two. Retaining it is deliberate: rewriting the cell would rewrite
rows the research units wrote, and CLAUDE.md forbids editing a register to
suit a tool. Whether the mirror is eventually retired is owner decision D-049.

independence_group
------------------
A connected component of `02-SOURCES/dependency.csv`, computed over rows whose
`source_a` and `source_b` both resolve to a ledger id. The grouping is
deliberately **conservative in one direction only**:

  * two sources in the SAME group MAY NOT be counted as independent
    confirmation of each other;
  * two sources in DIFFERENT groups are merely *not yet shown to be
    dependent* — that is not the same as proven independent.

So the count of distinct groups behind a claim is a **ceiling** on its
independent observations, never a floor. `DEP-003` states outright that two of
its sources are only "partially independent" and is still merged, because
merging can only ever lower the ceiling. Nothing in this script promotes or
demotes a claim: `python3 04-AUDITS/validate-registers.py --report` prints what
the numbers show, and D-051 asks whether they should gate anything.

evidence_role
-------------
Derived from the source's `category` in the access ledger, through the mapping
table below. It classifies what kind of thing the source is, which is a
property of the source rather than of the claim; a finer per-claim role is a
later refinement and would have to be authored, not derived. A category with
no mapping yields `UNCLASSIFIED`, which is a finding rather than a default.

Regenerate from the repository root:

    python3 04-AUDITS/claim-sources-build.py

Do not hand-edit 03-REGISTERS/CLAIM-SOURCES.csv; the next run overwrites it.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "02-SOURCES" / "access-ledger.csv"
DEPS = ROOT / "02-SOURCES" / "dependency.csv"
OUT = ROOT / "03-REGISTERS" / "CLAIM-SOURCES.csv"

# Directories whose CSVs carry source_id cells that this join covers.
SCAN_DIRS = ("03-REGISTERS", "04-AUDITS")

# Generated files are never scanned: the join must not join to itself.
GENERATED = {"03-REGISTERS/CLAIM-SOURCES.csv", "03-REGISTERS/CLAIM-STATUS.csv"}

# Cells that explicitly declare "this row rests on no source". They are not
# missing values and not unresolved ids; they produce no join row. Used by
# CROSS-DOMAIN-BRIDGES and INTERNAL-CONTRADICTIONS for rows that record a
# bridge deliberately not crossed, or a contradiction between two registers
# rather than between two sources.
EXPLICIT_NONE = {"-", "--", "n/a", "N/A", "NA", "NONE", "none"}

# One register cell writes a span of ledger ids as prose: "SRC-053 to SRC-058".
# The join expands it, because a span is unambiguous and the alternative is an
# unresolvable row. The register cell is NOT rewritten - that would be editing
# another unit's register - and every expanded row is marked so in notes, is
# reported by this script, and is held at MH-002 for owner confirmation.
RANGE = re.compile(r"^(?P<pre>[A-Z]+-)(?P<lo>\d+)\s+to\s+(?:(?P=pre))?(?P<hi>\d+)$")

ROLE_BY_CATEGORY = {
    "primary-corpus": "PRIMARY-SOURCE",
    "primary-text": "PRIMARY-SOURCE",
    "primary-text-edition": "PRIMARY-SOURCE",
    "primary-text-archive": "PRIMARY-SOURCE",
    "primary-source-repository": "PRIMARY-SOURCE",
    "primary-monograph": "PRIMARY-SOURCE",
    "primary-annotation": "ANALYTICAL-LAYER",
    "editorial-apparatus": "ANALYTICAL-LAYER",
    "primary-lexicon": "REFERENCE-WORK",
    "primary-lexical-data": "REFERENCE-WORK",
    "primary-reference-work": "REFERENCE-WORK",
    "primary-comparative-dataset": "REFERENCE-WORK",
    "reference-work-derivative": "REFERENCE-WORK-DERIVATIVE",
    "reference-dataset": "REFERENCE-WORK-DERIVATIVE",
    "derived-database": "REFERENCE-WORK-DERIVATIVE",
    "reconstruction-set": "RECONSTRUCTION",
    "tertiary-reference": "TERTIARY",
    "tertiary": "TERTIARY",
    "translation": "TRANSLATION",
    "secondary": "SECONDARY-LITERATURE",
    "secondary-literature": "SECONDARY-LITERATURE",
    "secondary-web": "SECONDARY-LITERATURE",
    "journal-literature": "SECONDARY-LITERATURE",
    "preprint-repository": "SECONDARY-LITERATURE",
    "paywalled-journal-archive": "SECONDARY-LITERATURE",
    "infrastructure": "INFRASTRUCTURE",
    "retrieval-channel": "INFRASTRUCTURE",
    "mcp-connector": "INFRASTRUCTURE",
    "search-index": "INFRASTRUCTURE",
    "citation-infrastructure": "INFRASTRUCTURE",
    "classification-and-bibliography": "INFRASTRUCTURE",
    "metadata": "INFRASTRUCTURE",
    "repository-self-audit": "SELF-AUDIT",
}


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ledger_index():
    idx = {}
    for row in read_csv(LEDGER):
        sid = (row.get("source_id") or "").strip()
        if sid:
            idx[sid] = row
    return idx


def independence_groups(ledger):
    """Connected components over dependency.csv, restricted to resolving ids."""
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    unresolved = []
    for row in read_csv(DEPS):
        # source_a / source_b are prose and may name a file, a qualifier or
        # several ids; source_a_ids / source_b_ids are the bare ledger ids
        # extracted from them. The graph is built from the id columns only.
        a = [x.strip() for x in (row.get("source_a_ids") or "").split(";") if x.strip()]
        b = [x.strip() for x in (row.get("source_b_ids") or "").split(";") if x.strip()]
        for side, vals in (("source_a_ids", a), ("source_b_ids", b)):
            for val in vals:
                if val not in ledger:
                    unresolved.append(
                        f"{row.get('dependency_id', '?')}.{side} = {val!r}")
        for x in a:
            for y in b:
                if x in ledger and y in ledger and x != y:
                    union(x, y)

    for sid in ledger:
        find(sid)

    roots = sorted({find(s) for s in ledger})
    number = {r: f"IG-{i + 1:03d}" for i, r in enumerate(roots)}
    return {s: number[find(s)] for s in ledger}, unresolved


def scan_files():
    for d in SCAN_DIRS:
        for path in sorted((ROOT / d).rglob("*.csv")):
            rel = str(path.relative_to(ROOT))
            if rel in GENERATED:
                continue
            rows = read_csv(path)
            if not rows or "source_id" not in rows[0]:
                continue
            yield path, rows


def main():
    ledger = ledger_index()
    groups, unresolved_deps = independence_groups(ledger)

    out_rows = []
    unknown_sources = set()
    unclassified = set()
    expanded_ranges = []
    declared_none = 0
    n = 0
    for path, rows in scan_files():
        rel = str(path.relative_to(ROOT))
        fields = list(rows[0])
        id_field = next(
            (c for c in fields if c and (c.endswith("_id") or c == "id")), None)
        has_locator = "locator" in fields
        for row in rows:
            claim_id = (row.get(id_field) or "").strip() if id_field else ""
            cell = (row.get("source_id") or "").strip()
            raw = [p.strip() for p in cell.split(";") if p.strip()]
            parts, expansions = [], {}
            for p in raw:
                if p in EXPLICIT_NONE:
                    declared_none += 1
                    continue
                m = RANGE.match(p)
                if m:
                    lo, hi = int(m.group("lo")), int(m.group("hi"))
                    width = len(m.group("lo"))
                    if lo <= hi and hi - lo < 100:
                        span = [f"{m.group('pre')}{i:0{width}d}"
                                for i in range(lo, hi + 1)]
                        expanded_ranges.append(
                            f"{rel}#{claim_id}: {p!r} -> {span[0]}..{span[-1]}")
                        for one in span:
                            expansions[one] = p
                        parts.extend(span)
                        continue
                parts.append(p)
            if not parts:
                continue
            locator = (row.get("locator") or "").strip() if has_locator else ""
            locator_basis = "row-locator" if locator else "row-reference-only"
            if not locator:
                locator = f"{rel}#{claim_id}"
            for ordinal, sid in enumerate(parts, start=1):
                n += 1
                led = ledger.get(sid)
                if led is None:
                    unknown_sources.add(sid)
                    role = "UNRESOLVED-SOURCE"
                    group = "IG-UNRESOLVED"
                else:
                    cat = (led.get("category") or "").strip()
                    role = ROLE_BY_CATEGORY.get(cat, "UNCLASSIFIED")
                    if role == "UNCLASSIFIED":
                        unclassified.add(cat)
                    group = groups.get(sid, "IG-UNRESOLVED")
                out_rows.append({
                    "join_id": f"CS-{n:05d}",
                    "claim_id": claim_id,
                    "register": rel,
                    "source_id": sid,
                    "source_ordinal_in_cell": ordinal,
                    "evidence_role": role,
                    "locator": locator,
                    "locator_basis": locator_basis,
                    "independence_group": group,
                    "notes": (f"RANGE-EXPANDED-FROM-PROSE-CELL {expansions[sid]!r} "
                              f"(MH-002)" if sid in expansions else ""),
                })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0]), quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(out_rows)

    registers = len({r["register"] for r in out_rows})
    print(f"claim-sources-build: {len(out_rows)} join rows from {registers} "
          f"registers -> {OUT.relative_to(ROOT)}")
    print(f"  independence groups over the ledger: "
          f"{len(set(groups.values()))} for {len(ledger)} sources")
    print(f"  rows declaring no source explicitly: {declared_none}")
    rc = 0
    if expanded_ranges:
        print("  prose source ranges expanded in the join only (MH-002):")
        for e in expanded_ranges:
            print(f"    {e}")
    if unresolved_deps:
        print("  dependency.csv cells that do not resolve to a ledger id:")
        for u in unresolved_deps:
            print(f"    {u}")
        rc = 1
    if unknown_sources:
        print("  source ids with no ledger row: "
              + ", ".join(sorted(unknown_sources)))
        rc = 1
    if unclassified:
        print("  ledger categories with no evidence_role mapping: "
              + ", ".join(sorted(unclassified)))
        rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
