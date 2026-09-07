# Adversarial review — PR #22, domain M

**Target:** `melakeela/research` PR #22, "Domain M — the six models gated, North
Dravidian re-measured on DEDR", head `253474b`, base `aa40d3a` (main).
**Reviewer:** independent; did not produce the work, holds no Write access to it.
**Date:** 2026-09-07. **Method:** `.claude/agents/adversarial-reviewer.md`, all
fourteen checks, with the three the owner pressed for run to exhaustion.

**Verdict: DO NOT MERGE AS IS.** Six blocking findings, four of which change
numbers or statuses in the register. Nothing here is a matter of taste; every
finding is reproducible from the commands given.

This is careful work. The self-audit commits caught two real defects before I
arrived (`DMM-006`, `HOLD-006`), the dependency mapping at `DEP-011`–`DEP-015`
is the best in the repository, and `BF-007`–`BF-009` are genuine method failures
logged against the author's own draft. That is why the findings below are worth
making: the unit is close enough to right that its remaining errors would
survive.

---

## How to reproduce anything below

```
git clone https://github.com/moli-mandala/data.git jambu
git -C jambu checkout dbae3102fe779aa60f5ef03108f7918ab2ede006
python3 04-AUDITS/domain-m-dedr-north-dravidian.py --repo jambu --reps 20 --swaps 5000
```

Every deterministic count in the unit reproduces exactly: 5,520 entries, 26
languages, 0 unparsed, Brahui 269 / Kurux 775 / Malto 704, 176 / 1 / 1 / 7 /
193, 260 of 269, 509 / 176 / 193, 604 cross-references, 118 resolved, 12
Brahui touchpoints, Brahui named on 1 of 159,756 CDIAL lines. **The arithmetic
is sound and I could not break it.** The findings are about what the numbers
are numbers *of*, and about what the null can and cannot say.

---

# BLOCKING

## F-1 — Thirty-two identifiers collide with rows already on `main`, each pointing at something different

This is the finding that must be fixed first, because it silently corrupts every
other row in the unit.

The branch forked at `bc5baf0`. `main` has since merged PR #10 and PR #20 and
allocated further identifiers in five registers. Every identifier this unit
allocated is already taken on `main` by a **different** row:

| namespace | branch allocated | already on `main` as |
|---|---|---|
| `SRC-053`–`SRC-068` (16) | Consensus connector … BSOAS passage | Internet Archive re-probe, VedaWeb repo, JAMBU CLDF, JAMBU DEDR, Munda reflexes, CDIAL … |
| `DEP-010`–`DEP-015` (6) | Jambu/DEDR dependencies | domain E dependencies |
| `BF-007`, `BF-008`, `BF-009` | domain M method failures | domain E, unit 2 method failures |
| `RA-006`, `RA-007` | connector re-audit, DMB rows | substrate word-list re-audit, diacritic crosswalk |
| `D-038`–`D-042` | scite, Al-Burz, metadata policy, consent, register gate | `the-northwest-cousin.html`, mandated-file naming, egress, allowlist |

```
python3 - <<'EOF'
import csv,io,subprocess
def rows(ref,p,c):
    t=subprocess.run(['git','show',f'{ref}:{p}'],capture_output=True,text=True).stdout
    return {r[c]:r for r in csv.DictReader(io.StringIO(t)) if r.get(c)}
a=rows('origin/main','02-SOURCES/access-ledger.csv','source_id')
b=rows('origin/claude/domain-m-brahui-models-8kd31m','02-SOURCES/access-ledger.csv','source_id')
print(a['SRC-059']['source_name']); print(b['SRC-059']['source_name'])
EOF
```

`source_id` is the only link a claim has to its retrieval. Merged naively, every
`VERIFIED` row in this unit repoints at a different ledger row — and the
validator will not notice, because it only asks whether an identifier resolves
to *some* row, and after the merge they all will. This is the exact failure
`CLAUDE.md`'s inheritance rule and `AGENTS.md` §1 exist to prevent, arriving
through the merge rather than through the research.

The repository already has the remedy and the precedent: `09-DECISIONS/
DECISION-ID-MAP.csv` carries a "third block, post-merge reassignment" written
for exactly this on the `aryan-racialization-guard` branch, and two merge
commits on `main` read *"reassign the branch's D-037 to D-043"*. Nothing
equivalent was done here, and `DECISION-ID-MAP.csv` is untouched by this PR.

