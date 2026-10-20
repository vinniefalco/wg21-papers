"""Step 12 round 1 reconcile: apply spine statement changes to 02-spine.md and the chapter copies.

Every statement change is written once here and applied to both files, so the copies stay
word for word identical. Basis edits, cuts, and the one inserted spine child are applied to
both files too. Run once; it refuses to run if a statement it replaces is already changed.
"""
import re
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
SPINE = S / "02-spine.md"
CHAPTERS = sorted(S.glob("ch-[0-9][0-9].md"))

NEW = {
    "p:who-decides": "The participants present decide a design's content: chairs call consensus on their votes, counted under the 2:1 norm, in the design rooms and the study groups that send them proposals. SD-4 assigns no one to rule on a design's quality, wording rooms check only that wording expresses the design, and national bodies vote on each draft as a whole.",
    "p:who-votes": "Each person in a subgroup's room has one vote, guests a convenor invites included, while no user votes in any WG21 poll or in the ballots on its drafts.",
    "m:players": "The players are result-seeking authors, design-bound authors, regulars, study group chairs, design room chairs, the convenor, national bodies, sponsors, and users. The proof takes as given SD-4's text, the choices of wording room chairs, guests, participants who are not regulars, and the direction group, the convenor's appointments, study groups, and guest invitations, and every move the settled lemmas do not weigh.",
    "m:moves-chair": "Any chair can choose the polls, order the agenda by SD-4's priorities, time-box a new proposal, re-poll after discussion, ask Against voters for reasons, and allow limited exploration of alternatives. Design and wording room chairs call consensus to forward proposals, design room chairs can delay one a meeting for a paperless rival, and study group chairs can poll which design to send on.",
    "m:moves-sponsor": "A sponsor can pay for participation and choose whom and how many it pays, and a sponsor that is a category C liaison has representatives who act for it. Unless it is an ISO member body or a liaison organization, a sponsor has no vote of its own in WG21's polls or in the ballots on WG21's drafts.",
    "l:neutral-outside": "The 2:1 comparison counts only Favor and Against votes, though SD-4 says a Neutral majority of those voting can be concerning.",
    "p:against-costs-more": "For a regular, an Against vote on a colleague's proposal costs more than a Neutral vote or none. It risks the colleague's later support no less, and SD-4 tells only Against voters to be ready to give reasons, which take time to prepare.",
    "p:doubt-outside-count": "On a colleague's proposal they doubt, a regular does better voting Against only when the change that vote can make outweighs the standing and time it costs. One Against vote changes the result only when the count sits one or two votes above the line, though it can also win changes to the design.",
    "p:prefer-vs-stop": "A participant can argue for another design and still vote Neutral, which leaves the count unchanged and, unlike Against, carries no request for reasons in SD-4.",
    "p:mutual-support": "Two regulars with pending proposals each risk the other's support for their own by opposing the other's proposal. When each one's doubt is worth less than that risk and the time for reasons, each does better refraining whatever the other does, and both do better than if both opposed.",
    "l:mutual-refrain": "In the case the table below describes, opposing the other's proposal costs each regular more in standing and time than it can change. So each ranks refraining above opposing, whatever the other does.",
    "p:persuasion-not-required": "A proposal can advance through WG21 with objections unresolved, since it needs consensus calls, under the 2:1 norm in the rooms and by the convenor at plenary, not every objector's persuasion.",
    "p:advance-unanswered": "A proposal can advance while discussed objections to it remain unresolved, because it advances on consensus calls, under the 2:1 norm in the rooms and by the convenor at plenary, and consensus need not imply unanimity.",
    "p:definition-without-procedure": "SD-4 adopts ISO's definition of consensus, marked by the absence of sustained opposition, but names no step for judging or registering one, nor criteria for an important part of the concerned interests. Whoever ISO's leadership is for a working group, SD-4's own steps for an objection include the 2:1 norm, Against voters' reasons on request, escalation, and plenary's 3-way poll and national-position question.",
    "l:consensus-test": "Under SD-4's definition, an objection prevents consensus as a sustained opposition only if it concerns a substantial issue, is maintained, and comes from an important part of the concerned interests. The leadership judges that part case by case, none of the three conditions asks whether the objection is right, and the process must seek to reconcile conflicting arguments.",
    "p:least-cost-response": "When an objection's Against votes are too few to stop the 2:1 norm, the cheapest response keeping it met at that poll is no change or a partial change. The count measures votes, not whether the objectors are right, and SD-4 expects any change the room directs to be made or defended with new information.",
    "p:change-list": "SD-4 asks an Against voter to be ready to name the changes that would win them over, or to say that none would. Concerns stated as changes give authors items to grant one at a time, while opposition in any form offers none and counts in the poll only as a vote.",
    "p:dissent-needs-paper": "Of minutes, non-public email lists, records of subgroup discussion, ballot comments, and papers, only a paper puts an objection's argument outside the password-protected materials without anyone else's help. Writing one takes time.",
    "p:reasons-unrecorded": "A proposal's case lasts for decades in its required paper, while an unwritten reason survives only in the memory of those who heard it. Outside the protected records, an objection's argument outlasts its hearers only in writing, such as the objector's paper or an author's paper showing the alternative or defending a declined change.",
    "p:repeat-objection": "SD-4 describes an objector who presses on after a consensus call, without new information or allowed escalation, as not accepting a group decision, whether or not anyone answered it. It says the same of a ballot comment repeating an objection decided where its national body was present and heard, unless the comment brings new information or the body warned all along that it would vote No.",
    "p:fluency": "Every design needs more than merit to be considered: a proposal needs an on-time paper and a presenter, a rival needs a paper to exist, and objections need fixed forms and times. Participants learn how the committee applies these rules partly by attending, some of it only that way, and other things equal, whoever knows more has the better chance of adoption, whatever their design skill.",
    "p:newcomer": "Other things equal, a newcomer, lacking what earlier meetings teach, spends more effort getting a paper considered than a returning participant, though SD-4 expects everyone to know its procedures. Where a study group incubates proposals on its topic, a newcomer's early proposal can start there.",
    "p:early-polls": "A design can become the incumbent at its first direction poll, when it has had less review than at any later meeting. From then on, a rival or a later change must redo or discard work built on it, at a cost that grows as more is built.",
    "p:challenger-bar": "A rival wins a voter from an incumbent only with an advantage worth more to that voter than their share of the reversal's cost. The advantage a rival needs grows with each decision built on the incumbent, while keeping the incumbent needs none.",
    "p:light-review": "Those who have not read a paper or followed its discussion typically abstain, so a proposal costing more to read than most stakes in it is voted on mainly by those with large stakes. Unless those of them who object cast at least a third of the Favor-plus-Against votes, it can advance with no change at all.",
    "p:burden-flip": "A design needs the 2:1 norm to advance, and once adopted, a paper or ballot comment to remove it needs the same, switching the default to keeping it. After a successful final ballot, design changes are expected to have near-unanimous consent, ISO bars technical changes at approval, and SD-4 calls published features much harder to update incompatibly.",
    "p:late-arrival": "An objector who arrives after a design has been adopted faces three obstacles at once. Removal needs a paper or ballot comment meeting the 2:1 norm, reversal costs more for every decision built on the design, and the record keeps its case but unwritten objections only in memory.",
    "p:sponsor-votes": "Each participant a sponsor pays to attend has a vote in the room and values its interests, and no rule limits how many it pays. SC22 may cap only the experts each national body or liaison appoints, and at SC22 itself each national body counts once.",
    "ind:adopted-parts": "Each part adopted adds to what a rival to the whole design must replace: the part itself and the work built on it, later parts that depend on it included.",
    "p:parts": "Presenting a design in parts lets the first parts be adopted before the whole is reviewed, and each adopted part adds to what a rival to the whole must replace. Its costs include a paper, a presentation, and a set of polls for each part.",
    "p:first-part": "A first part that fixes a design's structure can be adopted before reviewers can study in detail what later parts need of it, and then every rival to that structure must replace it. SD-4 asks no paper to state those needs, so a design-bound author's best first paper is the smallest part that fixes the structure and still meets the 2:1 norm against opponents who foresee the rest.",
    "p:large-position": "A large proposal has more sponsored authors in the room than a small one, and is expected to face more meetings where a poll can make it the incumbent or end its incumbency.",
    "p:small-position": "A small proposal's author bears every meeting's cost alone, and outside SD-4's priority categories the proposal gets agenda time only after the priority work. Where a study group incubates proposals on its topic, a small proposal can start there.",
    "p:size-attributes": "Each result in this chapter about large or small proposals rests on an attribute their definitions name: who pays the authors' costs, the number of authors, review's expected span, or the paper's length. So it holds for any proposal with that attribute, whatever its size.",
    "p:sg-decides": "On a topic with a study group, rival designs can be polled there first, among those who chose that room over the rooms meeting with it. The design it sends on is where the design room starts, and the design room, which owns selecting designs, can still poll a rival that has a paper.",
    "p:attrition": "In a long deadlock, a group whose sponsors keep paying its costs bears less per meeting than a group paying its own way. In the case the table below describes, the first does better holding and the second yielding, whichever design is better.",
    "l:hold-yield-both-hold": "When both groups hold and the deadlock ends with either design equally likely, each can expect half its stake on average, less its cost of holding through it. A group's participants whose costs sponsors pay bear less of that cost per meeting.",
    "p:chair-threshold": "Every contested consensus call has a cost: declaring consensus over Against votes risks later national body opposition, and declining delays work SD-4 says subgroup polls should favor. Departing from SD-4's stated practice can cost the caller's post: chairs serve at the convenor's choice with no fixed term, and the convenor for terms SC22 may decline to renew.",
    "p:chair-default": "A chair gains from departing from the 2:1 norm at most their stake in the poll, and cannot rule out added risk to their post. So a chair whose stake is worth less than that risk does better following the norm, re-polling first if they choose.",
    "l:call-above": "On a count above 2:1 after discussion, with Neutral votes short of a majority, a design room chair whose stake is worth less than what departing can cost ranks declaring consensus above declining.",
    "l:call-below": "On a count at or below 2:1 after discussion, such a chair ranks declining above declaring consensus.",
    "p:chair-confidence": "Of two papers otherwise alike, a chair does better taking up first the one whose author has a record of following procedures and responding to review, which promises fewer problems. SD-4 expects that record to come from taking part: presenting, answering questions, and making the changes the room directs.",
    "p:plenary-ratifies": "At plenary, design stays with the design rooms, SD-4 gives no weight to objections not escalated in time, and all present are asked for serious design concerns. Most polls pass by unanimous consent, and when opposition is significant the convenor usually asks whether Against votes are personal or national body positions.",
    "p:reward-timing": "Authors get the adoption they value at the poll, while a flaw that implementation and use have not yet exposed costs users only later, and can fall on any user of the feature.",
    "p:merit-gap": "Winning a consensus call and producing the design that serves users best coincide only as far as voters can judge that at the poll and no other value they hold outweighs it. SD-4 assigns no one to judge it for them.",
    "p:written-answer": "No rule requires a written answer to an objection beyond three: an author's defense of declining a directed change, ISO's response to enquiry ballot comments, and a TS ballot's Disposition of Comments. For the author, a written answer stating the objection makes it easier to raise again, but also shows later what would not be new, the test SD-4 applies to repeated objections.",
    "p:miss-cost": "A proposal that misses an edition's feature cutoff waits at least for the next edition, planned three years later. It can ship sooner as a white paper, which has no prescribed schedule, and the planned schedule keeps an unfinished feature from delaying the features that are ready.",
    "p:cutoff-effect": "At the feature cutoff, a one-meeting delay for a paperless rival sends a proposal to the next planned edition. So does an Against vote keeping it at or below the 2:1 line.",
    "p:prefer-is": "A TS delays IS adoption by about one to two years, and its experience can bring incompatible changes first: a gain to result-seeking authors, a risk to design-bound ones. It also reaches implementers and users early and can publish while concerns remain, if their holders agree, and the design room can require one, or the lighter white paper ISO and SC22 now recommend.",
    "l:ballot-rules": "Every national body may vote on enquiry and final ballots, which pass when two thirds of the P-members' counted votes are positive and at most a quarter of all counted votes negative. Abstentions and negative votes without technical comments go uncounted, ISO encourages abstaining without national consensus or expert input, sustained opposition does not apply, and a failed final draft returns to SC22.",
    "p:nb-comment": "A national body's No opposes every feature in the document at once, including ones its own experts support, while WG21 considers its comments whatever its vote. In the cases the table below describes, a body valuing the rest of a document does better voting Yes with comments, and one wanting the work in no form does better voting No.",
    "l:rank-rest-yes": "A body that values the rest of a document, as the table below defines it, ranks Yes with comments above abstaining. Only the Yes counts toward the approval it prefers, and its comments fare the same either way.",
    "l:rank-rest-abstain": "Such a body ranks abstaining above No, since only the No counts against the approval it prefers, and in this case its comments gain nothing from a No.",
    "p:credible-threat": "At ballot, a national body whose comments fare the same under any vote does better voting No over one feature only if it values removing that feature above the rest of the document on schedule. SD-4 expects such a body to have told the committee all along, and ISO asks every national body to make its standpoint clear early.",
    "p:nb-members": "A national body forms its position by its panel's own rules, which SD-4 does not state, so whether a sponsor's paid participants add weight there depends on those rules. In the United States, INCITS gives each voting member one vote, apart from up to four Defense Department votes, bars consultants a voting member funds from voting membership, and binds all delegates to official positions.",
    "l:incits-votes": "INCITS gives each organization one voting membership, apart from up to four Department of Defense votes on technical committees, and treats an entity another controls as part of it on its Executive Board. It admits a consultant as a voting member only if no voting member funds it, and lets the representatives of standards developing organizations and consortia be employed by other voting members.",
    "l:settled-regular": "Whatever the others choose, a regular does best voting Favor on colleagues' proposals they support. On one they doubt, Against does best only when the change it can make outweighs the standing and time it costs, and otherwise Neutral, not voting, or Favor does best.",
    "l:settled-design-bound": "Whatever the others choose, a design-bound author does best seeking direction polls as early as they can pass, proposing first the smallest part that fixes its features and can pass, and choosing the IS where it can pass. It does best leaving out a trade-off no reviewer would raise when stating it now costs more than later exposure would, seeking no poll it expects to lose to a rival, and answering objections with the cheapest change that keeps the design passing.",
    "l:settled-result-seeking": "Whatever the others choose, a result-seeking author does best stating a trade-off and granting a change whenever the better design they bring outweighs the votes or work they cost. It does best seeking an early poll or first part only where sooner adoption outweighs the cost it adds to later improvements, and backing any rival that serves users better by more than its share of the reversal's cost.",
    "l:settled-small-author": "Whatever the others choose, a small proposal's author does best keeping it presented while its chance of adoption is worth more to them than the cost, borne alone, of the meetings still ahead. The longer it must still wait behind priority work, the more those costs come to, and once they outweigh its chance, the author does best letting it stop.",
    "l:settled-sg-chair": "Whatever the others choose, a study group chair does best polling competing designs, side by side where several compete, and sending on one that meets the 2:1 norm, or none. Only a chair whose stake in the contest is worth more to them than what departing can cost does better departing from this.",
    "l:settled-design-chair": "Whatever the others choose, a design room chair whose stake is worth less than what departing can cost them does best following the 2:1 norm after discussion. It does best taking up first, of papers otherwise alike, the one whose author has a record of following the procedures.",
    "l:settled-convenor": "Whatever the others choose, the convenor does best following SD-4's plenary procedure unless their stake is worth more than what departing can cost them. That procedure fixes the call in two cases, declaring consensus when no one objects to unanimous consent or when all opposition is unescalated and holds no national position, and otherwise leaves it to the convenor.",
    "l:settled-nb": "Whatever the others choose, a national body whose comments fare the same under any vote does best voting Yes with comments if it values a document's rest above removing any one feature, and No otherwise. It does best raising its objections early, as SD-4 and ISO ask, and ISO encourages it to abstain when it lacks national consensus or expert input.",
    "l:settled-sponsor": "Whatever the others choose, a sponsor does best paying for participants in the rooms whose decisions it values, study groups included, while what their votes bring it is worth their cost. Each such participant votes valuing its interests, and no rule limits how many it pays.",
    "l:settled-user": "Whatever the others choose, a user without a sponsor does best taking part only when their own stake outweighs the full price, which they bear alone while any better design's gain goes to all users. Otherwise the best move is a cheaper one or none: TS feedback, a paper a participant presents, or a request to a national body.",
    "p:checks": "The rules provide these checks: every view must be heard, a third of the Favor-plus-Against votes can block, rivals with papers can be polled together, and implementation experience informs votes. Plenary invites serious design concerns, national bodies vote on each balloted draft and get answers to enquiry comments, editing committees verify applied changes, minutes can be challenged, and national bodies can appeal.",
    "l:checks-alternatives": "Chairs may allow limited exploration of alternatives, and SD-4 encourages polling alternatives side by side and asks a good paper to show the alternatives considered, its design principles, and motivating examples from today's code. Followup and rebuttal papers can be considered, an author who declines a directed change should defend that decision, and SD-4 does not significantly delay concrete proposals to wait for alternatives.",
    "l:checks-record": "SD-4 asks those with a concern to tell chairs and authors early, plenary solicits serious design concerns, national bodies vote on each enquiry and final ballot, every enquiry comment gets a written response, and editing committees verify applied changes. Minutes can be challenged, national bodies can appeal, on drafts only over principle or harm to ISO's or IEC's reputation, ISO says consensus requires resolving substantial objections and ends the committee stage when all technical issues are resolved, and SD-4 works in addition to the Directives.",
    "c:predictions": "If the settled pattern holds, the record should show the following. SD-4 keeps records of subgroup discussion password-protected but lets poll questions and numeric results be quoted, and each prediction names its evidence, counter-evidence, another explanation, and the data telling them apart.",
    "c:pred-sponsor-against": "Where one sponsor pays a proposal's authors and many participants present, and its interests include adoption, the model predicts a smaller Against share of the Favor-plus-Against votes than elsewhere; poll results and stated affiliations are the evidence. No smaller share would count against it, and comparing, by consented attribution, participants' votes on that sponsor's proposals before and after they move to a sponsor whose interests exclude those proposals would tell it apart from shared technical views.",
    "c:pred-abstention-length": "Among proposals with similar stakes polled in one room at one meeting, the model predicts fewer votes cast the longer the paper; quotable poll results and paper lengths are the evidence. No fall would count against it, and comparing papers on topics of similar breadth but different length would tell it apart from another explanation, that longer papers cover narrower topics fewer participants know.",
    "c:pred-parts": "The model predicts that large proposals tend to arrive as sequences of papers, each building on parts already adopted; the mailings are the evidence, and large designs mostly adopted in one paper would count against it. Another explanation is that large designs are easier to review in parts; whether later parts already drafted or implemented when the first was polled stayed out of the mailings until it was adopted would tell them apart.",
    "c:pred-first-part": "The model predicts that first papers of designs later extended part by part describe a small scope and seldom set out the later parts; the mailings are the evidence, and first papers setting them out would count against it. Another explanation is that small first steps lower risk; whether first papers left out later parts that already existed in drafts, implementations, or talks would tell them apart.",
    "c:pred-rival-polls": "The model predicts that once a design passes a design room's direction poll, a like rival draws less support than before in polls of the same form; quotable poll results are the evidence, and equal support would count against it. Another explanation is that the room learned more or the design improved; comparing only polls between which the incumbent's content and review time did not change would tell them apart.",
    "c:pred-removals": "The model predicts rare removals after adoption, by paper or ballot comment, likelier when national bodies whose No votes could fail a ballot oppose the design; working drafts, ballot comments, and poll results are the evidence. Frequent removals by narrow margins would count against it, and comparing removals with the papers or comments asking for them would tell it apart from another explanation, that adopted designs rarely need removal.",
    "c:pred-small-fade": "The model predicts that small proposals stop advancing without a negative poll more often than large ones; the mailings and poll results are the evidence, and no such difference would count against it. Another explanation is that small proposals are more often dropped on reflection; comparing stops by self-funded and sponsored authors on papers of similar length would tell them apart.",
    "c:pred-nb-positions": "The model predicts that national bodies state positions on few proposals; vetted national body comments and plenary records of national positions are the evidence, and positions on most proposals would count against it. Another explanation is that national bodies agree with most proposals; comparing how often they state positions on proposals with and without Against votes in subgroups would tell them apart.",
    "c:pred-written-answers": "The model predicts that papers advancing over Against votes often leave unstated the objections other published papers raised against them; the papers and poll results are the evidence, and routine answers would count against it. Another explanation is that the objections were answered in discussion; comparing such papers with what subgroup chairs answer at plenary when an objection is raised there would tell them apart.",
    "c:pred-defects": "If some unresolved objections point to real defects, the model predicts more defects found after adoption in features a design room forwarded over Against votes than in those forwarded with none; issues lists, correction papers, removals, and poll results are the evidence. No difference would count against it, and comparing features matched on scope, novelty, prior implementation, and use would tell it apart from another explanation, that contested features draw more scrutiny.",
    "c:pred-competing": "If closer study finds more defects, the model predicts fewer defects after adoption on topics whose deciding poll had competing papers from separate author groups than on one-paper topics; author lists, mailings, issues lists, and removals are the evidence. No difference would count against it, and comparing topics of equal novelty and poll turnout would tell it apart from another explanation, that important or well-understood topics draw rival papers and attention anyway.",
    "c:lever-reasons-all": "If SD-4 asked voters of every position to be ready to give reasons when the chair asks, Neutral would bear the reasons cost Against now bears, while not voting would bear none. The model predicts fewer Neutral votes and more participants not voting.",
    "c:lever-sponsor-limit": "If the rules limited how many participants one sponsor pays may vote in a room, the votes cast there by participants valuing its interests would be capped. The model predicts smaller differences in poll margins between large and small proposals.",
    "c:lever-nb-more": "If forming national positions during meetings cost less, national bodies would take more, and more plenary opposition would hold national positions, whose weight SD-4's procedure leaves to the convenor rather than the count. The model predicts larger changes in answer to objections national bodies back, slower progress for contested proposals, and less weight at plenary for how many participants each side has present.",
    "c:lever-nb-less": "If forming national positions during meetings cost more, national bodies would take fewer, plenary would seldom meet opposition holding them, and the ballot vote would be their only move counting directly toward stopping a document. Comments and appeals would remain, appeals on drafts only for principle or harm to ISO's or IEC's reputation, and the model predicts attendance, paid participants, and early incumbency deciding more content.",
}

