#!/usr/bin/env python3
"""
Reconstruction of the challenged Brahui leave-one-out geographic measurement,
and measurement of what it can and cannot support.

Written for 03-REGISTERS/domain-m-brahui-position.csv, claims DMB-010 to DMB-016.

WHAT THIS SCRIPT CANNOT SEE, stated in its own header per the BF-001 control:

  * It has no chronological term. Every coordinate is a present-day or
    recent-survey location. Nothing here dates anything.
  * The set of languages is a survival sample, not a sample of past
    distribution. Absence of a point is NOT PRESERVED / NOT PRODUCED in the
    negative-evidence typology, never evidence of past absence.
  * A point coordinate for a language is an editorial simplification. Glottolog
    assigns one latitude/longitude per languoid; real speech communities are
    areas, and several of these are or were far more extensive.
  * It has no term for shared descent. That is objection 2 (DMB-005), and it is
    the reason this script is paired with north-dravidian-cognate-sharing.py
    rather than reported alone.

Sources: SRC-050 (Glottolog CLDF languages.csv, coordinates), SRC-049 (DravLex,
which fixes WHICH twenty varieties are in the set).
"""
import csv, math, sys, json

# ---- the twenty DravLex varieties, with Glottolog coordinates (SRC-049, SRC-050)
# name, glottocode, latitude, longitude
LANGS = [
    ("Badga",         "bada1257", 11.3094,  76.5974),
    ("Betta_Kurumba", "bett1235", 11.6385,  76.6064),
    ("Brahui",        "brah1256", 29.04,    66.56),
    ("Gondi",         "nort2702", 18.1632,  81.3842),
    ("Kannada",       "nucl1305", 13.5878,  76.1198),
    ("Kodava",        "koda1255", 12.2443,  75.9161),
    ("Kolami",        "nort2699", 20.1022,  78.4934),
    ("Kota",          "kota1263", 11.4978,  76.9387),
    ("Koya",          "koya1251", 17.6772,  81.2096),
    ("Kurukh",        "kuru1302", 24.4644,  86.4657),
    ("Kuwi",          "kuvi1243", 18.8832,  83.7552),
    ("Malayalam",     "mala1464",  9.59208, 76.7651),
    ("Malto",         "saur1249", 24.8124,  87.6432),
    ("Ollari_Gadba",  "pott1240", 18.5968,  82.7586),
    ("Parji",         "duru1236", 19.0534,  82.4881),
    ("Tamil",         "tami1289", 10.520219,78.825989),
    ("Telugu",        "telu1262", 16.4529,  78.7024),
    ("Toda",          "toda1252", 11.4184,  77.0168),
    ("Tulu",          "tulu1258", 12.8114,  75.2651),
    ("Yeruva",        "ravu1237", 12.3231,  75.6265),
]

R_EARTH_KM = 6371.0088

def haversine(a, b):
    (la1, lo1), (la2, lo2) = a, b
    p1, p2 = math.radians(la1), math.radians(la2)
    dp, dl = p2 - p1, math.radians(lo2 - lo1)
    h = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2 * R_EARTH_KM * math.asin(math.sqrt(h))

def euclid_deg(a, b):
    """The metric the challenged measurement used: Euclidean distance over the
    raw (latitude, longitude) pair, in degrees. Not a distance on the earth."""
    return math.hypot(a[0]-b[0], a[1]-b[1])

def report(title):
    print("\n" + "=" * 78); print(title); print("=" * 78)

pts  = {n: (la, lo) for n, _, la, lo in LANGS}
names = [n for n, _, _, _ in LANGS]

# ---------------------------------------------------------------- 1. extent
report("1. Extent of the attested set (reference-free)")
lats = [p[0] for p in pts.values()]; lons = [p[1] for p in pts.values()]
print(f"latitude  {min(lats):.3f} .. {max(lats):.3f} N")
print(f"longitude {min(lons):.3f} .. {max(lons):.3f} E")
nw = max(names, key=lambda n: pts[n][0] - pts[n][1])   # most north-and-west
print(f"northernmost: {max(names, key=lambda n: pts[n][0])}")
print(f"westernmost : {min(names, key=lambda n: pts[n][1])}")

# ------------------------------------------- 2. nearest-neighbour, no reference
report("2. Nearest-neighbour distance for every variety (NO reference point)")
print("This is the reference-free measure of isolation. It needs no chosen")
print("northwestern anchor and so is not exposed to that free parameter.\n")
nn = {}
for n in names:
    other = [(haversine(pts[n], pts[m]), m) for m in names if m != n]
    d, m = min(other)
    nn[n] = (d, m)
for n in sorted(names, key=lambda x: -nn[x][0]):
    print(f"  {n:<15} {nn[n][0]:8.1f} km   nearest = {nn[n][1]}")
