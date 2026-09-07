#!/usr/bin/env python3
"""
build-canonical-files.py — generate 00-CONTROLLER/CANONICAL-FILES.csv.

One function, one authoritative file. Where more than one file serves a
function, exactly one is CANONICAL and the others are typed:

  CANONICAL               the authority for this function
  HISTORICAL              a dated snapshot, true when written, not present state
  INHERITED               preserved prior-thread material, no evidentiary standing
  SUPERSEDED              replaced; canonical_for_function names the replacement
  PENDING-RECONCILIATION  two live files claim one function and no owner
                          decision has chosen between them. Named, not hidden.

`validated` is read by validate-registers.py and decides what it enforces:

  GATED         the validator fails the build on a defect in this file
  REPORTED      the validator reports findings but does not fail — used where
                failing would demand rewriting research to satisfy a schema
  NOT-VALIDATED prose, scripts, or inherited material the validator ignores

The classification table below is the assertion. The script's job is to
prove it is complete: every tracked path must appear exactly once, or the
build fails. A file cannot enter this repository without an authority.
"""
import hashlib
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import csvdialect  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "00-CONTROLLER" / "CANONICAL-FILES.csv"

FIELDS = ["file_id", "function", "path", "role", "canonical_for_function",
          "authority", "responsible_writer", "validated", "id_prefix",
          "evidence_gate_column", "notes"]