THEOREM_P1 = "Under the rules and given the axioms, these choices form a settled pattern. A design-bound author seeks direction polls as early as they can pass, proposes first the smallest part that fixes the features it needs and can pass, and chooses the IS where it can pass. It leaves out a trade-off no reviewer would raise when stating it costs more than later exposure would, and answers objections with the cheapest change that keeps the design passing. A result-seeking author states trade-offs and makes changes whenever the better design they bring outweighs the votes or work they cost. It backs a rival that serves users better by more than its share of the reversal's cost. An author who values both chooses, at each two-way choice, as the type whose value differs more. A small proposal's author keeps it presented while its chance of adoption is worth the meetings still ahead, whose cost they bear alone. A regular votes Favor on colleagues' proposals they support, and Against one they doubt only when the change that vote can make outweighs the standing and time it costs. Otherwise the regular takes whichever of Neutral, not voting, or Favor does best, and Favor risks nothing with the colleague. A sponsor pays for participants where the decisions it values are made, study groups included. Chairs follow the 2:1 norm and the convenor SD-4's plenary procedure, unless their stake outweighs what departing can cost them. A national body whose comments fare the same under any vote votes Yes with comments unless removing one feature is worth as much to it as the rest of the document. A user without a sponsor takes part only when their own stake outweighs a full price borne alone, and otherwise uses a cheaper move or none."

