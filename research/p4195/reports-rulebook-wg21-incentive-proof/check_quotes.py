"""Step 1 gate: every quoted anchor in pre-digest-foundation, plus three named quotes, appears in the extract."""
import re
import sys
from pathlib import Path

KIT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\kit.md")
EXTRACT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\rules-extract.md")
EXTRA = [
    "more than twice as many in favor",
    "not akin to a right to veto",
    "may be asked for their reasons",
]

kit = KIT.read_text(encoding="utf-8")
block = re.search(r"^<pre-digest-foundation>$(.*?)^</pre-digest-foundation>$", kit, re.S | re.M).group(1)
anchors = []
for group in re.findall(r'\(("[^)]*")\)', block):
    anchors.extend(re.findall(r'"([^"]+)"', group))
quotes = anchors + EXTRA
extract = EXTRACT.read_text(encoding="utf-8")

missing = [q for q in quotes if q not in extract]
print(f"anchors from pre-digest-foundation: {len(anchors)}; extra: {len(EXTRA)}; total: {len(quotes)}")
for q in quotes:
    print(("  ok   " if q in extract else "  MISS ") + q)
if len(quotes) != 25 or missing:
    print(f"FAIL: expected 25 quotes, got {len(quotes)}; missing {len(missing)}")
    sys.exit(1)
print("PASS: all 25 quotes found")
