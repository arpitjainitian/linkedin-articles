# Summary of every article: problem and solution

A single list of every write-up in the repo, one line each for the problem it covers and the solution it gives. Status comes from each file's `Published:` line: **Published** means it is live on LinkedIn; **Draft** means it is written but not posted. Series with only a curtain raiser have a planned solution, not a written one. The series READMEs hold the full tables and links.

Retired files are at the end. The `qna/` folder has no Markdown files.

## Series 1: #JustAddRAG

| No. | Title | Status | Problem | Solution |
|---|---|---|---|---|
| 1 | Why does "Just add RAG" sound like 2 weeks but take 6 months? | Published (LinkedIn only, no file in repo) | A demo works in a day, so the project looks nearly done. | Plan for the hidden work: documents, testing, security, cost. |
| 2 | Why can't your AI read a PDF that a 10-year-old can? | Published (LinkedIn only, no file in repo) | The AI cannot use text it cannot read from a PDF or scan. | Fix document ingestion and OCR before blaming the model. |
| 3 | What if the answer was in your docs, but you cut it in half? | Published | Cutting documents into pieces can split the answer apart. | Choose a chunking method and test it on real questions. |
| 4 | Is your AI hallucinating, or just looking in the wrong place? | Published | Wrong answers often come from retrieving the wrong text. | Use a retrieval toolkit (hybrid search, reranking) and check what was found. |
| 5 | What does your AI say when it doesn't know? | Published | The AI gives fluent, confident answers even without sources. | Design a "not found" answer and require citations to sources. |
| 6 | Do you need an LLM, a database, or both? | Published | Every question is sent to an LLM, though many need a database lookup. | Route each question to a database, an LLM, or both. |
| 7 | What happens when your AI finds two versions of the truth? | Published | Old and new versions of a document compete in search. | Tag versions with dates and retrieve the current one. |
| 8 | Can the intern ask your AI about the CEO's salary? | Published | The AI can reveal documents the user is not allowed to see. | Enforce access rules at retrieval, not only in the prompt. |
| 9 | How many questions did you test before saying "it works"? | Published | "It works" is based on a few tries. | Build a ground-truth test set and measure scores. |
| 10 | A few cents per question: so why is finance calling? | Published | Small per-question costs add up quietly across many users. | Estimate cost per question before launch and set budgets. |
| 11 | It's fast in the demo, so why are users clicking twice? | Published | Real traffic is slower and less reliable than the demo. | Measure each step, set timeouts, and plan fallbacks. |
| 12 | Where did your user's passport just travel to? | Published | Personal data leaks into vendor systems and logs. | Map the data flow, minimise what is sent, and support deletion. |
| 13 | When your AI gives a wrong answer, can you tell why? | Published | Ordinary logs cannot show which document or step caused an answer. | Log each step with its sources and versions. |
| 14 | Nobody touched the code. Why did the answers change? | Published | Vendor model updates change answers without warning. | Pin model versions and re-run evals before any upgrade. |
| 15 | So, should you really "just add RAG"? | Published | RAG is treated as the answer to every AI problem. | Use a checklist to decide when RAG fits and what to build around it. |

## Series 2: Beyond Just RAG: From Answers to Actions

| No. | Title | Status | Problem | Solution |
|---|---|---|---|---|
| 1 | Your AI can answer. Now it has to act. | Published | An AI that answers cannot yet file claims or change records. | Plan for actions with checks, limits and approvals. |
| 2 | The receipt says ₹1,180. Or was it ₹118? | Published | The AI misreads amounts from messy receipts. | Extract exact values and check them before acting. |
| 3 | It filed the same claim twice | Published | A timeout makes the AI retry and file a duplicate. | Make retries safe with a request key, so a repeat does nothing new. |
| 4 | The claim was filed. The receipts weren't attached. | Published | A job stops halfway and leaves partial work. | Use checkpoints so the job resumes where it stopped. |
| 5 | It asked for the same receipt 40 times | Published | The agent loops on the same step. | Set step limits, detect repeats, and hand off to a person. |
| 6 | Does this even need an AI agent? | Published | Agents get used where a simple workflow would do. | Use a fixed workflow for routine tasks; use an agent only when needed. |
| 7 | Two claims, two different paths. Which one was right? | Published | Agents take different paths to the same goal, so they are hard to test. | Test the path as well as the final result. |
| 8 | So, should your AI do things, or just answer? | Published | Teams are unsure when giving an AI actions is safe. | Use a checklist before letting the AI act. |