THEOREM_P2 = "In this pattern a design's content can be fixed when it is least reviewed. Its first favorable poll can make it the incumbent, and objectors short of a third of the Favor-plus-Against votes cannot force a change. Every later rival or change must then redo work built on it, at a cost that grows whether or not the design is wrong. Objections count only in fixed forms and at fixed times, and some of how the committee applies these rules is learned only by attending. In a long deadlock, the group whose sponsors keep paying its costs can hold longest, whichever design is better. A proposal that costs more to read than most participants' stakes in it can advance with no change at all. An objector who arrives after adoption needs a paper or ballot comment meeting the 2:1 norm, faces a reversal cost that has grown, and finds unwritten objections kept only in memory. Other things equal, a proposal advances more readily when its authors keep presenting it or know the procedures, or when a sponsor pays for participants who hold its position. The same holds when the chair expects fewer problems from it, a poll has placed it among the work aimed at the next IS, or it is already the incumbent. No user votes, and the needs that reach a vote are those participants and their sponsors know, which need not match those of users at large. The participants present decide content, and no rule limits how many voters one sponsor pays for. A change to a design costs the sponsors who have built on it, while its gain is spread across all users. Authors get the adoption they value at the poll, while a flaw found only in implementation and use costs users later. Technical merit enters through what participants value, including a good result for users, and through the discussion, papers, and implementation experience that inform their votes. SD-4 assigns no one to rule on it, and the consensus test never asks whether an objection is right. No SD-4 step checks whether separately adopted designs work together, review worth its cost to users together but not to any one participant goes undone, and the record need not show whether objections were answered. The rules ask no author to state their own design's drawbacks. Leaving one out costs a design-bound author no step the rules require before adoption, while stating one can cost a result-seeking author votes. A first part that fixes a structure can be adopted before reviewers can study in detail what later parts need of it, and every rival to that structure must then replace it. The rules also provide checks: a third of the Favor-plus-Against votes can block, every view must be heard, rivals with papers can be polled together, implementation experience informs votes, and national bodies ballot each draft. Each result about large or small proposals holds for any proposal with the attributes it rests on."

