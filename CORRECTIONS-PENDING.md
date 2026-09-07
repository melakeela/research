# Corrections pending on four live pages

**Written:** 2026-09-07
**Unit type:** corrections brief. Report only.
**Branch:** `claude/four-pages-corrections-pending-gqk41q`

Four pages on MelaKeela publish figures or completeness claims that this
repository's registers do not support in the form published. This document
states, for each, what the page asserts, what the verified record says, which
owner decision governs, and a replacement draft in the shape step 14 requires.

**Nothing here edits a page.** `CLAUDE.md` forbids writing site code in this
repository, and the four changes are four separate approvals. Each brief is
written to be approved or refused on its own.

---

## 0. Reading notes, before the briefs

### 0.1 Two of the files this unit was pointed at do not exist

| Asked for | Status |
|---|---|
| `03-REGISTERS/rigveda-pur-family.csv` | exists, read, 28 claim rows |
| `03-REGISTERS/domain-e-measurements.csv` | exists, read, 30 claim rows |
| `03-REGISTERS/domain-m-measurements.csv` | **has never existed** in any commit reachable from any ref |
| `06-BRIEFS/site-reconciliation.md` | **has never existed** in any commit reachable from any ref |
| `06-BRIEFS/rv01-reconciliation.md` | exists, read, 478 lines |

Checked with `git log --all --diff-filter=ADR` over both paths: no add, delete
or rename. They were not moved; they were never written. Where a domain M
measurement or a site reconciliation was needed, these were used instead and
are named at the point of use:

- domain M — `03-REGISTERS/domain-m-brahui-position.csv`, 26 rows, the register
  that actually carries the Brahui position work.
- site reconciliation — `04-AUDITS/INTERNAL-CONTRADICTIONS.csv` (4 rows, of
  which `IC-E-002` and `IC-E-004` are step-13 checks against live pages) and
  `13-PRODUCT-ARCHITECTURE/museum-framework.md` §8.1.

`01-INHERITED/site-review/RUNNING-LIST-RECONCILIATION.md` was **not** opened,
per the instruction governing this unit.

### 0.2 The page text is reported, not retrieved

`melakeela/site` is not accessible from this session. Every sentence attributed
to a page below is quoted from **this repository's own record of it** or from
the instruction that commissioned this unit, and each quotation says which.
Where the two disagree, that is itself recorded as a finding rather than
resolved by preferring one — see brief 2 and brief 4.

This is a real limit. It means no brief here can say a page is *wrong*. Each
says what the register supports and where the published wording outruns it.

### 0.3 Inheritance

Nothing in `01-INHERITED/` was read. **This has two consequences that were
initially mis-stated and are corrected here after adversarial review.**

**Rows in `03-REGISTERS/inherited-claims.csv` are cited 13 times, across 8
distinct rows** — `IH-086` ×4, `IH-105` ×2, `IH-287` ×2, and `IH-060`, `IH-149`,
`IH-250`, `IH-329`, `IH-332` once each. An earlier draft of this section said
"three places" and was simply wrong; inherited standing rule 14 requires counts
in this project's own reports to be derived rather than estimated, and that one
was estimated.

**Two different uses, and only one of them is legitimate:**

- **Briefs 1, 3 and 4 cite `IH-` rows for what they show about the *state of the
  record*** — that a figure entered without a retrieval event, or that a piece of
  work is recorded as owed. That is a claim about this repository and it is
  sound. Brief 4 is the clean case: `IH-086`'s count was not quoted, it was
  tested (`VAR-001`).
- **Brief 2 does not.** Its arithmetic — 299 with 140, 315 with 194, 54 dated of
  199 — *is* `IH-250`, `IH-060` and `IH-105`, and an earlier draft carried those
  figures into proposed public copy. `CLAUDE.md` step 14 says public copy is
  drafted **only from accepted claims**, and `INHERITED-UNVERIFIED` is not one.
  The copy in §2.4 has been rewritten to say that our records disagree without
  reciting unverified figures as fact, and every figure kept in the *analysis*
  is now marked `INHERITED-UNVERIFIED` at the point of use. Brief 2 is
  correspondingly the weakest of the four and says so.

**And the exclusion of `01-INHERITED/` silently bounded a search.** See §2.1:
a negative claim about "every tracked file" was made from a search that had
excluded that directory, and the excluded directory contained the
counter-evidence. Retracted there, logged as `BF-017`, queued as `RA-018`.

### 0.4 The step-14 slots this document fills

`CLAUDE.md` step 14 names seven: QUESTION / WHAT IS OBSERVED / WHAT THE
EVIDENCE SUPPORTS / WHAT COMPLICATES IT / WHAT REMAINS UNKNOWN / MELAKEELA'S
CURRENT INTERPRETATION / WHAT WOULD CHANGE IT.

Each replacement below fills six. **MELAKEELA'S CURRENT INTERPRETATION is left
empty on every one of the four**, because on all four the interpretation is the
subject of an open owner decision. Drafting it here would be proposing past the
decision. WHAT WOULD CHANGE IT is filled, because step 12 requires a falsifier
and the falsifiers are already registered.

### 0.5 Retrieval performed for this unit

Two retrievals were run rather than deferred, because two of the four briefs
were otherwise going to hand back a plan:

| Ledger | What | Result |
|---|---|---|
| `SRC-085` | VedaWeb `vedaweb-data` re-clone | HEAD `d3eb8af`, the pinned commit; `strata.json` sha256 identical to `SRC-023`; extraction reproduces `PUR-001`'s 164,758 tokens exactly |
| `SRC-087` | JAMBU `moli-mandala/data` re-clone | HEAD `dbae310`, the pinned commit; `dedr.csv` sha256 identical to the value under `SRC-061` |
| `SRC-086` | this repository searched as a source | self-audit for any per-passage sense assignment for *varṇa-*: none |
| `SRC-088` | `ArimeKannada/Dictionary` | **`UNTESTED`** — not fetched, and **not blocked**: `github.com` is reachable on the channel that retrieved the other two. A scope decision, recorded so the gap is visible |

New registers written: `03-REGISTERS/rigveda-varna.csv` (9 rows),
`03-REGISTERS/rigveda-varna-occurrences.csv` (23 rows),
`03-REGISTERS/dedr-digitisation-lineage.csv` (8 rows). Dependency rows `DEP-024`
to `DEP-026`. Re-audits `RA-016` to `RA-018`. Contradiction `IC-P-001`.
Method failures by this unit: `BF-015` to `BF-017` (§5.1). The validator passes.

**This document was independently adversarially reviewed before the pull request
was opened, per constitution §8, and substantially corrected as a result. §5.1
lists every defect the review found and where each now stands.**

---

# Brief 1 — `the-northwest-cousin.html`, the Brahui figure

## 1.1 What the page currently asserts

Exact sentence, as recorded verbatim in `04-AUDITS/INTERNAL-CONTRADICTIONS.csv`
row `IC-E-002`, in `04-AUDITS/domain-e-dedr-digitisation-check.py` line 7 and in
`04-AUDITS/domain-e-method-comparative.md` line 182:

