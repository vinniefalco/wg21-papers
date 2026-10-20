"""Step 12 round 1: write the chapter fix files, the adversarial log section, and the counts.

Reads r1-findings.tsv (from r1_parse.py), r1-decisions-a.txt and r1-decisions-b.txt, the spine
statements now in 02-spine.md, and r1_spine_apply.py's lists of changed keys.
Writes fix-r1-chNN.md, r1-log-section.md, and r1-summary.txt. Appends the log section to
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
import r1_spine_apply  # noqa: E402

REVIEWER = {"R": "rules check", "D": "reader", "L": "logician"}
SECTION = {"R": "Rules check", "D": "Reader", "L": "Logician", "A": "Skeptics A", "B": "Skeptics B"}
TYPE_NAME = {"1": "type 1", "2": "type 2", "3": "type 3", "4": "type 4", "W": "wording", "P": "proof step"}

# Findings whose fix needs new proof steps (an invalid step or a missing step), by ID.
NEWSTEP = {
    "12.1L7", "12.1L10", "12.1L17", "12.1R10",
    "12.1L40", "12.1L44", "12.1L45", "12.1L47", "12.1L48", "12.1A39",
    "12.1R20", "12.1L51", "12.1L53", "12.1L55", "12.1L56", "12.1B43", "12.1B44",
}
# Changed spine statements whose chapter children must change.
CHILDREN_CHANGE = {
    "l:mutual-refrain",
    "p:dissent-needs-paper", "p:reasons-unrecorded", "p:fluency",
    "p:early-polls", "p:challenger-bar", "p:light-review",
    "ind:adopted-parts", "p:parts", "p:first-part",
    "p:chair-default", "l:call-above", "l:call-below", "p:plenary-ratifies",
    "p:merit-gap", "p:written-answer",
    "p:cutoff-effect", "p:prefer-is", "p:nb-comment", "l:rank-rest-yes", "l:rank-rest-abstain",
    "l:settled-regular", "l:settled-design-bound", "l:settled-result-seeking", "l:settled-small-author",
    "l:settled-sg-chair", "l:settled-design-chair", "l:settled-convenor", "l:settled-nb",
    "l:settled-sponsor", "l:settled-user", "thm:settled",
    "c:pred-sponsor-against", "c:pred-abstention-length", "c:pred-parts", "c:pred-first-part",
    "c:pred-rival-polls", "c:pred-removals", "c:pred-small-fade", "c:pred-nb-positions",
    "c:pred-written-answers", "c:pred-defects", "c:pred-competing",
    "c:lever-reasons-all", "c:lever-sponsor-limit", "c:lever-nb-more", "c:lever-nb-less",
}

EXTRA = [
    ("05", "l:skip-study", "12.1A7", "p:light-review now rests on reading a paper and following its discussion, not on close study", "Write \"A participant whose stake in a proposal is worth less than the time reading its paper and following its discussion takes does better doing neither.\" Cite f:not-vote and ax:review-cost."),
    ("05", "l:removal-polls, l:late-removal", "12.1L12", "\"normally\" is now covered by d:follows-norm", "Drop \"normally\" and cite d:follows-norm."),
    ("06", "inf:part-voter-share", "12.1L11", "the voter's share of the reversal's cost", "Cite ax:rework and ax:hours: every voter bears a share through the meeting time that redoing work takes from other papers."),
    ("06", "l:part-cost", "12.1L16", "p:parts's costs now include a set of polls for each part", "Write \"Each part needs its own paper, which takes time to write, its own presenter at each meeting where it is considered, and its own polls in the design and wording rooms and at plenary.\" Cite f:design-forward, f:wording-forward, and f:plenary-owns."),
    ("08", "inf:call-above-post, inf:call-below-post", "12.1L26", "the post risk now rests on ax:post-risk", "Cite ax:post-risk in both steps."),
    ("09", "l:nb-position-time", "12.1L31", "p:users-out's \"only where that is worth their members' time\"", "Cite ax:prefer, which now lists a national body's members' time among its values."),
    ("09", "l:paper-answers, l:iso-comment-answers", "12.1R12", "p:written-answer's third exception and the ISO absence", "Add a child proving from f:ts-disposition that SD-4 requires a Disposition of Comments paper answering a TS ballot's formal review comments, and cite f:iso-no-answer where the proof says ISO requires no other written answer."),
    ("10", "l:cutoff", "12.1L36", "the schedule clause of p:miss-cost", "Cite ax:schedule, which now says each planned edition holds the features approved by its cutoff."),
    ("10", "inf:no-gains-nothing, inf:comments-either-way", "12.1A25", "the ballot table's narrowed case", "Restate both for the case the table now defines: the body expects its comments to fare the same under any vote, as SD-4 says (f:no-means-no), and cannot rule out that its vote decides the result. Write \"removing any one feature through a failed ballot and a revised draft\" for \"blocking any one feature\"."),
    ("10", "l:ts-result-seeking, l:ts-design-bound", "12.1A37", "p:prefer-is's new TS clause", "Add a child proving from f:ts-unblock that a TS reaches implementers and users early and can publish while concerns remain, if their holders agree."),
    ("11", "inf:sg-call-norm", "12.1L3", "m:moves-chair now says study group chairs can poll which design to send on", "Write \"A study group chair can poll which design leaves the group as its initial proposal\"."),
    ("11", "inf:nb-late-plenary", "12.1L30", "SD-4's instruction, not what happens", "Write \"SD-4 says an objection first raised at plenary without escalation should get no weight there.\""),
    ("11", "inf:thm-sizes", "12.1L21", "p:size-attributes now covers chapter 6 only", "Prove the Theorem's size sentence from p:size-attributes and from l:settled-small-author, which rests on d:small's attribute that the author pays their own costs."),
    ("11", "inf:thm-paid-votes, inf:thm-no-cap, l:sponsor-paid-votes", "12.1L14", "a sponsor no longer \"adds a voter\"", "Write \"Each participant a sponsor pays to attend has a vote and values its interests\", and \"no rule limits how many it pays\" (d:rules)."),
    ("11", "inf:thm-reward-timing", "12.1L32", "the adoption value", "Write \"Authors get the adoption they value at the poll, while a flaw that implementation and use have not yet exposed costs users only later.\""),
    ("11", "inf:thm-light-review, l:thm-holding", "12.1A7", "reading, and sponsors who keep paying", "Write \"costs more to read\" for \"costs more to study\", and \"whose sponsors keep paying its costs\" (12.1B9)."),
    ("11", "inf:doubt-neutral", "12.1R5", "\"draws no request for reasons\"", "Write \"is a vote SD-4 asks no one to be ready to explain\"."),
    ("11", "inf:thm-late-arrival", "12.1L13", "removal routes", "Write \"a paper or ballot comment meeting the 2:1 norm\"."),
    ("11", "l:thm-checks-sizes, inf:thm-checks", "12.1L46", "\"checks on each of these effects\" is not shown", "Write \"The rules also provide checks: a third of the Favor-plus-Against votes can block, every view must be heard, rivals with papers can be polled together, implementation experience informs votes, and national bodies ballot each draft.\", matching the Theorem, with no claim that each effect has a check."),
    ("11", "l:dchair-call", "12.1A9", "a re-poll fits the norm", "Write \"With Neutral votes short of a majority, that is consensus above the line and declining at or below it, after any re-poll.\" Cite d:follows-norm."),
    ("11", "l:settled-convenor's children", "12.1A19", "the procedure leaves other calls to the convenor", "Add a child proving that for opposition escalated in time SD-4 says only that plenary decides whether there is consensus \"as determined by the Convener\", after the convenor usually asks about national positions (f:plenary-owns, f:plenary-nb)."),
    ("11", "l:small-wait-cost, inf:small-each-meeting, l:small-keep-stop", "12.1L42", "costs already paid are sunk", "Compare the chance of adoption with the cost of the meetings still ahead: the longer it must still wait behind priority work, the more those costs come to."),
    ("11", "l:bound-early, l:seeking-early, inf:early-improvement-cost, inf:thm-early-cost", "12.1L10", "a later change is not a reversal", "Write that a rival or a later change must redo or discard work built on the incumbent at a growing cost (p:early-polls, ax:rework), not that every change bears a reversal cost."),
    ("11", "l:nb-no", "12.1A25", "the narrowed ballot case", "State l:nb-no for a national body whose comments fare the same under any vote, as l:settled-nb now does."),
    ("12", "inf:sf-predict", "12.1A36", "p:large-position lost its plenary-progress sentence", "Rest the step on who pays the authors' costs (d:large, d:small), not on nearness to the work chairs take up first."),
    ("12", "inf:sa-share, inf:sl-cap, inf:sl-margins", "12.1L14", "a sponsor no longer \"adds a voter\"", "Write that each participant a sponsor pays has a vote and values its interests."),
    ("12", "inf:pa-design-bound, inf:fp-small", "12.1L39", "the first-part condition", "Write \"the smallest part that fixes the features it needs and can pass\"."),
]

CONTEXT = """Context from the round 1 reconcile, which changed the foundation and the spine before this file was written:

