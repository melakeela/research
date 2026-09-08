# HOLD-007 — no image repository is reachable, so no asset can be sourced

**Raised by:** the visual-asset sourcing survey, 2026-09-08
**Blocks:** every one of the 392 asset slots in
`01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, and therefore all
fifteen MVP pages.
**Ledger:** `SRC-089`, `SRC-093`, `SRC-096`, `SRC-098`
**Register:** `03-REGISTERS/asset-sourcing.csv`, claims `AS-001`, `AS-010`,
`AS-013`, `AS-017`, `AS-018`

## What is needed

An image. Any image, from any of the six classes, with a rights position that
can be written down.

## Why the hold is not "no openly licensed material exists"

It is not. The survey found the opposite: at least two major collections
(the Met, Cleveland) publish CC0 rights positions that were read from the
rightsholders' own repositories and are recorded `VERIFIED` at `AS-004` and
`AS-009`. Cleveland applies CC0 to as many as 30,000 **image files**, not
merely to metadata.

The hold is that this environment cannot reach any of them. Forty-two hosts
were probed on 2026-09-08 and every one answered 403 at the proxy CONNECT
except `raw.githubusercontent.com` and `media.githubusercontent.com`. That
list includes `images.metmuseum.org`, `openaccess-api.clevelandart.org`,
`commons.wikimedia.org`, `upload.wikimedia.org`, every IIIF endpoint, the
Archaeological Survey of India, the Tamil Nadu State Department of
Archaeology — and `creativecommons.org`, so a licence deed cannot be read
from its issuer either.

What the GitHub channel yielded is rights **texts** and one 317 MB metadata
dataset. Not one pixel.

## What this hold must not be read as saying

That the Place/ecology class has no openly licensed material. `AS-017` types
that absence `NOT ACCESSIBLE`, explicitly **not** `ABSENT DESPITE ADEQUATE
SEARCH`: the search was not adequate, because the environment prevented it.
Wikimedia Commons may hold usable photography of Keeladi and of Indus sites.
It was not consulted, so nothing is known either way.

The classes where the survey does assert that nothing openly licensed exists
are the three where the gap is definitional rather than logistical, and those
are recorded separately at `AS-015`, `AS-016` and `AS-019`. Opening the
allowlist will not close those.

## What would lift this hold

The `D-001` allowlist, applied to the hosts named in `SRC-089`. In descending
value for this programme:

1. `openaccess-api.clevelandart.org` and `openaccess-cdn.clevelandart.org` —
   the only verified route to CC0 image **files**.
2. `commons.wikimedia.org` and `upload.wikimedia.org` — the only plausible
   route to site photography that is not a fieldwork commission, and the only
   way to convert `AS-017` from `NOT ACCESSIBLE` into a measurement.
3. `images.metmuseum.org` and `collectionapi.metmuseum.org` — the 1,005
   object records censused at `AS-006` become 1,005 retrievable images.
4. `www.si.edu`, `edan.si.edu`, `smithsonian-open-access.s3-us-west-2.amazonaws.com`
   — promotes `AS-013` off `PROVISIONAL`.
5. `asi.nic.in`, `www.tnarch.gov.in`, `data.gov.in` — promotes `AS-018` off
   `PROVISIONAL` and is the only route to excavation-report figures.
6. `creativecommons.org` — so that a licence this project relies on can be
   quoted from its issuer rather than from a licensee's description of it.

## What proceeds without it

The rights analysis, which is what `06-BRIEFS/asset-sourcing-plan.md`
contains. Knowing which classes have a licence route and which have none is
independent of whether an image can be fetched today, and the three classes
flagged as uncosted commissioning are unaffected by any allowlist change.
