# What WG21's Rules Reward: Findings From the Incentive Proof

Under WG21's rules, the participants present decide what each C++ design contains, and SD-4, WG21's document of practices and procedures, assigns no one to rule on whether the design is good. A design becomes the incumbent, the design the room has agreed to keep working on, when it passes its first direction poll in EWG or LEWG. That poll can come at the meeting where the design is first presented, when it has had less review than it will ever have again. From then on, every rival and every later change must redo or discard the work built on it, at a cost that grows whether or not the design is wrong. Other things equal, knowing the procedures raises an author's chance of adoption whatever their design skill. No user votes. No rule limits how many voters one sponsor pays for, and in a long deadlock the group whose sponsors keep paying can hold longest, whichever design is better. No SD-4 step checks that separately adopted designs work together, the rules never ask an author for a design's drawbacks, and the record need not show whether an objection was answered or outvoted. These results use only SD-4's text, a few clauses of the ISO/IEC Directives, and assumptions any participant would grant. Each holds with the rules' checks in place, none assumes bad faith, and Appendix A proves them.

## 1. Better Is Not Enough

**A design can become the incumbent while it is least reviewed. From then on, a rival wins a voter only with an advantage worth more to that voter than their share of the cost of undoing what was built, and the incumbent needs no advantage to stay.**

A direction poll asks only whether work on a design should continue. A forwarding poll, which sends a proposal on to the next room, asks more, so a direction poll can pass where a forwarding poll would fail: even a voter who doubts the design can prefer that work continue, since the room can still direct changes. Passing one in EWG or LEWG, the design rooms, makes the design the incumbent, and the chair may take it at the meeting where the proposal is first presented. An author whose gain depends on the adopted design keeping particular features, for example because the interests of a sponsor, an organization paying the author's costs, depend on them, does best seeking that poll as early as it can pass. The proof calls this author design-bound.

Replacing an incumbent is a reversal: the removal or replacement of something the committee approved. It redoes or discards the wording, implementations, and dependent proposals built on the design, at a cost to their builders and in meeting time taken from other papers, and more is built after every favorable poll. So the cost of reversal grows as the design advances, whether or not it is wrong, and the advantage a rival needs grows with it. Under the 2:1 norm, SD-4's statement that a proposal normally advances when its Favor votes are more than twice its Against votes, objectors who cast less than a third of the votes cast Favor or Against cannot force a change with their votes. Once the design is adopted, removing it takes a paper or ballot comment that itself meets the 2:1 norm. The default has switched to keeping it.

Users can be left with a design whose content was fixed when it had its least review, and everything built on it raises the price of changing it, right or wrong. SD-4 describes where that ends: "Once a feature is in an IS, it is essentially cast in stone and much more difficult to update with breaking changes."

- **Rests on:** "We cannot act on ideas without papers, and we do not significantly delay progress on concrete proposals in order to wait for alternative proposals we might get in the future." (SD-4, "Proposals and papers")
- **What would show this wrong:** a similar rival drawing as much support after a design becomes the incumbent as before, in polls of the same form between which the incumbent's content and review time did not change (`c:pred-rival-polls`); or frequent removals of adopted designs by narrow margins (`c:pred-removals`).
- **Appendix A:** `p:early-polls`, `l:first-meeting-poll`, `l:poll-wording`, `ind:reversal-grows`, `p:challenger-bar`, `p:burden-flip`, `l:settled-design-bound`, `l:thm-fixed-early`

## 2. Every Design Needs More Than Merit

**Every design needs more than merit to be considered, and other things equal, the author who knows more of the procedures has the better chance of adoption, whatever their design skill.**

A proposal is considered only with an on-time paper and a qualified, prepared presenter. A rival without a paper, in SD-4's words, "does not exist" and does not block the proposal before the room. An objection counts in a subgroup poll only as a vote cast there. At plenary, the closing session where WG21 votes to adopt changes, SD-4 says an objection should get no weight unless its holder escalated it during the week, on the email lists by 5pm the evening before and within their national body, the national standards body that is a voting member of SC22, the ISO committee WG21 belongs to. When the only opposition was not escalated in time and holds no national position, SD-4's procedure has WG21's convenor declare consensus.

