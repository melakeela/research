#!/usr/bin/env python3
"""
domain-m-dedr-north-dravidian.py

Measures exclusive cognate-set sharing among Brahui, Kurux and Malto in the
Dravidian Etymological Dictionary (Burrow & Emeneau), and tests the observed
counts against a null that holds both entry size and per-language attestation
frequency fixed.

WHY THIS SCRIPT EXISTS
----------------------
PR #16 measured North Dravidian on DravLex, a 100-concept Swadesh-style
wordlist, and said in its own header that this was the wrong instrument: the
conventional case for the subgroup is phonological and morphological, and a
100-concept list cannot carry it. HOLD-004 named DEDR as the blocked source.

DEDR is still blocked at its own publisher (dsal.uchicago.edu, 403 at CONNECT).
What is reachable is a re-encoding of it inside the Jambu database
(github.com/moli-mandala/data), and GitHub is the one host that answers.
This is a DERIVED copy, not the original. Every dependency that follows from
that is recorded in 02-SOURCES/dependency.csv; see DEP-009, DEP-010, DEP-011.

WHAT THIS DOES NOT DO
---------------------
It does not measure phonological or morphological innovations, which is what
the subgroup is actually argued from. DEDR is a lexical instrument too — a much
larger and family-wide one than DravLex, but still lexical. HOLD-004 stays open
on Krishnamurti 2003 for that reason.

It also does not measure loanword strata. This re-encoding carries DEDR's
form and gloss fields only, not its notes, so Balochi and Indo-Aryan loan
annotations are absent from it. That absence is typed in the register; it is
a property of the encoding, not of DEDR.

SELF-FETCHING
-------------
Run with no arguments and it clones the pinned source into a scratch
directory. Pass --repo PATH to point at an existing clone.
"""
import argparse
import collections
import csv
import itertools
import json
import os
import random
import re
import subprocess
import sys
import tempfile

REPO_URL = "https://github.com/moli-mandala/data.git"
# The commit this measurement was taken at. A later commit may change the
# numbers; re-pin and re-run rather than assuming they carry over.
PINNED_COMMIT = "dbae3102fe779aa60f5ef03108f7918ab2ede006"

NORTH = ("Brahui", "Kurux", "Malto")
# DEDR's reconstruction pseudo-language. It is Burrow & Emeneau's own
# reconstruction, not an attested variety, and including it would make every
# entry it appears in look wider than its attestation.
PSEUDO = {"PDr."}

# Line shape of the DEDR dump: rowid, entry number, language code, 'Language'.
DEDR_LINE = re.compile(r"^(\d+),\s*(\d+),\s*(\d+),\s*'([^']*)',")
# Line shape of the CDIAL dump: language, entry, form, ...
CDIAL_LINE = re.compile(r"^([^,]*),\s*(\d+[a-z]?),")


def fetch(dest):
    print(f"cloning {REPO_URL} -> {dest}", file=sys.stderr)
    subprocess.run(["git", "clone", "--quiet", REPO_URL, dest], check=True)
    subprocess.run(["git", "-C", dest, "checkout", "--quiet", PINNED_COMMIT],
                   check=True)
    return dest


def load_dedr(repo):
    """entry number -> set of attested language names."""
    path = os.path.join(repo, "data", "dedr", "dedr.csv")
    entries = collections.defaultdict(set)
    unparsed = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = DEDR_LINE.match(line)
            if m:
                entries[int(m.group(2))].add(m.group(4))
            else:
                unparsed += 1
    entries = {k: (v - PSEUDO) for k, v in entries.items()}
    entries = {k: v for k, v in entries.items() if v}
    return entries, unparsed


def incidence(entries):
    langs = sorted({l for v in entries.values() for l in v})
    index = {l: i for i, l in enumerate(langs)}
    rows = []
    for _, v in sorted(entries.items()):
        rows.append(frozenset(index[l] for l in v))
    return langs, index, rows


def exclusive_count(rows, target):
    """Entries whose attestation set is exactly `target`."""
    t = frozenset(target)
    return sum(1 for r in rows if r == t)


