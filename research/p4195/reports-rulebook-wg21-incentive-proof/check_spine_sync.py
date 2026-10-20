"""Check that every spine statement in 02-spine.md matches its chapter copy word for word.

A statement is an item's text from its kind label to its basis (or key, when it has no basis),
joined across continuation paragraphs such as the Theorem's second paragraph. A table's
statement is its caption and its rows. Bases and citation lines are not compared, because the
spine gives intended bases and the chapters give the proofs. Chapter headings are compared too.

Usage: check_spine_sync.py
Exit status 0 when every spine key is found in exactly one chapter file with the same statement.
"""
import re
import sys
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent
SPINE = SCRATCH / "02-spine.md"
CHAPTERS = sorted(SCRATCH.glob("ch-[0-9][0-9].md"))

KEY = re.compile(r"\{#([a-z]+:[A-Za-z0-9-]+)(?: weakened)?\}\s*$")
ITEM = re.compile(r"^\s*1\.\s+(.*)$")
CAPTION = re.compile(r"^\*Table: (.*)\* \{#(t:[a-z0-9-]+)\}\s*$")
HEADING = re.compile(r"^## (\d+)\. (.*)$")


def statement(text):
    text = KEY.sub("", text).rstrip()
    cut = text.find(" *[")
    if cut >= 0:
        text = text[:cut]
    return text.strip()


def parse(path):
    items = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    buffer = None
    i = 0
    while i < len(lines):
        line = lines[i]
        head = HEADING.match(line)
        if head:
            items.setdefault("heading:" + head.group(1), []).append(head.group(2).strip())
            buffer = None
            i += 1
            continue
        cap = CAPTION.match(line)
        if cap:
            rows = []
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            while j < len(lines) and lines[j].startswith("|"):
                rows.append(lines[j].strip())
                j += 1
            items.setdefault(cap.group(2), []).append(cap.group(1) + "\n" + "\n".join(rows))
            buffer = None
            i = j
            continue
        m = ITEM.match(line)
        k = KEY.search(line)
        if m:
            buffer = [m.group(1)]
        elif buffer is not None and line.startswith("   ") and line.strip():
            buffer.append(line.strip())
        elif line.strip():
            buffer = None
        if k and buffer is not None:
            items.setdefault(k.group(1), []).append(statement(" / ".join(buffer)))
            buffer = None
        i += 1
    return items


def main():
    spine = parse(SPINE)
    chapters = {}
    for path in CHAPTERS:
        for key, texts in parse(path).items():
            chapters.setdefault(key, []).extend((path.name, t) for t in texts)
    problems = 0
    for key, texts in spine.items():
        if len(texts) != 1:
            print("spine defines %s %d times" % (key, len(texts)))
            problems += 1
            continue
        copies = chapters.get(key, [])
        if len(copies) != 1:
            print("%s: found in %d chapter places %s" % (key, len(copies), [c[0] for c in copies]))
            problems += 1
            continue
        name, text = copies[0]
        if text != texts[0]:
            problems += 1
            print("MISMATCH %s (%s)" % (key, name))
            print("  spine:   " + texts[0].replace("\n", " / "))
            print("  chapter: " + text.replace("\n", " / "))
    print("%d spine keys and headings checked, %d problems" % (len(spine), problems))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
