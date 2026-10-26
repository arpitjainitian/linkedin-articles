# 9. Is the AI Learning While You Chat With It? | Training vs inference

![Cover](images/09-training-vs-inference-cover.png)

*Explain It Like Hello World series: Training vs inference*

"Training" and "inference" appear in every AI budget, chip announcement and data policy. Most people assume the AI learns from every chat. Usually, it doesn't.

## The hello world

A student spends years at school. That's **training**: slow, expensive, done once.

Then the student sits an exam and answers one question. That's **inference**: quick, cheap, done millions of times.

When you chat with an AI, it's sitting the exam. It isn't back at school.

## One step further

Training turns the knobs (write-up 8) using huge amounts of text and computing power, over weeks or months. Then the knobs are frozen and the model is released.

Every question you ask is inference: the frozen model makes its guesses. It doesn't change its knobs because of your chat. A company may later use chats (if its policy allows) to train the **next** version, but that's a separate, later step.

## Where you've already met it

Chip news: some chips are built for training, others for inference. Privacy settings that ask "may we use your chats to improve our models?" That's about future training.

## The real name

**Training** and **inference**.

- **Training:** teaching the model by adjusting its knobs on lots of data.
- **Inference:** using the trained, frozen model to answer.
- **Knowledge cutoff:** the date its training data ends.

## What it's not

Inference isn't learning. If an AI seems to remember you, that's a separate memory feature or the chat history on its desk (write-up 6), not new training.

## Take this to your next meeting

1. Remember the AI's knowledge stops at its training cutoff unless it can search.
2. Check your vendor's policy on using your data for future training.
3. Expect most of your AI bill to be inference, paid per question.

School is training. Every answer is an exam.

Next write-up (10): **How Do You Teach an AI Something New?**

Follow me for the next one. Did you think the AI was learning from your chats?

**Earlier in this series:**

1. AI words everyone uses. Nobody explains. (the curtain raiser post) *(link added when published)*
2. How Does an AI Read a Word? *(link added when published)*
3. How Does an AI Write a Sentence? *(link added when published)*
4. How Does an AI Know "King" Is Close to "Queen"? *(link added when published)*
5. How Does an AI Know What "It" Means? *(link added when published)*
6. Why Does an AI Forget the Start of a Long Chat? *(link added when published)*
7. Why Does the Same Question Get Different Answers? *(link added when published)*
8. What Does "70B" Actually Mean? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
You corrected the AI yesterday.
Today it makes the same mistake.

Training is school. Chatting is the exam. The AI isn't learning mid-exam.

Your chat doesn't change the model's knobs.

Did you think the AI was learning from your chats?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 8. What Does "70B" Actually Mean? [link]
You're here: 9. Is the AI Learning While You Chat With It?
Next: 10. How Do You Teach an AI Something New?

Full list: in the curtain raiser post.
```
