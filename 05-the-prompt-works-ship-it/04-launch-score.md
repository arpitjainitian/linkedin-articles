# 4. What Score Is Good Enough to Launch? | Evals

*Works on my prompt series: evals, and the line you ship on*

"Overall score: 92%. Ship it?"

Look closer. The HR assistant scores 60% on maternity leave questions. Four in ten answers in that group are wrong.

The average looked fine because most questions are about payslips and office hours. The risky group was hidden inside a good number.

"Pretty good" is not a launch rule.

## An average can hide a failure

Think of a hospital that reports its average wait time. The average is 20 minutes, which sounds fine. But the emergency patients wait 90 minutes. The average is true, and it still tells you nothing about the people who matter most.

Your assistant has the same problem. One average hides the questions where a wrong answer costs the most.

## Set the gate before you test

A **release gate** is a rule that says "ship only if". Write it before the test runs, not after you see the score. Otherwise the gate drifts to match the result.

A simple gate has three parts:

- **Per category:** every type of question has its own score, such as leave, pay and office hours.
- **Per risk:** the riskier the category, the higher the bar. A wrong office address is annoying. A wrong leave entitlement can cost money and trust.
- **Blocking:** one failed high-risk category stops the release, however good the average looks.

## Keep the gate in code

Put the gate in a file the release process reads. When a score falls below its gate, the build fails and nobody needs to argue about the number.

Small categories need care too. A category with only three test questions gives a score you cannot trust. Add more questions to it before it can block a launch.

## Take this to your next kickoff meeting

1. Ask for scores per question type, not only the overall average.
2. Agree on the gate for each type before the first test, with the business owner.
3. Let the riskiest category block the launch on its own.

An average tells you how the assistant does on easy questions. The gate tells you whether it is safe to ship.

Next write-up (5): **Is your test set leaking into your prompt?**

Follow me for the next one. What is the one question your AI must never get wrong?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
"Overall score: 92%. Ship it?"

The same assistant scores 60% on maternity leave questions.

An average can hide the one group where a wrong answer costs the most.

Write-up 4 in my series, Works on my prompt (#WorksOnMyPrompt): how to set a release gate per question type, before you test.

What is the one question your AI must never get wrong?

#AIEngineering #GenAI #LLMEvals #AITesting #WorksOnMyPrompt
```

**Series index (post as the first comment, then pin it):**

```
📌 Works on my prompt: series index

1. It worked when you tried it. Will it work tomorrow?
2. Right answer, wrong reason?
3. Who checks the AI grader?
4. What score is good enough to launch? (you're here)
5. Is your test set leaking into your prompt? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