How the committee applies these rules is learned partly by attending, some of it only that way, and that knowledge differs from design skill. Other things equal, a proposal advances more readily when its authors keep presenting it or know the procedures, when a sponsor pays for participants who hold its position, when the chair expects fewer problems from it, when a poll has placed it among the work aimed at the next edition, or when it is already the incumbent. Of two papers otherwise alike, a chair does better taking up first the one whose author has a record of following the procedures and responding to review, and that record comes from taking part. A meeting's hours are fixed, so the time a priority paper gets comes out of the time left for the rest.

Other things equal, a newcomer, someone attending for the first time, spends more effort getting a paper considered than a returning participant, and SD-4 expects everyone to know its procedures. Where a study group incubates proposals, as EWGI and LEWGI do, a newcomer's early proposal can start there. An author who pays their own way bears every meeting's cost alone, and the longer the proposal waits behind priority work, the more meetings that author pays for. Once their cost outweighs its chance of adoption, the author does best letting it stop.

Design for design, a proposal from an author who knows the procedures and keeps presenting advances more readily than one from an author who does not, and work from someone new to the room starts with a lower chance than equally good work from someone who knows the procedures.

- **Rests on:** "Objections that are not so escalated, but are raised or re-raised in plenary, should not be given weight in plenary." (SD-4, "Escalating a serious “cannot live with” objection, or significant new information")
- **What would show this wrong:** papers by first-time participants advancing as readily as otherwise similar papers by returning ones, against the assumption that procedural knowledge comes partly from attending and raises the chance of adoption (`ax:learning`); or, per meeting spent waiting behind priority work, no more stops without a negative poll for self-funded authors' proposals than for sponsored authors' proposals of similar length (`c:pred-small-fade`).
- **Appendix A:** `p:fluency`, `p:late-objection`, `l:settled-convenor`, `l:thm-readily`, `p:chair-confidence`, `p:roadmap-poll`, `p:newcomer`, `l:settled-small-author`, `l:thm-sizes`

## 3. Doubt Stays Out of the Count

**A proposal that costs more to read than most participants' stakes in it is voted on mainly by those with large stakes, and unless the objectors among them cast a third of the votes cast Favor or Against, it can advance with no change at all.**

No participant can study every paper, and close study takes longer the bigger a design is. A bigger design also has more places where a defect can go unnoticed. For a reviewer whose stake, the difference the poll's outcome makes to what they value, does not grow with the design, close study stops being worth its time sooner on a big design than on a small one. Those who skip a paper and its discussion typically do not vote, so those with large stakes cast most of the votes. When the objectors among them are short of a third, the cheapest answer that keeps the 2:1 norm met is no change or a partial change.

A doubt enters the count only as an Against vote, and Against is the costly vote. A regular, a participant who expects to keep meeting many of the same colleagues, cannot rule out that voting Against a colleague's proposal will make that colleague support the regular's own proposals less readily. SD-4 also tells only Against voters to be ready to give reasons, which take time to prepare. Neutral and not voting leave the count unchanged, and no vote costs a regular less than Favor, which risks nothing with the colleague. So on a doubted colleague's proposal, a regular does better voting Against only when the change that vote can make outweighs the standing and time it costs, and one Against vote changes the result only when the count sits one or two votes above the 2:1 threshold. Two regulars with proposals pending, each doubting the other's by less than that cost, each do better refraining whatever the other does. No agreement is needed.

For reviewers whose stakes do not grow with a design, close study stops paying soonest on the designs with the most places for a defect to go unnoticed. A design can then pass unchanged while doubts that no Against vote recorded sit in the room.

- **Rests on:** "Not everyone is interested in every proposal, and participants who are not familiar with the material of a particular poll (did not read the paper and/or were not closely paying attention to the discussion) typically do not vote on that poll." (SD-4, "Subgroup responsibility and polls")
- **What would show this wrong:** across revisions of one proposal polled in one room, no fall in votes cast, relative to other papers polled at the same meetings, as the paper grows longer (`c:pred-abstention-length`); or anonymous design polls drawing no more Against votes on colleagues' proposals (`c:lever-anonymous`).
- **Appendix A:** `p:review-share`, `p:light-review`, `p:least-cost-response`, `p:against-costs-more`, `p:doubt-outside-count`, `p:mutual-support`, `l:settled-regular`, `l:thm-holding`

## 4. No User Votes

