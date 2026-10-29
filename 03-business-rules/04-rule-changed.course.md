# Lesson 3.4: When Rules Change (course companion)

*Module 3: Rules. Not for LinkedIn.*

## Learning objective

After this lesson, you can manage rule changes safely: one source of truth, versioned rules with effective dates, and tests before release.

## The story

Use [04-rule-changed.md](04-rule-changed.md): a monsoon waiver added to the prompt, not the code; promised free, charged ₹3,000; still in the prompt in December.

## Deep dive

**Drift between prompt and code.** Any rule stated in a prompt is a second copy. Copies drift. Customers act on what the AI said; billing acts on what the code does.

**Single source of truth.** Rules live in one store (code, a decision table, or a rules engine). The AI gets facts from tools ("is a waiver active for this booking?"), not from prompt text.

**Effective dating.** Every rule has valid-from and valid-to. Evaluation uses the booking or cancellation time. Temporary rules expire automatically; expired rules stay in history.

**Change process.** Version every change, with author and approver. Fast-track path for emergencies that still runs automated tests (a small set of representative bookings) before release.

**Prompt hygiene.** Periodically scan prompts for rule-like statements (amounts, dates, "always", "never", "waived") and move them into the rules store.

**Related.** Proving which rule version applied to a past decision is covered in [Today in AI No. 006](https://www.linkedin.com/pulse/today-ai-006-your-made-decision-can-you-prove-why-data-arpit-jain-vjenf) (decision lineage).

## Hands-on lab

1. Add a temporary waiver to a prompt only; show the mismatch with the code.
2. Move it into the rules table with effective dates; have the AI read it via a tool.
3. Test a booking inside and outside the date range.

## Quiz

1. Why is a rule in the prompt risky? *It becomes a second copy that drifts from the code.*
2. What stops temporary rules outstaying their welcome? *Effective dates with automatic expiry.*
3. Where should the AI get "is there a waiver?" from? *A tool reading the rules store.*

## Checklist line (for the module finale)

- [ ] Every rule lives in one place, versioned, with start and end dates, and none live in the prompt.

## Glossary

Single source of truth, effective dates, rule version, drift.

## Further reading

- [Today in AI No. 006](https://www.linkedin.com/pulse/today-ai-006-your-made-decision-can-you-prove-why-data-arpit-jain-vjenf) (decision lineage).

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
