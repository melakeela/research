# HOLD-008 — the documents that would settle Rigvedic relative chronology

**Opened:** 2026-09-09
**Unit:** domain A, Rigvedic chronology and transmission
**Blocks:** `A-1` in `03-REGISTERS/domain-a-hypothesis-eligibility.csv`
(`NOT-ELIGIBLE-SOURCE-BLOCKED`); `A-4` (`CANNOT-GATE`); the promotion of
`DA-001`, `DA-008` and `DA-015` past `PROVISIONAL`; step 11 for the whole
domain; and any public copy under method step 14.

## What is blocked, and why each matters

| Source | Ledger | State | Why this unit needed it |
|---|---|---|---|
| E. V. Arnold, *Vedic Metre in its Historical Development*, Cambridge 1905 | `SRC-026` (read 2026-09-07), `SRC-100` (refused 2026-09-08) | `EGRESS_BLOCKED` | The single source behind every stratum code in this repository. Needed to check that `strata.json` transcribes it faithfully, and to read what Arnold's criteria actually were. **The unit sent to examine the Arnold dependency could not open Arnold.** |
| Hellwig, Scarlata and Widmer, "Reassessing Rigvedic Strata", JAOS 2021 | `SRC-105` | abstract only | The one retrieved modern re-test. Which allomorphs, which stratifications and which controls are all unreadable from the abstract, and they decide the scope of the null. |
| Oldenberg, *Prolegomena*, 1888 | in `SRC-071`'s bibliography; not retrieved | not retrieved | The standard analysis of the collection and arrangement — `DATE 3`. Reaches this record only as a column of binary flags. |
| Kevin M. Ryan, "The Development of Diphthongs in Vedic Sanskrit", JAOS 2021 | `SRC-112` | abstract only | Would be a second metrical instrument, except that Ryan compiled `strata.json` (`DEP-031`). Whether it delimits "oldest material" independently of Arnold is exactly what the abstract does not say. |
| Any Pāṇini edition, translation or study | none | never retrieved | Constitution §4.A asks what the *chandasi* rules imply. This repository has never opened Pāṇini in any session. |
| Scite citation-context measurement | `SRC-104` | quota-refused | Method step 11. Would show how the 2021 result has been received — supporting, contrasting, mentioning. Same block as `D-003`. |
| Shahbazi, BSOAS XL (1977) 25–35 | via `SRC-109` | not retrieved | The Gāthic date that Burrow's figure rests on, and therefore one end of the spread pillar 4 inherits. |
| Proferes, cited by Elby at p.29 | via `SRC-114`, `DEP-033` | not retrieved | The Brāhmaṇa anchor of the stacked-interval argument. One survey citing one book. |

## The shape of the blockage

It is one-sided, and the direction is worth stating. **What remains reachable is
the transcribed digital layer; what is blocked is every document that would let
that layer be checked.** A session can measure `strata.json` to four decimal
places and cannot read the book it transcribes. That is not a neutral
constraint: it systematically favours claims *about* the annotation over claims
about the scholarship the annotation encodes, and it is the same asymmetry
`RA-008` records programme-wide.

Two of the eight were readable in this repository five weeks ago. `SRC-026` was
retrieved on 2026-09-07 and refused on 2026-09-08. Reachability is a timestamped
probe and not a property — `RA-003`, `D-042` — and this hold is an instance of
that, not an exception to it.

## Measured, 2026-09-09T02:31Z

Ten hosts a Rigvedic chronology unit would need were probed directly.
**All ten refused** (`SRC-118`): archive.org, jstor.org, doi.org, GRETIL, TITUS,
sanskrit-lexicon.uni-koeln.de, sanskrit-trikashaivism.com, ashtadhyayi.com,
wisdomlib.org, and vedaweb.uni-koeln.de — the last of which answered on
2026-09-07. Two lanes worked in the same session: the git proxy anonymous read
lane, which delivered the entire corpus, and the MCP connectors, which delivered
abstracts.

So the asymmetry above is not an impression. **Data in git repositories and
abstracts through commercial connectors are reachable; every library, archive,
dictionary and text collection is not.** `ashtadhyayi.com` and
`sanskrit-lexicon.uni-koeln.de` are among the refusals, which is why the Pāṇini
lane could not be opened even as a probe.

## What was done instead

Nothing was inferred to fill the gap. Where a source was needed and absent, the
register says so and the status stops:

- `A-1` is `NOT-ELIGIBLE-SOURCE-BLOCKED`, **not** rejected. Arnold's strata did
  not fail a test; the test could not be run.
- `A-4` (Pāṇini) is `CANNOT-GATE` with zero retrieval on both sides, and the
  absence is typed `NOT PRODUCED` — a fact about this record carrying no
  evidential weight in either direction.
- `DA-C-003` assesses the *form* of the absence-of-iron argument and declines to
  assess the argument, because `áyas-` has had no §7 treatment here.
- Step 11 is reported as not run.

## What would lift it

Any one of: archive.org restored to the allowlist; JSTOR access for the two JAOS
articles; a Scite quota; or the owner supplying Arnold 1905 and one Pāṇini
edition directly. The cheapest single item is **archive.org**, which alone would
return Arnold 1905 and Oldenberg 1888 and would move `A-1` off
`SOURCE-BLOCKED`.

Escalated at `D-001` and `D-042` (egress policy) and `D-003` (Scite quota). No
new owner decision is opened: this hold is an instance of blockages already
registered, and opening a fourth would duplicate them.
