# One-line summary of every article

A single list of every write-up in the repo, one line each. Status is taken from each file's `Published:` line: **Published** means it is live on LinkedIn; **Draft** means it is written but not posted. The series READMEs hold the full tables and links.

Retired files are at the end. The `qna/` folder has no Markdown files.

## Series 1: #JustAddRAG

| No. | Title | Status | One-line summary |
|---|---|---|---|
| 1 | Why does "Just add RAG" sound like 2 weeks but take 6 months? | Published (LinkedIn only, no file in repo) | Why an AI document-search demo is quick and production is slow. |
| 2 | Why can't your AI read a PDF that a 10-year-old can? | Published (LinkedIn only, no file in repo) | Document ingestion and OCR: the AI can only use what it can read. |
| 3 | What if the answer was in your docs, but you cut it in half? | Published | Chunking: how splitting documents can cut the answer apart. |
| 4 | Is your AI hallucinating, or just looking in the wrong place? | Published | Retrieval: most wrong answers come from finding the wrong text. |
| 5 | What does your AI say when it doesn't know? | Published | Grounding: making the AI admit when the sources don't cover the question. |
| 6 | Do you need an LLM, a database, or both? | Published | Choosing the right tool: many questions need a database lookup, not a model. |
| 7 | What happens when your AI finds two versions of the truth? | Published | Versions: old and new documents compete, and the AI may pick the old one. |
| 8 | Can the intern ask your AI about the CEO's salary? | Published | Permissions: the AI must respect who is allowed to see which document. |
| 9 | How many questions did you test before saying "it works"? | Published | Evals: a ground-truth test set is what proves the system works. |
| 10 | A few cents per question: so why is finance calling? | Published | Cost: small per-question prices add up across many users. |
| 11 | It's fast in the demo, so why are users clicking twice? | Published | Performance and availability: the demo is not the real load. |
| 12 | Where did your user's passport just travel to? | Published | Privacy: tracing where data goes and what the vendor keeps. |
| 13 | When your AI gives a wrong answer, can you tell why? | Published | Observability: logs that show which document and step produced an answer. |
| 14 | Nobody touched the code. Why did the answers change? | Published | Model changes: vendor updates can change answers without warning. |
| 15 | So, should you really "just add RAG"? | Published | Finale: a checklist for when RAG is the right answer and what to build around it. |

## Series 2: Beyond Just RAG: From Answers to Actions

| No. | Title | Status | One-line summary |
|---|---|---|---|
| 1 | Your AI can answer. Now it has to act. | Published | Curtain raiser: moving from an AI that answers to one that does tasks. |
| 2 | The receipt says ₹1,180. Or was it ₹118? | Published | Exact data: reading amounts from messy receipts without guessing. |
| 3 | It filed the same claim twice | Published | Safe retries: a timeout must not create a duplicate action. |
| 4 | The claim was filed. The receipts weren't attached. | Published | Jobs that stop halfway: resuming a multi-step task without starting over. |
| 5 | It asked for the same receipt 40 times | Published | Agents stuck in loops: how to stop an agent repeating itself. |
| 6 | Does this even need an AI agent? | Published | Workflow or agent: a fixed script often beats an agent for routine work. |
| 7 | Two claims, two different paths. Which one was right? | Published | Testing agents: checking paths, not just final answers. |
| 8 | So, should your AI do things, or just answer? | Published | Finale: a checklist for giving an AI actions safely. |

## Series 3: Just put the rules in the prompt

| No. | Title | Status | One-line summary |
|---|---|---|---|
| 1 | Why did the AI promise a full refund on a non-refundable ticket? | Published | Curtain raiser: rules written in a prompt are requests, not rules. |
| 2 | Code decides. The AI explains. | Published | Splitting the work: code applies the rule, the model explains it. |
| 3 | The policy is 40 pages. Who turns it into rules? | Published | From policy to rules: someone must translate the policy into checkable logic. |
| 4 | The waiver was in the prompt. Not in the code. | Published | When rules change: a temporary waiver must be a code change with an end date. |
| 5 | So, who should decide: the code or the model? | Published | Finale: a checklist for deciding which rules belong in code. |

## Series 4: Just tell it not to (guardrails)

