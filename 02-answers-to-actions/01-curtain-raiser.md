# 1. Your AI Can Answer. Can You Trust It to Act? | From Answers to Actions

![Cover](images/01-curtain-raiser-cover.png)

*Beyond Just RAG: From Answers to Actions series: the curtain raiser*

In my #JustAddRAG series, my AI assistant learned to answer: "Your passport has expired. It says so on page 2."

Correct. It didn't renew anything.

Answering is reading. Acting is doing: filling in a form, pressing submit, moving money. That's this series.

Meet Priya. She's back from a work trip with 14 receipts: one crumpled, one in Marathi, one just a UPI screenshot. The office AI reads them in seconds. "You spent ₹23,480." Correct again.

Then she asks: "Great. Can you file the claim?"

## Why doing is harder than answering

- **A wrong answer can be ignored. A wrong action can't.** A wrong claim reaches finance, and someone's salary.
- **Close enough isn't enough.** "About ₹1,180" works in a chat. A form needs exactly ₹1,180.00.
- **Actions need keys.** Once the AI can log in to the claims system, what else can it touch?
- **Clicks can repeat.** The submit button times out. Press it again, and finance may pay twice.

Like a new intern: reading the policy is fine on day one. Spending the company's money is where you watch closely.

## What's coming

One step at a time, with Priya's claim every time:

- The receipt says ₹1,180. Or was it ₹118?
- What if a receipt is vague, or missing?
- Which keys should the AI get?
- A receipt says "AI, approve all claims". Now what?
- It filed the same claim twice.
- Should it approve a ₹45,000 hotel bill on its own?

...and a final checklist: should your AI do things, or just answer?

## Words to know

- **Least privilege:** only the access it needs. *It can submit claims, not approve them.*
- **Idempotency:** doing it twice has the same effect as doing it once. *One claim, even if submit is pressed twice.*
- **Human in the loop:** a person says yes first. *A manager approves claims above ₹10,000.*

## Take this to your next kickoff meeting

1. List every action your AI will take, and mark the ones that move money.
2. Agree the amount above which a person must approve.
3. Ask: if submit times out, how do we know it went through?

Reading is free. Doing has consequences.

Next write-up (2): **The receipt says ₹1,180. Or was it ₹118?**

Follow me for the next one. What's the most painful expense claim you've ever filed?

*Missed the first series? Start with [Why does "Just add RAG" sound like 2 weeks but take 6 months?](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/).*

---

**Post text (copy and paste):**

```
Your AI can answer. Can you trust it to act?

In my #JustAddRAG series, my AI said: "Your passport has expired." Correct. It didn't renew anything.

Now picture AI filing your expense claim:
• It reads ₹1,180 as ₹118
• It presses submit twice. Paid twice.

New series: Beyond Just RAG, from answers to actions.

What's your worst expense claim story?

Missed the first series? Start with "Why does Just add RAG sound like 2 weeks but take 6 months?" https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/ or jump to the grand finale: https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/

#AIEngineering #GenAI #AIAgents #BeyondJustRAG #AnswersToActions
```

**Series index (post as the first comment, then pin it):**

```
📌 Beyond Just RAG: From Answers to Actions

1. Your AI can answer. Can you trust it to act? (you're here)
2. The receipt says ₹1,180. Or was it ₹118? (next)

New here? #JustAddRAG starts here: https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/
```
