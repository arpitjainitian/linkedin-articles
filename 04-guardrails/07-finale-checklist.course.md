# Lesson 4.7: The guardrails checklist (course companion)

*Module 4: Guardrails. Not for LinkedIn.*

## Learning objective

After this lesson, you can run the seven-line guardrails checklist on an AI project and turn each gap into a named owner and a next action.

## The story

Read the article: [07-finale-checklist.md](07-finale-checklist.md). Running example: an online electronics store's refund assistant, now with all five layers in place, and a checklist to test whether the fence really holds.

## Deep dive

Six lessons built one fence in layers. This lesson turns them into a checklist you can run on any AI project, and it explains how to use the checklist without fooling yourself.

**Why a checklist.** A checklist turns a set of principles into yes-or-no questions. Each line points to one lesson:

1. **Rules in code or fixed checks, not only in the prompt** (lesson 1). A prompt is a request. A check you can test is a rule.
2. **Questions screened before the model, blocks logged** (lesson 2). The bouncer at the door, with a record.
3. **Answers checked before the customer, including hints** (lesson 3). The final check, with a safe fallback.
4. **Attacks tested through every input** (lesson 4). Chat, documents, notes and tools, with an attack list that runs again after changes.
5. **Staff exceptions with login, expiry and a reviewed log** (lesson 5). A proper door for the fire brigade.
6. **Missed harm and false refusals measured per topic** (lesson 6). Two numbers, not one.
7. **One named owner, and the test set re-run after every change.** The fence needs a keeper.

**How to score it.** For each line, answer yes, partly or no, and write one piece of evidence: a test result, a log extract, a named role or a document. A "yes" with no evidence is a "partly". Teams often find that most lines are "partly" on the first pass, and that is useful information, not a failure.

**Turning gaps into work.** A "no" becomes a card with an owner, a due date and a test that proves it is fixed. The test matters: a fix that nobody can test is a hope, as lesson 4 showed.

**Common ways to fool yourself.** Three traps:

- **Checking the prompt and calling it done.** Line 1 is the most common false yes.
- **Testing only the chat box.** Line 4 fails for almost every first-time team, because the notes and documents were never on the list.
- **Measuring harm only.** Line 6 looks fine until someone counts the customers who left.

**The finale in practice.** Run one hour of red teaming with people who did not build the assistant, using the attack list from lesson 4. Then run the checklist with a second person, so one person's blind spot does not decide the score.

**Limits.** No checklist makes an AI safe for good. New products bring new doors, and topics change. The checklist shows where the fence has holes today. Keep it short, run it on a schedule, and update it when something surprises you.

## Hands-on lab

1. Copy the seven lines into a table with columns: line, yes or partly or no, evidence, owner.
2. Score a real or imagined assistant. Write evidence for each line.
3. Choose the two weakest lines. For each, write one action, one owner, and one test that proves it is fixed.
4. Ask a second person to score the same assistant. List the lines where your scores differ, and discuss why.

## Quiz

1. Why does the checklist ask for evidence on every line? *Because a yes without evidence is often a hope, and the evidence keeps the score honest.*
2. Which line do most first-time teams fail, and why? *Line 4, testing every input, because the notes and documents are often forgotten.*
3. What is the purpose of a second scorer? *To catch blind spots that the builder cannot see in their own work.*
4. Why is a fix without a test a weak fix? *Because nobody can prove it works, and it can quietly break again after the next change.*

## Checklist line

- [ ] The guardrails checklist has been scored with evidence, by two people, and each gap has an owner and a test.

## Glossary

- **Checklist:** a list of yes-or-no questions, each tied to evidence.
- **Evidence:** a test result, log extract, named role or document that supports an answer.
- **Owner:** the named person responsible for a gap until it is closed.
- **Regression test:** a test that runs again after every change, to catch old failures returning.

## Further reading

- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). A structured way to govern and measure AI risk over time.
- OWASP, [Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). A shared list of LLM risks to check your project against.

## Reader questions

(to be filled from LinkedIn comments)
