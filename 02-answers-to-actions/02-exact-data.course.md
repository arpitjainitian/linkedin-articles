# Lesson 2.2: Exact Data from Messy Receipts (course companion)

*Module 2: From answers to actions. Not for LinkedIn.*

## Learning objective

After this lesson, you can design an AI step that turns messy documents into exact, validated data, and that flags what it can't read instead of guessing.

## The story

Use the LinkedIn article [02-exact-data.md](02-exact-data.md) as the lesson intro: ₹1,180 read as ₹118, and a UPI screenshot "filled in" as Uber.

## Deep dive

**Why models get exact values wrong.** A language model predicts likely text. "₹118" and "₹1,180" are both plausible strings. Commas, Indian digit grouping (1,18,000 vs 118,000), blurred zeros and a GST line printed near the total all push it towards the wrong but plausible answer. Nothing in free text forces it to be exact.

**Structured output.** Instead of asking for prose, define a schema: `amount` (decimal, > 0, two places), `currency` (enum: INR), `date` (ISO date, within the trip dates), `merchant` (string or null), `category` (enum: taxi, hotel, meals, other), `confidence` per field. Use the provider's strict structured-output or function-calling mode so the response must match the schema. This fixes format; it does not fix truth.

**Validation, in layers.**
1. *Type checks:* amount is a number, date is a real date.
2. *Business rules:* date inside the trip, category allowed by policy, amount below the category limit.
3. *Cross-field checks:* line items add up to the total; GST is about 5% or 18% of the base, not equal to it.
4. *Cross-source checks (reconciliation):* the UPI amount matches the bank SMS or card statement; the hotel bill matches the booking.

**Null over guess.** Allow `merchant: null` and a low confidence score. Prompt the model that an empty field is better than an invented one, and test that it actually leaves fields empty (see the evals in #JustAddRAG write-up 9).

**Human review queue.** Anything that fails validation or has low confidence goes to a person with the receipt image and the extracted values side by side. Measure how often humans correct each field; that's your real accuracy number.

**Where code decides.** The model extracts; code validates and computes totals. Never let the model add up the amounts in prose.

## Hands-on lab

Using the expense-claims project:
1. Write a JSON schema for a receipt (amount, currency, date, merchant, category, confidence).
2. Run 10 sample receipts (include a blurred total, a UPI screenshot with no merchant, and a receipt with a GST line) through a model in structured-output mode.
3. Add validation: types, trip-date range, line items summing to the total, GST sanity check.
4. Route failures and low-confidence fields to a "needs review" list.
5. Report: how many fields were right, how many were caught by validation, how many slipped through.

## Quiz

1. Structured output guarantees the right format. Does it guarantee the right value? *No. It fixes the shape, not the truth; validation and cross-checks catch wrong values.*
2. A receipt has no merchant name. What should the AI return? *An empty value (null) with low confidence, routed to a person; never a guess.*
3. Name one cross-field check for a receipt. *Line items sum to the total; GST is a sensible percentage of the base amount.*
4. Who should compute the claim total: the model or code? *Code, from validated line items.*

## Checklist line (for the module finale)

- [ ] Exact data: does every field have a schema, validation, and a route to a person when the AI isn't sure?

## Glossary

Structured output, schema, validation, reconciliation, confidence score, human review queue.

## Further reading

- Provider documentation on structured outputs / JSON mode and function calling.
- #JustAddRAG write-up 2 (reading messy documents) and write-up 9 (evals).

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
