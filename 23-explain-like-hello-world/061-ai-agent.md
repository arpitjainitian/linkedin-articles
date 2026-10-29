# 61. What Makes an AI Agent an "Agent"? | AI agent

![Cover](images/061-ai-agent-cover.png)

*Explain It Like Hello World series: AI agent*

"AI agents" are the buzzword of the moment. Every product is suddenly an agent. What actually makes something an agent?

## The hello world

A chatbot is like a librarian: you ask, it answers, done. An agent is like a personal assistant: you say "book me a meeting with Priya next week", and it checks calendars, picks a slot, sends the invite and tells you when it's done.

That's the hello world: an **AI agent** takes a goal, decides the steps itself, uses tools to act, and keeps going until the job is done.

## One step further

Under the hood, it's a loop: the AI thinks about the next step, calls a tool (write-up 63), reads the result, and decides again, until the goal is met or it gets stuck.

That freedom is the power and the risk: an agent can take wrong steps, loop, or act on bad information. What goes wrong in practice is the theme of my Series 2, "Beyond Just RAG: From Answers to Actions".

## Where you've already met it

Coding assistants that edit files and run tests. Assistants that book, order or file things for you. My [Today in AI No. 001](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/) asks what happens when your agent visits someone else's website.

## The real name

An **AI agent**.

- **Agent:** an AI that plans steps and acts with tools to reach a goal.
- **Tool:** something the agent can use: search, calendar, database.
- **Agent loop:** think, act, check, repeat.

## What it's not

An agent isn't just a chatbot with a new name, and it doesn't need to be autonomous for everything. Many tasks are better as a fixed workflow.

## Take this to your next meeting

1. Ask: does this task need the AI to choose its own steps?
2. Give agents only the tools they need.
3. Put a person in charge of irreversible actions.

A chatbot answers. An agent gets it done.

Next write-up (62): **What Does "Agentic AI" Really Mean?**

Follow me for the next one. Which task would you hand to an AI agent first?

**Earlier in this series:**

1. [AI words everyone uses. Nobody explains.](https://lnkd.in/p/d8abaPhq) (the curtain raiser post)
2. [What Actually Counts as Artificial Intelligence?](https://www.linkedin.com/pulse/2-what-actually-counts-artificial-intelligence-arpit-jain-su9lf)
3. [How Does Machine Learning Learn Without Being Told the Rules?](https://www.linkedin.com/pulse/3-how-does-machine-learning-learn-without-being-told-rules-arpit-jain-ppdyf)
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
44. How Does Prompt Caching Make Repeated Prompts Cheaper? *(link added when published)*
45. How Does Speculative Decoding Make a Big AI Faster? *(link added when published)*
46. Why Does AI Run on a GPU, a Gaming Chip? *(link added when published)*
47. What Is a TPU, and Why Did Google Build One? *(link added when published)*
48. What Is an NPU, the AI Chip Inside Your New Laptop? *(link added when published)*
49. Can a Small Language Model Be Good Enough? *(link added when published)*
50. What Is On-Device AI, and Can an AI Live on Your Phone? *(link added when published)*
51. What Is Latency, and Why Does the AI Take So Long to Answer? *(link added when published)*
52. What Is Time to First Token, and Why Does the First Word Matter Most? *(link added when published)*
53. What Is RAG, and How Does an AI Answer From Your Documents? *(link added when published)*
54. What Is a Vector Database, and Where Does an AI Store Meaning? *(link added when published)*
55. How Does Semantic Search Understand What You Meant? *(link added when published)*
56. What Is a Knowledge Graph, and Who Is Connected to Whom? *(link added when published)*
57. What Is GraphRAG, and How Does an AI Answer About a Whole Pile of Documents? *(link added when published)*
58. What Is Grounding, and How Do You Keep an AI Tied to the Facts? *(link added when published)*
59. How Do Citations Show Where an AI Got Its Answer? *(link added when published)*
60. Can Deep Research Do Your Research for You? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)
- **Series 20, Today in AI** (ongoing): [start here](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/) or read [the latest issue](https://www.linkedin.com/pulse/today-ai-011-text-to-speech-fits-your-phone-internet-needed-jain-1ipuf)

---

**Post text (copy and paste):**

```
A librarian answers your question.
A personal assistant books the meeting.

A chatbot is the librarian. An AI agent is the assistant who gets it done.

Goal in, steps chosen, tools used.

Which task would you hand to an AI agent first?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: AI words everyone uses. Nobody explains. https://lnkd.in/p/d8abaPhq
Previous: 60. Can Deep Research Do Your Research for You? [link]
You're here: 61. What Makes an AI Agent an "Agent"?
Next: 62. What Does "Agentic AI" Really Mean?

Full list: in the curtain raiser post.
```
