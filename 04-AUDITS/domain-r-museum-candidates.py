#!/usr/bin/env python3
"""
domain-r-museum-candidates.py — the object side of domain R.

Builds 03-REGISTERS/domain-r-museum-candidates.csv from the CDLI catalogue
(SRC-102), one row per object whose catalogued material is lapis lazuli,
carnelian, or one of the materials those two are confused with.

Three things this register is careful about, because the domain's named
traps are all versions of the same error.

1. `material` in the CDLI catalogue is an ATTRIBUTION, not an analysis. The
   file has 64 columns and not one of them can hold a reference to an
   analytical study. A row saying "stone: lapis lazuli" records that a
   cataloguer wrote that down; it does not record that anyone measured it.
   The register therefore carries `analytical_provenance` as a separate
   column and it is empty for every row, which is the finding, not a gap in
   the register.

2. Two further classes are carried deliberately, and they are NOT the same
   thing. LOOK-ALIKE-CONTROL is glass, faience, Egyptian blue, frit, azurite,
   turquoise, sodalite and jasper: materials confusable with lapis or carnelian
   and mineralogically distinct from both. SAME-MINERAL-FAMILY is agate,
   chalcedony and sard, which are NOT controls at all - DRR-009 records that
   bead carnelian is heat-treated iron-rich agate, so an object catalogued
   "agate" and one catalogued "carnelian" may be the same mineral differing
   only in a cataloguer's word. Merging the two, as the first version of this
   script did, made the control set contain the target material.

3. Custody is stated as of a date, never in the present tense. The
   retrieved dump's own README says "Last update was August 2022" and the
   latest `date_updated` value in the 353,283 catalogue rows is 2022-08-21.
   Every custody cell is therefore custody as CDLI recorded it on or before
   that date, and is written that way.

Image licensing is not determined here and cannot be. The `photo_up` column
records that CDLI holds a scan; it says nothing about the terms under which
that scan may be used, the repository carries no LICENSE file, and
cdli.mpiwg-berlin.mpg.de is refused at the egress gateway (SRC-099). Every
row therefore reads NOT ACCESSIBLE and the question is D-055.
"""
import csv, os, re, collections

SCRATCH = os.environ.get("DOMAIN_R_DATA", ".")
CAT = os.path.join(SCRATCH, "cdli_cat.csv")
OUT = os.path.join(os.environ.get("DOMAIN_R_OUT", "03-REGISTERS"), "domain-r-museum-candidates.csv")
SNAPSHOT = "2022-08-21"

LAP = re.compile(r"lapis|lazul", re.I)
CAR = re.compile(r"carnelian|cornelian|\bsard\b", re.I)
# Split after adversarial review. Agate and chalcedony are NOT controls: DRR-009
# records that bead carnelian IS heat-treated iron-rich agate, so an object
# catalogued "agate" and one catalogued "carnelian" may be the same mineral
# differing only in a cataloguer's word. They are their own class.
SAME_FAMILY = re.compile(r"agate|chalcedony|\bsard\b", re.I)
LOOK = re.compile(r"sodalite|azurite|turquoise|jasper|glass|faience|frit|egyptian blue", re.I)

FIELDS = ["candidate_id", "candidate_class", "p_number", "designation", "object_type",
          "geological_source", "analytical_provenance", "workshop", "manufacturing_tradition",
          "exporter", "intermediary", "textual_provenance_label",
          "findspot", "findspot_precision", "excavation_no", "stratigraphic_level",
          "museum_attribution", "modern_custody", "custody_as_of",
          "acquisition_history", "image_held_by_cdli", "image_licence_status",
          "cdli_material_attribution", "cdli_period", "primary_publication",
          "status", "source_id", "locator", "retrieval_date", "notes"]

def main():
    csv.field_size_limit(1 << 30)
    rows, n = [], 0
    with open(CAT, newline="", encoding="utf-8", errors="replace") as f:
        for r in csv.DictReader(f):
            m = (r.get("material") or "").strip()
            cls = ("LAPIS-ATTRIBUTED" if LAP.search(m) else
                   "CARNELIAN-ATTRIBUTED" if CAR.search(m) else
                   "SAME-MINERAL-FAMILY (agate/chalcedony)" if SAME_FAMILY.search(m) else
                   "LOOK-ALIKE-CONTROL" if LOOK.search(m) else None)
            if not cls:
                continue
            n += 1
            idt = (r.get("id_text") or "").strip()
            p = "P%06d" % int(idt) if idt.isdigit() else ""
            prov = (r.get("provenience") or "").strip()
            prec = ("NO FINDSPOT RECORDED" if not prov else
                    "FINDSPOT UNCERTAIN (CDLI's own qualifier)" if re.search(r"uncertain|\?", prov, re.I) else
                    "FINDSPOT NAMED")
            coll = (r.get("collection") or "").strip()
            photo = (r.get("photo_up") or "").strip()
            rows.append({
              "candidate_id": f"MC-R-{n:04d}",
              "candidate_class": cls,
              "p_number": p,
              "designation": (r.get("designation") or "").strip(),
              "object_type": (r.get("object_type") or "").strip(),
              "geological_source": "",
              "analytical_provenance": "",
              "workshop": "",
              "manufacturing_tradition": "",
              "exporter": "",
              "intermediary": "",
              "textual_provenance_label": "",
              "findspot": prov,
              "findspot_precision": prec,
              "excavation_no": (r.get("excavation_no") or "").strip(),
              "stratigraphic_level": (r.get("stratigraphic_level") or "").strip(),
              "museum_attribution": (r.get("museum_no") or "").strip(),
              "modern_custody": coll or "NOT RECORDED",
              "custody_as_of": SNAPSHOT,
              "acquisition_history": (r.get("acquisition_history") or "").strip(),
              "image_held_by_cdli": "YES (%s)" % photo if photo else "NO FLAG",
              "image_licence_status": "NOT ACCESSIBLE (SRC-099; no LICENSE file in the retrieved repository; D-055)",
              "cdli_material_attribution": m,
              "cdli_period": (r.get("period") or "").strip(),
              "primary_publication": (r.get("primary_publication") or "").strip(),
              "status": "PROVISIONAL",
              "source_id": "SRC-102",
              "locator": f"cdli_cat.csv row id_text={idt}, columns material, provenience, collection, museum_no, acquisition_history, photo_up",
              "retrieval_date": "2026-09-08",
              "notes": ("Material is CDLI's cataloguing, not an analysis; no column in the source can cite one. "
                        "Status is PROVISIONAL and not VERIFIED because a single catalogue is one source: what is "
                        "VERIFIED is that CDLI records this, and that is what the locator points at."),
            })
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    c = collections.Counter(r["candidate_class"] for r in rows)
    TARGETS = {"LAPIS-ATTRIBUTED", "CARNELIAN-ATTRIBUTED"}
    prec = collections.Counter(r["findspot_precision"] for r in rows if r["candidate_class"] in TARGETS)
    img = collections.Counter(r["image_held_by_cdli"].split(" ")[0] for r in rows if r["candidate_class"] in TARGETS)
    print(f"{len(rows)} rows -> {OUT}")
    for k, v in c.most_common():
        print(f"   {v:>5}  {k}")
    print("  findspot precision, lapis and carnelian only:")
    for k, v in prec.most_common():
        print(f"   {v:>5}  {k}")
    print("  CDLI image flag, lapis and carnelian only:")
    for k, v in img.most_common():
        print(f"   {v:>5}  {k}")
    print("  analytical_provenance populated:", sum(1 for r in rows if r["analytical_provenance"]))

if __name__ == "__main__":
    main()
