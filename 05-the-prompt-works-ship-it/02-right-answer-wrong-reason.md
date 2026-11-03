# 2. Right Answer, Wrong Reason? | Evals

*Works on my prompt series: evals, one layer at a time*

"What's the notice period for my team?"

"30 days."

Correct. But the employee sits in Bengaluru, and the assistant read the Mumbai policy. The Mumbai policy also says 30 days, by luck. Next year it changes to 45 days in Mumbai, and nobody notices the answer came from the wrong place.

A lucky answer still fails tomorrow.

## The answer is the last link

An assistant works in layers. First it searches for the right passage. Then it applies the rules for this employee's location. Last, it writes the answer from what it found.

A test that checks only the final sentence cannot tell which link broke. The score is green while the method is wrong.

## Think of a maths test

A student copies the answer from the classmate beside them. The mark is full. The teacher learns nothing about the student, and the next test shows the gap.

Your evals should ask: did the right method run, or only did we get the right words?

## Grade each layer

Score each layer on its own:

- **Search:** did the right policy appear in the top results?
- **Rules:** was the right version used for this employee's location?
- **Answer:** does every claim come from the passage it relies on, and is anything missing?

Each test case now lists the expected source, not only the expected answer. An answer that matches but cites the wrong source fails.

## The fix in practice

- Store the expected source with every test question.
- Log which passage each answer used.
- Add questions where two locations give different answers, so a wrong location gets caught.

## Take this to your next kickoff meeting

1. Ask for the source in every test result, not only the answer.
2. Test the places where two versions of a rule could be read.
3. Count a right answer from the wrong source as a failure.

A right answer is only half a test.

Next write-up (3): **Who checks the AI grader?**

Follow me for the next one. Have you ever been right for the wrong reason?

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 4, Just tell it not to:** [start here](https://www.linkedin.com/feed/update/urn:li:activity:7522116495976529920/) or read [write-up 4, red teaming](https://www.linkedin.com/pulse/4-what-customer-tries-trick-red-teaming-arpit-jain-m7l5f)

---

**Post text (copy and paste):**

```
"What's the notice period for my team?"
"30 days."

Correct. But the employee is in Bengaluru, and the answer came from the Mumbai policy.

A lucky answer still fails tomorrow.

Write-up 2 in my series, Works on my prompt (#WorksOnMyPrompt): why a right answer can hide a wrong method, and how to grade each layer.

What's the last test that passed for the wrong reason?

#AIEngineering #GenAI #LLMEvals #AITesting #WorksOnMyPrompt
```

**Series index (post as the first comment, then pin it):**

```
📌 Works on my prompt: series index

1. It worked when you tried it. Will it work tomorrow?
2. Right answer, wrong reason? (you're here)
3. Who checks the AI grader? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
