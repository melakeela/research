# Cross-reference: the ChatGPT handoff against the existing record

**Written:** 2026-09-07
**Subjects:** `03-REGISTERS/inherited-claims.csv` rows `CG-001`–`CG-284`
(from `01-INHERITED/chatgpt-project-handoff.md`) checked against rows
`IH-001`–`IH-369` (from `01-INHERITED/claude-project-handoff.md`),
`01-INHERITED/site-review/`, and `01-INHERITED/curatorial-audit-v1.1/`
**Status of this document:** derived analysis of `INHERITED-UNVERIFIED`
sources. It establishes relationships between documents. **It promotes
nothing.** Two handoffs agreeing is not a retrieval, and agreement between
models summarising their own prior conversations is not source independence
— it may be one conversation reaching a register twice.

---

## Why agreement here is weak evidence

Section 13 of the ChatGPT handoff (`CG-238`) lists among its downloaded
context five files that are *prompts written to Claude*:
`MELAKEELA-CLAUDE-CORRECTIVE-CONTROLLER-v2.md`,
`MELA-KEELA-CLAUDE-FULL-SEQUENCE.md`,
`MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md`,
`MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md` and
`MELA-KEELA-CLAUDE-SAY-NEXT-RESEARCH-PROMPT.md`.

The ChatGPT side held the instructions the Claude side was working under.
So where the two handoffs agree on **method**, the likeliest explanation is
a shared upstream instruction, not two independent confirmations — the
source-genealogy problem of `CLAUDE.md` method step 5 and the
source-independence constraint, arriving inside our own inheritance.

Where they agree on **an observed fact about the platform** — a count, a
page defect — the two records are closer to independent, because they were
looking at different snapshots. That is why the atlas-count agreement
(§A.1) carries more weight than the debrahminization agreement (§A.6),
and neither carries enough to promote anything.

---

## Summary

284 rows were registered as `CG-001`–`CG-284`. Of those, **145 carry a
note citing at least one `IH-` row**; **139 cite none**, because the Claude
handoff has nothing on the subject.

| | Count | Section |
|---|---|---|
| Direct duplicates — both handoffs record the same item | 9 | A |
| **Flagged disagreements — both registered, unresolved** | **6** | **B** |
| Divergence by list membership or omission | 4 | C |
| In-repo artifact families whose citations were checked | 2 (12 line citations, all resolving) | D |
| `CG` rows whose notes cite no `IH` row at all | 139 of 284 | E |
| Bearing on already-open owner decisions | 5 | F |

The headline: **the two handoffs overlap far less than expected.** Just
under half the ChatGPT handoff — the entire source-repair chronology, the
P1–P3 specification audit, the Research Batch 1 rejection, the ten corpus
registers, the fourteen rejected-reasoning items — has **no counterpart at
all** in the Claude handoff. They are not two accounts of one project
history. They are two largely disjoint halves of it, and the disagreements
below sit at the seam.

Nine duplicates against 284 rows is itself a finding: it means the
disagreements in §B are not noise in a broadly agreeing record. They are
most of the places where the two records touch at all.

---

## A. Direct duplicates

Both handoffs independently record the same item. Registered in both
places; neither promoted.

**A.1 — Atlas counts are irreconcilable.** `CG-175` and `IH-250` record the
same disagreement, with the same window figures (299 against 315) and
overlapping site figures. `IH-250` carries two terms `CG-175` lacks (167→175,
199 site-class rows). A third independent sighting sits in this repository:
`01-INHERITED/curatorial-audit-v1.1/page-audit.csv` gives the artifact-atlas
page title as *"Artifact Atlas: 175 Ancient South Asian Sites Mapped"*. This
is the strongest agreement in the pair, and it agrees that the number is
**unknown**.

**A.2 — Rakhigarhi-only framing.** `CG-189` and `IH-029` / `IH-155` /
`IH-110`: the sample is not one individual but twelve on an Indus-Periphery
cline. Two independent records of the same defect.

The related Irula item is **not** a clean duplicate. `CG-188` adds that the
Irula-proxy correction left residue in prose and SVGs and that the rejected
premise must not return through labels, captions or accessible names.
`IH-030`, `IH-081` and `IH-310` record the Irula question but no
propagation failure. **Queued as `RA-013`** — with the recheck blocked on
access to the current site build, which this repository does not hold.

