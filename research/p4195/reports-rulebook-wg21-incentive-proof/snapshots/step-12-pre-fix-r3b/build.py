"""Check and emit the P4195 incentive proof.

Usage:
  build.py [check] --extract EXTRACT [--mode foundation|spine|full]
           [--max-items N] [--labels] [--dependents KEY[,KEY]] [--emit PATH]
           [--front FILE] [--appendix FILE] [--footer TEXT] SOURCE...

Without --labels, --dependents, or --emit, it runs the checks: one line per
failure, exit status 1 on any. A leading check word names that default and is
always dropped, so a source file named check must be given as ./check.
"""

import argparse
import bisect
import re
import sys
from collections import defaultdict, deque

KEY_RE = re.compile(r'(?:ax|d|f|l|inf|ind|p|c|t|m|thm):[a-z0-9-]+\Z')
ORPHAN_EXEMPT = ('m:', 't:', 'thm:', 'c:')

MARKER_RE = re.compile(r'( *)1\.(?: |$)')
END_RE = re.compile(r'\s*\{#([^{}]*)\}\s*$')
KEY_MARKER_RE = re.compile(r'\{#[^{}]*\}')
HEADING_RE = re.compile(r'## \d+\. \S')
CAPTION_RE = re.compile(r'\*Table: (.*)\*\s+\{#([^{}]*)\}\s*$')
ROW_RE = re.compile(r' {0,3}\|')
TABLE_CITE_RE = re.compile(r'\*\[(?:from|proved by)\s+[^\]]*\]\*$')
CITE_RE = re.compile(r'\*\[(from|proved by)\s+([^\]]*)\]\*')
CITE_OPEN_RE = re.compile(r'\*\[\s*(?:from|proved\s+by)\b', re.IGNORECASE)
CITE_OPENERS = ('*[from', '*[proved by')
SEPARATOR_CELL_RE = re.compile(r'[\s:-]*-[\s:-]*')
QUOTE_RE = re.compile(r'"[^"]*"')
CURLY_QUOTES = str.maketrans({'\u201c': '"', '\u201d': '"', '\u2018': "'", '\u2019': "'"})

WORDS = (
    'perverse', 'railroad', 'steamroll', 'capture', 'dominate', 'exploit',
    'gaming', 'stack the room', 'punish', 'retaliate', 'insider', 'outsider',
    'lock-in', 'cliff', 'obviously', 'clearly', 'of course', 'door', 'carry',
)

BLOCKS = {
    'item': 'list', 'cont': 'list', 'prose': 'prose', 'heading': 'heading',
    'caption': 'caption', 'row': 'table', 'cite': 'cite',
}


def inflections(word):
    if word.endswith('ing'):
        return [word, word + 's', word[:-3] + 'ed']
    if word.endswith('e'):
        return [word, word + 's', word + 'd', word[:-1] + 'ing']
    if re.search(r'[^aeiou]y$', word):
        return [word, word[:-1] + 'ies', word[:-1] + 'ied', word + 'ing']
    if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return [word, word + 'es', word + 'ed', word + 'ing']
    return [word, word + 's', word + 'ed', word + 'ing']


def forms(term):
    first, space, rest = term.partition(' ')
    if space:
        return [form + ' ' + rest for form in inflections(first)]
    head, hyphen, tail = term.rpartition('-')
    if hyphen:
        return ([head + '-' + form for form in inflections(tail)]
                + [form + '-' + tail for form in inflections(head)])
    return inflections(term)


def word_pattern():
    alternatives = sorted({form for term in WORDS for form in forms(term)}, key=len, reverse=True)
    body = '|'.join(r'\s+'.join(map(re.escape, form.split())) for form in alternatives)
    return re.compile(r'(?<!\w)(?:%s)(?!\w)' % body, re.IGNORECASE)


FORBIDDEN = (
    word_pattern(),
    re.compile('\u2014'),
    re.compile('--'),
    re.compile(r'(?<![A-Za-z0-9])P[0-9]{4}', re.IGNORECASE),
    re.compile(r'C\+\+[0-9]{2}', re.IGNORECASE),
)
YEAR_RE = re.compile(r'(?<![A-Za-z0-9])(?:199[0-9]|20[0-9]{2})(?![0-9])')