> counted directly from the Dravidian etymological dictionary, 191 of Brahui's
> 262 recorded roots have Tamil cognates

The load-bearing words are **"counted directly from the Dravidian etymological
dictionary"**. That reads as a fact about Burrow and Emeneau. It is a fact about
one machine-readable derivative of Burrow and Emeneau.

`IC-E-002` also records that the page already carries a caution that the
percentage misleads while the raw count does not. That caution is now itself
qualified: the raw count moves too.

## 1.2 What the verified register says

**The arithmetic is right.** `IC-E-002`: "The site's arithmetic reproduces
exactly from its own `dedr_roots.json` — 191 and 262 are correct for its data."
Nothing below disputes that, and no correction should imply a miscount.

**The same computation over other digitizations gives different figures.**
Measured this session, `03-REGISTERS/dedr-digitisation-lineage.csv`:

| Digitization | Lineage | Brahui entries | With a Tamil cognate | |
|---|---|---:|---:|---:|
| `dedr_roots.json` (site) | ArimeKannada/Dictionary | 262 | **191** | **73%** |
| JAMBU `dedr.csv` | DSAL scrape, 2013 SQL dump, deprecated | 269 | 220 | 82% |
| JAMBU `dedr_new.csv` | DSAL scrape, 2026 `parse.py`, current | 273 | 223 | 82% |
| DSAL online DEDR | — | \- | \- | `EGRESS_BLOCKED`, `SRC-056` |
| Printed DEDR, 2nd ed. 1984 | — | \- | \- | unreachable |

**But two of those three are one source, not two.** `DEDR-L-002`, from JAMBU's
own README lines 135 and 137: `dedr.csv` comes from a SQL database "scraped from
the online version" and is marked **deprecated**; `dedr_new.csv` comes from
`parse.py`, which at line 173 scrapes
`dsal.uchicago.edu/cgi-bin/app/burrow_query.py` over 514 pages. One upstream, two
scrapes. (The README gives no scrape *date* for the first; October 2013 is read
off the filename `dedr_new_entry_oct2013_edited.sql`, so it is a **file-naming
date, not an attested retrieval date** — step 2 wants the kind of date named, and
an earlier draft hardened it to "thirteen years apart" in public copy.) Under the source-independence rule they count
as **one**, recorded as `DEP-025`. Their agreement at 82% measures the stability
of a website, not the accuracy of either against the printed dictionary, and it
may not be weighed against the site's 73% as though it were two votes to one.

**The instrument is noisier than `IC-E-001` implies.** `DEDR-L-003`: across the
same 18 languages and by the same method, the two scrapes of the *identical*
source pages disagree on **5.5%** of entry-language assignments, against the
**10.3%** `IC-E-001` measures across lineages. Two parses of the same web pages
differ that much.

**Three qualifications, and the first cuts against this brief.** An earlier draft
carried none of them and said "roughly half the disagreement is parse noise".

1. **On Brahui — the one language the page's figure is about — the within-lineage
   rate is 2.2%, against `IC-E-002`'s cross-lineage 8.2%** (`DEDR-L-007`). About
   a quarter, not half. The parse-noise explanation is *weakest* precisely where
   the published number lives. That figure was in this unit's own output file and
   was left out of the first draft; the per-language range quoted above (2.0%
   Tamil to 14.3% Kolami) is computed over the 18 aggregate languages, which
   **exclude Brahui by construction**. Logged as `BF-015` under `BF-011`'s
   control, and written up as its own register row rather than as prose.
   It also cuts a second way: the site's 262 is further from both DSAL figures
   (269, 273) than they are from each other, which is what a genuinely separate
   lineage would look like — mild evidence *for* the independence `DEDR-L-005`
   records as untested.
2. **The 5.5% is directional.** Of the 1,414 disagreeing pairs, 465 are in
   `dedr.csv` only and **949 in `dedr_new.csv` only**. Two thirds is material the
   2026 re-parse has and the deprecated 2013 dump lacks — consistent with the old
   table being less complete, not with the new one being noisy. Only
   `dedr_new.csv` participates in the 10.3%.
3. **5.5 and 10.3 are not subtractable.** They are computed over different pairs
   of tables, and whether the disagreeing pairs are the *same* pairs in both
   comparisons was not tested. The contrast supports a magnitude comparison and
   nothing arithmetic.

**And the 10.3% cannot be re-derived here at all** (`DEDR-L-008`): the site's
`dedr_roots.json` is not in this repository, has no access-ledger row, and was
not available this session. Every figure this brief quotes from `IC-E-001` and
`IC-E-002` — the 10.3%, the 8.2%, the 191 and the 262 — is taken on the earlier
unit's report and checked only for internal consistency.

**And the thing the framing assumes has never been checked.** `DEDR-L-005`:
whether `ArimeKannada/Dictionary` derives from print or is itself another DSAL
scrape is **unknown**. It was not retrieved (`SRC-088`, typed NOT ATTEMPTED —
weaker than NOT ACCESSIBLE, because no attempt was made). `DEDR-L-006` therefore
records "the 10.3% is a disagreement between two independent readings of Burrow
and Emeneau" as a **`HYPOTHESIS`**, not a finding.

## 1.3 Owner decision

**`D-038` — OPEN.** *"Should `the-northwest-cousin.html` name the DEDR
digitization it counted and carry the range between the two?"* Options on file:
name the digitization and carry the range · keep the present wording · withhold
the figure until the digitizations are adjudicated.

**This brief does not propose past it.** The replacement below is drafted for
the first option because that is the only one that produces copy; if the owner
picks the second, nothing changes, and if the third, the section is withdrawn
rather than rewritten.

Two things the owner should know that `D-038` was raised without:

1. Its notes say "two digitizations". There are three tables and two lineages,
   and the second lineage is unretrieved. The **options are unchanged**, but
   "carry the range" now means a range whose endpoints are not two equal
   readings.
2. `RA-016`, queued this session, is **not blocked on `dsal.uchicago.edu`**.
   Retrieving `ArimeKannada/Dictionary` is a GitHub clone on the channel that
   already works, and it would settle `DEDR-L-005` without waiting on `D-043`.
   `D-038` may be cheaper to answer than its "downstream of `D-043`" note
   implies.

## 1.4 Proposed replacement

