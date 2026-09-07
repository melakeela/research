#!/usr/bin/env python3
"""
Domain E, measurement 3: the geography gate, in kilometres.

Constitution step 3 requires evidenced locations before any comparison,
and IH-033 records that the programme's Para-Munda failure was in part a
geography failure. That is testable rather than assertable: the retrieved
language table carries Glottolog coordinates and a clade label for 408
lects, so the distance from each family's nearest attested member to the
northwest can be computed instead of described.

What this measures: the ATTESTED modern distribution. Constitution §4.P
forbids converting modern areal distribution automatically into
prehistoric substrate, and this script does not do so; it establishes
where the families are recorded, which is the starting point of the gate,
not its conclusion.

"The northwest" is operationalised as the set of lects the same table
assigns to the clades of the Punjab, Sindh, Kashmir, Kohistan, Chitral,
the Kunar and Nuristan — Turner's and Glottolog's grouping, not ours.
Proto-nodes are excluded from the attested figures: a reconstructed
protolanguage has no location, only a hypothesis about one.

Source: SRC-060 (JAMBU cldf/languages.csv).
Usage: domain-e-geography.py [JAMBU_CLDF_DIR] [OUT_CSV]
"""
import csv, sys, math

CLDF = sys.argv[1] if len(sys.argv) > 1 else "/tmp/jambu/cldf"
OUT  = sys.argv[2] if len(sys.argv) > 2 else "domain-e-geography.csv"

DRAVIDIAN = {"S. Dravidian I", "S. Dravidian II", "C. Dravidian",
             "N. Dravidian", "Old Dravidian", "Brahui"}
MUNDA = {"Munda"}
NORTHWEST = {"Kohistani", "Shinaic", "Sindhic", "Lahndic", "Punjabic",
             "Kashmiric", "Kunar", "Chitrali", "Nuristani", "Pashai"}


def gc(a, b):
    la1, lo1, la2, lo2 = (math.radians(float(x)) for x in
                          (a["Latitude"], a["Longitude"], b["Latitude"], b["Longitude"]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371.0 * 2 * math.asin(math.sqrt(h))


rows = [r for r in csv.DictReader(open(f"{CLDF}/languages.csv")) if r["Latitude"]]
nw = [r for r in rows if r["Clade"] in NORTHWEST]


def attested(clades):
    return [r for r in rows if r["Clade"] in clades
            and not r["Name"].startswith("Proto")
            and r["Name"] not in ("Austroasiatic",)]


out = []
for fam, clades in (("Dravidian", DRAVIDIAN), ("Munda", MUNDA)):
    sel = attested(clades)
    d = sorted(((min(gc(s, n) for n in nw), s["Name"], s["Clade"]) for s in sel))
    lons = [float(s["Longitude"]) for s in sel]
    lats = [float(s["Latitude"]) for s in sel]
    out.append((f"GEO-{fam[:2].upper()}-01", fam, "attested lects with coordinates",
                len(sel), "", ""))
    out.append((f"GEO-{fam[:2].upper()}-02", fam, "longitude envelope (degrees E)",
                f"{min(lons):.2f}..{max(lons):.2f}", "", ""))
    out.append((f"GEO-{fam[:2].upper()}-03", fam, "latitude envelope (degrees N)",
                f"{min(lats):.2f}..{max(lats):.2f}", "", ""))
    out.append((f"GEO-{fam[:2].upper()}-04", fam,
                "great-circle km from the nearest attested member to the nearest northwestern lect",
                round(d[0][0]), d[0][1], d[0][2]))
    out.append((f"GEO-{fam[:2].upper()}-05", fam,
                "same, with the single nearest member removed",
                round(d[1][0]), d[1][1], d[1][2]))
    out.append((f"GEO-{fam[:2].upper()}-06", fam, "five nearest members (km)",
                "; ".join(f"{n} {k:.0f}" for k, n, _ in d[:5]), "", ""))

with open(OUT, "w", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(["geo_id", "family", "quantity", "value", "nearest_lect", "clade"])
    w.writerows(out)

for r in out:
    print(f"  {r[0]:<12} {r[1]:<10} {str(r[3]):<26} {r[2][:62]}")
print(f"\n-> {OUT}")
