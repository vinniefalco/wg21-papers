"""List module candidates in the spine: top-level items with no children whose only citer is one later item in the same chapter."""
import re
from pathlib import Path

SPINE = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof\02-spine.md")
ITEM = re.compile(r"^( *)1\. .*?\{#([a-z:0-9-]+)(?: weakened)?\}\s*$")
CITE = re.compile(r"\*\[(?:from|proved by)\s+([^\]]*)\]\*")
HEAD = re.compile(r"^## (\d+)\.")
EXEMPT = ("m:", "t:", "thm:", "c:")

items, chapter, last_top = [], None, None
for line in SPINE.read_text(encoding="utf-8").splitlines():
    h = HEAD.match(line)
    if h:
        chapter = int(h.group(1))
        continue
    m = ITEM.match(line)
    if not m:
        continue
    level = len(m.group(1)) // 3
    key = m.group(2)
    basis = [k.strip() for c in CITE.finditer(line) for k in c.group(1).split(",")]
    items.append({"key": key, "chapter": chapter, "level": level, "basis": basis,
                  "parent": None if level == 0 else last_top})
    if level == 0:
        last_top = key

index = {it["key"]: i for i, it in enumerate(items)}
citers = {it["key"]: [] for it in items}
for it in items:
    for k in it["basis"]:
        if k in citers:
            citers[k].append(it["key"])
has_children = {it["parent"] for it in items if it["parent"]}

print("Candidates (top-level, no children, one citer, same chapter, citer later):")
found = 0
for it in items:
    k = it["key"]
    if it["level"] or k.startswith(EXEMPT) or k in has_children:
        continue
    cs = citers[k]
    if len(cs) != 1:
        continue
    y = items[index[cs[0]]]
    if y["chapter"] != it["chapter"] or index[y["key"]] < index[k]:
        continue
    outside = [b for b in y["basis"] if b != k]
    found += 1
    print(f"  ch{it['chapter']}: {k} -> only cited by {y['key']} (level {y['level']}); "
          f"{y['key']} also rests on {len(outside)} other items: {outside}")
print(f"{found} candidates")
