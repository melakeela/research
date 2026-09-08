#!/usr/bin/env python3
"""Decompose the inherited 392 asset slots by acquisition economics.

Ledger: SRC-101. Register: AS-024. Brief: 06-BRIEFS/asset-sourcing-plan.md §4.

Reads 01-INHERITED/curatorial-audit-v1.1/asset-register.csv and mvp.csv and
derives every count the brief states, so that none of them is a figure taken
on trust. Run:  python3 04-AUDITS/asset-slot-decomposition.py

THE PARTITION IS A JUDGEMENT, AND IT IS WRITTEN OUT HERE SO IT CAN BE
ARGUED WITH. The workbook gives 392 slot names and one uniform
`Source / commission route = To research`. Assigning each slot name to an
acquisition economics is this repository's analysis, not the workbook's, and
the first version of it was wrong in a specific direction: it typed four slot
kinds IMPOSSIBLE that are only UNMEASURED, which inflated the brief's
headline finding. See BF-025. The rule now applied:

  SELF        the project makes it; no third party is involved beyond a
              public-domain base layer, which still needs an asset record.
  LICENCE     someone else's work is needed. A route may exist, may not, and
              in this environment could not be measured (SRC-089). This is
              NOT a claim that material exists.
  MIXED       partly open data, partly institutional.
  MUST-CREATE the record does not exist until this project creates it, under
              any access conditions whatever. Typed NOT PRODUCED.

MUST-CREATE is deliberately hard to qualify for. "No open licence was found"
is never enough, because nothing could be searched. Only "no search could
find it, because it is not there to find" qualifies.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "01-INHERITED" / "curatorial-audit-v1.1"

# slot name (as the workbook writes it) -> economics, with the reason.
PARTITION = {
    # Generic essay set
    "opening atmosphere asset":          ("SELF", "house design work"),
    "claim-specific diagram":            ("SELF", "the project's own argument about a contested claim; nobody else's to license"),
    "source facsimile":                  ("LICENCE", "a real manuscript or print image"),
    "social card":                       ("SELF", "house design work"),
    # Data/interactive
    "verified dataset":                  ("SELF", "the project produces it; the exposure is evidentiary, not legal"),
    "accessible SVG/map":                ("SELF", "built by the project over a public-domain base (AS-014)"),
    "legend":                            ("SELF", "built by the project"),
    "mobile alternative":                ("SELF", "built by the project"),
    "downloadable table":                ("SELF", "built by the project"),
    # Text/social-history
    "primary-text facsimile":            ("LICENCE", "a manuscript or early print image"),
    "translation excerpt rights":        ("LICENCE", "a modern translation is a separate work; see AS-021"),
    "editorial illustration or print ephemera": ("LICENCE", "period print material"),
    # Custody/institutional
    "collection record":                 ("LICENCE", "route already exercised: the Met CC0 dataset, AS-004/AS-006"),
    "accession/custody document":        ("MIXED", "partly in open collection data, partly institutional"),
    "object image rights":               ("LICENCE", "CC0 routes verified at AS-004 and AS-009; unreachable, not absent"),
    "institutional correspondence":      ("MUST-CREATE", "a request this project has not made and an answer not yet given"),
    "access-status evidence":            ("LICENCE", "partly pre-exists: Gallery Number is populated on 290 of the 1,005 Met records (SRC-100)"),
    # Language/script
    "manuscript/inscription image":      ("LICENCE", "an inscription photographed legibly"),
    "glyph diagram":                     ("SELF", "house work"),
    "language map":                      ("SELF", "house work over a public-domain base"),
    "pronunciation audio where licensed": ("LICENCE", "the workbook says 'where licensed' and does not say reconstructed; for an attested language, licensed audio plausibly exists and could not be measured"),
    # Place/ecology
    "site/landscape photography":        ("LICENCE", "unmeasured: Commons, Flickr Commons, Openverse, ASI and TNSDA all blocked"),
    "material macro":                    ("LICENCE", "unmeasured: detail photography plausibly sits in the CC0 image corpora of AS-009"),
    "ecological map":                    ("SELF", "house work over Natural Earth, public domain (AS-014)"),
    "present-context image":             ("LICENCE", "unmeasured: a recent openly licensed photograph of the site would satisfy it"),
}


def main() -> None:
    rows = list(csv.reader(open(WORKBOOK / "asset-register.csv", newline="", encoding="utf-8")))[4:]
    mvp = {l.split(",")[1]: l.split(",")[0]
           for l in (WORKBOOK / "mvp.csv").read_text(encoding="utf-8").splitlines()[4:]}

    classes, cls_slots, cls_mvp_pages, cls_mvp_slots = {}, {}, {}, {}
    econ, econ_mvp, unknown = {}, {}, []
    per_class_econ = {}
    pages = slots = mvp_pages = mvp_slots = 0

    for r in rows:
        if len(r) < 7 or not r[0]:
            continue
        slug, required = r[0], r[2].strip()
        names = [s.strip() for s in required.split(";")]
        # one workbook row writes "...or print ephemera where appropriate"
        names = [n[:-len(" where appropriate")] if n.endswith(" where appropriate") else n
                 for n in names]
        cls = names[0]
        pages += 1
        slots += len(names)
        classes[cls] = classes.get(cls, 0) + 1
        cls_slots[cls] = cls_slots.get(cls, 0) + len(names)
        is_mvp = slug in mvp
        if is_mvp:
            mvp_pages += 1
            mvp_slots += len(names)
            cls_mvp_pages[cls] = cls_mvp_pages.get(cls, 0) + 1
            cls_mvp_slots[cls] = cls_mvp_slots.get(cls, 0) + len(names)
        for n in names:
            if n not in PARTITION:
                unknown.append(n)
                continue
            kind = PARTITION[n][0]
            econ[kind] = econ.get(kind, 0) + 1
            per_class_econ.setdefault(cls, {})
            per_class_econ[cls][kind] = per_class_econ[cls].get(kind, 0) + 1
            if is_mvp:
                econ_mvp[kind] = econ_mvp.get(kind, 0) + 1

    assert not unknown, f"unpartitioned slot names: {sorted(set(unknown))}"
    print(f"pages {pages} | slots {slots} | MVP pages {mvp_pages} | MVP slots {mvp_slots}")
    print()
    print(f"{'class (by first slot name)':44} {'pages':>5} {'slots':>5} {'MVPp':>5} {'MVPs':>5}")
    for c in sorted(cls_slots, key=lambda x: -cls_slots[x]):
        print(f"  {c[:42]:42} {classes[c]:5} {cls_slots[c]:5} "
              f"{cls_mvp_pages.get(c, 0):5} {cls_mvp_slots.get(c, 0):5}")
    print()
    order = ("SELF", "LICENCE", "MIXED", "MUST-CREATE")
    print(f"{'economics':14} {'slots':>6} {'MVP slots':>10}")
    for k in order:
        print(f"  {k:12} {econ.get(k, 0):6} {econ_mvp.get(k, 0):10}")
    print(f"  {'TOTAL':12} {sum(econ.values()):6} {sum(econ_mvp.values()):10}")
    assert sum(econ.values()) == slots == 392, "partition does not cover every slot"
    assert sum(econ_mvp.values()) == mvp_slots == 62
    print()
    print("per class:")
    for c in sorted(per_class_econ, key=lambda x: -cls_slots[x]):
        d = per_class_econ[c]
        self_n, tot = d.get("SELF", 0), cls_slots[c]
        print(f"  {c[:42]:42} " + "  ".join(f"{k}={d.get(k, 0)}" for k in order)
              + f"   self-sufficient {100 * self_n / tot:.0f}%")


if __name__ == "__main__":
    main()
