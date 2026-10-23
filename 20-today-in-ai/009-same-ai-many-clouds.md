# Today in AI, No. 009: Same AI, Many Clouds. Where Does Your Data Actually Go? | In-Country AI

![Cover](images/009-same-ai-many-clouds-cover.png)

*Today in AI: what's new in AI, and what it means for you. In plain words.*

**In one line:** The best AI models are no longer tied to one cloud, and in India some of them now run without your data leaving the country. But "available" and "available here, today, in its newest version" are not the same thing.

## What happened

Three moves in a few weeks:

- **5 October 2026:** Anthropic's Claude Opus 5, Sonnet 5 and Haiku 4.5 became available on Amazon Bedrock with **in-country inference** in India. Requests are processed in AWS's Mumbai and Hyderabad regions. [1]
- **August 2026:** OpenAI's GPT-5.6 Terra and Luna got the same in-India option on Amazon Bedrock. [2]
- **21 October 2026:** OpenAI announced its models are coming to Google Cloud, in private preview for now. Microsoft stays its main partner. [3]

## Who hosts what, as of 23 October 2026

| | AWS (Bedrock) | Microsoft (Foundry) | Google Cloud (Vertex AI) | Oracle (OCI) |
|---|---|---|---|---|
| **Claude** (Anthropic) | ✅ In India: in-country | ✅ | ✅ | Not found |
| **GPT** (OpenAI) | ✅ In India: in-country (Terra, Luna) | ✅ Main partner | 🟡 Private preview | ✅ US marketplace |
| **Gemini** (Google) | ❌ | ❌ | ✅ Home | ✅ Gemini 2.5 |
| **Grok** (xAI) | Not found | ✅ | Not found | ✅ |

*From public announcements and model catalogs [1-7]. Catalogs change often, so check before you build.*

## What it means

Think of a restaurant chain. The same brand opens branches in many cities. "In-country" means the kitchen is in your city: your order never leaves town.

For years, picking an AI model also meant picking a cloud. That's ending. You can now keep the cloud you already trust, with its contracts, security and bills, and still use the model you want.

## Why it matters to you

- **Learning AI?** Learn the ideas (prompts, tools, evals), not one cloud's buttons. The same models now appear everywhere.
- **Leading a team?** For banks, hospitals and government work, data residency was often the blocker. India's DPDP Act raised the stakes. In-country inference removes a big "no" from the risk review.

## The catch

New dishes reach some branches later. Anthropic's newest models, Opus 5.5 and Sonnet 5.5 (September 2026), aren't on the India in-country list yet [1, 5]. On Bedrock in India, OpenAI's in-country choice is Terra and Luna, not the flagship Sol [2]. And "available on cloud X" can mean different things: on Microsoft Foundry, Claude can run on Anthropic's own infrastructure or on Azure's, with different data rules [4].

So the real question isn't "is the model on my cloud?" It's "which version, in which region, with my data going where?"

## One thing to do this week

- **Learners:** call the same model through two different providers and compare the setup. You'll see what really changes.
- **Leaders:** ask your team for one table: each AI feature, which model and version, which region, and whether data leaves the country.

## Words to know

- **Inference:** the AI answering a request. Every question you ask is one inference.
- **In-country inference:** that answering happens on servers inside your country.
- **Data residency:** rules about where data must be stored and processed.

## References and credits

