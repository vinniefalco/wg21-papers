"""Step 12 round 2: assemble old and new wording for the ledger from the pre-reconcile snapshot.

Writes r2-ledger-parts.md: the type 4 list with old and new wording, the foundation changes,
and the spine changes with the findings behind each. The ledger section quotes from it.
"""
import re
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import check_spine_sync  # noqa: E402
import r2_generate  # noqa: E402
import r2_spine_apply  # noqa: E402

SNAP = S / "snapshots" / "step-12-pre-reconcile-r2"


def items(path):
    """key -> full item text, for foundation-style single-line items."""
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.search(r"\{#([a-z]+:[A-Za-z0-9-]+)\}\s*$", line)
        if m:
            t = re.sub(r"^\s*1\.\s+\*\*[A-Za-z]+\.\*\*\s", "", line)
            out[m.group(1)] = t[: t.rfind(" {#")]
    return out


def stmt(text):
    cut = text.find(" *[")
    return text[:cut] if cut >= 0 else text


def chapter_items(paths):
    out = {}
    for path in paths:
        out.update(items(path))
    return out


def clean(text):
    return re.sub(r"^\*\*[A-Za-z]+\.\*\* ", "", text.replace("\n", " / "))


def main():
    findings, order = r2_generate.load_findings()
    dec = r2_generate.load_decisions()
    old_spine = check_spine_sync.parse(SNAP / "02-spine.md")
    new_spine = check_spine_sync.parse(S / "02-spine.md")
    old_f = items(SNAP / "01-foundation.md")
    new_f = items(S / "01-foundation.md")
    old_ch = chapter_items(sorted(SNAP.glob("ch-[0-9][0-9].md")))
    lines = ["# Round 2 reconcile: wording for the ledger", ""]

    lines += ["## Type 4 fixes", ""]
    for fid in order:
        d = dec[fid]
        if d["type"] != "4" or d["status"] not in "AS":
            continue
        key = findings[fid][2]
        if d["status"] == "A":
            old = clean(old_spine[key][0]) if key in old_spine else stmt(old_f.get(key, "?"))
            new = clean(new_spine[key][0]) if key in new_spine else stmt(new_f.get(key, "?"))
            lines.append("- %s %s: applied. Old: \"%s\" New: \"%s\"" % (fid, key, old, new))
        else:
            old = stmt(old_ch.get(key, "?"))
            lines.append("- %s %s: sent to fix-r2-ch%s.md. Old: \"%s\" Fix: %s" % (fid, key, d["ch"], old, d["note"]))

    lines += ["", "## Foundation changes", ""]
    for key in new_f:
        if key not in old_f:
            lines.append("- %s (new): \"%s\"" % (key, stmt(new_f[key])))
        elif stmt(old_f[key]) != stmt(new_f[key]):
            lines.append("- %s. Old: \"%s\" New: \"%s\"" % (key, stmt(old_f[key]), stmt(new_f[key])))

    lines += ["", "## Spine changes", ""]
    changed = list(r2_spine_apply.NEW) + list(r2_spine_apply.CAPTIONS) + ["thm:settled"]
    for key in changed:
        ids = [fid for fid in order if findings[fid][2] == key and dec[fid]["status"] in "ASM"]
        old = clean(old_spine[key][0]) if key in old_spine else "?"
        lines.append("- %s (%s). Old: \"%s\"" % (key, ", ".join(ids) if ids else "follow-on", old if key != "thm:settled" else "see snapshot step-12-pre-reconcile-r2"))
    for key, adds in r2_spine_apply.ADD_FROM.items():
        if key not in changed:
            lines.append("- %s: basis adds %s" % (key, ", ".join(adds)))
    for key in r2_spine_apply.CUT_ITEMS:
        lines.append("- %s: cut (global decision 4b)" % key)
    (S / "r2-ledger-parts.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("wrote r2-ledger-parts.md, %d lines" % len(lines))


if __name__ == "__main__":
    main()
