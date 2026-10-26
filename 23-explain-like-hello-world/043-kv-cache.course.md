# Lesson 23.43: KV cache (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain KV cache with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

You're reading a book aloud and adding one word at a time. Would you start again from page 1 before each new word? Of course not. You remember what you've read and just add the next word.

## One step further

For every token, attention (write-up 13) works out some notes: what this word is about and how it relates to others. Without a cache, the AI would recalculate those notes for the whole text each time it writes one more word.

With the cache, it keeps the notes and only computes them for the new word. The cost: the notes take memory, and long chats mean big caches.

## Exercise

Explain KV cache to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for KV cache? *Neither does an AI. It keeps notes, called the KV cache.*
2. What is it not? *It's not memory of you or past chats. The cache lasts only while one answer (or one cached prompt) is being processed.*
3. Name one place you've already met it. *Long answers that keep streaming smoothly. "Prompt caching" discounts from AI providers build on the same idea of reusing work (cost is covered in Series 8).*

## Glossary

- **Cache:** saved work you can reuse instead of redoing.
- **Key and value:** the two kinds of notes attention keeps for each token.
- **Prompt caching:** reusing the cache for a repeated start of a prompt.

## Further reading

- The series plan: [README.md](README.md).
