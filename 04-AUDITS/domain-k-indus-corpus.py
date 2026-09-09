#!/usr/bin/env python3
"""
Measure the one machine-readable Indus corpus reachable from this session,
and the sign-list crosswalk that ships with it.

Source: mayig/indus-valley-script-corpus @ ad2f1e218a34b8c33c57de0d6cb8d99272765bbb
        corpus/*/*.json  (SRC-102)   features/*.json  (SRC-103)
Ledger: SRC-101, SRC-102, SRC-103; dependency DEP-029, DEP-030

WHAT THIS SCRIPT MEASURES, AND WHAT IT DOES NOT

It measures the contents of a digitization. It does not measure the Indus
corpus. The digitization is one annotator's work in progress, transcribed
from the Corpus of Indus Seals and Inscriptions (Parpola et al.), which is
not retrievable in this session (SRC-109, SRC-111, DEP-029). Every number
printed here is a property of the file set, and the register rows that
carry these numbers say so in their own text rather than in a footnote.

Two conventions of the source are preserved rather than corrected:

  * Graphemes are stored left-to-right as they stand on the object. The
    README states the script is read right-to-left. This script reports
    positions in STORED order and additionally reports the mirrored index,
    and never silently applies a reading direction.
  * Each grapheme's feature vector begins with three default features -
    damage, line, uncertainty - followed by the sign-specific features
    declared in features/<id>.json. The script validates that invariant
    instead of assuming it.

Usage: domain-k-indus-corpus.py CLONE_ROOT [OUT_PREFIX]
Writes OUT_PREFIX-signs.csv (one row per sign type) and prints a report.
"""
import sys, os, json, glob, re, csv, collections, statistics

root = sys.argv[1] if len(sys.argv) > 1 else "."
out = sys.argv[2] if len(sys.argv) > 2 else "domain-k"

sides = []
for f in sorted(glob.glob(os.path.join(root, "corpus", "*", "*.json"))):
    for s in json.load(open(f)):
        s["_file"] = os.path.relpath(f, root)
        sides.append(s)

schema = {}
for f in sorted(glob.glob(os.path.join(root, "features", "*.json"))):
    d = json.load(open(f))
    schema[d["id"]] = d

R = {}
R["side_records"] = len(sides)
R["artefact_files"] = len(set(s["_file"] for s in sides))
R["distinct_object_ids"] = len(set(s["id"] for s in sides))

# --- catalogue coverage -----------------------------------------------
num = re.compile(r"^M-(\d+)([A-Za-z]*)$")
nums, suffixes = [], collections.Counter()
for s in sides:
    m = num.match(s["id"])
    if not m:
        raise SystemExit("unexpected object id: " + s["id"])
    nums.append(int(m.group(1)))
    suffixes[m.group(2)] += 1
R["cisi_min"], R["cisi_max"] = min(nums), max(nums)
R["cisi_gaps_in_range"] = sorted(set(range(min(nums), max(nums) + 1)) - set(nums))
R["side_suffixes"] = dict(suffixes)

# --- object types as the digitizer described them ----------------------
R["descriptions"] = collections.Counter(s.get("description", "") for s in sides)

# --- text length -------------------------------------------------------
lens = [len(s["graphemes"]) for s in sides]
R["sign_tokens"] = sum(lens)
R["len_mean"] = round(statistics.mean(lens), 2)
R["len_median"] = statistics.median(lens)
R["len_min"], R["len_max"] = min(lens), max(lens)
R["len_hist"] = dict(sorted(collections.Counter(lens).items()))

# --- sign inventory ----------------------------------------------------
# P000 is not a sign. features/P000.json describes it as "Represents a
# section of significant damage or lost material", so it is a placeholder
# for what could not be read. Totals are reported both ways: with it, which
# is what a naive count of the file gives, and without it, which is what a
# count of signs gives.
DAMAGE_MARKER = "P000"
freq = collections.Counter()
docfreq = collections.Counter()
first_stored, last_stored = collections.Counter(), collections.Counter()
for s in sides:
    gs = s["graphemes"]
    for g in gs:
        freq[g["id"]] += 1
    docfreq.update({g["id"] for g in gs})
    if gs:
        first_stored[gs[0]["id"]] += 1
        last_stored[gs[-1]["id"]] += 1
