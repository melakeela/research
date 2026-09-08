# Adversarial review — domain M, PR #22

**Reviewer:** independent agent, `.claude/agents/adversarial-reviewer.md`, nine checks.
**Unit under review:** `claude/domain-m-brahui-models-8kd31m` @ `253474b`.
**Merge base:** `bc5baf0`. **Review date:** 2026-09-07.
**Author:** a different agent. This reviewer produced none of the work and
edited none of it. Findings carry row IDs for the author to repair.

**Standing correction to the review brief.** The brief describes the unit as
"merged in PR #22". It is not merged. PR #22 is **open**, and
`mergeable_state` is **dirty** — it conflicts with `main` in seven files
(`02-SOURCES/access-ledger.csv`, `02-SOURCES/dependency.csv`,
`03-REGISTERS/domain-e-hypothesis-eligibility.csv`,
`04-AUDITS/BIAS-FAILURE-LOG.csv`, `04-AUDITS/REAUDIT-QUEUE.csv`,
`09-DECISIONS/OWNER-DECISIONS.csv`, `RESEARCH-QUEUE.md`). Several findings
below exist *because* `main` moved under the branch after it was cut, and they
become live at merge rather than being latent now. That distinction is stated
on each finding.

---

## Summary verdict

**Do not merge as it stands.** Six blocking findings, six substantive.

The arithmetic in this unit is sound. I re-derived every DEDR count from the
raw data with my own parser and my own curveball implementation, and every
headline number reproduces **exactly** — including the seven DEDR entry numbers
listed by hand in `DMM-003`. The permutation null does what the unit says it
does: both margins are held, the matrix genuinely randomises, and the null is
not a straw man. The self-audit rows (`BF-007`, `BF-008`, `BF-009`,
`DEP-010`–`DEP-015`) are the strongest work in the unit and several of them
caught real errors that would otherwise have shipped.

The unit fails on **which file it counted**, not on how it counted. Every DEDR
number in it derives from a file that the source repository marks *deprecated*,
that the source repository does not name as the provenance of its own DEDR
data, and that has not been touched upstream since June 2022. The current file
sits in the same clone, at the same pinned commit, and gives different numbers —
including a different membership for the seven etymologies of `DMM-003`. Nothing
in the unit records that a choice was made.

---

## Press point 1 — the permutation null

**Verdict: the null is sound and the p-values are reproducible. Two real
defects, one of them serious. The unit's own caveat row `DMI-004` is honest and
does most of the work required — but not all of it.**

### 1.1 What I did

I did not re-read the reported values. I wrote an independent parser and an
independent curveball implementation and re-ran the test from the raw data at
the pinned commit `dbae3102`, seed 20260907, 500 draws × 100,000 swaps.

### 1.2 The matrix genuinely randomises, and both margins hold — CONFIRMED

Checked directly on draw 1 rather than taken on trust:

| property | result |
|---|---|
| multiset of row sums (entry size) preserved | **identical** |
| every one of the 26 column sums (per-language attestation) preserved | **identical** |
| rows differing from the observed matrix after 100,000 swaps | **5,417 of 5,520** |

The unit reports 5,418 of 5,520 after 50,000 swaps; I get 5,417 after 100,000
on a different RNG stream. Same result. The trade is a correct curveball: `only_a`
and `only_b` are disjoint by construction, the pooled elements are conserved,
and each row is rebuilt at its original size. **`DMM-001`–`DMM-005` and
`DMI-004` are correct on this point and the check they claim to have run, ran.**

### 1.3 The five statistics reproduce — CONFIRMED

My independent run (500 draws; floor `1/501` = 0.0020) against the unit's
(2,000 draws; floor `1/2001` = 0.0005):

| statistic | obs | unit null mean | my null mean | unit 5–95th | my 5–95th |
|---|---|---|---|---|---|
| Kurux+Malto exclusive | 176 | 0.71 | **0.622** | 0–2 | **0–2** |
| Brahui+Kurux+Malto exclusive | 7 | 0.00 | **0.000** | 0–0 | **0–0** |
| Brahui+Kurux exclusive | 1 | 0.19 | **0.206** | 0–1 | **0–1** |
| Brahui+Malto exclusive | 1 | 0.18 | **0.126** | 0–1 | **0–1** |
| confined to North Dravidian | 193 | 5.38 | **5.214** | 2–9 | **2–9** |

Both floor statistics never reached in my run either. `DMM-004`'s
non-significant pair results replicate as non-significant (my p = 0.19 and
0.12 against their 0.17 both).

### 1.4 The null is NOT a straw man — CONFIRMED, and the unit under-claims

My working hypothesis on opening this was that a null destroying all
phylogenetic structure would be exceeded by every genuinely related pair,
making `p = 0.0005` uninformative. **That is not what the data show, and I
record it because it runs against the direction I was pressing.**

Of the 325 language pairs, 116 have a non-zero observed exclusive count, and
only **21** clear their own null at p ≤ 0.05. The 21 are almost exactly the
accepted subgrouping of Dravidian:

```
Malayalam–Tamil 359 (null 104.92)   Kurux–Malto 176 (null 0.62)
Kannada–Telugu  156 (null  69.43)   Kannada–Tulu 114 (null 49.19)
Kui–Kuwi         66 (null   1.76)   Gadaba–Parji  35 (null  0.75)
Manda–Pengo      24 (null   0.27)   Kota–Toda     24 (null  2.75)
Kolami–Naikri    16 (null   0.36)   ...
```

The test recovers known subgroups and rejects the other 95 non-zero pairs.
That is a validation of the instrument that is **available in the unit's own
data and is not reported**. Kurux–Malto's ratio to its null (176 : 0.62) is far
more extreme than Tamil–Malayalam's (359 : 104.92), because Tamil and Malayalam
are so well attested that the margins alone put them together constantly.
`DMM-002` is stronger than the unit claims for it.

**Finding AR-M-13 (minor, favourable).** `DMM-002` / `DMI-001` should record
the discriminating-power check: 21 of 325 pairs clear the null and they are the
accepted subgroups. This is the answer to "is the null a straw man", it is
computable from the committed script, and its absence leaves the unit's
strongest validation unstated.

### 1.5 BLOCKING — the triple test has no resolution