> ### QUESTION
> How much of Brahui's vocabulary is shared with Tamil, and how firmly do we
> know it?
>
> ### WHAT IS OBSERVED
> In the digitization of the *Dravidian Etymological Dictionary* this site
> counts from, Brahui appears under 262 entry numbers, and 191 of those
> entries — 73% — also carry a Tamil form.
>
> Counted in two other machine-readable versions of the same dictionary, the
> figures are 220 of 269 and 223 of 273, both 82%.
>
> ### WHAT THE EVIDENCE SUPPORTS
> That a large majority of Brahui's entries in this dictionary — somewhere
> between roughly seven and eight in ten — also carry a Tamil form. The
> majority is not in doubt. Its size is.
>
> ### WHAT COMPLICATES IT
> Every one of those numbers is a count over a *digitization*, not over the
> printed dictionary. We cannot check any of them against print: the online
> DEDR is unreachable from our research environment and we hold no copy.
>
> The two versions that agree on 82% are not two witnesses. Both are scrapes of
> the same website, one of them years older and since deprecated, and even so
> they differ on 5.5% of their entry-language assignments across the languages we
> could compare. Two parses of the same pages disagree that much — though for
> Brahui itself they differ by only 2.2%, less than they differ from our own
> figure. Precision on counts of this kind is limited in ways that no care in the
> counting removes.
>
> Sharing an entry number is also not the same as sharing a word. A DEDR entry
> groups forms an editor judged cognate; the count inherits every one of those
> judgements.
>
> ### WHAT REMAINS UNKNOWN
> Which digitization is closest to print — we cannot adjudicate them. Whether
> the version we count from is independent of the other two, or is a third
> scrape of the same website; we have not checked. And what the number would be
> if counted from Burrow and Emeneau directly.
>
> ### MELAKEELA'S CURRENT INTERPRETATION
> *(withheld — `D-038` open)*
>
> ### WHAT WOULD CHANGE IT
> Access to the printed DEDR or to `dsal.uchicago.edu` would let us count once
> and stop reporting a range. Retrieving `ArimeKannada/Dictionary` — which does
> not need either — would tell us whether the 73% and the 82% are two readings
> of a dictionary or one digitization's noise counted twice.

**On the phrase itself.** *"Counted directly from the Dravidian etymological
dictionary"* is the specific wording `IC-E-002` contradicts: it reads as a fact
about Burrow and Emeneau and is a fact about one digitization of it. An earlier
draft of this brief wrote "deletion required either way" — which quietly removes
`D-038`'s second option, "keep the present wording", and is therefore proposing
past the decision it says it is not proposing past. Corrected: if the owner
selects option two, this repository records `RA-011` as unresolved and the phrase
as contradicted by `IC-E-002`, and nothing is deleted.

---

# Brief 2 — `artifact-atlas.html`, the title

## 2.1 What the page currently asserts

The instruction commissioning this unit reports the title as carrying
**"175 sites and 315 windows"**.

**This repository records a different title.** `13-PRODUCT-ARCHITECTURE/museum-framework.md`
line 1454 and `DECISIONS-NEEDED.md` D-034 both record the audited v1 page as
titled:

> Artifact Atlas: 175 Ancient South Asian Sites Mapped

**A retraction.** An earlier draft of this brief stated that "a full-text search
of every tracked file returns no record anywhere of a title containing 315", and
built §2.2's argument on it. **That claim was false, and the way it was reached
is worse than the claim.** The search excluded `01-INHERITED/` under this unit's
scope instruction (§0.3) and then reported its result as covering every tracked
file. Adversarial review found the pairing in the excluded directory: the
site-review running list at line 210 associates the title's 175 with "evidence-window
counts of 299 or 315", and at line 686 with "175 or 194 sites and 315 windows".

Two consequences, and the second is the one that matters:

1. The corrected statement is: **no record in the directories this unit
   searched, which excluded `01-INHERITED/`.** An argument from absence must
   state its coverage in the same breath (constitution §6), and this one did
   not. Logged as `BF-017`, queued as `RA-018`.
2. **The pairing has a provenance.** It is not an invention at the page; it is
   a running-list formulation that put a title figure and a window figure side
   by side. That does not make the pairing sound — the two still come from
   records that disagree by 19 sites — but "no project record pairs them" is
   not the finding, and §2.2 below has been rewritten accordingly.

Those `01-INHERITED/` lines are cited here as **reported by the adversarial
review**, not read by this unit and not relied on as evidence for any figure.

So the correction has two parts, and the second is prior to the first: **which
string is actually on the page** is not established here, and cannot be, because
`melakeela/site` is not accessible from this session.

## 2.2 What the verified register says

**Nothing in this repository is `VERIFIED` about either number.** Both come
through `03-REGISTERS/inherited-claims.csv` at `INHERITED-UNVERIFIED`, and under
the inheritance rule no argument promotes them — only a retrieval would.

**Six site counts are on file.** `IH-250` (contradiction X-01):

| Count | Where it is stated |
|---:|---|
| 140 | live *Enter*; the owner's visual-concept document |
| 150 | MANIFEST description; VELI-02 |
| 158 | live *Explore* |
| 167 → 175 | VELI-09 §N; the live page title |
| 194 | VELI-02 §6; VELI-03 parsed records; VELI-13 |
| 199 | site-class rows |

**Two window counts are on file, and each is bound to a site count in its own
record.** `IH-060` (`INHERITED-UNVERIFIED`): the owner's visual-concept document
gives **140 sites and 299 windows**. `IH-105` (`INHERITED-UNVERIFIED`): the atlas
holds **194 site records and 315 class-windows** with 14 classes.

So: **299 was reported with 140, and 315 with 194.** A title pairing 175 with 315
takes its site count from the record that says 175 and its window count from a
record that says 194 — two figures that were never counted together, from records
that disagree by 19 sites. The running list did put 175 and 315 in one sentence
(§2.1), so the pairing has a provenance; what it does not have is a record in
which one dataset produced both.

**A further figure the title would inherit.** `IH-105` (`INHERITED-UNVERIFIED`)
also records that of 199 site-class rows, **54 are dated from excavation reports
and 145 are marked assumed**. Roughly three-quarters of the atlas's dating is
assumption. Any headline count carries that in silently.

**Every figure in this section is `INHERITED-UNVERIFIED` and none of it is
evidence.** It is the *state of the record*, which is what this brief is about:
seven site counts and two window counts, no retrieval behind any of them. Under
step 14 none of it may be drafted into public copy as fact, and §2.4 does not.
That is why brief 2 is the weakest of the four — it can show the record
disagrees with itself and can show nothing else.

**The audit rated this low risk.** `museum-framework.md` §8.1 records the v1
page as MVP rank 3, `Keep`, `Low` risk, 88 estimated bibliography entries
against 8 words of prose, and **no Claim Risk row** — the schema assessment's
words for it: the count 175 was *"adopted as settled fact, put in a page title,
and rated low-risk."*

## 2.3 Owner decision

**`D-034` — OPEN**, and this is the live one. *"Is 96 the authoritative page
count, and what is the atlas site count?"* Options: 96 supersedes the six on
file · 96 is a seventh unreconciled value; **and separately, state the atlas
site count.** It explicitly blocks "the Artifact Atlas page title at MVP rank 3."

**No number is proposed here.** Not 175, not 194, not a range, not "about 175".
The owner has reserved the count and it stays reserved.

**And `D-034` has already anticipated the move proposed below.** Its `notes`
column says of `museum-framework.md` §8.1: *"Neutralised but not answered — the
Atlas can be built without the number and **cannot be titled without it**."* The
owner should weigh that against §8.1 directly; this brief quotes both rather than
the half that suits it, having initially quoted only §8.1.