**Repair.** Merge `main`, renumber all thirty-two from the next free identifier
in each register, rewrite every in-tree reference (registers, method doc,
`validate-registers.py` docstring, `VALIDATOR-FINDINGS-2026-09-07.md`, HOLD
files, `RESEARCH-QUEUE.md`, the PR body), and record the reassignment. The `D-`
block needs `DECISION-ID-MAP.csv` rows; `CLAUDE.md` says a `D-` reference in an
older file is resolved through that map, and the PR body's five `D-0xx`
references will otherwise resolve to the wrong decisions permanently. GitHub
already reports the PR `mergeable_state: dirty`.

## F-2 — `main` already registers this exact file, under a stricter rule the unit breaches

Not a near miss. `main`'s `SRC-061` is *"DEDR (Burrow and Emeneau 1984, 2nd ed.)
as re-parsed in JAMBU `data/dedr/`"*, sha256
`1d91f819b9af2c530ba6688a089a775d4bd6bcaa7c8e30e90dacdcce3758943e`,
5,251,799 bytes, 68,807 reflex rows.

```
sha256sum jambu/data/dedr/dedr.csv
# 1d91f819b9af2c530ba6688a089a775d4bd6bcaa7c8e30e90dacdcce3758943e
```

Byte-identical to the file this unit measured. `main` also carries `SRC-060`
(the JAMBU CLDF database at the *same* pinned commit `dbae3102`, with a per-file
sha256 manifest at `02-SOURCES/domain-e-manifest-2026-09-07.md`), `SRC-062`
(the PDr layer), `SRC-065` (CDIAL) and `SRC-066` (the CDIAL Dravidian-mention
audit).

Two consequences, both blocking.

**(a) The status rule was already written and is not met.** `main`'s `SRC-061`
`blocking_constraint` reads:

> TWO REMOVES from the printed dictionary: print → DSAL digitization (SRC-056,
> EGRESS_BLOCKED) → JAMBU re-parse. **Counts over this table are VERIFIED as
> counts over this table. Assertions about the printed DEDR are PROVISIONAL.**

`DMM-001` is `VERIFIED` and its claim text opens *"The Dravidian Etymological
Dictionary of Burrow and Emeneau … contains 5,520 etymological entries across 26
attested Dravidian varieties"* — an assertion about the printed DEDR. So do
`DMM-002` (*"In DEDR, 176 entries are attested in…"*), `DMM-003`, `DMM-004`,
`DMM-005`, `DMM-009` (*"Turner's Comparative Dictionary … as re-encoded, names
Brahui on 1 line"* — this one is correctly scoped) and `DMM-008`. **Six of the
seven `VERIFIED` DEDR rows are worded as claims about the dictionary and must
be either restated as claims about the table or dropped to `PROVISIONAL`,**
under a constraint that was on `main` before this branch was opened.

**(b) `DEP-010` flattens a chain the repository had already typed.** `DEP-010`
says the encoding *"is not an independent witness to Dravidian etymology; it is
DEDR, parsed"* — one remove. `main` says two, and names the intermediate
(`SRC-056`, the DSAL digitisation, itself `EGRESS_BLOCKED`). F-4 below shows it
is really four. A source-genealogy row that shortens the chain is the specific
error `DEP-008` exists to catch, committed one register over.

`main`'s row also carries the reproducibility artefact this branch lacks: a
checksum manifest. `SRC-059` here records the clone and the commit but no hash
of the measured file, and the measurement's JSON output is not committed.

## F-3 — The file measured is marked **deprecated** upstream, and the current file changes the result

`moli-mandala/data` `README.md`, at the pinned commit, section **DEDR**:

> Originally, Suresh supplied a SQL database **scraped from the online version**
> (`data/dedr/dedr_new_entry_oct2013_edited.sql`) which was converted into a CSV
> at (`data/dedr/dedr.csv`). **These are now deprecated.**
>
> The current CSV format of the DEDR is generated using `data/dedr/parse.py`,
> which **scrapes the website** … The output is at `data/dedr/dedr_new.csv`.

`data/dedr/dedr.csv` — the file `load_dedr()` opens — is the deprecated one.
`dedr_new.csv` (76,303 lines against 68,807) is current. Nothing in `SRC-059`,
`DEP-010` or the method doc records this.

Recomputing the unit's own statistics on the current table, with dialect tags
normalised to base languages through `jambu/cldf/dialects.csv`:

| statistic | deprecated (`dedr.csv`) | current (`dedr_new.csv`) |
|---|---|---|
| entries | 5,520 | 5,544 |
| Brahui / Kurux / Malto attested | 269 / 775 / 704 | 273 / 788 / 716 |
| Kurux+Malto co-occurring | **509** | **522** |
| Kurux+Malto exclusive | **176** | **182** |
| Brahui+Kurux exclusive | 1 | 1 |
| **Brahui+Malto exclusive** | **1** | **2** |
| Brahui+Kurux+Malto exclusive | 7 | 7 |
| confined to North Dravidian | **193** | **197** |

Re-running the unit's own null (curveball, 300 draws × 100,000 swaps, seed
20260907) on the current table:

