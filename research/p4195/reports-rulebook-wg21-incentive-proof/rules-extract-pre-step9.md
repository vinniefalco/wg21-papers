---
produced: 2026-10-18
title: SD-4 and ISO/IEC Directives Part 1 (2026) rule text for the WG21 incentive proof
---

## SD-4: WG21 Practices and Procedures

```
Doc No: ISO/IEC JTC1/SC22/WG21/SD-4
Date: 2026-05-11
Project: JTC1.22.32 
Reply To: Guy Davidson
          Convenor, SC22/WG21
          Email: [email protected]

```

## Contents

- Purpose and audience
- Code of conduct
- Consensus
- Proposals and papers
- Subgroup responsibility and polls
- Closing plenary session responsibility and polls
- Technical specifications and white papers
- Working draft handling
- Ballots and comments
- How to report a potential technical concern, at any level of severity
- Escalating a serious "cannot live with" objection, or significant new information
- Other topics

## Purpose and audience

 This document contains important information that applies to all active WG21 participants, meaning accredited national body experts and especially those who attend our face-to-face meetings. Although this document is also useful to new participants to get up to speed, the material herein covers important procedures and situations that arise regularly in our meetings, email lists, formal ballots, and other participation, and everyone who participates in WG21 is expected to be familiar with this information.

 This document summarizes some of WG21's current practices and procedures, in addition to the requirements of the ISO/IEC Directives and JTC 1 Supplement available at the ISO Directives and Policies page.

 This document will call out with "ISO" or similar where states clear rules, and otherwise documents our WG21-specific practices for implementing the ISO guidance and organizing our meetings

 Note: This document does not repeat the basic material already covered in the following:

- The committee: Our organization, including the names of all of the officers and subgroup chairs.
- Meetings and participation: How WG21 meetings and teleconferences work; how to get involved and participate at face-to-face meetings; and what the committee email lists (aka "reflectors") are and who can join them.
- How to submit a proposal: How to get initial feedback to explore an idea and craft a proposal; whether an implementation is required; what ISO intellectual property rules to keep in mind; and how to present a proposal at a face-to-face meeting.
- The life of an ISO proposal: From 'cool idea' to 'international standard'
- SD-3: Study group organizational information.
- Meeting wikis: Contains meeting-specific wikis that contain all the meeting's agendas, detailed schedules, and discussion notes, as well as a meeting-nonspecific wiki containing timeless information such as how to join the mailing lists and manage your own list subscriptions.

## Code of Conduct

 We follow the ISO Code of Ethics and Conduct (March 2023) and IEC Code of Conduct -- together, the Code. (See also: ISO Code of Ethics and Conduct - Implementation (March 2023))

 To report a concern about a potential Code of Conduct violation, follow the steps in the ISO document "Guidance and Process For Addressing Misconduct and Breaches of the Code of Conduct."

 At the start of every meeting, we display the following ISO/IEC JTC 1 slide:

> #### Key ISO and IEC Messages on Ethics and Respect for the Attention of JTC 1 Committees
> 
> Escalate & resolve disputes
> 
> - Identify & escalate disputes in a timely manner for rapid resolution
> - Uphold the agreed dispute resolution processes
> 
> Behave ethically
> 
> - Act in good faith & with due care & diligence
> - Avoid collusive or anticompetitive behavior
> - Promote a culture of fair & ethical behavior
> 
> Respect others in meetings
> 
> - Be professional
> - Respect others & their opinions
> - Accept group decisions
> - Ensure that all views are heard & understood
> - Be tolerant of different cultural practices
> - Avoid metaphors, irony & be aware that jokes and humor may not translate
> 
> Respect others on social media
> 
> - Be respectful & not abusive
> - Don’t say anything that you might regret or don’t want your friends, family or colleagues to see

## Consensus

 Consensus is defined as follows in the ISO/IEC Guide 2:2004, as quoted in the ISO/IEC Directives:

> consensus: General agreement, characterized by the absence of sustained opposition to substantial issues by any important part of the concerned interests and by a process that involves seeking to take into account the views of all parties concerned and to reconcile any conflicting arguments.

> NOTE Consensus need not imply unanimity.

 Importantly, note what consensus is not:

- Consensus is not a tyranny of the majority. The majority cannot just say "we have enough votes" and refuse to listen to the concerns of the minority. The ISO Code of Conduct requires the majority to 'ensure that the views of all are heard and understood.'
- Consensus is not a tyranny of the minority. The minority, once they have had opportunity to be heard, cannot just say "we still object so you can't proceed" and refuse to accept the consensus of the majority to pursue a different direction. The ISO Code of Conduct requires the minority to 'accept group decisions.'
- Consensus does not preclude judicious escalation ("throwing an exception"). In rare cases, where the minority still believe that a serious error of judgment is being made, escalation can be appropriate in accord with the Escalation procedures covered later in this document; note that the key words are "rare" (not regular), "still" (it was raised before), and "serious." The ISO Code of Conduct encourages 'escalating disputes in a timely manner' with an 'agreed dispute resolution processes.' Escalation can become inappropriate in two ways: (a) when a serious objection is not raised "in a timely manner," such as being withheld until plenary session or formal ballot time rather than being raised consistently throughout the process starting as early as possible; or (b) when a participant or national body regularly uses the escalation process to express a pattern of strong disagreement on topic after topic, which erodes their credibility and is not the purpose of the escalation resolution process (like exception handling, escalation handling is for hard errors, and is not designed for expressing less serious conditions or for what should be ordinary control flow).

## Proposals and papers

 If a proposal doesn't have a paper, it doesn't exist. Any significant proposal requires a paper, including every proposal that is a design addition or change.

> Note: A paper is not needed for minor issues that are about improving standardese wording to implement the decided design. Those do not affect the design itself, and can be put on issues lists only.

 High-quality proposal papers. A proposal paper is much more than an "idea" that is written down. A good proposal paper should:

- Be example-based: Demonstrate motivating examples of how the code we have to write today is problematic and needs improvement. Show specific examples of how the proposed feature is intended to be used, including how those motivating examples would look if we had the new proposed feature.
- Be principle-based: Articulate the design principles for the proposed solution. Show how the proposed solution fits with the rest of the language’s principles and design philosophy (note: explicitly not with the language’s quirks). Ideally include citations of principles/philosophy articulated in The Design and Evolution of C++ (D&E).
- Show design alternatives considered: along with concrete examples showing why they were not pursued. The author should demonstrate that they have considered the problem reasonably thoroughly, and are not just running with the first idea that occurred to them.

 These three points are the main things that make the difference between "someone's cool idea" (which may be interesting but is procedurally unuseful) and "a real proposal" (that can be seriously evaluated and progressed).

> Note: For additional details about writing proposals, see also:
> 
> - How to submit a proposal: How to get initial feedback to explore an idea and craft a proposal; whether an implementation is required; what ISO intellectual property rules to keep in mind; and how to present a proposal at a face-to-face meeting.
> - The life of an ISO proposal: From 'cool idea' to 'international standard'

 On-time papers. All papers to be considered at a meeting must be received before that meeting's pre-meeting mailing deadline. The agenda for each meeting includes all papers in mailings since the previous meeting (from the post-meeting mailing of the previous meeting to the pre-meeting mailing of this meeting, inclusive), as well as possibly selected earlier papers that were not sufficiently addressed at a previous meeting in the judgment of the subgroup chair. Requiring papers to be received on time ensures that national body experts have sufficient time to consider the proposals in advance and arrive at the meeting prepared to participate in a productive discussion.

 Late papers. A proposal that does not have an on-time paper published since the previous meeting is not actionable and will not be considered during official meeting time; the author is encouraged to submit a revision as an on-time paper for a future meeting. (Note: Followup papers to an on-time paper, such as late or in-meeting rebuttal/elaboration/update papers to an on-time paper, can of course be considered; they are part of considering the on-time paper.)

> Corollary: If a topic does not have at least one on-time paper, the whole topic is not on the meeting agenda. Sticking to the published agenda, including the topics of papers published in the pre-meeting mailing, is essential to ensure all stakeholders have full opportunity to be present so that we have orderly progress. Per ISO rules, if a WG meeting were to take action on a topic that was not mentioned on the agenda (including in the topics of on-time papers), a national body could formally escalate an objection in SC 22 and JTC 1 to the entire WG meeting on the grounds that the national body had insufficient notice so as to be able to send any (or the right) participants to participate in that technical discussion topic.

 Prepared presenters. A proposal that does not have one of its authors, or another qualified and prepared presenter, to present it is not actionable and will not be considered during official meeting time. There are several reasons we insist a real proposer be present:

- The purpose of a presentation is for a person who is an expert in the paper's domain (including in constraints as well as design alternatives considered) to educate a group of general C++ experts. This requires that the presenter be qualified to answer detailed questions about design constraints in the problem domain, design alternatives considered and how they worked out, and so forth at a level that the group as a whole does not already know.
- A major outcome of the subgroup discussion is to give feedback and direction to the author regarding how to improve their proposal to create an updated revision for the next meeting. The presenter must be someone who is invested in the proposal and will ensure feedback will be used, which means the presenter will personally produce a new revision of the paper based on feedback or else will communicate feedback to the author to do so. Otherwise, the group's time to generate the feedback is meaningless.