## Series 3: Just put the rules in the prompt

| No. | Title | Status | Problem | Solution |
|---|---|---|---|---|
| 1 | Why did the AI promise a full refund on a non-refundable ticket? | Published | Rules written in a prompt are requests the model can ignore. | Put rules in code and let the AI explain them. |
| 2 | Code decides. The AI explains. | Published | One component is asked to both decide and explain. | Code makes the decision; the AI writes the explanation. |
| 3 | The policy is 40 pages. Who turns it into rules? | Published | A long policy does not turn into checkable rules by itself. | Translate the policy into rule tables that owners review. |
| 4 | The waiver was in the prompt. Not in the code. | Published | Temporary waivers stay in prompts and are never switched off. | Keep rules in code, with dates and owners. |
| 5 | So, who should decide: the code or the model? | Published | Teams do not agree which decisions belong to code. | Use a checklist to assign each decision to code or model. |

## Series 4: Just tell it not to (guardrails)

| No. | Title | Status | Problem | Solution |
|---|---|---|---|---|
| 1 | Why didn't "Please don't give medical advice" work? | Published | A prompt that says "never give medical advice" is not enforced. | Use layered guardrails, not a prompt alone. |
| 2 | What should you check before the question reaches the model? | Published | Risky questions reach the model, which tries to help. | Screen questions before the model sees them. |
| 3 | What should you check before the answer reaches the customer? | Published | The reply promises things the policy does not allow. | Check replies against the rules and send a safe fallback if needed. |
| 4 | What if a customer tries to trick it? | Draft | Clever wording and hidden instructions bypass rules. | Red-team the assistant, including attacks hidden in order notes. |
| 5 | What if your guardrails lock out your own team? | Draft | Guardrails block legitimate staff exceptions. | Give staff a logged, time-limited, human-approved route. |
| 6 | How strict is too strict? | Draft | Strict bots refuse safe requests, and nobody measures it. | Measure missed harm and false refusals together. |
| 7 | So, is your AI fenced or just asked nicely? | Draft | Guardrails are scattered and never checked. | Use a five-layer checklist mapped to code. |

## Series 5 to 16: curtain raisers only

No articles exist yet for these series. Each has one curtain raiser post, all in Draft. The solution is the planned topic, not a written one.

| Series | Title | Status | Problem | Planned solution |
|---|---|---|---|---|
| 5 The prompt works, ship it | Works on my prompt | Draft | "It works" on one prompt is treated as a test. | Real tests before shipping. |
| 6 Observability | We'll know when it breaks | Draft | A broken AI looks fine until users complain. | Monitoring and alerts. |
| 7 POC to production | It worked in the demo | Draft | A demo is not production: scale, errors and sign-off. | Production-readiness steps. |
| 8 Few cents per call | What's a few cents between friends? | Draft | Per-call costs add up fast at scale. | Cost controls and budgets. |
| 9 AI transformation | We bought AI, so we're AI-first now | Draft | Buying licences is mistaken for changing how the work is done. | Change the work, not just the tools. |
| 10 AI gateway | Everyone gets an API key | Draft | Many teams hold many keys, each with its own rules. | One gateway with keys, limits and logs. |
| 11 MCP server | Just plug it in | Draft | Plugging in tools gives AI access with no owners or limits. | Scoped tool access with named owners. |
| 12 AI memory | It should just remember me | Draft | Memory can keep things nobody agreed to store. | Rules for what is remembered, for how long, and how it is deleted. |
| 13 Knowledge graph | Just connect the dots | Draft | "What depends on what?" questions are hard for search. | Model the relationships in a knowledge graph. |
| 14 Agentic RAG | Let it do its own research | Draft | An agent searching on its own adds cost and risk. | Bounded agent search with checks. |
| 15 Multi-agent | More agents, more brains | Draft | More agents add coordination problems. | Clear roles and coordination rules. |
| 16 Agent harness | We bought the brain, we're done | Draft | Teams think the model is the whole system. | Build the harness around the model. |

