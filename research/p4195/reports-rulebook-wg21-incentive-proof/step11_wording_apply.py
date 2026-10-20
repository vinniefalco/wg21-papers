"""Apply the wording batches by key: kinds, citations, and keys are copied from the current files."""
import importlib.util
import re
from pathlib import Path

S = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof")
B = S / "step11-wording"
START = re.compile(r"^( *)1\. (\*\*\w+\.\*\* )?(.*)$")
END = re.compile(r"\{#([a-z:0-9-]+)(?: weakened)?\}\s*$")
CITES = re.compile(r"\*\[(?:from|proved by)[^\]]*\]\*")


def load():
    new = {}
    for path in sorted(B.glob("batch*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for key, text, note in mod.NEW:
            assert key not in new, "duplicate " + key
            new[key] = (text, note)
    return new


SNAP = S / "snapshots" / "step-11-spine-revised"


def rewrite(path, new, log):
    lines = (SNAP / path.name).read_text(encoding="utf-8").split("\n")
    out, i = [], 0
    while i < len(lines):
        m = START.match(lines[i])
        if not m:
            out.append(lines[i]); i += 1; continue
        j = i
        while not END.search(lines[j]):
            j += 1
        block = lines[i:j + 1]
        key = END.search(lines[j]).group(1)
        if key not in new:
            out.extend(block); i = j + 1; continue
        indent, kind = m.group(1), m.group(2) or ""
        joined = "\n".join(block)
        cites = " ".join(CITES.findall(joined))
        old = CITES.sub("", END.sub("", joined[len(indent) + 3 + len(kind):]))
        old = " ".join(p.strip() for p in old.split("\n") if p.strip())
        text, note = new.pop(key)
        paras = text.split("\n\n")
        tail = (" " + cites if cites else "") + " {#" + key + "}"
        if len(paras) == 1:
            out.append(indent + "1. " + kind + paras[0] + tail)
        else:
            out.append(indent + "1. " + kind + paras[0])
            for para in paras[1:-1]:
                out.extend(["", indent + "   " + para])
            out.extend(["", indent + "   " + paras[-1] + tail])
        log.append("- %s | %s | %s | claim unchanged%s" % (key, old, " ".join(text.split()), ("; " + note) if note else ""))
        i = j + 1
    path.write_text("\n".join(out), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    new = load()
    log = []
    for name in ("01-foundation.md", "02-spine.md"):
        rewrite(S / name, new, log)
    assert not new, "keys not found: %s" % sorted(new)
    head = ["# Step 11 wording changes", "",
            "Wording-only pass over every spine item and the foundation's axioms and definitions. One line per rewritten item: key | old | new | claim unchanged, with a note where the clause mapping is not plain. Kinds, citations, and keys are copied unchanged by `step11_wording_apply.py`.", ""]
    extra = (B / "over-limit.md").read_text(encoding="utf-8") if (B / "over-limit.md").exists() else ""
    (S / "step-11-wording-changes.md").write_text("\n".join(head + log) + "\n" + extra, encoding="utf-8", newline="\n")
    print("rewritten", len(log))
