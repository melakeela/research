# Rules, gates and adversarial tests

**Written:** 2026-09-08
**Subject:** `01-investigation-spec.md`, the children's investigation
"A hundred stone forts".

---

## 1. Framework §10.4.4 — rule by rule

| Rule | How this investigation stands against it |
|---|---|
| **No fabricated evidence, ever.** No invented objects, no composite "typical" artefacts, no illustrative reconstructions without the marker. | **Compliant, and the constraint shaped the product.** Every string a child reads that purports to be evidence is in `03-evidence-cards.md` with its register row and locator. There is **no image of a fort anywhere in the investigation**, because any such image would be a reconstruction of the object S-10 exists to say we do not have. |
| **Reconstructions are labelled**, in the child's own words, with what they were based on. | **Not engaged.** There is no reconstruction. Recorded rather than passed over. |
| **No ethnic or national identification of objects, people or remains.** | **Compliant.** No object, person or remain is identified with any group. The `dāsa`/`ārya` material is excluded entirely, and the exclusion is stated to the child (S-10). |
| **Human remains** only where community-authority and consent permit; never as a puzzle; exclusions stated to the child. | **Not engaged.** Nothing in the púr- corpus is a remain. D-026 is not reached. Recorded rather than passed over. |
| **No competition, no scoreboard, no time pressure.** | **Compliant.** No score, no correct/incorrect marking, no timer, no streak, no progress reward, on any screen. S-11's fourth statement is the only place a child can be wrong against the evidence, and it is still not marked. |
| **No sorting of human beings, no reward for extremist categories, no persecution staged as an experience.** | See §2. |

## 1.1 Framework §10.4.5 — safeguarding and data

| Rule | Standing |
|---|---|
| No account, none offered to under-16s; Field Bag local | **Compliant.** S-00 asks for nothing. S-13's bag is local; export is a file, not an upload. |
| No behavioural analytics, no third-party trackers, no advertising | **Compliant by specification.** Aggregate non-identifying counts only, measurement policy published. Named as gate **G-11** because it is an implementation property, not a design one, and a specification cannot enforce it. |
| No free-text publication; child text never transmitted, never enters the correction pipeline | **Compliant, and it forced a decision.** Framework §9.4 routes a PROVE IT disagreement into the correction pipeline. S-12 records disagreements and **does not transmit them**. §10.4.5 governs over §9.4 for this mode; `01-investigation-spec.md` S-12 states the resolution. |
| No photographs of children, no user-uploaded images | **Compliant.** No upload surface exists in the investigation. |

---

## 2. Framework §10.4.7 — the three constraints, and the one that binds hard

**Constraint 1 — no interface that asks a child to sort human beings.**

This is the constraint the fort material tests, and the framework says so
itself: backlog item 33's `COMPARE` step *"is the sorting interface the first
constraint forbids, and the flow supplies the buckets itself."*

The register would supply those buckets readily. `PUR-022` lists `ṛjiśvan-`,
`pipru-`, `divodāsa-`, `dāsī-`, `śambara-` and `śuṣṇa-` at 15× to 54× their
corpus rates inside fort stanzas; `PUR4J-030` splits 22 patron-side names from
22 opponent-side names; `PUR4J-010` records that the counts sort by narrative
cycle. A `COMPARE` step built on the strongest signal in the register would be
two piles of names and a question about which side each fort belonged to. **That
is the forbidden interface.** Framing it as a debunking would not lift the
prohibition; the child would still perform the sort.

**How the design implements the prohibition, and why it is not a filter.**

1. **`COMPARE` (S-08) admits exactly four kinds of term:** counts, materials,
   grammatical cases, words. The admissible set is closed at the interface, not
   at run time. A subject filter would not implement §10.4.7, because the same
   interaction is the same interaction whatever is loaded into it — the
   framework's own reasoning, applied here.
