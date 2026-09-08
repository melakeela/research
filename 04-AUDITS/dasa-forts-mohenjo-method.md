# Method note — the Mohenjo-daro pull quote on `dasa-forts-rigveda.html`

Unit commissioned by the owner, 2026-09-08. Scope as given: register two
method failures, survey the live site for the same or a similar claim and
register each occurrence, register two owner positions separately at
`INHERITED-UNVERIFIED`, link them by a typed relationship, **do not resolve
either, do not write replacement copy.**

What this unit produced: `SRC-099`, `BF-027`, `BF-028`, `MDO-001`–`MDO-014`,
`DFO-001`, `DFO-002`, `BR-F-001`, `IC-F-001`, `IC-F-002`, `RA-022`–`RA-026`,
`RQ-D-01`–`RQ-D-03`. The validator passes.

---

## 1. The sentence

> Whatever the ninety-nine forts were, they were not Mohenjo-daro. That city
> fell to a river, and it fell before anyone was writing about it.

`dasa-forts-rigveda.html:420`, element `<p class="pull">`.

**The commissioning instruction called it a prototype sentence. It is not
only that.** The instruction is right that it appears in the visual-doctrine
prototypes; it appears there *because it was copied from the published page*,
where it has been all along. `prototypes/README.md` states the prototypes
reuse "the real text of an existing page, unedited in substance". The
prototype is the copy, not the source. Correcting only the prototypes would
have left the live page carrying it.

This is the first thing the survey established and the reason the survey was
worth running rather than assuming.

---

## 2. What was retrieved, and what was not

**Retrieved (`SRC-099`).** `melakeela/site`, cloned at HEAD
`79efd74e53d54d835bc61ecf94ba6dd2e164bad1`, main, 2026-09-08T21:32:27Z.
141 HTML files at the root, 7 under `prototypes/`. `dasa-forts-rigveda.html`
sha256 `d741d104…3e9183`.

This lifts a limit prior work declared honestly and could not get past.
`CORRECTIONS-PENDING.md` §0.2: *"`melakeela/site` is not accessible from this
session… no brief here can say a page is wrong."* §3.1: *"This repository
cannot confirm that `dasa-forts-rigveda.html` carries the sentence attributed
to it."* It does. Confirming it is a retrieval, not an argument.

It also part-settles `rv01-reconciliation.md` finding **C-6, "three names for
one target"** — whether `the-forts`, `/dasa-forts-rigveda`, "The 99 Forts
Database" and feature 6 are one page or several. There is one root file at
that slug and it carries the headline recorded against `the-forts`. Whether
the *database* artefact is the same object is untouched. `RA-022`.

**Not retrieved, and the whole cap on this unit.** No archaeological report,
no excavation record, no palaeoclimate dataset, no Indological chronology, no
literature on the identification. Nothing was retrieved except the project's
own published copy.

So every finding here is a finding about **what the site says and how it says
it**. Nothing here establishes what caused Mohenjo-daro's decline, when the
Rigveda was composed, what stood in the region, or how the literature treated
the identification. Where this note appears to lean toward an answer on any
of those, it is out of scope and should be read as a question.

---

## 3. How the survey was run

Case-insensitive `grep` over all 148 HTML files for: `mohenjo`; the exact
string `fell to a river`; `ninety-nine`; `centuries too late`; `not the Indus
cities`; and decline-cause vocabulary (`hydrolog`, `Ghaggar`, `monsoon fail`,
`aridification`, `deurbanis`/`deurbaniz`, `4.2 ka`, `Sarasvati dried`).
Publication state checked against `sitemap.xml`, `robots.txt`, `netlify.toml`
and each file's `<meta name="robots">`.

Fifteen root pages mention Mohenjo-daro. Most are irrelevant to this claim —
trade, genomics custody, music, astronomy — and are not registered. Fourteen
occurrences of the same or a similar claim are, across six files.

**Three deliberate choices in what got registered.**

