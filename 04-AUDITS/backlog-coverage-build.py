#!/usr/bin/env python3
"""Build 06-BACKLOG/BACKLOG-COVERAGE.csv.

Column set: 00-CONTROLLER/METHODOLOGY-CONSTITUTION.md section 10, in the
order that section lists, sixteen columns.

One row per numbered item 1-89 plus one row per unnumbered programme, the
programmes placed between items 65 and 66 as they are in the original.

Fill policy, so that no cell asserts more than its source supports:

  title                    parsed out of 06-BACKLOG/BACKLOG-v2-ITEMS.md, so
                           the CSV cannot drift from the recovered titles.
  current_site_coverage    the instructed source, 06-BRIEFS/SITE-INVENTORY.md,
                           does not exist in this repository. Recorded as not
                           established rather than inferred from any other
                           artefact. See 06-BACKLOG/README.md.
  existing_route           same. No route inventory is present.
  prior_research_available computed here, by the declared keyword map below,
                           over 03-REGISTERS/ only. Reports where material
                           bearing on an item sits; asserts nothing about
                           what that material shows. Every inherited-claims
                           row counted is INHERITED-UNVERIFIED.
  status, owner_decision   left empty. The owner's, not this script's.
  the remaining columns    left empty. Deriving research_required,
                           product_spec_required, the two dependency columns,
                           proposed_destination, release or final_zip_location
                           from a bare title would be invention, and the
                           full original item text is outstanding.

The keyword map is deliberately conservative: an item is credited only where
a register's own subject matter matches the item's own title. It is not
driven by EXPANSION-PROMPT-2026-09-07.md, whose per-item prose is
INHERITED-UNVERIFIED and would otherwise decide these cells by assertion.

Run from the repository root:  python3 04-AUDITS/backlog-coverage-build.py
"""

import csv
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COLUMNS = [
    "backlog_id", "title", "current_site_coverage", "current_prompt_coverage",
    "prior_research_available", "research_required", "product_spec_required",
    "technical_dependency", "institutional_dependency", "existing_route",
    "proposed_destination", "release", "status", "reason", "final_zip_location",
]
# section 10 lists owner_decision between reason and final_zip_location
COLUMNS.insert(COLUMNS.index("final_zip_location"), "owner_decision")

SITE_COVERAGE = ("NOT ESTABLISHED — 06-BRIEFS/SITE-INVENTORY.md, the instructed "
                 "source, does not exist in this repository; coverage not inferred "
                 "from any other artefact (06-BACKLOG/README.md)")
ROUTE = ("NOT ESTABLISHED — no route inventory in this repository "
         "(06-BACKLOG/README.md)")
PROMPT_COVERAGE = ("TITLE ONLY — 06-BACKLOG/BACKLOG-v2-ITEMS.md. Full original item "
                   "text outstanding. Expansion prose in "
                   "06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md is INHERITED-UNVERIFIED "
                   "and is not the original text")

# item number -> regex matched against the claim and notes fields of
# 03-REGISTERS/inherited-claims.csv. Subject-matter match to the item title.
INHERITED_MAP = {
    1:  r"",           # every row bears on item 1; handled as a special case
    # item 2: disagreements between figures, and the figures themselves. Not
    # every row that happens to say "pages" — that matched file listings.
    2:  r"disagree|page count|site count|corpus total|word.?total|\bcounts?\b|"
        r"\btotals?\b|\broutes\b|\b96\b|\b105\b|\b108\b|\b133\b",
    11: r"\bIndus\b|Harapp|Mohenjo|Dholavira|\bseal\b|\bsign\b|\bscript\b",
    12: r"Avest|Iranian|Zara|BMAC|Oxus",
    14: r"Tamil|Sangam|Ca[nṅ]kam",
    15: r"P[āa]li|Prakrit|Jain|[śs]rama[nṇ]a|Buddh",
    16: r"A[sś]ok|Br[āa]hm[īi]|inscription|Keezhadi|Kodumanal|Adichanallur",
    18: r"excavat|stratigraph|Keezhadi|Kodumanal|Adichanallur|Arikamedu|Rakhigarhi|Harapp|Mohenjo|Dholavira",
    19: r"genetic|ancestr|haplogroup|\bDNA\b|endogam",
    33: r"\bchild|classroom|teacher",
    37: r"\bchild|classroom|teacher",
    42: r"governance|advis|editorial board",
    # item 44 is institutional funding policy. A bare "funding" also matches
    # rows about auditing a cited scholar's funding, which is item 1 and item 19
    # work, not this item's. "donor" is excluded: in this corpus it means
    # donor language, not a funder.
    44: r"funding taxonomy|funding architecture|funding source|SSHRC|Mitacs|"
        r"\bCMF\b|Canadian Heritage|donation|funder|philanthrop|"
        r"\bgrant(?:s|ing)?\b|sponsor",
    45: r"communit|consent|living knowledge",
    46: r"\brights\b|licen|copyright|custody",
}

