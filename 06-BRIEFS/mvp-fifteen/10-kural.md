# `kural` — page brief

**Page:** *Tirukkural: Tamil Ethics Without Caste or Ritual* · MVP rank **10** of 15 · `Tamil Retrofuture` · Decision `Revise` · Risk `Medium`

**Written:** 2026-09-08
**Unit type:** page brief. A brief is a statement of what a page would have to
be and what it would have to rest on. It is **not public copy**, and no
sentence in it may be lifted onto a page.
**Status of this brief:** every design statement is `HYPOTHESIS`, inherited
from `13-PRODUCT-ARCHITECTURE/museum-framework.md`, whose own §14.4 puts every
design proposition it contains at `HYPOTHESIS`. Every statement drawn from
`01-INHERITED/curatorial-audit-v1.1/` is `INHERITED-UNVERIFIED`. No retrieval
was performed to write this brief and no row was added to
`02-SOURCES/access-ledger.csv`.
**Method:** `04-AUDITS/mvp-fifteen-briefs-build.py`; index and shared gates in
`06-BRIEFS/mvp-fifteen/README.md`.


---

## 1. The question, in step 14 form

**QUESTION.** Which words for social rank, birth-group or ritual status occur in the Tirukkuṟaḷ, in which edition and recension, and what does their presence or absence support?

### Why the remaining six slots are empty

Step 14 draws public copy **from accepted claims**. This page has none: §3 below
records that nothing bearing on it stands above `INHERITED-UNVERIFIED`. Drafting
`WHAT THE EVIDENCE SUPPORTS` from claims at that standing would be writing public
copy for unverified claims, which is what `CLAUDE.md`'s inheritance rule and the
museum framework's Rule S-1 forbid. The slots are therefore left open, with the
work that would fill them named in §6.

| Step 14 slot | Draftable today | Why not |
|---|---|---|
| QUESTION | yes | stated above; a question asserts nothing |
| WHAT IS OBSERVED | partly | the workbook's structural counts are observations *about a page*, not about the past; the page's own observations are unretrieved |
| WHAT THE EVIDENCE SUPPORTS | no | no claim above `INHERITED-UNVERIFIED` |
| WHAT COMPLICATES IT | no | complications are claims too, and carry the same floor |
| WHAT REMAINS UNKNOWN | no | requires the negative-evidence typing of constitution §6, not yet performed |
| MELAKEELA'S CURRENT INTERPRETATION | no | an interpretation over an unverified claim set states confidence retrieval has not earned |
| WHAT WOULD CHANGE IT | no | falsifiers attach to claims; there are no claim rows to attach them to |


### What the workbook records as observed

879 words, type `text`, **1 estimated source entry**, 0 external links, 2 tables,
1 inline SVG, 55 inbound links. Decision `Revise`, Risk `Medium`. H1 and central
claim: *"Thirteen hundred and thirty couplets on how to live, and the word for
caste is not in any of them."* The workbook's assessment: *"Strong anchor text if
translations, editions, counts, and absences are reproducible."*

Every one of those four conditions is a separate problem, and the page carries
one source entry for all of them.


---

## 2. Environment and epistemic posture

**Environment:** `Tamil Retrofuture`. **Posture — the visitor's relation to the knowledge:** *known against an official account*. **`Avoid` — the failure this posture invites:** *"No kitsch, fake Tamil or neon overload"*.

The workbook's own function and effect cells for this environment: function *"Counter-history, public energy, learning"*, desired effect *"Spunky cultural memory"*, palette role *"Aubergine, magenta, orange, cyan"* (`environment-map.csv`, `INHERITED-UNVERIFIED`).


### Modes available in this posture

| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| Tamil Retrofuture | mandatory | available | mandatory | available | available |

*(Framework §1.7.)*


### Derivation

**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: Tamil Retrofuture, editorially, by the workbook.** That assignment is
`INHERITED-UNVERIFIED` and carries no override reason, because the register that
would hold one does not exist. `SCHEMA.md` §7: *"nothing in `03-REGISTERS/`
records a publication decision, an environment assignment, or a duplication
finding."* Creating the Editorial Register (§11.5) with `derived_posture`,
`assigned_posture`, `override_reason`, `decided_by`, `decided_date` is a
prerequisite for this page, not a nicety: an assignment with no derivation to
disagree with cannot be audited.

