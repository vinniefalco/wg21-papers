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
2. Under each top-level item that has no spine children, write the lettered lemmas that prove it, with roman steps where a lemma needs more than one link; under each spine child, write the roman steps that prove it. A child may cite only foundation items, spine items of earlier chapters, earlier items of this chapter, or its own children. Write no children for an item that restates or joins the items it cites, or follows from them in one step a committee member accepts on sight; its `*[from ...]*` citation is its proof.
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

Write one finding per failure to the Output file, at most three sentences, in this form: `KEY | type (invalid step, hidden premise, overreach, forward citation, table rank) | the problem | the weakest fix: weaker wording, an added cited premise, or a cut`. Write nothing for items that pass. Write the file in full.

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

Write one finding per objection to the Output file in this form: `KEY | reader | the objection | the weakest change that would make the reader accept the sentence`. Write the file in full.

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
