# Lesson 4.6: Safety vs usefulness, and false refusals (course companion)

*Module 4: Guardrails. Not for LinkedIn.*

## Learning objective

After this lesson, you can measure missed harm and false refusals side by side, and set strictness per topic with a safe next step on every refusal.

## The story

Read the article: [06-how-strict.md](06-how-strict.md). Running example: an online electronics store's refund assistant. "Has my headphone order been refunded? It arrived broken." gets "Sorry, I can't help with that", and the customer calls a rival store.

## Deep dive

Guardrails trade two errors against each other. A **missed harm** is a risky request that gets a harmful answer. A **false refusal** is a safe request that gets refused. Most teams only watch the first. A system tuned only for missed harm drifts toward refusing everything, and that failure is silent, because the refusals look responsible in a report.

**Measure both.** Build a test set with two halves: risky requests that must be refused, and safe requests that must be answered. Order-status and delivery questions belong in the safe half. Run the set after each change and report both numbers:

- Missed harm rate: risky requests that were answered.
- False refusal rate: safe requests that were refused.

A good change lowers one number without raising the other much. A change that lowers both is a win. A change that lowers only one, while the other climbs, needs a second look before shipping.

**Set strictness per topic.** A single global setting forces one trade-off on every topic. Order status and delivery can be answered freely. Refund exceptions and anything outside policy need a strict route. Give each topic its own rule and its own pair of numbers. Some teams use a topic map: each category has a route (answer, answer with a caveat, or route to a person).

**Refuse well.** A refusal is a message, and it can help. Compare two replies. The first ends the conversation. The second is still a refusal but gives the customer a next step: what the assistant can't do, who can help now, and how to reach them. Measure this too. A refusal with a next step is not a false refusal in the customer's eyes, even if it is a refusal in the test.

**Why false refusals hurt more than they seem.** Each one teaches the customer that the bot is useless, and teaches staff to ignore it. Over time the warnings that matter get ignored along with the noise, which is the smoke-alarm problem. There is also a direct cost: lost sales and more calls to the support line.

**Limits.** Strictness is one knob among several. A strict bot can still give wrong safe answers, and a loose bot can be right on easy questions. The numbers only say how the system behaves on your test set. Keep the test set current with real traffic, using blocked and redirected messages from the log (write-up 2 and write-up 3), and re-measure after each change.

## Hands-on lab

1. Write 20 test messages: 10 risky that must be refused and 10 safe that must be answered, with at least four safe order-status or delivery questions.
2. Run them through a simple rule-based screen. Count missed harm and false refusals.
3. Change one threshold or rule. Run the set again and compare both numbers.
4. Rewrite three refusals so each one includes a next step. Explain which of the two numbers you would expect to change, and why.

## Quiz

1. What is a false refusal? *A safe request that the system refuses.*
2. Why measure missed harm and false refusals together? *Because tuning only one drifts the system toward recklessness or uselessness, and the other error stays hidden.*
3. Why set strictness per topic? *Because a single setting forces the same trade-off on safe and risky topics alike.*
4. What makes a refusal more helpful? *A next step: what the assistant can't do, who can help now, and how to reach them.*

## Checklist line

- [ ] Missed harm and false refusals are both measured per topic, and every refusal offers a next step.

## Glossary

- **Missed harm:** a risky request that gets a harmful answer.
- **False refusal:** a safe request that gets refused.
- **Topic map:** the list of topics and the route each one takes: answer, caveat or person.
- **Next step:** the useful action a refusal offers the customer.

## Further reading

- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Covers measuring AI system behaviour and its trade-offs.
- OWASP, [Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Covers risks from both insecure and overly restrictive designs.

## Reader questions

(to be filled from LinkedIn comments)
