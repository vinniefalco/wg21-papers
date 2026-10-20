"""Fold a top-level item into the top-level item right after it, as its first lettered child.

Usage: step11_finish_fold.py CHILD_KEY PARENT_KEY FILE...

In each file, the child must be a one-line top-level item with no children, directly followed
by the parent's first line. The child line gains a 3-space indent and moves under the parent's
own line; the parent's from-citation drops the child and a proved-by citation names it first.
Line endings are kept as found.
"""
import re
import sys


def fold(path, child, parent):
    raw = open(path, 'rb').read().decode('utf-8')
    newline = '\r\n' if '\r\n' in raw else '\n'
    lines = raw.split(newline)
    ci = [i for i, l in enumerate(lines) if l.startswith('1. ') and l.rstrip().endswith('{#%s}' % child)]
    if len(ci) != 1:
        sys.exit('%s: expected one top-level line for %s, found %d' % (path, child, len(ci)))
    i = ci[0]
    head = lines[i + 1]
    if not head.startswith('1. ') or not head.rstrip().endswith('{#%s}' % parent):
        sys.exit('%s: %s is not followed by the one-line item %s' % (path, child, parent))
    if i + 2 < len(lines) and lines[i + 2].startswith('   '):
        sys.exit('%s: %s already has children; insert by hand' % (path, parent))
    from_re = re.compile(r'\*\[from ([^\]]*)\]\*')
    m = from_re.search(head)
    keys = [k.strip() for k in m.group(1).split(',')]
    if child not in keys:
        sys.exit('%s: %s does not cite %s' % (path, parent, child))
    keys.remove(child)
    proved = re.search(r'\*\[proved by ([^\]]*)\]\*', head)
    if proved:
        sys.exit('%s: %s already has a proved-by citation; insert by hand' % (path, parent))
    new_head = head[:m.start()] + '*[proved by %s]* *[from %s]*' % (child, ', '.join(keys)) + head[m.end():]
    lines[i:i + 2] = [new_head, '   ' + lines[i]]
    with open(path, 'wb') as f:
        f.write(newline.join(lines).encode('utf-8'))
    print('%s: folded %s into %s' % (path, child, parent))


def main():
    child, parent = sys.argv[1:3]
    for path in sys.argv[3:]:
        fold(path, child, parent)


if __name__ == '__main__':
    main()
