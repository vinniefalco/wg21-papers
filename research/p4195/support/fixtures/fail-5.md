## 1. Orphans

1. **Definition.** A session is a meeting. {#d:session}
1. **Lemma.** Sessions have chairs. {#l:unused}
1. **Proposition.** Every session keeps a record. *[proved by l:record]* {#p:unused-parent}
   1. **Lemma.** The chair keeps the record. *[from d:session]* {#l:record}
1. **Proposition.** Polls are recorded too. {#p:parent}
   1. **Lemma.** Each poll is written down. *[from d:session]* {#l:poll-written}
1. **Proposition.** Every chair keeps order. *[proved by l:order-rule, l:order-kept]* {#p:sibling-parent}
   1. **Lemma.** The rules call for order. *[from d:session]* {#l:order-rule}
   1. **Lemma.** Order is kept because the rules call for it. *[from l:order-rule]* {#l:order-kept}
1. **Proposition.** Every poll is counted. *[proved by l:count]* {#p:grand-parent}
   1. **Lemma.** The chair counts each poll. *[proved by l:tally]* {#l:count}
      1. **Step.** Each count is a tally. *[from d:session]* {#l:tally}
1. **Theorem.** Sessions exist. *[from d:session, l:poll-written, l:tally]* {#thm:exists}
1. **Remark.** Nothing cites this remark. *[from d:session]* {#m:uncited}
In plain terms: sessions have chairs *[from l:unused]*.

*Table: Nothing cites this table* {#t:uncited}
| Party | Keeps |
|-------|-------|
| Chair | The record |
*[from d:session]*
