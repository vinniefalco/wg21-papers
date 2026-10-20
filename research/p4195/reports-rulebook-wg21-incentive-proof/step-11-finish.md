# Step 11 finish

Gate state: the full check passes with 139 top-level items and 6 tables, so the final cap is 150. Chapter 11 has its round 2 proofs back, plus new proofs for the Theorem and every other chapter 11 item the always-prove rule covers.

## 1. Chapter 11 repair

The snapshot spine the task named, `snapshots\step-11-pre-refill-r3\02-spine.md`, is byte-identical to the current `02-spine.md`, so it cannot show what changed. Round 2's chapter 11 was written against the spine in `snapshots\step-11-refill-r2-done\02-spine.md`, so I compared against that one and against the old chapter's own copies of its spine items.

Restored, byte for byte from round 2's `ch-11.md`, by script (`step11_finish_assemble.py`): all 49 proof items, 21 lemmas and 28 steps. None of their keys is defined in any other file.

- `l:settled-regular`: 7
- `l:settled-design-bound`: 11
- `l:settled-result-seeking`: 7
- `l:settled-small-author`: 3
- `l:settled-sg-chair`: 5
- `l:settled-convenor`: 4
- `l:settled-nb`: 7
- `l:settled-sponsor`: 1
- `l:settled-user`: 4

Chapter 11 statements that changed since round 2, and how each is now proved:

- `thm:settled`, the integration sentence, where "No step" became "No SD-4 step". Round 2 gave the Theorem no proof. Its new step `inf:thm-fit` proves the sentence from `f:no-integration-check` and `p:integration`.
- `l:checks-deadlock` now adds that a TS can merge early for integration testing and cites `f:early-merge`. Round 2 gave it no proof. It now has four steps, and `inf:deadlock-early-merge` covers the new clause.

One restored lemma cites an item that changed in chapter 5: `l:bound-early` cites `l:poll-wording`, which is now scoped to design rooms. The lemma still holds as written, because every favorable poll adds to what a reversal must redo (`ind:reversal-grows`), so I left it unchanged.

New proofs, 57 items, wherever the always-prove rule applies and round 2 had none:

- `thm:settled`: 12 lemmas and 33 steps. The first lemma shows that the named choices form a settled pattern, from the settled lemmas and `d:settled-pattern`. Each later lemma takes one group of the second paragraph's sentences and cites its sources.
- `l:settled-design-chair`: 2 lemmas, one for the call and one for the agenda order.
- `l:weighs-both`: 2 lemmas, one for when both values favor the same option and one for when they conflict.
- The table-rank lemmas `l:disclose-result-seeking` and `l:disclose-design-bound`: 2 steps each.
- `l:checks-deadlock`: 4 steps.

