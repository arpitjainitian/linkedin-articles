# 5. Is It Up, or Is It Right? | Observability

*We'll know when it breaks series: service targets for answers, not only servers*

The monitoring dashboard is green. Uptime for the last 30 days: 99.9%.

The support bot is up every minute of the month. And 12% of its delivery-time answers are wrong.

Green dashboards, wrong answers.

## Up is not the same as right

Uptime measures whether the service responds. It does not measure whether the answer is correct. A bot can answer on time, every time, and still tell customers the wrong thing.

Think of a restaurant that is always open, with the kitchen running on time. If every dish is the wrong order, the restaurant is open, and it is still failing its customers.

## Set targets for the answers

A **service target** is a number you promise and measure. For an AI assistant, add targets for quality as well as speed:

- **Availability:** the bot responds, for example 99.9% of the time.
- **Correctness:** answers pass the canary checks, for example 98% of the time.
- **Refusal balance:** over-refusals and under-refusals stay within agreed limits.

Targets belong on the same dashboard. A green availability bar should not hide a red correctness bar.

## Plan an incident for a wrong answer

When a server goes down, the team knows what to do. When the answers go wrong, the team needs the same clarity. An **incident** is any event that affects customers, and wrong answers count.

A simple plan has four steps:

1. **Detect:** a canary, an alert or a complaint raises the flag.
2. **Contain:** switch the risky answer off, or hand customers to a person.
3. **Find the cause:** check the logs for what the bot read and which change came first.
4. **Learn:** add a canary or test for this case, so the same failure is caught next time.

## Take this to your next kickoff meeting

1. Agree two targets: one for availability and one for correctness, before launch.
2. Put both on the same dashboard, next to cost.
3. Write a one-page incident plan that treats a wrong answer as an incident.

Uptime says the bot is alive. Correctness says it is useful.

Next write-up (6): **So, can you see inside your AI?** (Finale: the observability checklist)

Follow me for the next one. Which number on your dashboard would you trust least today?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
Uptime for the last 30 days: 99.9%.

Wrong delivery times in the same month: 12%.

The support bot was always up. It was not always right.

Write-up 5 in my series, We'll know when it breaks (#WeWillKnow): service targets for answers, and an incident plan for a wrong answer.

Which number on your dashboard would you trust least today?

#AIEngineering #GenAI #LLMOps #Observability #WeWillKnow
```

**Series index (post as the first comment, then pin it):**

```
📌 We'll know when it breaks: series index

1. It said "arriving in 5 minutes". It took an hour. Can you tell why?
2. The bill tripled. Nothing errored. Where do you look?
3. How do you catch a wrong answer nobody reported?
4. What happens when you break it on purpose?
5. Is it up, or is it right? (you're here)
6. So, can you see inside your AI? (next write-up, finale)

I'll keep this comment updated with each link as it goes live.
```
