# 17. Why Doesn't the AI Re-Read Everything for Every Word? | KV cache

![Cover](images/17-kv-cache-cover.png)

*Explain It Like Hello World series: KV cache*

"KV cache." It's in every article about making AI faster and cheaper. It sounds like a database setting.

## The hello world

You're reading a book aloud and adding one word at a time. Would you start again from page 1 before each new word? Of course not. You remember what you've read and just add the next word.

That's the hello world: the **KV cache** is the AI's notes on everything it has already read, so it doesn't redo the work for each new token (write-up 3).

## One step further

For every token, attention (write-up 5) works out some notes: what this word is about and how it relates to others. Without a cache, the AI would recalculate those notes for the whole text each time it writes one more word.

With the cache, it keeps the notes and only computes them for the new word. The cost: the notes take memory, and long chats mean big caches.

## Where you've already met it

Long answers that keep streaming smoothly. "Prompt caching" discounts from AI providers build on the same idea of reusing work (cost is covered in Series 8).

## The real name

The **KV cache** (key-value cache).

- **Cache:** saved work you can reuse instead of redoing.
- **Key and value:** the two kinds of notes attention keeps for each token.
- **Prompt caching:** reusing the cache for a repeated start of a prompt.

## What it's not

It's not memory of you or past chats. The cache lasts only while one answer (or one cached prompt) is being processed.

## Take this to your next meeting

1. Expect long chats to use more memory, partly because of the cache.
2. Put the fixed part of your prompt first, so providers can reuse it.
3. Know that "faster serving" headlines often mean smarter caching.

Don't reread the whole book for every new word.

Next write-up (18): **How Can a Small AI Make a Big AI Faster?**

Follow me for the next one. Did you know AIs keep notes while they write?

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
16. Why Doesn't the Whole AI Wake Up for Every Question? *(link added when published)*

**Previous series:**

- **Series 1, #JustAddRAG:** [start here](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/) or jump to [the grand finale](https://www.linkedin.com/pulse/15-so-should-you-really-just-add-rag-grand-finale-arpit-jain-ninmf/)
- **Series 2, Beyond Just RAG: From Answers to Actions:** [start here](https://www.linkedin.com/pulse/1-your-ai-can-answer-now-has-act-from-answers-actions-arpit-jain-po6lf/) or jump to [the finale](https://www.linkedin.com/pulse/8-so-should-your-ai-do-things-just-answer-finale-arpit-jain-x7cxf)

---

**Post text (copy and paste):**

```
Reading a book aloud, one word at a time.
You don't restart from page 1 before every word.

Neither does an AI. It keeps notes, called the KV cache.

That's how long answers stay fast.

Did you know AIs keep notes while they write?

#AI #GenAI #LearnAI #ExplainItLikeHelloWorld
```

**Series index (post as the first comment):**

```
Explain It Like Hello World

Start here: 1. AI words everyone uses. Nobody explains. [link]
Previous: 16. Why Doesn't the Whole AI Wake Up for Every Question? [link]
You're here: 17. Why Doesn't the AI Re-Read Everything for Every Word?
Next: 18. How Can a Small AI Make a Big AI Faster?

Full list: in the curtain raiser post.
```
