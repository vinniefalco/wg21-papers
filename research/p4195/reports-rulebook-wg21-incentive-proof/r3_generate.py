"""Step 12 round 3: write the chapter fix files, the adversarial log section, and the counts.

Reads r3-findings.tsv (from r3_parse.py), r3-decisions-a.txt and r3-decisions-b.txt, the spine
statements now in 02-spine.md, and r3_spine_apply.py's lists of changed keys.
Writes fix-r3-chNN.md, r3-log-section.md, and r3-summary.txt. Appends the log section to
adversarial-log-draft.md only when run with --append-log.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import check_spine_sync  # noqa: E402
import r3_spine_apply  # noqa: E402

DATE = "2026-10-20"
REVIEWER = {"R": "rules check", "D": "reader", "L": "logician"}
SECTION = {"R": "Rules check", "D": "Reader", "L": "Logician", "A": "Skeptics A", "B": "Skeptics B"}
TYPE_NAME = {"1": "type 1", "2": "type 2", "3": "type 3", "4": "type 4", "W": "wording", "P": "proof step"}

# Sent findings whose fix needs new proof content: a new lemma or step, or a redesigned test.
# Citation-only and wording fixes are not counted.
NEWSTEP = {"12.3L9", "12.3L7", "12.3A30", "12.3B2", "12.3L12", "12.3B7", "12.3B11", "12.3B12", "12.3B22"}

# Changed spine statements whose chapter children must change, with what the fix should do.
# Only children in the same chapter as the statement; other follow-ons are in EXTRA.
CHILD_NOTES = {
    "m:moves-user": "inf:user-joins is unchanged. The new move is weighed in chapter 11 (l:user-moves, 12.3B17).",
    "p:reasons-unrecorded": "l:concern-followup takes 12.3R4's wording and l:argument-writing takes 12.3D7's; l:case-lasts and l:reason-fades already prove the rest.",
    "p:fluency": "l:objection-forms takes 12.3A17 (the late-documents clause scoped to outside ad hoc groups and comment resolution); l:rules-by-attending already proves the second sentence.",
    "p:late-arrival": "l:late-record takes 12.3D10; l:late-removal and l:late-reversal already prove the first sentence.",
    "p:first-part": "Its second sentence now names l:first-part-smallest's reason (ready and reviewed sooner), which is already its child; no new child is needed. l:first-part-foresight takes the narrowed ax:first-review (follow-on below).",
    "l:call-above": "Global decision 2: its steps already say \"a chair\"; check that inf:call-above-post and inf:call-below-post rest on p:chair-threshold and ax:post-risk, which cover every subgroup chair, and keep d:rooms in the bases.",
    "t:chair-call": "The caption now says \"A chair's consensus call\"; l:call-above and l:call-below follow (global decision 2).",
    "p:users-out": "l:traced-voters takes 12.3R6 (ISO member bodies cast the ballot votes); l:nb-position-time is unchanged.",
    "t:nb-ballot": "The caption now states that in both columns the No is accompanied by comments of a technical nature. In inf:oppose-no-rank and inf:no-gains-nothing, cite that case: only a No with technical comments counts against approval (inf:no-counts-against), and in the table's case the No has them (12.3L4, 12.3L5).",
    "l:settled-regular": "In l:favor-supported write \"On a poll of a colleague's proposal that a regular supports, ...\", and add a step that in a poll between two colleagues' designs, or an approval poll among them, a vote for one counts against the other, so ax:support's cost applies there (12.3B1, 12.3A7). inf:thm-authors-regulars inherits the scope.",
    "l:settled-user": "In l:user-moves write \"A user casts no vote in WG21's polls or ballots. Each move open to a user costs time or money: taking part, TS feedback, a paper a participant presents, or a move through a national body.\" (12.3B17)",
    "t:disclose": "In inf:rs-state-rank write that in that case stating the trade-off costs no adoption and takes time worth less than the better design it brings, so the author ranks it first; cite the case (12.3A36).",
    "thm:settled": "Make the Theorem's children prove the new sentences: the lemma l:thm-open-choices and l:thm-pattern (12.3L9, section \"Global decision 1\" below); l:thm-deciders, inf:thm-no-user-vote, and inf:thm-no-cap (12.3B17, 12.3D18, 12.3D19, 12.3R6, 12.3B16); l:thm-gaps and inf:thm-review-undone (12.3L10: \"In this pattern, whether to study a paper is a choice each player makes the way that does best for them, so no player does that review\", citing the dominance step inf:open-study); the regular sentence rests on l:settled-regular's new scope and the sponsor sentence on l:settled-sponsor (12.3L8), which already has the condition.",
    "c:pred-sponsor-against": "inf:sa-share sets aside the authors' own Favor votes, which the author list bounds (12.3B4); inf:sa-evidence takes 12.3A40; inf:sa-tell-apart takes the timing redesign (12.3L12); inf:sa-weighs takes 12.3D20.",
    "c:pred-abstention-length": "Rebuild inf:al-study, inf:al-rise, inf:al-evidence, inf:al-narrow, and inf:al-tell-apart for the new comparison: revisions at the same place in their proposals' sequences, measured by the length each adds since the previous revision (12.3A41), in polls of the same form, which holds stakes fixed (12.3L13), relative to other papers polled at the same meetings, which sets aside aging and narrower topics (12.3B9).",
    "c:pred-parts": "inf:pa-ease and inf:pa-tell-apart say \"little reason\" (12.3L14); inf:pa-tell-apart counts only later parts that already existed (12.3A42); inf:pa-sequence, inf:pa-evidence, and inf:pa-ease say \"large proposals\" (12.3D22 to 12.3D24).",
    "c:pred-first-part": "Rebuild inf:fp-seldom and inf:fp-tell-apart for the stand-in: first papers whose authors' stated sponsor has interests depending on the design's features (d:design-bound's own example; inf:sa-evidence for stated affiliations) are predicted to omit later parts more often than other first papers (12.3A43, 12.3B6); inf:fp-small and inf:fp-small-steps say \"first papers of small scope\" (12.3D25, 12.3D26).",
    "c:pred-removals": "inf:rm-tell-apart counts failed removal polls outside ballot comment resolution, where SD-4's consensus goal and near-unanimity apply (f:near-unanimous) (12.3A25), with 12.3D28's wording; inf:rm-need takes 12.3D27.",
    "c:pred-small-fade": "inf:sf-tell-apart compares stops before and after a waiting author's sponsor leaves WG21 altogether, a loss unrelated to the proposal and observable when all the sponsor's stated affiliations end (12.3L15); drop \"reflection made before submission\". inf:sf-evidence takes 12.3A44.",
    "c:pred-nb-positions": "Rebuild inf:nb-few as the cost prediction: forming a position takes members' time wherever it is formed, and attending in person, which costs a body less at meetings in its own country (ax:cost), lets its members know the discussion and caucus, so the model predicts more positions on proposals decided there; drop \"few\" (12.3L16). inf:nb-tell-apart holds the body fixed and compares meetings in its own country with others, between which agreement predicts no difference and which a body does not choose by agenda (12.3L17, 12.3A27). inf:nb-evidence takes 12.3A26 and 12.3B22.",
    "c:pred-written-answers": "inf:wa-tell-apart compares the unanswered share among omitted objections with the same share among stated objections, both raised at plenary (12.3A12), and states the consent condition (12.3A11); inf:wa-predict takes 12.3B11.",
    "c:pred-defects": "inf:de-predict says no difference would count against the model or that condition (12.3A45); inf:de-tell-apart takes 12.3B12.",
    "c:pred-competing": "inf:co-tell-apart matches scope and size as well as implementation experience and turnout, since harder topics have more parts and more places for defects (ax:unknown) (12.3A46); inf:co-shortfall takes 12.3L18.",
    "c:lever-reasons-all": "inf:ra-favor and inf:ra-shift add that a supporter whose vote seldom changes the result would weigh the reasons cost against Favor and could do better not voting (l:vote-count, inf:ra-cost) (12.3A13).",
    "c:lever-sponsor-limit": "Rebuild inf:sl-predict for the change: once the limit applies, the removed votes lower margins for proposals whose authors one sponsor pays beyond it, while proposals with as many authors paid by separate sponsors keep theirs and serve as the comparison (12.3A47).",
    "c:lever-written-answer": "inf:lw-borne: once the answer must be in a public record, the objection is in public writing whatever the paper says; inf:lw-predict keeps its prediction (12.3A48).",
    "c:lever-sustained-procedure": "inf:sp-register already proves that the leadership registers a declared opposition it does not resolve; name the recorded answer as the lever's addition to ISO's steps (12.3R14).",
    "c:lever-nb-more": "inf:nm-tabled takes 12.3R15 and 12.3D32; add a step that ISO bars formal discussion during official meetings of a document out for ballot or comment (f:ballot-discussion), so cheaper positions during meetings cannot reach it (12.3B20).",
    "c:lever-nb-less": "inf:nl-fewer drops the \"few\" sentence (12.3L16, 12.3D33); inf:nl-ballot takes 12.3B21.",
}

EXTRA = [
    ("03", "chapter 3 recap", "12.3A3", "the Against vote's reach", "In the recap write \"and counted alone it changes the result only when the count is one or two votes above the 2:1 threshold\" for \"and it changes the result only when the count is one or two votes above the 2:1 threshold\"."),
    ("05", "l:removal-polls", "12.3A18", "SD-4's goal for changes at ballot comment resolution", "Write \"Design rooms own selecting designs and plenary does not change them, so a removal, by paper or comment, needs the 2:1 norm in a design room.\" and add a sentence or step: \"One answering a ballot comment must also aim, SD-4 says, to improve consensus.\" Cite f:near-unanimous, which now quotes that sentence."),
    ("05", "l:ts-merge-default", "12.3A39", "the grace-period call", "Add that SD-4 asks participants who prefer a different approach to develop their own alternatives during the TS lag, keeping the default as it is. f:ts-default now quotes the grace-period sentence. Split into two sentences if over 30 words."),
    ("06", "l:first-part-foresight", "12.3A33", "ax:first-review now covers unpublished later parts", "Write \"At the first part's polls, only those who foresee the rest can base their vote on what the later parts will need of it. Others cannot study that in detail while those parts are unpublished, and SD-4 asks no paper to state it.\" inf:foresight-ask follows."),
    ("09", "chapter 9 recap", "12.3D13, 12.3R6", "the channel list", "In the recap write \"users' interests affect decisions only through what participants value, papers a participant presents, TS feedback, and ISO member bodies\"."),
    ("11", "inf:regular-alongside", "12.3A2", "m:moves-regular's new moves", "List the added moves (filing an issue, raising a concern on the email lists, commenting on minutes) with the others as moves that go with any vote and take time. Cite m:moves-regular."),
    ("11", "l:convenor-given", "12.3A16", "m:moves-convenor's new moves", "Show that seeing outcomes documented, addressing comments on minutes, and reviewing participation go with following SD-4's plenary procedure: they concern the record and attendance, not the call, which still does best whatever they are. Cite m:moves-convenor, f:minutes-objections, f:inactive-experts."),
    ("11", "l:sg-other-moves, inf:dchair-before-call", "12.3R2", "m:moves-chair's \"early, limited exploration\"", "Write \"allowing early, limited exploration\" for \"allowing limited exploration\" in both."),
    ("11", "inf:thm-no-cap", "12.3B16", "national bodies choose whom to appoint", "Write \"Each participant a sponsor pays to attend has a vote, and no rule limits how many it pays, while each must be appointed by a national body or liaison that chooses whom to appoint, and SC22 may cap how many each appoints.\" Split into two sentences if over 30 words. Cite p:sponsor-votes and d:rules."),
]

CONTEXT = """Context from the round 3 reconcile, which changed the foundation and the spine before this file was written:

