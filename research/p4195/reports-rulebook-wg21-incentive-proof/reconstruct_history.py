"""Rebuild the Step 7, 8, and 9 working files that were not saved as snapshots at the time.

Step 9: the current files, with the 2026-10-19 02:02 kit sentence removed.
Step 8: Step 9 with each logged Step 9 edit reversed.
Step 7: the copies kept as *-pre-step8.md, with the modules check reduced to Step 7's three modules.
Every reversal must match exactly once. Output goes to scratch history-build/step-NN/.
"""
import re
import sys
from pathlib import Path

SCRATCH = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof")
SUPPORT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support")
OUT = SCRATCH / "history-build"
KEY = re.compile(r"\{#([a-z:0-9-]+)(?: weakened)?\}\s*$")

KIT_SENTENCE = (" Write no children for an item that restates or joins the items it cites, or follows from them"
                " in one step a committee member accepts on sight; its `*[from ...]*` citation is its proof.")
NB_MEMBERS_STEP8 = (
    "1. **Proposition.** A national body decides its position by whatever internal rules its panel uses, which"
    " SD-4 does not state, and ISO asks it to take account of all interests concerned at the national level, so"
    " whether members whose costs one sponsor pays add weight to that sponsor's interests depends on those rules."
    " *[from f:late-info, f:escalate-nb, f:iso-early, ax:who-pays]* {#p:nb-members}")


def once(text, old, new):
    if text.count(old) != 1:
        sys.exit("expected exactly one match for: " + old[:80])
    return text.replace(old, new)


def drop_keys(text, keys):
    kept, dropped = [], 0
    for line in text.split("\n"):
        m = KEY.search(line)
        if m and m.group(1) in keys:
            dropped += 1
            continue
        kept.append(line)
    if dropped != len(keys):
        sys.exit("expected to drop %d keyed lines, dropped %d" % (len(keys), dropped))
    return "\n".join(kept)


def replace_key_line(text, key, new_line):
    lines = text.split("\n")
    hits = [i for i, line in enumerate(lines) if (m := KEY.search(line)) and m.group(1) == key]
    if len(hits) != 1:
        sys.exit("expected one line keyed " + key)
    lines[hits[0]] = new_line
    return "\n".join(lines)


def write(step, name, text):
    folder = OUT / step
    folder.mkdir(parents=True, exist_ok=True)
    (folder / name).write_text(text, encoding="utf-8", newline="\n")


def read(path):
    return Path(path).read_text(encoding="utf-8")


def main():
    kit9 = once(read(SUPPORT / "kit.md"), KIT_SENTENCE, "")
    modules = read(SCRATCH / "check_modules.py")

    # Step 9
    write("step-09", "01-foundation.md", read(SCRATCH / "01-foundation.md"))
    write("step-09", "02-spine.md", read(SCRATCH / "02-spine.md"))
    write("step-09", "02-incentive-map.md", read(SCRATCH / "02-incentive-map.md"))
    write("step-09", "rules-extract.md", read(SUPPORT / "rules-extract.md"))
    write("step-09", "check_modules.py", modules)
    write("step-09", "spine-labeled.md", read(SCRATCH / "spine-labeled.md"))
    write("step-09", "kit.md", kit9)

    # Step 8
    f8 = read(SCRATCH / "01-foundation.md")
    f8 = once(f8, "ISO/IEC Directives Part 1, clauses 0.1 and 0.7, contain these statements. {#f:iso-general}",
              "ISO/IEC Directives Part 1, clause 0.7, contains these statements. {#f:iso-general}")
    f8 = once(f8, "confirms; the edition of the Directives these items search replaces the JTC 1 Supplement, and the"
                  " proof does not search the other documents",
              "confirms; the proof does not search the JTC 1 Supplement or the other documents")
    f8 = once(f8, "state them, in the edition of the Directives that replaces the JTC 1 Supplement. For the United"
                  " States position it also uses INCITS's rules for counting votes.",
              "state them; it does not use the JTC 1 Supplement.")
    f8 = drop_keys(f8, {"f:supplements-replaced", "f:incits", "f:incits-one-vote", "f:incits-organization",
                        "f:incits-limits", "f:incits-position", "f:incits-caucus"})
    s8 = read(SCRATCH / "02-spine.md")
    s8 = replace_key_line(s8, "p:nb-members", NB_MEMBERS_STEP8)
    s8 = drop_keys(s8, {"l:incits-votes"})
    s8 = once(s8, " that chapter 1 quotes, in the edition that replaces the JTC 1 Supplement, and given the axioms,",
              " that chapter 1 quotes, and given the axioms,")
    s8 = once(s8, " m:players, f:supplements-replaced, d:settled-pattern]", " m:players, d:settled-pattern]")
    m8 = once(modules, '    "p:nb-members": ["l:incits-votes"],\n', "")
    write("step-08", "01-foundation.md", f8)
    write("step-08", "02-spine.md", s8)
    write("step-08", "02-incentive-map.md", read(SCRATCH / "02-incentive-map.md"))
    write("step-08", "rules-extract.md", read(SCRATCH / "rules-extract-pre-step9.md"))
    write("step-08", "check_modules.py", m8)
    write("step-08", "kit.md", kit9)

    # Step 7
    m7 = m8
    for line in ('    "m:players": ["p:chair-decides", "p:sponsor-no-vote"],\n',
                 '    "p:record-indistinct": ["l:iso-register-level"],\n',
                 '    "p:large-position": ["l:plenary-priority"],\n'):
        m7 = once(m7, line, "")
    write("step-07", "01-foundation.md", read(SCRATCH / "01-foundation-pre-step8.md"))
    write("step-07", "02-spine.md", read(SCRATCH / "02-spine-pre-step8.md"))
    write("step-07", "02-incentive-map.md", read(SCRATCH / "02-incentive-map-pre-step8.md"))
    write("step-07", "rules-extract.md", read(SCRATCH / "rules-extract-pre-step9.md"))
    write("step-07", "check_modules.py", m7)
    write("step-07", "kit.md", kit9)
    print("rebuilt step-07, step-08, step-09 in " + str(OUT))


if __name__ == "__main__":
    main()
