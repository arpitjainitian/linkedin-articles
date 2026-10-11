# Series 8: "Let the LLM handle the business rules"

**Theme:** LLMs are great with language and unreliable with rules. Know where the line is.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **A cinema ticket booth.** Students get 20% off, kids under 3 go free, Tuesdays are half price. Simple rules, until an LLM applies them.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #RulesNeedCode (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | Why Did the AI Give a Student Discount to a Grandmother? | Rules need to be applied the same way every time. | Curtain raiser: deterministic vs probabilistic | "I'm a student of life" gets 20% off | Planned |
| 2 | Which Decisions Should Never Be Left to an LLM? | Money, eligibility and compliance need certainty. | Where code decides and where the LLM explains | Tuesday half price, applied on Wednesday | Planned |
| 3 | How Do You Split the Work Between Code and the LLM? | Code decides, the LLM talks. | Rules engines, tool calling, the LLM as the friendly front | Code calculates the price; the LLM explains it nicely | Planned |
| 4 | What Happens When the Rules Change? | Rules in a prompt hide. Rules in code are visible. | Rule changes, versioning, testing rules | New Diwali offer added to the prompt, forgotten in code | Planned |
| 5 | How Do You Prove the Right Rule Was Applied? | "The AI decided" isn't an audit answer. | Audit trails, explanations, consistency | A customer disputes their ticket price | Planned |
| 6 | So, Who Should Decide: the Code or the Model? | Five write-ups, one checklist. | Finale: the rules checklist | The ticket booth, fair every time | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, one very simple running example, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