CAPTIONS = {
    "t:mutual-support": "Two regulars, each with a proposal pending, each of which lowers what the other values by less than the cost of opposing it. For each, the other's opposition costs more than their own opposing does. Refrains means votes Favor, Neutral, or not at all. First number: A's rank. Second number: B's rank. 4 is best. \u2020 marks a Pareto-optimal cell.",
    "t:hold-or-yield": "Two groups in a deadlock, with equal stakes in their own designs. Group A's sponsors pay its participants' costs and value its holding above what they pay, while group B's participants pay their own. Holding through the deadlock costs group A less than half its stake and group B more than half. A deadlock both hold ends with either design equally likely, and both yielding means a compromise worth half its stake to each. First number: group A's rank. Second number: group B's rank. 4 is best. \u2020 marks a Pareto-optimal cell.",
    "t:chair-call": "A design room chair's consensus call, when the chair's stake in the proposal is worth less to them than what departing from SD-4's norm can cost them. Neutral votes are short of a majority of those voting, and a re-poll fits the norm at any count. Columns: the count after discussion of the Against voters' concerns. Each cell: the chair's rank of the call. 2 is best within each column.",
    "t:disclose": "An author's choice, before an early direction poll, whether to state in the paper a trade-off no reviewer would otherwise raise. Stating it would lead the room to change, in a way that serves users better, a feature a design-bound author's gain depends on, and the proposal meets the 2:1 norm either way. Columns: the author's type. Each cell: the author's rank of the choice. 2 is best within each column.",
    "t:nb-ballot": "A national body's ballot vote. Columns: how the body values the document. \"Values the rest\" means it values publishing the rest of the document on schedule above removing any one feature through a failed ballot and a revised draft, and expects its comments to fare the same under any vote, as SD-4 says. \"Opposes the work\" means it does not want the work at all. In both, the body cannot rule out that its vote decides the result. Each cell: its rank of the vote. 3 is best within each column.",
}

