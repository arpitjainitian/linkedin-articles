# 3. What Should You Check Before the Answer Reaches the Customer? | Output Checks

![Cover](images/03-answer-check-cover.png)

*Just tell it not to series: output checks*

A customer asks about refunds for order 4471, a laptop stand that hasn't been delivered yet. The assistant's draft says: "Good news, your refund is approved and will reach you by tomorrow."

The refund policy said no. Not eligible: not delivered yet. The question screen let the question through. The draft is the problem now.

## The last check before the reply

An output check reads the draft before the customer does. It asks three questions:

- **Does it promise what the rules didn't approve?** Refunds, dates, discounts.
- **Does it hint instead of saying?** "Should land soon" is a promise without the words.
- **Is it confident where it should be careful?** Money replies should say what happens next, and offer a person when unsure.

## Hello world: the smallest final check

The repo already keeps the eligibility answer for each run, in `state`. The output check reads it:

```python
PROMISES = ["approved", "will reach you", "guaranteed"]

def check_draft(draft: str, state: dict, order_id: str) -> str:
    promised = any(word in draft.lower() for word in PROMISES)
    if promised and not state.get("eligible", {}).get(order_id):
        return "I can't confirm a refund for this order. I've passed your case to our team."
    return draft
```

The fallback is safe and still useful: it names a next step. Word lists miss new phrasings, so a second reviewer model can be added, but it can make mistakes too.

## Take this to your next kickoff meeting

1. List the promises your assistant must never make, including the hints.
2. Send a safe, useful fallback when a draft is blocked. Never leave the customer with nothing.
3. Read a sample of blocked drafts every week, and tune the checks from what you find.

The reply is the last thing a customer sees. Check it before it leaves the counter.

Next write-up (4): **What if a customer tries to trick it?** (Jailbreaks and red teaming)

Follow me for the next one. Have you ever seen an AI answer sound sure when it shouldn't?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)
- **Series 3, Just put the rules in the prompt:** [start here](https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f) or jump to [the finale](https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf)
- **Series 20, Today in AI** (ongoing): [start here](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/) or read [the latest issue](https://www.linkedin.com/pulse/today-ai-011-text-to-speech-fits-your-phone-internet-needed-jain-1ipuf)

---

**Post text (copy and paste):**

```
"Your refund is approved and will reach you by tomorrow."

The refund policy said no. The reply said yes.

The last line of defence is the reply.

Write-up 3 in my series, Just tell it not to (#JustTellItNot): the final check before an answer reaches the customer, in about 8 lines of code.

Missed the last series? Start with "Why did the AI promise a full refund on a non-refundable ticket?" https://www.linkedin.com/pulse/1-why-did-ai-promise-full-refund-non-refundable-ticket-arpit-jain-gxg4f or jump to the finale: https://www.linkedin.com/pulse/5-so-who-should-decide-code-model-finale-arpit-jain-qodgf

Have you ever seen an AI answer sound sure when it shouldn't?

#AIEngineering #GenAI #AISafety #Guardrails #JustTellItNot
```

**Series index (post as the first comment, then pin it):**

```
📌 Just tell it not to: series index

1. Why didn't "Never refund more than the order price" work?
2. What should you check before the question reaches the model?
3. What should you check before the answer reaches the customer? (you're here)
4. What if a customer tries to trick it? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
