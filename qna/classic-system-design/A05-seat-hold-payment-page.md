# System Design, A5: A User Picks a Seat, Then Waits on the Payment Page. Do You Hold the Seat?

*Q&A, system design track, Series A: Classic system design.*

**The question:** A user picks a seat, then sits on the payment page for minutes. Should the seat be held, for how long, and what happens when the hold expires or payment fails?

## What's really happening

If you don't hold the seat, the user pays and then finds the seat is gone. If you hold it forever, people block seats they never pay for, and genuine buyers lose out.

The answer is a **temporary hold with a timer**.

Think of a shop keeping a dress aside for you for 15 minutes while you fetch your wallet. After 15 minutes, it goes back on the rack.

## The design

1. **Hold on selection.** When the user picks a seat, mark it as held, not sold, with an expiry time.
2. **Show the timer.** "Seat held for 10:00 minutes." Users behave better when they can see the clock.
3. **Confirm on payment.** When payment succeeds, change held to sold, in one step.
4. **Release on expiry.** If the timer runs out, the seat goes back to available automatically.
5. **Release on failure.** If payment fails, release the seat straight away, or give a short grace period to retry.

## The key decisions

| Decision | Trade-off |
|---|---|
| How long to hold | Too short: users lose seats mid-payment. Too long: seats sit blocked. Base it on real payment times |
| Holds per user | Limit it, so one person can't block many seats |
| Late payment success | If payment succeeds after the hold expired, either honour it if the seat is still free, or refund automatically |

That last case matters most. Payment systems are slow sometimes. The design must handle "money arrived after the timer" without leaving the user stuck.

## What breaks at scale

Millions of holds expiring need a cheap way to release them. A store that supports automatic expiry (a TTL) handles this better than a job scanning the database every minute.

## Simple diagram idea

A seat's life as a simple loop: Available → Held (timer) → Sold. Two arrows back to Available: "timer expired" and "payment failed".

## What I'd say in the room

1. "I'd hold the seat with a timer when it's picked, shown clearly to the user."
2. "Payment success turns held into sold in one step. Expiry or failure releases it automatically."
3. "And I'd plan for late payments: honour them if the seat is still free, or refund automatically."

## Source

S2: IRCTC Tatkal booking scenario, written from publicly known Tatkal behaviour. Not based on IRCTC's internal design.

---

**Post text (copy and paste):**

```
System design question:

A user picks a seat, then sits on the payment page for minutes. Do you hold the seat? For how long? What if payment fails?

Don't hold it, and they pay for a seat that's gone. Hold it forever, and seats sit blocked.

How I'd design it:
• Hold the seat with a visible timer when it's picked
• Payment success turns "held" into "sold" in one step
• Timer expiry or payment failure releases it automatically
• Late payment? Honour it if the seat is still free, or refund automatically

Like a shop keeping a dress aside for 15 minutes.

How would you design it?

#SystemDesign #SoftwareArchitecture #Payments #IRCTC
```
