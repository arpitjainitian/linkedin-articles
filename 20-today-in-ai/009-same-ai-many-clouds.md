# Today in AI, No. 009: Same AI, Many Clouds. Where Does Your Data Actually Go? | In-Country AI

![Cover](images/009-same-ai-many-clouds-cover.png)

*Today in AI: what's new in AI, and what it means for you. In plain words.*

**In one line:** Top AI models now run on many clouds, and in India some run without your data leaving the country. But not always the newest version.

## What happened

- **29 September:** Anthropic's Claude (Opus 5, Sonnet 5, Haiku 4.5) went live on Amazon Bedrock with **in-country inference** in India, in Mumbai and Hyderabad. Anthropic announced it on 5 October. [1]
- **18 August:** OpenAI's GPT-5.6 Terra and Luna got the same in-India option. [2]
- **21 October:** OpenAI said its models are coming to Google Cloud, in private preview. [3]

## Who hosts what (23 October 2026)

**Global:**

- **AWS:** Claude ✅ Opus 5.5, Opus 5, Sonnet 5, Haiku 4.5 [1, 12]. GPT ✅ GPT-5.6 Sol, Terra, Luna [6]. Gemini ➖.
- **Microsoft:** GPT ✅ GPT-5.6 Sol, Terra, Luna [7]. Claude ✅ Opus 5.5, Sonnet 5.5, Haiku 5.5 [4]. Gemini ➖.
- **Google Cloud:** Gemini ✅ Gemini 4 Argon, Gemini 3.8 Flash [14]. Claude ✅ Opus 5.5, Sonnet 5.5, Haiku 5.5 [5]. GPT 🟡 GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, private preview [3].
- **Oracle:** Gemini ✅ Gemini 2.5 Pro, Flash, Flash-Lite [9]. GPT 🟡 GPT-5.5, announced [8]. Claude ➖.

**In India, with data staying in India:**

- **AWS:** Claude ✅ Opus 5, Sonnet 5, Haiku 4.5 [1]. GPT ✅ GPT-5.6 Terra, Luna [2]. Gemini ➖.
- **Microsoft:** GPT 🟡 GPT-5.4 mini and GPT-5.1, only on a dedicated plan where you pre-book capacity (pay-per-use: GPT-4o, GPT-4.1 mini) [10]. Claude ➖, offered only globally or in the US [4]. Gemini ➖.
- **Google Cloud:** Gemini ✅ Gemini 3.5 Flash, processed in Mumbai [15]. Claude ➖, no Indian region listed [16]. GPT ➖.
- **Oracle:** Gemini 🟡 Gemini 2.5 offered in Hyderabad, but Oracle doesn't say where it's processed [17]. Claude ➖. GPT ➖.

*Newest models listed, not every model. GPT means OpenAI's GPT models (open-weight gpt-oss not counted). ➖ = no public listing found. Catalogs change often.*

## What it means

Think of a restaurant chain. In-country means the kitchen is in your city: your order never leaves town.

Picking a model no longer means picking a cloud. For banks, hospitals and government work under India's DPDP Act, that removes a big "no" from the risk review.

## The catch

New dishes reach some branches later. Claude Opus 5.5 is on AWS, Microsoft and Google, but not yet in-country in India [1, 4, 5, 12]. In India, OpenAI's newest options are Terra and Luna on AWS, not the flagship Sol [2, 10].

## One thing to do this week

- **Learners:** call one model through two clouds. See what changes.
- **Leaders:** ask for one table: each AI feature, its model version, its region, and whether data leaves the country.

## Words to know

- **Inference:** the AI answering a request.
- **Data residency:** rules about where data is stored and processed.

## References and credits