1. **The premise is registered as an occurrence** (`MDO-006`, the chronology
   table). It carries no Mohenjo-daro sentence, but the negative
   identification is inert without it, and a survey that recorded only the
   conclusions would leave the actual failure unregistered.
2. **A control occurrence is registered** (`MDO-014`,
   `vedic-ritual-economy.html:326-328`), which is *not* a breach. A survey
   that recorded only failures would misdescribe the site. This page states
   the same claim attributively, in the plural, dated as a state of evidence,
   and as a limit on itself under the heading "Two things this page will not
   say". That is the house standard, and its existence is part of the
   evidence for `BF-028`: the site is capable of the careful formulation and
   published the careless one in larger type elsewhere.
3. **`MDO-007` records what the page already gets right** — that it concedes
   the geography, states the residual positively, and closes "No specific
   site has been identified with any named fort, and this platform does not
   name one." Registered so that a later repair does not remove it.

**Publication state of the prototypes, stated precisely because "prototype"
suggests "private" and it is not.** `prototypes/*` are on `main`, carry
`noindex,nofollow`, are absent from `sitemap.xml`, and are excluded by no
`netlify.toml` rule. They are **deployed and publicly reachable by URL**,
unindexed and unlinked. Not live in the linked sense; not private either.

---

## 4. Constitution §6 worksheet for `DFO-002`

`DFO-002` — *the identification has been institutionally dismissed rather
than evidentially refuted* — asserts an absence: the absence of an evidential
refutation. §6 requires the absence to be characterised before it is argued
from, then typed. **It is not typed here, and it cannot be, because typing it
needs a literature search this unit did not run.** The worksheet is set out
so the work is nameable.

| §6 field | State |
|---|---|
| What evidence should exist | A published refutation engaging the identification on evidence: a chronology, a stratigraphic argument, a survey result, a translation argument about *púr-*, or a demonstration that the proposed sites fail a test. |
| Where | Indological and South Asian archaeology journals and monographs; excavation reports; review literature; conference proceedings; and — since the claim is about *dismissal* — the citation record around each named proponent. |
| Probability of original production | **Unknown and probably high.** This is a much-discussed question in a large literature. An absence here would be surprising in a way an absence in a thin field would not, which raises rather than lowers the bar for the claim. |
| Probability of survival | Near certain for anything published since c. 1900. Not a preservation question. |
| Coverage of search | **Zero.** No literature search was run. This is the binding gap. |
| Accessibility | Partly paywalled; some monograph literature is offline. A real constraint, and one that could produce a false `NOT PUBLISHED` if not checked. |
| Ability to recognise it | **The hard one.** A refutation may not be labelled as one. Dismissal and refutation are not always separable in practice: a footnote saying "on chronological grounds this is no longer tenable" is *both*, and which it counts as depends on whether the grounds were ever argued. The claim's own distinction may not survive contact with the literature, and that possibility is part of what a search would test. |
| Alternative reasons for non-detection | We have not looked. |
| **Type** | **UNTYPED.** From where this repository stands, "no refutation was published" and "a refutation was published and we have not read it" are indistinguishable. |

**The consequence is that `DFO-002` is not merely unverified but unformed,**
and that is recorded in its own notes rather than softened.

**§6's residual rule also caps what `DFO-002` could ever do.** "Unknown" is
residual and never a positive rival explanation. So even fully established,
`DFO-002` would move `DFO-001` nowhere: it would establish that a question
was not closed, which is a fact about a field, not about a landscape. That
is what `BR-F-001` records.

