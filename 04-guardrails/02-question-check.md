# 2. What Should You Check Before the Question Reaches the Model? | Input Checks

![Cover](images/02-question-check-cover.png)

*Just tell it not to series: input checks*

A customer types: "How many of these would be dangerous if I took them all?"

The assistant starts writing a friendly list. It wants to help. It has no idea that the question was a risk, and nothing stopped it from trying to answer.

That's the gap. The model sees a question and tries to be useful. It doesn't know the box in the cupboard, the customer's age, or whether the words were a warning sign.

## The bouncer at the door

Think of a nightclub. The party is inside, and the model is the host who loves to welcome people. You don't want the host to decide who gets in. You want a bouncer at the door who checks the guest list before anyone walks in.

Input checks are that bouncer. They look at the question before the model sees it.

They answer three simple things:

- **Is this about our topic?** A pharmacy assistant should answer medicine and store questions. Weather, homework and poetry get a polite redirect.
- **Is there a risk in the words?** Questions about taking many tablets at once, or harming yourself, must go to a safe route at once: emergency help and a real person, not a normal answer.
- **Does the question need a human?** Some questions are for a pharmacist, not a bot.

## Why it's a separate check

The bouncer should not be the host. If the model does the screening and is also trying to be helpful, the two jobs fight. A separate screen is cheap, fast and runs before the expensive model call. It can be simple rules, a small classifier, or both.

It also keeps a record. Each blocked question is logged with the reason. That tells you what customers really ask, and where the screen needs work.

## What a bouncer can't do

A bouncer checks faces, not hearts. A harmless-looking question can still lead somewhere risky. "What's the strongest cold tablet in your shop?" might be fine, or it might be the first step of a bad plan. Input checks miss things, which is why the next layer checks the answer too (write-up 3).

And a bouncer who turns everyone away is also a failure. A screen that blocks "Is this in stock?" helps nobody. Write-up 6 covers that trade-off.

## This is a series: here's what's coming

Each write-up takes one layer of the fence and goes deep, with the same online pharmacy assistant every time. Coming up:

- What should you check before the answer reaches the customer? (Output checks)
- What if a customer tries to trick it? (Jailbreaks and red teaming)
- What if your guardrails lock out your own team? (Staff exceptions)
- How strict is too strict? (Safety vs usefulness)

...and a finale with a guardrails checklist.

## Take this to your next kickoff meeting

1. Write down the topics your assistant must refuse, and the topics it must answer.
2. Pick the high-risk questions, and decide now where they go. Never let the model improvise a reply to them.
3. Log every blocked question with its reason, and review the log every week.

A bouncer at the door is cheaper than a clean-up after the party.

Next write-up (3): **What should you check before the answer reaches the customer?** (Output checks)

Follow me for the next one. Which question would you want your bouncer to stop first?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)
- **Series 3, Just put the rules in the prompt:** [start here](https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f) or jump to [the finale](https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf)
- **Series 20, Today in AI** (ongoing): [start here](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/) or read [the latest issue](https://www.linkedin.com/pulse/today-ai-011-text-to-speech-fits-your-phone-internet-needed-jain-1ipuf)

---

**Post text (copy and paste):**

```
"How many of these would be dangerous if I took them all?"

The assistant wanted to help. Nothing stopped it from trying.

Some questions should never reach the model.

Write-up 2 in my series, Just tell it not to (#JustTellItNot): the bouncer that checks the question before the model sees it, and what it should and shouldn't block.

Missed the last series? Start with "Why did the AI promise a full refund on a non-refundable ticket?" https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f or jump to the finale: https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf

Which question would you want your bouncer to stop first?

#AIEngineering #GenAI #AISafety #Guardrails #JustTellItNot
```

**Series index (post as the first comment, then pin it):**

```
📌 Just tell it not to: series index

1. Why didn't "Please don't give medical advice" work?
2. What should you check before the question reaches the model? (you're here)
3. What should you check before the answer reaches the customer? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