**No user votes in any WG21 poll or in the ballots on its drafts, and the needs that reach a vote are the ones participants and their sponsors know, which need not match those of users at large.**

A user, in the proof, is a person who writes C++ and does not take part in WG21. Apart from guests a convenor invites, participants cast the votes in WG21's polls, and national bodies cast the votes on its drafts. A user's interests reach a decision only through what participants themselves value, a paper a participant presents, feedback on a Technical Specification (TS), and national bodies, which form positions only where that is worth their members' time. ISO bars participation fees, and meeting places should not significantly limit attendance. Still, only those who bear the cost of taking part, or whose sponsors do, vote in WG21's polls, and participants can propose only for needs they and their sponsors know. A user can become a participant, but a user without a sponsor then bears the full price alone, while the gain of a better design is spread across every user of the feature and one user's effort seldom changes an outcome.

Authors get the adoption they value at the poll. A flaw that implementation and use have not yet exposed costs them only later and in part, and its cost can fall on any user of the feature. SD-4 calls a TS a separately published "experimental branch" that can ship "to gain experience", and it "asks implementations/users to give feedback to identify shortcomings". A TS also delays adoption into the International Standard (IS) by about one to two years, and its experience can bring incompatible changes first. That is a gain to a result-seeking author, one whose gain depends on how well the adopted design serves users, and a risk to a design-bound author, who does best asking the design room for the IS wherever that can pass. The room can still require a TS or a white paper.

The standard's designs are chosen by people who bear the cost of being in the room, or whose sponsors do, for the needs they and their sponsors know. When a flaw surfaces after adoption, its cost can fall on any user of the feature, and no user voted on it.

- **Rests on:** "National bodies are expected to send experts to participate in person in WG21 if they want to affect the direction of the standard." (SD-4, "Ballots and comments")
- **What would show this wrong:** national bodies stating positions on most proposals rather than few (`c:pred-nb-positions`); or, if a TS stopped delaying adoption compared with an edition, no more designs sent to a TS or white paper (`c:lever-ts-path`).
- **Appendix A:** `p:who-votes`, `p:users-out`, `p:who-takes-part`, `l:settled-user`, `p:reward-timing`, `p:prefer-is`, `l:settled-design-bound`, `l:thm-deciders`

## 5. Whoever Is Present Decides, and Presence Can Be Paid For

**The participants present decide a design's content. Each participant a sponsor pays to attend has a vote and values the sponsor's interests, and no rule limits how many voters one sponsor pays for.**

Chairs call consensus on the votes of those present, counted under the 2:1 norm, in the design rooms and in the study groups that send them proposals. The wording rooms, CWG and LWG, check only that the wording expresses the design, and national bodies vote on each balloted draft as a whole. SC22 may cap the experts each national body or liaison appoints, and at SC22 itself each national body counts once, but no rule caps how many participants one sponsor pays. Each one it pays brings a vote that values its interests, so a sponsor does best paying for participants in the subgroups whose decisions it values, study groups included, while what they bring is worth what it pays.

A study group produces the initial proposal a design room starts from, and its voters are those who chose it over the rooms meeting at the same time. The design room can still poll a rival that has a paper. The fewer Favor and Against votes the other voters cast, the fewer paid participants it takes to cast a third of them, enough to block, or more than two thirds, enough to meet the norm.

Payment also bears on who can hold out in a deadlock. When each of two groups casts at least a third of those votes against the other's design, neither advances. Every meeting of the deadlock costs a group whose sponsors keep paying less than it costs a group paying its own way. In the case the proof works through, with equal stakes, sponsors who value the group's holding above what they pay, and holding costing the sponsored group less than half its stake and the self-funded group more than half, the first does better holding and the second does better yielding, whichever design is better.

The same 2:1 norm decides every proposal, however many users will rely on it. A change to the features a sponsor depends on costs that sponsor rework, lost fit with its requirements, and more review, while the gain of a better design is spread across every user of the feature. The count that decides a design's content depends only on who is present, what the poll asks, and how each person present votes.

