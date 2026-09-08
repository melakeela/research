# HOLD-006 — an Anukramaṇī, or any per-hymn ṛṣi attribution independent of Geldner

**Raised:** 2026-09-07
**Blocks:** constitution §4J's *poet lineage* field, at full strength.
**Does not block:** the rest of the §4J corpus. The field is populated from the
one source in hand, with what that source can and cannot support recorded on
every row.
**Ledger:** `SRC-080` (GRETIL), `SRC-081` (archive.org), `SRC-082` (TITUS),
`SRC-083` (fallbacks) — all `EGRESS_BLOCKED`. `SRC-070` is the source in hand.

## What is needed

A per-hymn attribution of composer, from a source that is not Geldner: the
Sarvānukramaṇī of Kātyāyana, the Bṛhaddevatā, or a critical edition that prints
the ṛṣi with each hymn. Any one of them would do.

## Why it is needed, specifically

§4J asks for **poet lineage** — a family, not only a name. The one source in
this container is `info/addressees.json` (`SRC-070`), whose per-hymn group
headings reproduce Geldner's editorial arrangement in *Der Rig-Veda* (HOS
33–35). Two problems, and the second is the larger:

1. **45 of the 103 passages have a heading that names a deity, not a poet** —
   "hymns to Indra" (26), "hymns to Agni" (11), "hymns to Viṣṇu", "hymns to the
   Viśvedevas", and so on. For those passages the source is silent on
   authorship. That silence is **NOT PRODUCED** under the negative-evidence
   standard: Geldner's headings are an arrangement, and where he arranged by
   deity he did not record a poet. It is not evidence that the hymn is
   anonymous.
2. **Where a poet *is* named, three removes separate the field from the
   composition event.** Geldner 1951 follows the Anukramaṇī tradition; that
   tradition is a late-Vedic to post-Vedic ascription; and the ascription is
   itself a claim about a text older than it. Every value is a fact about
   Geldner's arrangement, and the register says so on the row rather than in a
   preface.

There is also a **standing tradition** that books 2–7 are family books —
Gṛtsamada, Viśvāmitra, Vāmadeva, Atri, Bharadvāja, Vasiṣṭha — which would
supply a lineage for 40 of the 103 passages directly from the book number.
**It is not asserted anywhere in this unit**, because no retrieval in this
container establishes it and confidence does not promote a claim. It is
recorded here as the specific thing the missing source would settle.

## Why retrieval failed

Not a paywall, not robots, not authentication. Every candidate host answered a
**403 to the proxy CONNECT**. The finding worth carrying is that GRETIL,
archive.org and TITUS were all reachable **earlier the same day** — `SRC-028`
records 1,033,721 bytes from GRETIL, `SRC-025` records 1,054,774 bytes of OCR
text from archive.org, `SRC-033` records a 200 from TITUS. Same hosts, same
date, opposite result. The egress policy differs between sessions on this
environment, so a `retrieval_capable=YES` row is a statement about one moment
and cannot be relied on as a standing property.

That is `D-042`'s point, and this hold is a worked instance of it.

## What was done instead

The field is populated from `SRC-070` and marked `PROVISIONAL`, with a
`poet_attribution_basis` column on every row recording that the value is
Geldner's group heading, and a distinct value for the 45 passages where the
heading names a deity. Nothing is promoted, nothing is inferred from the book
number, and no passage receives a poet it does not have a source for.

## What would release the hold

Any of GRETIL, archive.org or TITUS on the environment allowlist — `D-043`
already asks for the second of the three for a different reason, and one
allowlist entry would serve both. Failing that, the owner supplying a
Sarvānukramaṇī text or a critical edition as a file.

## What changes if it is released

The 45 deity-headed passages could get a poet. The 58 that have one could be
checked against a source independent of Geldner, which would either corroborate
the field or reveal that it carries Geldner's arrangement rather than the
tradition's ascription. And the family-book attribution could be asserted with
a locator instead of being left out.
