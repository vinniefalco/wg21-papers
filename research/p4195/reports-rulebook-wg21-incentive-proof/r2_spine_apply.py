"""Step 12 round 2 reconcile: apply spine statement changes to 02-spine.md and the chapter copies.

Every statement change is written once here and applied to both files, so the copies stay
word for word identical. Basis edits and the one cut spine child are applied to both files too.
Run once; it refuses to run if the Theorem no longer has its round 1 wording.
"""
import re
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
SPINE = S / "02-spine.md"
CHAPTERS = sorted(S.glob("ch-[0-9][0-9].md"))

NEW = {
    # chapter 2
    "p:who-decides": "The participants present decide a design's content: chairs call consensus on their votes, counted under the 2:1 norm, in the design rooms and the study groups that send them proposals. SD-4 assigns no one to rule on a design's quality, wording rooms check only that wording expresses the design, and national bodies vote on each balloted draft as a whole.",
    "m:players": "The players are result-seeking authors, design-bound authors, regulars, study group chairs, design room chairs, the convenor, national bodies, sponsors, and users. The proof takes as given SD-4's text, the convenor's identity, appointments, study groups, and guest invitations, and the choices of wording room chairs, guests, non-regular participants, and the direction group.",
    "m:moves-chair": "Any chair can choose the polls, order the agenda by SD-4's priorities, re-poll after discussion, ask Against voters for reasons, and allow limited exploration of alternatives. Each chair can call consensus on its room's polls, and design room chairs can also time-box a new proposal or delay one a meeting for a paperless rival.",
    "m:moves-convenor": "The convenor can appoint chairs, form study groups, invite a guest for up to two meetings, take any plenary polls, and make plenary consensus calls. In plenary the convenor can ask whether Against votes are personal or national body positions.",
    "m:moves-nb": "A national body can appoint experts, vote Yes, No, or abstain on ballots, comment, state national positions in plenary, appeal, and object in SC22 and JTC 1 to off-agenda action. It can vote on or confirm the convenor's appointment and, with at least one other P-member, have a draft discussed when they disagree with the SC22 chair's decision.",
    # chapter 3
    "l:vote-count": "Under the 2:1 norm each Against vote raises by two the Favor votes a proposal needs, while Neutral votes and abstentions leave the count unchanged. One Against vote changes the result only at one or two votes above the 2:1 threshold, and at least a third of Favor-plus-Against votes cast Against keeps the norm unmet.",
    "l:neutral-outside": "The 2:1 comparison counts only Favor and Against votes, and SD-4 says a Neutral majority of those voting can be concerning.",
    "p:against-costs-more": "For a regular, an Against vote on a colleague's proposal costs more than a Neutral vote or none. It risks the colleague's later support at least as much, and SD-4 tells only Against voters to be ready to give reasons, which take time to prepare.",
    "p:doubt-outside-count": "On a colleague's proposal they doubt, a regular does better voting Against only when the change that vote can make outweighs the standing and time it costs. One Against vote changes the result only when the count is one or two votes above the 2:1 threshold, and it can also bring changes to the design.",
    "p:prefer-vs-stop": "A participant can argue for another design yet vote Neutral, which leaves the count unchanged and, unlike Against, is a vote SD-4 asks no one to be ready to explain.",
    "p:mutual-support": "Two regulars with pending proposals each risk the other's support for their own by opposing the other's proposal. If each one's doubt is worth less than that risk and the time for reasons, each does better refraining whatever the other does, and both do better than both opposing.",
    # chapter 4
    "p:persuasion-not-required": "A proposal can advance through WG21 with objections unresolved, since it needs consensus calls, under the 2:1 norm in subgroups and by the convenor at plenary, not every objector's persuasion.",
    "p:advance-unanswered": "A proposal can advance with discussed objections unresolved, because it advances on consensus calls under the 2:1 norm in subgroups and by the convenor at plenary. Consensus need not imply unanimity.",
    "p:definition-without-procedure": "SD-4 adopts ISO's definition of consensus, marked by no sustained opposition, but names no step for judging or registering one, or criteria for an important part of the concerned interests. Whoever ISO's leadership is for a working group, SD-4's steps for an objection include the 2:1 norm, Against voters' reasons on request, escalation, and plenary's 3-way poll and national-position question.",
    "p:least-cost-response": "When an objection's Against votes are too few to keep the 2:1 norm unmet, the cheapest response keeping it met at that poll is no change or a partial change. The count measures votes, not whether the objectors are right, and SD-4 expects any change the room directs to be made or defended with new information.",
    "p:change-list": "SD-4 asks an Against voter to be ready to name the changes that would change their position, or to say that none would. Concerns stated as changes give authors items to grant one at a time, while opposition in any form offers none and counts in the poll only as a vote.",
    "p:reasons-unrecorded": "A proposal's case lasts for decades in its required paper, while an unwritten reason survives only in the memory of those who heard it. SD-4 asks whoever raises a concern to file an issue or write a paper, and outside the protected records only writing keeps an objection's argument after its hearers leave.",
    "p:repeat-objection": "SD-4 describes an objector who keeps objecting after a consensus call, without new information or allowed escalation, as not accepting a group decision, whether or not anyone answered it. It describes likewise a ballot comment repeating an objection decided with its national body present and heard, unless it brings new information or the body always warned of a No.",
    "p:late-objection": "SD-4 gives an objection weight at plenary only if its holder escalated it during the week, on the email lists by 5pm the evening before and within their national body. There, by default, it is not a national position, and after the deadline even new information goes to the email lists or a ballot comment, with a discussion paper.",
    "p:fluency": "Every design needs more than merit to be considered: a proposal needs an on-time paper and a presenter, a rival a paper to exist, and objections fixed forms and times. Participants learn how the committee applies them partly, and some only, by attending, and other things equal, whoever knows more has the better chance of adoption, whatever their design skill.",
    "p:newcomer": "Other things equal, a newcomer, lacking what earlier meetings teach, spends more effort getting a paper considered than a returning participant, and SD-4 expects everyone to know its procedures. Where a study group incubates proposals on its topic, a newcomer's early proposal can start there.",
    # chapter 5
    "l:poll-wording": "A direction poll asks voters only to agree that work should continue, less than a forwarding poll asks, so it can pass where a forwarding poll would fail. Passing it in a design room makes the design the incumbent.",
    "p:roadmap-poll": "If a poll places a proposal among the work the committee aims to include in the next edition, the proposal joins a category SD-4 has chairs take up first. A meeting's hours are fixed, so the time it then gets comes out of the time left for papers outside those categories.",
    "p:light-review": "Since those who skip a paper and its discussion typically abstain, those with large stakes cast most votes on a proposal costing more to read than most stakes in it. Unless those of them who object cast at least a third of the Favor-plus-Against votes, it can advance with no change at all.",
    "p:late-arrival": "Three things hold at once for an objector who arrives after a design has been adopted. Removal needs a paper or ballot comment meeting the 2:1 norm, reversal costs more as more is built, and the record keeps its case but unwritten objections only in memory.",
    # chapter 6
    "p:first-part": "A first part fixing a design's structure can be adopted before reviewers can study in detail what later parts need, and every rival to that structure must then replace it. SD-4 asks no paper to state those needs, so a design-bound author does best proposing first the smallest part that fixes the structure and can pass.",
    "p:large-position": "A large proposal has more sponsored authors in the room than a small one, and more expected meetings where a poll can make it the incumbent or end its incumbency.",
    "p:size-attributes": "Each result here about large or small proposals rests on an attribute their definitions name: who pays the authors' costs, how many authors, review's expected span, or paper length. So it holds for any proposal with that attribute, whatever its size.",
    # chapter 7
    "p:sg-sponsor": "Paying participants to attend a study group puts voters who value the sponsor's interests where the design the design room starts from is chosen. Where the other voters cast fewer Favor-plus-Against votes, fewer paid participants make up a third of the total, enough to block, or over two thirds, enough to meet the norm.",
    # chapter 8
    "l:call-above": "In the case the table below describes, a design room chair ranks declaring consensus above declining on a count above 2:1 after discussion.",
    "p:chair-confidence": "Of two papers otherwise alike, a chair does better taking up first the one whose author's record of following procedures and responding to review makes them expect fewer problems. That record comes from taking part, which SD-4 expects of an author: presenting the proposal, answering questions, and making the changes the room directs.",
    "p:plenary-ratifies": "At plenary, design stays with the design rooms, SD-4 gives no weight to objections not escalated in time, and all present are asked for serious design concerns. SD-4 says most polls pass by unanimous consent, and when opposition is significant the convenor usually asks whether Against votes are personal or national body positions.",
    # chapter 9
    "p:who-takes-part": "Fees are barred and meeting places should not significantly limit attendance, and only those who bear the cost of taking part, or whose sponsors do, vote in WG21's polls. ISO can remove inactive national body experts, and participants can propose only for needs they and their sponsors know, which need not match users', since users differ from them.",
    "p:reward-timing": "Authors get the adoption they value at the poll. A flaw that implementation and use have not yet exposed costs them only later and in part, and its cost can fall on any user of the feature.",
    "p:merit-gap": "Winning a consensus call and producing the design serving users best coincide only as far as voters can judge that at the poll and weigh no other value above it. SD-4 assigns no one to rule on it for them.",
    "p:integration": "Change papers approved separately at one meeting first come together when the project editor merges their wording, which the editor's report records and a pre-ballot editing committee verifies. No SD-4 step checks whether the designs work together, while each author gains from their own design's adoption and a conflict costs users and later rework.",
    "p:written-answer": "No rule requires a written answer to an objection beyond an author's defense of declining a directed change, ISO's response to enquiry comments, and a TS ballot's Disposition of Comments. For the author, a written answer stating the objection makes it easier to raise again but also shows later readers what would not be new, SD-4's test for repeated objections.",
    # chapter 10
    "p:cutoff-effect": "At the feature cutoff, a one-meeting delay for a paperless rival sends a proposal to the next planned edition. So does an Against vote that keeps its count from meeting the 2:1 norm.",
    "p:prefer-is": "A TS delays IS adoption by about one to two years, and its experience can bring incompatible changes first: a gain to result-seeking authors, a risk to design-bound ones. It reaches implementers and users early, can publish while concerns remain if their holders agree, and the design room can require it or the white paper ISO and SC22 recommend.",
    "l:ballot-rules": "Every national body may vote on enquiry and final ballots, which pass with two thirds of P-members' counted votes positive and at most a quarter of all counted votes negative. Abstentions and negative votes without technical comments go uncounted, ISO encourages abstaining without national consensus or expert input, sustained opposition is inapplicable, and a failed final draft returns to SC22.",
    "p:nb-comment": "A national body's No opposes every feature in the document at once, including ones its own experts support, while WG21 considers its comments whatever its vote. In the table's cases, a body valuing the rest of a document does better voting Yes with comments, and one wanting the work in no form does better voting No.",
    "l:rank-oppose-no": "A body that wants the work in no form, as the table below defines it, ranks No above abstaining. Only the No counts against approval, which is what SD-4 says No is for.",
    "p:credible-threat": "A national body whose comments fare the same under any vote does better voting No over one feature only if it values removing it above the rest on schedule. SD-4 expects such a body to have told the committee all along, and ISO asks every national body to make its standpoint clear early.",
    "p:nb-members": "A national body forms its position by its panel's own rules, which SD-4 does not state, so whether a sponsor's paid participants add weight there depends on those rules. In the United States, INCITS gives each organization one vote, the Defense Department up to four, no vote to consultants a voting member funds, and binds delegates to official positions.",
    "l:incits-votes": "INCITS gives each organization one voting membership, except up to four Department of Defense votes on technical committees, and on its Executive Board counts a controlled entity with its controller. It admits a consultant as a voting member only if no voting member funds it, and lets standards developing organizations and consortia be represented by other voting members' employees.",
    # chapter 11
    "l:settled-design-bound": "Whatever the others choose, a design-bound author does best seeking early direction polls, the smallest first part fixing its features, and the IS, each as far as it can pass. It does best leaving out a trade-off no reviewer would raise when stating it costs more than later exposure, and answering objections with the cheapest change that keeps it passing.",
    "l:settled-result-seeking": "Whatever the others choose, a result-seeking author does best stating trade-offs and granting changes whenever the better design they bring outweighs the votes or work they cost. It does best backing any rival that serves users better by more than its share of the reversal's cost.",
    "l:settled-small-author": "Whatever the others choose, a small proposal's author does best keeping it presented while its chance of adoption outweighs the cost, borne alone, of the meetings still ahead. The longer it must still wait behind priority work, the more those costs come to, and once they outweigh its chance, the author does best letting it stop.",
    "l:settled-sg-chair": "Whatever the others choose, a study group chair whose stake is worth less than what departing can cost them does best polling competing designs side by side. It does best sending on a design that meets the 2:1 norm, or none when none does.",
    "l:settled-design-chair": "Whatever the others choose, a design room chair whose stake is worth less than what departing can cost does best following the 2:1 norm and polling rivals side by side. It does best taking up first, of papers otherwise alike, the one whose author has a record of following the procedures.",
    "l:settled-convenor": "Whatever the others choose, the convenor does best following SD-4's plenary procedure unless their stake is worth more than what departing can cost them. That procedure has the convenor declare consensus when nobody objects to unanimous consent or all opposition is unescalated and holds no national position, and otherwise leaves the call to them.",
    "l:settled-nb": "Whatever the others choose, a national body whose comments fare alike under any vote does best voting Yes with comments if it values the document's rest above removing any feature. Otherwise it does best voting No, and it does best raising its objections early, while ISO encourages it to abstain when it lacks national consensus or expert input.",
    "l:settled-sponsor": "Whatever the others choose, a sponsor does best paying for participants in the subgroups whose decisions it values, study groups included, while what they bring it is worth their cost. Each such participant votes valuing its interests, and no rule limits how many it pays.",
    "l:settled-user": "Whatever the others choose, a user without a sponsor does best taking part only when their own stakes in its polls outweigh the full price, which they bear alone. Otherwise the best move is a cheaper one or none: TS feedback, a paper a participant presents, or a request to a national body.",
    "p:checks": "The rules provide these checks: every view must be heard, a third of the Favor-plus-Against votes can block, rivals with papers can be polled together, and implementation experience informs votes. Plenary invites serious design concerns, national bodies vote on each balloted draft, get answers to enquiry comments, and can appeal, editing committees verify applied changes, and minutes can be challenged.",
    "l:checks-hearing": "SD-4 requires every view to be heard and understood and the majority to listen, and asks for respect, good faith, and no collusion, with conduct concerns reported through ISO's process. It asks discussion to build broad understanding and design room participants to weigh direction group opinions, welcomes negative comments, and a third of the Favor-plus-Against votes cast Against can block.",
    "l:checks-alternatives": "Chairs may allow limited exploration of alternatives, and SD-4 encourages side-by-side polls and asks a good paper for alternatives considered, design principles, and motivating examples from today's code. Followup and rebuttal papers can be considered, an author who declines a directed change should defend that decision, and SD-4 does not significantly delay concrete proposals to wait for alternatives.",
    "l:checks-record": "Plenary solicits serious design concerns, national bodies vote on each enquiry and final ballot, every enquiry comment gets a written response, and editing committees verify applied changes. Minutes can be challenged, and national bodies can appeal, on drafts only over principle or harm to ISO's or IEC's reputation.",
    # chapter 12
    "c:predictions": "If the settled pattern holds, the record should show the following. SD-4 password-protects records of subgroup discussion but lets poll questions and numeric results be quoted, and each prediction names its evidence, counter-evidence, another explanation, and the data telling them apart.",
    "c:pred-sponsor-against": "Where one sponsor pays a proposal's authors and many participants present, and its interests include adoption, the model predicts a smaller Against share of the Favor-plus-Against votes than elsewhere. No smaller share would count against it, and votes of participants who move to a sponsor whose interests exclude the proposal would tell it apart from shared technical views.",
    "c:pred-abstention-length": "Across revisions of one proposal polled in one room, the model predicts fewer votes cast, relative to other papers polled at the same meetings, as the paper grows longer. No fall would count against it, and since one proposal keeps its topic, the comparison sets aside another explanation, that longer papers cover narrower topics fewer participants know.",
    "c:pred-parts": "The model predicts that large proposals tend to arrive as sequences of papers, each building on adopted parts, and large designs mostly adopted in one paper would count against it. Another explanation, easier review in parts, gives no reason to omit from a first paper what later parts need of it, an omission the model predicts for design-bound authors.",
    "c:pred-first-part": "For design-bound authors, the model predicts small first papers that leave out the later parts of a design extended part by part; the mailings are the evidence. Finding no such omissions would count against it, and another explanation, that small first steps lower risk, gives no reason to omit any mention of later parts that already exist.",
    "c:pred-rival-polls": "The model predicts that once a design passes a design room's direction poll, a like rival draws less support than before in polls of the same form. Equal support would count against it, and comparing only polls between which the incumbent's content and review time did not change would tell it apart from learning or improvement.",
    "c:pred-removals": "The model predicts rare removals after adoption, likelier when national bodies whose No votes could fail a ballot oppose the design, and frequent narrow-margin removals would count against it. Another explanation is that adopted designs rarely need removal, and the share of failed removal polls with more Favor than Against votes would tell them apart.",
    "c:pred-small-fade": "Per meeting spent waiting behind priority work, the model predicts more stops without a negative poll for self-funded authors' proposals than for sponsored authors' proposals of similar length. No such difference would count against it, and stops rising once a waiting proposal's author loses their sponsor would tell it apart from another explanation, dropping on reflection.",
    "c:pred-nb-positions": "The model predicts that national bodies state positions on few proposals, and positions on most would count against it; vetted ballot comments, which count as national positions, are the evidence. Another explanation is that they agree with most proposals, and more positions from bodies whose experts attend in person, where forming one costs less, would tell them apart.",
    "c:pred-written-answers": "The model predicts that papers advancing over Against votes often leave unstated the objections other published papers raised against them, and routine answers would count against it. Another explanation is that the objections were answered in discussion, and omitted objections a subgroup chair's plenary summary shows went unanswered would tell them apart.",
    "c:pred-defects": "If some unresolved objections point to real defects, then at equal turnout the model predicts more defects found after adoption in features forwarded over Against votes than with none. No difference would count against it, and matching features on scope, novelty, prior implementation, and use would tell it apart from another explanation, the scrutiny novelty or use brings.",
    "c:pred-competing": "If closer study finds more defects, the model predicts fewer post-adoption defects on topics whose deciding poll had competing papers from separate author groups than on one-paper topics. No difference would count against it; another explanation is that important or well-understood topics draw rivals and attention anyway, and matching implementation experience and turnout tells them apart.",
    "c:lever-anonymous": "If design polls were anonymous, the standing part of an Against vote's cost would shrink for voters whom neither their words nor the count identify. The chair could no longer ask a particular Against voter for reasons, and the model predicts more Against votes on colleagues' proposals.",
    "c:lever-reasons-all": "If SD-4 asked every voter to be ready to give reasons on request, Neutral and Favor would bear the reasons cost Against now bears, and not voting none. The model predicts fewer Neutral votes, fewer Favor votes on doubted proposals, and more participants not voting.",
    "c:lever-sponsor-limit": "If the rules limited how many participants one sponsor pays may vote in a subgroup, the votes cast there by participants valuing its interests would be capped. The model predicts smaller margins for proposals whose authors one sponsor pays beyond the limit than for proposals with as many authors paid by separate sponsors.",
    "c:lever-nb-more": "If forming national positions during meetings cost less, national bodies would take more, and more plenary opposition would hold positions whose weight SD-4's procedure leaves to the convenor. For objections backed by bodies whose No votes could fail a ballot, the model predicts larger changes in answer and slower progress for contested proposals.",
    "c:lever-nb-less": "If forming national positions during meetings cost more, national bodies would take fewer, and plenary would seldom meet opposition holding them. Their ballot vote would be their only move counting directly toward stopping a document, and the model predicts attendance, paid participants, and early incumbency deciding more content.",
}

