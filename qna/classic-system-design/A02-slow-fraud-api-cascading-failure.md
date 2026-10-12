# System Design, A2: How Do You Stop One Slow API From Crashing Your Whole Checkout?

*Q&A, system design track, Series A: Classic system design.*

**The question:** During a holiday sale, the third-party fraud-check API your checkout depends on slows from 50 ms to 15 seconds per call. Checkout threads pile up waiting, and the whole e-commerce platform crashes. How do you stop one slow dependency from taking everything down?

## What's really happening

Each checkout request holds a thread while it waits for the fraud check. At 50 ms, threads come back quickly. At 15 seconds, they don't. New requests keep arriving, every thread ends up waiting, and soon nothing else can run: not search, not cart, not login.

A slow dependency is often worse than a dead one. A dead one fails fast. A slow one holds everything hostage.

This is a **cascading failure**.

Think of a single slow cashier in a supermarket where every queue merges into one. One slow till, and the whole shop stops moving.

## The fixes

| Problem | Fix |
|---|---|
| Calls wait forever | Set a strict **timeout**, for example 300 ms |
| Every call keeps trying a broken service | A **circuit breaker**: after repeated failures, stop calling for a while and fail fast |
| Fraud checks use the same threads as everything else | A **bulkhead**: a separate, limited pool of threads just for fraud calls |
| No answer means no checkout | **Graceful degradation**: decide a fallback, like allowing low-value orders and holding high-value ones for review |
| Retries pile on more load | Limited retries with **backoff** |

The key business decision: **what happens when the fraud check is unavailable?** That's not an engineering default. Risk, finance and product should agree it in advance.

## What breaks at scale

During a sale, traffic is many times normal. Without a bulkhead, even a short slowdown fills every thread in seconds. Test it before the sale by deliberately slowing the dependency in a test environment.

## Simple diagram idea

Checkout service with three separate pools (payment, fraud, inventory). The fraud pool is full and red, with a circuit breaker "open" sign. The other two pools are green and still serving.

## What I'd say in the room

1. "A slow dependency is holding threads, so every other request starves. It's a cascading failure."
2. "I'd add a tight timeout, a circuit breaker, and a separate thread pool for the fraud call, so it can't take down the rest."
3. "And I'd agree a fallback with the business in advance, like allowing small orders and queuing big ones for review."

## Related

- #JustAddRAG write-up 11: "It's fast in the demo, so why are users clicking twice?" (fallbacks and graceful degradation)

## Source

S1: question shared by Arpit.

---

**Post text (copy and paste):**

```
System design question:

During a holiday sale, the fraud-check API your checkout uses slows from 50 ms to 15 seconds. Threads pile up, and the whole site crashes. How do you stop one slow dependency from taking everything down?

A slow dependency is worse than a dead one. Dead fails fast. Slow holds every thread hostage.

How I'd fix it:
• A strict timeout on the call
• A circuit breaker that fails fast after repeated errors
• A separate thread pool just for fraud checks (a bulkhead)
• A fallback agreed with the business before the sale

How would you handle it?

#SystemDesign #SoftwareArchitecture #Resilience #Microservices
```