2. **Names are read, never operated.** `dívodāsāya` stands in the line at S-01
   and S-07 and stays in the line. It is never a card, bucket, drag target,
   filter or option. A standing card beside it tells the child the museum does
   not put people into groups. `PUR4J-010` is quoted on S-06 and S-12 **in
   prose**, as the reason the museum is unsure — never as a set of names to
   arrange. Gate **G-02**.
3. **The `dāsa`/`ārya` material is out of scope, and the exclusion is stated to
   the child** rather than silently applied, per §10.4.4's rule for excluded
   material.

**Constraint 2 — no points, scores or badges for extremist categories.** Not
engaged: there is no reward mechanic of any kind anywhere in the investigation,
for any category. §10.4.4's blanket prohibition on competition already covers it
and this design does not test the edge.

**Constraint 3 — no persecution as spectacle.** Not engaged. The corpus is about
walls being broken. No siege, capture, killing or subjugation is staged,
dramatized, role-played, simulated or reconstructed as an experience. `PUR-022`
and the `the-killed.html` page it also supports sit outside this investigation.

**Standing of these three constraints.** `INHERITED-UNVERIFIED` as to their
wording (§10.4.7; `RESEARCH-QUEUE.md` `WMP-9`; `D-037`), and binding regardless,
because they are prohibitions on what the institution builds rather than claims
about the past. This unit treats them as binding and cites none of them as
evidence for anything.

---

## 3. Posture and mode — and the derivation does not clearly fire

**This section was rewritten under adversarial review, which found the original
derivation both uncounted and self-contradicting. The corrected position is
weaker and is stated as such.**

### 3.1 What rule 3 actually requires

Framework §1.5 rule 3: *"If the **majority of the exhibit's load-bearing
propositions** resolve to typed absences rather than to positive claims →
**Nocturnal Veḷi**."*

The unit of the majority is **the exhibit's propositions**. It is not the
proportion of passages inside an individual claim.

### 3.2 Counting it properly

Of the 45 claim rows in `02-claim-basis.csv`, the rows carrying a constitution
§6 type are:

- `PUR4J-012` — 93 of 103 passages state no material, typed `NOT PRODUCED`.
- `PUR4J-016` / `HOLD-006` — passages whose heading names no poet, typed
  `NOT PRODUCED`.

`PUR4J-018` is a claim that a **dataset** carries no geographic content — an
absence in VedaWeb's metadata files, not a typed absence in the record of the
past. `PUR4J-024`'s "NOT ASSIGNED" is not one of §6's eight types.
`PUR4J-001`'s 82-of-103 is not typed anywhere. `HOLD-007` is a hold and §5 of
this document argues at length that it is **not** a typed absence and must never
be treated as one.

**That is 2 or 3 rows of 45. It is not a majority, and rule 3 does not fire on
the count.**

### 3.3 What the original derivation did, and why it was wrong

It listed six items and asserted a majority without counting, and it counted
*proportions inside individual claims* (82 of 103 passages, 93 of 103 passages)
where rule 3 counts *propositions of the exhibit*. Worse, it silently amended
the rule: §1.5 rule 3 says "typed absences", the derivation said "typed absences
**or holds**", and the hold it added was `HOLD-007` — which §5 of this same
document insists is not a typed absence. **§3 and §5 contradicted each other,
and the contradiction was load-bearing.** Recorded here rather than deleted.

### 3.4 Where that leaves the posture

Rules 1, 2 and 5 do not fire: no withheld access, no repair state, and the
supporting evidence is textual rather than material or site-bound.

**Rule 4 — relation dominance — is live and was dismissed too fast.** The
original text asserted "the substance is Claim Objects rather than Relationship
Objects" and moved on. But S-08's Field Bag entry records three comparisons *as*
Relationship Objects, and the investigation's governing question — how a textual
attestation stands to a material one — is a comparison. Against that: the
investigation's 45 load-bearing rows are Claim Objects almost without exception,
and the three comparisons are built *from* those rows rather than being the
substance the rows serve. The rule is close, not clearly failed, and it is not
this unit's to settle. **Rule 4 → Living Signal Field**, where §1.7 also makes
Field Mode *available*.

