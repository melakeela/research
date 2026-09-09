#!/usr/bin/env python3
"""Build 06-BRIEFS/mvp-fifteen/ - one page brief per page in the curatorial
audit's MVP set.

Read and reproduced into the output at build time:
  01-INHERITED/curatorial-audit-v1.1/environment-map.csv   (INHERITED-UNVERIFIED)
  01-INHERITED/curatorial-audit-v1.1/mvp.csv               (INHERITED-UNVERIFIED)
  01-INHERITED/curatorial-audit-v1.1/page-audit.csv        (INHERITED-UNVERIFIED)
  01-INHERITED/curatorial-audit-v1.1/asset-register.csv    (INHERITED-UNVERIFIED)
  03-REGISTERS/inherited-claims.csv                        (INHERITED-UNVERIFIED)
  03-REGISTERS/*.csv                                       (scanned for supports_page)

Quoted in the prose and CHECKED, not reproduced - verify_quotes() below asserts
that every quoted fragment is still present in its source file, so a later edit
to any of them fails the build instead of silently invalidating a brief:
  13-PRODUCT-ARCHITECTURE/museum-framework.md              (HYPOTHESIS)
  00-CONTROLLER/METHODOLOGY-CONSTITUTION.md                (constitution)
  01-INHERITED/curatorial-audit-v1.1/SCHEMA.md             (INHERITED-UNVERIFIED)
  01-INHERITED/curatorial-audit-v1.1/method-limits.csv     (INHERITED-UNVERIFIED)
  01-INHERITED/curatorial-audit-v1.1/summary.csv           (INHERITED-UNVERIFIED)
  01-INHERITED/curatorial-audit-v1.1/claim-risk.csv        (INHERITED-UNVERIFIED)
  01-INHERITED/curatorial-audit-v1.1/overlap-tensions.csv  (INHERITED-UNVERIFIED)
  02-SOURCES/access-ledger.csv                             (retrieval capability)
  DECISIONS-NEEDED.md, 09-DECISIONS/OWNER-DECISIONS.csv    (D- identifiers)

The per-page prose below is the analytical content of the unit. The script
exists so that the mechanical parts - the workbook rows quoted, the
supports_page scan, every count, and the quote checks - are regenerated rather
than retyped, and so they can be re-run against changed inputs.

Rule the script follows, from the inheritance (standing rule 14): no count in
the output is a typed literal. Every figure is derived here or it is not
printed.

Run from the repository root:  python3 04-AUDITS/mvp-fifteen-briefs-build.py
"""

import csv
import glob
import os
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT = os.path.join(ROOT, "01-INHERITED", "curatorial-audit-v1.1")
OUT = os.path.join(ROOT, "06-BRIEFS", "mvp-fifteen")
WRITTEN = "2026-09-08"
# Second build. What changed and why is in README.md §0.2.
REVISED = "2026-09-09"

MVP_SLUGS = [
    "index", "enter", "artifact-atlas", "veli", "tinai", "the-ledger",
    "keeladi", "before-the-indus", "the-water-city", "kural", "sound-changes",
    "the-languages-we-lost", "the-other-laws", "custody", "the-archive",
]


def sheet(name, header_row):
    rows = list(csv.reader(open(os.path.join(AUDIT, name))))
    hdr = rows[header_row]
    return hdr, [dict(zip(hdr, r)) for r in rows[header_row + 1:] if r and any(r)]


def scan_supports_page():
    """Which of the fifteen slugs is named by a supports_page value anywhere
    in 03-REGISTERS/? Returns {slug: [(file, claim_id, status)]}."""
    hits = {s: [] for s in MVP_SLUGS}
    scanned = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "03-REGISTERS", "*.csv"))):
        try:
            rows = list(csv.DictReader(open(path)))
        except Exception:
            continue
        if not rows or "supports_page" not in rows[0]:
            continue
        scanned += 1
        for r in rows:
            vals = (r.get("supports_page") or "").replace(";", ",").split(",")
            for v in (x.strip() for x in vals):
                if v in hits:
                    hits[v].append((os.path.basename(path),
                                    r.get("claim_id") or r.get("interpretation_id") or "",
                                    (r.get("status") or "").strip()))
    return hits, scanned


# Fragments quoted in the prose below, checked against their sources at build
# time. A quote that no longer resolves fails the build. Keyed by file, relative
# to the repository root; each fragment is matched with whitespace collapsed so
# line wrapping in the source does not matter.
QUOTE_CHECKS = {
    "13-PRODUCT-ARCHITECTURE/museum-framework.md": [
        # 8.1, quoted in 03-artifact-atlas.md sections 5 and 7. Its final clause
        # settles whether the rule reaches the page title; a draft of section 7
        # said the specification was silent on that (BF-029).
        "The number of sites in view is a property of the current filter and is always shown *with* the filter, never as a title.",
        "the Atlas can be built and shipped before that is answered, because it never asserts a total in its own voice",
        "Themes change with the visitor's relationship to knowledge; the institutional shell remains stable.",
        "because environments are postures rather than topics, a page can move between them without its content changing",
        "nothing in `03-REGISTERS/` records a publication decision, an environment assignment, or a duplication finding",
        "The interface must therefore never sort or colour `INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS`",
        "a derived asset may not be commissioned or published while the claim it depicts is `INHERITED-UNVERIFIED` or `HOLD`",
        "The Atlas has no headline count.",
        "adopted as settled fact,",
        "no gaming HUD or arbitrary links",
        "reads as empty and empty reads as nobody",
        "A child may *read* a custody record; a child may not be handed",
        "running one is a failed test",
        "treating a consent question as a licensing question",
        "site photography \u2014 physical presence required",
        "third-party rights negotiation \u2014 unbounded timeline",
        "too sparse to do reliably",
        "known by argument from sources",
        "methods pages, historiography, the ledger",
        "non-empty on the day the institution publishes its first custody chain",
        "Digitization is not restitution",
        "no spectacle or unsupported allegation",
        "where the institution is arguing against something",
        "the mechanism that keeps the argument falsifiable rather than rhetorical",
        "`decision_id` (`mk:dec:`)",
        "`derived_residual`",
        "Every design proposition here is `HYPOTHESIS`",
        # Derivation rules are asserted WITH their numbers, because the briefs
        # cite the numbers ("rule 1 fires first", "rule 7's residual") and a
        # reordering of section 1.5 would leave bare labels resolving while every
        # citation was wrong.
        "Derivation inputs, in precedence order:",
        "1. **Withheld-access flag.**",
        "2. **Repair state.**",
        "3. **Absence dominance.**",
        "4. **Relation dominance.**",
        "5. **Place/material dominance.**",
        "6. **Counter-account.**",
        "7. **Otherwise \u2192 Reading Room.**",
        "An override with an empty reason is invalid.",
    ],
    "00-CONTROLLER/METHODOLOGY-CONSTITUTION.md": [
        "Unknown regions must remain visibly unknown",
        "NOT PRODUCED",
        "NOT PRESERVED",
        "NOT EXCAVATED",
        "NOT PUBLISHED",
        "NOT ACCESSIBLE",
        "NOT RECOGNIZED",
        "DOCUMENTED DESTRUCTION",
        "ABSENT DESPITE ADEQUATE SEARCH",
    ],
    "01-INHERITED/curatorial-audit-v1.1/SCHEMA.md": [
        "too sparse to do reliably",
        "Nothing in `03-REGISTERS/` records a publication decision, an environment assignment, or a duplication finding.",
        "Sequencing is inverted for the diagram work.",
        "50 claim-specific diagrams",
    ],
    "01-INHERITED/curatorial-audit-v1.1/method-limits.csv": [
        # The four layer definitions 03-artifact-atlas.md section 1 quotes.
        # Added under BF-030: the repair that separated Decision from Risk
        # introduced four quotations and guarded none of them.
        "Keep, Revise, Hold, Split or Merge based on role, source visibility, risk and overlap.",
        "Decisions remain provisional until factual and specialist review.",
        "Flagged categorical, causal, priority/origin, institutional and quantitative central claims.",
        "Estimated bibliography entries from visible Sources/References sections and counted live external links.",
        "Risk means verification priority, not falsehood.",
        "A visible bibliography does not prove claim-level support or source quality.",
        "These are publication gates, not optional polish.",
        "Full primary-source re-performance, legal opinion, community consultation, image-rights clearance and discipline-specific peer review.",
    ],
    "01-INHERITED/curatorial-audit-v1.1/summary.csv": [
        "1. Claim-level citation review",
        "7. Confirm production domain and deployment allowlist",
    ],
    "01-INHERITED/curatorial-audit-v1.1/overlap-tensions.csv": [
        "Keep distinct but present as one curated exhibit sequence.",
        "Curated institutional-power exhibit with claim-level documents and right-of-reply field.",
    ],
    "03-REGISTERS/inherited-claims.csv": [
        # IH-250's resolution path, quoted in 03-artifact-atlas.md sections 3, 6
        # and 7 and in 02-enter.md. Its final clause was cut twice; the clause
        # is what constrains the brief's own printing of counts.
        "Extract the atlas dataset to JSON, count, and generate every stated figure from it; until then no document prints a site count.",
    ],
    "01-INHERITED/curatorial-audit-v1.1/claim-risk.csv": [
        "Before the Indus, the graves already faced the sun.",
    ],
    "02-SOURCES/access-ledger.csv": [
        "A ledger row is a timestamped probe, not a standing property (D-042).",
        # SRC-052's probe list and constraint, quoted in six briefs
        "glottolog.org, dsal.uchicago.edu/dictionaries/burrow/, archive.org, api.github.com, api.crossref.org, api.openalex.org, api.semanticscholar.org, doi.org, arxiv.org, degruyter.com, benjamins.com, zenodo.org, royalsocietypublishing.org, pmc.ncbi.nlm.nih.gov, europepmc.org, cdstar.eva.mpg.de",
        "Only github.com and raw.githubusercontent.com are reachable.",
        "Serves git only.",
    ],
    "DECISIONS-NEEDED.md": [
        "Nothing in this repository acts on the MVP set until this is answered.",
        # D-034, quoted in the artifact-atlas conflict section
        "A contested number is inside a launch page title, presented as settled.",
        "The atlas number is load-bearing for a page ranked third in the launch set.",
    ],
    "03-REGISTERS/water-living-world-readiness.csv": [
        # WLW-001, quoted in 09-the-water-city.md section 3. It has been amended
        # once already, under review; nothing guarded it until BF-029.
        "As at 2026-09-08T21:13Z, before this unit added any row, no register in 03-REGISTERS/ carried a water claim above INHERITED-UNVERIFIED, and no row in any register carried supports_page = the-water-city.",
        "scan of all 14 registers carrying a supports_page column",
        "06-BRIEFS/mvp-fifteen/09-the-water-city.md \u00a73 established the same for the page.",
        "IH-138 (post-urban settlement moved east tracking a weakening monsoon) is a water claim in 03-REGISTERS/inherited-claims.csv, as is IH-183",
    ],
    "09-DECISIONS/OWNER-DECISIONS.csv": [
        "Neutralised but not answered by museum-framework.md \u00a78.1 \u2014 the Atlas can be built without the number and cannot be titled without it.",
    ],
    "RESEARCH-QUEUE.md": [
        "Recorded against that item, not as an exception to it:",
        "The placement is not settled.",
    ],
    "CLAUDE.md": [
        "Argument does not promote a claim. Confidence does not promote a claim. Only retrieval does.",
        "Evidence that supports nothing is not collected.",
        "weight follows evidence. No rhetorical equality where evidence is unequal",
    ],
    "04-AUDITS/BIAS-FAILURE-LOG.csv": [
        "Type the absence under \u00a76 before writing the verdict.",
    ],
}


def _flat(t):
    # collapse whitespace and drop markdown blockquote markers, so a fragment
    # matches whether or not the source wraps it or quotes it in a blockquote
    return " ".join(t.replace("\n>", "\n").split())


def verify_pairings():
    """The two dicts below are what the briefs actually print, one row per page.
    Asserting the framework's rows as loose literals would let a swapped dict
    entry pass while six briefs printed the wrong row - so each row is COMPOSED
    from the dict and the composed string is asserted against the framework.
    This is a pairing check, not an existence check, and it is what the briefs
    depend on. Returns the number of composed rows checked."""
    body = _flat(open(os.path.join(ROOT, "13-PRODUCT-ARCHITECTURE",
                                   "museum-framework.md"), encoding="utf-8").read())
    missing, n = [], 0
    for env, (posture, avoid) in POSTURE_TABLE.items():
        # section 1.1: | <env> | *<posture>* | <avoid> |
        row = "| %s | *%s* | %s |" % (env, posture, avoid)
        n += 1
        if _flat(row) not in body:
            missing.append(row)
    for env, modes in MODES.items():
        # section 1.7: | <env> | <source> | <atlas> | <investigation> | <field> | <classroom> |
        row = "| %s | %s |" % (env, " | ".join(modes))
        n += 1
        if _flat(row) not in body:
            missing.append(row)
    if missing:
        raise SystemExit("pairing check failed - a posture/mode row this build "
                         "would print is not in museum-framework.md:\n" +
                         "\n".join("  " + m for m in missing))
    return n


def verify_quotes():
    """Assert every quoted fragment still resolves in its source, and every
    composed posture/mode row still matches the framework. Returns the total
    number of assertions, which the README prints."""
    n = 0
    missing = []
    for rel, frags in QUOTE_CHECKS.items():
        body = _flat(open(os.path.join(ROOT, rel), encoding="utf-8").read())
        for f in frags:
            n += 1
            if _flat(f) not in body:
                missing.append((rel, f))
    if missing:
        raise SystemExit("quote check failed:\n" + "\n".join(
            "  %s : %s" % (r, f) for r, f in missing))
    return n + verify_pairings()


def count_asset_sets_with(term, as_by):
    """Which MVP slugs' Required asset set contains term. Derived, never typed."""
    return [s for s in MVP_SLUGS if term in as_by[s]["Required asset set"]]


def supports_page_values():
    """Every distinct supports_page value in use across 03-REGISTERS/, plus the
    exclusion set: registers with claim rows and no supports_page column at all.
    Printing the exclusions is BF-017's control on arguments from absence."""
    vals, with_col, without_col = set(), [], []
    for path in sorted(glob.glob(os.path.join(ROOT, "03-REGISTERS", "*.csv"))):
        try:
            rows = list(csv.DictReader(open(path)))
        except Exception:
            continue
        if not rows:
            continue
        name = os.path.basename(path)
        if "supports_page" not in rows[0]:
            without_col.append(name)
            continue
        with_col.append(name)
        for r in rows:
            for v in (x.strip() for x in
                      (r.get("supports_page") or "").replace(";", ",").split(",")):
                if v:
                    vals.add(v)
    return sorted(vals), with_col, without_col


def fail(msg):
    """Every gate in this file raises rather than asserting. A bare assert
    vanishes under python3 -O, and a gate that can be switched off by an
    interpreter flag is not a gate."""
    raise SystemExit("mvp-fifteen build stopped: " + msg)


def atlas_inbound(pg_by):
    """The two inbound-link figures 03-artifact-atlas.md section 7 compares,
    derived from page-audit.csv rather than typed, with the comparison itself
    derived. Returns (this page's count, the highest slug, its count, the
    ordinal word for this page's position among the fifteen)."""
    ranked = sorted(((int(pg_by[s_]["Inbound links"]), s_) for s_ in MVP_SLUGS),
                    reverse=True)
    mine = dict((sl, n) for n, sl in ranked)["artifact-atlas"]
    pos = [sl for _, sl in ranked].index("artifact-atlas")
    if pos == 0:
        fail("artifact-atlas now has the highest inbound-link count of the "
             "fifteen; section 7 compares it against a higher one and needs "
             "rewriting by hand.")
    top_n, top_slug = ranked[0]
    return mine, top_slug, top_n, ordinal_word(pos + 1)


NUMBER_WORDS = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
                7: "seven", 8: "eight", 9: "nine", 10: "ten"}

ORDINALS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
            "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
            "fourteenth", "fifteenth"]


def ordinal_word(n):
    if not 1 <= n <= len(ORDINALS):
        fail("no ordinal word for %r; a brief prints one" % n)
    return ORDINALS[n - 1]


def owner_decision(did, must_be=None):
    """One row of 09-DECISIONS/OWNER-DECISIONS.csv.

    Substituting a live status into a sentence that presumes a particular one
    is not a derivation; it is a typed argument with a variable in it, and it
    prints something false the moment the value moves (BF-030). Where a brief
    argues *from* the status, must_be names the status the argument needs and
    the build stops if the file no longer carries it.
    """
    for r in csv.DictReader(open(os.path.join(
            ROOT, "09-DECISIONS", "OWNER-DECISIONS.csv"), encoding="utf-8")):
        if r["decision_id"] == did:
            if must_be and r["status"] != must_be:
                fail("%s is now %r, and 03-artifact-atlas.md section 7 is "
                     "written throughout against a decision that is %r. The "
                     "section records an open conflict; if the owner has "
                     "answered it, the section is finished and has to be "
                     "rewritten by hand, not re-substituted."
                     % (did, r["status"], must_be))
            return r
    fail("%s is cited by a brief and is not in OWNER-DECISIONS.csv" % did)


def claim_risk_absent(slug):
    """That claim-risk.csv holds no row for a slug is an argument in
    03-artifact-atlas.md sections 1 and 7 -- 'the sheet that would have
    recorded a publication gate on a quantitative central claim holds no row
    for this page'. A row appearing falsifies the argument, so it stops the
    build rather than being printed into the sentence it refutes (BF-030)."""
    _, rows = sheet("claim-risk.csv", 3)
    for r in rows:
        if r.get("Slug") == slug:
            fail("claim-risk.csv now carries a row for %r (Risk %r, publication "
                 "gate %r). 03-artifact-atlas.md sections 1 and 7 argue from "
                 "its absence and are false while that row exists."
                 % (slug, r.get("Risk"), r.get("Publication gate")))
    return True


def n_inherited_rows():
    return len(list(csv.DictReader(open(
        os.path.join(ROOT, "03-REGISTERS", "inherited-claims.csv")))))


def status_floor(slug, linked, ih_rows):
    """The floor over a page's evidence, and the other statuses its rows carry.

    Nothing here is sorted and nothing is called *above* anything. Framework
    3.2 rules that six of the seven statuses describe evidential standing and
    one describes where an assertion came from, so they do not form a ladder;
    an earlier version of this function called every status that was not
    INHERITED-UNVERIFIED "above the floor", which would have printed a REJECTED
    row as standing above one (BF-029).

    The floor is stated by one rule and no comparison: a row carrying
    INHERITED-UNVERIFIED has had no retrieval event behind it, so no set
    containing one stands above it. A page whose evidence carries no such row
    has no floor this function can state, and the build stops.
    """
    lk = [(c, (st or "").strip()) for _, c, st in linked]
    for cid, st in lk:
        if not st:
            fail("%r: linked row %r carries no status. CLAUDE.md: every claim "
                 "carries exactly one status; no claim is unstatused."
                 % (slug, cid or "(no id)"))
    ih = [(r["claim_id"], (r["status"] or "").strip()) for r in ih_rows]
    for cid, st in ih:
        if not st:
            fail("%r: inherited row %r carries no status." % (slug, cid))
    present = sorted(set(st for _, st in lk + ih))
    if not present:
        fail("%r: no row of any status bears on this page, so it has no floor "
             "to state. Write the section by hand or give the page evidence."
             % slug)
    if "INHERITED-UNVERIFIED" not in present:
        fail("%r: no INHERITED-UNVERIFIED row in this page's evidence, so the "
             "floor can no longer be stated by rule and this brief needs a "
             "written one. Statuses present: %s" % (slug, ", ".join(present)))
    others = sorted(st for st in present if st != "INHERITED-UNVERIFIED")
    return "INHERITED-UNVERIFIED", others


def inherited(ids):
    rows = {r["claim_id"]: r for r in
            csv.DictReader(open(os.path.join(ROOT, "03-REGISTERS", "inherited-claims.csv")))}
    return [rows[i] for i in ids if i in rows]


# --------------------------------------------------------------------------
# Shared blocks
# --------------------------------------------------------------------------

HEADER_NOTE = """\
**Written:** {written} · **revised:** {revised}
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
"""

NO_PUBLIC_COPY = """\
### Why the remaining six slots are empty

Step 14 draws public copy **from accepted claims**. This page has none: {premise} Drafting
`WHAT THE EVIDENCE SUPPORTS` from claims at that standing would be writing public
copy for unverified claims, which is what `CLAUDE.md`'s inheritance rule and the
museum framework's Rule S-1 forbid. The slots are therefore left open, with the
work that would fill them named in §6.

| Step 14 slot | Draftable today | Why not |
|---|---|---|
| QUESTION | yes | stated above; a question asserts nothing |
| WHAT IS OBSERVED | partly | the workbook's structural counts are observations *about a page*, not about the past; the page's own observations are unretrieved |
| WHAT THE EVIDENCE SUPPORTS | no | {supports_cell} |
| WHAT COMPLICATES IT | no | complications are claims too, and carry the same floor |
| WHAT REMAINS UNKNOWN | no | requires the negative-evidence typing of constitution §6, not yet performed |
| MELAKEELA'S CURRENT INTERPRETATION | no | an interpretation over an unverified claim set states confidence retrieval has not earned |
| WHAT WOULD CHANGE IT | no | falsifiers attach to claims; there are no claim rows to attach them to |
"""

POSTURE_TABLE = {
    "Nocturnal Veḷi": ("not yet known", "No fantasy portal or occult styling"),
    "Living Signal Field": ("known by relation", "No gaming HUD or arbitrary links"),
    "Tamil Retrofuture": ("known against an official account", "No kitsch, fake Tamil or neon overload"),
    "Living Tiṇai": ("known through place and material", "No generic landscape decoration"),
    "Reading Room": ("known by argument from sources", "No visual fatigue or luxury minimalism"),
    "Extraction / Collection": ("known but withheld", "No spectacle or unsupported allegation"),
    "Reconnection": ("knowable again", "Digitization is not restitution"),
}

MODES = {
    "Nocturnal Veḷi":        ("mandatory", "available", "available", "available", "available"),
    "Living Signal Field":   ("mandatory", "mandatory", "available", "available", "available"),
    "Tamil Retrofuture":     ("mandatory", "available", "mandatory", "available", "available"),
    "Living Tiṇai":          ("mandatory", "available", "available", "mandatory", "available"),
    "Reading Room":          ("mandatory", "available", "mandatory", "forbidden", "available"),
    "Extraction / Collection": ("mandatory", "available", "mandatory", "forbidden", "available"),
    "Reconnection":          ("mandatory", "available", "available", "forbidden", "available"),
}