def read(path):
    with open(path, encoding='utf-8-sig') as f:
        return f.read()


class Source:
    """One input file, split into lines."""

    def __init__(self, path, index):
        self.path = path
        self.index = index
        rows = read(path).split('\n')
        if rows[-1] == '':
            rows.pop()
        self.lines = [Line(self, num, row) for num, row in enumerate(rows, 1)]
        self.cites = []


class Line:

    def __init__(self, source, num, text):
        self.source = source
        self.num = num
        self.text = text
        self.kind = None
        self.owner = None
        self.pos = None


class Item:
    is_table = False

    def __init__(self, line, indent, parent, pos):
        self.line = line
        self.content = indent + 3
        self.parent = parent
        self.pos = pos
        self.key = None
        self.children = []
        self.lines = [line]
        self.end = None
        self.cites = []
        self.label = ''
        self.number = None


class Table:
    is_table = True

    def __init__(self, line, key, caption, pos):
        self.line = line
        self.key = key
        self.caption = caption
        self.pos = pos
        self.children = []
        self.lines = [line]
        self.end = None
        self.cites = []
        self.label = ''
        self.number = None


class Proof:

    def __init__(self, sources):
        self.sources = sources
        self.items = []
        self.tables = []
        self.units = []
        self.errors = []
        self.defs = {}
        self.dups = []

    def error(self, line, message):
        self.errors.append((line, message))


def name(unit):
    return unit.key or unit.label


def parse(proof, source):
    stack = {}
    in_list = False
    item = None
    table = None
    table_state = None
    for line in source.lines:
        line.pos = len(proof.units)
        text = line.text.rstrip()
        if table is not None:
            if not text:
                line.kind = 'blank'
                if table_state == 'rows':
                    table_state = 'after'
                continue
            if table_state != 'after' and ROW_RE.match(text):
                line.kind, line.owner = 'row', table
                table.lines.append(line)
                table_state = 'rows'
                continue
            if table_state != 'caption' and TABLE_CITE_RE.match(text):
                line.kind, line.owner = 'cite', table
                table.lines.append(line)
                strays(proof, table)
                table = None
                continue
            if table_state == 'caption':
                proof.error(table.line, 'table caption is not followed by a table')
            else:
                proof.error(line, 'table must end with a line holding only a *[from ...]* citation')
            table = None
        if not text:
            line.kind = 'blank'
            if item is not None:
                item.lines.append(line)
            continue
        marker = MARKER_RE.match(text)
        indent = len(text) - len(text.lstrip(' '))
        is_marker = marker is not None and indent in (0, 3, 6)
        if item is not None:
            if marker is None and indent >= item.content:
                line.kind, line.owner = 'cont', item
                item.lines.append(line)
                if END_RE.search(text):
                    close(proof, item, line, text)
                    item = None
                continue
            proof.error(item.line, 'item does not end with {#KEY}')
            item = None
        if is_marker:
            level = indent // 3 + 1
            parent = stack.get(level - 1) if in_list and level > 1 else None
            if level > 1 and parent is None:
                proof.error(line, 'nested item has no parent item above it')
            new = Item(line, indent, parent, len(proof.units))
            line.kind, line.owner = 'item', new
            if parent is not None:
                parent.children.append(new)
            proof.items.append(new)
            proof.units.append(new)
            stack[level] = new
            for deeper in range(level + 1, 4):
                stack.pop(deeper, None)
            in_list = True
            if END_RE.search(text):
                close(proof, new, line, text)
            else:
                item = new
            continue
        if marker is not None:
            proof.error(line, 'list marker indented %d spaces; use 0, 3, or 6' % indent)
            line.kind = 'prose'
            continue
        if indent and in_list:
            proof.error(line, 'indented line after an item ends; the key must end the last line of its item')
            line.kind = 'prose'
            continue
        in_list = False
        stack.clear()
        if text.startswith('*Table:'):
            caption = CAPTION_RE.match(text)
            key = caption.group(2).strip() if caption else ''
            if KEY_RE.match(key) and key.startswith('t:'):
                table = Table(line, key, caption.group(1), len(proof.units))
                table_state = 'caption'
                line.kind, line.owner = 'caption', table
                proof.tables.append(table)
                proof.units.append(table)
                continue
            proof.error(line, 'malformed table caption; use *Table: TEXT* {#t:KEY}')
        line.kind = 'heading' if HEADING_RE.match(text) else 'prose'
        if KEY_MARKER_RE.search(text):
            proof.error(line, 'key marker outside an item')
    if item is not None:
        proof.error(item.line, 'item does not end with {#KEY}')
    if table is not None:
        if table_state == 'caption':
            proof.error(table.line, 'table caption is not followed by a table')
        else:
            proof.error(table.line, 'table must end with a line holding only a *[from ...]* citation')


