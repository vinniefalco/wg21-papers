"""Rename the proposal size "enormous" to "large", fixing the article, without changing any line count."""
from pathlib import Path

FILES = [
    Path(r"c:\Users\Vinnie\.cursor\plans\wg21_incentive_model_96468661.plan.md"),
    Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof\01-foundation.md"),
    Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof\triage-decisions.txt"),
    Path(r"c:\Users\Vinnie\cursor\cabinet\_scratch\reports-rulebook-wg21-incentive-proof\ledger.md"),
    Path(r"c:\Users\Vinnie\cursor\wg21-papers\research\p4195\support\triage.md"),
]
PAIRS = [("an enormous", "a large"), ("An enormous", "A large"), ("enormous", "large"), ("Enormous", "Large")]

for path in FILES:
    data = path.read_bytes()
    text = data.decode("utf-8")
    before = text.count("\n")
    hits = sum(text.count(old) for old, _ in PAIRS[2:])
    for old, new in PAIRS:
        text = text.replace(old, new)
    if text.count("\n") != before:
        raise SystemExit(f"FAIL: line count changed in {path}")
    path.write_bytes(text.encode("utf-8"))
    print(f"{hits:3} replaced  {path.name}")
