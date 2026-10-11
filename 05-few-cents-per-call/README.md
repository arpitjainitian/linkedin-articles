# Series 5: "It's only a few cents per call"

**Theme:** AI costs are paid per use, and use always grows, especially on sale days.

**Level:** L2. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **A product-question assistant on a shopping site.** Millions of shoppers ask: "Does this phone support dual SIM?", "Will this fit a 6-foot bed?"

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #AICostsAddUp (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | A Few Cents per Question. Why Is the Sale-Day Bill So Big? | Small numbers, multiplied by millions, stop being small. | Curtain raiser: how AI costs add up | Big sale day: 20x the questions | Planned |
| 2 | What Is a Token, and Why Are You Paying for It? | You pay by the word, both ways. | Tokens in and out, why long answers cost more | "Does it have dual SIM?" answered in 300 words | Planned |
| 3 | Do You Need the Biggest Model for Every Question? | You don't send a professor to check a price tag. | Model choice, routing easy questions to cheaper models | "What colours does it come in?" sent to the most expensive model | Planned |
| 4 | Why Pay Twice for the Same Answer? | Thousands of shoppers ask the same question. | Caching, reusing answers, prompt caching | "Is it waterproof?" asked 40,000 times | Planned |
| 5 | What Else Is Hiding on the Bill? | Tokens are only one line. | Embeddings, search, storage, logs, people | Re-indexing the whole catalogue costs more than the chats | Planned |
| 6 | How Do You Stop a Runaway Bill? | One bug can burn a month's budget overnight. | Budgets, alerts, limits, circuit breakers | A retry loop answers the same question 2 lakh times | Planned |
| 7 | So, What Will Your AI Really Cost? | Six write-ups, one checklist. | Finale: estimate before you build | The shopping assistant's bill, predicted honestly | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