def confined_count(rows, universe):
    """Entries whose attestation set is a non-empty subset of `universe`."""
    u = frozenset(universe)
    return sum(1 for r in rows if r <= u)


def curveball(rows, rng, swaps):
    """
    Randomise a binary incidence matrix holding BOTH margins fixed: every
    entry keeps its number of attesting languages, and every language keeps
    its number of entries. Strona et al.'s curveball trade.

    This is the null that matters here. Brahui is attested in far fewer DEDR
    entries than Kurux or Malto, so a raw comparison of exclusive-set counts
    would be measuring coverage. Holding the column sums fixed removes that.
    """
    m = [set(r) for r in rows]
    n = len(m)
    done = 0
    while done < swaps:
        i = rng.randrange(n)
        j = rng.randrange(n)
        if i == j:
            continue
        a, b = m[i], m[j]
        shared = a & b
        only_a = list(a - shared)
        only_b = list(b - shared)
        k = min(len(only_a), len(only_b))
        if k == 0:
            continue
        pool = only_a + only_b
        rng.shuffle(pool)
        new_a = set(pool[:len(only_a)])
        new_b = set(pool[len(only_a):])
        m[i] = shared | new_a
        m[j] = shared | new_b
        done += 1
    return [frozenset(s) for s in m]


def permutation_test(rows, statistics, reps, seed, swaps):
    rng = random.Random(seed)
    observed = {name: fn(rows) for name, fn in statistics.items()}
    ge = {name: 0 for name in statistics}
    le = {name: 0 for name in statistics}
    draws = {name: [] for name in statistics}
    for _ in range(reps):
        shuffled = curveball(rows, rng, swaps)
        for name, fn in statistics.items():
            v = fn(shuffled)
            draws[name].append(v)
            if v >= observed[name]:
                ge[name] += 1
            if v <= observed[name]:
                le[name] += 1
    out = {}
    for name in statistics:
        d = sorted(draws[name])
        out[name] = {
            "observed": observed[name],
            "null_mean": sum(d) / len(d),
            "null_min": d[0],
            "null_max": d[-1],
            "null_p05": d[int(0.05 * len(d))],
            "null_p95": d[int(0.95 * len(d))],
            # one-sided exact p-values with the +1 correction
            "p_greater_or_equal": (ge[name] + 1) / (reps + 1),
            "p_less_or_equal": (le[name] + 1) / (reps + 1),
        }
    return out


def cdial_touchpoints(repo, entries):
    """
    Where the two standard comparative dictionaries touch.

    CDIAL (Turner, Indo-Aryan) carries cross-references to DEDR entries. This
    counts how many of those references land on a DEDR entry that has a Brahui
    form in it, against how many land on Kurux or Malto. It measures what the
    Indo-Aryan comparative record says about Brahui, at the only place the two
    dictionaries are joined in this dataset.
    """
    path = os.path.join(repo, "data", "cross-family-comparisons.csv")
    if not os.path.exists(path):
        return None
    csv.field_size_limit(10 ** 7)
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    def dedr_no(cell):
        cell = (cell or "").strip()
        if cell.startswith("d") and cell[1:].isdigit():
            return int(cell[1:])
        return None

    out = {
        "comparison_rows": len(rows),
        "relation": dict(collections.Counter(r["Relation"] for r in rows)),
        "direction": dict(collections.Counter(r["Direction"] for r in rows)),
        "confidence": dict(collections.Counter(r["Confidence"] for r in rows)),
        "resolved_to_dedr_entry": 0,
        "touching_brahui": 0,
        "touching_kurux": 0,
        "touching_malto": 0,
        "touching_any_north": 0,
        "brahui_entry_ids": [],
    }
    for r in rows:
        n = dedr_no(r.get("Compared_Entry_ID"))
        if n is None or n not in entries:
            continue
        out["resolved_to_dedr_entry"] += 1
        langs = entries[n]
        if "Brahui" in langs:
            out["touching_brahui"] += 1
            out["brahui_entry_ids"].append(n)
        if "Kurux" in langs:
            out["touching_kurux"] += 1
        if "Malto" in langs:
            out["touching_malto"] += 1
        if langs & set(NORTH):
            out["touching_any_north"] += 1
    return out


