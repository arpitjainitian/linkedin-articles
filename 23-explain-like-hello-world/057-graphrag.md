# 57. How Does an AI Answer Questions About a Whole Pile of Documents? | GraphRAG

![Cover](images/057-graphrag-cover.png)

*Explain It Like Hello World series: GraphRAG*

"GraphRAG." A newer twist on RAG that's trending in enterprise AI. Why add a graph?

## The hello world

Ask: "What are the common causes across all 500 incident reports from last year?" Normal RAG (write-up 53) finds a few similar pages, but no single page holds the answer.

That's the hello world: **GraphRAG** first builds a map of the people, systems and events across all documents (a knowledge graph, write-up 56), then answers from that map.

## One step further

An AI reads every document and extracts the important things and how they connect. Related groups are summarised. When a big-picture question arrives, the system answers from those summaries and links, not just from a few matching chunks.

It's good for "across everything" and "how is X connected to Y" questions. It costs more to build and to keep updated than plain RAG.

## Where you've already met it

Enterprise research and investigation tools that summarise themes across thousands of documents.

## The real name

**GraphRAG** (graph-based retrieval-augmented generation).

- **Entity:** a person, system, place or event pulled from text.
- **Community summary:** a summary of a group of connected entities.
- **Multi-hop question:** one that needs several linked facts.

## What it's not

GraphRAG isn't automatically better than RAG. For simple "find the answer on a page" questions, plain RAG is cheaper and enough. (Knowledge graphs in production are covered in Series 13.)

## Take this to your next meeting

1. Use GraphRAG for big-picture and connection questions.
2. Use plain RAG for single-fact look-ups.
3. Budget for building and refreshing the graph.

Map everything first. Then answer the big question.

Next write-up (58): **How Do You Keep an AI Tied to the Facts?**

Follow me for the next one. Do your hardest questions span many documents?

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
41. How Do You Fit a Giant AI on a Laptop? *(link added when published)*
42. Why Doesn't the Whole AI Wake Up for Every Question? *(link added when published)*
43. Why Doesn't the AI Re-Read Everything for Every Word? *(link added when published)*
44. Why Do Repeated Prompts Get Cheaper? *(link added when published)*
45. How Can a Small AI Make a Big AI Faster? *(link added when published)*
46. Why Does AI Run on Gaming Chips? *(link added when published)*
47. What Is a TPU, and Why Did Google Build One? *(link added when published)*
48. What's the AI Chip Inside Your New Laptop? *(link added when published)*
49. Can a Small AI Be Good Enough? *(link added when published)*
50. Can an AI Live on Your Phone? *(link added when published)*
51. Why Does the AI Take So Long to Answer? *(link added when published)*
52. Why Does the First Word Matter Most? *(link added when published)*
53. How Does an AI Answer From Your Documents? *(link added when published)*
54. Where Does an AI Store Meaning? *(link added when published)*
55. How Does Search Understand What You Meant? *(link added when published)*
56. How Do You Teach an AI Who Is Connected to Whom? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
"What are the common causes across 500 incident reports?"
No single page holds the answer.

GraphRAG maps everything first, then answers from the map.

For big-picture questions plain RAG can't handle.

Do your hardest questions span many documents?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 56. How Do You Teach an AI Who Is Connected to Whom? [link]
You're here: 57. How Does an AI Answer Questions About a Whole Pile of Documents?
Next: 58. How Do You Keep an AI Tied to the Facts?

Full list: in the curtain raiser post.
```