**Secondary environment.** The workbook gives this page `Reading Room` as
secondary — as it does for all 96. Framework §1.6.1 rules that a value constant
across every row is not a value: it is the single statement *"Source Mode
exists"*, and the column should be retired rather than migrated. This brief
treats the page's secondary environment as **Source Mode**, a universal display
state, not as a second posture.


**Investigation Mode is mandatory** (§1.7): Tamil Retrofuture is one of the three
postures where the institution argues against an official account, and PROVE IT
is what keeps such an argument falsifiable. This page is a good argument for the
rule — a claim of the form *'the word is not in the text'* is trivially
falsifiable and therefore ideal for the mode, provided the search set is
published with it.

The `Avoid` — *"no kitsch, fake Tamil or neon overload"* — bears on a page that
displays Tamil script: transliteration and script must be correct and sourced,
not decorative.


---

## 3. The evidence it rests on

**No register row in this repository names this page.** A scan of all 14 registers in `03-REGISTERS/` carrying a `supports_page` column returns zero rows for `kural` (`04-AUDITS/mvp-fifteen-briefs-build.py`, `scan_supports_page`). Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the page it feeds — so on the repository's own accounting, this page is supported by nothing.


**Adjacency is not support.** Where verified work in this repository happens to
be *about subjects a page discusses*, it is still not *linked to that page*: no
row in any register carries `supports_page` naming this slug. Under framework §3.3 a
claim's status comes from its own Evidence Links, so a page cannot inherit
standing by sitting next to a register. Linking is an editorial act (§11.5) and
transfers nothing by itself; the page's propositions have to be written as Claim
Objects and evidenced in their own right.


What exists instead is inherited material that **bears on** this page without being linked to it. Every row below is from `03-REGISTERS/inherited-claims.csv`, whose 369 rows all carry `INHERITED-UNVERIFIED` and all carry an empty `supports_page`.


| claim_id | status | locator | what it bears on |
|---|---|---|---|
| `IH-091` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L216` | The handoff's finding V-08, from `kural_ta.txt`, VELI-03 and MANIFEST — *'the first Tamil corpus'*: the Tirukkuṟaḷ has 1,330 couplets with **zero occurrences of *cāti* and zero of *vēṭam***. Entered here as `INHERITED-UNVERIFIED`; the handoff's own `VERIFIED` label did not survive intake. |
| `IH-248` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L462` | Section 8 HELD register: the Tamil, Pali and Prakrit corpus *other than the Kural* is recorded as NOT OBTAINED / NOT FOUND. The Kural is the exception — which is why this page exists — but the comparative material that would show what the Kural's silence means is not held. |
| `IH-012` | `INHERITED-UNVERIFIED` | `01-INHERITED/claude-project-handoff.md L57` | The parallel case, and a correction: *'no caste word in the Vedas' is wrong* — *varṇa* occurs 23 times in the Rigveda and the correct finding is that *jāti* is absent from it. The same argument-form on the same subject has already been found overstated once in this project. |


**The claim's form is the problem, and naming it costs no retrieval.** `IH-091`
records zero occurrences of **two** Tamil words. The headline says *"the word for
caste is not in any of them"* — the definite article doing work no census
supports. Tamil has several candidates for what an English reader means by
*caste*: *cāti*, *varṇam*, *kulam*, *kuṭi*, *piṟappu*, *marapu*. A census of two
forms establishes the absence of two forms.

This is `CLAUDE.md`'s translation standard operating exactly as specified — *caste*
is on its list of inherited English categories to audit before use, and the rule
is *do not let the translation decide the historical question*. Here the
translation is deciding it twice: once in choosing which Tamil words count as
'the word for caste', and once in treating their absence as evidence about Tamil
society rather than about Tamil lexis.

`IH-012` is the precedent, and it is close enough to be uncomfortable: the same
project made the same move about the Vedas, was corrected, and the corrected form
was narrower and more interesting. The corresponding narrower claim here would
name the forms searched and say what was not searched. That is a claim the
repository could actually support — and it is a **different claim** from the one
the page currently makes.

**This repository has already built the machine for it.**
`03-REGISTERS/rigveda-varna.csv` (7 `VERIFIED`) and
`rigveda-varna-occurrences.csv` are a lemma census with per-token morphology and
stratum, built by `04-AUDITS/rv-varna-census.py` off a retrieved corpus. The
method transfers directly to a Tamil text. What does not transfer is the corpus:
`kural_ta.txt` is named in the handoff and the MANIFEST and **is not in this
repository**, with no access-ledger row.


