# Lesson 3.1: Rules Need Code (course companion)

*Module 3: Rules. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain why business rules applied by a language model are inconsistent, and identify which decisions in a system must be made by code.

## The story

Use [01-curtain-raiser.md](01-curtain-raiser.md): a non-refundable Saver fare, a family emergency, and "Full refund, no fees".

## Deep dive

**Why models bend rules.** A model predicts a helpful, plausible reply. A sympathetic message shifts what "helpful" looks like; the policy text is just more context competing for attention. Long policies make it worse: exceptions far from the question get under-weighted.

**Inconsistency is built in.** Sampling, prompt changes and model updates mean the same case can get different outcomes. For money, eligibility and compliance, that's unacceptable even if the average answer is right.

**Arithmetic and dates.** Fees as percentages of fare, time windows to the minute, currency rounding: these belong in code, where they're exact and testable.

**The test.** Ask: would a regulator, an auditor or the customer accept "the AI decided"? If not, the decision belongs to code.

## Hands-on lab

1. Put a 2-page refund policy in a prompt.
2. Send the same 5 cancellation cases 10 times each, some with sympathetic stories.
3. Record refund amounts; measure how often the answer varies or breaks policy.

## Quiz

1. Why does a sad story change the AI's refund answer? *It shifts what the model sees as the most helpful reply; the policy is just more text.*
2. Name three kinds of decisions that should be made by code. *Money, eligibility, compliance.*
3. Deterministic or probabilistic: which do refunds need? *Deterministic.*

## Checklist line (for the module finale)

- [ ] Every money, eligibility and compliance decision is made by code, not the model.

## Glossary

Business rule, deterministic, probabilistic, policy.

## Further reading

- #JustAddRAG write-up 6 (LLM, database, or both).

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
