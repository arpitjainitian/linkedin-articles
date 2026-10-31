# Lesson 4.3: Output checks (course companion)

*Module 4: Guardrails. Not for LinkedIn.*

## Learning objective

After this lesson, you can design an output check that catches advice, hints and overconfidence before a reply reaches a customer, and define a safe fallback.

## The story

Read the article: [03-answer-check.md](03-answer-check.md). Running example: an online electronics store's refund assistant. The draft "your refund is approved and will reach you by tomorrow" has no amount, yet it promises money the policy never approved.

## Deep dive

An output check is the last step before a reply leaves the system. It reads the draft and decides: send it, rewrite it, or replace it with a safe fallback. It is the final look before the reply leaves the store.

**Why check outputs when inputs are screened?** Because a clean question can still get an unsafe answer. The model has its own tendencies, and the screen cannot see the answer before it is written. Only a check on the draft can catch what the model said.

**What counts as a problem?** Be specific, because vague rules miss things:

- **Explicit promises:** refund amounts, dates, discounts and approvals the policy did not give.
- **Hints:** wording that implies a promise without stating it, such as "should land soon", "that's sorted", or "don't worry about the policy".
- **False confidence:** a firm answer to a question that needs a person's judgement.
- **Tone:** casual or dismissive language on refund or complaint topics, even when the facts are right.

**How to detect them.** Three methods work together:

1. **Pattern rules** for clear cases, such as amounts near refund words or phrases that make promises about money.
2. **A reviewer model** that scores the draft against a written definition of advice. It catches hints that rules miss. It can also agree with a bad draft, so it is one signal, not the verdict.
3. **Sampling by a person.** A reviewer reads a sample of drafts each week and labels them. Their labels become the test set for the other two methods.

**The safe fallback.** When a draft fails, do not send a half-fixed version. Send a short, complete, safe reply that still helps: say what the assistant cannot do, name who can help now (a store adviser, the support line), and offer the next step the customer can take. A blocked draft that leaves the customer with nothing is a failure too, and it feeds the false-refusal count from write-up 6.

**Limits.** A check looks only for what it was built to find. A new style of hint passes until someone adds it. A reviewer model can be fooled in the same way as the assistant, so the human sample is what keeps the system honest. Output checks also rely on the other layers: the input screen before, and red teaming (write-up 4) to find gaps.

**Logging.** Keep the blocked drafts, with the rule or reviewer that blocked each one. Reading them shows what the assistant tries to say, and which checks are working.

## Hands-on lab

1. Write 10 draft replies from an assistant, 5 safe and 5 unsafe. Include at least two hints with no numbers.
2. Write three pattern rules that catch explicit advice in the unsafe drafts. Run them and record which drafts were caught.
3. Write a fallback reply for the blocked case. It must say what the assistant can't do, who can help now, and one next step.
4. List the drafts the rules missed. Write one sentence for each saying whether a reviewer model, a human sample or a new rule would catch it.

## Quiz

1. Why is an output check needed even when the input is screened? *Because a clean question can still produce an unsafe answer, which only a check on the draft can catch.*
2. What is a hint, in this context? *Wording that implies a promise without stating it, such as "should land soon".*
3. Why should a blocked draft be replaced with a helpful fallback? *So the customer still gets a next step, instead of nothing, which keeps false refusals low.*
4. What is the role of a weekly human sample? *It labels real drafts, checks the other methods, and supplies the test set.*

## Checklist line

- [ ] Every draft is checked for advice, hints and false confidence before it reaches the customer, and blocked drafts have a safe fallback.

## Glossary

- **Output check:** a step that reviews a draft reply before the customer sees it.
- **Hint:** a reply that implies advice without stating it.
- **Reviewer model:** a second model that scores a draft against a written definition.
- **Fallback:** the safe reply sent when a draft is blocked.

## Further reading

- OWASP, [Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Covers insecure output handling, which output checks address.
- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Covers human oversight and measurement.

## Reader questions

(to be filled from LinkedIn comments)