- Foundation. New Fact `f:ballot-discussion` (ISO 1.7.5: no formal discussion during official meetings of a document out for ballot or comment). Extended Facts: `f:in-situ` (plenary approves the changes in the applied form), `f:near-unanimous` (changes at ballot comment resolution have one goal, to improve consensus), `f:show-alternatives` (the author should show reasonably thorough consideration), `f:ts-default` (the TS lag is a grace period for developing alternatives), `f:late-documents` (ad hoc groups and comment resolution are exempt from the deadlines). `f:iso-no-answer` now also excepts 2.6.5's observations on each comment; `f:no-drawbacks-asked` now says neither SD-4 nor any listed clause uses the word trade-off. `ax:first-review`'s second sentence now reads "while those parts are unpublished". `d:user` now says a guest a convenor invites participates and so is not a user.
- Scope. `l:settled-regular` and the Theorem's regular sentence are now stated for a poll on one proposal. The Theorem's open choices now include any call SD-4 leaves to a chair or the convenor, such as the call at a Neutral majority and the choice among rivals that all meet the 2:1 norm. `l:call-above` and the chair table now cover any chair (global decision 2). "No user votes" in the Theorem now reads "No user votes in WG21's polls or ballots".
- Words. Write "is kept only in" or "remains only in", not "survives only in"; "affect decisions", not "reach decisions"; "large proposals", not "large designs"; "first papers of small scope", not "small first papers"; "allowing early, limited exploration" for the chairs' discretion. Do not use "carry" or "door".
- Length. Each item has at most two sentences of at most 30 words. Where a statement needs more, keep its claim in the item and make each other sentence a child step with its own key, one sentence each. Never nest deeper than three levels: a level-3 step that needs support cites an earlier level-3 step placed before it.
- Citations. A child may cite only foundation items, spine items of earlier chapters, earlier items of its own chapter, or its own children.
- Spine lines below quote statements already changed in this chapter and in `02-spine.md`. Do not edit those statements; make their children prove them, or cut children that no longer serve them. Never soften a plain, sharp, true statement.
"""

CH_SECTIONS = {
    "11": """## Global decision 1: a joint best reply for the Theorem's open choices

