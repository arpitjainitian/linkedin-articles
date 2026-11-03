# Lesson 6.3: Canary questions and silent failures (course companion)

*Module 6: Observability. Not for LinkedIn.*

## Learning objective

After this lesson, you can design canary questions with known answers, schedule them in production, and track refusal rate in both directions to catch silent failures.

## The story

Read the article: [03-canary-questions.md](03-canary-questions.md). Running example: a food-delivery support bot tells a customer that a delivered order is still on the way. Nobody complains, and every error dashboard stays green.

## Deep dive

A **silent failure** gives a normal-looking answer that is wrong. Error logs and uptime checks do not see it, because nothing technically failed. Complaints do see it, but late, and only from customers who write back.

**Canary questions.** A canary is a question with a known correct answer, sent on a schedule in production, the way a customer would ask it. If the answer changes from the expected result, the system raises an alert. The name comes from canaries in coal mines: an early sign that something in the environment has changed.

Good canaries are:

- **Specific:** "Where is order 9931?" with the expected status, not "How are deliveries?"
- **Stable:** the expected answer changes rarely, so a change means a real problem.
- **Varied:** cover the main kinds of question, not only the easy ones.

**Refusal rate in both directions.** An assistant can fail by saying too little, or by saying too much.

- **Over-refusal:** "I can't help with that" for ordinary questions. Customers leave.
- **Under-refusal:** answering questions it should hand to a person. Risk grows.

Track both rates over time. A rise in either is a signal, even when no one reports it.

**Matching canary results.** A canary's answer may be phrased differently each time. Compare the facts it contains, such as the status, rather than the exact words. Keep the comparison simple, and review the mismatches by hand at first.

**Limits.** Canaries cover the questions you chose. They will not notice a failure on a question nobody thought to ask. Pair them with sampled real traffic, reviewed on a schedule.

## Hands-on lab

1. Write 10 canary questions for a small assistant, each with the expected fact in one line.
2. Write a script that runs them and checks the expected fact, not the exact wording.
3. Run the script on a schedule, and record one mismatch when you change the data.
4. Count over-refusals and under-refusals on a sample of 50 real or simulated questions.

## Quiz

1. Why can a silent failure go unnoticed for weeks? *Because the answer looks normal, no error is logged, and only some customers complain.*
2. What makes a good canary question? *A specific question with a stable, known expected answer.*
3. Why track refusal rate in both directions? *Because too many refusals hurt users, and too few refusals can let risky answers through.*

## Checklist line

- [ ] Canary questions run in production on a schedule, and refusal rate is tracked in both directions.

## Glossary

- **Canary question:** a known question with a known answer, run in production to detect change.
- **Silent failure:** a wrong answer that looks normal and raises no error.
- **Over-refusal:** refusing ordinary questions the assistant should answer.
- **Under-refusal:** answering questions it should hand to a person.

## Further reading

- Your own complaint log: a useful check on what the canaries miss.
- Your provider's documentation on evaluation and monitoring features.

## Reader questions

- Which question does your team check every day by hand?
- Would your team notice if the refusal rate doubled next week?
