"""Step 12 round 2: write the chapter fix files, the adversarial log section, and the counts.

Reads r2-findings.tsv (from r2_parse.py), r2-decisions-a.txt and r2-decisions-b.txt, the spine
statements now in 02-spine.md, and r2_spine_apply.py's lists of changed keys.
Writes fix-r2-chNN.md, r2-log-section.md, and r2-summary.txt. Appends the log section to
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
import r2_spine_apply  # noqa: E402

REVIEWER = {"R": "rules check", "D": "reader", "L": "logician"}
SECTION = {"R": "Rules check", "D": "Reader", "L": "Logician", "A": "Skeptics A", "B": "Skeptics B"}
TYPE_NAME = {"1": "type 1", "2": "type 2", "3": "type 3", "4": "type 4", "W": "wording", "P": "proof step"}

# Findings sent to fix files whose fix needs new proof content: a new lemma or step, a rebuilt
# step, or a redesigned test. Citation-only and wording fixes are not counted.
NEWSTEP = {
    "12.2B2", "12.2A24", "12.2B12",
    "12.2L7", "12.2L10", "12.2L12", "12.2L14", "12.2L15", "12.2A1", "12.2A2", "12.2A8", "12.2A10",
    "12.2A16", "12.2B4", "12.2B15", "12.2B22", "12.2B26",
    "12.2L19", "12.2L22", "12.2L24", "12.2L25", "12.2L26", "12.2A5", "12.2A7", "12.2A11", "12.2A12",
    "12.2A13", "12.2A14", "12.2A17", "12.2A22", "12.2B1", "12.2B3", "12.2B5", "12.2B7", "12.2B8",
    "12.2B9", "12.2B10", "12.2B16", "12.2B19", "12.2B20", "12.2B27",
}

# Changed spine statements whose chapter children must change, with what the fix should do.
CHILD_NOTES = {
    "p:reasons-unrecorded": "Add a child step proving the new clause from f:report-followup: SD-4 asks whoever reports a concern to file the issue or write the paper and to make sure the feature's designers know. Keep l:argument-writing's list of writings.",
    "p:first-part": "Align l:first-part-smallest with \"can pass\": of two first parts that fix the same features and can pass, the smaller is ready and reviewed sooner. 12.2B2 narrows l:first-part-oppose, and 12.2A24 and 12.2B12 add the checks to l:first-part-foresight.",
    "l:call-above": "In inf:call-above-norm and inf:call-below-norm, use the caption's added case, that the chair finds no sustained opposition (d:follows-norm), so following the norm declares consensus above 2:1 and declining departs from it.",
    "p:integration": "Add the in-situ case (f:in-situ) to l:separate-approval or l:editor-merge: when the wording rooms reviewed a whole new draft with the changes applied, plenary approves the changes in that form and no editing committee is needed. Neither case is a step that checks whether designs work together, so l:conflict-costs and the absence stand.",
    "l:rank-oppose-no": "Make inf:oppose-no-rank use the case the table defines: the body cannot rule out that its vote decides the result, so only the No counting against approval ranks No first. l:rank-oppose-abstain's \"such a body\" inherits the case.",
    "l:settled-design-bound": "Keep l:bound-no-losing-poll, which now carries \"seeking no poll it expects to lose to a rival\" under the split rule, and add l:bound-vehicle (12.2A16).",
    "l:settled-result-seeking": "The early-poll condition moved to l:seeking-early: make its conclusion \"It does best seeking an early poll or first part only where sooner adoption outweighs the cost it adds to later improvements.\" and keep its steps.",
    "l:settled-design-chair": "Add the side-by-side child lemma (12.2A2).",
    "l:settled-nb": "Make l:nb-no and inf:nb-fail use the table's case (12.2B26, 12.2D70).",
    "l:settled-sponsor": "Rewrite l:sponsor-how-many (12.2B4).",
    "l:settled-user": "Rewrite inf:user-stake for the stakes in every poll taking part lets the user vote in, and move \"any better design's gain goes to all users\" into it (12.2B15, 12.2D72); l:user-take-part follows.",
    "l:checks-record": "Prove the two sentences with child steps, one sentence each, and keep the checks the old statement named as further child steps, one sentence each: SD-4 asks those with a concern to tell chairs and authors early (f:report-early); ISO says consensus requires resolving substantial objections and ends the committee stage when all technical issues are resolved (f:resolve-substantial, f:committee-stage); SD-4 works in addition to the Directives (f:sd4-scope); and ISO recommends that experts keep their national body informed at the earliest possible stage (f:expert-contact, moved here from the cut l:checks-attendance).",
    "thm:settled": "Make the Theorem's children prove the new wording: l:thm-pattern takes the open-choices sentence (12.2L12); l:thm-readily says \"the next edition\" (12.2D86); l:thm-costs-gains takes the new flaw sentence (12.2B11) and ax:rework (12.2L14); l:thm-gaps and l:thm-checks-sizes split as 12.2D91 and 12.2D93 give; the design-bound, chair, national body, and user sentences rest on the changed settled lemmas, so check that inf:thm-authors-regulars and inf:thm-others still follow.",
    "c:pred-sponsor-against": "Move the evidence (poll results and stated affiliations) into inf:sa-evidence and the comparison's details into inf:sa-tell-apart (12.2A17).",
    "c:pred-abstention-length": "Rebuild the steps for revisions of one proposal (12.2B16, 12.2L19, 12.2D99); inf:al-evidence carries the evidence, quotable poll results and paper lengths.",
    "c:pred-parts": "Rebuild inf:pa-ease and inf:pa-tell-apart for the new test (12.2B7); inf:pa-evidence carries the mailings as evidence.",
    "c:pred-first-part": "Narrow inf:fp-small and inf:fp-seldom to design-bound authors (12.2L22, 12.2D102), and rebuild inf:fp-small-steps and inf:fp-tell-apart for the mention test (12.2B8, 12.2L23).",
    "c:pred-removals": "inf:rm-evidence carries the evidence; rebuild inf:rm-tell-apart for the margins test (12.2L24), and reframe inf:rm-rare and inf:rm-nb as predictions (12.2D105, 12.2D106).",
    "c:pred-small-fade": "Rebuild inf:sf-small, inf:sf-predict, inf:sf-reflection, and inf:sf-tell-apart for the new comparison and test (12.2B9, 12.2B10, 12.2D108); inf:sf-evidence carries the mailings and poll results.",
    "c:pred-nb-positions": "Narrow inf:nb-evidence to vetted ballot comments (12.2A14) and rebuild inf:nb-tell-apart for the cost comparison (12.2B27).",
    "c:pred-written-answers": "inf:wa-evidence carries the evidence, the papers and poll results; rebuild inf:wa-tell-apart (12.2A7) and inf:wa-predict (12.2R16).",
    "c:pred-defects": "inf:de-evidence carries the evidence; add turnout to inf:de-predict and inf:de-tell-apart (12.2B19), and name the other explanation as the statement does (12.2L25).",
    "c:pred-competing": "inf:co-evidence carries the evidence; rebuild inf:co-tell-apart on implementation experience (12.2A22).",
    "c:lever-anonymous": "Rewrite inf:an-standing (12.2B5) and inf:an-reasons (12.2A5); inf:an-more follows.",
    "c:lever-reasons-all": "Update inf:ra-cost and inf:ra-shift for Favor's reasons cost (12.2B20).",
    "c:lever-sponsor-limit": "Rewrite inf:sl-cap, inf:sl-margins, and inf:sl-predict for the new comparison (12.2D117, 12.2B3).",
    "c:lever-nb-more": "Narrow inf:nm-changes (12.2L26), add ISO's caution to inf:nm-more (12.2A13), and cut or reword inf:nm-weight (12.2A12).",
    "c:lever-nb-less": "inf:nl-ballot carries the comments-and-appeals clause; narrow inf:nl-count (12.2A11) and cite inf:nb-few in inf:nl-fewer (12.2L27).",
}

EXTRA = [
    ("03", "chapter 3 recap", "12.2D11, 12.2D14", "\"the line\" is a figure of speech", "In the recap write \"is one or two votes above the 2:1 threshold\" for \"sits one or two votes above the line\"."),
    ("04", "chapter 4 recap", "12.2D22", "\"outlasts its hearers\"", "In the recap write \"only writing keeps an objection's argument after its hearers leave\"."),
    ("06", "chapter 6 recap", "12.2D32, 12.2B2", "the first-part condition", "In the recap write \"the smallest part that fixes the design's structure and can pass\" for \"... and still meets the 2:1 norm against opponents who foresee the rest\"."),
    ("08", "chapter 8 recap", "12.2D40", "\"which promises fewer problems\"", "In the recap write \"whose record makes them expect fewer problems\"."),
    ("09", "l:traced-voters", "12.2A9", "plenary voters", "Cite f:plenary-polls: in plenary polls each person present whose name is listed in ISO's global directory can vote, so plenary voters, like subgroup voters, are registered experts (f:registered)."),
    ("11", "inf:sg-call-norm", "12.2R3", "m:moves-chair's new wording", "m:moves-chair now says any chair can choose the polls and each chair can call consensus on its room's polls; cite f:chair-polls and f:sg-initial-proposal for a study group chair's poll on which design leaves the group."),
    ("11", "l:checks-attendance", "global decision 4b", "cut from the spine and this chapter", "Already cut, with its entry in p:checks' proved-by list. Its checks are stated elsewhere: the SC22 cap in p:sponsor-votes and inf:thm-no-cap, national interests in m:moves-user and p:users-out, agenda notice in m:moves-nb, direction group opinions now in l:checks-hearing, and experts informing their national body now in l:checks-record."),
    ("12", "chapter 12 recap", "12.2B9, 12.2D116", "the small-proposal prediction and \"in a room\"", "In the recap, state the stop prediction as the comparison of self-funded and sponsored authors' proposals per meeting spent waiting, and write \"in a subgroup\" for \"in a room\"."),
]

CONTEXT = """Context from the round 2 reconcile, which changed the foundation and the spine before this file was written:

