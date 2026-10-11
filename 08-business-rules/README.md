# Series 8: "Let the LLM handle the business rules"

**Theme:** LLMs are great with language and unreliable with rules. Know where the line is.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **An airline's refund and cancellation assistant.** Refunds depend on fare type, timing and fees. Clear rules, real money.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #RulesNeedCode (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | Why Did the AI Promise a Full Refund on a Non-Refundable Ticket? | Rules need to be applied the same way every time. | Curtain raiser: deterministic vs probabilistic | "Of course! Full refund, no fees" | Planned |
| 2 | Which Decisions Should Never Be Left to an LLM? | Money, eligibility and compliance need certainty. | Where code decides and where the LLM explains | Cancellation fee calculated differently every time | Planned |
| 3 | How Do You Split the Work Between Code and the LLM? | Code decides, the LLM talks. | Rules engines, tool calling, the LLM as the friendly front | Code calculates the refund; the LLM explains it kindly | Planned |
| 4 | What Happens When the Rules Change? | Rules in a prompt hide. Rules in code are visible. | Rule changes, versioning, testing rules | New monsoon waiver added to the prompt, missed in code | Planned |
| 5 | How Do You Prove the Right Rule Was Applied? | "The AI decided" isn't an answer for a regulator. | Audit trails, explanations, consistency | A passenger disputes their refund amount | Planned |
| 6 | So, Who Should Decide: the Code or the Model? | Five write-ups, one checklist. | Finale: the rules checklist | The refund assistant, fair every time | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
