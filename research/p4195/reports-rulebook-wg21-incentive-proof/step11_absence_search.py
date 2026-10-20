"""Step 11 absence searches over the SD-4 part of the rule extract (lines 6 to 357)."""
import re
import sys
from pathlib import Path

EXTRACT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\rules-extract.md")
FIRST, LAST = 6, 357

SEARCHES = {
    "integration": ["interact", "integrat", "coheren", "consisten", "together", "harmon", "conflict", "fits", "fit "],
    "later-parts": ["later", "future", "rule out", "preclud", "foreclos", "extension", "extend", "subsequent", "follow-on", "builds on", "depend"],
    "trade-offs": ["trade-off", "tradeoff", "trade off", "cost", "drawback", "downside", "disadvantage", "limitation", "weakness"],
    "quality": ["quality", "judge", "evaluat", "assess", "merit", "review"],
    "objections": ["objection", "concern", "answer", "address", "rebut", "respon", "rationale", "revision", "oppos", "disagree"],
}

lines = EXTRACT.read_text(encoding="utf-8").split("\n")
names = sys.argv[1:] or list(SEARCHES)
for name in names:
    print(f"=== {name} ===")
    for term in SEARCHES[name]:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        hits = [(n, text) for n, text in enumerate(lines, 1) if FIRST <= n <= LAST and pattern.search(text)]
        print(f"--- {term!r}: {len(hits)} line(s)")
        for n, text in hits:
            for m in pattern.finditer(text):
                start = max(0, m.start() - 110)
                end = min(len(text), m.end() + 110)
                print(f"  {n}: ...{text[start:end]}...")
