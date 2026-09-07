#!/usr/bin/env python3
"""
Independent re-derivation of PR #22's DEDR measurements.

Written for the adversarial review of domain M
(04-AUDITS/domain-m-adversarial-review-2026-09-07.md) WITHOUT reusing
04-AUDITS/domain-m-dedr-north-dravidian.py: separate parser, separate
curveball, separate statistics. If the two agree, the agreement means
something; if they were the same code it would not.

It answers three questions the review brief posed:

  1. Do the reported counts reproduce?  (They do, exactly, on the file
     the unit measured.)
  2. Does the null preserve both margins, genuinely randomise, and
     discriminate?  (Yes, yes, and yes -- but it has no resolution on the
     three-way statistic: p(>=1) == p(>=7).)
  3. Do the counts survive the choice of encoding?  (No. The Jambu
     repository ships two DEDR encodings. The unit measured the one its
     maintainers deprecated; the one they declare as their provenance
     gives different numbers and a different membership for the seven
     etymologies of DMM-003.)

Usage:
    domain-m-review-rederivation.py --repo PATH [--reps N] [--swaps N]

PATH is a clone of github.com/moli-mandala/data at commit
dbae3102fe779aa60f5ef03108f7918ab2ede006 -- the commit SRC-059 pins.
"""
import argparse
import collections
import csv
import itertools
import random
import re
import statistics
import subprocess
import sys
import tempfile

REPO_URL = "https://github.com/moli-mandala/data.git"
PINNED = "dbae3102fe779aa60f5ef03108f7918ab2ede006"
NORTH = {"Brahui", "Kurux", "Malto"}
PSEUDO = {"PDr."}

# The deprecated encoding is a converted phpMyAdmin dump: positional SQL
# values, single-quoted strings. Parsed here directly rather than through
# the unit's regex, so a shared parsing assumption cannot hide a shared error.
SQL_ROW = re.compile(r"^(\d+),\s*(\d+),\s*(\d+),\s*'((?:[^']|'')*)',")


def fetch(dest):
    subprocess.run(["git", "clone", "--quiet", REPO_URL, dest], check=True)
    subprocess.run(["git", "-C", dest, "checkout", "--quiet", PINNED], check=True)
    return dest