- **Rests on:** "In subgroup polls, each person in the room can cast one vote." (SD-4, "Subgroup responsibility and polls")
- **What would show this wrong:** where one sponsor pays a proposal's authors and many of those present, and its interests include adoption, an Against share no smaller than elsewhere; the votes of participants who move to a sponsor whose interests exclude the proposal would tell this apart from shared technical views (`c:pred-sponsor-against`).
- **Appendix A:** `p:who-decides`, `p:sponsor-votes`, `l:settled-sponsor`, `p:sg-decides`, `p:sg-sponsor`, `p:deadlock`, `p:attrition`, `p:sponsor-features`, `l:thm-deciders`

## 6. SD-4 Assigns No One to Rule on Whether a Design Is Good

**SD-4 assigns no one to rule on how good a design is, its consensus test never asks whether an objection is right, and the record the rules require need not show whether an objection was answered or outvoted.**

SD-4 defines consensus as ISO does: general agreement, marked by the absence of sustained opposition to substantial issues by any important part of the concerned interests, and by a process that seeks to take all views into account and reconcile conflicting arguments. An objection prevents consensus that way only if it concerns a substantial issue, is maintained, and comes from an important part of the concerned interests. None of the three conditions asks whether it is right. ISO's general principles say consensus "requires the resolution of substantial objections", yet SD-4 names no step for judging or registering a sustained opposition, and no criteria for an important part of the concerned interests. Its steps for an objection include the 2:1 norm, Against voters' reasons on request, escalation, and plenary's 3-way poll and question about national positions.

A proposal advances on consensus calls, made by chairs under the 2:1 norm in subgroups and by the convenor at plenary, not on every objector's persuasion. In the count, a right objection and a wrong one weigh the same: one Against vote per holder. The room can direct a change, and an author who declines one should defend that with new information, but the count measures votes, not whether the objectors are right. The design that serves users best wins only as far as voters can judge that at the poll and weigh no other value above it. Technical merit enters through what participants value, a good result for users among them, and through what discussion, papers, and implementation experience teach them before they vote.

SD-4 requires minutes but no record of how an objection was answered or why consensus was called over it, and the searched ISO clauses require none for a WG21 poll. From the password-protected records of subgroup discussion, SD-4 allows public quotation only of the poll question, its numbers, and words a person consents to have attributed to them. A proposal's case lasts for decades in its required paper, while an unwritten objection lasts only in the memory of those who heard it. Of minutes, email lists, subgroup records, ballot comments, and papers, only a paper puts an objection's argument outside the protected records without anyone else's help, and writing one takes time.

A design can be adopted over an objection that was right, and from what the rules require the record to hold, a later reader cannot tell an answered objection from an outvoted one. The proposal needs consensus calls, not a persuaded objector.

- **Rests on:** "A proposal normally advances if there are more than twice as many in favor of a proposal as against, after discussion of the concerns of those voting against and possibly a re-poll to see if opinions have improved." (SD-4, "Subgroup responsibility and polls")
- **What would show this wrong:** if some unresolved objections point to real defects, no more defects found after adoption in features forwarded over Against votes than in features forwarded with none, at equal turnout and matched on scope, novelty, prior implementation, and use (`c:pred-defects`); or papers that advance over Against votes routinely answering the objections other published papers raised against them (`c:pred-written-answers`).
- **Appendix A:** `p:who-decides`, `l:consensus-test`, `p:definition-without-procedure`, `p:persuasion-not-required`, `p:least-cost-response`, `p:merit-gap`, `l:thm-merit`, `p:record-indistinct`, `p:reasons-unrecorded`, `p:dissent-needs-paper`

## 7. No Step Checks That Separately Adopted Designs Work Together

**SD-4 names no step in which anyone checks whether designs adopted in separate papers work together, and a conflict between them costs users and later rework.**

Plenary approves each wording paper in its own poll, and during the meeting each paper's wording is written against the drafts adopted at the meeting's start. Change papers approved separately at one meeting first come together when the project editor merges their wording after the meeting. The editor's report summarizes the changes and any comments that arose in merging them, and before a ballot an editing committee verifies that the approved changes were applied correctly, unless the wording rooms already reviewed the whole draft with them applied. Those steps check the text against what was approved. SD-4 encourages merging a TS early to permit better "integration testing" in the full context of the IS, but names no step in which anyone checks one adopted design against another.

Each author gains from their own design's adoption. A design with more parts and more interactions with existing wording has more places where a defect can go unnoticed, and a conflict between two designs may surface only once they are implemented and used. Checking one design against another costs the checker time, while the gain is spread across every user. Integration review worth more to users together than it costs, but less to any one participant, is review no participant does better doing, and in the settled pattern it goes undone.

