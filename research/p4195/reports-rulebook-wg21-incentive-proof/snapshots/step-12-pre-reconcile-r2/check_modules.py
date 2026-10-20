"""Step 7 module gate: each module's inner items are cited only inside their module."""
import re
import sys
from pathlib import Path

SPINE = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof\02-spine.md")
MODULES = {
    "l:vote-count": ["l:against-double", "l:neutral-outside", "l:room-size", "l:one-third-against"],
    "p:persuasion-not-required": ["l:address-not-resolve", "p:advance-unanswered"],
    "p:record-indistinct": ["l:record-content", "l:record-checks", "l:iso-register-level"],
    "p:sg-decides": ["l:sg-purpose", "l:sg-attendance", "l:sg-start"],
    "p:disclosure": ["l:author-knows-more"],
    "p:miss-cost": ["l:cutoff"],
    "p:nb-members": ["l:incits-votes", "l:incits-positions"],
    "p:checks": ["l:checks-hearing", "l:checks-alternatives", "l:checks-deadlock", "l:checks-attendance", "l:checks-record"],
}
KEY = re.compile(r"\{#([a-z:0-9-]+)(?: weakened)?\}\s*$")
CITE = re.compile(r"\*\[(?:from|proved by)\s+([^\]]*)\]\*")

citers = {}
current = None
for line in SPINE.read_text(encoding="utf-8").splitlines():
    keys = [k.strip() for m in CITE.finditer(line) for k in m.group(1).split(",")]
    m = KEY.search(line)
    owner = m.group(1) if m else ("table" if line.startswith("*[") else None)
    for k in keys:
        citers.setdefault(k, set()).add(owner)

failures = []
for top, inner in MODULES.items():
    allowed = set(inner) | {top}
    for key in inner:
        outside = sorted(c for c in citers.get(key, set()) if c not in allowed)
        print(f"{key:26} cited by {sorted(citers.get(key, set()))}")
        if outside:
            failures.append(f"{key} cited outside its module by {outside}")
    if not citers.get(top):
        failures.append(f"{top} has no citer outside the module")
    else:
        print(f"{top:26} cited by {sorted(citers[top])}")
if failures:
    print("FAIL")
    for f in failures:
        print("  " + f)
    sys.exit(1)
print("PASS: every module's inner items are cited only inside it")