| statistic | obs | null mean | p(≥obs) |
|---|---|---|---|
| Kurux+Malto exclusive | 182 | 0.60 | 0.0033 (floor) |
| Brahui+Kurux exclusive | 1 | 0.15 | 0.1395 |
| **Brahui+Malto exclusive** | **2** | **0.14** | **0.0133** |
| Brahui+Kurux+Malto exclusive | 7 | 0.00 | 0.0033 (floor) |
| confined to North Dravidian | 197 | 1.71 | 0.0033 (floor) |

**`DMM-004` reverses.** The register states, at `VERIFIED`, that Brahui's
pairwise exclusive sharing with Kurux *and with Malto* is "indistinguishable
from chance" at p = 0.17. On the file the upstream database actually maintains,
Brahui+Malto is 2 and **p = 0.013**. The negative half of the unit's headline —
the half `DMI-001` and the PR body lean on — is an artefact of the deprecated
encoding.

**And the seven etymologies are not the same seven.** `DMM-003` lists them by
DEDR number: 1419, 1558, 2189, 2244, 2278, 3149, 5131. On the current table the
list is 1419, 2189, 2244, 2278, 3149, **4428**, 5131. It changes in both
directions and neither file is a superset:

- **4428** (`bēk` / `béku` / `bē` 'salt') is missing from the deprecated file
  because of a source markup defect the upstream maintainers document and repair
  by hand — `data/dedr/abbrevs.py`, `source_markup_repairs = {'4428': …}`,
  under the comment *"A small set of source entries has an unclosed initial
  `<b>` tag."* A real North Dravidian triple, absent from the measured file for
  a known parse bug.
- **1558** ('embrace / carry under the arm') keeps its six Kurux forms in the
  deprecated file and loses them in the current one, so it is a triple there and
  a Brahui–Malto pair here.

The enumeration in `DMM-003` is therefore a property of one encoding, presented
as a property of DEDR. `DMM-003`'s own caution — that 5131's Brahui form is
cited to `(MBE 1980a)` — is exactly the right instinct applied to one entry out
of seven.

**Repair.** Re-run against `data/dedr/dedr_new.csv` and re-derive
`DMM-001`–`DMM-005`, `DMM-006`, `DMM-008`; or state explicitly, in `SRC-059`,
`DEP-010`, the script docstring and every affected row, that the measurement is
of a deprecated 2013 encoding, with the deltas above on the face of the rows.
Do not do this silently: `DMM-004`'s conclusion is different on the two files
and the difference must be visible.

## F-4 — The null does not discriminate for the triple statistic, and `DMM-003` rests on it

The owner asked whether the observed statistic is an artefact of how DEDR groups
etymologies. Two parts, and they come apart.

**The margins are genuinely held.** Verified independently, not taken on the
author's word:

```
row-sum multiset preserved: True
every column sum preserved:  True
rows changed: 5418 of 5520   (50,000 swaps)
```

`only_a` and `only_b` are disjoint by construction, so the pooled re-deal
preserves every column sum exactly and every row size exactly. The chain is also
mixed: null mean for Kurux+Malto exclusive is 28.1 at 5,000 swaps and flat
(0.3–0.9) from 20,000 swaps to 1,000,000. At the reported 100,000 it is
stationary. **This half of the owner's press checks out and the PR's claim is
accurate.**

