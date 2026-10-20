# Findings check for draft 3 of the findings-first body

Draft 3 was written from the proof as it stands at the start of review round 3 (foundation and chapters 2 to 12 as of the round 2 fixes). Draft 2 was written from the `step-11` snapshot (11:16 on 2026-10-19), so every comparison with draft 2 below is between that snapshot and the current files. No proof file, plan, ledger, or kit was changed.

## Verdicts at a glance

All nine findings pass after the fixes listed under each one. No finding was cut. One wording was narrowed because the current proof no longer supports draft 2's phrasing (finding 8, "costs nothing the rules impose"), and several sentences were narrowed to the current keys where draft 2 overclaimed against them (listed under "Weakenings the current proof forces").

1. Better Is Not Enough (priority 1): PASS after 1 fix.
2. Every Design Needs More Than Merit (priority 1): PASS after 5 fixes.
3. Doubt Stays Out of the Count (priority 1): PASS.
4. No User Votes (priority 2): PASS after 1 fix (quote punctuation).
5. Whoever Is Present Decides, and Presence Can Be Paid For (priority 3): PASS after 1 fix.
6. SD-4 Assigns No One to Rule on Whether a Design Is Good (priority 4): PASS.
7. No Step Checks That Separately Adopted Designs Work Together (priority 4): PASS after 1 fix.
8. What No Reviewer Raises, the Author Need Not Say (priority 5): PASS, with one wording narrowed from draft 2.
9. The Smallest Part That Fixes the Structure Goes First (priority 6): PASS after 1 fix.

Mechanical checks on the draft: all 23 quoted spans appear word for word in the proof (script check against the foundation and chapters); no em dash, en dash, or double dash; no markdown table; no YAML frontmatter; no staging path; no forbidden word from `proof-style` outside quotations (the scan's only hits were "skill", "bodies", and the proof's own "judge" for voters and "judging" for a sustained opposition). Length: about 6,220 words, of which about 4,490 are the thesis and findings.

## Decisions taken for the user

The user has not ruled on these. Each is logged with its reason.

1. **No case histories in the body.** The proof's sealed-history rule keeps WG21 events out, and the body does not lean on them. A companion paper that works three cases against the chapter 12 predictions, with public sources, is the place for them; each prediction already names its evidence, what would count against it, and the data that would tell it apart from another explanation.
2. **EWGI and LEWGI are named** in finding 2 as examples of study groups that incubate proposals, though the proof items (`p:newcomer`, `p:small-position`) do not name them and word the point conditionally ("Where a study group incubates proposals on its topic").
3. **No person and no WG21 paper other than SD-4 is named**, and no meeting, poll result, or feature history is used as support. The box says so.
4. **Nine findings, not eight.** Draft 2's finding 8 joined disclosure and the first-part strategy. The user's priorities list them separately (5 and 6), and each now has a full Theorem clause, so draft 3 gives each its own finding. Cost: about 400 words. Confidence: medium, since "about eight" allows nine and the split follows the priority order.
5. **"What would show this wrong" lines kept**, as in draft 2, and rewritten to the current chapter 12 corollaries, which now name another explanation and the data to tell them apart. Finding 2 has no corollary that tests `p:fluency` directly, so its first falsifier is the axiom it rests on (`ax:learning`), and its second is `c:pred-small-fade`.
6. **The box is a blockquote** with three bold parts (assumptions, scope, what the proof does not claim), since the body may not use a table.
7. **INCITS note added to the box.** The thesis says the results use only SD-4, a few ISO clauses, and assumptions. The proof also quotes INCITS's procedures for how the United States forms its national position (`p:nb-members`). No finding in the body cites `p:nb-members`, but `l:settled-sponsor` and `l:settled-nb` list it in their bases, so the Theorem's citation chain reaches it. The box now states this in one sentence so the thesis stays true as written.
8. **Draft 2's "costs nothing the rules impose" narrowed** to the Theorem's own words, "costs no step the rules require before adoption" (finding 8). Reason under finding 8. This is not a return to the old "costs no votes"; the sentence still says stating a drawback can cost votes.
9. **Draft 2's "SD-4 sets no limit on how many voters one sponsor pays for" raised** to "No rule limits how many voters one sponsor pays for", since `l:thm-deciders` and `p:sponsor-votes` now say that and `d:rules` makes "rule" cover SD-4 and the quoted ISO clauses. The older overclaim, "add voters without limit", is not reintroduced.
10. **Length.** Draft 3 adds the stability page and the box, which draft 2 lacked, and gives each finding its mechanism, consequence, quoted rule, falsifier, and keys. If the user wants it shorter, the first cuts I would make are the list of choices on the stability page (it repeats the findings) and the second paragraph of findings 2 and 6. Confidence: medium, since the plan's 10 to 12 pages allows this length but draft 2 was much shorter.

## Each user priority, tested against the proof

1. **Procedural momentum and fluency let a determined author pass the content-settling stages with little review.** Supported in this form: a design's content can be fixed when it is least reviewed (`l:thm-fixed-early`); a design-bound author does best seeking direction polls as early as they can pass (`l:bound-early`); objectors short of a third cannot force a change with their votes (`inf:thm-early-unchanged`); other things equal, six factors that are not design quality make a proposal advance more readily (`l:thm-readily`); and a proposal costing more to read than most stakes in it can advance with no change at all (`l:thm-holding`). Not supported: any amount of review ("little review"). The draft says "least reviewed" and "with no change at all" instead. Findings 1, 2, and 3.
2. **Users are left out of the decisions.** Supported: no user votes in any WG21 poll or ballot (`p:who-votes`), users' interests reach decisions only through four channels (`p:users-out`), and the needs that reach a vote are those participants and sponsors know (`l:thm-deciders`). Finding 4.
3. **What the incentives reward, and who decides what goes in.** Supported: the participants present decide content, each participant a sponsor pays has a vote and values its interests, and no rule limits how many voters one sponsor pays for (`p:who-decides`, `p:sponsor-votes`, `l:thm-deciders`); authors get adoption at the poll while a later flaw's cost can fall on any user (`p:reward-timing`); merit enters only through what participants value and what informs their votes (`l:thm-merit`). Findings 4, 5, and 6.
4. **Quality control and integration.** Supported: SD-4 assigns no one to rule on quality and its consensus test never asks whether an objection is right (`f:no-merit-ruling`, `l:consensus-test`); no SD-4 step checks that separately adopted designs work together, and review worth its cost to users together but not to one participant goes undone in the pattern (`l:thm-gaps`). Findings 6 and 7.
5. **Undisclosed trade-offs.** Supported: the rules ask no author for drawbacks, a paper is considered without them, stating one can cost Favor votes, and leaving it out costs no step the rules require before adoption (`l:thm-disclosure`, `p:disclosure`); in the table's case the two author types choose oppositely (`t:disclose`). Finding 8.
6. **The minimal first part.** Supported: a design-bound author does best proposing first the smallest part that fixes the structure and can pass, and every rival to that structure must then replace it (`p:first-part`, `l:thm-first-part`); the limit is opponents who foresee the rest (`l:first-part-oppose`). Finding 9.

## Where the current proof is stronger than draft 2

Each item compares the `step-11` snapshot, which draft 2 used, with the current files.

