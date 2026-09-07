# Site review running list — reconciliation of the two committed versions

**Written:** 2026-09-07
**Subjects:** `MELAKEELASITEREVIEWRUNNINGLIST.md`, `MELAKEELASITEREVIEWRUNNINGLIST2.md`,
both committed unchanged to this directory
**Status of this document:** derived analysis of two `INHERITED-UNVERIFIED`
sources. It establishes the relationship between the two files. It does not
promote anything either file says.

---

## Verdict

**The later document is `MELAKEELASITEREVIEWRUNNINGLIST.md`.** It is Version 12.
`MELAKEELASITEREVIEWRUNNINGLIST2.md` is Version 10.

**The later supersedes the earlier. These are not parallel records.** Version 12
contains the whole of Version 10 — byte-identical for the first 899 of its 1349
lines — plus two new sections, two new change-log entries, and five revised
lines. Nothing in Version 10 is absent from Version 12 except the five passages
Version 12 rewrites, and those are revisions of the same passages, not
independent content that was dropped.

> **The filename numbering is inverted.** `...LIST2.md` is *earlier*, not later.
> A reader who takes the `2` as a version number will reverse the supersession
> and reinstate a workflow decision that Version 11 explicitly overturned. This
> is the single most consequential fact about the pair.

The evidence for direction is internal and unambiguous: each file carries a
`## Change log` whose final entry names its own version. Version 10's log ends
at "**2026-09-05 — Version 10**"; Version 12's log continues with Version 11 and
Version 12 entries that describe exactly the content Version 12 adds.

| | `...LIST2.md` | `...LIST.md` |
|---|---|---|
| Change-log terminus | **Version 10**, 2026-09-05 | **Version 12**, 2026-09-05 |
| Lines / bytes | 1116 / 116,947 | 1349 / 143,401 |
| Numbered sections | 1–22 | 1–24 |
| `LS-` items | LS-01 – LS-31 (31) | LS-01 – LS-51 (51) |
| `COR-` items | none | COR-01 – COR-18 (18) |
| `RV-` items | none | RV-01, RV-02 (2) |
| Research packets | R1 – R11 | R1 – R19 |
| Relationship | superseded | **current** |

---

## What differs

`diff` returns seven hunks. Five are single-passage rewrites inside the shared
region; two are pure additions at the end.

### 1. A reversal of the workflow's first step — five edited passages

This is the only place where Version 12 *changes* rather than *adds*, and every
one of the five edits serves the same reversal. Version 10 opens the programme
with a repository inventory; Version 12 opens it with an audit of the live
public site.

| Line | Version 10 | Version 12 |
|---|---|---|
| 900 | Companions: three files, **eleven** research prompts | Companions: four files, **nineteen** research prompts |
| 1022 | "**use separate Claude Chat research sessions for bounded packets**" | "**first ask Claude Chat to browse the public site**, then use separate research sessions" |
| 1024–1030 | Six workflow steps, beginning "**Claude Code inventory first**" | Seven workflow steps, beginning "**Claude Chat public-site audit first**"; repository reconciliation moves to step 6 |
| 1049/1050 | "Expand the companion prompt pack from eight to **eleven** packets" | "sections 23–24 extend the complete companion pack to **R1–R19**"; "Use the **live-site-first** sequence" |
| 1097/1098 | "Run the **Claude Code inventory** before research copy." | "Run the **public-site audit** before research… Run the Claude Code repository reconciliation **after** reviewed packets are consolidated provisionally and **before any build**." |

Version 12's own change log states the reversal directly: "*Version 11: Changed
the workflow to a Claude Chat live-public-site audit before research and a
Claude Code repository reconciliation before implementation.*"

The substantive consequence is that in Version 10 the repository is the primary
description of the site, while in Version 12 the live site is, and the
repository is checked against it later — Version 12 adds the reasoning that
"the repository may contain work the live crawler cannot see," which makes the
two inventories independent rather than redundant. Anything built on Version
10's step order is working from a superseded sequence.

