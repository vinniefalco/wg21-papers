# Code review: build-script-spec

Reviewed the uncommitted change in `research/p4195/support/` (all untracked, `git diff` empty): `build.py`, `test_build.py`, and every file in `fixtures/`, judged by reading only. Six findings.

1. `build.py` `render` returns prose and heading lines without `relabel`, so a citation in an `In plain terms:` recap is emitted with its raw key; the spec says emit copies prose lines unchanged but also says to replace each cited key with its label, and `run_checks` already treats these as citations under check 1. Lines from `--front` and `--appendix` are relabeled, so the two kinds of prose disagree. No emit fixture has a prose-line citation, so neither reading is pinned by a test.

2. `build.py` `render_proof` (through `BLOCKS`) inserts a blank line at every change of block kind and at each source-file boundary (caption to rows, rows to the closing citation, list to prose, heading to prose, and between items 11 and 12 in `fixtures/expected.md`), but the spec asks only for a blank line before a list that follows a table, a caption, or a prose line. The file-boundary break can turn a tight list that spans two source files into a loose one. The heading-to-prose break has no fixture, so it is also untested.

3. `build.py` `parse` and `close` have error branches that no test reaches: a table whose rows are followed mid-file by a line that is neither a row nor its citation (`fixtures/malformed.md` only ends a table at end of file), a bare caption or an unclosed item at end of file, a caption key that lacks the `t:` prefix, and a key marker with a suffix other than `weakened`. Removing any of these checks would leave every test passing, so a table missing its citation in the middle of a real source could regress silently.

4. `build.py` `main` drops a leading `check` positional only when no file named `check` exists in the working directory, a filesystem-dependent parsing rule the spec does not state. The branch that keeps such a file as a source has no test, and `test_build.py` `test_check_token_is_not_a_source` passes only when the runner's working directory has no file named `check`.

5. `build.py` `main` has two reporting paths with no test: the `OSError` handler that prints `cannot read` and returns 1, and the block that prints format errors and returns 1 under `--labels` or `--dependents` without `--emit`. Removing the second would let `--labels` and `--dependents` exit 0 on malformed sources with every test still passing.

6. `build.py` `parse_args` sets the `--max-items` default to 150 as the spec requires, but no test would fail if it changed, because `test_check_8_too_many_top_level_items` always passes an explicit value and the runs that use the default hold at most 14 top-level items. Any default of 14 or more would leave the suite green.