1. **The Theorem's sponsor claim now matches its proposition.** In `step-11`, `p:sponsor-votes` already said neither SD-4 nor the searched ISO clauses limit how many participants a sponsor pays, but the Theorem said "a sponsor can add voters without limit", which draft 2 corrected to "SD-4 sets no limit". Now `l:thm-deciders` says "no rule limits how many voters one sponsor pays for", and `d:rules` (new) defines "rule" as SD-4 plus the quoted ISO clauses. Draft 3 states that wider claim (thesis, finding 5).
2. **Paid voters value the sponsor's interests.** `p:sponsor-votes` and `p:sg-sponsor` now say each participant a sponsor pays "values its interests" (from `ax:prefer`), not only that the sponsor "adds a voter". `l:settled-sponsor` now adds "Each such participant votes valuing its interests, and no rule limits how many it pays" (finding 5).
3. **Drawbacks absence covers the ISO clauses.** `f:no-drawbacks-asked` searched SD-4 only in `step-11`; it now covers the quoted ISO clauses too, with more search terms. Draft 3 says "Neither SD-4 nor the quoted ISO clauses ask a paper or its author to state the design's drawbacks" (finding 8).
4. **The Theorem now covers the choices it leaves open.** `l:thm-pattern` in `step-11` concluded the pattern from the named choices alone; it now adds that each choice the Theorem leaves open is made the way that does best given the others' choices. The box states this scope once.
5. **Interest statement covers the ISO clauses.** `f:no-interest-statement` now covers the quoted ISO clauses, so no rule asks who pays an author or what interests the author or a sponsor has (finding 8).
6. **No-ruling absence searched more widely.** `f:no-merit-ruling` now also searched "opinion, select, pursu", so the direction group's opinion role was checked and still no one rules. The box says the direction group gives opinions but no one rules (finding 6, box).
7. **The 2:1 norm is a stated threshold.** `d:follows-norm` (new) removed "normally" from `p:burden-flip`, so "removing it takes a paper or ballot comment that itself meets the 2:1 norm" now holds plainly (finding 1).
8. **Objectors short of a third cannot force a change.** New in the Theorem (`inf:thm-early-unchanged`). Draft 3 states it in finding 1.
9. **Reversal also costs other papers' meeting time.** `ax:rework` now says reversal "takes meeting time from other papers" (finding 1).
10. **Favor's safety is now an axiom.** `ax:support` now says a Favor vote, or one the colleague cannot attribute, gives no reason for less ready support. In `step-11` the axiom covered only Neutral and not voting, though `l:favor-no-risk` already stated the result. Draft 3 uses it: no vote costs a regular less than Favor (finding 3, box).
11. **Chair's gain from departing is bounded.** `ax:post-risk` (new) and the rewritten `p:chair-default`: a chair gains from departing at most their stake and cannot rule out added risk to their post (stability page).
12. **Written-answer absence covers the ISO clauses.** `f:iso-no-answer` (new) says that apart from 2.6.5's response to enquiry comments, no listed ISO clause requires a written answer to a working group or ballot objection (finding 6, via `p:record-indistinct`).
13. **Predictions with tests that tell explanations apart.** `c:pred-rival-polls`, `c:pred-removals`, `c:pred-abstention-length`, `c:pred-sponsor-against`, `c:pred-defects`, and `c:pred-first-part` were rewritten, each naming another explanation and the data that would tell the two apart.
14. **Levers rewritten.** `c:lever-reasons-all` now also predicts fewer Favor votes on doubted proposals, `c:lever-nb-less` now says the ballot vote would be a national body's only move counting directly toward stopping a document, `c:lever-nb-more` is narrowed to objections backed by bodies whose No votes could fail a ballot, and `c:lever-sponsor-limit` now predicts margins by who pays the authors, not "large versus small proposals".

### Sharper wording of the same claim

- `p:challenger-bar` and `inf:thm-incumbent-edge`: "An incumbent needs no advantage to stay" (was "faces no reversal hurdle"). Draft 3 puts it in finding 1's claim.
- `p:least-cost-response`: "The count measures votes, not whether the objectors are right." Draft 3 uses it in finding 6. It replaced a sentence draft 2 relied on (see the weakenings below).
- `p:fluency`: "Every design needs more than merit to be considered" (was "No design is considered on merit alone"). Finding 2's title and claim.

### Already in the `step-11` proof, used for the first time in draft 3

- `inf:thm-no-request`: "SD-4 never uses the word trade-off." Finding 8's opening line.
- `l:favor-no-risk` and `inf:favor-cost`: no vote costs a regular less than Favor (finding 3).
- `l:convenor-weightless`: when all opposition is unescalated and holds no national position, SD-4's procedure has the convenor declare consensus (finding 2).
- `l:thm-readily`: the six things that, other things equal, make a proposal advance more readily (finding 2).
- `p:objector-coordination`: the same objectors can settle on blocking or on none voting Against (stability page).
- `c:pred-small-fade`, `c:pred-parts`, `c:pred-written-answers`, `c:pred-competing` (findings 2, 9, 6, 7), and the levers `c:lever-reasons-all` and `c:lever-nb-less`, which draft 2 did not list.

## Weakenings the current proof forces

These are draft 2 sentences whose wording now claims more than the current keys. Draft 3 uses the key's wording. None of these removes a finding.

1. Draft 2: "learning whether they are right changes nothing in the count." Now `p:least-cost-response` says "The count measures votes, not whether the objectors are right", because learning can change votes (`ax:attention`). Draft 3 uses the new sentence (finding 6).
2. Draft 2: "users pay for any flaw found later." Now `p:reward-timing`: a flaw "costs them [authors] only later and in part, and its cost can fall on any user of the feature." Draft 3: "its cost can fall on any user" (findings 4 and 8).
3. Draft 2: "A user can become a participant but pays the full price alone." Now `l:settled-user` is about "a user without a sponsor". Draft 3 narrows the subject.
4. Draft 2: "both refrain." Now `p:mutual-support`: "each does better refraining whatever the other does." Draft 3 uses that.
5. Draft 2: "the first holds and the second yields." Now `p:attrition`: "the first does better holding and the second yielding", in the table's case. Draft 3 uses that, and adds the caption's condition that the sponsors value the group's holding above what they pay.
6. Draft 2: "Objections count only in forms and by deadlines that attending teaches." Now `l:thm-objections`: "some of how the committee applies these rules is learned only by attending." Draft 3 says how the committee applies the rules is learned partly by attending, some only that way.
7. Draft 2: "only Against voters can be asked for reasons." Now `p:against-costs-more`: "SD-4 tells only Against voters to be ready to give reasons." Draft 3 uses that.
8. Draft 2: "An objection not escalated on the email lists and in the objector's national body by 5pm the evening before the closing plenary counts for nothing there." Now `p:late-objection`: escalated "during the week, on the email lists by 5pm the evening before and within their national body", and SD-4 says such objections "should not be given weight". Draft 3 follows both.
9. Draft 2: "omitting them costs nothing the rules impose." Now `l:thm-disclosure` and `inf:omit-free`: "costs ... no step the rules require before adoption", and `inf:omit-exposure` adds that a left-out trade-off can surface later and reopen the matter. Draft 3 uses the key's words and keeps "can cost Favor votes" for stating one.
10. Draft 2: "Users can inherit a structure voted on before anyone could study what it must support." Now `p:first-part` and `l:first-part-foresight`: "before reviewers can study in detail", and reviewers who foresee the rest can base their vote on it. Draft 3 uses "study in detail" and names the foreseeing reviewers.
11. Draft 2: "Otherwise the public record shows its holders as a number in a tally." Minutes are kept by whoever takes them (`l:minutes-others`), so the public record can hold more than a number. Draft 3 says what `l:records-protected` proves: from the protected records of subgroup discussion, SD-4 allows public quotation only of the poll question, its numbers, and words a person consents to have attributed.
12. Draft 2's thesis: "no one is assigned to judge whether it is good." Now "rule on", per the scope the user set and `f:no-merit-ruling`.
13. Draft 2's thesis: "the side whose costs are paid can hold longest." Now `l:thm-holding`: "the group whose sponsors keep paying its costs". Draft 3 says "keep paying" (thesis, finding 5).
14. Draft 2: "the author tied to particular features seeks the IS unless the design room requires a TS." Now `l:bound-vehicle`: "does best asking the design room for the IS where it can pass." Draft 3 uses that and says the room can still require a TS or white paper.

