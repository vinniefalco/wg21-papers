"""Audit chapters for proofs dropped since round 2 and for always-prove items left bare.

Usage: step11b_audit.py OLD_DIR NEW_DIR OLD_SPINE NEW_SPINE CHAPTER...

For each top-level item and spine child of each chapter, print round 2's children, the current
children, whether the statement changed between the spines, and the chapters of the proved
results (not ax:, d:, f:) its from-citation names.
"""
import re
import sys

END_RE = re.compile(r'\{#([^{}\s]+)(?: weakened)?\}\s*$')
HEAD_RE = re.compile(r'^## (\d+)\.')
CITE_RE = re.compile(r'\*\[(from|proved by)\s+([^\]]*)\]\*')
BASIC = ('ax:', 'd:', 'f:')


def parse(path):
    """Return ordered dict key -> dict(depth, parent, froms, text, chapter)."""
    out, cur, last, chapter = {}, [], {}, 1
    for line in open(path, encoding='utf-8-sig').read().replace('\r', '').split('\n'):
        h = HEAD_RE.match(line)
        if h:
            chapter = int(h.group(1))
        m0 = re.match(r'^( *)1\. ', line)
        if m0 and not cur:
            cur, depth = [line], len(m0.group(1)) // 3
        elif cur:
            cur.append(line)
        if cur:
            m = END_RE.search(line)
            if m:
                text = '\n'.join(cur)
                froms = [k.strip() for c in CITE_RE.finditer(text) if c.group(1) == 'from'
                         for k in c.group(2).split(',') if k.strip()]
                key = m.group(1)
                out[key] = dict(depth=depth, parent=last.get(depth - 1) if depth else None,
                                froms=froms, chapter=chapter,
                                text=CITE_RE.sub('', END_RE.sub('', text)).strip())
                last[depth] = key
                cur = []
    return out


def children(items, key):
    return [k for k, v in items.items() if v['parent'] == key]


def main():
    old_dir, new_dir, old_spine, new_spine = sys.argv[1:5]
    chapters = [int(n) for n in sys.argv[5:]]
    spine_old = parse(old_spine)
    spine_new = parse(new_spine)
    chapter_of = {k: v['chapter'] for k, v in spine_new.items()}
    for k in spine_new:
        if spine_new[k]['depth'] and spine_new[k]['parent']:
            chapter_of[k] = spine_new[spine_new[k]['parent']]['chapter'] if spine_new[k]['parent'] in spine_new else chapter_of[k]
    for n in chapters:
        old = parse('%s\\ch-%02d.md' % (old_dir, n))
        new = parse('%s\\ch-%02d.md' % (new_dir, n))
        for k in new:
            chapter_of.setdefault(k, n)
        print('=== chapter %d' % n)
        for key, item in new.items():
            in_spine = key in spine_new
            if not in_spine:
                continue
            res = sorted({chapter_of.get(c) for c in item['froms'] if not c.startswith(BASIC) and chapter_of.get(c)})
            changed = key in spine_old and spine_old[key]['text'] != spine_new[key]['text']
            oc = children(old, key) if key in old else []
            nc = children(new, key)
            flag = []
            if changed:
                flag.append('CHANGED')
            if oc and not nc:
                flag.append('DROPPED')
            if len(res) >= 2 and not nc:
                flag.append('JOIN-BARE')
            print('%-30s d%d r2=%-2d now=%-2d results=%s %s' % (
                key, item['depth'], len(oc), len(nc), res, ' '.join(flag)))


if __name__ == '__main__':
    main()
