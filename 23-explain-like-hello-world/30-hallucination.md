# 30. Why Does an AI Sound Sure When It's Wrong? | Hallucination

![Cover](images/30-hallucination-cover.png)

*Explain It Like Hello World series: Hallucination*

"The AI hallucinated." It's the most famous AI problem. The word makes it sound like the AI is seeing things.

## The hello world

Ask an AI for a book by a real author on a niche topic. It might name a plausible-sounding title that doesn't exist, with confidence.

That's the hello world: remember write-up 3. An AI writes by guessing **likely** next words. A likely-sounding answer and a true answer usually match. When they don't, you get a **hallucination**.

## One step further

The AI has no built-in "I don't know" signal. If its training text rarely covered something, it still produces the most likely-sounding words, and fluent text sounds sure.

Giving it the right source to read, asking it to cite, and allowing "I'm not sure" all help. (How this is handled in real systems is covered in #JustAddRAG 5.)

## Where you've already met it

Made-up citations, invented quotes, wrong dates said confidently, and fake legal cases that have landed lawyers in trouble.

## The real name

**Hallucination**, sometimes called **confabulation**.

- **Hallucination:** fluent output that isn't true or isn't supported.
- **Grounding:** making answers rely on a given source.
- **Citation:** pointing to where a claim came from.

## What it's not

It isn't lying (there's no intent) and it isn't a rare bug. It comes from how next-word guessing works, so it can be reduced, not fully removed.

## Take this to your next meeting

1. Check names, numbers, quotes and citations before using them.
2. Give the AI the source document instead of asking from memory.
3. Make "I'm not sure" an acceptable answer in your prompts.

Likely-sounding isn't the same as true.

Next write-up (31): **Can You Tell If AI Wrote This?**

Follow me for the next one. What's the most confident wrong answer an AI has given you?

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
21. Why Does the AI Think Before It Answers Now? *(link added when published)*
22. How Can One AI Read, See and Listen? *(link added when published)*
23. How Does an AI Draw a Picture From Noise? *(link added when published)*
24. How Does an AI Talk Back Without a Pause? *(link added when published)*
25. What Does "Open" Mean in Open AI Models? *(link added when published)*
26. How Do AI Agents Talk to Each Other? *(link added when published)*
27. How Does an AI Use a Computer Like You? *(link added when published)*
28. Can an AI Imagine What Happens Next? *(link added when published)*
29. What Does "Scored 90% on a Benchmark" Mean? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
Ask an AI for a book on a niche topic.
It names a real-sounding title. It doesn't exist.

An AI guesses likely words. Likely isn't always true. That's a hallucination.

Check names, numbers and quotes.

What's the most confident wrong answer an AI has given you?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 29. What Does "Scored 90% on a Benchmark" Mean? [link]
You're here: 30. Why Does an AI Sound Sure When It's Wrong?
Next: 31. Can You Tell If AI Wrote This?

Full list: in the curtain raiser post.
```