## Finding-by-finding check

Each finding lists the keys its sentences rest on, with each key's current statement quoted from the proof (the item's kind label and basis dropped), then a sentence check, the verdict, and what changed from draft 2.

### Finding 1. Better Is Not Enough (priority 1)

Keys:

- `p:early-polls`: "A design can become the incumbent at its first direction poll, when it has had less review than at any later meeting. From then on, a rival or a later change must redo or discard work built on it, at a cost that grows as more is built."
- `l:first-meeting-poll`: "When a proposal is first presented to the committee in a design room, the chair may take a direction poll on it at that meeting."
- `l:poll-wording`: "A direction poll asks voters only to agree that work should continue, less than a forwarding poll asks, so it can pass where a forwarding poll would fail. Passing it in a design room makes the design the incumbent."
- `l:direction-asks-less`: "A participant who would vote Favor on sending a design to the next room prefers that work on it continue rather than stop. One who doubts the design as it stands can prefer that too, since the room can direct changes."
- `ind:reversal-grows`: "Each decision built on a design adds work that reversing the design would redo or discard, and more is built after each favorable poll. So the cost of reversing a design grows as it advances, whether or not the design is wrong."
- `p:challenger-bar`: "A rival wins a voter from an incumbent only with an advantage worth more to that voter than their share of the reversal's cost. The advantage a rival needs grows with each decision built on the incumbent, while keeping the incumbent needs none."
- `inf:thm-incumbent-edge`: "An incumbent needs no advantage to stay, while a rival wins a voter from it only with an advantage worth more than that voter's share of the reversal's cost."
- `p:burden-flip`: "A design needs the 2:1 norm to advance, and once adopted, a paper or ballot comment to remove it needs the same, switching the default to keeping it. After a successful final ballot, design changes are expected to have near-unanimous consent, ISO bars technical changes at approval, and SD-4 calls published features much harder to update incompatibly."
- `l:settled-design-bound`: "Whatever the others choose, a design-bound author does best seeking early direction polls, the smallest first part fixing its features, and the IS, each as far as it can pass. It does best leaving out a trade-off no reviewer would raise when stating it costs more than later exposure, and answering objections with the cheapest change that keeps it passing."
- `l:bound-early`: "A design-bound author does best seeking direction polls as early as they can pass."
- `l:thm-fixed-early`: "In this pattern a design's content can be fixed when it is least reviewed. Every later rival or change must then redo work built on it, at a cost that grows whether or not the design is wrong."
- `inf:thm-early-unchanged`: "With objectors short of a third of the Favor-plus-Against votes, the design meets the 2:1 norm unchanged, so their votes cannot force a change. The cheapest change a design-bound author then needs to keep it passing in the room is none, unless the room directs one."
- `ax:rework`: "Reversing a decision, or changing a design after work is built on it, means redoing or discarding that work, which costs its builders and takes meeting time from other papers. After a favorable poll, authors and others build more on the design, such as wording, implementations, and proposals that depend on it."
- `d:design-bound`: "A design-bound author is one whose gain from a proposal depends on the adopted design keeping particular features fixed before review, for example because a sponsor's interests depend on them."
- `c:pred-rival-polls`: "The model predicts that once a design passes a design room's direction poll, a like rival draws less support than before in polls of the same form. Equal support would count against it, and comparing only polls between which the incumbent's content and review time did not change would tell it apart from learning or improvement."
- `c:pred-removals`: "The model predicts rare removals after adoption, likelier when national bodies whose No votes could fail a ballot oppose the design, and frequent narrow-margin removals would count against it. Another explanation is that adopted designs rarely need removal, and the share of failed removal polls with more Favor than Against votes would tell them apart."

Sentence check:

- Claim ("can become the incumbent while it is least reviewed"; "a rival wins a voter only with an advantage worth more ... than their share"; "the incumbent needs no advantage to stay"): `l:thm-fixed-early`, `p:early-polls`, `p:challenger-bar`, `inf:thm-incumbent-edge`. Holds at the keys' strength ("can").
- Direction poll asks less and can pass where a forwarding poll would fail, and a doubter can prefer that work continue: `l:poll-wording`, `l:direction-asks-less`.
- The chair may take it at the first meeting: `l:first-meeting-poll`.
- Design-bound author does best seeking it as early as it can pass: `l:bound-early`, `d:design-bound`.
- Reversal redoes wording, implementations, and dependent proposals, costs builders and other papers' meeting time, grows whether or not the design is wrong: `ax:rework`, `ind:reversal-grows`.
- Objectors short of a third cannot force a change "with their votes": `inf:thm-early-unchanged`, under `d:follows-norm` (box).
- Removal needs a paper or ballot comment meeting the 2:1 norm; default switched: `p:burden-flip`.
- "cast in stone": quoted from `f:is-hard-to-change`, which `p:burden-flip` cites.

Verdict: PASS. Fix made while drafting: "cannot force a change" became "cannot force a change with their votes", since `inf:thm-early-unchanged` leaves room for a change the room directs.

Changes from draft 2: the claim now uses the Theorem's lines; "Once adopted, it stays unless a removal meets the 2:1 norm" became "removing it takes a paper or ballot comment that itself meets the 2:1 norm", which is what `p:burden-flip` says and does not claim there is no other route; added the first-meeting poll, the meeting-time cost, and the one-third line; the falsifiers follow the rewritten corollaries.

### Finding 2. Every Design Needs More Than Merit (priority 1)

Keys:

