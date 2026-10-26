# 16. Why Doesn't the Whole AI Wake Up for Every Question? | Mixture of experts

![Cover](images/16-mixture-of-experts-cover.png)

*Explain It Like Hello World series: Mixture of experts*

"A mixture-of-experts model." Many of the newest big models use it. It sounds like a committee meeting.

## The hello world

Walk into a hospital with a broken arm. You don't see every doctor. A receptionist sends you to orthopaedics, and only those specialists get involved.

That's the hello world: a **mixture of experts** has many specialist parts and a router that sends each piece of text to only a few of them.

## One step further

For every token (write-up 2), a small router picks a handful of experts, often 2 out of 8, or a few out of hundreds. The others stay idle.

So a model can have a huge total size but use only a small part for each word. Mixtral 8x7B, for example, uses 2 of its 8 experts per token. It gets the knowledge of a big model at closer to the running cost of a small one.

## Where you've already met it

Several well-known open models (like Mixtral and DeepSeek) use this design, and many big commercial models are widely reported to.

## The real name

**Mixture of experts (MoE)**.

- **Expert:** one specialist part of the model.
- **Router:** the part that picks which experts handle each token.
- **Active parameters:** the knobs actually used for each token.

## What it's not

The experts aren't neat topics like "maths" or "law". They specialise in patterns the model found on its own. And all experts still have to be loaded in memory.

## Take this to your next meeting

1. Read "total" and "active" parameters separately when comparing models.
2. Expect MoE models to need lots of memory even if they're fast.
3. Judge them on your tasks, like any other model.

Big hospital, but you only see the doctors you need.

Next write-up (17): **Why Doesn't the AI Re-Read Everything for Every Word?**

Follow me for the next one. Did the hospital analogy make it click?

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

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
A broken arm. You don't see every doctor in the hospital.
Only the right specialists.

A mixture of experts sends each word to only a few specialists.

Big knowledge, smaller running cost.

Did the hospital analogy make it click?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 15. How Do You Fit a Giant AI on a Laptop? [link]
You're here: 16. Why Doesn't the Whole AI Wake Up for Every Question?
Next: 17. Why Doesn't the AI Re-Read Everything for Every Word?

Full list: in the curtain raiser post.
```
