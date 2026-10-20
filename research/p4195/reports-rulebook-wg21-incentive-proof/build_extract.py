"""Build rules-extract.md from the fetched SD-4 text and the ISO Directives, copying source lines verbatim.

Usage: build_extract.py [--dry-run]
"""
import re
import sys
from pathlib import Path

SD4 = Path(r"C:\Users\Vinnie\.cursor\projects\c-Users-Vinnie-cursor\agent-tools\0fa9968a-f19a-4720-9cf1-495bb866ae5a.txt")
ISO = Path(r"c:\Users\Vinnie\cursor\cabinet\_inbox\ISODirectives2026-part1.md")
OUT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\rules-extract.md")
SD4_HEADING = "## SD-4: WG21 Practices and Procedures"
FRONTMATTER = (
    "---\n"
    "produced: 2026-10-18\n"
    "title: SD-4 and ISO/IEC Directives Part 1 (2026) rule text for the WG21 incentive proof\n"
    "---"
)
CLAUSES = [
    "0.7", "1.7", "1.8.2", "1.12.1", "1.12.2", "1.12.3", "2.1.6", "2.1.7",
    "2.5.6", "2.5.7", "2.5.8", "2.5.9", "2.5.10",
    "2.6.2", "2.6.3", "2.6.4", "2.6.5",
    "2.7.2", "2.7.3", "2.7.4", "2.7.5", "2.7.6", "2.7.7",
    "3.1", "5.3.1", "5.4", "5.5", "5.6", "5.7",
    "6.1", "6.2", "6.3", "6.4", "6.5",
]
# A clause starts at a line opening with its bold dotted number: heading, paragraph, or list item.
START = re.compile(r"^(?:#{1,6} +|- +)?\*\*(?:<mark>)?(\d+(?:\.\d+)+)(?:</mark>)?(?=\*\*|\s)")
HEADING = re.compile(r"^(#{1,6}) ")


def parts(number):
    return len(number.split("."))


def clause_ranges(lines):
    starts = {}
    for i, line in enumerate(lines):
        m = START.match(line)
        if m:
            starts.setdefault(m.group(1), []).append(i)
    ranges = {}
    problems = []
    for clause in CLAUSES:
        found = starts.get(clause, [])
        if len(found) != 1:
            problems.append(f"{clause}: {len(found)} start lines {[n + 1 for n in found]}")
            continue
        s = found[0]
        k = parts(clause)
        end, reason = len(lines), "end of file"
        for j in range(s + 1, len(lines)):
            m = START.match(lines[j])
            if m and parts(m.group(1)) <= k:
                end, reason = j, f"clause {m.group(1)}"
                break
            h = HEADING.match(lines[j])
            if h and not m and len(h.group(1)) <= 2:
                end, reason = j, f"top-level heading {lines[j].strip()[:40]!r}"
                break
        ranges[clause] = (s, end, reason)
    return ranges, problems


def main():
    dry = "--dry-run" in sys.argv
    sd4_lines = SD4.read_text(encoding="utf-8").splitlines()
    iso_lines = ISO.read_text(encoding="utf-8").splitlines()

    sd4_start = [i for i, line in enumerate(sd4_lines) if line.strip() == SD4_HEADING]
    if len(sd4_start) != 1:
        sys.exit(f"FAIL: SD-4 heading found {len(sd4_start)} times")
    sd4_body = sd4_lines[sd4_start[0]:]

    ranges, problems = clause_ranges(iso_lines)
    for clause in CLAUSES:
        if clause not in ranges:
            continue
        s, e, reason = ranges[clause]
        body = iso_lines[s:e]
        inner = [f"{s + 1 + n}:{line.strip()[:50]}" for n, line in enumerate(body[1:], 1)
                 if HEADING.match(line) or line.strip().startswith("**") and START.match(line)]
        marks = sum(line.count("<mark>") for line in body)
        print(f"{clause:7} lines {s + 1}-{e} ({e - s} lines), ends at {reason}; "
              f"marks={marks}; inner={inner[:6]}")
    if problems:
        print("FAIL")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    if dry:
        print(f"dry run: SD-4 body {len(sd4_body)} lines from line {sd4_start[0] + 1}")
        return

    out = [FRONTMATTER, ""]
    out.extend(sd4_body)
    for clause in CLAUSES:
        s, e, _ = ranges[clause]
        body = iso_lines[s:e]
        while body and not body[-1].strip():
            body = body[:-1]
        out.append("")
        out.append(f"## ISO/IEC Directives Part 1, {clause}")
        out.append("")
        out.extend(body)
    OUT.write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