### Lowest status among them

**`INHERITED-UNVERIFIED`** — the status of every row above, and of every row that could be listed.


**On "lowest status".** `INHERITED-UNVERIFIED` is not the bottom rung of a
ladder. Framework §3.2: six of the seven statuses describe evidential standing
and one describes *where the assertion came from* — a prior model's summary of
its own conversation — so the interface *"must never sort or colour
`INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS` as though the
statuses formed a single ladder."* What can be said exactly is the operative
ceiling, and it is the same for all fifteen pages: **nothing bearing on this
page stands above `INHERITED-UNVERIFIED`.** Where the handoff labelled a finding
`VERIFIED` or `PROVISIONAL`, that label came in with it and did not survive
intake — `CLAUDE.md`, the inheritance rule.


---

## 4. Required asset class

From `01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, verbatim (`INHERITED-UNVERIFIED`):


| Field | Value |
|---|---|
| Required asset set | primary-text facsimile; translation excerpt rights; editorial illustration or print ephemera where appropriate |
| Documentary standard | Verified source, licence, credit, alt text, claim supported, date/place, manipulation disclosure |
| Priority | `MVP` |
| Source / commission route | To research |
| Status | `Needed` |


**How this class should be derived instead.** Framework §1.6.3(a) replaces genre-driven asset classes with a mapping from the exhibit's **evidence-class composition** — the constitution's step 4 inventory. The workbook derived this row from the page's `Type`, a 29-value vocabulary with 17 singletons that `SCHEMA.md` §4 finds *"too sparse to do reliably"* the production-planning work it is doing. Under §1.6.3(a) a page with no recorded evidence classes yields **no** production class, which is the correct output and is this page's actual state.


**`translation excerpt rights` is an unbounded dependency.** §1.6.3(a) maps
modern translation to *"third-party rights negotiation — unbounded timeline"*.
Quoting a modern English Tirukkuṟaḷ translation means clearing rights with a
rights-holder on their schedule. `DECISIONS-NEEDED.md` **D-029** (does the
institution ever assert fair dealing, and in which jurisdiction) is the open
decision that governs whether there is an alternative.

`primary-text facsimile` is the asset this page most needs and the one that would
most improve it: a facsimile of a named edition at a named locator is the
evidence the page's argument runs on. `editorial illustration` is a derived asset
and is embargoed under §3.12.


---

## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

1. The search set is stated. Which Tamil forms were counted, which were not, and why. Without it the headline is an assertion about a word class, not a count.
2. The edition and recension are named. The Tirukkuṟaḷ has a commentarial tradition and variant readings; a count is a count in a text, and `kural_ta.txt` is a file, not an edition.
3. The claim is narrowed to what the census supports, per the `IH-012` precedent, or the wider claim is dropped.
4. The absence is typed under constitution §6 — a didactic poem's silence about birth-groups is a curated silence, and `CLAUDE.md` is explicit that *silence in a curated record is not refutation*.
5. Translation rights are cleared or D-029 is answered.
6. PROVE IT exists (§1.7, mandatory in this posture), and the census is reproducible from it.


---

## 6. What unit of work would verify it

**MVP-U10 — the Tirukkuṟaḷ lemma census.** Retrieve a citable Tirukkuṟaḷ text;
name the edition; define and publish the search set; run the census with
per-occurrence locators as `rv-varna-census.py` does for the Rigveda; log the
retrieval; write the rows with `supports_page = kural`.

**The retrieval route is untested, and this brief does not assume one.** The only
open lane is the git proxy — `SRC-052` records `github.com` and
`raw.githubusercontent.com` as the reachable hosts, and `SRC-058` records the
anonymous read lane for arbitrary public repositories. Whether a citable
Tirukkuṟaḷ edition with a stated recension is served there is unknown; probing it
is step 1. If it is not, `05-HOLDS/` takes a row and the page's central claim
stays at the floor.

**Ceiling.** A single digitised text yields `PROVISIONAL` at best under §3.2 —
one edition is one source. `VERIFIED` needs a second independent edition, which
is what the Tamil Lexicon and a printed critical edition would supply, and
`dsal.uchicago.edu` is `SRC-056`, `retrieval_capable = NO`.


---

*Brief written 2026-09-08. Nothing in it is public copy. Nothing in it promotes a claim: promotion requires a retrieval event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