- `p:fluency`: "Every design needs more than merit to be considered: a proposal needs an on-time paper and a presenter, a rival a paper to exist, and objections fixed forms and times. Participants learn how the committee applies them partly, and some only, by attending, and other things equal, whoever knows more has the better chance of adoption, whatever their design skill."
- `p:late-objection`: "SD-4 gives an objection weight at plenary only if its holder escalated it during the week, on the email lists by 5pm the evening before and within their national body. There, by default, it is not a national position, and after the deadline even new information goes to the email lists or a ballot comment, with a discussion paper."
- `l:convenor-weightless`: "When all opposition rests on objections not escalated in time and holds no national position, SD-4's plenary procedure has the convenor declare consensus."
- `l:thm-readily`: "Other things equal, a proposal advances more readily when its authors keep presenting it or know the procedures, or when a sponsor pays for participants who hold its position. The same holds when the chair expects fewer problems from it, a poll has placed it among the work aimed at the next edition, or it is already the incumbent."
- `p:chair-confidence`: "Of two papers otherwise alike, a chair does better taking up first the one whose author's record of following procedures and responding to review makes them expect fewer problems. That record comes from taking part, which SD-4 expects of an author: presenting the proposal, answering questions, and making the changes the room directs."
- `p:roadmap-poll`: "If a poll places a proposal among the work the committee aims to include in the next edition, the proposal joins a category SD-4 has chairs take up first. A meeting's hours are fixed, so the time it then gets comes out of the time left for papers outside those categories."
- `p:newcomer`: "Other things equal, a newcomer, lacking what earlier meetings teach, spends more effort getting a paper considered than a returning participant, and SD-4 expects everyone to know its procedures. Where a study group incubates proposals on its topic, a newcomer's early proposal can start there."
- `l:settled-small-author`: "Whatever the others choose, a small proposal's author does best keeping it presented while its chance of adoption outweighs the cost, borne alone, of the meetings still ahead. The longer it must still wait behind priority work, the more those costs come to, and once they outweigh its chance, the author does best letting it stop."
- `inf:thm-sizes-small`: "Of a small proposal's defining attributes, its author's best choice rests only on paying their own costs, so it holds for any proposal whose author does."
- `ax:learning`: "A participant learns how the committee works partly by attending, some of it only that way, and this knowledge differs from skill at design. Participants can use only procedural options they know, and, other things equal, those who know more spend less effort getting a paper considered and have a better chance of adoption."
- `c:pred-small-fade`: "Per meeting spent waiting behind priority work, the model predicts more stops without a negative poll for self-funded authors' proposals than for sponsored authors' proposals of similar length. No such difference would count against it, and stops rising once a waiting proposal's author loses their sponsor would tell it apart from another explanation, dropping on reflection."

Sentence check:

- Claim: `p:fluency`, word for word in substance, with "other things equal" kept.
- Paper and presenter, paperless rival "does not exist", objection only as a vote in the room: `p:fluency` and its children (`l:paper-and-presenter`, `l:rival-needs-paper`, `l:objection-forms`); the quote is from `f:no-wait-alternatives`.
- Plenary weight only if escalated during the week, on the lists by 5pm the evening before and within the national body: `p:late-objection`.
- Convenor declares consensus when all opposition is unescalated and holds no national position: `l:convenor-weightless`.
- Six factors make a proposal advance more readily, other things equal: `l:thm-readily`.
- Chair takes up first the paper whose author has the record: `p:chair-confidence`, with `ax:repeat` giving the chair's expectation.
- A priority paper's time comes out of the time left for the rest: `p:roadmap-poll`.
- Newcomer spends more effort, other things equal; study group start: `p:newcomer`. EWGI and LEWGI named under decision 2.
- Self-funded author bears each meeting alone and does best letting the proposal stop once costs outweigh its chance: `l:settled-small-author`, extended to any self-funded author by `inf:thm-sizes-small`.

Verdict: PASS. Fixes made while drafting: (1) "Holding the design fixed" became "Other things equal", since `l:thm-readily` holds everything else fixed, not only the design; (2) "Other things equal" restored in the newcomer sentence, per `p:newcomer`; (3) "Work from someone new ... starts with the lower chance, however good it is" became "starts with a lower chance than equally good work from someone who knows the procedures", since `p:fluency` compares otherwise equal work; (4) the convenor's description fixed to "WG21's convenor" (it "convenes", per `d:rooms`); (5) "other papers" became "the rest" of the papers outside the priority work, per `p:roadmap-poll`.

Changes from draft 2: positive-form claim; the deadline sentence fixed (see weakening 8); added the convenor's default, the six factors, and the self-funded author; falsifiers now `ax:learning` and `c:pred-small-fade`.

### Finding 3. Doubt Stays Out of the Count (priority 1)

Keys:

- `p:review-share`: "Close study takes longer the bigger a design is, and a bigger design has more places where a defect can go unnoticed. For a reviewer whose stake does not grow with size, close study therefore stops being worth its time sooner on a big design than on a small one."
- `p:light-review`: "Since those who skip a paper and its discussion typically abstain, those with large stakes cast most votes on a proposal costing more to read than most stakes in it. Unless those of them who object cast at least a third of the Favor-plus-Against votes, it can advance with no change at all."
- `p:least-cost-response`: "When an objection's Against votes are too few to keep the 2:1 norm unmet, the cheapest response keeping it met at that poll is no change or a partial change. The count measures votes, not whether the objectors are right, and SD-4 expects any change the room directs to be made or defended with new information."
- `p:against-costs-more`: "For a regular, an Against vote on a colleague's proposal costs more than a Neutral vote or none. It risks the colleague's later support at least as much, and SD-4 tells only Against voters to be ready to give reasons, which take time to prepare."
- `inf:favor-cost`: "Favor costs the regular no standing with the proposal's author and no time for reasons, so no other vote costs the regular less."
- `p:doubt-outside-count`: "On a colleague's proposal they doubt, a regular does better voting Against only when the change that vote can make outweighs the standing and time it costs. One Against vote changes the result only when the count is one or two votes above the 2:1 threshold, and it can also bring changes to the design."
- `p:mutual-support`: "Two regulars with pending proposals each risk the other's support for their own by opposing the other's proposal. If each one's doubt is worth less than that risk and the time for reasons, each does better refraining whatever the other does, and both do better than both opposing."
- `l:settled-regular`: "Whatever the others choose, a regular does best voting Favor on colleagues' proposals they support. On one they doubt, Against does best only when the change it can make outweighs the standing and time it costs, and otherwise Neutral, not voting, or Favor does best."
- `l:thm-holding`: "In a long deadlock, the group whose sponsors keep paying its costs can hold longest, whichever design is better. A proposal that costs more to read than most participants' stakes in it can advance with no change at all."
- `c:pred-abstention-length`: "Across revisions of one proposal polled in one room, the model predicts fewer votes cast, relative to other papers polled at the same meetings, as the paper grows longer. No fall would count against it, and since one proposal keeps its topic, the comparison sets aside another explanation, that longer papers cover narrower topics fewer participants know."
- `c:lever-anonymous`: "If design polls were anonymous, the standing part of an Against vote's cost would shrink for voters whom neither their words nor the count identify. The chair could no longer ask a particular Against voter for reasons, and the model predicts more Against votes on colleagues' proposals."

Sentence check:

- Claim: `p:light-review`, `l:thm-holding`, with the one-third condition in the sentence.
- Bigger designs take longer to study and hide more defects; study stops paying sooner for a reviewer whose stake does not grow: `p:review-share`. The condition is kept in both places it is used.
- Cheapest answer under a third is no change or a partial change: `p:least-cost-response`.
- A doubt enters the count only as Against; Against costs more; only Against voters told to be ready with reasons: `l:vote-count`, `p:against-costs-more`.
- No vote costs a regular less than Favor: `inf:favor-cost`.
- Against does better only when its change outweighs standing and time; one vote matters only one or two above the threshold: `p:doubt-outside-count`.
- Two regulars each do better refraining whatever the other does; "No agreement is needed" follows from "whatever the other does": `p:mutual-support`.
- Consequence ("pass unchanged while doubts that no Against vote recorded sit in the room"): `p:light-review` with `l:settled-regular`.

