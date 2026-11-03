# 6. So, Can You See Inside Your AI? | Observability

*We'll know when it breaks series: the finale and the checklist*

"Arriving today."

Five write-ups ago, the support bot said that, and the team learned about it a week later from an angry customer.

Here is the same bot, with the signals in place.

| Signal | Before | After |
|---|---|---|
| Why an answer was given | Question and answer only | What the bot read, and which rules applied |
| Silent change | Found in the next monthly bill | Cost and cache hit rate alert the same day |
| Wrong answer nobody reported | Found by a complaint | Canary question fails within the hour |
| Dependency failure | Queue fills, customers wait | Timeout, retry limit and a safe fallback |
| Health on the dashboard | Uptime only | Uptime and correctness, side by side |

A green dashboard tells you the bot is running. These signals tell you it is right.

## The checklist

Before you say "we'll know when it breaks", check these five:

1. **Traces:** each answer records what it read and which rules applied.
2. **Cost and cache:** cost per answer and cache hit rate are tracked and alerted.
3. **Canaries:** known questions run in production, and refusals are watched in both directions.
4. **Faults:** each key dependency has a tested timeout, retry limit and fallback.
5. **Targets and incidents:** availability and correctness targets sit together, and a wrong answer has an incident plan with a named owner.

## What to say in the kickoff meeting

- Uptime is the start of the conversation, not the end.
- A silent change often shows first in the bill. Watch it.
- Name the person who can switch the risky answer path off today.

A system you can explain is a system you can fix.

This is the end of We'll know when it breaks. Next up: Series 7, POC to production, where the demo has to survive the real world.

Follow me for the next one. Could your team explain last week's worst AI answer, step by step?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
"Arriving today." It arrived a week later.

Five signals that would have caught it:
• Traces of what the bot read
• Cost and cache hit rate, with alerts
• Canary questions in production
• Tested timeouts and fallbacks
• Correctness targets next to uptime

Finale of We'll know when it breaks (#WeWillKnow): the observability checklist, with the food-delivery support bot.

Could your team explain last week's worst AI answer, step by step?

#AIEngineering #GenAI #LLMOps #Observability #WeWillKnow
```

**Series index (post as the first comment, then pin it):**

```
📌 We'll know when it breaks: series index

1. It said "arriving in 5 minutes". It took an hour. Can you tell why?
2. The bill tripled. Nothing errored. Where do you look?
3. How do you catch a wrong answer nobody reported?
4. What happens when you break it on purpose?
5. Is it up, or is it right?
6. So, can you see inside your AI? (you're here, finale)

Next series: POC to production, "It worked in the demo".
```