1. Business Standard, "Anthropic brings in-country Claude inference to India via Amazon Bedrock", October 2026. [Read it](https://www.business-standard.com/technology/artificial-intelligence/anthropic-claude-india-inference-amazon-bedrock-data-residency-126100500356_1.html). Also covered by [Analytics India Magazine](https://analyticsindiamag.com/ai-news/anthropic-brings-claude-in-country-inference-to-india-through-amazon-bedrock).
2. AWS, "Amazon Bedrock now supports OpenAI models in India", August 2026. [Read it](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-openai-india-v1/) (primary source). And AWS, "Introducing OpenAI models on Amazon Bedrock for in-country inferencing in India". [Read it](https://aws.amazon.com/blogs/machine-learning/introducing-openai-models-on-amazon-bedrock-for-in-country-inferencing-in-india/)
3. OpenAI, "OpenAI models are coming to Google Cloud", 21 October 2026. [Read it](https://openai.com/index/openai-models-google-cloud/) (primary source). Also covered by [CNBC](https://www.cnbc.com/2026/10/21/openai-bring-its-ai-models-to-googles-cloud-expands-beyond-microsoft.html) and [TechWire Asia](https://techwireasia.com/2026/10/openai-google-cloud-ai-models/), which also notes OpenAI's Oracle availability.
4. Microsoft Learn, "Claude models in Microsoft Foundry". [Read it](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models) (primary source). And Anthropic, "Claude in Microsoft Foundry is now generally available", June 2026. [Read it](https://claude.com/blog/claude-in-microsoft-foundry)
5. Anthropic, "Claude on Google Cloud", Claude Platform docs. [Read it](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai) (primary source)
6. AWS, "OpenAI GPT-5.6 Sol, Terra, and Luna now generally available on Amazon Bedrock", July 2026. [Read it](https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-sol-terra/) (primary source)
7. Oracle, "What's New in Oracle AI? October 2026 Edition". [Read it](https://blogs.oracle.com/ai-and-datascience/whats-new-in-oracle-ai-october-2026). And Microsoft, Foundry model catalog. [Read it](https://ai.azure.com/catalog/models)

Credit to Anthropic, OpenAI, AWS, Microsoft, Google Cloud and Oracle for their public announcements and documentation, and to the reporters at Business Standard, Analytics India Magazine, CNBC and TechWire Asia. Facts come from these sources, checked on 23 October 2026; the table is my summary of them, and the opinions are mine. Cover: original illustration, no third-party logos or images.

**Not sponsored.** This write-up is not sponsored by anyone. Nobody paid for it or reviewed it before publishing.

**Earlier issues of Today in AI:**

- [No. 001: What happens when your AI agent visits someone else's website?](https://www.linkedin.com/pulse/today-ai-001-what-happens-when-your-agent-visits-someone-arpit-jain-2vqmf/)
- [No. 002: What if your chatbot answered with buttons instead of paragraphs?](https://www.linkedin.com/pulse/today-ai-002-what-your-chatbot-answered-buttons-instead-arpit-jain-snkcf/)
- [No. 003: Why does Google's newest AI go to security teams first?](https://www.linkedin.com/pulse/today-ai-003-why-does-googles-newest-go-security-teams-arpit-jain-kpo3f)
- [No. 004: Why is Microsoft's new AI built to choose, not to chat?](https://www.linkedin.com/pulse/today-ai-004-why-microsofts-new-built-choose-chat-meet-arpit-jain-ypmkf/)
- [No. 005: If AI can build your dashboards, what's left for the data team?](https://www.linkedin.com/pulse/today-ai-005-can-build-your-dashboards-whats-left-data-arpit-jain-oukuf)
- [No. 006: Your AI made a decision. Can you prove why?](https://www.linkedin.com/pulse/today-ai-006-your-made-decision-can-you-prove-why-data-arpit-jain-vjenf)
- [No. 007: Should every question go to your most expensive AI?](https://www.linkedin.com/pulse/today-ai-007-should-every-question-go-your-most-expensive-arpit-jain-xjexf)
- [No. 008: Does using AI make you give up faster?](https://www.linkedin.com/pulse/today-ai-008-does-using-make-you-give-up-faster-learning-arpit-jain-ppghf/)

**Tags:** #AI #Cloud #DataResidency #AWS #TodayInAI

---

**People and pages to @mention** (type @ and pick from LinkedIn's list, in the article and the post): Anthropic, OpenAI, Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Oracle

**Post text (copy and paste):**

```
Same AI, many clouds. Where does your data actually go?

Claude now runs in-country in India on Amazon Bedrock. OpenAI's GPT models do too, and are coming to Google Cloud.

Like a restaurant chain opening a kitchen in your city: your order never leaves town.

The catch: the newest dishes reach some branches later.

Ask: which version, which region, data going where?

No. 009 of Today in AI. Sources in the article. Not sponsored.

#AI #Cloud #DataResidency #AWS #TodayInAI
```