# (glob-or-path, function, role, canonical_for_function, authority,
#  responsible_writer, validated, id_prefix, gate_column, notes)
TABLE = [
 ("CLAUDE.md", "Operating controller (Claude Code)", "CANONICAL", "", "self; subordinate to CONTROLLER-RECONCILIATION.md", "director session", "NOT-VALIDATED", "", "",
  "Tool-specific. The audit's recommendation that it become a thin adapter over a tool-neutral governance document is not taken here; see CONTRADICTION-REGISTER.csv CR-014."),
 ("AGENTS.md", "Operating controller (Codex reviewer)", "CANONICAL", "", "mirrors CLAUDE.md", "director session", "NOT-VALIDATED", "", "", "Advisory unless Codex is the actor."),
 ("README.md", "Orientation", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", "Orientation only. Never an authority for status, counts or layout."),
 ("AI-AGENT-ROSTER.md", "AI agent roster and gate description", "CANONICAL", "", "PROGRAMME.md", "director session", "NOT-VALIDATED", "", "",
  "Renamed from README-TEAM.md. These are Claude subagents, not a human research team."),
 ("RESEARCH-QUEUE.md", "Active research order", "CANONICAL", "", "CLAUDE.md; D-008 open", "director session", "NOT-VALIDATED", "R-", "", "Append-only. Some completion counts were stale and are corrected in this pass."),
 ("DECISIONS-NEEDED.md", "Prose case for blocking owner decisions", "CANONICAL", "", "09-DECISIONS/README.md", "director session", "GATED", "", "",
  "Authoritative for the argument, never for identifiers or status; OWNER-DECISIONS.csv governs both. Allocates no D- number of its own."),
 ("00-CONTROLLER/METHODOLOGY-CONSTITUTION.md", "Research methodology", "CANONICAL", "", "owner, committed unchanged", "owner", "NOT-VALIDATED", "", "",
  "Its section 15 archive numbering (11- to 19-) does not survive as repository directories; reconciliation section 4."),
 ("00-CONTROLLER/CONTROLLER-RECONCILIATION.md", "Controller conflict resolution", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "C-", "",
  "C-1 to C-9 here collide by normalisation with inherited corrections C-01 to C-09. The leading zero is load-bearing; see CR-009."),
 ("00-CONTROLLER/RESEARCH-CONSTITUTION.md", "Inherited standing method rules", "INHERITED", "00-CONTROLLER/METHODOLOGY-CONSTITUTION.md", "reconciliation C-8", "not written here", "NOT-VALIDATED", "", "",
  "Verbatim copy of the handoff section 11. Nothing cites it as governing. Keeps the inherited D-NN spelling by design."),
 ("00-CONTROLLER/PROGRAMME.md", "Operating structure, lanes and gates", "CANONICAL", "", "CLAUDE.md; constitution", "director session", "NOT-VALIDATED", "", "", "Adds no rule of its own; every gate cites its source."),
 ("00-CONTROLLER/REPOSITORY-MAP.md", "Folder authority matrix", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", "Defines each canonical folder: authority, allowed contents, inputs, outputs, writer."),
 ("00-CONTROLLER/PATH-MIGRATION.csv", "Path crosswalk and move plan", "CANONICAL", "", "REPOSITORY-MAP.md", "04-AUDITS/build-path-migration.py", "GATED", "PM-", "",
  "Generated. Every current path, its destination, and the references that must move with it. Rows are never deleted: this is how an old-path reference resolves."),
 ("00-CONTROLLER/CANONICAL-FILES.csv", "Canonical file register", "CANONICAL", "", "self", "04-AUDITS/build-canonical-files.py", "GATED", "CF-", "",
  "Generated. Read by validate-registers.py to decide what it enforces."),
 ("00-CONTROLLER/CONTRADICTION-REGISTER.csv", "Control-plane contradictions", "CANONICAL", "", "self", "director session", "GATED", "CR-", "",
  "Conflicting controllers, statuses, counts, identifiers, route inventories and decisions. Distinct from 04-AUDITS/INTERNAL-CONTRADICTIONS.csv, which is the constitution's required register for contradictions in the EVIDENCE."),
 ("00-CONTROLLER/STATUS-DIMENSIONS.md", "Status dimension definitions", "CANONICAL", "", "CLAUDE.md status vocabulary", "director session", "NOT-VALIDATED", "", "",
  "The enumerations validate-registers.py enforces. evidence_status is the single evidence gate."),
 ("00-CONTROLLER/OVERRIDE-LOG.csv", "Validation gate overrides", "CANONICAL", "", "AI-AGENT-ROSTER.md", "whoever takes the override", "GATED", "OV-", "",
  "A push that fails validation requires a committed row here, with reason, actor, date, the exact failures waived, and an expiry."),
 ("00-CONTROLLER/MIGRATION-HOLDS.csv", "Rows not migrated", "CANONICAL", "", "self", "director session", "GATED", "MH-", "",
  "A row that cannot be migrated without changing its meaning is left unchanged and recorded here. Distinct from 05-HOLDS/, which holds claims blocked on source access."),
 ("01-INHERITED/*", "Prior-thread material", "INHERITED", "", "CLAUDE.md inheritance rule", "not written here", "NOT-VALIDATED", "IH-", "",
  "No evidentiary standing. Never rewritten, never cited as evidence."),
 ("01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST2.md", "Site review running list", "SUPERSEDED", "01-INHERITED/site-review/MELAKEELASITEREVIEWRUNNINGLIST.md", "RUNNING-LIST-RECONCILIATION.md", "not written here", "NOT-VALIDATED", "", "",
  "Version 10. The confusingly named file without the 2 is version 12 and supersedes it."),
 ("02-SOURCES/access-ledger.csv", "Source retrieval and access events", "CANONICAL", "", "CLAUDE.md", "retriever", "GATED", "SRC-", "",
  "access_status remains overloaded: it mixes record standing, retrieval events and supersession prose. superseded_by was added; the re-typing is an owner decision. CR-004."),
 ("02-SOURCES/dependency.csv", "Source dependency", "CANONICAL", "", "CLAUDE.md; reconciliation C-3 recommends CSV over the constitution's JSON", "source-genealogist", "GATED", "DEP-", "",
  "D-013 open. SOURCE-DEPENDENCY.json is not created; if a JSON consumer appears it is generated from this file, never hand-maintained beside it."),
 ("02-SOURCES/*.md", "Retrieval manifests and notes", "CANONICAL", "", "CLAUDE.md", "retriever", "NOT-VALIDATED", "", "", "Corpus manifests cite external and temporary paths, which are not repository links."),
 ("03-REGISTERS/claim-sources.csv", "Claim-to-source relation", "CANONICAL", "", "self", "04-AUDITS/build-claim-sources.py", "GATED", "CS-", "",
  "Generated. Authoritative for which sources a claim rests on and which of them are one independent observation. The inline source_id cell is a mirror the validator forces to agree."),
 ("03-REGISTERS/inherited-claims.csv", "Inherited claim inventory", "CANONICAL", "", "CLAUDE.md inheritance rule", "04-AUDITS/inherited-claims-extraction.py", "GATED", "IH-", "evidence_status",
  "Generated. Every row is INHERITED-UNVERIFIED by construction and the generator asserts it."),
 ("03-REGISTERS/domain-e-claims.csv", "Domain E claims", "CANONICAL", "", "CLAUDE.md register format", "director session", "GATED", "DME-", "evidence_status", ""),
 ("03-REGISTERS/domain-e-interpretations.csv", "Domain E interpretations", "CANONICAL", "", "PROGRAMME.md step 7", "director session", "GATED", "DE-I-", "evidence_status", "Kept separate from measurements so an interpretation cannot inherit a measurement's standing."),
 ("03-REGISTERS/domain-e-measurements.csv", "Domain E measurements", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "GATED", "DE-M-", "evidence_status", ""),
 ("03-REGISTERS/domain-m-brahui-position.csv", "Domain M claims", "CANONICAL", "", "CLAUDE.md register format", "director session", "GATED", "DMB-", "evidence_status", "Carries the repository's one SUPERSEDED claim row, retained under the correction-history rule."),
 ("03-REGISTERS/rigveda-pur-family.csv", "Rigvedic pur-family claims", "CANONICAL", "", "CLAUDE.md register format", "director session", "GATED", "PUR-", "evidence_status", ""),
 ("03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv", "Hypothesis eligibility (mandated name)", "PENDING-RECONCILIATION", "", "constitution section 9; D-036 / D-039 both open", "chronology-gate", "GATED", "HYP-E-", "evidence_status",
  "Two live eligibility registers, not mapped row for row. Neither is canonical until the owner answers. CR-006."),
 ("03-REGISTERS/domain-e-hypothesis-eligibility.csv", "Hypothesis eligibility (domain E)", "PENDING-RECONCILIATION", "", "constitution section 9; D-036 / D-039 both open", "chronology-gate", "GATED", "E-", "evidence_status",
  "See CR-006. Its gate vocabulary and the mandated file's YES/NO vocabulary are now both parsed into gate_verdict."),
 ("03-REGISTERS/CROSS-DOMAIN-BRIDGES.csv", "Cross-domain bridge tests", "CANONICAL", "", "constitution step 10", "director session", "REPORTED", "BR-E-", "",
  "Its verdict column is free prose in eight distinct forms. Not migrated to an enum: doing so would restate research findings. MH-001."),
 ("03-REGISTERS/domain-e-hydronyms.csv", "Rigvedic hydronym occurrences", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "GATED", "HYD-", "", "Data table. Rows are evidence for claims stated elsewhere, not claims."),
 ("03-REGISTERS/domain-e-retroflex-residue.csv", "Retroflex residue lemmas", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "GATED", "RES-", "", "Data table."),
 ("03-REGISTERS/domain-e-cdial-loan-candidates.csv", "CDIAL loan candidates", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "GATED", "DE-CAND-", "", "Data table."),
 ("03-REGISTERS/domain-e-cdial-attribution-stats.csv", "CDIAL attribution statistics", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "NOT-VALIDATED", "", "", "key/value summary table; no identifier or source column."),
 ("03-REGISTERS/domain-e-evidence-mass.csv", "Evidence mass by distinction", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "GATED", "EM-", "", "Data table."),
 ("03-REGISTERS/domain-e-geography.csv", "Dravidian geographic measures", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "GATED", "GEO-", "",
  "Data table with no source column; its sources are recorded in the method note. GATED so that its GEO- identifiers are checked for uniqueness and prefix: domain-e-measurements.csv cites GEO-MU-04 as a locator, and an identifier used as a locator must come from a register that is itself governed."),
 ("03-REGISTERS/rigveda-pur-family-occurrences.csv", "pur-family occurrences", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "GATED", "PUR-OCC-", "", "Data table."),
 ("03-REGISTERS/domain-e-draft-copy.md", "Domain E draft public copy", "CANONICAL", "", "constitution step 14", "museum-translator", "NOT-VALIDATED", "", "", "Draft only. Nothing here is published copy."),
 ("04-AUDITS/BIAS-FAILURE-LOG.csv", "Method failure log", "CANONICAL", "", "constitution section 9", "adversarial-reviewer", "GATED", "BF-", "", ""),
 ("04-AUDITS/REAUDIT-QUEUE.csv", "Work requiring re-audit", "CANONICAL", "", "constitution section 9", "adversarial-reviewer", "GATED", "RA-", "", "status and priority carried composite values; decomposed in this pass into blocked_by and priority_reason."),
 ("04-AUDITS/ARCHIVE-AND-POWER-AUDIT.csv", "Archive and power audit", "CANONICAL", "", "constitution step 6 and section 4.V", "historiography-auditor", "GATED", "APA-E-", "", ""),
 ("04-AUDITS/INTERNAL-CONTRADICTIONS.csv", "Contradictions in the evidence", "CANONICAL", "", "constitution section 9", "adversarial-reviewer", "GATED", "IC-E-", "",
  "Evidence contradictions only. Control-plane contradictions go to 00-CONTROLLER/CONTRADICTION-REGISTER.csv."),
 ("04-AUDITS/validate-registers.py", "Mechanical validation", "CANONICAL", "", "CLAUDE.md; PROGRAMME.md gates", "director session", "NOT-VALIDATED", "", "", "The gate. Weakening it to pass rows is not an available move."),
 ("04-AUDITS/csvdialect.py", "CSV dialect preservation", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", "Reads and rewrites registers without reformatting them."),
 ("04-AUDITS/gatevocab.py", "Eligibility gate vocabulary", "CANONICAL", "", "00-CONTROLLER/STATUS-DIMENSIONS.md", "director session", "NOT-VALIDATED", "", "",
  "The prose-to-gate_verdict parse, shared by the migration that wrote the column and the validator that checks it still agrees with its prose. One copy, so the two cannot drift."),
 ("04-AUDITS/independence.py", "Source independence computation", "CANONICAL", "", "CLAUDE.md source independence constraint", "director session", "NOT-VALIDATED", "", "",
  "Union-find over 02-SOURCES/dependency.csv, shared by the join generator and the validator. The validator re-derives independence_group rather than trusting the generated column, which review showed was hand-editable."),
 ("04-AUDITS/test-push-gate.py", "Push gate test suite", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "",
  "Proves the pre-push hook denies what its header claims. Every spelling found past the parser by adversarial review is kept as a regression case."),
 ("04-AUDITS/build-claim-sources.py", "Claim/source join generator", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", ""),
 ("04-AUDITS/build-path-migration.py", "Path migration generator", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", ""),
 ("04-AUDITS/build-canonical-files.py", "Canonical file register generator", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", ""),
 ("04-AUDITS/migrate-status-dimensions.py", "Status split migration", "HISTORICAL", "", "self", "director session", "NOT-VALIDATED", "", "",
  "One-shot, idempotent, committed so the migration is reproducible and reviewable. Not re-run in normal work."),
 ("04-AUDITS/backlog-coverage-build.py", "Backlog coverage generator", "CANONICAL", "", "06-BACKLOG/README.md", "director session", "NOT-VALIDATED", "", "", ""),
 ("04-AUDITS/inherited-claims-extraction.py", "Inherited claim generator", "CANONICAL", "", "CLAUDE.md inheritance rule", "director session", "NOT-VALIDATED", "", "", ""),
 ("04-AUDITS/identifier-normalisation-brief.md", "Identifier audit", "HISTORICAL", "00-CONTROLLER/CANONICAL-FILES.csv", "self", "not rewritten", "NOT-VALIDATED", "", "",
  "A dated snapshot. Its present-state inventory is superseded: four registers it lists as absent now exist, HOLD- runs to 005, and BL- is zero-padded. Keep as an audit record, not as present state. CR-011."),
 ("04-AUDITS/VALIDATOR-FINDINGS-2026-09-07.md", "Validator findings", "HISTORICAL", "04-AUDITS/VALIDATION-REPORT.md", "self", "not rewritten", "NOT-VALIDATED", "", "",
  "Reports 43 failures against an earlier tree; the tree had 53 before this pass. Superseded by the current run. CR-012."),
 ("04-AUDITS/MIGRATION-REPORT-2026-09-07.md", "Migration record", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "",
  "What the 2026-09-07 status and claim/source migration changed, and how each change was checked. Dated because it describes one migration, not present state."),
 ("04-AUDITS/VALIDATION-REPORT.md", "Current validator findings", "CANONICAL", "", "04-AUDITS/validate-registers.py", "the validator", "NOT-VALIDATED", "", "",
  "Generated by --report. Supersedes the hand-written VALIDATOR-FINDINGS-2026-09-07.md, which went stale and was then read as current (CR-012)."),
 ("04-AUDITS/test-validate-registers.py", "Validator defect suite", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "",
  "Injects defects into a throwaway clone and asserts the validator rejects each. A validator that has never been watched to fail proves nothing."),
 ("04-AUDITS/*.md", "Method notes", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "NOT-VALIDATED", "", "", "Reproducibility notes for the measurement scripts."),
 ("04-AUDITS/*.py", "Measurement scripts", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "NOT-VALIDATED", "", "", "Reproduce a measurement from a pinned corpus."),
 ("04-AUDITS/*.csv", "Measurement output", "CANONICAL", "", "PROGRAMME.md step 4", "corpus-analyst", "NOT-VALIDATED", "", "", "Script output, not a register."),
 ("05-HOLDS/*", "Claims blocked on source access", "CANONICAL", "", "CLAUDE.md", "retriever", "GATED", "HOLD-", "", "One file per hold. Runs to HOLD-005."),
 ("06-BACKLOG/BACKLOG-COVERAGE.csv", "Backlog coverage", "CANONICAL", "", "constitution section 10", "04-AUDITS/backlog-coverage-build.py", "REPORTED", "BL-|PROG-", "",
  "Generated. All 95 current_site_coverage and existing_route cells read NOT ESTABLISHED because the inventory was sought at a path in this repository; it exists in melakeela/site. CR-001."),
 ("06-BACKLOG/BACKLOG-v2-ITEMS.md", "Recovered backlog titles", "INHERITED", "", "CLAUDE.md inheritance rule", "not written here", "NOT-VALIDATED", "", "", "Titles only. A title is not a specification."),
 ("06-BACKLOG/EXPANSION-PROMPT-2026-09-07.md", "Backlog expansion prompt", "INHERITED", "", "CLAUDE.md inheritance rule", "not written here", "NOT-VALIDATED", "", "", "Model-written prose from the same recovery. Not the original backlog text."),
 ("06-BACKLOG/README.md", "Backlog directory guide", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", ""),
 ("06-BRIEFS/*", "Research briefs", "CANONICAL", "", "constitution step 14", "museum-translator", "NOT-VALIDATED", "", "",
  "Shares stage number 06 with 06-BACKLOG. A real namespace defect; the repair is that numbering leaves folder names, not that a number is invented. CR-007."),
 ("09-DECISIONS/OWNER-DECISIONS.csv", "Owner decisions", "CANONICAL", "", "CLAUDE.md one identifier namespace", "director session", "GATED", "D-", "",
  "Authoritative for the D- namespace and for each decision's status."),
 ("09-DECISIONS/DECISION-ID-MAP.csv", "Decision identifier aliases", "CANONICAL", "", "09-DECISIONS/README.md", "director session", "GATED", "", "",
  "Rows are never removed. Declares no id_prefix and is exempt from cross-register identifier uniqueness by design: it exists to hold D- identifiers issued elsewhere, so its old_id column repeating them is the point."),
 ("09-DECISIONS/README.md", "Decisions directory guide", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", "Its three-value status list is corrected in this pass; the register carries four."),
 ("13-PRODUCT-ARCHITECTURE/museum-framework.md", "Product and museum specification", "PENDING-RECONCILIATION", "", "D-012 open", "director session", "NOT-VALIDATED", "", "",
  "Its folder number carries the constitution's archive expansion scheme into the repository, which reconciliation section 4 rules does not survive. Whether specifications belong here at all is D-012. Its posture counts derive from a 96-page snapshot. CR-008."),
 (".claude/agents/*", "AI agent definitions", "CANONICAL", "", "PROGRAMME.md", "director session", "NOT-VALIDATED", "", "", "Claude subagents. Not scholars, advisers, partners or human reviewers."),
 (".claude/hooks/*", "Local pre-push gate", "CANONICAL", "", "AI-AGENT-ROSTER.md", "director session", "NOT-VALIDATED", "", "",
  "Early feedback, not the gate. The enforceable gate is CI plus branch protection; branch protection is an owner action."),
 (".claude/settings.json", "Hook wiring", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", "Governs Bash only. It does not govern non-Bash tools or non-Claude clients."),
 (".github/workflows/*", "Continuous validation", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "",
  "Runs the validator on push and pull request. Requiring it before merge is branch protection, which only the owner can set."),
 (".mcp.json", "Literature connectors", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "",
  "Tool configuration, not research authority. Availability and quota are session facts and belong in access-ledger events."),
 (".gitignore", "Repository hygiene", "CANONICAL", "", "self", "director session", "NOT-VALIDATED", "", "", "Now excludes __pycache__ and *.pyc; a compiled file was tracked before this pass."),
]


def match(rel, pattern):
    if pattern == rel:
        return True
    if pattern.endswith("/*"):
        return rel.startswith(pattern[:-1])
    if "/*." in pattern:
        head, ext = pattern.split("/*")
        return rel.startswith(head + "/") and rel.endswith(ext) and "/" not in rel[len(head) + 1:]
    return False


def main():
    tracked = [p for p in subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                                         text=True, check=True).stdout.split()
               if not p.endswith(".gitkeep")]
    rows, unclassified = [], []
    for rel in sorted(tracked):
        hit = None
        for entry in TABLE:                      # first exact, then glob
            if entry[0] == rel:
                hit = entry
                break
        if hit is None:
            for entry in TABLE:
                if match(rel, entry[0]):
                    hit = entry
                    break
        if hit is None:
            unclassified.append(rel)
            continue
        _, function, role, canon, authority, writer, validated, prefix, gate, notes = hit
        rows.append({
            # Derived from the path, not from position. A positional id
            # renumbered 37 rows when two files were added, so CF-041 named a
            # different file before and after a commit - an identifier that
            # does not name one row is not an identifier.
            "file_id": "CF-" + hashlib.sha256(rel.encode("utf-8")).hexdigest()[:8],
            "function": function, "path": rel, "role": role,
            "canonical_for_function": canon, "authority": authority,
            "responsible_writer": writer, "validated": validated,
            "id_prefix": prefix, "evidence_gate_column": gate, "notes": notes,
        })

    if unclassified:
        print("UNCLASSIFIED PATHS — every file needs an authority:")
        for p in unclassified:
            print("  " + p)
        sys.exit(1)

    csvdialect.write(OUT, FIELDS, rows,
                     quoting=__import__("csv").QUOTE_ALL, lineterminator="\n")
    from collections import Counter
    print(f"canonical-files: {len(rows)} paths, all classified")
    for k, v in sorted(Counter(r["role"] for r in rows).items()):
        print(f"  role {k}: {v}")
    for k, v in sorted(Counter(r["validated"] for r in rows).items()):
        print(f"  validated {k}: {v}")


if __name__ == "__main__":
    main()