def named_mentions(repo):
    """
    How often the standard Indo-Aryan comparative dictionary names Brahui or
    Balochi at all. This is the search behind the typed absence in the
    register; it is reported as a count so the absence is checkable.
    """
    path = os.path.join(repo, "data", "cdial", "cdial.csv")
    counts = collections.Counter()
    lines = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            lines += 1
            low = line.lower()
            if "brahui" in low:
                counts["Brahui"] += 1
            if "baloch" in low or "baluch" in low:
                counts["Balochi"] += 1
    return {"cdial_lines": lines, "named": dict(counts)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", help="existing clone of moli-mandala/data")
    ap.add_argument("--reps", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20260907)
    ap.add_argument("--swaps", type=int, default=200000)
    ap.add_argument("--json", help="write the full result here")
    args = ap.parse_args()

    repo = args.repo or fetch(tempfile.mkdtemp(prefix="jambu-"))
    entries, unparsed = load_dedr(repo)
    langs, index, rows = incidence(entries)

    report = {
        "source_repo": REPO_URL,
        "pinned_commit": PINNED_COMMIT,
        "dedr_entries": len(entries),
        "dedr_unparsed_lines": unparsed,
        "languages": len(langs),
        "attestation": {l: sum(1 for r in rows if index[l] in r) for l in langs},
    }

    # ---- 1. every exclusive pair and triple, so no rank is reported alone ----
    pair_exclusive = {}
    for a, b in itertools.combinations(langs, 2):
        pair_exclusive[f"{a}|{b}"] = exclusive_count(
            rows, {index[a], index[b]})
    triple_exclusive = {}
    for a, b, c in itertools.combinations(langs, 3):
        triple_exclusive[f"{a}|{b}|{c}"] = exclusive_count(
            rows, {index[a], index[b], index[c]})
    report["pair_exclusive"] = pair_exclusive
    report["triple_exclusive"] = triple_exclusive

    def rank_of(d, key):
        v = d[key]
        higher = sum(1 for x in d.values() if x > v)
        return higher + 1, len(d)

    north_idx = {index[l] for l in NORTH}
    report["north_dravidian"] = {
        "kurux_malto_cooccurring": sum(
            1 for r in rows if {index["Kurux"], index["Malto"]} <= set(r)),
        "kurux_malto_exclusive": pair_exclusive["Kurux|Malto"],
        "brahui_kurux_exclusive": pair_exclusive["Brahui|Kurux"],
        "brahui_malto_exclusive": pair_exclusive["Brahui|Malto"],
        "brahui_kurux_malto_exclusive": triple_exclusive["Brahui|Kurux|Malto"],
        "confined_to_north": confined_count(rows, north_idx),
        "brahui_entries_total": report["attestation"]["Brahui"],
    }
    report["north_dravidian"]["brahui_entries_outside_north"] = (
        report["attestation"]["Brahui"]
        - sum(1 for r in rows if index["Brahui"] in r and set(r) <= north_idx))
    r, n = rank_of(pair_exclusive, "Kurux|Malto")
    report["north_dravidian"]["kurux_malto_rank"] = [r, n]
    r, n = rank_of(triple_exclusive, "Brahui|Kurux|Malto")
    report["north_dravidian"]["brahui_kurux_malto_rank"] = [r, n]

    # ---- 2. the null: both margins fixed ----
    stats = {
        "kurux_malto_exclusive":
            lambda rr: exclusive_count(rr, {index["Kurux"], index["Malto"]}),
        "brahui_kurux_malto_exclusive":
            lambda rr: exclusive_count(rr, north_idx),
        "confined_to_north":
            lambda rr: confined_count(rr, north_idx),
        "brahui_kurux_exclusive":
            lambda rr: exclusive_count(rr, {index["Brahui"], index["Kurux"]}),
        "brahui_malto_exclusive":
            lambda rr: exclusive_count(rr, {index["Brahui"], index["Malto"]}),
    }
    report["permutation"] = {
        "model": "curveball; entry size and language attestation both held fixed",
        "reps": args.reps, "seed": args.seed, "swaps_per_rep": args.swaps,
        "results": permutation_test(rows, stats, args.reps, args.seed, args.swaps),
    }

    # ---- 3. Brahui's partners across the whole family ----
    brahui = index["Brahui"]
    prof = {}
    for l in langs:
        if l == "Brahui":
            continue
        co = sum(1 for r in rows if brahui in r and index[l] in r)
        prof[l] = co
    report["brahui_cooccurrence"] = dict(
        sorted(prof.items(), key=lambda kv: -kv[1]))

    # ---- 4. where CDIAL and DEDR touch ----
    report["cdial_touchpoints"] = cdial_touchpoints(repo, entries)
    report["cdial_named_mentions"] = named_mentions(repo)

    # ---- 5. published counts this run either reproduces or does not ----
    nd = report["north_dravidian"]
    report["published_comparisons"] = {
        "kobayashi_tirkey_2019_kurux_malto_shared_etyma": {
            "published": 515, "measured": nd["kurux_malto_cooccurring"]},
        "kobayashi_tirkey_2019_kurux_malto_isolated": {
            "published": 175, "measured": nd["kurux_malto_exclusive"]},
        "bsoas_review_north_dravidian_list": {
            "published": 195, "measured": nd["confined_to_north"]},
    }

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(text + "\n")

    a = report["attestation"]
    p = report["permutation"]["results"]
    print(f"DEDR entries parsed: {len(entries)}  languages: {len(langs)}  "
          f"unparsed lines: {unparsed}")
    print(f"attested entries — Brahui {a['Brahui']}, Kurux {a['Kurux']}, "
          f"Malto {a['Malto']}")
    print()
    print("exclusive sets (attestation set is exactly this group)")
    print(f"  Kurux+Malto          {nd['kurux_malto_exclusive']:5d}"
          f"   rank {nd['kurux_malto_rank'][0]} of {nd['kurux_malto_rank'][1]} pairs")
    print(f"  Brahui+Kurux         {nd['brahui_kurux_exclusive']:5d}")
    print(f"  Brahui+Malto         {nd['brahui_malto_exclusive']:5d}")
    print(f"  Brahui+Kurux+Malto   {nd['brahui_kurux_malto_exclusive']:5d}"
          f"   rank {nd['brahui_kurux_malto_rank'][0]} of "
          f"{nd['brahui_kurux_malto_rank'][1]} triples")
    print(f"  confined to North Dr {nd['confined_to_north']:5d}")
    print(f"  Brahui entries whose reach goes outside North Dravidian: "
          f"{nd['brahui_entries_outside_north']} of {a['Brahui']}")
    print()
    print("null: curveball, both margins fixed")
    for k, v in p.items():
        print(f"  {k:32s} obs {v['observed']:5d}  null mean "
              f"{v['null_mean']:8.2f}  [{v['null_p05']}, {v['null_p95']}]  "
              f"p(>=obs) {v['p_greater_or_equal']:.4f}")
    print()
    print("published counts this run tried to reproduce")
    for k, v in report["published_comparisons"].items():
        print(f"  {k:52s} published {v['published']:4d}  measured {v['measured']:4d}")
    print()
    ct = report["cdial_touchpoints"]
    print(f"CDIAL<->DEDR cross-references: {ct['comparison_rows']} rows, "
          f"{ct['resolved_to_dedr_entry']} resolve to a DEDR entry here")
    print(f"  touching a Brahui-bearing entry: {ct['touching_brahui']}")
    print(f"  touching Kurux: {ct['touching_kurux']}   "
          f"Malto: {ct['touching_malto']}   any North Dravidian: "
          f"{ct['touching_any_north']}")
    print(f"CDIAL lines naming Brahui/Balochi: "
          f"{report['cdial_named_mentions']['named']} "
          f"of {report['cdial_named_mentions']['cdial_lines']} lines")


if __name__ == "__main__":
    main()
