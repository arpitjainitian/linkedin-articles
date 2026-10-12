# System Design, A3: How Do You Design for a Spike That Arrives at 10:00 AM Sharp Every Day?

*Q&A, system design track, Series A: Classic system design.*

**The question:** Tatkal booking opens at 10:00 AM sharp. Millions of users hit login and search in the same minute, while the rest of the day is quiet. How do you design for a spike that happens at a known second every day?

## What's really happening

Most traffic spikes are a surprise. This one isn't. You know the exact second it will happen, every day. That changes the design completely: you don't need to react fast, you can prepare early.

Think of a stadium on match day. They don't wait for the crowd to arrive before opening the gates. Staff, security and turnstiles are ready an hour before.

## The fixes

| Problem | Fix |
|---|---|
| Servers scale up too late | **Pre-scale** before 10:00, on a schedule, not on CPU alarms |
| Everyone logs in at 10:00 | Let users **log in early**, so 10:00 only handles booking |
| Search hits the database millions of times | **Cache** train and route data, which barely changes, close to users |
| More users than the system can serve at once | A **virtual waiting room**: a fair queue that lets users in at a safe rate |
| Static pages and images use server capacity | Serve them from a **CDN** |
| Hard to know the real limit | **Load test** at full Tatkal scale before it happens |

The waiting room matters most. It's better to tell a user "you're number 4,210 in the queue" than to let everyone in and crash for all of them.

## What breaks at scale

The bottleneck moves. Fix login, and search breaks. Fix search, and seat booking becomes the hot spot. Load testing has to cover the whole journey, not one page.

## Simple diagram idea

A traffic graph across a day: flat, then a sharp spike at 10:00. Overlaid: server capacity, which rises at 9:45 (pre-scaled) and drops after 10:30.

## What I'd say in the room

1. "This spike is predictable, so I'd prepare for it rather than react: pre-scale on a schedule before 10:00."
2. "I'd move work away from 10:00: early login, cached search data, and a CDN for anything static."
3. "And I'd put a fair virtual waiting room in front, so the system admits users at a rate it can actually serve."

## Source

S2: IRCTC Tatkal booking scenario, written from publicly known Tatkal behaviour. Not based on IRCTC's internal design.

---

**Post text (copy and paste):**

```
System design question:

Tatkal booking opens at 10:00 AM sharp. Millions of users arrive in the same minute. The rest of the day is quiet. How do you design for it?

The good news: this spike is predictable. So prepare, don't react.

How I'd do it:
• Pre-scale on a schedule before 10:00
• Let users log in early, so 10:00 is only for booking
• Cache train and route data close to users
• Put a fair virtual waiting room in front

Better "you're number 4,210 in the queue" than a crash for everyone.

How would you design it?

#SystemDesign #SoftwareArchitecture #Scalability #IRCTC
```