Verdict: PASS. No fix needed after drafting.

Changes from draft 2: see weakenings 4 and 7; added Favor's zero cost; the falsifier now uses revisions of one proposal (`c:pred-abstention-length`), not "proposals of similar stakes and breadth".

### Finding 4. No User Votes (priority 2)

Keys:

- `p:who-votes`: "Each person in a subgroup's room has one vote, guests a convenor invites included, while no user votes in any WG21 poll or in the ballots on its drafts."
- `l:traced-voters`: "Apart from guests, whose choices the proof takes as given, participants cast the votes in WG21's polls and national bodies cast those in the ballots on its drafts."
- `p:users-out`: "No user votes, and taking part costs the participant or their sponsor, while a better design's gain is spread across all users and seldom turns on one user's effort. Users' interests reach decisions only through what participants themselves value, papers a participant presents, TS feedback, and national bodies, which form positions only where that is worth their members' time."
- `p:who-takes-part`: "Fees are barred and meeting places should not significantly limit attendance, and only those who bear the cost of taking part, or whose sponsors do, vote in WG21's polls. ISO can remove inactive national body experts, and participants can propose only for needs they and their sponsors know, which need not match users', since users differ from them."
- `l:settled-user`: "Whatever the others choose, a user without a sponsor does best taking part only when their own stakes in its polls outweigh the full price, which they bear alone. Otherwise the best move is a cheaper one or none: TS feedback, a paper a participant presents, or a request to a national body."
- `p:reward-timing`: "Authors get the adoption they value at the poll. A flaw that implementation and use have not yet exposed costs them only later and in part, and its cost can fall on any user of the feature."
- `p:prefer-is`: "A TS delays IS adoption by about one to two years, and its experience can bring incompatible changes first: a gain to result-seeking authors, a risk to design-bound ones. It reaches implementers and users early, can publish while concerns remain if their holders agree, and the design room can require it or the white paper ISO and SC22 recommend."
- `l:bound-vehicle`: "A design-bound author does best asking the design room for the IS where it can pass."
- `l:thm-deciders`: "No user votes, and the needs that reach a vote are those participants and their sponsors know, which need not match those of users at large. The participants present decide content, and no rule limits how many voters one sponsor pays for."
- `c:pred-nb-positions`: "The model predicts that national bodies state positions on few proposals, and positions on most would count against it; vetted ballot comments, which count as national positions, are the evidence. Another explanation is that they agree with most proposals, and more positions from bodies whose experts attend in person, where forming one costs less, would tell them apart."
- `c:lever-ts-path`: "If a TS did not delay adoption compared with an edition, the author's cost of accepting a TS would fall. The model predicts more designs sent to a TS or white paper."

Sentence check:

- Claim: `p:who-votes`, `l:thm-deciders`.
- Who casts the votes, guests apart: `l:traced-voters`.
- Four channels for users' interests; national bodies form positions only where worth their members' time: `p:users-out`.
- Fees barred and access protected, yet only those who bear the cost, or whose sponsors do, vote; participants propose only for needs they and their sponsors know: `p:who-takes-part`.
- A user without a sponsor bears the full price alone; gain spread; one user's effort seldom matters: `l:settled-user`, `p:users-out`. The tautological "does best taking part only when its stakes outweigh the price" was left out of the body, which states the costs and gains instead.
- Adoption at the poll; a flaw costs authors later and in part and can fall on any user: `p:reward-timing`.
- TS quotes from `f:ts-experience` and `f:ts-feedback`; one-to-two-year delay, incompatible changes, gain and risk by author type, IS request, the room can require a TS or white paper: `p:prefer-is`, `l:bound-vehicle`.
- Consequence: `p:who-decides`, `p:who-takes-part`, `p:reward-timing`, `p:who-votes`.
- Rests on `f:in-person-expected`, which `p:who-takes-part` cites.

Verdict: PASS. Fix made while drafting: the commas and period after two quoted fragments were moved outside the quotation marks, so the quoted words match the source exactly.

Changes from draft 2: weakenings 2, 3, and 14; added the fee and access rules (a check, stated for fairness) and the TS's early reach.

### Finding 5. Whoever Is Present Decides, and Presence Can Be Paid For (priority 3)

Keys:

- `p:who-decides`: "The participants present decide a design's content: chairs call consensus on their votes, counted under the 2:1 norm, in the design rooms and the study groups that send them proposals. SD-4 assigns no one to rule on a design's quality, wording rooms check only that wording expresses the design, and national bodies vote on each balloted draft as a whole."
- `p:sponsor-votes`: "Each participant a sponsor pays to attend has a vote in the room and values its interests, and no rule limits how many it pays. SC22 may cap only the experts each national body or liaison appoints, and at SC22 itself each national body counts once."
- `l:settled-sponsor`: "Whatever the others choose, a sponsor does best paying for participants in the subgroups whose decisions it values, study groups included, while what they bring it is worth their cost. Each such participant votes valuing its interests, and no rule limits how many it pays."
- `p:sg-decides`: "On a topic with a study group, rival designs can be polled there first, among those who chose that room over the rooms meeting with it. The design it sends on is where the design room starts, and the design room, which owns selecting designs, can still poll a rival that has a paper."
- `l:sg-attendance`: "A participant can attend only one of the rooms meeting at the same time, and votes and speaks only there. So a study group's voters are those for whom its topic outweighs the rooms meeting with it."
- `p:sg-sponsor`: "Paying participants to attend a study group puts voters who value the sponsor's interests where the design the design room starts from is chosen. Where the other voters cast fewer Favor-plus-Against votes, fewer paid participants make up a third of the total, enough to block, or over two thirds, enough to meet the norm."
- `p:deadlock`: "When each of two groups casts at least a third of the Favor-plus-Against votes against the other's design, neither design meets the 2:1 norm. The deadlock lasts until voters change position, a design changes, the voters present change, a chair calls consensus below the norm, or the design room sends both to competing TSs."
- `p:attrition`: "In a long deadlock, a group whose sponsors keep paying its costs bears less per meeting than a group paying its own way. In the case the table below describes, the first does better holding and the second yielding, whichever design is better."
- `t:hold-or-yield` (caption): "Two groups in a deadlock, with equal stakes in their own designs. Group A's sponsors pay its participants' costs and value its holding above what they pay, while group B's participants pay their own. Holding through the deadlock costs group A less than half its stake and group B more than half. A deadlock both hold ends with either design equally likely, and both yielding means a compromise worth half its stake to each."
- `p:sponsor-features`: "Changing the features a sponsor's interests depend on costs that sponsor rework of what it built on them, lost fit with its requirements, and more review, all still to come. The gain of a better design is spread across all the feature's users, and the same 2:1 norm decides every proposal, however many users will rely on it."
- `l:count-depends`: "The count in a poll depends only on who is present, what the poll asks, and how each person present votes on it, if at all."
- `l:thm-deciders`: quoted under finding 4.
- `c:pred-sponsor-against`: "Where one sponsor pays a proposal's authors and many participants present, and its interests include adoption, the model predicts a smaller Against share of the Favor-plus-Against votes than elsewhere. No smaller share would count against it, and votes of participants who move to a sponsor whose interests exclude the proposal would tell it apart from shared technical views."

Sentence check:

