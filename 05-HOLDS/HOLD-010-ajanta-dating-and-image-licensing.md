# HOLD-010 — The Ajanta date, and image licensing for every object in this unit

**Opened:** 2026-09-09, domain R.
**Blocks:** `DRB-014` (recorded `HOLD`); the chronological placement of
`OBJ-R-006`; and the `open_licensed_image` field of all 13 object dossiers and
all 796 museum-candidate rows.
**Typed absences:** `DR-NEG-007`, `NOT ACCESSIBLE`.

## Part one — the date

`SRC-107` dates the Ajanta murals it sampled to **"the 2nd century bce"**, in
its abstract and again in its opening summary. No dating authority is cited for
that in any retrieved passage.

The date is recorded as the source's own statement and is **not adopted**. No
claim in this unit depends on it. It is held rather than corrected because
correcting a published date from unretrieved general knowledge would introduce
an unsourced claim carrying the authority of a correction — the failure
`BF-031` records avoiding.

It matters because it decides which corridor the object belongs to. A
second-century BCE Deccan wall painting and a fifth-century CE one sit in
different worlds, and `OBJ-R-006` is the only South Asian lapis object in this
unit.

**What would clear it:** an excavation or epigraphic authority for the painted
phase of the specific caves sampled — the Archaeological Survey of India's own
record for the site would suffice, and `asi.nic.in` is refused (`SRC-099`).

## Part two — image licensing

The owner's instruction asked, for every object that could carry a museum
exhibit, whether an openly licensed image exists. **For every object in this
unit the answer is: not determinable from here.**

- The CDLI catalogue's `photo_up` column records that a scan is held, not the
  terms of its use. 125 of the 371 lapis and carnelian objects carry that flag.
- The retrieved `cdli-gh/data` repository carries **no LICENSE file**: probes
  for `LICENSE`, `LICENSE.md`, `license.txt` and `COPYING` at
  `raw.githubusercontent.com` all return 404.
- Every custodian database that would state licence terms is refused at the
  egress gateway: `britishmuseum.org`, `collectionapi.metmuseum.org`,
  `metmuseum.org`, `collections.louvre.fr`, `penn.museum`, `api.si.edu`,
  `commons.wikimedia.org`, `wikidata.org`, and CDLI's own host (`SRC-099`).

So every row of `03-REGISTERS/domain-r-museum-candidates.csv` reads
`image_licence_status = NOT ACCESSIBLE`.

This is not a judgement that the images are unavailable. Several of these
institutions publish open licence terms as policy, and the likely true answer is
that a substantial number are openly licensed. **What is missing is permission
to know which**, and the question is `D-055`.

## Part three — what else is blocked with it

Custody has the same shape and is worse, because it is silently plausible.
Custody in this unit is stated **as of 2022-08-21**, the latest `date_updated`
in the 353,283 catalogue rows, and the retrieved dump's own README says "Last
update was August 2022". A four-year-old snapshot is the most recent custody
statement this session can reach.

For most objects that is a formality. For the objects the catalogue places in
the **National Museum of Iraq, Baghdad**, the **National Museum of Syria,
Idlib** — which holds 63 of the Dilmun texts, the Ebla archive material — and
for anything in Kabul or Mosul, it is not. `RA-026` queues the re-check for the
moment `D-055` is answered.

## What must not happen while it is held

No object in this unit may be described as available for a museum use, and no
image may be treated as usable. The rights-steward discipline runs on any
candidate before it enters a page brief, and `APA-R-005` records that 254 of the
371 lapis and carnelian candidates cannot be placed at all — many of them market
acquisitions with acquisition histories reading "Bought in Smyrna" or
"purchased: Sotheby, 22nd October, lot no. 86" — which raises an acquisition
question this unit is not equipped to answer.
