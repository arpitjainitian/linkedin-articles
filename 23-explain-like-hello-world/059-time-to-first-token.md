# 59. What Is Time to First Token, and Why Does the First Word Matter Most? | Time to first token

![Cover](images/059-time-to-first-token-cover.png)

*Explain It Like Hello World series: Time to first token*

"TTFT." AI teams obsess over it. It's the speed number users actually feel.

## The hello world

At a restaurant, a waiter who brings bread and water in one minute feels fast, even if the meal takes 20. A waiter who brings nothing for 15 minutes feels slow, even if everything arrives at once.

That's the hello world: **time to first token** is how long until the AI's first word appears.

## One step further

With streaming (write-up 29), people start reading as soon as the first word arrives. So the wait before that first word decides whether an AI feels fast.

It grows with long prompts, document look-ups before answering, reasoning time (write-up 86) and busy servers. Prompt caching (write-up 50) and smaller prompts shrink it.

## Where you've already met it

Chatbots that start typing almost instantly, versus ones that think for 10 seconds first.

## The real name

**Time to first token (TTFT)**.

- **TTFT:** the delay before the first word appears.
- **Tokens per second:** how fast words keep arriving after that.
- **Perceived speed:** how fast it feels to the user.

## What it's not

A fast first word doesn't mean a fast full answer. Measure both: the first word and the speed of the rest.

## Take this to your next meeting

1. Track time to first word as your main speed measure.
2. Show something quickly: a first word, a status, or progress.
3. Trim long prompts and cache the fixed parts.

Bring the bread first.

Next write-up (60): **What Is RAG, and How Does an AI Answer From Your Documents?**

Follow me for the next one. Does a fast first word make an AI feel faster to you?

**Earlier in this series:**

