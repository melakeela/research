#!/usr/bin/env python3
"""
build-claim-sources.py — generate 03-REGISTERS/claim-sources.csv.

The defect this fixes: 42 register cells held several source identifiers in
one opaque `source_id` string, semicolon-delimited. Nothing could read them.
The validator saw one identifier that resolved to nothing; independence could
not be computed; and a claim's sources could not be given individual roles or
locators. Duplicating the claim row per source was the obvious repair and the
wrong one: it would multiply claim identifiers and make row counts lie.

The repair is a normalised many-to-many join. One row per (claim, source)
pair, carrying the columns a flat cell cannot hold:

  join_id             stable identifier for the pair
  claim_id            the claim
  register            the register the claim lives in — claim identifiers are
                      unique per file, not repository-wide, so the join needs
                      both to be unambiguous
  source_id           one source, never a list
  evidence_role       SOLE if the claim rests on this source alone,
                      CONTRIBUTING if it is one of several. Derived from the
                      row itself; nothing is assigned by judgement here.
  register_class      CLAIM if the register carries an evidence_status column
                      and its rows are claims; DATA if it is an occurrence or
                      measurement table whose rows are evidence for a claim
                      stated elsewhere. Both had multi-valued source cells and
                      both are normalised here, but a DATA row is not a claim
                      and must not be counted as one.
  locator             the claim row's locator where the register has one.
                      The flat schema held a single locator for all of a
                      claim's sources, so the same locator appears on each of
                      that claim's join rows; per-source locators can be
                      filled in later without a schema change.
  independence_group  computed from 02-SOURCES/dependency.csv: sources the
                      dependency register says are one source, not two, share
                      a group. Two join rows in one group are ONE independent
                      observation, which is what CLAUDE.md's source-
                      independence constraint turns on and what no flat cell
                      could ever express.
  notes               provenance of the row

Authority. This register is authoritative for the claim-to-source relation.
The inline `source_id` cell is retained in each claim register, unchanged, as
a human-readable projection of it — retained rather than emptied because
rewriting it would edit research rows to satisfy a schema, and because
`VERIFIED` rows are required to carry a non-empty source reference. The two
cannot drift: validate-registers.py fails if the set of identifiers in a
claim row's cell is not exactly the set of join rows for that claim. That is
one authority with an enforced mirror, not two hand-maintained stores.

Generated. Do not hand-edit; re-run from the repository root.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import csvdialect  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "03-REGISTERS" / "claim-sources.csv"
DEPENDENCY = ROOT / "02-SOURCES" / "dependency.csv"

FIELDS = ["join_id", "claim_id", "register", "register_class", "source_id",
          "evidence_role", "locator", "independence_group", "notes"]

# Directories whose registers participate in the join. 01-INHERITED/ is
# excluded: it is a preserved archive and this repository does not rewrite it.
SEARCH_DIRS = ["03-REGISTERS", "04-AUDITS"]


import re

RANGE = re.compile(r"^(?P<prefix>[A-Z]+)-(?P<lo>\d+)\s*(?:to|-|–|—)\s*(?:(?P=prefix)-)?(?P<hi>\d+)$")
NO_SOURCE = {"-", "--", "n/a", "na", "none", ""}


def split_sources(cell):
    """Split a source cell into identifiers.

    Must agree exactly with validate-registers.split_sources, which enforces
    that this file and the inline cells say the same thing. A lone '-' means
    no source; a range is expanded to its members.
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


def independence_groups():
    """Union-find over the dependency register.

    Only pairs whose `effect_on_status` does NOT open with 'No effect' are
    merged. A dependency row that explicitly records no effect on independence
    (the same source probed twice, a layer cited alongside its container) is
    a fact about retrieval, not a collapse of two observations into one.
    """
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
            parent[max(ra, rb)] = min(ra, rb)

    merged = []
    if DEPENDENCY.exists():
        _, rows = csvdialect.read(DEPENDENCY)
        for row in rows:
            a = (row.get("source_a") or "").strip()
            b = (row.get("source_b") or "").strip()
            effect = (row.get("effect_on_status") or "").strip()
            if not a or not b or a == b:
                continue
            if effect.upper().startswith("NO EFFECT"):
                continue
            union(a, b)
            merged.append((row.get("dependency_id"), a, b))
    return parent, find, merged


def main():
    parent, find, merged = independence_groups()

    rows_out = []
    n = 0
    for d in SEARCH_DIRS:
        for path in sorted((ROOT / d).rglob("*.csv")):
            if path == OUT:
                continue
            fields, rows = csvdialect.read(path)
            if "source_id" not in fields:
                continue
            id_field = next((c for c in fields if c.endswith("_id") and c != "source_id"), None)
            if not id_field:
                continue
            rel = str(path.relative_to(ROOT))
            register_class = "CLAIM" if "evidence_status" in fields else "DATA"
            for row in rows:
                cid = (row.get(id_field) or "").strip()
                sources = split_sources(row.get("source_id"))
                if not cid or not sources:
                    continue
                role = "SOLE" if len(sources) == 1 else "CONTRIBUTING"
                locator = (row.get("locator") or "").strip()
                for sid in sources:
                    n += 1
                    root_id = find(sid)
                    rows_out.append({
                        "join_id": "CS-%04d" % n,
                        "claim_id": cid,
                        "register": rel,
                        "register_class": register_class,
                        "source_id": sid,
                        "evidence_role": role,
                        "locator": locator,
                        "independence_group": "IG-" + root_id,
                        # Left empty by construction. A note that is identical on
                        # every row is documentation, not data; it is in the
                        # docstring above. Row-specific notes go here.
                        "notes": "",
                    })

    csvdialect.write(OUT, FIELDS, rows_out,
                     quoting=__import__("csv").QUOTE_ALL, lineterminator="\n")

    groups = {}
    for r in rows_out:
        groups.setdefault(r["independence_group"], set()).add(r["source_id"])
    collapsing = {g: s for g, s in groups.items() if len(s) > 1}
    claims = {(r["register"], r["claim_id"]) for r in rows_out if r["register_class"] == "CLAIM"}
    data = {(r["register"], r["claim_id"]) for r in rows_out if r["register_class"] == "DATA"}
    multi = sum(1 for r in rows_out if r["evidence_role"] == "CONTRIBUTING")
    print(f"claim-sources: {len(rows_out)} join rows")
    print(f"  over {len(claims)} claim rows and {len(data)} data rows")
    print(f"  {multi} of them come from cells that held more than one source id")
    print(f"dependency merges applied: {len(merged)}")
    for dep, a, b in merged:
        print(f"  {dep}: {a} + {b} -> {find(a)}")
    print(f"independence groups holding more than one source: {len(collapsing)}")
    for g, s in sorted(collapsing.items()):
        print(f"  {g}: {', '.join(sorted(s))}")


if __name__ == "__main__":
    main()