What §8.1 does specify for v2 is that **the Atlas has no headline count** — a count is a claim with a status, an inclusion rule and a falsifier,
displayed inside the Atlas with its status visible or not displayed; the number
in view is a property of the current filter and is always shown with the filter,
never as a title. §8.1 states outright that under this specification the Atlas
"can be built and shipped before that is answered, because it never asserts a
total in its own voice."

**So the proposed replacement removes the number from the title and does not
supply one.** That is the one move available that neither guesses at `D-034` nor
leaves a contested figure in a launch page title.

The title also depends on `D-007` (whether Artifact Atlas v2 remains among the
first three builds) for *when*, not for *what*. It does not depend on `D-022`,
which governs layer grouping.

## 2.4 Proposed replacement

Title — the number comes out and nothing replaces it:

> **Artifact Atlas: Ancient South Asian Sites**

Then, as the first panel inside the Atlas rather than as a headline, and shown
beside the filter per §8.1:

> ### QUESTION
> How many sites does this atlas hold?
>
> ### WHAT IS OBSERVED
> Our own records disagree with each other. Seven different site counts and two
> different window counts have circulated across the project's working
> documents, and the two window counts were each reported alongside a site count
> that is not the one in this page's old title.
>
> None of those figures was produced from the atlas's data. They are figures
> from working documents, and we have not verified any of them.
>
> ### WHAT THE EVIDENCE SUPPORTS
> That we cannot presently say how many sites the atlas holds. None of the
> figures above was generated from the atlas's own data, and we are not going to
> pick one until they are.
>
> The number shown above the map is the number of sites matching your current
> filter. It changes when you change the filter, and it is the only site count
> on this page.
>
> ### WHAT COMPLICATES IT
> The figures are not seven counts of the same thing. Some count sites, one
> counts rows in a table, and the window counts count something different again
> — units that were reported as though they were comparable.
>
> Our records also indicate that most of the atlas's dating is assumed rather
> than taken from an excavation report. We have not verified that either, and it
> is the reason a headline count would be misleading even if we had one: it
> would present an inventory as settled that is mostly inference about dates.
>
> ### WHAT REMAINS UNKNOWN
> Which figure is current, and what each of the seven was counting. None has
> been generated from the atlas dataset itself.
>
> ### MELAKEELA'S CURRENT INTERPRETATION
> *(withheld — `D-034` open, and it is this page's title that it blocks)*
>
> ### WHAT WOULD CHANGE IT
> Extracting the atlas to a dataset and generating every stated figure from it.
> That is the resolution path already recorded for contradiction X-01, and it
> would replace all seven counts with one that carries a definition, an
> inclusion rule and a status.

**Interim rule, whatever `D-034` decides:** no document, page, title or
prospectus prints an atlas site count until the dataset generates it. That is
already the standing position on file — `IH-329` and `IH-332` both record it as
a hold — and this brief does not relax it.

---

# Brief 3 — `dasa-forts-rigveda.html`, the chronological claim

## 3.1 What the page currently asserts

**A caution about identity, first.** This repository cannot confirm that
`dasa-forts-rigveda.html` carries the sentence attributed to it. What it holds
is `06-BRIEFS/rv01-reconciliation.md` §5 finding **C-6, "Three names for one
target"**: the register's `supports_page` reads `forts (proposed)`, the
curatorial audit's slug is `the-forts`, Version 12's route is
`/dasa-forts-rigveda`, RV-01 says "The 99 Forts Database" and feature 6 says
"The 99 Forts" — and *"whether these are one page or several is established
nowhere."* The chronological headline below is recorded against the slug
`the-forts`. If those are two pages, this brief applies to the other one.

The headline as recorded, `rv01-reconciliation.md` §2.5 and §5:

> Ninety-nine forts, in Indus country, three centuries too late

## 3.2 What the verified register says

### 3.2.1 The correction that is *not* available

This is the trap in the brief, and the repository already saw it. `rv01-reconciliation.md`
§5 records it as **"A false conflict, recorded so it is not re-raised"**:

> The `the-forts` headline says the forts are "three centuries too late" while
> `PUR-026` says the `púr-` vocabulary is *not* a late accretion. These are not
> in contradiction: `PUR-026` concerns position *within* the Rigveda on Arnold's
> periodisation; the headline concerns the Rigveda's date *relative to* Indus
> urbanism. Both could hold. Neither supports the other.

**The stratum measurements do not correct "three centuries too late."** They are
measured on a different axis. Any correction that used them to do so would be
the exact error the register wrote itself a note to prevent — and it would fail
in the platform's own preferred direction, which is what makes it worth naming.

What the stratum measurements *do* correct is any claim on the page that the
fort vocabulary is **late within the Rigveda**, or that a particular hymn is
late. Those are the two claims addressed below.

### 3.2.2 The distribution, and a figure to fix

The instruction commissioning this unit states the measurement as **"61 of 106
occurrences in Archaic or Strophic strata."** Recomputed from
`03-REGISTERS/rigveda-pur-family-occurrences.csv` this session, **61 is not a
figure this register produces at any unit**:

| Unit | n | Archaic | Strophic | Archaic + Strophic |
|---|---:|---:|---:|---:|
| token (`PUR-014`) | 106 | 31 | 32 | **63** (59.4%) |
| pāda (`PUR-015`) | 104 | 31 | 32 | **63** (60.6%) |
| stanza | 103 | 31 | 31 | **62** (60.2%) |
| hymn | 86 | 23 | 26 | **49** (57.0%) |
| token, certain codes only | 92 | 30 | 26 | **56** |

The figure for the unit the instruction names — 106, tokens — is **63**. Two
tokens' worth of difference changes no conclusion, and it is corrected here only
so that a corrected page does not publish a number the register cannot reproduce.

(The last row's denominator is 92, not 106: 14 of the 106 tokens carry lowercase
codes, which Arnold's legend marks as assigned on metrical variations alone. An
earlier draft of this table wrote 106 there — a table correcting a misreported
denominator, misreporting one.)

**Where 61 might have come from is not established.** No sub-count returns it at
any unit; the adversarial review on this brief tested all four units crossed
against simplex-only, compounds-only and both certainty subsets — twenty
combinations — and none yields 61. The nearest number in the register is
`PUR-021`'s **61.3%**, the share of Popular-stratum tokens sitting in book 10,
which is a different statistic about a different population. That is a guess at
the provenance and is recorded as one, so the figure does not return. The substantive shape is unaffected: Archaic and Strophic together
are about 60% of the family against about 43% of the corpus, and the whole
result is elsewhere.

**Where the result actually is:** `PUR-017`. The family's largest departure from
the corpus baseline is the **Popular** stratum, Arnold's latest — 3 tokens
observed against 14.8 expected. Full distribution, `PUR-014` against `PUR-016`:

| Stratum | Family | Expected | Corpus share |
|---|---:|---:|---:|
| Archaic | 31 | 21.8 | 20.6% |
| Strophic | 32 | 24.0 | 22.7% |
| Normal | 17 | 26.3 | 24.8% |
| Cretic | 23 | 19.1 | 18.0% |
| **Popular** | **3** | **14.8** | **13.9%** |

χ² = 19.98 on 4 df, p = 0.0005 at token level; at the conservative unit of the
hymn, χ² = 14.57, p = 0.0057 (`PUR-018`). The hymn figure is the one to quote —
tokens within a hymn are not independent.

### 3.2.3 RV 3.45

Measured this session against the pinned corpus, and matching
`03-REGISTERS/rigveda-pur-passages.csv` row `PUR-P-034`:

- The one *púr-* occurrence in the hymn is **RV 3.45.2b**, `purā́m`, GEN.F.PL.
- Its Arnold stratum code is **`N` — Normal**, uppercase, so `certain` rather
  than assigned on metrical variations alone (`PUR-011`).
- **All five stanzas of RV 3.45 carry `N`.** The whole hymn is Normal.
- Arnold prints the periods A Archaic, S Strophic, N Normal, C Cretic,
  P Popular. **`PUR-011` verifies the *mapping* — which letter denotes which
  period, and the italic convention — against Arnold 1905 Appendix IV §265
  p. 269.** It does not verify that the five are chronologically ordered in that
  sequence. **That is `PUR-028`, a `HYPOTHESIS`**, and an earlier draft of this
  brief borrowed `PUR-011`'s "not inferred from the letters" and attached it to
  the ordering, letting a hypothesis inherit a verified status. On the sequence
  Arnold proposes, Normal is the middle of five with two after it — and the
  whole of the RV 3.45 argument rests on that proposal, not on a measurement.
- `PUR-P-034`'s `stanza_properties_flags` reads `(none)`: **no stanza-level
  lateness flag from Grassmann, Oldenberg, Arnold 1897, Wüst or Witzel.** Under
  the negative-evidence standard that is typed **NOT PRODUCED** — none of the
  five marked the stanza — and it is *not* a finding that the stanza is early.
  13 of the 103 passages carry such a flag; this is not one of them.

So on the two instruments the register holds, RV 3.45 is middle-stratum and
unflagged. Neither instrument places it late.

### 3.2.4 A word this repository has already audited and rejected

`06-BRIEFS/pur-translation-standard.md` §10 opens: **"'Fort' fails the audit as
a default gloss."** It is serviceable for the Śambara–Divodāsa passages, where
something is besieged and broken, and *"actively misleading at RV 7.95.1 (a
river), RV 7.15.14 (a god), RV 8.1.28 (a moving one), and RV 8.6.23 (a
simile)."* `RA-013` is **OPEN** on exactly this, and its scope is "every
occurrence of fort/forts/fortress in page copy". Constitution §7 lists *fort*
among the ten inherited English categories to be audited before use.

