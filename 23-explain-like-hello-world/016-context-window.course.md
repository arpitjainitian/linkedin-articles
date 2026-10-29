# Lesson 23.16: Context window (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain context window with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Picture a desk. Everything the AI can see right now has to fit on it: your question, the chat so far, any documents you pasted, and its answer.

## One step further

The desk is measured in tokens (write-up 11). Everything counts: your messages, its replies, hidden instructions, pasted files.

Most chat apps quietly drop or summarise old messages when the desk fills up. That's why a long chat can "forget" what you said at the start. Bigger desks help, but AIs can still miss details buried in the middle of a very long desk, and bigger desks cost more per question.

## Exercise

Explain context window to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for context window? *An AI's context window is its desk. When it's full, something falls off.*
2. What is it not? *The context window isn't memory. When the chat ends, the desk is cleared. Remembering you across chats is a separate feature (covered in Series 12, memory).*
3. Name one place you've already met it. *A long chat where the AI forgets your name or the rules you set at the start. Or a "this document is too long" error.*

## Glossary

- **Context window:** the most text an AI can consider at once.
- **Truncation:** cutting older text to make room.
- **Long context:** models with very large windows.

## Further reading

- The series plan: [README.md](README.md).