> Note: In the past, sometimes the subgroup chair has tried to help find a presenter. This is not useful and is actively discouraged, because in practice it results in a presenter who is at best semi-familiar with the topic and who is not personally invested in working on the paper.

 Delay vs. bird in the hand. We cannot act on ideas without papers, and we do not significantly delay progress on concrete proposals in order to wait for alternative proposals we might get in the future. If we have an active proposal that is making progress, and an objection is raised that a different competing approach would be better but that other approach does not yet have a paper, the EWG or LEWG subgroup chair may elect to delay the progress of the active proposal by one meeting to give the objector(s) opportunity to bring an on-time proposal paper. Otherwise, if a competing alternative does not have a paper, it does not exist and will not block progress of a proposal that we do have before us.

> Note: At early discussion phases, subgroup chairs have discretion to allow limited exploration of alternatives to an active proposal to decide whether a second paper is warranted, or to discuss broader prerequisite topics that are exposed by a paper under discussion.

 Using the 1-2 year TS lag effectively. If a proposal has consensus to be in a TS, but does not yet have consensus to be in the IS, that means its progress is delayed by approximately 1-2 years; that is the time it takes to publish the TS, and then wait for usually one year before the TS is proposed to be merged into the IS with any changes based on the TS experience. That window is a limited "grace period" wherein any participants who prefer a different approach than the one in that proposal should be actively working on developing their own alternative proposals. Do not wait, thinking that two years is a long time; it isn't. If by the time the TS is ready to be considered for merging into the IS we do not have alternative proposals actively progressing, the default action to is to move forward with the proposal we have, we will not wait indefinitely for something better.

## Subgroup responsibility and polls

 Subgroup chairs. Subgroup chairs are appointed by the convener, and are selected to match the current needs of the subgroup. They have no fixed term.

 Subgroup discussion. Discussion is orderly. Those who wish to speak raise their hands and are recognized by the chair. The chair is encouraged to keep a visible list when multiple people are in the queue.

 Subgroup polls. In subgroup polls, each person in the room can cast one vote. The subgroup chair may take any polls they choose. Typical kinds of polls include the following:

- Unanimous consent, where if there are no objections then it is known that everyone is either in favor or neutral, without having to count hands. This is typically used to save time when there may already be broad agreement.
- "5-way" polls, where the choices are Strongly Favor, Weakly Favor, Neutral, Weakly Against, and Strongly Against.
- Multiple polls, where multiple alternatives are polled (e.g., by 5-way poll) in order to see which has most consensus. This is encouraged so as not to lose the option that has the most consensus because of the order in which polls are taken.
- Approval polls, where there is a list of alternatives and the chair takes a single show of hands for those 'not opposed' to each alternative. Typically there is then a runoff approval poll among the most popular options. This is typically used to bikeshed naming.

 Notes:

- Subgroup polls, especially in design subgroups, should favor progress. A proposal normally advances if there are more than twice as many in favor of a proposal as against, after discussion of the concerns of those voting against and possibly a re-poll to see if opinions have improved. This is true even if a large number vote Neutral, though it can be concerning if a majority of all those voting vote Neutral.
- Not everyone in the room needs to vote (even Neutral). Not everyone is interested in every proposal, and participants who are not familiar with the material of a particular poll (did not read the paper and/or were not closely paying attention to the discussion) typically do not vote on that poll.
- Anyone voting Against, especially Strongly Against, may be asked for their reasons by the chair. They should be prepared to articulate their rationale, including either what change(s) would address their concern and change their position, or else that they are opposed to pursuing the proposal in any form and no change would change their position.

 Direction group. The direction group is a small by-invitation group of experienced participants who are asked to recommend priorities for WG21. Currently, that group consists of: Jeff Garland, Paul McKenney, Roger Orr, Bjarne Stroustrup, Daveed Vandevoorde, and Michael Wong. Their charter includes setting forth a group opinion on:

- Evolution direction (language and library): This includes both language and library topics, and includes both proposals in hand and proposals we do not have but should solicit. The direction group maintains a list of the proposals it considers the most important for the next version of C++ or to otherwise make progress such as in a TS, and the design group chairs use that that list to prioritize work at meetings. Typically, work on other topics will occur after there's nothing further left to do at this meeting to advance the listed items.
- Providing an opinion on any specific proposal: This includes whether the proposal should be pursued or not, and if pursued any changes that should be considered. Design group participants are strongly encouraged to give weight to an opinion that the design group feel strongly enough about to suggest.

 Study groups. Study groups (SGs) own "incubating" to produce an initial proposal that can then enter the usual design group processing. An SG is formed by the convener at the recommendation of a design subgroup chair when there appears to be broad interest in a topic, there is not yet a unified initial proposal to bring to the design subgroup (typically because proposals are immature, incomplete, and/or competing), and there is a strong candidate to chair the SG to ensure it operates productively.

> Note: For additional information, see SD-3: Study group organizational information.

 Design subgroups. The design subgroups (EWG and LEWG) own selecting and recommending feature designs and ship vehicles (TS or IS). Notes:

- Discussion should be constructive, help achieve a broad understanding of the proposal within the design subgroup, and to result in polls that give the proposal author meaningful and actionable feedback on whether and how to improve the proposal. Both positive and negative comments are welcome, but should always be constructive and respectful.
- If anyone has a concern that a particular new proposal should not take up extended subgroup time (e.g., is not well thought out, is in a direction that previously did not get interest or consensus, or is otherwise unlikely to progress in its current form), they should share their concern privately and in advance with the subgroup chair. The subgroup chair may choose (based on such requests or just on their own judgment) to expedite the proposal's initial handling to make sure a representative overview is heard but then determine whether it has enough subgroup interest before spending extended time exploring the details; for example, the chair might time-box initial discussion and then poll whether the subgroup is interested in discussing the proposal's details further.
- The proposal author is expected to participate in the design subgroup to present the proposal, answer questions, participate in design discussion, and implement any changes directed by the group, typically for subsequent revisions of the proposal to be considered at the next meeting. In rare cases, if the proposal author chooses not to implement a change directed by the group, the author should be prepared to defend that decision and bring new information to the next meeting as part of the paper revision; proposals that do not implement design subgroup direction harm their own chances of gaining consensus within the design group and/or in plenary.
- When a proposal's design achieves a general consensus of the design subgroup, as determined by the subgroup chair, for its design and ship vehicle, it is forwarded to the specification subgroups. The proposal author is expected to work with the design subgroup chair and the specification subgroup chair to find a wording expert to help them draft high-quality standardese wording before the specification subgroup review begins.

 Specification subgroups. The specification subgroups (CWG and LWG) own the recommendation of the "standardese" specification (aka "wording") that implements the intended design. Notes:

- The proposal author is expected to be available in the specification subgroup to make specification changes.
- If the specification subgroup has design questions or suggestions, those questions are referred back to the design group.
- The proposal author is expected to participate in the specification subgroup to answer questions and implement specification changes directed by the group.
- When a proposal's specification achieves a general consensus of the specification subgroup, as determined by the subgroup chair, that its specification correctly expresses the intended design, it is forwarded to the closing plenary (whole-WG21) session.

> Notes:
> 
> - The meeting's Straw Polls wiki page will be updated by 8:00pm local time the night before the closing plenary session to show all these polls (to be added in the main text by the specification subgroup chairs only — no one else should edit that page) and all final P- and N-numbered papers referred to in those polls (to be added as attachments to that page by their proposers).
> - For additional convenience, the specification subgroup chairs will endeavor to start filling in the Straw Polls wiki page on a best-effort basis during the week. However, this is not guaranteed, and anyone who wants the most current information should read the wiki notes of each specification subgroup to see current progress, including which items are planned to be brought forward to plenary. For example, on the CWG wiki, typically searching for "Ready for vote on Saturday" will show you all the items are they are approved.

 Work prioritization at meetings. Subgroup chairs prioritize first papers that are related to one or more of the following: Direction priorities recommended in P0939; work the committee is aiming to include in the next IS; and work that can make plenary progress at this meeting. After that they get to things on a best-effort basis as time allows.

## Closing plenary session responsibility and polls

 Presentations. The main subgroup chairs present their progress for the week:

- Design subgroup chairs present the proposals whose designs were approved at this meeting, including to solicit all present to express any serious design concerns that may not have been discovered in subgroups so that these can be known and addressed before extensive wording effort is invested. The list of approved designs will also be added to an update of the Proposal Designs Approved paper in the post-meeting mailing. (Note: This is a new procedure, doesn't yet exist. With each update, it will create a cumulative list of the proposal designs approved at each meeting.)
- Specification subgroup chairs present the polls to be brought forward.

 Plenary polls. In plenary polls, each person present whose nameis listed in the ISO LiveLink global directory can vote. The Convener may take any polls they choose; however, typically the most frequent polls are "3-way" polls where the choices are Favor, Against, and Neutral. Notes:

- The default is to ask if there is objection to unanimous consent. (Unanimous consent means that all participant positions are either Favor or Neutral, and that none are Against). Most polls pass by unanimous consent.
- If there is an objection to unanimous consent, the Convener takes a 3-way poll as described above. If there is significant opposition, the Convener will usually ask whether the Against votes are personal positions or national body positions, typically by asking the national body panel chairs who are present.

 Closing plenary session. The WG21 closing plenary session owns approval of adding a proposal and its specification wording to a working draft (TS or IS). The plenary session's responsibility is to decide whether there is consensus, as determined by the Convener, to adopt each proposed change that is recommended by the design and specification subgroups. The plenary session does not actively change the design or entertain extended design discussion, which always happens in the design subgroups. However, the plenary session participants may ask questions like: "does this handle case X?" and "did you consider alternative Y?" For such questions, the meeting chair will ask the appropriate subgroup chair (who may invite comment from the proposal's author) to answer whether that item was considered and to summarize the result of the discussion and the reason for the decision of the subgroup.

 Plenary session polls also include recommendations to ship a document for a formal ballot or for publication. If such a poll gets consensus, the document is considered to represent the consensus of WG21 for its current stage of development.