vals = sorted(d for d, _ in nn.values())
med = vals[len(vals)//2]
print(f"\nmedian nearest-neighbour distance          : {med:.1f} km")
print(f"Brahui nearest-neighbour distance          : {nn['Brahui'][0]:.1f} km")
print(f"ratio Brahui : median                      : {nn['Brahui'][0]/med:.1f}x")
print(f"second most isolated                       : "
      f"{sorted(names, key=lambda x:-nn[x][0])[1]} "
      f"({sorted(vals)[-2]:.1f} km)")
print(f"\nBrahui's nearest attested Dravidian neighbour is {nn['Brahui'][1]}.")
kur = haversine(pts['Brahui'], pts['Kurukh']); mal = haversine(pts['Brahui'], pts['Malto'])
print(f"  Brahui - Kurukh {kur:.1f} km ; Brahui - Malto {mal:.1f} km")
print(f"  Brahui - {nn['Brahui'][1]} {nn['Brahui'][0]:.1f} km")

# --------------------------------------------- 3. leave-one-out over a grid
report("3. Leave-one-out influence over a grid of northwestern reference points")
print("Statistic S(R, L) = distance from reference R to the NEAREST language in L.")
print("Influence(i, R)   = S(R, L minus i) - S(R, L).  Zero unless i is nearest.")
print("Grid: the quadrant north and west of the attested range, 24-36 N by")
print("60-76 E at 1 degree spacing (221 points). The grid is itself a choice;")
print("that is the point of reporting a grid rather than a single anchor.\n")

grid = [(la, lo) for la in range(24, 37) for lo in range(60, 77)]
infl_km  = {n: [] for n in names}
argmin_ct = {n: 0 for n in names}
for R in grid:
    ds = sorted((haversine(R, pts[n]), n) for n in names)
    s_full, nearest = ds[0]
    argmin_ct[nearest] += 1
    for n in names:
        rest = [d for d, m in ds if m != n]
        infl_km[n].append(min(rest) - s_full)

print("  variety          argmin share   median influence   max influence")
for n in sorted(names, key=lambda x: -max(infl_km[x])):
    v = sorted(infl_km[n]); m_ = v[len(v)//2]
    print(f"  {n:<15} {argmin_ct[n]/len(grid)*100:9.1f}%   {m_:12.1f} km   {max(v):10.1f} km")

nz = [n for n in names if max(infl_km[n]) > 0]
print(f"\nVarieties with any non-zero influence anywhere on the grid: {len(nz)} of 20")
print(f"  {', '.join(nz)}")
print(f"Grid share on which Brahui is the nearest attested Dravidian language: "
      f"{argmin_ct['Brahui']/len(grid)*100:.1f}%")
tot = sum(max(infl_km[n]) for n in names)
print(f"Brahui's share of the summed maximum influence across all 20: "
      f"{max(infl_km['Brahui'])/tot*100:.1f}%")

# ------------------------------------- 4. what deleting Brahui actually does
report("4. What deleting Brahui does to the statistic, by reference point")
for R, label in [((33.0, 72.0), "upper Indus / Kabul confluence area"),
                 ((30.0, 70.0), "middle Indus"),
                 ((27.0, 68.0), "lower Indus"),
                 ((29.5, 67.5), "Kachi / Bolan, next to Brahui itself"),
                 ((36.0, 64.0), "Bactria / upper Oxus"),
                 ((24.0, 76.0), "Malwa, a NON-northwestern control")]:
    ds = sorted((haversine(R, pts[n]), n) for n in names)
    s_full, nearest = ds[0]
    rest = sorted(d for d, m in ds if m != "Brahui")
    nxt = [m for d, m in ds if m != "Brahui"][0]
    print(f"\n  R = {R[0]:.1f}N {R[1]:.1f}E  ({label})")
    print(f"    nearest with Brahui   : {nearest} at {s_full:.0f} km")
    print(f"    nearest without Brahui: {nxt} at {rest[0]:.0f} km")
    print(f"    change                : {rest[0]-s_full:+.0f} km")

# ------------------------------ 5. the metric itself: euclidean-degrees error
report("5. Euclidean distance over degrees vs great-circle distance")
print("The challenged measurement used Euclidean distance on a lat/lon pair.")
print("Below, each variety's distance from one reference, both ways, with the")
print("degree figure converted at 111.32 km per degree for comparability.\n")
R = (30.0, 70.0)
print(f"  reference {R[0]}N {R[1]}E")
print(f"  {'variety':<15} {'great-circle':>13} {'euclid-deg x111.32':>20} {'error':>10}")
worst = (0, None)
for n in sorted(names, key=lambda x: haversine(R, pts[x])):
    gc = haversine(R, pts[n]); ed = euclid_deg(R, pts[n]) * 111.32
    err = (ed - gc) / gc * 100
    if abs(err) > abs(worst[0]): worst = (err, n)
    print(f"  {n:<15} {gc:10.0f} km {ed:17.0f} km {err:+9.1f}%")
print(f"\n  Largest error: {worst[1]} at {worst[0]:+.1f}%.")
print("  The error is a function of latitude, which is the axis the whole")
print("  northwest-versus-south contrast runs along.")

# does the metric change the ordering?
gc_order = sorted(names, key=lambda x: haversine(R, pts[x]))
ed_order = sorted(names, key=lambda x: euclid_deg(R, pts[x]))
print(f"\n  Rank order identical under both metrics from this reference: "
      f"{gc_order == ed_order}")
disagree = 0
for la in range(24, 37):
    for lo in range(60, 77):
        Rg = (la, lo)
        if (min(names, key=lambda x: haversine(Rg, pts[x]))
                != min(names, key=lambda x: euclid_deg(Rg, pts[x]))):
            disagree += 1
print(f"  Grid points where the two metrics disagree on WHICH language is "
      f"nearest: {disagree} of {len(grid)}")
