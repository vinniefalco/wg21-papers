"""Report changed items between two versions of the same files, and key collisions.

Usage:
  step11_finish_keys.py changed OLD NEW            items whose text differs, by key
  step11_finish_keys.py collide RESTORED FILE...   restored keys defined in other files
  step11_finish_keys.py cites FILE KEY...          which given keys FILE's items cite
"""
import re
import sys

END_RE = re.compile(r'\{#([^{}\s]+)(?: weakened)?\}\s*$')
MARKER_RE = re.compile(r'^( *)1\. ')
CITE_RE = re.compile(r'\*\[(?:from|proved by)\s+([^\]]*)\]\*')


def items(path):
    found, current = [], []
    for line in open(path, encoding='utf-8-sig').read().split('\n'):
        if MARKER_RE.match(line) and not current:
            current = [line]
        elif current:
            current.append(line)
        if current:
            e = END_RE.search(line)
            if e:
                found.append((e.group(1), '\n'.join(current)))
                current = []
    return found


def strip_cites(text):
    return CITE_RE.sub('', text)


def main():
    mode = sys.argv[1]
    if mode == 'changed':
        old = dict(items(sys.argv[2]))
        new = dict(items(sys.argv[3]))
        for key in new:
            if key not in old:
                print('ADDED', key)
            elif strip_cites(old[key]) != strip_cites(new[key]):
                print('STATEMENT CHANGED', key)
            elif old[key] != new[key]:
                print('CITES CHANGED', key)
        for key in old:
            if key not in new:
                print('REMOVED', key)
    elif mode == 'collide':
        restored = [k for k, _ in items(sys.argv[2])]
        others = {}
        for path in sys.argv[3:]:
            for k, _ in items(path):
                others.setdefault(k, path)
        for k in restored:
            if k in others:
                print('COLLISION', k, others[k])
    elif mode == 'cites':
        wanted = set(sys.argv[3:])
        for key, text in items(sys.argv[2]):
            cited = set()
            for m in CITE_RE.finditer(text):
                cited.update(c.strip() for c in m.group(1).split(','))
            hit = sorted(cited & wanted)
            if hit:
                print(key, '->', ', '.join(hit))


if __name__ == '__main__':
    main()