**Finding AR-M-07. Rows: `DMM-003`, `DMI-001`, method §4.2, PR body table.**

The null never produces a single Brahui–Kurux–Malto exclusive entry. I tested
the consequence directly:

| hypothetical observed value | p(≥) in my run |
|---|---|
| 1 | 0.0020 (floor) |
| 2 | 0.0020 (floor) |
| 3 | 0.0020 (floor) |
| **7 (actual)** | **0.0020 (floor)** |

**The p-value attached to `DMM-003` would be identical if there were exactly
one such etymology instead of seven.** The test carries zero information about
the magnitude of the observed count. It licenses "≥1 is surprising under a
structureless null" and nothing more.

Stated precisely: the gap between p(≥1) and p(≥7) is bounded by the frequency
with which the null reaches 1, and the unit's own reported null puts that at
zero (mean 0.00, 5th–95th 0–0). My 500-draw run reproduces a null maximum of
**0**. At 60 draws a single draw reached 1, giving p(≥1) = 0.0328 against
p(≥7) = 0.0164 — so the two are formally separable, by an amount that vanishes
at the 2,000 draws the unit actually ran. The separation is not a resolution.

This matters because `DMM-003` is the one finding in the unit pointing *toward*
the upper node, and the PR body asks reviewers (question 1) whether it is given
the weight it earns. The prose is careful — "seven is real and thin" — but the
statistical apparatus beside it implies a resolution it does not have. A reader
comparing `p = 0.0005` on the 7 with `p = 0.17` on the 1s will read a
twenty-five-fold difference in evidential strength that the test cannot
support; the correct reading is that the triple statistic is significant and
*unquantified*, while the pairwise statistics are non-significant.

Repair: state on `DMM-003` that the null's support for the triple is
insensitive to its magnitude between 1 and 7, so the p-value establishes
existence and not weight. The prose claim ("real and thin") survives; the
implied precision does not.

### 1.6 The entry-grouping artefact — the null cannot address it, and no row says so

**Finding AR-M-09. Rows: `DMI-004`, `DMI-005`, `DEP-010`, `DEP-013`.**

The brief asks whether the observed statistic is an artefact of how DEDR groups
etymologies into entries. The answer has two parts.

*Testable part — the direction is favourable to the unit.* Sub-entry treatment
does change the counts (quantified at AR-M-02 below), but merging sub-entries
can only enlarge an entry's language set, which destroys exclusivity rather than
creating it. Empirically, the encoding that *splits* sub-entries gives a
**higher** Kurux–Malto exclusive count (184) than the one that collapses them
(176). So on this axis the unit's numbers are conservative, not inflated. The
193 North-confined entries are small by construction (178 of size 2, 8 of size
1, 7 of size 3, mean 1.99), but 31.5% of all 5,520 entries are size ≤ 2, and
curveball holds row size fixed, so this is controlled.

*Untestable part — and this is the finding.* The curveball null permutes **over
entries, taking the entry as given**. But the entry is not a natural unit: it is
Burrow and Emeneau's editorial decision about what constitutes one etymology. If
the compilers habitually gave Kurux–Malto correspondences their own entry number
rather than folding them into wider entries, the 176 is a fact about
lexicographic practice, and **no permutation over entries can detect it, because
the permutation presupposes the very structure in question.**

`DMI-004` comes close — "it treats entries as exchangeable when in reality the
whole matrix is structured by descent and contact" — but names descent and
contact, not the compiler. `DMI-005` names compiler disposition, but only for
whether Brahui is *included*, not for how entries are *cut*. No row states that
the unit of analysis is itself an artefact of the instrument. Given that this
unit's central defence of its own instrument is `DMI-005`'s argument from
Emeneau's favourable disposition, the omission is load-bearing.

Repair: a row in `domain-m-interpretations.csv` stating that entry boundaries
are Burrow and Emeneau's editorial judgement, that the null conditions on them,
and that testing them requires DEDR's prose — which `HOLD-002` already blocks.

### 1.7 BLOCKING — the recorded procedure does not reproduce from the committed script

**Finding AR-M-08. Rows: `DMM-002`, `DMM-003`, `DMM-004`, `DMI-004`, method §4.1.**

Every one of those locators records **100,000 swaps per draw**. The committed
script sets:

```python
ap.add_argument("--swaps", type=int, default=200000)   # line 260
```

No invocation is recorded anywhere in the unit — not in the method document, not
in a commit message, not in a `--json` output file, because the script's
`--json` result was never committed. A reader running
`04-AUDITS/domain-m-dedr-north-dravidian.py` as committed executes a **different
procedure from the one the registers describe**, at twice the stated mixing.

This is not a cosmetic mismatch. `DMI-004` is `VERIFIED` on the ground that it
is "a statement about a procedure in this repository, checkable by reading and
re-running the script". The procedure it states is not the procedure the script
performs by default, and nothing in the repository records the flag that would
reconcile them.

Repair: either correct the four locators to 200,000, or record the exact
invocation and commit the `--json` report. Given `DMI-004` is `VERIFIED` on
reproducibility, the JSON should be committed regardless.

### 1.8 Mixing adequacy is asserted with a diagnostic that does not test it

**Finding AR-M-14 (minor). Rows: method §4.2, `DMI-004`.**

"5,418 of 5,520 rows differ from the original after 50,000 swaps — so it is
randomising and not merely shuffling within rows" establishes that the chain
*moved*. It does not establish that it *mixed*. At 100,000 swaps over 5,520 rows
each row is touched roughly 36 times; whether that is enough for the chain to
forget the observed matrix is a separate question, and each of the 2,000 draws
restarts from the observed matrix rather than continuing one chain. In practice
this is unlikely to matter — the observed values are so far into the tail that
under-mixing would bias *toward* the observed, and the results are extreme in
the opposite direction — but the claim as written overstates what the diagnostic
shows. A serial-correlation check across swap counts (e.g. null mean at 25k,
50k, 100k, 400k) would settle it in one run.

---

## Press point 2 — `VERIFIED` rows resting on something other than a retrieval

The unit found and corrected two itself: `DMM-006` (demoted to `PROVISIONAL`
because its published half rests on an abstract) and `DMC-006` (withdrawn
entirely to `HOLD-006`). Both corrections are correct and both run *against* the
unit's interest. I looked for the ones it did not find.

