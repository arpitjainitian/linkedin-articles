# Series 19: "We bought the brain, we're done"

**Theme:** The model is the brain. Everything around it is yours to build.

**Level:** L5. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **An insurance claims-processing agent.** The model reads the claim. Approvals, limits, logs and fallbacks are all yours to build.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #BrainNotBody (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [You Bought a Brilliant Model. Where's the System?](01-curtain-raiser.md) | A model alone doesn't settle a single claim. | Curtain raiser: model vs harness | The model reads the claim perfectly; nothing happens next | Draft for review |
| 2 | Who Decides What Happens Next? | Plans and decisions need structure. | Planning, control flow, state | Read the claim, check the policy, request documents: in what order? | Planned |
| 3 | Where Are the Brakes? | Every system needs a way to stop. | Guardrails, limits, human checks | It approves a 20-lakh claim on its own | Planned |
| 4 | What Does the Dashboard Show? | You need to see what it's doing. | Observability, evals, cost tracking | Nobody knows why claims are suddenly slower | Planned |
| 5 | Who Maintains It After Launch? | Systems need servicing. | Updates, model swaps, ownership | A new model arrives; the old checks don't fit | Planned |
| 6 | So, Are You Building the Whole System? | Five write-ups, one checklist. | Finale: the harness checklist | The claims agent, production-ready | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a car on a lift, X-ray view. The engine (the model) vs brakes, steering, dashboard and seatbelts (the harness). Humor stays.
