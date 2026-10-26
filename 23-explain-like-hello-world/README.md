# Series 23: "Explain It Like Hello World" (#ExplainItLikeHelloWorld)

**Theme:** trending AI ideas explained the "hello world" way: the smallest example that shows the whole idea working. No code. Plain words, one tiny example, then the real name.

**Who it's for:** anyone who hears AI words every day and nods along: students, managers, CXOs, engineers new to AI.

**How it differs from the other series:**
- Series 1 to 16 tell production stories (what goes wrong). This series explains the idea itself.
- Today in AI (20) explains news, which ages. This series explains concepts that stay useful.
- Words that other series cover in depth (RAG, MCP, agents, guardrails, memory, evals, gateways, cost) are explained here only at hello-world level, and each links to the series that covers what goes wrong in production.

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

One word per write-up. Season 1 covers the AI words in use so far; later seasons add new words as they appear.

| # | Write-up | Hello-world angle | Status |
|---|---|---|---|
| 1 | Curtain raiser: [AI Words Everyone Uses. Nobody Explains.](01-curtain-raiser-post.md) (post with cover only, no article) | Hello world, but for AI ideas | Draft for review |
| | **Part 0: The basics** | | |
| 2 | [What Actually Counts as AI?](002-artificial-intelligence.md) (Artificial intelligence) | AI is a computer doing something we'd say needs human intelligence. | Draft for review |
| 3 | [How Does a Computer Learn Without Being Told the Rules?](003-machine-learning.md) (Machine learning) | Machine learning learns the patterns from examples instead. | Draft for review |
| 4 | [What's "Deep" About Deep Learning?](004-deep-learning.md) (Deep learning) | Deep learning learns in layers, just like that. | Draft for review |
| 5 | [Is a Neural Network Really Like a Brain?](005-neural-network.md) (Neural network) | A neural network is billions of tiny voters adding up numbers. | Draft for review |
| 6 | [What Makes AI "Generative"?](006-generative-ai.md) (Generative AI) | Generative AI makes new things instead of just labelling old ones. | Draft for review |
| 7 | [Why Are They Called Foundation Models?](007-foundation-model.md) (Foundation model) | A foundation model is one big base that many AI products are built on. | Draft for review |
| 8 | [What Would It Mean for AI to Be "General"?](008-agi.md) (AGI) | AGI means one AI that can learn most tasks a person can. | Draft for review |
| 9 | [What Is Superintelligence, and Should We Worry?](009-superintelligence.md) (Superintelligence) | Superintelligence means AI smarter than the best humans in almost every field. | Draft for review |
| | **Part 1: How an AI reads and writes** | | |
| 10 | [How Does an AI Read a Word?](010-tokens.md) (Tokens) | An AI doesn't read words. It reads pieces, called tokens. | Draft for review |
| 11 | [How Does an AI Write a Sentence?](011-llm.md) (LLM) | An AI writes by guessing the next word, again and again. | Draft for review |
| 12 | [How Does an AI Know "King" Is Close to "Queen"?](012-embeddings.md) (Embeddings) | An embedding is a word's address on a map of meaning. | Draft for review |
| 13 | [How Does an AI Know What "It" Means?](013-attention.md) (Attention) | You glanced back at the other words. So does an AI. That's attention. | Draft for review |
| 14 | [What Is the "T" in GPT?](014-transformer.md) (Transformer) | A transformer lays the whole sentence out and reads it all at once. | Draft for review |
| 15 | [Why Does an AI Forget the Start of a Long Chat?](015-context-window.md) (Context window) | An AI's context window is its desk. When it's full, something falls off. | Draft for review |
| 16 | [Why Does the Same Question Get Different Answers?](016-temperature.md) (Temperature) | Temperature is how adventurous the AI's next word is. | Draft for review |
| | **Part 2: Talking to an AI** | | |
| 17 | [Why Does the Way You Ask Change the Answer?](017-prompt.md) (Prompt) | A prompt is your brief to the AI. Vague brief, vague answer. | Draft for review |
| 18 | [Is Prompt Engineering a Real Skill?](018-prompt-engineering.md) (Prompt engineering) | Prompt engineering is the second person. | Draft for review |
| 19 | [What's the Hidden Instruction Behind Every Chatbot?](019-system-prompt.md) (System prompt) | A system prompt is that briefing, given to the AI before you type. | Draft for review |
| 20 | [Can an AI Do a Task It Was Never Shown?](020-zero-shot.md) (Zero-shot) | The AI answers "negative" anyway. That's zero-shot. | Draft for review |
| 21 | [Why Do Examples Help an AI So Much?](021-few-shot.md) (Few-shot) | The AI answers GRN-TRS. That's few-shot: show a few examples, it copies the pattern. | Draft for review |
| 22 | [Why Does "Think Step by Step" Work?](022-chain-of-thought.md) (Chain of thought) | Writing the steps first helps an AI too. That's chain of thought. | Draft for review |
| 23 | [Is Context Engineering the New Prompt Engineering?](023-context-engineering.md) (Context engineering) | Context engineering is choosing what goes on the AI's desk. | Draft for review |
| 24 | [How Do You Get an AI to Fill In a Form?](024-structured-output.md) (Structured output) | Structured output makes the AI fill in boxes instead of writing paragraphs. | Draft for review |
| 25 | [Why Does the AI Type Its Answer Word by Word?](025-streaming.md) (Streaming) | Streaming serves each word of the answer as soon as it's ready. | Draft for review |
| | **Part 3: How an AI is made** | | |
| 26 | [What Does "70B" Actually Mean?](026-parameters.md) (Parameters) | 70B means 70 billion tiny knobs, each tuned during training. | Draft for review |
| 27 | [How Does an AI Go to School?](027-training.md) (Training) | Training is an AI doing that billions of times. | Draft for review |
| 28 | [What Happens When You Hit Send?](028-inference.md) (Inference) | That's inference: a frozen model answering. It isn't learning mid-exam. | Draft for review |
| 29 | [How Does an AI Learn Language in the First Place?](029-pretraining.md) (Pretraining) | Pretraining is the AI's general schooling, before any specialist course. | Draft for review |
| 30 | [How Do You Teach an AI Your Way of Doing Things?](030-fine-tuning.md) (Fine-tuning) | Fine-tuning teaches a general AI your menu. | Draft for review |
| 31 | [How Do You Customise an AI Without Retraining It?](031-lora.md) (LoRA) | LoRA is that recipe card: a small, swappable add-on to an AI. | Draft for review |
| 32 | [How Did the AI Learn to Be Polite?](032-rlhf.md) (RLHF) | Thumbs up, thumbs down, thousands of times. That's how AIs learned to answer. | Draft for review |
| 33 | [Can an AI Follow a Written Set of Principles?](033-constitutional-ai.md) (Constitutional AI) | Constitutional AI teaches a model to check its own answers against written principles. | Draft for review |
| 34 | [How Does a Small AI Learn From a Big One?](034-distillation.md) (Distillation) | What if the big one taught the small one? That's distillation. | Draft for review |
| 35 | [Can an AI Learn From Data Another AI Wrote?](035-synthetic-data.md) (Synthetic data) | So an AI writes them, and another AI learns from them. That's synthetic data. | Draft for review |
| 36 | [Who Teaches the AI What's Right?](036-data-labelling.md) (Data labelling) | Data labelling: people marking the right answers so AI can learn. | Draft for review |
| 37 | [Why Can an AI Ace the Practice Test and Fail the Real One?](037-overfitting.md) (Overfitting) | That's overfitting: memorising examples instead of learning the pattern. | Draft for review |
| 38 | [Why Did Bigger AI Keep Getting Better?](038-scaling-laws.md) (Scaling laws) | AI improved the same way. Researchers call it scaling laws. | Draft for review |
| 39 | [Can Bigger AI Suddenly Learn New Tricks?](039-emergent-abilities.md) (Emergent abilities) | Emergent abilities: skills that seem to appear once an AI is big enough. | Draft for review |
| 40 | [What Happens When AI Learns From AI?](040-model-collapse.md) (Model collapse) | Model collapse is AI learning from AI, and fading the same way. | Draft for review |
| | **Part 4: Smaller, faster, cheaper** | | |
| 41 | [How Do You Fit a Giant AI on a Laptop?](041-quantization.md) (Quantization) | Quantization is saving the same photo as a smaller file. | Draft for review |
| 42 | [Why Doesn't the Whole AI Wake Up for Every Question?](042-mixture-of-experts.md) (Mixture of experts) | A mixture of experts sends each word to only a few specialists. | Draft for review |
| 43 | [Why Doesn't the AI Re-Read Everything for Every Word?](043-kv-cache.md) (KV cache) | Neither does an AI. It keeps notes, called the KV cache. | Draft for review |
| 44 | [Why Do Repeated Prompts Get Cheaper?](044-prompt-caching.md) (Prompt caching) | Prompt caching reads it once and reuses the notes. | Draft for review |
| 45 | [How Can a Small AI Make a Big AI Faster?](045-speculative-decoding.md) (Speculative decoding) | That's speculative decoding: guess ahead, check in one go. | Draft for review |
| 46 | [Why Does AI Run on Gaming Chips?](046-gpu.md) (GPU) | AI picks the students. That's why it runs on GPUs. | Draft for review |
| 47 | [What Is a TPU, and Why Did Google Build One?](047-tpu.md) (TPU) | A TPU is Google's bread knife for AI maths. | Draft for review |
| 48 | [What's the AI Chip Inside Your New Laptop?](048-npu.md) (NPU) | That's the NPU: low-power AI, right on your device. | Draft for review |
| 49 | [Can a Small AI Be Good Enough?](049-small-language-model.md) (Small language model) | A small language model is the pocket dictionary. | Draft for review |
| 50 | [Can an AI Live on Your Phone?](050-on-device-ai.md) (On-device AI) | That's on-device AI: answers without the call. | Draft for review |
| 51 | [Why Does the AI Take So Long to Answer?](051-latency.md) (Latency) | That wait is latency: every step between asking and answering. | Draft for review |
| 52 | [Why Does the First Word Matter Most?](052-time-to-first-token.md) (Time to first token) | Time to first token is the AI's bread basket. | Draft for review |
| | **Part 5: Giving AI knowledge** | | |
| 53 | [How Does an AI Answer From Your Documents?](053-rag.md) (RAG) | RAG is an AI doing an open-book exam on your documents. | Draft for review |
| 54 | [Where Does an AI Store Meaning?](054-vector-database.md) (Vector database) | A vector database is a filing cabinet sorted by meaning. | Draft for review |
| 55 | [How Does Search Understand What You Meant?](055-semantic-search.md) (Semantic search) | Semantic search finds results by meaning, not just matching words. | Draft for review |
| 56 | [How Do You Teach an AI Who Is Connected to Whom?](056-knowledge-graph.md) (Knowledge graph) | A knowledge graph stores facts as things and the links between them. | Draft for review |
| 57 | [How Does an AI Answer Questions About a Whole Pile of Documents?](057-graphrag.md) (GraphRAG) | GraphRAG maps everything first, then answers from the map. | Draft for review |
| 58 | [How Do You Keep an AI Tied to the Facts?](058-grounding.md) (Grounding) | Grounding makes the AI the second student. | Draft for review |
| 59 | [How Do You Check Where an AI Got Its Answer?](059-citations.md) (Citations) | Citations give every AI answer a receipt. | Draft for review |
| 60 | [Can an AI Do Your Research for You?](060-deep-research.md) (Deep research) | Deep research is an AI doing that whole loop on its own. | Draft for review |
| | **Part 6: AI that acts** | | |
| 61 | [What Makes an AI an "Agent"?](061-ai-agent.md) (AI agent) | A chatbot is the librarian. An AI agent is the assistant who gets it done. | Draft for review |
| 62 | [What Does "Agentic" Really Mean?](062-agentic-ai.md) (Agentic AI) | Agentic is how far along that scale an AI system sits. | Draft for review |
| 63 | [How Does an AI Check the Weather?](063-tool-calling.md) (Tool calling) | So it asks your app to run a weather tool. That's tool calling. | Draft for review |
| 64 | [Why Is Everyone Talking About MCP?](064-mcp.md) (MCP) | MCP is that one plug, between AI apps and tools. | Draft for review |
| 65 | [How Do AI Agents Talk to Each Other?](065-a2a.md) (A2A) | A2A is how AI agents swap business cards and hand over tasks. | Draft for review |
| 66 | [Are Several AI Agents Better Than One?](066-multi-agent-system.md) (Multi-agent system) | A multi-agent system is that team, made of AI agents. | Draft for review |
| 67 | [How Does an AI Remember You?](067-ai-memory.md) (AI memory) | AI memory is that guest file, read back at the start of each chat. | Draft for review |
| 68 | [How Does an AI Use a Computer Like You?](068-computer-use.md) (Computer use) | Look, decide, click, look again. That's computer use. | Draft for review |
| 69 | [What's the Difference Between a Copilot and an Agent?](069-copilot.md) (Copilot) | An AI copilot suggests. You decide. An agent acts. | Draft for review |
| 70 | [Where Should an AI Agent Do Its Work?](070-agent-sandbox.md) (Agent sandbox) | An agent sandbox is that tray, for AI agents running code. | Draft for review |
| | **Part 7: New kinds of AI** | | |
| 71 | [Why Does the AI Think Before It Answers Now?](071-reasoning-model.md) (Reasoning model) | Most people blurt ₹10. Thinking step by step gets ₹5. Reasoning models do the same. | Draft for review |
| 72 | [How Can One AI Read, See and Listen?](072-multimodal-ai.md) (Multimodal AI) | One AI that reads, sees and listens. That's multimodal. | Draft for review |
| 73 | [How Does an AI Draw a Picture From Noise?](073-diffusion-model.md) (Diffusion model) | Now run it backwards. That's how AI draws: diffusion. | Draft for review |
| 74 | [How Does an AI Talk Back Without a Pause?](074-voice-ai.md) (Voice AI) | New voice AI hears, thinks and speaks in one breath. | Draft for review |
| 75 | [How Does an AI Make a Video From a Sentence?](075-text-to-video.md) (Text-to-video) | Text-to-video AI draws that flipbook from a single sentence. | Draft for review |
| 76 | [How Can a Video of Someone Be Fake?](076-deepfake.md) (Deepfake) | It might not be your CFO. That's a deepfake. | Draft for review |
| 77 | [Can an AI Copy Your Voice From a Few Seconds of Audio?](077-voice-cloning.md) (Voice cloning) | A few seconds of audio can be enough to clone a voice. | Draft for review |
| 78 | [Who Is That Presenter, If Nobody Filmed Them?](078-ai-avatar.md) (AI avatar) | That's an AI avatar: a presenter who was never filmed for this video. | Draft for review |
| 79 | [What's a Digital Twin, and Why Do Factories Want One?](079-digital-twin.md) (Digital twin) | A digital twin is a live copy you can safely experiment on. | Draft for review |
| 80 | [What Does "Open" Mean in Open AI Models?](080-open-weight-model.md) (Open-weight model) | That's the difference between closed and open-weight AI models. | Draft for review |
| 81 | [Can an AI Imagine What Happens Next?](081-world-model.md) (World model) | A world model is an AI that imagines what happens next. | Draft for review |
| 82 | [When Does AI Get a Body?](082-embodied-ai.md) (Embodied AI) | Embodied AI is AI with a body, learning the hard part. | Draft for review |
| | **Part 8: Trust, safety and rules** | | |
| 83 | [Why Does an AI Sound Sure When It's Wrong?](083-hallucination.md) (Hallucination) | An AI guesses likely words. Likely isn't always true. That's a hallucination. | Draft for review |
| 84 | [How Do You Stop an AI Saying the Wrong Thing?](084-guardrails.md) (Guardrails) | AI guardrails are checks on what goes in and what comes out. | Draft for review |
| 85 | [How Do People Trick an AI Into Breaking Its Rules?](085-jailbreak.md) (Jailbreak) | A jailbreak is clever wording that talks an AI out of its rules. | Draft for review |
| 86 | [Can a Web Page Give Orders to Your AI?](086-prompt-injection.md) (Prompt injection) | That's prompt injection: orders hidden in what the AI reads. | Draft for review |
| 87 | [Who Attacks an AI on Purpose?](087-red-teaming.md) (Red teaming) | Red teaming is attacking your own AI before anyone else does. | Draft for review |
| 88 | [How Do You Know an AI Is Getting Better?](088-evals.md) (Evals) | Evals are that list, for AI. | Draft for review |
| 89 | [Can One AI Mark Another AI's Homework?](089-llm-as-a-judge.md) (LLM-as-a-judge) | LLM-as-a-judge: one AI marking another, with a guide. | Draft for review |
| 90 | [How Does an AI End Up Unfair?](090-ai-bias.md) (Bias) | So the AI picks men too. That's AI bias. | Draft for review |
| 91 | [Can an AI Tell You Why It Decided?](091-explainability.md) (Explainability) | Explainability is being able to say why, in plain words. | Draft for review |
| 92 | [How Do You Make Sure an AI Wants What We Want?](092-alignment.md) (Alignment) | Alignment is making AI do what we mean, not just what we say. | Draft for review |
| 93 | [Can You Tell If AI Wrote This?](093-watermarking.md) (Watermarking) | AI watermarks work the same way: invisible, until you check. | Draft for review |
| 94 | [Who Makes the Rules for AI?](094-ai-regulation.md) (AI regulation) | AI regulation works the same way: rules by level of risk. | Draft for review |
| 95 | [Is Your Team Using AI You Don't Know About?](095-shadow-ai.md) (Shadow AI) | That's shadow AI: AI use nobody approved or knows about. | Draft for review |
| 96 | [Why Do Countries Want Their Own AI?](096-sovereign-ai.md) (Sovereign AI) | Sovereign AI is the same idea, for AI models, data and computing. | Draft for review |
| | **Part 9: Reading the headlines** | | |
| 97 | [What Does "Scored 90% on a Benchmark" Mean?](097-benchmarks.md) (Benchmarks) | A benchmark is a school exam for AI. Your work is a different exam. | Draft for review |
| 98 | [Can You Build an App by Describing It?](098-vibe-coding.md) (Vibe coding) | Describe it, test it, ask for changes. That's vibe coding. | Draft for review |
| 99 | [Why Is the Internet Filling Up With "AI Slop"?](099-ai-slop.md) (AI slop) | That's AI slop: content made cheaply, for clicks, not for you. | Draft for review |
| 100 | [How Do You Get Found When People Ask AI Instead of Google?](100-geo.md) (GEO) | GEO is making sure that answer can find and quote you. | Draft for review |
| 101 | [What Makes a Company "AI-Native"?](101-ai-native.md) (AI-native) | AI-native means built around AI from the start, not AI added later. | Draft for review |
| 102 | [Who Keeps an AI Running After Launch?](102-llmops.md) (LLMOps) | LLMOps is running the AI restaurant every day. | Draft for review |
| 103 | [Why Do Companies Put a Front Door in Front of AI?](103-ai-gateway.md) (AI gateway) | An AI gateway is that reception desk, for every AI request. | Draft for review |
| 104 | [Should Every Question Go to the Most Expensive AI?](104-model-routing.md) (Model routing) | Model routing sends each AI question to the right-sized model. | Draft for review |
| 105 | [Your AI Dictionary, One Line per Word](105-finale-ai-dictionary.md) (The finale) | Every word from the series, one line each | Draft for review |

*Order can change with what's trending; Part 0 and Part 1 go first because they unlock the rest.*
