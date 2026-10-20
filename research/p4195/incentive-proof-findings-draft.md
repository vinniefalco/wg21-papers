# What WG21's Rules Reward: Findings From the Incentive Proof

WG21's rules make the content of the C++ standard depend on who is in the room, when they vote, and what it costs them to say no. The participants present decide a design's content, by votes on which a chair calls consensus under a two-to-one norm. A design's first favorable direction poll can make it the incumbent while it is least reviewed, and every later rival or change then pays a reversal cost that grows whether or not the design is wrong. Objections count only in the forms and by the deadlines that attending teaches. A sponsor can add voters without limit, and in a long deadlock the side whose costs are paid can hold longest, whichever design is better.

What the rules leave out is as specific. No user votes. SD-4 assigns no one to judge whether a design is good, and its consensus test never asks whether an objection is right. No SD-4 step checks that separately adopted designs work together. The required record need not show whether an objection was answered or outvoted, and no author is asked to state a trade-off. Merit enters only through the voters: what they value, a good result for users included, and what they have learned by the time they vote.

The rules also have checks, among them the third of the votes that can block and plenary's call for serious design concerns, and every finding below holds with them in place. None assumes bad faith; each describes what the rules reward.

## 1. A Vote to Keep Working Makes the Incumbent

**A design can become the incumbent at its first direction poll, when it has had less review than at any later meeting, and from then on every rival and every change to it pays a reversal cost that grows whether or not the design is wrong.**

A direction poll asks voters only to agree that work should continue, so it can pass where a forwarding poll would fail, yet passing it in a design room makes the design the incumbent. An author whose gain depends on particular features staying fixed, whom the proof calls design-bound, has no better move than to seek that poll as early as it can pass.

So the starting design is chosen when the least is known about it. Every decision built on it afterward, in wording, implementations, and dependent proposals, adds work a reversal would redo or discard: a mistake is cheapest to fix at the first poll and dearer at every step after. Every improvement users later receive pays that rising price.

- **What would show this wrong:** rivals still polled as equal alternatives after a design passes its direction poll, or like rivals faring no worse in same-form polls after incumbency than before (`c:pred-rival-polls`).
- **Proved by:** `p:early-polls`, `l:poll-wording`, `p:incumbent-start`, `ind:reversal-grows`, `l:settled-design-bound`

## 2. Better Is Not Enough: The Rival Pays the Reversal Cost

**A rival wins a voter from the incumbent only if, to that voter, its advantage outweighs their share of the reversal cost, a hurdle that grows with each decision built on the incumbent while the incumbent faces none, and once the incumbent is adopted, the default switches to keeping it.**

Two credible designs face different questions. The incumbent must meet the 2:1 norm; the rival must also beat, for each voter, that voter's share of the cost of discarding what was built on the incumbent. A rival without a paper does not block it at all, and by default a TS ready to merge proceeds with the design in hand unless an alternative is actively progressing.

An objector who arrives after adoption meets three obstacles at once: removal needs its own paper meeting the 2:1 norm, reversal costs more for every decision built on the design, and the design's case lasts in its paper while unwritten objections live only in memory. After a successful final ballot, design changes are expected to have near-unanimous consent. A flaw that implementation and use expose only after adoption meets all of this.

- **What would show this wrong:** frequent removals of adopted designs by narrow margins, or removals that track the defect reports filed against adopted features (`c:pred-removals`).
- **Proved by:** `p:challenger-bar`, `p:incumbent-start`, `p:burden-flip`, `p:late-arrival`

## 3. No Design Is Heard on Merit Alone

**No design is considered on merit alone: a proposal needs an on-time paper and a presenter, a rival needs a paper to exist, and objections need fixed forms and times, all learned partly by attending and some only that way, so other things equal, whoever knows the procedures has the better chance of adoption, whatever their design skill.**

An objection not escalated on the email lists and within the objector's national body by 5pm the evening before the closing plenary gets no weight there. One repeated after a consensus call without new information or an allowed escalation is described as not accepting a group decision, whether or not anyone answered it.

