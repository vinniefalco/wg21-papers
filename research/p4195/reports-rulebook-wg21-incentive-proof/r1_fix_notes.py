"""One-off: correct word counts in r1-decisions-a.txt after measuring the applied statements."""
from pathlib import Path

p = Path(__file__).resolve().parent / "r1-decisions-a.txt"
t = p.read_text(encoding="utf-8")
fixes = [
    ("second sentence is 47 words|applied in part: 31 words, item kept at two sentences",
     "second sentence is 47 words|applied in part: 33 words, item kept at two sentences"),
    ('|31 words; "turns on" replaced by "marked by"', '|32 words; "turns on" replaced by "marked by"'),
    ("|applied in part (32 words) with 12.1R7", "|applied in part (31 words) with 12.1R7"),
    ("first sentence is 46 words|applied in part: 39 words; the item lists six choices",
     "first sentence is 46 words|applied in part: 38 words; the item lists six choices"),
    ("second sentence is 47 words|applied in part: 37 words", "second sentence is 47 words|applied in part: 39 words"),
    ("l:settled-sg-chair first sentence is 39 words|29 words", "l:settled-sg-chair first sentence is 39 words|30 words"),
    ("l:settled-user second sentence is 33 words|26 words", "l:settled-user second sentence is 33 words|24 words"),
    ("second sentence is 49 words|applied in part: 40 words, every check kept",
     "second sentence is 49 words|applied in part: 46 words, every check kept; a shorter split would drop checks it cites"),
    ("|applied in part: two sentences of about 38 words", "|applied in part: two sentences of 37 and 39 words"),
    ("|applied in part: 43 words with the groups defined at the forwarding poll",
     "|applied in part: 42 words with the groups defined at the forwarding poll"),
    ("first sentence is 48 words|applied in part: 40 words", "first sentence is 48 words|applied in part: 39 words"),
]
for a, b in fixes:
    assert t.count(a) == 1, a
    t = t.replace(a, b)
p.write_text(t, encoding="utf-8", newline="\n")
print("ok, %d notes corrected" % len(fixes))
