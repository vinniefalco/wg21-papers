"""Write step-11-spine-changes.md from the step-11-pre-spine snapshot and the revised files."""
import re
from pathlib import Path

S = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof")
SNAP = S / "snapshots" / "step-11-pre-spine"
START = re.compile(r"^( *)1\. (.*)$")
END = re.compile(r"\s*\{#([a-z:0-9-]+)(?: weakened)?\}\s*$")
KIND = re.compile(r"^\*\*\w+\.\*\* ")
CITE = re.compile(r"\s*\*\[(?:from|proved by)[^\]]*\]\*")


def statements(paths):
    out = {}
    for path in paths:
        buf = None
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            m = START.match(line)
            if m and buf is None:
                buf = m.group(2)
            elif buf is not None and line.strip():
                buf += " " + line.strip()
            if buf is not None:
                e = END.search(buf)
                if e:
                    text = KIND.sub("", END.sub("", buf))
                    out.setdefault(e.group(1), " ".join(CITE.sub("", text).split()))
                    buf = None
    return out


OLD = statements([SNAP / "01-foundation.md", SNAP / "02-spine.md"] + sorted(SNAP.glob("ch-*.md")))
NEW = statements([S / "01-foundation.md", S / "02-spine.md"])

# key, kind, old source key ("new" if none), new source key ("cut" if none), claim note
E = []
def add(key, kind, note, old=None, new=None):
    E.append((key, kind, old if old is not None else key, new if new is not None else key, note))

# Foundation
add("ax:repeat", "folded premise (A61)", "strengthened: adds a chair's expectation from an author's procedural record; basis D4195 premise A61, folded as the support report advises")
add("ax:prefer", "addition 3", "strengthened: a sponsor's interests can depend on particular features of a design; basis user-approved addition (3)")
add("ax:attention", "addition 12 (and 9)", "strengthened: what a participant learns from a paper or its discussion can change their vote; basis user-approved addition (12)")
add("ax:unknown", "folded premise (A9, A27)", "strengthened: a room cannot fully judge a design even after implementation, and more parts and interactions hide more defects; basis premises A9, A27")
add("ax:first-review", "folded premise (A84r)", "strengthened: reviewers of an early part cannot study in detail what later parts will require; basis premise A84r, with 'see' read as 'study in detail' per the support report")
add("ax:rework", "folded premise (A29)", "strengthened: more is built on a design after each favorable poll; basis premise A29")
add("ax:learning", "folded premise (A13, A19, A58, A59, A62)", "strengthened: some learning only by attending; procedure differs from design skill; options limited to those known; knowledge lowers effort and raises the chance of adoption, other things equal")
add("ax:turnover", "folded premise (A20, A67, A68)", "strengthened: papers stay available for decades; absentees learn only from records or memory; a written objection is easier to raise again")
add("ax:users-affected", "folded premise (A8, A18r) and addition 8", "strengthened: gain spread across all users while the cost of taking part falls on the one who takes part; users differ; one user's effort seldom changes an outcome")
add("d:player", "moved", "unchanged: the definition now opens d:settled-pattern", new="d:settled-pattern")
add("d:settled-pattern", "moved", "unchanged: absorbs d:player's definition")
add("d:direction-poll", "moved", "unchanged: merged with d:forwarding-poll as d:polls", new="d:polls")
add("d:forwarding-poll", "moved", "unchanged: merged into d:polls", new="d:polls")
add("d:polls", "moved", "unchanged: merges d:direction-poll and d:forwarding-poll into one item", old="new")
add("d:feature-cutoff", "moved", "unchanged: merged into d:edition", new="d:edition")
add("d:edition", "moved", "unchanged: absorbs d:feature-cutoff")
add("d:result-seeking", "addition 12", "new definition, as the plan words it; rests on the weighing clause of ax:prefer", old="new")
add("d:design-bound", "addition 12", "new definition, as the plan words it; rests on ax:prefer and addition (3)", old="new")
add("f:plenary-consent", "new fact (D4195 C102)", "strengthened: adds the next SD-4 sentence, 'Most polls pass by unanimous consent.', quoted from the extract")
add("f:principle-based", "new fact (addition 7)", "new quoted fact, SD-4 'Proposals and papers'; named so the integration absence can set it aside", old="new")
add("f:early-merge", "new fact (addition 7)", "new quoted fact, SD-4 'Technical Specifications (TS) and White Papers'", old="new")
add("f:sd4-drafts", "new fact (addition 7)", "new parent for SD-4 'Working draft handling'", old="new")
add("f:wording-baseline", "new fact (addition 7)", "new quoted fact", old="new")
add("f:editors", "new fact (addition 7)", "new quoted fact; a check that approved changes were applied, not a check that designs fit", old="new")
add("f:iso-ballots", "moved", "unchanged: the parent now names clause 2.6.3")
add("f:enquiry-count", "moved (from chapter 10)", "unchanged claim: the chapter 10 roman step becomes a Fact under f:iso-ballots, quotes checked by build.py check 6")
add("f:incits-limits", "new fact (INCITS 3.9.2.3)", "strengthened: adds 3.9.2.3's sentence that SDO and consortium representatives may be employed by other voting members, per the ledger note")
add("f:no-merit-ruling", "sharpened (addition 6)", "strengthened: adds judging a design's quality; search terms quality, judge, evaluat, assess, merit found no SD-4 role for it")
add("f:no-paper-objections", "moved (from chapter 12)", "unchanged claim, with the TS and white paper exit-criteria exception added; search rerun with the same terms")
add("f:no-drawbacks-asked", "new fact (addition 9)", "new absence; search found no trade-off, drawback, downside, disadvantage, limitation, or weakness, and 'cost' only for travel", old="new")
add("f:no-interest-statement", "new fact (addition 12)", "new absence; search found no disclose, declare, affiliation, employ, sponsor, fund, company, or behalf, and 'interest' only in other senses", old="new")
add("f:no-integration-check", "new fact (addition 7)", "new absence; hits for integrat, consisten, together, harmon, conflict, and fits name no such step (good-paper fit, TS integration testing, and unrelated senses)", old="new")
add("f:no-parts-step", "new fact (addition 10, D4195 C114)", "new absence; hits for part, later, future, extend, subsequent, and depend name no such step", old="new")

