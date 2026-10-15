# Lesson 2.4: Jobs That Stop Halfway (course companion)

*Module 2: From answers to actions. Not for LinkedIn.*

## Learning objective

After this lesson, you can design a multi-step AI action so that a failure in the middle leaves a clean, honest state: finished, resumable or undone.

## The story

Use [04-halfway.md](04-halfway.md): claim filed, upload fails at receipt 9, the AI says "Done!", the manager rejects it.

## Deep dive

**Multi-step actions have no automatic all-or-nothing.** A database can wrap steps in one transaction; calls to several external systems can't. Each step commits on its own.

**Order the steps.** Put reversible and private steps first (create a draft, upload attachments) and the visible or irreversible step last (submit to the approver, pay). This single change removes most half-done states.

**Checkpoints.** Record progress after each step (which receipts uploaded, their IDs). On retry, read the checkpoint and continue. Combine with idempotency keys from Lesson 2.3 so a repeated step doesn't duplicate.

**Compensation (the saga pattern).** For each step that can't be rolled back automatically, define an undo action: delete the draft, withdraw the claim, cancel the notification. If the job can't be completed within its limits, run the undo actions in reverse order.

**Honest status.** The agent's final message must come from verified step results, not from its own belief. Use a status object (steps, results, outstanding items) and generate the user message from it.

**Where this goes deeper.** Long-running work that survives server restarts is covered in Series 16 (the agent harness: state and checkpoints).

## Hands-on lab

1. Build a three-step job: create draft claim, upload N receipts, submit.
2. Make the upload fail randomly at one receipt.
3. Version A: submit first. Count half-done claims over 20 runs.
4. Version B: upload first, submit last, with checkpoints and a withdraw-draft undo. Count again.
5. Make the final user message come only from the verified status object.

## Quiz

1. Which step should come last? *The one that can't be undone or that others can see, like submitting.*
2. What is compensation? *An undo action for a step that already succeeded.*
3. Where should the "done" message come from? *From verified step results, not the model's assumption.*

## Checklist line (for the module finale)

- [ ] Halfway: is the irreversible step last, with a resume or undo plan for every step before it?

## Glossary

Partial failure, checkpoint, compensation, saga pattern, irreversible step.

## Further reading

- Articles on the saga pattern for distributed transactions.
- Lesson 2.3 (safe retries) in this module.

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
