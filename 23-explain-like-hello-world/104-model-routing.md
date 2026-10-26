# 104. Should Every Question Go to the Most Expensive AI? | Model routing

![Cover](images/104-model-routing-cover.png)

*Explain It Like Hello World series: Model routing*

"Model routing." "AI router." The trick behind cutting AI bills without making answers worse.

## The hello world

A hospital doesn't send every patient to the top surgeon. A nurse handles a sore throat; the specialist handles the complicated case.

That's the hello world: **model routing** sends each request to the right-sized AI: small and cheap for easy questions, big and expensive for hard ones.

## One step further

A router looks at each request (by rules, a small classifier, or a quick AI check) and picks a model. Easy questions go to a small model (write-up 49); hard ones go to a big or reasoning model (write-up 71). Some routers try the small model first and escalate if its answer isn't good enough.

Done well, most requests go to cheap models and quality holds. Done badly, hard questions get weak answers. Evals (write-up 88) keep it honest.

## Where you've already met it

AI apps with an "auto" model setting. Chatbots that quickly answer simple questions and take longer on hard ones.

## The real name

**Model routing**, done by a **router**.

- **Router:** the component that picks a model per request.
- **Escalation:** passing a request up to a stronger model.
- **Cost per answer:** what each answer costs, on average.

## What it's not

Routing isn't just "always use the cheapest". It's matching each question to a good-enough model, and checking that quality didn't drop. (My Today in AI No. 007 covers AI routers.)

## Take this to your next meeting

1. Look at your requests: how many are actually easy?
2. Route easy ones to small models and measure quality.
3. Escalate when the small model is unsure.

The nurse for the sore throat. The surgeon for the hard case.

Next write-up (105): **Your AI Dictionary, One Line per Word** (the finale)

Follow me for the next one. What share of your AI questions really need the biggest model?

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
57. How Does an AI Answer Questions About a Whole Pile of Documents? *(link added when published)*
58. How Do You Keep an AI Tied to the Facts? *(link added when published)*
59. How Do You Check Where an AI Got Its Answer? *(link added when published)*
60. Can an AI Do Your Research for You? *(link added when published)*
61. What Makes an AI an "Agent"? *(link added when published)*
62. What Does "Agentic" Really Mean? *(link added when published)*
63. How Does an AI Check the Weather? *(link added when published)*
64. Why Is Everyone Talking About MCP? *(link added when published)*
65. How Do AI Agents Talk to Each Other? *(link added when published)*
66. Are Several AI Agents Better Than One? *(link added when published)*
67. How Does an AI Remember You? *(link added when published)*
68. How Does an AI Use a Computer Like You? *(link added when published)*
69. What's the Difference Between a Copilot and an Agent? *(link added when published)*
70. Where Should an AI Agent Do Its Work? *(link added when published)*
71. Why Does the AI Think Before It Answers Now? *(link added when published)*
72. How Can One AI Read, See and Listen? *(link added when published)*
73. How Does an AI Draw a Picture From Noise? *(link added when published)*
74. How Does an AI Talk Back Without a Pause? *(link added when published)*
75. How Does an AI Make a Video From a Sentence? *(link added when published)*
76. How Can a Video of Someone Be Fake? *(link added when published)*
77. Can an AI Copy Your Voice From a Few Seconds of Audio? *(link added when published)*
78. Who Is That Presenter, If Nobody Filmed Them? *(link added when published)*
79. What's a Digital Twin, and Why Do Factories Want One? *(link added when published)*
80. What Does "Open" Mean in Open AI Models? *(link added when published)*
81. Can an AI Imagine What Happens Next? *(link added when published)*
82. When Does AI Get a Body? *(link added when published)*
83. Why Does an AI Sound Sure When It's Wrong? *(link added when published)*
84. How Do You Stop an AI Saying the Wrong Thing? *(link added when published)*
85. How Do People Trick an AI Into Breaking Its Rules? *(link added when published)*
86. Can a Web Page Give Orders to Your AI? *(link added when published)*
87. Who Attacks an AI on Purpose? *(link added when published)*
88. How Do You Know an AI Is Getting Better? *(link added when published)*
89. Can One AI Mark Another AI's Homework? *(link added when published)*
90. How Does an AI End Up Unfair? *(link added when published)*
91. Can an AI Tell You Why It Decided? *(link added when published)*
92. How Do You Make Sure an AI Wants What We Want? *(link added when published)*
93. Can You Tell If AI Wrote This? *(link added when published)*
94. Who Makes the Rules for AI? *(link added when published)*
95. Is Your Team Using AI You Don't Know About? *(link added when published)*
96. Why Do Countries Want Their Own AI? *(link added when published)*
97. What Does "Scored 90% on a Benchmark" Mean? *(link added when published)*
98. Can You Build an App by Describing It? *(link added when published)*
99. Why Is the Internet Filling Up With "AI Slop"? *(link added when published)*
100. How Do You Get Found When People Ask AI Instead of Google? *(link added when published)*
101. What Makes a Company "AI-Native"? *(link added when published)*
102. Who Keeps an AI Running After Launch? *(link added when published)*
103. Why Do Companies Put a Front Door in Front of AI? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
A hospital doesn't send every patient to the top surgeon.
A nurse handles the sore throat.

Model routing sends each AI question to the right-sized model.

Cheap for easy, powerful for hard.

What share of your AI questions really need the biggest model?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 103. Why Do Companies Put a Front Door in Front of AI? [link]
You're here: 104. Should Every Question Go to the Most Expensive AI?
Next: 105. Your AI Dictionary, One Line per Word

Full list: in the curtain raiser post.
```
