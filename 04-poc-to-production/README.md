# Series 4: "It worked in the demo"

**Theme:** A proof of concept proves it can work. Production proves it works every day, on every invoice.

**Level:** L2. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **Invoice processing in accounts payable.** AI reads supplier invoices and matches them to purchase orders. The demo used 10 clean PDFs.

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #ItWorkedInTheDemo (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [The Invoice Demo Got a Standing Ovation. Now What?](01-curtain-raiser.md) | The applause is the easy part. | Curtain raiser: the POC-to-production cliff | 10 clean invoices read perfectly; invoice 11 is a phone photo | Draft for review |
| 2 | Why Does It Work on 10 Invoices and Fail on 10,000? | Demos are hand-picked. Suppliers aren't. | Real data, edge cases, messy formats | Multi-page invoices, handwritten notes, three currencies | Planned |
| 3 | Who Owns It at Month-End, and Every Month After? | A POC has fans. Production needs owners. | Ownership, on-call, runbooks, a maintenance budget | Month-end close stuck; a big supplier changes its invoice layout | Planned |
| 4 | What Happens When 50,000 Invoices Arrive at Once? | One invoice isn't a load test. | Scale, queues, rate limits, cost at volume | Quarter-end backlog, everything slows down | Planned |
| 5 | How Long Will It Really Take? | The demo took a week. Production won't. | Estimating every layer, experiments that may fail, booking experts' time, a phased plan | "It reads invoices already, so four more weeks?" | Planned |
| 6 | Is Audit Seeing It for the First Time a Week Before Launch? | Late reviews become late launches. | Bringing audit, security and compliance in early | "Who approved this payment, the AI?" | Planned |
| 7 | How Do You Roll It Out Without Betting the Quarter? | Start small, then widen. | Limited rollout, go/no-go gates, the launch pack | 5% of suppliers first, the rest after month-end | Planned |
| 8 | Can You Switch It Off Without Stopping Finance? | Every AI system needs an off switch and a plan B. | Kill switch, manual fallback, graceful degradation | The model provider is down on the last day of the quarter | Planned |
| 9 | So, Is Your POC Ready for Production? | Eight write-ups, one checklist. | Finale: the production-readiness checklist | The invoice system, launch checklist in hand | Planned |

## Format (same as #JustAddRAG)

- **Length:** the post takes at most 15 seconds to read (about 55 words, 2 bullets max); the article at most 2 minutes (about 400 words). Crisp, simple, engaging for anybody.
- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a motor show. The concept car on the turntable vs the road-test checklist it must pass. Humor stays.
