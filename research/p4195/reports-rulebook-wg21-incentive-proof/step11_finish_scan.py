"""List always-prove items that have no children in the chapter files.

Always-prove kinds: settled lemmas (l:settled-*), the Theorem, table ranks (items a table cites),
corollaries (c:*), and items whose from-citations reach results (not ax:, d:, f:) of two or more
chapters, or items of two or more chapters counting the foundation as chapter 1.

Usage: step11_finish_scan.py FOUNDATION CHAPTER...
"""
import re
import sys

END_RE = re.compile(r'\{#([^{}\s]+)(?: weakened)?\}\s*$')
MARKER_RE = re.compile(r'^( *)1\. ')
HEAD_RE = re.compile(r'^## (\d+)\.')
CITE_RE = re.compile(r'\*\[(from|proved by)\s+([^\]]*)\]\*')
CAPTION_RE = re.compile(r'^\*Table: .*\{#(t:[a-z0-9-]+)\}\s*$')
BASIC = ('ax:', 'd:', 'f:')


def parse(paths):
    items, chapter_of, tables = [], {}, {}
    for index, path in enumerate(paths):
        chapter = 1 if index == 0 else None
        current, depth, last = [], None, {}
        table = None
        for line in open(path, encoding='utf-8-sig').read().split('\n'):
            h = HEAD_RE.match(line)
            if h and index:
                chapter = int(h.group(1))
            c = CAPTION_RE.match(line)
            if c:
                table = c.group(1)
                continue
            if table and line.startswith('*[from'):
                tables[table] = [k.strip() for m in CITE_RE.finditer(line) for k in m.group(2).split(',')]
                table = None
                continue
            m = MARKER_RE.match(line)
            if m and not current:
                depth = len(m.group(1)) // 3
                current = [line]
            elif current:
                current.append(line)
            if current:
                e = END_RE.search(line)
                if e:
                    text = '\n'.join(current)
                    key = e.group(1)
                    froms, proved = [], []
                    for cm in CITE_RE.finditer(text):
                        keys = [k.strip() for k in cm.group(2).split(',') if k.strip()]
                        (froms if cm.group(1) == 'from' else proved).extend(keys)
                    parent = last.get(depth - 1) if depth else None
                    item = dict(key=key, depth=depth, chapter=chapter, froms=froms,
                                proved=proved, parent=parent, children=[])
                    items.append(item)
                    chapter_of[key] = chapter
                    last[depth] = item
                    for deeper in (depth + 1, depth + 2):
                        last.pop(deeper, None)
                    if parent:
                        parent['children'].append(item)
                    current = []
    return items, chapter_of, tables


def main():
    items, chapter_of, tables = parse(sys.argv[1:])
    ranks = {k for keys in tables.values() for k in keys}
    rows = []
    for it in items:
        if it['chapter'] == 1 or it['children']:
            continue
        key = it['key']
        reasons = []
        if key.startswith('l:settled-'):
            reasons.append('settled lemma')
        if key.startswith('thm:'):
            reasons.append('Theorem')
        if key in ranks:
            reasons.append('table rank')
        if key.startswith('c:'):
            reasons.append('corollary')
        result_chapters = {chapter_of.get(k) for k in it['froms'] if not k.startswith(BASIC)}
        result_chapters.discard(None)
        all_chapters = {chapter_of.get(k) for k in it['froms']}
        all_chapters.discard(None)
        if len(result_chapters) >= 2:
            reasons.append('joins results of chapters %s' % sorted(result_chapters))
        elif len(all_chapters) >= 2:
            reasons.append('joins items of chapters %s' % sorted(all_chapters))
        if reasons:
            rows.append((it['chapter'], key, '; '.join(reasons)))
    for chapter, key, reason in rows:
        print('ch%02d  %-32s %s' % (chapter, key, reason))
    print('%d items' % len(rows))


if __name__ == '__main__':
    main()