# Chapter 2 (old chapters 2 and 3)
add("p:who-decides", "addition 6", "new lead of chapter 2; joins the rules it cites (wording rooms, ballots on whole documents, SD-4's quality absence)", old="new")
add("p:path", "cut", "padding: citers cite f:design-forward, f:wording-forward, f:plenary-owns; content kept in p:who-decides", new="cut")
add("p:design-in-rooms", "cut", "merged into p:who-decides, unchanged claim", new="p:who-decides")
add("p:chair-decides", "cut", "merged into p:who-decides, unchanged claim", new="p:who-decides")
add("p:who-votes", "sharpened", "changed: ballots added (from chapter 2's proof that ballots are cast by ISO member bodies); the registration clause moves to p:sponsor-votes, which cites f:registered")
add("m:players", "addition 12", "strengthened: lists result-seeking and design-bound authors as separate players; its children moved out, so it is no longer a module")
add("p:sponsor-no-vote", "adopted weakening", "weakened to the chapter 2 child's scope and moved into m:moves-sponsor", old="p:sponsor-no-vote-wg21", new="m:moves-sponsor")
add("m:moves-author", "sharpened", "unchanged: split into two sentences")
add("m:moves-regular", "sharpened", "unchanged: split into two sentences")
add("m:moves-chair", "sharpened", "unchanged: wording; basis adds f:direction-group")
add("m:moves-sponsor", "adopted weakening", "strengthened by the adopted statement: no vote of its own unless an ISO member body or liaison")
add("m:moves-user", "sharpened", "unchanged: split into two sentences")