Other things equal, a newcomer spends more effort than a returning participant getting a paper considered, and of two papers otherwise alike, a chair does better taking up first the one whose author has a record of following the procedures, which only taking part builds. First-time authors and late critics pay these costs whatever their designs or objections are worth.

- **What would show this wrong:** papers by first-time participants advancing as readily as otherwise similar papers by returning ones (the other-things-equal condition in `p:fluency`).
- **Proved by:** `p:fluency`, `p:newcomer`, `p:late-objection`, `p:repeat-objection`, `p:chair-confidence`

## 4. Hard-to-Study Designs Are Voted On by Those With the Most at Stake

**Participants who do not study a proposal typically abstain, so one that costs more to study than most participants' stakes in it is voted on mainly by those with large stakes, and unless the objectors among them cast at least a third of the Favor-plus-Against votes, it can advance with no change at all.**

Close study takes longer the bigger a design is, and a bigger design has more places for a defect to go unnoticed. A reviewer whose stake does not grow with size stops finding close study worth the time sooner on a big design, so the designs with the most places for a defect to hide lose those reviewers first.

The reviewer bears the cost of study while the gain is spread across every user, so review worth its cost to users together, but not to any one participant, is review no participant does better doing. When the objectors who studied fall short of a third, the cheapest answer that keeps the norm met is no change or a partial one.

- **What would show this wrong:** among proposals with similar stakes and topics of similar breadth, no rise in the share of those present not voting as papers grow longer (`c:pred-abstention-length`).
- **Proved by:** `p:light-review`, `p:review-share`, `p:review-shortfall`, `p:least-cost-response`

## 5. The People Who Use the Standard Never Vote on It

**No user votes in any WG21 poll or in the ballots on its drafts, and users' interests reach decisions only through what participants themselves value, papers a participant presents, TS feedback, and national bodies, which form positions only where that is worth their members' time.**

A user can become a participant, but one person pays the full price while a better design's gain is shared by every user of the feature, and one user's effort seldom changes an outcome. So a user takes part only when their own stake outweighs a cost borne alone, and the votes are cast by those who bear that cost or whose sponsors do.

The needs that reach a vote are those participants and their sponsors know, and since users differ from participants in what matters, those needs need not match users' needs. National bodies, which ISO asks to take account of all interests at the national level, form positions only where that is worth their members' time. Every design adopted this way applies to every user of its feature.

- **What would show this wrong:** national bodies stating positions on most proposals rather than on few (`c:pred-nb-positions`).
- **Proved by:** `p:who-votes`, `m:moves-user`, `p:users-out`, `p:who-takes-part`, `l:settled-user`

## 6. The Author Gains at Adoption; the Users Pay Later

**An author gains at adoption while a flaw that implementation and use have not yet exposed costs users afterward, and because a TS, the route for gaining that experience first, delays adoption by about one to two years and can bring incompatible changes, a design-bound author has no better move than to seek the IS unless the room requires a TS.**

The gain and the risk arrive at different times and fall on different people: the author's gain at the vote, a hidden flaw's cost later, on any user of the feature, none of whom voted. An author who values a good result for users weighs that later cost, and the proof counts that value; what the rules fix is the order.

A TS ships the design as an experiment and asks implementers and users to report shortcomings. To an author whose gain depends on how well the design serves users, whom the proof calls result-seeking, that experience is a gain; to a design-bound author it is delay plus risk to the features it needs. The design room can still require a TS.

- **What would show this wrong:** a TS made no slower than an edition, followed by no rise in the designs sent to a TS or white paper (`c:lever-ts-path`).
- **Proved by:** `p:reward-timing`, `l:implementation-informs`, `p:prefer-is`, `l:settled-design-bound`

## 7. Whoever Is Present Decides, and Presence Can Be Paid For