signs = {k: v for k, v in freq.items() if k != DAMAGE_MARKER}
R["damage_marker_tokens"] = freq.get(DAMAGE_MARKER, 0)
R["damage_marker_records"] = docfreq.get(DAMAGE_MARKER, 0)
R["sign_tokens_excl_marker"] = sum(signs.values())
R["sign_types_incl_marker"] = len(freq)
R["sign_types"] = len(signs)
R["hapax"] = sum(1 for v in signs.values() if v == 1)
R["top_signs_excl_marker"] = collections.Counter(signs).most_common(10)
R["docfreq_top"] = docfreq.most_common(5)
lens_excl = [sum(1 for g in s["graphemes"] if g["id"] != DAMAGE_MARKER) for s in sides]
R["len_mean_excl_marker"] = round(statistics.mean(lens_excl), 2)
R["len_median_excl_marker"] = statistics.median(lens_excl)
R["signlist_entries"] = len(schema)
R["signlist_unused"] = len(set(schema) - set(freq))
R["top_signs"] = freq.most_common(10)
R["first_stored_top"] = first_stored.most_common(5)
R["last_stored_top"] = last_stored.most_common(5)
R["signs_not_in_signlist"] = sorted(set(freq) - set(schema))

# --- default-feature validation and condition coding -------------------
bad = []
damage, uncertainty, line = collections.Counter(), collections.Counter(), collections.Counter()
for s in sides:
    for g in s["graphemes"]:
        f = g["features"]
        if g["id"] in schema:
            expect = len(schema[g["id"]].get("features", [])) + 3
            if len(f) != expect:
                bad.append((s["id"], g["id"], len(f), expect))
        if len(f) >= 3:
            damage[f[0]] += 1
            line[f[1]] += 1
            uncertainty[f[2]] += 1
R["feature_length_mismatches"] = bad
R["damage"] = dict(sorted(damage.items()))
R["line"] = dict(sorted(line.items()))
R["uncertainty"] = dict(sorted(uncertainty.items()))
R["damage_nonzero"] = sum(v for k, v in damage.items() if k)
R["uncertainty_nonzero"] = sum(v for k, v in uncertainty.items() if k)
R["damage_out_of_range"] = {k: v for k, v in damage.items() if k > 100}
R["uncertainty_out_of_range"] = {k: v for k, v in uncertainty.items() if k > 100}

# --- sign-list crosswalk ----------------------------------------------
# Each features/<P>.json declares which Parpola V-numbers, Wells W-numbers
# and Mahadevan M-numbers the annotator folded into that class.
cw = {"parpola_graphemes": collections.Counter(),
      "wells_graphemes": collections.Counter(),
      "mahadevan_graphemes": collections.Counter()}
per_entry = {k: collections.Counter() for k in cw}
empty = {k: [] for k in cw}
for pid, d in schema.items():
    for k in cw:
        vals = d.get(k, []) or []
        per_entry[k][pid] = len(vals)
        if not vals:
            empty[k].append(pid)
        for v in vals:
            cw[k][v] += 1
R["crosswalk"] = {}
for k in cw:
    counts = [per_entry[k][p] for p in schema]
    R["crosswalk"][k] = {
        "distinct_numbers": len(cw[k]),
        "total_references": sum(cw[k].values()),
        "entries_with_none": len(empty[k]),
        "entries_with_one": sum(1 for c in counts if c == 1),
        "entries_with_many": sum(1 for c in counts if c > 1),
        "max_folded_into_one_entry": max(counts),
        "numbers_used_by_more_than_one_entry": sorted(v for v, c in cw[k].items() if c > 1),
    }

# --- per-sign CSV ------------------------------------------------------
with open(out + "-signs.csv", "w", newline="") as fh:
    w = csv.writer(fh, quoting=csv.QUOTE_ALL)
    w.writerow(["parpola_class", "description", "tokens_in_corpus",
                "stored_initial", "stored_final", "parpola_v_numbers",
                "wells_w_numbers", "mahadevan_m_numbers"])
    for pid in sorted(set(schema) | set(freq)):
        d = schema.get(pid, {})
        w.writerow([pid, d.get("description", ""), freq.get(pid, 0),
                    first_stored.get(pid, 0), last_stored.get(pid, 0),
                    " ".join(d.get("parpola_graphemes", []) or []),
                    " ".join(d.get("wells_graphemes", []) or []),
                    " ".join(d.get("mahadevan_graphemes", []) or [])])

for k, v in R.items():
    print(f"{k}: {v}")
