---
name: WG21 incentive model
overview: Build the source material for a new WG21 paper as a plain-English proof in inert sentences. Numbered axioms and quoted rules earn the players, their moves, and payoff matrices through lemmas, inferences, and induction, up to an earned statement of the Nash equilibrium. The broad strokes are pre-digested in this plan. Fourteen steps, each with explicit subagent discipline, take the pre-digest through one sign-off checkpoint, an automatic spine freeze, parallel chapter proofs, and verification rounds to wg21-papers/research/p4195.
todos:
  - id: step-1
    content: "Step 1: build support/kit.md and support/rules-extract.md by shell, start the ledger"
    status: completed
  - id: step-2
    content: "Step 2: write build.py and patch Scrivener list levels (two coding subagents, two review subagents, in parallel)"
    status: completed
  - id: step-3
    content: "Step 3: check the pre-digested triage (one triage-check subagent), then reconcile"
    status: completed
  - id: step-4
    content: "Step 4: draft the foundation (axioms, definitions, facts) in keyed source format"
    status: completed
  - id: step-5
    content: "Step 5: review the foundation (five reviewers in parallel), reconcile, revise"
    status: completed
  - id: step-6
    content: "Step 6: CHECKPOINT 1, user signs off on the foundation and the triage"
    status: completed
  - id: step-7
    content: "Step 7: write the spine (every top-level claim, table shapes, Theorem draft, incentive mapping)"
    status: completed
  - id: step-8
    content: "Step 8: review the spine (four reviewers in parallel), reconcile, revise"
    status: completed
  - id: step-9
    content: "Step 9: spine freeze, recorded in the ledger without asking the user"
    status: completed
  - id: step-10
    content: "Step 10: fill chapters 2 to 12 (eleven chapter-fill subagents in parallel)"
    status: completed
  - id: step-11
    content: "Step 11: integrate, propagate weakened statements, up to three refill rounds, build.py full check"
    status: completed
  - id: step-12
    content: "Step 12: verify (five reviewers per round, fix subagents per chapter), up to five rounds"
    status: in_progress
  - id: step-13
    content: "Step 13: finish the Theorem, compactness pass, then abstract, title, how-to-read, appendices; review them"
    status: pending
  - id: step-14
    content: "Step 14: emit wg21-game-theory.md, copy sources and the adversarial log to support, render and check"
    status: pending
isProject: false
---

# WG21 Incentive Proof

## Goal

Source material for a new WG21 paper, written as a proof. An abstract states the conclusion up front. Numbered axioms and quoted rules come first. Every later item follows from items before it: the players, their moves, the payoff tables, the larger conclusions, and finally one or two paragraphs stating the settled pattern (the Nash equilibrium). Every sentence is inert: a reader of any affiliation accepts it on sight or sees that it follows from what it cites. A reader may dislike the conclusion but finds no step to deny.

## Background

- **The request.** The user asked for a game-theoretic analysis of the WG21 (ISO C++ committee) process. The players are paper authors, reviewers, design room and study group chairs, the convenor, national bodies, the sponsors (employers) who pay participants, and C++ users.
- **The method.** The model is deduced from the written rules alone, plus assumptions about people that no reader can reasonably deny. WG21's history is held out as test data: the user will later check the model against minutes and reflector threads, so no historical event may inform the proof.
- **Emphasis, from most space to least:**
  1. the design rooms (EWG, LEWG) and the study groups that feed them
  2. large sponsor-funded proposals that span several editions, compared with small individual ones
  3. the cost of voting Against a colleague's proposal, among regulars who meet at every meeting
  4. a short treatment of the three-year release schedule and its incentives
  5. a minor treatment of national bodies
  6. a brief mention of the wording rooms
- **The use.** The output becomes the foundation of a WG21 paper. Committee members, employers, and users must be able to follow it without knowing game theory, and agree with each step.

## Decisions already made

Do not re-ask these.

- **Format:** a numbered proof (axioms, definitions, facts, lemmas, inferences, inductions, propositions, corollaries, Theorem), not a report with an executive summary. An abstract states the conclusion first.
- **Checkpoints:** one, after the foundation review (Step 6, approved 2026-10-18). Step 9 is an automatic spine freeze with no sign-off, and the run continues to completion without asking the user anything unless a fatal error occurs.
- **Rule levers:** these appear only as testable "if this rule changed" corollaries, with no advocacy.
- **Writing:** every sentence is inert, motives come only from the axioms, and the `writer-register` block sets the register.
- **Rendering:** nested ordered lists, drawn by Scrivener as 1, a, i after the Step 2 patch. Labels are bold, the basis is in italics at the end, and ∎ appears once.
- **The original 14 assumptions** (in the `original-assumptions` block) were revised:
  - added: reciprocity, sponsor goals, vote visibility, and a fixed list of values
  - dropped: the C++20 contracts example, as sealed history
  - treated as rule readings rather than assumptions: items 10 and 12 to 14
  
  The pre-digested foundation reflects these revisions.
- **Candidate lists:** the user's two lists are leads, and the facts that cite history were already cut.
- **Proposal sizes:** the proof compares large proposals, which are sponsor-funded and span more than one edition, with small ones only. An earlier middle size, group proposals reviewed over several meetings, was cut.
- **Ship fixes from user feedback (2026-10-18):** each is handled where noted.
  - Every payoff table has its ranks filled (Step 10; Step 14's gate rejects a blank cell).
  - The JTC 1 Supplement is searched and its relevant clauses added to the extract, so the absence facts cover it (Step 9).
  - The reading of ISO's "leadership" is defended or widened to include the convenor; `l:iso-register-level` and `p:definition-without-procedure` state a claim that holds under either reading (Step 8 reconcile).
  - Each prediction names an innocent explanation and the data that would tell the two apart (Step 8 reconcile).
  - The Theorem says where technical merit enters (Step 8 reconcile).
  - The incubator study groups, EWGI and LEWGI, are mentioned in the small-proposal and newcomer items, worded conditionally since SD-4 does not name them (Step 8 reconcile).
  - A spine item says how the size results apply to proposals of neither size, by the attribute each result rests on (Step 8 reconcile).
  - INCITS's one-vote-per-organization rule is confirmed before `p:nb-members` relies on it; until then `p:nb-members` depends on each national body's own rules (Steps 8 and 9).
- **Modules:** Step 7 groups self-contained chains of spine items into modules, each a top-level conclusion with its steps as lettered children, so a reader can check each module alone and later items cite only its conclusion. A module's conclusion may also cite earlier items, and Step 11 runs the pass again after the chapters are filled.
- **Common-sense filter (user, 2026-10-19):** the proof shows a derivation only where a committee member could ask why a statement follows. An item that restates or joins the rules it cites, or follows from them in one step a reader accepts on sight, keeps its statement, its quotes, and its `*[from ...]*` citation, and loses its lemmas and steps. The checking still happens; its record lives in the ledger and the adversarial log, not in the paper. Step 11 applies the filter before Step 12 verifies, and `chapter-fill-instructions` tells refills not to write such proofs.
- **Paper structure (user agreed, 2026-10-19 10:27 and 10:29):** the paper leads with findings, and the proof is its appendix. Body, about 10 to 12 pages in P4195's voice: (1) a one-paragraph thesis, which says the results use only SD-4's own text and a few assumptions any participant would grant; (2) about eight named findings, each giving the claim at full provable strength, the mechanism in plain words, the consequence for the standard and its users, the SD-4 or ISO rule it rests on as a short quote, and its Appendix A items; (3) one page on why the pattern is stable; (4) a short box "What this rests on" (five to seven plain assumptions, and what the proof does not claim); (5) the reform levers. Terms are defined in plain words at first use. Appendix A holds the full proof (axioms, definitions, facts with full quotes, derivations, tables); Appendix B holds the method, the sources, and the review record. Each idea is stated once in the body and proved once in the appendix. Step 13 builds this with build.py's `--front` for the body. Open user decision: whether the body may cite P4195's case histories as illustrations, while the proof rests only on rules.
- **Sharpness (user feedback, 2026-10-19):** the chapters read as hedged, conditional, and padded, and they miss the sharp conclusions of D4195. Verified: spine items average 51 words against the 30-word rule, with 18 "unless" and 11 "though" clauses, and about a dozen results of the form "does better when worth more than its cost", which hold by definition once `d:does-better` uses the player's weighing. Causes: the Step 8 reconcile's weaker-wording fixes, which piled qualifiers into sentences; the weighing definition, which turned threshold results into tautologies; and a reader role with no check for hedges, tautologies, length, or sharpness. Remedies: sharpness rules in `proof-style`; new reader finding types (hedge, tautology, obvious, long) and an instruction not to soften a plain, sharp statement; Step 11 action 4 (Sharpen). A sharp statement must still be true: the Step 12 logician tests every sharpened claim for overreach. Plain language (user, 2026-10-19 03:17): statements are written for a reader outside the committee, in the positive form wherever it states the same claim, and worded to be interesting; absences and prohibitions keep their negative form, because a positive form would claim more; no rewrite changes a claim. The reader gains finding types negative and dull.
- **Item cap (user, 2026-10-19):** Step 11 runs build.py with `--max-items 200`, so that results serving the user priorities stay top-level during integration instead of being folded early or cut. After the collapse, the padding cuts, the sharpening, and the module pass, the count must reach the final cap: a target of 150 and a hard ceiling of 175, where each top-level item above 150 serves one of the user priorities or is cited by one that does. Step 11 records the final cap in the ledger, and every later build.py run passes it as `--max-items` when it is above 150.
- **User priorities (2026-10-19), in order; each is tested, not assumed:** (1) how procedural momentum and process fluency let a determined author's design pass the stages that settle its content with little review; (2) how C++ users are left out of the decisions; (3) what the incentives reward: users, the language, technical quality, or the room, its sponsors, and its authors, and who decides what goes in; (4) quality control and integration: what connects a decision to a good design, and whether anyone checks or is rewarded for making separately adopted papers work together; (5) whether authors do better leaving trade-offs undisclosed; (6) whether the best strategy is a minimal first part that fixes a design's structure, which later becomes hard to oppose. Step 11 additions, cuts, and the Theorem's emphasis follow this order; results that serve none of these stay only as needed context.
- **Dysfunction focus (user, 2026-10-19):** the paper surfaces where the rules reward behavior that harms the standard, its users, or the fair handling of objections. Items that prove normal or well-known practice stay only where a later result cites them or a reader needs them for context; Step 11 trims them hardest in chapters 2 and 3.
- **Step 11 additions (user agreed in principle, 2026-10-19):** (1) a conditional result that a poll placing a proposal among the work the committee aims to include in the next IS moves it into a category chairs take up first, at the expense of other papers' time; (2) a result that a sponsor does better paying for participation in a study group whose output it values, because the design room starts from that output, with the arithmetic that the fewer the voters in a room, the fewer participants make a third or two thirds of the Favor-plus-Against votes; (3) a clause in `ax:prefer` that a sponsor's interests can depend on particular features of a design, and a result that its sponsors do better keeping a design intact unless a change is worth more to them than the rework of what they have built on it, the loss of fit with their own requirements, and the added review, stated through costs still to come, never sunk costs. (4) a credible-threat result: the risk of national body opposition over one feature comes only from bodies that value blocking it above the rest of the document, which SD-4 expects to have said so before the ballot; (5) a comparative-statics question in chapter 12, "what if national bodies exercise more, or less, oversight during the meetings", answered from the proof's steps with the resulting settled pattern for each case, framed as a change in what forming a national position costs (oversight during meetings is the only per-proposal lever, since the ballot is all or nothing). Candidates from the D4195 support report join these if they pass the five-part test: accepted on sight, forward-looking, not a disguised conclusion, no bad faith, stated by attribute. Candidates the main agent identified from the user priorities, pending that report: (6) what decides content: the attending participants as counted under the 2:1 norm and called by chairs, with no one assigned to judge a design's quality, wording rooms checking only that wording expresses the design, and national bodies able only to accept or reject the whole document; (7) integration: an SD-4 absence fact, if a search confirms it, that no step checks whether separately adopted designs work together, and a result that an author's gain comes from their own design while a conflict's cost falls on users and later work; (8) users: a premise that a better design's gain is spread across all its users while participating costs the one who participates, and a result on why few users find participating worth it; (9) disclosure: a conditional result, with a premise that information in a paper can change votes, that an author who values adoption does better leaving a trade-off out before an early poll when the votes it would cost exceed what disclosure gains, against SD-4's "a good paper should"; (10) minimal first part: a conditional result that an author whose gain lies in a design's structure does better proposing first the smallest part that fixes that structure and can pass, limited by opponents who foresee the later parts; (11) process fluency: objections have weight only in the right form, channel, and time, which participants learn by attending. (12) Author types, part of the spine (user agreed, 2026-10-19): two definitions, not axioms, `d:result-seeking` (an author whose gain from a proposal depends on how well the adopted design serves its users, not on whether it keeps any particular feature) and `d:design-bound` (an author whose gain depends on the adopted design keeping particular features fixed before review, for example because a sponsor's interests depend on them), resting on the weighing clause of `ax:prefer` and addition (3); a clause in `ax:attention` that what a participant learns from a paper can change their vote, for the disclosure results; `m:players` lists the two kinds of author as separate players, while `m:moves-author` stays one list because the rules give both the same moves; chapter 11 replaces `l:settled-large-author` with one settled lemma per type (early polls, objections, disclosure, parts, rivals), adds a lemma that an author who weighs both makes each choice as the type whose value weighs more for it, and adds a result that the rules give both types the same moves and require neither to disclose trade-offs, so disclosure can cost a result-seeking author votes a design-bound author does not lose; the Theorem states each type's choices; one payoff table shows a choice by type. Expect about four more top-level items, so the Step 11 cuts must free at least as many.
- **User guidance on four candidate facts, already applied in `pre-triage`:**
  - SD-4 states no tally requirement.
  - ISO's duty to register opposition sits with the committee leadership, so WG21 breaks no rule. That the looseness creates incentives is a proposition to prove.
  - "The rules exclude no one" means no registered expert is excluded.
  - F3 may concern personal costs rather than money.

## Ground rules