ROWS = {
    "| **Decline or re-poll** | 1 | **2** |": "| **Decline** | 1 | **2** |",
}

HEADINGS = {"## 5. Momentum: incumbents and the cost of reversal": "## 5. Incumbents and the cost of reversal"}

ADD_FROM = {
    "p:who-decides": ["d:follows-norm"],
    "p:sponsor-votes": ["ax:prefer", "d:rules"],
    "p:early-polls": ["ax:rework"],
    "p:challenger-bar": ["ax:rework"],
    "ind:adopted-parts": ["ax:rework"],
    "p:burden-flip": ["d:follows-norm"],
    "p:sg-sponsor": ["d:follows-norm"],
    "p:fluency": ["f:late-documents"],
    "p:chair-threshold": ["ax:post-risk"],
    "p:chair-default": ["d:follows-norm", "ax:post-risk", "d:stake"],
    "l:call-above": ["d:follows-norm"],
    "l:call-below": ["d:follows-norm"],
    "p:written-answer": ["f:ts-disposition", "f:iso-no-answer", "d:rules"],
    "p:cutoff-effect": ["d:follows-norm"],
    "p:prefer-is": ["f:ts-unblock"],
    "p:credible-threat": ["f:no-means-no"],
    "l:incits-votes": ["f:incits-control"],
    "l:settled-design-chair": ["d:follows-norm"],
    "l:settled-sponsor": ["d:rules"],
    "l:settled-nb": ["f:no-means-no"],
    "l:checks-alternatives": ["f:example-based", "f:no-wait-alternatives"],
    "l:checks-deadlock": ["ax:schedule"],
    "p:checks": ["d:follows-norm"],
    "thm:settled": ["d:rules", "d:follows-norm", "p:least-cost-response"],
    "c:pred-sponsor-against": ["f:protected"],
    "c:pred-abstention-length": ["f:protected"],
    "c:pred-rival-polls": ["f:protected"],
    "c:pred-nb-positions": ["f:comment-vetting"],
    "c:pred-defects": ["f:design-forward"],
    "c:lever-nb-more": ["p:credible-threat"],
}