**The statistic does not.** The null destroys all phylogenetic structure, so it
answers "is there any structure here at all?", not "is *this* grouping real?".
For triples that makes it vacuous. Same null, same seed, 300 draws × 100,000
swaps:

| set | observed | null mean | p(≥obs) |
|---|---|---|---|
| **Tamil + Kurux + Malto** | **8** | 0.44 | **0.0033 (floor)** |
| Brahui + Kurux + Malto (`DMM-003`) | 7 | 0.00 | 0.0033 (floor) |
| Kui + Kurux + Malto | 5 | 0.01 | 0.0033 (floor) |
| Kannada + Kurux + Malto | 5 | 0.22 | 0.0033 (floor) |
| Gondi + Kurux + Malto | 4 | 0.06 | 0.0033 (floor) |
| Brahui + Kui + Kuwi | 2 | 0.02 | 0.0033 (floor) |
| Koraga + Kurux + Malto | 1 | 0.00 | 0.0066 |
| Manda + Kurux + Malto | 1 | 0.00 | 0.0066 |
| **Brahui + Toda + Kota** | **1** | 0.01 | **0.0166** |

Every triple tested is "significant". A single exclusive etymology reaches
p ≈ 0.017. Seven of nine hit the floor, including combinations no one has ever
proposed. `DMM-003`'s stated reasoning — *"the null expectation is effectively
zero: with Brahui in 269 entries, chance produces no such triples at all. So the
upper node is not nothing on this instrument"* — applies verbatim to
Brahui + Toda + Kota, where one etymology is observed and chance produces none.

And the observed count is not even first among its own family. Exclusive
Kurux+Malto+X for every X in the dictionary:

```
8  Tamil (3537)   7  Brahui (269)   5  Kui (938)   5  Kannada (2944)
4  Gondi (1306)   3  Malayalam      2  Tulu   2  Kolami   1  Parji …
```

**Kurux + Malto + Tamil = 8 > Kurux + Malto + Brahui = 7.** The unit's one
finding *for* the upper node ranks second behind a triple with no subgrouping
interpretation at all. This is not in the register.

The **pairwise** statistic behaves properly and should be kept. Brahui+Toda
(observed 1, null 0.37) gives p = 0.33 — correctly non-significant — while
Kurux+Malto (176 vs 0.78), Kui+Kuwi (66 vs 1.90) and Gadaba+Parji (35 vs 0.78)
all hit the floor. So `DMM-002` survives F-4 intact; `DMM-004` survives it
(and falls to F-3 instead).

**Repair.** `DMM-003` must not carry a p-value from this null. Report the
observed 7, the rank among Kurux+Malto+X (2nd of 24), the Tamil control, and a
calibration table of the same test on uncontroversial subgroups and on matched
implausible triples. `DMI-001`'s *"the null expectation is 0.00"* framing needs
the same treatment. The script should grow the control set as code so the next
reader cannot repeat this.

## F-5 — The validator change is stricter on the axis it argues, and **looser** on one it did not test

`VALIDATOR-FINDINGS-2026-09-07.md` gives a three-row negative test. It is
correct as far as it goes and it omits the case that matters. Full negative
test, old code and new, on a scratch tree with a ledger of `SRC-001`, `SRC-002`:

