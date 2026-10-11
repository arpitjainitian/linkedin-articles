# Series 5: "It's only a few cents per call"

**Theme:** AI costs are paid per use, and use always grows.

**Level:** L2. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **A school's homework-help bot.** 2,000 students, every evening, before every exam. Cheap per question, not cheap per term.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #AICostsAddUp (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | A Few Cents per Question. Why Is the Bill So Big? | Small numbers, multiplied, stop being small. | Curtain raiser: how AI costs add up | Exam week: 10x the questions | Planned |
| 2 | What Is a Token, and Why Am I Paying for It? | You pay by the word, both ways. | Tokens in and out, why long answers cost more | "Explain photosynthesis" answered in 2,000 words | Planned |
| 3 | Do You Need the Biggest Model for Every Question? | You don't hire a professor to check spelling. | Model choice, routing easy questions to cheaper models | "What's 7 times 8?" sent to the most expensive model | Planned |
| 4 | Why Pay Twice for the Same Answer? | Hundreds of students ask the same question. | Caching, reusing common answers, prompt caching | "When is the science exam?" asked 900 times | Planned |
| 5 | What Else Is Hiding on the Bill? | Tokens are only one line. | Embeddings, storage, logs, infrastructure, people | The search index costs more than the chatbot | Planned |
| 6 | How Do You Stop a Runaway Bill? | One bug can burn a month's budget overnight. | Budgets, alerts, limits, circuit breakers | A retry loop answers the same question 50,000 times | Planned |
| 7 | So, What Will Your AI Really Cost? | Six write-ups, one checklist. | Finale: estimate before you build | The school's bill, predicted honestly | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, one very simple running example, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
