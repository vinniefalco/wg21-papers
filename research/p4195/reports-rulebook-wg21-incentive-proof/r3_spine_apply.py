"""Step 12 round 3 reconcile: apply spine statement changes to 02-spine.md and the chapter copies.

Every statement change is written once here and applied to both files, so the copies stay
word for word identical. Basis additions are applied to both files too. The Theorem is changed
by sentence substitutions, each of which must match exactly once in each copy.
Run once; it refuses to run if the Theorem already has its round 3 wording.
"""
import re
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
SPINE = S / "02-spine.md"
CHAPTERS = sorted(S.glob("ch-[0-9][0-9].md"))

NEW = {
    # chapter 2
    "m:moves-regular": "A regular can attend or not, study a paper or not, speak, and vote Favor, Neutral, or Against, or not at all. A regular can also write a paper or file an issue, raise a concern with a chair or on the email lists, comment on minutes, and seek a national position.",
    "m:moves-chair": "Any chair can choose the polls, order the agenda by SD-4's priorities, re-poll after discussion, ask Against voters for reasons, and allow early, limited exploration of alternatives. Each chair can call consensus on its subgroup's polls, and design room chairs can also time-box a new proposal or delay one a meeting for a paperless rival.",
    "m:moves-convenor": "The convenor can appoint chairs, form study groups, invite a guest for up to two meetings, take any plenary polls, and make plenary consensus calls. The convenor can also ask in plenary whether Against votes are personal or national body positions, see outcomes documented, address comments on minutes, and review participation.",
    "m:moves-user": "A user casts no vote in WG21's polls or ballots but can give feedback on a TS or white paper or write a paper a qualified and prepared participant presents. A user can raise their interests with a national body, which ISO asks to weigh all national interests, vote on its position where its rules allow, or become a participant.",
    # chapter 3
    "p:doubt-outside-count": "On a colleague's proposal they doubt, a regular does better voting Against only when the change that vote can make outweighs the standing and time it costs. Counted alone, an Against vote changes the result only at one or two votes above the 2:1 threshold, but discussing its concerns can change other votes or the design.",
    # chapter 4
    "p:definition-without-procedure": "SD-4 adopts ISO's definition of consensus, marked by no sustained opposition, but names no step for judging or registering one, or criteria for an important part of the concerned interests. SD-4's steps for an objection include the 2:1 norm, Against voters' reasons on request, escalation, and plenary's 3-way poll and national-position question.",
    "p:reasons-unrecorded": "A proposal's case lasts for decades in its required paper, while an unwritten reason is kept only in the memory of those who heard it. SD-4 asks whoever raises a concern to see an issue filed or a paper written, and outside the protected records only writing keeps an objection's argument after its hearers leave.",
    "p:repeat-objection": "In SD-4's terms, a heard objector insisting after a consensus call that work cannot proceed, without new information or allowed escalation, is not accepting a group decision, answered or not. SD-4 describes likewise a ballot comment repeating an objection decided with its national body present and heard, unless it brings new information or the body always warned of a No.",
    "p:fluency": "Every design needs more than merit to be considered: a proposal needs an on-time paper and a presenter, a rival a paper to exist, and objections fixed forms and times. Other things equal, whoever knows more of how the committee applies them, some of it learned only by attending, has the better chance of adoption, whatever their design skill.",
    # chapter 5
    "p:late-arrival": "An objector who arrives after a design is adopted needs a paper or ballot comment meeting the 2:1 norm, against a reversal cost that grows as more is built. The record keeps the design's case, while unwritten objections are kept only in memory.",
    # chapter 6
    "p:sponsor-votes": "Each participant a sponsor pays to attend has a vote in the room and values its interests, and no rule limits how many it pays. Each is appointed by a national body or liaison that chooses whom to appoint, SC22 may cap only how many each appoints, and at SC22 each national body counts once.",
    "p:first-part": "A first part fixing a design's structure can be adopted before reviewers can study in detail what later parts need, and every rival to that structure must then replace it. SD-4 asks no paper to state those needs, and the smallest part fixing the structure that can pass is reviewed soonest, so a design-bound author does best proposing it first.",
    # chapter 7
    "l:sg-attendance": "A participant can attend only one of the rooms meeting at the same time, and votes and speaks only there. So when a study group meets alongside other rooms, its voters are those for whom its topic outweighs them.",
    # chapter 8
    "l:call-above": "In the case the table below describes, a chair ranks declaring consensus above declining on a count above 2:1 after discussion.",
    "p:plenary-ratifies": "At plenary, design stays with the design rooms, SD-4 says objections not escalated in time should get no weight, and all present are asked for serious design concerns. SD-4 says most polls pass by unanimous consent, and when opposition is significant the convenor usually asks whether Against votes are personal or national body positions.",
    # chapter 9
    "p:users-out": "No user votes, and taking part costs the participant or their sponsor, while a better design's gain is spread across all users and seldom depends on one user's effort. Users' interests affect decisions only through what participants value, papers a participant presents, TS feedback, and ISO member bodies, which form positions only where that is worth their members' time.",
    # chapter 10
    "l:incits-votes": "INCITS gives each organization one voting membership, the Defense Department up to four on technical committees and groups, and on its Executive Board counts a controlled entity with its controller. It admits a consultant as a voting member only if no voting member funds it, and lets standards developing organizations and consortia be represented by other voting members' employees.",
    "p:nb-members": "A national body forms its position by its panel's own rules, which SD-4 does not state, so whether a sponsor's paid participants add weight there depends on those rules. In the United States, INCITS gives each organization one voting membership, with a Defense Department exception, no vote to consultants a voting member funds, and binds delegates to official positions.",
    # chapter 11
    "l:settled-regular": "In a poll on one proposal, whatever the others choose, a regular does best voting Favor on colleagues' proposals they support. On one they doubt, Against does best only when the change it can make outweighs the standing and time it costs, and otherwise Neutral, not voting, or Favor does best.",
    "l:settled-user": "Whatever the others choose, a user without a sponsor does best taking part only when their own stakes in its polls outweigh the full price, which they bear alone. Otherwise the best move is a cheaper one or none: TS feedback, a paper a participant presents, or a move through a national body.",
    "l:checks-alternatives": "Chairs may allow early, limited exploration of alternatives, and SD-4 encourages side-by-side polls and asks a good paper for alternatives considered, design principles, and motivating examples from today's code. Followup and rebuttal papers can be considered, an author who declines a directed change should defend that decision, and SD-4 does not significantly delay concrete proposals to wait for alternatives.",
    # chapter 12
    "c:pred-sponsor-against": "Where one sponsor pays a proposal's authors and many participants present, and its interests include adoption, the model predicts a smaller Against share of non-author Favor-plus-Against votes than elsewhere. No smaller share would count against it, and votes of participants who move to a sponsor whose interests exclude the proposal would tell it apart from shared technical views.",
    "c:pred-abstention-length": "The model predicts that revisions adding more length draw fewer votes, relative to other papers polled at the same meetings, among revisions at the same place in their sequences. No such fall would count against it, and holding sequence place and poll form fixed sets aside a proposal's aging, changing stakes, and narrower topics fewer participants know.",
    "c:pred-parts": "The model predicts that large proposals tend to arrive as sequences of papers, each building on adopted parts, and large proposals mostly adopted in one paper would count against it. Another explanation, easier review in parts, gives little reason to omit from a first paper what later parts need of it, an omission the model predicts for design-bound authors.",
    "c:pred-first-part": "In the mailings, the model predicts first papers of small scope that omit a design's later parts, more often where the authors' stated sponsor has interests depending on its features. No such omissions would count against it, and another explanation, that small first steps lower risk, gives no reason to omit any mention of later parts that already exist.",
    "c:pred-removals": "The model predicts rare removals after adoption, likelier when national bodies whose No votes could fail a ballot oppose the design, and frequent narrow-margin removals would count against it. Another explanation is that adopted designs rarely need removal, and the share of failed removal polls outside ballot comment resolution with more Favor than Against votes would tell them apart.",
    "c:pred-small-fade": "Per meeting spent waiting behind priority work, the model predicts more stops without a negative poll for self-funded authors' proposals than for sponsored authors' proposals of similar length. No such difference would count against it, and stops rising after a waiting author's sponsor leaves WG21 altogether would tell it apart from another explanation, dropping on reflection.",
    "c:pred-nb-positions": "The model predicts that a national body states more positions on proposals decided at meetings in its own country, where its experts attend in person and forming one costs less. No such difference would count against it, and another explanation, agreement with most proposals, predicts none; vetted ballot comments on matters still open to them are the evidence.",
    "c:pred-written-answers": "The model predicts that papers advancing over Against votes often leave unstated the objections other published papers raised against them, and routine answers would count against it. Another explanation is that the objections were answered in discussion, and a larger unanswered share among omitted than stated objections, in chairs' plenary summaries, would tell them apart.",
    "c:pred-defects": "If some unresolved objections point to real defects, then at equal turnout the model predicts more defects found after adoption in features forwarded over Against votes than with none. No difference would count against the model or that condition, and matching features on scope, novelty, prior implementation, and use tells it apart from the scrutiny novelty or use brings.",
    "c:pred-competing": "If closer study finds more defects, the model predicts fewer post-adoption defects on topics whose deciding poll had competing papers from separate author groups than on one-paper topics. No difference would count against it; another explanation is that important or well-understood topics draw rivals and attention anyway, and matching scope, size, implementation experience, and turnout tells them apart.",
    "c:lever-reasons-all": "If SD-4 asked every voter to be ready to give reasons on request, Neutral and Favor would bear the reasons cost Against now bears, and not voting none. The model predicts fewer Neutral votes, fewer Favor votes from doubters and from supporters whose vote seldom changes the result, and more participants not voting.",
    "c:lever-sponsor-limit": "If the rules limited how many participants one sponsor pays may vote in a subgroup, the votes cast there by participants valuing its interests would be capped. The model predicts that, once the limit applies, margins fall for proposals whose authors one sponsor pays beyond it, relative to those with as many authors paid by separate sponsors.",
    "c:lever-written-answer": "If the rules required a written answer to each objection in a public record, every objection would be in public writing whatever the paper says. The model predicts that papers advancing over Against votes would state the objections they faced.",
    "c:lever-deadlock-rule": "If the rules set a decision procedure for deadlocks lasting a set number of meetings, no group would bear the cost of holding through a deadlock for longer. The model predicts fewer deadlocks that end when one side stops attending.",
    "c:lever-sustained-procedure": "If SD-4 adopted ISO's steps for assessing, registering, and addressing a sustained opposition, and added a recorded answer, a declared opposition left unresolved would be registered in writing. The model predicts registered oppositions in WG21's records.",
    "c:lever-nb-more": "If forming national positions during meetings cost less, national bodies would take more, and more plenary opposition would hold positions whose weight SD-4's procedure leaves to the convenor. For objections backed by bodies whose No votes could fail a ballot, the model predicts larger changes in answer and slower progress, outside documents out for ballot or comment.",
    "c:lever-nb-less": "If forming national positions during meetings cost more, national bodies would take fewer, and fewer plenary objections would hold them. Their ballot vote would be their only move counting directly toward stopping a document on any ground, and the model predicts attendance, paid participants, and early incumbency deciding more content.",
}

