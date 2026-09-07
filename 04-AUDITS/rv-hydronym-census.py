#!/usr/bin/env python3
"""
Census of Rigvedic river names, for step 3 (geography) of domain E.

Why a name list and not a gloss filter: the Zurich/Grassmann lemma layer
does not carry a hydronym category, and several river names are
lemmatised under an appellative or an adjective rather than under
themselves --

    sárasvatī  ->  lemma sárasvant-   (the masculine stem)
    asiknyā́   ->  lemma ásita-       ('black')

-- so a search over lemma names alone silently loses them. This script
therefore matches ACCENT-STRIPPED SURFACE FORMS against an explicit,
auditable list of candidate hydronym stems, and prints every hit with its
lemma so that each can be confirmed or rejected by hand. False positives
are expected and are removed in the register, not here; the point of the
script is recall.

Input:  rv_tokens_vedaweb.tsv (SRC-019/022/023/047)
Output: rv_hydronyms.tsv, one row per candidate occurrence.
"""
import csv, sys, unicodedata, collections

IN  = sys.argv[1] if len(sys.argv) > 1 else "rv_tokens_vedaweb.tsv"
OUT = sys.argv[2] if len(sys.argv) > 2 else "rv_hydronyms.tsv"

# (search key, conventional name, note). Keys are accent-stripped stems.
NAMES = [
    ("gang",       "Gaṅgā",       "Ganges; the key also catches the derivative gā́ṅgya-"),
    ("yamun",      "Yamunā",      "Jamuna"),
    ("sutudri",    "Śutudrī",     "Sutlej, oblique stem"),
    ("sarasvat",   "Sarasvatī",   "lemmatised under sárasvant-"),
    ("sutudr",     "Śutudrī",     "Sutlej"),
    ("vipas",      "Vipāś",       "Beas"),
    ("vipat",      "Vipāś",       "nom. sg. vipā́ṭ"),
    ("parusn",     "Paruṣṇī",     "Ravi"),
    ("asikn",      "Asiknī",      "Chenab; lemmatised under ásita-"),
    ("marudvrdh",  "Marudvṛdhā",  ""),
    ("vitast",     "Vitastā",     "Jhelum"),
    ("arjik",      "Ārjīkīyā",    "also an adjective/region name"),
    ("susom",      "Suṣomā",      "Sohan"),
    ("trstam",     "Tṛṣṭāmā",     ""),
    ("susart",     "Susartu",     ""),
    ("rasa",       "Rasā",        "mythical stream; also rása- 'sap'"),
    ("svety",      "Śvetyā",      "also the adjective śvetá- 'white'"),
    ("kubha",      "Kubhā",       "Kabul river"),
    ("gomat",      "Gomatī",      "also the adjective gómant-"),
    ("krumu",      "Krumu",       "Kurram"),
    ("mehatn",     "Mehatnū",     ""),
    ("sindhu",     "Sindhu",      "Indus; also the appellative 'river'"),
    ("drsadvat",   "Dṛṣadvatī",   ""),
    ("apaya",      "Āpayā",       ""),
    ("sarayu",     "Sarayu",      ""),
    ("anitabh",    "Anitabhā",    ""),
    ("sipha",      "Śiphā",       ""),
    ("kusava",     "Kuṣavā",      ""),
    ("vibal",      "Vibālī",      ""),
    ("silamavat",  "Silamāvatī",  ""),
    ("hariyup",    "Hariyūpīyā",  ""),
    ("yavyavat",   "Yavyāvatī",   ""),
    ("suvast",     "Suvāstu",     "Swat"),
]

KEEP_RING = "̥"

def strip(s):
    d = unicodedata.normalize("NFD", s)
    out = "".join(c for c in d
                  if unicodedata.category(c) != "Mn" or c == KEEP_RING)
    return unicodedata.normalize("NFC", out).replace(KEEP_RING, "").lower()

def main():
    rows = list(csv.DictReader(open(IN, encoding="utf-8"), delimiter="\t"))
    hits = []
    for r in rows:
        sfc = strip(r["surface"])
        for key, name, note in NAMES:
            if sfc.startswith(key):
                hits.append((name, key, note, r))
                break
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\t".join(["name","key","stanza","pada","tok_i","surface",
                           "lemma","morph","book","stratum","note"]) + "\n")
        for name, key, note, r in sorted(
                hits, key=lambda h: (h[0], h[3]["stanza"], h[3]["pada"])):
            f.write("\t".join([name, key, r["stanza"], r["pada"], r["tok_i"],
                               r["surface"], r["lemma"], r["morph"],
                               r["book"], r["stratum"], note]) + "\n")
    c = collections.Counter(h[0] for h in hits)
    for name, n in sorted(c.items(), key=lambda x: -x[1]):
        print("%-14s %4d" % (name, n))
    print("total candidate occurrences: %d" % len(hits))

if __name__ == "__main__":
    main()
