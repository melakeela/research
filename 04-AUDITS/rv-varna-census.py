#!/usr/bin/env python3
"""
Census of the lemma várṇa- in the Rigveda, and of the compounds built on it.

Written for CORRECTIONS-PENDING.md brief 4. what-varna-meant.html publishes
"All 23 Occurrences ... sorted by sense". The count 23 entered this repository
only as 03-REGISTERS/inherited-claims.csv IH-086, INHERITED-UNVERIFIED, from
gret_scan.json record 0 - a file this repository does not hold, whose stated
corpus total (180,196 words) is not the total of the pinned corpus (164,758).

This script tests the count against the pinned corpus instead. It does NOT
assign a sense to any occurrence: the Zurich layer carries lemma and
morphology, not sense, and Grassmann's gloss offers eight senses without
distributing them over passages. The sense sort is the owed work (IH-287,
handoff work item 19) and this script does not do it.

Source: VedaWebProject/vedaweb-data @ d3eb8af (CC-BY-4.0)
Ledger: SRC-019, SRC-022, SRC-023, SRC-085

Method is the pur- family method of 04-AUDITS/rigveda-pur-family-method.md
applied to a different lemma: select on lemma_id, not on a surface string.
The simplex lemma id is read from the corpus rather than hardcoded, by
matching Grassmann's lemma string.

Usage: rv-varna-census.py [TOKENS_TSV] [OUT_CSV]
"""
import csv, sys, collections

TOKENS = sys.argv[1] if len(sys.argv) > 1 else "/tmp/rv_tokens_vedaweb.tsv"
OUT    = sys.argv[2] if len(sys.argv) > 2 else "03-REGISTERS/rigveda-varna-occurrences.csv"

SIMPLEX = "várṇa-"          # Grassmann Nominalstamm; gloss at §gloss below
GLOSS   = "Farbe, Stamm, Art, Gattung, Partei, Menschenart, Stand, Kaste"

# Arnold's codes; lowercase = period indicated by metrical variations alone
# (PUR-011). Ordered earliest to latest as Arnold presents them.
STRATA = {"A": "Archaic", "S": "Strophic", "N": "Normal",
          "C": "Cretic", "P": "Popular"}

rows = list(csv.DictReader(open(TOKENS, encoding="utf-8"), delimiter="\t"))
print(f"corpus: {len(rows)} tokens")

# The simplex lemma id, read from the data.
ids = {r["lemma_id"] for r in rows if r["lemma"] == SIMPLEX}
assert len(ids) == 1, f"expected one lemma id for {SIMPLEX}, got {ids}"
lid = ids.pop()

simplex = [r for r in rows if r["lemma_id"] == lid]
# Compounds: any other lemma whose string contains the stem varṇa/varṇas.
comp = [r for r in rows if r["lemma_id"] != lid
        and ("varṇa" in r["lemma"] or "varṇas" in r["lemma"])]

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(["occ_id", "stanza", "pada", "token_index", "surface", "lemma",
                "lemma_id", "morphology", "arnold_stratum_code", "arnold_stratum",
                "stratum_certainty", "sense", "sense_source", "source_id",
                "retrieval_date"])
    for i, r in enumerate(sorted(simplex, key=lambda r: (r["stanza"], r["pada"],
                                                        int(r["tok_i"]))), 1):
        code = r["stratum"]
        w.writerow([f"VAR-OCC-{i:03d}", r["stanza"], r["pada"], r["tok_i"],
                    r["surface"], r["lemma"], r["lemma_id"], r["morph"], code,
                    STRATA.get(code.upper(), ""),
                    "certain" if code.isupper() else "metrical-variations-only",
                    "NOT ASSIGNED", "no retrieved source assigns a sense per passage",
                    "SRC-019; SRC-022; SRC-023; SRC-085", "2026-09-07"])

print(f"simplex {SIMPLEX} ({lid}): {len(simplex)} tokens")
print(f"  gloss: {GLOSS}  ({len(GLOSS.split(','))} senses, undistributed)")
print(f"  strata: {dict(collections.Counter(r['stratum'].upper() for r in simplex))}")
print(f"  books:  {dict(sorted(collections.Counter(int(r['book']) for r in simplex).items()))}")
print(f"  stanzas {len({r['stanza'] for r in simplex})}, "
      f"hymns {len({(r['book'], r['hymn']) for r in simplex})}")
print(f"compound tokens containing the stem: {len(comp)} "
      f"over {len({r['lemma'] for r in comp})} lemmas")
for lem, n in collections.Counter(r["lemma"] for r in comp).most_common():
    print(f"    {n:>3}  {lem}")
print(f"\n-> {OUT}")