- Claim: `p:who-decides`, `p:sponsor-votes`, `l:thm-deciders`.
- Who calls consensus where; wording rooms; whole-draft ballots: `p:who-decides`.
- SC22's cap is per national body or liaison; no rule caps one sponsor's paid participants: `p:sponsor-votes`.
- Sponsor does best paying for participants where decisions it values are made, while worth the cost: `l:settled-sponsor`.
- Study group's starting design, its voters, the design room's remaining power, the third and two-thirds arithmetic: `p:sg-decides`, `l:sg-attendance`, `p:sg-sponsor`.
- "neither advances": `p:deadlock` under `d:follows-norm` (box).
- Sponsored group bears less per meeting; in the table's case it does better holding and the self-funded group yielding, whichever design is better: `p:attrition`, `t:hold-or-yield`.
- Same norm however many users rely on it; costs of change to the sponsor; gain spread: `p:sponsor-features`.
- The count depends only on who is present, the poll, and the votes: `l:count-depends`.

Verdict: PASS. Fix made while drafting: the deadlock sentence now carries all the caption conditions that change the ranks, adding "sponsors who value the group's holding above what they pay".

Changes from draft 2: "SD-4 sets no limit" raised to "no rule limits" (gain 1); "values its interests" added (gain 2); weakening 5.

### Finding 6. SD-4 Assigns No One to Rule on Whether a Design Is Good (priority 4)

Keys:

- `f:no-merit-ruling`: "SD-4 assigns no one the role of ruling which side of a technical dispute is correct or how good a design is (SD-4, whole document; searched: rule, ruling, decide, arbiter, correct, authority, quality, judg, evaluat, assess, merit, opinion, select, pursu)."
- `l:consensus-test`: "Under SD-4's definition, an objection prevents consensus as a sustained opposition only if it concerns a substantial issue, is maintained, and comes from an important part of the concerned interests. The leadership judges that part case by case, none of the three conditions asks whether the objection is right, and the process must seek to reconcile conflicting arguments."
- `p:definition-without-procedure`: "SD-4 adopts ISO's definition of consensus, marked by no sustained opposition, but names no step for judging or registering one, or criteria for an important part of the concerned interests. Whoever ISO's leadership is for a working group, SD-4's steps for an objection include the 2:1 norm, Against voters' reasons on request, escalation, and plenary's 3-way poll and national-position question."
- `p:persuasion-not-required`: "A proposal can advance through WG21 with objections unresolved, since it needs consensus calls, under the 2:1 norm in subgroups and by the convenor at plenary, not every objector's persuasion."
- `l:any-form-vote`: "An Against voter opposed to pursuing the proposal in any form names no change, and their vote counts in a subgroup poll as one Against vote, like any other."
- `l:study-count`: "Studying whether objectors are right takes time, while the 2:1 comparison counts only how many vote Favor and how many vote Against."
- `p:least-cost-response`: quoted under finding 3.
- `p:merit-gap`: "Winning a consensus call and producing the design serving users best coincide only as far as voters can judge that at the poll and weigh no other value above it. SD-4 assigns no one to rule on it for them."
- `l:thm-merit`: "Technical merit enters through what participants value, including a good result for users, and through the discussion, papers, and implementation experience that inform their votes. SD-4 assigns no one to rule on it, and the consensus test never asks whether an objection is right."
- `p:record-indistinct`: "The record SD-4 and the searched ISO clauses require of a WG21 poll need not show whether an objection was answered or outvoted, or why consensus was called over it."
- `l:records-protected`: "SD-4 keeps records of subgroup discussion, meeting wikis, and non-public email lists password-protected. It allows quoting from them publicly only poll questions, numeric results, and words a person consents to have attributed."
- `p:reasons-unrecorded`: "A proposal's case lasts for decades in its required paper, while an unwritten reason survives only in the memory of those who heard it. SD-4 asks whoever raises a concern to file an issue or write a paper, and outside the protected records only writing keeps an objection's argument after its hearers leave."
- `p:dissent-needs-paper`: "Of minutes, non-public email lists, records of subgroup discussion, ballot comments, and papers, only a paper puts an objection's argument outside the password-protected materials without anyone else's help. Writing one takes time."
- `c:pred-defects`: "If some unresolved objections point to real defects, then at equal turnout the model predicts more defects found after adoption in features forwarded over Against votes than with none. No difference would count against it, and matching features on scope, novelty, prior implementation, and use would tell it apart from another explanation, the scrutiny novelty or use brings."
- `c:pred-written-answers`: "The model predicts that papers advancing over Against votes often leave unstated the objections other published papers raised against them, and routine answers would count against it. Another explanation is that the objections were answered in discussion, and omitted objections a subgroup chair's plenary summary shows went unanswered would tell them apart."

Sentence check:

- Claim: `f:no-merit-ruling`, `l:thm-merit`, `p:record-indistinct`.
- SD-4 defines consensus as ISO does, paraphrasing `f:consensus-def` and keeping its process clause, as `l:consensus-test` does; `f:consensus-source` shows SD-4 takes the definition from ISO.
- Three conditions, none asking rightness: `l:consensus-test`.
- ISO's "requires the resolution of substantial objections": quoted from `f:resolve-substantial`, which `l:address-not-resolve` cites; SD-4 names no step or criteria: `p:definition-without-procedure`. The juxtaposition states two proved facts and claims nothing about which governs inside a working group, which `l:iso-register-level` leaves open.
- Steps SD-4 does give, with "include", not a closed list: `p:definition-without-procedure`.
- Advances on consensus calls, not persuasion: `p:persuasion-not-required`.
- "In the count, a right objection and a wrong one weigh the same: one Against vote per holder": `l:study-count`, `l:any-form-vote`. This is about the count only; discussion can still change votes (`ax:attention`), which is why the draft no longer says learning changes nothing.
- Directed change and the count measuring votes: `p:least-cost-response`.
- Best design wins only as far as voters can judge it: `p:merit-gap`. Merit's channels: `l:thm-merit`.
- Record paragraph: `l:record-content` (child of `p:record-indistinct`), `l:records-protected`, `p:reasons-unrecorded`, `p:dissent-needs-paper`.
- "A design can be adopted over an objection that was right": `p:persuasion-not-required` with `l:consensus-test`. "The proposal needs consensus calls, not a persuaded objector": `p:persuasion-not-required`, with `p:least-cost-response` showing no objector need be persuaded when they are short of a third.

Verdict: PASS. No fix needed after drafting.

Changes from draft 2: "judge" became "rule on"; weakenings 1 and 11; added the consensus definition, ISO's resolution principle, and the steps SD-4 does give; the falsifier `c:pred-defects` now carries its condition ("if some unresolved objections point to real defects") and the equal-turnout comparison; added `c:pred-written-answers`.

### Finding 7. No Step Checks That Separately Adopted Designs Work Together (priority 4)

Keys:

