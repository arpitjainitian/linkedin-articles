# Lesson 23.18: Context rot (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain context rot with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A meeting that runs for three hours. By the end, nobody remembers the first decision, and the notes have so much in them that the key point is buried.

## One step further

The context window (write-up 16) has a fixed size, and the model pays attention across all of it. As the context grows, old details may be overlooked, and irrelevant text competes for attention. Research on long contexts has found that models often miss facts placed in the middle of long inputs.

The fixes are practical: keep only what matters, summarise old turns, start a fresh chat for a new task, and retrieve the right passages instead of pasting everything.

## Exercise

Explain context rot to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for context rot? *Context rot is an AI losing track as its context fills up.*
2. What is it not? *A bigger context window doesn't fix context rot by itself. A longer window can hold more text, but it doesn't guarantee the model uses all of it well.*
3. Name one place you've already met it. *Long chats where an AI forgets an earlier instruction, and tools that tell you to start a new chat when the thread gets long.*

## Glossary

- **Context rot:** answers degrading as context grows.
- **Lost in the middle:** facts in the middle of long input are missed more often.
- **Summarising:** shortening old turns into their key points.

## Further reading

- The series plan: [README.md](README.md).
