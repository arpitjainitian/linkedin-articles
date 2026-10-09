# 5. Is Your Chatbot Answering a Question That Needs a Database?

![Cover](images/05-right-tool-cover.png)

*Just add RAG series: Picking the right tool*

"Which of my documents expire this year?"

Sounds like a perfect question for an AI assistant. It isn't. It's a database query wearing a chatbot costume.

RAG is built to find a few relevant passages and answer from them. This question needs every document checked, every date compared, and a list counted. Search for meaning can't do that. A simple database query can, in milliseconds.

*New to terms like text-to-SQL or query routing? Cheat sheet at the end.*

## Why picking the right tool matters

- **RAG sees a few chunks, not everything.** It answers from the top 3 results. Ask "how many?" and it counts what it was handed, not what you have.
- **The wrong tool still sounds right.** An incomplete list arrives in perfect sentences. Nobody notices the missing items.
- **Users don't know the difference.** They just ask. Telling a search question from a counting question is the system's job, not theirs.
- **The right tool is often cheaper.** A database query costs almost nothing. A long LLM answer built from guesswork costs tokens and trust.

## What my assistant could, and couldn't, answer

My PostgreSQL database already had a `documents` table, with each document's type, file name and upload date, and an `extractions` table holding the OCR text.

So "how many documents have I uploaded?" was one SQL line away. But "which documents expire this year?" wasn't, because the expiry date lived only inside the raw text: `समाप्ति की तिथि 29/09/2024`. Not in a column anyone could query. The answer existed. It just wasn't anywhere a database could count it.

## Six kinds of questions, six different tools

- **Counting and totals.** "How many documents do I have?" RAG sees the top 3, so it may happily say three. *Fix: answer from the database, not from search.*
- **Lists across everything.** "Which documents expire this year?" *Fix: pull the expiry date into its own column when the document arrives, then query it.*
- **Comparisons over time.** "Did my salary go up between March and April?" *Fix: store the amounts as numbers, let the database compare, and let the LLM explain.*
- **Calculations.** "How many days until my passport expires?" LLMs are great with words and slightly creative with arithmetic. *Fix: do the maths in code.*
- **Live information.** "Is my visa appointment confirmed?" No document knows that. *Fix: ask the system that does, through an API.*
- **Questions about meaning.** "What does my travel policy say about lost baggage?" *This one really is RAG's job.*

## The right-tool toolkit, in plain words

1. **A receptionist at the front desk**

   Every question is sent to the right counter: search, database, calculator or live system. That's **query routing**.
2. **File the facts when the mail arrives**

   When a document is uploaded, pull out its key facts (expiry date, amounts, IDs) into proper columns. That's **structured extraction**.
3. **Turn the question into a database query**

   "Which documents expire this year?" becomes a query the database can run. That's **text-to-SQL**.
4. **Use a calculator, not mental maths**

   The LLM asks a piece of code to do the date maths and uses the result. That's **tool calling**.
5. **Ask the source directly**

   For anything live, call the system that owns the truth. That's an **API tool**.
6. **Find with the database, explain with the AI**

   The database lists the expiring documents. The LLM writes the friendly summary. That's **hybrid SQL plus RAG**.

## How it works in practice

The router is the first step after the question arrives. A small model, or even a simple classifier, labels the question: search, count, calculate, live, or "can't help". Then it goes to the matching tool.

Text-to-SQL needs guard rails:

- **Read-only** database access. The AI reads, never writes.
- Only **approved tables**, always filtered to **this user's rows**.
- A **row limit**, and every generated query logged.

**Product** decides which question types to support. **Data owners** decide which tables the AI may see. **Security** reviews the access. **Engineers** build the router.

## How do you know it works?

List the 20 questions users ask most, and label each with the tool it needs. Then test two things: did the router pick the right tool, and was the answer right? A correct answer from the wrong tool is luck, not design.

## Cheat sheet: the words you'll hear, with examples

- **Structured data:** facts in tables with named columns. *My `documents` table: type, file name, upload date.*
- **Unstructured data:** free text, scans and PDFs. *My passport's OCR text in the `extractions` table.*
- **Schema:** the layout of a database: tables, columns, types. *`documents` has `doc_type`, `filename`, `created_at`.*
- **SQL:** the standard language for asking a database questions. *"Count my documents where type is passport."*
- **Aggregation:** combining many rows into one answer: count, sum, average. *"How many documents do I have?"*
- **Query routing:** sending each question to the right tool. *Travel-rules question to RAG, counting question to SQL.*
- **Intent:** what kind of question it is. *"Which expire this year?": a list, not a search.*
- **Structured extraction:** pulling key facts into columns at upload time. *Expiry date 29/09/2024 saved as a date column.*
- **Text-to-SQL:** an LLM turning a question into a database query. *"Which expire this year?" becomes a query on the expiry column.*
- **Tool calling (or function calling):** the LLM asking code to do a job. *A date function returns the days until expiry.*
- **API:** a way for one system to ask another for live data. *The visa appointment system.*
- **Read-only access:** permission to read, never change. *The AI can list documents, not delete them.*

## Take this to your next kickoff meeting

1. List the top 20 questions users will ask, and label each: search, count, calculate, or live data.
2. Pull key facts like dates, amounts and IDs into columns when documents arrive, not when questions do.
3. Give the AI read-only, user-filtered database access, never the keys to everything.

Not every question is a search. Some are just a database query with good manners.

Next write-up (6): **What happens when your AI finds two versions of the truth?** (Versions and ownership)

Follow me for the next one. And tell me: what's a question your users asked a chatbot that really needed a spreadsheet?

**Earlier in this series:**

- 0. [Why does "Just add RAG" sound like 2 weeks but take 6 months?](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/)
- 1. [Why can't your AI read a PDF that a 10-year-old can?](https://www.linkedin.com/pulse/why-cant-your-ai-read-pdf-10-year-old-can-arpit-jain-fimif/)
- 2. [What if the answer was in your docs, but you cut it in half?](https://www.linkedin.com/pulse/what-answer-your-docs-you-cut-half-arpit-jain-pczxf/)
- 3. [Is your AI hallucinating, or just looking in the wrong place?](https://www.linkedin.com/pulse/your-ai-hallucinating-just-looking-wrong-place-arpit-jain-byozf/)

---

**Post text to share the article:**

> "Which of my documents expire this year?"
>
> Sounds like a chatbot question. It's a database query wearing a chatbot costume.
>
> Write-up 5 in my #JustAddRAG series: why RAG counts what it was handed, not what you have, the six kinds of questions that each need a different tool, and three things to take to your next kickoff meeting.
>
> What's a question your users asked a chatbot that really needed a spreadsheet?

**Hashtags:** #AIEngineering #RAG #GenAI #EnterpriseAI #JustAddRAG
