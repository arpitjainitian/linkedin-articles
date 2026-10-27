# 44. How Does Prompt Caching Make Repeated Prompts Cheaper? | Prompt caching

![Cover](images/044-prompt-caching-cover.png)

*Explain It Like Hello World series: Prompt caching*

"Prompt caching: up to 90% off." AI providers advertise it. Why would asking the same thing again cost less?

## The hello world

A teacher reads the same 50-page rulebook aloud before every exam question. Wasteful. Better: read it once, keep notes, and for each new question, only read the question.

That's the hello world: **prompt caching** saves the work done on the repeated start of a prompt and reuses it for the next request.

## One step further

Many apps send the same long beginning every time: instructions, policies, a document. The provider stores the processed version of that beginning (the KV cache, write-up 43) for a short while. If your next request starts the same way, it skips that work and charges much less for those tokens.

It only helps if the repeated part comes first and is exactly the same. Change one character at the start and the saving is lost.

## Where you've already met it

"Cached input" lines on AI bills. Faster replies in chat apps that reuse long instructions.

## The real name

**Prompt caching**, also called **context caching**.

- **Cache hit:** the repeated start was found and reused.
- **Prefix:** the beginning part of a prompt.
- **Cache lifetime:** how long the saved work is kept.

## What it's not

It's not caching answers. The AI still writes a fresh answer; only the reading of the repeated part is saved. (Cost strategies are covered in Series 8.)

## Take this to your next meeting

1. Put fixed instructions and documents first, the changing question last.
2. Keep the fixed part exactly identical between requests.
3. Check your bill for cached-token lines to see if it's working.

Read the rulebook once. Keep the notes.

Next write-up (45): **How Does Speculative Decoding Make a Big AI Faster?**

Follow me for the next one. Does your AI app send the same long instructions every time?

**Earlier in this series:**

1. [AI words everyone uses. Nobody explains.](https://lnkd.in/p/d8abaPhq) (the curtain raiser post)
2. What Actually Counts as Artificial Intelligence? *(link added when published)*
3. How Does Machine Learning Learn Without Being Told the Rules? *(link added when published)*
4. What's "Deep" About Deep Learning? *(link added when published)*
5. Is a Neural Network Really Like a Brain? *(link added when published)*
6. What Makes Generative AI "Generative"? *(link added when published)*
7. Why Are They Called Foundation Models? *(link added when published)*
8. What Is AGI, and What Would Make AI "General"? *(link added when published)*
9. What Is Superintelligence, and Should We Worry? *(link added when published)*
10. What Are Tokens, and Why Does an AI Read in Pieces? *(link added when published)*
11. How Does an LLM Write a Sentence? *(link added when published)*
12. How Do Embeddings Know "King" Is Close to "Queen"? *(link added when published)*
13. How Does Attention Help an AI Know What "It" Means? *(link added when published)*
14. What Is a Transformer, the "T" in GPT? *(link added when published)*
15. What Is a Context Window, and Why Does an AI Forget? *(link added when published)*
16. Why Does Temperature Change the AI's Answer? *(link added when published)*
17. What Is a Prompt, and Why Does the Way You Ask Matter? *(link added when published)*
18. Is Prompt Engineering a Real Skill? *(link added when published)*
19. What's in a System Prompt, the Hidden Instruction Behind Every Chatbot? *(link added when published)*
20. What Is Zero-Shot, and Can an AI Do a Task It Was Never Shown? *(link added when published)*
21. Why Does Few-Shot Prompting Work So Well? *(link added when published)*
22. Why Does Chain of Thought ("Think Step by Step") Work? *(link added when published)*
23. Is Context Engineering the New Prompt Engineering? *(link added when published)*
24. How Does Structured Output Get an AI to Fill In a Form? *(link added when published)*
25. Why Does Streaming Make the AI Type Word by Word? *(link added when published)*
26. What Do Parameters, Like "70B", Actually Mean? *(link added when published)*
27. What Happens During Training, When an AI Goes to School? *(link added when published)*
28. What Is Inference, and What Happens When You Hit Send? *(link added when published)*
29. What Is Pretraining, and How Does an AI Learn Language? *(link added when published)*
30. What Is Fine-Tuning, and How Does an AI Learn Your Way? *(link added when published)*
31. What Is LoRA, and How Do You Customise an AI Cheaply? *(link added when published)*
32. What Is RLHF, and How Did the AI Learn to Be Polite? *(link added when published)*
33. What Is Constitutional AI, and Can an AI Follow Principles? *(link added when published)*
34. What Is Distillation, and How Does a Small AI Learn From a Big One? *(link added when published)*
35. What Is Synthetic Data, and Can an AI Learn From AI-Written Data? *(link added when published)*
36. What Is Data Labelling, and Who Teaches the AI What's Right? *(link added when published)*
37. What Is Overfitting, and Why Can an AI Ace the Practice Test and Fail? *(link added when published)*
38. What Are Scaling Laws, and Why Did Bigger AI Keep Getting Better? *(link added when published)*
39. Are Emergent Abilities Real, or Does Bigger AI Just Seem to Learn New Tricks? *(link added when published)*
40. What Is Model Collapse, and What Happens When AI Learns From AI? *(link added when published)*
41. What Is Quantization, and How Does a Giant AI Fit on a Laptop? *(link added when published)*
42. What Is a Mixture of Experts, and Why Doesn't the Whole AI Wake Up? *(link added when published)*
43. What Is a KV Cache, and Why Doesn't the AI Re-Read Everything? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
Reading the same 50-page rulebook
before every single question.

Prompt caching reads it once and reuses the notes.

Same start, much cheaper.

Does your AI app send the same long instructions every time?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: AI words everyone uses. Nobody explains. https://lnkd.in/p/d8abaPhq
Previous: 43. What Is a KV Cache, and Why Doesn't the AI Re-Read Everything? [link]
You're here: 44. How Does Prompt Caching Make Repeated Prompts Cheaper?
Next: 45. How Does Speculative Decoding Make a Big AI Faster?

Full list: in the curtain raiser post.
```
