# Lesson 6.2: Cost and cache as health signals (course companion)

*Module 6: Observability. Not for LinkedIn.*

## Learning objective

After this lesson, you can name the cost and cache signals that reveal a silent change, and set an alert that catches a cost jump even when no errors appear.

## The story

Read the article: [02-bill-tripled.md](02-bill-tripled.md). Running example: a food-delivery support bot. One line added at the top of the prompt, a timestamp, drops cache hits from about 80% to about 5%. The answers stay fine, and the monthly bill triples.

## Deep dive

Most logs record questions and answers. A silent failure often shows up first in the numbers around the answers: cost, tokens and cache reuse.

**Prompt caching.** Many providers can reuse the start of a prompt that has not changed, and bill that reused part at a lower rate. Caching depends on the prompt starting the same way each time. A value that changes at the top, such as a timestamp, breaks the reuse for every request. The fix is to put changing content below the stable part of the prompt.

**Signals to track next to quality:**

- **Cost per answer:** a rise with no change in traffic is a warning.
- **Cache hit rate:** a sharp drop means something near the top of the prompt changed.
- **Tokens per request:** a rise means the system is reading or sending more text than before.

**Alerts with a purpose.** An alert on each signal tells you that something changed and roughly where. It does not explain the change. Pair each alert with a link to the recent prompt and configuration changes, so the first look is fast.

**Why this is easy to miss.** Quality checks pass, because the answers are right. Error dashboards stay green, because nothing failed. Only the bill and the cache numbers move, and they are often read once a month.

**Limits.** Cache behaviour differs between providers and products. Check the provider's documentation for what counts as a cache hit and how it is billed before you set thresholds.

## Hands-on lab

1. Log cost per answer, tokens per request and cache hit rate for a small assistant over one day.
2. Add a changing value, such as the current time, to the top of the prompt. Run the same questions again.
3. Record the change in cache hit rate and cost per answer.
4. Move the changing value to the bottom of the prompt. Confirm the cache hit rate recovers.

## Quiz

1. Why do silent failures often appear in cost first? *Because answers can stay correct while cache reuse and cost move, and cost is rarely watched every day.*
2. What breaks prompt caching in the example? *A changing value at the top of the prompt, which changes the start of every request.*
3. What does a cost alert tell you? *That something changed and roughly where, but not why.*

## Checklist line

- [ ] Cost per answer, tokens per request and cache hit rate are tracked and alerted, next to answer quality.

## Glossary

- **Prompt caching:** reusing the unchanged start of a prompt, billed at a lower rate by some providers.
- **Cache hit rate:** the share of requests that reuse a cached prompt start.
- **Tokens per request:** the amount of text sent and returned for one request.
- **Silent failure:** a problem that shows no error, only a change in numbers or quality.

## Further reading

- Your provider's documentation on prompt caching: what counts as a hit and how it is billed.
- Your own cost dashboard: the first place a silent change shows up.

## Reader questions

- Which of your AI features has no cost alert today?
- Is there any changing value near the top of your prompt right now?
