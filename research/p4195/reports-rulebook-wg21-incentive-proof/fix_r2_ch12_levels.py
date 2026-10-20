"""Lift three fourth-level steps in ch-12.md to the third level, placed just before the step that cites them.

The citing step's `*[proved by CHILD]*` becomes CHILD in its `*[from ...]*` list. Refuses to run twice.
"""
import re
import sys
from pathlib import Path

PATH = Path(__file__).resolve().parent / "ch-12.md"
PAIRS = [("inf:sa-consent", "inf:sa-tell-apart"), ("inf:rp-arises", "inf:rp-changes"), ("inf:wa-neither", "inf:wa-tell-apart")]


def main():
    lines = PATH.read_text(encoding="utf-8").split("\n")
    for child, parent in PAIRS:
        child_at = [i for i, line in enumerate(lines) if line.rstrip().endswith("{#%s}" % child)]
        parent_at = [i for i, line in enumerate(lines) if line.rstrip().endswith("{#%s}" % parent)]
        if len(child_at) != 1 or len(parent_at) != 1:
            print("blocked: %s or %s not found exactly once" % (child, parent))
            return 1
        child_line = lines[child_at[0]]
        if not child_line.startswith(" " * 9 + "1. "):
            print("blocked: %s is not at nine spaces; already lifted?" % child)
            return 1
        parent_line = lines[parent_at[0]]
        proved = "*[proved by %s]* " % child
        if proved not in parent_line:
            print("blocked: %s does not cite %s as its only child" % (parent, child))
            return 1
        parent_line = parent_line.replace(proved, "")
        parent_line, count = re.subn(r"\*\[from ([^\]]+)\]\*", lambda m: "*[from %s, %s]*" % (m.group(1), child), parent_line, count=1)
        if count != 1:
            print("blocked: %s has no from list" % parent)
            return 1
        lifted = " " * 6 + child_line[9:]
        del lines[child_at[0]]
        lines[parent_at[0]] = parent_line
        lines.insert(parent_at[0], lifted)
        print("lifted %s before %s" % (child, parent))
    PATH.write_text("\n".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
