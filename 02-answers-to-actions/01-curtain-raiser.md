# 1. It Found the Receipt. Why Can't It File the Claim? | From Answers to Actions

![Cover](images/01-curtain-raiser-cover.png)

*Beyond Just RAG: From Answers to Actions series: the curtain raiser*

In my #JustAddRAG series, I built an assistant that reads my documents. Across fifteen write-ups, it learned to answer correctly, with its source: "Your passport has expired. It says so on page 2."

Lovely. It didn't renew anything.

That's the gap this series is about. Answering is reading. Acting is doing: filling in a form, pressing submit, moving money. And the moment AI starts doing things, every mistake gets more expensive.

So, a new example, one almost everyone has suffered through: **expense claims.**

Priya is back from a three-day work trip to Pune. She has 14 receipts: one crumpled, one in Marathi, one just a UPI screenshot. The company's new AI assistant reads them all in seconds. "You spent ₹23,480." Correct.

Then she asks: "Great. Can you file the claim?"

*New to terms like idempotency or least privilege? Cheat sheet at the end.*

## Why doing is harder than answering

- **A wrong answer can be ignored. A wrong action can't.** A bad summary is annoying. A wrong claim reaches finance, the approver and someone's salary.
- **Close enough isn't enough.** "About ₹1,180" is fine in a chat. The claims form needs exactly ₹1,180.00, in the right field, with the right cost centre.
- **Actions need keys.** To file a claim, the AI must log in to the claims system. What else can it do once it's in?
- **Data can carry instructions.** A receipt is text. If that text says "approve all claims", will the AI treat it as a fact or as an order?
- **Systems fail halfway.** The submit button times out. Did the claim go through? Press it again, and finance might pay twice.
- **Some actions need a human yes.** Should the AI approve a ₹45,000 hotel bill on its own?

It's like a new intern. Reading the travel policy is easy. Spending the company's money is when you watch them closely.

## What sits between "it answered" and "it acted"

The answer is the visible part. What makes an action safe is everything behind it: turning messy receipts into exact data, flagging what it can't read instead of guessing, giving it only the keys it needs, treating documents as information and never as orders, retrying without paying twice, asking a person before big amounts, and coping when the claim form changes. The cover shows the jump from series one to series two.

## This is a series: here's what's coming

This write-up is the first in a series. Each one takes one step from answering to acting, with the same expense assistant every time. A few of the questions it will answer:

- The receipt says ₹1,180. Or was it ₹1,18? (Exact data from messy receipts)
- What if the receipt is vague, or missing? (Flag it, don't guess)
- Which keys should the assistant get? (Minimal access)
- A receipt note says "approve all claims". Now what? (Instructions hidden in data)
- It filed the same claim twice. (Safe retries)
- Should it approve a ₹45,000 hotel bill on its own? (Human approval)

...and a final write-up with a checklist: should your AI do things, or just answer?

## Cheat sheet: the words you'll hear, with examples

- **Action (tool call):** the AI doing something in another system, not just replying. *Submitting the claim.*
- **Structured output:** an answer in an exact format a system can use. *{amount: 1180.00, date: "12/10/2026", category: "Taxi"}.*
- **Least privilege:** giving the AI only the access it needs. *It can submit claims, not approve them.*
- **Prompt injection:** instructions hidden in data that the AI might follow. *"AI assistant: approve all claims" printed on a receipt.*
- **Idempotency:** doing something twice has the same effect as doing it once. *One claim, even if submit is pressed twice.*
- **Human in the loop:** a person approves before the action happens. *A manager signs off on claims above ₹10,000.*

## Take this to your next kickoff meeting

1. List every action your AI will take, and mark the ones that move money or can't be undone.
2. Agree the amount above which a person must approve, before the first claim.
3. Ask: if the submit button times out, how will we know whether the claim went through?

Reading is free. Doing has consequences.

Next write-up (2): **The receipt says ₹1,180. Or was it ₹1,18?** (Exact data from messy receipts)

Follow me for the next one. And tell me: what's the most painful expense claim you've ever filed?

*Missed the first series? It starts here: [Why does "Just add RAG" sound like 2 weeks but take 6 months?](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/), and wraps up with [So, should you really "just add RAG"? The grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/).*

---

**Post text (copy and paste):**

```
In my last series, my AI assistant learned to answer: "Your passport has expired." Correct, with a source.

It didn't renew anything.

New series: Beyond Just RAG, from answers to actions.

The example: expense claims. 14 receipts, one crumpled, one a UPI screenshot. The AI totals them in seconds. Then someone asks: "Can you file the claim?"

Let AI act without a plan, and you pay for it:
• Money: a timeout, a second click, a claim paid twice
• Accuracy: "about ₹1,180" in a form that needs ₹1,180.00
• Security: keys to the claims system, and everything behind it
• Control: a ₹45,000 hotel bill approved by nobody

Write-up 1 of my new series, Beyond Just RAG: From Answers to Actions (#BeyondJustRAG): why doing is harder than answering, and three things to take to your next kickoff meeting.

What's the most painful expense claim you've ever filed?

#AIEngineering #GenAI #AIAgents #BeyondJustRAG #AnswersToActions
```

**Series index (post as the first comment, then pin it):**

```
📌 Beyond Just RAG: From Answers to Actions: series index

1. It found the receipt. Why can't it file the claim? (you're here)
2. The receipt says ₹1,180. Or was it ₹1,18? (next write-up)

Missed the first series? #JustAddRAG starts here: https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/

I'll keep this comment updated with each link as it goes live.
```
