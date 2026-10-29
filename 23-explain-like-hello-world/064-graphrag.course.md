# Lesson 23.64: GraphRAG (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain GraphRAG with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Ask: "What are the common causes across all 500 incident reports from last year?" Normal RAG (write-up 58) finds a few similar pages, but no single page holds the answer.

## One step further

An AI reads every document and extracts the important things and how they connect. Related groups are summarised. When a big-picture question arrives, the system answers from those summaries and links, not just from a few matching chunks.

It's good for "across everything" and "how is X connected to Y" questions. It costs more to build and to keep updated than plain RAG.

## Exercise

Explain GraphRAG to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for GraphRAG? *GraphRAG maps everything first, then answers from the map.*
2. What is it not? *GraphRAG isn't automatically better than RAG. For simple "find the answer on a page" questions, plain RAG is cheaper and enough. (Knowledge graphs in production are covered in Series 13.)*
3. Name one place you've already met it. *Enterprise research and investigation tools that summarise themes across thousands of documents.*

## Glossary

- **Entity:** a person, system, place or event pulled from text.
- **Community summary:** a summary of a group of connected entities.
- **Multi-hop question:** one that needs several linked facts.

## Further reading

- The series plan: [README.md](README.md).