# Chapter 3 (old chapter 4)
add("l:vote-count", "sharpened (module)", "new module statement joining its four children; claims unchanged", old="new")
add("l:against-double", "moved", "unchanged: child of l:vote-count")
add("l:neutral-outside", "moved", "unchanged: child of l:vote-count")
add("l:room-size", "moved", "unchanged: child of l:vote-count")
add("l:one-third-against", "moved", "unchanged: child of l:vote-count")
add("l:reasons-against", "cut", "padding: restated two facts; citers cite f:against-reasons, f:no-reasons-other", new="cut")
add("p:against-costs-more", "sharpened", "weakened: the Favor clause is dropped, since ax:support states no risk for Favor and l:settled-regular now argues Favor directly")
add("p:stake-threshold", "cut", "merged into p:doubt-outside-count with both channels, outcome and changes, kept", new="p:doubt-outside-count")
add("p:doubt-outside-count", "sharpened", "unchanged claim restated without the tautology: which doubts enter the count, and what an Against vote buys; rank lemmas become its children")
add("l:vote-below", "moved", "unchanged: chapter 4 rank lemma, now a spine child of p:doubt-outside-count")
add("l:vote-above", "moved", "unchanged: chapter 4 rank lemma, now a spine child of p:doubt-outside-count")
add("p:objector-coordination", "D4195 C101", "new: two settled patterns among objectors, from l:vote-count; the proof does not say which arises", old="new")
add("p:prefer-vs-stop", "sharpened", "unchanged")
add("p:mutual-support", "adopted weakening", "weakened to the strict case (each doubt worth less than the risk), and states the table's best cell from its rank lemmas")
add("l:mutual-refrain", "moved", "unchanged: chapter 4 rank lemma, now a spine child")
add("l:mutual-own-vs-other", "moved", "unchanged: chapter 4 rank lemma, now a spine child")

# Chapter 4 (old chapter 5)
add("p:persuasion-not-required", "sharpened", "unchanged")
add("p:advance-unanswered", "sharpened", "unchanged: basis cites the forwarding facts in place of the cut p:chair-decides")
add("p:record-indistinct", "sharpened", "strengthened: adds 'or why consensus was called over it' from the cut p:chair-no-reasons, same facts")
add("l:record-content", "moved", "strengthened: adds no record of why a consensus call was made, which f:no-reason-record already states; now a module child")
add("l:record-checks", "moved", "unchanged: now a module child")
add("l:iso-register-level", "moved", "unchanged: basis adds f:pmember-consensus, f:committee-stage from the chapter 5 proof")
add("p:definition-without-procedure", "sharpened", "unchanged")
add("l:consensus-test", "sharpened", "unchanged")
add("p:least-cost-response", "D4195 C105", "strengthened: adds that finding out whether the objectors are right leaves the count unchanged, from l:vote-count")
add("p:change-list", "D4195 C106", "strengthened: concerns as changes can be granted one at a time; opposition in any form weighs in the poll only as a vote, from f:against-reasons")
add("p:dissent-needs-paper", "adopted weakening", "weakened to the listed record types, per the chapter 5 child")
add("p:reasons-unrecorded", "adopted weakening and D4195 C86", "weakened (a later participant can voice the reason only by thinking of it anew) and strengthened (a proposal's paper lasts for decades; A67 in ax:turnover)")
add("p:repeat-objection", "sharpened", "strengthened: adds the two exceptions for national body comments from the cut l:nb-comment-limits")
add("p:late-objection", "sharpened", "strengthened: absorbs p:nb-route (escalation within the national body and its default), same facts")
add("p:nb-route", "cut", "merged into p:late-objection", new="p:late-objection")
add("p:fluency", "addition 11 (D4195 C20, C43, C76, C79, C82)", "new: objections and proposals count only in set forms and times, learned partly by attending", old="new")
add("p:newcomer", "moved (from chapter 6), D4195 C75", "strengthened: adds the effort comparison, other things equal (A58 in ax:learning); the incubator clause is kept")