- `f:no-integration-check`: "SD-4 names no step in which anyone checks whether designs adopted in separate papers work together (SD-4, whole document; searched: interact, integrat, coheren, consisten, together, harmon, conflict, fits)."
- `p:integration`: "Change papers approved separately at one meeting first come together when the project editor merges their wording, which the editor's report records and a pre-ballot editing committee verifies. No SD-4 step checks whether the designs work together, while each author gains from their own design's adoption and a conflict costs users and later rework."
- `l:separate-approval`: "Plenary approves each wording paper in its own poll, and during the meeting each paper's wording is written against the drafts adopted at its start."
- `l:editor-merge`: "After the meeting the project editor applies all approved changes and reports on merging them, and before a ballot an editing committee verifies they were applied correctly. When the wording rooms have instead reviewed a whole new draft with the changes applied, plenary approves the changes in that form and no editing committee is needed."
- `l:conflict-costs`: "Each author gains from their own design's adoption. A conflict between designs may surface only once they are implemented and used, and then it costs users and forces rework of what was built on them."
- `p:review-shortfall`: "Close study costs the reviewer, while the gain of a better design is spread across all its users. So review worth more to users together than it costs, but less to any one participant, is review no participant does better doing."
- `l:thm-gaps`: "No SD-4 step checks whether separately adopted designs work together, and review worth its cost to users together but not to any one participant goes undone. The record need not show whether objections were answered."
- `inf:thm-review-undone`: "Review worth more to users together than it costs, but less to any one participant, is review no participant does better doing. In this pattern, whether to study a paper is a choice each participant makes the way that does best for them, so that review goes undone."
- `c:pred-competing`: "If closer study finds more defects, the model predicts fewer post-adoption defects on topics whose deciding poll had competing papers from separate author groups than on one-paper topics. No difference would count against it; another explanation is that important or well-understood topics draw rivals and attention anyway, and matching implementation experience and turnout tells them apart."

Sentence check:

- Claim: `f:no-integration-check`, `p:integration`.
- Separate polls, wording written against the meeting's baseline: `l:separate-approval`.
- Editor merges after the meeting and reports; editing committee verifies application, except when the wording rooms reviewed the whole draft: `l:editor-merge`.
- "Those steps check the text against what was approved": `f:editors` (verify "that all approved changes were applied correctly") with `f:no-integration-check`.
- SD-4 encourages early TS merges for "integration testing" (quoted from `f:early-merge`, which `l:checks-deadlock` cites) but names no step checking one adopted design against another: both facts, no claim about how often either happens.
- Defects go unnoticed more in bigger designs: `ax:unknown`. Conflict may surface only in implementation and use: `l:conflict-costs`.
- Integration review: the body applies `p:review-shortfall` in its conditional form ("Integration review worth more to users together than it costs, but less to any one participant, is review no participant does better doing") and says it goes undone in the settled pattern, per `inf:thm-review-undone`. It does not claim that all integration review has that worth.
- Consequence: `l:conflict-costs`, `f:no-integration-check`.

Verdict: PASS. Fix made while drafting: added SD-4's exception that no editing committee is needed when the wording rooms reviewed the whole new draft (`l:editor-merge`, `f:in-situ`).

Changes from draft 2: the review-shortfall sentence keeps its condition in the subject; added the "integration testing" contrast and `c:pred-competing`.

### Finding 8. What No Reviewer Raises, the Author Need Not Say (priority 5)

Keys:

- `f:no-drawbacks-asked`: "Neither SD-4 nor any ISO/IEC Directives Part 1 clause listed here asks a proposal paper or its author to state the design's drawbacks. The searched terms occur only for the costs of travel, meetings, and the procedures, for a TS or white paper's feedback and risk, for project planning, and for appeals (...)."
- `inf:thm-no-request`: "The rules give both kinds of author the same moves and ask no author to state their own design's drawbacks, and SD-4 never uses the word trade-off."
- `f:no-interest-statement`: "Neither SD-4 nor any ISO/IEC Directives Part 1 clause listed here asks an author to state who pays their costs or what interests they or a sponsor have in a proposal. (...)"
- `p:disclosure`: "Stating a drawback in the paper before an early poll can cost Favor votes when incumbency is decided, while a better-informed vote's gain is spread across the design's users. SD-4 says a good paper should show the alternatives considered, but it asks no paper to state its design's drawbacks, and a paper is considered without them."
- `p:same-moves`: "The rules treat both kinds of author alike: the same moves, and no request to state a design's drawbacks, a sponsor, or what the author's gain depends on. So stating a trade-off can cost a result-seeking author Favor votes that a design-bound author who leaves it out keeps."
- `t:disclose` (caption): "An author's choice, before an early direction poll, whether to state in the paper a trade-off no reviewer would otherwise raise. Stating it would lead the room to change a feature a design-bound author's gain depends on, in a way that serves users better. The proposal meets the 2:1 norm either way."
- `l:bound-omit`: "A design-bound author does best leaving out a trade-off no reviewer would raise when stating it now costs more than its later exposure would."
- `inf:omit-free`: "Leaving it out costs the author no step the rules require before adoption. The rules ask no proposal paper to state its design's drawbacks, and a paper is considered without them."
- `inf:omit-exposure`: "A trade-off left out can be found in implementation and use and reopen the matter as new information, and a change won then redoes or discards work the author built."
- `l:settled-result-seeking`: "Whatever the others choose, a result-seeking author does best stating trade-offs and granting changes whenever the better design they bring outweighs the votes or work they cost. It does best backing any rival that serves users better by more than its share of the reversal's cost."
- `l:thm-disclosure`: "The rules ask no author to state their own design's drawbacks. Leaving one out costs a design-bound author no step the rules require before adoption, while stating one can cost a result-seeking author votes."

Sentence check:

