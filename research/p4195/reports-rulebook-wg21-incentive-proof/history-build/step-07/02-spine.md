## 2. Where decisions are made

1. **Proposition.** A design enters the working draft only after a design room forwards it, a wording room forwards its wording, and plenary approves it. *[from f:design-forward, f:wording-forward, f:plenary-owns, d:rooms]* {#p:path}
1. **Proposition.** In each subgroup, whether a proposal advances depends on the chair's consensus call, and in plenary on the convenor's. *[from f:design-forward, f:wording-forward, f:plenary-owns, d:rooms]* {#p:chair-decides}
1. **Proposition.** Plenary does not redesign, so a design's content is settled in the design rooms and in the study groups whose initial proposals they take up. *[from f:plenary-no-design, f:sg-initial-proposal, p:path]* {#p:design-in-rooms}
1. **Proposition.** In a subgroup poll each person in the room can cast one vote; ISO bars experts not registered to the working group from its work but lets a convenor invite guests; and a user, who by definition does not participate, casts no vote. *[from f:one-vote, f:registered, f:guests, d:participant, d:user]* {#p:who-votes}
1. **Proposition.** No rule gives a sponsor a vote: subgroup votes belong to the people in the room, experts are appointed by national bodies or liaison organizations and act in a personal capacity, and ballots are cast by national bodies. *[from p:who-votes, f:experts-appointed, f:experts-personal, f:iso-ballot, d:sponsor]* {#p:sponsor-no-vote}
1. **Proposition.** The players are authors, regulars, study group chairs, design room chairs, the convenor, national bodies, sponsors, and users. *[from p:path, p:chair-decides, p:who-votes, p:sponsor-no-vote, d:player, d:author, d:regular, d:rooms, d:national-body, d:sponsor, d:user]* {#m:players}

## 3. What each player can do

1. **Proposition.** Each player has these moves under the rules. *[proved by m:moves-author, m:moves-regular, m:moves-chair, m:moves-convenor, m:moves-nb, m:moves-sponsor, m:moves-user]* {#m:moves}
   1. **Lemma.** An author can submit a paper, present it or have another qualified and prepared presenter do so, revise it, add co-authors, build an implementation, propose a ship vehicle, and withdraw the paper. *[from f:no-paper, f:present-required, f:direction-implement, f:vehicle, d:author]* {#m:moves-author}
   1. **Lemma.** A regular can attend or not, study a paper or not, speak, vote Favor, Neutral, or Against or not vote, write a paper, raise a concern privately with a chair, and ask their national body to take a national position. *[from f:one-vote, f:not-vote, f:no-paper, f:private-concern, f:escalate-nb, d:regular]* {#m:moves-regular}
   1. **Lemma.** A chair can choose the polls, order the agenda by SD-4's priorities, time-box a proposal, re-poll after discussion, ask Against voters for reasons, make the consensus call, delay a proposal one meeting for a rival without a paper, allow limited exploration of alternatives, and forward a proposal. *[from f:chair-polls, f:prioritization, f:agenda-papers, f:timebox, f:two-to-one, f:against-reasons, f:no-wait-alternatives, f:explore-alternatives, f:design-forward, f:wording-forward]* {#m:moves-chair}
   1. **Lemma.** The convenor can appoint chairs, form study groups, make plenary consensus calls, and ask whether Against votes in plenary are personal or national body positions. *[from f:chairs-appointed, f:sg-formation, f:plenary-owns, f:plenary-consent, f:plenary-nb]* {#m:moves-convenor}
   1. **Lemma.** A national body can appoint experts, vote on ballots, comment, state a national position in plenary, and appeal. *[from f:experts-appointed, f:iso-ballot, f:all-nbs-vote, f:comments-national, f:plenary-nb, f:appeal]* {#m:moves-nb}
   1. **Lemma.** A sponsor can pay for participation and choose whom it pays and how many. *[from d:sponsor, ax:who-pays, f:no-sponsor-cap]* {#m:moves-sponsor}
   1. **Lemma.** A user has no move in WG21's rules except becoming a participant. *[from p:who-votes, d:user]* {#m:moves-user}

## 4. The price of a vote

1. **Lemma.** Under the 2:1 norm, each Against vote raises by two the number of Favor votes a proposal needs. *[from f:two-to-one, d:positions]* {#l:against-double}
1. **Lemma.** Neutral votes and abstentions do not enter the 2:1 comparison, though SD-4 says a Neutral majority can be concerning. *[from f:two-to-one, f:not-vote, d:positions]* {#l:neutral-outside}
1. **Lemma.** SD-4 names Against voters as the voters a chair may ask for reasons, and names no such step for any other position. *[from f:against-reasons, f:not-vote]* {#l:reasons-against}
1. **Proposition.** For a regular, voting Against a colleague's proposal costs more than voting Neutral or not voting. *[from l:reasons-against, f:against-reasons, ax:support, ax:repeat, ax:prefer, d:regular, d:standing]* {#p:against-costs-more}
1. **Proposition.** A regular does better voting Against than voting Neutral only when their stake in the outcome exceeds the added cost of voting Against. *[from ax:prefer, p:against-costs-more, d:stake, d:does-better]* {#p:stake-threshold}
1. **Proposition.** A regular who doubts a proposal, and whose stake is below that added cost, does better voting Neutral or not voting, so the doubt does not enter the 2:1 comparison. *[from p:stake-threshold, l:neutral-outside]* {#p:doubt-outside-count}
1. **Lemma.** One more Against vote changes whether the 2:1 norm is met only when the Favor votes exceed twice the other Against votes by one or two, while its cost to the voter does not depend on the count. *[from f:two-to-one, d:positions, p:against-costs-more]* {#l:room-size}
1. **Proposition.** A participant can state a preference for another design and vote Neutral, which leaves the 2:1 count unchanged and is not a position SD-4 names for questions. *[from l:against-double, l:neutral-outside, l:reasons-against]* {#p:prefer-vs-stop}
1. **Lemma.** Any group casting at least one third of the Favor-plus-Against votes as Against prevents the 2:1 norm from being met. *[from f:two-to-one, d:positions]* {#l:organized-minority}

*Table: One regular's vote on a colleague's proposal. Columns: the regular's stake. Each cell: the regular's rank of the vote. 3 is best.* {#t:vote-choice}

| | Low stake | High stake |
|---|---|---|
| **Favor** | | |
| **Neutral** | | |
| **Against** | | |

*[from p:against-costs-more, p:stake-threshold, p:doubt-outside-count]*

1. **Proposition.** Two regulars with pending proposals each do better not opposing the other's proposal than opposing it, unless that proposal lowers what the regular values by more than the cost of opposing. *[from ax:support, ax:prefer, p:against-costs-more, d:does-better]* {#p:mutual-support}

*Table: Two regulars, each with a proposal pending. First number: A's rank. Second number: B's rank. 4 is best.* {#t:mutual-support}

| | B supports | B opposes |
|---|---|---|
| **A supports** | | |
| **A opposes** | | |

*[from p:mutual-support]*

## 5. What the record keeps

1. **Lemma.** SD-4 requires minutes and permits public quotation of poll questions and numeric results, nothing in it requires the record to show how an objection was answered, and at plenary a subgroup chair may be asked to summarize the reason for the subgroup's decision. *[from f:minutes, f:protected, f:no-reason-record, f:plenary-reason]* {#l:record-content}
1. **Lemma.** ISO lets participants comment on or object to minutes before they are confirmed, has the chair of SC22 see that points of view at SC22's meetings are summarized, and bars participants from commenting publicly on others' contributions. *[from f:minutes-objections, f:views-summarized, f:no-public-comment]* {#l:record-checks}
1. **Lemma.** ISO's recommended approach has the committee leadership, which for WG21's work is the chair of SC22, register an opposition that may first have been voiced at a working group meeting, and SD-4 adds no such step for subgroup polls. *[from f:iso-register, f:sustained-def, f:chair-judges, f:leadership-judges, f:no-sustained-procedure]* {#l:iso-register-level}
1. **Proposition.** SD-4 adopts ISO's definition of consensus, which turns on sustained opposition, for a working group that ISO says operates by consensus. Its own steps for opposition are the 2:1 norm after discussion, the chair's option to ask Against voters for reasons, and escalation, and it states neither ISO's step of assessing whether an opposition is sustained, nor criteria for an important part of the concerned interests, nor a step for registering an opposition. *[from f:wg-consensus, f:consensus-def, f:two-to-one, f:against-reasons, f:escalate-deadline, f:iso-register, f:no-sustained-procedure]* {#p:definition-without-procedure}
1. **Lemma.** Under the definition SD-4 adopts, an objection prevents consensus only if it concerns a substantial issue, is maintained, and comes from an important part of the concerned interests as the leadership judges case by case, so the test turns on an objection's backing rather than its merit, while the definition and SD-4 still require every view to be heard. *[from f:consensus-def, f:sustained-def, f:concerned-interests, f:majority-listen, f:views-heard]* {#l:backing-filter}
1. **Proposition.** The rules let a proposal advance once enough participants stop voting Against, whether or not they were persuaded. *[proved by l:address-not-resolve, p:advance-unanswered]* {#p:persuasion-not-required}
   1. **Lemma.** Under ISO, the obligation to address a sustained opposition is not an obligation to resolve it, and a sustained opposition is not a veto, though ISO's general principles say consensus requires the resolution of substantial objections. *[from f:not-veto, f:resolve-substantial]* {#l:address-not-resolve}
   1. **Proposition.** A proposal can advance while discussed objections to it remain unresolved, because advancing requires a consensus call, which the 2:1 norm normally supports, and consensus need not imply unanimity. *[from l:address-not-resolve, f:design-forward, f:two-to-one, f:consensus-def]* {#p:advance-unanswered}
1. **Proposition.** When an objection's Against votes are too few to prevent the 2:1 norm from being met, the least costly response that keeps the norm met is a change confined to part of the design, or no change. *[from ax:prefer, ax:redesign-cost, l:organized-minority]* {#p:least-cost-response}
1. **Proposition.** SD-4 asks an Against voter to name the changes that would address the concern; concerns stated as changes can each be granted, while an objection to the proposal in any form names no change that would address it. *[from f:against-reasons]* {#p:change-list}
1. **Proposition.** The record the rules require of a WG21 poll need not show whether an objection was answered or outvoted. *[from l:record-content, l:iso-register-level, l:record-checks]* {#p:record-indistinct}
1. **Proposition.** Minutes need not hold an objection's reasons and a ballot comment counts only as a national body position, so a paper is the only record of an objection's argument that its holder can produce alone, and writing it takes time. *[from l:record-content, f:comments-national, f:escalate-paper, ax:review-cost]* {#p:dissent-needs-paper}
1. **Proposition.** Reasons that no written record holds become unavailable to the committee once every participant who heard them has stopped attending. *[from ax:turnover, l:record-content]* {#p:reasons-fade}
1. **Proposition.** A participant who repeats an objection after a consensus call, without new information and outside judicious escalation, can be described in SD-4's own terms as not accepting a group decision, whether or not the objection was answered. *[from f:minority-accept, f:accept-decisions, f:escalation-allowed, f:ballot-decided, f:ballot-new-info]* {#p:repeat-objection}
1. **Proposition.** SD-4 gives no weight at plenary to an objection not escalated by the deadline, even one that brings new information, and sends such information to the email lists or to a national body comment with a discussion paper. *[from f:plenary-weight, f:escalate-deadline, f:late-info, f:escalate-paper]* {#p:late-objection}

## 6. Proposal size

1. **Proposition.** A participant keeps attending in person only while their own value from attending exceeds the costs that fall on them, which are lower when a sponsor pays, though ISO asks that remote participation be offered where possible and bars participation fees. *[from ax:cost, ax:who-pays, ax:prefer, f:iso-cost, f:remote, f:no-fee, f:in-person-expected]* {#p:money-vs-presence}
1. **Proposition.** After a design passes a direction poll in a design room, a rival without a paper does not block it, though the chair may delay it one meeting so an objector can bring one. SD-4 asks the design's author to implement the room's direction, a rival with a paper can be polled alongside it, and at a TS merge the default is to proceed with the design if no alternative is actively progressing. *[from f:no-paper, f:no-wait-alternatives, f:explore-alternatives, f:direction-implement, f:multiple-polls, f:ts-default, d:incumbent]* {#p:incumbent-start}
1. **Induction.** Each later decision built on a design adds to the work a reversal would redo or discard, so the cost of reversing the design does not fall as the design advances. *[from ax:rework, ax:prefer, d:reversal]* {#ind:reversal-grows}
1. **Proposition.** In a poll between a rival design and an incumbent, a voter favors the rival only when the voter values the rival's advantage above the part of the reversal's cost that falls on what the voter values. *[from ax:prefer, ind:reversal-grows, p:incumbent-start, d:incumbent]* {#p:challenger-bar}
1. **Proposition.** An author does better when favorable direction polls come early, while the design has had the least review, because each one makes the design an incumbent that later discussion starts from. *[from ax:prefer, ax:first-review, p:incumbent-start, ind:reversal-grows, d:direction-poll, d:does-better]* {#p:early-polls}
1. **Lemma.** A chair may take any poll, and a direction poll asks voters to accept less than a forwarding poll does. *[from f:chair-polls, d:direction-poll, d:forwarding-poll]* {#l:poll-wording}
1. **Induction.** SD-4 has chairs take up first the direction group's priorities, work the committee is aiming to include in the next IS, and work that can make plenary progress at this meeting. A proposal that advances at one meeting is closer to plenary at the next, so its priority does not fall as it advances. *[from f:prioritization, f:direction-group, ax:hours]* {#ind:priority-compounds}
1. **Proposition.** A sponsor that pays for more participants to attend a room adds to the votes available to the positions those participants hold. At SC22, by contrast, each national body counts once, every expert is appointed by a national body or a liaison organization, and the committee may cap the experts each one appoints. *[from f:no-sponsor-cap, f:one-vote, ax:who-pays, f:pmember-consensus, f:experts-appointed, f:expert-cap]* {#p:sponsor-votes}
1. **Proposition.** When a reviewer's stake does not grow with a proposal's length or complexity, a longer or more complex proposal gets a smaller share of that reviewer's close study. *[from ax:review-cost, ax:attention, ax:prefer, d:stake]* {#p:review-share}
1. **Lemma.** SD-4 describes the presenter as an expert in the paper's domain who educates general C++ experts, and directs concerns about a proposal to its authors. *[from f:presenter, f:concern-authors]* {#l:author-knows-more}
1. **Proposition.** An author's gain from adoption arrives at adoption, while the cost of a design flaw arrives after implementation and use and falls on every user of the feature. *[from ax:unknown, ax:users-affected, d:author]* {#p:reward-timing}
1. **Induction.** A large proposal adopted in parts makes each later part a step from the parts already adopted, so a rival must be compared with all of them. *[from p:incumbent-start, ind:reversal-grows, d:large]* {#ind:slices}
1. **Proposition.** Compared with a small proposal, a large proposal has more authors attending for it with their costs paid, more meetings in which to win polls, and more work built on each poll it wins. *[from d:large, d:small, p:sponsor-votes, ind:priority-compounds, ind:reversal-grows]* {#p:large-position}
1. **Lemma.** Implementation and use reduce uncertainty about a design, and SD-4 publishes a TS to gain that experience, though it tells users of a TS not to rely on it in production code. *[from ax:unknown, f:ts-experience, f:ts-feedback]* {#l:implementation-informs}
1. **Proposition.** The author of a small proposal pays their own costs. Unless the proposal falls in one of SD-4's priority categories it gets agenda time only after the priority work, and like every proposal it needs an on-time paper and a qualified, prepared presenter. *[from d:small, f:prioritization, f:agenda-papers, f:late-paper, f:present-required, f:invested]* {#p:small-position}
1. **Proposition.** A newcomer has had none of the learning that earlier meetings provide, though SD-4 expects every participant to be familiar with its procedures. *[from ax:learning, d:newcomer, f:familiar]* {#p:newcomer}

## 7. Study groups

1. **Lemma.** A participant chooses a study group's session over concurrent sessions when its topic matters more to them, so a study group's room holds the participants who made that choice. *[from ax:parallel-rooms, ax:prefer]* {#l:sg-attendance}
1. **Proposition.** A contest between competing designs is first settled in the study group, among the participants who chose its sessions, and its output enters the design room as the initial proposal the room starts from. *[proved by l:sg-purpose, l:sg-start]* {#p:sg-decides}
   1. **Lemma.** SD-4 has the convenor form a study group when a topic draws broad interest, has no unified initial proposal, and has a strong candidate to chair the group, and the study group produces the initial proposal that enters the design room. *[from f:sg-formation, f:sg-initial-proposal]* {#l:sg-purpose}
   1. **Lemma.** The design room starts from the study group's initial proposal, which a rival without a paper does not block, and the study group's room holds the participants who chose its sessions. *[from l:sg-purpose, l:sg-attendance, p:incumbent-start, f:sg-initial-proposal]* {#l:sg-start}
1. **Proposition.** When each of two groups casts at least one third of the Favor-plus-Against votes against the other's design, neither design meets the 2:1 norm, and the deadlock ends only if voters change position, a design changes until enough Against voters accept it, or the voters present change. *[from l:organized-minority]* {#p:deadlock}
1. **Proposition.** A design changed to end a deadlock either adds elements its Against voters want or removes elements they oppose. *[from p:deadlock]* {#p:design-changes}
1. **Proposition.** In a deadlock lasting many meetings, members of a group whose costs sponsors pay bear less personal cost per meeting than members of a group paying their own way. *[from ax:who-pays, ax:cost, p:deadlock]* {#p:attrition}
1. **Proposition.** SD-4 ties a study group's purpose to producing a unified initial proposal, and a deadlock produces none. *[from f:sg-formation, p:deadlock]* {#p:sg-unified}
1. **Proposition.** A concern held in one room enters another room's decision only if a person present in that room raises it. *[from ax:parallel-rooms, p:who-votes]* {#p:concern-presence}

*Table: Two groups in a deadlock, each paying a different cost per meeting. First number: group A's rank. Second number: group B's rank. 4 is best.* {#t:hold-or-yield}

| | B holds | B yields |
|---|---|---|
| **A holds** | | |
| **A yields** | | |

*[from p:deadlock, p:design-changes, p:attrition]*

## 8. Chairs and the convenor

1. **Lemma.** Subgroup chairs are appointed by the convenor with no fixed term, and the convenor is appointed by SC22 for terms of up to three years, renewable without limit after a call for candidates. *[from f:chairs-appointed, f:convenor-term]* {#l:appointments}
1. **Lemma.** SD-4 makes the subgroup chair the judge of consensus and assigns no one in WG21 the role of ruling which side of a technical dispute is correct. *[from f:design-forward, f:no-merit-ruling]* {#l:chair-role}
1. **Proposition.** A chair who declares consensus while some participants vote Against risks national body opposition later, and a chair who declines delays work that SD-4 says subgroup polls should favor. *[from f:favor-progress, f:plenary-nb, f:iso-ballot, f:escalate-nb, l:appointments, ax:prefer]* {#p:chair-costs}
1. **Proposition.** When more than twice as many vote Favor as Against, declaring consensus follows SD-4's norm and declining departs from it, though SD-4 says a Neutral majority can be concerning. *[from f:two-to-one, f:favor-progress, l:neutral-outside]* {#p:chair-default}
1. **Proposition.** When Favor votes are not more than twice the Against votes, SD-4 allows a re-poll after discussion of the Against voters' concerns, and only Against voters are named for questions in that discussion. *[from f:two-to-one, l:reasons-against]* {#p:repoll}
1. **Proposition.** No rule requires the record to say why a chair declared consensus while some participants voted Against, though plenary may ask the subgroup chair to summarize the reason, and recording reasons takes meeting time. *[from l:record-content, f:iso-no-reason-record, f:plenary-reason, ax:hours]* {#p:chair-no-reasons}
1. **Proposition.** SD-4 asks a participant who thinks a new proposal should not take up extended subgroup time to tell the chair privately and in advance, the chair may then time-box it after a representative overview, and no rule requires a record of the request. *[from f:private-concern, f:timebox, f:no-concern-record]* {#p:private-channel}
1. **Proposition.** Plenary does not redesign, gives no weight to an objection not escalated in time, solicits serious design concerns about designs approved at that meeting, and, when opposition is significant, has the convenor ask whether the Against votes are personal or national body positions. *[from p:design-in-rooms, f:plenary-no-design, f:plenary-weight, f:design-concerns-solicited, f:plenary-consent, f:plenary-nb]* {#p:plenary-ratifies}
1. **Proposition.** A wording room refers design questions back to the design room, so it can delay a design but cannot change it. *[from f:wording-refer, f:wording-forward]* {#p:wording-rooms}

*Table: A chair's consensus call. Columns: the count. Each cell: the chair's rank of the call. 2 is best within each column.* {#t:chair-call}

| | Above 2:1 | Not above 2:1 |
|---|---|---|
| **Declare consensus** | | |
| **Decline** | | |

*[from p:chair-costs, p:chair-default, p:repoll]*

## 9. The release schedule

1. **Proposition.** A proposal not approved before an edition's feature cutoff waits at least for a later edition, which WG21 plans three years after the one it missed. *[proved by l:cutoff]* {#p:miss-cost}
   1. **Lemma.** Once an edition's draft goes to ballot, a ballot comment cannot add a feature to it, and WG21 plans the next edition three years later. *[from f:ballot-no-new-features, d:feature-cutoff, d:edition, ax:schedule]* {#l:cutoff}
1. **Proposition.** If SD-4's one-meeting delay for a rival without a paper falls on the last meeting before the feature cutoff, the delayed proposal misses the edition. *[from f:no-wait-alternatives, p:miss-cost]* {#p:one-meeting-cycle}
1. **Proposition.** At the last meeting before the feature cutoff, an Against vote that stops a proposal delays it to a later planned edition. *[from p:miss-cost, l:against-double]* {#p:cutoff-effect}
1. **Proposition.** A TS delays an author's adoption by about one to two years, so an author prefers the IS unless the author values the TS's experience for users above that delay or the design room requires a TS. SD-4 now recommends the lighter white paper, which has no prescribed schedule. *[from f:ts-lag, ax:prefer, f:vehicle, f:ts-experience, f:white-paper, f:white-paper-process]* {#p:prefer-is}

*Table: The authors of a large proposal. Columns: the design room's choice of vehicle. Each cell: the authors' rank. 2 is best within each column.* {#t:push-or-ts}

| | Room forwards | Room requires TS |
|---|---|---|
| **Push for IS** | | |
| **Accept a TS** | | |

*[from p:prefer-is, p:large-position, ind:slices]*

1. **Proposition.** At ballot, a national body votes on the whole document, SD-4 asks that No mean the body does not want the work at all, and ISO forbids a Yes that is conditional on changes, so a national body cannot vote against one feature without voting against the whole document. *[from f:ballot-no, f:no-means-no, f:iso-ballot, f:no-conditional-yes]* {#p:bundling}
1. **Proposition.** Before adoption, a proposal needs the 2:1 norm to advance; after adoption, removing it needs a paper that meets the 2:1 norm; after a successful final ballot, a design change is expected to have near-unanimous consent, and no technical change is accepted at the approval stage; once published, SD-4 says the feature is much more difficult to update with breaking changes. *[from f:two-to-one, f:no-paper, f:near-unanimous, f:late-changes, f:is-hard-to-change]* {#p:burden-flip}
1. **Proposition.** Because WG21 plans each edition for a set time, an unfinished feature need not delay the features that are ready. *[from ax:schedule]* {#p:schedule-protects}

## 10. National bodies

1. **Lemma.** At enquiry and final ballots every national body may vote, abstentions are excluded from the count, a negative vote must give technical reasons, ISO encourages a body without national consensus or expert input to abstain, and the concept of sustained opposition does not apply to these votes. A draft that fails the final ballot goes back to the committee for reconsideration rather than ending the work. *[from f:all-nbs-vote, f:iso-ballot, f:no-conditional-yes, f:nb-abstain, f:not-ballots, f:failed-fdis]* {#l:ballot-rules}
1. **Lemma.** A No vote on a document opposes every feature in it, including features the body's own experts support. *[from p:bundling]* {#l:nb-no-scope}
1. **Proposition.** A national body that supports most of a document does better voting Yes with comments than voting No over one feature, since WG21 considers all national body feedback whatever the vote and ISO requires a response to every comment. *[from l:nb-no-scope, ax:prefer, f:no-means-no, f:respond-comments, f:comment-report, d:does-better]* {#p:nb-comment}
1. **Lemma.** SD-4 treats as out of scope a comment that adds a feature, and as out of harmony a comment that repeats a change already decided at a meeting the body attended, unless new information has arisen or the body told the committee all along that it would vote No. *[from f:ballot-no-new-features, f:ballot-decided, f:ballot-new-info, f:no-surprise]* {#l:nb-comment-limits}
1. **Proposition.** An objection has weight in plenary only if escalated in time on the email lists and within its holder's national body, where SD-4's default is that it is not a national position; after the deadline it can count only through the email lists or a national body ballot comment. *[from f:plenary-weight, f:escalate-deadline, f:escalate-nb, f:late-info]* {#p:nb-route}
1. **Proposition.** A national body decides its position by its members under its own rules, so the members a sponsor pays take part in deciding that position. *[from f:escalate-nb, f:late-info, ax:who-pays]* {#p:nb-members}
1. **Proposition.** SD-4 and ISO both ask national bodies to make objections known early. *[from f:timely, f:no-surprise, f:iso-early]* {#p:nb-early}
1. **Proposition.** A national body may appeal within eight weeks, an appeal on a draft is eligible only on questions of principle or harm to the reputation of ISO or IEC, and work continues during an appeal up to and including the approval stage. *[from f:appeal, f:appeal-pmember, f:appeal-technical, f:appeal-continues, f:sustained-appeal]* {#p:appeal-continues}

*Table: A national body's ballot vote. Columns: how much of the document it supports. Each cell: its rank of the vote. 2 is best within each column.* {#t:nb-ballot}

| | Most of it | Little of it |
|---|---|---|
| **Yes with comments** | | |
| **No** | | |

*[from p:nb-comment, l:nb-no-scope, p:bundling]*

## 11. The settled pattern

1. **Lemma.** Given the other players' choices in the pattern, a regular does no better than to vote Favor, Neutral, or not at all on a colleague's proposal, and to vote Against only when their stake exceeds the added cost of doing so. *[from p:stake-threshold, p:doubt-outside-count, p:prefer-vs-stop, l:room-size, p:mutual-support, p:repeat-objection, m:moves, d:settled-pattern]* {#l:settled-regular}
1. **Lemma.** Given the other players' choices, the authors of a large proposal do no better than to seek favorable direction polls early, adopt the work in parts, prefer the IS to a TS unless the TS's experience is worth its delay to them, and answer objections with the least costly change that keeps the 2:1 norm met, unless they value the users' gain from a larger change above its cost. *[from p:early-polls, p:incumbent-start, p:challenger-bar, ind:slices, p:large-position, p:prefer-is, p:least-cost-response, p:persuasion-not-required, p:change-list, l:author-knows-more, p:reward-timing, m:moves, d:settled-pattern]* {#l:settled-large-author}
1. **Lemma.** Given the other players' choices, the author of a small proposal does no better than to keep attending and presenting while their own value from the proposal exceeds the costs that fall on them, and to stop pursuing it when it does not. *[from p:small-position, p:money-vs-presence, p:newcomer, p:least-cost-response, m:moves, d:settled-pattern]* {#l:settled-small-author}
1. **Lemma.** Given the other players' choices, a study group chair does no better than to poll the competing designs on the topic and forward the one that meets the 2:1 norm, and, when none does, to keep the contest open until voters, designs, or attendance change. *[from p:sg-decides, p:deadlock, p:design-changes, p:attrition, p:sg-unified, p:concern-presence, p:chair-default, m:moves, d:settled-pattern]* {#l:settled-sg-chair}
1. **Lemma.** Given the other players' choices, a design room chair does no better than to declare consensus when Favor votes are more than twice the Against votes, to re-poll or decline when they are not, and to record the count and the outcome. *[from p:chair-default, p:repoll, p:chair-costs, p:chair-no-reasons, l:chair-role, p:private-channel, l:poll-wording, p:one-meeting-cycle, m:moves, d:settled-pattern]* {#l:settled-design-chair}
1. **Lemma.** Given the other players' choices, the convenor does no better than to declare plenary consensus on what the subgroups forward unless significant opposition holds national body positions. *[from p:plenary-ratifies, p:nb-route, p:wording-rooms, l:appointments, p:chair-costs, m:moves, d:settled-pattern]* {#l:settled-convenor}
1. **Lemma.** Given the other players' choices, a national body does no better than to vote Yes with comments on documents it mostly supports, to vote No only on documents it supports little of, and to raise its objections early. *[from p:nb-comment, l:nb-no-scope, l:nb-comment-limits, p:nb-early, l:ballot-rules, p:bundling, p:nb-members, m:moves, d:settled-pattern]* {#l:settled-nb}
1. **Lemma.** Given the other players' choices, a sponsor does no better than to pay for participation where the decisions it values are made, as long as their value to it exceeds the cost. *[from p:sponsor-votes, p:money-vs-presence, p:large-position, p:nb-members, m:moves, d:settled-pattern]* {#l:settled-sponsor}
1. **Lemma.** Given the other players' choices, a user does no better than to stay out of WG21 unless the user's stake in a decision exceeds the costs of becoming a participant. *[from p:who-votes, m:moves, p:money-vs-presence, p:reward-timing, d:settled-pattern]* {#l:settled-user}
1. **Proposition.** The rules also limit these effects: every view must be heard, conduct rules ask for respect and good faith and bar collusion, a group casting a third of the votes can block, alternatives can be explored, polled side by side, and must be shown in papers, implementation experience informs voters, national bodies ballot each draft and get a written answer to every comment, minutes can be challenged, and appeals are open. ISO also says consensus requires resolving substantial objections, and SD-4 works in addition to the Directives. *[from f:views-heard, f:majority-listen, f:respect-opinions, f:negative-welcome, f:good-faith, f:conduct-report, f:no-collusion, l:organized-minority, f:explore-alternatives, f:multiple-polls, f:show-alternatives, f:followup-papers, f:competing-ts, f:pre-merge, l:implementation-informs, l:ballot-rules, f:comment-report, f:respond-comments, l:record-checks, p:appeal-continues, f:design-concerns-solicited, p:schedule-protects, f:resolve-substantial, f:sd4-scope]* {#p:checks}
1. **Theorem.** Under SD-4 and the ISO/IEC Directives as written, and given the axioms, the following choices form a settled pattern, in which no player improves their position by changing only their own choice. Regulars vote Favor, Neutral, or not at all on colleagues' proposals and vote Against when their stake exceeds the added cost; authors seek favorable direction polls early and answer objections with the least costly change that keeps the 2:1 norm met, and the authors of large proposals adopt their work in parts and prefer the IS to a TS; sponsors pay for participation where the decisions they value are made; chairs declare consensus when Favor votes are more than twice the Against votes and record the count and the outcome; study groups settle contests between designs before the design rooms see them, and a contest that stays even ends when voters change position, a design changes, or one side stops attending; national bodies vote Yes with comments on documents they mostly support and raise objections early; and users stay out unless their stake exceeds the cost of taking part.

   In this pattern, a proposal's progress depends on the participants who attend for it and on the polls it has already won, the record need not show whether its objections were answered, and the checks in the rules limit each of these effects. *[from l:settled-regular, l:settled-large-author, l:settled-small-author, l:settled-sg-chair, l:settled-design-chair, l:settled-convenor, l:settled-nb, l:settled-sponsor, l:settled-user, p:checks, p:record-indistinct, p:reasons-fade, p:definition-without-procedure, l:backing-filter, d:settled-pattern]* {#thm:settled}

## 12. Corollaries

1. **Corollary.** If the settled pattern holds, the public record should show the following, and each prediction names what would count against it. *[proved by c:pred-sponsor-against, c:pred-neutral-length, c:pred-cutoff-margins, c:pred-slices, c:pred-removals, c:pred-sg-margins, c:pred-small-fade, c:pred-disclosure, c:pred-framing, c:pred-repeat-papers, c:pred-rebuttal-timing, c:pred-repair-authors, c:pred-rival-persistence, c:pred-nb-positions, c:pred-written-answers]* {#c:predictions}
   1. **Corollary.** Against votes are fewer, relative to Favor votes, on proposals whose author lists name more participants paid by one sponsor; poll results and author lists are the evidence, and as many Against votes on such proposals as on others would count against it. *[from p:sponsor-votes, p:mutual-support, thm:settled]* {#c:pred-sponsor-against}
   1. **Corollary.** The Neutral share of a poll rises with the length of the paper polled; poll results and paper lengths are the evidence, and no such rise would count against it. *[from p:review-share, p:doubt-outside-count, thm:settled]* {#c:pred-neutral-length}
   1. **Corollary.** Favor margins in design rooms are wider at the last meeting before a feature cutoff than at other meetings; poll results by meeting are the evidence, and no widening would count against it. *[from p:cutoff-effect, p:stake-threshold, thm:settled]* {#c:pred-cutoff-margins}
   1. **Corollary.** Large proposals appear as sequences of papers, each building on parts already adopted; the mailings are the evidence, and large designs adopted in one paper would count against it. *[from ind:slices, p:large-position, thm:settled]* {#c:pred-slices}
   1. **Corollary.** Removals after adoption are rare and arrive with national body comments or with a group casting at least one third of the votes; working drafts and poll results are the evidence, and frequent removals by narrow margins would count against it. *[from p:burden-flip, l:organized-minority, p:nb-comment, thm:settled]* {#c:pred-removals}
   1. **Corollary.** Study group polls on a design show wider Favor margins than the design room's later polls on the same design; poll results are the evidence, and narrower study group margins would count against it. *[from p:sg-decides, l:sg-attendance, thm:settled]* {#c:pred-sg-margins}
   1. **Corollary.** Small proposals stop advancing more often without a negative poll than after one; the mailings and poll results are the evidence, and small proposals that stop mostly after negative polls would count against it. *[from p:small-position, l:settled-small-author, thm:settled]* {#c:pred-small-fade}
   1. **Corollary.** Early revisions of proposal papers show fewer design alternatives than later revisions; successive public revisions are the evidence, and early revisions as complete as later ones would count against it. *[from p:early-polls, f:show-alternatives, thm:settled]* {#c:pred-disclosure}
   1. **Corollary.** Papers that start a large design describe their first part as small and self-contained more often than papers for later parts do; the mailings are the evidence, and no such difference would count against it. *[from ind:slices, thm:settled]* {#c:pred-framing}
   1. **Corollary.** Participants who lose a poll return with further papers on the same objection; repeat papers and poll results are the evidence, and objections that end with the poll would count against it. *[from p:record-indistinct, p:dissent-needs-paper, thm:settled]* {#c:pred-repeat-papers}
   1. **Corollary.** Rebuttal papers appear more often at the meeting where the paper they answer is presented than before it; mailing dates are the evidence, and rebuttals spread evenly across meetings would count against it. *[from f:followup-papers, p:late-objection, thm:settled]* {#c:pred-rebuttal-timing}
   1. **Corollary.** Papers that fix an adopted design name authors with longer attendance than papers that propose new designs; author lists are the evidence, and no such difference would count against it. *[from p:burden-flip, d:standing, thm:settled]* {#c:pred-repair-authors}
   1. **Corollary.** Rival designs continue as papers after losing polls more often when their authors have already written several revisions; rival papers across meetings are the evidence, and no such relation would count against it. *[from ind:reversal-grows, thm:settled]* {#c:pred-rival-persistence}
   1. **Corollary.** National bodies form positions on few proposals; national body comments and plenary records of national positions are the evidence, and positions on most proposals would count against it. *[from p:nb-route, l:ballot-rules, thm:settled]* {#c:pred-nb-positions}
   1. **Corollary.** Papers that advance over Against votes rarely state the objections they faced; the papers and poll results are the evidence, and papers that routinely state and answer their objections would count against it. *[from p:record-indistinct, p:least-cost-response, thm:settled]* {#c:pred-written-answers}
1. **Corollary.** Each rule change below would remove the support for a named item, and the model predicts the stated effect. *[proved by c:lever-anonymous, c:lever-reasons-all, c:lever-sponsor-limit, c:lever-written-answer, c:lever-deadlock-rule, c:lever-ts-path, c:lever-sustained-procedure]* {#c:levers}
   1. **Corollary.** If design polls were anonymous, a colleague could not tell who voted Against, the standing part of the cost of voting Against would disappear, and the model predicts more Against votes on colleagues' proposals. *[from p:against-costs-more, ax:support, thm:settled]* {#c:lever-anonymous}
   1. **Corollary.** If a chair asked voters of every position for reasons, the extra cost of voting Against would shrink, and the model predicts more Against votes and fewer Neutral ones. *[from l:reasons-against, p:against-costs-more, thm:settled]* {#c:lever-reasons-all}
   1. **Corollary.** If the rules limited how many participants one sponsor may send to a room, the votes a sponsor can add would be capped, and the model predicts smaller differences in poll margins between large and small proposals. *[from p:sponsor-votes, p:large-position, thm:settled]* {#c:lever-sponsor-limit}
   1. **Corollary.** If the rules required a written answer to each objection in the record, the record would show whether an objection was answered, and the model predicts fewer repeated objections and fewer objection papers. *[from p:record-indistinct, p:dissent-needs-paper, thm:settled]* {#c:lever-written-answer}
   1. **Corollary.** If the rules set a decision procedure for deadlocks lasting a set number of meetings, attrition would no longer decide them, and the model predicts shorter deadlocks and fewer that end when one side stops attending. *[from p:attrition, p:deadlock, thm:settled]* {#c:lever-deadlock-rule}
   1. **Corollary.** If a TS did not delay adoption compared with an edition, the author's cost of accepting a TS would fall, and the model predicts more designs sent to a TS or white paper. *[from p:prefer-is, thm:settled]* {#c:lever-ts-path}
   1. **Corollary.** If SD-4 adopted ISO's steps for assessing, registering, and addressing a sustained opposition, with a recorded answer, the gap between the definition and the procedure would close, and the model predicts registered oppositions in WG21's records and fewer objections raised again at plenary. *[from p:definition-without-procedure, p:record-indistinct, thm:settled]* {#c:lever-sustained-procedure}
