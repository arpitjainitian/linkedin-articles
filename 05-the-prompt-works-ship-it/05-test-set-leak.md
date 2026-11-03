# 5. Is Your Test Set Leaking Into Your Prompt? | Evals

*Works on my prompt series: evals, and the test you keep honest*

The HR assistant scores 98% on the test set. The team is pleased.

Then someone opens the prompt. Every one of the 50 test questions is pasted in as an example, with its correct answer.

The assistant did not learn the policy. It learned the test.

Tune to the test, and you only pass the test.

## A practice paper that becomes the exam

Think of a student who gets the exam paper a week early. They practise every question, memorise the answers and score full marks. The mark is real. It just does not show they understand the subject.

Your prompt is the student. If the test questions sit inside the prompt, the score measures memory, not skill.

## How leaks happen

Leaks are easy to miss, because nobody sets out to cheat:

- **Copy-paste:** a failing question is added to the prompt as an example, "so it stops failing".
- **Shared examples:** the few-shot examples in the prompt are drawn from the test set.
- **Repeated tuning:** the team changes the prompt until the test score rises. Each change fits the test a little more.

## Keep some questions for the final check

Split your questions into two sets before you start:

- **Tuning set:** the questions the team looks at while improving the prompt.
- **Held-back set:** questions nobody reads until release. They are the honest check.

Keep the held-back set out of the prompt, out of examples and out of the team's daily runs. Refresh it from new real questions every so often, so it does not go stale.

## Check for leaks in code

Add a check that fails the build when any held-back question, or a close copy of it, appears in the prompt. A simple text match catches the obvious cases. It will not catch every paraphrase, so keep the held-back set small and private.

## Take this to your next kickoff meeting

1. Split the test questions into a tuning set and a held-back set on day one.
2. Keep the held-back questions out of the prompt, and check for copies in the build.
3. Report the held-back score, not the tuning score, as the result.

A test you have studied is no longer a test.

Next write-up (6): **So, is your AI tested or just tried?** (Finale: the evals checklist)

Follow me for the next one. Would your team notice if the test questions were in the prompt?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
The assistant scored 98% on the test set.

Then we opened the prompt. All 50 test questions were pasted in as examples.

It did not learn the policy. It learned the test.

Write-up 5 in my series, Works on my prompt (#WorksOnMyPrompt): how test questions leak into prompts, and how to keep a held-back set honest.

Would your team notice if the test questions were in the prompt?

#AIEngineering #GenAI #LLMEvals #AITesting #WorksOnMyPrompt
```

**Series index (post as the first comment, then pin it):**

```
📌 Works on my prompt: series index

1. It worked when you tried it. Will it work tomorrow?
2. Right answer, wrong reason?
3. Who checks the AI grader?
4. What score is good enough to launch?
5. Is your test set leaking into your prompt? (you're here)
6. So, is your AI tested or just tried? (next write-up, finale)

I'll keep this comment updated with each link as it goes live.
```