- **Paths.** This plan is `c:\Users\Vinnie\.cursor\plans\wg21_incentive_model_96468661.plan.md`. In this plan, `support/` means `c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\`, and "scratch" means `c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof\`. Fill every path field in a dispatch with an absolute path.
- **Shell.** Windows PowerShell. Run scripts with `c:\Users\Vinnie\cursor\wg21-paperworks\.venv\Scripts\python.exe`.
- **Starting.** Begin only when the user says go. Read this plan in full. If scratch `ledger.md` exists, resume at the first step whose gate has not passed; otherwise begin at Step 1.
- **Questions.** After Step 6, ask the user nothing and run to the end of Step 14, deciding each open point and recording it with its falsifier in the ledger. Stop only for a fatal error: a failure that no step in this plan can resolve and that prevents finishing, such as a missing input, a tool that cannot run, or a subagent that returns blocked twice.

- **Concurrency (user, 2026-10-19 07:26).** At most 8 subagents run at once, every one with `run_in_background: true`. Never stop a running subagent to meet the cap; start a new one only while fewer than 8 are running. A fan-out larger than the free slots goes in waves, each wave in one message, which overrides "in one message" wherever a step says it; reconciling still waits until every member of the fan-out has reported.
- **Snapshots (user, 2026-10-19).** No step destroys intermediate information, so any step can be redone from its saved state. Run scratch `snapshot.py take <tag>` at every step's gate (tag `step-NN`) and before every action that overwrites working files: each reconcile or adoption of changes (`step-NN-pre-<action>`), each refill or fix round (`step-11-pre-refill-rN`, `step-12-pre-fix-rN`), the collapse and padding cuts (`step-11-pre-collapse`), and each emit or render. A snapshot holds the foundation, spine, incentive map, chapter files, ledger, adversarial log, modules check, labeled emits, review files, the rule extract, the kit, the triage table, build.py, and this plan, with a manifest of sizes and hashes; it is never edited or deleted. To redo from step N, run `snapshot.py restore step-NN`, which snapshots the current state first and deletes nothing, then rerun from step N+1. Review and fix outputs that a later round would overwrite are kept under round-numbered names.
- **Inputs.** Only these sources inform the proof:
  - SD-4, dated 2026-05-11, already fetched
  - [cabinet/_inbox/ISODirectives2026-part1.md](c:\Users\Vinnie\cursor\cabinet\_inbox\ISODirectives2026-part1.md)
  - the user's decisions recorded in this plan
  - the current consolidated ISO/IEC JTC 1 Supplement to Directives Part 1, for the clauses Step 9 adds to the extract (user decision, 2026-10-18)
  - INCITS's published procedures, only to confirm how INCITS counts votes when it forms a national position (user decision, 2026-10-18)
  - the D4195 draft, `wg21-papers/source/2026-10-october/d4195-culture-of-sd-4.md`, only as leads for candidate axioms and conclusions: each is proved from the foundation or marked unsupported, and its names, paper numbers, and events stay out of the proof (user decision, 2026-10-19)
- **Leads, not evidence.** The pre-digested analysis and the two candidate lists below are leads. Every Fact is checked against the rule extract. Every derived item is proved or cut.
- **Sealed history.** Follow the `sealed-history-rule` block. No individual is named.
- **No other workspace file** informs the content, apart from the D4195 draft as leads, listed above. This rule does not cover the Scrivener code and its documentation, which Step 2 and Step 14 use only to change and run the renderer.
- **File locations:**
  - Showing the work: [wg21-papers/research/p4195/support/](c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support), written `support/` below. It holds `kit.md`, `build.py` and its tests, `rules-extract.md`, `triage.md`, `adversarial-log.md`, and at the end `source/` with the keyed proof files.
  - The finished proof: `wg21-papers/research/p4195/wg21-game-theory.md`.
  - Work in progress: `cabinet/_scratch/reports-rulebook-wg21-incentive-proof/`, written "scratch" below. It holds drafts, review files, `ledger.md`, and test renders.
  - Neither repo location exists yet. Everything stays uncommitted for the user's review.
- **The plan is the canonical source.** During execution, do not edit this plan's instructions; update only todo statuses. Work products and run state live in files.

## Proof conventions

- **Numbering:** one sequence of top-level numbers runs through all chapters, continuing across chapter headings. A step with parts gets lettered children. A lettered child with a chain of small steps gets roman children. Example labels: 14, 14b, 14b.ii.
- **Labels:** each item opens with its kind in bold. The statement is upright. The basis is in italics and brackets at the end. A ∎ appears once, at the end of the Theorem.
- **Keys:** while drafting, every item carries a stable key and cites by key. `build.py` assigns final labels and rewrites citations.
- **Inert sentences:** follow the `proof-style` block, which holds the standard, the forbidden words with their replacements, and no/yes pairs.
- **Conditional conclusions:** every conclusion holds "under the rules in force, and given the axioms." Conclusions describe what the rules reward, never what any person does.
- **Motives:** motives come only from the axioms. They are stated once and apply equally to every player in a role, so no player is singled out.
- **Register:** every writing agent, and the main agent when drafting, writes in the register set by the `writer-register` block.
- **Counter-forces included:** the proof states the checks in the rules that work and folds them into the Theorem. These include: a group holding more than one third of the votes can block; implementation experience informs voters; the schedule keeps one unfinished feature from delaying the rest; national bodies ballot the draft.
- **Compact by rule:**
  - at most 150 top-level items in the finished proof, under the "Item cap" decision: Step 11 works under a ceiling of 200 and ends at or under the final cap
  - one sentence per item, two at most
  - every item other than a milestone, a table, the Theorem, or a corollary must be cited by a later item, or it is cut
  - each chapter ends with a plain-terms recap of at most three sentences
- **Payoff tables:** follow the `payoff-table-format` block.

## Subagent discipline

Every subagent is launched with this template, copied verbatim. Replace every uppercase field, write `none` for an absent `OR NONE` field, and add no other text. Before dispatch, search the filled template for `<[A-Z][A-Z ]*>`. Fill any remaining placeholder, or stop.

```text
Grep <KIT PATH> with `^</?<ROLE TAG>>`. Require exactly two matches in opening-then-closing order. Use their line numbers to read only that inclusive range. Return blocked when either tag is missing, duplicated, reversed, indented, or decorated. Follow the extracted instructions using the values below. Read any other block the instructions name from the same file the same way. Write only the Output file and any file the instructions say to update.

Kit: <KIT PATH>
Role values: <ROLE VALUES OR NONE>
Scope: <SCOPE OR NONE>
Repo: <REPO PATH OR NONE>
Foundation: <FOUNDATION PATH OR NONE>
Spine: <SPINE PATH OR NONE>
Drafts: <DRAFT PATHS OR NONE>
Rule extract: <EXTRACT PATH OR NONE>
Output: <OUTPUT PATH>
```

- **Dispatch by reference.** Never copy, summarize, or paraphrase kit content into a dispatch. The kit is a byte-for-byte copy of this plan's tagged blocks.
- **Subagent setup.** Use subagent type `generalPurpose` and model `inherit`.
- **Parallelism.** Launch every subagent of a fan-out in one message. Wait for all of them to return before reconciling.
- **Checklist before a fan-out.** Write a numbered checklist of the fan-out's subagents and output files in `ledger.md`. Check off each subagent when its file exists and is non-empty.
- **One deliverable each.** Each subagent writes one output file, in full, on every run, so a re-run replaces it.
- **Small returns.** Each subagent returns status, counts, and the output path only, within these caps: 150 words for reviewers and triage, 200 for chapter fill and fix, 300 for coding.
- **Main context.** The main context holds this plan, the ledger, return lines, the triage, and review findings. It reads whole chapter drafts only in Steps 11 and 13. In Step 12 it reads only the items that findings cite.
- **Standing finding.** A finding stands when it shows any of these: a false fact, an invalid step, a hidden premise, an overreach, an axiom a reasonable reader could deny, wording that is not inert, WG21 history, or a name. Every finding, standing or rejected, goes in scratch `adversarial-log-draft.md` with its reason.
- **Regenerate, don't patch.** A chapter with more than eight standing findings in one round is re-filled from the spine, not patched.
- **Ledger.** `ledger.md` records the step checklist, each gate result, fan-out checklists, changes to the pre-digest, and each autonomous decision with its falsifier. A fresh context resumes by reading this plan and the ledger, then starting at the first step without a passed gate.

## Steps

<step-1>

### Step 1: Build the kit and the rule extract

- **Owner:** the main agent, by shell only. No subagent runs in this step.
- **Parallel:** none. Every later step reads these files.
- **Reads:**
  - this plan
  - the fetched SD-4 text at `C:\Users\Vinnie\.cursor\projects\c-Users-Vinnie-cursor\agent-tools\0fa9968a-f19a-4720-9cf1-495bb866ae5a.txt`; if that file is missing, re-fetch https://isocpp.org/std/standing-documents/sd-4-wg21-practices-and-procedures
  - `cabinet/_inbox/ISODirectives2026-part1.md`
- **Writes:** `support/kit.md`, `support/rules-extract.md`, the scratch folder, and scratch `ledger.md`.
- **Actions:**
  1. Create `wg21-papers/research/p4195/support/` and the scratch folder.
  2. Build `kit.md` with a script that copies every tagged block in the Shared blocks, Role blocks, Specs, Pre-digested analysis, and Candidate lists sections of this plan byte for byte, tag lines included. The script then requires exactly two unindented matches of `^</?TAG>` in `kit.md` for every tag.
  3. Build `rules-extract.md` with a script that copies source text, typing none of it by hand:
     - research frontmatter: `produced: 2026-10-18` and `title: SD-4 and ISO/IEC Directives Part 1 (2026) rule text for the WG21 incentive proof`
     - the SD-4 text, from its "SD-4: WG21 Practices and Procedures" heading to the end
     - these ISO clauses, each copied whole under a heading naming the clause: 0.7; 1.7; 1.8.2; 1.12.1 to 1.12.3; 2.1.6 and 2.1.7; 2.5.6 to 2.5.10; 2.6.2 to 2.6.5; 2.7.2 to 2.7.7; 3.1; 5.3.1; 5.4 to 5.7; 6.1 to 6.5
     - ISO clause boundaries: a clause starts at a line that opens with its bold dotted number, whether as a heading (`###### **2.6.3** ...`), a paragraph (`**2.5.7** ...`), or a list item (`- **2.7.2** ...`). It ends just before the next clause start whose number has as many parts or fewer (2.5.7 ends at 2.5.8, and 2.5.10 ends at 2.6), or before a top-level heading such as Annexes. A bold number without a dot, such as the page number `**39**`, is not a clause start. Page numbers and copyright lines inside a clause are copied as they are.
  4. Grep the extract for 25 quotes: every quoted anchor in the `pre-digest-foundation` block, plus "more than twice as many in favor", "not akin to a right to veto", and "may be asked for their reasons".
  5. Start `ledger.md` with the fourteen-step checklist.
- **Gate:** every tag passes the two-match check, and all 25 quotes are found.

</step-1>

<step-2>

### Step 2: Write build.py and patch Scrivener

- **Owner:** two coding subagents, then two code-review subagents.
- **Parallel:** with Step 3. The two coding dispatches and the Step 3 triage dispatch go in one message, then the two review dispatches go in one message.
- **Baseline:** before dispatch, run the Scrivener test command from `scrivener-spec` once and record its result line in the ledger.
- **Dispatch, coding:**
  - build script: role tag `coding-instructions`, Role values `spec=build-script-spec`, Repo `c:\Users\Vinnie\cursor\wg21-papers`, Output `wg21-papers/research/p4195/support/build.py`
  - Scrivener: role tag `coding-instructions`, Role values `spec=scrivener-spec`, Repo `c:\Users\Vinnie\cursor\wg21-paperworks`, Output `c:\Users\Vinnie\cursor\wg21-paperworks\packages\scrivener\scrivener\renderer.py`
- **Dispatch, review:** role tag `code-review-instructions`, with Role values `spec=` set to the same spec and Repo as the matching coding dispatch. Outputs are scratch `review-code-build.md` and `review-code-scrivener.md`.
- **Fix:** when a review returns findings, dispatch `coding-instructions` again with Role values `spec=<spec>; findings=<review file>`, then review once more. Stop after five fix rounds and report any open finding.
- **Gate:** both reviews are clean or every finding is closed, and both test commands named in the specs pass, apart from Scrivener failures already in the baseline.

</step-2>

<step-3>

### Step 3: Check the pre-digested triage

- **Owner:** one triage-check subagent, then the main agent.
- **Parallel:** with Step 2. Its dispatch goes in the same message as Step 2's coding dispatches.
- **Dispatch:** role tag `triage-check-instructions`, Rule extract `wg21-papers/research/p4195/support/rules-extract.md`, Output `wg21-papers/research/p4195/support/triage.md`.
- **Reconcile:**
  - Read `triage.md` in full.
  - Decide each disputed or missing-premise row from the extract text. Set its final verdict and append `main: <reason>`.
  - Record each change to the pre-digested foundation or spine in the ledger. Steps 4 and 7 apply those changes.
- **Gate:** no row is left disputed or missing premise.

</step-3>

<step-4>

### Step 4: Draft the foundation

- **Owner:** the main agent.
- **Overlap:** the main agent may draft from the `pre-digest-foundation` block while the Step 2 and Step 3 subagents run in the background. It applies the Step 3 changes once Step 3's gate passes, and runs build.py once Step 2's gate passes.
- **Reads:**
  - the `writer-register` block, adopted before drafting
  - the `pre-digest-foundation` block
  - `triage.md` and `rules-extract.md`
  - the `proof-style` and `proof-terms` blocks
  - the ledger
- **Writes:** scratch `01-foundation.md`, in keyed source format:
  - It starts with `## 1. Starting points`, followed by Axioms, Definitions, and Facts.
  - Facts are grouped under one parent per source section, with each quoted rule as a lettered child.
  - Every quote is copied from the extract.
- **Actions:** apply the ledger changes from Step 3, then run `build.py check --mode foundation` over `01-foundation.md`.
- **Gate:** build.py passes.

</step-4>

<step-5>

### Step 5: Review the foundation

- **Owner:** four review subagents in one message, then the main agent. The foundation has no derived items, so the logician is not dispatched.
- **Checklist:** list the four reviews in the ledger first.
- **Dispatch:** every dispatch uses Scope `all`, Foundation and Drafts `01-foundation.md`, and Rule extract `support/rules-extract.md`.
  - `rules-check-instructions`, Output scratch `review-foundation-rules.md`
  - `reader-instructions`, Output scratch `review-foundation-reader.md`
  - `skeptic-instructions`, Role values `readers=design room chair; convenor; author of a large proposal`, Output scratch `review-foundation-skeptics-a.md`
  - `skeptic-instructions`, Role values `readers=employer standards lead; C++ user; national body head`, Output scratch `review-foundation-skeptics-b.md`
- **Reconcile:**
  - Read all four files in full.
  - Apply each standing finding to `01-foundation.md` with the weakest fix that resolves it.
  - Log every finding.
  - Rerun build.py.