THEOREM_OLD_START = "1. **Theorem.** Under the rules and given the axioms, these choices form a settled pattern. A design-bound author seeks direction polls as early as they can pass"

THEOREM_P1 = "Under the rules and given the axioms, these choices form a settled pattern. A design-bound author seeks early direction polls, proposes first the smallest part fixing the features it needs, and asks for the IS, each as far as it can pass. It leaves out a trade-off no reviewer would raise when stating it costs more than later exposure would, and answers objections with the cheapest change that keeps the design passing. A result-seeking author states trade-offs and makes changes whenever the better design they bring outweighs the votes or work they cost. It backs a rival that serves users better by more than its share of the reversal's cost. An author who values both chooses, at each two-way choice, as the type whose value differs more. A small proposal's author keeps it presented while its chance of adoption is worth the meetings still ahead, whose cost they bear alone. A regular votes Favor on colleagues' proposals they support, and Against one they doubt only when the change that vote can make outweighs the standing and time it costs. Otherwise the regular takes whichever of Neutral, not voting, or Favor does best, and Favor risks nothing with the colleague. A sponsor pays for participants where the decisions it values are made, study groups included. Chairs follow the 2:1 norm and poll competing designs side by side, and the convenor follows SD-4's plenary procedure, unless their stake outweighs what departing can cost them. A national body whose comments fare alike under any vote votes Yes with comments unless removing one feature is worth as much to it as the rest of the document. A user without a sponsor takes part only when their own stakes in its polls outweigh a full price borne alone, and otherwise uses a cheaper move or none. Each player makes every choice left open here in the way that does best for them given the others' choices. These include a result-seeking author's vehicle request, a design room chair's one-meeting delay, the convenor's call where SD-4 leaves it open, and whether to study a paper."

