# Lesson 23.60: Vector database (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain vector database with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A normal database is a filing cabinet sorted by name: find "Invoice 4471" instantly. But ask it for "documents about late payments" and it only finds exact words.

## One step further

Every chunk of text is turned into an embedding, a long list of numbers, and stored. A question is turned into an embedding too. The database quickly finds the nearest points among millions, using clever shortcuts so it doesn't compare every single one.

It powers semantic search (write-up 61) and RAG (write-up 58). Many ordinary databases now add vector search too.

## Exercise

Explain vector database to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for vector database? *A vector database is a filing cabinet sorted by meaning.*
2. What is it not? *A vector database doesn't understand or check facts. It finds similar-sounding text, which can be similar but wrong. And you may not need a separate one; your existing database might do vectors.*
3. Name one place you've already met it. *Behind AI search in apps, "similar products" suggestions, and document chatbots.*

## Glossary

- **Vector:** a list of numbers representing meaning.
- **Nearest neighbour:** the closest stored point to your question.
- **Index:** the structure that makes searching fast.

## Further reading

- The series plan: [README.md](README.md).
