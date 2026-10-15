# Lesson 2.3: Safe Retries (course companion)

*Module 2: From answers to actions. Not for LinkedIn.*

## Learning objective

After this lesson, you can make any AI action that changes something (files, pays, sends) safe to retry, so a timeout never causes a duplicate.

## The story

Use [03-same-claim-twice.md](03-same-claim-twice.md): a timeout, a second submit, CLM-1041 and CLM-1042, paid twice.

## Deep dive

**Why timeouts are ambiguous.** A request can fail before it reaches the server, fail while running, or succeed with the reply lost on the way back. From the caller's side, all three look the same: no answer. Treating "no answer" as "failed" causes duplicates.

**Read vs write.** Reading is naturally safe to repeat. Writing (create claim, pay, send email) is not, unless designed to be.

**Idempotency keys.** The caller creates a unique key for the intent (for example from employee, trip and claim period) and sends it with the request. The server stores processed keys; a second request with the same key returns the original result instead of creating a new record. Payment providers commonly support this pattern. If your target system doesn't, add a check-then-create step on your side with a lock.

**Status checks.** After a timeout, query by the key or business reference ("does a claim exist for this trip?") before retrying.

**Retry policy.** Exponential backoff with jitter, a small maximum number of attempts, and retries only for errors that are safe to retry (timeouts, temporary errors), never for "rejected by policy".

**Agents specifically.** Give the agent tools that are idempotent by design, and tell it in the tool description that a timeout means "check status". Log every attempt with its key.

## Hands-on lab

1. Build a fake claims API that sometimes delays its reply past the timeout but still creates the claim.
2. Write an agent tool `submit_claim` without a key, run 20 times, count duplicates.
3. Add an idempotency key and a status-check step; run 20 times again; duplicates should be zero.

## Quiz

1. After a timeout, did the claim fail? *Unknown: it may have succeeded with the reply lost.*
2. What does an idempotency key do? *Makes repeated requests with the same key count once.*
3. Which errors should be retried? *Temporary ones like timeouts; never business rejections.*

## Checklist line (for the module finale)

- [ ] Retries: does every money-moving action carry a unique key, with a status check before any retry?

## Glossary

Timeout, retry, idempotency, idempotency key, exponential backoff, status check.

## Further reading

- Payment-provider documentation on idempotent requests.
- #JustAddRAG write-up 11 (performance and availability).

## Reader questions

*(Add good questions and answers from LinkedIn comments here.)*
