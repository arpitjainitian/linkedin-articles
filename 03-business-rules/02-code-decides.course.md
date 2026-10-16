# Lesson 3.2: Code Decides, the AI Explains (course companion)

*Module 3: Rules. Not for LinkedIn.*

## Learning objective

After this lesson, you can design an AI assistant where code makes every rule-based decision and the model only explains it, using tool calling.

## The story

Use [02-code-decides.md](02-code-decides.md): code calculates ₹1,240; the AI explains it kindly and offers an exception request.

## Deep dive

**Architecture.** The model receives the customer message and has a tool `calculate_refund(booking_id)`. The tool runs deterministic code (or a rules engine) and returns a structured result: eligible, refund amount, fee, rule ID, explanation keys. The model writes the reply using only those values.

**Guarding the numbers.** Validate the final reply: every amount and date in the text must match the tool result. If not, regenerate or fall back to a template.

**Rules engines vs plain code.** Simple policies fit in ordinary code with a decision table. Larger, frequently changing policies may justify a rules engine so non-developers can maintain rules. Either way: versioned and tested.

**Exceptions.** The model can't grant exceptions. It can create an escalation with the customer's reason, routed to a person with authority. That person's decision is recorded with their name.

**What the model is still great at.** Understanding the request ("I need to cancel my Delhi flight"), finding the booking, explaining in the customer's language, handling follow-ups, empathy.

## Hands-on lab

1. Write `calculate_refund` as plain code with a small decision table (fare type x hours before departure).
2. Give it to a model as a tool; test 10 cancellations, including sympathetic ones.
3. Add a check that the reply's numbers match the tool result.

## Quiz

1. Who calculates the refund? *Code, called by the AI as a tool.*
2. What may the AI change in the reply? *The wording, never the numbers.*
3. What happens when a customer asks for an exception? *Escalate to a person with authority.*

## Checklist line (for the module finale)

- [ ] The AI calls code for every decision and never changes the numbers in its reply.

## Glossary

Tool calling, rules engine, decision table, escalation.

## Further reading

- Provider documentation on tool use / function calling.

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