# Chapter 5 (momentum, from old chapters 6 and 9)
add("ind:reversal-grows", "folded premise (A29), D4195 C31", "strengthened: 'grows' replaces 'does not fall' (A29 in ax:rework), and 'whether or not the design is wrong'")
add("p:incumbent-start", "moved, sharpened", "unchanged")
add("p:early-polls", "sharpened (D4195 C30, C84)", "changed: states when the incumbency poll can come and what it imposes; the author's 'does better ... unless' moves to the two author-type lemmas")
add("p:challenger-bar", "sharpened (D4195 C25)", "strengthened: the hurdle grows and the incumbent faces none, from ind:reversal-grows")
add("l:poll-wording", "sharpened (D4195 C77, C83, C85)", "strengthened: passing a direction poll makes the design the incumbent; 'a chair may take any poll' is left to m:moves-chair")
add("p:roadmap-poll", "addition 1", "new conditional result", old="new")
add("p:review-share", "moved, D4195 C29", "strengthened: adds more places for defects (A27 in ax:unknown)")
add("p:light-review", "D4195 C98", "new", old="new")
add("p:burden-flip", "moved (from chapter 9), D4195 C64", "unchanged: states the default flip the old basis gave")
add("p:late-arrival", "D4195 C3, C50, C102", "new; the three obstacles point the same way, and the proof claims no multiplication", old="new")

# Chapter 6
add("p:sponsor-votes", "moved, sharpened", "unchanged")
add("p:sponsor-features", "addition 3, D4195 C120", "new: costs still to come fall on the sponsors, the gain is spread across users, one 2:1 norm for every proposal", old="new")
add("ind:adopted-parts", "sharpened (D4195 C112)", "strengthened: from large proposals to any design adopted in parts; its steps used only that the parts belong to one design")
add("p:parts", "sharpened", "changed: states the gain and the cost; 'do better ... unless' moves to l:settled-design-bound")
add("p:first-part", "addition 10, D4195 C109, C111, C115", "new; best first move only for a design-bound author, limited by opponents who foresee the rest", old="new")
add("p:large-position", "sharpened", "unchanged: l:plenary-priority folded into its statement")
add("l:plenary-priority", "cut", "folded into p:large-position and p:roadmap-poll", new="p:large-position")
add("p:small-position", "sharpened", "weakened: drops 'needs an on-time paper and a presenter', now in p:fluency; adds that the author bears every meeting's cost alone (d:small)")
add("p:size-attributes", "sharpened", "unchanged")
add("p:money-vs-presence", "cut", "padding: citers cite ax:cost, ax:who-pays, f:remote; its facts are cited by p:who-takes-part", new="cut")

# Chapter 7
add("p:sg-decides", "sharpened", "unchanged; module now holds l:sg-attendance")
add("l:sg-purpose", "unchanged", "unchanged")
add("l:sg-attendance", "sharpened (moved into the p:sg-decides module)", "changed from a threshold tautology to study group voters' self-selection; absorbs p:concern-presence")
add("l:sg-start", "sharpened", "weakened: the voters clause moves to l:sg-attendance")
add("p:concern-presence", "cut", "folded into l:sg-attendance", new="l:sg-attendance")
add("p:sg-sponsor", "addition 2", "new, with the arithmetic of a third and two thirds", old="new")
add("p:deadlock", "sharpened (D4195 C6)", "unchanged: 'at least a third'")
add("p:design-changes", "adopted weakening (replaced)", "cut: p:deadlock's 'a design changes' covers both paths the chapter 7 child found; l:settled-sg-chair cites p:deadlock", old="p:design-changes", new="cut")
add("p:attrition", "sharpened (D4195 C92)", "strengthened: states the table's settled cell, proved by its rank lemmas, whichever design is better")
add("p:sg-unified", "cut", "padding: l:settled-sg-chair cites f:sg-formation, f:sg-initial-proposal, p:deadlock", new="cut")
for k in ("l:hold-yield-holder-gains", "l:hold-yield-both-hold", "l:hold-yield-whole-over-half", "l:hold-yield-half-over-deadlock", "l:hold-yield-half-over-none", "l:hold-yield-cheap-holds", "l:hold-yield-costly-yields"):
    add(k, "moved", "unchanged: chapter 7 rank lemma, now a spine child of p:attrition; two sentences joined where there were two, and p:attrition dropped from its basis to avoid a cycle")