Two features can each pass every review the rules provide and still conflict once both are in the standard. The conflict may surface only in implementation and use, where it costs users and forces rework of what was built on both.

- **Rests on:** "an editing committee to verify that all approved changes were applied correctly by the project editor before the document is transmitted for ballot" (SD-4, "Working draft handling")
- **What would show this wrong:** a step in SD-4 in which someone checks designs adopted in separate papers against each other; the result rests on a search of SD-4 that found none (`f:no-integration-check`). If closer study finds more defects, the model also predicts fewer defects after adoption on topics whose deciding poll had competing papers from separate author groups than on one-paper topics, and no difference would count against it (`c:pred-competing`).
- **Appendix A:** `p:integration`, `l:separate-approval`, `l:editor-merge`, `l:conflict-costs`, `p:review-shortfall`, `l:thm-gaps`, `f:no-integration-check`

## 8. What No Reviewer Raises, the Author Need Not Say

**The rules ask no author to state a design's drawbacks, and a paper is considered without them. Stating one can cost Favor votes before the poll that decides incumbency, while leaving it out costs no step the rules require before adoption.**

SD-4 never uses the word trade-off. Its list of what a good proposal paper should do includes design principles, motivating examples, and the design alternatives considered, with examples of why they were not pursued. Neither SD-4 nor the quoted ISO clauses ask a paper or its author to state the design's drawbacks, who pays the author's costs, or what interests the author or a sponsor has in the proposal.

What a participant learns from a paper can change their vote. For a trade-off no reviewer would raise, stating it before an early direction poll can cost Favor votes when incumbency is decided, while the gain of a better-informed vote is spread across the design's users. The rules give both kinds of author the same moves. When stating a trade-off would lead the room to change a feature the design-bound author's gain depends on, in a way that serves users better, and the proposal passes either way, the result-seeking author does best stating it and the design-bound author does best leaving it out. No rule makes a paper show which kind of author wrote it. A trade-off left out can still surface in implementation and use and reopen the matter as new information.

The votes that decide incumbency can be cast without a drawback the author knew and no reviewer raised. If it surfaces later, a change won then redoes or discards work already built, and the flaw's cost can fall on any user.

- **Rests on:** "Show design alternatives considered: along with concrete examples showing why they were not pursued." (SD-4, "Proposals and papers", under "A good proposal paper should:")
- **What would show this wrong:** a rule in SD-4 or the quoted ISO clauses that asks a paper or its author to state the design's drawbacks; the result rests on a search of both that found none (`f:no-drawbacks-asked`).
- **Appendix A:** `p:disclosure`, `p:same-moves`, `t:disclose`, `l:settled-design-bound`, `l:settled-result-seeking`, `l:thm-disclosure`, `f:no-drawbacks-asked`, `f:no-interest-statement`

## 9. The Smallest Part That Fixes the Structure Goes First

**A design-bound author does best proposing first the smallest part that fixes the design's structure and can pass. Once that part is adopted, every rival to the structure must replace it and the work built on it.**

A part of a design proposed on its own is a design addition, which needs its own paper, and each part's paper advances on its own consensus calls in the design and wording rooms and at plenary. So a first part can be adopted before the later parts are presented. Its reviewers cannot study in detail what those parts will need of it until they arrive, and only reviewers who foresee the rest can base their vote on that. SD-4 asks no paper that proposes part of a design to state what later parts will require of it, and names no step for reviewing the parts together.

Fixing the structure in the first part fixes it sooner, and every later part that depends on it adds to the cost of the reversal a rival would need. Of two first parts that fix the same features and can pass, the smaller is ready and reviewed sooner. The limit is the opponents who foresee the rest. Blocking the first part takes a third of the votes cast Favor or Against, while removing it once adopted takes more than two thirds, so opponents who together can block do better voting Against it early than seeking its removal later.

Users can inherit a structure adopted before reviewers could study in detail what it must support, and every part built on it adds to what a rival structure would have to replace.