## Technical Specifications (TS) and White Papers

 A TS or white paper is an experimental branch. In ISO, a TS or white paper is for a feature that does not yet have consensus for an IS. A TS or white paper is a separately published "experimental branch" that can ship separately to gain experience — either with an experimental part of the design, or to get enough overall experience so that participants are comfortable that the overall design works as well as hoped. We usually do not put work into a TS or white paper unless WG21 likes the general direction the feature is exploring, and would entertain merging it into the IS in some form (possibly after significant further transformation) if it turns out to work out successfully; features we know we do not intend to put in the IS are not worth shipping in experimental form either.

> Note: A good example is the Reflection TS. There, we knew from the outset that we intended to radically change the surface interface from a template metaprogramming style to a value style. The goal of the TS was to get feedback on the core reflection capability under the hood of that "skinnable" interface.

> Note: The only exception so far is the Transactional Memory TS. In that case, WG21 was asked to take an existing industry specification and republish a refined version as an ISO TS without an expectation of merging it into the IS because the material was known to be experimental.

 TS vs white paper: They are functionally the same, but a white paper has a very-lightweight ISO process and is now recommended by ISO and SC22.

- A TS goes through similar ISO balloting as an IS, at the SC22 and JTC1 and ISO/ITTF levels, though with fewer and slightly shorter steps than an IS. A TS is subject to ISO minimum/maximum time schedules, requires an ISO project to be formally created, when technically complete is sent by WG21 to be formally balloted with a round of formal review comments collated by ISO that must be formally responded to with a Disposition of Comments paper, and even after final national body approval it is subject to sometimes-lengthy ISO editing review and changes including that follows ISO's prescribed format which includes both written and unwritten rules.
- A white paper is adopted within our immediate parent committee SC22; it has no prescribed time schedule, no prescribed format, no ISO editing, and when technically complete is sent by WG21 to SC22 to be approved by a simple vote by SC22 national bodies to adopt the draft as a white paper.

 Starting in 2023, ISO recommended to SC22 that SC22 WGs consider white papers as an option to avoid the ISO process bottlenecks.

 Proposal vs. TS / white paper: A TS or white paper is a shipped product, not just a proposal. Unlike a proposal paper (which is maintained by the author independently), a TS or white paper:

- is a document owned by the committee;
- is changed only as directed by full committee approval polls;
- has higher quality wording requirements;
- is shipped as an official ISO publication; and
- unblocks early implementers and users.

 TS / white paper vs. draft IS: A TS or white paper is an experimental product, not a draft-standard feature. Unlike a feature in a draft C++ standard, a TS or white paper:

- allows us to unblock the progress mentioned in the previous paragraph even when there is not yet consensus on the design, when people and national bodies typically still have strong technical concerns but are temporarily willing to publish without making the changes suggested by those concerns in return for knowing the consensus gap will be addressed later based on experience with the TS or white paper;
- is considered "non-normative" because conformance is not required and the contents are subject to change; and
- asks implementations/users to give feedback to identify shortcomings and puts them on notice to expect breaking changes (they typically should not rely on the feature in production code).

 Starting a new TS or white paper. We can initiate a new TS or white paper project once material (one or more related proposals) gets to the stage where the committee wants to pursue turning it into an initial working draft for a TS or white paper, and the subgroup chair has identified an appropriate project editor acceptable to the convener that the convener will appoint to maintain the draft. This is initiated by a plenary session poll to turn the document(s) into a new working draft and direct the convener to arrange with ISO to start work on a TS or white paper; these two steps are done simultaneously in order to ensure we never have an open project without a working draft (the reverse is okay).

> Note: The wording of the plenary session straw poll is as follows.
> 
> - Move to direct the Convener to request a New Work Item for a [Technical Specification | White Paper] on "C++ Extensions for [Topic]" and create a working draft with [PxxxxRnn "Title X" and PyyyyRmm "Title Y" and ...] as its initial content.

 Listing specific goals. The TS or white paper should list known specific questions on which feedback is desired, including:

- What are we hoping to learn through this TS or white paper?
- What are the exit criteria (especially, the list of must-address controversial issues) before we can consider merging this TS or white paper into the IS?

 A TS or white paper is not an open-ended fishing expedition. It starts with a specific design and aims at answering specific questions. To help potential users, the goals section should outline the extent to which the initial design is considered is considered "firm" (as opposed to a simple strawman outlining the problem space) and what questions the committee would like users to help answer. This should help users estimate the degree of risk incurred using an implementation and help implementers estimate the effort involved in an implementation (e.g., if understanding of "performance" is part of the desired results of a TS or white paper effort the implementation effort might differ from a TS or white paper goal related to "teachability").

 Breaking changes. A major reason to put a feature in a TS or white paper is to permit taking further breaking changes before it is standardized. Once a feature is in an IS, it is essentially cast in stone and much more difficult to update with breaking changes. WG21 has never adopted a TS or white paper into the IS without significant change.

 Merging TS or white paper to draft IS. When considering merging a TS or white paper into the draft IS, there are typically two sets of issues:

1. post-merge issues, where we have a consensus to merge the TS or white paper into the IS working draft and then addressing these issues afterwards; and
2. pre-merge issues, where we do not have a consensus to merge into the IS working draft until this specific set of issues is first addressed.

 Post-merge issues are likely, but not guaranteed, to be addressed before the IS ships. Pre-merge issues are issues where many participants would "rather not have the feature in the IS at all than have it without those issues addressed." We encourage all participants to keep the second set as small as possible, for real make-or-break concerns only, so that we can merge a TS or white paper early to permit better "integration testing" as we refine it further in the full context of the IS, and permit other parts of the standard to adapt to the new feature. Issues that people and national bodies were willing to hold in abeyance with provisional resolutions for the TS or white paper are expected to have to be addressed, possibly pre-merge; however, people are encouraged not to rehash decisions that already had consensus when the TS or white paper was started unless new information has emerged.

 A TS or white paper can can fail or remain a TS or white paper. Some experiments don't work out, and sometimes a TS or white paper can fail to be completed or can succeed only as a TS or white paper. For example, the Array TS was abandoned for lack of consensus, and the Transactional Memory TS was not integrated into the IS because it was not obvious that a sufficiently large part of the C++ community would benefit from it being in the IS rather than in a TS.

## Working draft handling

 Approving updated working drafts. In the opening plenary session of each meeting, we routinely adopt the updated working drafts generated after the previous meeting as described in the next paragraph. During the meeting, the wording for all new proposed changes is written against these adopted drafts as the meeting's baseline.

 Approving changes to working drafts. In the closing plenary session of each meeting, we have a series of polls each asking to approve applying changes specified in a given wording paper or issues list entry to update a specific working draft.

> Note: The wording of the plenary session straw poll is as follows.
> 
> - Move to apply [paper or issue number(s)] to the [Topic] working draft.

 Applying changes to working drafts. After the meeting, each project editor produces an updated candidate working draft that applies all the changes approved for that draft, and generates an editor's report summarizing those changes and any other comments that arose while applying and merging them. The updated draft typically appears in the post-meeting mailing, but no later than the pre-meeting mailing for the next meeting. Project editors may make editorial changes at any time, but may only make technical changes approved by plenary.

 Sending drafts out for ballots. If a working draft is also ready to be sent out for ISO ballot, and there were changes approved to the draft, then the poll to direct the convener to send the document out for ballot also includes naming an editing committee to verify that all approved changes were applied correctly by the project editor before the document is transmitted for ballot.

> Note: The wording of the plenary session straw poll is as follows.
> 
> - Move to appoint an editing committee composed of [...] to approve the correctness of the [Topic] working draft as modified by the motions approved at this meeting, and to direct the Convener to transmit the approved updated working draft for [PDTS|CD|DIS|FDIS ballot or publication].

 When the specification subgroups reviewed an updated draft with changes applied in situ. Occasionally, if the specification subgroups have already reviewed an entire new working draft paper with changes applied, rather than a change paper describing wording diffs, then the plenary polls are adjusted as follows:

- To approve the change, instead of a poll to apply a paper to the working draft, we have a poll to approve the changes in the form already applied to the new working draft paper. (Note: For procedural simplicity, we still re-adopt the same working draft at the beginning of the next meeting as usual.)
- To send the draft out for ballot, an editing committee is not needed since it has already been verified that changes were applied correctly.

## Ballots and comments

 National bodies and participation. All ISO JTC 1 / SC 22 "P" (Participating) national bodies can send accredited experts to participate in person at WG21 meetings and can vote on ballot documents. National bodies are expected to send experts to participate in person in WG21 if they want to affect the direction of the standard.