- New and changed foundation items. `d:rules` (new) says what "the rules" covers and that absence claims cover SD-4 whole and the quoted ISO clauses. `d:follows-norm` (new) defines following the 2:1 norm (consensus on a count above 2:1 after discussion and any re-poll, and on no other count, with Neutral votes short of a majority) and states once that what advances in a subgroup, and what Against votes block there, is what happens under a chair who follows the norm: drop per-sentence qualifiers such as "normally" or "when the chair follows the norm" and cite `d:follows-norm` instead. `ax:post-risk` (new): a chair cannot rule out that a call not following the 2:1 norm, or polling that departs from what SD-4 encourages, puts their post at more risk, and the convenor likewise for SD-4's plenary procedure. `ax:rework` now says reversing a decision, or changing a design after work is built on it, means redoing or discarding that work, which costs its builders and takes meeting time from other papers. `ax:support` now says a Favor vote gives the colleague no reason to support the voter less readily. `ax:schedule` now says each planned edition holds the features approved by its cutoff. `ax:prefer` now lists a national body's members' time among its values. `d:does-better` now defines "does best" as no other option worth more, so write "does best" for "does no better than". `d:incumbent` now defines a rival as a design on the same topic that is not an incumbent. `f:no-merit-ruling` now covers ruling only, so write "rule on", never "judge", for what SD-4 assigns no one. New facts: `f:example-based`, `f:ts-disposition`, `f:ts-unblock`, `f:comment-vetting`, `f:late-documents`, `f:incits-control`, `f:incits-delegates`, `f:iso-no-answer`.
- Words. Write "another explanation" or "the other explanation", never "innocent explanation", and "a flaw found only in implementation and use", never "hidden flaw".
- Spine lines below quote statements already changed in this chapter and in `02-spine.md`. Do not edit those statements; make their children prove them, or cut children that no longer serve them. Keep every sentence at most 30 words where the claim allows, in the positive form, and never soften a plain, sharp, true statement.
"""


def load_findings():
    rows = list(csv.reader(open(S / "r1-findings.tsv", encoding="utf-8"), delimiter="\t"))[1:]
    return {r[0]: r for r in rows}, [r[0] for r in rows]


def load_decisions():
    dec = {}
    for name in ("r1-decisions-a.txt", "r1-decisions-b.txt"):
        for line in (S / name).read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                p = line.split("|")
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
    kind = fid[4]
    return finding[3] if kind in "RDL" else "objection"


def disposition(d):
    if d["status"] == "A":
        return "applied, %s: %s" % (TYPE_NAME[d["type"]], d["note"])
    if d["status"] == "S":
        return "sent to fix-r1-ch%s.md, %s" % (d["ch"], TYPE_NAME[d["type"]])
    if d["status"] == "M":
        return d["note"]
    return d["note"]


def main():
    findings, order = load_findings()
    dec = load_decisions()
    owner = chapter_of_keys()
    spine = check_spine_sync.parse(check_spine_sync.SPINE)
    changed = list(r1_spine_apply.NEW) + list(r1_spine_apply.CAPTIONS) + ["thm:settled", "l:incits-positions"]
    by_ch = {}
    for key in changed:
        ch = owner.get(key)
        if ch is None:
            sys.exit("no chapter holds " + key)
        by_ch.setdefault(ch, []).append(key)

    # fix files
    summary_rows = []
    for ch in ["%02d" % n for n in range(2, 13)]:
        lines = ["# Round 1 fixes, chapter %d" % int(ch), "", CONTEXT, "## Spine statements changed by the reconcile", ""]
        n_spine = 0
        newstep = 0
        for key in by_ch.get(ch, []):
            text = re.sub(r"^\*\*[A-Za-z]+\.\*\* ", "", spine[key][0].replace("\n", " / "))
            if key == "l:incits-positions":
                note = "New spine child of p:nb-members, already in this chapter. It rests on its citations; write no children for it."
            elif key.startswith("t:"):
                note = "The table's caption and rows now read: \"%s\" Check that each rank lemma above the table still follows from the caption." % text
            else:
                note = "The spine statement now reads: \"%s\" Make its children prove it, or cut children that no longer serve it." % text
            what = "new spine child" if key == "l:incits-positions" else ("caption changed" if key.startswith("t:") else "statement changed")
            lines.append("%s | spine change, round 1 reconcile | %s | %s" % (key, what, note))
            n_spine += 1
            if key in CHILDREN_CHANGE:
                newstep += 1
        if ch == "03":
            lines.append("l:vote-below, l:vote-above, t:vote-choice | spine change, round 1 reconcile | cut as true by definition (12.1D19 to 12.1D23) | Already cut from this chapter with their steps, and their citers now cite p:doubt-outside-count. Check that l:objectors-none, l:objectors-block, and inf:refrain-rank still follow from p:doubt-outside-count's first sentence.")
            n_spine += 1
        if ch == "07":
            lines.append("p:sg-sponsor | spine change, round 1 reconcile | basis | Its basis now cites d:follows-norm, which defines what Against votes block; the statement is unchanged.")
            n_spine += 1
        if ch == "11":
            lines.append("l:checks-deadlock | spine change, round 1 reconcile | basis | Its basis now cites ax:schedule for the schedule clause (12.1L36); cite it in inf:deadlock-schedule.")
            n_spine += 1
        sent = [d for d in (dec[i] for i in order) if d["status"] == "S" and d["ch"] == ch]
        lines += ["", "## Findings", ""]
        for d in sent:
            f = findings[d["id"]]
            lines.append("%s | %s, %s (%s) | %s | %s" % (f[2], reviewer_label(d["id"], f), finding_type(d["id"], f), d["id"], d["problem"], d["note"]))
            if d["id"] in NEWSTEP:
                newstep += 1
        extra = [e for e in EXTRA if e[0] == ch]
        if extra:
            lines += ["", "## Follow-on edits from findings applied to the foundation or spine", ""]
            for _, keys, fid, problem, fix in extra:
                lines.append("%s | follow-on of %s | %s | %s" % (keys, fid, problem, fix))
        if not sent and not by_ch.get(ch):
            continue
        (S / ("fix-r1-ch%s.md" % ch)).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        role = "chapter-fill-instructions" if newstep > 8 else "fix-instructions"
        summary_rows.append((ch, len(sent), n_spine, newstep, role))

    # log section
    counts = Counter(d["status"] for d in dec.values())
    types = Counter(d["type"] for d in dec.values() if d["status"] in "AS")
    by_reviewer = Counter(i[4] for i in order)
    out = ["## Step 12, verify round 1 (2026-10-19)", ""]
    out.append("Reviewers: rules check (12.1R), reader (12.1D), logician (12.1L), skeptics A (12.1A: design room chair, convenor, author of a large proposal), skeptics B (12.1B: employer standards lead, C++ user, national body head). %d findings: rules check %d, reader %d, logician %d, skeptics A %d, skeptics B %d. Reconciled under the force-keeping rule (plan Step 12, user 13:14): a scope or definition stated once (type 1), an added premise or fact that passes the five-part test (type 2), a narrower subject (type 3), and weaker wording only where the claim was false as stated (type 4); wording fixes that keep the claim exactly are marked wording, and a proof step added with no new premise is marked proof step. Dispositions: applied by the reconcile %d, sent to a chapter fix file %d, merged %d, rejected %d. Fixes by type, applied and sent: type 1 %d, type 2 %d, type 3 %d, type 4 %d, wording %d, proof step %d. The ledger's \"Step 12, round 1 reconcile\" section lists every weakening, the foundation and spine changes, and the global decisions." % (
        len(order), by_reviewer["R"], by_reviewer["D"], by_reviewer["L"], by_reviewer["A"], by_reviewer["B"],
        counts["A"], counts["S"], counts["M"], counts["R"],
        types["1"], types["2"], types["3"], types["4"], types["W"], types["P"]))
    for kind in "RDLAB":
        out += ["", "### " + SECTION[kind], ""]
        for fid in order:
            if fid[4] != kind:
                continue
            f, d = findings[fid], dec[fid]
            label = reviewer_label(fid, f)
            ftype = finding_type(fid, f)
            out.append("- %s | %s | %s | %s: %s | %s" % (fid, label, f[2], ftype, d["problem"], disposition(d)))
    (S / "r1-log-section.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

    # summary
    sm = ["counts by disposition: " + ", ".join("%s %d" % (k, counts[k]) for k in "ASMR"),
          "fixes by type (applied and sent): " + ", ".join("%s %d" % (TYPE_NAME[k], types[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "applied by type: " + ", ".join("%s %d" % (TYPE_NAME[k], Counter(d["type"] for d in dec.values() if d["status"] == "A")[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "sent by type: " + ", ".join("%s %d" % (TYPE_NAME[k], Counter(d["type"] for d in dec.values() if d["status"] == "S")[k]) for k in ["1", "2", "3", "4", "W", "P"]),
          "type 4 IDs: " + ", ".join("%s (%s)" % (d["id"], findings[d["id"]][2]) for d in (dec[i] for i in order) if d["type"] == "4" and d["status"] in "AS"),
          "dispatch: chapter | findings sent | spine lines | needing new proof steps | role"]
    for row in summary_rows:
        sm.append("  ch-%s | %d | %d | %d | %s" % row)
    (S / "r1-summary.txt").write_text("\n".join(sm) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(sm))

    if "--append-log" in sys.argv:
        log = S / "adversarial-log-draft.md"
        text = log.read_text(encoding="utf-8")
        if "## Step 12, verify round 1 (2026-10-19)" in text:
            sys.exit("log section already present")
        log.write_text(text.rstrip("\n") + "\n\n" + "\n".join(out) + "\n", encoding="utf-8", newline="\n")
        print("appended log section")


if __name__ == "__main__":
    main()
