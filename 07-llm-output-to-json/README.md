# Series 7: "LLM output → JSON → done"

**Theme:** Getting text from an LLM is easy. Getting reliable data out of it is engineering.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **Turning a grocery list into an order.** "2 kg rice, milk, and those biscuits I like" becomes items, quantities and prices.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #StructureIsHard (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | Why Does My "Perfect" JSON Break One Time in Fifty? | Mostly right is still broken for a computer. | Curtain raiser: structured output | One missing bracket and the order fails | Planned |
| 2 | What If the Model Invents a Field? | "Delivery_mood: happy" isn't in your schema. | Schemas, validation, strict output modes | A made-up "discount" field the shop never offered | Planned |
| 3 | What Do You Do With "Those Biscuits I Like"? | Real requests are vague. | Missing, ambiguous and partial data, asking back | Which biscuits? How many? | Planned |
| 4 | Should You Retry, Repair or Refuse? | Every bad output needs a plan. | Retries, repair, fallbacks, human review | "2 kg" read as "2 kilograms of milk" | Planned |
| 5 | What Happens When the Format Changes Next Month? | Schemas grow. Old prompts don't know. | Versioning, backwards compatibility | New field "brand"; old orders break | Planned |
| 6 | So, Can You Trust Your Model's Output? | Five write-ups, one checklist. | Finale: the structured-output checklist | The grocery order, validated end to end | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, one very simple running example, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
