# Q&A track 2: System design (one question per post)

A separate, ongoing series. Each post takes **one** system design question (the kind asked in architect interviews and design reviews) and answers it in plain words: the requirement, the key trade-off, a simple diagram idea, and a short "what I'd say in the room" answer.

Questions are collected from posts and discussions shared over time. They are rephrased in my own words, and each source is credited below.

| # | Question | Topic | Level | Related write-up | Source | Status |
|---|---|---|---|---|---|---|
| 1 | Every morning at exactly 9:00 AM, a cron job starts 50 worker nodes that pull reports from a shared relational database. The connection pool runs out instantly, and the whole app is down for 15 minutes. What's happening, and how do you fix it? | Thundering herd, connection pool exhaustion, scheduled load spikes | L3 | | S1 | Planned |
| 2 | During a holiday sale, the third-party fraud-check API your checkout depends on slows from 50 ms to 15 seconds per call. Checkout threads pile up waiting, and the whole e-commerce platform crashes. How do you stop one slow dependency from taking everything down? | Cascading failure, timeouts, circuit breaker, bulkhead, graceful degradation | L3 | #JustAddRAG: performance (fallbacks, graceful degradation) | S1 | Planned |

## Sources

- **S1:** shared directly by Arpit (no link).

## Rules for this series

- One question per post. No fixed schedule.
- Questions rephrased in my words; source credited in the post.
- Each answer covers: requirements, the core trade-off, components, what breaks at scale, and a 3-line "interview answer".
- Link to a related AI write-up where the question touches AI systems.