REMOVE_FROM = {
    "p:large-position": ["f:prioritization", "f:design-forward", "f:wording-forward", "f:plenary-owns"],
    "l:incits-votes": ["f:incits-position", "f:incits-caucus"],
}

REPOINT = {"l:vote-below": "p:doubt-outside-count", "l:vote-above": "p:doubt-outside-count"}
DROP_PROVED = {"p:doubt-outside-count"}
ADD_PROVED = {"p:nb-members": ["l:incits-positions"]}
CUT_ITEMS = ["l:vote-below", "l:vote-above"]
CUT_TABLES = ["t:vote-choice"]
INSERT_AFTER = {
    "l:incits-votes": "   1. **Lemma.** INCITS's Executive Board approves the United States position that goes to ANSI, and every United States delegate must support an official position, which the TAG may set before a meeting. At an international plenary, the delegation may determine the position on a new issue by caucus consensus. *[from f:incits-position, f:incits-delegates, f:incits-caucus]* {#l:incits-positions}",
}

KEYPAT = r"\{#%s(?: weakened)?\}"
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
        new = []
        for k in keys:
            k2 = REPOINT.get(k, k)
            if k2 == key:
                continue
            if kind == "from" and k2 in REMOVE_FROM.get(key, []):
                continue
            if k2 not in new:
                new.append(k2)
        if kind == "proved by" and key in DROP_PROVED:
            new = []
        if kind == "proved by" and key in ADD_PROVED:
            new += [k for k in ADD_PROVED[key] if k not in new]
        out.append((kind, new))
    if key in ADD_FROM:
        kinds = [k for k, _ in out]
        if "from" not in kinds:
            out.append(("from", []))
        for i, (kind, keys) in enumerate(out):
            if kind == "from":
                for k in ADD_FROM[key]:
                    if k not in keys:
                        keys.append(k)
                out[i] = (kind, keys)
    if key in ADD_PROVED and "proved by" not in [k for k, _ in out]:
        out.insert(0, ("proved by", list(ADD_PROVED[key])))
    return out