The unit's `VERIFIED` surface is 14 rows: `DMM-001`–`005`, `008`, `009`, `017`,
`018`; `DMI-004`, `006`, `011`, `012`; `DMC-004`. I traced every one to its
ledger row. Three fail.

### 2.1 BLOCKING — `DMI-011` is VERIFIED on a failed retrieval

**Finding AR-M-05. Row: `DMI-011`.**

`DMI-011` carries `source_id` **`SRC-058`**. `SRC-058` is the session egress
re-probe. Its own ledger fields read:

```
category          : infrastructure
retrieval_capable : no
access_status     : EGRESS_BLOCKED
```

A `VERIFIED` row is pointed at a ledger row recording that retrieval **failed**.
The validator passes it because `SRC-058` exists in the ledger and check 3 tests
existence, not character.

The row's *content* — that ancient Balochistan's speech zones remain unknown and
nothing in this unit narrows them — is true and is well typed (`NOT RECOGNIZED`,
`NOT EXCAVATED`). The defect is the citation: a claim about the state of this
repository is being sourced to a blocked-egress probe, which is not what
established it. Under `CLAUDE.md`'s inheritance rule — "only retrieval
promotes" — a row whose named source is a non-retrieval cannot be `VERIFIED` on
that source.

Repair: either re-source `DMI-011` to the registers whose absence it summarises,
or demote it. The same construction should be checked wherever else `SRC-058`
appears as a `source_id`.

### 2.2 BLOCKING — `DMI-012` is VERIFIED and assembles four clauses, two of which are abstract-level

**Finding AR-M-06. Row: `DMI-012` (and by inheritance the PR body's "The
archive, measured" section).**

`DMI-012` is `VERIFIED` on `SRC-054`, locator `DMM-009, DMM-018, DMM-021;
SRC-058`. Its four clauses:

| clause | rests on | that row's status |
|---|---|---|
| population genetics is the plurality of full-text matches | `DMM-018` | VERIFIED (but see AR-M-10) |
| CDIAL names Brahui once in 159,756 lines | `DMM-009` | VERIFIED — I reproduced it exactly |
| **"the Brahui data underlying the standard Dravidian etymological record is one scholar's publications plus eight hours of fieldwork"** | **`DMM-021`** | **PROVISIONAL** |
| Al-Burz is indexed but unreachable | `SRC-058` | EGRESS_BLOCKED |

Clause 3 rests **wholly** on `DMM-021`, which is `PROVISIONAL` because it is a
first-page extract returned by the Consensus connector from Emeneau 1997, an
article the unit states was "not opened beyond that". This is precisely the
class the brief asked me to find: a `VERIFIED` row one of whose load-bearing
clauses is carried by an abstract-level retrieval, with the status upgrade
happening in the move from measurement register to interpretation register.

It is also the most quotable sentence in the unit — "Bray plus eight hours"
appears in the PR body, in `DEP-011`, in `DMI-005` and in the method document's
archive audit — and it is the clause with the weakest retrieval behind it. That
combination is what check 3 (asymmetric scrutiny) exists to catch. The unit
scrutinised `DMM-006`'s published half hard and correctly. It did not apply the
same test to the extract that supports its most rhetorically effective finding.

Repair: demote `DMI-012` to `PROVISIONAL`, or split clause 3 out and let the
remainder stand. `DEP-011` inherits the same defect and should carry the same
qualification: its central quotation is from an unopened article's first page.

### 2.3 `DMM-018` and `DMI-012` are VERIFIED on a non-reproducible ranking

**Finding AR-M-10 (substantive). Rows: `DMM-018`, `DMI-012`.**

`DMM-018` is `VERIFIED` on `SRC-054`, and its claim is a count of what a
semantic search returned: "8 passages across 5 articles, of which 5 passages
from 3 articles are HLA and mitochondrial DNA population genetics".

The locator gives a timestamp and five DOIs, so the *articles* are checkable.
The *claim* is not: it is a statement about the ranked output of a proprietary,
unversioned, continuously-reindexed search service at one moment. No later
reviewer can re-perform it. Compare `DMM-001`–`005`, where the locator names a
pinned git commit and a script and I re-derived every number from scratch in an
afternoon.

This does not make `DMM-018` false — I have no reason to doubt it — but
`VERIFIED` in this repository means "re-checked against a named source with
locator and retrieval date", and the re-check is unavailable by construction.
The honest status is `PROVISIONAL` with the ranking's non-reproducibility named,
or `VERIFIED` narrowed to the five DOIs actually returned (which *are*
checkable) rather than to the proportion, which is not.

`RA-008` already gestures at the instability of connector reachability. This is
the same problem one level up: connector *results* are as unstable as connector
*reach*.

### 2.4 What I checked and could not break

- **`DMM-009`** — I re-ran the count on `data/cdial/cdial.csv`: **159,756 lines,
  Brahui 1, Balochi/Baluchi 3.** Exact. The `ABSENT DESPITE ADEQUATE SEARCH`
  typing and its bounding to this dictionary are correct.
- **`DMI-008`'s grep** — `baloch|baluch` returns **0** across `data/dedr/dedr.csv`,
  `data/dedr/params.csv` and `cldf/entry-texts.csv`, as claimed. I checked that
  `cldf/entry-texts.csv` is a real 1.5 MB file and not a Git-LFS pointer stub,
  because a grep of a pointer stub would return 0 for the wrong reason. It is
  real. (`cldf/forms.csv` and `data/form-identities.csv` *are* pointer stubs in
  this clone; neither is used by the unit.) I extended the grep to four files the
  unit did not check, including `dedr_new.csv`: also 0. The `NOT PRODUCED`
  typing holds and holds more broadly than claimed.
- **`DMM-017` / `DMC-004`** — genuinely full text, chunks 8 and 19 of 35, live
  DOI. The one unimpeachable publication row in the unit.
- **`DMM-006`, `DMM-007`, `DMM-010`–`016`, `019`–`022`** — all correctly
  `PROVISIONAL`, all with the abstract-level limitation stated on the row's face.
  `DMM-007`'s handling of the misattributed BSOAS passage (`BF-007`, `SRC-064`
  named "Unattributed", `access_status ATTRIBUTION_UNRESOLVED`) is exemplary.