# item number -> (register file, one-line description of what it holds)
REGISTER_MAP = {
    2:  [("03-REGISTERS/rigveda-pur-family.csv",
          "PUR-001 records a 39,832 / 39,833 pada discrepancy between two layers "
          "of one corpus — a live numerical inconsistency with its cause stated")],
    9:  [("03-REGISTERS/domain-e-hypothesis-eligibility.csv",
          "E-1 to E-4 gate Dravidian attestation, Proto-Dravidian reconstruction, "
          "accepted loans and the substrate residue as four separate things"),
         ("03-REGISTERS/domain-e-claims.csv", "domain E claim rows")],
    10: [("03-REGISTERS/domain-e-hypothesis-eligibility.csv",
          "E-1 records Brahui, Kurukh and Malto distribution and states it is a "
          "fact about the present and recorded past, not about the Rigvedic period"),
         ("05-HOLDS/HOLD-002-dedr-unreachable.md",
          "no Dravidian source was reachable; nothing about Dravidian is asserted "
          "at any status")],
    11: [("03-REGISTERS/domain-e-hypothesis-eligibility.csv",
          "E-8 to E-11 gate Para-Munda, the unidentified prefixing language, "
          "Masica's Language X and unattributed residue")],
    13: [("03-REGISTERS/domain-e-hypothesis-eligibility.csv",
          "E-2 gates Proto-Dravidian as a reconstruction, not an attested language"),
         ("03-REGISTERS/domain-e-retroflex-residue.csv",
          "253 Rigvedic lemmata classified by whether the regular retroflexion "
          "rules derive the marked segment — adjacent evidence, Indo-Aryan not "
          "Proto-Dravidian")],
    25: [("03-REGISTERS/domain-e-hydronyms.csv",
          "469 Rigvedic river-name occurrences with stanza, pada and stratum — "
          "place-and-time rows of the kind an atlas consumes")],
}

SPECIAL_1 = ("03-REGISTERS/inherited-claims.csv — all {n} rows, IH-001 to IH-{last}, "
             "every one INHERITED-UNVERIFIED and so every one within this item's "
             "scope; 04-AUDITS/REAUDIT-QUEUE.csv")


def parse_items():
    """Return [(kind, number_or_none, title, section)] from the recovered file."""
    path = os.path.join(ROOT, "06-BACKLOG", "BACKLOG-v2-ITEMS.md")
    text = open(path, encoding="utf-8").read()
    body = text.split("## Recovered content — exactly as supplied", 1)[1]
    items, section = [], ""
    for line in body.splitlines():
        line = line.rstrip()
        m_sec = re.match(r"^((?:I|V|X)[IVX]*)\. (.+)$", line)
        m_item = re.match(r"^(\d+)\. (.+)$", line)
        m_prog = re.match(r"^\* (Programme \d+) — (.+)$", line)
        if m_sec and not m_item:
            section = f"{m_sec.group(1)}. {m_sec.group(2)}"
        elif m_item:
            items.append(("item", int(m_item.group(1)), m_item.group(2), section))
        elif m_prog:
            items.append(("programme", m_prog.group(1), m_prog.group(2), ""))
    return items


def inherited_rows():
    path = os.path.join(ROOT, "03-REGISTERS", "inherited-claims.csv")
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def prior_research(number, rows):
    parts = []
    if number == 1:
        ids = sorted(r["claim_id"] for r in rows)
        parts.append(SPECIAL_1.format(n=len(rows), last=ids[-1].split("-")[1]))
    else:
        pattern = INHERITED_MAP.get(number)
        if pattern:
            hits = [r["claim_id"] for r in rows
                    if re.search(pattern, r["claim"], re.I)
                    or re.search(pattern, r.get("notes") or "", re.I)]
            if hits:
                noun = "row" if len(hits) == 1 else "rows"
                where = (hits[0] if len(hits) == 1
                         else f"first {hits[0]}, last {hits[-1]}")
                parts.append(
                    f"03-REGISTERS/inherited-claims.csv — {len(hits)} {noun} matched "
                    f"on subject by 04-AUDITS/backlog-coverage-build.py, all "
                    f"INHERITED-UNVERIFIED, {where}")
    for path, note in REGISTER_MAP.get(number, []):
        parts.append(f"{path} — {note}")
    if not parts:
        return "NONE IN 03-REGISTERS/"
    return "; ".join(parts)


def main():
    items = parse_items()
    rows = inherited_rows()
    numbers = [n for kind, n, _, _ in items if kind == "item"]
    assert numbers == list(range(1, 90)), f"expected items 1-89, got {len(numbers)}"
    progs = [i for i in items if i[0] == "programme"]
    assert len(progs) == 6, f"expected six programmes, got {len(progs)}"

    placement = ("Unnumbered in the original and placed between items 65 and 66. "
                 "Not item 90-95; does not extend the 1-89 numbering "
                 "(06-BACKLOG/BACKLOG-v2-ITEMS.md)")

    ordered = ([i for i in items if i[0] == "item" and i[1] <= 65]
               + progs
               + [i for i in items if i[0] == "item" and i[1] > 65])

    out = []
    for kind, number, title, section in ordered:
        if kind == "item":
            backlog_id = f"BL-{number:03d}"
            reason = f"Original section: {section}" if section else ""
            prior = prior_research(number, rows)
        else:
            backlog_id = "PROG-" + number.split()[1]
            title = f"{number} — {title}"
            reason = placement
            prior = "NONE IN 03-REGISTERS/"
        row = dict.fromkeys(COLUMNS, "")
        row.update({
            "backlog_id": backlog_id,
            "title": title,
            "current_site_coverage": SITE_COVERAGE,
            "current_prompt_coverage": PROMPT_COVERAGE,
            "prior_research_available": prior,
            "existing_route": ROUTE,
            "reason": reason,
        })
        out.append(row)

    dest = os.path.join(ROOT, "06-BACKLOG", "BACKLOG-COVERAGE.csv")
    with open(dest, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} rows -> {dest}")
    print("items 1-89 plus six programmes between 65 and 66")


if __name__ == "__main__":
    main()
