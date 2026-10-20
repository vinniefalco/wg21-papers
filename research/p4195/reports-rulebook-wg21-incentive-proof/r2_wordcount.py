"""Step 12 round 2: check that every new spine statement has at most two sentences of at most 30 words.

Tables and the Theorem may have more sentences; every sentence must still be at most 30 words.
Quoted labels in captions count as words. Run with no arguments.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2_spine_apply as m  # noqa: E402


def sentences(text):
    return [s for s in re.split(r'(?<=\.)\s+(?=[A-Z"])', text) if s.strip()]


def main():
    items = dict(m.NEW)
    items.update(m.CAPTIONS)
    items["thm-p1"] = m.THEOREM_P1
    items["thm-p2"] = m.THEOREM_P2
    bad = 0
    for key, text in items.items():
        parts = sentences(text)
        if not key.startswith(("t:", "thm")) and len(parts) > 2:
            print("SENTENCES %s %d" % (key, len(parts)))
            bad += 1
        for s in parts:
            n = len(s.split())
            if n > 30:
                print("LONG %s %d: %s" % (key, n, s[:90]))
                bad += 1
        if "\u2014" in text or "--" in text:
            print("DASH %s" % key)
            bad += 1
    print("checked %d, problems %d" % (len(items), bad))


if __name__ == "__main__":
    main()