## Series 20: Today in AI (open-ended, numbered)

| No. | Title | Status | Problem | Solution |
|---|---|---|---|---|
| 000 | Curtain raiser: AI news is a firehose | Draft | Too much AI news to follow. | A short series that explains one development at a time. |
| 001 | What happens when your AI agent visits someone else's website? | Published | AI agents visit websites in ways site owners did not expect. | Site owners need to see and control agent visits. |
| 002 | What if your chatbot answered with buttons instead of paragraphs? | Published | Long chatbot answers are hard to scan and act on. | Answers with charts and buttons, as OpenAI's Intelligent UI does. |
| 003 | Why does Google's newest AI go to security teams first? | Published | A very capable AI could be misused for cyber attacks. | Release it in stages, starting with security experts. |
| 004 | Why is Microsoft's new AI built to choose, not to chat? | Published | Chat models write text when a business needs a choice. | Decision models that pick from options. |
| 005 | If AI can build your dashboards, what's left for the data team? | Published | Dashboards are easy to make, but numbers can disagree. | The data team owns trusted data and the meaning of each number. |
| 006 | Your AI made a decision. Can you prove why? | Published | A decision cannot be traced back to its reasons. | Record decision lineage, not only data lineage. |
| 007 | Should every question go to your most expensive AI? | Published | Every question goes to the most expensive model. | An AI router sends easy questions to small, cheap models. |
| 008 | Does using AI make you give up faster? | Published | People persist less once the AI help is gone. | Use hints carefully and practise without AI too. |
| 009 | Same AI, many clouds. Where does your data actually go? | Published | Unclear where AI processing happens. | In-country AI that keeps processing inside a country's cloud region. |
| 010 | Your AI agent is waiting. Are you still paying? | Published | Idle agents still cost money. | Google's Agent Compute Engine pauses each agent in an isolated computer. |
| 011 | AI text-to-speech that fits on your phone. No internet needed. | Published | Cloud voice sends your text to a server. | A small voice model that runs on the device. |
| 012 | Would you send your AI twin to a job interview? | Draft | Résumés miss people with unusual careers. | Recruiters question an AI twin first, with trust concerns still open. |
| 013 | What if the chart is the easy part? | Published | Different AI tools return different numbers for the same question. | One governed definition behind every screen. |

## System design (AI)

| No. | Title | Status | Problem | Solution |
|---|---|---|---|---|
| 8 | Your AI agent is accurate, but token usage keeps climbing. How would you fix it? | Draft | Accurate agent, rising token use for the same work. | Measure first, fix the usual causes, protect accuracy, then monitor. (Only No. 8 is in the repo; the README plans 33.) |

## Claude Architect exam

| No. | Title | Status | Problem | Solution |
|---|---|---|---|---|
| 0 | Curtain raiser: Claude Architect, one objective at a time | Draft | Exam prep feels like a wall of material. | Learn one objective at a time, with a store example. |
| 1 | How does an agent know when to stop? | Draft | An agent stops on words like "done", not the real signal. | Stop on the model's stop signal; keep a step cap only as a safety net. |

## Explain It Like Hello World (Series 23)

Each row is one term. The problem is the confusion a reader has; the solution is the plain explanation. Draft means not yet posted.

