"""Step 9: copy quoted passages from a research file into the rule extract, typing none by hand.

Usage: append_research_extract.py RESEARCH SPEC

SPEC is a text file with one line per section: research heading | extract heading.
The script copies every blockquote line under the research heading, drops "> [...]"
skip markers, and appends the text to the extract under "## <extract heading>".
A section already present in the extract is not appended twice.
"""
import sys
from pathlib import Path

EXTRACT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\rules-extract.md")


def quoted_blocks(text):
    blocks = {}
    current = None
    for line in text.splitlines():
        if line.startswith('#'):
            current = line.lstrip('#').strip()
            blocks.setdefault(current, [])
        elif current is not None and line.startswith('>'):
            body = line[1:]
            if body.startswith(' '):
                body = body[1:]
            if body.strip() != '[...]':
                blocks[current].append(body)
    return blocks


def tidy(lines):
    out = []
    for line in lines:
        if not line.strip() and (not out or not out[-1].strip()):
            continue
        out.append(line.rstrip())
    while out and not out[-1].strip():
        out.pop()
    return out


def main():
    research = Path(sys.argv[1]).read_text(encoding='utf-8')
    spec = Path(sys.argv[2]).read_text(encoding='utf-8')
    blocks = quoted_blocks(research)
    extract = EXTRACT.read_text(encoding='utf-8')
    added = []
    for row in spec.splitlines():
        if not row.strip():
            continue
        source, target = (part.strip() for part in row.split('|'))
        if source not in blocks or not tidy(blocks[source]):
            sys.exit('no quoted text under research heading: ' + source)
        heading = '## ' + target
        if heading in extract.splitlines():
            continue
        extract = extract.rstrip('\n') + '\n\n' + heading + '\n\n' + '\n'.join(tidy(blocks[source])) + '\n'
        added.append(target)
    EXTRACT.write_text(extract, encoding='utf-8', newline='\n')
    for target in added:
        print('added: ' + target)


if __name__ == '__main__':
    main()