- **Gate:** every standing finding is applied and logged, and build.py passes.

</step-5>

<step-6>

### Step 6: Checkpoint 1

- **Owner:** the main agent. Stop and wait for the user.
- **Present:**
  - the foundation with labels in place of keys, emitted to scratch `foundation-labeled.md` by `build.py --mode foundation --emit`
  - the triage counts
  - every change made to the pre-digest, and why
- **Gate:** user approval. Apply the user's changes, then rerun Step 5 on the changed items only.

</step-6>

<step-7>

### Step 7: Write the spine

- **Owner:** the main agent.
- **Reads:** the `writer-register` block (adopted before drafting), the approved `01-foundation.md`, the `pre-digest-spine` block, `triage.md`, and the ledger.
- **Writes:**
  - scratch `02-spine.md`, in keyed source format, which holds:
    - for chapters 2 to 12, each chapter heading and every top-level item, with its kind, statement, and key, and its intended basis written as `*[from ...]*`
    - the children of `m:moves`, keyed `m:moves-<player>`, and the children of `c:predictions` and `c:levers`, keyed `c:pred-<topic>` and `c:lever-<topic>`, which keeps the whole proof within 150 top-level items
    - each table's caption, row labels, and column labels, in the table format, with the ranks left blank
    - the Theorem draft
  - scratch `02-incentive-map.md`, one line per candidate incentive, mapping it to a spine key or marking it a conjecture. This file is kept separate so the spine stays parseable.
- **Actions:**
  1. Run `build.py check --mode spine` over `01-foundation.md` and `02-spine.md`. Resolve each uncited item it reports by citing it from a later item, usually a chapter 11 lemma or a chapter 12 corollary, or by cutting it and recording the cut in the ledger.
  2. Modularize. List each spine item's direct citers. Where a group of consecutive items in one chapter is cited only from inside the group, except its last item, make the last item a top-level item and the others its lettered children, cited by `*[proved by ...]*`; the last item keeps `*[from ...]*` for any earlier items it also rests on. Keep a module only when it has one clear conclusion, rests on few outside items, has its conclusion cited from outside it, and fits the three numbering levels; leave a chain flat when it reads better flat. Record each module in the ledger with its conclusion and the outside items it rests on.
  3. Rerun build.py.
- **Gate:** build.py passes, with no uncited items and at most 150 top-level items, and each module's inner items are cited only inside its module.

</step-7>

<step-8>

### Step 8: Review the spine

- **Owner:** four review subagents in one message, then the main agent.
- **Checklist:** list the four reviews in the ledger first.
- **Dispatch:** every dispatch uses Scope `all`, Foundation `01-foundation.md`, Spine and Drafts `02-spine.md`, and Rule extract `support/rules-extract.md`. The four dispatches:
  - `logician-instructions`
  - `reader-instructions`
  - `skeptic-instructions`, with the skeptics A readers from Step 5
  - `skeptic-instructions`, with the skeptics B readers from Step 5
  
  Outputs are scratch `review-spine-<role>.md`.
- **Spine rule for the logician:** judge each spine statement as if its intended basis were already proved.
- **Reconcile:** the same as Step 5, applied to `02-spine.md`.
- **Gate:** the same as Step 5.

</step-8>

<step-9>

### Step 9: Spine freeze

- **Owner:** the main agent. Do not wait for the user or ask for sign-off.
- **Before freezing:**
  1. Fetch the current consolidated JTC 1 Supplement. Copy into `support/rules-extract.md`, under a heading naming each clause, every JTC 1-specific clause on working groups, consensus, sustained opposition, records and minutes, voting, and appeals. Rerun every absence search over the added text, update the absence facts, `f:absences`, and the chapter 1 recap, and add a fact for any rule the Supplement adds. The fetched text is research.
  2. Fetch INCITS's procedures and check whether INCITS counts one vote per member organization when it forms a national position. If it does, add that as a fact under its own source and cite it in `p:nb-members`; if not, or if the text cannot be found, keep `p:nb-members` conditional on each national body's own rules. The fetched text is research.
  3. Rerun `build.py check --mode spine`.
- **Record in the ledger:**
  - the spine with labels in place of keys, emitted to scratch `spine-labeled.md` by `build.py --mode spine --emit` over `01-foundation.md` and `02-spine.md`
  - the Theorem draft
  - the incentive mapping
  - each open question, with the main agent's decision and its falsifier
- **Gate:** the record is written and build.py passes. The spine is then frozen for subagents. Only the main agent changes a spine statement, in Steps 11 to 13, and it keeps `02-spine.md` and the chapter file holding the statement in agreement.

</step-9>

<step-10>

### Step 10: Fill the chapters

- **Owner:** eleven chapter-fill subagents, one per chapter 2 to 12, all launched in one message.
- **Checklist:** list the eleven chapters and their output files in the ledger first.
- **Dispatch, each:**
  - role tag `chapter-fill-instructions`
  - Role values `chapter=<N>`
  - Foundation `01-foundation.md`, Spine `02-spine.md`, Rule extract `support/rules-extract.md`
  - Output scratch `ch-<NN>.md`
- **Gate:** eleven non-empty files exist, and the ledger lists every weakened key.

</step-10>

<step-11>

### Step 11: Integrate

- **Owner:** the main agent, plus a refill fan-out if needed.
- **Actions:**
  1. Add the items under Decisions, "Step 11 additions", and any the D4195 support report marks provable, each with its basis, and treat them as spine changes. For each weakened key, decide whether the spine adopts the weaker statement. Run `build.py --dependents <keys>` over `01-foundation.md` and `02-spine.md`, and adjust each dependent spine statement so that it still follows.
  2. If any spine statement changed, re-dispatch `chapter-fill-instructions`, in one message, for every chapter that holds a changed item or a dependent. If a refill reports new weakened keys, repeat action 1 and this action, up to three refill rounds in all; after the third, the main agent makes any later change itself.
  3. Collapse obvious proofs (the common-sense filter). Where a top-level item or spine child restates or joins the items it cites, or follows from them in one step a committee member accepts on sight, delete its lemmas and steps, keep its statement, and give it a `*[from ...]*` citation naming the items the deleted children cited. Keep the children of any item that weighs values, counts votes in more than one step, joins items from different chapters, or is a table rank, a settled lemma, the Theorem, or a corollary. Point any citation of a deleted child at its parent, and record each collapsed item in the ledger. Then, per the dysfunction focus, cut any item that proves normal or well-known practice when every item that cites it can cite that item's own basis instead; re-point those citations, starting with chapters 2 and 3.
  4. Sharpen. Rewrite every spine item and chapter statement under the sharpness rules in `proof-style`: the sharpest true claim first; conditions moved into definitions, captions, or the author types; no qualifier the claim does not need; at most 30 words; plain words a reader outside the committee understands, in the positive form wherever it states the same claim, and worded to be worth reading. Every rewrite keeps its claim exactly; the ledger records any statement whose claim had to change, as a weakening. Replace each result that holds by definition, such as "does better when it is worth more", with what makes it true: which costs and gains fall on whom, and when. Keep every condition a Step 8 finding showed to be needed, but move it out of the main clause where possible. Open each chapter with its sharpest proved conclusion, using the D4195 conclusions the support report marks PROVED or PROVABLE where they fit, and write the Theorem's consequences as short declarative sentences. Mirror changed spine statements in `02-spine.md`, and take a `step-11-pre-sharpen` snapshot first.
  5. Run the module pass of Step 7 again, over the foundation and the chapter files. Fold a group into its last item only when every folded item's own proof fits one level below it; otherwise mark the group with a `### ` heading that names its conclusion. Mirror each fold in `02-spine.md`, and record each module and heading in the ledger.
  6. Run `build.py check --mode full` on the foundation and all chapters, with `--max-items 200` until actions 3 to 5 are done and with the final cap after them (Decisions, "Item cap").
- **Gate:** build.py passes, with no orphans, no unknown keys, and no forward citations; each module's inner items are cited only inside its module; actions 3 and 4 have been applied to every chapter; and the top-level count is at or under the final cap, which the ledger records.

</step-11>

<step-12>

### Step 12: Verify

- **Owner:** five reviewers per round in one message, then the main agent, then fix subagents in one message.
- **Scope:** round 1 is `all`. Each later round covers the keys changed in the previous round plus everything `build.py --dependents` lists for them, run over `01-foundation.md` and the chapter files, never with `02-spine.md`, which would define every spine key twice. A chapter that was re-filled is in scope whole.
- **Dispatch, reviewers:** five reviewers: the four from Step 5 plus `logician-instructions`. Drafts are the foundation and every chapter file. Outputs are scratch `review-r<R>-<role>.md`. For rounds after the first, Scope lists the keys.
- **Reconcile:** the same as Step 5, except for the choice of fix (user, 2026-10-19 13:14: "we're on the way to weakening literally everything"). For each standing finding, apply the fix that keeps the most force while making the claim true, in this order: (1) a scope or definition stated once, such as the 2:1 norm's "normally" or what "the rules" covers, so each sentence keeps its plain claim; (2) an added premise or fact that passes the five-part test; (3) a narrower subject (who or when); (4) weaker wording, only when the claim is false as stated. Reject a finding that is true but immaterial, an edge case a reader supplies without changing the conclusion, and log the reason. Track how many claims each round weakens; a round that weakens a headline result, a settled lemma, or the Theorem names it in the ledger. The main agent applies standing findings on foundation items itself and lists each in the ledger, since the user approved the foundation at Checkpoint 1. Then split the other standing findings by chapter into scratch `fix-r<R>-ch<NN>.md`.
- **Dispatch, fixes:** for every chapter with standing findings, use role tag `fix-instructions` with:
  - Role values `findings=fix-r<R>-ch<NN>.md`
  - Foundation `01-foundation.md`, Spine `02-spine.md`
  - Drafts and Output both set to that chapter's file
  
  A chapter with more than eight standing findings that need new proof steps (an invalid step, a hidden premise that needs a new lemma, or a changed spine statement whose children must change) gets `chapter-fill-instructions` instead, with Role values `chapter=<N>; findings=fix-r<R>-ch<NN>.md`. Wording findings (long, negative, hedge, judging word, figure of speech, term, dull, motive) do not count toward the eight, because a refill rewrites the whole chapter and puts all of it back in scope (main agent, 2026-10-19 13:20).
- **After the fixes:** the main agent applies any fix deferred to the spine and reruns build.py.
- **Loop:** repeat for up to five rounds, stopping after a round with no standing finding. Any dispute still open after round five goes to Appendix B, tied to the axiom or fact it turns on.
- **Gate:** build.py passes, and every standing finding is applied or logged.

</step-12>

<step-13>

### Step 13: Finish

- **Owner:** the main agent, then five reviewers in one message, then the main agent again.
- **Actions:**
  0. Adopt the `writer-register` block before writing anything in this step.
  1. Rewrite the Theorem in chapter 11 as one or two paragraphs. Tie every clause to a cited item, and end with ∎.
  2. Compactness: run build.py, cut every orphan, merge items that say the same thing, and rerun. Record each cut and merge in the ledger. This comes before the front matter and appendices so that they cite only surviving keys.
  3. Write scratch `00-front.md`, which holds:
     - **working title:** it states the result
     - **abstract:** 150 to 250 words. The first sentence states the settled pattern. The next two or three sentences give the most striking proven results, each with its rule basis. It closes by saying the proof uses only SD-4 and the ISO/IEC Directives, names no one, and cites no incident.
     - **How to read this proof:** item kinds, citation forms, labels, and table ranks
  4. Write scratch `13-appendices.md`, which holds:
     - **A:** a crosswalk mapping the original 14 assumptions, the 45 candidate incentives, and the 34 candidate facts to their labels or to the reason each was cut. Build it from the `original-assumptions`, `candidate-incentives`, `candidate-facts`, and `pre-triage` blocks (the `pre-triage` rows A1 to A14 are the draft crosswalk for the original assumptions), `triage.md`, scratch `02-incentive-map.md`, and the ledger's cuts and merges, writing citations as keys so build.py turns them into labels.
     - **B:** the hardest objections and how each was resolved, plus any open dispute
     - **C:** a glossary built from `proof-terms`
     - **D:** references: SD-4 (2026-05-11) with its URL; the ISO/IEC Directives Part 1, 2026; and Lamport, "How to Write a Proof," marked as cited from memory
  5. Dispatch the five reviewers from Step 12. Set Drafts to `00-front.md`, `13-appendices.md`, and every chapter file, and Scope to `00-front.md, 13-appendices.md, thm:settled` plus every key that compactness changed. Reconcile as in Step 5.
  6. Run `build.py check --mode full --front 00-front.md --appendix 13-appendices.md` over the foundation and all chapters.
- **Gate:** build.py passes, including the front matter and appendices, and none of the reviewed text has a standing finding.

</step-13>

<step-14>

### Step 14: Assemble and render

- **Owner:** the main agent, by shell.
- **Actions:**
  1. Run `build.py --mode full --emit c:\Users\Vinnie\cursor\wg21-papers\research\p4195\wg21-game-theory.md --front 00-front.md --appendix 13-appendices.md --footer "YYYY-MM-DD HH:MM - <model name> (Cursor agent)"` over `01-foundation.md` and `ch-02.md` to `ch-12.md`, in order. The emit runs every check first, including the forbidden-string check on the front matter and appendices, and writes nothing if one fails. The emitted file has no frontmatter.
  2. Copy the keyed source files into `support/source/`. Write `support/adversarial-log.md` from the scratch log, with research frontmatter.
  3. Render the final file through the patched Scrivener to a scratch PDF with `c:\Users\Vinnie\cursor\wg21-paperworks\.venv\Scripts\scrivener.exe <file> -o <pdf>`, which is the `packages/scrivener/README.md` command run through the venv instead of `uv run`. With pypdfium2 from the paperworks venv, find the page where chapter 2 starts and the page that holds Table 1 by searching the PDF text, then convert those two pages and the first page to PNG and view them. Confirm three things: the 1 / a / i levels, numbering that continues across headings, and readable tables.
  4. Set every todo status in this plan to `completed`, then report to the user.
- **Gate:** the emit in action 1 passes every check, no payoff table has a blank cell, and the three pages show correct numbering and readable tables.

</step-14>

## Plan review

These checks were run against the steps above. The most recent pass checked whether a fresh context could execute the plan.