### 2.5 The gate does not check most of this unit's evidentiary surface

**Finding AR-M-15 (minor, pre-existing). Row: `04-AUDITS/validate-registers.py`.**

Source-identifier resolution runs only inside `if status == "VERIFIED"`. A
`PROVISIONAL` row may cite an identifier that does not exist in the ledger and
the validator passes. I confirmed this with a fixture (`ZZ-005` below). This
predates D-042 and is not introduced by it — but 25 of the 45 rows in this
unit's four registers are `PROVISIONAL`, and they carry the whole of the
publication evidence. The gate covers the smaller half.

---

## Press point 3 — the Jambu re-encoding

**Verdict: it is an attributed scrape, not a scholarly digitisation, and the
unit measured the wrong file. The counts are faithful to the file used; the
file used is deprecated upstream.**

### 3.1 What Jambu is, from its own record

`SRC-059` describes `data/dedr/dedr.csv` as "a machine-readable re-encoding of
the Dravidian Etymological Dictionary" and credits "Arora, Farris, Basu,
Kolichala". That is accurate as far as it goes. Here is the rest.

**Who made it, and how.** `moli-mandala/data` README, §"DEDR", verbatim:

> "Originally, Suresh supplied a SQL database **scraped from the online
> version** (`data/dedr/dedr_new_entry_oct2013_edited.sql`) which was converted
> into a CSV at (`data/dedr/dedr.csv`). **These are now deprecated**."
>
> "The **current** CSV format of the DEDR is generated using
> `data/dedr/parse.py`, which **scrapes the website** and caches it in
> `data/dedr/dedr.pickle` ... The output is at `data/dedr/dedr_new.csv`."

The SQL file's own header confirms the chain:

```
-- phpMyAdmin SQL Dump / version 4.4.15.10
-- Generation Time: Sep 09, 2021 at 03:10 PM
-- Database: `suresh_dedr`
CREATE TABLE IF NOT EXISTS `dedr_new_entry_oct2013` (...)
```

So the chain of custody for **every DEDR count in this unit** is:

> Burrow & Emeneau 1984, Clarendon Press (print, in copyright)
> → DSAL Chicago digital edition (`dsal.uchicago.edu/dictionaries/burrow/`)
> → scraped into a private MySQL database (`suresh_dedr`), table snapshot **October 2013**
> → phpMyAdmin dump, **2021-09-09**
> → converted to `dedr.csv`, committed to Jambu **2022-06-18**
> → **deprecated upstream**
> → measured here as `SRC-059`.

Six hops. "Suresh" is almost certainly Suresh Kolichala, one of the four Jambu
authors `SRC-059` already names — so this is a scrape supplied by a named
co-author and linguist, not an anonymous one. That is materially exculpatory and
I record it as such: **"unattributed scrape" would be too strong.**

**Attribution.** Good. `cldf/sources.bib` carries a correct entry crediting
Burrow and Emeneau, Clarendon Press, 2nd edition, 1984, with the DSAL URL.
`cldf/references.csv` names the editor (Aryaman Arora) and records `OCR: No`.
The upstream authors are properly credited.

