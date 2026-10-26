# 10. How Do You Teach an AI Something New? | Pretraining, fine-tuning and LoRA

![Cover](images/10-fine-tuning-lora-cover.png)

*Explain It Like Hello World series: Pretraining, fine-tuning and LoRA*

"We'll fine-tune it." "Just use LoRA." Teams say these when an AI doesn't talk the way they want. What actually changes?

## The hello world

Think of a chef.

**Pretraining** is culinary school: years of learning to cook everything.
**Fine-tuning** is a short course in one cuisine, say South Indian, that changes how the chef cooks.
**LoRA** is a recipe card clipped to the chef's apron: small, cheap, removable, and it changes a few dishes without retraining the chef.

## One step further

Pretraining builds the model from scratch on huge amounts of text. Very few companies do it.

Fine-tuning continues training on a smaller, focused set of examples, adjusting the model's knobs (write-up 8) towards your style or task.

LoRA freezes the original knobs and trains a small add-on of extra knobs instead. It's much cheaper, and you can swap add-ons for different tasks.

## Where you've already met it

Company chatbots that answer in a fixed brand tone. Image apps that learn your face from a handful of photos often use a LoRA-style add-on.

## The real name

**Pretraining**, **fine-tuning** and **LoRA** (low-rank adaptation).

- **Pretraining:** the first, huge training run that builds the model.
- **Fine-tuning:** extra training on focused examples.
- **LoRA:** a small trainable add-on; the main model stays frozen.

## What it's not

Fine-tuning is mainly for style, format and behaviour, not for adding fresh facts. For facts that change, looking them up at question time usually works better (#JustAddRAG).

## Take this to your next meeting

1. Try better instructions and examples first; they cost nothing.
2. Fine-tune for how it should answer, not for what's new this week.
3. Ask whether a LoRA add-on would do before paying for full fine-tuning.

School, a short course, a recipe card. Pick the smallest that works.

Next write-up (11): **How Did the AI Learn to Be Polite?**

Follow me for the next one. Has your team ever fine-tuned when a better prompt would have done?

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

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
"Let's fine-tune the model."
On what, and why?

Pretraining is chef school. Fine-tuning is a short course. LoRA is a recipe card.

Start with the smallest change that works.

Has your team ever fine-tuned when a better prompt would have done?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 9. Is the AI Learning While You Chat With It? [link]
You're here: 10. How Do You Teach an AI Something New?
Next: 11. How Did the AI Learn to Be Polite?

Full list: in the curtain raiser post.
```