1. AWS, "Amazon Bedrock expands Claude model availability to in-country inferencing in India", 29 September 2026. [Read it](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-expands-claude-model-availability-to-india-cross-region-inference/) (primary source). Also covered by [Analytics India Magazine](https://analyticsindiamag.com/ai-news/anthropic-brings-claude-in-country-inference-to-india-through-amazon-bedrock) and [Business Standard](https://www.business-standard.com/technology/artificial-intelligence/anthropic-claude-india-inference-amazon-bedrock-data-residency-126100500356_1.html), 5 October 2026.
2. AWS, "Amazon Bedrock now supports OpenAI models in India", 18 August 2026. [Read it](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-openai-india-v1/) (primary source)
3. OpenAI, "OpenAI models are coming to Google Cloud", 21 October 2026. [Read it](https://openai.com/index/openai-models-google-cloud/) (primary source). Also covered by [CNBC](https://www.cnbc.com/2026/10/21/openai-bring-its-ai-models-to-googles-cloud-expands-beyond-microsoft.html) and [TechWire Asia](https://techwireasia.com/2026/10/openai-google-cloud-ai-models/).
4. Microsoft Learn, "Claude models in Microsoft Foundry", updated 22 September 2026. [Read it](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models) (primary source). And Anthropic, "Claude in Microsoft Foundry is now generally available", 29 June 2026. [Read it](https://claude.com/blog/claude-in-microsoft-foundry)
5. Anthropic, "Claude Models on Google Cloud", Claude Platform docs (model ID table). [Read it](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai) (primary source)
6. AWS, "OpenAI GPT-5.6 Sol, Terra, and Luna now generally available on Amazon Bedrock", 13 July 2026. [Read it](https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-sol-terra/) (primary source)
7. Microsoft, "GPT-5.6 now available in Microsoft Foundry", 9 July 2026. [Read it](https://azure.microsoft.com/en-us/blog/gpt-5-6-now-available-in-microsoft-foundry/) (primary source)
8. IT Brief, "OpenAI and Oracle to offer models on OCI Marketplace", June 2026. [Read it](https://itbrief.news/story/openai-oracle-to-offer-models-on-oci-marketplace)
9. Oracle, "Use Google Gemini 2.5 in OCI Generative AI", release note, 1 October 2025. [Read it](https://docs.oracle.com/iaas/releasenotes/generative-ai/gemini-2-5-GA.htm) (primary source)
10. Microsoft Learn, "Region availability for Foundry Models sold by Azure" (Standard/Regional and Regional Provisioned tables, South India), updated 19 October 2026. [Read it](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability) (primary source)
11. IBEF, "Google expands AI infrastructure in India with local hosting of Gemini models", 9 July 2026. [Read it](https://www.ibef.org/news/google-expands-ai-infrastructure-in-india-with-local-hosting-of-gemini-models)
12. AWS, "Claude Opus 5.5 is now available on AWS". [Read it](https://aws.amazon.com/blogs/machine-learning/claude-opus-5-5-is-now-available-on-aws/) (primary source)
13. Google Cloud, "Supporting Viksit Bharat: announcing AI investments in India", 11 November 2025 (Gemini 2.5 Flash with processing in India). [Read it](https://cloud.google.com/blog/products/gcp/supporting-viksit-bharat-announcing-ai-investments-in-india) (primary source)
14. Google Cloud, "Gemini Enterprise Agent Platform release notes" (Gemini 4 Argon GA 13 October 2026; Gemini 3.8 Flash GA 2 September 2026). [Read it](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes) (primary source)
15. Google Cloud, "Gemini 3.5 Flash" model page (ML processing regions include asia-south1, Mumbai). [Read it](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash) (primary source)
16. Google Cloud, Claude model pages on Agent Platform (Sonnet 4.6: us-east5, europe-west1, asia-southeast1, global; Haiku 4.5: us-east5, europe-west1, global). [Read it](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/sonnet-4-6) (primary source)
17. Oracle, "New Regions for Google Gemini 2.5 in OCI Generative AI", 21 January 2026 (adds India South, Hyderabad). [Read it](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/gemini-2-5-regions.htm) (primary source)

Credit to Anthropic, OpenAI, AWS, Microsoft, Google Cloud and Oracle for their public announcements and documentation, and to the reporters at Analytics India Magazine, Business Standard, CNBC, TechWire Asia and IT Brief and IBEF. Facts come from these sources, checked on 23 October 2026; the cloud list is my summary of them, and the opinions are mine. Cover: original illustration, no third-party logos or images.

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
