"""Rebuild ch-11.md: round 2's top-level blocks wherever their statements match the current file.

Usage: step11_finish_assemble.py OLD_CHAPTER CURRENT_CHAPTER OUTPUT

A block is a top-level item with every line up to the next top-level item, table caption,
or prose line. A block is taken from OLD when every item the current block holds has the same
statement in OLD (citations ignored); otherwise the current block is kept. Prints each choice.
"""
import re
import sys

MARKER_RE = re.compile(r'^1\. ')
END_RE = re.compile(r'\{#([^{}\s]+)(?: weakened)?\}\s*$')
CITE_RE = re.compile(r'\s*\*\[(?:from|proved by)\s+[^\]]*\]\*')


def blocks(lines):
    out, current = [], None
    for line in lines:
        starts_top = bool(MARKER_RE.match(line))
        is_other = bool(line) and not line.startswith(' ') and not starts_top
        if starts_top:
            current = ['item', [line]]
            out.append(current)
        elif is_other or current is None or current[0] != 'item':
            if current is not None and current[0] == 'other':
                current[1].append(line)
            else:
                current = ['other', [line]]
                out.append(current)
        else:
            current[1].append(line)
    return out


def statements(block_lines):
    """Map each key in the block to its statement text without citations."""
    found, buf = {}, []
    for line in block_lines:
        if re.match(r'^ *1\. ', line) and not buf:
            buf = [line]
        elif buf:
            buf.append(line)
        if buf:
            m = END_RE.search(line)
            if m:
                text = '\n'.join(buf)
                text = END_RE.sub('', text)
                found[m.group(1)] = CITE_RE.sub('', text).strip()
                buf = []
    return found


def key_of(block_lines):
    for line in block_lines:
        m = END_RE.search(line)
        if m:
            return m.group(1)
    return None


def main():
    old_path, cur_path, out_path = sys.argv[1:4]
    read = lambda p: open(p, encoding='utf-8-sig').read().split('\n')
    old = {key_of(b[1]): b[1] for b in blocks(read(old_path)) if b[0] == 'item'}
    result = []
    for kind, lines in blocks(read(cur_path)):
        if kind != 'item':
            result.extend(lines)
            continue
        key = key_of(lines)
        current = statements(lines)
        previous = statements(old.get(key, []))
        same = key in old and all(previous.get(k) == text for k, text in current.items())
        # A trailing blank line belongs to the separation between blocks; keep the current one.
        trailing = []
        body = lines
        while body and body[-1] == '':
            trailing.append('')
            body = body[:-1]
        chosen = old[key] if same else body
        while chosen and chosen[-1] == '':
            chosen = chosen[:-1]
        result.extend(chosen + trailing)
        print('%-28s %s (%d lines)' % (key, 'round 2' if same else 'current', len(chosen)))
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(result))


if __name__ == '__main__':
    main()
