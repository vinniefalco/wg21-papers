"""Snapshots of the run's working files, so any step can be redone from its saved state.

Usage:
  snapshot.py take TAG [NOTE]               copy every working file into snapshots/TAG
  snapshot.py adopt TAG NOTE NAME=PATH ...  save files kept elsewhere as snapshot TAG, under their working names
  snapshot.py restore TAG                   snapshot the current state, then copy TAG's files back
  snapshot.py list                          list snapshots and their notes

A snapshot is never overwritten or deleted. Restore never deletes a working file; it lists
working files that are absent from the snapshot so they can be moved to cabinet/_trash by hand.
"""
import hashlib
import shutil
import sys
from datetime import datetime
from pathlib import Path

SCRATCH = Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof")
SUPPORT = Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support")
PLAN = Path(r"c:\Users\Vinnie\.cursor\plans\wg21_incentive_model_96468661.plan.md")
SNAPSHOTS = SCRATCH / "snapshots"

FIXED = {
    "01-foundation.md": SCRATCH / "01-foundation.md",
    "02-spine.md": SCRATCH / "02-spine.md",
    "02-incentive-map.md": SCRATCH / "02-incentive-map.md",
    "ledger.md": SCRATCH / "ledger.md",
    "adversarial-log-draft.md": SCRATCH / "adversarial-log-draft.md",
    "check_modules.py": SCRATCH / "check_modules.py",
    "foundation-labeled.md": SCRATCH / "foundation-labeled.md",
    "spine-labeled.md": SCRATCH / "spine-labeled.md",
    "rules-extract.md": SUPPORT / "rules-extract.md",
    "kit.md": SUPPORT / "kit.md",
    "triage.md": SUPPORT / "triage.md",
    "build.py": SUPPORT / "build.py",
    "plan.md": PLAN,
}
GLOBS = ("ch-*.md", "review-*.md", "fix-*.md")


def working_files():
    files = {name: path for name, path in FIXED.items() if path.exists()}
    for pattern in GLOBS:
        for path in sorted(SCRATCH.glob(pattern)):
            files[path.name] = path
    return files


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_snapshot(tag, note, entries):
    target = SNAPSHOTS / tag
    if target.exists():
        sys.exit("snapshot exists and is never overwritten: " + tag)
    target.mkdir(parents=True)
    rows = []
    for name, (source, original) in sorted(entries.items()):
        shutil.copy2(source, target / name)
        rows.append("%s\t%d\t%s\t%s" % (name, source.stat().st_size, digest(source), original))
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = ["tag: " + tag, "taken: " + stamp, "note: " + note, ""]
    (target / "MANIFEST.txt").write_text("\n".join(header + rows) + "\n", encoding="utf-8", newline="\n")
    print("snapshot %s: %d files" % (tag, len(rows)))


def take(tag, note):
    write_snapshot(tag, note, {name: (path, path) for name, path in working_files().items()})


def adopt(tag, note, pairs):
    current = working_files()
    entries = {}
    for pair in pairs:
        name, source = pair.split("=", 1)
        source = Path(source)
        if not source.exists():
            sys.exit("missing source: %s" % source)
        original = FIXED.get(name) or current.get(name) or SCRATCH / name
        entries[name] = (source, original)
    write_snapshot(tag, note, entries)


def restore(tag):
    target = SNAPSHOTS / tag
    manifest = target / "MANIFEST.txt"
    if not manifest.exists():
        sys.exit("no such snapshot: " + tag)
    take("auto-before-restore-%s-%s" % (tag, datetime.now().strftime("%Y%m%d-%H%M%S")),
         "automatic snapshot taken before restoring " + tag)
    restored = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")
        if len(parts) != 4:
            continue
        name, _, sha, original = parts
        source = target / name
        if digest(source) != sha:
            sys.exit("snapshot file changed since it was taken: " + name)
        shutil.copy2(source, Path(original))
        restored.add(Path(original))
        print("restored " + original)
    extra = [str(path) for path in working_files().values() if path not in restored]
    for path in extra:
        print("not in snapshot, left in place: " + path)


def list_snapshots():
    if not SNAPSHOTS.exists():
        return
    for manifest in sorted(SNAPSHOTS.glob("*/MANIFEST.txt")):
        head = manifest.read_text(encoding="utf-8").splitlines()[:3]
        print(" | ".join(head))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    command = sys.argv[1]
    if command == "take" and len(sys.argv) >= 3:
        take(sys.argv[2], " ".join(sys.argv[3:]))
    elif command == "adopt" and len(sys.argv) >= 5:
        adopt(sys.argv[2], sys.argv[3], sys.argv[4:])
    elif command == "restore" and len(sys.argv) == 3:
        restore(sys.argv[2])
    elif command == "list":
        list_snapshots()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
