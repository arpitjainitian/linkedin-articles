# 12. How Does a Small AI Learn From a Big One? | Distillation

![Cover](images/12-distillation-cover.png)

*Explain It Like Hello World series: Distillation*

"A distilled model." Small, fast AIs are often described this way. It sounds like whisky, and the idea isn't far off.

## The hello world

A senior doctor (the big AI) and a junior doctor (the small AI) see the same patients. The junior doesn't just learn the final diagnosis. They learn how the senior weighs every option: "probably flu, maybe a cold, unlikely anything worse".

That's the hello world: a small **student** model learns by copying a big **teacher** model's answers and reasoning.

## One step further

The teacher answers a large set of questions. The student is trained to match the teacher's outputs, including how likely it thought each option was, which carries more information than a single right answer.

The student ends up much smaller and cheaper, keeping much of the teacher's skill on the tasks it was taught.

## Where you've already met it

The "mini", "flash" or "lite" versions of popular models are often built this way. Fast on-device assistants too (write-up 20).

## The real name

**Distillation**, also called **knowledge distillation**.

- **Teacher model:** the big model being learned from.
- **Student model:** the small model doing the learning.
- **Distilled model:** the small model that results.

## What it's not

The student isn't a full copy. It loses some skill, especially outside what it was taught. Also check licences: some providers forbid using their outputs to train other models.

## Take this to your next meeting

1. Try the small, cheap version of a model before the big one.
2. Test it on your own hard cases; that's where students slip.
3. Check the licence before training on another model's outputs.

A small student, taught by a big teacher.

Next write-up (13): **Can an AI Learn From Data Another AI Wrote?**

Follow me for the next one. Have you tried a model's mini version?

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

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
A big AI is smart but slow and costly.
A small AI is fast but weaker.

What if the big one taught the small one? That's distillation.

Many fast, cheap AIs are built this way.

Have you tried a model's mini version?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 11. How Did the AI Learn to Be Polite? [link]
You're here: 12. How Does a Small AI Learn From a Big One?
Next: 13. Can an AI Learn From Data Another AI Wrote?

Full list: in the curtain raiser post.
```
