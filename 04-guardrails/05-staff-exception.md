# 5. What If Your Guardrails Lock Out Your Own Team? | Staff Exceptions

![Cover](images/05-staff-exception-cover.png)

*Just tell it not to series: staff exceptions*

It's 9 pm. A pharmacist is on an emergency call and needs an answer about overdose risk, fast.

The assistant refuses. It's the right refusal for a customer typing into a shop chat. For a pharmacist on a live call, it's the wrong door, locked at the wrong moment.

The fence was built for strangers. Nobody remembered the fire brigade.

## The fire door in the castle wall

A castle needs a way for its own people in and out, especially in an emergency. A wall with no gate for the fire brigade doesn't protect the castle. It just traps the people inside.

Guardrails have the same problem. A rule strict enough to stop strangers can also stop your own staff. The fix is not to remove the fence. It's to build a proper door for the people who should use it.

## Three parts of a good staff door

- **Identity comes from a login, not from a sentence.** "I'm a pharmacist" typed into a chat proves nothing, because anyone can type it. Staff should sign in, and the system should check their role.
- **Break-glass access for emergencies.** A time-limited path that a verified person can open in an emergency. It is logged, and it expires on its own.
- **A vetted fallback.** When the bot can't answer, it should route to a human pharmacist or to emergency services, and show information from approved sources only.

## Every override needs a record

Each exception should answer four questions in the log: who, when, why, and what was answered. Then review the log regularly. An override that nobody reviews slowly becomes the back door everyone uses.

This is also where people quietly cheat. If staff get annoyed by the fence, they share a login, or they type a fake job title. Good design makes the honest path easy, so nobody needs the dishonest one.

## What a staff door can't do

A staff door is a weak point, so it needs more care than the front gate. Keep exceptions narrow, test them the same way you test the front door (write-up 4), and take them away when a person changes role.

## This is a series: here's what's coming

The same pharmacy assistant, one layer at a time. Next:

- How strict is too strict? (Safety vs usefulness)

...and a finale with a guardrails checklist.

## Take this to your next kickoff meeting

1. Decide who can get past the fence, and make them prove it with a login, not a typed sentence.
2. Give every emergency override an expiry time and a log entry.
3. Review the override log every week, and remove access the moment someone changes role.

A fence should stop strangers, not the fire brigade.

Next write-up (6): **How strict is too strict?** (Safety vs usefulness)

Follow me for the next one. Who in your team would need a way through the fence in an emergency?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)
- **Series 3, Just put the rules in the prompt:** [start here](https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f) or jump to [the finale](https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf)
- **Series 20, Today in AI** (ongoing): [start here](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/) or read [the latest issue](https://www.linkedin.com/pulse/today-ai-011-text-to-speech-fits-your-phone-internet-needed-jain-1ipuf)

---

**Post text (copy and paste):**

```
9 pm. A pharmacist on an emergency call needs an answer, fast.

The assistant refuses. The fence was built for strangers.

A fence should stop strangers, not the fire brigade.

Write-up 5 in my series, Just tell it not to (#JustTellItNot): how to give your own team a proper staff door, with a login, an expiry time and a log.

Missed the last series? Start with "Why did the AI promise a full refund on a non-refundable ticket?" https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f or jump to the finale: https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf

Who in your team would need a way through the fence in an emergency?

#AIEngineering #GenAI #AISafety #Guardrails #JustTellItNot
```

**Series index (post as the first comment, then pin it):**

```
📌 Just tell it not to: series index

1. Why didn't "Please don't give medical advice" work?
2. What should you check before the question reaches the model?
3. What should you check before the answer reaches the customer?
4. What if a customer tries to trick it?
5. What if your guardrails lock out your own team? (you're here)
6. How strict is too strict? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
