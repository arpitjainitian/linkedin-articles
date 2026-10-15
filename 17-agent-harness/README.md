# Series 17: "We bought the brain, we're done"

**Theme:** The model is the brain. Everything around it is yours to build.

**Level:** L5. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **An insurance claims-processing agent.** The model reads the claim. Approvals, limits, logs and fallbacks are all yours to build.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #BrainNotBody (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [You Bought a Brilliant Model. Where's the System?](01-curtain-raiser.md) | A model alone doesn't settle a single claim. | Curtain raiser: model vs harness | The model reads the claim perfectly; nothing happens next | Draft for review |
| 2 | Where Does the Agent Keep Its Place? | A claim can take three days. The agent can't hold its breath that long. | State, checkpoints, resuming after a crash | The server restarts mid-claim: start again, or carry on? | Planned |
| 3 | Where Does It Practise Before Touching Real Claims? | Never test the brakes on the motorway. | Sandboxes, staging vs production, backups kept outside the system | A test run approves real payouts | Planned |
| 4 | What Does the Model Actually See? | The model can only decide on what you show it. | Context engineering: what goes in, in what order, what's left out | The policy is cut off; the exclusion clause never reaches the model | Planned |
| 5 | What Happens When Five Small Gaps Line Up? | Incidents are chains, not single causes. | Defence in layers, incident reviews | Broad access, no confirmation, backups in the same place | Planned |
| 6 | So, Are You Building the Whole System? | Five write-ups, one checklist. | Finale: the harness checklist | The claims agent, production-ready | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a car on a lift, X-ray view. The engine (the model) vs brakes, steering, dashboard and seatbelts (the harness). Humor stays.
