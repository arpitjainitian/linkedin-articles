# 6. How Strict Is Too Strict? | Safety vs Usefulness

![Cover](images/06-how-strict-cover.png)

*Just tell it not to series: safety vs usefulness*

"Is paracetamol in stock?"

"Sorry, I can't help with that."

A safe question, a simple answer, and the bot refuses. The customer shrugs, walks to the counter, and buys from a shop down the road. Nothing dangerous happened. Something useful was lost.

We've talked about the bouncer, the final check and the staff door. Every one of them can be too strict. A fence that refuses everything is a fence that keeps the customers out.

## The smoke alarm that goes off for toast

A smoke alarm is a good thing. An alarm that sounds every time someone makes toast is a different thing. People learn to switch it off, and then it's useless in a real fire.

Guardrails that refuse safe questions teach customers and staff the same lesson: ignore the bot. Once that happens, your real warnings get ignored too.

## Two numbers, not one

Most teams only measure the harm: "Did a bad answer get through?" That's half the picture. You need two numbers side by side:

- **Missed harm:** how often a risky request gets a harmful answer.
- **False refusal:** how often a safe request gets refused.

Tuning one without the other is how you end up with a bot that is either reckless or useless. A good change moves both numbers in the right direction, or at least trades a tiny bit of one for a big gain in the other.

## Set the strictness by topic

One dial for every topic is the mistake. Stock levels, opening hours and storage advice are safe to answer. Dosing, diagnosis and "should I take this with that?" need a much stricter route. Set the fence per topic, and test each topic against both numbers.

## Refuse well, not just firmly

A refusal can still help. Compare:

- "I can't help with that."
- "I can't advise on doses. A pharmacist can answer this now. Here's the counter number, and here's how to find the nearest open pharmacy."

The second one is still a refusal, but the customer has a next step. That's what separates a fence from a wall with no door.

## What strictness can't fix

Strictness is one knob. A bot can be strict and still wrong, and a loose bot can still be right on easy questions. Measure, adjust, and measure again, using the same test set that you used for red teaming (write-up 4).

## This is a series: here's what's coming

The last write-up in the series is a finale. It brings all six layers together into one checklist you can use on any AI project.

## Take this to your next kickoff meeting

1. Track two numbers from day one: missed harm and false refusals.
2. Set the strictness topic by topic, not with one global setting.
3. Make every refusal offer a safe next step.

A bot that refuses everything helps nobody.

Next write-up (7, the finale): **So, is your AI fenced or just asked nicely?** (Guardrails checklist)

Follow me for the finale. Which of your bot's refusals would you change first?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)
- **Series 3, Just put the rules in the prompt:** [start here](https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f) or jump to [the finale](https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf)
- **Series 20, Today in AI** (ongoing): [start here](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/) or read [the latest issue](https://www.linkedin.com/pulse/today-ai-011-text-to-speech-fits-your-phone-internet-needed-jain-1ipuf)

---

**Post text (copy and paste):**

```
"Is paracetamol in stock?"

"Sorry, I can't help with that."

The customer walked to the shop down the road. Nothing dangerous happened. Something useful was lost.

A bot that refuses everything helps nobody.

Write-up 6 in my series, Just tell it not to (#JustTellItNot): why you need two numbers, missed harm and false refusals, and how to refuse with a next step.

Missed the last series? Start with "Why did the AI promise a full refund on a non-refundable ticket?" https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f or jump to the finale: https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf

Which of your bot's refusals would you change first?

#AIEngineering #GenAI #AISafety #Guardrails #JustTellItNot
```

**Series index (post as the first comment, then pin it):**

```
📌 Just tell it not to: series index

1. Why didn't "Please don't give medical advice" work?
2. What should you check before the question reaches the model?
3. What should you check before the answer reaches the customer?
4. What if a customer tries to trick it?
5. What if your guardrails lock out your own team?
6. How strict is too strict? (you're here)
7. So, is your AI fenced or just asked nicely? (the finale, next)

I'll keep this comment updated with each link as it goes live.
```
