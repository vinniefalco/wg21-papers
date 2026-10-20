"""Insert proof children under items, keeping each file's line endings.

Usage: step11b_apply.py SPEC...

Spec lines (paths relative to the scratch folder):
  @@ FILE NAME                      the chapter file the following operations edit
  @@ RESTORE KEY FROM PATH          copy KEY's descendant lines from PATH, as they stand there
  @@ ADD KEY                        the lines up to the next @@ line are new descendants of KEY

New descendants go after KEY's existing descendants. The keys of new direct children are
appended to KEY's proved-by citation, which is created before its first from-citation, or
before its key marker when it has none. Every new line must sit 3 or 6 spaces deeper than KEY.
"""
import re
import sys
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent
END_RE = re.compile(r'\{#([^{}\s]+)(?: weakened)?\}\s*$')
KEY_OF = re.compile(r'\{#([a-z]+:[a-z0-9-]+)(?: weakened)?\}\s*$')


def indent(line):
    return len(line) - len(line.lstrip(' '))


def item_end(lines, key):
    hits = [i for i, l in enumerate(lines) if KEY_OF.search(l) and KEY_OF.search(l).group(1) == key]
    if len(hits) != 1:
        sys.exit('expected one item %s, found %d' % (key, len(hits)))
    i = hits[0]
    start = i
    while start > 0 and not re.match(r'^ *1\. ', lines[start]):
        start -= 1
    return start, i


def descendants_end(lines, start, end):
    base = indent(lines[start])
    j = end + 1
    while j < len(lines) and lines[j].strip() and indent(lines[j]) > base:
        j += 1
    return j


def add_proved_by(line, key, new_keys):
    if not new_keys:
        return line
    m = re.search(r'\*\[proved by ([^\]]*)\]\*', line)
    if m:
        keys = [k.strip() for k in m.group(1).split(',')] + new_keys
        return line[:m.start()] + '*[proved by %s]*' % ', '.join(keys) + line[m.end():]
    f = line.find('*[from ')
    if f < 0:
        f = KEY_OF.search(line).start()
        return line[:f].rstrip() + ' *[proved by %s]* ' % ', '.join(new_keys) + line[f:]
    return line[:f] + '*[proved by %s]* ' % ', '.join(new_keys) + line[f:]


def insert(lines, key, new_lines):
    start, end = item_end(lines, key)
    base = indent(lines[start])
    for l in new_lines:
        if indent(l) not in (base + 3, base + 6) or not KEY_OF.search(l):
            sys.exit('bad line under %s: %s' % (key, l[:60]))
    direct = [KEY_OF.search(l).group(1) for l in new_lines if indent(l) == base + 3]
    at = descendants_end(lines, start, end)
    lines[at:at] = new_lines
    lines[end] = add_proved_by(lines[end], key, direct)
    return direct


def restore_lines(path, key):
    raw = (SCRATCH / path).read_bytes().decode('utf-8').replace('\r\n', '\n')
    old = raw.split('\n')
    start, end = item_end(old, key)
    at = descendants_end(old, start, end)
    return old[end + 1:at]


def run(spec_path):
    ops, current = [], None
    for line in Path(spec_path).read_text(encoding='utf-8').split('\n'):
        if line.startswith('@@ '):
            current = line[3:].split()
            ops.append((current, []))
        elif current is not None and line.strip():
            ops[-1][1].append(line.rstrip())
    target, lines, newline = None, None, None

    def flush():
        if target is not None:
            data = newline.join(lines)
            (SCRATCH / target).write_bytes(data.encode('utf-8'))

    for words, body in ops:
        if words[0] == 'FILE':
            flush()
            target = words[1]
            raw = (SCRATCH / target).read_bytes().decode('utf-8')
            newline = '\r\n' if '\r\n' in raw else '\n'
            lines = raw.replace('\r\n', '\n').split('\n')
        elif words[0] == 'RESTORE':
            key, path = words[1], words[3]
            new_lines = restore_lines(path, key)
            direct = insert(lines, key, new_lines)
            print('%s: restored %d lines under %s (%s)' % (target, len(new_lines), key, ', '.join(direct)))
        elif words[0] == 'ADD':
            direct = insert(lines, words[1], body)
            print('%s: added %d lines under %s (%s)' % (target, len(body), words[1], ', '.join(direct)))
        else:
            sys.exit('unknown op %s' % words[0])
    flush()


if __name__ == '__main__':
    for spec in sys.argv[1:]:
        run(spec)