- Absence facts. `f:no-drawbacks-asked` and `f:no-interest-statement` now cover SD-4 and every quoted ISO clause, so "the rules ask no ..." is supported for drawbacks, who pays, and interests. Write "no proposal paper" where the claim is about drawbacks, since SD-4 asks a TS or white paper for its must-address controversial issues.
- Scope. `d:follows-norm` now says what advances in a subgroup, and what Against votes block there, is what happens under a chair who follows the norm and finds no sustained opposition. Do not add that condition to sentences; cite `d:follows-norm`.
- `ax:support` now says a vote the colleague cannot attribute gives no reason for less ready support.
- New facts: `f:plenary-polls` (plenary voters and the convenor's polls), `f:report-followup` (file the issue or write the paper), `f:meeting-access` (ISO 5.3.1 on invitation letters, accessibility, and locations), `f:in-situ` (drafts the wording rooms reviewed with the changes applied). Extended facts: `f:minutes` (minute-taking), `f:negative-welcome` (broad understanding), `f:iso-early` (substantial comments tabled at meetings), `f:presenter` (qualified to answer detailed questions).
- The Theorem now names polling rivals side by side for design room chairs, and ends its first paragraph with a sentence on the choices it leaves open, which each player makes in the way that does best for them given the others' choices. `l:checks-attendance` is cut from the spine and chapter 11.
- Words. Write "the next edition", not "the next IS"; "subgroup", not "room", where a subgroup is meant; "the 2:1 threshold" or "meeting the 2:1 norm", not "the line"; and in chapter 12, "the model predicts" for every prediction a step states.
- Length. Each item has at most two sentences of at most 30 words. Where a statement needs more, keep its claim in the item and make each other sentence a child step with its own key, one sentence each.
- Citations. A child may cite only foundation items, spine items of earlier chapters, earlier items of its own chapter, or its own children.
- Spine lines below quote statements already changed in this chapter and in `02-spine.md`. Do not edit those statements; make their children prove them, or cut children that no longer serve them. Never soften a plain, sharp, true statement.
"""


def load_findings():
    rows = list(csv.reader(open(S / "r2-findings.tsv", encoding="utf-8"), delimiter="\t"))[1:]
    return {r[0]: r for r in rows}, [r[0] for r in rows]


def load_decisions():
    dec = {}
    for name in ("r2-decisions-a.txt", "r2-decisions-b.txt"):
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
        return "sent to fix-r2-ch%s.md, %s" % (d["ch"], TYPE_NAME[d["type"]])
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
        if d["status"] == "M" and not re.search(r"merged with 12\.2[RDLAB]\d+", d["note"]):
            sys.exit("merge without target: " + fid)
        if d["status"] == "R" and not d["note"].startswith("rejected"):
            sys.exit("reject without reason: " + fid)
    owner = chapter_of_keys()
    spine = check_spine_sync.parse(check_spine_sync.SPINE)
    changed = list(r2_spine_apply.NEW) + list(r2_spine_apply.CAPTIONS) + ["thm:settled"]
    by_ch = {}
    for key in changed:
        ch = owner.get(key)
        if ch is None:
            sys.exit("no chapter holds " + key)
        by_ch.setdefault(ch, []).append(key)
    basis_only = {}
    for key in r2_spine_apply.ADD_FROM:
        if key not in changed:
            basis_only.setdefault(owner[key], []).append(key)

    summary_rows = []
    for ch in ["%02d" % n for n in range(2, 13)]:
        lines = ["# Round 2 fixes, chapter %d" % int(ch), "", CONTEXT, "## Spine statements changed by the reconcile", ""]
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
            lines.append("%s | spine change, round 2 reconcile | %s | %s" % (key, what, note))
            n_spine += 1
        for key in basis_only.get(ch, []):
            lines.append("%s | spine change, round 2 reconcile | basis | Its basis now also cites %s; the statement is unchanged." % (key, ", ".join(r2_spine_apply.ADD_FROM[key])))
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
        if not sent and not by_ch.get(ch) and not extra:
            continue
        (S / ("fix-r2-ch%s.md" % ch)).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        total = newstep + n_children
        role = "chapter-fill-instructions" if total > 8 else "fix-instructions"
        summary_rows.append((ch, len(sent), n_spine, len(extra), newstep, n_children, total, role))

    counts = Counter(d["status"] for d in dec.values())
    types = Counter(d["type"] for d in dec.values() if d["status"] in "AS")
    by_reviewer = Counter(i[4] for i in order)
    out = ["## Step 12, verify round 2 (2026-10-19)", ""]
    out.append("Reviewers: rules check (12.2R), reader (12.2D), logician (12.2L), skeptics A (12.2A: design room chair, convenor, author of a large proposal), skeptics B (12.2B: employer standards lead, C++ user, national body head). Scope: the 466 keys of scratch `r2-scope.txt`. %d findings: rules check %d, reader %d, logician %d, skeptics A %d, skeptics B %d. Reconciled under the force-keeping rule (plan Step 12, user 13:14): a scope or definition stated once (type 1), an added premise or fact that passes the five-part test (type 2), a narrower subject (type 3), and weaker wording only where the claim was false as stated (type 4); wording fixes that keep the claim exactly are marked wording, and a proof step added with no new premise is marked proof step. Dispositions: applied by the reconcile %d, sent to a chapter fix file %d, merged %d, rejected %d. Fixes by type, applied and sent: type 1 %d, type 2 %d, type 3 %d, type 4 %d, wording %d, proof step %d. The ledger's \"Step 12, round 2 reconcile\" section lists every weakening, the foundation and spine changes, and the global decisions." % (
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
    (S / "r2-log-section.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

    sm = ["counts by disposition: " + ", ".join("%s %d" % (k, counts[k]) for k in "ASMR"),
          "fixes by type (applied and sent): " + ", ".join("%s %d" % (TYPE_NAME[k], types[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "applied by type: " + ", ".join("%s %d" % (TYPE_NAME[k], Counter(d["type"] for d in dec.values() if d["status"] == "A")[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "sent by type: " + ", ".join("%s %d" % (TYPE_NAME[k], Counter(d["type"] for d in dec.values() if d["status"] == "S")[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "type 4 IDs: " + ", ".join("%s (%s)" % (d["id"], findings[d["id"]][2]) for d in (dec[i] for i in order) if d["type"] == "4" and d["status"] in "AS"),
          "rejected: " + ", ".join(d["id"] for d in (dec[i] for i in order) if d["status"] == "R"),
          "dispatch: chapter | findings sent | spine lines | follow-on lines | new-proof findings | spine children to change | total | role"]
    for row in summary_rows:
        sm.append("  ch-%s | %d | %d | %d | %d | %d | %d | %s" % row)
    (S / "r2-summary.txt").write_text("\n".join(sm) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(sm))

    if "--append-log" in sys.argv:
        log = S / "adversarial-log-draft.md"
        text = log.read_text(encoding="utf-8")
        if "## Step 12, verify round 2 (2026-10-19)" in text:
            sys.exit("log section already present")
        log.write_text(text.rstrip("\n") + "\n\n" + "\n".join(out) + "\n", encoding="utf-8", newline="\n")
        print("appended log section")


if __name__ == "__main__":
    main()