| row | `source_id` cell | old (main) | new (PR #22) |
|---|---|---|---|
| N-01 | `SRC-001; SRC-002` | fails (uninformative) | passes ✓ correct |
| N-02 | `SRC-001; SRC-999` | fails, names whole cell | fails, names `SRC-999` ✓ better |
| N-03 | `SRC-999` | fails | fails ✓ |
| N-06 | `SRC-001;SRC-001` | fails | passes ✓ correct |
| **N-04** | **`;`** | **fails** | **PASSES** ✗ |
| **N-05** | **` ; ; `** | **fails** | **PASSES** ✗ |

```
OLD: 6 failure(s)     NEW: 2 failure(s)   (only N-02's SRC-999 and N-03)
```

`source_ids("; ;")` returns `[]`, the resolution loop never executes, and check 2
passes because `"; ;".strip()` is truthy. **A `VERIFIED` row whose `source_id`
is nothing but separators now passes the whole validator.** The old rule caught
it. That is a real regression in a push-blocking gate, and it is the one thing
the PR asked the reviewer to look for.

One line fixes it:

```python
sids = source_ids(row.get("source_id"))
if (row.get("source_id") or "").strip() and not sids:
    fail(f"{rel}:{n}: source_id cell contains no identifier")
```

**A second gap, pre-existing and now load-bearing.** `REQUIRED_FOR_VERIFIED` is
enforced only `if col in fields`. `03-REGISTERS/domain-m-balochi-chronology.csv`
has no `retrieval_date` column at all, so **`DMC-004` is `VERIFIED` with no
retrieval date and the validator cannot see it.** A register can exempt itself
from `CLAUDE.md`'s requirement by omitting the column. This unit is the first to
ship a register that does.

**On the headline.** "43 failures to 0, none suppressed" is accurate. I get 42
running `main`'s validator against the PR head, and the missing one is the
class-2 prose-status cell already repaired — 42 + 1 = 43, and no register row
was deleted, no status promoted, no claim's standing changed. The change is a
net improvement. It is not yet strictly stricter.

**And the change is now needed on `main` regardless of this PR.** Running the
validator as it stands on `main`:

```
validate-registers: 53 failure(s)
```

Up from 43. PR #10 merged `domain-e-interpretations.csv` and
`domain-e-measurements.csv`, which carry ten more multi-valued `source_id`
cells of exactly the class-1 kind, and `main` does not have the class-2 fix.
So the push gate is currently blocking **every** push on `main`, not only this
branch, and it will keep doing so until `source_ids()` lands. That makes F-5 a
repair to make before merge rather than an argument against merging: the
direction of the change is right, its one-line gap is not.

## F-6 — `D-042` is marked `ANSWERED` with an owner answer, one commit after it was raised, and it is the decision that unblocked the author's own push

`11d0f8e` raises `D-042`. `34adb19`, the next commit, resolves it: *"The owner
answered D-042 with findings option 1 plus the class 2 fix."* The row carries
`status=ANSWERED`, `owner_answer`, `answer_date=2026-09-07`.

I make no claim that the owner did not answer. I note what the repository can
prove: nothing distinguishes an owner answer from a self-answer, and this is the
one decision in the unit whose effect was to loosen a push-blocking gate that
was blocking the author. `VALIDATOR-FINDINGS-2026-09-07.md` says of the same
change, before it was made, that *"amending the validator to make current rows
pass is exactly the move the repository forbids doing casually."*

Given F-5 — the amendment as shipped is looser in a way its own negative test
did not cover — the owner should countersign `D-042` before merge, and the repo
should decide what artefact records an owner answer. This is `AGENTS.md`
escalation territory, not a research finding.

---

# NON-BLOCKING

## F-7 — `DMM-005`'s 193 includes eight single-language entries

`confined_count()` counts entries whose attestation set is any non-empty subset
of {Brahui, Kurux, Malto}, singletons included:

```
176  (Kurux, Malto)      8  (Kurux,)       7  (Brahui, Kurux, Malto)
  1  (Brahui, Kurux)     1  (Brahui, Malto)                  total 193
```

Eight Kurux-only entries — forms with no cognate anywhere — are counted as
"confined to North Dravidian". They are not evidence of a subgroup in either
direction. `DMM-005`'s claim text is literally accurate ("attested only within
some subset"), but `DMM-006` compares the 193 against the BSOAS passage's *"a
list of words found only in Kurux and Malto, together with a few that these
share with Brahui (195 items)"* — a description of **shared** words. The
comparable figure is 185, not 193. Report both, or restrict the statistic to
|attestation| ≥ 2.

## F-8 — `BF-004`'s own `future_control` is not obeyed by `DMM-004`

`BF-004`, already in the log, requires: *"Any null result in this repository
reports the point estimate and its direction alongside the p-value, **and states
the power limitation**, before it is allowed to bear on a hypothesis."*

`DMM-004` is a null result and it bears on `DMI-001` and on `DMG-1`–`DMG-5`. It
gives the point estimate (1) and the null mean (0.19 / 0.18) — good — and states
no power limitation. It should, because the limitation is severe and precisely
statable. From the unit's own reported `p(≥1) = 0.1739`, the implied
λ ≈ 0.191, so **p(≥2) ≈ 0.016**: the test's entire detection threshold is *one
additional etymology*. "Indistinguishable from chance" here means "one etymology
short of significant" — which is what F-3 then demonstrates, since the current
encoding supplies that etymology for Malto.

This is the failure log's first `future_control` to be tested by a later unit,
and it was not checked. Under reviewer check 11, an unchecked control makes the
log decorative.

## F-9 — Asymmetric scrutiny between `DMM-003` and `DMM-004`

The PR states both halves are reported "at equal weight", and at the level of
prose they are. At the level of scrutiny they are not:

- `DMM-003` (favours the upper node): p-value from a null that does not
  discriminate (F-4); enumeration from a deprecated encoding (F-3); no control
  triple; no rank reported against Kurux+Malto+X; ranked "20 of 2,600" without
  noting that the 19 above it are all high-attestation South Dravidian
  combinations.
- `DMM-004` (runs against it): correctly reported, but with no power statement
  (F-8), and its conclusion reverses on the current file (F-3).

The prestige-bias section of the method doc catches the *instrument* exposure
well (`DMI-005`'s argument that a thin result from a favourably disposed
dictionary is worth more is genuinely good). The counter-narrative section
correctly refuses `BF-008`. Neither test caught the asymmetry in **statistical
scrutiny**, because both are aimed at claim content rather than at method. The
§8 tests as run in this unit cannot catch a bias that lives in a null model —
worth recording as their limit.

## F-10 — `DMM-018` is `VERIFIED` on a non-reproducible query with a partial denominator

The locator is a semantic-search query, a timestamp, and five DOIs. The claim is
a **ratio**: "8 passages across 5 articles, of which 5 passages from 3 articles
are HLA and mitochondrial DNA population genetics", and "15 passages across 10
articles, of which 6 passages from 4 articles are HLA". Only the genetics DOIs
are recorded. The other seven articles are not identified, so the denominator
cannot be checked, the classification of each hit is the author's judgement
rather than a retrieved fact, and a semantic ranker over a changing proprietary
corpus will not return the same set twice. The result payload is not committed.

The claim is almost certainly true and it is the evidential basis of `DMI-012`
and of the archive audit, which is why it needs a re-findable locator: list all
fifteen DOIs and commit the returned result set.

## F-11 — `DMM-017` is `VERIFIED` from 2 of 35 chunks, including a claim about the whole paper

The phonological content (*cu > s with Southwest Iranian, not *th > h or
*dz > d, Balochi not placeable in Southwest Iranian) is properly located in
chunks 0008 and 0019 and is `VERIFIED` correctly. The second sentence —
*"The paper's argument is that irregularity in West Iranian is not reducible to
lexical borrowing from Persian…"* — is a claim about a 31-page paper's overall
thesis made from 2 of its 35 chunks. Split the row: the located phonology stays
`VERIFIED`; the characterisation of the argument goes `PROVISIONAL` until the
other 33 chunks are read. `SRC-072` already records "2 of 35" honestly; the row
does not carry the consequence.

## F-12 — Four `VERIFIED` rows have locators that point at this repository, not at a source

`DMI-006` (`locator = DEP-012, DEP-015`), `DMI-011` (`SRC-058`; locator is a
constitution section), `DMI-012` (`DMM-009, DMM-018, DMM-021`), and `DMI-004`
(the script). Each is defended as "a statement about the state of this
repository, which is checkable" — a coherent category, and the defence is
honest. But then `source_id = SRC-059` / `SRC-054` is wrong: the source is the
repository, not the dataset. As written, a reader cannot distinguish "checked
against a retrieved source" from "checked against our own earlier row", which is
the distinction `VERIFIED` exists to carry. Either introduce an explicit
convention for repository-internal statements or move these to `PROVISIONAL`.

## F-13 — Self-report: "twenty of twenty-two measurement rows"

Method doc §12, prestige-bias, fourth paragraph: *"Twenty of twenty-two
measurement rows are sourced through connectors indexing Anglophone journal
publishing."* Counted from the file:

```
SRC-059 (GitHub clone):        7 rows  DMM-001..005, 008, 009
Consensus (SRC-060..071, 077): 13 rows
Scholar Gateway (SRC-054, 072): 2 rows
                        total  15 of 22, not 20
```

Reviewer check 12: counts are data-derived, never a running tally, *including in
Claude's own reports*. The disclosure it supports is right and does not need
inflating — 15 of 22, with 13 through a single free-tier connector, is the
stronger statement anyway because it names the concentration.

---

# The three the owner pressed on — direct answers

**1. The permutation null.** Margins: **confirmed sound**, independently. Row
sizes and per-language attestation are both preserved exactly, `only_a`/`only_b`
are disjoint so the re-deal cannot alter a column sum, and the chain is mixed at
the reported swap count (flat from 20,000 to 1,000,000). Brahui's thin
attestation cannot masquerade as a result and the PR's claim to have checked
rather than assumed this is accurate. *Artefact of how DEDR groups etymologies:*
**yes, for the triple statistic.** The null holds margins but destroys the
family tree, and for three-language sets that makes any observed count ≥ 1
significant — Kurux+Malto+Tamil (8) and Brahui+Toda+Kota (1) both reach the
floor. `DMM-003`'s p-value carries no information about Brahui. The pairwise
statistic is fine and `DMM-002` stands. One documentation defect: the register
and method doc say 100,000 swaps, the script's default is 200,000, and no JSON
output is committed — immaterial to the numbers (both are in the stationary
regime), but the exact invocation is not recoverable from the repository.

**2. `VERIFIED` rows resting on an abstract.** **None in the measurements
register** — the last one, `DMM-006`, was caught by the author's own self-audit
commit `3658c9e` and corrected to `PROVISIONAL`, correctly, with the reasoning
("a comparison can be no stronger than its weaker term") right. That check
passes. Three adjacent problems remain, none of them an abstract: `DMM-017`
generalises from 2 of 35 chunks (F-11); `DMM-018` rests on a non-reproducible
query with a partial denominator (F-10); four `DMI` rows are `VERIFIED` against
the repository's own rows (F-12). And six `VERIFIED` rows rest on a **retrieval
that happened** but is described as the printed dictionary rather than the table
(F-2), which is a different and larger problem than an abstract.

**3. Jambu — digitisation or scrape.** **A scholarly digitisation whose DEDR
component is, by its own documentation, a scrape — and the unit measured the
deprecated copy of it.** Jambu is a real academic database: named authors
(Arora, Farris, Basu, Kolichala), an arXiv paper (2306.02514), CLDF format,
per-source audit trails, reviewed samples, and elsewhere in the same README
scrupulous reuse-term notes ("CC-BY-4.0", "CC-BY-SA-4.0", "Reuse terms were not
stated on the source site", "copyrighted and is not redistributed"). Attribution
to Burrow and Emeneau is present and correct in `cldf/sources.bib`. So: not an
unattributed scrape.

But for DEDR specifically the README says the data was scraped from the DSAL
online edition — twice, once as a third party's 2013 SQL dump and once by
`parse.py` — the repository carries **no LICENSE file**, and DEDR is the one
major source with **no reuse-terms note**, while the bibliography's URL is
`dsal.uchicago.edu`, the host this project logs `EGRESS_BLOCKED` and holds under
`HOLD-002`.

What that does to every count derived from it:

- The chain is four links, not one: Burrow & Emeneau (Clarendon, 1984) → DSAL
  digitisation → 2013 third-party SQL scrape, hand-edited → CSV conversion,
  **upstream-deprecated**. `DEP-010` records one link; `main`'s `SRC-061`
  records two; neither records the deprecation.
- Every count is a count of that artefact. `main`'s own already-written rule
  covers it and is not met (F-2).
- The counts change on the current file, and one of them reverses (F-3).
- The "parse check with a published answer key" argument weakens: the deprecated
  file's residuals against the published 515/175/195 are −6/+1/−2; the current
  file's are +7/+7/+2. The better parse agrees *less* well, so near-agreement is
  not evidence of a faithful parse — it is evidence about which edition and
  counting convention the published figures used. `BF-009` correctly refuses to
  read the agreement as confirmation of the *subgroup*; it should also stop
  reading it as confirmation of the *parse*, which is the load-bearing use
  `DEP-010` and `DMM-006` both make of it.
- A rights question arises that no one raised: a copyrighted 1984 dictionary,
  re-encoded without stated terms, used as the load-bearing instrument of a
  published unit. `D-030` ("Which open licence does the evidence base carry?")
  is open and the repository has a `rights-steward`. This warrants an owner
  decision alongside `D-041`.

---

# What I looked for and did not find

So the next reviewer knows where I did not look.

- **Inherited material cited as evidence** (check 10). None. No `IH-` or `HD-`
  row is used as a source anywhere in the unit; `R-10`, `IH-031`, `IH-135` and
  `IH-156` are referenced only as things *not* to build on, which is correct.
- **Rejected reasoning returning** (check 14). None found. `DMG-2` is written
  precisely so that `R-10`'s rejection of migration-as-default is not read as a
  finding, and `DMB-023`'s refusal to infer from a 1980 title is respected —
  `SRC-065` is McAlpin **2003**, and the row says so.
- **Congenial correction** (check 13). The two self-audit corrections both run
  *against* the author's convenience (`DMM-006` demoted, `DMC-006` withdrawn).
  Neither moved a result toward a preferred reading. `BF-008`'s refusal of the
  genetic null is the strongest single act of discipline in the unit.
- **Proportional space** (check 6). No model received analytical space; all six
  read `CANNOT-GATE` with the criterion named. `DMG-6`'s decomposition note is
  correct and unusually clear. The `DMG-4` flag ("best served by what was
  retrieved") is disclosed rather than acted on, which is right.
- **Negative evidence** (check 7). Typed correctly throughout — `NOT PRODUCED`,
  `ABSENT DESPITE ADEQUATE SEARCH`, `NOT ACCESSIBLE` in `HOLD-005` and
  `DMI-008`, each bounded to a named instrument. "Unknown" is kept residual in
  `DMI-011`. I could not break this.
- **Translation standard** (check 8). Not engaged: the unit cites glosses from a
  dictionary rather than construing consequential ancient words, so §7's ten
  fields are not triggered. The seven etymologies in `DMM-003` are given as
  DEDR entry numbers with English glosses, which is the correct depth for a
  count. If any of the seven is ever quoted in public copy, §7 applies then.
- **Falsifiers** (check 9). Present for `DMM-002`, `DMM-003`, `DMI-001`–`003`,
  `DMC-001` and the models. Absent for `DMM-005` (the 260-of-269 figure the PR
  calls most load-bearing — `DMI-003` carries one for the interpretation but
  the measurement row has none), `DMM-008`, `DMM-009` and `DMM-018`.
- **Domain E collateral.** The `E-11` status edit is exactly what
  `VALIDATOR-FINDINGS` describes: `status` set to `VERIFIED`, the qualification
  moved to the head of `reason` rather than dropped, `eligible_for_extended_
  analysis` untouched. The guard is stated more prominently than before. No
  objection.
- **What I could not check.** Whether the owner answered `D-042` (F-6). Whether
  the Consensus abstracts quoted in `DMM-010`–`DMM-022` say what the rows say
  they say — that connector is not authorised in my session, so every
  `PROVISIONAL` row sourced through `SRC-053` is untested here, and `RA-006`
  says the exposure is real. Krishnamurti 2003, still unread, still the thing
  `HOLD-004` is right to stay open on.

---

# Order of repair

1. **F-1** — merge `main`, renumber all thirty-two identifiers, write the
   `DECISION-ID-MAP` rows, rewrite every reference including the PR body.
   Nothing else can be checked until the identifiers mean what they say.
2. **F-2** — reconcile with `main`'s `SRC-060`/`SRC-061`; adopt the two-remove
   rule; restate or demote the six DEDR `VERIFIED` rows; add the checksum.
3. **F-3** — re-measure on `dedr_new.csv`; re-derive `DMM-001`–`DMM-006`,
   `DMM-008`; state the `DMM-004` reversal on the face of the row.
4. **F-4** — strip the p-value from `DMM-003`; add the control table to the
   script and to the register.
5. **F-5** — one-line validator fix plus the missing negative-test rows;
   decide what to do about registers that omit `retrieval_date`.
6. **F-6** — owner countersigns `D-042`.
7. F-7 through F-13 — row-level, can travel together.

Re-review after repair. I do not treat this review as settled.

---

*Reviewer's note for the memory: the recurring failure class in this repository
is not fabrication — it is **identifier drift across branches** (third
occurrence: PR #17, PR #10, now PR #22) and **status inflation at the boundary
between an artefact and the thing it encodes**. Both are invisible to
`validate-registers.py` by construction. A pre-flight check that diffs a
branch's newly allocated identifiers against `origin/main` would have caught
F-1 and F-2 before the PR was opened.*