def close(proof, item, line, text):
    item.end = line
    strays(proof, item)
    parts = END_RE.search(text).group(1).split()
    if parts and KEY_RE.match(parts[0]) and parts[1:] in ([], ['weakened']):
        item.key = parts[0]
    else:
        proof.error(line, 'malformed key marker {#%s}' % ' '.join(parts))


def strays(proof, unit):
    """Report each key marker in a finished item or table other than its own key."""
    for line in unit.lines:
        if line.kind == 'caption':
            text = unit.caption
        elif line is unit.end:
            text = END_RE.sub('', line.text)
        else:
            text = line.text
        if KEY_MARKER_RE.search(text):
            proof.error(line, 'stray key marker; the key must end the %s'
                        % ('caption line' if unit.is_table else 'last line of its item'))


def citations(proof, line):
    """Return (kind, key) for each citation on the line."""
    found = []
    matches = list(CITE_RE.finditer(line.text))
    starts = {match.start() for match in matches}
    for opener in CITE_OPEN_RE.finditer(line.text):
        if opener.start() in starts:
            continue
        if opener.group(0) in CITE_OPENERS:
            proof.error(line, 'citation must open and close on one line')
        else:
            proof.error(line, 'malformed citation opener %s; use *[from or *[proved by' % opener.group(0))
    for match in matches:
        keys = [key.strip() for key in match.group(2).split(',')]
        if not all(keys):
            proof.error(line, 'citation has an empty key')
        found.extend((match.group(1), key) for key in keys if key)
    return found


def letters(n):
    text = ''
    while n:
        n, rest = divmod(n - 1, 26)
        text = chr(ord('a') + rest) + text
    return text


