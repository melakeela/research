#!/usr/bin/env python3
"""
test-validate-registers.py — prove the validator fails when it should.

A validator that passes is worth nothing until you have watched it fail. Each
case below injects one defect into a throwaway clone, runs the validator, and
asserts that a failure naming that defect comes back. A case that injects a
defect and still passes is itself a failure.

Run from the repository root:  python3 04-AUDITS/test-validate-registers.py
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(clone):
    # --respect-overrides, because that is the single channel the pre-push hook
    # and CI both use. The tree carries four real failures that OVERRIDE-LOG
    # OV-001 covers — rows that cannot be typed without an owner decision — so
    # without the flag the baseline is red and no injected defect means
    # anything. An injected defect produces a failure OV-001's signatures do
    # not match, which is the property being tested.
    p = subprocess.run([sys.executable, "04-AUDITS/validate-registers.py",
                        "--respect-overrides"],
                       cwd=clone, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def edit(clone, rel, old, new, count=1):
    path = clone / rel
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"fixture text not found in {rel}: {old[:60]!r}")
    path.write_text(text.replace(old, new, count), encoding="utf-8")


# (name, mutate(clone), expected substring in the failure output)
CASES = [
    ("status outside the evidence vocabulary",
     lambda c: edit(c, "03-REGISTERS/domain-e-claims.csv", "VERIFIED,SRC-047", "CONFIRMED,SRC-047"),
     "evidence_status 'CONFIRMED' not in its vocabulary"),

    ("gate verdict smuggled into evidence_status",
     lambda c: edit(c, "03-REGISTERS/domain-e-claims.csv", "VERIFIED,SRC-047", "ELIGIBLE,SRC-047"),
     "evidence_status 'ELIGIBLE' not in its vocabulary"),

    ("source id that resolves to nothing",
     lambda c: edit(c, "03-REGISTERS/domain-e-claims.csv", "SRC-047", "SRC-999"),
     "SRC-999 is not in the access ledger"),

    ("inline source cell disagreeing with the join",
     lambda c: edit(c, "03-REGISTERS/domain-e-claims.csv",
                    "SRC-019; SRC-022; SRC-023; SRC-047", "SRC-019; SRC-022"),
     "the join register holds"),

    ("several source ids back in one opaque cell in the join",
     lambda c: edit(c, "03-REGISTERS/claim-sources.csv",
                    '"CS-0001","BR-E-001","03-REGISTERS/CROSS-DOMAIN-BRIDGES.csv","DATA","SRC-065"',
                    '"CS-0001","BR-E-001","03-REGISTERS/CROSS-DOMAIN-BRIDGES.csv","DATA","SRC-065; SRC-059"'),
     "holds more than one identifier"),

    ("VERIFIED row with no locator",
     lambda c: edit(c, "03-REGISTERS/domain-e-claims.csv",
                    "git rev-parse HEAD; sha256sum; 04-AUDITS/rv-token-extract.py output line count", ""),
     "VERIFIED row missing locator"),

    ("locator that cannot be re-found",
     lambda c: edit(c, "03-REGISTERS/domain-e-claims.csv",
                    "git rev-parse HEAD; sha256sum; 04-AUDITS/rv-token-extract.py output line count",
                    "see the article"),
     "is not specific enough to re-find"),

    ("SUPERSEDED row pointing at nothing",
     lambda c: edit(c, "03-REGISTERS/domain-m-brahui-position.csv",
                    '"SUPERSEDED","SRC-048"', '"SUPERSEDED","SRC-048"').__class__ and
               blank_column(c, "03-REGISTERS/domain-m-brahui-position.csv", "superseded_by"),
     "names no replacement in superseded_by"),

    ("duplicate identifier inside one register",
     lambda c: edit(c, "03-REGISTERS/domain-e-claims.csv", "DME-003,", "DME-002,"),
     "duplicate claim_id DME-002"),

    ("D- reference with no owner decision",
     lambda c: (c / "00-CONTROLLER/REPOSITORY-MAP.md").write_text(
         (c / "00-CONTROLLER/REPOSITORY-MAP.md").read_text() + "\n\nSee D-777.\n"),
     "reference D-777 has no OWNER-DECISIONS row"),

    ("HOLD- reference with no hold file",
     lambda c: (c / "00-CONTROLLER/REPOSITORY-MAP.md").write_text(
         (c / "00-CONTROLLER/REPOSITORY-MAP.md").read_text() + "\n\nSee HOLD-042.\n"),
     "reference HOLD-042 has no file in 05-HOLDS/"),

    ("dependency row citing a source that is not in the ledger",
     lambda c: edit(c, "02-SOURCES/dependency.csv", "DEP-001,SRC-023", "DEP-001,SRC-998"),
     "source_a SRC-998 is not in the ledger"),

    ("a tracked file with no authority row",
     lambda c: track_new_file(c, "04-AUDITS/orphan-note.md", "no authority governs this\n"),
     "is tracked but has no authority row"),

    ("publishing a claim that is not release-eligible",
     lambda c: edit(c, "03-REGISTERS/domain-e-claims.csv",
                    "VERIFIED,SRC-047", "VERIFIED,SRC-047", 1) or
               set_column(c, "03-REGISTERS/domain-e-claims.csv", "DME-001",
                          "publication_status", "PUBLISHED"),
     "PUBLISHED but not release-eligible"),

    ("VERIFIED in a register that cannot record a retrieval (F1)",
     lambda c: set_column(c, "03-REGISTERS/HYPOTHESIS-ELIGIBILITY.csv", "HYP-E-000",
                          "evidence_status", "VERIFIED", idcol="hypothesis_id"),
     "in a register with no source_id, locator, retrieval_date column"),

    ("an emptied inline source cell while the join still holds rows (F2)",
     lambda c: set_column(c, "03-REGISTERS/domain-e-claims.csv", "DME-019",
                          "source_id", ""),
     "inline but the join register holds"),

    ("a join row for a claim that exists nowhere (F2)",
     lambda c: (c / "03-REGISTERS/claim-sources.csv").write_text(
         (c / "03-REGISTERS/claim-sources.csv").read_text()
         + '"CS-9999","DME-999","03-REGISTERS/domain-e-claims.csv","CLAIM",'
           '"SRC-047","SOLE","somewhere","IG-SRC-047",""\n'),
     "which holds no such row"),

    ("two registers issuing the same identifier (F7)",
     lambda c: (c / "03-REGISTERS/domain-e-interpretations.csv").write_text(
         (c / "03-REGISTERS/domain-e-interpretations.csv").read_text()
         + '"DME-001","a duplicate of a claim in another register","PROVISIONAL",'
           '"","","","","","","","UNASSIGNED","UNASSIGNED","UNASSIGNED","",""\n'),
     "is also issued by"),

    ("a gate_verdict outside its vocabulary (F7)",
     lambda c: set_column(c, "03-REGISTERS/domain-e-hypothesis-eligibility.csv", "E-3",
                          "gate_verdict", "PROBABLY", idcol="hypothesis_id"),
     "gate_verdict 'PROBABLY' not in its vocabulary"),

    ("an override with a non-date expiry (F3)",
     lambda c: (c / "00-CONTROLLER/OVERRIDE-LOG.csv").write_text(
         (c / "00-CONTROLLER/OVERRIDE-LOG.csv").read_text()
         + '"OV-901","because","someone","2026-09-07","never",'
           '"evidence_status not in its vocabulary","one push","owner",""\n'),
     "is not an ISO date"),

    ("an override signature short enough to waive everything (F3)",
     lambda c: (c / "00-CONTROLLER/OVERRIDE-LOG.csv").write_text(
         (c / "00-CONTROLLER/OVERRIDE-LOG.csv").read_text()
         + '"OV-902","because","someone","2026-09-07","2026-10-01","-","one push","owner",""\n'),
     "waives failures nobody has read"),

    ("an override signature naming only a file path (S4)",
     lambda c: (c / "00-CONTROLLER/OVERRIDE-LOG.csv").write_text(
         (c / "00-CONTROLLER/OVERRIDE-LOG.csv").read_text()
         + '"OV-903","because","someone","2026-09-07","2026-10-01",'
           '"03-REGISTERS/domain-e-claims.csv","one push","owner",""\n'),
     "name no defect"),




    ("a hand-edited independence_group in the join (S6)",
     lambda c: set_column(c, "03-REGISTERS/claim-sources.csv", "CS-0001",
                          "independence_group", "IG-SRC-999", idcol="join_id"),
     "does not match"),

    ("a duplicated join_id (S9)",
     lambda c: set_column(c, "03-REGISTERS/claim-sources.csv", "CS-0002",
                          "join_id", "CS-0001", idcol="join_id"),
     "duplicate join_id CS-0001"),

    ("a PROVISIONAL row with its source emptied (S2)",
     lambda c: set_column(c, "03-REGISTERS/domain-e-claims.csv", "DME-019",
                          "evidence_status", "PROVISIONAL") or set_column(
         c, "03-REGISTERS/domain-e-claims.csv", "DME-019", "source_id", ""),
     "PROVISIONAL row missing source_id"),

    ("an override cannot waive a missing retrieval field",
     lambda c: blank_locators(c, 1) or add_overrides(
         c, 1, "VERIFIED row missing locator"),
     "VERIFIED row missing locator"),

    ("overrides composed to waive more than the total cap",
     lambda c: blank_locators(c, 9) or add_overrides(
         c, 3, "VERIFIED row missing locator"),
     "VERIFIED row missing locator"),

    ("an override signature that is a path plus a colon (Q3)",
     lambda c: (c / "00-CONTROLLER/OVERRIDE-LOG.csv").write_text(
         (c / "00-CONTROLLER/OVERRIDE-LOG.csv").read_text()
         + '"OV-904","because","someone","2026-09-07","2026-10-01",'
           '"03-REGISTERS/domain-e-claims.csv:","one push","owner",""\n'),
     "name no defect"),

    ("a claim register downgraded to REPORTED (Q1)",
     lambda c: set_column(c, "00-CONTROLLER/CANONICAL-FILES.csv",
                          "03-REGISTERS/domain-e-claims.csv", "validated",
                          "REPORTED", idcol="path"),
     "cannot be REPORTED"),

    ("a VERIFIED row whose locator cites inherited material (Q13)",
     lambda c: set_column(c, "03-REGISTERS/rigveda-pur-family.csv", "PUR-002",
                          "locator", "01-INHERITED/claude-project-handoff.md L451"),
     "locator cites inherited material"),

    ("a REPORTED register with no hold row naming it (T12)",
     lambda c: set_column(c, "00-CONTROLLER/CANONICAL-FILES.csv",
                          "03-REGISTERS/domain-e-claims.csv", "validated",
                          "REPORTED", idcol="path"),
     "is REPORTED but no MIGRATION-HOLDS.csv row names it"),

    ("a misspelled validated mode (T12)",
     lambda c: set_column(c, "00-CONTROLLER/CANONICAL-FILES.csv",
                          "03-REGISTERS/domain-e-claims.csv", "validated",
                          "gated", idcol="path"),
     "is not one of ['GATED', 'NOT-VALIDATED', 'REPORTED']"),

    ("a row with eligibility prose and no gate verdict (T10)",
     lambda c: set_column(c, "03-REGISTERS/domain-e-hypothesis-eligibility.csv",
                          "E-9", "gate_verdict", "UNASSIGNED",
                          idcol="hypothesis_id"),
     "eligibility prose but no gate_verdict"),

    ("a hold file nothing references",
     lambda c: track_new_file(c, "05-HOLDS/HOLD-099-orphan.md", "# HOLD-099\n\nnothing waits on this\n"),
     "HOLD-099 is referenced by nothing outside"),

    ("a DECISIONS-NEEDED section with no register row pointing back",
     lambda c: (c / "DECISIONS-NEEDED.md").write_text(
         # D-004 is a real decision whose detail_ref is empty: it is
         # non-blocking, so under the routing rule it gets no prose section.
         (c / "DECISIONS-NEEDED.md").read_text() + "\n\n## D-004 — prose it should not have\n"),
     "section D-004 has no OWNER-DECISIONS row whose detail_ref points back"),

    ("an override row with no expiry",
     lambda c: (c / "00-CONTROLLER/OVERRIDE-LOG.csv").write_text(
         (c / "00-CONTROLLER/OVERRIDE-LOG.csv").read_text()
         + '"OV-001","because","someone","2026-09-07","","",""\n'),
     "override row missing ['expiry_date', 'affected_validation_failures']"),
]


def blank_column(clone, rel, column):
    import csv
    path = clone / rel
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
        fields = list(rows[0].keys())
    for r in rows:
        if (r.get("evidence_status") or "") == "SUPERSEDED":
            r[column] = ""
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
        w.writeheader()
        w.writerows(rows)


def set_column(clone, rel, row_id, column, value, idcol="claim_id"):
    import csv
    path = clone / rel
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
        fields = list(rows[0].keys())
    hit = False
    for r in rows:
        if (r.get(idcol) or "") == row_id:
            r[column] = value
            hit = True
    if not hit:
        raise AssertionError(f"fixture row {row_id} not found in {rel}")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_ALL,
                           lineterminator="\r\n")
        w.writeheader()
        w.writerows(rows)


def track_new_file(clone, rel, content):
    (clone / rel).write_text(content, encoding="utf-8")
    subprocess.run(["git", "add", rel], cwd=clone, check=True, capture_output=True)


def sync(clone):
    """Mirror ROOT's tracked working tree into the clone, deletions included.

    The clone is made from committed history, which may lag the working tree
    being tested — a renamed file would otherwise survive in the clone and
    fail the control-plane check for reasons that have nothing to do with the
    case under test.
    """
    want = set(subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout.split())
    have = set(subprocess.run(["git", "ls-files"], cwd=clone, capture_output=True,
                              text=True, check=True).stdout.split())
    for rel in have - want:
        (clone / rel).unlink(missing_ok=True)
    for rel in want:
        dst = clone / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, dst)
    subprocess.run(["git", "add", "-A"], cwd=clone, check=True, capture_output=True)


def blank_locators(clone, n):
    """Empty the locator on the first n VERIFIED rows of the domain E claims."""
    import csv
    path = clone / "03-REGISTERS/domain-e-claims.csv"
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
        fields = list(rows[0].keys())
    hit = 0
    for r in rows:
        if r["evidence_status"] == "VERIFIED" and hit < n:
            r["locator"] = ""
            hit += 1
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, quoting=csv.QUOTE_ALL,
                           lineterminator="\r\n")
        w.writeheader()
        w.writerows(rows)


def add_overrides(clone, count, signature):
    """Append `count` override rows, each waiving the same signature."""
    log = clone / "00-CONTROLLER/OVERRIDE-LOG.csv"
    text = log.read_text(encoding="utf-8")
    for i in range(count):
        text += (f'"OV-9{i:02d}","composition","attacker","2026-09-07","2026-10-01",'
                 f'"{signature}","one push","none",""\n')
    log.write_text(text, encoding="utf-8")


def main():
    with tempfile.TemporaryDirectory() as tmp:
        clone = Path(tmp) / "clone"
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(clone)],
                       check=True, capture_output=True)
        sync(clone)

        code, out = run(clone)
        if code != 0:
            print("BASELINE FAILED — the tree must pass (with OV-001 honoured) "
                  "before injected defects mean anything")
            print(out)
            return 1
        print(f"baseline: clean tree passes ({len(CASES)} cases to run)\n")

        passed = failed = 0
        for name, mutate, expected in CASES:
            subprocess.run(["git", "checkout", "--quiet", "--", "."], cwd=clone, check=True)
            subprocess.run(["git", "clean", "-qfd"], cwd=clone, check=True)
            subprocess.run(["git", "reset", "--quiet"], cwd=clone, check=True)
            sync(clone)
            try:
                mutate(clone)
            except AssertionError as exc:
                print(f"  ERROR  {name}: {exc}")
                failed += 1
                continue
            code, out = run(clone)
            if code == 0:
                print(f"  MISSED {name}: validator passed a tree containing this defect")
                failed += 1
            elif expected not in out:
                print(f"  WRONG  {name}: failed, but not with the expected message")
                print(f"         expected substring: {expected!r}")
                failed += 1
            else:
                print(f"  caught {name}")
                passed += 1

        print(f"\n{passed} caught, {failed} not caught, {len(CASES)} cases")
        return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
