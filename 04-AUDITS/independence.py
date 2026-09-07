#!/usr/bin/env python3
"""
independence.py — which cited sources are one independent observation.

Shared by the generator that writes `independence_group` into
03-REGISTERS/claim-sources.csv and the validator that checks it is still
right. Two copies would let the generated column drift from the dependency
register it is supposed to summarise, and the column decides whether a claim
citing four sources rests on four observations or on two. Adversarial review
showed the column could simply be hand-edited to erase every independence
finding; the validator now re-derives it from here and compares.

The merge rule, stated plainly because it is the fragile part: two sources
are merged when 02-SOURCES/dependency.csv names them both and its
`effect_on_status` does NOT open with "No effect". A row that records no
effect is a fact about retrieval — the same source probed twice, a layer
cited alongside its container — not a collapse of two observations into one.

That is a substantive evidentiary question resting on the first two words of
a free-prose column. Rewording one cell would silently merge or unmerge two
sources. It is recorded as CONTRADICTION-REGISTER.csv CR-025 and the fix is a
controlled column on the dependency register, which is a schema change and
belongs with D-044.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY = ROOT / "02-SOURCES" / "dependency.csv"


def groups():
    """Return (find, merges) — find(source_id) gives its group root."""
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

    merges = []
    if DEPENDENCY.exists():
        with open(DEPENDENCY, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                a = (row.get("source_a") or "").strip()
                b = (row.get("source_b") or "").strip()
                effect = (row.get("effect_on_status") or "").strip()
                if not a or not b or a == b:
                    continue                      # self-pair or no second source
                if effect.upper().startswith("NO EFFECT"):
                    continue
                union(a, b)
                merges.append((row.get("dependency_id"), a, b))
    return find, merges


def group_of(find, source_id):
    return "IG-" + find(source_id)
