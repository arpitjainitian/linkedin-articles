# System Design, A4: 60 Seats, 50,000 Clicks. How Do You Never Sell a Seat Twice?

*Q&A, system design track, Series A: Classic system design.*

**The question:** A train has 60 Tatkal seats and 50,000 people click "Book" in the same few seconds. How do you make sure no seat is ever sold twice?

## What's really happening

Two users read "1 seat left" at the same moment. Both see it as available. Both book it. Now one seat has two passengers.

This is a **race condition**: the gap between checking and updating lets two people slip through.

Think of two people reaching for the last samosa on a plate. Both saw it was there. Only one can have it. The system has to decide who, instantly and fairly.

## The fixes

| Approach | How it works | Good for |
|---|---|---|
| **Atomic decrement** | One single database step: "reduce seats by 1 only if seats > 0". It succeeds or fails, nothing in between | Simple seat counts |
| **Row lock** | Lock the seat row while booking it; others wait | Specific seat numbers |
| **Optimistic locking** | Each seat has a version number; an update only works if the version hasn't changed | Lower contention |
| **Single-writer queue** | All booking requests for a train go through one ordered queue | Very hot trains |
| **In-memory counter** | A fast counter (for example in Redis) hands out seats, then the database confirms | Extreme spikes |

Whatever you choose, the rule is the same: **the check and the update must happen as one step.**

## What breaks at scale

Locks on one popular train become a queue in themselves. Under extreme load, an in-memory counter in front of the database absorbs the rush, and the database only sees the 60 winners, not the 50,000 attempts.

## Simple diagram idea

50,000 arrows hitting one box labelled "Seats left: 60". Only 60 arrows pass through. The rest get "Sold out" instantly.

## What I'd say in the room

1. "The risk is a race condition: two users check and book the same seat between the read and the write."
2. "I'd make check-and-book a single atomic step, with an atomic decrement or a lock on the seat."
3. "For extreme spikes, I'd put a fast in-memory counter in front, so the database only handles the actual winners."

## Source

S2: IRCTC Tatkal booking scenario, written from publicly known Tatkal behaviour. Not based on IRCTC's internal design.

---

**Post text (copy and paste):**

```
System design question:

60 Tatkal seats. 50,000 people click "Book" in the same few seconds. How do you make sure no seat is sold twice?

The danger is a race condition: two people check "1 seat left" at the same moment, and both book it.

How I'd fix it:
• Make check-and-book one atomic step ("reduce by 1 only if more than 0")
• Or lock the seat while it's being booked
• For extreme spikes, a fast in-memory counter in front, so the database only sees the 60 winners

The rule: checking and updating must happen as one step.

How would you design it?

#SystemDesign #Concurrency #Databases #IRCTC
```