ROMAN = ((1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), (90, 'xc'),
         (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i'))


def roman(n):
    text = ''
    for value, digits in ROMAN:
        count, n = divmod(n, value)
        text += digits * count
    return text


def build_proof(sources):
    proof = Proof(sources)
    for source in sources:
        parse(proof, source)
    number = 0
    for item in proof.items:
        if item.parent is None:
            number += 1
            item.number = number
            item.label = str(number)
        else:
            ordinal = item.parent.children.index(item) + 1
            if item.parent.parent is None:
                item.label = item.parent.label + letters(ordinal)
            else:
                item.label = '%s.%s' % (item.parent.label, roman(ordinal))
    for number, table in enumerate(proof.tables, 1):
        table.number = number
        table.label = 'Table %d' % number
    for unit in proof.units:
        if unit.key is None:
            continue
        if unit.key in proof.defs:
            proof.dups.append((unit, proof.defs[unit.key]))
        else:
            proof.defs[unit.key] = unit
    for unit in proof.units:
        for line in unit.lines:
            unit.cites.extend((kind, key, line) for kind, key in citations(proof, line))
    for source in sources:
        for line in source.lines:
            if line.kind in ('prose', 'heading'):
                source.cites.extend((kind, key, line) for kind, key in citations(proof, line))
    return proof


def attach(proof, source):
    """Collect the citations of a front or appendix file."""
    for line in source.lines:
        source.cites.extend((kind, key, line) for kind, key in citations(proof, line))
    return source


def offsets(texts):
    starts = [0]
    for text in texts[:-1]:
        starts.append(starts[-1] + len(text) + 1)
    return starts


def normalize(text):
    return ' '.join(text.translate(CURLY_QUOTES).split())


def is_separator(text):
    text = text.strip()
    if '|' not in text:
        return False
    return all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in text.strip('|').split('|'))


def blank_out(pattern, text):
    return pattern.sub(lambda match: re.sub(r'[^\n]', ' ', match.group(0)), text)


def forbidden(lines, years=True):
    """Yield (line, column, message) for each forbidden string outside straight double quotes."""
    texts = ['' if is_separator(line.text) else line.text for line in lines]
    text = blank_out(QUOTE_RE, '\n'.join(texts))
    starts = offsets(texts)
    hits = []
    for pattern in FORBIDDEN + ((YEAR_RE,) if years else ()):
        hits.extend((match.start(), match.group(0)) for match in pattern.finditer(text))
    for offset, found in sorted(hits):
        i = bisect.bisect_right(starts, offset) - 1
        if found == '\u2014':
            message = 'forbidden em dash'
        else:
            message = 'forbidden "%s"' % ' '.join(found.split())
        yield lines[i], offset - starts[i], message


def runs(lines, keep):
    block = []
    for line in lines:
        if keep(line):
            block.append(line)
        elif block:
            yield block
            block = []
    if block:
        yield block


def descendants(item):
    yield item
    for child in item.children:
        yield from descendants(child)


def cycles(units, graph):
    """Return the strongly connected components of the citation graph that hold a cycle."""
    index, low, stack, on_stack, found = {}, {}, [], set(), []
    for root in units:
        if root in index:
            continue
        index[root] = low[root] = len(index)
        stack.append(root)
        on_stack.add(root)
        work = [(root, iter(graph[root]))]
        while work:
            node, edges = work[-1]
            for target in edges:
                if target not in index:
                    index[target] = low[target] = len(index)
                    stack.append(target)
                    on_stack.add(target)
                    work.append((target, iter(graph[target])))
                    break
                if target in on_stack:
                    low[node] = min(low[node], index[target])
            else:
                work.pop()
                if work:
                    parent = work[-1][0]
                    low[parent] = min(low[parent], low[node])
                if low[node] == index[node]:
                    component = []
                    while True:
                        member = stack.pop()
                        on_stack.discard(member)
                        component.append(member)
                        if member is node:
                            break
                    if len(component) > 1 or node in graph[node]:
                        found.append(component)
    return found


def cycle_path(start, members, graph):
    """Return a shortest cycle from start back to start, which must lie on a cycle within members."""
    previous = {}
    queue = deque([start])
    while True:
        node = queue.popleft()
        for target in graph[node]:
            if target is start:
                path = [node]
                while path[-1] is not start:
                    path.append(previous[path[-1]])
                return path[::-1] + [start]
            if target in members and target not in previous:
                previous[target] = node
                queue.append(target)


def run_checks(proof, extract, mode, max_items, front=None, appendix=None):
    failures = [(0, line, message, 0) for line, message in proof.errors]

    def fail(check, line, message, column=0):
        failures.append((check, line, message, column))

    extras = [source for source in (front, appendix) if source]
    for unit, first in proof.dups:
        fail(1, unit.line, '%s is defined twice, first at %s:%d'
             % (unit.key, first.line.source.path, first.line.num))
    for owner in proof.units + proof.sources + extras:
        for kind, key, line in owner.cites:
            if key not in proof.defs:
                fail(1, line, '%s is cited but not defined' % key)

    def check_target(citer, pos, children, kind, key, line):
        target = proof.defs.get(key)
        if target is None:
            return
        if kind == 'from' and target.pos >= pos:
            fail(2, line, '%s cites %s with from, but %s is not earlier' % (citer, key, key))
        elif kind == 'proved by' and key not in children:
            fail(3, line, '%s cites %s with proved by, but %s is not its child' % (citer, key, key))

    for unit in proof.units:
        children = {child.key for child in unit.children}
        for kind, key, line in unit.cites:
            check_target(name(unit), unit.pos, children, kind, key, line)
    for source in proof.sources:
        for kind, key, line in source.cites:
            check_target('%s line' % line.kind, line.pos, (), kind, key, line)

    graph = {unit: [proof.defs[key] for _, key, _ in unit.cites if key in proof.defs]
             for unit in proof.units}
    for component in cycles(proof.units, graph):
        start = min(component, key=lambda unit: unit.pos)
        path = cycle_path(start, set(component), graph)
        fail(4, start.line, 'citation cycle ' + ' -> '.join(name(unit) for unit in path))

    if mode != 'foundation':
        citers = defaultdict(set)
        for unit in proof.units:
            for _, key, _ in unit.cites:
                citers[key].add(unit)
        for unit in proof.units:
            if unit.key is None or unit.key.startswith(ORPHAN_EXEMPT):
                continue
            subtree = list(descendants(unit))
            inside = set(subtree)
            if not any(citer not in inside
                       for member in subtree if member.key
                       for citer in citers[member.key]):
                fail(5, unit.line, '%s is an orphan' % unit.key)

    rules = normalize(extract)
    for item in proof.items:
        texts = [line.text for line in item.lines]
        text = '\n'.join(texts)
        if '**Fact.**' not in text:
            continue
        starts = offsets(texts)
        for match in QUOTE_RE.finditer(text):
            i = bisect.bisect_right(starts, match.start()) - 1
            for piece in match.group(0)[1:-1].split('...'):
                piece = normalize(piece)
                if piece and piece not in rules:
                    fail(6, item.lines[i], '%s quotes text missing from the extract: "%s"'
                         % (name(item), piece), match.start() - starts[i])

    for unit in proof.units:
        if unit.is_table:
            groups = [[line] for line in unit.lines if line.kind != 'cite']
        else:
            groups = [unit.lines]
        for group in groups:
            for line, column, message in forbidden(group):
                fail(7, line, message, column)
    for source in proof.sources:
        for block in runs(source.lines, lambda line: line.kind in ('prose', 'heading')):
            for line, column, message in forbidden(block):
                fail(7, line, message, column)
    for source, years in ((front, True), (appendix, False)):
        if source:
            for block in runs(source.lines, lambda line: line.text.strip()):
                for line, column, message in forbidden(block, years=years):
                    fail(7, line, message, column)

    top = sum(1 for item in proof.items if item.parent is None)
    if mode != 'foundation' and top > max_items:
        fail(8, None, '%d top-level items, more than --max-items %d' % (top, max_items))

    return report(failures)


def report(failures):
    def order(failure):
        check, line, _, column = failure
        if line is None:
            return (check, -2, 0, column)
        return (check, line.source.index, line.num, column)

    out = []
    for check, line, message, _ in sorted(failures, key=order):
        tag = 'format' if check == 0 else 'check %d' % check
        if line is None:
            out.append('%s: %s' % (tag, message))
        else:
            out.append('%s:%d: %s: %s' % (line.source.path, line.num, tag, message))
    return out


def relabel(text, labels):
    def swap(match):
        keys = [key.strip() for key in match.group(2).split(',') if key.strip()]
        return '*[%s %s]*' % (match.group(1), ', '.join(labels.get(key, key) for key in keys))
    return CITE_RE.sub(swap, text)


def render(line, labels):
    owner, text = line.owner, line.text
    if line.kind in ('prose', 'heading'):
        return relabel(text, labels)
    if line.kind == 'caption':
        return '*Table %d. %s*' % (owner.number, relabel(owner.caption, labels))
    if line.kind == 'item':
        body = text[MARKER_RE.match(text).end():]
        text = ' ' * owner.out_indent + owner.marker + ' ' + body
    elif line.kind == 'cont':
        text = ' ' * owner.out_content + text[owner.content:]
    if line is owner.end:
        text = END_RE.sub('', text)
    return relabel(text, labels).rstrip()


def render_proof(proof, labels):
    out = []
    previous = None
    gap = True
    for source in proof.sources:
        for line in source.lines:
            if line.kind == 'blank':
                out.append('')
                gap = True
                continue
            block = BLOCKS[line.kind]
            if not gap and block != previous:
                out.append('')
            out.append(render(line, labels))
            previous, gap = block, False
    return out


def emit(proof, front, appendix, footer):
    labels = {key: unit.label for key, unit in proof.defs.items()}
    for item in proof.items:
        if item.parent is None:
            item.marker, item.out_indent = '%d.' % item.number, 0
        else:
            item.marker, item.out_indent = '1.', item.parent.out_content
        item.out_content = item.out_indent + len(item.marker) + 1
    sections = []
    if front:
        sections.append([relabel(line.text, labels) for line in front.lines])
    sections.append(render_proof(proof, labels))
    if appendix:
        sections.append([relabel(line.text, labels) for line in appendix.lines])
    if footer:
        sections.append(['*%s*' % footer])
    out = []
    for section in sections:
        while section and not section[0].strip():
            section.pop(0)
        while section and not section[-1].strip():
            section.pop()
        if section:
            if out:
                out.append('')
            out.extend(section)
    return '\n'.join(out) + '\n'


def dependents(proof, keys):
    wanted = [key.strip() for key in keys.split(',') if key.strip()]
    status = 0
    for key in wanted:
        if key not in proof.defs:
            print('%s is not defined' % key)
            status = 1
    citers = defaultdict(list)
    for unit in proof.units:
        for _, key, _ in unit.cites:
            citers[key].append(unit)
    seen = set()
    queue = deque(key for key in wanted if key in proof.defs)
    while queue:
        for unit in citers[queue.popleft()]:
            if unit not in seen:
                seen.add(unit)
                if unit.key:
                    queue.append(unit.key)
    for unit in sorted(seen, key=lambda unit: unit.pos):
        print(name(unit), unit.label)
    return status


def write(path, text):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def count(n, noun):
    return '%d %s%s' % (n, noun, '' if n == 1 else 's')


def parse_args(argv):
    parser = argparse.ArgumentParser(prog='build.py', description='Check and emit the incentive proof.')
    parser.add_argument('--extract', required=True, help='rule text that Fact quotes must appear in')
    parser.add_argument('--mode', choices=('foundation', 'spine', 'full'), default='full')
    parser.add_argument('--max-items', type=int, default=150, metavar='N',
                        help='top-level item limit in spine and full modes (default 150)')
    parser.add_argument('--labels', action='store_true', help='print each key with its label')
    parser.add_argument('--dependents', metavar='KEYS',
                        help='comma-separated keys; print every item that cites them, directly or not')
    parser.add_argument('--emit', metavar='PATH', help='write the proof only if every check passes')
    parser.add_argument('--front', metavar='FILE', help='copied before the proof on emit')
    parser.add_argument('--appendix', metavar='FILE', help='copied after the proof on emit')
    parser.add_argument('--footer', metavar='TEXT', help='written as the last line, in italics')
    parser.add_argument('sources', nargs='+', metavar='SOURCE')
    return parser.parse_intermixed_args(argv)


def main(argv=None):
    args = parse_args(argv)
    paths = list(args.sources)
    if paths[0] == 'check':
        paths.pop(0)
    if not paths:
        print('build.py: no SOURCE files given')
        return 2
    checking = bool(args.emit) or not (args.labels or args.dependents)
    try:
        proof = build_proof([Source(path, index) for index, path in enumerate(paths)])
        front = attach(proof, Source(args.front, -1)) if args.front else None
        appendix = attach(proof, Source(args.appendix, len(paths))) if args.appendix else None
        extract = read(args.extract) if checking else ''
    except OSError as error:
        print('build.py: cannot read %s: %s' % (error.filename, error.strerror))
        return 1
    status = 0
    if not checking and proof.errors:
        for text in report([(0, line, message, 0) for line, message in proof.errors]):
            print(text)
        status = 1
    if args.labels:
        for unit in proof.units:
            if unit.key:
                print(unit.key, unit.label)
    if args.dependents:
        status = max(status, dependents(proof, args.dependents))
    if not checking:
        return status
    failures = run_checks(proof, extract, args.mode, args.max_items, front, appendix)
    for text in failures:
        print(text)
    if failures:
        return 1
    if args.emit:
        output = emit(proof, front, appendix, args.footer)
        try:
            write(args.emit, output)
        except OSError as error:
            print('build.py: cannot write %s: %s' % (args.emit, error.strerror))
            return 1
        print('wrote %s' % args.emit)
    else:
        top = sum(1 for item in proof.items if item.parent is None)
        print('ok: mode %s, %s, %s' % (args.mode, count(top, 'top-level item'),
                                       count(len(proof.tables), 'table')))
    return status


if __name__ == '__main__':
    sys.stdout.reconfigure(errors='backslashreplace')
    sys.exit(main())
