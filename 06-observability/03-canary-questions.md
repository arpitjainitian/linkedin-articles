# 3. How Do You Catch a Wrong Answer Nobody Reported? | Observability

*We'll know when it breaks series: canary questions and silent failures*

"Where's my order?"

The support bot replies: "Your order left the kitchen 20 minutes ago and is on the way."

It is yesterday's status. The order was delivered this morning.

Nobody complained. Zero complaints can mean zero checks.

## The quiet failure

A loud failure shows itself. An error page, a timeout, a crash. Everyone sees it.

A quiet failure looks like a normal answer. The customer reads it, shrugs and moves on. Some never write back at all. The wrong answer leaves no trace in the error dashboard, because nothing technically failed.

## Think of a smoke alarm that never beeps

Picture a building with a smoke alarm that is switched off. The building looks calm. Nobody smells smoke because nothing is checking the air.

A complaint is a smoke alarm that depends on someone noticing. It is late, and it only catches the people who speak up.

## Use canary questions

A **canary** is a known question with a known correct answer, asked on a schedule, in production, just like a customer would ask it. Think of the canary in a coal mine: if it stops singing, something in the air is wrong.

For the food-delivery bot, a canary might be:

- "Where's order 9931?" with the expected status: "delivered".
- "What is the refund policy for a missing item?" with the expected policy version.

Run the canaries every hour. If an answer changes from the expected result, raise an alert before a customer does.

## Watch refusals in both directions

The bot can fail by saying too much, or by saying too little. Track both:

- **Too many refusals:** "Sorry, I can't help with that," for ordinary questions.
- **Too few refusals:** answers given to questions the bot should hand to a person.

A rise in either one is a signal, even when no one complains.

## Take this to your next kickoff meeting

1. Write 10 canary questions with known answers before launch.
2. Run them on a schedule in production, and alert on any change.
3. Track refusal rate in both directions, not only errors.

A quiet system is not always a healthy one. Ask it questions you already know the answer to.

Next write-up (4): **What happens when you break it on purpose?**

Follow me for the next one. What is one question you could ask your AI every day, just to be sure?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
"Where's my order?"

The bot said: "On the way." The order was delivered that morning.

Nobody complained. Zero complaints can mean zero checks.

Write-up 3 in my series, We'll know when it breaks (#WeWillKnow): canary questions that run in production, and why refusals need watching in both directions.

What is one question you could ask your AI every day, to be sure?

#AIEngineering #GenAI #LLMOps #Observability #WeWillKnow
```

**Series index (post as the first comment, then pin it):**

```
📌 We'll know when it breaks: series index

1. It said "arriving in 5 minutes". It took an hour. Can you tell why?
2. The bill tripled. Nothing errored. Where do you look?
3. How do you catch a wrong answer nobody reported? (you're here)
4. What happens when you break it on purpose? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
