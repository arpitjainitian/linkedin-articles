# System Design, A7: Bots Book in Milliseconds, Real Users Can't Log In. How Do You Keep It Fair?

*System design series, part A: classic system design.*

**The question:** Bots and automation scripts book Tatkal tickets in milliseconds, while real users can't get past login. How do you keep it fair without blocking genuine users?

## What's really happening

A script can fill a form and click "Book" faster than any human. It can also open many sessions at once. If the system treats every request the same, the fastest machine wins every time.

The hard part is the other side: genuine users on slow phones and shared networks must not be blocked by mistake.

Think of a concert ticket counter where some people send ten friends to stand in ten lines. The fix isn't to close the counter. It's to check that each ticket goes to a real person, one per person.

## The fixes, in layers

| Layer | What it does |
|---|---|
| **Rate limits** | Cap how many requests one account, device or IP can make per minute |
| **Bot signals** | Look at behaviour: impossibly fast form filling, identical timing, scripted patterns |
| **Challenges** | Show a CAPTCHA or extra check only to suspicious traffic, not everyone |
| **Account rules** | Verified accounts, limits on bookings per account per day |
| **Fair queue** | A waiting room where position is assigned, not won by speed |
| **Booking window rules** | For example, require login a few minutes before opening |

No single check works alone. Bots adapt. Layers make it expensive to cheat.

## The key trade-off

Every check you add slows down real users too. So apply the heavy checks only where the risk is: suspicious behaviour, not every visitor.

## What breaks at scale

Blocking by IP fails when thousands of real users share one network, like an office or a mobile carrier. Device and behaviour signals scale better than IP lists.

## Simple diagram idea

A funnel of traffic passing three filters: rate limit, behaviour check, challenge-if-suspicious. Real users pass through with almost no friction. Bot traffic drops at each layer.

## What I'd say in the room

1. "Speed shouldn't decide who wins, so I'd remove the advantage of being fast and many."
2. "Layers: rate limits per account and device, behaviour-based bot detection, and challenges only for suspicious traffic."
3. "Plus a fair queue where position is assigned, so a script gains nothing by clicking first."

## Related

- #JustAddRAG write-up 8: "Can the intern ask your AI about the CEO's salary?" (permissions and security)

## Source

S2: IRCTC Tatkal booking scenario, written from publicly known Tatkal behaviour. Not based on IRCTC's internal design.

---

**Post text (copy and paste):**

```
System design question:

Bots book Tatkal tickets in milliseconds. Real users can't get past login. How do you keep it fair without blocking genuine users?

If speed decides who wins, the fastest script always wins.

How I'd design it:
• Rate limits per account and device
• Bot detection based on behaviour, not just IP
• Challenges only for suspicious traffic, not everyone
• A fair queue where your place is assigned, not won by clicking first

Make cheating expensive. Keep honest users fast.

How would you design it?

#SystemDesign #Security #Scalability #IRCTC
```
