# System Design, A9: How Fresh Does "Seats Available" Need to Be?

*Q&A, system design track, Series A: Classic system design.*

**The question:** Seat availability is shown on millions of screens and changes every second during Tatkal. How fresh does it need to be, and how do you serve it without hammering the booking database?

## What's really happening

Millions of people refresh the availability page. If every refresh asks the booking database, the database spends all its time answering "how many seats?" instead of actually booking seats.

The key insight: **the number on the screen doesn't need to be perfect. The booking does.**

Think of a cinema's "Housefull" board outside. It might be a minute behind. Nobody minds. But the person at the counter must never sell the same seat twice.

## The design

1. **Separate reading from booking.** Bookings go to the main database. Availability is read from a fast copy or cache.
2. **Update the cache from bookings.** Every booking or cancellation pushes the new count to the cache.
3. **Accept a small delay.** Show availability that's a few seconds old, and say so: "Updated 5 seconds ago."
4. **Check for real at booking time.** The final booking step always checks the true count in the main database (see Q4).
5. **Show ranges when it's tight.** "Few seats left" is more honest than an exact number that changes every second.

This split between the write side and the read side is often called **CQRS**, and accepting a short delay is called **eventual consistency**.

## The key trade-off

Freshness vs load. Exact real-time numbers for millions of screens would cost a lot and slow down booking. A few seconds of delay costs almost nothing, as long as the booking itself is exact.

## What breaks at scale

Pushing every single update to millions of screens creates its own storm. Batch updates every second or two, and let screens refresh at slightly different times.

## Simple diagram idea

Two paths. Write path: "Book" → main database → event → cache. Read path: millions of screens → cache only. A small clock on the cache: "a few seconds behind".

## What I'd say in the room

1. "The display can be a few seconds old. The booking must be exact. So I'd separate the two."
2. "Bookings hit the main database; availability is served from a cache updated by booking events."
3. "The final booking step always re-checks the real count, so a slightly stale screen never causes an oversell."

## Related

- Q4: 60 seats, 50,000 clicks. How do you never sell a seat twice?

## Source

S2: IRCTC Tatkal booking scenario, written from publicly known Tatkal behaviour. Not based on IRCTC's internal design.

---

**Post text (copy and paste):**

```
System design question:

Seat availability shows on millions of screens and changes every second during Tatkal. How fresh does it need to be?

The insight: the number on the screen doesn't need to be perfect. The booking does.

How I'd design it:
• Bookings go to the main database
• Availability is served from a cache, updated by booking events
• The screen can be a few seconds behind, and says so
• The final booking step always checks the real count

Like a cinema's "Housefull" board: a minute late is fine. Selling a seat twice is not.

How would you design it?

#SystemDesign #Caching #Scalability #IRCTC
```