> Note: Typically that means regularly sending representatives to attend WG21 face-to-face meetings. In the rare case that an NBs is an SC22 P-member but is unable to send representatives to attend WG21 meetings (typically due to severe economic hardship whereby they can participate by remote ballot review but not in person due to travel costs, or due to force majeure such as unexpected changes in governmental travel restrictions), they are still strongly encouraged to participate in WG21 email lists and raise concerns there instead of waiting for ballot comments.

 Ballot purpose and structure. An ISO comment ballot is a request for national bodies (NBs) to provide specific feedback on the material that is in the balloted document. It has two components:

- Vote for general approval/disapproval: Essentially, "do you want to see this work progress (possibly with changes), yes or no?" A Disapproval (No) vote should be used only to express that the national body does not want the work (TS or IS) to progress at all in any form — to block further progress on all parts of the work item.

> Note: In the past, ISO used to have ballot resolution meetings (BRMs) where resolving key comments by a national body could turn a No into a Yes, and national bodies would report whether they changed their vote. We no longer have that procedure or any formal mechanism to change a vote after the ballot. Therefore, No should mean "No, we don't want this TS or IS at all," because sufficient No votes have that effect — most ballots fail if more than 1/3 of NBs vote No, so voting No only to try to give the NB's comments a higher priority is ineffective (we consider all NB feedback at all times, not just on ballots, and regardless of the Yes/No vote on a ballot) and counterproductive (could actually cause the whole project to fail).

- Comments for specific feedback: Regardless of the approval/disapproval vote, most ballots can contain comments. All editorial and technical comments on the content of that document are in scope. A comment is expected to contain a proposed resolution with sufficient detail to be actionable; if more detail is required than fits easily in the comment form, referencing or attaching a paper is encouraged.

> Note: Ballot comments are treated by ISO, and therefore by WG21, as national body positions. Confusion arises when a national body submits comments without first vetting that the national body as a whole supports all the comments. In the past, some national bodies have included all comments from their members without vetting, which leads to receiving comments that a majority of the national body's own members did not support, or that contradict each other. To aid orderly comment handling, national bodies are encouraged to vet that the comments they submit are indeed national positions.

 Inappropriate ballot comments. Two specific kinds of comments are therefore not appropriate:

- A ballot comment that requests adding an additional feature that is not already in the document is out of scope. New feature proposals are encouraged, but the correct way to bring them to WG21 is by presenting a proposal paper and working to build consensus to add the feature.
- A ballot comment that requests a change that was already considered and decided otherwise at a WG21 meeting, and comes from a national body that was present at the meeting and had an opportunity to have their objections be heard and considered, is out of harmony with the ISO Code of Conduct's commitment to 'accept group decisions.' Once the WG has consensus to send a document for ballot, to repeat as an NB comment an objection that previously failed to carry the day is actually making, not a new technical objection, but an objection to the consensus of the WG.

> Note: There are two exceptions:
> 
> 1. If sufficient new information came to light since the last discussion that it is reasonable to believe enough people could change their opinions to affect the previous consensus. That information, of course, requires an on-time paper for the ballot resolution meeting, and ideally that paper would be available early and referenced directly in the ballot comment.
> 2. If the national body really strongly objects to a specific item so much that they are willing to vote No on progressing the whole TS or IS that it's in, and have informed the committee all along of the strength of their feeling (see "Escalation..." below). If WG21 were to ballot a document over those objections, they would know that a No With Comments could happen; but the No vote, and negative comments, would be regarding a previously discussed and decided matter, they should never arise for the first time as a surprise No vote on a ballot.

 Ballot comment resolution improves consensus. Any technical changes made during ballot comment resolution have one goal: to improve consensus. In the case of a successful final approval ballot, where after ballot comment resolution the document will be sent directly to ISO for publication without another ballot, any design change made between the ballot and publication will be expected to have near-unanimous consent in subgroups and in plenary. This is because we need to have strong confidence that the design change is not reducing the existing consensus, and we do not have another ballot to find out whether the change would affect the opinion of any NBs who are not represented at the meeting where ballot comment resolution is being done.

## How to report a potential technical concern, at any level of severity

 If you notice a potential problem, please follow these steps:

1. Keep the mindset that it's a "potential" problem. Very often, even experienced participants find that a potential problem they spot turns out to be a misunderstanding or to have a well-considered rationale. Keeping the view that it's a "potential" problem greatly improves the tone and productiveness of all discussions.
2. Describe the problem, and ask whether it was considered. If the concern is about a feature proposal (whether already adopted or still underway) include the proposal authors; as the feature's designers they will be among the best experts about the issue.
3. If it was considered, and you think you have disagreement with the decision, explain how and why, and based on what (implementation/deployment/user experience are useful points).
4. If it wasn't considered, again explain how and why there's a problem, and based on what.
5. Discuss whether it can be handled as an issue or whether a paper is needed.
6. File the issue or write the paper, or otherwise make sure such a follow-up happens. Ensure the feature's designers (proposal authors) are aware of the follow-up issue or paper.

- Consider beforehand how severe the problem is. Is the house on fire, or is it just a minor gaffe/inconvenience? To whom? Based on what?
- Listen to what other people say, and consider their viewpoints on the matter. Even if people disagree with your viewpoint, remember to read/listen what they say, and consider why.

 In general, these steps should happen:

- As early as possible, inform the EWG and LEWG chairs and the proposal's authors: They need to be aware of your concern, are trained in triaging and prioritizing issues and concerns, and can offer calm advice on how to proceed.
- As early as possible, inform the subgroup: preferably during the discussion in a meeting, even more preferably before a meeting on a reflector. This is in accord with the ISO Code of Conduct's "timely manner" expectation.
- If you didn't notice it then, before the straw poll.
- If you didn't notice it then, after the meeting on a reflector.

## Escalating a serious "cannot live with" objection, or significant new information

 If you feel that a subgroup decision is making a serious mistake so severe that you feel you cannot live with the result, and/or you learn of significant new information not considered in the subgroup discussion that could reasonably change the view of the other participants:

 As early as possible, make the EWG and LEWG chairs aware of your concern. If it is a subgroup decision made during the week and that will be brought forward to plenary that week, you should proactively raise it during the week:

- On the committee email lists: Ideally the issue should be raised on the relevant subgroup's email list immediately following the subgroup discussion to which the objection appertains, but in no case any later than the deadline of 5pm the evening before the closing plenary session (and posting much sooner than that is strongly encouraged, ideally right after the subgroup decision they feel is wrong, is strongly encouraged).
- Within your own national body: This is so that the national body chair has opportunity to caucus with their members and determine whether the position may be a national position (normally the default is no, not a national position, unless it was discussed before or during the meeting to determine that it is a national position).

 That way, when we come to plenary, everyone has had opportunity to be informed of the serious concern with time to consider it, and when the Convener asks your national body's chair whether the objection is a personal or national position, they will be equipped to answer. Objections that are not so escalated, but are raised or re-raised in plenary, should not be given weight in plenary. (In the rare case of new information that is found 'just the night before' plenary, it has still passed the cutoff for plenary participants to be able to give it informed and prepared consideration in time for plenary, and it is a race condition that we linearize by saying it has failed to be raised before the cutoff, and should be handled per the next bullet including with a followup paper.)

 If it is new information found after the deadline (including between meetings), they should raise it:

- On the committee email lists.
- As a national body ballot comment. If a participant does not raise the concern within their national body, and succeed in convincing enough people in their caucus to make it a national body position (by whatever internal rules that particular national body panel uses to determine such), it won't become a national position.

 In both cases, it should be raised with a discussion paper containing detailed information (at least a draft paper if a final one is not yet available).

## Other topics

 Protected materials. The following materials are not publicly available and are always password-protected:

- Documents on which ISO asserts copyright, notably the final text of a TS/IS.
- Meeting records of subgroup discussion, meeting wikis, and non-public committee email lists (aka reflectors), which often include personal positions and discussion. It is not allowed to quote from these publicly (e.g., in papers and blog posts) except that the following are allowed: (a) quoting straw poll questions and numeric results; and (b) quoting words or positions attributed to a specific person with that person's prior consent.

 Minutes.

- All meetings must be minuted. This includes telecons as well as in-person meetings.
- If you are present at a meeting of WG21 or any of its study groups, you should be prepared to take minutes, and to accept nomination to do so in the absence of volunteers.
- This was the result of a plenary poll at Wroclaw in 2024.

## ISO/IEC Directives Part 1, 0.7

###### **0.7 General Directives procedures** 

These procedures have been established by ISO and IEC in recognition of the need for International Standards to be cost-effective and timely, as well as widely recognized and generally applied. To attain these objectives, the procedures are based on the following concepts. 

- a) Current technology and project management 

Within the framework of these procedures, the work may be accelerated, and the task of Experts and secretariats facilitated both by current technology (e.g. IT tools) and project management methods. 

- b) Consensus 

Consensus, which requires the resolution of substantial objections, is an essential procedural principle and a necessary condition for the preparation of International Standards that will be accepted and widely used. Although it is necessary for the technical work to progress speedily, sufficient time is required before the approval stage for the discussion, negotiation and resolution of significant technical disagreements. 

For further details on the principle of "consensus", see 2.5.7. 

###### c) Discipline 