An earlier draft of §3.4 wrote "the Rigveda's fort vocabulary" and "fort
language" unglossed across all 106 occurrences, and cited neither the standard
nor `RA-013` — while brief 4 was applying §7 to *caste* with some emphasis. The
asymmetry is the point: §7 was applied where it cut against a Victorian
lexicographer and skipped where it complicated a MelaKeela page's own framing.
That is a prestige-bias failure in this unit's own work, logged as `BF-017`, and
this document's first prestige-bias test missed it (§5.1).

§3.4 no longer uses "fort" as a default gloss. The page's *title* and slug are a
separate question and are `RA-013`'s and `D-045`'s, not this brief's.

### 3.2.5 What caps all of this

Four caps, and they are load-bearing enough that a corrected page that dropped
them would be worse than the current one:

1. **`PUR-026` is `PROVISIONAL`, not `VERIFIED`.** "The *púr-* vocabulary is not
   a late accretion" is capped because it rests entirely on Arnold's scheme being
   chronological. The *measurement* is `VERIFIED`; the *inference* is not.
2. **`PUR-028` is a `HYPOTHESIS`.** "Arnold's five periods correspond to real
   chronological stages of composition" is logged separately and explicitly so
   that `PUR-026` cannot silently inherit a higher status through it. Arnold
   himself calls the period names "provisional" (1905 §§60–61).
3. **The strata are one source.** `PUR-013`: `strata.json` is a transcription of
   Arnold 1905. Citing VedaWeb and Arnold is citing one source twice (`DEP-001`).
4. **The second instrument does not confirm the first, and "null" overstates
   what it did.** `PUR-020`: family books (2–7) against the rest, 6.98 per
   10,000 against 6.07, χ² = 0.50 on 1 df, p = 0.48. Reported per `BF-004`'s
   control — point estimate, direction and power limitation before it bears on
   anything: the direction is the *same* as the metrical instrument's (family
   books slightly higher), and at 106 tokens the test has too little power to
   resolve an effect of the size the metrical instrument reports. **`RA-002` is
   OPEN on precisely this**, asking whether "the two instruments do not agree"
   should read "one is significant and the other cannot resolve an effect this
   size". The second reading is the defensible one and §3.4 uses it. An earlier
   draft of §3.4 stated the null as a flat disagreement with neither estimate
   nor power — `BF-004`'s control, broken by a unit citing `BF-004`'s register.
5. **And where the two instruments *do* point the same way they are entangled** —
   `PUR-021`: 61.3% of all Popular tokens are in book 10, so the Popular deficit
   and the low book-10 rate are largely one observation counted twice.

## 3.3 Owner decisions

Two are open and both are **non-blocking** — neither stops this correction:

- **`D-044`** — is the passage unit of the §4J forts corpus the stanza (103
  rows), the pāda (104), the hymn (86) or the token (106)? Its own note says it
  blocks nothing. It does decide which row of the table in §3.2.2 a corrected
  page should quote. Until it is answered, quote the unit explicitly with the
  number, as that table does.
- **`D-045`** — does the site-facing artefact keep the inherited name "The 99
  Forts Database"? Relevant because `PUR4J-003` records that **ninety-nine is
  not the modal count** — one hundred is, by 9 passages to 6 — and the table has
  103 rows, so the name is neither the row count nor the commonest count.

Neither is proposed past. The draft below quotes the token unit, names it as
such, and takes no position on the artefact's name.

## 3.4 Proposed replacement

For the intra-Rigvedic chronology section only. **The "three centuries too late"
headline is a different claim on a different axis and is not touched here**
(§3.2.1).

