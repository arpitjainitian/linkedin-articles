# 6. So, Is Your AI Tested or Just Tried? | Evals

*Works on my prompt series: the finale and the checklist*

"We tried it. It works."

Five write-ups ago, that sentence was the whole plan. Here is what the HR assistant's scorecard looks like once the team has tested it properly.

| Check | Before | After |
|---|---|---|
| Right for the right reason | Only the answer was checked | Each answer's source is checked too |
| The grader | A score out of 10 | Checked against people, with a checklist |
| Launch rule | "92% overall, ship it" | A gate per category, the risky ones block |
| Honest score | Test questions in the prompt | A held-back set, kept out of the prompt |
| Every change | Tried by hand | Run the same tests again |

Tried is a feeling. Tested is a scorecard someone can check.

## The checklist

Before you say "it works", check these five:

1. **Sources:** every test case stores the expected source, not only the answer.
2. **Grader:** the AI grader agrees with people on a gold set, and uses yes-or-no checks.
3. **Gates:** each question category has a threshold set from its risk, before testing.
4. **Held-back set:** some questions stay out of the prompt, and a build check guards them.
5. **Every change:** the same tests run again after each prompt, model or data change.

## What to say in the kickoff meeting

- We do not ship on "I tried it". We ship on the scorecard.
- The risky categories decide the launch, not the average.
- The honest score comes from questions the team has not studied.

A test you can repeat is worth more than a demo you can only repeat once.

This is the end of Works on my prompt. Next up: Observability, Series 6, where the question becomes "how do we know it broke?"

Follow me for the next one. What is on your team's AI scorecard today?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
"We tried it. It works."

That was our whole test plan. Then we built a real scorecard.

Five checks before anyone says "it works":
• Sources, not only answers
• A grader that agrees with people
• A gate per category, risky ones block
• A held-back set, kept out of the prompt
• Every change tested again

Finale of Works on my prompt (#WorksOnMyPrompt): the evals checklist, with an HR assistant scorecard.

What is on your team's AI scorecard today?

#AIEngineering #GenAI #LLMEvals #AITesting #WorksOnMyPrompt
```

**Series index (post as the first comment, then pin it):**

```
📌 Works on my prompt: series index

1. It worked when you tried it. Will it work tomorrow?
2. Right answer, wrong reason?
3. Who checks the AI grader?
4. What score is good enough to launch?
5. Is your test set leaking into your prompt?
6. So, is your AI tested or just tried? (you're here, finale)

Next series: Observability, "We'll know when it breaks".
```
