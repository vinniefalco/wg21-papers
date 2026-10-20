## 1. Setting

1. **Definition.** A session is a meeting that one chair runs. {#d:session}
1. **Definition.** A poll is a show of hands taken during a session. *[from d:session]* {#d:poll}
1. **Fact.** "The chair decides whether consensus exists." *[from d:session]* {#f:chair-decides}
1. **Fact.** "A poll records the room's view ... does not bind the chair." *[from d:poll]* {#f:poll-advisory}
In plain terms: the chair makes the call, and a poll only informs it *[from f:chair-decides, f:poll-advisory]*.
1. **Assumption.** Each participant answers a poll question at most once. {#ax:one-answer}
1. **Inference.** A poll result informs the chair but cannot settle the question. *[from f:chair-decides, f:poll-advisory]* {#inf:poll-informs}

*Table: Who holds which power* {#t:powers}

| Party | Power |
|:------|------:|
| Chair | Decides consensus |
| Room | Gives advice |

*[from f:chair-decides, f:poll-advisory]*
1. **Lemma.** The two rows of the table cover every party in a session. *[from t:powers, d:session]* {#l:parties}

## 2. Results

1. **Proposition.** A chair who sets a poll aside still acts within the rules. *[proved by l:rules-allow, l:poll-weak]* {#p:set-aside}
   1. **Lemma.** The rules give the decision to the chair. *[from f:chair-decides]* {#l:rules-allow}
   1. **Lemma.** A poll never binds anyone. *[proved by l:advisory, l:no-compel]* {#l:poll-weak weakened}
      1. **Step.** Polls are advisory. *[from f:poll-advisory]* {#l:advisory}
      1. **Step.** Advice does not compel. *[from l:advisory]* {#l:no-compel}
1. **Observation.** Each question is polled on its own. *[from ax:one-answer]* {#ind:each-question}
1. **Theorem.** No poll result, taken alone, settles a question in a session.

   The proof joins the setting to the results above. *[proved by l:main-informs, l:main-free]* {#thm:main}
   1. **Lemma.** Polls inform the chair, one question at a time. *[from inf:poll-informs, ind:each-question]* {#l:main-informs}
   1. **Lemma.** The chair may act against a poll.
      Every party is covered, so no one else holds the decision. *[proved by l:main-free-step]* {#l:main-free}
      1. **Step.** The chair may set the poll aside. *[from l:parties, p:set-aside]* {#l:main-free-step}
1. **Corollary.** A poll is advice to the chair. *[from thm:main]* {#c:advice}