add("t:hold-or-yield", "moved", "unchanged ranks; citation reconciled to the five rank lemmas, as chapter 7 wrote it", old="new", new="cut")

# Chapter 8
add("p:chair-threshold", "sharpened", "changed: states the costs of every call and the post risk of a departure (absorbs p:chair-costs and l:appointments); the 'does better only when' moves to the settled lemmas")
add("p:chair-costs", "cut", "merged into p:chair-threshold", new="p:chair-threshold")
add("l:appointments", "cut", "folded into p:chair-threshold", new="p:chair-threshold")
add("l:chair-role", "cut", "content in p:who-decides", new="p:who-decides")
add("p:chair-default", "sharpened", "unchanged, absorbs p:repoll; adds the table's result from its rank lemmas")
add("p:repoll", "cut", "merged into p:chair-default; 'only Against voters are named for questions' is in p:against-costs-more", new="p:chair-default")
add("l:call-above", "moved", "unchanged: chapter 8 rank lemma, now a spine child")
add("l:call-below", "moved", "unchanged: chapter 8 rank lemma, now a spine child")
add("p:chair-confidence", "D4195 C78 (A61)", "new", old="new")
add("p:chair-no-reasons", "cut", "merged into p:record-indistinct; weakened: 'recording reasons takes meeting time' dropped", new="p:record-indistinct")
add("p:private-channel", "sharpened", "unchanged")
add("p:plenary-ratifies", "sharpened (D4195 C102)", "strengthened: adds 'most polls pass by unanimous consent' (f:plenary-consent); 'does not redesign' restated positively")
add("p:wording-rooms", "cut", "content in p:who-decides", new="p:who-decides")

# Chapter 9
add("p:users-out", "addition 8, D4195 C38, C39, C107", "new lead of chapter 9", old="new")
add("p:who-takes-part", "D4195 C18, C40, C81, C96", "new", old="new")
add("p:reward-timing", "moved, sharpened (D4195 C32)", "unchanged")
add("l:implementation-informs", "moved, folded premise (A9)", "strengthened: even after implementation a room cannot fully judge a design")
add("p:merit-gap", "D4195 C4", "new; rests on A9 in ax:unknown", old="new")
add("p:review-shortfall", "D4195 C10, C28", "new; direction shown, size not", old="new")
add("p:integration", "addition 7", "new; the absence fact is searched, and the nearest SD-4 steps are named and set aside", old="new")
add("l:author-knows-more", "moved, sharpened", "unchanged")
add("p:disclosure", "addition 9, D4195 C87", "new", old="new")
add("p:written-answer", "D4195 C87, C89", "new; the effect on the author can go either way", old="new")