National Bodies need to ensure discipline with respect to deadlines and timetables to avoid long and uncertain periods of "dead time". Similarly, to avoid re-discussion, National Bodies have the responsibility to ensure that their technical standpoint is established, taking account of all interests concerned at the national level, and that this standpoint is made clear at an early stage of the work rather than, for example, at the final (approval) stage. Moreover, National Bodies need to recognize that substantial comments tabled at meetings are counter-productive since no opportunity is available for other delegations to carry out the necessary consultations at home, without which rapid achievement of consensus will be difficult. National Bodies are encouraged to abstain if there is a lack of national consensus or Expert input on a specific ballot. 

- d) Cost-effectiveness 

These procedures take into account the total cost of the operation. The concept of "total cost" includes direct expenditure by National Bodies, expenditure by the offices in Geneva (funded mainly by the dues of National Bodies), travel costs and the value of the time spent by Experts in working groups and committees at both national and international level. 

Opportunities for remote participation at face-to-face meetings should be provided to the extent possible (see Clause 5). 

- e) Terminology used in this document 

Wherever appropriate in this document, for the sake of brevity, the following terminology has been adopted to represent concepts that are similar or identical within ISO and IEC. 

|**Term**|**ISO**|**IEC**|
|---|---|---|
|National Body|Member Body (MB)|National Committee (NC)|
|technical management<br>board|Technical Management<br>Board (ISO/TMB)|Standardization<br>Management Board<br>(IEC SMB)|
|Chief Executive Officer<br>(CEO)|Secretary-General|Secretary-General|
|Office of the CEO|Central Secretariat (CS)|Secretariat (Sec)|
|council board|ISO Council|IEC Board|
|Secretary/Committee<br>Manager|Committee Manager|Secretary|
|committee|TCs, SCs, PCs and SyCs|TCs, SCs, PCs and SyCs|



**8** 

© ISO/IEC 2026 – All rights reserved 

In addition, the following abbreviations are used in this document. 

- IS International Standard IWA International Workshop Agreement JPC joint project committee JTC joint technical committee JWG joint working group PAS Publicly Available Specification PC project committee SC subcommittee SEG Standardization Evaluation Group SRD Systems Reference Deliverable SyC systems committee TC technical committee JSyC joint systems committee TR Technical Report TS Technical Specification WG working group 

###### f) Code of ethics and conduct 

Individuals participating in ISO and IEC activities must comply with the mandatory ISO Code of Ethics and Conduct [5] and the IEC Code of conduct [6] for technical work. 

**9** 

© ISO/IEC 2026 – All rights reserved 

## ISO/IEC Directives Part 1, 1.7

###### **1.7 Participation in the work of committees** 

- **1.7.1** All National Bodies have the right to participate in the work of committees. 

To achieve maximum efficiency and the necessary discipline in the work, each National Body shall clearly indicate to the Office of the CEO, with regard to each committee, if it intends 

- to participate actively in the work, with an obligation to vote on all questions formally submitted for voting within the committee, on new work item proposals, enquiry drafts and all drafts for final approval (see 1.7.4), and to contribute to meetings ( **P-members** ), or 

- to follow the work as an observer, and therefore to receive committee documents and to have the right to submit comments and to attend meetings ( **O-members** ). 

A National Body may choose to be neither a P-member nor an O-member of a given committee, in which case it will have neither the rights nor the obligations indicated above with regard to the work of that committee. Nevertheless, all National Bodies, irrespective of their status within a committee, have the right to vote on enquiry drafts (see 2.6) and on final draft International Standards (see 2.7). 

National Bodies have the responsibility to organize their national input in an efficient and timely manner, taking account of all relevant interests at their national level. 

**1.7.2** Membership of a subcommittee is open to any National Body, regardless of its membership status in the parent committee. 

Members of a parent committee shall be given the opportunity to notify their intention to become a P-member or O-member of a subcommittee at the time of its establishment. 

Membership of a parent committee does not imply automatic membership of a subcommittee; National Bodies shall notify their intended status in each subcommittee. 

**1.7.3** A National Body may, at any time, begin or end membership or change its membership status in any committee, subject to the requirements of 1.7.4. 

Furthermore, a P-member may voluntarily downgrade to O-member if it consistently lacks expertise to vote at the committee level or to participate in working groups. 

**1.7.4** A committee secretariat shall notify the Office of the CEO if a P-member of that committee has been persistently inactive or has failed to vote: 

a) persistently inactive criteria 

- a P-member is considered persistently inactive by failing to attend two successive committee meetings (either in person or remote) and by failing to have any Expert(s) appointed to the technical work; or 

b) failing to vote criteria 

- a P-member has failed to vote on any of the following document(s): 

   - proposal stage ballot; 

   - enquiry stage ballot; 

**16** 

© ISO/IEC 2026 – All rights reserved 

###### • approval stage ballot (for IS, TS, PAS, TR, SRD and validation draft (VD)). 

NOTE 1 Abstentions are taken into account when evaluating P-member participation. 

Upon receipt of such a notification, the Chief Executive Officer shall remind the National Body of its obligation to take an active part in the work of the committee. In the absence of a satisfactory response to this reminder within four weeks, the status of the National Body shall, without exception, automatically be changed to that of an O-member. 

Even with the existence of a response within four weeks, should the member in question continue to be persistently inactive (see condition a) above) up to and including the next plenary meeting (or a minimum six months), the status of the National Body shall, without exception, automatically be changed to that of O-member. 

A National Body whose status is so changed may, after a period of 12 months, indicate to the Office of the CEO that it wishes to regain the P-membership of the committee, in which case this shall be granted. 

NOTE 2 1.7.4 does not apply to the development of Guides. 

**1.7.5** For votes by correspondence or during a committee meeting, a simple majority of the P-members voting is required for approval unless otherwise specified in the ISO/IEC Directives. 

For strategic matters (e.g. changing the scope of a document or the scope of a committee, change of allocation of a project), a discussion among committee members should first take place before a formal committee decision is taken. 

When a document is out for ballot or for commenting at the committee stage, formal discussion during official meetings or distribution of positions using official ISO and IEC IT tools is prohibited. This does not prohibit discussion on sections of the document that are not out for ballot or comment. 

In all votes, abstentions are not counted. 

A vote by correspondence should include the possibility to abstain. 

Proxy voting is not permitted. 

**1.7.6** In certain cases, consensus may be confirmed for questions which are expected to contain no controversial issues and for which agreement of the committee is foreseen in advance. Such questions may be distributed for a period of four weeks. If no objection is received during this period, the question is considered to be approved. If any committee P-member objects to the question during this period, the Secretary/Committee Manager shall withdraw the question immediately and resolve the question by vote, either at a meeting or by correspondence. P-members wishing to raise an objection to a consent question are requested to notify the responsible Secretary/Committee Manager as soon as possible to prevent undue delays. 

## ISO/IEC Directives Part 1, 1.8.2

###### **1.8.2 Responsibilities** 

The Chair of a technical committee is responsible for the overall management of that technical committee, including any subcommittees and working groups. 

The Chair of a committee shall 

- a) act in a purely international capacity, divesting themselves of a national position; thus, the Chair cannot serve concurrently as the delegate of a National Body in their own committee; 

- b) guide the Secretary/Committee Manager of that committee in carrying out their duties; 

- c) conduct committee meetings with a view to reaching an agreement on committee drafts (see 2.5); 

- d) ensure at meetings that all points of view expressed are adequately summarized so that they are understood by all present; 

- e) ensure at meetings that all decisions are clearly formulated and made available in written form by the Secretary/Committee Manager for confirmation during the meeting; 

- f) take appropriate decisions at the committee stage (see 2.5) and enquiry stage (see 2.6); 

- g) advise the technical management board on important matters relating to that technical committee via the technical committee secretariat. For this purpose, the Chair shall receive reports from the Chairs of any subcommittees via the subcommittee secretariats; 

- h) ensure that the policy and strategic decisions of the technical management board are implemented in the committee; 

- i) ensure the establishment and ongoing maintenance of a strategic business plan covering the activities of the technical committee and all groups reporting to the technical committee, including all subcommittees; 

- j) ensure the appropriate and consistent implementation and application of the committee's strategic business plan to the activities of the technical committee's or subcommittee's work programme; 

- k) assist in the case of an appeal against a committee decision. 

The Chair has no vote, and questions on which the vote is equally divided shall be subject to further discussion. 

In case of unforeseen unavailability of the Chair at a meeting, an acting Chair may be proposed by the Secretary/Committee Manager and approved by the committee for the meeting. SC Chairs shall attend meetings of the parent committee as required and may participate in the discussion but do not have the right to vote. In exceptional circumstances, if a Chair is prevented from attending, the Chair shall delegate the Secretary/Committee Manager to represent the subcommittee. In the case where no representative from the SC can attend, a written report shall be provided. 

## ISO/IEC Directives Part 1, 1.12.1

**1.12.1** Committees may establish, by decision of the committee, working groups for specific projects (see 2.4, 2.5, 2.6, Clause 3 and Clause 4). Working groups shall be numbered in sequence in the order in which they are established. A new working group (WG) or joint working group (JWG) shall not be established for preliminary work items (see 2.2). A WG operates by consensus, reports and gives recommendations, if any, to its parent committee through a WG Convenor appointed by the parent committee. The Convenor shall act in a purely international capacity, divesting themselves of a national position. 