**Licence.** None. There is **no `LICENSE`, `COPYING` or `NOTICE` file anywhere
in the repository**, and `cldf/Wordlist-metadata.json` contains **zero**
occurrences of `license`, `dc:license`, `rights` or `dc:rights` — unusual for a
CLDF dataset, where a licence field is conventional. The underlying dictionary
is in copyright and the DSAL edition is a licensed digital edition. Jambu itself
is scrupulous about this elsewhere (the README records, for other sources, "The
publisher PDF is not redistributed; its SHA-256, rights note..."; "The scanned
volume is copyrighted and is not redistributed"). For DEDR it makes no such
statement.

**Answer to the brief's question.** It is a **scholarly project's unlicensed
scrape**: correctly attributed at the bibliographic level, built by a named
linguist by scraping DSAL, published with no licence, and — for the specific
file used here — deprecated by its own maintainers.

### 3.2 BLOCKING — the unit measured the deprecated file

**Finding AR-M-01. Rows: `SRC-059`, `DEP-010`, `DMM-001`–`005`, `DMM-008`,
`DMM-009`, `DMI-001`, `DMI-003`, `DMI-006`, method §4.1, PR body throughout.**

Jambu's own `cldf/references.csv` declares, for the `dedr` record:

```
Provenance : data/dedr/dedr_new.csv
```

Jambu names `dedr_new.csv` as the provenance of its DEDR data. The unit measured
`dedr.csv`, which Jambu names as the provenance of nothing and marks deprecated.

File histories inside the pinned clone:

| file | last upstream commit | lines |
|---|---|---|
| `data/dedr/dedr.csv` (measured) | **2022-06-18** "more data and model code" | 68,807 |
| `data/dedr/dedr_new.csv` (current) | **2026-08-23** "Expand comparative sources and rebuild CLDF" | 76,303 |

`SRC-059` records the clone "pinned at commit `dbae3102` dated 2026-08-30". That
is true of the *repository* and false of the *data*: the file measured has not
moved since June 2022. The pin creates an appearance of currency that the file
does not have.

Nothing in `SRC-059`, `DEP-010`, the method document or the PR body records that
`dedr.csv` is one of two DEDR encodings in the clone, that it is deprecated, or
that a choice was made. `DEP-013` does anticipate the *mechanism* — "the
expected consequence of edition and encoding: which DEDR edition, whether
sub-entries are counted" — but treats it as an untestable residual while the
alternative file sat in the same directory.

### 3.3 BLOCKING — what the counts do on the file Jambu declares

**Finding AR-M-02. Rows: `DMM-001`, `DMM-002`, `DMM-003`, `DMM-005`, `DMM-006`,
`DMI-003`, method §4.2 and §4.4, PR body table.**

I re-ran the same measurements on `dedr_new.csv` at the same pinned commit,
rolling Jambu's dialect lects up to base languages via `cldf/dialects.csv`.

| statistic | unit (`dedr.csv`) | current (`dedr_new.csv`) | Δ |
|---|---|---|---|
| entries | 5,520 | **5,619** | +99 |
| attested languages | 26 | **32** | +6 |
| Brahui attestation | 269 | **274** | +5 |
| Kurux attestation | 775 | **794** | +19 |
| Malto attestation | 704 | **724** | +20 |
| Kurux+Malto exclusive | **176** | **184** | +8 |
| Brahui+Kurux exclusive | 1 | 1 | — |
| Brahui+Malto exclusive | **1** | **2** | +1 |
| Brahui+Kurux+Malto exclusive | 7 | 7 | — (**but see below**) |
| confined to North Dravidian | **193** | **199** | +6 |
| Brahui reaching outside North Dr. | **260 of 269** | **264 of 274** | — |
| Kurux & Malto co-occurring | **509** | **527** | +18 |

**The seven etymologies of `DMM-003` are not the same seven.** `DMM-003` lists
them by DEDR number, which is exactly the right practice and is what makes this
checkable:

- unit: 1419, 1558, 2189, 2244, 2278, 3149, **5131**
- current: 1419, **—**, 2189, 2244, 2278, 3149, 5131, **4428**

**DEDR 1558 ("embrace / carry under the arm") is not exclusive to North
Dravidian in the current encoding, and DEDR 4428 is.** DEDR 4428 is named in
Jambu's own `data/dedr/abbrevs.py` under `source_markup_repairs` — an entry with
an unclosed `<b>` tag in the source HTML that the current parser repairs and the
deprecated one did not. So at least one difference is a *known, documented parse
defect* in the file the unit measured, corrected upstream, in an entry that
lands directly on this unit's headline finding.

`DMI-003`'s "260 of 269" — described in the unit as "the single most
load-bearing number" — becomes 264 of 274. The *interpretation* is unaffected
(96.7% versus 96.4%), and I say so plainly: **this finding does not overturn any
conclusion in the unit.** What it overturns is the unit's entitlement to state
these as measured facts without naming the encoding, and it falsifies one of the
seven named etymologies, which is a checkable claim about the world.

*Honest counter-point.* The deprecated file matches the **published** counts
better than the current one does:

| published | deprecated (used) | current | closer |
|---|---|---|---|
| K&T 515 shared etyma | 509 (Δ −6) | 527 (Δ +12) | deprecated |
| K&T 175 isolated | 176 (Δ +1) | 184 (Δ +9) | deprecated |
| BSOAS 195-item list | 193 (Δ −2) | 199 (Δ +4) | deprecated |

A 2013 DSAL snapshot is plausibly closer to printed DEDR than a 2026 re-scrape
that has been augmented to 32 lects with sub-entries split. So there is a real
argument that `dedr.csv` is the *more faithful* instrument for this purpose.
**That argument is not made anywhere in the unit**, and it cannot be made
retrospectively as though it had been: the unit shows no awareness that a second
file exists. It also cuts at `DMM-006`, which uses the published-count agreement
as evidence "that DMM-001 to DMM-005 are reading Burrow and Emeneau correctly
rather than reading a corrupted file" — on the current encoding the same test
agrees worse on all three, so the test is measuring edition alignment, not parse
fidelity, which is a different claim from the one `DMM-006` makes for it.

### 3.4 BLOCKING — the same dataset already has a source_id on `main`, from a unit that used the other file

**Finding AR-M-03. Rows: `SRC-059`, `DEP-010`, `DEP-012`, `DMI-006`, method §11.**

`main` (after PR #10) already carries:

```
SRC-061 : DEDR (Burrow and Emeneau 1984, 2nd ed.) as re-parsed in JAMBU data/dedr/
          dedr.csv 1d91f819b9af2c530ba6688a089a775d4bd6bcaa7c8e30e90dacdcce3758943e
          (5251799 bytes, 68807 reflex rows) ... Editor Aryaman Arora, OCR No
```

I ran `sha256sum` on the file in my clone: **`1d91f819b9af...`, byte-identical.**
Domain E and domain M hashed the same file.

At merge the repository will hold **two source identifiers for one dataset**
(`SRC-059` and `SRC-061`) with different provenance descriptions. That is the
exact hazard `02-SOURCES/dependency.csv` exists to prevent, and it will be
invisible to the validator, which checks that identifiers resolve, not that they
are distinct sources.

Worse, domain E did the DEDR-digitisation work already and reached further:

- `04-AUDITS/domain-e-dedr-digitisation-check.py` on `main` **defaults to
  `dedr_new.csv`** — the current file. The repository's established convention
  for reading Jambu's DEDR is the file domain M did not use.
- Its docstring states "This unit's DEDR came through JAMBU, which **re-parses
  the DSAL digitization**" — domain E recorded the scrape relationship that
  `SRC-059` and `DEP-010` omit.
- `IC-E-001` records a **10.3% disagreement between two DEDR digitisations**.
- `IC-E-002` records the published Brahui figure moving **from 191 of 262 (73%)
  to 223 of 273 (82%)** between them — a Brahui denominator of **273**, against
  domain M's **269**, for the same dictionary in the same repository.
- `D-038` on `main` — "Should the-northwest-cousin.html name the DEDR
  digitization it counted and carry the range between the two?" — is an **open
  owner decision about precisely this question**, blocking published copy.

Method §11 ("Checking this repository against itself", step 13) checks only
against PR #16's `DMB-` rows. It does not mention domain E.

**Mitigation, stated fairly:** domain M was cut from `bc5baf0`, before PR #10
merged. The author could not have read this at branch time. But the PR is open
and must be merged, and at merge the repository will assert two different Brahui
denominators from one dictionary with no row reconciling them. That needs an
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv` row (`IC-M-00n`) and a `DEP-` row tying
`SRC-059` to `SRC-061`, and `DMM-001` needs to name the encoding in its claim
text so the two are distinguishable on their face.

### 3.5 What this does to each count — summary for the author

| count | verdict |
|---|---|
| 5,520 entries / 26 languages / 68,808 lines / 0 unparsed | **exact** on the file used; I reproduced all four independently |
| 269 / 775 / 704 attestations | **exact** on the file used; 274 / 794 / 724 on the current file |
| 176 Kurux+Malto exclusive, rank 2 of 325 | **exact**, rank confirmed; 184 on the current file |
| 7 Brahui+Kurux+Malto exclusive | count exact; **membership wrong** — 1558 out, 4428 in, on the current file |
| 1 and 1 pairwise (DEDR 3358, 3861) | **exact**, both entry numbers confirmed; Brahui+Malto becomes 2 on the current file |
| 193 confined to North Dravidian | **exact**; 199 on the current file |
| 260 of 269 | **exact**; 264 of 274 on the current file — interpretation unchanged |
| 509 / 176 / 193 vs published 515 / 175 / 195 | **exact**; 527 / 184 / 199 on the current file, i.e. agreement is edition-dependent |
| 604 CDIAL↔DEDR cross-references, 118 resolving, 12 Brahui | not re-derived (accepted; same file, same parse, arithmetic verified by inspection) |
| CDIAL 159,756 lines, Brahui 1, Balochi 3 | **exact**, re-derived |

**No count in this unit is arithmetically wrong.** Every one is
encoding-dependent and none says so.

---

## The D-042 validator change

**Verdict: the gate is sound and catches what the brief asked me to test. The
claim made for it is false, and the identifier it was allocated collides with
`main`.**

### 4.1 Negative test — a bad identifier in a multi-valued cell IS caught

I built a fixture register outside the repository and ran both the new validator
and the pre-D-042 one from `bc5baf0` against it.

| fixture | cell | new (D-042) | old |
|---|---|---|---|
| `ZZ-001` | `SRC-059; SRC-054` — both real | pass | **FAIL** (false positive) |
| `ZZ-002` | `SRC-059; SRC-999` — second invented | **FAIL** ✓ | FAIL |
| `ZZ-003` | `SRC-999; SRC-059` — first invented | **FAIL** ✓ | FAIL |
| `ZZ-004` | `SRC-999` — single invented | **FAIL** ✓ | FAIL |
| `ZZ-005` | `SRC-999` on a **PROVISIONAL** row | pass | pass |
| `ZZ-006` | `SRC-059, SRC-999` — comma, not semicolon | **FAIL** ✓ | FAIL |

The new validator's messages name the offending identifier:
`source_id SRC-999 not in access ledger`. **A bad identifier hidden inside an
otherwise-good multi-valued cell is caught, in either position, and a
comma-separated cell does not slip through.** The gate does its job.

### 4.2 SUBSTANTIVE — "stricter, not looser" is false

**Finding AR-M-12. Row: `04-AUDITS/validate-registers.py` module docstring;
`D-042`; PR body, reviewer question 4.**

The docstring asserts:

> "Splitting on ';' and resolving each one is therefore **STRICTER** than what
> it replaces, not looser"

The test table refutes this. The new rule's rejection set is a **strict subset**
of the old rule's: it rejects nothing the old rule accepted, and accepts one
class the old rule rejected (`ZZ-001` — all-good multi-valued cells). By the
ordinary meaning of strictness on a gate, the change is **more permissive**.

**The unit's own document already contains the refutation.**
`VALIDATOR-FINDINGS-2026-09-07.md` prints a negative-test table whose first row
reads:

| row | cell | old | new |
|---|---|---|---|
| all four identifiers real | `SRC-001; SRC-002` | **fails** (uninformative) | **passes** |

That is the permissive direction, stated by the author, one line below the
sentence claiming there isn't one. My independent fixture reproduces their table
exactly. The disagreement is not about the behaviour — we measured the same
behaviour — it is that the prose draws the wrong conclusion from it.

**Corroborated on the real tree, not just a fixture.** Running the *old*
validator against `main` today produces 53 failures, of which 52 are
`source_id` failures. I checked every identifier appearing in them
(`SRC-019`, `SRC-021`–`024`, `SRC-026`, `SRC-032`, `SRC-037`, `SRC-040`,
`SRC-043`, `SRC-046`, `SRC-047`, `SRC-053`, `SRC-059`–`SRC-065`, `SRC-068`)
against the ledger: **every one resolves individually. All 52 are false
positives of the `ZZ-001` class.** So "43 failures to 0" was achieved almost
entirely by the permissive direction — which is the right outcome, obtained for
a reason the docstring will not name.

The accurate claim is the one the docstring's *next* sentence already makes and
which is true: the new rule is **more discriminating** — "a cell containing one
good identifier and one bad one now fails on the bad one instead of failing
uninformatively on both" — and it eliminates a false-positive class. That is a
good change and I would not have it reverted. But the PR body invites the
reviewer to read this as a change to the gate and asks whether it is stricter.
It is not, and "43 failures to 0, none suppressed" was achieved precisely by the
permissive direction: those 43 were the false positives at `ZZ-001`.

Repair: replace "STRICTER than what it replaces, not looser" with the accurate
characterisation — strictly more permissive on all-valid multi-source cells,
identical on every cell containing an invalid identifier, and more
discriminating in what it reports. Nothing else about the change needs to
change. The same sentence appears in `VALIDATOR-FINDINGS-2026-09-07.md` and
needs the same repair.

### 4.2b The class 2 fix is correct — I tried to break it and could not

I expected to find that clearing the gate had cost a caveat. It did not.
`03-REGISTERS/domain-e-hypothesis-eligibility.csv` row `E-11` had a `status`
cell carrying prose (`"VERIFIED as a measurement; not a claim about origins"`),
outside `CLAUDE.md`'s closed vocabulary. The unit identified it, **refused to
fix it unilaterally** on the ground that the row is the constitution §4.E
"unknown is residual" guard and "changing its status field without the owner
seeing the change is how a guard gets quietly loosened", escalated it, and only
then made the change. I checked the result: `status` is now `VERIFIED` and the
qualification sits at the **head** of the `reason` cell, in capitals —
"VERIFIED AS A MEASUREMENT, NOT AS A CLAIM ABOUT ORIGINS" — with
`eligible_for_extended_analysis` still reading `NOT-A-HYPOTHESIS — a residue,
never a rival explanation`. The guard is intact and more prominent than before.
The claim "none of them suppressed ... no status was promoted" holds. **No
finding.**

One thing a reviewer cannot check from the tree: `D-042`'s row reads
`status: ANSWERED` with an `owner_answer` and an `answer_date` of 2026-09-07.
Whether the owner in fact answered within that session is not verifiable from
the repository, and I am not alleging that they did not — I note only that an
`ANSWERED` decision that unblocked the unit's own push gate is the one class of
decision a later auditor has no way to confirm, and that this is a property of
the register format rather than of this unit.

### 4.3 BLOCKING — `D-038` to `D-042` are all double-allocated

**Finding AR-M-04. Rows: `D-038`, `D-039`, `D-040`, `D-041`, `D-042` in
`09-DECISIONS/OWNER-DECISIONS.csv`; every reference to them in the unit.**

`CLAUDE.md` makes `OWNER-DECISIONS.csv` authoritative for `D-` identifiers and
requires the next free one be taken from the CSV. `main` merged PR #10 after
this branch was cut, and PR #10's merge reassigned domain E's rows upward.
`09-DECISIONS/DECISION-ID-MAP.csv` on `main` records the result:

| id | on `main` (via PR #10) | on this branch |
|---|---|---|
| D-038 | Two DEDR digitizations disagree, and one is published | scite connector upgrade |
| D-039 | Do the twelve mandated files accumulate across domains? | University of Balochistan hosts allowlist |
| D-040 | Are measurements and interpretations separated? | citing a passage with wrong metadata |
| D-041 | Is the git proxy's anonymous lane the standing channel? | consent for community-authored Brahui material |
| D-042 | Domain E under a GitHub-only egress policy? | the register gate / this validator change |

**All five collide.** At merge, `OWNER-DECISIONS.csv` will carry each identifier
twice, and the validator's own `decision_ids()` check will fail with
`D-042 appears 2 times` — the gate this unit repaired will block on the unit
that repaired it.

The blast radius is wide because these identifiers are cited throughout:
`D-040` in `BF-007` and `SRC-064`; `D-041` in `HOLD-006`, `DMG-2` and `DMI-011`;
`D-039` in the PR body's domains request; `D-042` in the validator docstring and
in `VALIDATOR-FINDINGS-2026-09-07.md`. After merge every one of those references
resolves to two rows, which is the exact failure `DECISION-ID-MAP.csv` exists to
prevent.

Note the irony worth acting on: **`main`'s `D-038` is "Two DEDR digitizations
disagree, and one is published."** The repository already has an open owner
decision on the question this review's press point 3 raises. Domain M's
`D-038` should be renumbered *and* domain M should be reconciled against
`main`'s `D-038`, `IC-E-001` and `IC-E-002`.

Repair: on merging `main`, reassign this branch's five decisions to the next
free identifiers above `main`'s highest allocation, rewrite every in-tree
reference, and add a `DECISION-ID-MAP.csv` row per reassignment with the
old→new mapping. `main` keeps every identifier it has allocated. (This review
deliberately allocates no replacement identifiers: allocation comes from
`OWNER-DECISIONS.csv` at merge time, and a reviewer writing candidate numbers
into an audit document is how the collision happened in the first place.)

---

## Remaining checks

**Falsifiers (spec check 9) — AR-M-11, substantive.** Method §10 carries a good
falsifier list. **No register row carries a falsifier**: the four domain M
registers contain zero instances of "would change" or "falsif", and have no
falsifier column. Step 12 asks that accepted claims record what would change
them; a falsifier that lives only in an audit document travels separately from
the claim and will be lost the moment a row is quoted elsewhere. `DMM-003`
especially needs its falsifier on its face, given AR-M-02.

**Bridges (spec check 4) — clean.** `DMI-009` and `BF-008` handle the
genetics/linguistics bridge correctly and the refusal to let `DMM-020`
corroborate `DMM-004` is exactly right — it would have been the most persuasive
available move and the unit declined it. `DMI-002` keeps shared vocabulary and
shared descent apart. The attestation gradient is respected: no hypothetical
donor is treated as symmetrical with the attested record.

**Chronology and geography (spec check 5) — clean and unusually good.**
`domain-m-balochi-chronology.csv` has a `which_of_the_four_histories` column and
uses it to separate `DMC-002` (a confederacy and a regnal date) from language
history. `DMC-001`'s 500-year window is reported as a window and its hedge
("generally thought") is on the row.

**Proportional space (spec check 6) — clean.** All six models read
`CANNOT-GATE`, never `FAIL`, and none receives analytical space. `DMG-4` is
flagged as best-served-by-the-evidence *without* being advanced. `DMG-6` is
flagged as needing decomposition before it can be gated at all. The refusal to
let a documented modern westward Brahui migration support a medieval eastward
migration model is correct and was the most quotable thing available.

**Negative evidence (spec check 7) — clean.** Three absences typed separately
and correctly in `DMI-008` (`NOT PRODUCED` / `NOT ACCESSIBLE` / `ABSENT DESPITE
ADEQUATE SEARCH`), and I verified the `NOT PRODUCED` typing empirically across
more files than the unit checked. "Unknown" is not used as a rival explanation
anywhere.

**Translation standard (spec check 8) — not applicable.** No consequential
ancient word is analysed and none of the audited English categories (*race,
tribe, slave, barbarian, fort, religion, caste, civilization, invasion,
indigenous*) is used load-bearingly. Correctly, this unit's evidence is lexical
counts, not textual interpretation. Note that the PR body's "Not opened" section
flags Nandi's *fort* argument for domain J — that is where check 8 will bite.

**Inherited material (spec check 10) — clean.** No `IH-` or `HD-` row is cited
as evidence. `IH-236` is referenced in `DMG-2` as a pointer to an unread source,
which is its correct use.

**Failure log controls (spec check 11) — mostly obeyed.** `BF-007`→`RA-006`,
`BF-008`→`RA-007` are properly wired. `BF-009` has an **empty** re-audit column
where the other two have one; if `BF-009`'s control ("when a measurement
reproduces a published number, ask first whether the publication took its number
from the same source") is general, earlier work needs a queue row — and AR-M-02
shows the control was not applied to the encoding question. Minor: **AR-M-16**.

**Self-report (spec check 12) — accurate.** I counted rather than accepting
stated figures. 26 ledger rows added (`SRC-053`–`SRC-078`), matching. Register
rows: measurements 22 (9 VERIFIED / 13 PROVISIONAL), interpretations 12 (4/8),
model gates 6 (all CANNOT-GATE), chronology 5 (1/4). The PR body's claims about
what was refused, held and gated all check out against the files. The PR body
does not overstate its registers — which, given how much it claims, is itself
worth recording.

**Congenial corrections (spec check 13) — clean, and this is the unit's
strongest feature.** Both self-audit corrections run **against** the unit's
interest: `DMM-006` demoted, `DMC-006` withdrawn. `BF-008` refuses a corroboration
that would have been convenient. `BF-009` refuses three reproductions as
confirmation. `DEP-012` and `DEP-015` volunteer that this unit is not an
independent replication of PR #16. I looked specifically for a correction moving
toward the preferred reading (`BF-004`'s pattern) and did not find one.

**Rejected reasoning (spec check 14) — clean.** `R-10` (late migration as
default) is explicitly honoured in `DMG-2`, including the harder half — that
being disfavoured is not a reason to gate it out either. No `REJECTED` row was
deleted or touched.

---

## Findings index

| ID | Severity | Rows | Finding |
|---|---|---|---|
| AR-M-01 | **BLOCKING** | `SRC-059`, `DEP-010`, `DMM-001`–`005`,`008`,`009` | Measured `dedr.csv`, deprecated upstream and not Jambu's declared provenance; scrape chain and absent licence unrecorded |
| AR-M-02 | **BLOCKING** | `DMM-001`–`006`, `DMI-003` | Counts differ on the current encoding; DEDR 1558 out, 4428 in, among `DMM-003`'s seven |
| AR-M-03 | **BLOCKING** | `SRC-059`, `DEP-010`, method §11 | Duplicates `main`'s `SRC-061` (same SHA-256); contradicts domain E's Brahui denominator; `IC-E-001/002` and `main`'s `D-038` not reconciled |
| AR-M-04 | **BLOCKING** | `D-038`–`D-042` | Five-way decision-ID collision with `main`; will break the validator's own check 5 at merge |
| AR-M-05 | **BLOCKING** | `DMI-011` | `VERIFIED` on `SRC-058`, whose `access_status` is `EGRESS_BLOCKED` |
| AR-M-06 | **BLOCKING** | `DMI-012`, `DEP-011` | `VERIFIED`; clause 3 rests wholly on `DMM-021`, `PROVISIONAL`, an unopened article's first page |
| AR-M-07 | substantive | `DMM-003`, `DMI-001` | Triple test has no resolution: p(≥1) = p(≥7) = floor |
| AR-M-08 | substantive | `DMM-002`–`004`, `DMI-004` | 100,000 swaps recorded; script defaults to 200,000; no invocation or JSON committed |
| AR-M-09 | substantive | `DMI-004`, `DMI-005` | Entry boundaries are a Burrow–Emeneau editorial artefact the permutation conditions on and cannot test; no row says so |
| AR-M-10 | substantive | `DMM-018`, `DMI-012` | `VERIFIED` on a non-reproducible connector ranking |
| AR-M-11 | substantive | all four registers | Falsifiers live only in the method document, not on rows |
| AR-M-12 | substantive | `validate-registers.py`, `D-042` | "STRICTER, not looser" is false; rejection set is a strict subset of the old rule's |
| AR-M-13 | minor | `DMM-002`, `DMI-001` | Discriminating-power check (21 of 325 pairs) available and unreported — favourable to the unit |
| AR-M-14 | minor | method §4.2 | "5,418 rows differ" shows movement, not mixing |
| AR-M-15 | minor, pre-existing | `validate-registers.py` | `PROVISIONAL` rows' `source_id`s are never resolved; that is 25 of 45 rows here |
| AR-M-16 | minor | `BF-009` | Empty re-audit column where `BF-007` and `BF-008` have one |

---

## Where I did not look

So the next reviewer knows where the record is untested:

- **`DMM-008`'s CDIAL↔DEDR cross-reference counts** (604 / 118 / 12 / 30 / 23 /
  40) were not independently re-derived. Same file, same parse, and the code
  reads correctly, but I did not re-run it.
- **`domain-m-brahui-position.csv`** (`DMB-` rows, PR #16) is not modified by
  this PR and I reviewed it only where domain M's new rows depend on it.
- **The publication content of the `PROVISIONAL` rows.** I verified their
  *status* and their *locators*; I did not attempt to retrieve Kobayashi &
  Tirkey, McAlpin, Korn, Spooner, Badalkhan, Smirnitskaya, Nair, Kolipakam,
  Singh or Ahmed to check that the abstracts say what the rows say they say.
  `RA-006` is open for exactly this reason and this review does not close it.
- **`HOLD-005` and `HOLD-006`** were read for their typing, not audited against
  the rights and consent framework. `HOLD-006` and `D-041` are the rights
  steward's, not this reviewer's.
- **Whether Jambu's scrape of DSAL is within DSAL's terms of use.** I established
  that it is a scrape, that attribution is present and that no licence is
  declared. Whether that is lawful acquisition is an owner escalation under
  `CLAUDE.md`'s stopping rules, not a reviewer's finding.

## What the two §8 tests caught here

**Prestige-bias challenge.** Caught AR-M-01/02/03: DEDR is the canonical
instrument, and "a machine-readable re-encoding of Burrow and Emeneau" was
accepted as a description without the six-hop custody chain behind it being
opened. The prestige of the *dictionary* transferred to the *file*. It cannot
catch whether Burrow and Emeneau's cognate judgements are themselves right —
`DMI-005` correctly says nothing here can.

**Preferred-counter-narrative challenge.** Caught little, because the unit ran
this test on itself effectively: `BF-008` refuses the genetic null, `DMG-2`
refuses to gate out late migration merely because the inherited record
disfavours it, and the modern westward Brahui migration is explicitly withheld.
The one residue is AR-M-06 — the "Bray plus eight hours" finding is the unit's
most rhetorically effective archive-audit result, it is congenial to the
project's decolonial framing, and it rests on the thinnest retrieval in the
`VERIFIED` set. That is the direction this test exists to check.

---

*Reviewer's note.* This unit's failure is not carelessness. It is the specific
failure of trusting a well-made derived artefact one hop further than its own
maintainers do. `DEP-010` gets the relationship between Jambu and DEDR exactly
right — "it is not an independent witness to Dravidian etymology; it is DEDR,
parsed" — and then does not ask which parse. The repair is small and entirely
mechanical: re-run on `dedr_new.csv`, report both, and name the encoding in
`DMM-001`'s claim text. The conclusions survive it.
