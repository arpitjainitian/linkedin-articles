# 7. So, Is Your AI Fenced or Just Asked Nicely? | The Finale

![Cover](images/07-finale-checklist-cover.png)

*Just tell it not to series: the finale*

Back to the sign on the gate: "Please don't give medical advice."

It's polite. It's clear. It's also the first thing a clever customer walks past.

Over six write-ups we've built the fence, one layer at a time, around an online pharmacy assistant. Here is the whole fence on one page.

## The layers, in order

1. **The bouncer (write-up 2).** The question is screened before the model sees it. Off-topic and risky questions get a safe route, and each block is logged.
2. **The final check (write-up 3).** The draft is checked before the customer sees it. Hints count as advice, and a safe fallback replaces a blocked draft.
3. **The trick test (write-up 4).** Your own team attacks the assistant before launch, through the chat, documents, notes and tools. The attack list runs again after every change.
4. **The staff door (write-up 5).** Verified staff get a proper way through, with a login, an expiry time and a log that someone reviews.
5. **The right strictness (write-up 6).** Each topic has its own dial, measured with two numbers: missed harm and false refusals.

The prompt sits inside all of this as a good intention, not as the wall.

## The guardrails checklist

Use this on any AI project. A "no" on any line is a gap to close.

- [ ] The important rules live in code or fixed checks, not only in the prompt.
- [ ] Questions are screened before the model, and blocked questions are logged.
- [ ] Answers are checked before the customer sees them, including hints.
- [ ] Attacks are tested through every input: chat, documents, notes and tools.
- [ ] Staff exceptions use a login, an expiry time and a log, reviewed regularly.
- [ ] Missed harm and false refusals are both measured, per topic.
- [ ] One named person owns the fence, and the test set is re-run after every change.

## What the checklist can't promise

No checklist makes an AI safe for good. Attackers adapt, your topics change, and new products bring new doors. The checklist tells you where the fence has holes today. The work is keeping the list short, testing it, and fixing what the tests find.

## Take this to your next kickoff meeting

1. Put the seven lines of the checklist on the first page of your project plan.
2. Name one owner for the fence, and one owner for the test set.
3. Before launch, run one hour of red teaming with people who didn't build the assistant.

Asking nicely is a good start. A fence is what keeps it safe.

## Thank you, and a question

This series took a sign on a gate and turned it into a fence. Which layer would you build first in your own assistant?

**Previous series:**

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)
- **Series 3, Just put the rules in the prompt:** [start here](https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f) or jump to [the finale](https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf)
- **Series 20, Today in AI** (ongoing): [start here](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/) or read [the latest issue](https://www.linkedin.com/pulse/today-ai-011-text-to-speech-fits-your-phone-internet-needed-jain-1ipuf)

---

**Post text (copy and paste):**

```
"Please don't give medical advice."

It's polite. It's clear. It's also the first thing a clever customer walks past.

A sign asks nicely. A fence is what keeps it safe.

The finale of my series, Just tell it not to (#JustTellItNot): five layers and a seven-line checklist you can use on any AI project.

Missed the last series? Start with "Why did the AI promise a full refund on a non-refundable ticket?" https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f or jump to the finale: https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf

Which layer would you build first in your own assistant?

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
6. How strict is too strict?
7. So, is your AI fenced or just asked nicely? (you're here, the finale)

Thanks for reading. Save the checklist and share it with whoever says "we already told it not to."
```