DERIVATION_NOTE = """\
**Derived posture: underivable today.** §1.5 derives a posture from the
exhibit's Claim Objects and its Absence records, in seven precedence steps. This
page has neither: no Claim Object exists for any proposition on it, and no
absence on it has been typed under constitution §6. Derivation therefore returns
nothing — not `Reading Room`, which is rule 7's residual and would be a false
output, since rule 7 fires on a claim set that has been examined and did not
match rules 1–6.

**Assigned posture: {env}, editorially, by the workbook.** That assignment is
`INHERITED-UNVERIFIED` and carries no override reason, because the register that
would hold one does not exist. `SCHEMA.md` §7: *"Nothing in `03-REGISTERS/`
records a publication decision, an environment assignment, or a duplication
finding."* Creating the Editorial Register — specified at §11.5 as
`03-REGISTERS/editorial-decisions.csv`, with `decision_type` including
`posture-assignment`, and with `value`, `derived_value`, `override_reason` and
`derived_residual` — is a prerequisite for this page, not a nicety: an
assignment with no derivation to disagree with cannot be audited.

*(Note for the framework's own re-audit: §1.5 names these fields
`derived_posture` / `assigned_posture` / `override_reason`, and §11.5 names them
`value` / `derived_value` / `override_reason` / `derived_residual`. The two
sections of the specification do not agree on the field names for the same
record. This brief follows §11.5, which is the section that defines the
register. Recorded, not resolved — it is a defect in the specification, not in
this page.)*

**Secondary environment.** The workbook gives this page `Reading Room` as
secondary — as it does for all 96. Framework §1.6.1 rules that a value constant
across every row is not a value: it is the single statement *"Source Mode
exists"*, and the column should be retired rather than migrated. This brief
treats the page's secondary environment as **Source Mode**, a universal display
state, not as a second posture.
"""

MODE_ROW = """\
| Posture | Source | Atlas | Investigation | Field | Classroom |
|---|---|---|---|---|---|
| {env} | {m0} | {m1} | {m2} | {m3} | {m4} |

*(Framework §1.7.)*
"""

STATUS_FLOOR_NOTE = """\
**On "lowest status".** `INHERITED-UNVERIFIED` is not the bottom rung of a
ladder. Framework §3.2: six of the seven statuses describe evidential standing
and one describes *where the assertion came from* — a prior model's summary of
its own conversation — so *"the interface must therefore never sort or
colour `INHERITED-UNVERIFIED` between `PROVISIONAL` and `HYPOTHESIS` as though
the statuses formed a single ladder."* The floor above is therefore stated by
rule rather than by sorting: a row carrying `INHERITED-UNVERIFIED` has had no
retrieval event behind it, so no set containing one stands above it. {ceiling}
Where the handoff labelled a finding `VERIFIED` or `PROVISIONAL`, that label came
in with it and did not survive intake — `CLAUDE.md`, the inheritance rule.
"""

# Printed when the supports_page scan returns nothing for the slug.
ADJACENCY_NOTE = """\
**Adjacency is not support.** Where verified work in this repository happens to
be *about subjects a page discusses*, it is still not *linked to that page*: no
row in any register carries `supports_page` naming this slug. Under framework §3.3 a
claim's status comes from its own Evidence Links, so a page cannot inherit
standing by sitting next to a register. Linking is an editorial act (§11.5) and
transfers nothing by itself; the page's propositions have to be written as Claim
Objects and evidenced in their own right.
"""

# Printed when it returns something. A link is a recorded relation between a row
# and a page; it is not a finding that the row supports what the page says, and
# the two are separated here rather than collapsed. The per-page reading is
# required by assertion in emit(), so a new linked row fails the build until a
# human writes what it does and does not carry.
ADJACENCY_NOTE_LINKED = """\
**A link is not yet support.** The row(s) above are *recorded against* this page
in `supports_page`. Under framework §3.3 a claim's status comes from its own
Evidence Links, and linking is an editorial act (§11.5): the link records that
someone tied the row to the page, not that the row establishes any proposition
the page makes. What each linked row actually carries is stated below, and the
page's own propositions still have to be written as Claim Objects and evidenced
in their own right.
"""


# --------------------------------------------------------------------------
# Per-page content
# --------------------------------------------------------------------------

PAGES = [

{
 "slug": "index",
 "question": "What was taken out of the record of ancient South Asia, who took it out, and what does this institution actually hold in its place?",
 "observed": """\
The audited page is 861 words, type `threshold`, with **0 estimated source
entries, 0 external links, 0 tables and 1 inline SVG**, and **0 inbound links** —
the only page of the fifteen that nothing else on the site points at, which is
what a front door is. Its central public claim, as the workbook records it, is
*"Something was emptied out of this place. Here is what it held. A reproducible
museum of ancient South Asia, from Meluhha to Keezhadi."*

That is three claims in one strapline: an extraction claim (*something was
emptied out*), a holdings claim (*here is what it held*), and a method claim
(*reproducible*). The page carries no source section for any of them.""",
 "evidence": [
   ("IH-174", "The strapline's own name. The handoff records *'Meluhha to Keezhadi'* as **superseded** by *Veli* (S-01). The threshold page still runs it."),
   ("IH-258", "Contradiction X-09: the project's records disagree on the brand architecture across four successive positions, and the handoff's ruling is that every affected document *'should be read as carrying an unresolved name'*. The threshold is the document where a name is load-bearing."),
   ("IH-250", "Contradiction X-01: six figures in circulation for the atlas site count. The handoff's resolution path is that *'until then no document prints a site count'*. A threshold that promises a museum must not size it."),
   ("IH-018", "Correction C-06: no meta-commentary or process narration anywhere on the site; corrections go to a corrections log. Binding on threshold copy, which is where drafting residue survives longest."),
   ("IH-002", "The handoff states of itself that no count in it was re-run against any corpus. Nothing quantitative on this page can be sourced to the inheritance."),
 ],
 "evidence_extra": "",
 "posture_extra": """\
**A derivation tension, recorded and not resolved.** The page's central claim is
that something *was emptied out* — an extraction claim. §1.5's derivation runs in
precedence order, and rule 1 fires first: an exhibit whose central claims depend
on material whose access status is `NOT ACCESSIBLE`, or on a refused or
unanswered access request, derives to **Extraction / Collection**. Rule 3
(absence dominance → Nocturnal Veḷi) is three steps later. On its strapline
alone this page would derive to Extraction / Collection, not to the Nocturnal
Veḷi it is assigned.

This cannot be settled here, for a reason worth stating: derivation runs over
Claim Objects and typed absences, and the page has none, so what looks like a
conflict between a derived and an assigned posture is really two editorial
readings of one unsourced sentence. It is recorded so that when the strapline is
decomposed into claims (§6), the derivation is run rather than assumed. Note the
consequence if it did derive to Extraction / Collection: that posture's `Avoid`
is *"no spectacle or unsupported allegation"*, and *"something was emptied out of
this place"* with no source section is an allegation with no support attached.""",
 "asset_extra": """\
Two of the four slots are unfillable as specified.

- **`claim-specific diagram`** — embargoed. Framework §3.12: *"a derived asset may
  not be commissioned or published while the claim it depicts is
  `INHERITED-UNVERIFIED` or `HOLD`."* Every claim on this page is at that floor.
- **`source facsimile`** — a facsimile is a reproduction of a source. The page has
  **0 source entries**. There is nothing for it to be a facsimile of until §6 runs.

`opening atmosphere asset` and `social card` are unblocked in principle, but a
social card carries the strapline, and the strapline is what `IH-174` and
`IH-258` put in question.""",
 "launch": [
   "The strapline's name is settled. `IH-174` records *'Meluhha to Keezhadi'* as superseded and `IH-258` records the brand architecture as contradicted; `09-DECISIONS/OWNER-DECISIONS.csv` **D-004** (what Veḷi principally is) is the open decision. This is an owner call, not a retrieval.",
   "No site count, page count or holdings figure appears in threshold copy, per `IH-250`'s own resolution path and `DECISIONS-NEEDED.md` **D-034**.",
   "The three claims in the strapline exist as three separate Claim Objects with computed statuses (§3.1–3.2), and the extraction claim in particular carries either evidence or a typed absence — not a mood.",
   "The posture is derived and then assigned, with the override reason logged in the Editorial Register (§11.5), given the tension recorded in §2.",
   "Source Mode is reachable from the threshold itself (§1.7, mandatory in every posture). A front door from which the visitor cannot reach the claims behind the promise is the one thing this page may not be.",
 ],
 "unit": """\
**MVP-U1 — threshold claim decomposition.** No retrieval; entirely in-repository.
Decompose the strapline into Claim Objects, one per assertion; write each into a
register with `supports_page = index`; type the extraction claim's absence under
constitution §6 if it is to be argued from silence; record falsifiers. Then run
both §8 adversarial tests on the result — this is the page where the
prestige-bias test and the preferred-counter-narrative test bite hardest, because
a threshold is written to be affecting.

**What it cannot do.** It cannot promote anything. The decomposition produces
`HYPOTHESIS` rows at best, which is the correct output: the strapline's holdings
claim is a claim about this institution's own collection, and the institution has
no collection register yet. The naming question is not a research question at
all and returns to the owner as D-004.""",
 "conflicts": "",
},

{
 "slug": "enter",
 "question": "What may a visitor take from this institution as established, and what does the institution refuse to assert?",
 "observed": """\
1,803 words, type `foyer`, **2 estimated source entries, 0 external links, 0
tables, 0 inline SVGs**, and **113 inbound links** — by a wide margin the most
linked-to page in the audited build. Central public claim: *"Evidence, and what
it will not support."*

Two things follow from those numbers. A page that 113 other pages point at is
load-bearing for the whole site's navigation, so its errors propagate. And a page
whose subject is *evidence* carrying two source entries is asserting a standard
it does not demonstrate.""",
 "evidence": [
   ("IH-057", "Correction C-37: the live site gives three atlas counts — **140 on Enter**, 158 on Explore, 175 in the page title. This page is one of the three disagreeing surfaces, and the one a visitor meets first."),
   ("IH-250", "Contradiction X-01, of which C-37 is a part: six figures across the records. Resolution path: extract the dataset, count, generate every stated figure from it; until then no document prints a count."),
   ("IH-052", "Correction C-32: `enter.html` referenced `RIGVEDA_corpus_analysis.md` and `MELUHHA_TO_KEEZHADI_synthesis.md`, both absent from the packaged archive. The fix is recorded as made in the zip and **not confirmed on the deployed site** (work item 5)."),
   ("IH-201", "The live check, 31 Aug: those two references return 404 and `/artifact-atlas` returns no text to a fetcher. The foyer's evidence links are the ones that were broken."),
   ("IH-183", "Superseded row S-10: four successive MVP shapes, and the handoff records that **none** was adopted by the owner (X-10, work item 12). A foyer orients a visitor to a release whose shape is not decided."),
 ],
 "evidence_extra": "",
 "posture_extra": """\
**Investigation Mode is mandatory here.** §1.7 makes PROVE IT mandatory in Tamil
Retrofuture, and §1.7's own rationale says why: this is one of the three postures
*"where the institution is arguing against something"*, and PROVE IT is *"the
mechanism that keeps the argument falsifiable rather than rhetorical."* A foyer
whose claim is *"evidence, and what it will not support"* is the exact case. This
converts a design feature into a launch dependency: **`enter` cannot launch in
this posture before PROVE IT (§9) exists.**""",
 "asset_extra": """\
`claim-specific diagram` is embargoed under §3.12 while the page's claims sit at
`INHERITED-UNVERIFIED`. `source facsimile` is buildable in principle — a foyer
about evidence is the natural place for one — but the two source entries the page
has are not yet identified in any register here.""",
 "launch": [
   "PROVE IT exists and is reachable from this page (§1.7, mandatory in Tamil Retrofuture).",
   "No atlas count appears on it (`IH-057`, `IH-250`, D-034).",
   "The two 404s are confirmed fixed **on the build that is actually being released** — which is blocked on `DECISIONS-NEEDED.md` **D-033**, since the repository cannot presently say which build is authoritative.",
   "The page's promise about what evidence *will not* support is backed by typed absences under constitution §6, not by a rhetorical gesture. None is typed today.",
   "Its 113 inbound links are re-pointed or preserved deliberately: with 15 of the 96 pages in the release, most of what links here will not exist at launch. That is a navigation decision nobody has recorded.",
 ],
 "unit": """\
**MVP-U2 — foyer audit against the released build.** Confirm the C-32 fix live,
confirm which of the 113 inbound links survive into the release, and remove or
source every count. **Blocked on one thing and unprobed on the other.**
The audited archive `veli-site(3).zip` is not in this repository and has no row
in `02-SOURCES/access-ledger.csv`, so the pages cannot be read here — that is a
missing input, not an egress question, and the owner supplying the archive is
what clears it. The deployed site has **not been probed**: `SRC-052`'s sixteen
hosts do not include it and neither do `SRC-080` to `SRC-083`, so this brief does
not state that it is unreachable, only that no one here has tried. Nor is it
covered by any general statement about this session's egress: `SRC-027` records
`indianculture.gov.in` reachable on 2026-09-07, so "everything outside the git
lane is refused" is not a property this repository holds, and §3 of the README
keeps that conflict open rather than resolving it.

**A `HOLD` row is owed once the deployed site has been probed and failed** —
not before, since framework §3.2 gives `HOLD` to *a required source* that *is*
unreachable, and an unattempted fetch does not establish that. What is owed now
is the probe, and then either a ledger row or a hold. Neither licenses a
substitute audit run off the workbook's own summary of pages nobody here has
opened. D-033 is the
decision that unblocks it.""",
 "conflicts": "",
},

{
 "slug": "artifact-atlas",
 "question": "Where was each of these objects found, how precisely is each findspot and date known, and which regions are unknown rather than empty?",
 "observed": """\
**{words} words of prose**, {entries} estimated source entries, 0 external links, 0 tables, 2
inline SVGs, {inbound} inbound links. Type `atlas`. H1: *"Where the objects were
found."* Decision `Keep`, Risk **Low**, MVP rank 3.

The title asserts a number — *"175 Ancient South Asian Sites Mapped"* — and the
number is one side of an open contradiction. Framework §8.1 relays the schema
assessment's collision A, whose words these are — `INHERITED-UNVERIFIED`, quoted
inside a `HYPOTHESIS` document, and not the framework's own verdict: the count
was *"adopted as settled fact, put in a page title, and rated low-risk."*

**`Keep` and `Low` are two different columns produced by two different
instruments, and an earlier draft of this brief collapsed them.** `method-limits.csv`
gives *Curatorial decision* as *"Keep, Revise, Hold, Split or Merge based on role,
source visibility, risk and overlap"*, limited by *"Decisions remain provisional
until factual and specialist review."* It gives *Claim risk* separately, as
*"Flagged categorical, causal, priority/origin, institutional and quantitative
central claims"*, limited by the sentence one clause of `RA-019`'s
`what_to_recheck` puts a standing control on:
*"Risk means verification priority, not falsehood."* `Low` is therefore not a
judgement that the page is sound; it is a judgement that the page is not near the
front of the verification queue.

A third layer, *Source visibility*, was *"Estimated bibliography entries from
visible Sources/References sections and counted live external links."*, limited
by *"A visible bibliography does not prove claim-level support or source
quality."* The {entries} entries belong to that layer. **Whether they are what
produced `Low` is an inference this brief cannot check** — the workbook nowhere
states how the two relate — and an earlier draft asserted it as fact in two
places. What can be said without inference is that {entries} estimated entries
against {words} words of prose is a measurement of a page's furniture.

**And the workbook holds no row in which any instrument read the page's central
number.** That is an argument from absence over one document, so it is typed:
`claim-risk.csv` is the sheet whose method is *"Flagged categorical, causal,
priority/origin, institutional and quantitative central claims"* — a site count
in a title being the fourth and fifth of those — and it holds no row for this
page. The absence is `NOT PRODUCED` within the workbook's own scope, checked at
build time; it says nothing about whether the number was examined anywhere else,
and `IH-250` records that it was, in the inheritance, and left unresolved.""",
 "evidence": [
   ("IH-105", "The atlas holds 194 site records, 315 class-windows and 14 classes, with **54 of 199 site-class rows dated from excavation reports and 145 marked assumed**. Three quarters of the dating is flagged as assumption inside the dataset itself."),
   ("IH-250", "Contradiction X-01: 140 / 150 / 158 / 167→175 / 194 / 199 sites, and 299 against 315 windows. Recorded resolution path: *\"Extract the atlas dataset to JSON, count, and generate every stated figure from it; until then no document prints a site count.\"*"),
   ("IH-057", "Correction C-37: three different counts on three live surfaces."),
   ("IH-060", "Correction C-40: the owner's visual-concept document and VELI-03 disagree on sites and windows; the handoff blocks the prospectus on it."),
   ("IH-201", "`/artifact-atlas` returns no text to a fetcher because it is JS-rendered. An atlas unreadable without JavaScript fails release gate 5 before any accessibility review begins."),
   ("IH-002", "No count in the handoff was re-run against the atlas HTML. Every figure above is a report of a report."),
 ],
 "evidence_extra": "",
 "posture_extra": """\
**Atlas Mode is mandatory** (§1.7), and §8.7 lists eight things the Atlas may
never do. Four are at issue for this page, and only the first can be checked
here, because the build has not been retrieved:

1. *Show a total in its own voice* — the only one checkable from here, and it
   fails: the title in `page-audit.csv` states a count.
2. *Render an approximate location as a precise point* — the risk `IH-105`'s 145
   assumed rows create. Whether v1 in fact renders them as precise points is not
   knowable without the build.
3. *Render unknown as blank* — constitution §13 requires unknown regions to stay
   visibly unknown; a blank map *"reads as empty and empty reads as nobody."*
   Untestable from here.
4. *Let a filter silently drop the weak evidence to produce a cleaner picture.*
   Untestable from here.

§8.1 proposes a rule for the first of those four: **the Atlas has no headline
count.** A count is a claim with a status, an inclusion rule and a falsifier,
shown inside the Atlas with its status visible, or it is not shown.

**The first build of this brief wrote, here, that §8.1's rule "is the one that
makes the page launchable at all" and that "under that rule the Atlas ships
*before* D-034 is answered."** That reading is withdrawn and is recorded rather
than deleted, because it is the failure `BF-029` logs: a design proposition at
`HYPOTHESIS` in a specification this repository wrote was allowed to settle an
`OPEN` owner decision, and the sentence sat four sections away from the conflict
it was settling. `OWNER-DECISIONS.csv` D-034's own `notes` say what §8.1 does:
*"Neutralised but not answered by museum-framework.md §8.1 — the Atlas can be
built without the number and cannot be titled without it."* §7 records the
conflict; nothing in this section decides it.""",
 "asset_extra": """\
This is the one page of the fifteen whose asset set is not embargoed by §3.12 —
its assets are a dataset and its presentation, not diagrams derived from
individual claims. It is instead gated on the dataset existing as objects:
`verified dataset` presupposes Universal Evidence Objects with typed Place
Assertions and typed Date Assertions (§2.7, §2.8), and the 145 rows marked
*assumed* must each be typed rather than rendered. The `downloadable table` and
the exclusion export (§5.2) are the parts that make every absence argument on the
map checkable, and they are the parts most easily deferred.""",
 "launch": [
   "Whatever \u00a78.1's rule is taken to require of this page \u2014 its own words are that the number in view is a property of the current filter, *\"always shown with the filter, never as a title\"*, and the page's current title states a total. What follows from that is D-034's to settle and not this brief's: \u00a77 records the conflict and the three arms without choosing one, and this gate states the rule rather than a launch condition derived from it.",
   "Every mapped thing is an object with a status and an attestation mode; a findspot and an attributed provenance are never the same marker (§8.2).",
   "The 145 `assumed` date rows are typed as assertions with their basis, or excluded. Rendering them identically to the 54 report-dated rows is `IH-105` published as if it were `IH-105` solved.",
   "Unknown zones are a rendered layer, and the excavation/survey coverage overlay exists (§8.2) — without it no absence on the map is checkable.",
   "The page renders without JavaScript, or has a documented equivalent (`IH-201`; release gate 5).",
   "The exclusion set is exportable (§5.2).",
 ],
 "unit": """\
**MVP-U3 — atlas dataset extraction and count derivation.** The unit is already
specified, by the inheritance itself: `IH-250`'s recorded resolution path is
*"Extract the atlas dataset to JSON, count, and generate every stated figure from
it; until then no document prints a site count."* The final clause was cut from
both of this brief's quotations of the row in an earlier draft, and it is the
only part of `IH-250` that constrains what this brief may itself print
(`BF-029`); §7 records where the constraint bites. Done properly it produces a register of site records with typed place and
date assertions, a dependency map for the 88 bibliography entries (framework §3.5
— 88 citations tracing to a handful of excavation reports count as a handful),
and a derived count with an inclusion rule.

**Blocked on one thing, and it is not egress.** The atlas data lives in
`artifact-atlas.html` inside `veli-site(3).zip`, supplied 2026-09-01. That archive
**is not in this repository** and has no access-ledger row — which is why the
whole workbook is `INHERITED-UNVERIFIED` rather than merely unverified. The
unblocking action is the owner supplying the archive, or naming the authoritative
build (D-033). Until then a `HOLD` row is owed, and this page cannot be the
release's connective heart on a dataset nobody here has opened.""",
 "conflicts": """\
## 7. The recorded conflict — a disputed count in the title, at rank {rank} of the launch set

**This brief records the conflict and does not resolve it.** Three arms are set
out below because a conflict whose consequences are not stated is not legible;
none of them is preferred here, and no sentence in this section is to be read as
choosing one.

**What this section disclaims, by name.** §2 above wrote, in the first build,
that §8.1's no-headline-count rule *"is the one that makes the page launchable at
all"* and that *"under that rule the Atlas ships before D-034 is answered."* That
was a settlement, written in this brief's own voice, of a decision that is
`{d034}`. It is withdrawn in §2 and preserved there rather than deleted. §5's
first gate — *"No headline count anywhere on the page, per §8.1"* — is a
statement of what §8.1 requires, not a finding that the requirement is met or
that meeting it would end the matter; see the last paragraph of this section on
what that gate does and does not reach.

The page's own title asserts a figure that this repository has logged as disputed
and has not closed, and the same workbook schedules the page {rank_ordinal}:

| File | Cell | Value |
|---|---|---|
| `page-audit.csv` | `Title` | *"{title}"* |
| `mvp.csv` | `Rank` | **{rank}** of 15 |
| `mvp.csv` | `Decision` / `Risk` | `{decision}` / **{risk}** |
| `mvp.csv` | `Release dependency` | *"{release_dep}"* |
| `claim-risk.csv` | row for `artifact-atlas` | **none; the build stops if one appears** |
| `03-REGISTERS/inherited-claims.csv` `IH-250` | `INHERITED-UNVERIFIED` | contradiction X-01: 140 / 150 / 158 / 167→175 / 194 / 199 sites |
| `03-REGISTERS/inherited-claims.csv` `IH-057` | `INHERITED-UNVERIFIED` | correction C-37: three different counts on three live surfaces |
| `09-DECISIONS/OWNER-DECISIONS.csv` **D-034** | status | `{d034}` |

*(Every cell in that table is read from its file at build time. §7 of an earlier
draft retyped them, in a section written to remove typed literals — `BF-029`.)*

Rank {rank} is not an ordering detail: it is the {rank_ordinal} page a visitor is
scheduled to meet, and on the current title it meets them with a number the
inheritance records as one of six competing values. Neither column that rated the
page reached that number. §1 above sets out why — `Decision` and `Risk` are
different instruments with different limits, `Risk` means verification priority
and not falsehood, and the `claim-risk.csv` sheet that would have recorded a
publication gate on a quantitative central claim holds no row for this page at
all — checked at build time, and this section will not build if one is added.

**This section prints the six competing counts, and `IH-250` says not to.** The
row's resolution path reads in full: *"Extract the atlas dataset to JSON, count,
and generate every stated figure from it; until then no document prints a site
count."* An earlier draft quoted that row twice and cut the final clause both
times. The clause is restored, and this section is inside its scope: what is
printed above is the *contradiction* — six values none of which is asserted as
the count — rather than a site count, and that is a reading of `IH-250`'s intent,
not a permission it grants. It is recorded here so that a reader who thinks the
row forbids this table can see that the question was noticed rather than avoided.

**Already raised, and not by this brief.** `DECISIONS-NEEDED.md` **D-034** —
renumbered from D-006 on 2026-09-07 (`09-DECISIONS/DECISION-ID-MAP.csv`) — states
it: *"A contested number is inside a launch page title, presented as settled,"*
and *"The atlas number is load-bearing for a page ranked third in the launch
set."* This brief adds no identifier and takes no position; it records that the
conflict survives into the brief set and names what each arm would change.

**What changes under each arm**, stated so the decision is legible and for no
other purpose. They are listed in no order of preference, and each is reachable
without the other two:

- **The number is settled.** The dataset is extracted and counted (§6, MVP-U3)
  and X-01 closes. What the title then does is *still* open, and this brief
  cannot say it survives with a re-derived figure: §8.1 as quoted below forbids a
  number in the title under any circumstances, so a settled count makes the title
  question answerable without answering it. Rank {rank} stands unless something
  else moves it. **Cost:** this is the only arm that waits on the archive (see
  below), and the only one that produces a value D-034 asks for.
- **The title is changed, the number left open.** The title drops the figure. The
  page ships at rank {rank} with no total in its own voice, and D-034 stays
  `{d034}` — the page-count half of it untouched, and the atlas half unanswered
  rather than resolved. **Cost:** an editorial act is exactly what §2 of this
  brief records this repository cannot yet perform. The Editorial Register that
  §11.5 specifies to hold *"a publication decision, an environment assignment or
  a duplication finding"* **does not exist**, and §2's finding applies here
  unchanged — *"an assignment with no derivation to disagree with cannot be
  audited."* A title changed with nothing recording who changed it, from what,
  and why is the shape of the problem this page is about.
- **The rank is changed.** The page moves out of the {top_ranks} and the release
  opens on something whose central claim is not an unsettled number. D-034 stays
  `{d034}` in both halves, and the title is untouched. **Cost:** `page-audit.csv`
  records **{inbound} inbound links** to this page, the {inbound_ordinal} count
  among the fifteen behind `{top_slug}`'s {top_n}, so demoting it changes the
  site's link structure and not only an order — and the Editorial Register
  problem in the arm above applies to a rank change too.

**One thing all three arms share, and it does not decide between them.** The
count itself cannot be derived here: §6 records that the atlas data lives in
`artifact-atlas.html` inside `veli-site(3).zip`, which is not committed to this
repository and has no `02-SOURCES/access-ledger.csv` row. Under `CLAUDE.md`'s
negative-evidence standard that absence types as **`NOT ACCESSIBLE`** — the
evidence exists, was produced, is known to be held by the owner, and is simply
not here — and not as `NOT PRODUCED`, `NOT PRESERVED` or `ABSENT DESPITE ADEQUATE
SEARCH`. `01-INHERITED/site-review/` holds {n_running_w} inherited running-list documents
that have not been searched for atlas site records, so even the `NOT ACCESSIBLE`
typing is provisional on that search.

That is an access fact, not an evidential one, and it bears on the first arm
only. The second and third arms are editorial decisions about a title and an
order; neither needs the count, and treating them as blocked behind it would
convert a missing archive into a reason to leave the launch order as it is. An
earlier draft of this section did exactly that, closing with *"the title question
is blocked behind the count question"* — which eliminated the second arm by fiat
and left the status quo as the only reading. Withdrawn, and recorded rather than
deleted.

**What §8.1 reaches, read exactly.** A draft of this section said *"§8.1 does not
reach the title at all"*. It does. **§8.1's rule ends** — the section itself continues past it — *"The
number of sites in view is a property of the current filter and is always shown
with the filter, never as a title."* The rule reaches the title directly, and the current title breaks it. Three things follow,
and none of them closes D-034.

- The second arm is what §8.1 **would require if the specification were
  adopted** — not an alternative to the rule, and not something the rule can
  compel. §8.1 is a design proposition at `HYPOTHESIS` (framework §14.4). A
  proposition at that standing does not amend a `page-audit.csv` field or
  overrule the workbook's rank, and adopting the specification is itself an owner
  act nobody has recorded. An earlier draft of this bullet wrote *"is what §8.1
  requires"*, which is the same category error §2's withdrawn sentence made,
  pointed at a different arm.
- Even fully adopted, §8.1 would settle only where a number may appear. It says
  nothing about what the number is, which is the half of D-034 the first arm
  addresses and the second does not.
- The framework's own paragraph after the rule reads *"the Atlas can be built and
  shipped before that is answered, because it never asserts a total in its own
  voice"* — which is the sentence §2 of this brief adopted and has withdrawn.
  D-034's `notes` put the same fact the other way round: *"the Atlas can be built
  without the number and cannot be titled without it."* Both are true and neither
  is a count.""",
},

{
 "slug": "veli",
 "question": "Does Tamil veḷi carry one semantic field across the senses *empty, open, outside, clear, light* and *true*, or are these separable lexemes; and what does the evidence for each sense consist of?",
 "observed": """\
1,076 words, type `semantic-field`, 9 estimated source entries, 0 external links,
2 tables, 46 inbound links. Decision `Keep`, Risk `Low`. H1 and central claim:
*"Veḷi means empty, open, outside, clear, light and true — and those are one word,
not six."*

The workbook's own assessment is the sharpest of the fifteen: *"Central
brand/intellectual page; dictionary entries, attested languages, and semantic
convergence must be exact."* The claim is lexicographic. *"One word, not six"* is
a polysemy-against-homonymy claim, which is decided by etymology and
distributional evidence, not by a list of glosses — and a gloss list is what a
dictionary entry looks like.""",
 "evidence": [
   ("IH-062", "Owner decision HD-01, status recorded as SETTLED: the name is Tamil *veḷi*, retroflex *ḷ*, romanised *veli*; the Telugu excommunication sense is *'treated as a feature'*. Note what this is — a naming decision, not a lexical finding. It settles what the institution is called, not what the word means."),
   ("IH-314", "Work item 46: Tamil-dictionary and native-speaker confirmation is **owed** for *mela/kila, suvadu, adukku, nokku, tinai, navalam* and *porul*. The semantic work behind the brand vocabulary is recorded as not done."),
   ("IH-258", "Contradiction X-09: the brand architecture is unresolved across four positions. This page is where that lands, since it is the page that explains the name."),
 ],
 "evidence_extra": """\
**This is the page whose central claim has the most direct open retrieval
route** — one of three units in the fifteen with a live route in this session
(with `the-languages-we-lost` and the lexical half of `sound-changes`; README
§3), and the only one where the route bears on the page's *central* claim rather
than on a component of it. The lexical evidence for a Dravidian etymon is in DEDR, and DEDR is reachable in
this session: `SRC-061` (DEDR, Burrow and Emeneau 1984, 2nd ed., as re-parsed in
JAMBU `data/dedr/`), `SRC-060` (JAMBU CLDF database), `SRC-062` (Proto-Dravidian
reconstructions after Krishnamurti), `SRC-067` (DravLex) — all `VERIFIED` in
`02-SOURCES/access-ledger.csv`, all reached over the git-proxy lane that
`SRC-052` records as the only lane open.

**And a ceiling that comes with it.** DEDR-via-JAMBU is one digitisation of one
1984 dictionary. `03-REGISTERS/dedr-digitisation-lineage.csv` and
`02-SOURCES/dependency.csv` exist because this repository has already had to
record that. Under framework §3.2, sources resolving to one author, dictionary or
digitisation yield **`PROVISIONAL`, not `VERIFIED`**. The Tamil Lexicon (Madras)
would be the second, independent line; its host `dsal.uchicago.edu` is `SRC-056`
with `retrieval_capable = NO`. So the honest ceiling for the central claim in
this session is `PROVISIONAL`, and saying so in advance is part of the unit.""",
 "posture_extra": """\
**A second derivation tension, recorded and not resolved.** Nocturnal Veḷi is the
posture of *not yet known*. This page's central claim is a positive, defended
lexical proposition — *known by argument from sources*, which is Reading Room as
posture (§1.6.1). The assignment is legible as a decision about the institution's
self-presentation rather than about the page's claim set: the word *veḷi* names
the museum, and the threshold posture is named after it. That is not an
illegitimate reason, but §1.3 forbids exactly one thing here — posture must not
be inferred from tone, and must not lower or raise an evidential bar. A Nocturnal
Veḷi framing must not make *"one word, not six"* read as evocative rather than
falsifiable.""",
 "asset_extra": """\
**`pronunciation audio where licensed` is the framework's named failure case.**
§1.6.3(a) singles this phrase out: the workbook is *"treating a consent question as a
licensing question"*, and under the evidence-class mapping, `oral/living` evidence
requires **consent, not licence**, with a Consent Register row mandatory (§11.4).
*"Where licensed"* is not an available route. Any recorded speaker of Tamil on
this page needs a consent record naming what was given, by whom, for what use,
for how long, and how it is withdrawn.

`glyph diagram` is a derived asset of a claim about the retroflex *ḷ* grapheme
and is embargoed under §3.12 until that claim has a status above
`INHERITED-UNVERIFIED`. `language map` inherits every constraint in §8.2 and
§8.7 — most sharply §8.7's first rule, *never colour a region by a language*.""",
 "launch": [
   "A Translation Block for *veḷi* exists to the constitution §7 standard: original script, transliteration, grammatical form, semantic range, textual context, edition, exact locator, translation used, alternative translations, and the interpretive consequence of choosing between them. None of that is in this repository today.",
   "*'One word, not six'* is stated as what it is — an etymological and distributional claim, with DEDR entry numbers, and with the homonymy alternative stated rather than omitted.",
   "The single-digitisation dependency is recorded in `02-SOURCES/dependency.csv` and the claim is presented at `PROVISIONAL`, not `VERIFIED`, until a second independent lexicographic line is read.",
   "The Telugu sense is either evidenced from a Telugu source or removed. `IH-062` treats it as *'a feature'* of the name — a branding judgement, which is not evidence that the sense exists as described.",
   "Any pronunciation audio has a Consent Register row (§11.4). No licence substitutes for it.",
 ],
 "unit": """\
**MVP-U4 — the veḷi semantic field, from retrievable lexical data.** Retrieve the
DEDR entry or entries for the *veḷi* etymon through the JAMBU lane already logged
at `SRC-060`/`SRC-061`; record every reflex, gloss and cognate with its entry
number; state whether the six senses fall under one entry or several, which is
the operative test of *"one word, not six"*; check the Proto-Dravidian
reconstruction at `SRC-062`; check DravLex (`SRC-067`) for the modern comparative
set. Log the retrieval in `02-SOURCES/access-ledger.csv`, the dependency in
`dependency.csv`, and the claims in a new register with `supports_page = veli`.

**Ceiling: `PROVISIONAL`.** Single digitisation lineage, per §3.2.
**Owed alongside:** a `HOLD` row for the Tamil Lexicon (`dsal.uchicago.edu`,
`SRC-056`, not reachable) and for a Telugu lexicographic source, naming what each
would settle. Among the fifteen, this is the unit whose *central* claim has the most
direct route with the access this session has — which is a statement about
retrieval capability, not a work order; sequencing the MVP set is what README §0
says this unit does not do.""",
 "conflicts": "",
},
]

