# Lesson 23.65: Hybrid search (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain hybrid search with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A library with two catalogues. One lists books by exact title and author. The other groups books by what they are about. Use both, and you find the book you named and the ones you didn't know to ask for.

## One step further

Keyword search (sometimes called sparse search) is great for exact names, codes and product numbers. Semantic search (dense search) finds similar meanings even when the words differ. Hybrid search runs both and merges the two lists, using a method such as reciprocal rank fusion.

In RAG systems (write-up 60), hybrid search often beats either method alone, because each one makes up for the other's blind spots. A reranker can then sort the merged list.

## Exercise

Explain hybrid search to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for hybrid search? *Hybrid search combines both, so you find exact matches and similar meanings.*
2. What is it not? *Hybrid search isn't always needed. For a small set of documents, one method may be enough. Add the second method when you see misses on exact terms or on meaning.*
3. Name one place you've already met it. *Shopping and document search that finds an exact product code and similar items, and company search tools that find both a policy number and a related policy.*

## Glossary

- **Keyword search:** finds exact words and codes.
- **Dense search:** matches by meaning, using embeddings.
- **Rank fusion:** merging two ranked lists into one.

## Further reading

- The series plan: [README.md](README.md).
