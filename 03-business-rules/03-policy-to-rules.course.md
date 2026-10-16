# Lesson 3.3: From Policy to Rules (course companion)

*Module 3: Rules. Not for LinkedIn.*

## Learning objective

After this lesson, you can turn a natural-language policy into a tested, traceable decision table, using AI as a drafting assistant and humans as approvers.

## The story

Use [03-policy-to-rules.md](03-policy-to-rules.md): a 40-page policy, "exceptional circumstances", and 60 AI-drafted rules with 3 invented.

## Deep dive

**Step 1: inventory.** List every decision the assistant must make (eligibility, refund amount, fee, credit vs cash, exceptions).

**Step 2: extract with AI, with citations.** Ask the model to propose rules as structured rows, each with the exact policy quote and page. Reject any row without a verbatim source quote; that removes most invented rules.

**Step 3: resolve ambiguity.** Collect vague terms ("reasonable", "exceptional", "at discretion"). For each, the rule owner picks: a precise definition, a short list, or "route to a person". Record the decision.

**Step 4: resolve conflicts.** Where sections disagree, the rule owner decides precedence and the policy gets fixed at the source.

**Step 5: decision table and tests.** Encode as a table (conditions → outcome). Check completeness (every combination covered) and overlap (no two rows match the same case with different outcomes). Back-test on historical cases; investigate every mismatch.

**Ownership.** Policy/legal owns meaning; engineering owns implementation; both sign off changes.

## Hands-on lab

1. Take a 2-page sample refund policy.
2. Ask a model to extract rules as JSON rows with quote and page.
3. Remove rows without exact quotes; list vague terms; decide them.
4. Build a decision table; check gaps and overlaps; back-test on 20 sample past cases.

## Quiz

1. How do you catch rules the AI invented? *Require a verbatim source quote for every rule.*
2. What do you do with "exceptional circumstances"? *Define it as a list, or route those cases to a person.*
3. Who owns what a rule means? *The policy owner, not engineering.*

## Checklist line (for the module finale)

- [ ] The policy was turned into approved, traceable rules, with vague words decided and back-tested on past cases.

## Glossary

Decision table, rule owner, traceability, back-testing, ambiguity.

## Further reading

- Introductions to decision tables and DMN (Decision Model and Notation).

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