CAPTIONS = {
    "t:mutual-support": "Two regulars, each with a proposal pending, each of which lowers what the other values by less than the cost of opposing it. For each, the other's opposition costs more than their own opposing does. Refrains means votes Favor, Neutral, or not at all. First number: A's rank. Second number: B's rank. 4 is best. \u2020 marks a Pareto-optimal cell: no other cell gives one regular a higher rank without giving the other a lower one.",
    "t:hold-or-yield": "Two groups in a deadlock, with equal stakes in their own designs. Group A's sponsors pay its participants' costs and value its holding above what they pay, while group B's participants pay their own. Holding through the deadlock costs group A less than half its stake and group B more than half. A deadlock both hold ends with either design equally likely, and both yielding means a compromise worth half its stake to each. First number: group A's rank. Second number: group B's rank. 4 is best. \u2020 marks a Pareto-optimal cell: no other cell gives one group a higher rank without giving the other a lower one.",
    "t:chair-call": "A chair's consensus call, when the chair's stake in the proposal is worth less to them than what departing from the 2:1 norm can cost them. Neutral votes are short of a majority of those voting, the chair finds no sustained opposition, and a re-poll fits the norm at any count. Columns: the count after discussion of the Against voters' concerns. Each cell: the chair's rank of the call. 2 is best within each column.",
    "t:nb-ballot": "A national body's ballot vote. Columns: how the body values the document. \"Values the rest\" means it values publishing the rest of the document on schedule above removing any one feature through a failed ballot and a revised draft SC22 may produce. It also expects its comments to fare the same under any vote, as SD-4 says. \"Opposes the work\" means it does not want the work at all. In both, its No is accompanied by comments of a technical nature, and it cannot rule out that its vote decides the result. Each cell: its rank of the vote. 3 is best within each column.",
    "t:disclose": "An author's choice, before an early direction poll, whether to state in the paper a trade-off no reviewer would otherwise raise. Stating it would lead the room to change a feature a design-bound author's gain depends on, in a way that serves users better. Writing the statement takes time worth less to a result-seeking author than the better design it brings. The proposal meets the 2:1 norm either way. Columns: the author's type. Each cell: the author's rank of the choice. 2 is best within each column.",
}

