# Code review: build.py against build-script-spec

Change reviewed: the untracked `research/p4195/support/` files the spec names (`build.py`, `test_build.py`, `fixtures/`), judged by reading only.

1. `build.py` `render_proof` inserts a blank line at every change of block kind (heading to prose, caption to table rows, table rows to their citation line, list to prose), while the spec asks only for a blank line before a list that follows a table, a caption, or a prose line. `fixtures/expected.md` locks these extra blank lines in, so the emitted proof departs from the spec's layout wherever the source has those adjacencies.

2. `build.py` `Source.__init__` takes a `text` parameter that no caller passes (`main` builds every `Source` from a path and `test_build.py` never constructs one), so the `if text is None` test is always true and the parameter is dead.

3. `build.py` joins lines before matching, in `run_checks` for check 6 and in `forbidden` with `runs` for check 7, so a quote or multi-word phrase can span a line break, but no fixture wraps a Fact quote, a quoted string, or a forbidden phrase across lines. A line-by-line rewrite would still pass `test_check_6_fact_quote_missing_from_extract` and `test_check_7_forbidden_strings` while leaving wrapped Fact quotes unchecked or wrongly paired.

4. `build.py` `run_checks` check 5 treats an item's subtree (`descendants`) as one unit and ignores citations from inside it (`inside`), but `fixtures/fail-5.md` has only one-level subtrees whose sole inside citation is the parent's own `proved by`. Narrowing the exclusion to the item alone, or stopping `descendants` at direct children, would still pass `test_check_5_orphan`, so an uncited parent whose children cite each other, and a parent whose only outside citation lands on a grandchild, are untested.

5. `build.py` `letters` and `roman` are tested only at ordinals 1 and 2 (`test_labels_continue_across_sources` reaches `10b` and `8b.ii`), so the spec's own `c` and `iii`, and every `ROMAN` entry past `i` such as `iv`, have no test that would fail if they broke.

6. `build.py` `write` calls `os.makedirs` on the emit path's parent, creating directories the spec does not mention, and no test emits into a missing directory.
