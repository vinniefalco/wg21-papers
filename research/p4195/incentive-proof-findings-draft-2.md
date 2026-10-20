# What WG21's Rules Reward: Findings From the Incentive Proof

Under WG21's rules, what goes into C++ depends on who is in the room and when they vote, and no one is assigned to judge whether it is good. A design can become the incumbent while it is least reviewed. Every rival then pays a reversal cost that grows whether the design is right or wrong. Objections count only in forms and by deadlines that attending teaches. SD-4 sets no limit on sponsored voters, and in a long deadlock the side whose costs are paid can hold longest, whichever design is better. No user votes. No SD-4 step checks that separately adopted designs work together, and the record need not show whether an objection was answered or outvoted.

The rules do have checks, such as a blocking third of the votes, and every finding holds with them in place. None assumes bad faith. Each describes what the rules reward.

## 1. Better Is Not Enough

**A design can become the incumbent while least reviewed, and its reversal cost then grows, right or wrong.**

Users can be left with a design chosen when the least was known about it, and everything built on it since raises the price of undoing it, though the design has grown no more wrong. Once adopted, it stays unless a removal meets the 2:1 norm.

The first direction poll comes when a design is least reviewed. It asks only whether work should continue, yet passing it in a design room makes the design the incumbent. To win each voter, a rival's advantage must exceed that voter's share of the cost of discarding what was built. The incumbent faces no such test. For an author tied to particular features, such as those a sponsor relies on, the best move is to seek that poll as early as it can pass.

- **What would show this wrong:** rivals still polled as equal alternatives after a design passes its direction poll, or frequent removals of adopted designs by narrow margins (`c:pred-rival-polls`, `c:pred-removals`).
- **Proved by:** `p:early-polls`, `l:poll-wording`, `ind:reversal-grows`, `p:challenger-bar`, `p:burden-flip`, `l:settled-design-bound`

## 2. No Design Is Heard on Merit Alone

**No design is considered on merit alone, and procedural knowledge raises an author's odds regardless of design skill.**

Work from outside the room starts behind, however good it is. Take two papers alike in every other way. The one from a first-time author takes more effort just to get considered. The one whose author knows the procedures has the better chance, and a chair has reason to take it up first if that author has a record of following them.

A proposal needs an on-time paper and a presenter, and a rival without a paper "does not exist." An objection not escalated on the email lists and in the objector's national body by 5pm the evening before the closing plenary counts for nothing there, which leaves the late critic out. Part of this is learned only by attending.

- **What would show this wrong:** papers by first-time participants advancing as readily as otherwise similar papers by returning ones (the condition in `p:fluency`).
- **Proved by:** `p:fluency`, `p:newcomer`, `p:late-objection`, `p:chair-confidence`

## 3. Doubt Stays Out of the Count

**A design too costly for most to study can pass unchanged, voted on mainly by large stakeholders.**

The designs with the most places for a defect to hide lose close study first. Study takes longer the bigger a design is, so reviewers whose stake does not grow with size give it up sooner, and those who skip the study typically skip the vote. Unless the objectors who remain cast a third of the Favor-plus-Against votes, the cheapest answer is no change or a partial one.

Voting Against a colleague's proposal risks that colleague's later support, and only Against voters can be asked for reasons. Neutral costs less and leaves the count untouched, so a doubt counts only when it is worth that price. Two colleagues with proposals pending, each doubting the other's by less than that price, both refrain, with no agreement needed.

- **What would show this wrong:** among proposals of similar stakes and breadth, no rise in abstentions as papers lengthen (`c:pred-abstention-length`), or anonymous polls drawing no more Against votes on colleagues' proposals (`c:lever-anonymous`).
- **Proved by:** `p:light-review`, `p:review-share`, `p:least-cost-response`, `p:against-costs-more`, `p:doubt-outside-count`, `p:mutual-support`

## 4. The Author Gains at Adoption; the Users Pay Later

**The author gains at adoption; users pay for any flaw found later, and no user votes.**

The needs that reach a vote are the ones participants and their sponsors know, which need not match users'. A user can become a participant but pays the full price alone, while a better design's gain is shared by every user and one user rarely changes an outcome. Users' interests arrive only through participants' own values, papers a participant presents, TS feedback, and national bodies, which form positions only where that is worth their members' time.

A TS, SD-4's way to find shortcomings before the IS, delays adoption by about one to two years and can bring incompatible changes. So the author tied to particular features seeks the IS unless the design room requires a TS, and flaws still hidden at adoption land on users.

- **What would show this wrong:** national bodies stating positions on most proposals rather than few (`c:pred-nb-positions`), or a TS made no slower than an edition drawing no more designs (`c:lever-ts-path`).
- **Proved by:** `p:who-votes`, `p:users-out`, `p:who-takes-part`, `p:reward-timing`, `p:prefer-is`, `l:settled-user`

