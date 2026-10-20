"""Step 12 round 2, global decision 1: search the ISO clauses in the rule extract.

Searches every ISO/IEC Directives Part 1 section of the extract (0.1 to 6.5) for the stems that
f:no-drawbacks-asked and f:no-interest-statement searched in SD-4, plus synonyms, and prints
each hit with its section and the sentence around it.
"""
import re
from pathlib import Path

EXTRACT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\rules-extract.md")
GROUPS = {
    "drawbacks": ["trade-off", "tradeoff", "trade off", "drawback", "downside", "disadvantage", "limitation",
                  "weakness", "shortcoming", "cost", "risk", "detriment", "negative impact", "adverse", "impact"],
    "interests": ["disclos", "declar", "affiliat", "interest", "employ", "sponsor", "fund", "compan", "behalf",
                  "patent", "conflict"],
}


def sections():
    out = []
    current = None
    for line in EXTRACT.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            out.append([current, []])
            continue
        if current is not None:
            out[-1][1].append(line)
    return [(name, " ".join(lines)) for name, lines in out if name.startswith("ISO/IEC Directives Part 1")]


def main():
    secs = sections()
    print("ISO sections searched: %d (%s ... %s)" % (len(secs), secs[0][0][26:], secs[-1][0][26:]))
    for group, stems in GROUPS.items():
        print("\n== %s" % group)
        for stem in stems:
            for name, text in secs:
                for m in re.finditer(re.escape(stem), text, re.I):
                    lo = max(0, text.rfind(". ", 0, m.start()) + 2)
                    hi = text.find(". ", m.end())
                    hi = len(text) if hi < 0 else hi + 1
                    print("[%s] %s: %s" % (stem, name[26:], text[lo:hi].strip()[:300]))


if __name__ == "__main__":
    main()
