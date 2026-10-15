# Series 9: "We'll know when it breaks"

**Theme:** If you can't explain a wrong answer, you can't fix it.

**Level:** L3. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **A food-delivery app's support bot.** "Where's my order?", "Refund for the missing item." When it's wrong, the customer knows within minutes.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #WeWillKnow (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [It Said "Arriving in 5 Minutes". It Took an Hour. Can You Tell Why?](01-curtain-raiser.md) | "The AI was wrong" isn't a diagnosis. | Curtain raiser: observability for AI | Old tracking data, wrong order, or a bad prompt? | Draft for review |
| 2 | The Bill Tripled. Nothing Errored. Where Do You Look? | Silent changes often show up in cost first. | Cache hit rate and cost as health signals | One line added to the prompt; cache hits drop, the bill triples | Planned |
| 3 | How Do You Catch a Wrong Answer Nobody Reported? | Zero complaints can mean zero checks. | Canary questions, silent failures, refusal rate in both directions | "Where's my order?" answered with yesterday's status, and nobody complains | Planned |
| 4 | What Happens When You Break It on Purpose? | Find the weak spot before Friday night does. | Fault injection, testing fallbacks, blast radius | The tracking service goes slow at 8 PM on a Friday | Planned |
| 5 | Is It Up, or Is It Right? | Green dashboards, wrong answers. | Service targets for AI, incident response | 99.9% uptime, 12% wrong delivery times | Planned |
| 6 | So, Can You See Inside Your AI? | Five write-ups, one checklist. | Finale: the observability checklist | The support bot, explained answer by answer | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a car dashboard at night. Warning lights and gauges for each topic, one light blinking. Humor stays.