> ### QUESTION
> Is the Rigveda's *púr-* vocabulary a late addition to the text?
>
> ### WHAT IS OBSERVED
> The word *púr-* and the six words built on it occur 106 times in the Rigveda.
> Sorted by Arnold's metrical periods, 63 of those 106 fall in the two he places
> earliest, Archaic and Strophic — about 60%, against about 43% of the corpus at
> large.
>
> The sharpest figure is at the other end. In Arnold's Popular period, the one he
> places last, *púr-* occurs 3 times where the period's share of the corpus
> predicts about 15.
>
> RV 3.45, sometimes cited as a late hymn, is not late on this measure: all five
> of its stanzas carry Arnold's Normal code — the middle of the five, on the
> sequence he proposes — and none of the five scholars whose stanza judgements
> we hold has flagged it.
>
> ### WHAT THE EVIDENCE SUPPORTS
> That *púr-* is not concentrated in the latest layer of the Rigveda. On the one
> stratification we can apply, it is thinnest there.
>
> ### WHAT COMPLICATES IT
> **We are not translating *púr-* on this page, and that is deliberate.**
> Grassmann's dictionary gives "wall of stones and clay, entrenchment,
> palisade" — not city, not town, not fortress. "Fort" is serviceable for the
> passages where something is besieged and broken and actively misleading
> elsewhere in the same corpus, where a *púr-* is a river, a god, something that
> moves, or a simile. So this section counts a Sanskrit word and does not tell
> you in English what it was.
>
> The chronology rests on one scholar. The period codes come from Arnold's
> *Vedic Metre* of 1905 and from nowhere else, and Arnold called his own period
> names provisional. That his five metrical periods are real stages of
> composition, in that order, is an assumption we are making, not something we
> have shown.
>
> A second test does not confirm the first. Ordering the text by the family
> books instead of by metre gives 6.98 occurrences per ten thousand words in
> books 2–7 against 6.07 in the rest — a difference in the same direction, far
> too small to distinguish from chance (p = 0.48). With 106 occurrences that
> test could not have detected an effect of the size the metrical one reports,
> so it is better read as unable to resolve the question than as disagreeing.
> And where the two do point the same way they are not independent: most
> Popular-period material sits in book 10, so they are largely one observation
> counted twice.
>
> That no scholar flagged RV 3.45 is not a judgement that the hymn is early. It
> means none of them marked it, which can happen for reasons that have nothing
> to do with the hymn.
>
> ### WHAT REMAINS UNKNOWN
> When any of this was composed in calendar years. Arnold's periods are relative
> and this page makes no absolute date claim from them.
>
> And what a *púr-* was. Counting the word is not describing the thing.
>
> ### MELAKEELA'S CURRENT INTERPRETATION
> *(withheld — `D-044` and `D-045` open; see §3.3)*
>
> ### WHAT WOULD CHANGE IT
> A stratification of the Rigveda independent of Arnold, applied to the same 106
> occurrences. If it put fort language late, this section would be wrong. Until
> one exists, one instrument is what we have and this page says so.

**Two corrections regardless of the rest:** if the page carries **61**, it
becomes **63** with the unit named (§3.2.2). If the page treats **RV 3.45** as
late, that goes (§3.2.3).

---

# Brief 4 — `what-varna-meant.html`, "All 23 Occurrences"

## 4.1 What the page currently asserts

As reported in the instruction commissioning this unit:

> All 23 Occurrences… sorted by sense

**This repository holds no record of that string.** A full-text search of every
tracked file returns nothing; the page's wording has not been seen from this
session and is quoted as reported. The finding below does not depend on the
exact wording. It depends on two things the phrase does regardless of how it is
worded: it asserts **completeness** ("all"), and it asserts a **sense
assignment** ("sorted by sense").

## 4.2 What the verified register says

### 4.2.1 The count was inherited; this unit measured it

Before this session, 23 was in the repository only as
`03-REGISTERS/inherited-claims.csv` **`IH-086`** — *"Varna occurs 23 times in
the Rigveda (180,196 words)"* — at **`INHERITED-UNVERIFIED`**, from
`gret_scan.json` record 0, a file this repository does not hold. Under the
inheritance rule only a retrieval promotes it, so it was tested rather than
quoted.

Re-retrieved VedaWeb at the pinned commit `d3eb8af` (`SRC-085`; `strata.json`
checksum identical to `SRC-023`; extraction reproduces `PUR-001`'s 164,758
tokens exactly) and censused by lemma id rather than by surface string, the
method of the *púr-* family:

**`VAR-001`, `VERIFIED`** — the Zurich annotation assigns the simplex lemma
*várṇa-* (Grassmann id `lemma_varRa_7738`) to **exactly 23 tokens**, in 23 stanzas and 21 hymns. All 23 are listed individually in
`03-REGISTERS/rigveda-varna-occurrences.csv`.

**The count reproduces. The denominator does not.** `VAR-002`: `IH-086`'s
"180,196 words" is not the pinned corpus, which is 164,758 tokens — a
15,438-token gap between two tokenizations of the same text, unexplained here.
`IH-086` is promoted **on the count alone**; nothing about 180,196 is promoted.

### 4.2.2 "All" is true of the simplex and not of the word

**`VAR-007`, `VERIFIED`** — a further **24 tokens** belong to **13 distinct
compound lemmas** built on *-varṇa-*, headed by *híraṇyavarṇa-* "gold-coloured"
with 9. The compound test is a string test over lemma strings and is a **floor**:
it misses at least *sā́varṇi-* and *sāvarṇyá-*, one token each.

So the corpus holds 23 simplex occurrences and at least 24 more inside
compounds. "All 23 occurrences" is exact for the simplex lemma and, unqualified,
overstates its own completeness for the word. The compounds are correctly
excluded from the 23 — they should not be counted in — but the boundary needs
stating rather than assuming.

### 4.2.3 The sense sort is owed, and nothing here backs it

**`VAR-008`, `VERIFIED`** (`SRC-086`, this repository searched as a source) — no
register in `03-REGISTERS/` carried a sense or human-applied column for *varṇa-*
before this unit. The 18 rows in `inherited-claims.csv` that mention the word are
every one `INHERITED-UNVERIFIED`. Two of them are the point:

- **`IH-287`** — handoff work item 19, Tier 2: *"The varna 23 human-applied
  split and the colour/skin count done right are owed."* Recorded as owed. No
  file records it as done.
- **`IH-086`**'s own note — *"The human-applied split is marked NEEDS-CHECK."*

**`VAR-004`, `VERIFIED`** — the Zurich layer carries lemma and morphology and
**no sense field**, and no source retrieved in this session assigns a sense to
any individual occurrence. Typed **NOT PRODUCED**: the annotation was not built
to record sense, so its silence says nothing about whether the occurrences share
one.

**`VAR-003`, `VERIFIED`** — and the lexicon does not close the gap. Grassmann
glosses *várṇa-* with **eight senses in a single undivided string**: *Farbe,
Stamm, Art, Gattung, Partei, Menschenart, Stand, Kaste* — colour, stock, kind,
class, party, human-kind, estate, caste. It supplies the **range**; it does not
distribute it over passages. A sense sort cannot be read off it.

Note what the eighth gloss is. **"Kaste" is Grassmann's nineteenth-century
interpretive category, not an attested Rigvedic sense**, and constitution §7
lists *caste* among the inherited English categories to be audited before use.
Sorting the 23 by Grassmann's gloss would let a Victorian lexicographer decide
the historical question — the failure §7 exists to prevent.

**`VAR-009` is therefore a `HYPOTHESIS`**, not a result: that the 23 divide into
a human-applied group and a non-human group is the proposition "sorted by sense"
asserts, and it has not been tested here.

### 4.2.4 What the register *can* say about the 23

Measurements only, drawn for the record rather than for the page:

