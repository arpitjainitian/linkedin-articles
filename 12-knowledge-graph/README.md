# Series 12: "Just connect the dots"

**Theme:** Some questions are about connections, not documents.

**Level:** L4. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **Supplier risk at a manufacturer.** "A flood just hit one region. Which of our products depend on a supplier there?"

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #JustConnectTheDots (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | A Flood Hit One Region. Which of Your Products Are at Risk? | Some questions need connections, not paragraphs. | Curtain raiser: why graphs | Search finds the supplier, not the products that depend on it | Planned |
| 2 | What Is a Knowledge Graph, Really? | Dots and lines, with meaning. | Entities, relationships, how GraphRAG answers | Suppliers, parts and products as dots; "supplies" and "used in" as lines | Planned |
| 3 | Who Builds the Graph, and How? | Graphs don't draw themselves. | Extracting entities and relationships, cleaning duplicates | "ABC Pvt Ltd", "ABC Private Limited", "ABC Ltd": same supplier? | Planned |
| 4 | What Happens When Suppliers Change? | New supplier, new part, new risk. | Keeping the graph current, versioning | A part moves to a new supplier; the graph still points to the old one | Planned |
| 5 | When Is a Graph Worth the Effort? | Not every problem needs one. | GraphRAG vs plain RAG, cost and complexity | "What's this supplier's address?" doesn't need a graph | Planned |
| 6 | So, Should You Add a Knowledge Graph? | Five write-ups, one checklist. | Finale: the GraphRAG checklist | Supplier risk, mapped or not | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a metro map. Suppliers, parts and products as stations, with lines connecting them. Humor stays.
