# Series 16: "Let's make it agentic"

**Theme:** An agent is a loop that plans, acts and checks. Powerful, and easy to get wrong.

**Level:** L4. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **A weekend-trip planning assistant.** An AI that plans a weekend in Jaipur: hotel, weather, train, restaurant. Many steps, one goal.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #AgentsExplained (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | What Makes an AI an Agent? | Answering is easy. Doing is different. | Curtain raiser: chatbot vs agent | "Plan my weekend in Jaipur" | Planned |
| 2 | How Does an Agent Decide What to Do Next? | Plan, act, look, repeat. | The agent loop, planning and reflecting | Checks the weather before booking an open-air dinner | Planned |
| 3 | Why Does My Agent Keep Going in Circles? | Loops need exits. | Stop conditions, step limits, budgets | Searches hotels 40 times and never books | Planned |
| 4 | When Is a Simple Workflow Better Than an Agent? | Not every task needs freedom. | Workflows vs agents, predictability | Booking the same train every Friday doesn't need an agent | Planned |
| 5 | What Happens When a Step Fails Halfway? | The train is booked. The hotel isn't. | Error handling, rollback, retries | Half a trip planned, money spent | Planned |
| 6 | How Do You Test Something That Takes a Different Path Every Time? | Same request, different steps. | Evaluating agents, task success, traces | Two runs, two different hotels, both fine? | Planned |
| 7 | So, Should You Make It Agentic? | Six write-ups, one checklist. | Finale: the agent checklist | The weekend trip, planned safely | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, one very simple running example, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