THEOREM_SUBS = [
    ("A regular votes Favor on colleagues' proposals they support, and Against one they doubt only when the change that vote can make outweighs the standing and time it costs.",
     "In a poll on one proposal, a regular votes Favor on colleagues' proposals they support. They vote Against one they doubt only when the change that vote can make outweighs the standing and time it costs."),
    ("A sponsor pays for participants where the decisions it values are made, study groups included.",
     "A sponsor pays for participants where the decisions it values are made, study groups included, while what they bring it is worth their cost."),
    ("These include a result-seeking author's vehicle request, a design room chair's one-meeting delay, the convenor's call where SD-4 leaves it open, and whether to study a paper.",
     "These include a result-seeking author's vehicle request, a design room chair's one-meeting delay, any call SD-4 leaves to a chair or the convenor, and whether to study a paper."),
    ("No user votes, and the needs that reach a vote are those participants and their sponsors know, which need not match those of users at large.",
     "No user votes in WG21's polls or ballots, and the needs put to a vote are those participants and sponsors know, which need not match those of users at large."),
    ("No SD-4 step checks whether separately adopted designs work together, and review worth its cost to users together but not to any one participant goes undone.",
     "No SD-4 step checks whether separately adopted designs work together, and no player does review worth its cost to users together but not to any one participant."),
]
THEOREM_GUARD = "any call SD-4 leaves to a chair or the convenor"