1. [AI words everyone uses. Nobody explains.](https://lnkd.in/p/d8abaPhq) (the curtain raiser post)
2. [What Actually Counts as Artificial Intelligence?](https://www.linkedin.com/pulse/2-what-actually-counts-artificial-intelligence-arpit-jain-su9lf)
3. [How Does Machine Learning Learn Without Being Told the Rules?](https://www.linkedin.com/pulse/3-how-does-machine-learning-learn-without-being-told-rules-arpit-jain-ppdyf)
4. [What's "Deep" About Deep Learning?](https://www.linkedin.com/pulse/4-whats-deep-learning-arpit-jain-rvlff)
5. [Is a Neural Network Really Like a Brain?](https://www.linkedin.com/pulse/5-neural-network-really-like-brain-arpit-jain-jpigf)
6. What Makes Generative AI "Generative"? *(link added when published)*
7. Why Are They Called Foundation Models? *(link added when published)*
8. What Is a Frontier Model, and Who Decides? *(link added when published)*
9. What Is AGI, and What Would Make AI "General"? *(link added when published)*
10. What Is Superintelligence, and Should We Worry? *(link added when published)*
11. What Are Tokens, and Why Does an AI Read in Pieces? *(link added when published)*
12. How Does an LLM Write a Sentence? *(link added when published)*
13. How Do Embeddings Know "King" Is Close to "Queen"? *(link added when published)*
14. How Does Attention Help an AI Know What "It" Means? *(link added when published)*
15. What Is a Transformer, the "T" in GPT? *(link added when published)*
16. What Is a Context Window, and Why Does an AI Forget? *(link added when published)*
17. What's a Knowledge Cutoff, and Why Is the AI Behind on News? *(link added when published)*
18. What Is Context Rot, and Why Do Long Chats Get Worse? *(link added when published)*
19. Why Does Temperature Change the AI's Answer? *(link added when published)*
20. What Is a Prompt, and Why Does the Way You Ask Matter? *(link added when published)*
21. Is Prompt Engineering a Real Skill? *(link added when published)*
22. What's in a System Prompt, the Hidden Instruction Behind Every Chatbot? *(link added when published)*
23. What Is Zero-Shot, and Can an AI Do a Task It Was Never Shown? *(link added when published)*
24. Why Does Few-Shot Prompting Work So Well? *(link added when published)*
25. Why Does Chain of Thought ("Think Step by Step") Work? *(link added when published)*
26. What Is Reflection, and Why Does an AI Check Its Own Answer? *(link added when published)*
27. Is Context Engineering the New Prompt Engineering? *(link added when published)*
28. How Does Structured Output Get an AI to Fill In a Form? *(link added when published)*
29. Why Does Streaming Make the AI Type Word by Word? *(link added when published)*
30. What Do Parameters, Like "70B", Actually Mean? *(link added when published)*
31. What Happens During Training, When an AI Goes to School? *(link added when published)*
32. What's the Difference Between Supervised and Unsupervised Learning? *(link added when published)*
33. What Is Inference, and What Happens When You Hit Send? *(link added when published)*
34. What Is Pretraining, and How Does an AI Learn Language? *(link added when published)*
35. What Is Fine-Tuning, and How Does an AI Learn Your Way? *(link added when published)*
36. What Is LoRA, and How Do You Customise an AI Cheaply? *(link added when published)*
37. How Does Reinforcement Learning Teach AI by Trial and Error? *(link added when published)*
38. What Is RLHF, and How Did the AI Learn to Be Polite? *(link added when published)*
39. What Is Constitutional AI, and Can an AI Follow Principles? *(link added when published)*
40. What Is Distillation, and How Does a Small AI Learn From a Big One? *(link added when published)*
41. What Is Synthetic Data, and Can an AI Learn From AI-Written Data? *(link added when published)*
42. What Is Data Labelling, and Who Teaches the AI What's Right? *(link added when published)*
43. What Is Overfitting, and Why Can an AI Ace the Practice Test and Fail? *(link added when published)*
44. What Are Scaling Laws, and Why Did Bigger AI Keep Getting Better? *(link added when published)*
45. Are Emergent Abilities Real, or Does Bigger AI Just Seem to Learn New Tricks? *(link added when published)*
46. What Is Model Collapse, and What Happens When AI Learns From AI? *(link added when published)*
47. What Is Quantization, and How Does a Giant AI Fit on a Laptop? *(link added when published)*
48. What Is a Mixture of Experts, and Why Doesn't the Whole AI Wake Up? *(link added when published)*
49. What Is a KV Cache, and Why Doesn't the AI Re-Read Everything? *(link added when published)*
50. How Does Prompt Caching Make Repeated Prompts Cheaper? *(link added when published)*
51. How Does Speculative Decoding Make a Big AI Faster? *(link added when published)*
52. What Is Test-Time Compute, and Why Does Thinking Cost More? *(link added when published)*
53. Why Does AI Run on a GPU, a Gaming Chip? *(link added when published)*
54. What Is a TPU, and Why Did Google Build One? *(link added when published)*
55. What Is an NPU, the AI Chip Inside Your New Laptop? *(link added when published)*
56. Can a Small Language Model Be Good Enough? *(link added when published)*
57. What Is On-Device AI, and Can an AI Live on Your Phone? *(link added when published)*
58. What Is Latency, and Why Does the AI Take So Long to Answer? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)
- **Series 20, Today in AI** (ongoing): [start here](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/) or read [the latest issue](https://www.linkedin.com/pulse/today-ai-011-text-to-speech-fits-your-phone-internet-needed-jain-1ipuf)

---

**Post text (copy and paste):**

```
Bread and water in one minute: fast service.
Nothing for 15 minutes: slow, even if it all arrives at once.

Time to first token is the AI's bread basket.

It's the speed users actually feel.

Does a fast first word make an AI feel faster to you?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: AI words everyone uses. Nobody explains. https://lnkd.in/p/d8abaPhq
Previous: 58. What Is Latency, and Why Does the AI Take So Long to Answer? [link]
You're here: 59. What Is Time to First Token, and Why Does the First Word Matter Most?
Next: 60. What Is RAG, and How Does an AI Answer From Your Documents?

Full list: in the curtain raiser post.
```
