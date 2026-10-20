"""One-off: rephrase four uses of "carry" in the round 1 decisions, then refresh the generated files.

Regenerates the fix files and r1-log-section.md with r1_generate.py, and replaces the round 1
section at the end of adversarial-log-draft.md with the regenerated text.
"""
import subprocess
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
PAIRS = [
    ("(force kept: the first sentence carries the claim)", "(force kept: the first sentence makes the claim)"),
    ("a directed change carries out a direction poll's approval rather than reversing it",
     "a directed change puts a direction poll's approval into effect rather than reversing it"),
    ("not a threat the convenor must carry out", "not a threat the convenor must act on"),
    ("make omission carry rule-based risks", "give omission rule-based risks"),
]
for name in ("r1-decisions-a.txt", "r1-decisions-b.txt"):
    p = S / name
    t = p.read_text(encoding="utf-8")
    for a, b in PAIRS:
        t = t.replace(a, b)
    p.write_text(t, encoding="utf-8", newline="\n")

subprocess.run([sys.executable, str(S / "r1_generate.py")], check=True, stdout=subprocess.DEVNULL)

log = S / "adversarial-log-draft.md"
text = log.read_text(encoding="utf-8")
marker = "## Step 12, verify round 1 (2026-10-19)"
head = text[: text.index(marker)]
section = (S / "r1-log-section.md").read_text(encoding="utf-8")
log.write_text(head + section, encoding="utf-8", newline="\n")
print("log section replaced; carry left:", sum(section.lower().count(w) for w in (" carry", " carries")))
