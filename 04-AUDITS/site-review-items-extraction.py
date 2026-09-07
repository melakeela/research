# -*- coding: utf-8 -*-
"""Extract the LS- and COR- coverage items from the two committed site-review
running-list versions and APPEND them to 03-REGISTERS/inherited-claims.csv.

Appends only. The existing IH-001..IH-369 rows extracted from
01-INHERITED/claude-project-handoff.md are read and rewritten byte-identical;
they are never renumbered, because DECISIONS-NEEDED.md and other files cite
those IDs.

Both source files enter as INHERITED-UNVERIFIED under the inheritance rule in
CLAUDE.md. An LS- or COR- row is a coverage commitment written by the owner and
prior model threads, not a finding. Nothing here carries a retrieval event, so
source_id, retrieval_date and supports_page stay empty exactly as in the
handoff rows.
"""
import csv, io, re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = "01-INHERITED/site-review"
V12 = "MELAKEELASITEREVIEWRUNNINGLIST.md"    # Version 12 — later, current
V10 = "MELAKEELASITEREVIEWRUNNINGLIST2.md"   # Version 10 — earlier, superseded
REG = "03-REGISTERS/inherited-claims.csv"

ROW = re.compile(r"^\|\s*((?:LS|COR)-\d+)\s*\|(.*)\|\s*$")


def scan(fname):
    """Return {item_id: (line_no, title, scope, packet, section)}."""
    out, sec2, sec3 = {}, "", ""
    with io.open(os.path.join(BASE, DIR, fname), encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            if line.startswith("## "):
                sec2, sec3 = line[3:].strip(), ""
            elif line.startswith("### "):
                sec3 = line[4:].strip()
            m = ROW.match(line)
            if not m:
                continue
            cells = [c.strip() for c in m.group(2).split("|")]
            assert len(cells) == 3, (fname, n, cells)
            title, scope, packet = cells
            out[m.group(1)] = (n, title, scope, packet, sec3 or sec2)
    return out


cur = scan(V12)
old = scan(V10)

# What each file is expected to hold; a mismatch means the sources moved.
assert sorted(k for k in cur if k.startswith("LS-")) == \
       ["LS-%02d" % i for i in range(1, 52)], "v12 LS set changed"
assert sorted(k for k in cur if k.startswith("COR-")) == \
       ["COR-%02d" % i for i in range(1, 19)], "v12 COR set changed"
assert sorted(k for k in old if k.startswith("LS-")) == \
       ["LS-%02d" % i for i in range(1, 32)], "v10 LS set changed"
assert not [k for k in old if k.startswith("COR-")], "v10 has no COR items"

# Every item the earlier file carries must survive unchanged in the later one;
# that is what makes Version 12 a supersession rather than a parallel record.
for k, v in old.items():
    assert cur[k][1:4] == v[1:4], "text drift between versions at %s" % k


def key(item_id):
    kind, num = item_id.split("-")
    return (0 if kind == "LS" else 1, int(num))


rows = []
for item_id in sorted(cur, key=key):
    n, title, scope, packet, section = cur[item_id]
    claim = ("The site review running list schedules %s “%s” as a "
             "coverage item: %s Assigned: %s." % (item_id, title, scope, packet))
    locator = "%s/%s L%d" % (DIR, V12, n)
    if item_id in old:
        note = ("Version 12 §%s. Also in %s (Version 10) L%d, textually "
                "identical; registered once under the source-independence rule "
                "because the two files are one lineage, not two witnesses."
                % (section, V10, old[item_id][0]))
    else:
        note = ("Version 12 §%s. Added after Version 10; absent from %s."
                % (section, V10))
    note += (" Coverage commitment, not a finding: it records what the running "
             "list proposes to investigate, and promotion requires a retrieval "
             "event in 02-SOURCES/access-ledger.csv.")
    rows.append((claim, locator, note))

# ---------- append ----------
path = os.path.join(BASE, REG)
with io.open(path, encoding="utf-8", newline="") as fh:
    existing = list(csv.reader(fh))
header, body = existing[0], existing[1:]
assert header == ["claim_id", "claim", "status", "source_id", "locator",
                  "retrieval_date", "supports_page", "notes"], "schema drift"
assert not [r for r in body if not r[0].startswith("IH-")], "unexpected id prefix"
start = max(int(r[0].split("-")[1]) for r in body)
assert start == len(body) == 369, "expected 369 contiguous handoff rows"

for i, (claim, locator, note) in enumerate(rows, start + 1):
    body.append(["IH-%03d" % i, claim, "INHERITED-UNVERIFIED", "", locator,
                 "", "", note])

with io.open(path, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(header)
    for r in body:
        assert "\n" not in "".join(r), r[0]
        w.writerow(r)

ids = [r[0] for r in body]
assert len(set(ids)) == len(ids), "duplicate claim_id"
assert all(r[2] == "INHERITED-UNVERIFIED" for r in body), "status drift"
assert all(r[3] == "" and r[5] == "" and r[6] == "" for r in body), \
    "non-empty reserved field"
print("appended %d rows: IH-%03d..IH-%03d" % (len(rows), start + 1, len(body)))
print("  LS-: %d (%d shared with Version 10, %d new)"
      % (len([r for r in cur if r.startswith("LS-")]),
         len([r for r in cur if r.startswith("LS-") and r in old]),
         len([r for r in cur if r.startswith("LS-") and r not in old])))
print("  COR-: %d (all new; Version 10 has none)"
      % len([r for r in cur if r.startswith("COR-")]))
print("register total: %d rows" % len(body))