- **Rests on:** "Any significant proposal requires a paper, including every proposal that is a design addition or change." (SD-4, "Proposals and papers")
- **What would show this wrong:** large designs mostly adopted in one paper rather than as sequences of papers building on adopted parts (`c:pred-parts`); or, for design-bound authors, first papers of designs extended part by part routinely setting out their later parts. A first paper that omits any mention of later parts already in existence when it appeared favors the model over the other explanation, that small first steps lower risk (`c:pred-first-part`).
- **Appendix A:** `p:first-part`, `p:parts`, `ind:adopted-parts`, `l:first-part-foresight`, `l:first-part-fix`, `l:first-part-smallest`, `l:first-part-oppose`, `l:thm-first-part`

## Why the Pattern Holds

Appendix A's Theorem gathers the choices behind these findings into one settled pattern, which game theory calls a Nash equilibrium: a set of choices, one for each player, in which no player gains by changing only their own choice. The players are design-bound and result-seeking authors, regulars, study group and design room chairs, the convenor, national bodies, sponsors, and users.

Most of the pattern's choices do best for their player whatever the others choose. A design-bound author seeks early direction polls, the smallest first part, and the IS, each as far as it can pass, leaves out a trade-off no reviewer would raise when stating it costs more than later exposure would, and answers objections with the cheapest change that keeps the design passing. A result-seeking author states trade-offs and makes changes whenever the better design they bring outweighs the votes or work they cost, and backs a rival that serves users better by more than its share of the reversal's cost. An author who values both chooses, at each two-way choice, as the type whose value differs more. A regular votes Favor on colleagues' proposals they support, and Against a doubted one only when the change that vote can make outweighs the standing and time it costs. A sponsor pays for participants where the decisions it values are made, study groups included. Chairs follow the 2:1 norm and poll competing designs side by side, and the convenor follows SD-4's plenary procedure, unless their stake outweighs what departing can cost them. A national body whose comments fare alike under any vote votes Yes with comments unless removing one feature is worth as much to it as the rest of the document, and a user without a sponsor takes part only when their own stakes outweigh a full price borne alone.

Change any one player's choice and that player gains nothing. A regular who votes Against a doubted colleague's proposal when the change that vote can make is worth less than its cost spends standing and time, and one Against vote moves the result only when the count sits one or two votes above the 2:1 threshold. A chair who departs from the 2:1 norm gains at most their stake in the poll and cannot rule out added risk to their post, since chairs serve at the convenor's choice with no fixed term. A design-bound author who states a trade-off no reviewer would raise, when stating it costs more than later exposure would, spends time writing it, can lose Favor votes, and can lead the room to change a feature its gain depends on. A sponsor that stops paying for participants worth their cost to it gives up their votes. A national body that values the rest of a document above removing one feature, and votes No over that feature, opposes every feature in the document at once, while WG21 considers its comments whatever its vote.

The checks are part of the pattern. A third of the votes cast Favor or Against can block, every view must be heard, rivals with papers can be polled side by side, implementation experience informs votes, plenary invites serious design concerns, and national bodies vote on each balloted draft and get answers to their enquiry comments. Every finding above holds with all of them in place.

Stable does not mean unique. With many Favor votes cast, one objector's Against vote changes the result only if enough others vote Against too, so its worth to each objector depends on how the others vote. The same objectors can then settle either way: just enough of them vote Against to block, or none of them does. Both are settled patterns.

Each lever the proof tests is a change to a rule or to what a move costs, and each removes the support for a named result. The last section lists them.

## What This Rests On