- **`VAR-005`** — by Arnold stratum: Archaic 4, Strophic 4, Normal 8, Cretic 6,
  Popular 1. Reported as a measurement and nothing more. **At n = 23 no
  distributional inference is drawn** against the corpus baseline and none
  should be: expected counts in three of five cells are below 6.
- **`VAR-006`** — by book: 1 six, 2 six, 3 two, 4 one, 9 six, 10 two. Books 5,
  6, 7 and 8 carry none. Six of 23 are in book 9, the Soma maṇḍala, where a
  colour sense of the purifying draught is an obvious candidate reading — but
  that is a reading, not a measurement, and the register does not make it.

### 4.2.5 The direction the error would run

`IH-149` records **`R-03`: leading with *varṇa* as "the colour of a dawn" was
REJECTED by the owner**, as the paradigm case of the failure mode, with the rule
"both halves in the same breath, the indictment first, nuance after, never as a
replacement." A sense sort built from Grassmann's gloss would land on colour
first by construction. That is a known, named, already-rejected failure, and it
is recorded here so a corrected page does not walk back into it.

## 4.3 Owner decision

**No `D-` row governs this page.** `IH-287` is a work item, not an owner
decision, and it stays `INHERITED-UNVERIFIED` — a register row would be a
promotion, and only retrieval promotes.

**So brief 4 is the only one of the four that is not waiting on the owner.** It
is waiting on a unit of work: reading all 23 passages against the nine
translations bundled with the corpus (`SRC-072` to `SRC-077` — an earlier draft
wrote `SRC-070` to `SRC-077`, but `SRC-070` is `addressees.json` and `SRC-071`
is `stanza_properties.json`, neither a translation; `SRC-077` bundles the four
partial ones) under the §7 translation standard — original script, transliteration, grammatical form,
semantic range, textual context, edition, exact locator, translation used,
alternatives, and the interpretive consequence of choosing between them. That is
scoped in `VAR-009` and is not done here.

If the owner wants the sense sort re-affirmed as a standing product commitment
rather than a carried-over work item, that would take a fresh `D-` allocated
from `09-DECISIONS/OWNER-DECISIONS.csv`. This brief does not allocate one.

## 4.4 Proposed replacement

The count survives. The completeness claim gets a boundary. The sense sort comes
out until it is done.

> ### QUESTION
> How often does *varṇa* appear in the Rigveda, and what does it mean there?
>
> ### WHAT IS OBSERVED
> The word *varṇa* on its own occurs **23 times** in the Rigveda, across 23
> stanzas in 21 hymns. We counted them in a lemma-annotated edition of the text
> rather than by searching for a string, and all 23 are listed below with their
> book, hymn, stanza and grammatical form.
>
> It also appears inside compounds at least 24 further times, in 13 different
> compound words — *híraṇyavarṇa-* "gold-coloured" is the commonest, at 9. Those
> are not counted in the 23.
>
> ### WHAT THE EVIDENCE SUPPORTS
> The count, and the list. Both are reproducible from a published edition.
>
> ### WHAT COMPLICATES IT
> **We cannot yet tell you what each of the 23 means.** The annotation that
> gives us the count records grammar, not sense. The standard dictionary offers
> eight meanings for the word in one undivided entry — colour, stock, kind,
> class, party, human-kind, estate, caste — and does not say which applies
> where.
>
> The eighth of those, "caste", is a nineteenth-century editor's word for what
> he took the Sanskrit to mean. Whether any of these 23 passages carries a social
> sense is exactly what we have not established — so sorting them by that
> dictionary entry would be letting a Victorian lexicographer answer the question
> this page is asking.
>
> ### WHAT REMAINS UNKNOWN
> How many of the 23 apply the word to people rather than to colour, and how
> many carry any social sense at all. This is the question the page exists to
> answer and we have not answered it. Doing it properly means reading all 23
> passages against several translations and recording where the translators
> disagree — because on a word like this one, they do.
>
> ### MELAKEELA'S CURRENT INTERPRETATION
> *(withheld — the sense reading is not done; see above)*
>
> ### WHAT WOULD CHANGE IT
> That reading, done and published with the passages, the competing translations
> and the reasons for each choice. Until then this page gives you the count and
> the list and stops there.

**Required removal:** the phrase **"sorted by sense"**, or any equivalent, until
the reading exists. Publishing the 23 with their locations and grammar is
supported today. Publishing them sorted by sense is not, and the register has
recorded it as owed since the inheritance was compiled.

---

## 5. Adversarial tests on this document

Run per constitution §8. **The first run of these tests, written before
independent review, passed this document. It should not have.** An independent
adversarial review then found fourteen defects, three of them method failures in
this unit's own work. Both runs are recorded below, because a self-test that
cleared work an independent reviewer did not clear is itself the finding.

### 5.1 What the independent review found

Everything below was found by the adversarial reviewer, not by §5.2–§5.3, and is
fixed in this document and its registers:

| | Defect | Where it now stands |
|---|---|---|
| 1 | Brief 2's public copy proposed a site-count **range** — the one thing §2.3 reserves to `D-034` | sentence deleted; §2.4 says we cannot say |
| 2 | Brief 2 claimed "a full-text search of **every tracked file**" for a search that had **excluded `01-INHERITED/`**, where the counter-evidence sits | retracted in §2.1; `BF-017`, `RA-018` |
| 3 | `VAR-007` read 24 tokens / 13 lemmas and called it a floor; the true figure is **23 / 12** and 24 was an over-count | script rewritten to adjudicate on gloss; `BF-016`, `RA-017` |
| 4 | Brief 3's copy used **"fort"** as an unglossed default, which `pur-translation-standard.md` §10 records as failing the §7 audit and `RA-013` is OPEN on | §3.2.4 added; copy rewritten; `BF-017` |
| 5 | The **Brahui within-lineage cell (2.2% against 8.2%)** — the measurement that cuts against brief 1 — was in this unit's output file and in no register row | `DEDR-L-007`; `BF-015` under `BF-011`'s control |
| 6 | `DEDR-L-005` was `VERIFIED` citing `SRC-088`, **a ledger row recording that nothing was retrieved** | re-sourced to `SRC-086` |
| 7 | `SRC-085`–`SRC-087` carried **`00:00Z` placeholder retrieval times** in a retrieval ledger | corrected to the actual clone times |
| 8 | Brief 1's "deletion required either way" **removed `D-038`'s second option** | restated in §1.4 |
| 9 | **"NOT ATTEMPTED"** was invented as a ninth negative-evidence type | dropped; `SRC-088` is `UNTESTED`, and says why |
| 10 | `VAR-002` performed a **half-promotion** of `IH-086` that the status vocabulary does not have, and never effected it | demoted to `PROVISIONAL`; `IH-086` explicitly left alone |
| 11 | §0.3 said `IH-` rows were cited "in three places" (**13**) and "never as support for a figure" (**brief 2 did exactly that**) | §0.3 rewritten |
| 12 | Five wrong numbers in `VERIFIED` rows: certain-only denominator 106→**92**; "three of five" cells below 6→**all five**; "four family books"→**three**; `VAR-001`'s surface-form parenthesis; translations `SRC-070`→**`SRC-072`** | all corrected |
| 13 | `PUR-011` verifies the letter **mapping**; the brief attached "not inferred from the letters" to the **ordering**, which is `PUR-028`, a `HYPOTHESIS` | §3.2.3 and copy corrected |
| 14 | The by-book **null** was stated without estimate, direction or power, breaking `BF-004`'s control; `RA-002` is OPEN on that sentence | §3.2.5 and copy corrected |

