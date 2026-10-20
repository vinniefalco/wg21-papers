"""Compare chapter items by key between spine files and chapter files.

Usage: step11_finish_diff.py OLD_SPINE NEW_SPINE CHAPTER_FILE CHAPTER_NUMBER
"""
import difflib
import re
import sys

END_RE = re.compile(r'\{#([^{}\s]+)(?: weakened)?\}\s*$')
MARKER_RE = re.compile(r'^( *)1\. ')


def chapter_block(text, number):
    lines = text.split('\n')
    out, inside = [], False
    for line in lines:
        if line.startswith('## '):
            inside = line.startswith('## %d.' % number)
            if inside:
                out.append(line)
            continue
        if inside:
            out.append(line)
    return out


def items(lines):
    """Return ordered list of (key, depth, text) for every item, joining continuation lines."""
    found, current, depth = [], [], None
    for line in lines:
        m = MARKER_RE.match(line)
        if m and not current:
            depth = len(m.group(1)) // 3
            current = [line]
        elif current:
            current.append(line)
        if current:
            e = END_RE.search(line)
            if e:
                found.append((e.group(1), depth, '\n'.join(current)))
                current = []
    return found


def main():
    old_spine, new_spine, chapter, number = sys.argv[1:5]
    number = int(number)
    read = lambda p: open(p, encoding='utf-8-sig').read()
    old = items(chapter_block(read(old_spine), number))
    new = items(chapter_block(read(new_spine), number))
    chap = items(read(chapter).split('\n'))
    old_d = {k: t for k, _, t in old}
    new_d = {k: t for k, _, t in new}
    chap_d = {k: t for k, _, t in chap}
    print('old spine items:', [k for k, _, _ in old])
    print('new spine items:', [k for k, _, _ in new])
    for key, depth, text in new:
        if key not in old_d:
            print('\n=== NEW IN SPINE:', key)
            continue
        if old_d[key] != text:
            print('\n=== CHANGED:', key)
            for line in difflib.ndiff(old_d[key].split('. '), text.split('. ')):
                if line[:1] in '+-?':
                    print(line)
    for key in old_d:
        if key not in new_d:
            print('\n=== DROPPED FROM SPINE:', key)
    print('\n--- chapter vs new spine')
    for key, depth, text in new:
        if key not in chap_d:
            print('MISSING IN CHAPTER:', key)
        elif chap_d[key] != text:
            print('DIFFERS IN CHAPTER:', key)
            for line in difflib.ndiff(text.split('. '), chap_d[key].split('. ')):
                if line[:1] in '+-?':
                    print('   ', line)


if __name__ == '__main__':
    main()