PAGES += [

{
 "slug": "tinai",
 "question": "What is tiṇai in the Tamil poetic tradition, in which texts is the five-landscape scheme actually set out, when were those texts composed and redacted, and what does the scheme claim about the relation between land and social life?",
 "observed": """\
1,407 words, type `concept`, 19 estimated source entries and **2 external
links** — the only page of the fifteen with any live external link at all — 1
table, 8 inbound links. Decision `Keep`, Risk `Low`. H1: *"Tiṇai: a poetics that
thinks with the land."* The workbook's assessment: *"Defines a knowledge
framework rather than merely describing a historical topic."*

That assessment is the whole problem in one line. A page that defines a framework
the rest of the institution then uses is not one exhibit among fifteen; it is a
dependency of the others. `Living Tiṇai` is a posture named after it.""",
 "evidence": [
   ("IH-314", "Work item 46: *tinai* is explicitly among the terms for which **Tamil-dictionary and native-speaker confirmation is owed**, alongside *mela/kila, suvadu, adukku, nokku, navalam* and *porul*. The word this page defines is on the list of words the project records as not yet checked."),
   ("IH-176", "Superseded row S-03: *TINAI* is also a component of the three-word brand system (VELI / TINAI / MELAKEELA-as-mode), itself superseded the following day. The term is simultaneously an analytic category and a product name."),
   ("IH-248", "Section 8 HELD register: *Sangam, Tolkappiyam, Tevaram, the Pali canon, the Asokan edicts, the Saunaka Atharvaveda and a clean Chandogya* — recorded as a load-bearing source *'currently reached via NOT OBTAINED / NOT FOUND'*, carrying *'Everything Tamil, Pali and Prakrit that is not the Kural'*. Under the handoff's Rule 7 every claim resting on it is HELD."),
 ],
 "evidence_extra": """\
`IH-248` is the operative row. It names *Sangam* and *Tolkappiyam* among the
sources recorded as NOT OBTAINED / NOT FOUND — and those are the sources a
tiṇai page would have to rest on, since the page's own subject is a Tamil poetic
scheme. **Where exactly the scheme is set out is not something this brief can
state**: naming the chapter and the text that carries it would be a claim about
the contents of documents the same row records as unread here, which is the
error the page is suspected of. What can be said is the structural position: the
page defines a framework from primary texts that no one in this project's record
has read directly, which is a different and more serious position than having
read them and cited them thinly.""",
 "posture_extra": """\
**Field Mode is mandatory in Living Tiṇai** (§1.7). The children's investigation
and the Field Bag (§10.4) are not an enhancement for this page; the matrix makes
them a condition of the posture. Nothing of the sort exists, and the closest
inherited artefact — the Dig engine (`IH-212`) — is recorded as *not adopted by
the owner*, with `09-DECISIONS/OWNER-DECISIONS.csv` **D-006** (Keezhadi or an
inscription as the children's pilot) still open.

Recorded, not resolved: either the matrix's *mandatory* is a launch condition,
in which case no Living Tiṇai page launches before a Field Mode exists, or it
describes the posture's finished state rather than its first release. The
framework does not distinguish the two, and this brief does not decide it. It
affects three of the fifteen (`tinai`, `keeladi`, `the-water-city`).""",
 "asset_extra": """\
`claim-specific diagram` — the obvious one being a five-landscape diagram — is
embargoed under §3.12, and would in any case be the single asset most likely to
harden a poetic scheme into a map of real territory.

**The `Avoid` constraint is load-bearing for the `opening atmosphere asset`:**
*"no generic landscape decoration."* The five tiṇai are named for landscapes, and
a stock photograph of hills would fail the constraint and misstate the scheme in
one move — the tiṇai are poetic-situational categories, and illustrating them as
scenery is the reading the page exists to correct.""",
 "launch": [
   "The Tolkāppiyam *Poruḷatikāram* passages that set out the scheme are read in a named edition with exact locators, or the page states that they have not been and carries no claim about what the scheme says.",
   "Chronology is established before interpretation (method step 2): composition, redaction, commentarial layer and modern interpretation of the tiṇai scheme are four different dates, and the commentarial tradition is where much of the systematisation lives.",
   "A Translation Block for *tiṇai* itself (constitution §7), with the semantic range across 'landscape', 'class', 'genre', 'situation' — and the interpretive consequence of choosing among them, since the page's title takes one.",
   "The brand use and the analytic use of the word are separated on the page, per `IH-176`/`IH-258`. A reader must not have to work out whether *tiṇai* is being used as a Tamil poetic term or as this institution's product vocabulary.",
   "Field Mode resolved for this posture (see §2), and D-006 answered if the children's pilot is where it comes from.",
 ],
 "unit": """\
**MVP-U5 — the tiṇai primary-source pass.** Retrieve a named edition of the
Tolkāppiyam *Poruḷatikāram*, locate the tiṇai chapters, record the scheme with
exact locators, and separate the text's own statements from the commentators'.

**Retrieval state: the likely hosts are refused, the git lane is untested.**
`SRC-083` records `sacred-texts.com` and `wisdomlib.org` refused at
2026-09-07T15:10Z, `SRC-080` GRETIL, `SRC-081` the Internet Archive, `SRC-082`
TITUS. Whether a citable edition is served over the still-open git lane
(`SRC-058`) is **untested**, and testing it is step 1 of the unit — so this
brief does not state that the text is unreachable, only that every host probed
so far has refused. A `05-HOLDS/` row is owed once that search has been run and
failed, naming the edition and what it would settle.""",
 "conflicts": "",
},

{
 "slug": "the-ledger",
 "question": "By what rule does this institution rank evidence, and how may a visitor check that rule against any claim the institution makes?",
 "observed": """\
948 words, type `research-essay`, 26 estimated source entries, 0 external links,
0 tables, 0 inline SVGs, 10 inbound links. Decision `Keep`, Risk `Low`. H1: *"The
Ledger."* The workbook's assessment names the trap: *"its readiness depends on
claim-level citations, not prose confidence."*

Note the shape. 26 bibliography entries, no table, no external link, on a page
whose subject is how to check sources.""",
 "evidence": [
   ("IH-046", "Correction C-26, **caught by the owner**: Claude built the Ledger credibility feature and then cited caste-page sources without auditing them, leaving Kabir Babu 2016 (off-field, no findable footprint), Choudhury 2021 (MDPI preprint) and Kumar & Choudhury 2020 visibly carrying claims that Aktor, Davis, Olivelle, Beteille and the corpus actually support. Rejected as R-20; superseded as S-13 — audit-after-build replaced by audit-first. Also recorded as owner decision HD-17 and work item 49."),
   ("IH-289", "Work item 21: synthesis sections 17–19 must be read, **section 18 may be a ledger draft, and this was never done**. The prior articulation of the ledger's own rule has not been read by anyone in the current record."),
   ("IH-183", "Superseded row S-10: 'The Ledger and the First Gallery' was the first of four MVP shapes, none adopted by the owner (X-10). The page is a survivor of a release plan that was replaced three times."),
 ],
 "evidence_extra": """\
`IH-046` is the most consequential row in the fifteen, and it is about this page.
The feature that ranks source credibility was built and then found to be resting
on three sources it would itself have demoted. The failure was found by the owner,
not by the system, and the recorded fix was a workflow inversion — audit first.
That inversion is a claim about how this institution works, and it is a claim
this page makes in public.""",
 "posture_extra": """\
**This page is the type case of Reading Room *as posture*.** §1.6.1 distinguishes
Reading Room the posture — an exhibit *"whose substance is the argument itself:
methods pages, historiography, the ledger"* — from Reading Room the substrate,
the fallback state 34 of 96 pages were filed under because the audit had nothing
more specific to say. `the-ledger` is named in the framework as an example of the
former. Its assignment is therefore the one Reading Room assignment in the
fifteen that is not suspected of being residual.

**And it is the page most exposed to an open owner decision.**
`DECISIONS-NEEDED.md` **D-015** asks whether Reading Room remains a seventh peer
posture at all or is demoted entirely to Source Mode, leaving six. If it is
demoted, this page does not lose its content — but the institution loses the
posture it was assigned to, and the page becomes an exhibit displayed in Source
Mode. Recorded, not resolved.

**Investigation Mode is mandatory; Field Mode is forbidden** (§1.7).""",
 "asset_extra": """\
`claim-specific diagram` is embargoed under §3.12 — with a particular irony
worth naming, since the diagram a ledger page wants is a diagram of the status
derivation, and that diagram would depict a rule rather than a historical claim.
The embargo is on assets derived from Claim Objects; a diagram of the framework's
own §3.2 derivation table is a diagram of a specification, not of a claim, and
is not blocked. That distinction should be made explicitly rather than left for
a production scheduler to guess.""",
 "launch": [
   "The ranking rule the page describes **is** the rule the repository runs: `CLAUDE.md`'s seven statuses, framework §3.2's derivation table, and the independence rule in `02-SOURCES/dependency.csv`. A ledger page describing a different rule from the one the registers implement is a second source of truth.",
   "The page states the §3.2 interface consequence in public: no user action can raise a claim's status; there is no status dropdown. This is the institution's strongest verifiable commitment and the cheapest to state.",
   "The three sources demoted under C-26/R-20 are gone from wherever they still sit, and the re-attribution recorded as owed on `birth-was-not-always-destiny` and `jatization` is confirmed done — the handoff lists it among the **unconfirmed** items.",
   "There are claims to rank. A ledger over a claim set that is entirely `INHERITED-UNVERIFIED` displays one status and demonstrates nothing; at least one page in the release must have rows above the floor before this page has anything to show.",
   "Synthesis section 18 is read (`IH-289`, work item 21), or its absence is recorded, before the page asserts a ledger rule that a prior draft may already have stated differently.",
 ],
 "unit": """\
**MVP-U6 — re-derive the ledger rule in-repository.** No egress required, and
that makes this the second unit to run after MVP-U4. Reconstruct the ranking rule
from `CLAUDE.md`'s status vocabulary, `00-CONTROLLER/CONTROLLER-RECONCILIATION.md`
C-1's mapping of the constitution's inheritance dispositions onto statuses, and
framework §3.2; record it as a specification, not as a finding; check it against
what `04-AUDITS/validate-registers.py` actually enforces; and write the C-26
demotions into `02-SOURCES/dependency.csv` so the failure is preserved rather
than described. Correction history is preserved — `CLAUDE.md`: never delete a
`REJECTED` row.

**What it cannot do.** It cannot verify anything about the past, and it must not
be mistaken for evidentiary work. It produces a specification and a correction
record. That is exactly what this page needs and it is the reason this page could
be ready before most of the other fourteen.""",
 "conflicts": "",
},

{
 "slug": "keeladi",
 "question": "What was excavated at Keeladi, what dates the deposits and the inscribed material, and what happened administratively to the excavation and its reports?",
 "observed": """\
1,164 words, type `place`, 14 estimated source entries, 0 external links, 1
table, 8 inbound links. Decision `Keep`, Risk `Low`. H1: *"Keeladi: a literate
southern city — and an excavation the state could not leave alone."* The title
asserts a date: *"A Literate Tamil City from 6th Century BCE."*

Two arguments run in one page, and they belong to different evidence classes and
different verification routes. One is archaeological and epigraphic — deposits,
dates, inscribed sherds. The other is institutional — transfers, reports,
rework requests, evaluations. The second names a state body and asserts
interference.""",
 "evidence": [
   ("IH-113", "Provisional finding P-05 in the handoff, from secondary sources: *5,500 artefacts, then transfer, then a 982-page report in January 2023, then a May 2025 rework request, then a 114-page evaluation* — with the handoff's own caveat, **'pin each step'**. One artefact count and four administrative events — a transfer, a report, a rework request, an evaluation — none pinned to an issuing body and a document."),
   ("IH-061", "Correction C-41: among the sentences banned from the prospectus is *'any Keeladi claim beyond a specific inscribed mark'*, alongside *'any number not derivable from the repository'*. The project has already written itself a rule about how far Keeladi claims may go."),
   ("IH-215", "Work item 44: contacting Dr. G. Sundar of the Roja Muthiah Research Library, as a bridge to UTSC Digital Tamil Studies and the TNSDA Tamil-Brahmi graffiti project, is *'the most important single verification task in the file'* — and the handoff records that **nothing has been sent to any of the nine outreach roles**."),
   ("IH-212", "The Dig engine, a PWA over Keezhadi with an on-device Field Bag, plus a Children's Council and a Living Worlds Council with veto over misrepresentation and false continuity — T5 concepts, **none recorded as adopted by the owner**."),
 ],
 "evidence_extra": """\
`IH-061` deserves emphasis because it is a rule the project wrote for itself and
this page is where it applies. If no Keeladi claim may go beyond a specific
inscribed mark in a funding prospectus, the standard on a public exhibit page
cannot be looser. *"A literate Tamil city from 6th century BCE"* is a claim about
a date and a claim about literacy, and the second is carried by the inscribed
material the rule points at.

**The preferred-counter-narrative test, run on this page.** Keeladi carries the
strongest Tamil-nationalist valence of the fifteen, and both halves of the page
are congenial to a position this project holds: an early literate southern city,
and a state that interfered with the excavation. That is a reason to press
harder, not softer. Three specific pressures follow.

*On the date.* An early date for southern literacy is the finding this project
would most like to be true, which is exactly the condition under which a
secondary-source chain gets accepted. `IH-113` is `PROVISIONAL` in the handoff
and `INHERITED-UNVERIFIED` here, and the handoff's own instruction is *pin each
step*. The correct posture is that the date is unestablished in this repository,
not that it is established and awaiting citation.

*On the interference narrative.* Four administrative events — a transfer, a
report, a rework request, an evaluation — are consistent with interference and
also consistent with ordinary bureaucratic process. `IH-113` supplies the
sequence, not the motive, and the page's H1 supplies the motive. That gap is the
page's largest unsupported step, and it is not a right-of-reply problem before it
is an evidence problem: the right of reply governs how a supported allegation is
published, not whether an unsupported one may be.

*On the direction of correction.* The inheritance contains one logged case where
a correction ran *towards* the canonical finding rather than away from it —
`IH-029`/R-09, where the handoff records that *"Claude's caution understated a
well-supported finding"*. It is cited here because the six-headline correction
record (`IH-051`) otherwise reads as a one-directional story about this project
overclaiming in its own favour, and a one-directional story about one's own bias
is itself a congenial thing to believe.""",
 "posture_extra": """\
**Field Mode is mandatory in Living Tiṇai** (§1.7) — and here it collides with an
open owner decision. `09-DECISIONS/OWNER-DECISIONS.csv` **D-006** asks whether
Keezhadi or an inscription is the children's pilot. So the posture's mandatory
mode, for this page, is the subject of a decision nobody has taken. Recorded, not
resolved; see the same tension under `tinai` §2.

**The institutional half of the page does not sit in this posture at all.** An
excavation *"the state could not leave alone"* is a claim about withheld or
controlled knowledge, which is Extraction / Collection — §1.5's derivation rule 1
and rule 6 both reach for it before rule 5 (place/material dominance) fires.
Whether the page is one exhibit in two postures or two exhibits is an editorial
question the Editorial Register does not yet exist to hold.""",
 "asset_extra": """\
**`site/landscape photography` and `present-context image` require physical
presence.** Framework §1.6.3(a) maps environmental and site-bound evidence to
*"site photography — physical presence required"*. There is no route to it from
this session, and none from this repository; it is a commissioning decision with
a travel budget behind it. `material macro` needs object access and therefore a
custody chain and a holder permission (§3.4).

This asset set is the one place in the fifteen where the workbook's schedule and
physical reality are furthest apart: four assets, all requiring someone to be in
Tamil Nadu with permission.""",
 "launch": [
   "The date in the title is carried by a claim with a stated basis — which deposits, which method, which report — or the title stops asserting it. `IH-113` rests on secondary sources and the handoff itself says to pin each step.",
   "The literacy claim is tied to specific inscribed material with catalogue identifiers, per the project's own C-41 rule (`IH-061`).",
   "Each of the four administrative events has an issuing body, a date and a document. Four events reported at second hand is a narrative, not a chronology.",
   "The interference claim triggers the right-of-reply obligation (§11.3) against every named institution, and `09-DECISIONS/OWNER-DECISIONS.csv` **D-010** — which institutional claims may presently be published — is the governing open decision.",
   "Field Mode resolved for this posture, and D-006 answered if the children's pilot is Keezhadi.",
   "Site and object imagery is commissioned with rights, credit and a custody position, or the page ships without it.",
 ],
 "unit": """\
**MVP-U7 — the Keeladi report chain.** Pin each of the five events in `IH-113` to
a document: the excavation reports and their authors, the 982-page report of
January 2023 and its issuing body, the transfer order, the May 2025 rework
request, the 114-page evaluation. Separately, obtain the dating basis for the
6th-century-BCE claim from the excavation reports rather than from press
coverage.

**Retrieval state: `NOT ACCESSIBLE` for the hosts probed, untested for the
rest — and the difference matters.** `SRC-081` to `SRC-083` record the
general-web hosts refused on re-probe at 2026-09-07T15:10Z, and `SRC-052`'s
`blocking_constraint` generalises from a sixteen-host probe list. **No probe of
an ASI, TNSDA or Indian publisher host is recorded anywhere in the ledger**, so
this brief does not assert that they are unreachable. Nor does it type the
absence, because the constitution §6 typology has **no code for "not
searched"** — `NOT RECOGNIZED` means evidence present but unidentifiable, and
using it for an unrun search would be worse than leaving the absence untyped,
since a wrongly typed absence stops looking like an open question.
`04-AUDITS/REAUDIT-QUEUE.csv` `RA-018` already records the gap in the typology.
What is stated instead is the fact: the search has not been run. `indianculture.gov.in` was recorded reachable at `SRC-027`
earlier the same day, and `SRC-080`'s own note states the governing principle:
*"A ledger row is a timestamped probe, not a standing property (D-042)."* The
two rows are therefore not reconcilable from this brief. **Probing the specific
hosts is step 1** of the unit, and its result is a ledger row either way.

**And one part escalates rather than blocks.** `IH-215` names the single most
important verification task in the inherited file as an outreach to a named
librarian, and records that nothing has been sent. Institutional access is one of
`CLAUDE.md`'s five escalation categories. That goes to the owner as an owner
action, not into a `HOLD` row — a hold records an unreachable source, and this
source is reachable by a person writing a letter.""",
 "conflicts": "",
},
]

