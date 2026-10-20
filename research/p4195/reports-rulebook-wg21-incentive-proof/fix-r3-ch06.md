# Round 3 fixes, chapter 6

Context from the round 3 reconcile, which changed the foundation and the spine before this file was written:

- Foundation. New Fact `f:ballot-discussion` (ISO 1.7.5: no formal discussion during official meetings of a document out for ballot or comment). Extended Facts: `f:in-situ` (plenary approves the changes in the applied form), `f:near-unanimous` (changes at ballot comment resolution have one goal, to improve consensus), `f:show-alternatives` (the author should show reasonably thorough consideration), `f:ts-default` (the TS lag is a grace period for developing alternatives), `f:late-documents` (ad hoc groups and comment resolution are exempt from the deadlines). `f:iso-no-answer` now also excepts 2.6.5's observations on each comment; `f:no-drawbacks-asked` now says neither SD-4 nor any listed clause uses the word trade-off. `ax:first-review`'s second sentence now reads "while those parts are unpublished". `d:user` now says a guest a convenor invites participates and so is not a user.
- Scope. `l:settled-regular` and the Theorem's regular sentence are now stated for a poll on one proposal. The Theorem's open choices now include any call SD-4 leaves to a chair or the convenor, such as the call at a Neutral majority and the choice among rivals that all meet the 2:1 norm. `l:call-above` and the chair table now cover any chair (global decision 2). "No user votes" in the Theorem now reads "No user votes in WG21's polls or ballots".
- Words. Write "is kept only in" or "remains only in", not "survives only in"; "affect decisions", not "reach decisions"; "large proposals", not "large designs"; "first papers of small scope", not "small first papers"; "allowing early, limited exploration" for the chairs' discretion. Do not use "carry" or "door".
- Length. Each item has at most two sentences of at most 30 words. Where a statement needs more, keep its claim in the item and make each other sentence a child step with its own key, one sentence each. Never nest deeper than three levels: a level-3 step that needs support cites an earlier level-3 step placed before it.
- Citations. A child may cite only foundation items, spine items of earlier chapters, earlier items of its own chapter, or its own children.
- Spine lines below quote statements already changed in this chapter and in `02-spine.md`. Do not edit those statements; make their children prove them, or cut children that no longer serve them. Never soften a plain, sharp, true statement.

## Spine statements changed by the reconcile

p:sponsor-votes | spine change, round 3 reconcile | statement changed | The spine statement now reads: "Each participant a sponsor pays to attend has a vote in the room and values its interests, and no rule limits how many it pays. Each is appointed by a national body or liaison that chooses whom to appoint, SC22 may cap only how many each appoints, and at SC22 each national body counts once." Make its children prove it, or cut children that no longer serve it. | fixed
p:first-part | spine change, round 3 reconcile | statement changed | The spine statement now reads: "A first part fixing a design's structure can be adopted before reviewers can study in detail what later parts need, and every rival to that structure must then replace it. SD-4 asks no paper to state those needs, and the smallest part fixing the structure that can pass is reviewed soonest, so a design-bound author does best proposing it first." Make its children prove it, or cut children that no longer serve it. Its second sentence now names l:first-part-smallest's reason (ready and reviewed sooner), which is already its child; no new child is needed. l:first-part-foresight takes the narrowed ax:first-review (follow-on below). | fixed

## Findings


## Follow-on edits from findings applied to the foundation or spine

l:first-part-foresight | follow-on of 12.3A33 | ax:first-review now covers unpublished later parts | Write "At the first part's polls, only those who foresee the rest can base their vote on what the later parts will need of it. Others cannot study that in detail while those parts are unpublished, and SD-4 asks no paper to state it." inf:foresight-ask follows. | fixed