THEOREM_P2 = "In this pattern a design's content can be fixed when it is least reviewed. Its first favorable poll can make it the incumbent, and objectors short of a third of the Favor-plus-Against votes cannot force a change. Every later rival or change must then redo work built on it, at a cost that grows whether or not the design is wrong. Objections count only in fixed forms and at fixed times, and some of how the committee applies these rules is learned only by attending. In a long deadlock, the group whose sponsors keep paying its costs can hold longest, whichever design is better. A proposal that costs more to read than most participants' stakes in it can advance with no change at all. An objector arriving after adoption needs a paper or ballot comment meeting the 2:1 norm, faces a reversal cost that has grown, and finds unwritten objections kept only in memory. Other things equal, a proposal advances more readily when its authors keep presenting it or know the procedures, or when a sponsor pays for participants who hold its position. The same holds when the chair expects fewer problems from it, a poll has placed it among the work aimed at the next edition, or it is already the incumbent. No user votes, and the needs that reach a vote are those participants and their sponsors know, which need not match those of users at large. The participants present decide content, and no rule limits how many voters one sponsor pays for. A change to a design costs the sponsors who have built on it, while its gain is spread across all users. Authors get adoption at the poll, while a flaw found only in implementation and use costs them later and in part, and can fall on any user. Technical merit enters through what participants value, including a good result for users, and through the discussion, papers, and implementation experience that inform their votes. SD-4 assigns no one to rule on it, and the consensus test never asks whether an objection is right. No SD-4 step checks whether separately adopted designs work together, and review worth its cost to users together but not to any one participant goes undone. The record need not show whether objections were answered. The rules ask no author to state their own design's drawbacks. Leaving one out costs a design-bound author no step the rules require before adoption, while stating one can cost a result-seeking author votes. A first part fixing a structure can be adopted before reviewers can study in detail what later parts need, and every rival to that structure must then replace it. The rules also provide checks: a third of the Favor-plus-Against votes can block, and every view must be heard. Rivals with papers can be polled together, implementation experience informs votes, and national bodies vote on each balloted draft. Each result about large or small proposals holds for any proposal with the attributes it rests on."