| No. | Title | Status | One-line summary |
|---|---|---|---|
| 1 | Why didn't "Please don't give medical advice" work? | Published | Curtain raiser (pharmacy version, as posted): a prompt is a request, not a fence. |
| 2 | What should you check before the question reaches the model? | Published | Input checks: a bouncer that screens questions before the model sees them. |
| 3 | What should you check before the answer reaches the customer? | Published | Output checks: catching promises the policy never approved. |
| 4 | What if a customer tries to trick it? | Draft | Red teaming: testing attacks, including ones hidden in order notes. |
| 5 | What if your guardrails lock out your own team? | Draft | Staff exceptions: a supervised, logged route for approved exceptions. |
| 6 | How strict is too strict? | Draft | Safety vs usefulness: measuring missed harm and false refusals together. |
| 7 | So, is your AI fenced or just asked nicely? | Draft | Finale: five layers mapped to code, plus a guardrails checklist. |

## Series 5 to 16: curtain raisers only

No articles exist yet for these series. Each has one curtain raiser post, all in Draft.

| Series | Title | Status | One-line summary |
|---|---|---|---|
| 5 The prompt works, ship it | Works on my prompt | Draft | "It works" on one prompt is not a test. |
| 6 Observability | We'll know when it breaks | Draft | Without tracking, a broken AI looks fine. |
| 7 POC to production | It worked in the demo | Draft | A demo is not production: scale, errors and sign-off. |
| 8 Few cents per call | What's a few cents between friends? | Draft | Small per-call costs add up fast at scale. |
| 9 AI transformation | We bought AI, so we're AI-first now | Draft | Buying licences is not transforming how the work gets done. |
| 10 AI gateway | Everyone gets an API key | Draft | One gateway beats many keys, each with its own rules. |
| 11 MCP server | Just plug it in | Draft | Plugging in tools needs permissions, limits and owners. |
| 12 AI memory | It should just remember me | Draft | Memory needs rules about what is kept, for how long, and who sees it. |
| 13 Knowledge graph | Just connect the dots | Draft | A graph answers "what depends on what" questions that search cannot. |
| 14 Agentic RAG | Let it do its own research | Draft | Letting an agent search on its own adds cost and risk. |
| 15 Multi-agent | More agents, more brains | Draft | More agents add coordination problems, not just capability. |
| 16 Agent harness | We bought the brain, we're done | Draft | The model is only part of the system; the harness does the work around it. |

## Series 20: Today in AI (open-ended, numbered)

| No. | Title | Status | One-line summary |
|---|---|---|---|
| 000 | Curtain raiser: AI news is a firehose | Draft | A post announcing the series, not an article. |
| 001 | What happens when your AI agent visits someone else's website? | Published | Wikimedia reported AI agents crawling its site and what that means for site owners. |
| 002 | What if your chatbot answered with buttons instead of paragraphs? | Published | OpenAI's Intelligent UI turns answers into charts and buttons. |
| 003 | Why does Google's newest AI go to security teams first? | Published | Gemini 4 Argon was released in stages, starting with security experts. |
| 004 | Why is Microsoft's new AI built to choose, not to chat? | Published | Decision models pick options instead of writing paragraphs. |
| 005 | If AI can build your dashboards, what's left for the data team? | Published | Claude Dashboards makes screens easy; trusted data and meaning are the real job. |
| 006 | Your AI made a decision. Can you prove why? | Published | Data lineage vs decision lineage: tracing the decision, not just the data. |
| 007 | Should every question go to your most expensive AI? | Published | AI routers send easy questions to small, cheap models. |
| 008 | Does using AI make you give up faster? | Published | A study found AI help can lower persistence once the AI is gone. |
| 009 | Same AI, many clouds. Where does your data actually go? | Published | In-country AI keeps data and inference inside a country's cloud region. |
| 010 | Your AI agent is waiting. Are you still paying? | Published | Google's Agent Compute Engine gives each agent a paused, isolated computer. |
| 011 | AI text-to-speech that fits on your phone. No internet needed. | Published | A small on-device voice model that runs without the cloud. |
| 012 | Would you send your AI twin to a job interview? | Draft | TwinCafe lets recruiters question a candidate's AI twin first. |
| 013 | What if the chart is the easy part? | Published | Claude Dashboards beta and the provider race; a fictional store story. |

## System design (AI)

