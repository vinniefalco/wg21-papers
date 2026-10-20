"""Step 3 reconcile: set final verdicts from triage-decisions.txt and append main: reasons to triage.md."""
import re
import sys
from pathlib import Path

SCRATCH = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof")
TRIAGE = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\triage.md")
ROW = re.compile(r"^- ([FI]\d+) \| ")
STATUS_OLD = "or missing premise (a destination statement needs a premise its basis does not supply and the foundation does not yet contain)."
STATUS_NEW = (STATUS_OLD[:-1] + "; or resolved (the main agent decided a disputed or missing-premise row "
              "from the extract, as the row's closing main: note says).")

decisions = {}
for block in SCRATCH.joinpath("triage-decisions.txt").read_text(encoding="utf-8").strip().split("\n\n"):
    ident, verdict, reason = block.strip().split("\n")
    if ident in decisions:
        sys.exit(f"FAIL: duplicate decision for {ident}")
    decisions[ident] = (verdict.strip(), reason.strip())

lines = TRIAGE.read_text(encoding="utf-8").splitlines()
out, seen, rows = [], set(), 0
for line in lines:
    if STATUS_OLD in line:
        line = line.replace(STATUS_OLD, STATUS_NEW)
    m = ROW.match(line)
    if m:
        rows += 1
        ident = m.group(1)
        fields = line.split(" | ", 5)
        if len(fields) != 6:
            sys.exit(f"FAIL: {ident} has {len(fields)} fields")
        if " | main: " in line:
            sys.exit(f"FAIL: {ident} already has a main note")
        if ident in decisions:
            verdict, reason = decisions[ident]
            fields[2] = verdict
            line = " | ".join(fields) + " | main: " + reason
            seen.add(ident)
    out.append(line)

missing = sorted(set(decisions) - seen)
if missing:
    sys.exit(f"FAIL: decisions with no row: {missing}")
TRIAGE.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

open_rows = []
for line in out:
    m = ROW.match(line)
    if m:
        final = line.split(" | ", 5)[2]
        if "disputed" in final or "missing premise" in final:
            open_rows.append(m.group(1))
print(f"rows: {rows}; decisions applied: {len(seen)}; status line updated: {STATUS_NEW in chr(10).join(out)}")
if open_rows:
    print(f"FAIL: still open: {open_rows}")
    sys.exit(1)
print("PASS: no row is left disputed or missing premise")
