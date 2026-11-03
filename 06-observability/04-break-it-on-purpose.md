# 4. What Happens When You Break It on Purpose? | Observability

*We'll know when it breaks series: fault testing before the weekend does it for you*

Friday, 8 pm. The tracking service slows down. Response time goes from 1 second to 40.

The support bot does what it was built to do. It waits. Then it tells customers: "I can't find your order right now." Then it tries again, and again, and the queue behind it grows.

Nobody planned for this. Nobody tested it.

Find the weak spot before Friday night does.

## Test the failure, not only the happy path

Most tests check that the bot works when everything is working. Fault testing asks a different question: what happens when one part breaks?

Think of a car's brakes. You do not wait for an emergency to learn whether they work. You test them on a quiet road, at low speed, with someone ready to stop.

## Break one part on purpose

**Fault injection** means causing a failure on purpose, in a test or a safe environment, and watching what the system does. For the food-delivery bot, the tests might:

- Make the tracking service respond after 30 seconds.
- Return an error from the refund service.
- Return an empty result from the menu service.

For each one, write down what the bot should do. For example: "Say the status is unavailable, offer a human, and stop retrying after three tries."

## Limit the damage

A failure should stay small. The **blast radius** is how far a failure spreads. Keep it small with simple limits:

- **Timeouts:** stop waiting after a set time.
- **Retry limits:** try a few times, then stop.
- **Fallbacks:** give a safe answer, such as "Your order is being checked, we will message you".

A bot with no retry limit can fill a queue in minutes. A bot with one fails quietly and safely.

## Take this to your next kickoff meeting

1. List the three services the bot depends on most, and what each failure should look like to a customer.
2. Inject one slow response and one error in a test, before launch.
3. Check that the bot stops retrying, gives a safe answer and offers a person.

A system you have never broken is a system you have not tested.

Next write-up (5): **Is it up, or is it right?**

Follow me for the next one. What does your AI do when the system behind it goes slow?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
Friday, 8 pm. The tracking service slows from 1 second to 40.

The support bot waits, retries, and fills the queue.

Nobody had tested it.

Write-up 4 in my series, We'll know when it breaks (#WeWillKnow): fault injection, blast radius and retry limits, tested on a quiet afternoon.

What does your AI do when the system behind it goes slow?

#AIEngineering #GenAI #LLMOps #Observability #WeWillKnow
```

**Series index (post as the first comment, then pin it):**

```
📌 We'll know when it breaks: series index

1. It said "arriving in 5 minutes". It took an hour. Can you tell why?
2. The bill tripled. Nothing errored. Where do you look?
3. How do you catch a wrong answer nobody reported?
4. What happens when you break it on purpose? (you're here)
5. Is it up, or is it right? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
