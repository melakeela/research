#!/usr/bin/env python3
"""
Does the retrieved cognate-coded Dravidian data support a North Dravidian
subgroup - Brahui, Kurukh, Malto - as against every other grouping of the same
size in the same dataset?

Written for 03-REGISTERS/domain-m-brahui-position.csv, claims DMB-017 to DMB-022.

WHAT THIS SCRIPT CANNOT SEE, per the BF-001 control:

  * It measures EXCLUSIVELY SHARED COGNATE SETS. That is not the same thing as
    a shared innovation. A cognate set found in exactly Brahui, Kurukh and
    Malto is equally consistent with (a) a lexical innovation in their common
    ancestor and (b) a Proto-Dravidian retention lost in the other seventeen.
    Subgrouping arguments require (a) and this instrument cannot distinguish
    them. Every number below is an UPPER BOUND on candidate lexical
    innovations, never a count of them.
  * It sees lexicon only. Krishnamurti's own North Dravidian argument is
    phonological and morphological. Those data are not in this dataset and
    were not retrievable (HOLD-002, and the source itself is unread: IH-237).
  * The cognate judgements are expert coding by scholars who knew the
    conventional classification, and DravLex's own bibliography names
    Krishnamurti 2003 as a source. The instrument is therefore NOT independent
    of the hypothesis it is being used to test. This is a source-genealogy
    dependency in the step-5 sense and is recorded in 02-SOURCES/dependency.csv.
  * A 100-item wordlist. Absence of a cognate set from a language is
    NOT PRODUCED by the list, not evidence of absence from the language.
  * Coverage is unequal (Kuwi 56 concepts, Ollari_Gadba 59, Parji 64). Raw
    exclusive-sharing counts favour groups of well-covered languages, so every
    count is reported alongside its coverage denominator.

Source: SRC-049 (lexibank/dravlex at 37578075e5ccb09c43022f7f1282125e748de84d).
"""
import csv, itertools, collections, os, sys, hashlib, urllib.request, tempfile

# DravLex pinned to the commit recorded in the ledger row SRC-049 and in
# 02-SOURCES/dravlex-glottolog-manifest-2026-09-07.md. Set DRAVLEX_DIR to a
# local checkout to skip the fetch; otherwise the two files are pulled from
# that exact commit and their sha256 verified before anything is counted.
PIN = "37578075e5ccb09c43022f7f1282125e748de84d"
RAW = "https://raw.githubusercontent.com/lexibank/dravlex/" + PIN + "/cldf/"
SHA = {
    "forms.csv":    "c1b2c7f02cdddd6cfab67373d7eb50b6e27ddb592070b83de3a128899d055fde",
    "cognates.csv": "1eb8b6ddc6d07106c509ba38e601a2e18a65a1779336e8b6d47fb0996aff4c48",
}

def dravlex_dir():
    d = os.environ.get("DRAVLEX_DIR")
    if d and all(os.path.exists(os.path.join(d, f)) for f in SHA):
        return d
    d = os.path.join(tempfile.gettempdir(), "dravlex-" + PIN[:12])
    os.makedirs(d, exist_ok=True)
    for f in SHA:
        path = os.path.join(d, f)
        if not os.path.exists(path):
            sys.stderr.write("fetching %s from %s\n" % (f, PIN[:12]))
            urllib.request.urlretrieve(RAW + f, path)
        got = hashlib.sha256(open(path, "rb").read()).hexdigest()
        if got != SHA[f]:
            raise SystemExit("sha256 mismatch for %s: expected %s got %s"
                             % (f, SHA[f], got))
    return d

SP = dravlex_dir()

forms = list(csv.DictReader(open(os.path.join(SP, "forms.csv"), encoding="utf-8")))
LANGS = sorted({f["Language_ID"] for f in forms})
NORTH = ("Brahui", "Kurukh", "Malto")

def report(t):
    print("\n" + "=" * 78); print(t); print("=" * 78)

# concept coverage, and cognate set -> languages
concepts   = collections.defaultdict(set)          # lang -> {concept}
cset_langs = collections.defaultdict(set)          # cognateset -> {lang}
cset_conc  = {}
loanforms  = collections.Counter()
for f in forms:
    concepts[f["Language_ID"]].add(f["Parameter_ID"])
    if f["Loan"] == "true":
        loanforms[f["Language_ID"]] += 1
    if f["Cognacy"]:
        cset_langs[f["Cognacy"]].add(f["Language_ID"])
        cset_conc[f["Cognacy"]] = f["Parameter_ID"]