ADD_FROM = {
    "m:moves-regular": ["f:report-early", "f:report-followup", "f:escalate-deadline", "f:minutes-objections"],
    "m:moves-convenor": ["f:minutes-objections", "f:inactive-experts"],
    "m:moves-user": ["f:incits-one-vote", "f:incits-organization", "f:incits-position"],
    "p:doubt-outside-count": ["f:two-to-one", "ax:attention"],
    "p:chair-default": ["d:rooms"],
    "l:call-above": ["d:rooms"],
    "l:call-below": ["d:rooms"],
    "p:users-out": ["f:all-nbs-vote", "d:national-body"],
    "c:pred-first-part": ["d:design-bound"],
    "c:pred-removals": ["f:near-unanimous"],
    "c:pred-nb-positions": ["ax:cost", "f:ballot-decided"],
    "c:pred-written-answers": ["f:plenary-reason", "f:protected"],
    "c:pred-competing": ["ax:unknown"],
    "c:lever-written-answer": ["f:protected"],
    "c:lever-nb-more": ["f:ballot-discussion"],
    "c:lever-nb-less": ["f:agenda-notice"],
}

BASIS = re.compile(r"\s*\*\[(proved by|from) ([^\]]*)\]\*")
ITEM = re.compile(r"^(\s*1\.\s+\*\*[A-Za-z]+\.\*\*\s)(.*)$")