WG Convenors shall be appointed by the committee for up to three-year terms. Such appointments shall be confirmed by their National Body (or liaison). The Convenor may be reappointed for additional terms of up to three years. There is no limit to the number of terms. Prior to the expiry of the term, the Secretary/Committee Manager shall issue a six-week minimum call to identify any candidates who wish to be considered for the position. If multiple candidates are nominated, the committee shall appoint a Convenor from among the candidates. 

Responsibility for any changes of Convenors rests with the committee and not with the National Body (or liaison). When a WG Convenor's term ends or if the position becomes vacant, the Secretary/Committee Manager shall launch a six-week minimum call to identify new candidates. If a candidate is already known, the Secretary/Committee Manager may combine the decision of the committee to appoint the Convenor with the call to identify any additional candidates for the WG. If any additional nominations are made or if the appointment is not approved by the committee, the Secretary/Committee Manager shall launch a subsequent six-week ballot and the candidate with the highest number of votes will be appointed. 

If a WG has an unexpected vacancy in the convenorship, the committee leadership may appoint an acting Convenor, while launching a call to identify candidates. Any such acting Convenor shall only be permitted for a maximum term of six months. 

The Convenor may be supported by a WG Secretary as needed. 

The nomination of the WG Secretary shall be confirmed by their National Body. 

A WG comprises a number of Experts individually appointed by the P-members, category A liaison and Liaison Representatives from committees in liaison (see 1.15 and 1.16) and category C organizations (see 1.17). The WG deals with a specific task allocated to it. 

The Experts appointed by a P-member or category A liaison act in a personal capacity and not as the official representative of them. The Liaison Representatives appointed by a category C liaison or committees in liaison act as official representatives of the organizations by which they have been appointed. It is recommended that the Experts and Liaison Representatives keep close contact with that P-member or liaison to inform them about the progress of the work and of the various opinions in the WG at the earliest possible stage. 

It is recommended that WGs be reasonably limited in size. The committee may therefore decide upon the maximum number of Experts appointed by each P-member and liaison organization. 

Once the decision to set up a WG has been taken, P-members and category A and category C liaisons shall be officially informed to appoint Expert(s) or Liaison Representatives. 

When a committee has decided to set up a WG, it shall ensure that a Convenor or an acting Convenor is appointed at the same time the WG is set up. The Convenor shall arrange for the first meeting of the WG to be held within 12 weeks. This information shall be communicated immediately after the committee's decision to the P-members and category A and category C liaisons, with an invitation to appoint Experts within six weeks. Additional projects may be assigned, where appropriate, to existing WGs. 

**22** 

© ISO/IEC 2026 – All rights reserved 

WGs may establish subgroups. 

## ISO/IEC Directives Part 1, 1.12.2

**1.12.2** The composition of the WG is defined in the ISO Global Directory (GD) or in the IEC Expert Management System (EMS) as appropriate. Experts not registered to a WG in the ISO GD or the IEC EMS, as appropriate, shall not participate in its work. 

Convenors may invite a specific guest to participate in up to two meetings to provide relevant expertise to the WG and shall notify the guest's National Body of the invitation ahead of the meeting via the Office of the CEO (copying the Secretary/Committee Manager of the committee). 

If the ongoing participation of a guest is necessary, such participation shall be as a WG Expert via the appropriate National Body or a liaison. 

## ISO/IEC Directives Part 1, 1.12.3

**1.12.3** Convenors should review the participation in the WG at regular intervals to identify persistently inactive P-member Experts. 

Convenors shall report inactive P-member Experts to the Secretary/Committee Manager for the follow-up action with the relevant P-members through the Office of the CEO. In the absence of satisfactory responses from the relevant P-members, the inactive P-member Experts shall be removed by the Office of the CEO. Such P-member Experts shall not be eligible for reappointment to the WG in which they were inactive by the respective P-member for a period of one year. 

In case of lack of Experts from the required number of P-members in the WG to meet the minimum number (as defined in 2.3.5), the Convenor shall inform the committee secretariat, who shall launch another call for Experts. 

If the subsequent call for Experts from the required number of P-members fails, the Convenor shall consult with the committee secretariat to decide if the project can or should continue. 

If the decision is to continue with Experts from fewer than the required number of P-members, the committee secretariat shall request permission from the technical management board to proceed. 

## ISO/IEC Directives Part 1, 2.1.6

###### **2.1.6 Target dates** 

###### **2.1.6.1 General** 

The committee shall establish, for each project in its work programme, target dates for the completion of each of the following steps: 

- circulation of the first working draft (in the event that only an outline of a working document has been provided by the proposer of the new work item proposal — see 2.3); 

- circulation of the committee draft (if any); 

- submission of the enquiry draft; 

- submission of the final draft International Standard; 

- publication (in agreement with the Office of the CEO). 

These target dates shall correspond to the shortest possible development times to produce International Standards rapidly and shall be reported to the Office of the CEO, which distributes the information to all National Bodies. 

In establishing target dates, the relationships between projects shall be taken into account. Priority shall be given to those projects intended to lead to International Standards upon which other International Standards will depend for their implementation. The highest priority shall be given to those projects having a significant effect on international trade and recognized as such by the technical management board. 

The technical management board may also instruct the secretariat of the committee concerned to submit the latest available draft to the Office of the CEO for publication as a Technical Specification (see 3.1). 

All target dates shall be kept under continuous review and amended as necessary and shall be clearly indicated in the work programme. Revised target dates shall be notified to the technical management board. 

All work items (excluding PWIs) which have been in the work programme for more than 36 months (limit date) and have not reached the approval stage (see 2.7) shall be automatically cancelled by the Office of the CEO. If the project has not reached the enquiry stage six months prior to the limit date, the project shall be automatically cancelled by the Office of the CEO. 

A single extension of up to 12 months can be given for an International Standard project on request by the Secretary/Committee Manager of the committee to the Office of the CEO. 

Committees should follow the good practices document [10] for effective management of projects. 

Time spent on interlaboratory testing during the development of a document shall not be counted in the overall development time. The project is given the status "on hold" on request from the Secretary/Committee Manager of the committee. The status of interlaboratory testing shall be reviewed at each plenary meeting of the committee. 

###### **2.1.6.2 Project plan** 

When a proposed new project is approved (whether for a new document or for the amendment or revision of an existing document), when submitting the results to the Office of the CEO, the committee secretariat shall provide an appropriate project plan. 

Committee secretariats are reminded to perform risk assessments during project planning to identify potential problems in advance and set the target dates accordingly. The target dates shall be kept under continuous review by committee secretariats, which shall ensure that they are reviewed and either confirmed or revised at each committee meeting. Such reviews shall also seek to confirm that projects are still market relevant. In cases in which they are found to be no longer required or if the 

**33** 

© ISO/IEC 2026 – All rights reserved 

likely completion date will be too late, thus causing market players to adopt an alternative solution, the projects shall be cancelled or transformed into another document. 

If a committee intends to include graphical symbols in its project, it shall follow the process outlined in 2.5.2 as soon as possible. 

## ISO/IEC Directives Part 1, 2.1.7

###### **2.1.7 Project management** 

The secretariat of the committee is responsible for the management of all projects in the work programme of that committee, including monitoring their progress against the agreed target dates. 

If target dates (see 2.1.6) are not met, and there is insufficient support for the work (that is, the acceptance requirements for new work given in 2.3.5 are no longer met), the committee responsible shall cancel the work item. 

## ISO/IEC Directives Part 1, 2.5.6

**2.5.6** Consideration of successive drafts shall continue until a consensus of the P-members as judged by the Chair has been obtained, or a decision to abandon or defer the project has been made. 

Consideration of successive committee drafts should be focused on resolving the comments raised by National Bodies and liaisons for the purpose of achieving consensus among the P-members (see 2.5.3). 

## ISO/IEC Directives Part 1, 2.5.7

**2.5.7** The decision to circulate an enquiry draft (see 2.6.1) shall be taken by the Chair of the committee on the basis of the consensus among the P-members. 

It is the responsibility of the Chair of the committee, in consultation with the Secretary/Committee Manager of the committee and, if necessary, the Project Leader, to judge whether there is consensus bearing in mind the definition of consensus given in ISO/IEC Guide 2:2004 [11]. 

" **consensus"** : general agreement, characterized by the absence of sustained opposition to substantial issues by any important part of the concerned interests and by a process that involves seeking to take into account the views of all parties concerned and to reconcile any conflicting arguments 

NOTE Consensus need not imply unanimity." 

The following applies to the definition of consensus: 

In the process of reaching a consensus, many different points of view will be expressed and addressed as the document evolves. However, "sustained oppositions" are views expressed at minuted meetings of the committee, working group (WG) or other groups (e.g. advisory groups) and which are maintained by an important part of the concerned interest and which are incompatible with the committee consensus. The notion of "concerned interest(s)" will vary depending on the dynamics of the committee and shall therefore be determined by the committee leadership on a case-by-case 

**39** 

© ISO/IEC 2026 – All rights reserved 

basis. The concept of sustained opposition is not applicable in the context of National Body votes on enquiry or approval ballots since these are subject to the applicable voting rules. 

Those expressing sustained opposition have a right to be heard, and the following approach is recommended when a sustained opposition is declared. 