def process(path, used):
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line in HEADINGS:
            out.append(HEADINGS[line])
            used.add("heading")
            i += 1
            continue
        cap = re.match(r"^\*Table: (.*)\* \{#(t:[a-z0-9-]+)\}\s*$", line)
        if cap and cap.group(2) in CUT_TABLES:
            j = i + 1
            while j < len(lines) and not lines[j].startswith("*["):
                j += 1
            j += 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            while out and not out[-1].strip():
                out.pop()
            if j < len(lines) and not re.match(r"^\s*1\.\s", lines[j]):
                out.append("")
            used.add(cap.group(2))
            i = j
            continue
        if cap and cap.group(2) in CAPTIONS:
            out.append("*Table: %s* {#%s}" % (CAPTIONS[cap.group(2)], cap.group(2)))
            used.add(cap.group(2))
            i += 1
            continue
        if line in ROWS:
            out.append(ROWS[line])
            used.add("row")
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
            if not line.startswith("1. **Theorem.** Under SD-4 and the quoted clauses"):
                sys.exit("Theorem already changed in " + path.name)
            out.append("1. **Theorem.** " + THEOREM_P1)
            used.add("thm-p1")
            i += 1
            continue
        if km:
            key = km.group(1)
            if key == "thm:settled" and not line.lstrip().startswith("1."):
                prefix, stmt, bases, key_text = split_line(line)
                stmt = THEOREM_P2
                used.add("thm-p2")
                out.append(join_line("   ", stmt, edit_bases(key, bases), key_text))
                i += 1
                continue
            prefix, stmt, bases, key_text = split_line(line)
            if key in NEW:
                stmt = NEW[key]
                used.add(key)
            new_bases = edit_bases(key, bases)
            out.append(join_line(prefix, stmt, new_bases, key_text))
            if key in INSERT_AFTER:
                # place after this item's own children in the chapter
                indent = len(line) - len(line.lstrip())
                j = i + 1
                while j < len(lines) and lines[j].strip() and (len(lines[j]) - len(lines[j].lstrip())) > indent:
                    out.append(lines[j])
                    j += 1
                out.append(INSERT_AFTER[key])
                used.add("insert:" + key)
                i = j
                continue
            i += 1
            continue
        out.append(line)
        i += 1
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def main():
    targets = [SPINE] + CHAPTERS
    seen = {}
    for path in targets:
        used = set()
        process(path, used)
        for u in used:
            seen.setdefault(u, []).append(path.name)
        if used:
            print("%s: %d edits" % (path.name, len(used)))
    wanted = list(NEW) + list(CAPTIONS) + CUT_ITEMS + CUT_TABLES + ["thm-p1", "thm-p2", "heading", "row"]
    wanted += ["insert:" + k for k in INSERT_AFTER]
    for w in wanted:
        files = seen.get(w, [])
        if len(files) != 2 or files[0] != SPINE.name:
            print("CHECK %s applied in %s" % (w, files))


if __name__ == "__main__":
    main()
