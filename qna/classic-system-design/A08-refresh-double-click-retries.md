# System Design, A8: Users Keep Hitting Refresh and "Book". How Do You Handle Retries Safely?

*Q&A, system design track, Series A: Classic system design.*

**The question:** Users hit refresh and "Book" repeatedly when the site is slow, multiplying the load and creating duplicate requests. How do you handle retries and double clicks safely?

## What's really happening

When a page is slow, people click again. And again. Each click is a new request. So a slow system gets more load exactly when it can least handle it, and a user can end up with two bookings or two payments.

This is a **retry storm**.

Think of pressing a lift button ten times. It doesn't come faster. But in software, each press can actually call another lift.

## The fixes

| Problem | Fix |
|---|---|
| Two clicks create two bookings | An **idempotency key**: each booking attempt gets a unique ID, and the server ignores repeats of the same ID |
| The button can be pressed again | **Disable the button** after the first click and show "Booking in progress" |
| Refresh re-sends the form | After submitting, **redirect** to a status page, so refresh only reloads the status |
| Apps retry instantly on errors | **Exponential backoff with jitter**: wait longer between each retry, at slightly random times |
| Users don't know if it worked | A **status page** that shows the booking's real state |
| Overloaded servers keep accepting work | **Load shedding**: politely reject extra requests early instead of slowing down for everyone |

The most important one is the idempotency key. Even if every other fix fails, it guarantees one booking per attempt.

## What breaks at scale

Every client retrying at fixed intervals creates synchronised waves of traffic. Random jitter spreads retries out, so they don't all hit at the same moment.

## Simple diagram idea

A user clicking "Book" three times. All three requests carry the same idempotency key. The server processes the first and returns the same result for the other two.

## What I'd say in the room

1. "Slow pages trigger repeat clicks, which multiply load and risk duplicate bookings."
2. "I'd give each booking attempt an idempotency key, so repeats return the same result instead of a new booking."
3. "On the client, disable the button, redirect after submit, and retry with backoff and jitter."

## Related

- Q6: The money is gone, the ticket isn't. How do you make sure it never happens?
- #JustAddRAG write-up 11: "It's fast in the demo, so why are users clicking twice?"

## Source

S2: IRCTC Tatkal booking scenario, written from publicly known Tatkal behaviour. Not based on IRCTC's internal design.

---

**Post text (copy and paste):**

```
System design question:

The site is slow, so users hit refresh and "Book" again and again. Load multiplies, and some get two bookings. How do you handle it?

Pressing the lift button ten times doesn't bring it faster. In software, each press can call another lift.

How I'd fix it:
• An idempotency key per booking attempt, so repeats return the same result
• Disable the button after the first click
• Redirect to a status page after submit
• Retries with backoff and jitter, not instantly

One attempt, one booking. However many clicks.

How would you handle it?

#SystemDesign #DistributedSystems #Reliability #IRCTC
```