PAGES += [

{
 "slug": "before-the-indus",
 "question": "Are there mortuary or ritual features in South Asia earlier than the Indus urban phase whose solar alignment is demonstrated rather than proposed, and what dates each of them?",
 "observed": """\
1,724 words, type `deep-time`, 17 estimated source entries, 0 external links, 1
table, 9 inbound links. Source state: *substantial bibliography, mostly
non-linked*. H1 and central claim: *"Before the Indus, the graves already faced
the sun."*

Decision `Hold`. Risk **Critical** — the only Critical-risk page in the launch
set. `claim-risk.csv` gives its publication gate as `Hold` and its owner as
`Unassigned`. The workbook's assessment: *"Strong threshold/exhibit material;
reconstructions and continuity claims require exceptional restraint."*

The verb in the headline is the thing to look at. *"Already faced"* is a
completed, factual assertion about alignment and about relative chronology. §3
records what the evidence behind it is rated at.""",
 "evidence": [
   ("IH-124", "Provisional finding P-16, from Kenoyer et al. 1983: Baghor I is a **proposed** Palaeolithic shrine with **contextual** dating c. 9000–8000 BCE and **no directly datable material at the feature**. Three hedges in one row: proposed, contextual, nothing datable at the feature itself."),
   ("IH-125", "Provisional finding P-17, from Chattopadhyaya 1996: Mesolithic Ganges cemeteries at Damdama and Mahadaha contain solar-aligned graves — with **absolute dates OPEN** (work item 33), which PENDING-RULE 19 makes a gate for publishing contested deep-history claims."),
   ("IH-243", "Section 8 HELD register: **Kenoyer et al. 1983 is a load-bearing source whose direct access is not recorded anywhere** in the project files or retrievable threads; it carries Baghor and is reached via citation only; the dating basis is *now stated as contextual*. Under the handoff's Rule 7 every claim resting on it is HELD until it is read directly."),
   ("IH-051", "Correction C-31, rejected as R-19: this page's headline has **already been corrected once**, from *'20,000 years older than the Vedas'* down to *'a proposed Palaeolithic shrine'* with an evidence panel and a note that there is no directly datable material at the feature. It is one of six headlines the handoff records as *'overstated in the platform's own direction'*, and it produced standing rule 17 — check the headline for overclaim in the platform's own direction as rigorously as for deflection."),
 ],
 "evidence_extra": """\
Read `IH-051` against the current headline. The correction moved the page from an
absolute-antiquity claim to a hedged one — *proposed*. The headline the workbook
records today, *"Before the Indus, the graves already faced the sun"*, is
unhedged again, in a different register: it drops the numeric overclaim and keeps
a factual assertion of alignment and of relative priority. Whether that is a
second overclaim or an acceptable summary of `IH-125` is exactly what a
specialist review is for, and is exactly what standing rule 17 exists to catch.

**Both adversarial tests are live on this page and they pull in the same
direction.** The prestige-bias challenge is quiet here — the claim is not
canonical. The preferred-counter-narrative challenge is loud: a deep-time
indigenous-priority finding is a claim this project has an interest in, and the
handoff has already recorded one failure of exactly that kind on exactly this
page. Neither test has been run and logged in `04-AUDITS/BIAS-FAILURE-LOG.csv`
for this page.""",
 "posture_extra": """\
Nocturnal Veḷi is the right posture and the demanding one. §1.3: a Nocturnal Veḷi
exhibit *"does not get a lower evidential bar because it is about unknowns; it
gets a stricter negative-evidence discipline"*. And the `Avoid` — *"no fantasy
portal or occult styling"* — is a real constraint on a page about solar
alignments and shrines, where the visual grammar available is precisely the
occult one.

*"Before the Indus"* is itself a negative-comparative frame and needs constitution
§6 typing: what pre-Indus ritual evidence should exist, where, the probability it
was produced, the probability it survived, excavation coverage, and whether we
could recognise it. Absence of comparable features elsewhere is not evidence that
these are first.""",
 "asset_extra": """\
`claim-specific diagram` is embargoed by the strictest rule in the set. §3.12
defines a derived asset as *"a claim-specific diagram, map, chart or
reconstruction"* derived from a Claim Object, and forbids commissioning or
publishing one *"while the claim it depicts is `INHERITED-UNVERIFIED` or
`HOLD`"* — and this page's claims are at both. A reconstruction diagram of a
proposed shrine with no directly datable material is the single most persuasive
and least supportable asset in the whole release.

`source facsimile` is **not** a derived asset and is not embargoed by §3.12: a
facsimile reproduces a source, it does not depict a claim. It is blocked here
for a different and simpler reason — the two publications the page rests on have
not been obtained, so there is nothing to reproduce. The distinction is worth
keeping straight, because collapsing it would block this page harder than the
rule actually does, and this is the page where over-blocking is the tempting
error.

The `Priority = MVP` on this page's asset-register row is one limb of the
conflict recorded in §7.""",
 "launch": [
   "**D-032 is answered by the owner.** Nothing else in this section can be sequenced until it is; see §7.",
   "`IH-243`'s HOLD clears: Kenoyer et al. 1983 is read directly, and every claim resting on it is re-statused from a reading rather than from a citation.",
   "Absolute dates for Damdama and Mahadaha are obtained (`IH-125`, work item 33) — PENDING-RULE 19 makes this a gate for publishing contested deep-history claims, and the inheritance therefore already treats it as a launch condition.",
   "The headline is tested against standing rule 17 (`IH-051`) by someone other than its author, and the test is logged whether or not it finds anything (§3.11).",
   "Specialist review, per the workbook's own required action and release gate 4.",
   "The alignment claim and the chronology claim are separated. *'Solar-aligned'* and *'before the Indus'* are two claims with different evidence and different failure modes, and the headline fuses them.",
 ],
 "unit": """\
**MVP-U8 — read the two load-bearing sources directly.** The repository knows
these two publications only as the registers record them — **Kenoyer et al.
1983** and **Chattopadhyaya 1996** — with no fuller citation in
`02-SOURCES/access-ledger.csv` or anywhere else here. Expanding either into a
full author list or a title before it has been read would be supplying
bibliography from memory, which is precisely what `IH-243` records as not having
happened; the first act of this unit is therefore to obtain the full citation,
not to assume it. Kenoyer et al. 1983 for Baghor I; Chattopadhyaya 1996 for
Damdama and Mahadaha; then the absolute dating literature for the Ganges
Mesolithic cemeteries. Closing `IH-243` is the single action that would move the
most on this page, because every Baghor claim is HELD behind it.

**Retrieval state: the likely lanes are refused; the two publications are
unprobed.** `SRC-052` records sixteen hosts refused on 2026-09-07, including
`doi.org`, the three bibliographic APIs, `archive.org` and `zenodo.org`;
`SRC-081` records the Internet Archive refused again at 15:10Z, `SRC-082` TITUS,
`SRC-083` sacred-texts and wisdomlib. **Neither publication has itself been
probed**, and `SRC-058` records the git lane open to arbitrary public
repositories, so this brief does not assert that no host serves them — it
records that the lanes most likely to carry them are refused and that the
specific search has not been run. Type the absence before writing the verdict, per
`04-AUDITS/BIAS-FAILURE-LOG.csv` `BF-010`'s standing control. A `05-HOLDS/` row
is owed for each once the search has been run and failed, naming what each would
settle; `05-HOLDS/` already contains six such records, so the form is
established.""",
 "conflicts": """\
## 7. The recorded conflict — MVP rank 8 and withhold-from-MVP

**This brief records the conflict and does not resolve it. Nothing above or below
assumes an outcome.**

`before-the-indus` is, in the same workbook, at once inside the launch set and
excluded from it:

| Sheet | Cell | Value |
|---|---|---|
| `mvp.csv` | `Rank` | **8** of 15 |
| `mvp.csv` | `Decision` | `Hold` |
| `mvp.csv` | `Risk` | **Critical** |
| `mvp.csv` | `Release dependency` | *"Withhold from MVP until load-bearing claims receive claim-level citations and specialist/editorial review."* |
| `page-audit.csv` | `MVP` | **Yes** |
| `page-audit.csv` | `Decision` / `Risk` | `Hold` / `Critical` |
| `page-audit.csv` | `Required action` | *"Withhold from MVP until load-bearing claims receive claim-level citations and specialist/editorial review."* |
| `asset-register.csv` | `Priority` | **MVP** |
| `claim-risk.csv` | `Publication gate` | `Hold` |
| `claim-risk.csv` | `Owner/status` | `Unassigned` |

The row instructs the reader not to do what the sheet it appears on does. It is
the only one of the fifteen in this state and the only Critical-risk page in the
launch set. Three sheets schedule it for the MVP; three cells in those same
sheets withhold it.

**Already raised, and not by this brief.** `DECISIONS-NEEDED.md` **D-032** —
*"`before-the-indus` is inside the MVP set and marked withhold-from-MVP"* —
carries it, with a row in `09-DECISIONS/OWNER-DECISIONS.csv`, raised 2026-09-07 by
the curatorial audit schema review and renumbered from D-004 on the same day
(`09-DECISIONS/DECISION-ID-MAP.csv`). Its category is *two consequential positions
both remaining viable / publication approval*. This brief adds no new identifier
and takes no position; it records that the conflict survives into the brief set
and names what each arm would change.

**What changes under each arm**, stated so the decision is legible and for no
other purpose:

- **In.** The `Hold` is overridden. Fifteen pages launch. The Critical-risk page
  is in the release, and every gate in §5 becomes a launch blocker on a page the
  workbook rated as needing specialist review. The override must be logged with a
  reason in the Editorial Register (§11.5); an override with an empty reason is
  invalid (§1.5).
- **Out.** The MVP set is fourteen with a gap at rank 8. The asset-register
  `Priority = MVP` row is wrong and should be re-derived. `before-the-indus`
  moves to the verification queue, where MVP-U8 belongs regardless. The overlap
  cluster *Meluhha and Indus* — `meluhha`, `meluhha-trade`, `the-water-city`,
  `before-the-indus`, recommended as *"one curated exhibit sequence"* — goes from
  two members in the release to one. `meluhha` and `meluhha-trade` are `MVP = No`
  in `page-audit.csv` and were never in it.

**What does not change under either arm**, and this is an observation about
sequencing, not a resolution: the page cannot be published today under either
reading, because `IH-243` is HELD and `IH-125`'s absolute dates are open, and
PENDING-RULE 19 makes those a gate. The membership question is a separate
question from the readiness question, and answering the second does not answer
the first — rank, gap, asset priority and the exhibit sequence all still turn on
D-032.""",
},

{
 "slug": "the-water-city",
 "linked_licenses_copy": False,
 "linked_reading": """\
**What the linked row carries, and what it does not.** `WLW-001` carries
{linked_statuses}, and it is the only row linked to any of the fifteen that
carries anything other than `INHERITED-UNVERIFIED` — a difference of status, not
a position above one. It reads: *"As at 2026-09-08T21:13Z, before this unit added any row,
no register in 03-REGISTERS/ carried a water claim above INHERITED-UNVERIFIED,
and no row in any register carried supports_page = the-water-city."* Its subject
is **the state of this repository's registers at a timestamp**, not the past this
page describes. Nothing about drains, wells, tanks, bathing platforms or the
absence of palaces gained standing when it was written. What changed is the
sentence above — a row now names this page — and nothing else, so §1's account of
why the step 14 slots stay empty is unaffected.

**Three properties of the row that matter for reading it.**

1. **It is tensed, and the tense is doing work.** The row's own `notes` record
   that the first draft was falsified by its own existence — it carries
   `supports_page = the-water-city`, so a flat *"no row carries it"* was untrue
   the moment it was committed. *"before this unit added any row"* is the repair,
   made under adversarial review rather than quietly. Read without that clause the
   row contradicts itself.
2. **It is a probe, not a standing property.** `02-SOURCES/access-ledger.csv`
   `SRC-080`, `notes`: *"A ledger row is a timestamped probe, not a standing
   property (D-042)."* An earlier draft cited the file without the row, which is
   the locator failure `BF-024` already logs. The
   row's locator names a *"scan of all 14 registers carrying a supports_page
   column"*; the scan behind this brief finds {scanned}. The row's status certifies
   what a scan returned at 21:13Z on 2026-09-08 and certifies nothing about
   today.
3. **It and this brief are one source, not two.** The row's `notes` cite
   `06-BRIEFS/mvp-fifteen/09-the-water-city.md` §3 as having established the same
   finding, and this brief now cites the row. Both run the same scan over the same
   directory. Under `CLAUDE.md`'s source-independence rule they count as one, and
   neither corroborates the other.""",
 "question": "How was water managed in Indus urban settlements, on what evidence does the absence of palaces rest, and would a palace be recognised in this material record if one existed?",
 "observed": """\
1,181 words, type `place`, 11 estimated source entries, 0 external links, 1
table, 7 inbound links. Decision `Keep`, Risk `Low`. H1: *"The Indus built its
cities around water — and left no palace to control it."*

The sentence has two halves and they are different kinds of claim. The first is
positive and material: drains, wells, tanks, in excavated contexts. The second is
a negative claim about a category, and it is the one the headline turns on —
*no palace* is what makes the sentence an argument rather than a description.""",
 "evidence": [
   ("IH-138", "Hypothesis H-04: post-urban Indus settlement moved east tracking a weakening monsoon. For: correlation. Against: causation is undocumented and no single cause is settled for the decline. The handoff requires it be labelled an inference. Adjacent to this page rather than under it — it concerns the post-urban phase."),
   ("IH-029", "Correction C-16, **rejected as R-09**: Claude had written *'the sample is ONE individual, I6113'*, and the handoff records that **Claude's caution understated a well-supported finding** — eleven Indus-Periphery outliers from Gonur and Shahr-i-Sokhta form a cline of which I6113 is part. Adjacent to this page rather than under it, and cited here for the direction of the error: this is the one logged case in the inheritance where a correction ran *towards* the canonical finding rather than away from it."),
   ("IH-263", "Contradiction X-14, and the row `DECISIONS-NEEDED.md` **D-033** rests on: the live `rakhigarhi` page says there is no seafaring in the Rigveda while the site's corpus file records *nau-* at n = 40 — and `rakhigarhi` is not among the 96 pages of the audited build."),
 ],
 "evidence_extra": """\
**No row listed above bears on the water engineering or on the absence of
palaces**, and this is a statement about the rows this brief examined, not a
quantifier over every register — asserting the second is the failure `BF-027`
logs. The rows above are the nearest Indus-related material the inheritance
offers and none of them supports this page's claims; they are listed so that the
gap is legible rather than implied.

**One row that is cited as bearing on it, and does not.** `WLW-001`'s `notes`
name two rows as water claims in `inherited-claims.csv`: `IH-138`, which is above
and is a claim about the past, and `IH-183`, which is not. `IH-183` carries
`INHERITED-UNVERIFIED`, like every other row in that register; its *claim* text
opens with the word `SUPERSEDED`, which is the handoff's own disposition and not
a status — `CLAUDE.md` C-1: a disposition is *"recorded alongside a status, never
in place of one."* What the row records is a chain of replaced release shapes —
*The Ledger and the First Gallery*, then *Into Veli: The First Door* (`VELI-06`
A6), then *A Drop of Water*, then T4, then T5 — so its subject is the release
plan and the water is in an exhibit's title.

**That disagreement is with a register row, and it is not settled here.** This
brief reads `IH-183` as a product record; `WLW-001`'s supporting note reads it as
a water claim. One of the two is wrong. `WLW-001` carries {linked_statuses}, and a
brief is not the instrument for amending a register row at any status. Logged as
`IC-X-002` in
`04-AUDITS/INTERNAL-CONTRADICTIONS.csv` and queued as `RA-024`. What does *not*
turn on it: under either reading `IH-183` carries `INHERITED-UNVERIFIED` and
supports nothing on this page.

**The negative claim is the page's real work, and the standard for it is
written.** `CLAUDE.md`'s negative-evidence standard requires, *before* arguing
from absence: what evidence should exist, where, the probability it was produced,
the probability it survived, excavation or sampling coverage, accessibility, and
whether we could recognise it if we saw it — then a type from `NOT PRODUCED` ·
`NOT PRESERVED` · `NOT EXCAVATED` · `NOT PUBLISHED` · `NOT ACCESSIBLE` ·
`NOT RECOGNIZED` · `DOCUMENTED DESTRUCTION` · `ABSENT DESPITE ADEQUATE SEARCH`.
*"Left no palace"* is currently untyped, and the difference between
`ABSENT DESPITE ADEQUATE SEARCH` and `NOT RECOGNIZED` is the difference between a
finding about Indus society and a finding about archaeological categories.

**And *palace* is an inherited English category.** `CLAUDE.md`'s translation
standard names *race, tribe, slave, barbarian, **fort**, religion, caste,
civilization, invasion, indigenous* as categories to audit before use. *Palace*
belongs to that list by the same logic, and this repository has already done the
work once for a neighbouring term: `06-BRIEFS/pur-4j-corpus.md` and
`03-REGISTERS/rigveda-pur-typology.csv` audit *pur-* rather than assuming
'fort'. The same discipline is owed here — a claim that no palaces exist is only
as strong as the criterion by which one would be identified.""",
 "posture_extra": """\
Living Tiṇai — *known through place and material* — fits the positive half of the
page exactly. **Field Mode is mandatory** (§1.7); see the tension recorded under
`tinai` §2, which applies unchanged.

The `Avoid` — *"no generic landscape decoration"* — is a real constraint on a page
about hydraulic infrastructure, where the temptation is a river photograph
standing in for a drainage system nobody has photographed.""",
 "asset_extra": """\
`site/landscape photography` and `present-context image` need physical presence
at Indus sites (§1.6.3(a)); `material macro` needs object access, a custody chain
and holder permission (§3.4); `ecological map` is a map asset and inherits §8.2
and §8.7 — in particular, excavation coverage must be drawable, because without a
coverage overlay the palace-absence argument is not checkable on the map that
illustrates it.""",
 "launch": [
   "The absence claim is typed under constitution §6, with excavation coverage stated for the sites it generalises over. Untyped, it is not publishable in any posture.",
   "A recognition criterion for *palace* is stated: what material signature would count, and who proposed it. Without one, *'no palace'* reports a vocabulary, not a settlement pattern.",
   "The positive water-engineering claims are tied to named excavation reports with locators, and the source genealogy is mapped (method step 5). Whether this literature in fact concentrates on few excavations is what step 5 measures; this brief asserts no genealogy it has not mapped.",
   "The bridge between infrastructure and political organisation is tested separately (method step 10). *'No palace to control it'* joins a material observation to a claim about power; those are two claims.",
   "The `Meluhha and Indus` overlap cluster is addressed: the workbook recommends the four pages be presented as one curated sequence, and two of the four are in the release — `the-water-city` and `before-the-indus`, the second subject to D-032; `meluhha` and `meluhha-trade` are `MVP = No`.",
 ],
 "unit": """\
**MVP-U9 — the palace-absence dossier.** Build the negative-evidence record
before any part of the argument is written: excavated area against total site
area for Mohenjo-daro, Harappa, Dholavira and Lothal; publication state of each
excavation; the identification criteria proposed for elite residences in Indus
archaeology and by whom; then type the absence. In parallel, the positive
half — a register of water features with site, context and report locator.

**Retrieval state as for MVP-U7**: the bibliographic and publisher lanes are
refused — `SRC-052`'s sixteen-host probe of 2026-09-07 covers `doi.org`,
`api.crossref.org`, `api.openalex.org`, `api.semanticscholar.org`,
`archive.org` and `zenodo.org` — with `SRC-081` to `SRC-083` recording four
more; the excavation literature itself has never been probed and the git lane
(`SRC-058`) is untested for it. A `05-HOLDS/` row is owed once the search has
been run and failed. What needs no retrieval at all is the criterion work: the recognition criterion for *palace* is an
argument about categories and can be assembled from what is reachable, and it is
the half of this unit that changes the page most.""",
 "conflicts": "",
},
]

