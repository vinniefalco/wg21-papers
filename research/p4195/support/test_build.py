import contextlib
import errno
import io
import os
import tempfile
import unittest

import build

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURES = os.path.join(HERE, 'fixtures')
EXTRACT = os.path.join(FIXTURES, 'extract.md')


def fixture(name):
    return os.path.join(FIXTURES, name)


def write_source(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def run(*args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = build.main(['--extract', EXTRACT, *args])
    return code, out.getvalue().splitlines()


def format_errors(path):
    return [
        f'{path}:4: format: list marker indented 2 spaces; use 0, 3, or 6',
        f'{path}:5: format: item does not end with {{#KEY}}',
        f'{path}:7: format: malformed key marker {{#l:Bad-Key}}',
        f'{path}:9: format: indented line after an item ends; the key must end the last line of its item',
        f'{path}:10: format: citation must open and close on one line',
        f'{path}:12: format: citation has an empty key',
        f'{path}:13: format: malformed citation opener *[From; use *[from or *[proved by',
        f'{path}:13: format: malformed citation opener *[Proved by; use *[from or *[proved by',
        f'{path}:14: format: malformed citation opener *[ from; use *[from or *[proved by',
        f'{path}:14: format: malformed citation opener *[proved  by; use *[from or *[proved by',
        f'{path}:15: format: key marker outside an item',
        f'{path}:17: format: nested item has no parent item above it',
        f'{path}:19: format: malformed table caption; use *Table: TEXT* {{#t:KEY}}',
        f'{path}:20: format: table caption is not followed by a table',
        f'{path}:23: format: malformed key marker {{#l:suffix strong}}',
        f'{path}:24: format: malformed table caption; use *Table: TEXT* {{#t:KEY}}',
        f'{path}:24: format: key marker outside an item',
        f'{path}:30: format: table must end with a line holding only a *[from ...]* citation',
        f'{path}:36: format: table must end with a line holding only a *[from ...]* citation',
        f'{path}:39: format: item does not end with {{#KEY}}',
        f'{path}:40: format: list marker indented 4 spaces; use 0, 3, or 6',
        f'{path}:43: format: item does not end with {{#KEY}}',
        f'{path}:44: format: list marker indented 9 spaces; use 0, 3, or 6',
        f'{path}:45: format: stray key marker; the key must end the last line of its item',
        f'{path}:47: format: stray key marker; the key must end the last line of its item',
        f'{path}:49: format: stray key marker; the key must end the caption line',
        f'{path}:52: format: stray key marker; the key must end the caption line',
        f'{path}:55: format: table must end with a line holding only a *[from ...]* citation',
    ]


class BuildTests(unittest.TestCase):

    def assertFailures(self, args, expected):
        code, lines = run(*args)
        self.assertEqual(lines, expected)
        self.assertEqual(code, 1)

    def assertPasses(self, args):
        code, lines = run(*args)
        self.assertEqual(code, 0, lines)

    def test_format_errors(self):
        path = fixture('malformed.md')
        self.assertFailures(['--mode', 'foundation', path], format_errors(path))
        with tempfile.TemporaryDirectory() as tmp:
            caption = os.path.join(tmp, 'caption.md')
            item = os.path.join(tmp, 'item.md')
            write_source(caption, '*Table: A caption at the end of the file* {#t:last}\n')
            write_source(item, '1. **Lemma.** This item reaches the end of the file.\n')
            self.assertFailures(['--mode', 'foundation', caption, item], [
                f'{caption}:1: format: table caption is not followed by a table',
                f'{item}:1: format: item does not end with {{#KEY}}',
            ])
            front = os.path.join(tmp, 'front.md')
            target = os.path.join(tmp, 'proof.md')
            write_source(front, 'This note rests on *[From thm:main]*.\n')
            self.assertFailures(['--front', front, '--emit', target, fixture('proof.md')], [
                f'{front}:1: format: malformed citation opener *[From; use *[from or *[proved by',
            ])
            self.assertFalse(os.path.exists(target))

    def test_format_errors_fail_labels_and_dependents(self):
        path = fixture('malformed.md')
        errors = format_errors(path)
        for option in (['--labels'], ['--dependents', 'd:session']):
            code, lines = run(*option, path)
            self.assertEqual(lines[:len(errors)], errors)
            self.assertEqual(code, 1)

    def test_unreadable_source(self):
        path = fixture('missing.md')
        self.assertEqual(run(path), (1, [f'build.py: cannot read {path}: {os.strerror(errno.ENOENT)}']))

    def test_check_1_key_cited_but_undefined_or_defined_twice(self):
        path = fixture('fail-1.md')
        front = fixture('fail-1-front.md')
        appendix = fixture('fail-1-appendix.md')
        self.assertFailures(['--front', front, '--appendix', appendix, path], [
            f'{front}:3: check 1: d:front-only is cited but not defined',
            f'{path}:4: check 1: d:session is defined twice, first at {path}:3',
            f'{path}:5: check 1: d:missing is cited but not defined',
            f'{path}:6: check 1: d:unwritten is cited but not defined',
            f'{appendix}:3: check 1: d:appendix-only is cited but not defined',
        ])

    def test_check_2_from_citation_names_later_item(self):
        path = fixture('fail-2.md')
        self.assertFailures([path], [
            f'{path}:3: check 2: d:chair cites d:session with from, but d:session is not earlier',
            f'{path}:4: check 2: prose line cites d:session with from, but d:session is not earlier',
        ])

    def test_check_3_proved_by_names_non_child(self):
        path = fixture('fail-3.md')
        self.assertFailures([path], [
            f'{path}:4: check 3: thm:no-bind cites l:advisory with proved by, but l:advisory is not its child',
            f'{path}:5: check 3: prose line cites l:advisory with proved by, but l:advisory is not its child',
        ])

    def test_check_4_citation_cycle(self):
        path = fixture('fail-4.md')
        self.assertFailures([path], [
            f'{path}:5: check 2: l:self cites l:self with from, but l:self is not earlier',
            f'{path}:3: check 4: citation cycle p:decide -> l:step -> p:decide',
            f'{path}:5: check 4: citation cycle l:self -> l:self',
        ])

    def test_check_5_orphan(self):
        path = fixture('fail-5.md')
        extras = ['--front', fixture('fail-5-front.md'), '--appendix', fixture('fail-5-appendix.md')]
        expected = [
            f'{path}:4: check 5: l:unused is an orphan',
            f'{path}:5: check 5: p:unused-parent is an orphan',
            f'{path}:9: check 5: p:sibling-parent is an orphan',
        ]
        self.assertFailures([*extras, path], expected)
        self.assertFailures(['--mode', 'spine', *extras, path], expected)
        self.assertPasses(['--mode', 'foundation', *extras, path])

    def test_check_6_fact_quote_missing_from_extract(self):
        path = fixture('fail-6.md')
        self.assertFailures([path], [
            f'{path}:4: check 6: f:misquote quotes text missing from the extract: "binds the chair."',
            f'{path}:5: check 6: f:ellipsis quotes text missing from the extract: '
            '"The chair decides \u2026 consensus exists."',
            f'{path}:7: check 6: f:wrapped quotes text missing from the extract: "a poll binds the chair."',
        ])

    def test_check_7_forbidden_strings(self):
        path = fixture('fail-7.md')
        front = fixture('fail-7-front.md')
        appendix = fixture('fail-7-appendix.md')
        self.assertFailures(['--front', front, '--appendix', appendix, path], [
            f'{front}:3: check 7: forbidden "2026"',
            f'{front}:4: check 7: forbidden "of course"',
            f'{path}:5: check 7: forbidden "Captured"',
            f'{path}:5: check 7: forbidden "of course"',
            f'{path}:6: check 7: forbidden "P1234"',
            f'{path}:6: check 7: forbidden "--"',
            f'{path}:6: check 7: forbidden "C++26"',
            f'{path}:6: check 7: forbidden "2025"',
            f'{path}:7: check 7: forbidden "gamed"',
            f'{path}:8: check 7: forbidden "carry"',
            f'{path}:9: check 7: forbidden "clearly"',
            f'{path}:11: check 7: forbidden "dominates"',
            f'{path}:14: check 7: forbidden "Insiders"',
            f'{path}:17: check 7: forbidden "carry"',
            f'{path}:18: check 7: forbidden "punishes"',
            f'{path}:18: check 7: forbidden "stacked the room"',
            f'{path}:18: check 7: forbidden "carried"',
            f'{path}:19: check 7: forbidden "lock-ins"',
            f'{path}:19: check 7: forbidden "locked-in"',
            f'{path}:21: check 7: forbidden "perverse"',
            f'{path}:21: check 7: forbidden "railroad"',
            f'{path}:21: check 7: forbidden "steamroll"',
            f'{path}:21: check 7: forbidden "exploit"',
            f'{path}:22: check 7: forbidden "retaliate"',
            f'{path}:22: check 7: forbidden "outsider"',
            f'{path}:22: check 7: forbidden "cliff"',
            f'{path}:23: check 7: forbidden "obviously"',
            f'{path}:23: check 7: forbidden "door"',
            f'{path}:24: check 7: forbidden "1990"',
            f'{path}:24: check 7: forbidden "1999"',
            f'{path}:24: check 7: forbidden "2099"',
            f'{path}:25: check 7: forbidden "stack the room"',
            f'{path}:28: check 7: forbidden "exploits"',
            f'{path}:30: check 7: forbidden "stack the room"',
            f'{appendix}:4: check 7: forbidden "insiders"',
        ])
        with tempfile.TemporaryDirectory() as tmp:
            dash = os.path.join(tmp, 'dash.md')
            write_source(dash, '1. **Theorem.** One member, one vote \u2014 always. {#thm:dash}\n')
            self.assertFailures([dash], [f'{dash}:1: check 7: forbidden em dash'])

    def test_check_8_too_many_top_level_items(self):
        path = fixture('proof.md')
        expected = ['check 8: 11 top-level items, more than --max-items 10']
        self.assertFailures(['--max-items', '10', path], expected)
        self.assertFailures(['--mode', 'spine', '--max-items', '10', path], expected)
        self.assertPasses(['--max-items', '11', path])
        self.assertPasses(['--mode', 'foundation', '--max-items', '10', path])
        with tempfile.TemporaryDirectory() as tmp:
            many = os.path.join(tmp, 'many.md')
            items = ['1. **Remark.** A remark. {#m:r%d}\n' % n for n in range(1, 152)]
            write_source(many, ''.join(items))
            self.assertFailures([many], ['check 8: 151 top-level items, more than --max-items 150'])
            write_source(many, ''.join(items[:150]))
            self.assertPasses([many])

    def test_emit_matches_expected_file(self):
        options = [
            '--front', fixture('front.md'),
            '--appendix', fixture('appendix.md'),
            '--footer', '2026-10-18 build.py fixture',
        ]
        sources = [fixture('proof.md'), fixture('proof-2.md')]
        with tempfile.TemporaryDirectory() as tmp:
            target = os.path.join(tmp, 'proof.md')
            code, _ = run(*options, '--max-items', '10', '--emit', target, *sources)
            self.assertEqual(code, 1)
            self.assertFalse(os.path.exists(target))
            self.assertPasses([*options, '--emit', target, *sources])
            with open(target, encoding='utf-8', newline='') as f:
                actual = f.read()
        with open(fixture('expected.md'), encoding='utf-8') as f:
            expected = f.read()
        self.assertEqual(actual, expected)

    def test_emit_into_missing_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = os.path.join(tmp, 'missing')
            target = os.path.join(folder, 'proof.md')
            self.assertEqual(run('--emit', target, fixture('proof.md')),
                             (1, [f'build.py: cannot write {target}: {os.strerror(errno.ENOENT)}']))
            self.assertFalse(os.path.exists(folder))

    def test_labels_continue_across_sources(self):
        code, lines = run('--labels', fixture('proof.md'), fixture('proof-2.md'))
        self.assertEqual(lines, [
            'd:session 1',
            'd:poll 2',
            'f:chair-decides 3',
            'f:poll-advisory 4',
            'ax:one-answer 5',
            'inf:poll-informs 6',
            't:powers Table 1',
            'l:parties 7',
            'p:set-aside 8',
            'l:rules-allow 8a',
            'l:poll-weak 8b',
            'l:advisory 8b.i',
            'l:no-compel 8b.ii',
            'ind:each-question 9',
            'thm:main 10',
            'l:main-informs 10a',
            'l:main-free 10b',
            'l:main-free-step 10b.i',
            'c:advice 11',
            'm:weigh 12',
            't:outcomes Table 2',
            'l:either 13',
            'c:every-poll 14',
        ])
        self.assertEqual(code, 0)

    def test_letters_and_roman_numerals(self):
        self.assertEqual([build.letters(n) for n in (1, 2, 3, 26, 27, 52, 53, 702, 703)],
                         ['a', 'b', 'c', 'z', 'aa', 'az', 'ba', 'zz', 'aaa'])
        numerals = {
            1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 14: 'xiv',
            40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
            1000: 'm', 1994: 'mcmxciv', 3888: 'mmmdccclxxxviii',
        }
        self.assertEqual({n: build.roman(n) for n in numerals}, numerals)
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, 'labels.md')
            steps = ('one', 'two', 'three', 'four')
            write_source(path, ''.join([
                '1. **Proposition.** A claim in three parts. {#p:parts}\n',
                '   1. **Lemma.** The first part. {#l:first}\n',
                '   1. **Lemma.** The second part. {#l:second}\n',
                '   1. **Lemma.** The third part. {#l:third}\n',
                *('      1. **Step.** Step %s. {#l:%s}\n' % (step, step) for step in steps),
            ]))
            self.assertEqual(run('--labels', path), (0, [
                'p:parts 1', 'l:first 1a', 'l:second 1b', 'l:third 1c',
                'l:one 1c.i', 'l:two 1c.ii', 'l:three 1c.iii', 'l:four 1c.iv',
            ]))

    def test_dependents_follow_citations_transitively(self):
        path = fixture('proof.md')
        code, lines = run('--dependents', 'l:parties,ax:one-answer', path)
        self.assertEqual(lines, [
            'ind:each-question 9',
            'thm:main 10',
            'l:main-informs 10a',
            'l:main-free 10b',
            'l:main-free-step 10b.i',
            'c:advice 11',
        ])
        self.assertEqual(code, 0)
        self.assertEqual(run('--dependents', 'd:absent', path), (1, ['d:absent is not defined']))

    def test_check_token_is_not_a_source(self):
        expected = (0, ['ok: mode spine, 11 top-level items, 1 table'])
        self.assertEqual(run('check', '--mode', 'spine', fixture('proof.md')), expected)
        self.assertEqual(run('check'), (2, ['build.py: no SOURCE files given']))
        with tempfile.TemporaryDirectory() as tmp, contextlib.chdir(tmp):
            write_source('check', '1. **Lemma.** A file named check is not a source. {#l:stray}\n')
            self.assertEqual(run('check', '--mode', 'spine', fixture('proof.md')), expected)


if __name__ == '__main__':
    unittest.main()
