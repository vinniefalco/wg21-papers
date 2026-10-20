# Code review: build-script-spec

Reviewed the uncommitted change in `research/p4195/support/` (all untracked, `git diff` empty): `build.py`, `test_build.py`, and every file in `fixtures/`, judged by reading only. Three findings. The extra blank lines `render_proof` adds at block changes other than before a list are still not in the spec, but the round 2 fix kept them on purpose for markdown parsing, so they are not raised again.

1. `build.py` `run_checks` runs checks 2 and 3 only over item and table citations, so prose-line citations collected in `Source.cites` reach check 1 alone. An `In plain terms:` recap whose `from` citation names a later item therefore passes, though the spec's check 2 covers every `from` citation with no exception for prose lines, and no fixture has a prose line that cites forward.

2. `test_build.py` `test_check_7_forbidden_strings` only reaches forms from the -e and -ing branches of `build.py` `inflections` plus plain plurals, so the consonant-y (carried), -sh (punished), hyphenated (locked-in), and multi-word (stacked the room) forms built by `inflections` and `forms` have no case. It also has no negative case such as recaptured, so the whole-word lookarounds in `word_pattern` could be dropped with every test still passing.

3. `build.py` `citations` and `CITE_OPEN_RE` recognize only the exact lowercase openers `*[from` and `*[proved by`, so a near-miss such as `*[From d:session]*` or `*[Proved by l:x]*` is silently treated as plain text. It raises no format error, is ignored by checks 1 through 5, and `emit` copies the raw key into the published proof.