**A.3 — "Iranian-related" is not "from Iran".** `CG-191` and `IH-109`,
in substance word for word.

**A.4 — Load-bearing comparative sources have never been read.**
`CG-155` and `IH-231`–`IH-248`: Mayrhofer, Kuiper 1991, Witzel,
Krishnamurti, DEDR. Both handoffs reach the same conclusion from different
records. `CG-155` adds Arnold, Oldenberg, Hellwig–Scarlata–Widmer,
Jamison–Brereton, Lubotsky, Rau, Southworth and Zvelebil, named in no
Claude-side ledger.

**A.5 — A written rule is not a gate.** `CG-164` (conditional schema and
build checks, with invalid examples proving rejection) and `IH-271`
(a `lint.py` so typed numbers must equal data).

**A.6 — Decolonization removes privileges, it does not install a
counter-narrative.** `CG-069` and `IH-361` ("strip the thumb from the
scale, not press the other pan"). Same rule, different metaphor. See the
independence caveat above.

**A.7 — A badge, a filename or a closing phrase is not a status.**
`CG-064`, `CG-074`, `CG-112`, `CG-185`, `CG-274` and `IH-167` / `IH-350`.

**A.8 — Cited-through-a-slide sources are held until read.** `CG-275`
and `IH-344`.

**A.9 — No partner is named before a written yes.** `CG-086` and
`IH-061` / `IH-216`.

---

## B. Flagged disagreements

**Both readings are registered. None is resolved here.** Where the item is
an owner's to settle, that is said.

### B.1 — What the project is called

| | |
|---|---|
| ChatGPT handoff | `CG-179`: *MelaKeela remains the working public museum name*; Veḷi as threshold / infrastructure is open; a fourth candidate, **Tuṟai**, is in play; no silent rename. |
| Claude handoff | `IH-062`: *"The name is Veḷi (Tamil veḷi), retroflex ḷ, romanised veli"* — recorded as an **adopted owner decision**. `IH-176`, `IH-177`, `IH-257`, `IH-258` then record the architecture as contested and held open under `HD-14`; `IH-276` makes it the owner's and **blocking**. |

The Claude handoff contradicts *itself* here — `IH-062` states the name as
settled while `IH-276` makes it an open blocking decision. The ChatGPT
reading is corroborated by
`01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md` L556, which
records exactly this contradiction ("Part A says the relationship among
Mela Keela, Veḷi and Tuṟai is unresolved; Part F declares the name is
Veḷi") and states current owner direction as Mela Keela the museum, Veḷi
its threshold.

**Disposition:** owner's. Already open as `D-004` in
`09-DECISIONS/OWNER-DECISIONS.csv`. `Tuṟai` was not previously on the
repository's list of candidates.

### B.2 — Daylight or near-black

| | |
|---|---|
| ChatGPT handoff | `CG-046`, `CG-180`, `CG-218`, `CG-219`, `CG-220`: a **genuine live conflict**. The earlier doctrine (`D04`) specifies pearly daylight, open horizons, warm off-white, dawn blue, clay, sage, ink, restrained gold, and *explicitly forbids applying the near-black system uniformly*. The later public-copy standard (`D09`) reinstates near-black with an epistemic justification — darkness as the unknown field around the evidence. Hierarchy **OPEN**. |
| Claude handoff | `IH-065`: dark ground, velippaṭu, colour encodes argument, grey `#5f6f7a` means NO DATA — recorded as **settled owner decision**. `IH-066`: the owner's *"I like the darkness."* |

Both are owner-direction claims and they cannot both be operative. `CG-213`
offers the only route out that is not a reversal: environments may be
per-exhibit rather than universal. `CG-220` adds the necessary caution —
the owner rejected *poor execution* (`CG-081`), which is not a rejection of
every underlying principle, and must not be used to erase prior assets.

**Disposition:** owner's, and **not currently on the decisions register**.
Raised as `D-044` by this pass.

### B.3 — What "58" was

| | |
|---|---|
| ChatGPT handoff | `CG-039`: 58 was a **working subset mistaken for the whole platform** — an error, corrected by a 108-route report, itself overtaken by a 133-route integration (`CG-040`). Absence claims built on the subset were withdrawn (`CG-041`). |
| Claude handoff | `IH-007`, `IH-185`, `IH-251`: 58 is the platform's **true size on 30 August**, the first term of a growth series 58 → 69 → 75 → 85 → 102 → 127 → ~135. |

The two series share only the number 58 and disagree about what it denotes.
96, 105, 108, 133 and 139 appear in no `IH` row; 69, 102 and 127 appear in
no `CG` row. Corroboration for the ChatGPT reading sits at
`MELAKEELASITEREVIEWRUNNINGLIST.md` L558 and L642.

**Neither handoff certifies a current total, and neither does this pass.**
`CG-043` supplies the diagnosis both records needed: pages, HTML files,
content routes and redirects are four different units and were being
compared as one. Bears on open decision `D-034`.

### B.4 — Where Para-Munda sits

| | |
|---|---|
| ChatGPT handoff | `CG-120`: Para-Munda is **outside the active explanatory framework** for insufficient positive diagnostic evidence — and explicitly *not* because modern Munda genetics disproves every extinct northwest Austroasiatic-related language. |
| Claude handoff | `IH-033`, `IH-036`, `IH-343`: Para-Munda earns **a brief historical note with its evidential burden stated**, inside the record, and is not dismissed on its proponent's identity (`IH-035`, `IH-157`). |

The guard clauses agree exactly; `CG-120` reproduces
`00-CONTROLLER/METHODOLOGY-CONSTITUTION.md` L240 almost verbatim. The
placement differs: outside the framework, or inside it as a stated minority.
This is an attestation-gradient question (`CLAUDE.md`, Constitution §4E) and
is answerable by evidence rather than by preference — but not by this pass.

### B.5 — Whether "the late books" is a legitimate phrase

`CG-117` rejects the reasoning that Maṇḍalas 1, 8, 9 and 10 are one
uniformly demonstrably late layer, and states that **maṇḍala number is not
a time axis**.

`IH-016` records the corrected river finding in exactly those terms: Kubhā
2, Krumu 2, Gomatī 2, Suvāstu 1, "every occurrence in Books 5, 8 or 10,
**the late books**". `IH-336` then derives standing rule 1 — metrical
stratum and book order are two instruments, neither carries a directional
claim alone.

So the Claude handoff's *correction* to an overreach reproduces the move
`CG-117` forbids, inside the replacement text. The correction is not
thereby wrong; the phrase carrying it is doing work the phrase cannot do.

**Queued as `RA-012` in `04-AUDITS/REAUDIT-QUEUE.csv`.**

### B.6 — Whether DMC eligibility is settled

| | |
|---|---|
| ChatGPT handoff | `CG-248`: DMC and CMF are dated 4 September research notes; programme rules must be retrieved and reverified; **no current deadline or eligibility conclusion is certified.** |
| Claude handoff | `IH-059`, `IH-133`: DMC requires one year of legal existence at submission, so a September 2026 incorporation is ineligible for December 2026; plan revised to **December 2027** (`IH-184`, `IH-262`, `IH-328`). |

Divergence by omission rather than flat contradiction. The safer reading is
the ChatGPT one, and the Claude handoff itself supplies the reason:
`IH-246` records that the DMC **2027** guidelines were never accessed and
that the 2026 guidelines were reached via web search only, and `IH-313`
lists their verification as owed. A specific, actionable, load-bearing
funding claim rests on an unretrieved source.

---

## C. Divergence by list membership

Not contradictions — lists that should match and do not.

**C.1 — Living Worlds.** `CG-195` names Water, Food, Word/Language first,
then City, Body, Mind, Movement, Nature, Work, Power, Play, Belief.
`IH-211` names twelve: Water, Food, Mind, Body, **Home**, Movement, Nature,
Work, Belief, Language, Power, Play — adopted "from the ChatGPT comparison
as the single strongest idea in either document". `CG-195` has **City** and
lacks **Home**. A third list at `MELAKEELASITEREVIEWRUNNINGLIST.md` L811
gives Food, Water, Body, Mind, Work, Language, Power, Movement, Nature and
"the other Living Worlds" — matching neither exactly. Bears on `D-005`.

**C.2 — Engines.** `CG-183` records four / six / nine; `IH-010` records six
(T4), `IH-210` nine (VELI-12). "Four" appears only in the ChatGPT record.
`CG-072` adds the warning both records needed: ten *visitor functions* are
not ten *engines*.

**C.3 — The children's programme's standing.** `CG-087` records it as
**proposed, not adopted**, corroborated by the running list's own section
heading (L393) and the ages 8–11 scope at L404. `IH-210` and `IH-212`
describe the same product (VELI-10, DIG) without recording that it is
unadopted; `IH-267` records only a scope conflict. The unadopted status is
carried by one handoff and not the other.

**C.4 — The backlog.** `CG-063` records **89 backlog IDs and 41 vision
items, 23 NOT FOUND**. The Claude-side backlog is VELI-03 items 1–11
(`IH-195`). These are not the same object. Bears on `D-014`.

---

## D. Corroborated against in-repo inherited artifacts

The ChatGPT handoff cites two artifact families this repository holds. Its
citations were checked. **They check out** — which establishes that the
handoff quoted its sources accurately, and establishes nothing about
whether those sources are right.

**D.1 — The curatorial audit.** `CG-034` gives 96 HTML pages, 46 keep, 20
revise, 15 hold, 11 split, 4 merge, and risk 52 low / 23 medium / 6 high /
15 critical. Every figure is reproduced by
`01-INHERITED/curatorial-audit-v1.1/summary.csv` and by `page-audit.csv`
tallied by column (96 rows; Risk: Low 52, Medium 23, High 6, Critical 15;
Decision: Keep 46, Revise 20, Hold 15, Split 11, Merge 4; MVP Yes 15). The
15-page MVP of `CG-037` and `CG-182` is the same 15. The audit's own
`method-limits.csv` calls itself editorial and source-risk triage, *not*
completed peer review — so the corroboration is of transcription, not truth.

**D.2 — The running list.** Eleven citations resolve correctly against
`MELAKEELASITEREVIEWRUNNINGLIST.md`:

| Handoff row | Claim | Line |
|---|---|---|
| `CG-045` | one compact header; no Method row, no duplicate search | L45, L47 |
| `CG-087` | children's dossier proposed, not adopted; ages 8–11 | L393, L404 |
| `CG-179` | the Mela Keela / Veḷi / Tuṟai brand contradiction | L556 |
| `CG-039`, `CG-040` | 58-file subset error; 108-route report; 133 integration | L558, L642 |
| `CG-144` | Who Made the Past? as §20, recorded 5 September | L803, L811 |
| `CG-197` | Who Mapped Speech? as its own programme | L894, L904 |
| `CG-201` | the Strait / corridor-power programme | L1182 |

`CG-223` states the handoff read "sections 15–24". Version 12 of the
running list has sections 1–24; Version 10 stops at 22
(`01-INHERITED/site-review/RUNNING-LIST-RECONCILIATION.md`). **The handoff
read the current version.**

---

## E. No counterpart in `IH-001`–`IH-369`

Roughly half the ChatGPT handoff is new to this repository. The
load-bearing blocks:

- **The six-stage source-repair chronology** (`CG-101`–`CG-108`), including
  the 0/23 exhaustive searches and 0/23 comparative dossiers of `CG-105`,
  the corrected daṇḍa locator RV 7.33.6 (`CG-103`), the mayūra citation at
  RV 3.45.1 inside an audit asserting absence (`CG-102`), and the
  Talageri over-extension (`CG-103`). Sole source is `D12`, which this
  repository does not hold (`CG-234`).
- **The fourteen rejected-reasoning items** (`CG-115`–`CG-128`).
- **The P1–P3 specification audit**, all of §9 (`CG-158`–`CG-173`).
- **Research Batch 1's rejection and the ten required corpus registers**
  (`CG-130`–`CG-142`), with the eight-field search-log requirement of
  `CG-141`.
- **The eight-way absence typology** (`CG-071`) — already live here as
  `CLAUDE.md`'s negative-evidence standard, but absent from the Claude
  handoff, whose nearest equivalents are `IH-342` and `IH-005`.
- **Proto-Dravidian `*ẓ`** and the five-way reconstruction/phone/phoneme/
  branch-outcome/script-accommodation distinction (`CG-097`).
- **The logo decision chronology** (`CG-049`–`CG-058`), including the
  selected "top right" concept with only the vertical line black. The
  Claude register records no logo selection at all.
- **Four audience variants for the deck** (`CG-079`) and the rejection of
  its visual execution (`CG-081`).
- **Two audit items with no Claude-side equivalent:** Y-chromosome versus
  autosomal conflation (`CG-190`) and infrastructure-injected analytics
  versus package-originated requests (`CG-192`).
- **Six rejected route shortcuts** (`CG-204`–`CG-209`): Mehrgarh/Marhaši,
  the Meluhha/Marhaši/Magan/Dilmun conflation, blue-object-equals-lapis,
  earliest-recovered-equals-first-contact, ships-at-Agade-equals-seized,
  and trade-always-precedes-war.

---

## F. Bearing on already-open owner decisions

| Decision | New material |
|---|---|
| `D-004` — what Veḷi principally is | `CG-179` adds **Tuṟai** as a fourth candidate and the running-list corroboration at L556. See §B.1. |
| `D-005` — is WATER the first Living World | `CG-195` gives a third world-list, with City and without Home. See §C.1. |
| `D-013` — `dependency.csv` or `SOURCE-DEPENDENCY.json` | `CG-267` names `SOURCE-DEPENDENCY.json` in the minimal record set, which is where the alternative name came from. |
| `D-014` — commit the 89-item v2 backlog | `CG-063` is a second, independent record of the 89 IDs, plus 41 vision items and 23 `NOT FOUND`. See §C.4. |
| `D-034` — authoritative page and atlas counts | `CG-174` adds 96, 105, 108, 133 and 139 to the page series and `CG-043` supplies the unit-conflation diagnosis. See §B.3 and §A.1. |

**Raised by this pass:** `D-044`, the daylight/near-black hierarchy (§B.2).

---

## G. Two objections this register cannot answer about itself

`CG-109` and `CG-167` object to composite status labels and to mixing all
statuses into one field: *"Even 'VERIFIED' is incomplete as a composite
label, because locator, Saṃhitā, Padapāṭha, morphology and exhaustive
search need separate fields."*

`03-REGISTERS/inherited-claims.csv` has exactly one `status` column, as
`CLAUDE.md`'s register format requires. The objection lands. It is recorded
and not acted on, because the register format is controller-level.

`CG-168` objects to arbitrary string references that accept nonexistent
IDs. Every one of the 284 rows appended by this pass carries an **empty
`source_id`** — correctly, since no retrieval backs any of them, and
`CLAUDE.md` requires `source_id` to resolve to a row in
`02-SOURCES/access-ledger.csv`. The register format has no way to say
"deliberately empty pending retrieval" as distinct from "not filled in".

---

## H. What this pass did not do

- **No promotion.** All 653 register rows are `INHERITED-UNVERIFIED`. No
  retrieval was performed and no row was added to
  `02-SOURCES/access-ledger.csv`.
- **No resolution.** Every disagreement in §B is registered from both
  sides and left standing.
- **No renaming.** The handoff's `D01`–`D15` artifact labels are kept as
  written and flagged at `CG-222` as a namespace distinct from
  `09-DECISIONS`, per its own instruction at `CG-268`.
- **No external retrieval.** No domain was requested and none was blocked.

What it *did* add, beyond the 284 register rows and this document:

- `RA-012` and `RA-013` in `04-AUDITS/REAUDIT-QUEUE.csv` — the two places
  where an inherited method item touches earlier registered work (§B.5,
  §A.2). Neither retracts anything; both name what to recheck.
- `D-044` in `09-DECISIONS/OWNER-DECISIONS.csv` — the daylight/near-black
  hierarchy (§B.2), the one disagreement in §B that was not already on the
  decisions register. It blocks nothing here, so it gets a CSV row and no
  prose section in `DECISIONS-NEEDED.md`.
- No `HD-` or `D-` identifier was allocated to any owner decision *asserted
  inside* the ChatGPT handoff. Those stay `INHERITED-UNVERIFIED` register
  rows, on the same footing as the Claude handoff's `HD-01`–`HD-20`. A
  register row is not a promotion, and only retrieval promotes.