- **Fresh-context check:** a reader who saw none of the planning conversation finds all of this in the plan:
  - the purpose and emphasis (Background)
  - every user decision (Decisions already made)
  - absolute paths, the shell, the Python to use, and how to start or resume
  - the original 14 assumptions for the crosswalk
  - the full instruction text for every subagent role
  - specs for both code changes
  
  Fixes made in that pass:
  - absolute paths
  - the build.py usage line and its `--extract` option
  - an orphan rule that keeps a parent grouping Facts from being flagged
  - whole-word matching for forbidden words
  - reviewer handling of text without keys
  - a separate incentive map, so the spine stays parseable
  - an explicit file scope for `--dependents` in Step 11
  - no logician in the foundation review, since the foundation has no derived items

- **Data flow:**
  - Step 1 produces the kit, the extract, the folders, and the ledger.
  - Step 2 needs only the kit. Step 3 needs the kit and the extract.
  - Step 4 needs build.py from Step 2 and the triage from Step 3.
  - Each step from 5 to 14 reads only files that earlier steps produced.
  - No step depends on anything that exists only in conversation: the pre-digest, every user decision, the sealed-history rule, and the file locations are all in this plan.
- **Parallel work:**
  - Steps 2 and 3 run together, as do the coding and review pairs inside Step 2.
  - The reviewers run in parallel in Steps 5, 8, 12, and 13.
  - The eleven chapter fills run in parallel in Step 10, and so does any refill in Step 11.
  - The fix subagents run in parallel in Step 12.
- **Combined:** the earlier separate extract, kit, and dependency-check steps became Step 1 plus a build.py run at every gate.
- **Load per step:** most steps have one deliverable. Step 2 has two independent halves that run in parallel, and Steps 7, 13, and 14 each produce several files in sequence.
- **Ambiguity:** each of these terms has one definition: "standing finding," "orphan," "weakened," and "changed key." Every output path is fixed, and every return has a word cap.
- **Risks and their handling:**
  - **Duplicate lemmas across chapters:** the spine places each shared statement in the earliest chapter that needs it, and chapter fill forbids re-proving an earlier chapter's spine statement.
  - **Cascading weakened statements:** Step 11 runs `--dependents` and allows up to three refill rounds, and the main agent handles anything beyond that.
  - **Review volume:** after round 1, reviewers see only changed items and their dependents.
  - **A missing SD-4 file:** Step 1 re-fetches it.
  - **False quote failures:** build.py normalizes whitespace and curly quotes before comparing.
  - **Main context growth:** returns are capped, and the main agent reads chapter drafts only in Steps 11 and 13.
- **Practices adopted from the planning tools and the how-to:**
  - dispatch by reference to tagged blocks
  - one deliverable per subagent
  - a checklist before each fan-out
  - parallelism stated explicitly
  - separate finder and challenger subagents
  - a mechanical gate (build.py, including forbidden strings)
  - no/yes pairs and vocabulary replacements
  - regenerating a chapter instead of patching it
  - a ledger for resuming
  - the plan as the canonical source
- **Run-readiness pass (2026-10-18):** a review against the actual input files before Step 1. Fixes made:
  - ISO clause boundaries for clauses that are bold paragraphs rather than headings, and a 25-quote gate in Step 1
  - build.py: continued items, prose lines, table separator rows, a top-level item cap, uncited spine items in spine mode, checks on the front matter and appendices, and a blank line before a list that follows a table
  - proposal sizes reduced to small and large at the user's direction
  - Step 13 compacts before writing the front matter and appendices, and its review covers the appendices and sees every chapter
  - render check pages that show a chapter boundary and a table
  - the spine-change rule after the Step 9 freeze, Step 12's foundation findings, the files for `--dependents`, and re-fills that see their findings
  - an exception to "Name no person" for the references list, and Scrivener commands run through the venv with a test baseline

## Shared blocks

<writer-register>

You are an institutional economist laying out a formal proof, in plain English, for the C++ committee members it describes: every sentence must be one they accept on first reading, even when they dislike where the proof leads.

</writer-register>

<proof-style>

- Every sentence states one plain thing that a reader of any affiliation accepts on sight, or that follows directly from the items it cites. Model: "Attending a meeting in person costs money." No sentence argues; the sequence of sentences brings the reader to the conclusion.
- Motives enter only through the axioms. `ax:prefer` gives every player in a role the same motive, and every sentence about what a player prefers follows from it, for example: "A regular who values their standing does better voting Neutral than Against."
- Never give a person or group a motive, belief, or intent beyond what the axioms give every player in that role. Never suggest bad faith. Never say what players actually do; say what the rules reward a player who holds the axiom's values.
- Write each item as one sentence. Use two only when one sentence would pass 30 words. The Theorem is the one exception: it runs one or two paragraphs. Lead with the sharpest true claim in plain words, and put conditions in definitions, table captions, or the author types rather than in the sentence; use a qualifier such as unless, though, only when, or in part only when the claim is false without it. Never state a result that holds by definition, such as that a player does better with an option worth more to it; state what makes the option worth more or less: which costs and gains fall on whom, and when. Write so a reader outside the committee understands and wants to read on: concrete subjects, active verbs, short sentences, and the positive form whenever it states the same claim. Keep a negative only when the claim is an absence or a prohibition, where a positive form would claim more. Never change a claim to make it plainer or livelier.
- Open each item with its kind in bold: `**Axiom.**`, `**Definition.**`, `**Fact.**`, `**Lemma.**`, `**Inference.**`, `**Induction.**`, `**Proposition.**`, `**Corollary.**`, or `**Theorem.**`. Roman-level steps take no kind.
- Axioms and Definitions take no basis. A Fact quotes the rule word for word in straight double quotes, then gives its source in parentheses, for example `(SD-4, "Subgroup responsibility and polls")` or `(ISO/IEC Directives Part 1, 2.5.7)`. A Fact that states what a document does not contain names the terms searched, for example `(SD-4, whole document; searched: record, reason, answer)`. Quote whole sentences; use `...` only where the sentence names a WG21 paper or a person or crosses a page break, and set any quotation inside the quote in curly marks.
- When a quoted passage crosses a page number or copyright line in the rule extract, split the quote with `...` at that point.
- End every other item with its basis in italics: `*[from KEY, KEY]*` for earlier items, `*[proved by KEY, KEY]*` for the item's own children only, or both when it rests on both.
- End every item with its key: `{#KEY}`. Use the prefixes `ax:`, `d:`, `f:`, `l:`, `inf:`, `ind:`, `p:`, `c:`, `t:`, `m:`, `thm:`.
- Write every list marker as `1.`. Indent a level-2 item 3 spaces and a level-3 item 6 spaces.
- Use the term `proof-terms` assigns to each concept, and no synonym.
- Never write these words outside quotations; write the replacement instead:
  - "perverse": state what the rule rewards.
  - "railroad" or "steamroll": "declare consensus while some participants vote Against."
  - "capture" or "dominate": "provide most of the participants in."
  - "exploit" or "gaming": "use."
  - "stack the room": "send more participants to the room."
  - "punish" or "retaliate": "support less readily."
  - "insider": "regular." "outsider": "newcomer."
  - "lock-in": "the cost of reversal."
  - "cliff": "the feature cutoff."
  - "kill" or "die", said of a proposal: "stop advancing."
  - "obviously," "clearly," "of course": delete.
  - "door," "carry": rephrase.
- No figures of speech, no em dashes, no double dashes.
- No and yes:
  - No: "Chairs push proposals through over objections." Yes: "A chair may declare consensus while some participants vote Against."
  - No: "Authors bury objections." Yes: "Nothing in SD-4 requires the record to show how an objection was answered."
  - No: "Big companies flood the room." Yes: "SD-4 sets no limit on how many participants paid by one sponsor may vote in a subgroup poll."
  - No: "Objectors are punished." Yes: "A participant who votes Against a colleague's proposal cannot rule out that the colleague will support the participant's own proposals less readily."
  - No: "Authors want to avoid scrutiny." Yes: "An author who values adoption does better when fewer participants vote Against."
- End each chapter with `In plain terms:` and at most three sentences that restate proven items and add nothing.

</proof-style>

<proof-terms>

- participant: a registered expert attending a WG21 meeting.
- regular: a participant who expects to attend future meetings with the same colleagues.
- newcomer: a participant attending for the first time.
- author: a participant who presents a proposal paper as one of its authors.
- sponsor: an organization that pays some or all of a participant's costs of taking part.
- user: a person who writes C++ and does not participate.
- design room: EWG or LEWG. study group: any WG21 study group. wording room: CWG or LWG. subgroup: any of these. plenary: the closing plenary session of a WG21 meeting.
- chair: the chair of a subgroup. convenor: the WG21 convenor.
- national body: an ISO member body that is a P-member of SC22.
- Favor, Neutral, Against: poll positions as SD-4 capitalizes them; Strongly Favor and Weakly Favor count as Favor, and likewise for Against.
- the 2:1 norm: SD-4's statement that a proposal normally advances when more than twice as many are in favor as against.
- consensus call: a chair's or the convenor's determination of consensus.
- direction poll: a poll on whether to continue work on a design. forwarding poll: a poll to send a proposal to the next room.
- incumbent: the design on a topic that has passed a direction poll in a subgroup.
- edition: one published version of the C++ standard. feature cutoff: the last meeting at which a new feature can be approved for an edition.
- reversal: removing or replacing something the committee has approved.
- standing: the readiness of colleagues to support a participant's future proposals.
- stake: the difference a poll's outcome makes to what a player values.
- small proposal, large proposal: as defined in the foundation.
- settled pattern: a set of choices, one per player, in which no player improves their own position by changing only their own choice; game theory calls this a Nash equilibrium.

</proof-terms>

<payoff-table-format>

- Use 2 rows by 2 columns, or 3 rows by 2 columns when a player has three choices.
- In a two-player table, rows are the first player's choices and columns the second player's choices; each cell holds "first player's rank, second player's rank."
- In a one-player table, rows are the player's choices and columns are situations; each cell holds the player's rank of that choice in that situation.
- Ranks are whole numbers. A player's best outcome gets the highest number, equal to the number of outcomes that player ranks, and the worst gets 1.
- Row and column labels have at most three words. Bold each cell where the settled pattern lies. In a two-player table, also put a dagger (†) after the ranks of each Pareto-optimal cell, one for which no other cell gives one player a higher rank without giving the other a lower one, and say so in the caption.
- Prove every rank comparison as a lemma above the table. Below the table, write one line holding only the citation of those lemmas.
- Worked example, with invented ranks, showing format only:

