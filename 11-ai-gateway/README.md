# Series 11: "Just call the model API directly"

**Theme:** When many teams use AI, someone has to be the front door.

**Level:** L4. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **One office, many teams, one AI account.** Sales, HR, support and finance all call the same AI provider with the same key. What could go wrong?

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #AIGateway (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | Five Teams, One API Key. What Could Go Wrong? | Shared keys, shared bills, shared blame. | Curtain raiser: why a gateway | Nobody knows which team spent the budget | Planned |
| 2 | Who Is Allowed to Use Which Model? | Not every team needs the most expensive one. | Access control, keys per team, model policies | HR's bot calling the priciest model for every email | Planned |
| 3 | What Happens When One Team Floods the Provider? | One busy team can slow everyone down. | Rate limits, quotas, fair sharing | Sales' campaign blocks support's chatbot | Planned |
| 4 | What If the AI Provider Goes Down? | Every team breaks at once. | Fallbacks, multiple providers, routing | Monday morning outage, every bot silent | Planned |
| 5 | Who Spent What, on What? | A single bill hides everything. | Cost tracking per team, logs, governance | Finance can't split the AI invoice | Planned |
| 6 | So, Does Your Company Need an AI Front Door? | Five write-ups, one checklist. | Finale: the gateway checklist | The office, with one front door | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, one very simple running example, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