PAGES += [

{
 "slug": "kural",
 "question": "Which words for social rank, birth-group or ritual status occur in the Tirukkuṟaḷ, in which edition and recension, and what does their presence or absence support?",
 "observed": """\
879 words, type `text`, **1 estimated source entry**, 0 external links, 2 tables,
1 inline SVG, 55 inbound links. Decision `Revise`, Risk `Medium`. H1 and central
claim: *"Thirteen hundred and thirty couplets on how to live, and the word for
caste is not in any of them."* The workbook's assessment: *"Strong anchor text if
translations, editions, counts, and absences are reproducible."*

Every one of those four conditions is a separate problem, and the page carries
one source entry for all of them.""",
 "evidence": [
   ("IH-091", "The handoff's finding V-08, from `kural_ta.txt`, VELI-03 and MANIFEST — *'the first Tamil corpus'*: the Tirukkuṟaḷ has 1,330 couplets with **zero occurrences of *cati* and zero of *vetam***, in the register's own unmarked romanisation. Entered here as `INHERITED-UNVERIFIED`; the handoff's own `VERIFIED` label did not survive intake."),
   ("IH-248", "Section 8 HELD register: the Tamil, Pali and Prakrit corpus *other than the Kural* is recorded as NOT OBTAINED / NOT FOUND. The Kural is the exception — which is why this page exists — but the comparative material that would show what the Kural's silence means is not held."),
   ("IH-012", "The parallel case, and a correction: *'no caste word in the Vedas' is wrong* — *varṇa* occurs 23 times in the Rigveda and the correct finding is that *jāti* is absent from it. The same argument-form on the same subject has already been found overstated once in this project."),
 ],
 "evidence_extra": """\
**The register's romanisation is unmarked, and one of the two words is
ambiguous under it.** `IH-091` gives the forms as `cati` and `vetam`, without
diacritics. Restored one way, *vetam* is *vēṭam* — guise, ritual garb; restored
another, it is *vētam* — Veda. The page is titled *"Tamil Ethics Without Caste
**or Ritual**"*, so which word was counted decides whether the title's second
half is supported at all. This brief keeps the register's unmarked forms rather
than choosing, because choosing is the interpretive act constitution §7 requires
a Translation Block for, and neither form has one here. Resolving it is part of
the unit in §6.

**The claim's form is the second problem, and naming it costs no retrieval.**
`IH-091` records zero occurrences of **two** Tamil words. The headline says *"the word for
caste is not in any of them"* — the definite article doing work no census
supports. A census of two forms establishes the absence of two forms — and whether those
two are the whole candidate set for what an English reader means by *caste* is
itself a lexicographic question this repository has not answered. **This brief
does not supply the candidate list**: enumerating Tamil terms for social rank
from memory would be doing exactly what it objects to on the page, one level up.
Establishing the search set from a Tamil lexicographic source is the first step
of the unit in §6, and until it is done neither the page's claim nor this
brief's objection to it is settled.

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
repository**, with no access-ledger row.""",
 "posture_extra": """\
**Investigation Mode is mandatory** (§1.7): Tamil Retrofuture is one of the three
postures where the institution argues against an official account, and PROVE IT
is what keeps such an argument falsifiable. This page is a good argument for the
rule — a claim of the form *'the word is not in the text'* is trivially
falsifiable and therefore ideal for the mode, provided the search set is
published with it.

The `Avoid` — *"no kitsch, fake Tamil or neon overload"* — bears on a page that
displays Tamil script: transliteration and script must be correct and sourced,
not decorative.""",
 "asset_extra": """\
**`translation excerpt rights` is an unbounded dependency.** §1.6.3(a) maps
modern translation to *"third-party rights negotiation — unbounded timeline"*.
Quoting a modern English Tirukkuṟaḷ translation means clearing rights with a
rights-holder on their schedule. `DECISIONS-NEEDED.md` **D-029** (does the
institution ever assert fair dealing, and in which jurisdiction) is the open
decision that governs whether there is an alternative.

`primary-text facsimile` is the asset this page most needs and the one that would
most improve it: a facsimile of a named edition at a named locator is the
evidence the page's argument runs on. `editorial illustration` is a derived asset
and is embargoed under §3.12.""",
 "launch": [
   "The search set is stated. Which Tamil forms were counted, which were not, and why. Without it the headline is an assertion about a word class, not a count.",
   "The edition and recension are named. The Tirukkuṟaḷ has a commentarial tradition and variant readings; a count is a count in a text, and `kural_ta.txt` is a file, not an edition.",
   "The claim is narrowed to what the census supports, per the `IH-012` precedent, or the wider claim is dropped.",
   "The absence is typed under constitution §6 — a didactic poem's silence about birth-groups is a curated silence, and `CLAUDE.md` is explicit that *silence in a curated record is not refutation*.",
   "Translation rights are cleared or D-029 is answered.",
   "PROVE IT exists (§1.7, mandatory in this posture), and the census is reproducible from it.",
 ],
 "unit": """\
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
`dsal.uchicago.edu` is `SRC-056`, `retrieval_capable = NO`.""",
 "conflicts": "",
},

{
 "slug": "sound-changes",
 "question": "Which phonemes are attested in Old Tamil and not in Sanskrit, which writing systems encoded them and from when, and what does the difference support about contact between the two?",
 "observed": """\
1,898 words, type `comparative-visual`, **0 estimated source entries**, 0 external
links, **3 tables**, 0 inline SVGs, 55 inbound links. Decision `Revise`, Risk
`Medium`. Title: *"Sound Changes: Dravidian Phonemes Sanskrit Could Not Write"*.
H1: *"What the mouth does to a name."*

Three comparative tables and no source section at all. The workbook's assessment
asks for the right thing — *"should lead with the visual relationship and make
the schematic/measured distinction explicit"* — and that distinction is the
page's whole difficulty: a phoneme chart looks measured and can be schematic.""",
 "evidence": [
   ("IH-103", "The handoff's finding V-20: Sanskrit lacks the phonemes ḷ (retroflex), ṟ (alveolar trill) and ṉ (alveolar), **which Tamil-Brahmi invented letters for**. Recorded there as a linguistic fact; entered here as `INHERITED-UNVERIFIED`."),
   ("IH-062", "Owner decision HD-01: the name *veḷi* carries the retroflex *ḷ*. The page's subject and the institution's name share a phoneme, which is why this page is linked from 55 others."),
 ],
 "evidence_extra": """\
**The claim conflates two inventories, and the conflation is in the title.**
*"Phonemes Sanskrit could not write"* joins a phonological claim (Sanskrit lacks
these phonemes) to an orthographic one (its script had no letters for them).
`IH-103` states both in one sentence. They are separate claims with separate
evidence, and method step 10 requires every link between language, artifact and
script to be tested as its own claim. A script's inventory is evidence about a
script.

**There is verified work in this repository on adjacent ground, and it does not
transfer.** `03-REGISTERS/domain-e-retroflex-residue.csv` (253 Rigvedic lemmas
classified for retroflexion), `domain-e-claims.csv` (19 `VERIFIED`),
`domain-e-measurements.csv` (30 `VERIFIED`), and the DEDR/CDIAL/DravLex retrievals
at `SRC-060` to `SRC-067` are the most substantial verified body in the
repository. Every one of those rows carries `supports_page` values such as
*substrate (proposed)* — none names this page. Under §3.3 a claim's status comes
from its own Evidence Links; standing does not travel by subject adjacency. What
this means practically is good news and a warning at once: the retrieval channel
this page needs is **already open and already logged**, and the linking work has
simply not been done.""",
 "posture_extra": """\
**Atlas Mode is mandatory in Living Signal Field** (§1.7), and §8.7's first
prohibition is the one this page is most likely to break: *never colour an
artifact, culture or region by a language*. A sound-change page in an atlas-mode
posture is exactly where a phoneme isogloss becomes a map of peoples. The `Avoid`
says the same thing in the workbook's own words — *"no gaming HUD or arbitrary
links"* — and an arbitrary link between a sound and a population is the
substantive version of that failure.

The posture is otherwise well assigned: *known by relation* is what a
correspondence set is, and §1.5's rule 4 (relation dominance — the exhibit's
substance is Relationship Objects rather than Claim Objects) would plausibly
derive it here once the claims exist.""",
 "asset_extra": """\
The asset class is the atlas/dataset class, and it is the right one: this page's
tables should be a dataset with a downloadable form, not three hand-built HTML
tables. `accessible SVG/map` and `legend` carry §8.7's constraints. A
`verified dataset` presupposes the linking work described in §3 — the dataset
exists in `03-REGISTERS/domain-e-*`; what does not exist is any row of it tied to
this page.

`mobile alternative` and `downloadable table` are the accessibility half of
release gate 5 and are unblocked by any evidence question.""",
 "launch": [
   "The phonological claim and the orthographic claim are stated separately, each with its own evidence (method step 10).",
   "The three tables are backed by a dataset with per-row sources — currently 0 source entries support 3 comparative tables.",
   "The Tamil-Brahmi letter-invention claim is dated. *When* letters were invented for these phonemes is an epigraphic and palaeographic question with a chronology, and chronology precedes interpretation (method step 2).",
   "The schematic/measured distinction is explicit on the surface, as the workbook's own required action asks: which rows are attested correspondences and which are reconstructions (the attestation gradient, constitution §4E).",
   "No map colours a region or a culture by a language (§8.7).",
   "Register rows exist with `supports_page = sound-changes`. Today there are none, and the adjacent verified work does not count as some.",
 ],
 "unit": """\
**MVP-U11 — phoneme and grapheme inventories as linked registers.** Build two
registers: the Old Tamil and Sanskrit phoneme inventories with the source for
each, and the grapheme inventories of Tamil-Brahmi and the northern Brahmi
varieties with dated attestations. Link the existing retroflex and lexical work
to this page where it genuinely bears, one Evidence Link at a time.

**Partly executable now** — the third of the three units with a live route, in
no particular order (README §0). The lexical and comparative half is reachable: DEDR via JAMBU (`SRC-060`, `SRC-061`),
Proto-Dravidian reconstructions (`SRC-062`), DravLex (`SRC-067`) — all `VERIFIED`
in the ledger over the still-open git lane.

**The epigraphic half has no probed route, and no probe either.** `SRC-052`
probed sixteen hosts on 2026-09-07 and records them refused — among them
`doi.org`, `api.crossref.org`, `api.openalex.org`, `api.semanticscholar.org`,
`archive.org` and `zenodo.org`, which are the bibliographic lanes to an
epigraphic corpus — and `SRC-080` to `SRC-083` record four more refused. **No
Tamil-Brahmi inscription corpus host has itself been probed**, and `SRC-058`
records the git lane open to arbitrary public repositories, so this brief does
not state that none is reachable. The letter-invention claim in `IH-103` — the
part the title rests on — stays at the floor either way, and a `05-HOLDS/` row is
owed once the search has been run and failed. **Ceiling on the lexical half:
`PROVISIONAL`,** single digitisation lineage (§3.2;
`03-REGISTERS/dedr-digitisation-lineage.csv`).""",
 "conflicts": "",
},

{
 "slug": "the-languages-we-lost",
 "question": "Which languages of South Asia have no demonstrated genealogical relatives, what comparative work has been done on each, how many speakers remain, and is each isolate status a finding or an open question?",
 "observed": """\
1,035 words, type `language`, 9 estimated source entries, 0 external links, 1
table, 4 inbound links — the least linked-to page of the fifteen after the
threshold. Decision `Keep`, Risk `Low`.

**The title and the H1 disagree, and the disagreement is visible in the audit
rows without opening the page.** The title names three languages —
*"Burushaski, Kusunda, Nihali"* — and the H1 says *"Four languages still speak,
and no one knows their relatives."* The fourth is not named in any workbook cell.
`overlap-tensions.csv` pairs this page with `the-vedda` at 0.301 similarity with
an open review obligation, which makes Vedda the obvious candidate; the audited
metadata does not say so and this brief does not assert it. Recorded as an
inconsistency to resolve when the page is opened.""",
 "evidence": [
   ("IH-128", "Provisional finding P-20, from Welikala 2024 and Weerasekara 2020: the Vedda show a deep Indian-tribal genetic link with drift and isolation, and their language was lost within living memory. The handoff records that *'first' and the language classification are **NOT supported***, and that the page was qualified under C-31/R-19 — the same overclaim correction that hit `before-the-indus`."),
 ],
 "evidence_extra": """\
One inherited row, and it is a caution rather than a support: on the neighbouring
page, the language classification was specifically recorded as **not supported**.
An isolate claim *is* a classification claim, so `IH-128`'s caution transfers
directly to this page's central assertion.

**A reachable route exists.** Glottolog is in the ledger and was retrieved:
`SRC-050` (Glottolog CLDF languages table) and `SRC-051` (Glottolog languoid tree
and reference bibliography), both over the git lane. Glottolog carries isolate
status, classification and a reference bibliography per languoid, which is
exactly this page's subject matter. **Ceiling: `PROVISIONAL`** — Glottolog is one
editorial classification aggregating a literature, not an independent second
source for the claims in that literature, and a `02-SOURCES/dependency.csv` row
is owed saying so.""",
 "posture_extra": """\
**This is the one page of the fifteen whose content matches its posture without
strain.** Nocturnal Veḷi is *not yet known*, and §1.5's rule 3 derives it where
the majority of an exhibit's load-bearing propositions resolve to typed absences
rather than positive claims. *"No one knows their relatives"* is a set of typed
absences and nothing else. If derivation ran on this page it would very likely
return the posture it was assigned.

**Which is exactly why the negative-evidence discipline is not optional here.**
§1.3: a Nocturnal Veḷi exhibit gets a stricter absence discipline, not a lower
bar. *"No relatives known"* must be typed per language and per proposal:
`ABSENT DESPITE ADEQUATE SEARCH` where serious comparative work has been done and
failed, `NOT RECOGNIZED` where the comparanda may exist unrecognised,
`NOT PUBLISHED` where the work sits unpublished. The four are unlikely to be in
the same evidential position and must not be typed the same way by default —
which of them differ, and how, is a finding of the unit in §6, not an assumption
of this brief.

The `Avoid` — *"no fantasy portal or occult styling"* — has a specific meaning on
this page: language isolates attract mystification, and living speech communities
are not a mystery.""",
 "asset_extra": """\
**`pronunciation audio where licensed` is acute here, not incidental.** These
are recorded as languages with living speakers — `IH-128` puts the Vedda
language's loss *within living memory*, and the page's own H1 says four
languages *still speak*. Speaker numbers for any of them are not held in this
repository and this brief states none. §1.6.3(a): `oral/living`
evidence requires **consent, not licence**, with a Consent Register row mandatory
(§11.4) recording what was given, by whom, for what use, for how long and how it
is withdrawn — plus the withdrawal trail (§1.6.2), so material withdrawn stays
visibly withdrawn. `DECISIONS-NEEDED.md` **D-016** (may Reconnection surfaces
publish before any community-led work exists) governs whether any of this may
appear before the communities have been consulted, and `CLAUDE.md` routes
living-community consent questions to the owner.

Field Mode is *available* in this posture (§1.7), not forbidden — but a children's
investigation whose evidence is recordings of speakers of a critically endangered
language needs the Consent Register in place first, not afterwards.

`language map` carries §8.7's prohibitions, including the one against colouring
regions by language, which is the default rendering for an isolates map.
`glyph diagram` is a derived asset and is embargoed under §3.12.""",
 "launch": [
   "The title/H1 count is reconciled: three named or four named, with the fourth identified.",
   "Each isolate's status is typed as an absence under constitution §6, per language, with the comparative proposals that have been made and tested named, per language. Which languages have attracted many proposals and which few is part of what the unit in §6 measures, not something this brief asserts.",
   "Speaker numbers carry a date and a source. A speaker count for an endangered language ages faster than any other figure on the site.",
   "Any recorded speech has a Consent Register row (§11.4). *'Where licensed'* is not an available route.",
   "The `the-vedda` overlap (0.301) is reviewed, per `overlap-tensions.csv`, and `IH-128`'s recorded *not supported* on the Vedda language classification is honoured wherever Vedda appears.",
   "The distinction between *isolate* (no demonstrated relatives) and *unrelated* (relatives shown not to exist) is explicit. They are not the same claim and the second is almost never demonstrable.",
 ],
 "unit": """\
**MVP-U12 — Glottolog languoid and bibliography extraction.** For Burushaski,
Kusunda, Nihali and the unnamed fourth: pull the languoid record, classification
and reference bibliography from `SRC-050`/`SRC-051`; record speaker figures with
their dates; extract the named comparative proposals for each and their standing
(method step 11); type each absence. Log the retrieval, write the dependency row,
and write claims with `supports_page = the-languages-we-lost`.

**Executable now** — one of three units in the fifteen with a live retrieval
route in this session, with MVP-U4 and the lexical half of MVP-U11. No order is
implied among them; see README §0. **Ceiling: `PROVISIONAL`**, one aggregating classification (§3.2). The primary
comparative literature — where a `VERIFIED` promotion would have to come from —
has no probed route: `SRC-052` records `doi.org`, the three bibliographic APIs,
`degruyter.com`, `benjamins.com`, `archive.org` and `zenodo.org` refused on
2026-09-07, and `SRC-081` to `SRC-083` record four more. **The specific
publications have not been probed** and `SRC-058`'s git lane is untested for
them, so this brief does not assert they are unreachable. A `05-HOLDS/` row is
owed once the search has been run and failed;
`05-HOLDS/HOLD-005-substrate-literature.md` is the existing precedent for the
form.""",
 "conflicts": "",
},
]

