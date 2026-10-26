# Lesson 23.63: Tool calling (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain tool calling with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Ask an AI "What's the weather in Pune right now?" It can't know: its knowledge stopped at training (write-up 27). So it says, in effect: "Please run the weather tool for Pune." Your app runs it, gets "31°C, sunny", and hands it back. The AI replies: "It's 31°C and sunny in Pune."

## One step further

You describe the available tools to the AI: their names, what they do and what they need. When a tool would help, the AI replies with a structured request (write-up 24) instead of an answer. Your code runs the tool and returns the result, and the AI continues.

The AI never runs anything itself; your software stays in control of what actually happens.

## Exercise

Explain tool calling to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for tool calling? *So it asks your app to run a weather tool. That's tool calling.*
2. What is it not? *The AI doesn't run the tool or access your systems directly. Your code decides whether and how to run each request, which is where safety checks belong.*
3. Name one place you've already met it. *Chatbots that search the web, check your calendar or look up an order. Every AI agent (write-up 61).*

## Glossary

- **Tool:** a function or service the AI can request.
- **Tool description:** what the AI is told the tool does.
- **Tool result:** what comes back after running it.

## Further reading

- The series plan: [README.md](README.md).