| No. | Title | Status | Problem | Solution |
|---|---|---|---|---|
| 1 | AI words everyone uses. Nobody explains. | Published | AI jargon is used everywhere and explained nowhere. | One plain explanation per word, one write-up at a time. |
| 2 | What actually counts as artificial intelligence? | Published | "AI" now covers phones, toothbrushes and more. | AI is any machine doing a task that seems to need thinking. |
| 3 | How does machine learning learn without being told the rules? | Published | People assume AI is hand-coded rules. | Machine learning finds patterns from examples. |
| 4 | What's "deep" about deep learning? | Published | "Deep" sounds philosophical. | Many layers of simple units, which made AI good at seeing and hearing. |
| 5 | Is a neural network really like a brain? | Published | The brain comparison is taken too literally. | A neural network is layers of numbers that adjust. |
| 6 | What makes generative AI "generative"? | Published | "GenAI" is everywhere, but the difference from older AI is unclear. | It creates new content, such as text or images, not only sorting it. |
| 7 | Why are they called foundation models? | Published | "Foundation model" sounds like construction. | One large base model that many apps are built on. |
| 8 | What is a frontier model, and who decides? | Published | "Frontier" sounds official but is not a fixed rank. | The newest, most capable base model; the label is not an official ranking. |
| 9 | What is AGI, and what would make AI "general"? | Draft | "AGI is coming" is predicted and disputed. | AI that matches people across most tasks; nobody agrees on a test. |
| 10 | What is superintelligence, and should we worry? | Draft | Warnings use the word, but it sounds like science fiction. | An AI far smarter than people; a debated concern. |
| 11 | What are tokens, and why does an AI read in pieces? | Draft | People think a token is a word; it is not. | Tokens are text chunks the model reads and bills, often under a word. |
| 12 | How does an LLM write a sentence? | Draft | "Large language model" sounds like a giant brain. | It predicts the next token, again and again, very fast. |
| 13 | How do embeddings know "king" is close to "queen"? | Draft | "Embeddings" sounds like maths homework. | Meaning is turned into numbers, so similar words sit close together. |
| 14 | How does attention help an AI know what "it" means? | Draft | "Attention" sounds vague. | Each word looks at the other words that matter to it. |
| 15 | What is a transformer, the "T" in GPT? | Draft | The "T" in GPT is unexplained. | The design built on attention that most modern AI uses. |
| 16 | What is a context window, and why does an AI forget? | Draft | Bigger context windows are advertised without meaning. | The amount of text the model can see at once. |
| 17 | What's a knowledge cutoff, and why is the AI behind on news? | Draft | Chatbots are confidently out of date. | Training data stops at a date, so newer events are unknown to the model. |
| 18 | What is context rot, and why do long chats get worse? | Draft | Long chats and documents get worse answers. | Quality can slip as the context grows; longer is not always better. |
| 19 | Why does temperature change the AI's answer? | Draft | "Set temperature to zero" is used like a spell. | Temperature controls how random the next word choice is. |
| 20 | What is a prompt, and why does the way you ask matter? | Draft | "Write a better prompt" is advice without a definition. | A prompt is everything the model is given; wording changes results. |
| 21 | Is prompt engineering a real skill? | Draft | It is unclear whether it is a real job skill. | Clear, tested instructions for a model: useful, not magic. |
| 22 | What's in a system prompt, the hidden instruction behind every chatbot? | Draft | Companies hide their system prompts. | The standing instruction the company gives the model. |
| 23 | What is zero-shot, and can an AI do a task it was never shown? | Draft | "Zero-shot" sounds like a sports term. | Asking for a task with no examples. |
| 24 | Why does few-shot prompting work so well? | Draft | Long instructions often fail. | A few examples in the prompt often work better. |
| 25 | Why does chain of thought ("think step by step") work? | Draft | Models give wrong answers to harder questions. | Asking for steps helps the model reason. |
| 26 | What is reflection, and why does an AI check its own answer? | Draft | The first answer contains mistakes. | The model reviews its own draft before answering. |
| 27 | Is context engineering the new prompt engineering? | Draft | Prompt wording is not enough for complex tasks. | Choose what information the model sees, not only the wording. |
| 28 | How does structured output get an AI to fill in a form? | Draft | Code cannot read free-form answers. | The model returns data in a fixed format, such as JSON. |
| 29 | Why does streaming make the AI type word by word? | Draft | Waiting for the full answer feels slow. | Each token is sent as it is made, so the answer starts sooner. |
| 30 | What do parameters, like "70B", actually mean? | Draft | Model sizes are quoted without meaning. | Parameters are the learned numbers inside a model. |
| 31 | What happens during training, when an AI goes to school? | Draft | Training is mysterious and expensive. | Parameters are adjusted using huge amounts of example text. |
| 32 | What's the difference between supervised and unsupervised learning? | Draft | The two terms are confused. | Supervised learning uses labelled answers; unsupervised finds patterns in unlabelled data. |
| 33 | What is inference, and what happens when you hit send? | Draft | Inference costs dominate bills, but the term is unclear. | Inference is the model running to produce an answer. |
| 34 | What is pretraining, and how does an AI learn language? | Draft | "Pre-trained" is unexplained. | The first, most expensive stage: learning language from vast text. |
| 35 | What is fine-tuning, and how does an AI learn your way? | Draft | Teams fine-tune without knowing what changes. | Training a pre-trained model further on your own examples. |
| 36 | What is LoRA, and how do you customise an AI cheaply? | Draft | Customising a model sounds costly. | LoRA adds small trainable pieces, which makes tuning cheaper. |
| 37 | How does reinforcement learning teach AI by trial and error? | Draft | "RL" is used without explanation. | The model learns from rewards for good actions. |
| 38 | What is RLHF, and how did the AI learn to be polite? | Draft | The acronym hides why chatbots are polite. | Humans rank answers, and the model learns to prefer the ones they like. |
| 39 | What is constitutional AI, and can an AI follow principles? | Draft | "Constitutional AI" sounds like a parliament. | The model checks answers against written principles. |
| 40 | What is distillation, and how does a small AI learn from a big one? | Draft | Small models are described as "distilled" without meaning. | A small model is trained to copy a bigger model's answers. |
| 41 | What is synthetic data, and can an AI learn from AI-written data? | Draft | "Synthetic data" sounds fake. | Data made by a model, used for training, with limits. |
| 42 | What is data labelling, and who teaches the AI what's right? | Draft | Hidden human work behind AI is unseen. | People mark examples as right or wrong. |
| 43 | What is overfitting, and why can an AI ace the practice test and fail? | Draft | Models that look perfect in tests fail in use. | The model memorises examples and misses new ones. |
| 44 | What are scaling laws, and why did bigger AI keep getting better? | Draft | Companies spend billions on bigger models without a clear reason. | Bigger models with more data and compute improved predictably, for a time. |
| 45 | Are emergent abilities real, or does bigger AI just seem to learn new tricks? | Draft | New skills appear suddenly at scale, which is disputed. | Researchers still debate whether the skills appear suddenly or gradually. |
| 46 | What is model collapse, and what happens when AI learns from AI? | Draft | AI-written text floods the web and may be used for training. | Training on AI output again and again can make models worse. |
| 47 | What is quantization, and how does a giant AI fit on a laptop? | Draft | Big models do not fit on small devices. | Store the numbers in less space so the model runs on smaller hardware. |
| 48 | What is a mixture of experts, and why doesn't the whole AI wake up? | Draft | Running a huge model costs too much per word. | Only some specialist parts run for each word. |
| 49 | What is a KV cache, and why doesn't the AI re-read everything? | Draft | Long answers repeat work and slow down. | The KV cache saves earlier work so it is not repeated. |
| 50 | How does prompt caching make repeated prompts cheaper? | Draft | Same prompts are paid for again and again. | Reused prompt starts are billed at a lower rate. |
| 51 | How does speculative decoding make a big AI faster? | Draft | Big models answer slowly. | A small model drafts words and the big model checks them. |
| 52 | What is test-time compute, and why does thinking cost more? | Draft | Thinking models cost more per answer. | Letting the model think longer gives better answers at higher cost. |
| 53 | Why does AI run on a GPU, a gaming chip? | Draft | Chip shortages are in the news, and the reason is unclear. | GPUs do many simple maths steps at once, which AI needs. |
| 54 | What is a TPU, and why did Google build one? | Draft | TPUs are mentioned without explanation. | Google's own AI chip. |
| 55 | What is an NPU, the AI chip inside your new laptop? | Draft | "AI PC" marketing is unclear. | A chip that runs AI tasks efficiently on a laptop or phone. |
| 56 | Can a small language model be good enough? | Draft | Bigger is assumed to be better. | Small models can do focused tasks well at lower cost. |
| 57 | What is on-device AI, and can an AI live on your phone? | Draft | Data may leave the phone for AI. | The model runs on the device, so data stays there. |
| 58 | What is latency, and why does the AI take so long to answer? | Draft | Users say AI is slow without knowing why. | Latency is the wait before an answer, which users feel most. |
| 59 | What is time to first token, and why does the first word matter most? | Draft | The speed number is unclear. | The time until the first word appears. |
| 60 | What is RAG, and how does an AI answer from your documents? | Draft | Models do not know a company's own documents. | Find relevant text first, then let the model answer from it. |
| 61 | Why does AI cut your documents into chunks? | Draft | Whole documents are too big to search and send. | Split them into searchable pieces. |
| 62 | What is a vector database, and where does an AI store meaning? | Draft | "Vector database" sounds like maths. | A database that searches by meaning, using embeddings. |
| 63 | How does semantic search understand what you meant? | Draft | Keyword search misses meaning. | It matches meaning, not only exact words. |
| 64 | What is reranking, and why does AI search look twice? | Draft | The first search results are not always the best. | A second pass reorders results so the best come first. |
| 65 | What is hybrid search, and why use two ways to search? | Draft | Keyword and meaning search each miss some answers. | Combine both to find more of the right text. |
| 66 | What is a knowledge graph, and who is connected to whom? | Draft | Connections between things are hard to query. | A map of things and the links between them. |
| 67 | What is GraphRAG, and how does an AI answer about a whole pile of documents? | Draft | Plain RAG struggles with questions across many documents. | RAG that uses a knowledge graph to connect the documents. |
| 68 | What is grounding, and how do you keep an AI tied to the facts? | Draft | AI answers drift from the sources. | Tie answers to supplied sources. |
| 69 | How do citations show where an AI got its answer? | Draft | Citations may not be real. | Citations point to sources, which still need checking. |
| 70 | Can deep research do your research for you? | Draft | Research takes hours of searching. | Deep research runs many searches and writes a report; check its sources. |
| 71 | What makes an AI agent an "agent"? | Draft | Every product now calls itself an agent. | An agent plans steps and uses tools to reach a goal. |
| 72 | What is an agent harness, and why does every agent need one? | Draft | Agents need safe, controlled surroundings. | The software around the model that runs the agent safely. |
| 73 | What does "agentic AI" really mean? | Draft | "Agentic" is used loosely. | AI that acts on its own across steps. |
| 74 | What is loop engineering, and why is it the next step after prompts? | Draft | Agents loop or stop at the wrong time. | Design the loop: what the agent checks and when it stops. |
| 75 | How does tool calling let an AI check the weather? | Draft | Models cannot reach live data by themselves. | The model asks code to run a tool, then uses the result. |
| 76 | What is MCP, and why is everyone talking about it? | Draft | Every tool needs a custom connection. | Model Context Protocol: a standard way to plug tools into AI apps. |
| 77 | What are agent skills, and why do agents need a playbook? | Draft | Agents lack know-how for specific tasks. | Packaged know-how an agent loads for a task. |
| 78 | What is A2A, and how do AI agents talk to each other? | Draft | Agents from different vendors cannot work together. | A protocol for agents to talk to each other. |
| 79 | Is a multi-agent system better than one AI agent? | Draft | Teams assume more agents are always better. | Several agents help some tasks and add coordination cost to others. |
| 80 | What is a supervisor agent, and who decides which agent does what? | Draft | Many agents need someone to assign work. | A manager agent that hands out tasks. |
| 81 | How does AI memory remember you? | Draft | Chat apps say they "remember" people. | Saved notes or stored records, not the model learning from chats. |
| 82 | What is a checkpoint, and why is it better than starting over? | Draft | A failed long task starts again from zero. | A saved point the agent can resume from. |
| 83 | How does computer use let an AI click like you? | Draft | Many tasks have no API. | The AI looks at the screen and clicks and types. |
| 84 | What's the difference between a copilot and an agent? | Draft | The two words are used interchangeably. | A copilot helps while you work; an agent acts on its own. |
| 85 | What is an agent sandbox, and where should an AI agent work? | Draft | An agent running code could damage real systems. | An isolated space where the agent can run code safely. |
| 86 | What is a reasoning model, and why does the AI think before it answers? | Draft | Quick answers can be wrong on hard questions. | A model that spends extra steps reasoning first. |
| 87 | What is a decision model, and why does it choose instead of chat? | Draft | Chat models write when a choice is needed. | A model built to pick among options. |
| 88 | What is multimodal AI, and how can one AI read, see and listen? | Draft | "Multimodal" is in every launch with no meaning. | One model that handles text, images, audio or video. |
| 89 | How does a diffusion model draw a picture from noise? | Draft | Image generators seem like magic. | Starts from noise and removes it step by step. |
| 90 | How does voice AI talk back without a pause? | Draft | Voice assistants feel slow. | Real-time models listen and speak with little delay. |
| 91 | How does text-to-video make a video from a sentence? | Draft | Video generation sounds impossible. | A model generates video frames from a description. |
| 92 | What is a deepfake, and how can a video of someone be fake? | Draft | Fake videos of real people spread. | AI-made video or audio of someone doing something they did not. |
| 93 | Can voice cloning copy your voice from a few seconds of audio? | Draft | Scams use cloned voices. | Cloning copies a voice from a short sample. |
| 94 | What is an AI avatar, the presenter nobody filmed? | Draft | Presenters in videos may not be real people. | A digital person who speaks on screen, made by AI. |
| 95 | What's a digital twin, and why do factories want one? | Draft | Testing changes in a real factory is risky. | A virtual copy used to test changes. |
| 96 | What does "open" mean in an open-weight model? | Draft | "Open" is used to mean different things. | The weights are published, which is not the same as fully open source. |
| 97 | What is a world model, and can an AI imagine what happens next? | Draft | Robots need to predict what happens next. | A model that predicts how the world changes. |
| 98 | What is embodied AI, and when does AI get a body? | Draft | Humanoid robots are in the news. | AI inside a robot that acts in the physical world. |
| 99 | What is hallucination, and why does an AI sound sure when it's wrong? | Draft | Models make up false content with confidence. | The model produces plausible but false content. |
| 100 | What is AI sycophancy, and why does the AI keep agreeing? | Draft | AI tells people what they want to hear. | The model tends to agree with the user. |
| 101 | What are guardrails, and how do you stop an AI saying the wrong thing? | Draft | Enterprise AI needs limits on what it says. | Checks and limits that screen what goes in and out. |
| 102 | What does "human-in-the-loop" really mean? | Draft | The phrase is used without checking that the human can review. | A person reviews key steps, but only if they can really check. |
| 103 | What is a jailbreak, and how do people trick an AI? | Draft | People share tricks to break AI rules. | Attempts to make the model ignore its rules. |
| 104 | What is prompt injection, and can a web page give orders to your AI? | Draft | Hidden text in content can steer an AI agent. | Treat content the AI reads as data, not instructions. |
| 105 | What is red teaming, and who attacks an AI on purpose? | Draft | Weaknesses are found by users, too late. | Testers attack the model on purpose first. |
| 106 | What are evals, and how do you know an AI is getting better? | Draft | "Evals" is jargon for testing. | Tests that measure quality on a set of tasks. |
| 107 | What is LLM-as-a-judge, and can one AI mark another AI's homework? | Draft | Grading answers by hand does not scale. | One model grades another's answers, with known limits. |
| 108 | What is AI bias, and how does an AI end up unfair? | Draft | AI treats people unfairly by gender, race or region. | Unfair results come from the data or design, and need testing. |
| 109 | What is explainability, and can an AI tell you why it decided? | Draft | Customers and regulators ask why an AI said no. | Show the reasons behind a decision; hard for large models. |
| 110 | What is alignment, and how do you make an AI want what we want? | Draft | Goals of AI systems may differ from people's. | Make AI systems act in line with human goals and values. |
| 111 | Can watermarking tell you if AI wrote this? | Draft | It is hard to know what is AI-made. | Hidden or attached marks show AI origin; not foolproof. |
| 112 | What is AI regulation, and who makes the rules for AI? | Draft | Companies are unsure what AI laws require. | Laws such as the EU AI Act set duties for AI use. |
| 113 | What does "responsible AI" actually involve? | Draft | "Responsible AI" is claimed without detail. | Policies, testing, oversight and records. |
| 114 | What is shadow AI, and is your team using AI you don't know about? | Draft | Staff use AI tools the company has not approved. | Know which tools are in use and offer approved ones. |
| 115 | What is sovereign AI, and why do countries want their own? | Draft | Countries depend on foreign AI providers. | Build national models and data centres for control. |
| 116 | What do benchmarks mean, like "scored 90%"? | Draft | Benchmark scores are quoted without context. | Standard tests, useful but not complete. |
| 117 | What is vibe coding, and can you build an app by describing it? | Draft | Apps are built without anyone reading the code. | Describe the app to an AI; this works best for simple tools. |
| 118 | What is AI slop, and why is the internet filling up with it? | Draft | Low-quality AI content floods feeds and search. | Name the problem so people can spot and avoid it. |
| 119 | What is AI washing, and how do you spot it? | Draft | "AI-powered" is claimed for products with little AI. | Check what the AI actually does. |
| 120 | What is GEO, and how do you get found when people ask AI? | Draft | Websites are not written for AI answers. | Make content easy for AI answers to use. |
| 121 | What makes a company "AI-native"? | Draft | "AI-native" is used without meaning. | A company built around AI from the start. |
| 122 | What is LLMOps, and who keeps an AI running after launch? | Draft | Demos work but production AI breaks. | Daily running, monitoring and updates of AI in production. |
| 123 | What is observability, and why can't you debug an AI without it? | Draft | AI failures are hard to find without visibility. | Logs, traces and metrics that show what the system did. |
| 124 | What is an AI gateway, the front door to your AI? | Draft | Many teams call many AI providers with no control. | One controlled entry point with rules and logs. |
| 125 | What is model routing, and should every question go to the biggest AI? | Draft | AI bills grow when every question uses the biggest model. | Send each question to the right-sized model. |
| 126 | Your AI dictionary, one line per word | Draft | Series terms are scattered across write-ups. | Finale: one line for every term. |

## Retired files (not part of any series)

| File | Status | Problem | Solution |
|---|---|---|---|
| `_retired/02-users-will-love-the-chatbot/01-first-10-seconds.md` | Retired | Chatbots lose trust in the first 10 seconds. | Design the first answer carefully. |
| `_retired/07-llm-output-to-json/01-curtain-raiser.md` | Retired | A "perfect" JSON profile breaks one time in fifty. | Validate structured output. |
| `_retired/14-connect-agent-to-tools/01-curtain-raiser.md` | Retired | Agents may be allowed to give money back without limits. | Limit what tools can do. |
| `_retired/14-lets-make-it-agentic/01-curtain-raiser.md` | Retired | "Make it agentic" is vague. | Define what makes an AI an agent. |
| `22-claude-architect-exam/_retired/01-agentic-loops-long-parentpace.md` | Retired | Long ParentPace version of objective 1.1. | Replaced by the store version. |
