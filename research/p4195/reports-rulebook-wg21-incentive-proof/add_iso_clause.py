"""Step 9: copy one whole ISO clause from the Directives into the rule extract, by Step 1's boundary rule.

Usage: add_iso_clause.py CLAUSE BEFORE_CLAUSE

The clause starts at the line that opens with its bold dotted number and ends just before
the next clause start with as many parts or fewer, or before a top-level heading. It is
inserted under "## ISO/IEC Directives Part 1, CLAUSE" just before the extract heading for
BEFORE_CLAUSE, so the ISO clauses stay in order.
"""
import re
import sys
from pathlib import Path

SOURCE = Path(r"c:\Users\Vinnie\cursor\cabinet\_inbox\ISODirectives2026-part1.md")
EXTRACT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\rules-extract.md")
START = re.compile(r'^\s*(?:#+\s*)?(?:-\s*)?\*\*(\d+(?:\.\d+)+)\b')


def main():
    clause, before = sys.argv[1], sys.argv[2]
    parts = clause.count('.') + 1
    lines = SOURCE.read_text(encoding='utf-8').splitlines()
    begin = next(i for i, line in enumerate(lines)
                 if (m := START.match(line)) and m.group(1) == clause)
    end = len(lines)
    for i in range(begin + 1, len(lines)):
        m = START.match(lines[i])
        if (m and m.group(1).count('.') + 1 <= parts) or lines[i].startswith('# '):
            end = i
            break
    body = '\n'.join(lines[begin:end]).strip('\n')
    heading = '## ISO/IEC Directives Part 1, ' + clause
    marker = '## ISO/IEC Directives Part 1, ' + before
    extract = EXTRACT.read_text(encoding='utf-8')
    if heading in extract.splitlines():
        sys.exit('already present: ' + heading)
    if marker not in extract.splitlines():
        sys.exit('missing marker: ' + marker)
    extract = extract.replace(marker + '\n', heading + '\n\n' + body + '\n\n' + marker + '\n', 1)
    EXTRACT.write_text(extract, encoding='utf-8', newline='\n')
    print('added %s: source lines %d to %d' % (heading, begin + 1, end))


if __name__ == '__main__':
    main()
