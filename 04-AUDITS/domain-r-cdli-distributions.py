#!/usr/bin/env python3
"""
domain-r-cdli-distributions.py — distributions over the accepted attestations.

Reads 03-REGISTERS/domain-r-cdli-attestations.csv, written by
domain-r-cdli-extract.py, and reports the four things the fourteen-step
method asks for before any interpretation: when (period), where (findspot as
CDLI attributes it), in whose custody, and whether the four toponyms are ever
named in one and the same text.

Every period and provenience below is CDLI's cataloguing, not this
repository's dating. A period label on a tablet dates the tablet, not the
event it records and not the object it mentions.
"""
import csv, collections, os, re, sys

REG = os.environ.get("DOMAIN_R_OUT", "03-REGISTERS")
rows = list(csv.DictReader(open(os.path.join(REG, "domain-r-cdli-attestations.csv"), encoding="utf-8")))
TOP = ["MELUHHA", "MAGAN", "DILMUN", "MARHASI"]
MAT = ["LAPIS", "CARNELIAN"]

def period_key(p):
    m = re.search(r"ca\.\s*(\d+)", p or "")
    return -int(m.group(1)) if m else 1

def table(target, col, keep=None, top=12):
    c = collections.Counter()
    seen = set()
    for r in rows:
        if r["target"] != target: continue
        if keep and r["classification"] not in keep: continue
        k = (r["p_number"], r[col])
        if k in seen: continue           # count texts, not occurrences
        seen.add(k)
        c[r[col] or "(blank)"] += 1
    return c, sum(c.values())

TOPONYM_KEEP = {"PLACE-DETERMINATIVE (ki)", "LAND-DETERMINATIVE (kur)", "UNMARKED", "PERSON-OF (lu2-)"}
STONE_KEEP = {"STONE-DETERMINATIVE ({na4})", "AKKADIAN-LOGOGRAM (no {na4})"}

print("=" * 78)
print("PERIOD — distinct texts, CDLI's period attribution")
for t in TOP + MAT:
    keep = TOPONYM_KEEP if t in TOP else STONE_KEEP
    c, n = table(t, "cdli_period", keep)
    print(f"\n{t}  ({n} texts)")
    for k, v in sorted(c.items(), key=lambda kv: (period_key(kv[0]), -kv[1]))[:12]:
        print(f"   {v:>5}  {k}")

print("\n" + "=" * 78)
print("PROVENIENCE — distinct texts, CDLI's findspot attribution")
for t in TOP + MAT:
    keep = TOPONYM_KEEP if t in TOP else STONE_KEEP
    c, n = table(t, "cdli_provenience", keep)
    print(f"\n{t}  ({n} texts)")
    for k, v in c.most_common(8):
        print(f"   {v:>5}  {k}")

print("\n" + "=" * 78)
print("CUSTODY — distinct texts, CDLI's collection attribution")
for t in TOP + MAT:
    keep = TOPONYM_KEEP if t in TOP else STONE_KEEP
    c, n = table(t, "cdli_collection", keep)
    print(f"\n{t}  ({n} texts)")
    for k, v in c.most_common(6):
        print(f"   {v:>5}  {k[:78]}")

print("\n" + "=" * 78)
print("CO-OCCURRENCE — are the four toponyms ever named in one text?")
by_text = collections.defaultdict(set)
meta = {}
for r in rows:
    if r["target"] in TOP and r["classification"] in TOPONYM_KEEP:
        by_text[r["p_number"]].add(r["target"])
        meta[r["p_number"]] = r
pairs = collections.Counter()
for p, s in by_text.items():
    for a in sorted(s):
        for b in sorted(s):
            if a < b: pairs[(a, b)] += 1
print(f"\n{len(by_text)} texts name at least one of the four.")
for n in (4, 3, 2, 1):
    k = [p for p, s in by_text.items() if len(s) == n]
    print(f"   {len(k):>4} texts name exactly {n}")
print("\npairwise co-occurrence, in texts:")
for (a, b), n in pairs.most_common():
    print(f"   {n:>4}  {a} + {b}")
print("\ntexts naming three or more:")
for p, s in sorted(by_text.items()):
    if len(s) >= 3:
        m = meta[p]
        print(f"   {p}  {sorted(s)}  {m['cdli_period']} | {m['cdli_provenience']} | {m['cdli_collection'][:44]}")

print("\n" + "=" * 78)
print("EARLIEST — the oldest CDLI period label carrying each target")
for t in TOP + MAT:
    keep = TOPONYM_KEEP if t in TOP else STONE_KEEP
    best = None
    for r in rows:
        if r["target"] != t or r["classification"] not in keep: continue
        k = period_key(r["cdli_period"])
        if k == 1: continue
        if best is None or k < best[0]: best = (k, r)
    if best:
        r = best[1]
        print(f"\n{t}: {r['cdli_period']}")
        print(f"   {r['p_number']} {r['cdli_provenience']} | {r['cdli_collection'][:56]}")
        print(f"   {r['raw_token']}   line: {r['line'][:120]}")
