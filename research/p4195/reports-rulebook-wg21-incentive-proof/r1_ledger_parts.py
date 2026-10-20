"""Step 12 round 1: assemble old and new wording for the ledger from the pre-reconcile snapshot.

Writes r1-ledger-parts.md: the type 4 list with old and new wording, the foundation changes,
and the spine changes with the findings behind each. The ledger section quotes from it.
"""
import re
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import check_spine_sync  # noqa: E402
import r1_generate  # noqa: E402
import r1_spine_apply  # noqa: E402

SNAP = S / "snapshots" / "step-12-pre-reconcile-r1"
HEADLINE = {
    "p:early-polls", "l:poll-wording", "ind:reversal-grows", "p:challenger-bar", "p:burden-flip", "l:settled-design-bound",
    "p:fluency", "p:newcomer", "p:late-objection", "p:chair-confidence", "p:light-review", "p:review-share",
    "p:least-cost-response", "p:against-costs-more", "p:doubt-outside-count", "p:mutual-support", "p:who-votes",
    "p:users-out", "p:who-takes-part", "p:reward-timing", "p:prefer-is", "l:settled-user", "p:who-decides",
    "p:sponsor-votes", "p:sg-sponsor", "p:deadlock", "p:attrition", "p:merit-gap", "l:consensus-test",
    "p:persuasion-not-required", "p:record-indistinct", "p:reasons-unrecorded", "p:dissent-needs-paper",
    "p:integration", "p:review-shortfall", "p:disclosure", "p:same-moves", "t:disclose", "p:first-part", "p:parts",
    "ind:adopted-parts", "l:vote-count", "p:sg-decides", "p:chair-threshold", "p:miss-cost", "l:settled-regular",
    "c:predictions",
}


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


def main():
    findings, order = r1_generate.load_findings()
    dec = r1_generate.load_decisions()
    old_spine = check_spine_sync.parse(SNAP / "02-spine.md")
    new_spine = check_spine_sync.parse(S / "02-spine.md")
    old_f = items(SNAP / "01-foundation.md")
    new_f = items(S / "01-foundation.md")
    lines = ["# Round 1 reconcile: wording for the ledger", ""]

    lines += ["## Type 4 fixes", ""]
    for fid in order:
        d = dec[fid]
        if d["type"] != "4" or d["status"] not in "AS":
            continue
        key = findings[fid][2]
        tags = []
        if key in HEADLINE:
            tags.append("headline")
        if key.startswith("l:settled-"):
            tags.append("settled lemma")
        if key == "thm:settled":
            tags.append("Theorem")
        tag = " [%s]" % ", ".join(tags) if tags else ""
        if d["status"] == "A":
            if key in old_spine:
                old = old_spine[key][0]
                new = new_spine.get(key, ["(cut)"])[0]
            else:
                old = stmt(old_f.get(key, "?"))
                new = stmt(new_f.get(key, "?"))
            lines.append("- %s %s%s: applied. Old: \"%s\" New: \"%s\"" % (fid, key, tag, re.sub(r"^\*\*[A-Za-z]+\.\*\* ", "", old.replace("\n", " / ")), re.sub(r"^\*\*[A-Za-z]+\.\*\* ", "", new.replace("\n", " / "))))
        else:
            lines.append("- %s %s%s: sent to fix-r1-ch%s.md. Fix: %s" % (fid, key, tag, d["ch"], d["note"]))

    lines += ["", "## Foundation changes", ""]
    for key in new_f:
        if key not in old_f:
            lines.append("- %s (new): \"%s\"" % (key, stmt(new_f[key])))
        elif stmt(old_f[key]) != stmt(new_f[key]):
            lines.append("- %s. Old: \"%s\" New: \"%s\"" % (key, stmt(old_f[key]), stmt(new_f[key])))

    lines += ["", "## Spine changes", ""]
    changed = list(r1_spine_apply.NEW) + list(r1_spine_apply.CAPTIONS) + ["thm:settled"]
    for key in changed:
        ids = [fid for fid in order if findings[fid][2] == key and dec[fid]["status"] == "A"]
        ids += [fid for fid in order if dec[fid]["status"] == "M" and findings[fid][2] == key]
        lines.append("- %s: %s" % (key, ", ".join(ids) if ids else "follow-on of a foundation or scope change"))
    lines.append("- l:incits-positions (new spine child of p:nb-members): 12.1D68, 12.1A31, 12.1L37")
    lines.append("- l:vote-below, l:vote-above, t:vote-choice (cut): 12.1D19 to 12.1D23")
    lines.append("- heading of chapter 5: 12.1D40")
    (S / "r1-ledger-parts.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("wrote r1-ledger-parts.md, %d lines" % len(lines))


if __name__ == "__main__":
    main()