report("0. Dataset shape and coverage")
print(f"{len(forms)} forms, {len(LANGS)} varieties, "
      f"{len({f['Parameter_ID'] for f in forms})} concepts, "
      f"{len(cset_langs)} cognate sets")
print(f"\n  {'variety':<15} {'concepts':>9} {'loan-flagged forms':>20}")
for l in LANGS:
    print(f"  {l:<15} {len(concepts[l]):9d} {loanforms[l]:20d}")

# --------------------------------------------------- 1. pairwise sharing rate
report("1. Pairwise cognate-sharing rate, over concepts both varieties attest")
def share_rate(a, b):
    common = concepts[a] & concepts[b]
    if not common: return 0.0, 0, 0
    hit = 0
    for c in common:
        sets_a = {k for k, v in cset_langs.items() if cset_conc[k] == c and a in v}
        sets_b = {k for k, v in cset_langs.items() if cset_conc[k] == c and b in v}
        if sets_a & sets_b: hit += 1
    return hit / len(common), hit, len(common)

# precompute concept -> lang -> sets  (faster)
by_conc = collections.defaultdict(lambda: collections.defaultdict(set))
for k, langs in cset_langs.items():
    for l in langs:
        by_conc[cset_conc[k]][l].add(k)

def share_rate(a, b):
    common = concepts[a] & concepts[b]
    if not common: return 0.0, 0, 0
    hit = sum(1 for c in common if by_conc[c][a] & by_conc[c][b])
    return hit / len(common), hit, len(common)

print("\nBrahui against all nineteen others, ranked:\n")
print(f"  {'variety':<15} {'rate':>8} {'shared':>8} {'common concepts':>17}")
br = sorted(((share_rate("Brahui", l), l) for l in LANGS if l != "Brahui"),
            key=lambda x: -x[0][0])
for (rate, hit, n), l in br:
    mark = "  <- conventional North Dravidian" if l in NORTH else ""
    print(f"  {l:<15} {rate*100:7.1f}% {hit:8d} {n:17d}{mark}")

print("\nKurukh against all nineteen others, top five:\n")
ku = sorted(((share_rate("Kurukh", l), l) for l in LANGS if l != "Kurukh"),
            key=lambda x: -x[0][0])[:5]
for (rate, hit, n), l in ku:
    mark = "  <- conventional North Dravidian" if l in NORTH else ""
    print(f"  {l:<15} {rate*100:7.1f}% {hit:8d} {n:17d}{mark}")

print("\nMalto against all nineteen others, top five:\n")
ma = sorted(((share_rate("Malto", l), l) for l in LANGS if l != "Malto"),
            key=lambda x: -x[0][0])[:5]
for (rate, hit, n), l in ma:
    mark = "  <- conventional North Dravidian" if l in NORTH else ""
    print(f"  {l:<15} {rate*100:7.1f}% {hit:8d} {n:17d}{mark}")

allpairs = sorted(((share_rate(a, b)[0], (a, b))
                   for a, b in itertools.combinations(LANGS, 2)), key=lambda x: -x[0])
print(f"\nAll 190 pairs by sharing rate. Rank of the three North Dravidian pairs:")
for i, (r, p) in enumerate(allpairs, 1):
    if set(p) <= set(NORTH):
        print(f"  rank {i:3d}/190  {p[0]}-{p[1]:<10} {r*100:5.1f}%")
print(f"  median pair rate {allpairs[len(allpairs)//2][0]*100:.1f}%   "
      f"top pair {allpairs[0][1]} {allpairs[0][0]*100:.1f}%   "
      f"bottom pair {allpairs[-1][1]} {allpairs[-1][0]*100:.1f}%")

# ------------------------------------------------ 2. exclusive sharing, pairs
report("2. Exclusively shared cognate sets - pairs")
print("A set counts if BOTH members attest it and NO other variety does.")
print("Upper bound on candidate shared lexical innovations, not a count of them.\n")
def exclusive(group):
    g = set(group)
    return [k for k, v in cset_langs.items() if v == g]
pair_ex = sorted(((len(exclusive(p)), p) for p in itertools.combinations(LANGS, 2)),
                 key=lambda x: -x[0])
print("  top ten pairs:")
for n, p in pair_ex[:10]:
    mark = "  <- North Dravidian" if set(p) <= set(NORTH) else ""
    print(f"    {n:3d}  {p[0]}-{p[1]}{mark}")
print("\n  the three North Dravidian pairs:")
for n, p in pair_ex:
    if set(p) <= set(NORTH):
        rank = [i for i, (m, q) in enumerate(pair_ex, 1) if q == p][0]
        print(f"    {n:3d}  {p[0]}-{p[1]:<10} rank {rank}/190")

