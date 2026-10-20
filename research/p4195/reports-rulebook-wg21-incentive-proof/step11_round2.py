"""Step 11 refill round 2 integration: rewrite spine items by key and log each change."""
import re
from pathlib import Path

S = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof")
START = re.compile(r"^( *)1\. (\*\*\w+\.\*\* )(.*)$")
END = re.compile(r"\{#([a-z:0-9-]+)\}\s*$")
FROM = re.compile(r"\*\[from [^\]]*\]\*")
PROVED = re.compile(r"\*\[proved by [^\]]*\]\*")
CITE = re.compile(r"\s*\*\[(?:from|proved by)[^\]]*\]\*")

K = "round 2 integration"
CH = {
    "p:integration": ("Papers approved separately at one meeting first come together when the project editor merges their wording, which the editor's report records and a pre-ballot editing committee verifies. No SD-4 step checks whether the designs work together, while each author gains from their own design's adoption and a conflict costs users and later rework.",
        "f:approval-polls, f:wording-baseline, f:editors, f:no-integration-check, ax:prefer, ax:unknown, ax:users-affected, ax:rework",
        "weakened to the ledger's wording, with two exactness fixes: 'one meeting', since new wording is written against drafts that already hold earlier papers, and 'SD-4', the scope of the absence search; the nearest-steps list is replaced by the merge, report, and verification steps, and f:early-merge moves to l:checks-deadlock"),
    "p:reasons-unrecorded": ("A proposal's case lasts for decades in its required paper, while an unwritten reason survives only with those who heard it and, once they all leave, only by rediscovery. Outside the protected records, an objection's argument outlasts its hearers only in writing, such as the objector's paper or an author's paper showing the alternative or defending a declined change.",
        None, "weakened to the chapter 4 child: any writing, a third party's included, can hold the argument; the two papers are examples"),
    "p:incumbent-start": ("A design passing a design room's direction poll becomes the incumbent, a paperless rival cannot block it, and the chair may delay it one meeting for a paper to arrive. A rival with a paper can be polled alongside it, the room can direct changes, and by default a TS merge proceeds with it unless an alternative is actively progressing.",
        None, "scoped to design rooms, as d:incumbent counts only their direction polls (chapter 5 note)"),
    "l:poll-wording": ("A direction poll asks voters only to agree that work should continue, less than a forwarding poll asks, so it can pass where a forwarding poll would fail. Yet passing it in a design room makes the design the incumbent.",
        None, "dependent of the scoped p:incumbent-start: incumbency comes only from a design room's direction poll"),
    "c:pred-rival-polls": ("After a design passes a design room's direction poll, papers and poll questions on its topic present rivals as changes to it, even when no technical content has changed; poll questions and paper titles are the evidence, and rivals presented as equal alternatives would count against it. An innocent explanation is that the wording tracks the incumbent's real change of status; comparing like rivals in same-form polls before and after incumbency tells them apart.",
        None, "dependent of the scoped p:incumbent-start: the prediction concerns designs that became incumbents"),
    "l:checks-deadlock": ("Competing TSs are possible, a TS or white paper should list the controversial issues to address before it merges, and SD-4 expects pre-merge issues to be addressed. Implementation experience informs voters, a TS can merge early for integration testing, a white paper has no prescribed schedule, and the schedule keeps an unfinished feature from delaying ready ones.",
        "f:competing-ts, f:ts-exit-criteria, f:pre-merge, f:early-merge, l:implementation-informs, f:white-paper-process, p:miss-cost",
        "strengthened: adds the early TS merge for integration testing (f:early-merge), which p:integration no longer cites; 'planned schedule' is 'schedule'"),
}
THM_OLD = "No step checks whether separately adopted designs work together,"
THM_NEW = "No SD-4 step checks whether separately adopted designs work together,"


def statement(block):
    text = START.match(block[0]).group(3) + "".join(" " + l.strip() for l in block[1:])
    return " ".join(CITE.sub("", END.sub("", text)).split())


path = S / "02-spine.md"
lines = path.read_text(encoding="utf-8").split("\n")
out, log, i = [], [], 0
while i < len(lines):
    m = START.match(lines[i])
    if not m:
        out.append(lines[i]); i += 1; continue
    j = i
    while not END.search(lines[j]):
        j += 1
    key = END.search(lines[j]).group(1)
    if key in CH and j == i:
        line = lines[i]
        text, frm, note = CH.pop(key)
        cites = " ".join(PROVED.findall(line) + ([("*[from %s]*" % frm)] if frm else FROM.findall(line)))
        log.append("- %s | %s | %s | %s | %s" % (key, K, statement([line]), text, note))
        out.append(m.group(1) + "1. " + m.group(2) + text + " " + cites + " {#" + key + "}")
    else:
        block = "\n".join(lines[i:j + 1])
        if key == "thm:settled":
            assert block.count(THM_OLD) == 1
            block = block.replace(THM_OLD, THM_NEW)
            log.append("- thm:settled | %s | (integration sentence) %s ... | %s ... | dependent of p:integration: scoped to SD-4, the scope of the absence search" % (K, THM_OLD, THM_NEW))
        out.extend(block.split("\n"))
    i = j + 1
assert not CH, CH
path.write_text("\n".join(out), encoding="utf-8", newline="\n")
changes = S / "step-11-spine-changes.md"
changes.write_text(changes.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(log) + "\n", encoding="utf-8", newline="\n")
print("changed", len(log))
