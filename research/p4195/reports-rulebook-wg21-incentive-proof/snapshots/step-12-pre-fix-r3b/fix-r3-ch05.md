# Round 3 fixes, chapter 5

Context from the round 3 reconcile, which changed the foundation and the spine before this file was written:

- Foundation. New Fact `f:ballot-discussion` (ISO 1.7.5: no formal discussion during official meetings of a document out for ballot or comment). Extended Facts: `f:in-situ` (plenary approves the changes in the applied form), `f:near-unanimous` (changes at ballot comment resolution have one goal, to improve consensus), `f:show-alternatives` (the author should show reasonably thorough consideration), `f:ts-default` (the TS lag is a grace period for developing alternatives), `f:late-documents` (ad hoc groups and comment resolution are exempt from the deadlines). `f:iso-no-answer` now also excepts 2.6.5's observations on each comment; `f:no-drawbacks-asked` now says neither SD-4 nor any listed clause uses the word trade-off. `ax:first-review`'s second sentence now reads "while those parts are unpublished". `d:user` now says a guest a convenor invites participates and so is not a user.
- Scope. `l:settled-regular` and the Theorem's regular sentence are now stated for a poll on one proposal. The Theorem's open choices now include any call SD-4 leaves to a chair or the convenor, such as the call at a Neutral majority and the choice among rivals that all meet the 2:1 norm. `l:call-above` and the chair table now cover any chair (global decision 2). "No user votes" in the Theorem now reads "No user votes in WG21's polls or ballots".
- Words. Write "is kept only in" or "remains only in", not "survives only in"; "affect decisions", not "reach decisions"; "large proposals", not "large designs"; "first papers of small scope", not "small first papers"; "allowing early, limited exploration" for the chairs' discretion. Do not use "carry" or "door".
- Length. Each item has at most two sentences of at most 30 words. Where a statement needs more, keep its claim in the item and make each other sentence a child step with its own key, one sentence each. Never nest deeper than three levels: a level-3 step that needs support cites an earlier level-3 step placed before it.
- Citations. A child may cite only foundation items, spine items of earlier chapters, earlier items of its own chapter, or its own children.
- Spine lines below quote statements already changed in this chapter and in `02-spine.md`. Do not edit those statements; make their children prove them, or cut children that no longer serve them. Never soften a plain, sharp, true statement.

## Spine statements changed by the reconcile

p:late-arrival | spine change, round 3 reconcile | statement changed | The spine statement now reads: "An objector who arrives after a design is adopted needs a paper or ballot comment meeting the 2:1 norm, against a reversal cost that grows as more is built. The record keeps the design's case, while unwritten objections are kept only in memory." Make its children prove it, or cut children that no longer serve it. l:late-record takes 12.3D10; l:late-removal and l:late-reversal already prove the first sentence.

## Findings

l:late-record | reader, figure of speech (12.3D10) | l:late-record: "survive only with those who heard them" | Write "The design's case lasts in its paper, while objections no one wrote down are kept only by those who heard them."

## Follow-on edits from findings applied to the foundation or spine

l:removal-polls | follow-on of 12.3A18 | SD-4's goal for changes at ballot comment resolution | Write "Design rooms own selecting designs and plenary does not change them, so a removal, by paper or comment, needs the 2:1 norm in a design room." and add a sentence or step: "One answering a ballot comment must also aim, SD-4 says, to improve consensus." Cite f:near-unanimous, which now quotes that sentence.
l:ts-merge-default | follow-on of 12.3A39 | the grace-period call | Add that SD-4 asks participants who prefer a different approach to develop their own alternatives during the TS lag, keeping the default as it is. f:ts-default now quotes the grace-period sentence. Split into two sentences if over 30 words.