Also from the review and folded in: `DEDR-L-008` (the 10.3% is not re-derivable
from this repository — the site JSON has no ledger row); `IC-P-001` (`D-045`'s
notes cite `PUR4J-003` at a superseded value, 8 against 9); the October 2013 date
is read off a filename, not attested; and `DEP-025`'s two fields carry prose
rather than resolvable ids, because `dedr.csv` has no ledger row of its own —
recorded, not fixed, since `DEDR-L-001` implicitly argues for giving it one.

**Three of the fourteen are method failures by this unit** and are logged in
`04-AUDITS/BIAS-FAILURE-LOG.csv` as `BF-015`, `BF-016` and `BF-017`. An earlier
version of §5.3 said no `BF-` row was owed "because nothing in this unit was
found to be a method failure by an earlier unit" — which quietly reframes the
log as a record of *other* units' failures. Constitution §9 logs them wherever
they occur, including here.

### 5.2 Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly cited
or nationally useful?*

**It did, and the first run of this test missed it.** That run said "Brief 3 is
where the risk sits, and it runs the other way" — it examined Arnold, found him
capped four times, and stopped. It never asked the §7 question about *fort*,
which is the inherited English category sitting in the page slug, in the draft
copy and in the register's own `supports_page` value. §7 was applied hard to
*caste* in brief 4, where it cuts against a Victorian lexicographer, and skipped
on *fort* in brief 3, where it complicates MelaKeela's own framing. That is the
failure, and it is `BF-017`.

What survives the corrected run:

- **Brief 3** caps Arnold four times (§3.2.5), quotes `PUR-026` as `PROVISIONAL`
  and `PUR-028` as `HYPOTHESIS` in the draft copy rather than only in the
  apparatus, and now refuses "fort" as a default gloss in that copy.
- **Brief 1** does not treat the DSAL lineage as authoritative because it is the
  academic host; `DEDR-L-002` demotes it to one source precisely to stop that.
- **Brief 4** refuses Grassmann's gloss as a sense assignment.

### 5.3 Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**It did, in brief 1, and the first run of this test missed that too.** Omitting
the Brahui cell (§1.2 qualification 1) made the case against a published
MelaKeela figure look stronger than this unit's own data supports — and the
omitted number is the one that most directly weakens it. Direction: against the
published page, in the platform's favour. `BF-015`.

A second instance, smaller: an earlier draft of brief 4's copy wrote that "caste"
is *"not something the Rigveda says"* — asserting a sense-negative in the
project's preferred direction, in a brief whose whole argument is that no sense
reading has been done. Corrected in §4.4.

What survives:

- **§3.2.1 is the strongest thing in the document.** The commissioning
  instruction invited reading the *púr-* strata against "three centuries too
  late". Those are different axes, `rv01-reconciliation.md` §5 had already logged
  it as a false conflict, and using the strata there would have produced a
  correction in the platform's preferred direction out of a category error. It is
  refused explicitly and in the brief's own text. The independent review checked
  brief 3's copy for a smuggled route back and found none.
- **Brief 1** does not conclude that 82% is right and 73% wrong, which would have
  raised the Brahui–Tamil figure and favoured the Dravidian-continuity reading.
- **Brief 2** proposes no site count in either direction.

### 5.4 Where this document is weakest

1. **No page was retrieved.** Four briefs about live pages, none read. No brief
   can say a page is wrong — only where the published wording outruns the
   register.
2. **Brief 2 is the weakest of the four and rests entirely on
   `INHERITED-UNVERIFIED` rows.** It can show the record disagrees with itself
   and nothing else, its premise about the title is uncorroborated here, and one
   of its negative claims has already had to be retracted (§2.1).
3. **Brief 4's premise is uncorroborated as to wording.** The substance holds —
   the sense sort is registered as owed — but the quoted string is not in this
   repository.
4. **`SRC-088` was not attempted**, and it is the cheapest thing bearing on
   `D-038`. Left for `RA-016`.
5. **`IC-E-001`'s 10.3% could not be checked** (`DEDR-L-008`). Its input is not
   in this repository and has no ledger row, so every figure brief 1 quotes from
   it is taken on report.
6. **This document's own self-tests failed.** §5.2 and §5.3 both cleared work an
   independent reviewer did not clear, in both directions the two tests exist to
   catch. The tests are worth no more than the independence of whoever runs
   them, and that is the general finding here.

## 6. Summary for approval

Four independent decisions. Each can be taken without the others.

| # | Page | Change | Blocked on |
|---|---|---|---|
| 1 | `the-northwest-cousin.html` | Replace "counted directly from the Dravidian etymological dictionary"; name the digitization; carry the range | **`D-038` OPEN** — three options on file, drafted for one; option two ("keep the present wording") remains available |
| 2 | `artifact-atlas.html` | Remove the count from the title; move it inside as a filter-bound claim | **`D-034` OPEN** — the live one; no number proposed |
| 3 | `dasa-forts-rigveda.html` | 61 → 63 with the unit named; drop any late reading of RV 3.45; leave "three centuries too late" alone | `D-044`, `D-045` open but **non-blocking** |
| 4 | `what-varna-meant.html` | Keep the 23 and the list; state the compound boundary; remove "sorted by sense" | **Nothing** — waiting on a unit of work, not a decision |

All four changes belong in `melakeela/site`. None is made here.

## 7. Domains requested

No retrieval was refused at the egress proxy during this unit. Both clones —
`github.com/VedaWebProject/vedaweb-data` and `github.com/moli-mandala/data` —
succeeded on the session git proxy.

Two standing blocks are load-bearing on brief 1 and are carried forward from
earlier sessions rather than re-probed here:

- **`dsal.uchicago.edu`** (`SRC-056`, `EGRESS_BLOCKED`) — the canonical online
  DEDR, and the upstream both JAMBU tables scrape. Requested under `D-043`.
- **`archive.org`** (`SRC-081`, `EGRESS_BLOCKED` on re-probe) — requested under
  `D-043`. Alongside it, `gretil.sub.uni-goettingen.de` (`SRC-080`),
  `titus.uni-frankfurt.de` (`SRC-082`) and `sacred-texts.com` /
  `www.wisdomlib.org` (`SRC-083`) are all `EGRESS_BLOCKED` on file; none was
  needed by this unit and none was re-probed here.

One domain is **not** blocked and is the cheapest open item on brief 1:
`github.com/ArimeKannada/Dictionary` (`SRC-088`), reachable by the channel that
already works, not attempted here, queued as `RA-016`.
