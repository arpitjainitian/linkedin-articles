# System Design, A6: The Money Is Gone, the Ticket Isn't. How Do You Make Sure It Never Happens?

*Q&A, system design track, Series A: Classic system design.*

**The question:** Payment succeeds at the bank, but the booking confirmation never arrives because of a timeout. The money is gone, the ticket isn't. How do you design so this never leaves a user stuck?

## What's really happening

Booking a ticket touches two systems: the bank and the booking system. They can't be updated together in one perfect step. So sometimes one succeeds and the other doesn't know.

The bank says "paid". The booking system never heard back. The user sees an error and an empty bank balance.

You can't prevent every timeout. You can make sure every one gets **fixed**.

Think of paying at a shop counter when the card machine freezes. A good shop doesn't argue. It checks the bank statement, and either gives you the item or your money back.

## The design

1. **One ID for the whole journey.** Create a booking ID before payment and send it to the bank. Every step uses that same ID.
2. **Safe retries.** Make "confirm booking" **idempotent**: running it twice with the same ID gives the same result, not two tickets.
3. **A clear state for "unsure".** Booking states like: started, payment pending, paid, confirmed, refunded. A timeout puts it in "payment pending", not "failed".
4. **Ask the bank.** For anything stuck in "payment pending", check the bank's status by booking ID.
5. **Reconcile regularly.** A job compares the bank's records with bookings and fixes every mismatch: confirm the ticket if a seat exists, otherwise refund automatically.
6. **Tell the user honestly.** "Payment received, confirming your ticket" is better than "Failed".

This step-by-step approach, with a way to undo each step, is often called a **saga**.

## What breaks at scale

At Tatkal scale, even a tiny share of timeouts means thousands of stuck users in a few minutes. Reconciliation has to be automatic and fast, not a support team working through emails.

## Simple diagram idea

Booking states as boxes: Started → Payment pending → Paid → Confirmed. From Paid, a branch to Refunded when no seat is left. A "reconciler" checking the bank's list against the bookings list.

## What I'd say in the room

1. "Two systems can't commit together, so I'd design for 'unsure' instead of pretending it can't happen."
2. "One booking ID end to end, idempotent confirmation, and a 'payment pending' state for timeouts."
3. "Then automatic reconciliation against the bank: confirm the ticket if possible, refund automatically if not."

## Related

- Q2: How do you stop one slow API from crashing your whole checkout?

## Source

S2: IRCTC Tatkal booking scenario, written from publicly known Tatkal behaviour. Not based on IRCTC's internal design.

---

**Post text (copy and paste):**

```
System design question:

Payment succeeds at the bank. The booking confirmation times out. The money is gone, the ticket isn't. How do you make sure no user stays stuck?

You can't stop every timeout. You can make sure every one gets fixed.

How I'd design it:
• One booking ID from start to finish, shared with the bank
• "Confirm" is safe to retry: same ID, same result, never two tickets
• A "payment pending" state instead of "failed"
• Automatic reconciliation with the bank: confirm if possible, refund if not

How would you design it?

#SystemDesign #DistributedSystems #Payments #IRCTC
```
