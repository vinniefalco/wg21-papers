# Code review: build.py against build-script-spec

1. **Beyond the spec.** `build.py` `render_proof` uses `BLOCKS` to insert a blank line at every change of block type (heading to prose, caption to rows, last row to the table's citation line, list to prose), but the spec asks only for a blank line before a list that follows a table, a caption, or a prose line, and says emit copies prose lines unchanged. `fixtures/expected.md` locks in the extra blanks. Some of them are what stop markdown from folding a table's citation line into the table and a recap into the item above it.

2. **Beyond the spec.** `build.py` `main` prints `ok: mode M, N top-level items, N tables` after a clean check and `wrote PATH` after emit, while the spec defines check output only as one line per failure. `test_build.py` `test_check_token_is_not_a_source` locks in the ok line.

3. **Untested.** `build.py` `parse` lets blank lines sit between a table caption and its rows and between the rows and the citation line, and rejects rows that follow such a blank (`table_state` `'after'`); the spec's table format describes none of this. No fixture puts a blank line inside a table, so these transitions could break without a test failing.

4. **Untested.** `test_build.py` `test_check_7_forbidden_strings` never uses nine of the nineteen forbidden words (perverse, railroad, steamroll, exploit, retaliate, outsider, cliff, obviously, door), and the only years it tests are 2025 and 2026. Dropping or misspelling one of those words in `build.py` `WORDS`, or changing `YEAR_RE` so it misses 1990 to 1999 or flags years outside 1990 to 2099, would still pass.

5. **Swallowed error.** `build.py` `parse` reports a `1.` marker at an indent other than 0, 3, or 6 only when no item is open. If the item above has not reached its key yet and the marker sits at or past that item's content column (a nested item indented 4 spaces, or a fourth level at 9), the line is read as a continuation: the stray item merges into the open item, can supply its key, and neither the bad-indent nor the missing-key error appears. Emit then writes it as a nested list item with no label of its own, and no fixture covers the case.

6. **Swallowed error.** `build.py` `parse` flags a stray `{#...}` marker only on prose and heading lines; one inside a table row, or mid-line in an item before its closing key, is neither reported nor removed, because `render` strips only the closing marker at the end of an item's last line. The spec's emit rule says to strip the markers, so such a marker would reach the emitted file.

7. **Dead code.** `build.py` `cycle_path` ends with `return [start]`, which cannot run: `run_checks` only calls it on a strongly connected component that holds a cycle, so the breadth-first search always finds an edge back to `start` first.
