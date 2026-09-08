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

## 3. Posture and mode — the gate hiding inside a label

Derivation is in `01-investigation-spec.md` §2. Restated here because it decides
whether the investigation may exist:

- **§1.5 rule 3, absence dominance, fires.** The majority of load-bearing
  propositions resolve to typed absences or holds: `PUR4J-001` (82 of 103 state
  no count), `PUR4J-012` (93 of 103 state no material), `PUR4J-018` (no
  geography at all), `PUR4J-016`/`HOLD-006` (48 of 103 poet attributions
  `NOT PRODUCED`), `PUR4J-024` (three of five types `NOT ASSIGNED`), `HOLD-007`
  (no ground evidence). → **Nocturnal Veḷi.**
- Rules 1, 2, 4, 5 do not fire; rule 7 (Reading Room, the residual) is reached
  only if rule 3 is not applied.
- **§1.7:** Field Mode is *available* in Nocturnal Veḷi and **forbidden** in
  Reading Room.

**Therefore a careless posture assignment does not mis-label this investigation.
It forbids it.** The assignment must be written to the Editorial Register with
`derived_posture`, `assigned_posture` and (empty) `override_reason` before any
build. Gate **G-01**.

The posture's `Avoid` — *"no fantasy portal or occult styling"* — is a live risk,
because "the mystery of the ninety-nine forts" is the register the material
invites. Refused: every unknown in this investigation is ordinary, countable and
specific, and each is shown with what it would take to close it.

---

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
- 48 of 103 poet attributions → `NOT PRODUCED` (`PUR4J-016`, `HOLD-006`).
  Geldner's headings are an arrangement; where he arranged by deity he recorded
  no poet. Not in scope for any screen; recorded here because S-03 tells the
  child two of their six questions have no answer.

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

Eleven. None is optional. Each blocks the screen or screens named.

| Gate | Blocks | What must happen |
|---|---|---|
| **G-01** | everything | Posture assignment written to the Editorial Register with its §1.5 derivation. Nocturnal Veḷi permits Field Mode; Reading Room forbids it. §1.7. |
| **G-02** | S-06, S-08, S-12 | `PUR4J-010` and `PUR4J-030` are readable as prose and are structurally incapable of entering any comparison, filter or drag interface. Verified against the built interface, not the design. §10.4.7. |
| **G-03** | S-04, S-05, S-07, S-09 | **D-044** — the row unit of the §4J corpus — is answered. Every count in the investigation is at the stanza unit (103). A different unit changes every figure a child handles. |
| **G-04** | S-11, S-12 | No screen uses the inherited "99" as a quantity of anything. It appears only as a `VERIFIED` count of six passages (`PUR4J-002`) and as a fact about reception (`PUR4J-I-02`). D-045 is therefore not a blocker, and this gate is the check that it stays that way. |
| **G-05** | S-01, S-07 | Diacritic and encoding pass against the pinned corpus. Specifically: the `vy āā̀syat` artefact in `PUR-P-041` resolved, and the verbatim Griffith / Geldner / Grassmann renderings of RV 4.30.20 pulled from `SRC-072`–`SRC-074` to replace the register's paraphrase. Requires a fresh clone at `d3eb8af`. |
| **G-06** | S-02 | The translator menu does not present four translators as four independent checks. `DEP-021`, `DEP-023`. **Note:** `DEP-021`'s `source_b` points at `SRC-026` (Arnold 1905) where its own prose describes Grassmann's *Wörterbuch*, which has no ledger row. The dependency it records is right; its pointer is not. Logged as `IC-P-003`. Do not implement this gate by following the pointer. |
| **G-07** | S-03 | The six offered questions are bound to real `mk:qst:` nodes (§2.1, §6.6). No `mk:` identifier has been minted in this repository. |
| **G-08** | all draft copy | Reading-age test on every quotation block in `01-investigation-spec.md`, with children in the 8–11 band, before any of it is used. The copy is drafted from statused claims; it is not tested for comprehension. |
| **G-09** | S-02, S-06, S-07, S-10 | **Rights position per quoted translation** (§11.8). Griffith 1890 and Grassmann 1876–7 are long out of copyright on their publication dates. **Geldner 1951, Renou and Elizarenkova 1989–99 are not obviously so**, and a children's product quoting them publicly needs an answered rights position, not an assumption in either direction. Bears on D-029 and D-030. This unit takes no position and has no legal advice. |
| **G-10** | S-06, S-12 | No screen presents `PUR4J-I-01` more confidently than `PROVISIONAL`, and the evidence against it (`PUR4J-010`) appears on the same screen as the reading. §7 above. |
| **G-11** | everything | No behavioural analytics, no third-party trackers, no advertising, verified in the built artefact. Aggregate non-identifying counts only; measurement policy published. §10.4.5. |

**And one that is not a gate but an owner decision.** **D-046** — whether a
corpus investigation is admissible as the children's pilot at all. D-006 offers
Keezhadi or an inscription; this is neither. Raised in `DECISIONS-NEEDED.md`.

---

## 9. What an adversarial reviewer should attack first

Recorded so the next reviewer does not have to find it.

1. **S-09 should probably not exist.** It rests on a `HYPOTHESIS`, its second
   instrument returns a null, and the two instruments are entangled. The case for
   keeping it is that it is the only screen where a child meets a real
   statistical result *and* the reason not to trust it, and that an investigation
   with no MAYBE screen teaches that the four words are three. That case may be
   wrong. If it is, the investigation loses one screen and no claim.
2. **S-10's empty box may be too abstract for eight.** Searching a list of 88
   sources and finding nothing is a sophisticated experience. An eleven-year-old
   will get it. Whether an eight-year-old gets *"we haven't looked"* as distinct
   from *"there's nothing there"* is an empirical question this specification
   cannot settle. G-08 is where it gets answered, and a failure there is a
   redesign of S-10, not a relaxation of it.
3. **The stone fort is a hundred-fort passage, not a ninety-nine one.** The title
   "A hundred stone forts" is accurate to `PUR4J-002` and `PUR4J-012` and is
   deliberately *not* the famous number. A reviewer should check that no screen
   drifts back toward 99 as the headline, which is what `G-04` is for.
4. **This unit read the registers; it did not re-run them.** Every figure is
   quoted from a row that already carried it. If a register row is wrong, this
   specification is wrong in the same place, and `RA-001` is already open against
   `PUR-003`–`PUR-005`.
