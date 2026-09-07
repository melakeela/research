# HOLD-002 — no Dravidian etymological source is reachable

**Raised by:** domain E source probe, 2026-09-07
**Blocks:** distinctions 1–4 of constitution §4.E — attested Dravidian
languages, reconstructed Proto-Dravidian, accepted Old Indo-Aryan Dravidian
loans, and proposed Dravidian substrate forms.
**Ledger:** `SRC-037`, `SRC-040`, `SRC-041`, `SRC-042`, `SRC-045`, `SRC-046`

## What is needed

A Dravidian etymological reference with citable entry numbers. In order of
preference:

1. **Burrow, T. and M. B. Emeneau, *A Dravidian Etymological Dictionary*,
   2nd edition, Oxford: Clarendon Press, 1984** (DEDR). The reference work.
   Cited by entry number, which is what makes a claim like "DEDR 1444"
   re-findable. Web presentation at
   `https://dsal.uchicago.edu/dictionaries/burrow/`.
2. The 1961 first edition and the 1968 and 1972 supplements, scanned on
   `archive.org` (identifiers `dravidianetymolo0000burr_u1k6` and
   `dravidianetymolo0000tbur` were named by the search channel, SRC-046, and
   have **not** been confirmed by retrieval).
3. Any Dravidian comparative lexicon with stable entry numbering, including
   the Cologne mirror set.

## What was tried

| Host | Channel | Result |
|---|---|---|
| `dsal.uchicago.edu` | curl, WebFetch | 403 at CONNECT, both |
| `archive.org` | curl, WebFetch | 403 at CONNECT, both |
| `sanskrit-lexicon.uni-koeln.de` | curl | 403 at CONNECT |
| `www.cologne-digital-sanskrit-dictionaries.de` | curl | 403 at CONNECT |
| `starlingdb.org` | curl | 403 at CONNECT |
| `titus.uni-frankfurt.de` | curl, WebFetch | 403 at CONNECT, both |
| `gretil.sub.uni-goettingen.de` | curl, WebFetch | 403 at CONNECT, both |

GRETIL and TITUS were probed because the task named them. Neither is a
Dravidian etymological source in the first place — GRETIL is a Sanskrit and
Middle Indo-Aryan e-text archive — so their loss is not what blocks this
hold; `dsal.uchicago.edu` and `archive.org` are.

## What is *not* claimed

That no Dravidian etymology exists for any Rigvedic word. That would be an
absence argument, and under the negative-evidence standard this absence is
typed **NOT ACCESSIBLE** — a property of this session's network policy, with
no evidential bearing whatever on Dravidian or Indo-Aryan lexicon.

Nothing in this unit may be read as evidence against a Dravidian loan
hypothesis. The register records the Dravidian comparanda that a reader
would expect to see here as absent-because-unretrieved, not as absent.

## What the answer would change

DEDR would let the loan-etymology half of domain E be evidenced at all. As
it stands, every claim in this unit that would require a Dravidian etymon
carries `HOLD` and is excluded from analysis, and the measurements that were
made are corpus-internal and do not depend on it.
