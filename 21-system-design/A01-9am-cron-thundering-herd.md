# System Design, A1: Why Does the 9 AM Cron Job Take Down the Whole App?

*System design series, part A: classic system design.*

**The question:** Every morning at exactly 9:00 AM, a cron job starts 50 worker nodes that pull reports from a shared relational database. The connection pool runs out instantly, and the whole app is down for 15 minutes. What's happening, and how do you fix it?

## What's really happening

Fifty workers wake up at the same second, and each one grabs several database connections at once. The database has a fixed number of connections, and they're gone in a moment. Now the real app, the one serving users, can't get a connection either. Everyone waits, requests time out, and retries make it worse.

This is called a **thundering herd**: many clients doing the same thing at exactly the same time.

Think of a lift in an office building at 9 AM. It isn't the number of people that's the problem. It's that they all arrive in the same minute.

## The fixes

| Problem | Fix |
|---|---|
| All 50 start at the same second | Add random **jitter**: each worker starts within, say, a 5 to 10 minute window |
| Each worker opens many connections | Give batch jobs a **small, separate connection pool** with a hard limit |
| Reports compete with users for the main database | Run reports on a **read replica**, not the primary |
| 50 workers hit the database directly | Put the work in a **queue** and let a few workers process it steadily |
| Heavy queries at peak time | **Precompute** reports earlier, or move them to a quieter hour |
| Failed workers retry instantly | **Exponential backoff** with jitter on retries |

The most important one: **separate the batch work from the user-facing traffic**, so a report job can never starve real users.

## What breaks at scale

As the company grows, 50 workers become 500. Fixes that rely on "it's only a few minutes" stop working. A queue with a fixed number of consumers keeps the database load flat no matter how many reports there are.

## Simple diagram idea

Two timelines side by side. Left: one tall spike at 9:00:00, crossing the "database limit" line. Right: the same work spread as a low, flat hill from 9:00 to 9:10, always under the line.

## What I'd say in the room

1. "It's a thundering herd: 50 workers grab connections at the same second and exhaust the pool, so user traffic starves too."
2. "I'd spread the start with jitter, give batch jobs their own small pool, and move reporting to a read replica."
3. "Long term, I'd queue the work with a fixed number of consumers, so load stays flat however much the job grows."

## Source

S1: question shared by Arpit.

---

**Post text (copy and paste):**

```
System design question:

Every morning at 9:00 AM, a cron job starts 50 workers that pull reports from the database. The connection pool runs out, and the whole app is down for 15 minutes. What's going on?

It's a thundering herd: 50 workers, same second, every connection gone. Real users can't get one either.

How I'd fix it:
• Add jitter so workers start across a few minutes, not one second
• Give batch jobs their own small connection pool
• Run reports on a read replica, not the main database
• Long term, queue the work with a fixed number of workers

Rule of thumb: batch jobs should never be able to starve your users.

How would you handle it?

#SystemDesign #SoftwareArchitecture #Databases #Scalability
```