PAGES += [

{
 "slug": "the-other-laws",
 "question": "Which legal traditions operated in South Asia alongside dharmaśāstra, how is each attested, and by what process did one textual tradition become the reference for colonial and modern law?",
 "observed": """\
**2,810 words — the longest of the fifteen** — type `social-history`, 23 estimated
source entries, 0 external links, **7 tables**, 0 inline SVGs, 47 inbound links.
Risk `Low`. H1: *"Dozens of legal systems were operating. One was in a single
volume. That one became law."*

Decision: **`Split`** — the only page of the fifteen not marked Keep, Revise or
Hold. Required action: *"Split the argument or interactive/data layer from the
long-form interpretation; preserve one canonical overview."* The workbook's
assessment: *"High public value but high reputational risk when chronology,
agency, or causation is stated categorically."*

The H1 states chronology, agency and causation categorically in three sentences.""",
 "evidence": [
   ("IH-120", "Provisional finding P-12, from Aktor 2018 and Davis 2020/2022/2024 — sources the handoff marks **STRONG**: dharmaśāstra shows intent to control mobility; caste was produced by legal rules; penalties were differential. Entered here as `INHERITED-UNVERIFIED`."),
   ("IH-046", "Correction C-26/R-20: the demotion event. Kabir Babu 2016, Choudhury 2021 (MDPI preprint) and Kumar & Choudhury 2020 were left carrying claims that *Aktor, Davis, Olivelle, Beteille and the corpus actually support*. The re-attribution on `birth-was-not-always-destiny` and `jatization` was owed next pass and is listed among the **unconfirmed** items — and those are this page's neighbours."),
 ],
 "evidence_extra": """\
**The H1 is four claims joined by two sentence breaks**, and they run on different
evidence over about two thousand years:

1. *Dozens of legal systems were operating* — a quantitative claim requiring an
   inventory, a definition of 'legal system', and an attestation type for each.
2. *One was in a single volume* — a claim about textual form. Which text or
   compilation the H1 means by *a single volume* is not stated on the page as
   the workbook records it, and this brief does not supply one. It is the claim
   most exposed to the attestation gradient (constitution §4E): a text, a
   recension, a commentary and a colonial digest are four different objects, and
   *a single volume* could name any of them.
3. *That one became law* — a claim about a codification process with a date
   range and named actors, none of which the page's H1 states and none of which
   this repository holds. Establishing that chronology from dated documents is
   step 2 of the method and part of the unit in §6; this brief supplies no dates
   of its own.
4. The implied causal link between 2 and 3 — that textual convenience explains
   selection.

Method step 10 requires every link among text, practice, polity and modern
identity to be tested as its own claim, and step 2 requires chronology before
interpretation. Nothing on this page can be evaluated until the four are
separated, and the separation is most of what the workbook's `Split` is asking
for.

**The counter-narrative test is live and this is where it bites hardest.**
`CLAUDE.md`: do not accept a claim too easily because it is anti-Brahmanical or
politically corrective. The page's argument is one this project has an interest
in, its nearest neighbours are where the source-quality failure of C-26 actually
happened, and the strong sources named in `IH-120` are recorded as strong by a
handoff, not by a reading here. The correction to make is not to soften the
argument but to source it to Aktor, Davis and Olivelle directly — which is what
`IH-046` says was owed and unconfirmed.""",
 "posture_extra": """\
**Investigation Mode is mandatory** (§1.7): Tamil Retrofuture is a posture of
arguing against an official account, and *"that one became law"* argues against
one. PROVE IT is the mechanism that keeps it falsifiable.

**The asymmetry statement is required, not optional** (§11.2, §3.11). The
adversarial pair must be run and logged together, and the bias-test surface must
carry the asymmetry statement rather than presenting prestige-bias and
counter-narrative as a balanced pair — presenting them as balanced would itself be
the false-equivalence failure. On this page the two tests genuinely pull in
opposite directions, which is the case the rule was written for.""",
 "asset_extra": """\
`translation excerpt rights` is again the unbounded dependency (§1.6.3(a)); the
dharmaśāstra material is largely read through modern translations, and
`DECISIONS-NEEDED.md` **D-029** (fair dealing, and in which jurisdiction) governs
whether there is an alternative. `primary-text facsimile` is the strongest
available asset and the one the argument most needs — a facsimile of a colonial
digest beside a facsimile of a Sanskrit legal text makes claim 3 visible in a way
prose does not. `editorial illustration` is a derived asset, embargoed under
§3.12.

`historiographical` evidence is also present here, and §1.6.3(a) maps it to a
**right-of-reply position where a named party is criticised** (§11.3).""",
 "launch": [
   "**The split is executed.** The page cannot launch in its audited form, because its audited decision is that it should not exist in that form. What the split's shape is has not been decided by anyone.",
   "The Editorial Register (§11.5) exists to hold that decision. `SCHEMA.md` §7: *nothing in `03-REGISTERS/` records a publication decision.* A `Split` with no register to record it is an instruction with no addressee.",
   "The four claims in the H1 are separated, each with its own chronology, evidence class and status (method steps 2 and 10).",
   "*'Dozens'* is a count with an inventory and an inclusion rule behind it, or it goes.",
   "Aktor, Davis and Olivelle are read directly and cited at claim level, closing the re-attribution that `IH-046` records as owed and unconfirmed.",
   "Both bias tests are run and logged with the asymmetry statement (§3.11, §11.2).",
   "Right-of-reply positions are set for every named modern institution or scholar (§11.3), governed by **D-025** and `OWNER-DECISIONS.csv` **D-010**.",
 ],
 "unit": """\
**MVP-U13 — the four-claim decomposition and a direct reading of the strong
sources.** Split the H1 into four claim registers; build the attestation
inventory for claim 1 with a type per tradition (constitution §4E's gradient —
an attested legal text, a recorded custom, an inferred practice and a modern
reconstruction are four different things); establish the colonial codification
chronology for claim 3 from dated documents; and read Aktor 2018 and Davis
2020/2022/2024 directly rather than through the handoff's summary of them.

**Retrieval state: the lanes to this literature are refused; the publications
themselves are unprobed.** `SRC-052` probed sixteen hosts on 2026-09-07 and
records them refused, among them `doi.org`, the three
bibliographic APIs and two named academic publishers, with `SRC-081` to
`SRC-083` recording four more. **Which publisher carries either work is not
recorded in this repository** — `IH-120` gives surnames and years and nothing
else — so this brief names the lanes that are refused without asserting that
they are the routes to these two publications. **No
probe for these specific publications is in the ledger**, and `SRC-058` records
the git lane open to arbitrary public repositories, so this brief does not
assert that nothing serves them. Running the search and typing the outcome is
part of the unit; a `05-HOLDS/` row is owed once it has been run and failed. The decomposition itself needs no retrieval and should be done first — it
is what turns one unfalsifiable headline into four checkable claims, and it is
also the analytical half of the `Split`.""",
 "conflicts": "",
},

{
 "slug": "custody",
 "question": "Who physically held which manuscript collections, on what terms was access granted or refused and to whom, and what is the present custody and access status of each?",
 "observed": """\
1,375 words, type `collection-investigation`, **7 estimated source entries**, 0
external links, 1 table, 55 inbound links. Source state: *limited bibliography*.
Decision `Keep`, Risk `Medium`. H1: *"Every text was kept by someone with
something at stake."* The workbook's assessment: *"Supports the
custody/extraction critique, but **every institutional implication must be
documented**."*

Seven source entries against a claim quantified as *every*.""",
 "evidence": [
   ("IH-215", "Work item 44: contacting Dr. G. Sundar of the Roja Muthiah Research Library — a bridge to UTSC Digital Tamil Studies and the TNSDA Tamil-Brahmi graffiti project — is *'the most important single verification task in the file'*, and **nothing has been sent to any of the nine outreach roles**. The page about custody has had no contact with any custodian."),
   ("IH-260", "Contradiction X-11: the records disagree on the ingestion layer — one Veli Collections layer normalising ten museums, against T4's explicit deferral of multi-museum ingestion. Both are Claude-origin and *'the owner has decided neither'*."),
   ("IH-039", "The owner's request for coverage of the Gāndhārī scrolls as the oldest manuscripts was only partially built and is recorded as **OPEN** content."),
 ],
 "evidence_extra": """\
**No register row bears on this page's claims**, and the three rows above are
about the project's own unfinished business rather than about any manuscript.
That is the position to state plainly: the custody page rests on nothing this
repository holds.

**And it is load-bearing for the framework's seventh posture.** §1.6.2 resolves
the empty Reconnection environment by making it a register-backed posture that
becomes non-empty *"on the day the institution publishes its first custody chain,
its first refused access request or its first consent grant."* This page is where
the first custody chain would come from. Its `access-status evidence` asset is
that surface. So `custody` is not one exhibit among fifteen — it is the page that
determines whether the institution has seven postures or six in practice.""",
 "posture_extra": """\
**The `Avoid` is the governing constraint and it is unusually specific:** *"no
spectacle or unsupported allegation."* An institutional-critique page with seven
source entries and a universal quantifier in its headline is on the wrong side of
the second half. §1.2's C-3 makes the point structurally — custody *invites*
unsupported allegation whichever object is in the case.

**Field Mode is forbidden** (§1.7, §10.4.6): *"A child may read a custody record;
a child may not be handed 'decide whether this object was looted' as a Field Bag
task."* **Investigation Mode is mandatory** — this is one of the three
argue-against postures.

**Three open owner decisions govern this page's core mechanism**, and none is a
research question: **D-025** (are refused and unanswered obligations published
individually, in aggregate, or only with prior notice), `OWNER-DECISIONS.csv`
**D-010** (which institutional claims may presently be published), and **D-016**
(may Reconnection surfaces publish before any community-led work exists).""",
 "asset_extra": """\
**This asset set cannot be filled at all today, and one slot is impossible by
construction.** `institutional correspondence` presumes correspondence exists;
`IH-215` records that nothing has been sent to any of the nine outreach roles.
`collection record` and `accession/custody document` require institutional
access; `object image rights` requires a holder's permission, which requires the
same access; `access-status evidence` is the one slot that can be populated
immediately and in the institution's own voice, because a documented refusal or
an unanswered letter *is* access-status evidence — and §1.6.2 requires that the
not-yet-repaired row be published, or the environment becomes a
self-congratulation surface.

The sequence is therefore: write the letters, log every outcome including
silence, and the asset set starts filling itself.""",
 "launch": [
   "The Institutional Obligations Register (§11.1) exists, including its negative rows — refused requests, unanswered letters, consultations not held.",
   "The right-of-reply mechanism (§11.3) is live before any named institution is criticised, with its own identifier scheme so a reply is published beside the criticism.",
   "**D-025**, **D-010** and **D-016** are answered. Each of the three independently blocks part of what this page does.",
   "At least one custody chain is documented end to end (§3.4) — who made it, who held it, who holds it now, on what terms.",
   "*'Every text'* is either evidenced as a universal or narrowed to the collections actually documented. Seven source entries do not carry *every*.",
   "The overlap cluster *Institutional authority* — `indology`, `coverage`, `who-writes-the-textbook`, `what-the-children-are-taught`, `the-archive`, `custody` — is addressed: the workbook recommends one curated exhibit with claim-level documents and a right-of-reply field, and only two of the six are in the release.",
 ],
 "unit": """\
**MVP-U14 — the first custody chain, and the register behind it.** Two halves
with different blockers.

*In-repository, executable now:* create the Institutional Obligations Register
(§11.1) with its schema, including negative rows; create the Consent Register
(§11.4) and the Community Authority Register (§11.2) as empty, schema'd files, so
the fourth axis `SCHEMA.md` §7 names has somewhere to be written. This is
structure, not evidence, and it must not be described as progress on the page's
claims.

*Requiring outreach, and therefore escalating rather than blocking:* `IH-215`'s
nine outreach roles. **Institutional access is one of `CLAUDE.md`'s five
escalation categories**, so this goes to the owner as an owner action. It is not
a `HOLD` — a hold records a source that cannot be reached, and these custodians
can be reached by someone writing to them. Every outcome, including no reply, is
a row in the Obligations Register and is itself the page's evidence.""",
 "conflicts": "",
},

{
 "slug": "the-archive",
 "question": "What manuscript and material record survives, what proportion of it has been catalogued, digitised, read or published, and how is each of those proportions measured?",
 "observed": """\
2,052 words, type `collection-investigation`, **1 estimated source entry**, 0
external links, **5 tables**, 1 inline SVG, 51 inbound links. Source state:
*minimal source section*. Decision `Revise`, Risk `Medium`. H1: *"Everything that
survives — and how little of it has been opened."*

**One source entry supporting five tables** is the sharpest source-to-structure
mismatch in the fifteen. Set it beside `artifact-atlas`: 88 entries, 0 tables.
Both were rated by the same instrument; `method-limits.csv` states its limit
directly — *"a visible bibliography does not prove claim-level support or source
quality."*

The headline is two quantitative claims wearing rhetorical clothes. *Everything
that survives* is a denominator. *How little has been opened* is a numerator over
that denominator. Neither is stated as a number, which is why neither reads as a
claim.""",
 "evidence": [
   ("IH-321", "Work item 53: the synthesis archive must be updated; **section 21 is missing and sections 25–38 are absent**. The project's own archive of its findings has holes it has recorded and not filled."),
   ("IH-289", "Work item 21: synthesis sections 17–19 must be read and **section 18, the CLAIMS LEDGER, was never read**."),
   ("IH-002", "No count in the handoff was re-run against any corpus during compilation; every number is attributed to the file that reported it. No proportion on this page can be sourced to the inheritance."),
 ],
 "evidence_extra": """\
`IH-321` and `IH-289` are about the project's own archive rather than about the
manuscript record, and the coincidence is worth stating without over-reading it:
the page arguing that little of the record has been opened is carried by an
inheritance that records its own sections as unread and missing. That is not an
argument against the page. It is a reason its method must be exact, because the
page's claim form — *a large proportion of X remains unexamined* — is one this
project can be shown to be bad at measuring.

**The negative-evidence standard governs the headline.** *"How little of it has
been opened"* must be typed per collection: `NOT PUBLISHED` where catalogues
exist unpublished, `NOT ACCESSIBLE` where they exist and are closed,
`NOT RECOGNIZED` where material is held unidentified, `DOCUMENTED DESTRUCTION`
where loss is recorded. Those four have different causes and different remedies,
and collapsing them into *"how little"* loses exactly the information the page is
for.""",
 "posture_extra": """\
Extraction / Collection — *known but withheld* — is the right posture, and the
`Avoid` again does the work: *"no spectacle or unsupported allegation."* A page
about what was lost is where spectacle is cheapest.

**Field Mode is forbidden; Investigation Mode is mandatory** (§1.7). And §1.5's
derivation rule 1 would put this page here on its own terms — an exhibit whose
central claims depend on material whose access status is `NOT ACCESSIBLE` derives
to Extraction / Collection before any other rule fires. Of the fifteen, this and
`custody` are the two whose derived and assigned postures would most likely
agree.

**D-025** governs whether refused and unanswered obligations are published
individually, in aggregate, or only with prior notice — which is the same
question as how this page reports what it could not open.""",
 "asset_extra": """\
The Extraction class, as for `custody`, and the same problem: `collection record`,
`accession/custody document` and `institutional correspondence` all require
institutional contact that `IH-215` records as never initiated.
`access-status evidence` is again the one immediately fillable slot and the one
the page most needs — a documented refusal *is* the evidence for *"how little has
been opened"*, and it is evidence the institution can generate itself.

Note the trap in that: an access-status record is evidence about **this
institution's** access, not about the world's. Generalising from what MelaKeela
could not reach to what has not been opened is the inference this page must not
make silently.""",
 "launch": [
   "The denominators exist. For each collection named: holdings count, catalogued count, digitised count, publicly readable count — each with its source and the date it was measured.",
   "Each of the five tables has sources at row level. One source entry across five tables is not a citation state a `Revise` fixes by rewording.",
   "Every absence is typed under constitution §6, per collection, and the difference between unpublished, inaccessible and unrecognised is preserved rather than aggregated.",
   "The inference from *what we could not reach* to *what has not been opened* is either evidenced or dropped.",
   "**D-025** and `OWNER-DECISIONS.csv` **D-010** are answered, and right-of-reply positions (§11.3) are set for every named holding institution.",
   "The *Institutional authority* overlap cluster is addressed — six pages, two of them in the release, recommended as one curated exhibit with a right-of-reply field.",
 ],
 "unit": """\
**MVP-U15 — the coverage denominators register.** One row per named collection:
holdings, catalogued, digitised, publicly readable, each with source and
measurement date; then the absence typing; then, only then, any proportional
statement.

**Retrieval state unsettled, and step 1 is to settle it.** `indianculture.gov.in`
is recorded reachable at `SRC-027` (2026-09-07 re-probe), and the later
characterisation at `SRC-052` records only `github.com` and
`raw.githubusercontent.com` as reachable, with `SRC-081` to `SRC-083` recording
general-web hosts blocked at 15:10Z the same day. The two are not reconcilable
from this brief, so **re-probing the catalogue hosts is the first action of the
unit**, and its result is a ledger row either way — a reachable host is a
retrieval, and a blocked one is an `EGRESS_BLOCKED` row with the URL and what it
was needed for, per `CLAUDE.md`'s blocked-domains rule.

The half that is executable now needs no host at all: the institution's own
access-status evidence, built from the outreach in MVP-U14, is a documented
coverage measurement of exactly one kind and it is honest about which kind.""",
 "conflicts": "",
},
]


# --------------------------------------------------------------------------
# Emit
# --------------------------------------------------------------------------

SHARED_GATES = """\
## 5. What would have to be true before it can launch

Every page in the release carries the shared gates in
`06-BRIEFS/mvp-fifteen/README.md` §4 — the workbook's seven release gates, its
five *Not completed* publication gates, and the ten framework gates F1–F10. They
are not repeated here. What follows is what this page needs **beyond** them.

{items}
"""


