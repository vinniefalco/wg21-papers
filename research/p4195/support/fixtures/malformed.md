## 1. Malformed

1. **Definition.** A session is a meeting. {#d:session}
  1. **Lemma.** Two spaces is not a level. {#l:two-spaces}
1. **Lemma.** This item never gets a key.
A prose line ends it.
1. **Lemma.** The key has capitals. {#l:Bad-Key}
1. **Lemma.** The key ends this line. {#l:closed}
   This line comes after the key.
1. **Lemma.** The citation breaks *[from
   d:session]* across lines. {#l:split}
1. **Lemma.** The citation has an empty key. *[from d:session, ]* {#l:empty}
1. **Lemma.** Citation openers are lowercase. *[From d:session]* *[Proved by l:closed]* {#l:capital}
1. **Lemma.** Citation openers take no extra spaces. *[ from d:session]* *[proved  by l:closed]* {#l:spaced}
A prose line holds a stray marker. {#l:stray}

   1. **Lemma.** No item above holds this one. {#l:no-parent}

*Table: A caption with no key*
*Table: A caption with no table* {#t:lonely}
No row follows it.

1. **Lemma.** The marker has an unknown suffix. {#l:suffix strong}
*Table: A caption keyed like a lemma* {#l:not-a-table}

*Table: A table cut short* {#t:cut}
| Party | Power |
|-------|-------|
| Chair | Decides |
A prose line stands where the citation belongs.

*Table: A table split by a blank line* {#t:gap}
| Party | Power |
|-------|-------|

| Chair | Decides |
*[from d:session]*

1. **Lemma.** This item has not reached its key.
    1. **Lemma.** Four spaces is not a level. {#l:four-spaces}
1. **Lemma.** The top of a deep list. {#l:top}
   1. **Lemma.** The middle of the deep list. {#l:middle}
      1. **Lemma.** This third-level item has not reached its key.
         1. **Lemma.** A fourth level is not a level. {#l:fourth}
1. **Lemma.** A marker {#l:early} sits mid-line. {#l:mid-line}
1. **Lemma.** This item runs over two lines,
   and a marker {#l:early-too} sits on the second. {#l:second-line}

*Table: A caption with a {#t:inner} marker* {#t:marked}
| Party | Power |
|-------|-------|
| Chair {#t:chair} | Decides |
*[from d:session]*

*Table: An unfinished table* {#t:unfinished}
| Party | Power |
|-------|-------|
| Chair | Decides |