- The leadership shall first assess whether the opposition can be considered a "sustained opposition", i.e. whether it has been sustained by an important part of the concerned interest. If this is not the case, the leadership will register the opposition (i.e. in the report/minutes, records, etc.) and continue to lead the work on the document. 

- If the leadership determines that there is a sustained opposition, it shall try and resolve it in good faith. However, a sustained opposition is not akin to a right to veto. The obligation to address the sustained oppositions does not imply an obligation to resolve them successfully. 

The responsibility for assessing whether or not a consensus has been reached rests entirely with the leadership. This includes assessing whether there is sustained opposition or whether any sustained opposition can be resolved without compromising the existing level of consensus on the rest of the document. In such cases, the leadership will register the opposition and continue the work. 

Those parties with sustained oppositions may avail themselves of appeals mechanisms as detailed in Clause 6. 

In case of doubt concerning consensus on a revised CD, approval by a two-thirds majority of the P-members voting may be deemed to be sufficient for the revised CD to be accepted for registration as an enquiry draft; however, every attempt shall be made to resolve negative votes. 

The secretariat of the committee responsible for the CD shall ensure that the enquiry draft fully embodies decisions taken either at meetings or by correspondence. 

## ISO/IEC Directives Part 1, 2.5.8

**2.5.8** When consensus has been reached, the committee secretariat shall submit the finalized version of the draft in electronic form suitable for distribution to the National Bodies for enquiry (2.6.1), to the Office of the CEO (with a copy to the parent committee secretariat in the case of a subcommittee) within a maximum of 16 weeks. 

## ISO/IEC Directives Part 1, 2.5.9

**2.5.9** The committee stage ends when all technical issues have been resolved, and a CD is accepted for circulation as an enquiry draft and is registered by the Office of the CEO. Texts that do not conform to the ISO/IEC Directives, Part 2 shall be returned to the secretariat with a request for correction before they are registered. 

## ISO/IEC Directives Part 1, 2.5.10

**2.5.10** If the technical issues with an International Standard project cannot all be resolved within the appropriate time limits, committees may consider publishing an intermediate document in the form of a Technical Specification (see 3.1) pending agreement on an International Standard. 

## ISO/IEC Directives Part 1, 2.6.2

###### **2.6.2** Votes submitted by National Bodies shall be explicit: positive, negative, or abstention. 

A vote may be accompanied by editorial or technical comments on the understanding that the Secretary/Committee Manager, in consultation with the Chair of the committee and Project Leader, will decide how to deal with them. 

If a National Body finds an enquiry draft unacceptable, it shall vote negatively and state the reasons by submitting comments of a technical nature. A National Body shall not cast a positive vote which is conditional on the acceptance of modifications. 

In the case where a National Body has voted negatively and has submitted technical comments that are not clearly of a technical nature, the Secretary/Committee Manager shall contact the National Body within two weeks of the ballot closure. If the committee leadership and the National Body do not find an agreement, the matter is escalated to the technical management board via the Office of the CEO. 

## ISO/IEC Directives Part 1, 2.6.3

###### **2.6.3** An enquiry draft is approved if 

- a) a two-thirds majority of the votes cast by the P-members are in favour, and 

b) not more than one-quarter of the total number of votes cast are negative. 

Abstentions are excluded when the votes are counted, as well as negative votes not accompanied by any comments of a technical nature. Comments received after the normal voting period are submitted to the committee secretariat for consideration at the time of the next review of the International Standard. 

## ISO/IEC Directives Part 1, 2.6.4

**2.6.4** On receipt of the results of the voting and any comments, an appropriate group of the committee, which would typically be the working group to which the project is assigned, will, at a meeting, address any comments received and prepare, as needed, a revised version. The group will advise the Chair on the possible courses of action. The Chair of the committee, in consultation with the Secretary/Committee Manager and the Project Leader or working group Convenor, and the Office of the CEO, shall take one of the following courses of action: 

- a) when the approval criteria of 2.6.3 are met, and no technical changes are to be included, to proceed directly to publication (see 2.8); 

- b) when the approval criteria of 2.6.3 are met, but technical changes are to be included: 

   - 1) to register the revised enquiry draft, as modified, as a final draft International Standard, or 

   - 2) to circulate the revised enquiry draft for voting (see 2.6.1). The revised enquiry draft will be circulated for a voting period of eight weeks. Committees are limited to only one revised enquiry draft where the approval criteria are met in this case; 

- c) when the approval criteria of 2.6.3 are not met: 

   - 1) to circulate the revised enquiry draft for eight weeks voting (see 2.6.1), or 

   - 2) to circulate the revised committee draft for comments, or 

   - 3) to circulate a revised draft as a draft Technical Specification, or 

   - 4) to cancel the project, subject to a decision by the committee. 

In case 3), the project shall start at the approval stage (i.e. DTS: draft Technical Specification). 

## ISO/IEC Directives Part 1, 2.6.5

**2.6.5** Not later than 12 weeks after the end of the voting period, a full report shall be prepared by the secretariat of the committee and circulated by the Office of the CEO to the National Bodies. The report shall 

- a) show the result of the voting, 

- b) state the decision of the Chair of the committee, 

- c) reproduce the text of the comments received, and 

- d) include the observations of the secretariat of the committee on each of the comments submitted. 

**41** 

© ISO/IEC 2026 – All rights reserved 

Every attempt shall be made to resolve negative votes. 

If, within eight weeks from the date of dispatch, two or more P-members disagree with the decision of the Chair, the draft shall be discussed at a meeting (see Clause 5). 

Committees are required to respond to all comments received. 

## ISO/IEC Directives Part 1, 2.7.2

- **2.7.2** Votes submitted by National Bodies shall be explicit: positive, negative, or abstention. 

A National Body may submit comments on any FDIS vote. 

If a National Body finds a final draft International Standard unacceptable, it shall vote negatively and state the reasons by submitting comments of a technical nature. It shall not cast a positive vote that is conditional on the acceptance of modifications. 

In the case where a National Body has voted negatively and has submitted comments that are not clearly of a technical nature, the Secretary/Committee Manager shall contact the National Body within two weeks of the ballot closure. If the committee leadership and the National Body do not find an agreement, the matter is escalated to the technical management board via the Office of the CEO. 

## ISO/IEC Directives Part 1, 2.7.3

**2.7.3** A final draft International Standard having been circulated for voting, is approved if 

a) a two-thirds majority of the votes cast by the P-members are positive, and 

b) not more than one-quarter of the total number of votes cast are negative. 

Abstentions are excluded when the votes are counted, as well as negative votes not accompanied by any comments of a technical nature. 

## ISO/IEC Directives Part 1, 2.7.4

**2.7.4** The Secretary/Committee Manager has the responsibility to bring any errors that may have been introduced in the preparation of the draft to the attention of the Office of the CEO by the end of the voting period; further editorial or technical changes are not accepted at this stage. 

**42** 

© ISO/IEC 2026 – All rights reserved 

## ISO/IEC Directives Part 1, 2.7.5

**2.7.5** All comments received will be retained for the next review and will be recorded on the voting form as "noted for future consideration". The Office of the CEO shall electronically archive these comments. However, the Secretary/Committee Manager, along with the Office of the CEO, may seek to resolve obvious editorial errors. Technical changes to an approved FDIS are not allowed. 

At the end of the voting period, the result of voting, indicating either the formal approval by National Bodies to issue the International Standard or formal rejection of the final draft International Standard, is available to all National Bodies. 

## ISO/IEC Directives Part 1, 2.7.6

**2.7.6** If the final draft International Standard has been approved in accordance with the conditions of 2.7.3, it shall proceed to the publication stage (see 2.8). 

## ISO/IEC Directives Part 1, 2.7.7

**2.7.7** If the final draft International Standard is not approved in accordance with the conditions in 2.7.3, the document shall be referred back to the committee concerned for reconsideration in light of the technical reasons submitted in support of the negative votes. 

The committee shall decide to: 

- resubmit a modified draft as a committee draft, enquiry draft or final draft International Standard; or 

- publish a Technical Specification (see 3.1); or 

- cancel the project. 

## ISO/IEC Directives Part 1, 3.1

###### **3.1 Technical Specifications (TS)** 

- **3.1.1** A committee may decide to prepare and publish a Technical Specification when: 

- the subject in question is still under development, or 

- the committee has developed a document it wishes to publish as specified in 2.6.4 and 2.7.7. 

A Technical Specification may contain normative provisions. 

**3.1.2** The committee may decide for new projects to follow the procedure set out in 2.3 to initiate the development of a Technical Specification. The required stages for the preparation of a Technical Specification shall be the preparatory stage as set out in 2.4 and the approval stage for publication (eight-week DTS (draft Technical Specification) ballot). The DTS shall be accompanied by a completed gender responsive standards (GRS) declaration form [3], [4]. 

Committees may also choose to use an optional committee stage as set out in 2.5. 

The decision to publish the resulting document as a Technical Specification shall require a two-thirds majority vote of the P-members voting. If technical changes are required following the ballot, a subsequent ballot is required to approve the revised draft. 

Abstentions are excluded when the votes are counted, as well as negative votes not accompanied by any comments of a technical nature. 

**3.1.3** When the P-members of a committee have agreed upon the publication of a Technical Specification, the draft specification shall be submitted electronically by the secretariat of the committee to the Office of the CEO within 16 weeks for publication. Competing Technical Specifications offering different technical solutions are possible, provided that they do not conflict with existing International Standards. 

