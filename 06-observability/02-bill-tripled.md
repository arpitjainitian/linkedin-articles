# 2. The Bill Tripled. Nothing Errored. Where Do You Look? | Observability

*We'll know when it breaks series: watching the signals that stay quiet*

On Monday, the food-delivery support bot's monthly bill tripled.

No alerts. No errors. Every answer looked normal.

The only change was one line added to the top of the prompt: "Today's date is 14 March, 9:42 am." The team wanted the bot to know the time. The line changed every few minutes.

Silent changes often show up in cost first.

## Why one line cost three times more

Many AI providers can reuse the start of a prompt that did not change. This is called **prompt caching**. The reused part is billed at a lower rate.

A timestamp at the top changes the start of every prompt. The reuse stopped. Cache hits fell from about 80% to about 5%, and the bot paid full price for the same text, again and again.

The answers were fine. The cost was not.

## Think of a shop with a moving queue

Imagine a shop where the same customers always stand in the same line. Staff prepare their orders ahead, so service is fast and cheap. Then the shop moves one sign, and every customer has to re-queue from the start.

Nobody is rude. The shop just does the same work over and over.

## Cost and cache are health signals

Plain logs show what was asked and answered. They rarely show these signals, so add them:

- **Cost per answer:** a jump with no change in traffic is a warning.
- **Cache hit rate:** a sharp drop means something near the top of the prompt changed.
- **Tokens per request:** a rise means the bot is reading more than it used to.

Set a simple alert on each. The alert does not tell you why, but it tells you where to look first.

## Take this to your next kickoff meeting

1. Track cost per answer and cache hit rate next to answer quality.
2. Keep changing content, like dates, below the stable part of the prompt.
3. Alert on a cost jump, even when no errors appear.

A bill is a monitor too. Read it.

Next write-up (3): **How do you catch a wrong answer nobody reported?**

Follow me for the next one. Which number in your AI project would you notice first if it jumped?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)

---

**Post text (copy and paste):**

```
One line at the top of the prompt: "Today's date is..."

The support bot's bill tripled. No errors. No alerts.

Cache hits fell from about 80% to 5%. The answers were fine. The cost was not.

Write-up 2 in my series, We'll know when it breaks (#WeWillKnow): why cost and cache hit rate are health signals, and why a timestamp at the top can cost you.

Which number would you notice first if it jumped?

#AIEngineering #GenAI #LLMOps #Observability #WeWillKnow
```

**Series index (post as the first comment, then pin it):**

```
📌 We'll know when it breaks: series index

1. It said "arriving in 5 minutes". It took an hour. Can you tell why?
2. The bill tripled. Nothing errored. Where do you look? (you're here)
3. How do you catch a wrong answer nobody reported? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