**The participants present decide a design's content, a sponsor adds one voter to the room for each participant it pays to attend, and neither SD-4 nor the ISO clauses the proof searched limit how many participants one sponsor pays.**

Design is settled in the design rooms and the study groups feeding them: wording rooms check only that wording expresses the design, plenary does not redesign, and national bodies ballot only on whole documents. A study group picks the design the design room starts from, and the fewer its other voters, the fewer paid participants make up the third that blocks or the more than two thirds that meets the norm.

Paid presence also decides who can wait. When two groups each cast at least a third of the votes against the other's design, neither meets the norm, and each meeting of deadlock costs a sponsored group less than a self-funded one. With equal stakes, if holding costs the sponsored group under half its stake and the other over half, the first holds and the second yields, whichever design is better.

- **What would show this wrong:** where one sponsor pays a proposal's authors and many of those present, an Against share no lower than on similar same-topic proposals by authors with other affiliations (`c:pred-sponsor-against`).
- **Proved by:** `p:who-decides`, `p:sponsor-votes`, `p:sg-sponsor`, `p:deadlock`, `p:attrition`

## 8. Doubt Counts Only When It Is Worth Voting Against

**An Against vote on a colleague's proposal costs a regular more than a Neutral vote or none, because it risks the colleague's later support no less and only Against voters can be asked for reasons, so a doubt enters the 2:1 count only when it is worth that extra cost.**

A chair may ask anyone voting Against for reasons, including the changes that would win them over or that none would; no step asks the same of a Neutral voter, so a participant can argue for another design, vote Neutral, and leave the count unchanged. One more Against vote changes the result only when the count sits one or two votes above the line, though it can also win changes to the design.

Two regulars with proposals pending each risk the other's support by opposing, and when each one's doubt is worth less than that risk and the time for reasons, neither opposes, and both do better than if both had. No agreement is needed: restraint is each one's best move whatever the other does.

- **What would show this wrong:** anonymous design polls drawing no more Against votes on colleagues' proposals than polls whose votes colleagues can see (`c:lever-anonymous`).
- **Proved by:** `p:against-costs-more`, `p:doubt-outside-count`, `p:prefer-vs-stop`, `p:mutual-support`, `l:settled-regular`

## 9. Nobody Is Assigned to Judge Whether a Design Is Good

**Winning a consensus call and producing the design that serves users best coincide only as far as voters can judge quality at the poll and weigh it above their other values: SD-4 assigns no one to judge it for them, and its consensus test never asks whether an objection is right.**

What connects a vote to a good design is the voters: what they value and what discussion, papers, and implementation experience have shown them. A proposal can advance with objections unresolved, and when the Against votes are too few to stop the 2:1 norm, learning whether those objectors are right leaves the count unchanged.

SD-4 requires minutes but no record of how an objection was answered or why consensus was called over it, and no step for registering a sustained opposition. The proposal's case lasts for decades in its paper. Outside the protected records, an objection's argument outlasts its hearers only in writing, such as a paper; otherwise the public record shows its holders as a number in a tally.

- **What would show this wrong:** features adopted while Against votes remained showing no more defects after adoption than features adopted by unanimous consent, matched on scope, novelty, prior implementation experience, and use (`c:pred-defects`).
- **Proved by:** `p:merit-gap`, `l:consensus-test`, `p:persuasion-not-required`, `p:least-cost-response`, `p:record-indistinct`, `p:definition-without-procedure`, `p:reasons-unrecorded`, `p:dissent-needs-paper`

## 10. No Step Checks That Separately Adopted Papers Work Together

**Papers approved separately at one meeting first come together when the project editor merges their wording, and no SD-4 step checks whether their designs work together, while each author gains from their own design's adoption and a conflict costs users and later rework.**

Each paper's wording is written against the draft adopted at the meeting's start and approved in its own plenary poll. The editor then applies them all and reports what arose in merging, and before a ballot an editing committee verifies that the changes were applied correctly. Those steps check that the text says what was approved, not that the designs fit each other.