The stability date (4.2) shall be provided on the cover page of the DTS. 

## ISO/IEC Directives Part 1, 5.3.1

###### **5.3.1 General** 

Committee and working group meetings may be held face-to-face or virtually (see 5.1). The meeting type shall be decided by the committee or working group leaders before registration and shall be clearly stated in the meeting notice. 

**53** 

© ISO/IEC 2026 – All rights reserved 

The host coordinates with the committee Chair and the Secretary/Committee Manager or the working group Convenor about the organization of the meetings, as appropriate. The Office of the CEO shall be informed accordingly. The host shall provide clear logistical information, including the accessibility of the meeting facilities, and shall provide invitation letters upon request. Participants may indicate specific accessibility needs, and the host shall make reasonable efforts to accommodate them. 

Meetings should, as a general rule, be organized in locations where entry restrictions or other constraints do not significantly limit the ability of participants to attend. 

Meetings hosts shall not charge participants any sort of participation fee, nor require accommodation at specific hotels or hotel rates for any meetings. The basic meeting facilities shall be funded entirely by resources from a National Body or voluntary sponsors. 

Large meetings can be expensive or complicated to stage and support, and the resource requirements may exceed those that the host can provide. It is, therefore, acceptable for a meeting to have one or more sponsors contributing to its organization and cost. Nevertheless, while it is acceptable for sponsors to be identified, and for their support to be recognized in the meeting, a meeting shall not be used as an opportunity for the promotion for commercial or other reasons of the products or services of any sponsor. 

## ISO/IEC Directives Part 1, 5.4

###### **5.4 Distribution of documents** 

The Secretary/Committee Manager or Project Leader/Convenor is responsible for ensuring that documents are distributed on time and for planning ahead to meet the applicable deadlines. 

The document distribution deadlines for both committee and working group meetings are set out in Table 3. These deadlines represent minimum timeframes, and general practical considerations (for example, visa issuance and travel arrangements) shall be taken into account when planning and organizing meetings. 

**Table 3 – Document distribution minimum deadlines** 

|**Committee meetings**|||
|---|---|---|
|**Document**|**Face-to-face**|**Virtual**|
|Calling notice and meeting logistics|16 weeks before the meeting|8 weeks before the meeting|
|Draft agenda|16 weeks before the meeting|8 weeks before the meeting|
|Proposals for new agenda items,<br>documents for decision, or<br>contributions|6 weeks before the meeting|6 weeks before the meeting|
|Final draft agenda|4 weeks before the meeting|4 weeks before the meeting|
|Decisions|48 hours after the meeting|48 hours after the meeting|
|Meeting report/minutes|4 weeks after the meeting|4 weeks after the meeting|
|**Working group and other committe**|**e subgroup meetings**||
|**Document**|**Face-to-face**|**Virtual**|
|Calling notice and meeting logistics|6 weeks before the meeting|4 weeks before the meeting|
|Draft agenda|6 weeks before the meeting|4 weeks before the meeting|
|Proposals for new agenda items,<br>documents for consultation, or<br>contributions|3 weeks before the meeting|3 weeks before the meeting|
|Final draft agenda|2 weeks before the meeting|2 weeks before the meeting|
|Meeting report/minutes|4 weeks after the meeting|4 weeks after the meeting|



A committee, a working group or a committee subgroup may consider content, take decisions or make recommendations on matters for which documents were not distributed within the applicable deadlines. In such cases, the leadership shall ensure that all P-members or Experts present agree to proceed and are prepared to take such decisions or make recommendations. 

Ad hoc groups are exempt from the deadline requirements set out in Table 3 and may organize themselves as needed, with appropriate flexibility. 

Successive meetings operating from the same agenda (i.e. comments resolution on the same document) are also exempt from these deadline requirements. 

## ISO/IEC Directives Part 1, 5.5

###### **5.5 Documenting decisions and meeting report/minutes** 

At the start of a meeting, a small drafting group may be created to help prepare and review the decisions and recommendations. Where possible, it should include at least one meeting participant fluent in English. 

**55** 

© ISO/IEC 2026 – All rights reserved 

The Secretary/Committee Manager or Project Leader/Convenor shall ensure that meeting outcomes are properly documented and shared. Decisions shall be distributed within 48 hours after the meeting, and the meeting report/minutes shall be distributed within four weeks. 

If no comments are received within four weeks after distribution, the meeting report/minutes is considered approved. If comments are received, they shall be addressed by the Secretary/Committee Manager or Convenor. If objections are received, the meeting report/minutes remains unconfirmed until the next meeting, and any approved changes are recorded in the meeting report/minutes of that next meeting. 

## ISO/IEC Directives Part 1, 5.6

###### **5.6 Recording of meetings** 

Meetings may only be recorded or transcribed by the Secretary/Committee Manager and only if all participants are informed at the start of the meeting and no one objects. Any participant may ask for the recording or transcription to be switched off during their intervention. 

Recordings and transcripts may only be used to support the preparation of the meeting report/minutes or to clarify what was said. 

Recordings and transcripts remain in the custody of the Secretary/Committee Manager, shall be treated as confidential, shall not be shared with third parties, and shall be destroyed once the reports/minutes are approved. 

Authorized artificial intelligence (AI) tools may be used to support the preparation of the report/minutes under the same conditions as recordings (refer to ISO Guidance [14] and IEC Guidance [15]). 

For subgroup meetings (such as working groups, advisory groups, editing groups or ad hoc groups), recordings and transcripts may be made under the same conditions by the Convenor, Secretary/Committee Manager, Project Leader, Project Editor or other designated individual. 

## ISO/IEC Directives Part 1, 5.7

###### **5.7 Media at meetings** 

Media representatives shall not attend any meetings, e.g. committee meetings, working group meetings. 

Participants shall not comment publicly on the discussions, positions, or contributions made by others during meetings. 

Only the meeting leadership may speak publicly on the consensus reached, and only in the context of an official press activity linked to the meeting. 

All official press releases are prepared and issued by the Office of the CEO, which retains the final decision on their content. 

**56** 

© ISO/IEC 2026 – All rights reserved 

## ISO/IEC Directives Part 1, 6.1

###### **6.1 General** 

- **6.1.1** National Bodies have the right of appeal 

- a) to the parent technical committee on a decision of a subcommittee; 

- b) to the technical management board on a decision of a technical committee; 

- c) to the council board on a decision of the technical management board, 

within eight weeks of the decision in question. 

The decision of the council board on any case of appeal is final. 

**6.1.2** A P-member of a committee may appeal against any action, or inaction, on the part of the committee, when the P-member considers that such action or inaction is 

- a) not in accordance with 

   - the Statutes and Rules of Procedure [16], [17]; 

   - the ISO/IEC Directives; or 

- b) not in the best interests of international trade and commerce, or such public factors as safety, health or environment. 

**6.1.3** Matters under appeal may be either technical or administrative in nature. 

Appeals on decisions concerning new work item proposals, committee drafts, enquiry drafts and final draft International Standards are only eligible for consideration if 

- questions of principle are involved, or 

- the contents of a draft may be detrimental to the reputation of ISO or IEC. 

- **6.1.4** All appeals shall be fully documented to support the P-member's concern. 

## ISO/IEC Directives Part 1, 6.2

###### **6.2 Appeal against a subcommittee decision** 

**6.2.1** The documented appeal shall be submitted by the P-member to the secretariat of the parent technical committee, with a copy to the Chief Executive Officer. 

**6.2.2** Upon receipt, the secretariat of the parent technical committee shall advise all its P-members of the appeal and take immediate action, by correspondence or at a meeting, to consider and decide on the appeal, consulting the Chief Executive Officer in the process. 

**6.2.3** If the technical committee supports its subcommittee, then the P-member which initiated the appeal may either 

**57** 

© ISO/IEC 2026 – All rights reserved 

- accept the technical committee's decision, or 

- appeal against it. 

## ISO/IEC Directives Part 1, 6.3

###### **6.3 Appeal against a technical committee decision** 

- **6.3.1** Appeals against a technical committee decision may be of two kinds: 

- an appeal arising out of 6.2.3, or 

- an appeal against an original decision of a technical committee. 

**6.3.2** The documented appeal shall, in all cases, be submitted to the Chief Executive Officer, with a copy to the Chair and secretariat of the technical committee. 

**6.3.3** The Chief Executive Officer shall, following whatever consultations they deem appropriate, refer the appeal together with their comments to the technical management board within four weeks after receipt of the appeal. 

The technical management board shall address the appeal at its next meeting. Meetings to address the appeal shall invite representatives of the parties to the appeal to make their arguments virtually. The technical management board shall ensure that all parties are treated equally. 

## ISO/IEC Directives Part 1, 6.4

###### **6.4 Appeal against a technical management board decision** 

An appeal against a decision of the technical management board shall be submitted to the Chief Executive Officer with full documentation on all stages of the case. 

The Chief Executive Officer shall refer the appeal together with their comments to the members of the council board within four weeks after receipt of the appeal. 

The council board shall make its decision within 12 weeks. 

## ISO/IEC Directives Part 1, 6.5

###### **6.5 Progress of work during an appeal process** 

When an appeal is against a decision relating to work in progress, the work shall be continued up to and including the approval stage (see 2.7). 

**58** 

© ISO/IEC 2026 – All rights reserved 
