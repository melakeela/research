#!/usr/bin/env python3
"""
Domain E, step 13: check MelaKeela against this unit's sources.

The site ships dedr_roots.json - DEDR entry numbers per Dravidian language -
and the-northwest-cousin.html publishes figures computed from it, including
"191 of Brahui's 262 recorded roots have Tamil cognates".

Those figures come from a DIFFERENT digitization of the same dictionary.
RERUN.md line 25 names the site's source as
github.com/ArimeKannada/Dictionary (Files/Language.xlsx). This unit's DEDR
came through JAMBU, which re-parses the DSAL digitization (SRC-056).
Print is unreachable from either (SRC-051), so neither can be adjudicated.

This script measures how far apart they are. It is not an accusation that
the site is wrong: the site's arithmetic reproduces exactly from its own
data. It measures how much a count over any single DEDR digitization can
be trusted, which turns out to be less than the decimal places suggest.

Usage: domain-e-dedr-digitisation-check.py [SITE_JSON] [JAMBU_DEDR_CSV] [OUT_CSV]
"""
import json, csv, sys, collections

SITE  = sys.argv[1] if len(sys.argv) > 1 else "/home/user/site/dedr_roots.json"
JAMBU = sys.argv[2] if len(sys.argv) > 2 else "/tmp/jambu/data/dedr/dedr_new.csv"
OUT   = sys.argv[3] if len(sys.argv) > 3 else "domain-e-dedr-digitisation-check.csv"

# Only labels that correspond one-to-one. Gadba/Gadaba, Brahui/Brah, Gondi
# and Koraga are excluded from the aggregate because JAMBU splits the last
# two into dialect sub-labels: a difference in labelling is not a
# disagreement about the dictionary, and mixing the two would manufacture a
# result. Brahui is reported separately because the site publishes a figure
# from it.
MAP = {"Tamil": "Tam", "Malayalam": "Mal", "Kota": "Kota", "Toda": "Toda",
       "Kannaḍa": "Kannada", "Koḍagu": "Kodagu", "Tulu": "Tulu",
       "Telugu": "Telugu", "Kolami": "Kolami", "Naikṛi": "Naikri",
       "Parji": "Parji", "Konḍa": "Konda", "Pengo": "Pengo", "Kui": "Kui",
       "Kuwi": "Kuwi", "Kuṛux": "Kurux", "Malto": "Malto", "Manḍa": "Manda"}

site = json.load(open(SITE))
ret = collections.defaultdict(set)
for r in csv.reader(open(JAMBU)):
    if len(r) < 3:
        continue
    n = r[1][1:]
    if n.isdigit():
        ret[r[0]].add(int(n))

rows, so, ro, sh = [], 0, 0, 0
for s_lab, j_lab in MAP.items():
    s, j = set(site[s_lab]), ret[j_lab]
    a, b, c = len(s - j), len(j - s), len(s & j)
    so, ro, sh = so + a, ro + b, sh + c
    rows.append([s_lab, j_lab, len(s), len(j), a, b, c,
                 round(100.0 * (a + b) / max(1, a + b + c), 1)])

# Brahui, reported separately, plus the site's published derived figure.
sb, jb = set(site["Brahui"]), ret["Brah"]
st, jt = set(site["Tamil"]), ret["Tam"]

with open(OUT, "w", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(["site_label", "jambu_label", "site_entries", "jambu_entries",
                "site_only", "jambu_only", "shared", "disagreement_pct"])
    w.writerows(rows)
    w.writerow(["Brahui", "Brah", len(sb), len(jb), len(sb - jb), len(jb - sb),
                len(sb & jb), round(100.0 * (len(sb - jb) + len(jb - sb)) / len(sb | jb), 1)])
    w.writerow(["TOTAL (18 mapped languages)", "", "", "", so, ro, sh,
                round(100.0 * (so + ro) / (so + ro + sh), 1)])
    w.writerow(["Brahui roots with a Tamil cognate", "site data", len(sb & st),
                f"{round(100.0*len(sb&st)/len(sb))}%", "jambu data", len(jb & jt),
                f"{round(100.0*len(jb&jt)/len(jb))}%",
                "site publishes 191 of 262 = 73%"])

for r in rows:
    print(f"  {r[0]:<12} site {r[2]:>5}  jambu {r[3]:>5}  disagree {r[7]:>5}%")
print(f"\n  TOTAL over 18 languages: {round(100.0*(so+ro)/(so+ro+sh),1)}% disagreement")
print(f"  Brahui: site {len(sb)} / jambu {len(jb)}; Tamil-cognate roots "
      f"{len(sb&st)} ({round(100.0*len(sb&st)/len(sb))}%) vs "
      f"{len(jb&jt)} ({round(100.0*len(jb&jt)/len(jb))}%)")
print(f"\n-> {OUT}")