# Chapter 10 (old chapters 9 and 10)
add("p:miss-cost", "sharpened", "strengthened: absorbs p:schedule-protects")
add("l:cutoff", "unchanged", "unchanged")
add("p:schedule-protects", "cut", "merged into p:miss-cost", new="p:miss-cost")
add("p:cutoff-effect", "sharpened", "unchanged: absorbs p:one-meeting-cycle")
add("p:one-meeting-cycle", "cut", "merged into p:cutoff-effect", new="p:cutoff-effect")
add("p:prefer-is", "sharpened (addition 12)", "changed: states the delay and the opposite worth of TS experience to the two author types; the 'does better ... unless' is dropped")
add("t:is-or-ts", "cut", "cut with its three rank lemmas: its ranks only restated the room's choice of vehicle", old="new", new="cut")
add("p:bundling", "cut", "content in p:who-decides; national body items cite it and the ballot facts", new="p:who-decides")
add("l:ballot-rules", "sharpened", "strengthened: states both ballots' pass thresholds, from f:enquiry-count and f:iso-ballot")
add("l:nb-no-scope", "cut", "merged into p:nb-comment", new="p:nb-comment")
add("p:nb-comment", "sharpened", "strengthened: adds that a body wanting the work in no form does better voting No, from its rank lemmas")
add("l:rank-rest-yes", "moved", "unchanged: chapter 10 rank lemma, now a spine child")
add("l:rank-rest-abstain", "moved", "unchanged: chapter 10 rank lemma, now a spine child")
add("l:rank-oppose-no", "moved", "unchanged: chapter 10 rank lemma, now a spine child")
add("l:rank-oppose-abstain", "moved", "unchanged: chapter 10 rank lemma, now a spine child")
add("l:nb-comment-limits", "cut", "folded into p:repeat-objection and p:credible-threat; l:cutoff covers added features", new="p:repeat-objection")
add("p:credible-threat", "addition 4", "new", old="new")
add("p:nb-members", "adopted weakening", "weakened to the chapter 10 child's INCITS wording, with 3.9.2.3 quoted in f:incits-limits", old="p:nb-members-incits")
add("l:incits-votes", "new fact (INCITS 3.9.2.3)", "strengthened: adds that SDO and consortium representatives may be employed by other voting members")
add("p:nb-early", "cut", "folded into p:credible-threat and l:settled-nb", new="p:credible-threat")
add("p:appeal-continues", "cut", "padding: l:checks-record cites its facts", new="cut")

# Chapter 11
add("l:settled-regular", "adopted weakening (tie), sharpened", "unchanged choice: under 'does no better than', 'otherwise Neutral' already holds at the tie; adds the vote's cost and narrow gain")
add("l:settled-large-author", "replaced (addition 12)", "replaced by l:settled-design-bound, l:settled-result-seeking, and l:weighs-both; each choice is now stated by type", old="l:settled-large-author-weak", new="l:settled-design-bound")
add("l:settled-design-bound", "addition 12", "new: early polls, parts, vehicle, disclosure, rivals, objections", old="new")
add("l:settled-result-seeking", "addition 12", "new", old="new")
add("l:weighs-both", "addition 12", "new; holds for two-way choices under ax:prefer's single scale", old="new")
add("p:same-moves", "addition 12", "new", old="new")
add("l:disclose-result-seeking", "addition 12", "new rank lemma", old="new")
add("l:disclose-design-bound", "addition 12", "new rank lemma", old="new")
add("t:disclose", "addition 12", "new table: one choice by author type", old="new", new="cut")
add("l:settled-small-author", "sharpened", "unchanged: costs borne alone")
add("l:settled-sg-chair", "sharpened", "unchanged")
add("l:settled-design-chair", "sharpened (D4195 C78)", "strengthened: adds taking up first the paper of an author with a procedural record (p:chair-confidence)")
add("l:settled-convenor", "adopted weakening", "weakened to the cases SD-4's procedure settles", old="l:settled-convenor-weak")
add("l:settled-nb", "sharpened", "unchanged")
add("l:settled-sponsor", "sharpened (addition 2)", "strengthened: study groups included (p:sg-sponsor)")
add("l:settled-user", "adopted weakening, addition 8", "weakened to the net-gain form, and states the cost-and-gain asymmetry", old="l:settled-user-weak")
add("p:checks", "sharpened", "unchanged across parent and children; the list moves into five spine children; adds f:principle-based and f:editors")
add("l:checks-hearing", "moved", "unchanged: chapter 11 child, now in the spine")
add("l:checks-alternatives", "moved", "strengthened: adds a good paper's design principles (f:principle-based)")
add("l:checks-deadlock", "moved", "unchanged")
add("l:checks-attendance", "moved", "unchanged")
add("l:checks-record", "moved", "strengthened: adds the editing committee and the appeal limits (facts formerly under p:appeal-continues)")
add("thm:settled", "adopted weakening, rewritten by priority", "follows the adopted and new lemmas; states each author type's choices and the six priority results, each from a cited item", old="thm:settled-weak")

