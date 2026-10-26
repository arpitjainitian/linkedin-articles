# Lesson 23.61: AI agent (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain AI agent with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A chatbot is like a librarian: you ask, it answers, done. An agent is like a personal assistant: you say "book me a meeting with Priya next week", and it checks calendars, picks a slot, sends the invite and tells you when it's done.

## One step further

Under the hood, it's a loop: the AI thinks about the next step, calls a tool (write-up 63), reads the result, and decides again, until the goal is met or it gets stuck.

That freedom is the power and the risk: an agent can take wrong steps, loop, or act on bad information. What goes wrong in practice is the theme of my Series 2, "Beyond Just RAG: From Answers to Actions".

## Exercise

Explain AI agent to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for AI agent? *A chatbot is the librarian. An AI agent is the assistant who gets it done.*
2. What is it not? *An agent isn't just a chatbot with a new name, and it doesn't need to be autonomous for everything. Many tasks are better as a fixed workflow.*
3. Name one place you've already met it. *Coding assistants that edit files and run tests. Assistants that book, order or file things for you.*

## Glossary

- **Agent:** an AI that plans steps and acts with tools to reach a goal.
- **Tool:** something the agent can use: search, calendar, database.
- **Agent loop:** think, act, check, repeat.

## Further reading

- The series plan: [README.md](README.md).