def split_line(line):
    """Return (prefix, statement, bases list of (kind, keys), key_text) for an item line with a key."""
    m = re.search(r"\s*(\{#[a-z]+:[A-Za-z0-9-]+(?: weakened)?\})\s*$", line)
    key_text = m.group(1)
    body = line[: m.start()]
    first = body.find(" *[")
    if first < 0:
        stmt_part, basis_part = body, ""
    else:
        stmt_part, basis_part = body[:first], body[first:]
    bases = [(b.group(1), [k.strip() for k in b.group(2).split(",") if k.strip()]) for b in BASIS.finditer(basis_part)]
    im = ITEM.match(stmt_part)
    if im:
        return im.group(1), im.group(2), bases, key_text
    lead = re.match(r"^(\s*)", stmt_part).group(1)
    return lead, stmt_part[len(lead):], bases, key_text


def join_line(prefix, stmt, bases, key_text):
    parts = [prefix + stmt]
    for kind, keys in bases:
        if keys:
            parts.append("*[%s %s]*" % (kind, ", ".join(keys)))
    return " ".join(parts) + " " + key_text


def edit_bases(key, bases):
    out = [(kind, list(keys)) for kind, keys in bases]
    if key in ADD_FROM:
        if "from" not in [k for k, _ in out]:
            out.append(("from", []))
        for i, (kind, keys) in enumerate(out):
            if kind == "from":
                out[i] = (kind, keys + [k for k in ADD_FROM[key] if k not in keys])
    return out


def substitute(text, used, where):
    for i, (old, new) in enumerate(THEOREM_SUBS):
        n = text.count(old)
        if n > 1:
            sys.exit("Theorem sentence %d matches %d times in %s" % (i, n, where))
        if n == 1:
            text = text.replace(old, new)
            used.add("thm-sub-%d" % i)
    return text


def process(path, used):
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines:
        cap = re.match(r"^\*Table: (.*)\* \{#(t:[a-z0-9-]+)\}\s*$", line)
        if cap and cap.group(2) in CAPTIONS:
            out.append("*Table: %s* {#%s}" % (CAPTIONS[cap.group(2)], cap.group(2)))
            used.add(cap.group(2))
            continue
        km = re.search(r"\{#([a-z]+:[A-Za-z0-9-]+)(?: weakened)?\}\s*$", line)
        if line.startswith("1. **Theorem.**") and not km:
            out.append(substitute(line, used, path.name))
            continue
        if km:
            key = km.group(1)
            if key == "thm:settled":
                line = substitute(line, used, path.name)
            prefix, stmt, bases, key_text = split_line(line)
            if key in NEW:
                stmt = NEW[key]
                used.add(key)
            new_bases = edit_bases(key, bases)
            if new_bases != bases:
                used.add("from:" + key)
            out.append(join_line(prefix, stmt, new_bases, key_text))
            continue
        out.append(line)
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def main():
    targets = [SPINE] + CHAPTERS
    for path in targets:
        if THEOREM_GUARD in path.read_text(encoding="utf-8"):
            sys.exit("Theorem already has its round 3 wording in " + path.name)
    seen = {}
    for path in targets:
        used = set()
        process(path, used)
        for u in used:
            seen.setdefault(u, []).append(path.name)
        if used:
            print("%s: %d edits" % (path.name, len(used)))
    wanted = list(NEW) + list(CAPTIONS) + ["thm-sub-%d" % i for i in range(len(THEOREM_SUBS))]
    wanted += ["from:" + k for k in ADD_FROM]
    bad = 0
    for w in wanted:
        files = seen.get(w, [])
        if len(files) != 2 or files[0] != SPINE.name:
            print("CHECK %s applied in %s" % (w, files))
            bad += 1
    print("%d changes, %d to check" % (len(wanted), bad))


if __name__ == "__main__":
    main()