## 5. Whoever Is Present Decides, and Presence Can Be Paid For

**Whoever is present decides a design's content, and SD-4 sets no limit on how many voters one sponsor pays for.**

The standard's designs are chosen by whoever is in the design rooms and study groups at the poll. A sponsor adds one voter there for each participant it pays to send; SD-4 sets no limit on how many, though SC22 may cap the experts each national body or liaison appoints. In a study group, where the starting design is picked, the fewer the other voters, the fewer paid participants it takes to block or to pass.

Paid presence also decides who can wait out a deadlock. When two groups can each block the other, every meeting costs the sponsored group less than the self-funded one. With equal stakes, if holding costs the sponsored group under half its stake and the other over half, the first holds and the second yields, whichever design is better.

- **What would show this wrong:** where one sponsor pays a proposal's authors and many of those present, an Against share no lower than on similar same-topic proposals by authors with other affiliations (`c:pred-sponsor-against`).
- **Proved by:** `p:who-decides`, `p:sponsor-votes`, `p:sg-sponsor`, `p:deadlock`, `p:attrition`

## 6. Nobody Is Assigned to Judge Whether a Design Is Good

**SD-4 assigns no one to judge quality, and its consensus test never asks whether an objection is right.**

A correct objection held by too few voters can be outvoted and the design adopted over it. The best design for users wins only as far as voters can see its quality at the poll and put it first. When objectors are too few to stop the 2:1 norm, learning whether they are right changes nothing in the count.

Nor must the record say what happened. SD-4 requires minutes but no account of how an objection was answered or why consensus was called over it. The proposal's case lasts for decades in its paper. Outside the protected records, an objection's argument outlives its hearers only in writing, such as a paper. Otherwise the public record shows its holders as a number in a tally.

- **What would show this wrong:** features adopted while Against votes remained showing no more defects after adoption than features adopted by unanimous consent, matched on scope, novelty, prior implementation experience, and use (`c:pred-defects`).
- **Proved by:** `p:merit-gap`, `l:consensus-test`, `p:persuasion-not-required`, `p:least-cost-response`, `p:record-indistinct`, `p:reasons-unrecorded`, `p:dissent-needs-paper`

## 7. No Step Checks That Separately Adopted Papers Work Together

**No SD-4 step checks that separately adopted designs work together; a conflict falls on users and later rework.**

Two features can each clear every review and still conflict once both are in the standard. Papers approved separately at one meeting first meet when the project editor merges their wording. The editor reports what arose, and before a ballot an editing committee verifies that approved changes were applied correctly. Those steps check the text against the votes, not one design against another.

Each author gains from their own design's adoption. A design with more parts and more interactions with existing wording has more places for a defect to hide. Checking one design against another costs the checker time, while the gain is spread across every user, so that review, worth its cost to users together but not to any one participant, goes undone.

- **What would show this wrong:** a step in SD-4 in which someone checks designs adopted in separate papers against each other; the result rests on a search that found none.
- **Proved by:** `p:integration`, `p:review-shortfall`

## 8. What Reviewers Cannot See, the Author Need Not Say

**Stating drawbacks can cost votes and omitting them costs nothing the rules impose; a first part can fix structure early.**

Users can inherit a structure voted on before anyone could study what it must support. For a trade-off no reviewer would raise, leaving it out costs nothing the rules impose, while stating it before an early poll can cost Favor votes as incumbency is decided. So when stating it would improve the design without sinking it, the author who cares only about users states it and the author tied to particular features does not. No paper must show which kind wrote it.

A first part's reviewers cannot study what later parts will need of it, and SD-4 asks no paper to say. Once it is adopted, every rival must replace it. So that author's best opening paper is the smallest part that fixes the structure and still clears the 2:1 norm against opponents who foresee the rest.

- **What would show this wrong:** a rule asking papers to state drawbacks, or the first papers of designs later extended in parts routinely setting out what those parts need (`c:pred-first-part`).
- **Proved by:** `p:disclosure`, `p:same-moves`, `t:disclose`, `p:first-part`, `p:parts`, `ind:adopted-parts`

## What Follows for Reform

The proof names rule changes that would each remove the support for a named result. A written answer to each objection would show whether it was answered, and adopting ISO's steps for a sustained opposition would put registered oppositions in WG21's records. Capping how many of the participants one sponsor pays may vote in a room would narrow the gap in poll margins between large and small proposals. A procedure for deadlocks that last a set number of meetings would mean fewer ending when one side stops attending. Cheaper national positions would bring larger changes in answer to objections national bodies back, though contested proposals would move more slowly. Anonymous polls would draw more Against votes on colleagues' proposals, but chairs could no longer ask for reasons.

None of these asks anyone to behave better. Each changes what the rules reward.

*2026-10-19 11:14 - claude-opus-5.5*
