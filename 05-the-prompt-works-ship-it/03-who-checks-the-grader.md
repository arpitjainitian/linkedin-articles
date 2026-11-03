# 3. Who Checks the AI Grader? | Evals

*Works on my prompt series: evals, and the judge that marks them*

"Can I carry forward 10 leaves?"

Answer A: "Thank you for asking! What a great question. You are welcome to carry forward up to 10 leaves."

Answer B: "No. The maximum is 5."

The policy says 5. The AI grader gives Answer A 9 out of 10 and Answer B 6 out of 10.

A judge that likes nice writing is not a judge.

## Many teams let an AI do the marking

Reading every answer by hand does not scale. So teams ask a model to grade the answers: "Is this answer good, from 1 to 10?"

It is fast and cheap. But the grader has tastes, and those tastes can be wrong.

## What graders get wrong

Graders often prefer:

- **Longer answers**, even when the extra words add nothing.
- **Polite tone**, even when the facts are wrong.
- **Their own style**, which can make a similar answer look better.

A grader can also miss a wrong fact, if it cannot check the policy itself.

## Think of an essay contest

Imagine a judge who marks essays by neatness. The neat, wrong essay wins. Nobody asked whether the facts were right, so the contest measures handwriting, not knowledge.

Your grader has the same risk. Its score only means something if it agrees with people on the things that matter.

## Audit the judge

Check the grader against people before you trust it:

1. Take 50 answers that people have already graded.
2. Let the grader score the same 50.
3. Measure how often the grader and the people agree.
4. Read every case where they disagree. The reason usually shows the bias.

Keep a small set of answers with known right and wrong facts. This is your gold set. If the grader fails the gold set, do not use its scores.

## Give the grader a checklist, not a feeling

Replace "rate this from 1 to 10" with yes-or-no questions:

- Does the answer state the limit in the policy?
- Does it say anything the policy does not support?
- Would a person act on it without checking?

A checklist is harder to charm.

## Take this to your next kickoff meeting

1. Keep a gold set that people have graded by hand.
2. Measure how well the AI grader agrees with people, before trusting its scores.
3. Give the grader a checklist of facts to check, not a single mark out of 10.

A judge you have never checked is just another opinion.

Next write-up (4): **What score is good enough to launch?**

Follow me for the next one. Have you ever trusted a score you never checked?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
"You are welcome to carry forward up to 10 leaves."

The policy says 5. The AI grader gave that answer 9 out of 10.

A grader that likes nice writing is not a judge.

Write-up 3 in my series, Works on my prompt (#WorksOnMyPrompt): how to audit an AI grader against people, and why a checklist beats a score out of 10.

Have you ever checked your AI grader against human marks?

#AIEngineering #GenAI #LLMEvals #AITesting #WorksOnMyPrompt
```

**Series index (post as the first comment, then pin it):**

```
📌 Works on my prompt: series index

1. It worked when you tried it. Will it work tomorrow?
2. Right answer, wrong reason?
3. Who checks the AI grader? (you're here)
4. What score is good enough to launch? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
