"""Compute a Step 12 review round's scope: keys changed since a snapshot, their dependents, and refilled chapters whole.

Usage: scope_next_round.py <before-snapshot-tag> <out-file> [refilled-chapter-file ...]

Compares item text in the foundation and chapter files of the snapshot with the current scratch files,
runs build.py --dependents over the current foundation and chapters, and writes the scope keys one per line.
"""
import re
import subprocess
import sys
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent
SUPPORT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support")
PYTHON = Path(r"c:\Users\Vinnie\cursor\wg21-paperworks\.venv\Scripts\python.exe")
FILES = ["01-foundation.md"] + ["ch-%02d.md" % n for n in range(2, 13)]
KEY_LINE = re.compile(r"\{#([a-z]+:[^} ]+)( weakened)?\}\s*$")


def items(directory):
    """Map each key to its item text, attributing table rows to the table they follow."""
    found = {}
    for name in FILES:
        path = directory / name
        if not path.exists():
            continue
        buffer, table_key, in_table = [], None, False
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("|") and table_key:
                found[table_key] += "\n" + stripped
                in_table = True
                continue
            if in_table and stripped.startswith("*[") and table_key:
                found[table_key] += "\n" + stripped
                in_table = False
                continue
            in_table = False
            match = KEY_LINE.search(stripped)
            if match:
                key = match.group(1)
                found[key] = "\n".join(buffer + [stripped])
                buffer = []
                table_key = key if key.startswith("t:") else None
            elif stripped.startswith("#"):
                buffer = []
            elif stripped:
                buffer.append(stripped)
    return found


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    before = items(SCRATCH / "snapshots" / sys.argv[1])
    now = items(SCRATCH)
    out = Path(sys.argv[2])
    if not out.is_absolute():
        out = SCRATCH / out
    changed = sorted(key for key, text in now.items() if before.get(key) != text)
    removed = sorted(key for key in before if key not in now)
    result = subprocess.run(
        [str(PYTHON), str(SUPPORT / "build.py"), "--mode", "full", "--extract", str(SUPPORT / "rules-extract.md"),
         "--dependents", ",".join(changed)] + [str(SCRATCH / name) for name in FILES],
        capture_output=True, text=True, env={"PYTHONDONTWRITEBYTECODE": "1", "SYSTEMROOT": r"C:\Windows"})
    dependents = sorted({line.split()[0] for line in result.stdout.splitlines()
                         if line.strip() and re.match(r"^[a-z]+:", line.split()[0])})
    refilled = set()
    for name in sys.argv[3:]:
        refilled |= set(items_in_file(SCRATCH / name))
    scope = sorted(set(changed) | set(dependents) | refilled)
    out.write_text("\n".join(scope) + "\n", encoding="utf-8")
    print("keys now %d; changed or new %d; removed %d; dependents %d; refilled-chapter keys %d; scope %d (%.0f%%)" % (
        len(now), len(changed), len(removed), len(dependents), len(refilled), len(scope), 100.0 * len(scope) / len(now)))
    unchanged_out = sorted(set(now) - set(scope))
    print("outside scope (%d): %s" % (len(unchanged_out), ", ".join(unchanged_out)))
    if result.returncode:
        print("build.py --dependents exit %d: %s" % (result.returncode, result.stdout[-500:] + result.stderr[-500:]))
    return 0


def items_in_file(path):
    return [KEY_LINE.search(line.strip()).group(1) for line in path.read_text(encoding="utf-8").splitlines()
            if KEY_LINE.search(line.strip())]


if __name__ == "__main__":
    sys.exit(main())