I read "items joining results from different chapters" as items that cite derived results (anything other than axioms, definitions, and facts) from two or more chapters. Under the looser reading, items of different chapters with the foundation counted as chapter 1, almost every item in the proof would qualify, including roman steps, which cannot have children. Under my reading, `l:checks-hearing` and `l:checks-record` (facts plus one chapter's result) need no proof.

Chapter 11 now holds 128 keyed units: 21 spine items, the table `t:disclose`, and 106 proof items. Every sentence in a restored or new item is 30 words or fewer.

## 2. Full check

The first run after the repair (full mode, item limit 200) passed: 140 top-level items, 6 tables, no failures. Nothing needed fixing, and no spine statement changed.

## 3. Module pass

I searched for chains of consecutive top-level items using citations from both the spine and the chapter files (`step11_finish_chains.py`). There was one fold:

- `l:author-knows-more` is folded into `p:disclosure` in chapter 9, in both `ch-09.md` and `02-spine.md`. `p:disclosure` now has `*[proved by l:author-knows-more]*` and drops that key from its `*[from ...]*` list. The lemma's only use was this proposition, which joins results from chapters 5 and 9 and previously had no proof.
- `MODULES` in `check_modules.py` gained `"p:disclosure": ["l:author-knows-more"]`. The module gate passes with 8 modules.

Not folded:

- `p:dissent-needs-paper` is also cited by chapter 12's `inf:sp-gain`.
- `l:settled-result-seeking` is a false positive from `find_modules.py`, which does not parse the Theorem's two-line item. The Theorem and chapter 12 both cite it.

Snapshot `step-11-pre-module` was taken before the fold.

## 4. Rerun and cap

- Full: `ok: mode full, 139 top-level items, 6 tables`, under an item limit of 200 and under the default limit of 150.
- Spine: 139 top-level items, 6 tables. Foundation: 58.
- Final cap: 150, since the count is under it. No cuts are needed.

## 5. Preview

- `preview\full-draft.md` (180,953 bytes) and `preview\full-draft.pdf` (56 pages).
- No raw keys are left in citations. The Theorem is item 137, and its proof renders as 137a to 137l with roman steps.

## 6. Unresolved, for Step 12 or a follow-up

Round 3 dropped round 2 proofs in other chapters too, under the same instruction. The round 2 versions are in snapshot `step-11-refill-r2-done`.

- Chapter 4: `p:least-cost-response` (2 children).
- Chapter 5: `l:poll-wording` (1).
- Chapter 9: `p:merit-gap` (1) and `p:written-answer` (4).
- `p:reasons-unrecorded` and `p:integration` lost only weakened children whose wording the spine has since adopted, so those losses are expected.
- Recommendation: restore the chapter 4, 5, and 9 proofs the same way, checking `l:poll-wording`'s against its design-room scoping (medium confidence: the parts that weigh values or join chapters fall under the always-prove rule, while the rest may pass the common-sense filter).

Other items outside chapter 11 that the always-prove rule covers but that have no proof:

- Table-rank lemmas with no steps: chapter 3 (4), chapter 7 (5), chapter 10 (4). Chapters 8 and 11 give their rank lemmas steps.
- Items joining results from two or more chapters: `p:dissent-needs-paper`, `p:fluency` (chapter 4); `p:late-arrival` (5); `ind:adopted-parts`, `p:parts`, `l:first-part-fix`, `l:first-part-oppose` (6); `l:hold-yield-holder-gains` (7); `p:plenary-ratifies` (8); `p:merit-gap` (9).

Theorem wording for the Step 12 logician to test:

- "a sponsor can add voters without limit": `p:sponsor-votes` also says SC22 may cap the experts each national body or liaison appoints.
- "review whose gain is spread across all users goes undone": the proof gives `p:review-shortfall`'s narrower form, review worth more to users together than it costs but less to any one participant.
- "checks on each of these effects": this rests on `p:checks`, which lists checks without pairing each one with an effect.

Also, four chapter items (`p:who-decides`, `l:consensus-test`, `p:first-part`, `p:users-out`) have shorter `*[from ...]*` lists than their spine entries. Their statements are identical, and the difference predates this step.

## Files

- Changed: `ch-11.md`, `ch-09.md`, `02-spine.md`, `check_modules.py`, `preview\full-draft.md`, `preview\full-draft.pdf`.
- Added scripts: `step11_finish_diff.py`, `step11_finish_keys.py`, `step11_finish_scan.py`, `step11_finish_assemble.py`, `step11_finish_chains.py`, `step11_finish_fold.py`.
- Snapshots: `step-11-pre-module`, then `step-11`.
- The ledger is not edited, so this step still needs recording there.

## Step 11b: closing the gaps

Gate state: the full check passes with an item limit of 150 (139 top-level items, 6 tables), the spine check gives 139, and the module gate passes with 8 modules. The preview is 62 pages. Proof items in chapters 2 to 12 rose from 245 to 331: 8 restored from round 2, 3 reused from round 1, and 75 new.

### Restored from round 2 (8 items)

- Chapter 4, `p:least-cost-response`: `l:change-cost`, `l:study-count`.
- Chapter 5, `l:poll-wording`: `l:direction-asks-less`.
- Chapter 9, `p:merit-gap`: `l:merit-in-vote`.
- Chapter 9, `p:written-answer`: `l:paper-answers`, `l:iso-comment-answers`, `l:answer-in-writing`, `l:answer-shows-new`.
- I did not restore the weakened children of `p:reasons-unrecorded` and `p:integration`, because the spine has since adopted their wording. Both statements got new proofs instead.

### Statements re-proved because they changed since round 2

- `p:reasons-unrecorded` (chapter 4): three lemmas (the case lasts in its paper, an unwritten reason fades, the argument survives only in writing), and the last of them has three steps.
- `p:incumbent-start` (chapter 5): four lemmas, the first covering the design-room scoping.
- `l:poll-wording` (chapter 5): the restored lemma, plus `l:design-room-incumbent` for "in a design room".
- `p:integration` (chapter 9): three lemmas covering separate approval in plenary, the editor's merge and the editing committee's check, and what a conflict costs.

### Items citing proved results from two or more chapters, now proved

- Chapter 4: `p:dissent-needs-paper` (four lemmas, three of them from round 1) and `p:fluency` (four).
- Chapter 5: `p:late-arrival` (three).
- Chapter 6: `ind:adopted-parts` (two), `p:parts` (three), and `l:first-part-fix` and `l:first-part-oppose` (three steps each).
- Chapter 7: `l:hold-yield-holder-gains` (three steps).
- Chapter 8: `p:plenary-ratifies` (four).
- Chapter 9: `p:merit-gap` (the restored lemma plus `l:call-from-votes`).
- Chapter 11: the restored lemmas `l:seeking-early` (three steps), `l:small-wait-cost` (two), and `l:sg-call` (two).
- Three of the new lemmas themselves joined chapters, so they got steps too: `l:argument-writing`, `l:part-adds-hurdle`, `l:call-from-votes`.
- A rescan finds no settled lemma, Theorem, table rank, corollary, or cross-chapter item at levels 1 and 2 without a proof.

### Table-rank lemmas proved (13 lemmas, 23 steps)

- Chapter 3: `l:vote-below`, `l:vote-above`, `l:mutual-refrain`, `l:mutual-own-vs-other` (7 steps).
- Chapter 7: the five `l:hold-yield-*` rank lemmas (9 steps).
- Chapter 10: `l:rank-rest-yes`, `l:rank-rest-abstain`, `l:rank-oppose-no`, `l:rank-oppose-abstain` (7 steps).

### Theorem change, in `02-spine.md` and `ch-11.md`

- "a sponsor can add voters without limit" became "SD-4 sets no limit on how many voters one sponsor can pay for", in `thm:settled` in both files and in its proof lemma `l:thm-deciders`.
- The step `inf:thm-no-cap` now adds that each paid participant must still be an expert a national body or liaison appoints, and that SC22 may cap how many each appoints. It cites `p:sponsor-votes` and `f:experts-appointed`.

### Checks run

- Full check, item limit 150: `ok: mode full, 139 top-level items, 6 tables`.
- Spine check: 139 top-level items, 6 tables. Module gate (`check_modules.py`): PASS.
- Every spine statement is still copied word for word. The only differences are the four shortened `*[from ...]*` lists noted above.
- No proof sentence is longer than 30 words, and each chapter file keeps one line-ending style.
- Preview: `preview\full-draft.md` and `preview\full-draft.pdf`, 62 pages, with no raw keys in citations.

### For Step 12

- `t:mutual-support`'s caption says neither proposal lowers what the other regular values "by more than" the cost of opposing it, which allows equality, while `l:mutual-refrain` needs the Against vote to be worth less than its cost. The new step `inf:refrain-worth` states the lemma's strict premise. The caption may need "by less than" (medium confidence: the table's strict ranks need the strict case).
- Still open from before: the Theorem's "review whose gain is spread across all users goes undone" and "checks on each of these effects".

### Files

- Changed: `ch-03.md` to `ch-11.md`, `02-spine.md`, and the two preview files.
- Added: `step11b_audit.py`, `step11b_apply.py`, and the spec files in `step11-finish-parts`.
- Snapshot: `step-11b`.
