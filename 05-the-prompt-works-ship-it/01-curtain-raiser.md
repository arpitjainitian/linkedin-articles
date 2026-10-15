# 1. It Worked When You Tried It. Will It Work Tomorrow?

![Cover](images/01-curtain-raiser-cover.png)

*Works on my prompt series: the curtain raiser*

*After Series 4, Just tell it not to: It's fenced in. But how do you know it's right, every day?*

"I tried it, and it works."

Picture an HR policy assistant for a company's employees. The developer asks it, "How many leaves can I carry forward?" It answers correctly, with the right policy section. A screenshot goes into the status update. Green tick. Ship it.

Three weeks after launch, an employee in Bengaluru asks about the notice period. The number is right, but it came from the Mumbai policy. The team's AI grader marks it 10/10. The overall score looks great, yet maternity questions are right only 60% of the time.

Nobody noticed, because nobody was checking. The test plan was one question, asked once, on a laptop.

## Why "I tried it" isn't a test

Traditional software gives the same output for the same input. AI doesn't, quite. It can be right on Monday and wrong on Wednesday, and still sound equally confident both times.

- **One question proves one question.** The demo question is always the easy one.
- **A right answer can be right by luck.** It quoted the right number from the wrong policy. Next time, it won't.
- **AI graders have tastes.** A judge model can prefer a polite wrong answer to a blunt right one.
- **One average hides a weak spot.** 92% overall can mean 60% on the questions that matter most.
- **Tests can leak.** Paste the test questions into the prompt as examples, and scores go up while nothing improves.

The basics (a real test set, an answer key, re-testing every change) are in [write-up 9 of my #JustAddRAG series](https://www.linkedin.com/pulse/9-how-many-questions-did-you-test-before-saying-works-arpit-jain-vrmqf). This series goes one level deeper.

It's a student who studied for exactly one exam question and got full marks on it. Lovely result. Please don't let them sit the real exam yet.

## What sits behind "it works"

The demo is the visible part. What tells you an AI is really ready is checking each step, not just the final answer; checking the AI grader itself; agreeing a pass mark before launch; and keeping test questions the model has never seen. Teams call this **evals**, short for evaluations. The report card on the cover shows how most launches score today.

## This is a series: here's what's coming

This write-up is the first in a series. Each one takes one part of testing and goes deep, with the same HR assistant every time. A few of the questions it will answer:

- Right answer, wrong reason? (Grading each step)
- Who checks the AI grader? (Auditing the judge)
- What score is good enough to launch? (Release gates)
- Is your test set leaking into your prompt? (Fresh test questions)

...and a final write-up with a checklist for testing AI properly.

## Take this to your next kickoff meeting

1. For ten answers, check the source it used, not just the final answer.
2. Have people grade 50 answers, and compare with your AI grader's marks.
3. Agree the pass mark for each type of question before launch, not after.

"It worked when I tried it" is a demo. "It passed 300 questions this morning" is a test.

Next write-up (2): **Right answer, wrong reason?** (Grading each step)

Follow me for the next one. And tell me: how many questions did your last AI project test before someone said "it works"?

---

**Post text (copy and paste):**

```
"I tried it, and it works."

One question. Asked once. On a laptop. Green tick in the status update.

Three weeks later: the right notice period, from the wrong city's policy. Marked 10/10 by the AI grader.

Ship on "I tried it", and you pay for it:
• Accuracy: wrong answers nobody notices until employees complain
• Trust: one wrong HR answer, and people go back to emailing HR
• Risk: policy answers that create real disputes
• Speed: every change becomes scary, because nothing checks it

Write-up 1 in my new series, Works on my prompt (#WorksOnMyPrompt): why trying it isn't testing it, what good evals check, and three things to take to your next kickoff meeting.

How many questions did your last AI project test before someone said "it works"?

#AIEngineering #GenAI #LLMEvals #AITesting #WorksOnMyPrompt
```

**Series index (post as the first comment, then pin it):**

```
📌 Works on my prompt: series index

1. It worked when you tried it. Will it work tomorrow? (you're here)
2. Right answer, wrong reason? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