CAPTIONS = {
    "t:chair-call": "A design room chair's consensus call, when the chair's stake in the proposal is worth less to them than what departing from the 2:1 norm can cost them. Neutral votes are short of a majority of those voting, the chair finds no sustained opposition, and a re-poll fits the norm at any count. Columns: the count after discussion of the Against voters' concerns. Each cell: the chair's rank of the call. 2 is best within each column.",
    "t:nb-ballot": "A national body's ballot vote. Columns: how the body values the document. \"Values the rest\" means it values publishing the rest of the document on schedule above removing any one feature through a failed ballot and a revised draft SC22 may produce. It also expects its comments to fare the same under any vote, as SD-4 says. \"Opposes the work\" means it does not want the work at all. In both, the body cannot rule out that its vote decides the result. Each cell: its rank of the vote. 3 is best within each column.",
    "t:disclose": "An author's choice, before an early direction poll, whether to state in the paper a trade-off no reviewer would otherwise raise. Stating it would lead the room to change a feature a design-bound author's gain depends on, in a way that serves users better. The proposal meets the 2:1 norm either way. Columns: the author's type. Each cell: the author's rank of the choice. 2 is best within each column.",
}

ADD_FROM = {
    "p:who-votes": ["f:plenary-polls"],
    "m:moves-convenor": ["f:plenary-polls"],
    "m:moves-nb": ["f:convenor-term"],
    "p:record-indistinct": ["f:iso-no-answer"],
    "p:reasons-unrecorded": ["f:report-followup"],
    "p:who-takes-part": ["f:meeting-access"],
    "p:reward-timing": ["ax:rework"],
    "p:integration": ["f:in-situ"],
    "l:checks-hearing": ["f:direction-opinion"],
    "l:checks-record": ["f:expert-contact"],
    "l:settled-design-chair": ["f:multiple-polls", "ax:post-risk"],
    "c:pred-removals": ["d:follows-norm", "f:protected"],
    "c:pred-small-fade": ["p:size-attributes"],
    "c:pred-nb-positions": ["f:comments-national"],
    "c:pred-competing": ["l:implementation-informs"],
    "thm:settled": ["ax:rework"],
}

