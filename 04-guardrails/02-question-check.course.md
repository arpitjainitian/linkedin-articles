# Lesson 4.2: Input checks (course companion)

*Module 4: Guardrails. Not for LinkedIn.*

## Learning objective

After this lesson, you can design an input screen that blocks off-topic and high-risk questions before the model sees them, and log each decision.

## The story

Read the article: [02-question-check.md](02-question-check.md). Running example: an online electronics store's refund assistant. A customer asks for the email addresses of other customers who bought headphones, and the assistant starts writing a list because nothing stopped the question.

## Deep dive

An input check is a screen that runs before the model call. Its job is to decide one of three things for each message: answer it normally, route it somewhere safe, or refuse it with a helpful redirect. The model never sees the blocked messages, so a clever answer cannot slip past it.

**Why a separate step?** Two reasons. The screen runs before the expensive model call, so it is cheap. And it has one job, so it is easier to test than a model whose instructions compete with each other. Putting the screen in the same prompt as the helpful assistant creates a conflict: the same model is asked to welcome the guest and check the guest list.

**What does the screen look at?** Three things, in order of cost:

1. **Rules.** Keyword and pattern lists, such as phrases that ask for other customers' data. Cheap and predictable, but blind to rephrasing.
2. **A small classifier.** A model trained or prompted only to label messages: on topic or off, risk level, needs a human. More flexible than rules, and still fast.
3. **Escalation.** When the screen is unsure, it sends the message to a safe route, not to the full assistant.

For the highest-risk category, such as a message that suggests harm to oneself, the safe route is immediate: a short, caring reply that points to emergency help and a real person. It does not try to be a complete answer.

**Topic limits.** A store's support assistant should answer about orders, delivery and refunds. Other topics get a polite redirect. Topic limits are not a safety feature by themselves, but they cut the surface area an attacker can use.

**Logging.** Every blocked or redirected message gets a record: time, reason, route taken. Store only what you need, and remove personal details where you can. The log is how you learn what customers really ask. It also shows whether the screen is too tight, when many safe questions are being blocked. That measurement links to write-up 6.

**Limits.** An input screen sees the message, not the intent behind it. A harmless-looking question can lead to a risky answer, which is why output checks exist (write-up 3). A screen that is too loose lets risk through, and one that is too tight refuses order-status questions. Both failures are visible in the log if you look for them.

## Hands-on lab

1. Write 15 example messages: 5 on-topic, 5 off-topic, 5 high-risk (including one that hides its intent in a harmless phrase).
2. Build a rule-based screen with three outputs: `answer`, `redirect`, `safe_route`. Test it against your 15 messages.
3. Record each decision in a log file with a timestamp and a reason.
4. Find the message the rules missed. Write one sentence on how a classifier or a human review would catch it.

## Quiz

1. What are the three outcomes of an input screen? *Answer normally, route to a safe path, or refuse with a helpful redirect.*
2. Why keep the screen separate from the assistant's prompt? *Because one model would be asked to welcome guests and check the guest list at once, and the two jobs conflict.*
3. Why must the high-risk route be short and caring? *Because the goal is to get the person to emergency help and a real person quickly, not to give a complete answer.*
4. What does a log of blocked questions tell you? *What customers really ask, and whether the screen is too loose or too tight.*

## Checklist line

- [ ] Every message is screened before the model, and every block is logged with its reason.

## Glossary

- **Input check:** a screen that decides what happens to a message before the model sees it.
- **Topic limit:** the list of subjects the assistant answers and the subjects it redirects.
- **Classifier:** a small model or rule set that labels a message, such as on topic or high risk.
- **Escalation:** passing an unclear case to a safer path or a human.

## Further reading

- OWASP, [Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Covers prompt injection, which input checks help reduce.
- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Covers monitoring and logging as part of managing AI risk.

## Reader questions

(to be filled from LinkedIn comments)