| No. | Title | Status | One-line summary |
|---|---|---|---|
| 8 | Your AI agent is accurate, but token usage keeps climbing. How would you fix it? | Draft | Find where the extra tokens go and cut them without losing accuracy. (Only No. 8 is in the repo; the README plans 33.) |

## Claude Architect exam

| No. | Title | Status | One-line summary |
|---|---|---|---|
| 0 | Curtain raiser: Claude Architect, one objective at a time | Draft | Series intro: studying the Claude Architect exam with a fictional store. |
| 1 | How does an agent know when to stop? | Draft | Objective 1.1: stop on the model's stop signal, not on its wording or a step count. |

## Explain It Like Hello World (Series 23)

Each line is the main idea of one write-up. Draft means not yet posted.

| No. | Title | Status | One-line summary |
|---|---|---|---|
| 1 | AI words everyone uses. Nobody explains. | Published | Curtain raiser: the AI words this series will explain, one at a time. |
| 2 | What actually counts as artificial intelligence? | Published | AI is any machine doing a task that seems to need thinking; the word is stretched. |
| 3 | How does machine learning learn without being told the rules? | Published | Machine learning finds patterns from examples instead of hand-written rules. |
| 4 | What's "deep" about deep learning? | Published | Deep learning uses many layers of simple units, which is why it got good at seeing and hearing. |
| 5 | Is a neural network really like a brain? | Published | A neural network is layers of numbers that adjust; the brain comparison is loose. |
| 6 | What makes generative AI "generative"? | Published | Generative AI creates new content, such as text or images, rather than only sorting it. |
| 7 | Why are they called foundation models? | Published | A foundation model is one large base model that many apps are built on. |
| 8 | What is a frontier model, and who decides? | Published | A frontier model is the newest, most capable base model; the label is not an official rank. |
| 9 | What is AGI, and what would make AI "general"? | Draft | AGI means AI that matches people across most tasks; no one agrees on a test. |
| 10 | What is superintelligence, and should we worry? | Draft | An AI far smarter than people; a concern for scientists, but still a debated idea. |
| 11 | What are tokens, and why does an AI read in pieces? | Draft | Tokens are chunks of text the model reads and bills; often less than a word. |
| 12 | How does an LLM write a sentence? | Draft | An LLM predicts the next token again and again, very fast. |
| 13 | How do embeddings know "king" is close to "queen"? | Draft | Embeddings turn meaning into numbers, so similar words sit close together. |
| 14 | How does attention help an AI know what "it" means? | Draft | Attention lets each word look at the other words that matter to it. |
| 15 | What is a transformer, the "T" in GPT? | Draft | The transformer is the model design built on attention that most modern AI uses. |
| 16 | What is a context window, and why does an AI forget? | Draft | The context window is how much text the model can see at once. |
| 17 | What's a knowledge cutoff, and why is the AI behind on news? | Draft | The model's training data stops at a date, so newer events are unknown to it. |
| 18 | What is context rot, and why do long chats get worse? | Draft | Answers can slip as a conversation or document grows. |
| 19 | Why does temperature change the AI's answer? | Draft | Temperature controls how random the next word choice is. |
| 20 | What is a prompt, and why does the way you ask matter? | Draft | A prompt is everything the model is given to work from; wording changes results. |
| 21 | Is prompt engineering a real skill? | Draft | Writing clear, tested instructions for a model: useful, but not magic. |
| 22 | What's in a system prompt, the hidden instruction behind every chatbot? | Draft | A system prompt is the standing instruction the company gives the model. |
| 23 | What is zero-shot, and can an AI do a task it was never shown? | Draft | Zero-shot means asking for a task with no examples. |
| 24 | Why does few-shot prompting work so well? | Draft | Showing a few examples in the prompt often beats long instructions. |
| 25 | Why does chain of thought ("think step by step") work? | Draft | Asking for steps helps the model reason through harder problems. |
| 26 | What is reflection, and why does an AI check its own answer? | Draft | The model reviews its own draft, which catches some mistakes. |
| 27 | Is context engineering the new prompt engineering? | Draft | Context engineering is choosing what information the model sees, not only the wording. |
| 28 | How does structured output get an AI to fill in a form? | Draft | The model returns data in a fixed format, such as JSON, that code can read. |
| 29 | Why does streaming make the AI type word by word? | Draft | Streaming sends each token as it is made, so answers start sooner. |
| 30 | What do parameters, like "70B", actually mean? | Draft | Parameters are the learned numbers inside a model; 70B means 70 billion. |
| 31 | What happens during training, when an AI goes to school? | Draft | Training adjusts the parameters using huge amounts of example text. |
| 32 | What's the difference between supervised and unsupervised learning? | Draft | Supervised learning uses labelled answers; unsupervised looks for patterns with none. |
| 33 | What is inference, and what happens when you hit send? | Draft | Inference is the model running to produce an answer, and it is where most cost now goes. |
| 34 | What is pretraining, and how does an AI learn language? | Draft | Pretraining is the first, most expensive stage: learning language from vast text. |
| 35 | What is fine-tuning, and how does an AI learn your way? | Draft | Fine-tuning trains a pre-trained model further on your examples. |
| 36 | What is LoRA, and how do you customise an AI cheaply? | Draft | LoRA adds small trainable pieces, so fine-tuning is cheaper. |
| 37 | How does reinforcement learning teach AI by trial and error? | Draft | The model learns from rewards for good actions. |
| 38 | What is RLHF, and how did the AI learn to be polite? | Draft | Humans rank answers, and the model learns to prefer the ones people like. |
| 39 | What is constitutional AI, and can an AI follow principles? | Draft | The model checks its answers against a written set of principles. |
| 40 | What is distillation, and how does a small AI learn from a big one? | Draft | A small model is trained to copy a bigger model's answers. |
| 41 | What is synthetic data, and can an AI learn from AI-written data? | Draft | Data made by a model, used for training; useful, but with limits. |
| 42 | What is data labelling, and who teaches the AI what's right? | Draft | People mark examples as right or wrong, which teaches the model. |
| 43 | What is overfitting, and why can an AI ace the practice test and fail? | Draft | The model memorises the practice examples and misses new ones. |
| 44 | What are scaling laws, and why did bigger AI keep getting better? | Draft | Bigger models with more data and compute improved in a predictable way, for a time. |
| 45 | Are emergent abilities real, or does bigger AI just seem to learn new tricks? | Draft | New skills seem to appear at scale; researchers still debate whether they are sudden. |
| 46 | What is model collapse, and what happens when AI learns from AI? | Draft | Training on AI output over and over can make models worse. |
| 47 | What is quantization, and how does a giant AI fit on a laptop? | Draft | Quantization stores the numbers in less space, so models run on smaller hardware. |
| 48 | What is a mixture of experts, and why doesn't the whole AI wake up? | Draft | Only some specialist parts of the model run for each word, which saves cost. |
| 49 | What is a KV cache, and why doesn't the AI re-read everything? | Draft | The KV cache saves earlier work so the model does not recompute it. |
| 50 | How does prompt caching make repeated prompts cheaper? | Draft | Reusing the same prompt start is billed at a lower rate. |
| 51 | How does speculative decoding make a big AI faster? | Draft | A small model drafts words and the big model checks them, which is faster. |
| 52 | What is test-time compute, and why does thinking cost more? | Draft | Letting the model think longer gives better answers at higher cost. |
| 53 | Why does AI run on a GPU, a gaming chip? | Draft | GPUs do many simple maths steps at once, which AI needs. |
| 54 | What is a TPU, and why did Google build one? | Draft | A TPU is Google's own AI chip. |
| 55 | What is an NPU, the AI chip inside your new laptop? | Draft | An NPU runs AI tasks on a laptop or phone efficiently. |
| 56 | Can a small language model be good enough? | Draft | Small models can do focused tasks well at lower cost. |
| 57 | What is on-device AI, and can an AI live on your phone? | Draft | The model runs on the device, so data does not leave it. |
| 58 | What is latency, and why does the AI take so long to answer? | Draft | Latency is the wait before an answer, which users feel most. |
| 59 | What is time to first token, and why does the first word matter most? | Draft | The time until the first word appears, which shapes how fast it feels. |
| 60 | What is RAG, and how does an AI answer from your documents? | Draft | RAG finds relevant text first, then gives it to the model to answer from. |
| 61 | Why does AI cut your documents into chunks? | Draft | Chunking splits documents into pieces small enough to search and send. |
| 62 | What is a vector database, and where does an AI store meaning? | Draft | A database that searches by meaning, using embeddings. |
| 63 | How does semantic search understand what you meant? | Draft | Semantic search matches meaning, not only exact words. |
| 64 | What is reranking, and why does AI search look twice? | Draft | A second pass re-orders search results so the best ones come first. |
| 65 | What is hybrid search, and why use two ways to search? | Draft | Combining keyword and meaning search finds more of the right text. |
| 66 | What is a knowledge graph, and who is connected to whom? | Draft | A map of things and how they connect, like people and companies. |
| 67 | What is GraphRAG, and how does an AI answer about a whole pile of documents? | Draft | RAG that uses a knowledge graph to answer questions across many documents. |
| 68 | What is grounding, and how do you keep an AI tied to the facts? | Draft | Grounding ties answers to supplied sources. |
| 69 | How do citations show where an AI got its answer? | Draft | Citations point to sources, but the links still need checking. |
| 70 | Can deep research do your research for you? | Draft | Deep research runs many searches and writes a report; check its sources. |
| 71 | What makes an AI agent an "agent"? | Draft | An agent plans steps and uses tools to reach a goal, not just answer. |
| 72 | What is an agent harness, and why does every agent need one? | Draft | The software around the model that runs the agent safely. |
| 73 | What does "agentic AI" really mean? | Draft | AI that acts on its own over steps; the word is used loosely. |
| 74 | What is loop engineering, and why is it the next step after prompts? | Draft | Designing the loop an agent runs in: what it checks and when it stops. |
| 75 | How does tool calling let an AI check the weather? | Draft | The model asks code to run a tool, then uses the result. |
| 76 | What is MCP, and why is everyone talking about it? | Draft | Model Context Protocol: a standard way to plug tools into AI apps. |
| 77 | What are agent skills, and why do agents need a playbook? | Draft | Packaged know-how an agent loads for a task. |
| 78 | What is A2A, and how do AI agents talk to each other? | Draft | A2A is a protocol for agents from different vendors to work together. |
| 79 | Is a multi-agent system better than one AI agent? | Draft | Several agents help on some tasks and add coordination cost on others. |
| 80 | What is a supervisor agent, and who decides which agent does what? | Draft | A manager agent that assigns work to other agents. |
| 81 | How does AI memory remember you? | Draft | Memory is saved notes or stored records, not the model learning from chats. |
| 82 | What is a checkpoint, and why is it better than starting over? | Draft | A saved point an agent can resume from after a failure. |
| 83 | How does computer use let an AI click like you? | Draft | The AI looks at the screen and clicks and types, like a person. |
| 84 | What's the difference between a copilot and an agent? | Draft | A copilot helps you while you work; an agent acts on its own. |
| 85 | What is an agent sandbox, and where should an AI agent work? | Draft | An isolated space where an agent can run code without touching real systems. |
| 86 | What is a reasoning model, and why does the AI think before it answers? | Draft | A model that spends extra steps reasoning before answering. |
| 87 | What is a decision model, and why does it choose instead of chat? | Draft | A model built to pick among options, not to write. |
| 88 | What is multimodal AI, and how can one AI read, see and listen? | Draft | One model that handles text, images, audio or video. |
| 89 | How does a diffusion model draw a picture from noise? | Draft | Starts from random noise and removes it step by step until an image appears. |
| 90 | How does voice AI talk back without a pause? | Draft | Real-time voice models listen and speak with very little delay. |
| 91 | How does text-to-video make a video from a sentence? | Draft | A model generates video frames from a text description. |
| 92 | What is a deepfake, and how can a video of someone be fake? | Draft | AI-made video or audio that shows someone saying or doing something they did not. |
| 93 | Can voice cloning copy your voice from a few seconds of audio? | Draft | Voice cloning copies a voice from a short sample; useful, and open to scams. |
| 94 | What is an AI avatar, the presenter nobody filmed? | Draft | A digital person who speaks on screen, made by AI. |
| 95 | What's a digital twin, and why do factories want one? | Draft | A virtual copy of a factory, city or system used to test changes. |
| 96 | What does "open" mean in an open-weight model? | Draft | The model weights are published, which is not the same as fully open source. |
| 97 | What is a world model, and can an AI imagine what happens next? | Draft | A model that predicts how the world changes, useful for robots and simulation. |
| 98 | What is embodied AI, and when does AI get a body? | Draft | AI inside a robot or machine that acts in the physical world. |
| 99 | What is hallucination, and why does an AI sound sure when it's wrong? | Draft | The model makes up plausible but false content. |
| 100 | What is AI sycophancy, and why does the AI keep agreeing? | Draft | The model tends to tell people what they want to hear. |
| 101 | What are guardrails, and how do you stop an AI saying the wrong thing? | Draft | Checks and limits that screen what goes in and out of the model. |
| 102 | What does "human-in-the-loop" really mean? | Draft | A person reviews or approves key steps, but only works if the person can really check. |
| 103 | What is a jailbreak, and how do people trick an AI? | Draft | Tricks that try to make the model ignore its rules. |
| 104 | What is prompt injection, and can a web page give orders to your AI? | Draft | Hidden text in content the AI reads can try to change its behaviour. |
| 105 | What is red teaming, and who attacks an AI on purpose? | Draft | Testers attack a model on purpose to find weaknesses before users do. |
| 106 | What are evals, and how do you know an AI is getting better? | Draft | Tests that measure the model's quality on a set of tasks. |
| 107 | What is LLM-as-a-judge, and can one AI mark another AI's homework? | Draft | One model grades another model's answers, with known limits. |
| 108 | What is AI bias, and how does an AI end up unfair? | Draft | Unfair results that come from the data or design. |
| 109 | What is explainability, and can an AI tell you why it decided? | Draft | Showing the reasons behind a decision; hard for large models. |
| 110 | What is alignment, and how do you make an AI want what we want? | Draft | Making AI systems act in line with human goals and values. |
| 111 | Can watermarking tell you if AI wrote this? | Draft | Hidden or attached marks that show content came from AI; not foolproof. |
| 112 | What is AI regulation, and who makes the rules for AI? | Draft | Laws such as the EU AI Act set duties for AI use. |
| 113 | What does "responsible AI" actually involve? | Draft | Policies, testing, oversight and records that show AI is used safely. |
| 114 | What is shadow AI, and is your team using AI you don't know about? | Draft | Staff using AI tools the company has not approved. |
| 115 | What is sovereign AI, and why do countries want their own? | Draft | Countries building their own models and data centres for control. |
| 116 | What do benchmarks mean, like "scored 90%"? | Draft | Standard test scores; useful, but they do not show everything. |
| 117 | What is vibe coding, and can you build an app by describing it? | Draft | Building software by describing it to an AI, often without reading the code. |
| 118 | What is AI slop, and why is the internet filling up with it? | Draft | Low-quality AI content that floods feeds and search results. |
| 119 | What is AI washing, and how do you spot it? | Draft | Calling a product "AI-powered" when the AI is small or missing. |
| 120 | What is GEO, and how do you get found when people ask AI? | Draft | Generative engine optimisation: making content easy for AI answers to use. |
| 121 | What makes a company "AI-native"? | Draft | A company built around AI from the start, not AI added later. |
| 122 | What is LLMOps, and who keeps an AI running after launch? | Draft | The daily work of running, monitoring and updating AI in production. |
| 123 | What is observability, and why can't you debug an AI without it? | Draft | Logs, traces and metrics that show what a running system did. |
| 124 | What is an AI gateway, the front door to your AI? | Draft | One controlled entry point for all AI calls, with rules and logs. |
| 125 | What is model routing, and should every question go to the biggest AI? | Draft | Sending each question to the right-sized model to cut cost. |
| 126 | Your AI dictionary, one line per word | Draft | Finale: one line for every term in the series. |

## Retired files (not part of any series)

| File | Status | One-line summary |
|---|---|---|
| `_retired/02-users-will-love-the-chatbot/01-first-10-seconds.md` | Retired | Chatbot first impressions: the first 10 seconds decide trust. |
| `_retired/07-llm-output-to-json/01-curtain-raiser.md` | Retired | Why a "perfect" JSON profile breaks one time in fifty. |
| `_retired/14-connect-agent-to-tools/01-curtain-raiser.md` | Retired | Should your AI be allowed to give money back? |
| `_retired/14-lets-make-it-agentic/01-curtain-raiser.md` | Retired | What makes an AI an agent? |
| `22-claude-architect-exam/_retired/01-agentic-loops-long-parentpace.md` | Retired | Long ParentPace version of objective 1.1 (agentic loops), replaced by the store version. |

`qna/` has folders but no Markdown files, so it has no articles to summarise.