REMOVE_PROVED = {"p:checks": ["l:checks-attendance"]}
CUT_ITEMS = ["l:checks-attendance"]

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
    out = []
    for kind, keys in bases:
        new = [k for k in keys if not (kind == "proved by" and k in REMOVE_PROVED.get(key, []))]
        out.append((kind, new))
    if key in ADD_FROM:
        if "from" not in [k for k, _ in out]:
            out.append(("from", []))
        for i, (kind, keys) in enumerate(out):
            if kind == "from":
                out[i] = (kind, keys + [k for k in ADD_FROM[key] if k not in keys])
    return out


def process(path, used):
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        cap = re.match(r"^\*Table: (.*)\* \{#(t:[a-z0-9-]+)\}\s*$", line)
        if cap and cap.group(2) in CAPTIONS:
            out.append("*Table: %s* {#%s}" % (CAPTIONS[cap.group(2)], cap.group(2)))
            used.add(cap.group(2))
            i += 1
            continue
        km = re.search(r"\{#([a-z]+:[A-Za-z0-9-]+)(?: weakened)?\}\s*$", line)
        if km and km.group(1) in CUT_ITEMS:
            indent = len(line) - len(line.lstrip())
            used.add(km.group(1))
            i += 1
            while i < len(lines) and lines[i].strip() and (len(lines[i]) - len(lines[i].lstrip())) > indent:
                i += 1
            continue
        if line.startswith("1. **Theorem.**") and not km:
            if not line.startswith(THEOREM_OLD_START):
                sys.exit("Theorem already changed in " + path.name)
            out.append("1. **Theorem.** " + THEOREM_P1)
            used.add("thm-p1")
            i += 1
            continue
        if km:
            key = km.group(1)
            prefix, stmt, bases, key_text = split_line(line)
            if key == "thm:settled" and not line.lstrip().startswith("1."):
                out.append(join_line("   ", THEOREM_P2, edit_bases(key, bases), key_text))
                used.add("thm-p2")
                i += 1
                continue
            if key in NEW:
                stmt = NEW[key]
                used.add(key)
            out.append(join_line(prefix, stmt, edit_bases(key, bases), key_text))
            i += 1
            continue
        out.append(line)
        i += 1
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def main():
    targets = [SPINE] + CHAPTERS
    for path in targets:
        if path.name != SPINE.name and "Theorem already changed" in path.read_text(encoding="utf-8"):
            sys.exit("unexpected text in " + path.name)
    seen = {}
    for path in targets:
        used = set()
        process(path, used)
        for u in used:
            seen.setdefault(u, []).append(path.name)
        if used:
            print("%s: %d edits" % (path.name, len(used)))
    wanted = list(NEW) + list(CAPTIONS) + CUT_ITEMS + ["thm-p1", "thm-p2"]
    bad = 0
    for w in wanted:
        files = seen.get(w, [])
        if len(files) != 2 or files[0] != SPINE.name:
            print("CHECK %s applied in %s" % (w, files))
            bad += 1
    print("%d changes, %d to check" % (len(wanted), bad))


if __name__ == "__main__":
    main()
