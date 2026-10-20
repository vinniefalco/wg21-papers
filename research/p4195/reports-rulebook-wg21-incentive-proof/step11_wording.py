"""Step 11 wording pass: measure sentences, and apply new statements by key without touching kinds, citations, or keys."""
import re
import sys
from pathlib import Path

S = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof")
START = re.compile(r"^( *)1\. (.*)$")
END = re.compile(r"\s*\{#([a-z:0-9-]+)(?: weakened)?\}\s*$")
KIND = re.compile(r"^\*\*(\w+)\.\*\* ")
CITE = re.compile(r"\s*\*\[(?:from|proved by)[^\]]*\]\*")
SPLIT = re.compile(r"(?<=[.?!])\s+(?=[A-Z\"(])")


def items(path, kinds=None):
    """Yield (key, kind, statement) for each item; statements have citations stripped."""
    buf = None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        m = START.match(line)
        if m and buf is None:
            buf = m.group(2)
        elif buf is not None and line.strip():
            buf += "\n" + line.strip()
        if buf is not None:
            e = END.search(buf)
            if e:
                k = KIND.match(buf)
                kind = k.group(1) if k else ""
                text = CITE.sub("", END.sub("", KIND.sub("", buf))).strip()
                if kinds is None or kind in kinds:
                    yield e.group(1), kind, text
                buf = None


def sentences(text):
    out = []
    for para in text.split("\n"):
        out.extend(s for s in SPLIT.split(para.strip()) if s)
    return out


def scope():
    found = list(items(S / "01-foundation.md", {"Axiom", "Definition"}))
    spine = list(items(S / "02-spine.md"))
    return found + spine


def measure(label):
    rows = scope()
    lens, over, long_items = [], [], []
    for key, kind, text in rows:
        sents = sentences(text)
        if kind != "Theorem" and len(sents) > 2:
            long_items.append((key, len(sents)))
        for s in sents:
            n = len(s.split())
            lens.append(n)
            if n > 30:
                over.append((key, n))
    print(f"{label}: items {len(rows)}, sentences {len(lens)}, average {sum(lens)/len(lens):.1f}, longest {max(lens)}")
    print(f"  sentences over 30: {len(over)}; items over two sentences (not Theorem): {long_items}")
    return over


if __name__ == "__main__":
    over = measure(sys.argv[1] if len(sys.argv) > 1 else "now")
    if "--list" in sys.argv:
        for key, n in sorted(over, key=lambda x: -x[1]):
            print(f"  {key}={n}")
