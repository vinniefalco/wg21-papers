# Who decides in a session

This note shows that a poll informs the chair but never settles a question on its own *[from 10]*. The deciding step is *[from 10b.i]*.

## 1. Setting

1. **Definition.** A session is a meeting that one chair runs.
2. **Definition.** A poll is a show of hands taken during a session. *[from 1]*
3. **Fact.** "The chair decides whether consensus exists." *[from 1]*
4. **Fact.** "A poll records the room's view ... does not bind the chair." *[from 2]*

In plain terms: the chair makes the call, and a poll only informs it *[from 3, 4]*.

5. **Assumption.** Each participant answers a poll question at most once.
6. **Inference.** A poll result informs the chair but cannot settle the question. *[from 3, 4]*

*Table 1. Who holds which power*

| Party | Power |
|:------|------:|
| Chair | Decides consensus |
| Room | Gives advice |

*[from 3, 4]*

7. **Lemma.** The two rows of the table cover every party in a session. *[from Table 1, 1]*

## 2. Results

8. **Proposition.** A chair who sets a poll aside still acts within the rules. *[proved by 8a, 8b]*
   1. **Lemma.** The rules give the decision to the chair. *[from 3]*
   1. **Lemma.** A poll never binds anyone. *[proved by 8b.i, 8b.ii]*
      1. **Step.** Polls are advisory. *[from 4]*
      1. **Step.** Advice does not compel. *[from 8b.i]*
9. **Observation.** Each question is polled on its own. *[from 5]*
10. **Theorem.** No poll result, taken alone, settles a question in a session.

    The proof joins the setting to the results above. *[proved by 10a, 10b]*
    1. **Lemma.** Polls inform the chair, one question at a time. *[from 6, 9]*
    1. **Lemma.** The chair may act against a poll.
       Every party is covered, so no one else holds the decision. *[proved by 10b.i]*
       1. **Step.** The chair may set the poll aside. *[from 7, 8]*
11. **Corollary.** A poll is advice to the chair. *[from 10]*
12. **Remark.** A chair may weigh one poll against another. *[from 11]*

## 3. Outcomes

Each poll ends in one of two results.

*Table 2. What each poll result tells the chair*

| Result | Tells the chair |
|--------|-----------------|
| For | The room leans toward the change |
| Against | The room leans away from the change |

*[from 11]*

13. **Lemma.** Either result leaves the decision with the chair. *[from Table 2, 10]*
14. **Corollary.** The chair decides after every poll. *[from 13]*

## Sources

- SD-4, WG21 practices and procedures, revised in 2026.
- The party table is *[from Table 1]*.

*2026-10-18 build.py fixture*
