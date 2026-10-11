# Series 17: "Let it do its own research"

**Theme:** Letting AI search on its own is like a good researcher: smarter, slower, and needing supervision.

**Level:** L5. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **Contract review for the legal team.** "Which of our vendor contracts let them exit without notice?" Hundreds of contracts, one answer.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #LetItResearch (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | What If the AI Could Search More Than Once? | One search rarely answers a real question. | Curtain raiser: plain RAG vs agentic RAG | One search finds 3 contracts; there are 40 | Planned |
| 2 | How Does the Agent Decide What to Search Next? | Good research asks better questions as it goes. | Query planning, follow-up searches, reasoning | Finds "termination", then searches "notice period" and "exit clause" | Planned |
| 3 | Why Did a Simple Question Take Two Minutes? | More searches mean more waiting and cost. | Latency and cost of multi-step retrieval | 30 searches for a one-line answer | Planned |
| 4 | When Does the Agent Know It Has Enough? | Research needs an end. | Stopping rules, confidence, budgets | Still reading contracts at midnight | Planned |
| 5 | When Is Plain RAG Good Enough? | Most questions need one search. | Choosing the simpler path, routing | "When does the Acme contract end?" needs one lookup | Planned |
| 6 | So, Should Your Agent Do Its Own Research? | Five write-ups, one checklist. | Finale: the agentic RAG checklist | The contract question, answered properly | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: its own iceberg plus an original meme scene and a sticky-note punchline.
