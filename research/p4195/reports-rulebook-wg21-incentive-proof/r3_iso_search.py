"""Step 12 round 3: search the rule extract for the stems two round 3 findings turn on.

Group "answers" searches every ISO/IEC Directives Part 1 section for observation and the other
f:iso-no-answer stems (12.3R1). Group "trade-off" searches every section of the extract, SD-4 and
INCITS included, for the three spellings f:no-drawbacks-asked lists (12.3L11). Prints each hit with
its section and the sentence around it, then the count per stem.
"""
import re
from pathlib import Path

EXTRACT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\rules-extract.md")
GROUPS = {
    "answers": (["observation"], True),
    "trade-off": (["trade-off", "tradeoff", "trade off"], False),
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
    return [(name, " ".join(lines)) for name, lines in out]


def main():
    secs = sections()
    for group, (stems, iso_only) in GROUPS.items():
        pool = [s for s in secs if s[0].startswith("ISO/IEC Directives Part 1")] if iso_only else secs
        print("\n== %s (%d sections)" % (group, len(pool)))
        for stem in stems:
            n = 0
            for name, text in pool:
                for m in re.finditer(re.escape(stem), text, re.I):
                    n += 1
                    lo = max(0, text.rfind(". ", 0, m.start()) + 2)
                    hi = text.find(". ", m.end())
                    hi = len(text) if hi < 0 else hi + 1
                    print("[%s] %s: %s" % (stem, name, text[lo:hi].strip()[:240]))
            print("  %s: %d hits" % (stem, n))


if __name__ == "__main__":
    main()