**Rule 7, the residual, gives Reading Room**, where §1.7's table makes Field Mode
**forbidden**.

**So the derived posture is Nocturnal Veḷi only on a reading of rule 3 this unit
can no longer support by counting, Living Signal Field on a plausible reading of
rule 4, and Reading Room on the residual.** Two of the three permit Field Mode
and one forbids it.

### 3.5 The consequence, stated plainly

**This is now an open question that gates the build, not a settled derivation.**
An assigned posture is editorial (§1.5) and may override a derived one with a
logged reason — so the investigation is not thereby forbidden. What it may not
do is claim a derivation it does not have.

`04-rules-and-gates.md` cannot assign the posture. Gate **G-01** now requires
the assignment to be made by whoever holds the Editorial Register, with the
derivation above in front of them, and with an `override_reason` written if the
assignment is Nocturnal Veḷi. An override with an empty reason is invalid
(§1.5).

### 3.6 A contradiction in the governing document, found while relying on it

§1.7's **table** gives Reading Room / Field = *forbidden*. §1.7's **prose**,
immediately below the same table, states the rule as *"Field Mode is forbidden
in Extraction / Collection and Reconnection"* — omitting Reading Room.

Since §1.5 rule 7 makes Reading Room the **residual** posture, whether Field Mode
is forbidden there decides whether a large class of children's work may be built
at all, and the framework says it two ways. This unit reads the table as
governing, because it is the more specific statement. **That reading is recorded,
not settled**, and is logged as `IC-P-004` in
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv`.

### 3.7 The posture's Avoid, whichever it is

Nocturnal Veḷi's `Avoid` is *"no fantasy portal or occult styling"*, and it is a
live risk, because "the mystery of the ninety-nine forts" is the register this
material invites. Refused: every unknown here is ordinary, countable and
specific, and each is shown with what it would take to close it. Living Signal
Field's `Avoid` — *"no gaming HUD or arbitrary links"* — is met by the absence of
any score, timer or progress mechanic. Reading Room's — *"no visual fatigue or
luxury minimalism"* — is a presentation matter outside this repository.

## 4. Constitution §14 — the public-copy shape

Step 14 requires: QUESTION / WHAT IS OBSERVED / WHAT THE EVIDENCE SUPPORTS /
WHAT COMPLICATES IT / WHAT REMAINS UNKNOWN / MELAKEELA'S CURRENT INTERPRETATION /
WHAT WOULD CHANGE IT.

| Step-14 element | Where it lands |
|---|---|
| QUESTION | S-00 |
| WHAT IS OBSERVED | S-01, S-02, S-04, S-05, S-06, S-07, S-09 |
| WHAT THE EVIDENCE SUPPORTS | S-08, S-11 |
| WHAT COMPLICATES IT | S-06 (counts sort by story), S-07 (iron/bronze), S-09 (second instrument null, and entangled) |
| WHAT REMAINS UNKNOWN | S-10 |
| MELAKEELA'S CURRENT INTERPRETATION | S-12, **disclosed last** per framework §9.3 |
| WHAT WOULD CHANGE IT | S-12 |

The order is not the constitution's order. WHAT REMAINS UNKNOWN is placed
immediately before DECIDE rather than after it, so that the child's conclusion
is formed *with* the absences in view rather than after being handed one. This is
a deliberate departure and is recorded as such.

---

## 5. The negative-evidence standard, and the distinction the investigation exists to teach

Constitution §6 types an absence as one of `NOT PRODUCED` · `NOT PRESERVED` ·
`NOT EXCAVATED` · `NOT PUBLISHED` · `NOT ACCESSIBLE` · `NOT RECOGNIZED` ·
`DOCUMENTED DESTRUCTION` · `ABSENT DESPITE ADEQUATE SEARCH`.

**Absences in this investigation that are typed:**

- 93 of 103 passages state no material → `NOT PRODUCED` (`PUR4J-012`). A hymn
  praising the breaking of a wall had no occasion to say what the wall was made
  of. Shown to the child as **WE DON'T KNOW — nobody wrote it down.**
- Poet attributions → `NOT PRODUCED`, and **the two sources disagree on how
  many.** `PUR4J-016` (`VERIFIED`) gives 55 passages with a poet and 48 without,
  and types **all 48**. `HOLD-006` types **45** — the deity-headed ones — and its
  closing paragraph says "the 58 that have one", against `PUR4J-016`'s 55. The
  3 headings that name neither a poet nor a deity (a metre, a collection, and a
  strophe-type that is also a poet's name) are counted with the poets in one
  file and against them in the other.
  **An earlier draft of this section picked 45 from one file and 48 from the
  other and reconciled them with a sentence neither source contains.** That is a
  brief silently correcting a `VERIFIED` register row. Withdrawn: the
  discrepancy is now stated as a discrepancy and logged as `RA-021` in
  `04-AUDITS/REAUDIT-QUEUE.csv`. Whichever number is right, the typing is
  `NOT PRODUCED` and the reasoning is `HOLD-006`'s: Geldner's headings are an
  arrangement, and where he arranged by deity he recorded no poet. That is not
  evidence the hymn is anonymous.
  Not in scope for any screen; recorded here because S-03 tells the child that
  two of their six questions have no answer.

- **`PUR4J-018` is not an absence about the poem, and S-10 must not use it as
  one.** It is `VERIFIED` that the *pinned corpus* carries no geographic content
  — `info/rv_locations.tsv` is a citation-format conversion table. That is an
  absence in VedaWeb's metadata, not in the Rigveda. What the *poem* carries is
  `PUR4J-028`: six passages hold `sindhu-`, three a proper name for both
  translators, two a common noun for both, one disputed. S-10 was rewritten
  under review, which found it telling the child "the poem never says where, not
  once" while citing the very row recording three agreed river-names. The
  simplification ran toward the investigation's own thesis, which is the
  direction to watch.

**The absence that is NOT typed, and must not be.**

`HOLD-007` — no archaeological source in `02-SOURCES/access-ledger.csv` — is
**not** an absence under §6 and is not typed as one. §6 types absences *in the
record of the past*: what should exist, where, whether it was produced,
preserved, excavated, published, reachable, recognisable. An unrun retrieval is
none of those. It is a fact about this repository's to-do list.

Typing it as `NOT EXCAVATED` would assert that the relevant ground has not been
dug — which this unit has not established and has no source for. Typing it as
`ABSENT DESPITE ADEQUATE SEARCH` would be worse: no search was made.

**This distinction is the investigation's whole subject at the adult grain, and
S-10 is it at the child's grain.** A child who leaves able to say "we haven't
looked" rather than "there's nothing there" has learned the thing the museum
finds hardest to say about itself. If the two kinds of WE DON'T KNOW were
collapsed into one word, the investigation would teach the opposite lesson.

---

## 6. Prestige-bias challenge

*Did this privilege a claim because it is canonical, Sanskritic, Brahmanical,
Indo-European, European, colonial, institutionally prestigious, repeatedly cited
or nationally useful?*

**Three risks found, two corrected in the design, one recorded as a standing
control.**

1. **The English word "fort", handed over free.** The whole investigation is
   about a Sanskrit word, and every screen after S-02 would be reasoning about
   an English category if the child were simply given one. Constitution §7 names
   *fort* in its list of inherited English categories to audit before use.
   **Corrected:** S-02 makes the child choose the English word from the ones real
   translators used, records the choice as theirs, and shows Grassmann's actual
   gloss — *a wall of stones and clay* — before the menu. The choice is then
   used as the label on every later screen.
2. **Four translators presented as four checks.** Griffith, Geldner, Grassmann
   and Renou agreeing looks like corroboration. `DEP-021` and `DEP-023` record
   that it is not. **Corrected:** gate **G-06**, and the independence warning
   travels on `EC-02`.
3. **Arnold, and the prestige of a χ².** S-09 carries a real statistical result
   (`PUR-018`, p = 0.0057) resting on a single 1905 monograph (`PUR-013`,
   `DEP-001`) whose periodisation is a `HYPOTHESIS` (`PUR-028`). A number with a
   p-value on it is the most persuasive thing in the investigation and the least
   secure. **Controlled, not corrected:** the whole screen is a MAYBE, the banner
   cannot be dismissed, the p-value is not shown to the child at all, the null
   from the second instrument is shown, and the entanglement between the two
   instruments is shown. This is the strongest available control and the screen
   is still the investigation's weakest.

No `BIAS-FAILURE-LOG` row is warranted: all three were caught and handled inside
this unit rather than after it.

## 7. Preferred-counter-narrative challenge

*Did this accept a claim too easily because it is Dravidian, Indigenous,
anti-colonial, anti-Brahmanical, subaltern, diffusionist or politically
corrective?*

**One risk, and it is the investigation's central temptation.**

The available soft landing is to teach the child that the poem is *just* a poem —
that "ninety-nine" is a figure of speech, that no forts existed, that the whole
thing is boasting. It is deflationary, it flatters a sceptical posture, it costs
nothing to assert, and every screen from S-04 to S-06 leans that way.

The register refuses it and so does this design:

- `PUR4J-I-01` is held at `PROVISIONAL` *because* it is the convenient answer,
  and `BF-014` logs a preferred-counter-narrative failure against its first
  version, where three of five parts of a supporting claim were wrong and all
  three errors ran toward its own conclusion.
- **S-06 therefore shows the evidence against the museum's own reading, on the
  same screen, immediately after showing the reading**: the counts sort by
  narrative cycle, "seven autumnal forts" is near-verbatim at two locators, and
  ornament should not sort by story (`PUR4J-010`).
- **S-12 states the limit explicitly:** `PUR4J-I-01`'s own
  `what_it_does_not_establish` — a formulaic count can be attached to a real
  siege; the number being conventional says nothing about whether anything was
  besieged.
- **`PUR4J-026` is on S-12** to stop S-06 collapsing: all six ninety-nine
  passages are textual strongholds. The formulaic character of the *count* does
  not make the *passages* formulaic.
- **S-10's answer options do not include "no".** They include "we don't know,
  and nobody here has looked", which is the honest position. Selecting "no" is
  permitted and returns "that might turn out to be right; right now nobody here
  can show you why" — the same response as "yes".

Gate **G-10** exists so that no screen presents `PUR4J-I-01` more confidently
than the register does.

## 7.1 A third test this unit ran on itself

*Did the design choose its centre because it teaches well, rather than because
the evidence is strongest there?*

S-06 — the river passage — is placed at the centre because a child can verify it
unaided in under a minute. That is a pedagogic reason, not an evidentiary one,
and pedagogic reasons are how children's material gets built on the memorable
rather than the true.

**Checked and upheld.** `PUR4J-006` is `VERIFIED`, is the counts unit's own
declared control case, and its note records that it is the case that defeats a
stanza-level co-occurrence measure — the same restraint `PUR-022` exercised. It
is both the most teachable and among the most load-bearing rows in the register.
Where those two coincide, taking the coincidence is not a failure. It is recorded
so that a later reviewer can check the reasoning rather than the outcome.

---

## 8. The build gates

Twelve. None is optional. Each blocks the screen or screens named.

| Gate | Blocks | What must happen |
|---|---|---|
| **G-01** | everything | Posture **assigned** by whoever holds the Editorial Register, with §3's derivation in front of them and an `override_reason` written if the assignment is Nocturnal Veḷi. §3.2 shows rule 3 does not fire on a proper count; rule 4 is live; rule 7's residual is Reading Room, where §1.7's table forbids Field Mode. An override with an empty reason is invalid (§1.5). **Not a label — on the residual reading this investigation may not be built.** See also `IC-P-004`: §1.7's table and its own prose disagree about Reading Room. |
| **G-02** | S-06, S-08, S-12 | `PUR4J-010` and `PUR4J-030` are readable as prose and are structurally incapable of entering any comparison, filter or drag interface. Verified against the built interface, not the design. §10.4.7. |
| **G-03** | S-04, S-05, S-07, S-09 | Every count in the investigation is at the stanza unit (103), and the screens say so. **D-044 does not block this** — `OWNER-DECISIONS.csv` gives its `blocks` as "Nothing. The corpus is built at the stanza and every register is keyed on it; a change would be a rebuild, not a blocker", and `CLAUDE.md` makes that file authoritative. An earlier draft of this gate asserted D-044 as a blocker against its own register row; withdrawn. What the gate actually checks is that no screen mixes units — the token, pāda, stanza and hymn figures are all in the registers and only the stanza figures may reach a child. |
| **G-04** | S-11, S-12 | No screen uses the inherited "99" as a quantity of forts: it appears only as a `VERIFIED` count of six passages (`PUR4J-002`). **This gate failed in the first draft and the failure is instructive.** S-11 labelled *"Ninety-nine is the famous number"* as **FOUND** on `PUR4J-I-02`, which is `PROVISIONAL` — the mapping broken in the promoting direction — and the only evidence in this repository that 99 *is* famous is MelaKeela's own unsourced page headline and Version 12 line numbers, i.e. `INHERITED-UNVERIFIED` material, so §0.2 was breached on the same line. The gate had been written to catch 99-as-a-quantity and did not think to check 99-as-a-reception-fact. Now: **the reception claim is WE THINK, and the screen tells the child the museum has not checked where it got the number from.** D-045 remains not a blocker. |
| **G-05** | S-01, S-07 | Diacritic and encoding pass against the pinned corpus. Specifically: the `vy āā̀syat` artefact in `PUR-P-041` resolved, and the verbatim Griffith / Geldner / Grassmann renderings of RV 4.30.20 pulled from `SRC-072`–`SRC-074` to replace the register's paraphrase. Requires a fresh clone at `d3eb8af`. |
| **G-06** | S-02 | The translator menu does not present four translators as four independent checks. `DEP-021`, `DEP-023`. **Note:** `DEP-021`'s `source_b` points at `SRC-026` (Arnold 1905) where its own prose describes Grassmann's *Wörterbuch*, which has no ledger row. The dependency it records is right; its pointer is not. Logged as `IC-P-003`. Do not implement this gate by following the pointer. |
| **G-07** | S-03 | The six offered questions are bound to real `mk:qst:` nodes (§2.1, §6.6). No `mk:` identifier has been minted in this repository. |
| **G-08** | all draft copy | Reading-age test on every quotation block in `01-investigation-spec.md`, with children in the 8–11 band, before any of it is used. The copy is drafted from statused claims; it is not tested for comprehension. |
| **G-09** | S-02, S-06, S-07, S-10 | **Rights position per quoted translation** (§11.8). Griffith 1890 and Grassmann 1876–7 are long out of copyright on their publication dates. **Geldner 1951, Renou and Elizarenkova 1989–99 are not obviously so**, and a children's product quoting them publicly needs an answered rights position, not an assumption in either direction. Bears on D-029 and D-030. This unit takes no position and has no legal advice. |
| **G-10** | S-06, S-12 | No screen presents `PUR4J-I-01` more confidently than `PROVISIONAL`, and the evidence against it (`PUR4J-010`) appears on the same screen as the reading. §7 above. |
| **G-11** | everything | No behavioural analytics, no third-party trackers, no advertising, verified in the built artefact. Aggregate non-identifying counts only; measurement policy published. §10.4.5. |
| **G-12** | S-09 | The by-**hymn** observed and expected stratum counts derived from `rigveda-pur-family-occurrences.csv` (86 hymns of 1,028), because `PUR-018`'s note makes the hymn the unit to quote and tokens within a hymn are not independent. This unit did not derive them — that is a corpus operation and this unit performed none — and the screen may not ship with the token-level table standing in. Requires the same fresh clone as G-05. |

**And one that is not a gate but an owner decision.** **D-046** — whether a
corpus investigation is admissible as the children's pilot at all. D-006 offers
Keezhadi or an inscription; this is neither. Raised in `DECISIONS-NEEDED.md`.

---

## 9. Review history, and what to attack next

**This unit was adversarially reviewed on 2026-09-08 and repaired.** The review
found 30-odd defects; the repairs are in the branch history, and the ones that
changed a position rather than a sentence are recorded in place rather than
tidied away — §2 (the indirect COMPARE breach), §3 (the posture derivation,
rewritten), §5 (the poet figures and the `PUR4J-018` misuse), gates G-01, G-03,
G-04 and the new G-12, and §0.1 and §0.2 of the spec.

Four repairs were substantive enough to name here:

1. **The posture derivation did not fire on a proper count**, and had silently
   amended rule 3 to include holds — the holds §5 of this document insists are
   not typed absences. §3 now says so and G-01 requires an editorial assignment
   with a written reason instead. **On the residual reading this investigation
   may not be built at all**, and that is now visible rather than argued past.
2. **`PUR4J-013` was absent from the entire unit** — the row recording that only
   one of the eight metal forts is an enemy's, and that in two of them the fort
   *is* a god or a river. Its omission left `PUR-027` less challenged than the
   register leaves it *and* withheld from S-07 the sharpest evidence in the
   corpus for the investigation's own question. It is now on both screens.
3. **S-08 performed the excluded move with the vocabulary stripped out** — "the
   other side", "somebody else's forts" — while S-10 told the child the museum
   was not showing them that material. A compliance table checking only for
   name-cards passed it.
4. **Four child-facing FOUND statements overstated their rows**, all four in the
   direction of the investigation's own thesis. That direction is the finding,
   not the four sentences.

**What to attack next.** The reviewer's own list, plus what it declined to check:

1. **S-09 should probably not exist.** It rests on a `HYPOTHESIS`, its second
   instrument returns a null, the two are entangled, and it now also carries an
   unfilled gate (G-12) because the by-hymn figures have not been derived. The
   case for keeping it is that it is the only screen where a child meets a real
   result *and* the reason not to trust it. That case may be wrong.
2. **S-10's empty box may be too abstract for eight.** Whether an eight-year-old
   gets *"we haven't looked"* as distinct from *"there's nothing there"* is
   empirical. G-08 answers it; a failure there is a redesign of S-10, not a
   relaxation of it.
3. **Every original-language string is provisional.** G-05 and G-12 mean the
   primary-source layer and the S-09 figures are not yet fixed. This is a
   specification whose evidence layer awaits a clone.
4. **The exit criterion's first sentence rests on the museum's own paraphrase**
   (`PUR4J-014`), not a translator's words. G-05 blocks it. The claim survives
   the substitution; the sentence may not.
5. **`BIAS-FAILURE-LOG.csv` has not had a full column-by-column pass against
   this unit.** The reviewer checked `RA-018`'s `future_control` (arguments from
   absence require a stated search coverage — and found S-09's banner breaching
   it, now repaired) and did not check the others. That pass is outstanding.
6. **This unit read the registers; it did not re-run them.** `RA-001` is open
   against `PUR-003`–`PUR-005`, and the claim basis now says so on those rows
   instead of calling them settled.
