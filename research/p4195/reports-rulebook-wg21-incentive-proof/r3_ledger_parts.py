"""Step 12 round 3: assemble old and new wording for the ledger from the pre-reconcile snapshot.

Writes r3-ledger-parts.md: the type 4 list with old and new wording, the foundation changes,
and the spine changes with the findings behind each. The ledger section quotes from it.
"""
import re
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import check_spine_sync  # noqa: E402
import r3_generate  # noqa: E402
import r3_spine_apply  # noqa: E402

SNAP = S / "snapshots" / "step-12-pre-reconcile-r3"

# Type 4 findings whose applied change is to spine statements other than the finding's own key,
# and the Theorem sentence substitution (by index in THEOREM_SUBS) a Theorem finding made.
TYPE4_SPINE = {
    "12.3R6": ["p:users-out"],
    "12.3L14": ["c:pred-parts"],
    "12.3L16": ["c:pred-nb-positions", "c:lever-nb-less"],
}
TYPE4_THEOREM = {"12.3L8": 1}


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


def clean(text):
    return re.sub(r"^\*\*[A-Za-z]+\.\*\* ", "", text.replace("\n", " / "))


def main():
    findings, order = r3_generate.load_findings()
    dec = r3_generate.load_decisions()
    old_spine = check_spine_sync.parse(SNAP / "02-spine.md")
    new_spine = check_spine_sync.parse(S / "02-spine.md")
    old_f = items(SNAP / "01-foundation.md")
    new_f = items(S / "01-foundation.md")
    old_ch = {}
    for path in sorted(SNAP.glob("ch-[0-9][0-9].md")):
        old_ch.update(items(path))
    lines = ["# Round 3 reconcile: wording for the ledger", ""]

    lines += ["## Type 4 fixes", ""]
    for fid in order:
        d = dec[fid]
        if d["type"] != "4" or d["status"] not in "AS":
            continue
        key = findings[fid][2]
        if fid in TYPE4_THEOREM:
            o, n = r3_spine_apply.THEOREM_SUBS[TYPE4_THEOREM[fid]]
            lines.append("- %s %s: applied to the Theorem's sentence. Old: \"%s\" New: \"%s\"" % (fid, key, o, n))
        elif d["status"] == "A" and key in new_spine:
            lines.append("- %s %s: applied. Old: \"%s\" New: \"%s\"" % (fid, key, clean(old_spine[key][0]), clean(new_spine[key][0])))
        elif d["status"] == "A" and key in new_f:
            lines.append("- %s %s: applied. Old: \"%s\" New: \"%s\"" % (fid, key, stmt(old_f[key]), stmt(new_f[key])))
        elif d["status"] == "S":
            lines.append("- %s %s: sent to fix-r3-ch%s.md. Old: \"%s\" Fix: %s" % (fid, key, d["ch"], stmt(old_ch.get(key, "?")), d["note"]))
        else:
            lines.append("- %s %s: applied through the spine statements below; the chapter step follows in its fix file." % (fid, key))
        for skey in TYPE4_SPINE.get(fid, []):
            lines.append("  - %s. Old: \"%s\" New: \"%s\"" % (skey, clean(old_spine[skey][0]), clean(new_spine[skey][0])))

    lines += ["", "## Foundation changes", ""]
    for key in new_f:
        if key not in old_f:
            lines.append("- %s (new): \"%s\"" % (key, stmt(new_f[key])))
        elif stmt(old_f[key]) != stmt(new_f[key]):
            lines.append("- %s. Old: \"%s\" New: \"%s\"" % (key, stmt(old_f[key]), stmt(new_f[key])))

    lines += ["", "## Spine changes", ""]
    changed = list(r3_spine_apply.NEW) + list(r3_spine_apply.CAPTIONS) + ["thm:settled"]
    for key in changed:
        ids = [fid for fid in order if findings[fid][2] == key and dec[fid]["status"] in "ASM"]
        old = clean(old_spine[key][0]) if key in old_spine else "?"
        if key == "thm:settled":
            subs = "; ".join("\"%s\" became \"%s\"" % (o, n) for o, n in r3_spine_apply.THEOREM_SUBS)
            lines.append("- thm:settled (%s): sentence substitutions: %s" % (", ".join(ids) if ids else "follow-on", subs))
        else:
            lines.append("- %s (%s). Old: \"%s\"" % (key, ", ".join(ids) if ids else "follow-on", old))
    for key, adds in r3_spine_apply.ADD_FROM.items():
        if key not in changed:
            lines.append("- %s: basis adds %s" % (key, ", ".join(adds)))
    (S / "r3-ledger-parts.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("wrote r3-ledger-parts.md, %d lines" % len(lines))


if __name__ == "__main__":
    main()