*Table: Two regulars, each with a proposal pending. First number: A's rank. Second number: B's rank. 4 is best. † marks a Pareto-optimal cell.* {#t:example}

| | B supports | B opposes |
|---|---|---|
| **A supports** | **4, 4** † | 2, 3 |
| **A opposes** | 3, 2 | 1, 1 |

*[from l:example-a, l:example-b]*

</payoff-table-format>

<sealed-history-rule>

- Use no event, meeting, poll result, paper number, feature history, or person from WG21's past as support for any item.
- Structural facts are allowed: the rooms and roles that exist, the three-year schedule, and that implementers build compilers and libraries.
- Illustrations are invented and labeled as invented.
- Name no person, except an author in the references list. Name no WG21 paper except SD-4.

</sealed-history-rule>

## Role blocks

<triage-check-instructions>

You check a pre-digested triage of two candidate lists against the rules. You did not write the triage.

Read these blocks from the Kit file, each by its tag pair: `pre-triage`, `candidate-facts`, `candidate-incentives`, `pre-digest-foundation`, `pre-digest-spine`, and `sealed-history-rule`. Read the Rule extract in full.

For each candidate fact F1 to F34 and each candidate incentive I1 to I45:

1. Read its pre-triage verdict and destination.
2. When the verdict rests on a rule, find the rule text in the extract and record the section and the quote's first eight words. When the text is absent or says something else, mark the row `disputed` and state what the extract says.
3. When the verdict is Axiom, ask whether a reader of any affiliation would deny the axiom as worded in `pre-digest-foundation`. If one would, propose a weaker wording.
4. When the verdict is Prove or Weaken, check that the destination statement in `pre-digest-spine` follows from its intended basis. If a needed premise is missing, mark the row `missing premise` and state the premise.
5. When a row's only support is WG21 history, change it to Dropped for a fact or Conjecture for an incentive.

Write one row per candidate to the Output file in this form: `ID | pre-triage verdict | final verdict | destination key or reason | source section and quote start | note`. Write the file in full.

Return only done or blocked; the counts of rows agreed, disputed, missing premise, and changed to Dropped or Conjecture; and the output path, within 150 words.

</triage-check-instructions>

<chapter-fill-instructions>

You are an institutional economist laying out a formal proof, in plain English, for the C++ committee members it describes: every sentence must be one they accept on first reading, even when they dislike where the proof leads.

You write the proof for one chapter. You prove the chapter's spine statements; you never change them.

Read these blocks from the Kit file, each by its tag pair: `proof-style`, `proof-terms`, `payoff-table-format`, and `sealed-history-rule`. Read the Foundation file and the whole Spine file. Read the Rule extract when a step needs a rule. The chapter number is `chapter=` in Role values. When Role values also name `findings=`, read that file and write the chapter so that none of those findings applies to it.

1. Copy the chapter's heading line and each of its spine items, top-level items and the children the spine gives them alike, word for word, in spine order, with their keys.
2. Under each top-level item that has no spine children, write the lettered lemmas that prove it, with roman steps where a lemma needs more than one link; under each spine child, write the roman steps that prove it. A child may cite only foundation items, spine items of earlier chapters, earlier items of this chapter, or its own children. Write no children for an item that only restates what it cites, or follows from it in one step a committee member accepts on sight; its `*[from ...]*` citation is its proof. Always prove a settled lemma, the Theorem, a table rank, a corollary, and any item that joins results from different chapters, however short its proof.
3. Give each parent a `*[proved by ...]*` citation naming its children, and keep `*[from ...]*` for any earlier items it also rests on, or alone when earlier items alone prove it.
4. Give every new item a key with the right prefix. Never re-prove a statement that a spine item of an earlier chapter states; cite that item instead.
5. For each table the spine assigns to this chapter, prove each rank comparison as a lemma, then write the table as `payoff-table-format` specifies.
6. End the chapter with `In plain terms:` and at most three sentences.
7. When a spine statement cannot be proved from the items you may cite, leave it unchanged. Write the strongest statement you can prove as a child marked `{#KEY weakened}`, and report the original key.

Write the chapter to the Output file, starting at byte zero with the heading line. Write the file in full.

Return only done or blocked; the counts of spine items proved, spine items weakened, and new items; the weakened keys; and the output path, within 200 words.

</chapter-fill-instructions>

<logician-instructions>

You check that every derived item follows from the items it cites, and from nothing else.

Read `proof-style` and `proof-terms` from the Kit file by their tag pairs. Read the Foundation file and every Drafts file. Check the keys or files Scope names, or everything in the Drafts files when Scope is `all`. For text without a key, such as the abstract or an appendix, write `front` or `appendix` plus the paragraph number in place of KEY.

For each derived item in scope, ask in order:

1. Taken as true, do the cited items make this statement true?
2. Does the statement rely on a fact, assumption, or term that no cited item supplies? That is a hidden premise.
3. Is the statement stronger than its basis, for example "always" where the basis supports "can"?
4. Does a citation point forward, other than `*[proved by ...]*` naming the item's own children?
5. In a table, does every rank follow from the lemmas the table cites?

Write one finding per failure to the Output file, at most three sentences, in this form: `KEY | type (invalid step, hidden premise, overreach, forward citation, table rank) | the problem | the fix that keeps the most force: a scope or definition stated once, an added cited premise, a narrower subject, or weaker wording or a cut only if the claim is false as stated`. A claim that is true but omits an edge case a reader supplies without changing the conclusion is not a failure. Write nothing for items that pass. Write the file in full.

Return only done or blocked, finding counts by type, and the output path, within 150 words.

</logician-instructions>

<rules-check-instructions>

You check every Fact, and every sentence that describes a rule, against the rule extract.

Read `proof-style` and `sealed-history-rule` from the Kit file by their tag pairs. Read the Rule extract in full and every Drafts file. Check the keys or files Scope names, or everything in the Drafts files when Scope is `all`. For text without a key, such as the abstract or an appendix, write `front` or `appendix` plus the paragraph number in place of KEY.

For each item in scope:

1. For a Fact that quotes, confirm the quoted text appears in the extract under the section named, and that the item claims only what the quoted text says.
2. For a Fact that states what a document does not contain, search the whole document for the named terms and for their synonyms, and list the terms you searched.
3. For any other item that states what SD-4 or the ISO Directives require, permit, or omit, find the text that supports it.

Write one finding per failure to the Output file in this form: `KEY | type (misquote, wrong section, unsupported rule claim, unsupported absence claim) | what the extract says | fix`. Write the file in full.

Return only done or blocked, finding counts by type, and the output path, within 150 words.

</rules-check-instructions>

<reader-instructions>

You read every sentence as a committee member checking it for fairness, plain wording, and sharpness.

Read `proof-style`, `proof-terms`, and `sealed-history-rule` from the Kit file by their tag pairs. Read every Drafts file. Check the keys or files Scope names, or everything in the Drafts files when Scope is `all`. For text without a key, such as the abstract or an appendix, write `front` or `appendix` plus the paragraph number in place of KEY.

For each sentence in scope, ask:

1. Would a reader of any affiliation accept it on sight, or see that it follows from what it cites? Is it the sharpest true statement: no qualifier the claim does not need, no condition a definition or caption could hold, at most 30 words, not true by definition, and worth a proof rather than obvious? A plain, sharp statement of what the rules reward is inert; do not soften it. Would a person outside the committee understand it and find it worth reading, and is it in the positive form wherever that states the same claim?
2. Does it use a word on the forbidden list, any other word that judges, or a figure of speech?
3. Does it give a person or group a motive, belief, or intent beyond what `ax:prefer` gives every player in that role, suggest bad faith, or claim what players actually do?
4. Does it mention a WG21 event, meeting, poll result, paper other than SD-4, feature history, or person?
5. Does it use a term other than the one `proof-terms` assigns to that concept?

Write one finding per failure to the Output file in this form: `KEY | type (not inert, judging word, figure of speech, motive, history, name, term, hedge, tautology, obvious, long, negative, dull) | the words at issue | an inert rewrite that keeps the claim exactly, or "cut" for an obvious item`. Write the file in full.

Return only done or blocked, finding counts by type, and the output path, within 150 words.

</reader-instructions>

<skeptic-instructions>

You read the proof as each reader named by `readers=` in Role values, one reader at a time. Each reader wants to reject the conclusion, and looks for any sentence they can honestly deny.

Read `proof-style` and `proof-terms` from the Kit file by their tag pairs. Read the Foundation file and every Drafts file. Check the keys or files Scope names, or everything in the Drafts files when Scope is `all`. For text without a key, such as the abstract or an appendix, write `front` or `appendix` plus the paragraph number in place of KEY.

For each reader, decide accept or object for each sentence in scope. Object only when the reader can name a concrete reason the sentence is false, unsupported, or incomplete in a way that changes a later conclusion. Also record any check in the rules that limits an effect a sentence describes, when the proof does not already state that check.

Write one finding per objection to the Output file in this form: `KEY | reader | the objection | the change that keeps the most force and would make the reader accept the sentence: a scope stated once, an added cited fact or premise, a narrower subject, or weaker wording only if the sentence is false as written`. An objection that a reader would drop once they saw the scope or definitions the proof states elsewhere is not an objection. Write the file in full.

Return only done or blocked, objection counts by reader, and the output path, within 150 words.

</skeptic-instructions>

<fix-instructions>

You are an institutional economist laying out a formal proof, in plain English, for the C++ committee members it describes: every sentence must be one they accept on first reading, even when they dislike where the proof leads.

You apply reconciled fixes to one chapter.

Read `proof-style`, `proof-terms`, `payoff-table-format`, and `sealed-history-rule` from the Kit file by their tag pairs. Read the findings file named by `findings=` in Role values, the Drafts file (the chapter), the Foundation file, and the Spine file.

For each finding in order, apply its fix and keep the item's key. When a fix weakens a statement, edit only that statement and its own children. When a fix would change a spine statement, do not apply it; report the key instead. Close each finding by appending ` | fixed` or ` | rejected: <reason>` to its line in the findings file.

Write the chapter file in full to the Output file.

Return only done or blocked; the counts fixed, rejected, and deferred; the changed keys; the deferred keys; and the output path, within 200 words.

</fix-instructions>

<coding-instructions>

You implement one specified change with its tests. Nothing else.

Read the spec block named by `spec=` in Role values from the Kit file by its tag pair. When Role values also name `findings=`, read that file and fix its open findings instead of starting over. Close each finding by appending ` | fixed: <how>` or ` | rejected: <reason>`.

Write only the files the spec names or asks for, including its tests and fixtures. Write the tests first, run them, and confirm they fail. Then implement until they pass. Run the spec's full test command. Leave every change uncommitted; never run git add, git commit, git stash, or any command that rewrites history.

Return only done or blocked, the files touched, the test command, and its result line, within 300 words.

</coding-instructions>

<code-review-instructions>

You review one uncommitted change against its spec. You did not write it. You write findings; you never fix.

Read the spec block named by `spec=` in Role values from the Kit file by its tag pair. In the Repo, run `git status --short` and `git diff` (both read-only), and read every untracked file the spec names, including every file in a folder it names. Judge by reading; do not run code or tests.

Ask in order: Does the change do what the spec says? Does it do anything the spec does not say? Does every new behavior have a test that would fail if the behavior broke? Is any error swallowed? Is any code dead?

Write one finding per failure to the Output file, at most three sentences, naming the file and symbol. Write the file in full.

Return only clean or the finding count, and the output path, within 150 words.

</code-review-instructions>

## Specs

<scrivener-spec>

- Repo: `c:\Users\Vinnie\cursor\wg21-paperworks`, package `packages/scrivener`.
- Change 1: in `scrivener/renderer.py`, method `_render_list`, set `bulletType` for an ordered list from its depth: depth 0 gives `"1"`, depth 1 gives `"a"`, depth 2 gives `"i"`, and deeper levels repeat that cycle. Keep `bulletFormat` `"%s."` and the start number. Make the label-width reservation measure the widest label in the list's own style. Unordered lists do not change.
- Change 2: add `ol ol { list-style-type: lower-alpha; }` and `ol ol ol { list-style-type: lower-roman; }` to the stylesheet that `scrivener/css.py` generates, with the same selector prefix as its other rules, and to `css/default.css`.
- Tests: a three-level nested ordered list produces ListFlowables with bulletType `"1"`, `"a"`, and `"i"`; the generated CSS contains both new rules. Follow the existing test placement and naming.
- Test command: from `packages/scrivener`, run `c:\Users\Vinnie\cursor\wg21-paperworks\.venv\Scripts\python.exe -m pytest tests/ -v`. This is the full-suite command in `TESTING.md`, run through the venv instead of `uv run`, which can re-sync the venv.

</scrivener-spec>

<build-script-spec>

- Files: `wg21-papers/research/p4195/support/build.py`, `support/test_build.py`, and test fixtures and expected output in `support/fixtures/`, Python standard library only, run with `c:\Users\Vinnie\cursor\wg21-paperworks\.venv\Scripts\python.exe`. Test command: `python -m unittest` from `support/`.
- Usage: `build.py --extract EXTRACT [--mode foundation|spine|full] [--max-items N] [--labels] [--dependents KEY[,KEY]] [--emit PATH] [--front FILE] [--appendix FILE] [--footer TEXT] SOURCE...`. Without `--labels`, `--dependents`, or `--emit`, it runs the checks. The steps write `build.py check --mode M` as shorthand for this usage over the source files each step names, with `--extract` set to `support/rules-extract.md`.
- Source format:
  - Chapter headings are lines of the form `## N. Title`.
  - List items have three levels, with marker `1.` at every level; a level-2 item is indented 3 spaces and a level-3 item 6 spaces.
  - Each item ends with `{#KEY}`, or `{#KEY weakened}`. A key is lowercase, starts with one of `ax:`, `d:`, `f:`, `l:`, `inf:`, `ind:`, `p:`, `c:`, `t:`, `m:`, `thm:`, and continues with letters, digits, and hyphens.
  - Citations are `*[from KEY, KEY]*` and `*[proved by KEY, KEY]*`.
  - A table is a caption line `*Table: TEXT* {#t:KEY}`, the markdown table, then a line holding only a `*[from ...]*` citation.
  - An item may continue on following lines indented to its content column, including a second paragraph after a blank line. Its key ends its last line.
  - Any other non-blank line outside items and tables, such as an `In plain terms:` recap, is a prose line. Emit copies it unchanged.
- Labels: top-level items are numbered from 1, continuously across the source files in the order given. Level-2 items are lettered a, b, c; level-3 items take roman numerals i, ii, iii. A full label looks like `14b.ii`. Tables are numbered Table 1, Table 2, in order.
- Checks: print one line per failure and exit 1 on any.
  1. A key is cited but not defined, or is defined twice.
  2. A `from` citation names an item that is not earlier in the order.
  3. A `proved by` citation names anything other than the citing item's own children.
  4. A citation cycle exists.
  5. An item is an orphan: neither it nor any of its descendants is cited by another proof item, and its key does not start with `m:`, `t:`, `thm:`, or `c:`. A child named in its parent's `proved by` citation counts as cited. Mode `foundation` skips this check. Modes `spine` and `full` apply it to every item.
  6. A Fact quote is missing from the extract. In any item containing `**Fact.**`, each straight-double-quoted string, split at `...`, must appear in the extract after collapsing whitespace and mapping curly quotes to straight ones.
  7. A forbidden string appears outside straight double quotes in item text, prose lines, table captions, or table cells. Table separator rows, whose cells hold only dashes and colons, are exempt. The forbidden strings are: perverse, railroad, steamroll, capture, dominate, exploit, gaming, stack the room, punish, retaliate, insider, outsider, lock-in, cliff, obviously, clearly, of course, door, carry; an em dash; `--`; the letter P followed by four digits; `C++` followed by two digits; and a four-digit number from 1990 to 2099. Words match as whole words, case-insensitively, including inflected forms such as plurals and past tenses. The `--front` and `--appendix` files are checked too, except that the four-digit-number rule skips the appendix file, whose references include dates.
  8. In modes `spine` and `full`, the source files hold more than `--max-items` top-level items (default 150).
- Modes and options:
  - `check` (the default), with `--mode foundation|spine|full`. The mode defaults to `full`.
  - `--labels`: print each key with its label.
  - `--dependents KEY[,KEY]`: print every item that cites the given keys, directly or through other items, with labels.
  - `--emit PATH`: run every check for the mode first, and write the output file only if all pass.
  - `--front FILE` and `--appendix FILE`: accepted in check mode and on emit. On emit they are copied before and after the proof, with citations rewritten to labels. Every key they cite must be defined (check 1), and their citations do not count toward the orphan check.
  - `--footer TEXT`: written as the last line, in italics.
- Emit:
  - Replace each cited key with its label and strip the `{#...}` markers.
  - Write each top-level marker as its real number. Keep `1.` for nested markers, and indent each child to its parent's content column.
  - Write table captions as `*Table N. TEXT*`.
  - Put a blank line before a list that follows a table, a caption, or a prose line, so the list's first number survives markdown parsing.
- Tests: one fixture with two chapters, one table followed by more items, one weakened item, one item continued over two paragraphs, one `In plain terms:` recap, and one deliberate failure of each check; test check 8 with a small `--max-items`. Write one test per check, plus one emit test that compares against an expected file.

</build-script-spec>

## Pre-digested analysis

<pre-digest-foundation>

Draft for Step 4. The wording is a starting point; Steps 3 and 5 may change it.

Axioms:

- `ax:cost`: Attending a WG21 meeting in person costs money and time.
- `ax:who-pays`: A sponsor can pay a participant's travel and salary, but cannot attend, speak, or vote in the participant's place.
- `ax:repeat`: A participant who attends regularly expects to meet the same colleagues at future meetings.
- `ax:prefer`: Given a choice, each participant, sponsor, and national body prefers the option that brings more of what it values at less cost to it. For this proof, a participant values adoption of the proposals they support, their sponsor's interests, their standing, their time and money, and a good result for users; a sponsor values its interests; a national body values the outcomes its members support.
- `ax:support`: A participant who votes Against a colleague's proposal cannot rule out that the colleague will support the participant's own proposals less readily; a Neutral vote or no vote gives the colleague no more reason for this than an Against vote does.
- `ax:attention`: No participant can study every paper closely, so each chooses which papers to study.
- `ax:review-cost`: Reviewing a longer or more complex paper takes more time than reviewing a shorter or simpler one.
- `ax:unknown`: Before a design has been implemented and used, nobody can be certain how well it will work in practice.
- `ax:first-review`: When a proposal is first presented, it has received less committee review than at any later meeting.
- `ax:rework`: If a decision is reversed, the work built on it must be redone or discarded.
- `ax:redesign-cost`: Revising a design throughout costs its authors more work than a change confined to one part of it.
- `ax:learning`: A participant learns how the committee works partly by attending its meetings.
- `ax:turnover`: Over the years, some participants stop attending and others join.
- `ax:hours`: A meeting has a fixed number of hours, so time given to one paper is not available to another.
- `ax:schedule`: WG21 publishes a new edition of the C++ standard on a fixed three-year schedule.
- `ax:parallel-rooms`: When several subgroups meet at the same time, a participant can attend only one of them.
- `ax:users-affected`: A design in the standard applies to every user of the feature it specifies.

Definitions (each matching `proof-terms`): `d:participant`, `d:regular`, `d:newcomer`, `d:author`, `d:sponsor`, `d:user`, `d:rooms`, `d:standing`, `d:stake`, `d:direction-poll`, `d:forwarding-poll`, `d:incumbent`, `d:edition`, `d:feature-cutoff`, `d:reversal`, `d:settled-pattern`, and the two sizes:

- `d:small`: a proposal by one author whose design is reviewed within one meeting.
- `d:large`: a proposal whose review spans more than one edition and whose authors' participation is paid by one or more sponsors.

Facts, by source section. Quote word for word from the extract; each anchor below is the quote's opening.

- SD-4, "Consensus": `f:consensus-def` ("General agreement, characterized by the absence of sustained opposition"; "Consensus need not imply unanimity"), `f:timely` ("Escalation can become inappropriate in two ways"), `f:escalation-credibility` ("regularly uses the escalation process").
- SD-4, Code of Conduct slide: `f:accept-decisions` ("Accept group decisions").
- SD-4, "Proposals and papers": `f:no-paper` ("If a proposal doesn't have a paper, it doesn't exist."), `f:present-required` ("A proposal that does not have one of its authors"), `f:presenter` ("a person who is an expert in the paper's domain"), `f:bird-in-hand` ("we do not significantly delay progress on concrete proposals"; "may elect to delay the progress of the active proposal by one meeting"), `f:ts-lag` ("its progress is delayed by approximately 1-2 years"), `f:ts-default` ("the default action to is to move forward with the proposal we have").
- SD-4, "Subgroup responsibility and polls": `f:chairs-appointed`, `f:one-vote`, `f:chair-polls`, `f:two-to-one`, `f:favor-progress`, `f:not-vote`, `f:against-reasons`, `f:direction-group`, `f:sg-formation`, `f:sg-incubate`, `f:vehicle`, `f:private-concern`, `f:timebox`, `f:direction-implement`, `f:design-forward`, `f:wording-refer`, `f:wording-forward`, `f:prioritization`.
- SD-4, "Closing plenary session responsibility and polls": `f:plenary-owns`, `f:plenary-no-design`, `f:plenary-nb`.
- SD-4, "Technical Specifications (TS) and White Papers": `f:ts-experience` ("experimental branch"), `f:cast-in-stone` ("essentially cast in stone").
- SD-4, "Ballots and comments": `f:ballot-no` ("No should mean"; "most ballots fail if more than 1/3 of NBs vote No"), `f:ballot-no-new-features`, `f:ballot-decided`, `f:near-unanimous`.
- SD-4, the section on escalating a serious objection: `f:plenary-weight` ("should not be given weight in plenary"), `f:escalate-nb` ("normally the default is no, not a national position").
- SD-4, "How to report a potential technical concern": `f:concern-authors` ("include the proposal authors").
- SD-4, "Other topics": `f:protected` ("quoting straw poll questions and numeric results"), `f:minutes` ("All meetings must be minuted.").
- ISO 0.7: `f:iso-cost` ("travel costs and the value of the time spent by Experts").
- ISO 1.12.1 and 1.12.2: `f:convenor-term`, `f:experts-personal`, `f:registered`.
- ISO 2.5.7: `f:leadership-judges`, `f:not-veto`, `f:iso-register`, quoted with enough context to show the duty belongs to the committee leadership judging consensus among P-members.
- ISO 2.6.3 and 2.7.3: `f:iso-ballot`, approval by two thirds of P-members voting with not more than one quarter of all votes negative.
- ISO 6.1.1 and 6.5: `f:appeal`, `f:appeal-continues`.

Facts stating what a document does not contain (the rules checker must confirm each by search):

- `f:no-reason-record`: SD-4 contains no requirement that the record of a poll show how an objection was answered.
- `f:no-sponsor-cap`: ISO lets a committee limit the number of experts per P-member, and neither document limits the number of participants per sponsor.
- `f:no-merit-ruling`: SD-4 assigns no one the role of ruling which side of a technical dispute is correct.

</pre-digest-foundation>

<pre-digest-spine>

Draft for Step 7. Each line is one top-level item: key, kind, statement, then intended basis in brackets. Chapter 1 is the foundation. Step 7 may sharpen the wording, and every statement must meet `proof-style`.

2. Where decisions are made

- `p:path` (Proposition): A design enters the working draft only after a design room forwards it, a wording room forwards its wording, and plenary approves it. [f:design-forward, f:wording-forward, f:plenary-owns, d:rooms]
- `p:chair-decides` (Proposition): In each subgroup, whether a proposal advances depends on the chair's consensus call, and in plenary on the convenor's. [f:design-forward, f:wording-forward, f:leadership-judges, f:plenary-owns]
- `p:design-in-rooms` (Proposition): Plenary does not redesign, so a design's content is settled in the design rooms and in the study groups that feed them. [f:plenary-no-design, f:sg-incubate, p:path]
- `p:who-votes` (Proposition): Only registered experts present in the room vote in a subgroup poll, and users have no vote. [f:one-vote, f:registered, d:participant, d:user]
- `p:sponsor-no-vote` (Proposition): The rules give votes to participants and to national bodies, and none to sponsors. [f:one-vote, f:experts-personal, f:iso-ballot]
- `m:players` (Proposition): The players are authors, regulars, study group chairs, design room chairs, the convenor, national bodies, sponsors, and users. [p:path, p:chair-decides, p:who-votes, p:sponsor-no-vote, d:sponsor, d:author, d:regular]

3. What each player can do

- `m:moves` (Proposition): Each player's moves under the rules, one lettered child per player:
  - author: submit a paper, present it, revise it, add co-authors, build an implementation, propose a ship vehicle, withdraw [f:no-paper, f:present-required, f:direction-implement, f:vehicle]
  - regular: attend or not; study a paper or not; speak; vote Favor, Neutral, or Against, or not vote; write a paper; raise a concern privately with a chair; ask their national body for a national position [f:one-vote, f:not-vote, f:no-paper, f:private-concern, f:escalate-nb]
  - chair: choose polls, order the agenda by SD-4's priorities, time-box, re-poll, ask Against voters for reasons, make the consensus call, delay a proposal one meeting for a competing paper, forward [f:chair-polls, f:prioritization, f:timebox, f:two-to-one, f:against-reasons, f:bird-in-hand, f:design-forward]
  - convenor: appoint chairs, form study groups, make plenary consensus calls, ask whether Against votes are national positions [f:chairs-appointed, f:sg-formation, f:plenary-owns, f:plenary-nb]
  - national body: vote on ballots, comment, state a national position in plenary, appeal [f:iso-ballot, f:ballot-no, f:plenary-nb, f:appeal]
  - sponsor: pay for participation, and choose whom and how many [d:sponsor, ax:who-pays]
  - user: no move except becoming a participant [p:who-votes]

4. The price of a vote

- `l:against-double` (Lemma): Under the 2:1 norm, each Against vote raises by two the number of Favor votes a proposal needs. [f:two-to-one]
- `l:neutral-outside` (Lemma): Neutral votes and abstentions do not enter the 2:1 comparison, though SD-4 notes that a majority of Neutral votes can be concerning. [f:two-to-one, f:not-vote]
- `l:reasons-against` (Lemma): SD-4 names Against voters as the voters a chair may ask for reasons, and names no such step for any other position. [f:against-reasons, f:not-vote]
- `p:against-costs-more` (Proposition): For a regular, voting Against a colleague's proposal costs more than voting Neutral or not voting. [l:reasons-against, ax:support, ax:repeat, d:regular, d:standing]
- `p:stake-threshold` (Proposition): Under the preference axiom, a regular chooses Against over Neutral only when their stake in the outcome exceeds the added cost of Against. [ax:prefer, p:against-costs-more, d:stake]
- `p:doubt-outside-count` (Proposition): A regular who doubts a proposal, and whose stake is below that cost, votes Neutral or not at all, so the doubt does not enter the 2:1 comparison. [p:stake-threshold, l:neutral-outside]
- `l:room-size` (Lemma): The more people vote, the smaller the chance that one Against vote decides whether the 2:1 norm is met, while the vote's cost to the voter stays the same. [l:against-double, p:against-costs-more]
- `p:prefer-vs-stop` (Proposition): Saying in discussion that one prefers another design costs less than voting Against, because only the vote enters the count and only Against voters are named for questions. [l:reasons-against, l:against-double]
- `l:organized-minority` (Lemma): Any group holding more than one third of the Favor-plus-Against votes prevents the 2:1 norm from being met. [f:two-to-one]
- `t:vote-choice` (Table 1): one regular's choice of Favor, Neutral, or Against, for a small stake and for a large stake.
- `p:mutual-support` (Proposition): Two regulars with pending proposals each do better not opposing the other's proposal than opposing it, unless one proposal harms the other's interests. [ax:support, ax:prefer, p:against-costs-more]
- `t:mutual-support` (Table 2): two regulars, each choosing to support or oppose the other's proposal.

5. What the record keeps

- `l:record-content` (Lemma): SD-4 requires minutes and permits public quotation of poll questions and numeric results, and nothing in it requires the record to show how an objection was answered. [f:minutes, f:protected, f:no-reason-record]
- `l:iso-register-level` (Lemma): ISO's duty to register an opposition belongs to the committee leadership judging consensus among national bodies, and SD-4 adds no such duty for subgroup polls. [f:iso-register, f:no-reason-record]
- `l:address-not-resolve` (Lemma): Under ISO, the obligation to address a sustained opposition is not an obligation to resolve it, and a sustained opposition is not a veto. [f:not-veto]
- `p:advance-unanswered` (Proposition): A proposal can advance while objections to it remain unanswered, because advancing requires a consensus call, not an answer. [l:address-not-resolve, f:design-forward, f:two-to-one]
- `p:persuasion-not-required` (Proposition): The rules let a proposal advance once enough participants stop voting Against, whether or not they were persuaded. [f:consensus-def, f:two-to-one, p:advance-unanswered]
- `p:least-cost-response` (Proposition): When an objection's supporters are too few to stop the 2:1 count, the least costly response that keeps the count is a change confined to part of the design, or no change. [ax:prefer, ax:redesign-cost, l:organized-minority]
- `p:change-list` (Proposition): SD-4 asks an Against voter to name the changes that would address the concern; concerns stated as changes can be granted one at a time, while an objection to the proposal in any form names no change that addresses it. [f:against-reasons]
- `p:record-indistinct` (Proposition): The record the rules require cannot show whether an objection was answered or outvoted. [l:record-content]
- `p:dissent-needs-paper` (Proposition): For an objection to remain in WG21's documents as an argument rather than a count, its holder must write a paper, which costs as much as writing a proposal. [f:no-paper, l:record-content, ax:cost]
- `p:reasons-fade` (Proposition): Reasons not written into a paper become unavailable to the committee as the participants who heard them stop attending. [ax:turnover, l:record-content]
- `p:repeat-objection` (Proposition): A participant who repeats an objection after a consensus call can be described, in SD-4's own terms, as not accepting a group decision, whether or not the objection was answered. [f:accept-decisions, f:escalation-credibility, f:ballot-decided]
- `p:late-objection` (Proposition): An objection first raised at plenary or at ballot receives no weight under SD-4 unless it brings significant new information. [f:plenary-weight, f:timely, f:ballot-decided]

6. Proposal size

- `p:money-vs-presence` (Proposition): The participants who can attend year after year are those whose costs a sponsor pays or whose own value from attending exceeds their own costs. [ax:cost, ax:who-pays, ax:prefer, f:iso-cost]
- `p:incumbent-start` (Proposition): After a design passes a direction poll, later discussion of its topic starts from it: an alternative without a paper does not exist, an alternative with a paper can delay it by at most one meeting at the chair's choice, SD-4 asks authors to implement the room's direction, and at TS merge the default is to proceed with the proposal in hand. [f:no-paper, f:bird-in-hand, f:direction-implement, f:ts-default, d:incumbent]
- `ind:reversal-grows` (Induction): Each later decision built on a design adds to the work its reversal would redo or discard, so the cost of reversing the design does not decrease as the design advances. [ax:rework, d:reversal]
- `p:challenger-bar` (Proposition): A rival design displaces an incumbent only when voters judge the rival's advantage to be larger than the cost of reversal. [ax:prefer, ind:reversal-grows, p:incumbent-start]
- `p:early-polls` (Proposition): An author gains from favorable direction polls held early, when the design has had the least review, because each favorable poll becomes the starting point for the next discussion. [ax:first-review, p:incumbent-start, ind:reversal-grows, d:direction-poll]
- `l:poll-wording` (Lemma): A chair may take any poll, and a direction poll asks voters to accept less than a forwarding poll. [f:chair-polls, d:direction-poll, d:forwarding-poll]
- `ind:priority-compounds` (Induction): SD-4 gives agenda priority to the direction group's priorities, to work aimed at the next edition, and to work that can reach plenary at the current meeting; a proposal that advances at one meeting is closer to plenary at the next, so its priority does not fall as it advances. [f:prioritization, f:direction-group, ax:hours]
- `p:sponsor-votes` (Proposition): A sponsor that pays for more participants to attend a room adds to the number of votes available to the positions those participants hold. [f:no-sponsor-cap, f:one-vote, ax:who-pays]
- `p:review-share` (Proposition): As a proposal grows longer and more complex, the time to review it grows while a reviewer's chance of changing the outcome does not, so a reviewer with a small stake studies a smaller share of it closely. [ax:review-cost, ax:attention, l:room-size, ax:prefer]
- `l:author-knows-more` (Lemma): SD-4 describes the presenter as the domain expert who educates general C++ experts, and directs concerns about a proposal to its authors. [f:presenter, f:concern-authors]
- `p:reward-timing` (Proposition): An author's gain from adoption arrives at adoption, while the cost of a design flaw arrives after implementation and use and applies to every user of the feature. [ax:unknown, ax:users-affected, d:author]
- `ind:slices` (Induction): A large proposal adopted in parts makes each later part a step from the parts already adopted, and a rival must be compared against all of them. [p:incumbent-start, ind:reversal-grows, d:large]
- `p:large-position` (Proposition): Compared with a small proposal, a large proposal has more participants attending for it, more meetings in which to win polls, and more work built on each poll it wins. [d:large, d:small, p:sponsor-votes, ind:priority-compounds, ind:reversal-grows]
- `l:implementation-informs` (Lemma): Implementation and use reduce uncertainty about a design, and SD-4 ships a TS to gain that experience, so voters know more about a design with implementation experience than about one without it. [ax:unknown, f:ts-experience]
- `p:small-position` (Proposition): The author of a small proposal pays more of their own costs, receives agenda time after SD-4's priority work, and must attend to present. [ax:who-pays, f:prioritization, f:present-required, d:small]
- `p:newcomer` (Proposition): At equal design quality, a newcomer pays the same costs as a regular and knows fewer of the procedures that decide when an objection counts. [ax:learning, f:timely, f:private-concern, d:newcomer]
- `t:push-or-ts` (Table 3): the author of a large proposal choosing to push for the IS or accept a TS, against a design room that forwards or requires a TS.

7. Study groups

- `l:sg-purpose` (Lemma): SD-4 forms a study group when proposals on a topic are immature, incomplete, or competing, and the study group produces the initial proposal that enters the design room. [f:sg-formation, f:sg-incubate]
- `l:sg-attendance` (Lemma): A participant chooses a study group's session over concurrent sessions when its topic matters more to them, so a study group's room holds the participants who made that choice. [ax:parallel-rooms, ax:prefer]
- `p:sg-decides` (Proposition): A contest between competing designs is decided mainly in the study group, because its output enters the design room as the incumbent. [l:sg-purpose, p:incumbent-start]
- `p:deadlock` (Proposition): When each of two groups holds more than one third of the Favor-plus-Against votes, no design meets the 2:1 norm, and the deadlock ends only if voters change position, the design changes until enough Against voters accept it, or the voters present change. [l:organized-minority]
- `p:design-changes` (Proposition): A design changed to end a deadlock either adds elements its Against voters want or removes elements they oppose. [p:deadlock]
- `p:attrition` (Proposition): In a deadlock lasting many meetings, members of a group whose costs sponsors pay bear less personal cost per meeting than members of a group paying their own way. [ax:who-pays, ax:cost, p:deadlock]
- `p:sg-unified` (Proposition): SD-4 ties a study group's purpose to producing a unified initial proposal, and a deadlock produces none. [f:sg-formation, p:deadlock]
- `p:concern-presence` (Proposition): A concern held in one room enters another room's decision only if a participant present in that room raises it; a tooling concern about a language feature (SG15's topic) counts in the design room only through participants present there, while a contested language feature (SG21's topic) is contested in its own study group first. [ax:parallel-rooms, p:sg-decides]
- `t:hold-or-yield` (Table 4): two groups in a deadlock, each choosing to hold or yield, with unequal costs per meeting.

8. Chairs and the convenor

- `l:appointments` (Lemma): Subgroup chairs are appointed by the convenor with no fixed term, and the convenor is appointed by the parent committee for renewable three-year terms. [f:chairs-appointed, f:convenor-term]
- `l:chair-role` (Lemma): The rules make the chair the judge of consensus and assign no one the role of ruling which side of a technical dispute is correct. [f:leadership-judges, f:design-forward, f:no-merit-ruling]
- `p:chair-costs` (Proposition): A chair who declares consensus over objections risks later national body opposition, and a chair who declines delays work that SD-4 says subgroup polls should favor. [f:favor-progress, f:plenary-nb, f:iso-ballot]
- `p:chair-default` (Proposition): When the count meets the 2:1 norm, declaring consensus follows SD-4's stated norm and declining departs from it, so the rules make advancing the default at or above 2:1. [f:two-to-one, f:favor-progress]
- `p:repoll` (Proposition): Below 2:1, SD-4 allows a re-poll after discussion of the Against voters' concerns, and only Against voters are named for questions in that discussion. [f:two-to-one, l:reasons-against]
- `p:chair-no-reasons` (Proposition): Nothing in the rules requires a chair to record why consensus was declared over objections, and recording reasons takes meeting time. [l:record-content, ax:hours]
- `p:private-channel` (Proposition): SD-4 asks participants with concerns about a new proposal to raise them privately and in advance with the chair, who may then time-box the proposal; this channel leaves no record and is available only to participants who know of it. [f:private-concern, f:timebox, ax:learning]
- `p:plenary-ratifies` (Proposition): Because plenary does not redesign and gives no weight to objections not escalated in time, a design that reaches plenary with subgroup approval can be opposed there with effect mainly through national positions. [f:plenary-no-design, f:plenary-weight, f:plenary-nb]
- `p:wording-rooms` (Proposition): A wording room refers design questions back to the design room, so it can delay a design but cannot change it. [f:wording-refer]
- `t:chair-call` (Table 5): a chair declaring or declining consensus, when supporters are many and objectors few, and the reverse.

9. The release schedule

- `l:cutoff` (Lemma): Once an edition's draft goes to ballot, a ballot comment cannot add a feature to it. [f:ballot-no-new-features, d:feature-cutoff, d:edition]
- `p:miss-cost` (Proposition): A proposal not approved before an edition's feature cutoff waits at least one full three-year cycle. [l:cutoff, ax:schedule]
- `p:one-meeting-cycle` (Proposition): If SD-4's one-meeting delay for a competing paper falls on the last meeting before the cutoff, the proposal misses the edition. [f:bird-in-hand, p:miss-cost]
- `p:cutoff-effect` (Proposition): At the last meeting before the cutoff, an Against vote that stops a proposal delays it by at least three years. [p:miss-cost, l:against-double]
- `p:prefer-is` (Proposition): Because a TS delays adoption by about one to two years and an edition ships every three years, an author who wants adoption prefers the IS to a TS unless the design room requires a TS. [f:ts-lag, ax:schedule, ax:prefer, f:vehicle]
- `p:bundling` (Proposition): At ballot, a national body votes on the whole edition, and SD-4 asks that No mean the body does not want the edition at all, so a national body cannot vote against one feature without voting against every feature in the edition. [f:ballot-no, f:iso-ballot]
- `p:burden-flip` (Proposition): Before adoption, a proposal needs the 2:1 norm to advance; after adoption, removing it needs a paper that meets the 2:1 norm; after the final ballot, a design change needs near-unanimous consent; once published, the feature is "essentially cast in stone." [f:two-to-one, f:no-paper, f:near-unanimous, f:cast-in-stone]
- `p:schedule-protects` (Proposition): Because an edition ships on schedule, no unfinished feature delays the features that are ready. [ax:schedule]

10. National bodies

- `l:nb-no-scope` (Lemma): A No vote on an edition opposes every feature in it, including features the body's own experts support. [p:bundling]
- `p:nb-comment` (Proposition): A national body that supports most of an edition does better voting Yes with comments than voting No over one feature. [l:nb-no-scope, ax:prefer]
- `l:nb-comment-limits` (Lemma): SD-4 treats as out of scope a comment that adds a feature, and as out of harmony a comment that repeats an objection already decided at a meeting the body attended, unless new information arises. [f:ballot-no-new-features, f:ballot-decided]
- `p:nb-route` (Proposition): For an individual objection to have weight in plenary, it must become a national position before plenary, and SD-4 makes "no, not a national position" the default. [f:plenary-nb, f:escalate-nb]
- `p:nb-members` (Proposition): A national body decides its position by its members under its own rules, so a sponsor that pays many of a body's active members has those members' votes in deciding the body's position. [f:escalate-nb, ax:who-pays]
- `p:nb-early` (Proposition): SD-4 asks national bodies to state objections early and treats an objection first raised at ballot as out of harmony with accepting group decisions, so the absence of an early national objection is what the rules treat as no objection. [f:timely, f:ballot-decided]
- `p:appeal-continues` (Proposition): Work continues during an appeal up to and including the approval stage, so an appeal does not stop an edition. [f:appeal-continues]
- `t:nb-ballot` (Table 6): a national body choosing Yes with comments or No, when it supports most of the edition and when it supports little of it.

11. The settled pattern

- One lemma per player, keyed `l:settled-<player>`, covering the regular, the author of a large proposal, the author of a small proposal, the study group chair, the design room chair, the convenor, the national body, the sponsor, and the user. Each lemma states the player's settled choice and shows that no move in `m:moves` improves the player's position while the other players' choices stay fixed, citing chapters 4 to 10.
- `thm:settled` (Theorem), draft:
  - Under SD-4 and the ISO/IEC Directives as written, and given the axioms, the following choices form a settled pattern, in which no player improves their position by changing only their own choice.
  - Regulars vote Favor, Neutral, or not at all on colleagues' proposals, and vote Against when their stake exceeds the cost of doing so.
  - Authors seek favorable polls early and answer objections with the least costly change that keeps the 2:1 count. Authors of large proposals adopt their work in parts and prefer the IS to a TS.
  - Sponsors pay for participation in proposals that serve their interests and in opposition to proposals that harm them.
  - Chairs declare consensus when the count meets the 2:1 norm, and record the count and the outcome.
  - Study groups settle contests between designs before the design rooms see them. A contest that stays even ends when voters change position, the design changes, or one side stops attending.
  - National bodies vote Yes on editions and comment on details.
  - Users do not take part.
  - In this pattern, a proposal's progress depends on the participants who attend for it and on the polls it has already won, and the record does not show whether its objections were answered.

12. Corollaries

- `c:predictions` (Corollary), one lettered child per prediction. Each names evidence a paper may quote (poll questions and numeric results, public papers and their author lists, mailings, working drafts) and states what would count against it:
  - Against votes are fewer, relative to Favor, on proposals whose author lists name more participants paid by one sponsor.
  - The Neutral share of a poll rises with the length of the paper polled.
  - Favor margins in design rooms are wider at the last meeting before a feature cutoff.
  - Large proposals appear as sequences of papers, each building on parts already adopted.
  - Removals after adoption are rare, and arrive with national body comments or with a group holding more than one third of the votes.
  - Study group polls on a design show wider Favor margins than the design room's later polls on the same design.
  - Small proposals stop advancing more often without a negative poll than with one.
  - One prediction for each triage conjecture.
- `c:levers` (Corollary), one lettered child per rule lever. Each takes the form "if this rule changed, this item fails, and the model predicts this":
  - anonymous design polls (`p:against-costs-more`)
  - reasons asked of every position (`l:reasons-against`)
  - a limit per sponsor (`p:sponsor-votes`)
  - a required written answer to each objection (`p:record-indistinct`)
  - a decision rule for deadlocks that last a set number of meetings (`p:attrition`)
  - a TS path that does not cost an edition (`p:prefer-is`)

</pre-digest-spine>

<pre-triage>

Draft verdicts for Step 3 to check. Form: ID | verdict | destination keys or reason.

Facts:

- F1 | Rule | f:two-to-one, f:design-forward, f:leadership-judges
- F2 | Corrected, then Rule | l:record-content; SD-4 requires minutes and permits quoting poll questions and numeric results; it states no tally requirement and contains no requirement to record how an objection was answered
- F3 | Corrected, split | ax:who-pays, p:money-vs-presence; a sponsor can bear money costs, but not the participant's presence or standing
- F4 | Derived, weakened | ind:reversal-grows; the part about the standing of those who backed earlier polls is dropped as not derivable
- F5 | Derived | p:record-indistinct
- F6 | Derived | p:persuasion-not-required
- F7 | Corrected, then Rule | l:iso-register-level; the clause is 2.5.7, and the duty belongs to the committee leadership
- F8 | Derived | p:dissent-needs-paper
- F9 | Axiom and Derived | ax:first-review, p:early-polls
- F10 | Derived | p:incumbent-start
- F11 | Axiom | ax:review-cost
- F12 | Derived | p:review-share
- F13 | Axiom, first clause only | ax:repeat; the cost of confrontation is derived in chapter 4
- F14 | Derived | p:who-votes
- F15 | Axiom | ax:attention
- F16 | Rule | f:against-reasons
- F17 | Axiom and Derived | ax:turnover, p:reasons-fade
- F18 | Derived | p:least-cost-response
- F19 | Derived | p:prefer-vs-stop
- F20 | Rule and Derived | f:chair-polls, l:poll-wording
- F21 | Axiom | ax:learning
- F22 | Corrected, then Derived | p:dissent-needs-paper; "only" is dropped, since minutes and national body comments also keep dissent
- F23 | Derived | p:who-votes
- F24 | Derived | p:advance-unanswered
- F25 | Axiom and Derived | ax:redesign-cost, p:least-cost-response
- F26 | Derived | f:present-required, p:small-position
- F27 | Dropped | ax:learning covers what the proof needs
- F28 | Derived, inert wording | p:chair-costs
- F29 | Rule | f:not-veto
- F30 | Corrected, then Rule | p:who-votes; registered experts only
- F31 | Derived | p:private-channel, p:newcomer
- F32 | Derived, inert wording | p:small-position; "good work" becomes "a proposal"
- F33 | Derived | l:implementation-informs
- F34 | Dropped | d:standing and ax:learning cover what the proof needs

Incentives:

- I1 | Weaken | p:persuasion-not-required
- I2 | Weaken | l:chair-role
- I3 | Prove | p:early-polls
- I4 | Weaken | p:challenger-bar; the standing component is dropped
- I5 | Prove | p:money-vs-presence
- I6 | Weaken | p:large-position, ind:slices
- I7 | Prove | p:chair-no-reasons
- I8 | Weaken | p:record-indistinct; the claim about a written answer becoming a liability is a conjecture
- I9 | Prove | p:incumbent-start
- I10 | Prove | p:review-share
- I11 | Prove | p:who-votes, ax:cost
- I12 | Prove | p:least-cost-response
- I13 | Prove | p:prefer-vs-stop
- I14 | Weaken | p:late-objection
- I15 | Weaken | p:review-share
- I16 | Merge | p:against-costs-more
- I17 | Merge | p:least-cost-response
- I18 | Weaken | ind:priority-compounds, p:private-channel
- I19 | Prove | p:newcomer, p:private-channel
- I20 | Prove | p:chair-default
- I21 | Weaken | l:poll-wording
- I22 | Prove | p:dissent-needs-paper
- I23 | Weaken | p:newcomer
- I24 | Weaken | p:repeat-objection
- I25 | Weaken | p:small-position, p:attrition
- I26 | Prove | l:organized-minority, f:consensus-def
- I27 | Prove | p:plenary-ratifies
- I28 | Conjecture | chapter 12 prediction
- I29 | Weaken | ind:slices
- I30 | Conjecture | chapter 12 prediction, with I29
- I31 | Weaken | p:repeat-objection
- I32 | Prove | p:prefer-is
- I33 | Weaken | p:attrition
- I34 | Weaken | p:change-list
- I35 | Weaken | ind:priority-compounds, ind:slices
- I36 | Weaken | p:nb-route
- I37 | Prove | p:mutual-support
- I38 | Merge | p:review-share
- I39 | Weaken | p:nb-early
- I40 | Prove | p:nb-comment
- I41 | Merge | p:review-share
- I42 | Conjecture | chapter 12 prediction
- I43 | Conjecture | chapter 12 prediction
- I44 | Conjecture | chapter 12 prediction
- I45 | Conjecture | chapter 12 prediction

Original assumptions (from the `original-assumptions` block), draft crosswalk for Appendix A:

- A1 | covered | ax:prefer, since a participant values adoption of the proposals they support
- A2 | covered, split | ax:cost, ax:who-pays
- A3 | covered | ax:prefer, with the fixed list of values
- A4 | covered | ax:repeat; reciprocity is added as ax:support
- A5 | rule reading | f:favor-progress, p:chair-default
- A6 | covered | ax:attention
- A7 | derived | p:who-votes
- A8 | covered, example dropped | ax:unknown, f:ts-experience; the C++20 contracts example is sealed history
- A9 | covered, weakened | ax:rework, ind:reversal-grows; the standing component is dropped
- A10 | rule reading | p:incumbent-start
- A11 | covered | ax:learning
- A12 | rule reading | f:design-forward, f:leadership-judges
- A13 | rule reading | f:two-to-one
- A14 | rule reading, corrected | l:record-content, l:iso-register-level

</pre-triage>

## Candidate lists (verbatim, supplied by the user)

The history-citing facts (old 5, 12, 20, 32, 33, 34, 35, 37, 38, 42, 43, and 45) were cut at the user's direction and the rest renumbered. The original 14 assumptions are kept for the Appendix A crosswalk. Their `[65]` footnote marks and "(section 2)" point into a document this plan does not use, and item 8's contracts example is sealed history; none of these enters the proof.

<original-assumptions>

1. Authors who keep bringing a paper forward want it adopted.
2. Taking part costs time and money, every year.
3. People weigh what an action costs against what it is likely to get them, which can include the satisfaction of helping others.<sup>[65]</sup>
4. Participants expect to work with the same people for years.
5. Chairs want the group to reach decisions.
6. Reviewers have limited time and care more about some areas than others.
7. Any one outside user has very little chance of changing an outcome.
8. At the time of a poll, the room cannot fully judge how good a design is. SD-4 assumes as much when it describes a TS as an "experimental branch" that ships "to gain experience," and the removal of contracts from the C++20 draft (section 2) shows it.
9. Reversing a decision costs more the more work has been built on it. Cost here is opportunity cost, the value of what a reversal gives up:<sup>[65]</sup> discarded wording and implementations, committee time to redo the work, schedule risk, and the standing of those who backed earlier polls. Effort already spent does not count.
10. A later proposal is discussed relative to whatever the room already favors.
11. Procedural knowledge comes from attending, and it improves a participant's odds.
12. A proposal advances when the chair declares consensus.
13. Consensus is the chair's judgment. SD-4 says a proposal "normally advances if there are more than twice as many in favor of a proposal as against."
14. SD-4 does not require a poll's record to hold more than a tally and an outcome. A chair may ask those voting against for their reasons; nothing requires the record to say how those reasons were answered, or why the room proceeded anyway.

</original-assumptions>

<candidate-incentives>

45 distinct possible incentives, ranked from highest impact and confidence down to lowest.

1. Authors aim to outlast objections rather than answer them, as a proposal advances once the chair declares consensus and SD-4 does not require any finding that the remaining objections were answered.
2. Chairs aim to turn conflict into a decision rather than rule on which side is technically right, as their role is to get the group to decisions, and ruling on technical truth would make them the supreme technical authority.
3. Authors push for favorable direction polls as early as possible, as each poll raises the cost of reversal, so a later competitor has to beat the paper plus every decision the committee has already made.
4. The room sticks with an incumbent design unless a challenger's advantage exceeds the full cost of reversal, as switching would throw away wording, implementations, committee time, and schedule, and would cost the standing of everyone who backed the earlier polls.
5. Only people who can absorb the cost of attending year after year (whoever pays it) propose and persist, as an author enters only when the expected payoff beats a recurring cost of travel, lodging, and weeks of time.
6. Authors of large, multi-year, employer-funded features push hardest for early lock-in and resist late correction most, as their cost of reversal grows with years of work, reputation, and coalition capital.
7. Chairs have little reason to write down why consensus was declared over the remaining objections, as SD-4 asks only for a tally and an outcome and puts the duty to explain on the person voting Against.
8. The winning side has little reason to put a strong statement of the losing argument into the permanent record, as a written answer to an objection becomes a future liability, while a bare "the committee achieved consensus" is much harder to reopen.
9. A rival design that arrives after a direction is set is heard and polled only as an amendment or objection to the incumbent, as every discussion starts from whatever the room already favors.
10. Reviewers study proposals deeply only in areas they care about and abstain elsewhere, as review costs them time while its benefits are spread across everyone.
11. Ordinary C++ users stay out of the process, as the cost of study and travel is large and the chance that one user's review changes the result is close to zero.
12. Authors answer objections with the cheapest move that makes them non-dispositive, such as a narrow accommodation, a scope caveat, or persuading the room the concern is non-blocking, as that serves the poll as well as actually answering the objection, at a fraction of the cost.
13. Participants say they prefer a rival design far more often than they act to stop a proposal, as preventing a proposal from proceeding spends much more social and institutional capital than preferring another.
14. The room discounts late objections, especially from outsiders, as acting on them means discarding accumulated consensus, invalidating previous work, spending scarce meeting time, and trusting someone who took no part in the decisions being questioned.
15. Reviewers give the least scrutiny to the proposals that most need it, as review cost rises with a proposal's length, opacity, and entanglement with existing wording while each reviewer's chance of changing the outcome stays small.
16. Participants stay personally cordial and pick their fights carefully, as they expect to face the same people for decades and status goes to those who absorb criticism without becoming impossible to work with.
17. Authors with a lopsided tally have little reason to find out whether the few remaining objectors are right, as the poll already clears the bar and the institution pays almost nothing for the discovery.
18. Chairs give agenda access and confidence to procedurally fluent authors, as advancing their papers presents less risk, and each success compounds into more reputation and access.
19. Insiders intervene at the moments that matter while newcomers and late critics miss them, as only repeated attendance teaches when a consequential decision is really being made, which moves are available, and what must already have happened for an intervention to count.
20. Chairs lean toward advancing rather than deferring, as deferring brings frustrated authors, slipping schedules, and accusations of letting one or two people veto progress.
21. Fluent participants steer early polls toward soft questions like "encourage further work," as those pass easily yet build momentum, legitimacy, and an expectation of eventual adoption.
22. Objectors often leave nothing in the record but a tally, as SD-4 keeps dissent only through new papers, and writing one demands the same authorship, time, fluency, and persistence as proposing.
23. A newcomer with a better design faces worse odds and higher costs than a fluent insider with a weaker one, as fluency both raises the chance of adoption and lowers the cost of pursuing it, giving the insider more attempts.
24. Objectors stop opposing when their social capital runs out rather than when they are persuaded, as the question shifts from "are you right?" to "how hard will you resist?" and every repeat Strongly Against vote reads as blocking everyone else's work.
25. A design without a persistent champion goes nowhere, and a losing rival usually fades through less agenda time, more revision requests, and no forwarding poll rather than outright rejection, as persistence changes the odds of winning independently of technical quality.
26. A lone expert's objection counts for little unless it is organized and sustained across meetings, as the consensus definition gives weight only to sustained opposition from an important part of the concerned interests.
27. Individual objectors acquiesce at plenary once a proposal arrives with years of work and subgroup approval, as moving the whole room to opposition is a coordination problem that gets harder with every accumulated decision.
28. Authors disclose only the minimum needed to win the poll, as more disclosure creates a larger surface for opposition to raise concerns.
29. Authors of large architectures lead with the smallest installable piece that forecloses competing designs, as once it is adopted every rival must compete against that foundation plus its accumulated consensus and extension roadmap.
30. Authors frame foundational papers as minimal and conservative ("just installs the foundation"), as low apparent stakes mean the cost of discovering what the paper forecloses exceeds what most reviewers will spend.
31. Authors come to describe a persistent objection as reopening a settled question ("already considered repeatedly, no new information"), as that can be true even when the objection was never answered, and it recasts the objector as refusing to accept a legitimate decision.
32. Authors and their coalition resist moving a feature to a TS or a later standard, as delay is a direct cost to them and progress on the current release depends on closure.
33. Skilled authors withdraw, revise, negotiate, or postpone rather than force an "A or B, vote now" showdown, as persistence alone raises their odds in a war of attrition.
34. Under institutional pressure, an architectural objection gets broken into a list of local fixes, as each fix is cheap to grant and the breakdown quietly takes the question of whether the architecture should exist off the table.
35. Experienced authors of large features try to secure scheduling, chair confidence, and the study group's committed time before they invest, as under the reversal-cost inequality whatever is secured first is hardest to dislodge.
36. Objectors who lose in a subgroup appeal to another subgroup or a national body, as the subgroup's record keeps only the tally, so a lost poll there reads as a lost argument.
37. Long-term participants accommodate each other's proposals and trade concessions, as blocking a colleague today invites being blocked tomorrow, even when the resulting feature would fail an independent cost-benefit test.
38. Reviewers who are not parties to a dispute rarely check a rebuttal against the opposition paper it answers, as verification is expensive and the direction is already set, which leaves only the objectors motivated to find its errors.
39. Chairs advance once national body (NB) risk looks manageable and read months of NB silence as clearance, as NB opposition is a main risk of advancing too aggressively.
40. National bodies stay out of most proposals, as coordinating a national position is costly and only worth it on highly salient issues.
41. Authors gain from technical opacity and can push hard-to-review proposals forward unchanged, as reviewers facing a high review cost abstain rather than scrutinize.
42. Minorities who feel unheard push harder, and majorities who read that as obstruction discount them further, as nothing in the record shows the objection was understood before it was rejected.
43. Authors time rebuttal papers for the meeting where their secured position will next be challenged, as a rebuttal arriving alongside the opposition lets the room treat the objection as answered, and the record later reads like reconciliation.
44. Fixing a flawed design after subgroup consensus falls to senior members willing to absorb the cost of repair, as the committee's informal peerage gives them the standing to make the room reconsider.
45. Objectors keep pressing a rival design after losing polls, as they too have invested analysis and reputation in it, and each accommodation that misses the architectural concern looks like evasion.

</candidate-incentives>

<candidate-facts>

34 potential facts ranked the same way:

1. A proposal advances when the chair declares consensus, and consensus is the chair's judgment, guided by SD-4's rule of thumb of more than twice as many in favor as against.
2. SD-4 requires a poll's record to hold only a tally and an outcome, so the record cannot show whether an objection was answered or outvoted.
3. Taking part costs travel, lodging, and weeks of time every year, and what decides who can play is whether that cost can be absorbed year after year, not who pays it.
4. Reversal cost grows with everything built on a decision (discarded wording and implementations, committee time to redo the work, schedule risk, and the standing of those who backed earlier polls), so it is negligible for a three-page paper and very large for a multi-year feature.
5. The record cannot distinguish a proposal that survived because it was excellent from one that survived because its authors were persistent, funded, and procedurally fluent.
6. Consensus does not require persuasion, so a participant can lose a poll without being convinced.
7. SD-4 reprints ISO's consensus definition but not ISO clause 2.5.6, which requires leadership to register opposition in the minutes and to try in good faith to resolve sustained opposition.
8. The proposal survives as a durable document, while oral dissent survives only as a tally.
9. Direction polls come first in a proposal's life, when the design is least mature.
10. A poll changes the committee's state, not just its information: before it a question is open, after it the committee "has direction," and the next meeting starts from there.
11. Review cost scales with paper length (a proxy for design complexity), technical opacity, and entanglement with existing standard wording.
12. Review is a public good: it costs the reviewer, its benefits are spread across everyone, and any one reviewer's chance of changing the outcome is small.
13. Participants deal with the same people for years, often decades, which makes open confrontation expensive.
14. Any single outside user has almost no chance of changing an outcome.
15. Reviewers have limited time and care more about some areas than others.
16. SD-4 puts the duty to explain on the person voting Against, who should be ready to say what change would address their concern, or that no change would.
17. The people who were in the room leave over time, so reasons that were never written down are eventually lost.
18. Once the tally clears the bar, the process pays the author little for finding out whether the few remaining objectors are right.
19. Saying "I prefer B" costs little, while saying "I am willing to prevent A from proceeding" costs considerably more social and institutional capital.
20. Poll wording decides what is being decided: the same proposal can pass "do we like this direction?" and fail "forward this paper for C++29."
21. Procedural knowledge comes from attending, is partly tacit, and both raises a participant's odds and lowers their cost of taking part.
22. SD-4 preserves dissent only through new papers, which take the same authorship, time, fluency, and persistence as proposals.
23. Polls count only committee participants, so the ratio reflects who can afford to take part, not the wider C++ population.
24. A concern can receive extensive consideration without ever being answered.
25. Answering an objection by redesign costs far more than neutralizing it with a narrow accommodation or a scope caveat.
26. Influence comes from an argument plus a person willing to keep advancing it, and a compelling argument without a champion is weak.
27. Procedural fluency and technical expertise are separable, though doing the work builds fluency, so the two correlate over time.
28. A chair faces costs either way: advancing over objections risks accusations of railroading and national body opposition, while deferring risks frustrated authors, slipping schedules, and accusations of letting one or two people veto progress.
29. ISO does not require an objection to be resolved successfully, only addressed in good faith, and a sustained opposition is not a veto.
30. The rules exclude no one, but the consensus definition's terms favor insiders: "sustained" opposition takes attendance across meetings, an "important part of the concerned interests" takes institutional standing, and opposition has to be organized to count.
31. Everyone has similar formal rights, but only fluent participants know all the available moves and when a consequential decision is really being made.
32. Good work can stall for purely procedural reasons, such as going to the wrong group, lacking the expected motivation, or arriving after scheduling decisions.
33. Accumulated revision and implementation evidence has real weight and is not just psychological momentum.
34. Standing in the committee is informal and earned, a kind of peerage built on mastering a domain, writing credible papers, and shepherding work over years.

</candidate-facts>
