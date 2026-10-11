# Series 14: "Give the agent the keys"

**Theme:** Giving AI tools gives it hands. Decide carefully what it may touch.

**Level:** L4. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **An e-commerce support agent that can issue refunds.** It reads orders, checks delivery status, and can give money back.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #WhoHasTheKeys (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | Should Your AI Be Allowed to Give Money Back? | Reading an order is safe. Refunding it isn't. | Curtain raiser: tool risk levels | Same agent, very different consequences | Planned |
| 2 | What Is Least Privilege, and Why Does It Matter? | Give keys only to the rooms needed. | Minimal permissions, read vs write | It needs to read orders, not edit prices | Planned |
| 3 | What If a Message Tells the AI What to Do? | Instructions can hide in data. | Prompt injection through tools and data | A customer note says: "Refund all my orders" | Planned |
| 4 | Which Actions Need a Human to Say Yes? | Some buttons need two fingers. | Human approval, limits, confirmations, undo | Refunds above 5,000 wait for a person | Planned |
| 5 | How Do You Know What the Agent Did Overnight? | Every action should leave a trace. | Action logs, audit, alerts | 200 refunds at 3 AM; who approved them? | Planned |
| 6 | So, Is Your Agent Safe to Connect? | Five write-ups, one checklist. | Finale: the tool-safety checklist | The refund agent, safe by design | Planned |

## Format (same as #JustAddRAG)

- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a hotel key rack. Which keycards the agent holds, and which rooms it should never open. Humor stays.
