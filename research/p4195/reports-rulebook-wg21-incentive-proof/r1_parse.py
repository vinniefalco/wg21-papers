"""Parse the five Step 12 round 1 reviews into one numbered list of findings.

Writes r1-findings.tsv: id, reviewer, key, type or reader, problem, suggested fix.
IDs: 12.1R (rules), 12.1D (reader), 12.1L (logician), 12.1A (skeptics A), 12.1B (skeptics B).
"""
import csv
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
REVIEWS = [
    ("R", "rules", "review-r1-rules.md"),
    ("D", "reader", "review-r1-reader.md"),
    ("L", "logician", "review-r1-logician.md"),
    ("A", "skeptics A", "review-r1-skeptics-a.md"),
    ("B", "skeptics B", "review-r1-skeptics-b.md"),
]


def rows(prefix, path):
    text = path.read_text(encoding="utf-8").splitlines()
    in_findings = prefix != "R"
    section = ""
    for line in text:
        if prefix == "R":
            if line.startswith("## Findings"):
                in_findings = True
                continue
            if line.startswith("## ") and in_findings:
                in_findings = False
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if not in_findings:
            continue
        s = line.strip()
        if s.startswith("- "):
            s = s[2:]
        parts = [p.strip() for p in s.split(" | ")]
        if len(parts) < 4 or parts[0].startswith("Scope:"):
            continue
        yield section, parts[0], parts[1], parts[2], " | ".join(parts[3:])


def main():
    out = []
    for prefix, reviewer, name in REVIEWS:
        n = 0
        for section, key, typ, problem, fix in rows(prefix, S / name):
            n += 1
            out.append(("12.1%s%d" % (prefix, n), reviewer, key, typ, problem, fix, section))
        print("%s: %d" % (reviewer, n))
    with open(S / "r1-findings.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["id", "reviewer", "key", "type", "problem", "fix", "section"])
        w.writerows(out)
    if len(sys.argv) > 1:
        for r in out:
            print("%s | %s | %s | %s" % (r[0], r[2], r[3], r[4][:110]))


if __name__ == "__main__":
    main()
