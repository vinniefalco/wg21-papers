"""Find module chains: consecutive top-level items in one chapter whose members, except the
last, are cited only from inside the chain, with every folded member's proof one level deep.

Citations are collected from the spine and from the chapter files, so a member cited by any
proof item outside the chain is not foldable. Tables end a chain.

Usage: step11_finish_chains.py SPINE FOUNDATION CHAPTER...
"""
import re
import sys

END_RE = re.compile(r'\{#([^{}\s]+)(?: weakened)?\}\s*$')
MARKER_RE = re.compile(r'^( *)1\. ')
HEAD_RE = re.compile(r'^## (\d+)\.')
CITE_RE = re.compile(r'\*\[(?:from|proved by)\s+([^\]]*)\]\*')
CAPTION_RE = re.compile(r'^\*Table: .*\{#(t:[a-z0-9-]+)\}\s*$')
TABLE_CITE_RE = re.compile(r'^\*\[from ')


def parse(path, chapter_default=None):
    """Return units in order: dicts with key, depth, chapter, cites, parent key, is_table."""
    units, chapter, current, last, table = [], chapter_default, [], {}, None
    for line in open(path, encoding='utf-8-sig').read().replace('\r', '').split('\n'):
        h = HEAD_RE.match(line)
        if h:
            chapter = int(h.group(1))
            continue
        c = CAPTION_RE.match(line)
        if c:
            table = dict(key=c.group(1), depth=0, chapter=chapter, cites=[], parent=None, is_table=True)
            units.append(table)
            continue
        if table is not None and TABLE_CITE_RE.match(line):
            table['cites'] = [k.strip() for m in CITE_RE.finditer(line) for k in m.group(1).split(',')]
            table = None
            continue
        m = MARKER_RE.match(line)
        if m and not current:
            depth = len(m.group(1)) // 3
            current = [line]
            cur_depth = depth
        elif current:
            current.append(line)
        if current:
            e = END_RE.search(line)
            if e:
                text = '\n'.join(current)
                cites = [k.strip() for cm in CITE_RE.finditer(text) for k in cm.group(1).split(',') if k.strip()]
                parent = last.get(cur_depth - 1) if cur_depth else None
                unit = dict(key=e.group(1), depth=cur_depth, chapter=chapter, cites=cites,
                            parent=parent, is_table=False)
                units.append(unit)
                last[cur_depth] = e.group(1)
                for deeper in (cur_depth + 1, cur_depth + 2):
                    last.pop(deeper, None)
                current = []
    return units


def main():
    spine_path, foundation_path = sys.argv[1:3]
    chapters = sys.argv[3:]
    spine = parse(spine_path)
    full = parse(foundation_path, 1)
    for path in chapters:
        full.extend(parse(path))
    top_of = {}
    for source in (spine, full):
        for u in source:
            k = u['key']
            if u['depth'] == 0:
                top_of[k] = k
            elif u['parent']:
                top_of[k] = top_of.get(u['parent'], u['parent'])
    citers = {}
    for source in (spine, full):
        for u in source:
            for k in u['cites']:
                citers.setdefault(k, set()).add(u['key'])
    depth_below = {}
    for u in full:
        if u['depth'] == 2:
            depth_below[top_of.get(u['key'])] = 2
        elif u['depth'] == 1:
            depth_below.setdefault(top_of.get(u['key']), 1)

    def subtree_keys(top):
        return {k for k, t in top_of.items() if t == top}

    tops = [u for u in spine if u['depth'] == 0]
    found = 0
    for start in range(len(tops)):
        chain = []
        for u in tops[start:]:
            if chain and (u['chapter'] != chain[0]['chapter'] or u['is_table']):
                break
            if u['is_table']:
                break
            chain.append(u)
            if len(chain) < 2:
                continue
            inside = set()
            for member in chain:
                inside |= subtree_keys(member['key'])
            ok = True
            reasons = []
            for member in chain[:-1]:
                k = member['key']
                if k.startswith(('m:', 't:', 'thm:', 'c:')):
                    ok = False
                    break
                outside = set()
                for sk in subtree_keys(k):
                    outside |= {c for c in citers.get(sk, set()) if c not in inside}
                if outside:
                    ok = False
                    break
                if depth_below.get(k, 0) >= 2:
                    ok = False
                    reasons.append('%s has grandchildren' % k)
                    break
            last = chain[-1]['key']
            last_outside = set()
            for sk in subtree_keys(last):
                last_outside |= {c for c in citers.get(sk, set()) if c not in inside}
            if ok and (last_outside or last.startswith(('m:', 't:', 'thm:', 'c:'))):
                found += 1
                print('ch%d: fold %s into %s (last cited by %s)' % (
                    chain[0]['chapter'], ', '.join(m['key'] for m in chain[:-1]), last,
                    ', '.join(sorted(last_outside)[:6])))
    print('%d chains' % found)


if __name__ == '__main__':
    main()
