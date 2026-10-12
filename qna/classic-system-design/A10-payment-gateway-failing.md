# System Design, A10: The Payment Gateway Starts Failing at 10:00 AM. What Now?

*Q&A, system design track, Series A: Classic system design.*

**The question:** At 10:00 AM, the payment gateway starts failing for a large share of users. How do you protect the booking system and give users a fair second chance?

## What's really happening

The payment gateway is outside your control. When it fails at the busiest minute, two things go wrong at once: your system piles up waiting on it, and users who already won a seat are about to lose it through no fault of their own.

So the goal is two-fold: **protect the system**, and **protect the users' place**.

Think of a cash counter where the card machine stops working. A good shop doesn't send everyone home. It holds their items, opens another machine or takes UPI, and serves them in the same order.

## The design

1. **Fail fast.** A **circuit breaker** on the payment call stops the booking system from piling up behind a broken gateway (see Q2).
2. **Have a second route.** If possible, a **backup gateway** or another payment method, with automatic switching.
3. **Keep the seat held.** Extend the seat hold for users whose payment failed because of the gateway, not because of them.
4. **Queue the retries.** Put failed payments in an ordered queue and retry them as the gateway recovers, in the order users arrived.
5. **Tell users the truth.** "Payment provider issue. Your seat is held for 15 more minutes. We'll retry automatically."
6. **Reconcile afterwards.** Some "failed" payments may have actually gone through. Match them against the bank and confirm or refund (see Q6).

## The key trade-off

Fairness vs seats. Holding seats longer for affected users means fewer seats for new users during the outage. That's usually the fair choice: the people who already won shouldn't lose because of someone else's failure.

## What breaks at scale

When the gateway comes back, everyone retries at once and knocks it over again. Release the queued retries at a steady, controlled rate.

## Simple diagram idea

Booking service → circuit breaker → gateway A (red, failing). A dotted line to gateway B (green). Below, a queue of "payment retry" items, released one by one as the gateway recovers.

## What I'd say in the room

1. "I'd protect the system first: a circuit breaker so booking doesn't pile up behind a failing gateway."
2. "Then protect the user: keep their seat held longer, switch to a backup gateway if we have one, and queue retries in arrival order."
3. "Afterwards, reconcile with the bank, because some 'failed' payments will have actually succeeded."

## Related

- Q2: How do you stop one slow API from crashing your whole checkout?
- Q6: The money is gone, the ticket isn't. How do you make sure it never happens?

## Source

S2: IRCTC Tatkal booking scenario, written from publicly known Tatkal behaviour. Not based on IRCTC's internal design.

---

**Post text (copy and paste):**

```
System design question:

At 10:00 AM, the payment gateway starts failing for many users. How do you protect the booking system and give users a fair second chance?

Two goals: protect the system, and protect the users' place.

How I'd design it:
• A circuit breaker so booking doesn't pile up behind the failing gateway
• A backup gateway or payment method, if available
• Keep seats held longer for users hit by the outage
• Retry failed payments in arrival order as the gateway recovers
• Reconcile afterwards: some "failed" payments actually went through

People who already won a seat shouldn't lose it to someone else's outage.

How would you design it?

#SystemDesign #Resilience #Payments #IRCTC
```
