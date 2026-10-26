# Series 23: "Explain It Like Hello World" (#ExplainItLikeHelloWorld)

**Theme:** trending AI ideas explained the "hello world" way: the smallest example that shows the whole idea working. No code. Plain words, one tiny example, then the real name.

**Who it's for:** anyone who hears AI words every day and nods along: students, managers, CXOs, engineers new to AI.

**How it differs from the other series:**
- Series 1 to 16 tell production stories (what goes wrong). This series explains the idea itself.
- Today in AI (20) explains news, which ages. This series explains concepts that stay useful.
- Topics already explained elsewhere are left out and linked instead: RAG (#JustAddRAG), MCP (Series 11), agents and agent loops (Series 2, 15), guardrails (Series 4), memory (Series 12), evals (Series 5), cost and caching (Series 8).

**Hashtag:** #ExplainItLikeHelloWorld

## Format of every write-up

1. **The buzzword:** what people say, and why it sounds scary.
2. **The hello world:** the smallest example that shows the whole idea working.
3. **Now add one thing:** one step up, to how it really works.
4. **Where you've already met it:** an everyday product.
5. **The real name:** the technical term, revealed at the end, plus 2 or 3 words to know.
6. **What it's not:** the most common misunderstanding.

**Rules:** no code; no jargon before the idea lands; one analogy; post at most 15 seconds, article at most 2 minutes; hook alone on its own line in the post; no emoji markers; ends with the "Previous series" block.

## Write-ups

### Part 1: How an AI reads and writes

| # | Topic | Hello-world angle | Status |
|---|---|---|---|
| 1 | Curtain raiser: [AI Words Everyone Uses. Nobody Explains.](01-curtain-raiser-post.md) (post with cover only, no article) | Hello world, but for AI ideas | Draft for review |
| 2 | [How Does an AI Read a Word?](02-tokens.md) (Tokens) | How an AI reads "unbelievable" as three pieces | Draft for review |
| 3 | [How Does an AI Write a Sentence?](03-how-llm-writes.md) (How an LLM writes) | Guessing the next word, again and again | Draft for review |
| 4 | [How Does an AI Know "King" Is Close to "Queen"?](04-embeddings.md) (Embeddings) | Words placed on a map by meaning | Draft for review |
| 5 | [How Does an AI Know What "It" Means?](05-attention.md) (Attention) | Every word glancing at every other word to work out "it" | Draft for review |
| 6 | [Why Does an AI Forget the Start of a Long Chat?](06-context-window.md) (Context window) | The AI's desk: what fits, and what falls off | Draft for review |
| 7 | [Why Does the Same Question Get Different Answers?](07-temperature.md) (Temperature) | Why the same question gets different answers | Draft for review |

### Part 2: How an AI is made

| # | Topic | Hello-world angle | Status |
|---|---|---|---|
| 8 | [What Does "70B" Actually Mean?](08-parameters.md) (Parameters) | 70 billion tiny dials, tuned by reading | Draft for review |
| 9 | [Is the AI Learning While You Chat With It?](09-training-vs-inference.md) (Training vs inference) | Years at school vs answering one exam question | Draft for review |
| 10 | [How Do You Teach an AI Something New?](10-fine-tuning-lora.md) (Pretraining, fine-tuning and LoRA) | School, then a specialist course, then a recipe card | Draft for review |
| 11 | [How Did the AI Learn to Be Polite?](11-rlhf.md) (RLHF) | Learning from thumbs up and thumbs down | Draft for review |
| 12 | [How Does a Small AI Learn From a Big One?](12-distillation.md) (Distillation) | A teacher model training a student model | Draft for review |
| 13 | [Can an AI Learn From Data Another AI Wrote?](13-synthetic-data.md) (Synthetic data) | An AI writing practice questions for another AI | Draft for review |
| 14 | [Why Did Bigger AI Keep Getting Better?](14-scaling-laws.md) (Scaling laws) | Why bigger got better, and why it's slowing | Draft for review |

### Part 3: Making it smaller, faster, cheaper

| # | Topic | Hello-world angle | Status |
|---|---|---|---|
| 15 | [How Do You Fit a Giant AI on a Laptop?](15-quantization.md) (Quantization) | The same photo saved as a smaller file | Draft for review |
| 16 | [Why Doesn't the Whole AI Wake Up for Every Question?](16-mixture-of-experts.md) (Mixture of experts) | A hospital with specialists, not one general doctor | Draft for review |
| 17 | [Why Doesn't the AI Re-Read Everything for Every Word?](17-kv-cache.md) (KV cache) | Not re-reading the whole book for every new word | Draft for review |
| 18 | [How Can a Small AI Make a Big AI Faster?](18-speculative-decoding.md) (Speculative decoding) | A fast intern drafts, the expert just checks | Draft for review |
| 19 | [Why Does AI Run on Gaming Chips?](19-gpus.md) (Why AI needs GPUs) | One professor vs a thousand students doing sums at once | Draft for review |
| 20 | [Can an AI Live on Your Phone?](20-on-device-ai.md) (Small and on-device models) | A pocket dictionary vs the library | Draft for review |

### Part 4: New kinds of AI

| # | Topic | Hello-world angle | Status |
|---|---|---|---|
| 21 | [Why Does the AI Think Before It Answers Now?](21-reasoning-models.md) (Reasoning models) | Thinking out loud before answering | Draft for review |
| 22 | [How Can One AI Read, See and Listen?](22-multimodal.md) (Multimodal AI) | One AI that reads, sees and listens | Draft for review |
| 23 | [How Does an AI Draw a Picture From Noise?](23-diffusion.md) (Diffusion) | A picture appearing out of noise | Draft for review |
| 24 | [How Does an AI Talk Back Without a Pause?](24-voice-ai.md) (Voice AI) | Hearing, thinking and speaking in one breath | Draft for review |
| 25 | [What Does "Open" Mean in Open AI Models?](25-open-weight.md) (Open-weight vs closed models) | A recipe you can cook at home vs a restaurant dish | Draft for review |
| 26 | [How Do AI Agents Talk to Each Other?](26-a2a.md) (A2A (agent-to-agent)) | Agents swapping business cards | Draft for review |
| 27 | [How Does an AI Use a Computer Like You?](27-computer-use.md) (Computer use) | An AI that clicks and types like you | Draft for review |
| 28 | [Can an AI Imagine What Happens Next?](28-world-models.md) (World models) | An AI that imagines what happens next | Draft for review |

### Part 5: Reading the headlines

| # | Topic | Hello-world angle | Status |
|---|---|---|---|
| 29 | [What Does "Scored 90% on a Benchmark" Mean?](29-benchmarks.md) (Benchmarks) | What "scored 90% on MMLU" actually means | Draft for review |
| 30 | [Why Does an AI Sound Sure When It's Wrong?](30-hallucination.md) (Hallucination) | Why a next-word guesser sometimes guesses confidently wrong | Draft for review |
| 31 | [Can You Tell If AI Wrote This?](31-watermarking.md) (AI watermarking) | An invisible signature in AI text and images | Draft for review |
| 32 | [Can You Build an App by Describing It?](32-vibe-coding.md) (Vibe coding) | Describing an app instead of writing it | Draft for review |
| 33 | [Your AI Dictionary, One Line per Word](33-finale-ai-dictionary.md) (The finale) | Every word from the series, one line each | Draft for review |

*Order can change with what's trending; Part 1 goes first because it unlocks the rest.*