Add one lemma under the Theorem, placed immediately before `l:thm-pattern`, with the key `l:thm-open-choices`. Cite it in `l:thm-pattern`'s `*[from ...]*` list and add it to the Theorem's `*[proved by ...]*` list. Keep `l:thm-pattern`'s two sentences exactly as they are. Write the lemma at the second level and its steps at the third, one sentence of at most 30 words each, citing only foundation items, spine items of earlier chapters, and earlier items of chapter 11.

Statement to write: "Each choice the Theorem leaves open can be made so that all of them do best together, wherever the rules order them, they act on separate polls, or one does best whatever the other chooses."

Steps, in this order (wording may be improved; claims and citations as given):

1. `inf:open-first`: National bodies appoint experts and sponsors choose whom to pay before a meeting, and a paper reaches the meeting's mailing before anyone studies it. Cite f:experts-appointed, m:moves-sponsor, f:agenda-papers.
2. `inf:open-order`: In a design room, a chair's one-meeting delay comes before the forwarding poll, the author's vehicle request is made by that poll, and the chair's call follows its votes. Cite f:no-wait-alternatives, f:design-forward, f:vehicle, f:two-to-one.
3. `inf:open-plenary`: The convenor's plenary call comes after the subgroups' calls, and national bodies vote on a draft only after plenary sends it to ballot. Cite f:plenary-owns, f:plenary-consent, f:editors, f:iso-ballot.
4. `inf:open-votes`: In each poll, Favor does best for a regular who supports the proposal whatever the others choose, and the doubters' votes have a settled pattern. Cite l:settled-regular, p:objector-coordination.
5. `inf:open-back`: Each ordered choice is among finitely many options, so working back from the last, each has a best option given the choices before it and the best choices after it, and these do best together. Cite inf:open-first, inf:open-order, inf:open-plenary, inf:open-votes, d:does-better, d:settled-pattern.
6. `inf:open-rooms`: Open choices made at the same time in separate rooms act on separate polls, and each player's gain from its own choice turns on its own poll and costs, so neither changes the other's payoff. Cite ax:parallel-rooms, d:stake, ax:prefer, ax:post-risk.
7. `inf:open-study`: A participant for whom close study of a paper is worth less than its cost does best skipping it whatever the others study, since what study brings them through the poll is worth no more than their stake. Cite p:review-share, p:review-shortfall, d:stake, ax:review-cost, d:does-better.

