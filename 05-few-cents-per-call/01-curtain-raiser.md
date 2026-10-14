# 1. A Few Cents per Question. Why Is the Sale-Day Bill So Big?

![Cover](images/01-curtain-raiser-cover.png)

*What's a few cents between friends? series: the curtain raiser*

"It's only a few cents per question."

Picture a shopping site that adds an AI assistant to every product page. Shoppers ask: "Does this phone support dual SIM?", "Will this fit a 6-foot bed?", "Is it waterproof?" In the pilot, the bill is tiny. A few cents a question. Finance barely notices.

Then the big sale arrives. Traffic jumps twenty times. The same questions come from lakhs of shoppers in a single day, and every one of them is answered live, at full price, for every shopper, for free.

The bill for that week arrives in finance's inbox like a party invitation nobody asked for.

## Why small numbers stop being small

AI is paid for per use, not per licence. That sounds safe until you remember that use always grows, and grows fastest on your busiest days. The bill isn't only an engineering problem. It's a set of business decisions nobody made on purpose.

- **Nobody decided who pays.** The assistant is free for every shopper, on every product, every day. Is it a feature, or a cost nobody owns?
- **Renting looked cheap, until the sale.** Paying per call is perfect for a pilot. At sale-day volume, running a model yourself might cost less. Or more. Nobody checked.
- **Everything runs "right now".** Product descriptions that could be rewritten overnight, at a lower rate, are generated live at full price.
- **Some features earn their bill. Some don't.** Size advice cuts returns. "Fun product facts" costs lakhs and sells nothing.
- **Next year's budget is a guess.** More shoppers, cheaper models, new features: will the bill grow or shrink?

The engineering basics (tokens, caching, smaller models, limits that stop a runaway bill) are in [write-up 10 of my #JustAddRAG series](https://www.linkedin.com/pulse/10-few-cents-per-question-so-why-finance-calling-cost-arpit-jain-bqppf/). This series is about the money decisions on top.

A few cents is a lovely number on a slide. Multiplied by a sale day, it's a different conversation.

## What sits behind "a few cents"

The price per question is the visible part. What decides the real bill is a handful of business decisions: who pays for the feature, whether you rent the model or run it yourself, which jobs need an answer right now, which features are worth their cost, and how you plan next year's budget. The receipt on the cover is the full list.

## This is a series: here's what's coming

This write-up is the first in a series. Each one takes one line of the bill and goes deep, with the same shopping assistant every time. A few of the questions it will answer:

- What should you charge for your AI feature? (Pricing)
- API or your own GPUs? (Rent or own)
- Does every answer need to come right now? (Batch vs real time)
- Which AI features are worth what they cost? (Value per feature)
- How do you forecast next year's AI bill? (Forecasting)

...and a final write-up on estimating the real cost before you build.

## Take this to your next kickoff meeting

1. Multiply the cost per question by your sale-day traffic, not your pilot traffic.
2. Ask who pays for the AI feature: the customer, a product budget, or nobody yet.
3. List which AI jobs need an answer right now, and which could wait until tonight.

AI costs aren't scary because they're big. They're scary because nobody multiplied them in advance.

Next write-up (2): **What should you charge for your AI feature?** (Pricing)

Follow me for the next one. And tell me: what's the biggest "only a few cents" surprise you've seen?

---

**Post text (copy and paste):**

```
"It's only a few cents per question."

Then the big sale arrives. Twenty times the traffic. Every answer live, at full price, free for every shopper.

Assume a few cents stays small, and you pay for it:
• Cost: a sale-day bill nobody multiplied in advance
• Waste: features that cost lakhs and sell nothing
• Risk: a budget built on a guess
• Trust: finance stops saying yes to the next AI idea

Write-up 1 in my new series, What's a few cents between friends? (#FewCentsMore): why small AI costs stop being small, the money decisions behind the bill, and three things to take to your next kickoff meeting.

What's the biggest "only a few cents" surprise you've seen?

#AIEngineering #GenAI #FinOps #AICost #FewCentsMore
```

**Series index (post as the first comment, then pin it):**

```
📌 What's a few cents between friends?: series index

1. A few cents per question. Why is the sale-day bill so big? (you're here)
2. What should you charge for your AI feature? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