# Chapter 12
add("c:predictions", "sharpened", "unchanged: eleven children")
add("c:pred-sponsor-against", "adopted weakening (D4195 C65)", "weakened to the matched comparison", old="c:pred-sponsor-matched")
add("c:pred-abstention-length", "unchanged", "unchanged")
add("c:pred-parts", "sharpened", "unchanged: basis adds p:first-part")
add("c:pred-first-part", "D4195 C110 (prediction)", "new", old="new")
add("c:pred-rival-polls", "D4195 C91 (prediction)", "new", old="new")
add("c:pred-removals", "adopted weakening", "weakened per the chapter 12 child", old="c:pred-removals-likely")
add("c:pred-small-fade", "D4195 C94 (prediction)", "unchanged")
add("c:pred-nb-positions", "unchanged", "unchanged: basis re-pointed")
add("c:pred-written-answers", "sharpened", "unchanged: basis adds f:no-paper-objections, p:written-answer")
add("c:pred-defects", "D4195 C116 (prediction)", "new; states A86 and A87r as the prediction's assumption and matching", old="new")
add("c:pred-competing", "D4195 C119 (prediction)", "new; states A88's content as the prediction's assumption", old="new")
add("c:levers", "addition 5", "strengthened scope: changes to what a move costs as well as to rules")
for k in ("c:lever-anonymous", "c:lever-reasons-all", "c:lever-sponsor-limit", "c:lever-written-answer", "c:lever-deadlock-rule", "c:lever-ts-path", "c:lever-sustained-procedure"):
    add(k, "sharpened", "unchanged: basis re-pointed to surviving keys")
add("c:lever-nb-more", "addition 5", "new comparative statics: more national body oversight during meetings", old="new")
add("c:lever-nb-less", "addition 5", "new comparative statics: less national body oversight during meetings", old="new")


def show(source, key):
    if key == "new":
        return "new"
    if key == "cut":
        return "cut"
    return source.get(key, "(" + key + ")")


lines = [
    "# Step 11 spine changes",
    "",
    "One line per change: key | kind | old statement or \"new\" | new statement or \"cut\" | claim unchanged, weakened, or strengthened, with basis. Old statements come from snapshot `step-11-pre-spine` (spine, foundation, and chapter files, where weakened children carry the adopted wording); new statements from the revised `01-foundation.md` and `02-spine.md`. Chapter headings changed: old chapters 2 and 3 merged as \"2. Who decides, and with what moves\", old chapters 9 and 10 merged as \"10. The schedule and national bodies\", and a new chapter \"9. Users, quality, and disclosure\".",
    "",
]
listed = set()
for key, kind, old, new, note in E:
    listed.add(key)
    lines.append("- %s | %s | %s | %s | %s" % (key, kind, show(OLD, old), show(NEW, new), note))

unlisted_changed = sorted(k for k in NEW if k in OLD and NEW[k] != OLD[k] and k not in listed)
unlisted_new = sorted(k for k in NEW if k not in OLD and k not in listed)
spine_old = statements([SNAP / "02-spine.md"])
unlisted_gone = sorted(k for k in spine_old if k not in NEW and k not in listed)
(S / "step-11-spine-changes.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print("entries", len(E))
print("unlisted changed:", unlisted_changed)
print("unlisted new:", unlisted_new)
print("unlisted gone:", unlisted_gone)