> **Assumptions.** The proof starts from these, stated in full as axioms in Appendix A.
>
> - Attending a meeting in person costs money and time. A sponsor can pay a participant's travel and salary but cannot attend, speak, or vote in the participant's place.
> - A participant who attends most meetings expects to meet many of the same colleagues again. A participant who votes Against a colleague's proposal cannot rule out that the colleague will support their own proposals less readily; a Favor vote, or one the colleague cannot attribute, gives no reason for this.
> - Other things equal, each player prefers more of what it values, sooner and cheaper. A participant values adoption of the proposals they support, their sponsor's interests, their standing, any chair or convenor post they hold, their time and money, and a good result for users. A sponsor values its interests, which can depend on particular features of a design.
> - No participant can study every paper closely. Longer and more complex papers take longer to write and review, preparing reasons for a vote takes time, and what a participant learns from a paper or its discussion can change their vote.
> - Until a design is implemented and used, nobody can be sure how well it works. When a proposal is first presented, it has had less review than at any later meeting.
> - Reversing a decision, or changing a design after work is built on it, means redoing or discarding that work, and more is built after each favorable poll.
> - A participant learns how the committee works partly by attending, some of it only that way, and this knowledge differs from skill at design.
>
> **Scope.** These are stated once, here, so that each finding keeps its plain claim.
>
> - "The rules" means SD-4 and the clauses of ISO/IEC Directives Part 1 that the proof quotes, in the edition that replaces the JTC 1 Supplement. A claim that the rules ask for nothing of a kind covers SD-4 whole and those clauses. The proof does not search the other documents SD-4 lists as covering material it does not repeat. It also quotes INCITS's procedures for how the United States forms its national position, and no finding above cites that result.
> - The 2:1 norm is read as a threshold. With Neutral votes short of a majority of those voting, a chair follows the norm by declaring consensus exactly on counts above 2:1 after discussion and any re-poll. Results describe a chair who follows the norm and finds no sustained opposition, and SD-4 names no step or criteria for that finding.
> - Results describe what the rules reward a player who holds the values above, never what anyone actually does or intends.
> - The Theorem has each player make the choices it leaves open, such as whether to study a paper, or the convenor's call where SD-4 leaves it open, in the way that does best for them given the others' choices.
> - SD-4 assigns no one to rule on a design's quality. The direction group gives opinions, which design room participants are strongly encouraged to weigh, but no one rules.
>
> **What the proof does not claim.**
>
> - That anyone acts in bad faith, or holds a motive beyond the values listed above.
> - That any adopted feature is flawed or that any WG21 decision went wrong. It uses no meeting, poll result, or feature history, and names no person and no WG21 paper but SD-4.
> - How often any of this happens, or by how much. The predictions with each finding say what the record should show if the pattern holds, and what would count against it.
> - That the rules lack checks. The blocking third, the hearing of every view, side-by-side polls, implementation experience, and national body ballots are all part of the pattern.

## What Would Change the Pattern

The last chapter of Appendix A works out nine changes, each to a rule or to what a move costs, and what the model predicts each would do. None asks anyone to behave better. Each changes what the rules reward.

- **A written answer to each objection.** If the rules required one in the record, the record would show whether an objection was answered. The model predicts that papers advancing over Against votes would state the objections they faced. (`c:lever-written-answer`)
- **ISO's steps for a sustained opposition.** If SD-4 adopted ISO's steps for assessing, registering, and addressing a sustained opposition, with a recorded answer, the model predicts registered oppositions in WG21's records. (`c:lever-sustained-procedure`)
- **A limit on one sponsor's voters.** If the rules limited how many participants one sponsor pays may vote in a subgroup, the model predicts smaller margins for proposals whose authors one sponsor pays beyond the limit than for proposals with as many authors paid by separate sponsors. (`c:lever-sponsor-limit`)
- **A deadlock procedure.** If the rules set a decision procedure for deadlocks lasting a set number of meetings, the model predicts fewer deadlocks that end when one side stops attending. (`c:lever-deadlock-rule`)
- **A TS without the delay.** If a TS did not delay adoption compared with an edition, the model predicts more designs sent to a TS or white paper. (`c:lever-ts-path`)
- **Anonymous design polls.** The standing part of an Against vote's cost would shrink for voters whom neither their words nor the count identify, and the chair could no longer ask a particular Against voter for reasons. The model predicts more Against votes on colleagues' proposals. (`c:lever-anonymous`)
- **Reasons from every voter.** If SD-4 asked every voter to be ready to give reasons on request, Neutral and Favor would bear the reasons cost Against bears now. The model predicts fewer Neutral votes, fewer Favor votes on doubted proposals, and more participants not voting. (`c:lever-reasons-all`)
- **Cheaper national positions.** If forming national positions during meetings cost less, national bodies would take more. For objections backed by bodies whose No votes could fail a ballot, the model predicts larger changes in answer and slower progress for contested proposals. (`c:lever-nb-more`)
- **Costlier national positions.** If forming them cost more, national bodies would take fewer, and their ballot vote would be their only move counting directly toward stopping a document. The model predicts attendance, paid participants, and early incumbency deciding more content. (`c:lever-nb-less`)

*2026-10-19 21:53 - claude-opus-5.5*