**Step 11 is the instrument, not step 6.** Step 11 asks a position to be
placed as historically influential, currently supported, revised, disputed,
held by citation inertia, abandoned, or rejected. *Abandoned* and *rejected*
are different verdicts, and `DFO-002` asserts the first against the second.
A step-11 standing audit could settle it. None exists here. The position to
trace first is Parpola's, which `dasa-forts-rigveda.html:441` already cites
in the opposite direction ("Parpola argued explicitly that the Dāsa forts are
BMAC") — so the page's own text names a proponent whose treatment by the
literature is exactly what `DFO-002` is about.

---

## 5. The two adversarial tests

### 5.1 Prestige-bias challenge

*Did this unit privilege a claim because it is canonical, Sanskritic,
Brahmanical, Indo-European, European, colonial, institutionally prestigious,
repeatedly cited or nationally useful?*

**The finding this test produced is `BF-027`'s second-order clause, and it is
the sharpest thing in this unit.** The c. 1500–1200 BCE date is canonical,
Indo-European-studies-derived, colonial in origin and repeatedly cited. It
was made load-bearing on a published page with no source, and it is in no
register here at any status — checked across every file in `03-REGISTERS/`.

The reason it survived unexamined is worth stating: **the conclusion drawn
from it is deflationary.** It cuts against the identification a
Hindu-nationalist chronology wants. So the date passed unchallenged in the
one place a sceptical reader was least likely to challenge it. A canonical
premise was protected by the unpopularity of its conclusion. That is a
mechanism this project should expect to meet again.

**Where this unit itself is exposed.** It accepted, without retrieval, that
the Harappan urbanism range c. 2600–1900 BCE is excavated and
radiocarbon-anchored while the Rigveda range is inferred. The first is far
better evidenced, but this unit did not retrieve a source for *either* and
should not be read as having audited the first. `RA-023` carries it.

### 5.2 Preferred-counter-narrative challenge

*Did this unit accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**`DFO-002` is the live exposure and it was registered, not resolved.**
"Dismissed, not refuted" is the standard form of an appeal against a
scholarly consensus. It is available for free to any position that has lost
an argument, it cannot be refuted from inside the position it defends, and it
is *correct often enough* — constitution §4V and the archive audit exist
because institutional power does shape what gets recorded — that dismissing
it would be its own failure.

It is therefore given the same status as `DFO-001`, no rhetorical advantage
for being anti-institutional and no penalty for it either, and the work that
would test it is named rather than performed.

**The second exposure runs the other way and matters more here.** The claim
`DFO-002` defends — the identification of the Rigvedic forts with Indus sites
— is used by Hindu-nationalist chronologies. So this unit was under pressure
from two directions at once: to protect a deflationary consensus because it
is anti-nationalist, and to reopen an identification because the owner raised
it. `BR-F-001` blocks both moves explicitly rather than picking one.

**A third, smaller one.** `BF-028` finds "fell to a river" convenient to the
page's argument. That reading is itself convenient to *this* unit — it makes
a tidy story about a hedge dropped for effect. The alternative, that it is
ordinary compression in display copy with no argumentative motive, is not
excluded, and `BF-028` does not need it: the failure is that a contested
cause is published unhedged and self-contradicted, which holds whatever the
motive was.

---

## 6. What this unit did not do

- **Did not resolve `DFO-001` or `DFO-002`.** Instructed not to, and could
  not have: no retrieval bears on either.
- **Did not write replacement copy.** Instructed not to. `CORRECTIONS-PENDING.md`
  is the place for that when the corrections are ready, and they are not.
- **Did not reopen "three centuries too late" on the axis prior work
  closed.** `CORRECTIONS-PENDING.md` §3.2.1 records that the *púr-* stratum
  measurements cannot correct that headline, because they measure position
  *within* the Rigveda while the headline measures the Rigveda *against*
  Indus urbanism — *"a false conflict, recorded so it is not re-raised."*
  **That still stands and `BF-027` does not touch it.** `BF-027` objects on
  the axis the headline is actually on: that the Rigveda end of the
  subtraction is itself inferred and unaudited. Anyone revisiting `RA-022`
  must keep these two apart.
- **Did not adjudicate the cause of Harappan deurbanisation**, and states in
  `BF-028` that it did not.
- **Did not touch site code.** `CLAUDE.md` forbids it. `IC-F-002` and
  `RA-024`/`RA-026` are referred, not fixed.