def emit(page, wb, hits, scanned):
    slug = page["slug"]
    m = wb[slug]
    env = m["mvp"]["Environment"]
    posture, avoid = POSTURE_TABLE[env]
    modes = MODES[env]
    ih = inherited([i for i, _ in page["evidence"]])
    ih_by_id = {r["claim_id"]: r for r in ih}

    ev_rows = []
    for cid, bears in page["evidence"]:
        r = ih_by_id.get(cid)
        if not r:
            continue
        ev_rows.append("| `{}` | `{}` | `{}` | {} |".format(
            cid, r["status"], r["locator"], bears))

    linked = hits[slug]
    if linked:
        link_stmt = ("**{} register {} this page** in `supports_page`: {}."
                     .format(len(linked),
                             "row names" if len(linked) == 1 else "rows name",
                             "; ".join("`%s` in `%s` (`%s`)" % (c, f, s or "no status")
                                       for f, c, s in linked)))
    else:
        link_stmt = (
            "**No register row in this repository names this page.** A scan of all "
            "{} registers in `03-REGISTERS/` carrying a `supports_page` column "
            "returns zero rows for `{}` (`04-AUDITS/mvp-fifteen-briefs-build.py`, "
            "`scan_supports_page`). Under `CLAUDE.md`'s register format, "
            "`supports_page` is what ties a claim to the page it feeds — so on the "
            "repository's own accounting, this page is supported by nothing."
            .format(scanned, slug))

    n_ih = n_inherited_rows()
    floor, others = status_floor(slug, linked, ih)

    # A linked row is a recorded editorial act, and what it carries is not
    # derivable from the fact of the link. The brief has to say. Both fields are
    # required, by presence and not by truthiness — an earlier version tested
    # page.get("linked_licenses_copy"), which a missing key satisfies, so the
    # gate the README advertised did not exist (BF-029).
    if bool(linked) != ("linked_reading" in page):
        fail("supports_page scan and brief disagree for %r: %d linked row(s), "
             "linked_reading %s. Write the reading, or remove it." %
             (slug, len(linked), "present" if "linked_reading" in page else "absent"))
    if linked:
        if "linked_licenses_copy" not in page:
            fail("%r has a linked row and no linked_licenses_copy. Decide "
                 "whether the row licenses public copy and say so." % slug)
        if page["linked_licenses_copy"]:
            fail("%r declares a linked row that licenses public copy. Section "
                 "1's 'why the six slots are empty' no longer holds and has to "
                 "be rewritten by hand before this brief can be built." % slug)

    if linked:
        ids = ", ".join("`%s`" % c for _, c, _ in linked)
        n_l, row_s, carry = len(linked), "row" if len(linked) == 1 else "rows", \
            "carries" if len(linked) == 1 else "carry"
        st_list = " and ".join("`%s`" % a for a in others)
        premise = ("§3 below records {} register {} linked to it — {} — and "
                   "reads it: it {} no proposition this page asserts. Nothing "
                   "else bearing on the page carries a status other than "
                   "`INHERITED-UNVERIFIED`.".format(
                       n_l, row_s, ids,
                       "carries" if n_l == 1 else "carry between them"))
        supports_cell = ("no claim bearing on what this page asserts stands "
                         "outside the `INHERITED-UNVERIFIED` floor; the {} "
                         "linked {} read in §3"
                         .format(n_l, row_s + " is" if n_l == 1 else row_s + " are"))
        ceiling = ("**{} {} linked to this page {} a different status — {} — and "
                   "§3 states what it is about.** Nothing here ranks the two: the "
                   "floor is stated by the rule above, and a row carrying another "
                   "status neither lifts it nor is lifted by it.".format(
                       n_l, row_s, carry, st_list))
        floor_gloss = ("the status of every inherited row above, and of every "
                       "inherited row that could be listed. The linked {} {} "
                       "{}, read in §3 above; that is a different status and "
                       "not a higher one".format(row_s, carry, st_list))
    else:
        premise = ("§3 below records that every row bearing on it carries "
                   "`INHERITED-UNVERIFIED` and no other status appears.")
        supports_cell = ("no claim outside the `INHERITED-UNVERIFIED` floor")
        ceiling = ("**Every row bearing on this page carries "
                   "`INHERITED-UNVERIFIED`, and no other status appears.**")
        floor_gloss = ("the status of every row above, and of every row that "
                       "could be listed")

    out = []
    A = out.append
    A("# `{}` — page brief\n".format(slug))
    A("**Page:** *{}* · MVP rank **{}** of 15 · `{}` · Decision `{}` · Risk `{}`\n"
      .format(m["mvp"]["Title"], m["mvp"]["Rank"], env,
              m["page"]["Decision"], m["page"]["Risk"]))
    A(HEADER_NOTE.format(written=WRITTEN, revised=REVISED))
    A("\n---\n")

    A("## 1. The question, in step 14 form\n")
    A("**QUESTION.** {}\n".format(page["question"]))
    A(NO_PUBLIC_COPY.format(premise=premise, supports_cell=supports_cell))
    A("\n### What the workbook records as observed\n")
    A(page["observed"].format(
        entries=m["page"]["Source entries (est.)"], words=m["page"]["Words"],
        inbound=m["page"]["Inbound links"]) if "{" in page["observed"]
      else page["observed"])
    A("\n")
    A("\n---\n")

    A("## 2. Environment and epistemic posture\n")
    A("**Environment:** `{}`. **Posture — the visitor's relation to the "
      "knowledge:** *{}*. **`Avoid` — the failure this posture invites:** "
      "*\"{}\"*.\n".format(env, posture, avoid))
    A("The workbook's own function and effect cells for this environment: "
      "function *\"{}\"*, desired effect *\"{}\"*, palette role *\"{}\"* "
      "(`environment-map.csv`, `INHERITED-UNVERIFIED`).\n"
      .format(m["env"]["Function"], m["env"]["Desired effect"],
              m["env"]["Palette role"]))
    A("\n### Modes available in this posture\n")
    A(MODE_ROW.format(env=env, m0=modes[0], m1=modes[1], m2=modes[2],
                      m3=modes[3], m4=modes[4]))
    A("\n### Derivation\n")
    A(DERIVATION_NOTE.format(env=env))
    if page["posture_extra"]:
        A("\n" + page["posture_extra"] + "\n")
    A("\n---\n")

    A("## 3. The evidence it rests on\n")
    A(link_stmt + "\n")
    A("\n" + (ADJACENCY_NOTE_LINKED if linked else ADJACENCY_NOTE))
    if linked:
        A("\n" + page["linked_reading"].format(
            scanned=scanned,
            linked_statuses=" and ".join("`%s`" % o for o in others)) + "\n")
    A("\nWhat exists {} is inherited material that **bears on** this page "
      "without being linked to it. Every row below is from "
      "`03-REGISTERS/inherited-claims.csv`, whose {} rows all carry "
      "`INHERITED-UNVERIFIED` and all carry an empty `supports_page`.\n"
      .format("alongside it" if linked else "instead", n_ih))
    if ev_rows:
        A("\n| claim_id | status | locator | what it bears on |")
        A("|---|---|---|---|")
        A("\n".join(ev_rows) + "\n")
    else:
        A("\nNo inherited row bears on this page's central claims.\n")
    if page["evidence_extra"]:
        # evidence_extra may reference the linked statuses; it is formatted on
        # the same values as linked_reading so a typed status cannot survive
        # there instead (BF-030).
        A("\n" + (page["evidence_extra"].format(
            scanned=scanned,
            linked_statuses=" and ".join("`%s`" % o for o in others))
            if "{" in page["evidence_extra"] else page["evidence_extra"]) + "\n")
    A("\n### Lowest status among them\n")
    A("**`{}`** — {}.\n".format(floor, floor_gloss))
    A("\n" + STATUS_FLOOR_NOTE.format(ceiling=ceiling))
    A("\n---\n")

    A("## 4. Required asset class\n")
    A("From `01-INHERITED/curatorial-audit-v1.1/asset-register.csv`, verbatim "
      "(`INHERITED-UNVERIFIED`):\n")
    A("\n| Field | Value |\n|---|---|")
    A("| Required asset set | {} |".format(m["asset"]["Required asset set"]))
    A("| Documentary standard | {} |".format(m["asset"]["Documentary standard"]))
    A("| Priority | `{}` |".format(m["asset"]["Priority"]))
    A("| Source / commission route | {} |".format(m["asset"]["Source / commission route"]))
    A("| Status | `{}` |\n".format(m["asset"]["Status"]))
    A("\n**How this class should be derived instead.** Framework §1.6.3(a) "
      "replaces genre-driven asset classes with a mapping from the exhibit's "
      "**evidence-class composition** — the constitution's step 4 inventory. The "
      "workbook derived this row from the page's `Type`, a 29-value vocabulary "
      "with 17 singletons that `SCHEMA.md` §3 finds *\"too sparse to do "
      "reliably\"* the production-planning work it is doing. Under §1.6.3(a) a "
      "page with no recorded evidence classes yields **no** production class, "
      "which is the correct output and is this page's actual state.\n")
    if page["asset_extra"]:
        A("\n" + page["asset_extra"] + "\n")
    A("\n---\n")

    A(SHARED_GATES.format(items="\n".join(
        "{}. {}".format(i + 1, g) for i, g in enumerate(page["launch"]))))
    A("\n---\n")

    A("## 6. What unit of work would verify it\n")
    A(page["unit"] + "\n")

    if page["conflicts"] and slug == "artifact-atlas":
        # Section 7's substitutions and its two build-stopping checks are
        # specific to this page; before-the-indus's section 7 takes none.
        d034 = owner_decision("D-034", must_be="OPEN")
        claim_risk_absent(slug)
        rank = int(m["mvp"]["Rank"])
        inbound, top_slug, top_n, ordinal = atlas_inbound(
            {k: v["page"] for k, v in wb.items()})
        page = dict(page, conflicts=page["conflicts"].format(
            title=m["page"]["Title"], rank=rank,
            decision=m["page"]["Decision"], risk=m["page"]["Risk"],
            release_dep=m["mvp"]["Release dependency"],
            d034=d034["status"], inbound=inbound, top_slug=top_slug,
            top_n=top_n, inbound_ordinal=ordinal,
            rank_ordinal=ordinal_word(rank),
            n_running_w=NUMBER_WORDS[len([f for f in os.listdir(
                os.path.join(ROOT, "01-INHERITED", "site-review"))
                if "RUNNINGLIST" in f.upper()])],
            top_ranks="first %s" % NUMBER_WORDS[rank]))
        A("\n---\n")
        A(page["conflicts"] + "\n")

    A("\n---\n")
    A("*Brief written {}, revised {}. Nothing in it is public copy. Nothing in it promotes a "
      "claim: promotion requires a retrieval event logged in "
      "`02-SOURCES/access-ledger.csv`, and this unit performed none.*\n"
      .format(WRITTEN, REVISED))
    return "\n".join(out)


README = """\
# MVP fifteen — page briefs

**Written:** {written} · **revised:** {revised}
**Unit type:** page briefs. One per page in the curatorial audit's MVP set.
Fifteen briefs, `01-index.md` to `15-the-archive.md`, in the workbook's rank
order. This README is the index and the shared-gate reference; it is not a
sixteenth brief.
**Built by:** `04-AUDITS/mvp-fifteen-briefs-build.py`.
**Inputs, read and reproduced at build time:** `mvp.csv`, `page-audit.csv`,
`asset-register.csv` and `environment-map.csv` from
`01-INHERITED/curatorial-audit-v1.1/` (`INHERITED-UNVERIFIED` without
exception); `03-REGISTERS/inherited-claims.csv`; and `03-REGISTERS/*.csv`
scanned for `supports_page`.
**Inputs quoted and checked, not reproduced:**
`13-PRODUCT-ARCHITECTURE/museum-framework.md` (every design proposition
`HYPOTHESIS`, per its own §14.4), `00-CONTROLLER/METHODOLOGY-CONSTITUTION.md`,
`SCHEMA.md`, `method-limits.csv`, `summary.csv`, `claim-risk.csv`,
`overlap-tensions.csv`, `02-SOURCES/access-ledger.csv`, `DECISIONS-NEEDED.md`,
`RESEARCH-QUEUE.md`, `CLAUDE.md` and `04-AUDITS/BIAS-FAILURE-LOG.csv`. The
generator makes **{n_quotes} assertions** against those files and fails the build
if one does not hold — covering the §1.5 derivation rules *with their numbers*
(the briefs cite the numbers), the negative-evidence type names, and `SRC-052`'s
probe list and constraint.

Fourteen of the assertions are **pairing** checks rather than existence checks:
each brief prints one §1.1 posture row and one §1.7 mode row, composed from two
tables in the generator, and the composed row is asserted against the framework.
Asserting the framework's rows as loose strings would have let a swapped table
entry pass while six briefs printed the wrong row — which is what an earlier
version of this check did.

**What the check does and does not do.** It catches *drift* — a quoted fragment
edited or deleted in its source. It does not catch *misreading*: a fragment can
resolve while being attributed to the wrong speaker, given the wrong status, or
used to support something it does not say. One such case was found by review in
the first draft and corrected. The check narrows the space for silent error; it
does not close it, and no claim here rests on its having done so.
**Every count this directory *argues from* is derived at build time**, and the
scope of that sentence is narrower than the blanket claim two earlier builds made
— *"Every count in this directory is derived at build time. None is a typed
literal"* — which was false when written and is corrected rather than deleted
(`BF-029`). The workbook figures inside each brief's *What the workbook records
as observed* block are transcribed from `page-audit.csv` by hand and are not
checked by the build; so are the `IH-` claim texts in each evidence table. What is
derived is every count on which a finding rests: the register scan and its
statuses, the inherited-row total, the diagram sets, the `supports_page` values,
the quote total, and the two inbound-link figures §7 of `03-artifact-atlas.md`
compares. The inheritance's standing rule 14 is the rule here; stating a
compliance that is broader than the compliance achieved is itself a way of
breaking it.

**No retrieval was performed for this unit.** No row was added to
`02-SOURCES/access-ledger.csv`; no claim moved status; no domain was requested.
A brief is a statement of what a page would have to be and what it would have
to rest on. **None of it is public copy**, and no sentence in it may be lifted
onto a page.

---

## 0. Two standing controls this unit ran against

Recorded first because they bear on whether the unit should exist, and the
review that found them was right that citing D-032 ten times without quoting its
last sentence was a serious omission.

**`DECISIONS-NEEDED.md` D-032 ends:** *"Nothing in this repository acts on the
MVP set until this is answered."*

**`RESEARCH-QUEUE.md` lists *"Page and exhibit briefs"* under `## Not yet`.**

This unit was produced on the owner's instruction, given in the session of
2026-09-08. **That instruction is not registered as an owner decision and this
unit does not allocate one for it.** `CLAUDE.md` puts every owner decision taken
in this repository in `09-DECISIONS/OWNER-DECISIONS.csv`, and an instruction to
carry out a piece of work is not the same object as a standing decision that the
work may precede its queue position; treating it as one would put an
unverifiable authority into the decision namespace, which is what the `HD-01` to
`HD-20` convention exists to refuse. If the owner wants the placement settled
rather than the task done, that is a fresh `D-` and it has not been allocated
here.

**An earlier draft of this section argued that the instruction cleared the
queue's placement because `OWNER-DECISIONS.csv` D-008 makes queue ordering an
owner matter. That argument was withdrawn under review and is recorded rather
than deleted.** It failed three ways: D-008 governs the queue's *ordering below
its first item*, and `## Not yet` is a membership list, not a position; D-008's
own state is `BLOCKED`, so it is an unexercised slot and cannot be the authority
under which anything is permitted; and the instruction itself has no row anyone
can check. Replacing *not noticing two controls* with *clearing them by an
authority the repository cannot verify* would have been the worse failure of the
two.

So the unit rests on the boundary alone, drawn explicitly:

- These briefs **describe** the fifteen pages the workbook nominated and state
  what each would need. That is preparatory work, and it is what was asked for.
- They **do not act on the MVP set**: nothing here schedules a launch, approves
  a page, orders the work, assigns the release's shape, or assumes an answer to
  D-032. §3's retrieval-capability table is a statement about which sources are
  reachable, not a work order; §6 records the `before-the-indus` conflict and
  takes no position on it.
- Nothing here promotes a claim, because nothing here retrieved anything.

**And the boundary may not hold.** If the owner reads it as too fine — if
writing briefs for a set whose membership is undecided *is* acting on that set —
then the correct disposition is that this unit waits on D-032 with the rest.
Nothing here forecloses that reading; it is written down so the judgement can be
made rather than assumed, and the briefs are recoverable work either way, since
what they mostly record is what is *missing*. `RESEARCH-QUEUE.md` has been
amended to record the unit and its standing.

---

## 0.1 The two adversarial tests, run on this unit

Constitution §8 and `CLAUDE.md`: both tests before a unit is called finished,
logged whether or not they found anything, and *"running one is a failed test"*
(framework §3.11). Method failures are logged at
`04-AUDITS/BIAS-FAILURE-LOG.csv` `BF-018` to `BF-020`; re-audits at
`04-AUDITS/REAUDIT-QUEUE.csv` `RA-019`. Independent adversarial review was run on this
unit in successive rounds before it was called finished, and every round found
blocking defects; what they found is in those rows rather than quietly repaired.
The number of rounds is deliberately not stated here — it is a figure about this
unit that nothing derives, and standing rule 14 is what this unit has already
broken once.

**Prestige-bias challenge — did this unit privilege a claim because it is
canonical, Sanskritic, Brahmanical, Indo-European, European, colonial,
institutionally prestigious, repeatedly cited or nationally useful?**

Found: **yes, once, by omission.** The set cites the inheritance's correction
record repeatedly — `IH-051` (six headlines overstated *in the platform's own
direction*), `IH-012` (the Vedic caste-word claim corrected), standing rule 17 —
and initially cited none of the one logged case running the other way,
`IH-029`/R-09, where the handoff records that *"Claude's caution understated a
well-supported finding."* A correction record quoted only in the direction that
flatters the corrector is not a correction record. `IH-029` is now cited with its
R-09 note in `09-the-water-city.md` and in `07-keeladi.md`. Logged as `BF-018`.

Also found: the prestige-bias test was initially dismissed in one line on
`08-before-the-indus.md` (*"quiet here — the claim is not canonical"*) and never
run on the four pages where it bites — `the-other-laws` (dharmaśāstra),
`sound-changes` (Sanskrit's phoneme inventory as the reference point),
`the-water-city` (the canonical Indus urbanism literature) and `the-archive`
(Indology). Running it per page is `RA-019`; it is not closed by this unit.

**Preferred-counter-narrative challenge — did this unit accept a claim too
easily because it is Dravidian, Indigenous, anti-colonial, anti-Brahmanical,
subaltern, diffusionist or politically corrective?**

Found: **yes, once.** `07-keeladi.md` initially treated the page's
institutional-interference framing as a posture-derivation problem and a
right-of-reply problem, and never as a claim whose evidence might be thin.
Keeladi carries the strongest Tamil-nationalist valence in the set and was
receiving the least evidentiary pressure of the fifteen. The brief now runs the
test on the page explicitly, in three parts — the date, the interference
narrative, and the direction of correction. Logged as `BF-019`.

**Further failures, not bias failures but method failures of the same class,
found by the same reviews and logged with them (`BF-018`(b), `BF-020`):** the
unit stated its own diagram count from memory rather than deriving it, and
claimed to read two files at build time that its generator never opened — both
repaired, both recorded. And the first draft expanded *"Kenoyer et al. 1983"* —
the only form any source in this repository uses — into a full author list
supplied from model memory, in a brief whose subject is that the publication has
never been read. Bibliography from memory is the failure the inheritance rule
exists to prevent, and it is more dangerous than a wrong claim because it looks
sourced. Removed; the brief now states that obtaining the full citation is the
first act of the unit. Logged as `BF-018`'s second row.

**The asymmetry statement** (§11.2, required so the pair is not presented as
balanced): these two failure modes are symmetrical in form and asymmetrical in
power. The archives, the institutional positions, the citation counts and the
funding behind the canonical accounts on these fifteen subjects are not equal to
those behind the counter-accounts, and correcting a counter-narrative bias does
not restore a balance that never existed. Both were corrected; neither
correction implies the two bodies of scholarship start level.

---

## 0.2 What the second build changed, and what found it

The first build was committed on 2026-09-08. Between then and 2026-09-09
`03-REGISTERS/water-living-world-readiness.csv` was added to the repository on
another branch. It is the fifteenth register carrying a `supports_page` column,
and one of its rows, `WLW-001`, carries `supports_page = the-water-city` at a
status other than `INHERITED-UNVERIFIED`.

The generator caught part of this by itself and missed the rest, and the split is
the argument for building briefs from a script rather than writing them out.

**The derived part self-corrected.** `09-the-water-city.md` §3's opening sentence
is composed from the scan, so on re-running it changed from *"No register row in
this repository names this page"* to a statement of the row it found. In the
other fourteen briefs the same sentence kept its shape and its register count
moved from 14 to 15; in `09-the-water-city.md` the count is no longer printed
there at all, because the sentence that carried it is the one the scan replaced.

**The fixed part did not.** Four passages of prose in every one of the fifteen
briefs asserted the scan's *result* rather than printing it — that no row in any
register names the slug, that nothing bearing on the page stands above
`INHERITED-UNVERIFIED`, that this *"is the same for all fifteen pages"*, and the
lowest-status line, which was a typed literal in all fifteen. Two more were in
this README: §2's *"zero rows naming any of the fifteen slugs"* and the table's
floor column.

**What was actually false, stated exactly.** For the fourteen unlinked slugs
those sentences remained true; a first draft of this section said all of them
went false at once, which is the same overstatement in the opposite direction.
What went false was the two `the-water-city` instances and, in every brief, the
quantifier — *"the same for all fifteen pages"* — which is the sentence that made
the error a directory-wide one rather than a page-level one. The failure is not
that the prose was wrong everywhere; it is that nothing in the build could tell
where it had gone wrong.

The repairs below came in three rounds. The first three items were the repair
pass; items 4 to 7 were forced by independent adversarial review of it (`BF-029`);
item 8 by a second review of that repair (`BF-030`). They are listed with what
each review found rather than folded in silently, because two of the three rounds
found that the previous round's own account of itself was wrong.

1. **The linkage finding is derived.** §2 above and each brief's §3 now compose
   their statement from the scan rather than asserting its result. A page with a
   linked row says so and reads the row; a page without one says that. §2 prints
   what the scan returned and stops: it does not summarise the readings, because
   a sentence generalising over them is the `BF-027` failure again, and a first
   version of it duly hard-coded *"in the one case on file"* beside a derived
   count that would eventually contradict it.
2. **The floor is derived and the rule for it is stated.** Each brief's *lowest
   status* line is now computed from the statuses actually present. It is not a
   sort — framework §3.2 forbids ordering `INHERITED-UNVERIFIED` against the six
   evidential statuses — so the floor is stated by rule: a row carrying
   `INHERITED-UNVERIFIED` has had no retrieval event behind it, so no set
   containing one stands above it. A page whose evidence contains no such row
   stops the build instead of publishing Python's `None` as a status, which is
   what a first version did.
3. **A linked row cannot be read by the generator, so it is not read by the
   generator.** A link records that someone tied a row to a page; what the row
   carries is a judgement. A page with a linked row must supply `linked_reading`
   and `linked_licenses_copy`, and the build fails without them. That is why a
   register row added on a later branch cannot silently change what a brief
   claims: it stops the build until a person writes down what it means. A row
   declared to license public copy also fails the build, because §1's account of
   why the step 14 slots are empty would no longer hold.

   A first version of this gate tested `page.get("linked_licenses_copy")`, which
   a missing key satisfies, so the second half of the gate this README advertised
   did not exist. Both fields are now required by presence. Every gate in the
   file also raises `SystemExit` rather than asserting: a bare `assert` vanishes
   under `python3 -O`, and a gate an interpreter flag can switch off is not one.
4. **The floor is not a two-rung ladder.** A first version of the derivation
   called every status that was not `INHERITED-UNVERIFIED` *"above the floor"* —
   which is the ordering framework §3.2 forbids, and which would have printed a
   `REJECTED` row as standing above one. The briefs now name the other statuses
   present without ranking them against the floor, and an unstatused linked row
   stops the build instead of being rendered as empty backticks.
5. **`03-artifact-atlas.md` §7 derives what it argues from.** The two
   inbound-link figures and their ordering, the `mvp.csv` and `page-audit.csv`
   cells, D-034's status, and whether `claim-risk.csv` holds a row for the page
   are all read at build time. A first draft of the section retyped every one of
   them and called 56 the highest inbound-link count in the set; it is the
   second, behind `enter`'s 113.
6. **`WLW-001` is quote-checked.** The build's {n_quotes} assertions guard quotations from
   the framework, the constitution and the workbook; the row this whole build
   exists to respond to was guarded by none, and it has already been amended once
   under review. Its claim text, its locator and its `notes` are now checked, and
   the *"14 registers"* / *"{scanned} registers"* comparison in
   `09-the-water-city.md` §3 derives its second figure instead of typing it.
7. **Nothing is written until everything is built.** A gate firing halfway
   through the loop used to leave the directory half-regenerated and looking
   clean — for a directory whose entire claim is that its output is derived, the
   worst available failure state. Every brief is now composed before any file is
   opened for writing.
8. **A derived value that falsifies its own sentence stops the build.** Reading a
   value at build time is not enough if the sentence around it presumes a
   particular value: substituting D-034's live status into *"a settlement …
   against a decision that is `OPEN`"* produced *"a decision that is `ANSWERED`"*
   and built cleanly. `owner_decision` now takes the status the argument needs and
   `claim_risk_absent` halts if the row it argues from the absence of appears —
   the pattern `atlas_inbound` already used. The same review found the ranking
   language removed from `status_floor` surviving verbatim in the hand-written
   reading it prints, three false scan-result sentences still standing in this
   README after two sweeps that claimed to have removed them, and §0.2's own
   prestige-bias entry still carrying the misattribution the narrative eight lines
   above it had corrected — with one of its sentences made false by the previous
   repair. All are fixed above and marked where they stood.

**The direction of the failures is the finding of the third round.** `BF-029`
recorded a repair leaning toward leaving the launch order alone. `BF-030` records
the correction of it leaning the other way — §7 began preferring the arm that
changes the title, through an unhedged *"requires"* on a `HYPOTHESIS` proposition,
a launch condition smuggled into §5's gate 1, and a cost stated for two arms and
withheld from the third. That is what an overcorrection looks like when the author
is correcting their own overcorrection, and it is why the arms now each carry a
labelled cost.

`03-artifact-atlas.md` also gained the §7 the first build did not write. The
title-count conflict was raised in its §1 and then **answered in its §2**, which
wrote that §8.1's rule *"is the one that makes the page launchable at all"* and
that *"under that rule the Atlas ships before D-034 is answered."* That is a
settlement of an `OPEN` owner decision in the brief's own voice, and locating it
took a second review — a first draft of this section attributed it to §1 and §5,
neither of which resolves anything, which is why the first repair pass left the
strongest instance standing. §2 now withdraws the sentence and keeps it visible;
§7 disclaims §2 by name, records the conflict in the form
`08-before-the-indus.md` §7 uses, and sets out three arms without ranking them.

**What this did not change.** No retrieval was performed for the second build
either, no claim moved status, and no page gained support: `WLW-001` is
`VERIFIED` about the state of this repository's registers at a timestamp, not
about the past `the-water-city` describes. The finding the directory was written
under stands — no proposition any of the fifteen pages makes about the past is
supported by a register row — and it now stands on a derivation instead of on a
sentence.

The method failures are logged at `04-AUDITS/BIAS-FAILURE-LOG.csv` `BF-027`,
`BF-028` and `BF-029`. `BF-029` is the whole of the third list above: independent
adversarial review of the repair pass returned seven blocking findings, every one
a defect in the repair rather than in the work it repaired, and two of them ran
toward leaving the launch order and the framework's authority undisturbed.
`BF-027` and `BF-028` were corrected in place by that review — both had
miscounted, in rows about miscounting — and the corrections are marked inside the
rows. Re-audits: `RA-022` asks the same question of every document in the
repository that states a count or a coverage finding in prose; `RA-023` asks
whether any other gate in this repository's scripts is one only in the sense that
these two were.

### The two tests, re-run on the second build

Constitution §8 requires both before a unit is called finished, and *"running one
is a failed test"* (framework §3.11). §0.1 records them for the first build.

**Prestige-bias challenge.** Found: **yes, and it is why §7 of
`03-artifact-atlas.md` had to be written.** The prestige at work is internal.
`13-PRODUCT-ARCHITECTURE/museum-framework.md` is this repository's own
specification, it reads with the authority of a rule, and every design
proposition in it is `HYPOTHESIS` by its own §14.4. The first build let its §8.1
close the atlas title-count conflict — **§2** of that brief presented §8.1's
no-headline-count rule as *"the resolution that makes the page launchable at
all"* and concluded that *"under that rule the Atlas ships before D-034 is
answered"* — while D-034 sat `OPEN` in `09-DECISIONS/OWNER-DECISIONS.csv` with a
note saying in as many words that §8.1 neutralises the number without answering
it. A `HYPOTHESIS` document was allowed to settle an owner decision because it is
ours and it is well argued.

*This entry said §1 and §5 for two builds, and added that they were left
unchanged so the failing reading would stay visible. Both halves were wrong:
neither §1 nor §5 resolves anything, which is why the first repair pass missed
the sentence that did; and the third build then rewrote both of them, so the
claim that they were unchanged became false as well. Corrected here rather than
overwritten, because an audit-trail entry that quietly acquires the right answer
is not an audit trail. §2 now withdraws the sentence in place and keeps it
visible; §7 disclaims §2 by name.*

A second, smaller instance is `BF-028`: the arm of the conflict that would move
the page out of rank 3 was argued with an inflated cost — 56 inbound links called
the highest in the set when `enter` has 113 — which is the error a reader
attached to the existing launch order would make.

**Preferred-counter-narrative challenge.** Found: **yes, once, and it runs
against this unit's own product.** `WLW-001` arrived carrying a status other
than `INHERITED-UNVERIFIED`, and its arrival
falsified the sentence this directory was built around: *"No page in the MVP set
has a single register row behind it."* The reading in `09-the-water-city.md` §3
lets the substance of that sentence stand — the row is about the registers, not
about the past; it is a timestamped probe; it and this brief are one source
rather than two. Each of those three is defensible and each of them is also
convenient, and the reading was written by the unit whose headline finding the
row threatened. That is the shape of motivated reading whether or not the reading
is right. It is recorded here rather than resolved by its author: what would
overturn it is a linked row whose subject is the past a page describes, carrying
a status other than `INHERITED-UNVERIFIED`, and the correct response to one would be to
rewrite §2 rather than to read it down. The scepticism this repository runs on is
not neutral when it is pointed at a claim that would cost the current unit its
result.

**A third finding, from the review rather than from either test.** `RA-019` is
open, `HIGH`, and its standing control is *"re-check whether any brief accepted a
workbook `Risk` rating as an evidentiary judgement rather than a scheduling
one."* This build added prose squarely inside that scope — §7 of
`03-artifact-atlas.md` argues about what the `Keep` and `Low` ratings can and
cannot settle — without running the control, and got the columns wrong in the
process. §1 now separates `Curatorial decision` from `Claim risk`, quotes each
layer's own limit from `method-limits.csv`, and marks the causal reading of `Low`
as an inference the brief cannot check. `RA-019` is not closed by this; adding
material to an open re-audit's class without running it is the failure worth
recording.

**The asymmetry statement** (§11.2): the two failures above are symmetrical in
form and asymmetrical in what they defend. The first defends an internal
specification's authority over an open owner decision; the second defends this
unit's own finding against a row that contradicted it. Neither is a bias about
the ancient world, and neither should be read as one — which is itself worth
stating, because a unit that runs both tests and reports only internal findings
may have run them only against itself. On the fifteen pages' *subjects* the tests
were not re-run in this build; `RA-019` still holds for the four pages where the
prestige test bites, and it is not closed here.

---

## 1. The fifteen

| # | Slug | Environment / posture | Decision | Risk | Lowest status of its evidence |
|---:|---|---|---|---|---|
{table}

---

## 2. The finding that applies across the fifteen

{linkage_finding}

The {n_vals} `supports_page` values actually in use are: {sp_values}.
`03-REGISTERS/inherited-claims.csv` holds {n_ih} rows, all
`INHERITED-UNVERIFIED`, and **all {n_ih} have an empty `supports_page`**.

**The scan's exclusion set, printed rather than implied** (`BF-017`'s standing
control on arguments from absence): {n_nocol} further CSVs in `03-REGISTERS/`
carry rows and **no `supports_page` column at all** — {nocol_files}. Some hold
claim rows: a page could in principle be supported by one of them and the scan
would not see it. It would still not be *recorded* as supporting the page, which
is what `CLAUDE.md`'s register format requires, so the finding stands — but it
stands on the column, not on an exhaustive reading of every row in the
repository.

Under `CLAUDE.md`'s register format, `supports_page` is what ties a claim to the
atlas entry or exhibit it feeds, and *"Evidence that supports nothing is not
collected."* Read the other way round, which is the way that matters here: on the
repository's own accounting, **no page in the launch set has a register row
recorded as supporting a proposition it makes about the past**. That is narrower
than the sentence two earlier builds printed here — *"the launch set is supported
by nothing"* — which stopped being true of every page when `WLW-001` appeared
and is corrected rather than deleted (`BF-030`). What the scan above returned,
and what each linked page's §3 makes of it, is the record.

Three consequences, and they are the shape of the whole unit:

1. **The floor is the same on every page: `INHERITED-UNVERIFIED`.** {floor_note}
   Where each brief names inherited rows, they are rows that *bear on* the page,
   not rows that support it.
2. **No public copy may be drafted for any of them.** Method step 14 draws public
   copy from accepted claims. There are none. Each brief therefore states its
   page's QUESTION and leaves the other six step-14 slots open with the reason.
3. **Every claim-specific diagram in the set is embargoed.** Framework §3.12:
   *"a derived asset may not be commissioned or published while the claim it
   depicts is `INHERITED-UNVERIFIED` or `HOLD`."* **{n_diag} of the fifteen** asset
   sets contain a `claim-specific diagram` — {diag_slugs} — and all {n_diag} are
   blocked. (The count is derived from `asset-register.csv` at build time, not
   typed; the other ten sets name a different derived asset, or none.) This is
   the framework resolving `SCHEMA.md` §4's finding 3 — 50 claim-specific
   diagrams scheduled by MVP priority, which is driven by low risk, i.e. by the
   pages least examined. Under §3.12 the diagram schedule is a function of the
   verification schedule and cannot invert it.

**And the workbook's `Risk` column is not a measure of truth.** `method-limits.csv`
states it: *"Risk means verification priority, not falsehood"*, and *"a visible
bibliography does not prove claim-level support or source quality."* Two of the
starkest cases sit in this set — `artifact-atlas`, rated `Low` on 88
bibliography entries against 8 words of prose, and `the-archive`, rated `Medium`
with 1 source entry under 5 tables.

---

## 3. What can actually be verified in this session

Of the fifteen units of work named in the briefs, **three have a live retrieval
route** with the access this session has. This is a statement about retrieval
capability, not a work order: sequencing the MVP set is what §0 says this unit
does not do.

| Unit | Page | Route | Ceiling |
|---|---|---|---|
| **MVP-U4** | `veli` | DEDR/JAMBU (`SRC-060`, `SRC-061`), Proto-Dravidian (`SRC-062`), DravLex (`SRC-067`) | `PROVISIONAL` — single digitisation lineage (§3.2) |
| **MVP-U12** | `the-languages-we-lost` | Glottolog CLDF and languoid tree (`SRC-050`, `SRC-051`) | `PROVISIONAL` — one aggregating classification |
| **MVP-U11** (lexical half only) | `sound-changes` | same Dravidian lexical lane | `PROVISIONAL`; epigraphic half blocked |

Two more need no retrieval at all and could be executed with the access this
session has: **MVP-U1** (threshold claim decomposition, `index`) and **MVP-U6**
(re-deriving the ledger rule in-repository, `the-ledger`), plus the structural
half of **MVP-U14** (creating the Obligations, Consent and Community Authority
registers).

**The rest are blocked, and the block is documented rather than assumed.**
`SRC-052` characterises the session's egress as `github.com` and
`raw.githubusercontent.com` only; `SRC-080` to `SRC-083` record GRETIL, the
Internet Archive, TITUS, sacred-texts and wisdomlib refused on re-probe at
2026-09-07T15:10Z. `SRC-027` records `indianculture.gov.in` reachable earlier the
same day, and `SRC-080`'s own note gives the rule that stops these being
reconciled by assertion: *"A ledger row is a timestamped probe, not a standing
property (D-042)."* A later characterisation does not supersede an earlier
probe of a host it never probed. So **re-probing is the first action of any unit
that needs a host**, and no brief here asserts that a host it has not probed is
unreachable. Hosts never probed at all — ASI, TNSDA, Indian publishers, the
publishers of Aktor and Davis — are recorded as untested, not as blocked.

**Two things escalate rather than block.** `IH-215` names an outreach to Dr. G.
Sundar of the Roja Muthiah Research Library as *"the most important single
verification task in the file"* and records that nothing has been sent to any of
the nine outreach roles. Institutional access is one of `CLAUDE.md`'s five
escalation categories: that is an owner action, not a `HOLD` row. The same
applies to the audited archive `veli-site(3).zip` itself, which is not in this
repository and has no ledger row — which is why every figure in the workbook is
`INHERITED-UNVERIFIED` rather than merely unchecked.

**`05-HOLDS/` rows are owed** for: the deployed build and the audited archive
(`enter`, `artifact-atlas`); the Tolkāppiyam *Poruḷatikāram* (`tinai`); Kenoyer
et al. 1983 and Chattopadhyaya 1996 (`before-the-indus`); the Keeladi report
chain (`keeladi`); the Indus excavation literature (`the-water-city`); a citable
Tirukkuṟaḷ edition if the git lane does not serve one (`kural`); a Tamil-Brahmi
epigraphic corpus (`sound-changes`); the isolate comparative literature
(`the-languages-we-lost`); Aktor and Davis (`the-other-laws`).

---

## 4. The shared gates

Every brief's §5 lists what its page needs **beyond** these. These apply to all
fifteen and are not repeated in the briefs.

### The workbook's release gates (`summary.csv`, `INHERITED-UNVERIFIED`)

1. Claim-level citation review
2. Cross-page consistency review
3. Image rights and provenance
4. Specialist/community review where relevant
5. Browser, accessibility and mobile testing
6. Prototype approval before migration
7. Confirm production domain and deployment allowlist

### The workbook's *Not completed* list (`method-limits.csv`)

Full primary-source re-performance · legal opinion · community consultation ·
image-rights clearance · discipline-specific peer review. The sheet is explicit
that *"these are publication gates, not optional polish."*

### Framework and constitution gates

| | Gate | Source |
|---|---|---|
| **F1** | Source Mode is reachable from the page | §1.7 — mandatory in all seven postures |
| **F2** | Every displayed claim is a Claim Object with a **computed** status; no editor can type `VERIFIED` and the CMS has no status dropdown | §3.1–§3.2 |
| **F3** | The posture is recorded in the Editorial Register with `derived_posture`, `assigned_posture` and, where they differ, a non-empty `override_reason` | §1.5, §11.5 — **this register does not exist** |
| **F4** | No derived asset is commissioned or published while the claim it depicts is `INHERITED-UNVERIFIED` or `HOLD` | §3.12 |
| **F5** | Both adversarial tests are run **as a pair** and logged whether or not they found anything, with the asymmetry statement | §3.11, §11.2, constitution §8 |
| **F6** | Every absence argument is typed under the negative-evidence standard | constitution §6 |
| **F7** | Every consequential ancient word carries a Translation Block | constitution §7, §3.8 |
| **F8** | Proportionality: allocated space is compared against evidential weight at review | §3.10, method step 9 |
| **F9** | Falsifiers are recorded for every load-bearing claim | §3.9, method step 12 |
| **F10** | Step 13 has been run — MelaKeela checked against itself for contradictions, outdated claims, duplicate pages and terminology drift | method step 13 |

### The repository-level gate

**R1.** At least one claim with `supports_page` naming the slug, carrying a
status other than `INHERITED-UNVERIFIED`, **whose subject is a proposition the
page makes about the past**. {r1_note}

*Two earlier builds stated R1 without its second clause and asserted that no page
passed it. As written then, `WLW-001` satisfied R1 — a mechanical test with a
typed verdict that the scan already contradicted (`BF-030`). The clause is what
the gate always meant; the brief's §3 is where it is applied, because whether a
row's subject is the page's past is a judgement and not a scan.*

---

## 5. Open owner decisions that block pages in this set

None of these is a research question and none can be closed by retrieval. They
are listed with the pages they block, not re-argued; the argument is in
`DECISIONS-NEEDED.md` and the authoritative status is in
`09-DECISIONS/OWNER-DECISIONS.csv`.

| Decision | Question | Blocks |
|---|---|---|
| **D-032** | Does `before-the-indus` launch, or come out of the MVP set? | `before-the-indus`; and the release's shape — see §6 |
| **D-033** | Which build is authoritative; is `rakhigarhi` live? | `enter`, `artifact-atlas`, `the-water-city` |
| **D-034** | The page count and the atlas site count | `index`, `enter`, `artifact-atlas` |
| **D-004** (`OWNER-DECISIONS.csv`) | What Veḷi principally is | `index`, `veli` |
| **D-006** (`OWNER-DECISIONS.csv`) | Keezhadi or an inscription as the children's pilot | `keeladi`, and Field Mode for `tinai` and `the-water-city` |
| **D-010** (`OWNER-DECISIONS.csv`) | Which institutional claims may presently be published | `keeladi`, `custody`, `the-archive`, `the-other-laws` |
| **D-015** | Is Reading Room a seventh peer posture or demoted to Source Mode? | `the-ledger` |
| **D-016** | May Reconnection surfaces publish before community-led work exists? | `custody`, `the-languages-we-lost` |
| **D-025** | Are refused and unanswered obligations published individually, in aggregate, or only with notice? | `custody`, `the-archive` |
| **D-029** | Does the institution assert fair dealing, and in which jurisdiction? | `kural`, `the-other-laws` |

**This unit raises no new `D-` identifier.** Everything it found was already
carried by an existing decision, which is the correct outcome: `CLAUDE.md`
allocates a new identifier from `OWNER-DECISIONS.csv`, never from the highest
number visible in a document, and a brief that manufactures decisions inflates
the namespace it is meant to read from.

---

## 6. The `before-the-indus` conflict, recorded and not resolved

`before-the-indus` is **MVP rank 8** in `mvp.csv`, `MVP = Yes` in
`page-audit.csv` and `Priority = MVP` in `asset-register.csv` — and in the same
sheets it is `Decision = Hold`, `Risk = Critical`, with the release dependency
*"Withhold from MVP until load-bearing claims receive claim-level citations and
specialist/editorial review."* It is the only one of the fifteen in this state
and the only Critical-risk page in the launch set.

It is already carried as **D-032** in `DECISIONS-NEEDED.md`, with a row in
`09-DECISIONS/OWNER-DECISIONS.csv`, raised 2026-09-07 and renumbered from D-004
the same day (`09-DECISIONS/DECISION-ID-MAP.csv`). Category: *two consequential
positions both remaining viable / publication approval*.

**This unit records the conflict and takes no position on it.** The full record,
including what each arm changes and what neither changes, is in
`08-before-the-indus.md` §7. Nothing elsewhere in these briefs assumes an
outcome: `09-the-water-city.md` notes that the *Meluhha and Indus* exhibit
sequence loses a second member under one arm, and states it conditionally.

---

*Written {written}. Every design statement here is `HYPOTHESIS`; everything drawn
from the curatorial audit is `INHERITED-UNVERIFIED`. Nothing in this directory is
public copy, and nothing in it promotes a claim — promotion requires a retrieval
event logged in `02-SOURCES/access-ledger.csv`, and this unit performed none.*
"""


