# Lesson 23.63: Semantic search (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain semantic search with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

Search a recipe site for "quick dinner without meat". Old search looks for those exact words and misses "20-minute vegetarian pasta".

## One step further

Both your query and the documents are turned into embeddings (write-up 13), points on a meaning map. Results are the documents closest to your query, even if they share no words.

It's great for natural questions, but weaker for exact things like product codes or names. That's why good systems mix it with keyword search, called hybrid search.

## Exercise

Explain semantic search to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for semantic search? *Semantic search finds results by meaning, not just matching words.*
2. What is it not? *Semantic search isn't always better. For exact names, IDs and codes, plain keyword search often wins.*
3. Name one place you've already met it. *Search boxes that find "budget airfares" when you typed "cheap flights". Photo apps that find "beach" without tags.*

## Glossary

- **Semantic:** about meaning.
- **Keyword search:** matching the exact words.
- **Hybrid search:** combining meaning and keyword search.

## Further reading

- The series plan: [README.md](README.md).