- Claim: `l:thm-disclosure`, `p:disclosure`, `inf:omit-free`.
- "SD-4 never uses the word trade-off": `inf:thm-no-request`.
- What SD-4's good-paper list includes (principles, motivating examples, alternatives): `f:principle-based`, `f:example-based`, `f:show-alternatives`, summarized in `l:checks-alternatives`.
- No rule asks for drawbacks, who pays, or interests: `f:no-drawbacks-asked`, `f:no-interest-statement`.
- Learning can change votes: `ax:attention`. Stating before an early poll can cost Favor votes; gain spread: `p:disclosure`.
- Same moves; in the table's case the two types choose oppositely: `p:same-moves`, `t:disclose`. The sentence carries the caption's three conditions (the change hits a feature the design-bound author's gain depends on, it serves users better, the proposal passes either way).
- "No rule makes a paper show which kind of author wrote it": the kinds are defined by what the gain depends on, and `p:same-moves` says the rules ask no author to state that.
- A left-out trade-off can surface later and reopen the matter: `inf:omit-exposure`.
- Consequence: the votes deciding incumbency can be cast without it; a change won later redoes work; the flaw's cost can fall on any user: `inf:omit-exposure`, `p:reward-timing`.

Verdict: PASS. The one narrowing from draft 2 (decision 8, weakening 9) is that "costs nothing the rules impose" became "costs no step the rules require before adoption". The Theorem itself was narrowed this way in review (`step-11` read "nothing the rules impose"), because `inf:omit-exposure` adds a cost that can come later. The sentence still says stating a drawback can cost votes, so the old "costs no votes" overclaim is not back.

Changes from draft 2: split from the first-part finding (decision 4); the drawbacks and interest absences now cover the ISO clauses (gains 3 and 5); "SD-4 never uses the word trade-off" added; the type contrast now says "does best", not "states it / does not".

### Finding 9. The Smallest Part That Fixes the Structure Goes First (priority 6)

Keys:

- `p:first-part`: "A first part fixing a design's structure can be adopted before reviewers can study in detail what later parts need, and every rival to that structure must then replace it. SD-4 asks no paper to state those needs, so a design-bound author does best proposing first the smallest part that fixes the structure and can pass."
- `p:parts`: "Presenting a design in parts lets the first parts be adopted before the whole is reviewed, and each adopted part adds to what a rival to the whole must replace. Its costs include a paper, a presentation, and a set of polls for each part."
- `inf:part-is-addition`: "A part of a design proposed on its own is a design addition, which SD-4 requires to have a paper."
- `l:part-advances-alone`: "Each part's paper advances on its own consensus calls in the design and wording rooms and at plenary, so an early part can be adopted before later parts are presented."
- `ind:adopted-parts`: "Each part adopted adds to what a rival to the whole design must replace: the part itself and the work built on it, later parts that depend on it included."
- `l:first-part-foresight`: "At the first part's polls, only those who foresee the rest can base their vote on what the later parts will need of it. Others cannot study that in detail until those parts are presented, and SD-4 asks no paper to state it."
- `l:first-part-fix`: "A design-bound author does better when its first part fixes the features its gain depends on, as the structure later parts build on, than when a later part fixes them. The first part is adopted sooner, and every later part that depends on it adds to the cost of the reversal a rival would need."
- `l:first-part-smallest`: "Of two first parts that fix the same features and can pass, the smaller is ready and reviewed sooner. So a design-bound author whose gain depends on those features does better with the smaller, which can fix them sooner."
- `l:first-part-oppose`: "Against votes on the first part can keep it from meeting the 2:1 norm, while removing it once adopted needs a paper or ballot comment meeting the norm. So opponents who foresee the rest, and whose Against votes together can reach a third of the Favor-plus-Against votes, do better voting Against the first part than seeking its removal."
- `inf:oppose-early-rank`: "Blocking the first part takes a third of the Favor-plus-Against votes, while removing it later takes over two thirds, so opponents who together can block do better voting Against early."
- `f:no-parts-step`: "SD-4 asks no paper that proposes part of a design to state what later parts will require of it, and names no step for reviewing such parts together (...)."
- `l:thm-first-part`: "A first part fixing a structure can be adopted before reviewers can study in detail what later parts need, and every rival to that structure must then replace it."
- `c:pred-parts`: "The model predicts that large proposals tend to arrive as sequences of papers, each building on adopted parts, and large designs mostly adopted in one paper would count against it. Another explanation, easier review in parts, gives no reason to omit from a first paper what later parts need of it, an omission the model predicts for design-bound authors."
- `c:pred-first-part`: "For design-bound authors, the model predicts small first papers that leave out the later parts of a design extended part by part; the mailings are the evidence. Finding no such omissions would count against it, and another explanation, that small first steps lower risk, gives no reason to omit any mention of later parts that already exist."

Sentence check:

- Claim: `p:first-part`, `ind:adopted-parts` ("the part and the work built on it").
- Each part is a design addition needing a paper and advances on its own calls: `inf:part-is-addition`, `l:part-advances-alone`.
- Reviewers cannot study later needs in detail until presented; only those who foresee the rest can base their vote on them: `l:first-part-foresight` (and `ax:first-review`).
- No paper must state later needs, no step reviews parts together: `f:no-parts-step`.
- Fixing early fixes sooner and raises the reversal cost; the smaller part is ready and reviewed sooner: `l:first-part-fix`, `l:first-part-smallest`.
- The limit: blocking takes a third, removing takes over two thirds, so opponents who can block do better voting Against early: `l:first-part-oppose`, `inf:oppose-early-rank`.
- Consequence: `l:thm-first-part`, `ind:adopted-parts`. "a rival structure" replaces my first wording, "a better structure", since the keys speak of any rival.

Verdict: PASS. Fix made while drafting: "The check is the opponents" became "The limit is the opponents", since "check" names the rules' checks elsewhere in the body.

Changes from draft 2: split from disclosure (decision 4); weakening 10; added the one-third versus two-thirds contrast and `c:pred-parts`; `c:pred-first-part` now carries its tell-apart test.

## Thesis, stability page, box, and levers

- **Thesis.** Each sentence repeats a finding at its finding's strength: "participants present decide" (`p:who-decides`), "assigns no one to rule" (`f:no-merit-ruling`), incumbency at the first direction poll, which can come at the first meeting (`d:incumbent`, `l:first-meeting-poll`, `ax:first-review`), growing reversal cost (`l:thm-fixed-early`), "Other things equal" on procedures (`p:fluency`), "No user votes" (`p:who-votes`), "No rule limits" and "keep paying" (`l:thm-deciders`, `l:thm-holding`), the three absences (`f:no-integration-check`, `f:no-drawbacks-asked`, `p:record-indistinct`), and "Each holds with the rules' checks in place" (`thm:settled`, `p:checks`). The INCITS note in the box keeps "use only SD-4's text, a few clauses of the ISO/IEC Directives, and assumptions" true for the body (decision 7). PASS.
- **Stability page.** Definition: `d:settled-pattern`. "Most of the pattern's choices do best for their player whatever the others choose": every settled lemma opens "Whatever the others choose", and `l:thm-pattern` covers the open choices. The list of choices follows the Theorem's first paragraph. Each deviation example carries its condition: the regular (`p:doubt-outside-count`), the chair (`p:chair-default`, `p:chair-threshold`), the design-bound author ("when stating it costs more than later exposure would", `l:bound-omit`, `inf:state-costs`), the sponsor ("worth their cost to it", `l:sponsor-paid-votes`, `l:sponsor-how-many`), and the national body ("values the rest of a document above removing one feature", `p:nb-comment`, `l:settled-nb`). Checks: `p:checks`, `l:thm-checks-sizes`. "Stable does not mean unique": `p:objector-coordination`. Last line: `c:levers`. Fix made while drafting: the first deviation paragraph lacked the conditions for the design-bound author, the sponsor, and the national body; they were added. PASS.
- **Box.** Assumptions follow `ax:cost`, `ax:who-pays`, `ax:repeat`, `ax:support`, `ax:prefer`, `ax:attention`, `ax:review-cost`, `ax:unknown`, `ax:first-review`, `ax:rework`, and `ax:learning`, grouped into seven bullets. Fixes made while drafting: "No one can study every paper" became "No participant can study every paper closely" (`ax:attention`), and "Other things equal" was added to the preference bullet (`ax:prefer`). Scope bullets: `d:rules`, the not-searched documents from `f:absences`, the INCITS note, `d:follows-norm` and `f:no-sustained-procedure`, the axioms-not-behavior scope, the Theorem's open choices (`thm:settled`), and "rule on" with the direction group's opinion role (`f:direction-opinion`, `f:no-merit-ruling`). Each scope appears once in the body. PASS.
- **Levers.** All nine chapter 12 levers, each at its corollary's wording: `c:lever-written-answer`, `c:lever-sustained-procedure`, `c:lever-sponsor-limit`, `c:lever-deadlock-rule`, `c:lever-ts-path`, `c:lever-anonymous`, `c:lever-reasons-all`, `c:lever-nb-more`, `c:lever-nb-less`. None argues for adoption, per the plan's decision that levers appear only as testable "if this rule changed" results. "None asks anyone to behave better. Each changes what the rules reward" restates `c:levers` ("Each change below, to a rule or to what a move costs"). PASS.