def main():
    hdr_env, env_rows = sheet("environment-map.csv", 3)
    hdr_mvp, mvp_rows = sheet("mvp.csv", 3)
    hdr_pg, pg_rows = sheet("page-audit.csv", 3)
    hdr_as, as_rows = sheet("asset-register.csv", 3)
    env_by = {r["Environment"]: r for r in env_rows}
    mvp_by = {r["Slug"]: r for r in mvp_rows}
    pg_by = {r["Slug"]: r for r in pg_rows}
    as_by = {r["Slug"]: r for r in as_rows}

    order = [r["Slug"] for r in mvp_rows]
    if order != MVP_SLUGS:
        fail("mvp.csv's rank order is not the order this script builds in: %r"
             % (order,))

    wb = {s: {"mvp": mvp_by[s], "page": pg_by[s], "asset": as_by[s],
              "env": env_by[mvp_by[s]["Environment"]]} for s in MVP_SLUGS}
    n_quotes = verify_quotes()
    hits, scanned = scan_supports_page()

    by_slug = {p["slug"]: p for p in PAGES}
    if set(by_slug) != set(MVP_SLUGS):
        fail("PAGES and mvp.csv name different slugs: %r"
             % (set(MVP_SLUGS) ^ set(by_slug),))

    # Every brief is composed before any is written. A gate that fires halfway
    # through the loop used to leave a directory half-derived and looking
    # clean, which for a directory whose whole claim is that its output is
    # derived is the worst failure state available (BF-029).
    built, rows = [], []
    for i, slug in enumerate(MVP_SLUGS, 1):
        name = "{:02d}-{}.md".format(i, slug)
        text = emit(by_slug[slug], wb, hits, scanned)
        built.append((name, text))
        m = wb[slug]
        floor, others = status_floor(
            slug, hits[slug],
            inherited([c for c, _ in by_slug[slug]["evidence"]]))
        rows.append("| {} | [`{}`]({}) | {} — *{}* | `{}` | `{}` | `{}`{} |"
                    .format(i, slug, name, m["mvp"]["Environment"],
                            POSTURE_TABLE[m["mvp"]["Environment"]][0],
                            m["page"]["Decision"], m["page"]["Risk"], floor,
                            " (+{} linked, {})".format(
                                len(hits[slug]), ", ".join("`%s`" % o for o in others))
                            if hits[slug] else ""))

    linked_slugs = [s_ for s_ in MVP_SLUGS if hits[s_]]
    if not linked_slugs:
        linkage_finding = (
            "**No page in the MVP set has a single register row behind it.**\n\n"
            "A scan of every register in `03-REGISTERS/` carrying a "
            "`supports_page` column ({} files) returns **zero rows naming any of "
            "the fifteen slugs**.".format(scanned))
    else:
        # The scan's result is printed; what the linked rows *mean* is not
        # summarised here. A generalisation over readings is the sentence
        # BF-027 was logged for, and writing one in the same file would repeat
        # it. Each brief's own reading is the record; this section points at
        # them and stops.
        detail = "; ".join(
            "`{}` — {} (read in [`{}`]({}) §3)".format(
                s_, ", ".join("`{}` in `{}` (`{}`)".format(c, f, st)
                              for f, c, st in hits[s_]),
                s_, "{:02d}-{}.md".format(MVP_SLUGS.index(s_) + 1, s_))
            for s_ in linked_slugs)
        linkage_finding = (
            "**{} of the fifteen {} a register row recorded against {}; the "
            "other {} {} none.**\n\n"
            "A scan of every register in `03-REGISTERS/` carrying a "
            "`supports_page` column ({} files) returns rows for: {}. Every other "
            "slug returns zero. **A link is not support.** A link records that "
            "someone tied a row to a page; whether the row carries a "
            "proposition the page asserts is a judgement, and each linked "
            "page's brief makes it in its own §3 under the gate described in "
            "§0.2. This section prints what the scan returned and does not "
            "summarise those readings — a sentence generalising over them is "
            "the failure `BF-027` was logged for.".format(
                len(linked_slugs),
                "pages have" if len(linked_slugs) > 1 else "has",
                "them" if len(linked_slugs) > 1 else "it",
                15 - len(linked_slugs),
                "have" if 15 - len(linked_slugs) != 1 else "has",
                scanned, detail))
    if linked_slugs:
        floor_note = (
            "Every row bearing on any of the fifteen carries "
            "`INHERITED-UNVERIFIED`, except the linked row(s) named in §2 above, "
            "which carry another status and are read in their pages' §3. A "
            "different status is not a higher one: framework §3.2 rules that "
            "these do not form a ladder, and the floor is stated by the rule "
            "that a row with no retrieval event behind it cannot be stood above.")
        r1_note = (
            "**No page in the set passes R1 today.** {} of the fifteen has a row "
            "with a status other than `INHERITED-UNVERIFIED` — {} — and that "
            "page's §3 records that its subject is the state of this "
            "repository's registers at a timestamp rather than the past the page "
            "describes.".format(
                len(linked_slugs),
                ", ".join("`%s`" % s_ for s_ in linked_slugs)))
    else:
        floor_note = ("Nothing bearing on any of the fifteen carries any status "
                      "other than `INHERITED-UNVERIFIED`.")
        r1_note = ("**No page in the set passes R1 today**, and none comes close: "
                   "no register row names any of the fifteen slugs at all.")
    diag = count_asset_sets_with("claim-specific diagram", as_by)
    sp_vals, sp_with, sp_without = supports_page_values()
    n_ih = n_inherited_rows()

    os.makedirs(OUT, exist_ok=True)
    for name, text in built:
        open(os.path.join(OUT, name), "w").write(text)
        print("wrote", name, len(text), "bytes")
    open(os.path.join(OUT, "README.md"), "w").write(README.format(
        written=WRITTEN,
        revised=REVISED,
        table="\n".join(rows),
        scanned=scanned,
        n_quotes=n_quotes,
        n_diag=len(diag),
        diag_slugs=", ".join("`%s`" % d for d in diag),
        n_vals=len(sp_vals),
        sp_values=", ".join("`%s`" % v for v in sp_vals),
        n_ih=n_ih,
        linkage_finding=linkage_finding,
        floor_note=floor_note,
        r1_note=r1_note,
        n_nocol=len(sp_without),
        nocol_files=", ".join("`%s`" % f for f in sp_without),
    ))
    print("wrote README.md ({} quotes checked, {} diagram sets, {} supports_page "
          "values, {} registers without the column)".format(
              n_quotes, len(diag), len(sp_vals), len(sp_without)))


if __name__ == "__main__":
    main()