### 2. Two whole sections added (lines 1103–1330, 228 lines)

- **§23 Indo-Iranian contact corridor, material routes and live-site-first
  planning** — subsections 23.1–23.6. Introduces the `COR-` series (COR-01 –
  COR-10) and LS-32 – LS-41.
- **§24 Final expansion: sound borrowing, divergent archives, language refugia
  and the Strait** — subsections 24.1–24.8. Adds COR-11 – COR-18, RV-01, RV-02
  and LS-42 – LS-51.

§24.1 is titled "Critical method made operational" and, per the Version 12 log,
"[m]ade decolonization, debrahminization, de-Indo-Europeanization and
nationalist-narrative auditing explicit evidence operations." That is the same
vocabulary as this repository's governing principle, and it is present **only**
in the later file.

### 3. Two change-log entries added (lines 1346–1349)

Versions 11 and 12, both dated 2026-09-05.

---

## What is identical

Lines 1–899 are byte-for-byte identical: the review principles, and sections 1
through 21.7 — information architecture, navigation, header, visitor flow,
visual depth, editorial economy, method and disclosure, argument quality, live
inconsistencies, genetics safeguards, the Artifact Atlas, the independent
assessment triage, the entry-page redesign, the children's dossier, the merged
project instructions, the 108-route checkpoint, the vision/execution synthesis,
the subaltern-history programme, and the language-science coverage backlog
through LS-31.

All 31 `LS-` rows shared by the two files are textually identical; verified by
diffing the extracted table rows. Version 12 renumbers no item and revises no
item it inherited.

---

## Bearing on D-014

Both files are relevant to `DECISIONS-NEEDED.md` D-014 and neither closes it.

1. **Neither document is the 89-item backlog.** The string `89` does not occur
   in either file, and neither contains a section answering to "MelaKeela.com v2
   — Master Research, Product & Institutional Backlog". This confirms from the
   documents themselves what the owner stated. `06-BACKLOG/BACKLOG-COVERAGE.csv`
   remains blocked, as do owner decisions D-008, D-009 and D-011.

2. **The prompt-pack is still absent, and it is larger than D-014 recorded.**
   Version 12 names five companion files, one more than D-014's table lists:

   | Named in Version 12 | In D-014's table? | In this repository? |
   |---|---|---|
   | `MELA-KEELA-CLAUDE-FULL-SEQUENCE.md` | yes | no |
   | `MELA-KEELA-LANGUAGE-RESEARCH-PROMPTS.md` | yes | no |
   | `MELA-KEELA-CLAUDE-LIVE-SITE-AUDIT-PROMPT.md` | yes | no |
   | `MELA-KEELA-CLAUDE-SAY-NEXT-RESEARCH-PROMPT.md` | **no** | no |
   | `MELA-KEELA-WHO-MADE-THE-PAST.md` | **no** | no |

   The last two should be added to D-014's request.

3. **D-014's body refers to the running list in the singular.** There are two,
   they are ten and twelve versions deep respectively, and only one is current.
   The entry has been amended accordingly.

---

## Consequences for use

- **Cite Version 12 (`MELAKEELASITEREVIEWRUNNINGLIST.md`) as the current
  running list.** Retain Version 10 as the superseded record — it is the only
  witness to the repository-inventory-first workflow that Version 11 overturned,
  and under the correction-history rule that reasoning stays visible so it is
  not re-proposed.
- **Do not treat the two as independent sources.** Version 12 is a lineal
  descendant of Version 10, not a second opinion on the same material. Two
  citations to "the running list" that trace to these two files count as one
  under the source-independence rule.
- **Neither file is evidence for any historical claim it contains.** Both are
  owner and model working documents. Their `LS-` and `COR-` rows are research
  *questions and coverage commitments*, not findings, and they enter
  `03-REGISTERS/inherited-claims.csv` at `INHERITED-UNVERIFIED` accordingly.
- **Version numbering in the filenames cannot be trusted.** Any future version
  should be committed under a name carrying its change-log version number.
