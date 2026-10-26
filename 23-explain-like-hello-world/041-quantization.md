# 41. How Do You Fit a Giant AI on a Laptop? | Quantization

![Cover](images/041-quantization-cover.png)

*Explain It Like Hello World series: Quantization*

"A 4-bit quantized model." It's how big AIs run on laptops and phones. It sounds like physics.

## The hello world

Take a photo and save it as a smaller file. It's a bit less sharp, but you can still see everything that matters, and it takes a fraction of the space.

That's the hello world: **quantization** stores an AI's billions of knobs (write-up 26) with fewer digits each, so the whole model shrinks.

## One step further

Normally each knob is stored as a very precise number, like 0.73914. Quantization rounds it, say to 0.74, using fewer bits of memory. Going from 16 bits to 4 bits per knob makes the model roughly four times smaller and often faster.

Round too hard and quality drops, like an over-compressed photo turning blocky. Good methods keep most of the quality.

## Where you've already met it

Running an AI on a laptop with apps like Ollama or LM Studio. Model downloads labelled "Q4" or "4-bit".

## The real name

**Quantization**.

- **Quantization:** storing a model's numbers with less precision.
- **Bit:** the basic unit of computer memory; fewer bits per number, smaller model.
- **Precision:** how many digits each number keeps.

## What it's not

Quantization isn't free. Quality can slip, especially on maths, rare languages or long reasoning. Test the smaller version on your real tasks.

## Take this to your next meeting

1. Use quantized models to run AI locally or cheaply.
2. Test quality on your hardest examples before switching.
3. Compare a bigger quantized model with a smaller full one; either can win.

Same photo, smaller file. Same AI, smaller memory.

Next write-up (42): **Why Doesn't the Whole AI Wake Up for Every Question?**

Follow me for the next one. Have you run an AI on your own laptop?

**Earlier in this series:**

1. AI words everyone uses. Nobody explains. (the curtain raiser post) *(link added when published)*
2. What Actually Counts as AI? *(link added when published)*
3. How Does a Computer Learn Without Being Told the Rules? *(link added when published)*
4. What's "Deep" About Deep Learning? *(link added when published)*
5. Is a Neural Network Really Like a Brain? *(link added when published)*
6. What Makes AI "Generative"? *(link added when published)*
7. Why Are They Called Foundation Models? *(link added when published)*
8. What Would It Mean for AI to Be "General"? *(link added when published)*
9. What Is Superintelligence, and Should We Worry? *(link added when published)*
10. How Does an AI Read a Word? *(link added when published)*
11. How Does an AI Write a Sentence? *(link added when published)*
12. How Does an AI Know "King" Is Close to "Queen"? *(link added when published)*
13. How Does an AI Know What "It" Means? *(link added when published)*
14. What Is the "T" in GPT? *(link added when published)*
15. Why Does an AI Forget the Start of a Long Chat? *(link added when published)*
16. Why Does the Same Question Get Different Answers? *(link added when published)*
17. Why Does the Way You Ask Change the Answer? *(link added when published)*
18. Is Prompt Engineering a Real Skill? *(link added when published)*
19. What's the Hidden Instruction Behind Every Chatbot? *(link added when published)*
20. Can an AI Do a Task It Was Never Shown? *(link added when published)*
21. Why Do Examples Help an AI So Much? *(link added when published)*
22. Why Does "Think Step by Step" Work? *(link added when published)*
23. Is Context Engineering the New Prompt Engineering? *(link added when published)*
24. How Do You Get an AI to Fill In a Form? *(link added when published)*
25. Why Does the AI Type Its Answer Word by Word? *(link added when published)*
26. What Does "70B" Actually Mean? *(link added when published)*
27. How Does an AI Go to School? *(link added when published)*
28. What Happens When You Hit Send? *(link added when published)*
29. How Does an AI Learn Language in the First Place? *(link added when published)*
30. How Do You Teach an AI Your Way of Doing Things? *(link added when published)*
31. How Do You Customise an AI Without Retraining It? *(link added when published)*
32. How Did the AI Learn to Be Polite? *(link added when published)*
33. Can an AI Follow a Written Set of Principles? *(link added when published)*
34. How Does a Small AI Learn From a Big One? *(link added when published)*
35. Can an AI Learn From Data Another AI Wrote? *(link added when published)*
36. Who Teaches the AI What's Right? *(link added when published)*
37. Why Can an AI Ace the Practice Test and Fail the Real One? *(link added when published)*
38. Why Did Bigger AI Keep Getting Better? *(link added when published)*
39. Can Bigger AI Suddenly Learn New Tricks? *(link added when published)*
40. What Happens When AI Learns From AI? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
A giant AI needs a giant computer.
Your laptop has a fraction of that memory.

Quantization is saving the same photo as a smaller file.

It's how big AIs fit on laptops and phones.

Have you run an AI on your own laptop?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 40. What Happens When AI Learns From AI? [link]
You're here: 41. How Do You Fit a Giant AI on a Laptop?
Next: 42. Why Doesn't the Whole AI Wake Up for Every Question?

Full list: in the curtain raiser post.
```