# ---------------------------------------------- 3. exclusive sharing, triples
report("3. Exclusively shared cognate sets - triples (all 1140)")
tri = sorted(((len(exclusive(t)), t) for t in itertools.combinations(LANGS, 3)),
             key=lambda x: -x[0])
print("  top twelve triples:")
for n, t in tri[:12]:
    mark = "  <- North Dravidian" if set(t) == set(NORTH) else ""
    print(f"    {n:3d}  {'-'.join(t)}{mark}")
nd = [(n, t) for n, t in tri if set(t) == set(NORTH)][0]
rank = [i for i, (m, q) in enumerate(tri, 1) if set(q) == set(NORTH)][0]
print(f"\n  Brahui-Kurukh-Malto: {nd[0]} exclusively shared sets, "
      f"rank {rank} of 1140")
ties = sum(1 for n, t in tri if n == nd[0])
print(f"  {ties} of the 1140 triples have the same count ({nd[0]}).")
print(f"  {sum(1 for n,t in tri if n > nd[0])} triples score higher.")
print(f"  Median triple: {tri[len(tri)//2][0]}.  Top triple: {tri[0][0]}.")

# coverage-controlled: how many concepts do all three attest?
def common_concepts(group):
    s = None
    for l in group:
        s = concepts[l] if s is None else s & concepts[l]
    return s
print(f"\n  Coverage control. Concepts attested by all of Brahui, Kurukh, Malto: "
      f"{len(common_concepts(NORTH))}")
print("  Triples ranked by exclusive sets per 100 commonly attested concepts:")
norm = sorted(((len(exclusive(t)) / max(len(common_concepts(t)), 1) * 100, t,
                len(exclusive(t)), len(common_concepts(t)))
               for t in itertools.combinations(LANGS, 3)), key=lambda x: -x[0])
for r, t, n, c in norm[:8]:
    mark = "  <- North Dravidian" if set(t) == set(NORTH) else ""
    print(f"    {r:5.2f} per 100  ({n}/{c})  {'-'.join(t)}{mark}")
ndn = [(r, t, n, c) for r, t, n, c in norm if set(t) == set(NORTH)][0]
ndrank = [i for i, (r, t, n, c) in enumerate(norm, 1) if set(t) == set(NORTH)][0]
print(f"\n    Brahui-Kurukh-Malto: {ndn[0]:.2f} per 100 ({ndn[2]}/{ndn[3]}), "
      f"rank {ndrank} of 1140")

# ------------------------------- 4. does Brahui attach to Kurukh-Malto at all?
report("4. Does Brahui attach to the Kurukh-Malto unit?")
km = exclusive(("Kurukh", "Malto"))
bkm = exclusive(NORTH)
print(f"  Kurukh+Malto exclusively           : {len(km)} sets")
print(f"  Brahui+Kurukh+Malto exclusively    : {len(bkm)} sets")
print(f"  Brahui+Kurukh exclusively          : {len(exclusive(('Brahui','Kurukh')))} sets")
print(f"  Brahui+Malto exclusively           : {len(exclusive(('Brahui','Malto')))} sets")
print("\n  The Glottolog tree (SRC-051) is North Dravidian -> {Brahui, Kurux-Malto},")
print("  i.e. Brahui is a PRIMARY branch and Kurukh-Malto a unit below it. On")
print("  that tree the diagnostic quantity for the top node is the third line")
print("  above, and for the lower node the first line.")
if bkm:
    print("\n  The Brahui-Kurukh-Malto exclusive sets, by concept:")
    for k in bkm:
        ex = [f["Form"] for f in forms if f["Cognacy"] == k]
        print(f"    {cset_conc[k]:<18} set {k:<8} forms: {', '.join(ex)}")

# how many sets does Brahui share with ANY other language at all
brsets = {k for k, v in cset_langs.items() if "Brahui" in v}
alone  = {k for k in brsets if cset_langs[k] == {"Brahui"}}
print(f"\n  Brahui cognate sets total          : {len(brsets)}")
print(f"  ...of which Brahui-only (singleton) : {len(alone)} "
      f"({len(alone)/len(brsets)*100:.0f}%)")
sing = {l: len([k for k, v in cset_langs.items() if v == {l}]) /
           max(len([k for k, v in cset_langs.items() if l in v]), 1) * 100
        for l in LANGS}
print("  Singleton share for every variety, ranked:")
for l in sorted(LANGS, key=lambda x: -sing[x]):
    mark = "  <-" if l in NORTH else ""
    print(f"    {l:<15} {sing[l]:5.1f}%{mark}")