def load_deprecated(repo):
    """data/dedr/dedr.csv -- the file PR #22 measured. Deprecated upstream."""
    entries = collections.defaultdict(set)
    lines = unparsed = 0
    with open(f"{repo}/data/dedr/dedr.csv", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            lines += 1
            m = SQL_ROW.match(line)
            if m:
                entries[int(m.group(2))].add(m.group(4))
            else:
                unparsed += 1
    entries = {k: v - PSEUDO for k, v in entries.items()}
    return {k: v for k, v in entries.items() if v}, lines, unparsed


def load_current(repo):
    """
    data/dedr/dedr_new.csv -- the file cldf/references.csv names as the
    provenance of Jambu's DEDR data. Dialect lects are rolled up to their
    base language through cldf/dialects.csv, so the two encodings are
    compared at the same granularity.
    """
    dialect = {}
    with open(f"{repo}/cldf/dialects.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["Source_Language_ID"]:
                dialect[r["Source_Language_ID"]] = r["Language_ID"]
    base = {"Tam": "Tamil", "Mal": "Malayalam", "Brah": "Brahui",
            "OMal": "Malayalam", "OTelugu": "Telugu", "Or": "Oriya"}
    csv.field_size_limit(10 ** 7)
    entries = collections.defaultdict(set)
    with open(f"{repo}/data/dedr/dedr_new.csv", newline="", encoding="utf-8") as f:
        for r in csv.reader(f):
            if len(r) < 3:
                continue
            code, eid = r[0].strip(), r[1].strip()
            if eid.startswith("d"):
                entries[eid].add(dialect.get(code) or base.get(code, code))
    return entries


def exclusive(entries, target):
    t = frozenset(target)
    return sum(1 for v in entries.values() if frozenset(v) == t)


def confined(entries, universe):
    u = frozenset(universe)
    return sum(1 for v in entries.values() if frozenset(v) <= u)


def counts(entries, label, expected=None):
    langs = sorted({l for v in entries.values() for l in v})
    att = {l: sum(1 for v in entries.values() if l in v) for l in langs}
    out = {
        "entries": len(entries),
        "languages": len(langs),
        "Brahui": att.get("Brahui"), "Kurux": att.get("Kurux"),
        "Malto": att.get("Malto"),
        "kurux_malto_exclusive": exclusive(entries, {"Kurux", "Malto"}),
        "brahui_kurux_exclusive": exclusive(entries, {"Brahui", "Kurux"}),
        "brahui_malto_exclusive": exclusive(entries, {"Brahui", "Malto"}),
        "brahui_kurux_malto_exclusive": exclusive(entries, NORTH),
        "confined_to_north": confined(entries, NORTH),
        "kurux_malto_cooccurring":
            sum(1 for v in entries.values() if {"Kurux", "Malto"} <= set(v)),
    }
    out["brahui_outside_north"] = out["Brahui"] - sum(
        1 for v in entries.values() if "Brahui" in v and set(v) <= NORTH)
    triples = sorted(str(k) for k, v in entries.items()
                     if frozenset(v) == frozenset(NORTH))
    print(f"\n--- {label} ---")
    for k, v in out.items():
        note = ""
        if expected and k in expected:
            note = "  MATCHES PR #22" if expected[k] == v else \
                   f"  <-- PR #22 reports {expected[k]}"
        print(f"  {k:30s} {v}{note}")
    print(f"  {'north-exclusive entry numbers':30s} {triples}")
    return out, triples


def margins(rows, n_lang):
    col = collections.Counter()
    for r in rows:
        col.update(r)
    return sorted(len(r) for r in rows), [col[i] for i in range(n_lang)]


def curveball(rows, rng, swaps):
    """
    Strona et al. trade. Both margins fixed: each entry keeps its number of
    attesting languages, each language keeps its number of entries.
    """
    m = [set(r) for r in rows]
    n = len(m)
    done = 0
    while done < swaps:
        i, j = rng.randrange(n), rng.randrange(n)
        if i == j:
            continue
        a, b = m[i], m[j]
        shared = a & b
        only_a, only_b = list(a - shared), list(b - shared)
        if not only_a or not only_b:
            continue
        pool = only_a + only_b
        rng.shuffle(pool)
        m[i] = shared | set(pool[:len(only_a)])
        m[j] = shared | set(pool[len(only_a):])
        done += 1
    return [frozenset(s) for s in m]


def null_test(entries, reps, swaps, seed):
    langs = sorted({l for v in entries.values() for l in v})
    idx = {l: i for i, l in enumerate(langs)}
    rows = [frozenset(idx[l] for l in v) for _, v in sorted(entries.items())]
    north = frozenset(idx[l] for l in NORTH)
    km = frozenset({idx["Kurux"], idx["Malto"]})
    bk = frozenset({idx["Brahui"], idx["Kurux"]})
    bm = frozenset({idx["Brahui"], idx["Malto"]})

    def stats(rs):
        c = collections.Counter(rs)
        pairs = {p: c[frozenset(p)]
                 for p in itertools.combinations(range(len(langs)), 2)}
        return pairs, c[north], sum(v for k, v in c.items() if k <= north)

    obs_pairs, obs_trip, obs_conf = stats(rows)
    rng = random.Random(seed)
    rs0, cs0 = margins(rows, len(langs))
    draws = collections.defaultdict(list)
    pair_draws = collections.defaultdict(list)
    for rep in range(reps):
        sh = curveball(rows, rng, swaps)
        if rep == 0:
            rs1, cs1 = margins(sh, len(langs))
            print(f"\n--- the null, checked rather than assumed ---")
            print(f"  row-size multiset preserved exactly : {rs0 == rs1}")
            print(f"  every column sum preserved exactly  : {cs0 == cs1}")
            print(f"  rows changed after {swaps} swaps    : "
                  f"{sum(1 for x, y in zip(rows, sh) if x != y)} of {len(rows)}")
        p, t, cf = stats(sh)
        draws["brahui_kurux_malto_exclusive"].append(t)
        draws["confined_to_north"].append(cf)
        for k, v in p.items():
            pair_draws[k].append(v)
    for name, key in (("kurux_malto_exclusive", km),
                      ("brahui_kurux_exclusive", bk),
                      ("brahui_malto_exclusive", bm)):
        k = tuple(sorted(key))
        draws[name] = pair_draws[k]

    print(f"\n--- five statistics, {reps} draws x {swaps} swaps, seed {seed} ---")
    obs = {"kurux_malto_exclusive": obs_pairs[tuple(sorted(km))],
           "brahui_kurux_exclusive": obs_pairs[tuple(sorted(bk))],
           "brahui_malto_exclusive": obs_pairs[tuple(sorted(bm))],
           "brahui_kurux_malto_exclusive": obs_trip,
           "confined_to_north": obs_conf}
    for name, d in draws.items():
        d = sorted(d)
        ge = sum(1 for x in d if x >= obs[name])
        print(f"  {name:30s} obs {obs[name]:4d}  null mean "
              f"{statistics.mean(d):7.3f}  max {d[-1]:3d}  "
              f"[{d[int(.05*len(d))]}, {d[int(.95*len(d))]}]  "
              f"p(>=obs) {(ge+1)/(len(d)+1):.4f}")

    # RESOLUTION. The finding at AR-M-07: this test cannot tell 7 from 1.
    td = sorted(draws["brahui_kurux_malto_exclusive"])
    print("\n--- resolution of the three-way statistic (AR-M-07) ---")
    for h in (1, 2, 3, 7):
        ge = sum(1 for x in td if x >= h)
        print(f"  p(>= {h}) = {(ge+1)/(len(td)+1):.4f}"
              + ("   <-- the observed value" if h == 7 else ""))

    # DISCRIMINATING POWER. The finding at AR-M-13, favourable to the unit.
    print("\n--- discriminating power across all pairs (AR-M-13) ---")
    nonzero = [k for k in obs_pairs if obs_pairs[k] > 0]
    sig = [k for k in obs_pairs
           if (sum(1 for x in pair_draws[k] if x >= obs_pairs[k]) + 1)
           / (reps + 1) <= 0.05]
    print(f"  pairs total {len(obs_pairs)}, non-zero {len(nonzero)}, "
          f"significant at p<=0.05: {len(sig)}")
    for v, k in sorted(((obs_pairs[k], k) for k in sig), reverse=True)[:12]:
        print(f"    {langs[k[0]]:14s} {langs[k[1]]:14s} obs {v:4d}   "
              f"null mean {statistics.mean(pair_draws[k]):7.2f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo")
    ap.add_argument("--reps", type=int, default=500)
    ap.add_argument("--swaps", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=20260907)
    ap.add_argument("--skip-null", action="store_true")
    a = ap.parse_args()
    repo = a.repo or fetch(tempfile.mkdtemp(prefix="jambu-review-"))

    deprecated, lines, unparsed = load_deprecated(repo)
    print(f"data/dedr/dedr.csv: {lines} lines, {unparsed} unparsed by this "
          f"parser  (PR #22 reports 68808 / 0)")

    # PR #22's reported values, for a match/mismatch column.
    reported = {
        "entries": 5520, "languages": 26, "Brahui": 269, "Kurux": 775,
        "Malto": 704, "kurux_malto_exclusive": 176,
        "brahui_kurux_exclusive": 1, "brahui_malto_exclusive": 1,
        "brahui_kurux_malto_exclusive": 7, "confined_to_north": 193,
        "kurux_malto_cooccurring": 509, "brahui_outside_north": 260,
    }
    _, dep_triples = counts(
        deprecated, "DEPRECATED data/dedr/dedr.csv -- the file PR #22 measured",
        reported)
    _, cur_triples = counts(
        load_current(repo),
        "CURRENT data/dedr/dedr_new.csv -- Jambu's declared provenance",
        reported)

    print("\n--- the seven etymologies of DMM-003 (AR-M-02) ---")
    dn = {t.lstrip("d") for t in dep_triples}
    cn = {t.lstrip("d") for t in cur_triples}
    print(f"  in the deprecated encoding only : {sorted(dn - cn)}")
    print(f"  in the current encoding only    : {sorted(cn - dn)}")
    print(f"  in both                         : {sorted(dn & cn)}")

    if not a.skip_null:
        null_test(deprecated, a.reps, a.swaps, a.seed)


if __name__ == "__main__":
    main()
