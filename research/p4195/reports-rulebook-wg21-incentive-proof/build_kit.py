"""Copy the plan's tagged blocks into kit.md byte for byte, then check every tag pair."""
import re
import sys
from pathlib import Path

PLAN = Path(r"c:\Users\Vinnie\.cursor\plans\wg21_incentive_model_96468661.plan.md")
KIT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\kit.md")
SECTIONS = (
    "## Shared blocks",
    "## Role blocks",
    "## Specs",
    "## Pre-digested analysis",
    "## Candidate lists",
)
EXPECTED = {
    "writer-register", "proof-style", "proof-terms", "payoff-table-format",
    "sealed-history-rule", "triage-check-instructions", "chapter-fill-instructions",
    "logician-instructions", "rules-check-instructions", "reader-instructions",
    "skeptic-instructions", "fix-instructions", "coding-instructions",
    "code-review-instructions", "scrivener-spec", "build-script-spec",
    "pre-digest-foundation", "pre-digest-spine", "pre-triage",
    "original-assumptions", "candidate-incentives", "candidate-facts",
}
OPEN = re.compile(rb"^<([a-z0-9-]+)>\r?\n?$")
CLOSE = re.compile(rb"^</([a-z0-9-]+)>\r?\n?$")

data = PLAN.read_bytes()
lines = data.splitlines(keepends=True)
eol = b"\r\n" if b"\r\n" in data else b"\n"

blocks = []
section_wanted = False
open_tag = None
start = None
for i, line in enumerate(lines):
    if open_tag is None:
        if line.startswith(b"## "):
            section_wanted = line.decode("utf-8").startswith(SECTIONS)
            continue
        m = OPEN.match(line)
        if m:
            open_tag, start = m.group(1).decode(), i
        continue
    m = CLOSE.match(line)
    if m and m.group(1).decode() == open_tag:
        if section_wanted:
            chunk = b"".join(lines[start:i + 1])
            if not chunk.endswith(b"\n"):
                chunk += eol
            blocks.append((open_tag, chunk))
        open_tag = None

if open_tag is not None:
    sys.exit(f"FAIL: unclosed tag <{open_tag}> at plan line {start + 1}")

KIT.write_bytes(eol.join(chunk for _, chunk in blocks))

failures = []
names = [name for name, _ in blocks]
if set(names) != EXPECTED or len(names) != len(EXPECTED):
    failures.append(f"tag set mismatch: missing={sorted(EXPECTED - set(names))} "
                    f"extra={sorted(set(names) - EXPECTED)} count={len(names)}")

kit_lines = KIT.read_bytes().decode("utf-8").splitlines()
plan_text = data.decode("utf-8")
for name, chunk in blocks:
    pattern = re.compile(rf"^</?{re.escape(name)}>")
    hits = [(n, line) for n, line in enumerate(kit_lines) if pattern.search(line)]
    if len(hits) != 2:
        failures.append(f"{name}: {len(hits)} matches")
        continue
    (n1, l1), (n2, l2) = hits
    if l1 != f"<{name}>" or l2 != f"</{name}>" or n1 >= n2:
        failures.append(f"{name}: bad pair {l1!r} at {n1 + 1}, {l2!r} at {n2 + 1}")
    if chunk.decode("utf-8") not in plan_text:
        failures.append(f"{name}: block is not a byte copy of the plan")

print(f"kit: {KIT} ({KIT.stat().st_size} bytes, {len(blocks)} blocks)")
for name, chunk in blocks:
    print(f"  {name}: {chunk.count(b'\n')} lines")
if failures:
    print("FAIL")
    for f in failures:
        print("  " + f)
    sys.exit(1)
print("PASS: every tag has exactly one unindented opening line followed by one closing line")
