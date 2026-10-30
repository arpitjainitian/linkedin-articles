# Series 8: "What's a few cents between friends?"

**Theme:** AI costs are paid per use, and use always grows, especially on sale days. The basics (tokens, caching, cheaper models, runaway bills) are covered in #JustAddRAG 10, so this series is about the money decisions: pricing, build vs rent, timing, value and forecasting.

**Level:** L2. Written so anyone can follow it, with no domain knowledge needed.

**Running example:** **A product-question assistant on a shopping site.** Millions of shoppers ask: "Does this phone support dual SIM?", "Will this fit a 6-foot bed?"

**One example, used in every write-up of this series.** No switching mid-series.

**Hashtag:** #FewCentsMore (proposal)

## Planned write-ups

| # | Title | The hook | What it covers | Example moment | Status |
|---|---|---|---|---|---|
| 1 | [A Few Cents per Question. Why Is the Sale-Day Bill So Big?](01-curtain-raiser-post.md) | Small numbers, multiplied by millions, stop being small. | Curtain raiser: how AI costs add up | Big sale day: 20x the questions | Draft for review |
| 2 | What Should You Charge for Your AI Feature? | If every answer costs you money, someone has to pay for it. | Pricing AI features, unit economics per customer | Free for every shopper, or only for members? | Planned |
| 3 | API or Your Own GPUs? | Renting is easy. Owning comes with its own bill. | Paying per call vs running open models yourself | Sale-day spikes on a rented API, or your own servers idle in March? | Planned |
| 4 | Does Every Answer Need to Come Right Now? | Waiting an hour can cost half as much. | Batch processing, off-peak jobs, real-time vs later | Rewriting 50,000 product descriptions overnight | Planned |
| 5 | Which AI Features Are Worth What They Cost? | Some features earn their bill. Some just spend it. | Cost per outcome, keep-or-kill decisions | Size advice cuts returns; "fun product facts" costs lakhs and sells nothing | Planned |
| 6 | How Do You Forecast Next Year's AI Bill? | Last year's bill is a poor guide. | Forecasting usage, growth and price changes; budgets | Twice the shoppers, half the price per token: bigger bill or smaller? | Planned |
| 7 | So, What Will Your AI Really Cost? | Six write-ups, one checklist. | Finale: estimate before you build | The shopping assistant's bill, predicted honestly | Planned |

## Format (same as #JustAddRAG)

- **Course companion:** every write-up also gets `NN-slug.course.md` (learning objective, deep dive, hands-on lab, quiz, checklist line, glossary, further reading, reader questions). See [COURSE.md](../COURSE.md). Never posted on LinkedIn.
- **Length:** the post takes at most 15 seconds to read (about 55 words, 2 bullets max); the article at most 2 minutes (about 400 words). Crisp, simple, engaging for anybody.
- Curiosity-question titles, numbered from 1, "write-up" naming, no fixed schedule.
- Start with why the topic matters; plain-language analogies with technical names revealed at the end; light "Fix:" pointers.
- Polite humor, ONE real running example used in every write-up, cheat sheet at the end, three kickoff takeaways.
- Post text in a copy-paste block, with the "you pay for it" impact of the wrong choice.
- Cover: a completely new design for this series (its own layout, palette and visual idea, not the #JustAddRAG iceberg template). Starting idea: a restaurant bill. The "few cents" starter vs the long receipt unrolling to the floor. Humor stays.
