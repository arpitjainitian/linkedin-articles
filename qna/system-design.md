# Q&A track 2: System design (one question per post)

A separate, ongoing series. Each post takes **one** system design question (the kind asked in architect interviews and design reviews) and answers it in plain words: the requirement, the key trade-off, a simple diagram idea, and a short "what I'd say in the room" answer.

Questions are collected from posts and discussions shared over time. They are rephrased in my own words, and each source is credited below.

| # | Question | Topic | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 1 | Every morning at exactly 9:00 AM, a cron job starts 50 worker nodes that pull reports from a shared relational database. The connection pool runs out instantly, and the whole app is down for 15 minutes. What's happening, and how do you fix it? | Thundering herd, connection pool exhaustion, scheduled load spikes | L3 | | S1 | Planned |
| 2 | During a holiday sale, the third-party fraud-check API your checkout depends on slows from 50 ms to 15 seconds per call. Checkout threads pile up waiting, and the whole e-commerce platform crashes. How do you stop one slow dependency from taking everything down? | Cascading failure, timeouts, circuit breaker, bulkhead, graceful degradation | L3 | #JustAddRAG: performance (fallbacks, graceful degradation) | S1 | Planned |
| 3 | Tatkal booking opens at 10:00 AM sharp. Millions of users hit login and search in the same minute, while the rest of the day is quiet. How do you design for a spike that happens at a known second every day? | Predictable spikes, pre-scaling, virtual waiting room, caching | L3 | | S2 | Planned |
| 4 | A train has 60 Tatkal seats and 50,000 people click "Book" in the same few seconds. How do you make sure no seat is ever sold twice? | Inventory consistency, locking, atomic decrement, oversell prevention | L4 | | S2 | Planned |
| 5 | A user picks a seat, then sits on the payment page for minutes. Should the seat be held, for how long, and what happens when the hold expires or payment fails? | Seat holds, TTL reservations, payment timeouts, release and reallocation | L3 | | S2 | Planned |
| 6 | Payment succeeds at the bank, but the booking confirmation never arrives because of a timeout. The money is gone, the ticket isn't. How do you design so this never leaves a user stuck? | Distributed transactions, idempotency, saga, reconciliation, refunds | L4 | | S2 | Planned |
| 7 | Bots and automation scripts book Tatkal tickets in milliseconds, while real users can't get past login. How do you keep it fair without blocking genuine users? | Bot detection, rate limiting, CAPTCHA, fair queuing | L3 | #JustAddRAG: permissions and security | S2 | Planned |
| 8 | Users hit refresh and "Book" repeatedly when the site is slow, multiplying the load and creating duplicate requests. How do you handle retries and double clicks safely? | Idempotency keys, retry storms, client backoff | L3 | #JustAddRAG: performance | S2 | Planned |
| 9 | Seat availability is shown on millions of screens and changes every second during Tatkal. How fresh does it need to be, and how do you serve it without hammering the booking database? | Read/write separation, caching, eventual consistency, CQRS | L4 | | S2 | Planned |
| 10 | At 10:00 AM, the payment gateway starts failing for a large share of users. How do you protect the booking system and give users a fair second chance? | Third-party dependency failure, circuit breaker, queue-based retry, fairness | L4 | Q2 (slow fraud API) | S2 | Planned |

## Sources

- **S1:** shared directly by Arpit (no link).
- **S2:** IRCTC Tatkal booking scenarios, written from publicly known Tatkal behaviour (fixed opening time, small quota, huge demand). Not based on IRCTC's internal design.

## Rules for this series

- One question per post. No fixed schedule.
- Questions rephrased in my words; source credited in the post.
- Each answer covers: requirements, the core trade-off, components, what breaks at scale, and a 3-line "interview answer".
- Link to a related AI write-up where the question touches AI systems.
