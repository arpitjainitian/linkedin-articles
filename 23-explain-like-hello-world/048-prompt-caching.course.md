# Lesson 23.48: Prompt caching (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain prompt caching with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A teacher reads the same 50-page rulebook aloud before every exam question. Wasteful. Better: read it once, keep notes, and for each new question, only read the question.

## One step further

Many apps send the same long beginning every time: instructions, policies, a document. The provider stores the processed version of that beginning (the KV cache, write-up 47) for a short while. If your next request starts the same way, it skips that work and charges much less for those tokens.

It only helps if the repeated part comes first and is exactly the same. Change one character at the start and the saving is lost.

## Exercise

Explain prompt caching to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for prompt caching? *Prompt caching reads it once and reuses the notes.*
2. What is it not? *It's not caching answers. The AI still writes a fresh answer; only the reading of the repeated part is saved. (Cost strategies are covered in Series 8.)*
3. Name one place you've already met it. *"Cached input" lines on AI bills. Faster replies in chat apps that reuse long instructions.*

## Glossary

- **Cache hit:** the repeated start was found and reused.
- **Prefix:** the beginning part of a prompt.
- **Cache lifetime:** how long the saved work is kept.

## Further reading

- The series plan: [README.md](README.md).
