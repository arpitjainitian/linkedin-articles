# 21. Why Does the AI Think Before It Answers Now? | Reasoning models

![Cover](images/21-reasoning-models-cover.png)

*Explain It Like Hello World series: Reasoning models*

"Reasoning models." "Thinking mode." Newer AIs pause, show "thinking...", then answer. What's happening in that pause?

## The hello world

Ask a friend: "A bat and a ball cost ₹110. The bat costs ₹100 more than the ball. How much is the ball?" Most blurt "₹10". Wrong. Ask them to work it out step by step, and they get ₹5.

That's the hello world: a **reasoning model** writes out its working before giving the answer.

## One step further

Normal next-token prediction (write-up 3) commits to an answer straight away. A reasoning model is trained to first produce a long chain of steps: try an approach, check it, backtrack, try again. Only then does it answer.

More thinking usually means better results on maths, coding and planning, but it uses more tokens, so it's slower and costs more per question.

## Where you've already met it

"Thinking" or "extended thinking" toggles in chat apps, and answers that take 20 seconds instead of 2.

## The real name

**Reasoning models**, using **test-time compute**.

- **Chain of thought:** the step-by-step working the model writes out.
- **Test-time compute:** spending more computing power while answering, not while training.
- **Thinking budget:** a limit on how long it can think.

## What it's not

The thinking isn't a perfect window into how it decided, and more thinking isn't always better. Simple questions don't need it, and you pay for every thinking token.

## Take this to your next meeting

1. Turn thinking on for maths, code and planning; off for quick facts.
2. Watch the cost: thinking tokens are billed.
3. Still check the final answer, not just the working.

Work it out, then answer.

Next write-up (22): **How Can One AI Read, See and Listen?**

Follow me for the next one. Did you get ₹10 or ₹5?

**Earlier in this series:**

1. AI words everyone uses. Nobody explains. (the curtain raiser post) *(link added when published)*
2. How Does an AI Read a Word? *(link added when published)*
3. How Does an AI Write a Sentence? *(link added when published)*
4. How Does an AI Know "King" Is Close to "Queen"? *(link added when published)*
5. How Does an AI Know What "It" Means? *(link added when published)*
6. Why Does an AI Forget the Start of a Long Chat? *(link added when published)*
7. Why Does the Same Question Get Different Answers? *(link added when published)*
8. What Does "70B" Actually Mean? *(link added when published)*
9. Is the AI Learning While You Chat With It? *(link added when published)*
10. How Do You Teach an AI Something New? *(link added when published)*
11. How Did the AI Learn to Be Polite? *(link added when published)*
12. How Does a Small AI Learn From a Big One? *(link added when published)*
13. Can an AI Learn From Data Another AI Wrote? *(link added when published)*
14. Why Did Bigger AI Keep Getting Better? *(link added when published)*
15. How Do You Fit a Giant AI on a Laptop? *(link added when published)*
16. Why Doesn't the Whole AI Wake Up for Every Question? *(link added when published)*
17. Why Doesn't the AI Re-Read Everything for Every Word? *(link added when published)*
18. How Can a Small AI Make a Big AI Faster? *(link added when published)*
19. Why Does AI Run on Gaming Chips? *(link added when published)*
20. Can an AI Live on Your Phone? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
A bat and a ball cost ₹110. The bat costs ₹100 more.
How much is the ball?

Most people blurt ₹10. Thinking step by step gets ₹5. Reasoning models do the same.

They write out their working before answering.

Did you get ₹10 or ₹5?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 20. Can an AI Live on Your Phone? [link]
You're here: 21. Why Does the AI Think Before It Answers Now?
Next: 22. How Can One AI Read, See and Listen?

Full list: in the curtain raiser post.
```