A design with more parts and more interactions with existing wording has more places for a defect to go unnoticed. Checking one design against another costs the checker time while the gain is spread across every user, so where that check is worth more to users together than to any one participant, no participant does better making it.

- **What would show this wrong:** a step in SD-4 in which someone checks designs adopted in separate papers against each other; the result rests on a search that found none.
- **Proved by:** `p:integration`, `p:review-shortfall`

## 11. Stating a Trade-off Can Cost Votes; Leaving It Out Costs Nothing the Rules Impose

**The rules ask no paper to state its design's drawbacks, its sponsor, or what its author's gain depends on, so for a trade-off no reviewer would otherwise raise, leaving it out costs a design-bound author nothing the rules impose, while stating it can cost a result-seeking author Favor votes the other keeps.**

Stating a drawback before an early poll can cost Favor votes just when incumbency is decided, while the gain from a better-informed vote is spread across the design's users. SD-4 asks a good paper to show the alternatives considered, but not the design's own drawbacks, and a paper is considered without them.

Take a trade-off no reviewer would raise that, if stated before an early direction poll, would lead the room to change a feature so the design serves users better, with the 2:1 norm met either way. The result-seeking author does better stating it, the design-bound author leaving it out. Both follow the rules, and nothing a paper must contain shows which kind wrote it.

- **What would show this wrong:** a rule asking papers to state their drawbacks, or first papers of designs later extended in parts routinely setting out the later parts they serve (`c:pred-first-part`).
- **Proved by:** `p:disclosure`, `p:same-moves`, `t:disclose`, `l:settled-design-bound`, `l:settled-result-seeking`

## 12. The Smallest Part That Fixes the Structure Goes First

**Reviewers cannot study what later parts will need of a first part that fixes a design's structure, SD-4 asks no paper to say, and once that part is adopted every rival must replace it, so a design-bound author's best first paper is the smallest part that fixes the structure and still meets the 2:1 norm against opponents who foresee the rest.**

Presenting a design in parts lets the first parts be adopted before the whole is reviewed, at the cost of a paper and a presentation for each. Once a part is adopted, every later part builds on it, and a rival to the whole must replace every part already in.

The 2:1 norm sets the limit: if opponents who foresee the rest can cast a third of the votes against the smallest such part, the best first paper is one that can pass. Short of that, the structure everything later depends on is fixed by the vote that could see the least of what depends on it.

- **What would show this wrong:** large designs adopted in one paper, or designs presented in parts publishing all their parts together rather than each only after the last is adopted (`c:pred-parts`).
- **Proved by:** `p:first-part`, `p:parts`, `ind:adopted-parts`, `l:settled-design-bound`

## What Follows for Reform

These results follow from rules and from what moves cost, so changing either changes the pattern. The proof names nine such changes and predicts what each would do:

- **Require a written answer to each objection in the record.** Papers advancing over Against votes would state the objections they faced.
- **Adopt ISO's steps for assessing, registering, and addressing a sustained opposition, with a recorded answer.** Registered oppositions would appear in WG21's records.
- **Limit how many participants paid by one sponsor may vote in a room.** Poll margins would differ less between large and small proposals.
- **Set a decision procedure for deadlocks that last a set number of meetings.** Fewer deadlocks would end with one side ceasing to attend.
- **Make a TS no slower than an edition.** More designs would go to a TS or white paper.
- **Make national positions cheaper to form during meetings.** Objections national bodies back would win larger changes, contested proposals would move more slowly, and how many participants each side has present would weigh less at plenary.

Some levers have a price. Anonymous design polls would draw more Against votes on colleagues' proposals, but chairs could no longer ask Against voters for reasons. Letting chairs ask voters of every position for reasons would mean fewer Neutral votes and more participants not voting at all. Making national positions costlier to form would leave attendance, paid participants, and early incumbency deciding more content.

None of these asks anyone to behave better. Each changes what the rules reward.

*2026-10-19 11:00 - claude-opus-5.5*
