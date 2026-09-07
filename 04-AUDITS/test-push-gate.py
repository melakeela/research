#!/usr/bin/env python3
"""
test-push-gate.py — prove the pre-push hook denies what it claims to deny.

The hook's header makes four promises: that it recognises a push however it
is spelled, that there is no ordinary bypass, that it fails closed, and that
an override must be committed, bounded and specific. Each is tested here
against a throwaway copy with a real validator failure in it, because a gate
nobody has watched refuse something is not a gate.

The four bypasses in the DENY list marked (F4) were found by adversarial
review walking past an earlier parser. They are kept as regressions.

Run from the repository root:  python3 04-AUDITS/test-push-gate.py
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOK = ".claude/hooks/block-push-on-register-failure.sh"

DENY = [
    ("git push", 'git push'),
    ("git push with arguments", 'git push -u origin some-branch'),
    ("extra whitespace", 'git   push'),
    ("env wrapper", 'env git push'),
    ("absolute path", '/usr/bin/git push'),
    ("sh -c wrapper", "sh -c 'git push'"),
    ("eval wrapper", 'eval "git push"'),
    ("subshell (F4)", '(git push)'),
    ("command substitution (F4)", 'echo $(git push)'),
    ("xargs (F4)", 'echo push | xargs git'),
    ("quote-split verb (F4)", 'git pu"sh"'),
    ("fully quoted verb (F4)", 'git "push"'),
    # Found by the second adversarial pass walking past the first repair (S3).
    ("escaped tab in the token (S3)", 'gi\\t push'),
    ("escaped char in the verb (S3)", 'git pus\\h'),
    ("escaped leading slash (S3)", '\\git push'),
    ("line continuation between token and verb (S3)", 'git \\\n push'),
    ("line continuation inside the verb (S3)", 'git p\\\nush'),
    ("continuation then a flag (S3)", 'git \\\npush --force'),
    ("positional expansion between them (S3)", 'git "$@" push'),
    ("parameter expansion between them (S3)", 'git ${GIT_OPTS-} push'),
    ("a flag before the subcommand (S3)", 'git --file push origin'),
    ("removed marker no longer bypasses", 'MELAKEELA_REGISTER_GATE=off git push'),
    ("echo-marker trick", 'echo MELAKEELA_REGISTER_GATE=off; git push'),
]

ALLOW = [
    ("an unrelated command", 'ls -la'),
    ("a read-only git command", 'git log --oneline'),
    ("a commit whose message says push", 'git commit -m "add push button"'),
    ("a commit about removing the bypass", 'git commit -m "remove the push bypass"'),
    # False positives the first repair introduced (S3).
    ("a log search for the word push", 'git log --oneline --grep=push'),
    ("a grep for the word push", 'git grep push -- 03-REGISTERS'),
]

# (name, override row appended to OVERRIDE-LOG.csv, should the push be allowed)
OVERRIDES = [
    ("expiry 'never' with a one-character signature (F3)",
     '"OV-901","because","someone","2026-09-07","never","-","one push","owner","exploit"', False),
    ("a signature too short to name a failure (F3)",
     '"OV-902","because","someone","2026-09-07","2026-12-31","-","one push","owner","short"', False),
    ("a waiver running more than 90 days (F3)",
     '"OV-903","because","someone","2026-09-07","2029-01-01",'
     '"evidence_status \'CONFIRMED\' not in its vocabulary","one push","owner","too long"', False),
    ("an expired waiver",
     '"OV-904","because","someone","2026-01-01","2026-02-01",'
     '"evidence_status \'CONFIRMED\' not in its vocabulary","one push","owner","expired"', False),
    ("a live waiver for a different failure",
     '"OV-905","because","someone","2026-09-07","2026-10-01",'
     '"some entirely unrelated failure text","one push","owner","non-matching"', False),
    ("a waiver naming only a register path (S4)",
     '"OV-907","because","someone","2026-09-07","2026-10-01",'
     '"03-REGISTERS/domain-e-claims.csv","one push","owner","file-wide"', False),
    ("a bounded, specific, unexpired waiver",
     '"OV-906","genuine emergency","someone","2026-09-07","2026-10-01",'
     '"evidence_status \'CONFIRMED\' not in its vocabulary","one push","owner","valid"', True),
]


def ask(tree, command, payload=None):
    """Return True if the hook denies the command."""
    body = payload if payload is not None else json.dumps(
        {"tool_name": "Bash", "tool_input": {"command": command}})
    p = subprocess.run(["bash", str(tree / HOOK)], input=body, cwd=tree,
                       capture_output=True, text=True,
                       env={"CLAUDE_PROJECT_DIR": str(tree),
                            "PATH": "/usr/local/bin:/usr/bin:/bin",
                            "HOME": str(tree)})
    out = p.stdout.strip()
    if not out:
        return False
    json.loads(out)          # a malformed decision is a failure in itself
    return True


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tree = Path(tmp) / "tree"
        # A real clone, not a copy: the validator's control-plane check reads
        # `git ls-files`, so a tree without git history fails for reasons that
        # have nothing to do with the gate.
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(tree)],
                       check=True, capture_output=True)
        want = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout.split()
        have = subprocess.run(["git", "ls-files"], cwd=tree, capture_output=True,
                              text=True, check=True).stdout.split()
        for rel in set(have) - set(want):
            (tree / rel).unlink(missing_ok=True)
        for rel in want:
            dst = tree / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, dst)
        subprocess.run(["git", "add", "-A"], cwd=tree, check=True, capture_output=True)

        # A clean tree must allow, or nothing below distinguishes the gate
        # from a hook that denies everything.
        if ask(tree, "git push"):
            print("BASELINE FAILED: the hook denies a push on a clean tree")
            return 1
        print("baseline: clean tree allows a push")

        claims = tree / "03-REGISTERS/domain-e-claims.csv"
        claims.write_text(claims.read_text(encoding="utf-8")
                          .replace("VERIFIED,SRC-047", "CONFIRMED,SRC-047", 1),
                          encoding="utf-8")
        if not ask(tree, "git push"):
            print("BASELINE FAILED: the hook allows a push on a failing tree")
            return 1
        print("baseline: failing tree denies a push\n")

        passed = failed = 0
        for name, cmd in DENY:
            if ask(tree, cmd):
                print(f"  denies  {name}")
                passed += 1
            else:
                print(f"  ALLOWED {name}  <-- bypass")
                failed += 1
        for name, cmd in ALLOW:
            if not ask(tree, cmd):
                print(f"  allows  {name}")
                passed += 1
            else:
                print(f"  DENIED  {name}  <-- false positive")
                failed += 1

        # Fail-closed conditions.
        if ask(tree, None, payload="not json"):
            print("  denies  an unparseable payload")
            passed += 1
        else:
            print("  ALLOWED an unparseable payload  <-- fails open")
            failed += 1

        validator = tree / "04-AUDITS/validate-registers.py"
        stashed = validator.read_text(encoding="utf-8")
        validator.unlink()
        if ask(tree, "git push"):
            print("  denies  a missing validator")
            passed += 1
        else:
            print("  ALLOWED a missing validator  <-- fails open")
            failed += 1
        validator.write_text(stashed, encoding="utf-8")

        log = tree / "00-CONTROLLER/OVERRIDE-LOG.csv"
        clean = log.read_text(encoding="utf-8")
        for name, row, expect_allow in OVERRIDES:
            log.write_text(clean + row + "\n", encoding="utf-8")
            denied = ask(tree, "git push")
            ok = (not denied) if expect_allow else denied
            verb = "allows" if expect_allow else "refuses"
            print(f"  {verb:7s} {name}" if ok
                  else f"  WRONG   {name}  <-- expected "
                       f"{'allow' if expect_allow else 'deny'}")
            passed += ok
            failed += not ok
        log.write_text(clean, encoding="utf-8")

        print(f"\n{passed} correct, {failed} wrong")
        return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
