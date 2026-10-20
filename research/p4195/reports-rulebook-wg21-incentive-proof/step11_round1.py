"""Step 11 refill round 1 integration: rewrite spine items by key and log each change."""
import re
from pathlib import Path

S = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof")
SNAP = S / "snapshots" / "step-11-refill-r1-done"
START = re.compile(r"^( *)1\. (\*\*\w+\.\*\* )(.*)$")
END = re.compile(r"\{#([a-z:0-9-]+)\}\s*$")
FROM = re.compile(r"\*\[from [^\]]*\]\*")
PROVED = re.compile(r"\*\[proved by [^\]]*\]\*")
CITE = re.compile(r"\s*\*\[(?:from|proved by)[^\]]*\]\*")

K = "round 1 integration"
CH = {
    "p:cutoff-effect": ("At the feature cutoff, a one-meeting delay for a paperless rival sends a proposal to the next planned edition. So does an Against vote keeping it below the 2:1 line, when the chair follows the norm.",
        "p:miss-cost, f:no-wait-alternatives, l:vote-count, f:two-to-one, f:plenary-owns, d:edition",
        "weakened to the chapter 10 child: the Against-vote half holds when the chair follows the norm, since SD-4 leaves a call below it to the chair"),
    "p:sg-sponsor": ("Paying participants to attend a study group puts a sponsor's voters where the design the design room starts from is chosen. Where the other voters cast fewer Favor-plus-Against votes, fewer paid participants make up a third of the total, enough to block, or over two thirds, enough to meet the norm.",
        None, "weakened to the chapter 7 child: counted in the other voters' Favor-plus-Against votes, since Neutral voters are not in that total"),
    "p:review-share": ("Close study takes longer the bigger a design is, and a bigger design has more places where a defect can go unnoticed. For a reviewer whose stake does not grow with size, close study therefore stops being worth its time sooner on a big design than on a small one.",
        None, "weakened to the chapter 5 child and stated as the imbalance of study time and stake, not as a threshold that holds by definition"),
    "p:reasons-unrecorded": ("A proposal's case lasts for decades in its required paper, while an unwritten reason survives only with those who heard it and, once they all leave, only by rediscovery. Outside the protected records, an objection's argument survives only in a paper that states it: the objector's own, or an author's paper showing the alternative or defending a declined change.",
        "f:no-paper, ax:turnover, p:dissent-needs-paper, p:record-indistinct, f:show-alternatives, f:direction-implement",
        "weakened to the chapter 4 child and stated positively: an author's paper can also hold the argument when it shows the alternative or defends a declined change"),
    "p:who-takes-part": ("Fees are barred and everyone in a subgroup's room has one vote, yet only those who bear the cost of taking part, or whose sponsors do, vote in WG21's polls. ISO can remove inactive national body experts, and participants propose for needs they and their sponsors know, which, since users differ from them in what matters, need not match users'.",
        "f:no-fee, f:remote, f:iso-cost, f:in-person-expected, f:registered, f:inactive-experts, p:who-votes, ax:cost, ax:who-pays, ax:prefer, ax:users-affected, f:present-required",
        "weakened to the chapter 9 child (no absence fact supports 'exclude no registered expert'), and strengthened by the new fact f:inactive-experts (ISO 1.12.3)"),
    "c:pred-rival-polls": ("After a design passes a direction poll, papers and poll questions on its topic present rivals as changes to it, even when no technical content has changed; poll questions and paper titles are the evidence, and rivals presented as equal alternatives would count against it. An innocent explanation is that the wording tracks the incumbent's real change of status; comparing like rivals in same-form polls before and after incumbency tells them apart.",
        "p:incumbent-start, p:early-polls, p:challenger-bar, f:multiple-polls, thm:settled",
        "weakened per the chapter 12 child: Favor counts are compared only within one poll form, since a change and a side-by-side choice ask different questions"),
    "c:pred-competing": ("If closer study before adoption finds more defects, topics on which competing papers from separate author groups reached the deciding poll show fewer defects after adoption than topics with one paper; author lists, mailings, issues lists, and removals are the evidence, and no difference would count against it. An innocent explanation is that important or well-understood topics draw competing papers and expert attention anyway, and comparing topics of equal novelty and poll turnout tells them apart.",
        "p:review-share, p:review-shortfall, ax:prefer, f:multiple-polls, f:not-vote, thm:settled",
        "weakened per the chapter 12 child: matching on scope dropped, since stakes need not grow with size; turnout measures attention, as those unfamiliar typically do not vote"),
    "c:lever-nb-less": ("If forming national positions during meetings cost more, national bodies would take fewer, plenary would seldom meet opposition holding them, and the whole-document ballot would be their main check. Appeals would remain, on drafts only for questions of principle or harm to ISO's or IEC's reputation, and the model predicts attendance, paid participants, and early incumbency deciding more content.",
        "p:who-decides, p:credible-threat, l:settled-convenor, l:settled-nb, p:sponsor-votes, p:early-polls, m:moves-nb, f:appeal-technical, thm:settled",
        "weakened per the chapter 12 child: 'main' for 'only', naming the appeal route that remains"),
    "l:settled-regular": ("Whatever the others choose, a regular does no better than to vote Favor on colleagues' proposals they support, and on one they doubt, Against does best only when worth more than its added cost. Otherwise Neutral, not voting, or even Favor can do best, since Favor risks nothing with the colleague, while Against costs risk to colleagues' support and time for reasons, and changes the result only one or two votes above the line.",
        "p:against-costs-more, p:doubt-outside-count, l:vote-count, p:objector-coordination, p:prefer-vs-stop, p:mutual-support, p:repeat-objection, p:cutoff-effect, ax:support, ax:prefer, m:moves, d:does-better, d:settled-pattern",
        "doubter clause restated with no new assumption: ax:support lets Neutral or not voting carry some standing risk and gives Favor none"),
}
THM_OLD = "A regular votes Favor on colleagues' proposals they support and otherwise Neutral or not at all, voting Against only for a doubt worth more than that vote's extra cost."
THM_NEW = "A regular votes Favor on colleagues' proposals they support, and Against one they doubt only when that is worth more than its added cost. Otherwise the regular takes whichever of Neutral, not voting, or Favor does best, and Favor risks nothing with the colleague."


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
            old_stmt = statement(lines[i:j + 1])
            block = block.replace(THM_OLD, THM_NEW).replace("*[from l:settled-regular,", "*[from ax:support, l:settled-regular,")
            log.append("- thm:settled | %s | (regular clause) %s | %s | dependent of l:settled-regular; the regular clause restated as in that lemma, with ax:support cited" % (K, THM_OLD, THM_NEW))
        out.extend(block.split("\n"))
    i = j + 1
assert not CH, CH
path.write_text("\n".join(out), encoding="utf-8", newline="\n")
changes = S / "step-11-spine-changes.md"
changes.write_text(changes.read_text(encoding="utf-8").rstrip("\n") + "\n" + "\n".join(log) + "\n", encoding="utf-8", newline="\n")
print("changed", len(log))