Then `inf:thm-review-undone` cites `inf:open-study` (12.3L10). Do not claim more: the one pair this lemma does not cover is two participants for whom close study of the same paper can be worth its cost, choosing at once without knowing each other's choice. The ledger reports that pair for the main agent; do not narrow `l:thm-pattern` or the Theorem, and do not add a premise for it.
""",
}


def load_findings():
    rows = list(csv.reader(open(S / "r3-findings.tsv", encoding="utf-8"), delimiter="\t"))[1:]
    return {r[0]: r for r in rows}, [r[0] for r in rows]


def load_decisions():
    dec = {}
    for name in ("r3-decisions-a.txt", "r3-decisions-b.txt"):
        for line in (S / name).read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                p = line.split("|")
                if len(p) != 6:
                    sys.exit("bad decision line: " + line[:80])
                dec[p[0]] = dict(id=p[0], status=p[1], type=p[2], ch=p[3], problem=p[4], note=p[5])
    return dec


def chapter_of_keys():
    owner = {}
    for path in sorted(S.glob("ch-[0-9][0-9].md")):
        for m in re.finditer(r"\{#([a-z]+:[A-Za-z0-9-]+)(?: weakened)?\}", path.read_text(encoding="utf-8")):
            owner[m.group(1)] = path.name[3:5]
    return owner


def reviewer_label(fid, finding):
    kind = fid[4]
    if kind in REVIEWER:
        return REVIEWER[kind]
    return finding[3]


def finding_type(fid, finding):
    return finding[3] if fid[4] in "RDL" else "objection"


def disposition(d):
    if d["status"] == "A":
        return "applied, %s: %s" % (TYPE_NAME[d["type"]], d["note"])
    if d["status"] == "S":
        return "sent to fix-r3-ch%s.md, %s" % (d["ch"], TYPE_NAME[d["type"]])
    return d["note"]


def main():
    findings, order = load_findings()
    dec = load_decisions()
    missing = [fid for fid in order if fid not in dec]
    extra_ids = [fid for fid in dec if fid not in findings]
    if missing or extra_ids:
        sys.exit("decisions missing %s, unknown %s" % (missing, extra_ids))
    for fid, d in dec.items():
        if d["status"] not in "ASMR" or (d["status"] in "AS" and d["type"] not in TYPE_NAME):
            sys.exit("bad status or type: " + fid)
        if d["status"] == "S" and not re.fullmatch(r"\d\d", d["ch"]):
            sys.exit("sent without chapter: " + fid)
        if d["status"] == "M" and not re.search(r"merged with 12\.3[RDLAB]\d+", d["note"]):
            sys.exit("merge without target: " + fid)
        if d["status"] == "R" and not d["note"].startswith("rejected"):
            sys.exit("reject without reason: " + fid)
    for fid in NEWSTEP:
        if dec[fid]["status"] != "S":
            sys.exit("new-proof finding not sent: " + fid)
    owner = chapter_of_keys()
    spine = check_spine_sync.parse(check_spine_sync.SPINE)
    changed = list(r3_spine_apply.NEW) + list(r3_spine_apply.CAPTIONS) + ["thm:settled"]
    for key in CHILD_NOTES:
        if key not in changed:
            sys.exit("child note for unchanged key " + key)
    by_ch = {}
    for key in changed:
        ch = owner.get(key)
        if ch is None:
            sys.exit("no chapter holds " + key)
        by_ch.setdefault(ch, []).append(key)
    basis_only = {}
    for key in r3_spine_apply.ADD_FROM:
        if key not in changed:
            basis_only.setdefault(owner[key], []).append(key)

    summary_rows = []
    for ch in ["%02d" % n for n in range(2, 13)]:
        lines = ["# Round 3 fixes, chapter %d" % int(ch), "", CONTEXT, "## Spine statements changed by the reconcile", ""]
        n_spine = 0
        n_children = 0
        for key in by_ch.get(ch, []):
            text = re.sub(r"^\*\*[A-Za-z]+\.\*\* ", "", spine[key][0].replace("\n", " / "))
            if key.startswith("t:"):
                note = "The table's caption and rows now read: \"%s\" Check that each rank lemma above the table still follows from the caption." % text
                what = "caption changed"
            else:
                note = "The spine statement now reads: \"%s\" Make its children prove it, or cut children that no longer serve it." % text
                what = "statement changed"
            if key in CHILD_NOTES:
                note += " " + CHILD_NOTES[key]
                n_children += 1
            lines.append("%s | spine change, round 3 reconcile | %s | %s" % (key, what, note))
            n_spine += 1
        for key in basis_only.get(ch, []):
            lines.append("%s | spine change, round 3 reconcile | basis | Its basis now also cites %s; the statement is unchanged." % (key, ", ".join(r3_spine_apply.ADD_FROM[key])))
            n_spine += 1
        sent = [d for d in (dec[i] for i in order) if d["status"] == "S" and d["ch"] == ch]
        newstep = sum(1 for d in sent if d["id"] in NEWSTEP)
        lines += ["", "## Findings", ""]
        for d in sent:
            f = findings[d["id"]]
            lines.append("%s | %s, %s (%s) | %s | %s" % (f[2], reviewer_label(d["id"], f), finding_type(d["id"], f), d["id"], d["problem"], d["note"]))
        extra = [e for e in EXTRA if e[0] == ch]
        if extra:
            lines += ["", "## Follow-on edits from findings applied to the foundation or spine", ""]
            for _, keys, fid, problem, fix in extra:
                lines.append("%s | follow-on of %s | %s | %s" % (keys, fid, problem, fix))
        if ch in CH_SECTIONS:
            lines += ["", CH_SECTIONS[ch]]
        if not sent and not by_ch.get(ch) and not extra and not basis_only.get(ch):
            continue
        (S / ("fix-r3-ch%s.md" % ch)).write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8", newline="\n")
        total = newstep + n_children
        role = "chapter-fill-instructions" if total > 8 else "fix-instructions"
        summary_rows.append((ch, len(sent), n_spine, len(extra), newstep, n_children, total, role))

    counts = Counter(d["status"] for d in dec.values())
    types = Counter(d["type"] for d in dec.values() if d["status"] in "AS")
    by_reviewer = Counter(i[4] for i in order)
    out = ["## Step 12, verify round 3 (%s)" % DATE, ""]
    out.append("Reviewers: rules check (12.3R), reader (12.3D), logician (12.3L), skeptics A (12.3A: design room chair, convenor, author of a large proposal), skeptics B (12.3B: employer standards lead, C++ user, national body head). Scope: the 453 keys of scratch `r3-scope.txt`. %d findings: rules check %d, reader %d, logician %d, skeptics A %d, skeptics B %d. Reconciled under the force-keeping rule (plan Step 12, user 13:14): a scope or definition stated once (type 1), an added premise or fact that passes the five-part test (type 2), a narrower subject (type 3), and weaker wording only where the claim was false as stated (type 4); wording fixes that keep the claim exactly are marked wording, and a proof step added with no new premise is marked proof step. Rejection tests applied strictly: an objection a reader drops on seeing a scope or definition the proof states elsewhere, and an edge case that changes no conclusion. Dispositions: applied by the reconcile %d, sent to a chapter fix file %d, merged %d, rejected %d. Fixes by type, applied and sent: type 1 %d, type 2 %d, type 3 %d, type 4 %d, wording %d, proof step %d. The ledger's \"Step 12, round 3 reconcile\" section lists every weakening, the rejections by reason, the foundation and spine changes, and the global decisions." % (
        len(order), by_reviewer["R"], by_reviewer["D"], by_reviewer["L"], by_reviewer["A"], by_reviewer["B"],
        counts["A"], counts["S"], counts["M"], counts["R"],
        types["1"], types["2"], types["3"], types["4"], types["W"], types["P"]))
    for kind in "RDLAB":
        out += ["", "### " + SECTION[kind], ""]
        for fid in order:
            if fid[4] != kind:
                continue
            f, d = findings[fid], dec[fid]
            out.append("- %s | %s | %s | %s: %s | %s" % (fid, reviewer_label(fid, f), f[2], finding_type(fid, f), d["problem"], disposition(d)))
    (S / "r3-log-section.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

    sm = ["counts by disposition: " + ", ".join("%s %d" % (k, counts[k]) for k in "ASMR"),
          "fixes by type (applied and sent): " + ", ".join("%s %d" % (TYPE_NAME[k], types[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "applied by type: " + ", ".join("%s %d" % (TYPE_NAME[k], Counter(d["type"] for d in dec.values() if d["status"] == "A")[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "sent by type: " + ", ".join("%s %d" % (TYPE_NAME[k], Counter(d["type"] for d in dec.values() if d["status"] == "S")[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "type 4 IDs: " + ", ".join("%s (%s)" % (d["id"], findings[d["id"]][2]) for d in (dec[i] for i in order) if d["type"] == "4" and d["status"] in "AS"),
          "rejected: " + ", ".join(d["id"] for d in (dec[i] for i in order) if d["status"] == "R"),
          "merged: " + ", ".join(d["id"] for d in (dec[i] for i in order) if d["status"] == "M"),
          "by reviewer and status: " + "; ".join("%s %s" % (SECTION[k], dict(Counter(dec[i]["status"] for i in order if i[4] == k))) for k in "RDLAB"),
          "dispatch: chapter | findings sent | spine lines | follow-on lines | new-proof findings | spine children to change | total | role"]
    for row in summary_rows:
        sm.append("  ch-%s | %d | %d | %d | %d | %d | %d | %s" % row)
    (S / "r3-summary.txt").write_text("\n".join(sm) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(sm))

    if "--append-log" in sys.argv:
        log = S / "adversarial-log-draft.md"
        text = log.read_text(encoding="utf-8")
        if "## Step 12, verify round 3 (" in text:
            sys.exit("log section already present")
        log.write_text(text.rstrip("\n") + "\n\n" + "\n".join(out) + "\n", encoding="utf-8", newline="\n")
        print("appended log section")


if __name__ == "__main__":
    main()
