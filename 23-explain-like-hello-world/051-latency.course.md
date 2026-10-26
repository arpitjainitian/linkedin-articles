# Lesson 23.51: Latency (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain latency with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

You ask a question in a shop. The time until the shopkeeper finishes answering is what you feel as "slow" or "fast".

## One step further

For AI, latency adds up from many steps: sending your message, looking up documents (write-up 53), the model reading the prompt, the model writing the answer token by token (write-up 11), and any tool calls in between.

Long prompts, big models, reasoning (write-up 71) and agents doing many steps all add delay. Smaller models, caching (write-up 44), streaming (write-up 25) and doing steps in parallel all cut it.

## Exercise

Explain latency to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for latency? *That wait is latency: every step between asking and answering.*
2. What is it not? *Latency isn't only about the model. Slow document search, network hops and extra steps often add more delay than the AI itself. (Performance in production is covered in #JustAddRAG 11.)*
3. Name one place you've already met it. *The spinner before a chatbot replies. Voice assistants that feel awkward because of the pause.*

## Glossary

- **Latency:** the delay between request and response.
- **Time to first token:** the delay before the first word (write-up 52).
- **Throughput:** how many requests a system can handle.

## Further reading

- The series plan: [README.md](README.md).
