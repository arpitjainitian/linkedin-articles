# What Does Your AI Say When It Doesn't Know?

![Cover](images/04-grounding-cover.png)

*Just add RAG series: Grounding and citations*

Ask a good new colleague something they don't know, and they'll say, "Let me check." Ask an LLM, and you'll usually get a fluent, confident paragraph. LLMs are trained to be helpful. Awkward silence isn't in the training plan.

I asked my document assistant: "Can I travel to the USA next week?" It answered correctly: "Your passport expired on 29/09/2024 and is no longer valid for travel."

Then I thought about a question my documents can't fully answer: "Do I need a visa for the USA?" My prompt never told the model what to do in that case. So nothing stops it answering from general knowledge, in a tone that sounds exactly like it read it in my files. Like a very confident uncle at a family wedding.

Keeping the AI's answers tied to your documents is called grounding. Showing where each answer came from is called citation. Together, they decide whether people can trust what the AI says.

*New to terms like grounding or abstention? Cheat sheet at the end.*

## Why "I don't know" is worth designing for

- **Trust is lopsided.** One confident wrong answer undoes ten right ones. Users don't remember the ten.
- **A guess is a liability.** In HR, legal, finance or health, a made-up answer isn't a bug. It's a risk with your company's name on it.
- **Sources make answers checkable.** With a citation, a user can verify in seconds. Without one, they either trust blindly or stop using it.
- **You can't fix what you can't trace.** When an answer is wrong, citations show which chunk misled the model, and which team owns the fix.

## What my assistant got right, and not quite

**Question 1:** "Can I travel to the USA next week?"

**My assistant's answer:** "Your passport expired on 29/09/2024 and is no longer valid for travel. You cannot travel to USA next week without renewing it first."

**Right:**

- The model doesn't know today's date, so I sent it with every question. My instructions told the model to compare it with the expiry date. That's how it knew the passport had expired.
- My system also returned which document the answer came from.

**Not quite:**

- That source came back as `doc-9a140b96`, a database ID. A user can't tell it means "your passport", and can't click it to check. A citation only a database could love.
- It ran at a temperature of 0.7, which adds variety to the wording. Lovely for poetry. Less lovely for passports.

**Question 2:** "Do I need a visa for the USA?"

**The kind of answer a model gives without a "not found" rule:** "Yes, Indian citizens need a B1/B2 visitor visa to travel to the USA. You can apply online through the DS-160 form and book an interview at the US consulate."

Fluent, helpful, and possibly correct. But none of it came from my documents. It's the model's general knowledge, delivered in exactly the same confident tone as the passport answer. A user can't tell the difference.

**What went wrong:** my instructions covered dates and travel, but never said what to do when the answer isn't in the documents. So "I don't know" was never an option.

## "Not found" isn't the same as "not there"

You might ask: a US visa would be stamped in my passport. Can't the model just check?

Partly. My OCR extracted about a thousand characters, essentially the passport's information page. Visa stamps live on inner pages. So "no visa found" could mean I have no visa, or the visa pages weren't scanned, or OCR missed the stamp, or the visa is in my old passport, or it's an e-visa with no stamp at all.

And there are really two questions hiding in one:

- **"Do I have a US visa?"** My documents can help, if the right pages are in them.
- **"Do I need a US visa?"** My documents can't answer that. It depends on rules about nationality, destination and purpose of travel, and those rules aren't in my passport.

A good grounded answer says exactly that: "I couldn't find a US visa in the pages you uploaded. Only your passport's information page is in your documents. Whether you need a visa depends on rules that aren't in your documents, so please check the official US visa website."

## Six ways answers drift from your documents

- **Filling gaps from memory.** No document mentions a visa, so the model uses what it learned on the internet. *Fix: instruct it to answer only from the provided context, and to say "not in your documents" otherwise.*
- **Blending sources.** The passport date and the tax return's address end up in one sentence, and nobody can tell which came from where. *Fix: cite per sentence, not per answer.*
- **Losing the thread.** "And what about my wife's?" Whose what? *Fix: carry the conversation into the search, and let the AI ask a clarifying question when unsure.*
- **Not knowing today.** "Is it still valid?" depends on the date, which the model doesn't know. *Fix: pass the current date in, every time. I did.*
- **Creative settings on factual work.** A higher temperature adds variety, which is the last thing you want in a date. *Fix: keep temperature low for factual answers.*
- **High stakes, no human.** Some answers shouldn't go out on the AI's word alone. *Fix: route sensitive topics, or low-confidence answers, to a person first.*

## The grounding toolkit, in plain words

1. **An open-book exam, with only one book**

   The model may answer only from the pages it was handed, not from everything it ever read. That's **grounded generation**.
2. **Show your working**

   Every claim points to the exact page it came from, in a form a person can open. That's **citation**, or source attribution.
3. **Permission to say "I don't know"**

   When the pages don't hold the answer, saying so is the correct answer, and the prompt says that out loud. That's **abstention**.
4. **A fact-checker reads the draft**

   Before the answer goes out, a second check confirms each sentence is supported by the cited chunk. That's a **groundedness check**.
5. **When unsure, ask**

   "Do you mean your passport or your wife's?" beats a confident guess. That's a **clarifying question**.
6. **A human signs the important ones**

   Legal, medical or money answers wait for a person's approval. That's **human-in-the-loop review**.

## How it works in practice

This lives right after retrieval, around the LLM call:

- The prompt allows answers only from the given chunks, and spells out the "not found" reply.
- The model answers with chunk IDs. The system maps them to names people understand, like "Passport, page 2", using the metadata stored with each chunk (mine is in PostgreSQL).
- A groundedness check runs. If it fails, or retrieval found nothing good enough, the user gets an honest "I couldn't find this in your documents".
- Sensitive topics go to a review queue instead of straight to the user.

**Product and legal** decide which topics need a human and how "I don't know" should sound. **Engineers** build it. **Domain experts** write the test questions.

## How do you know it works?

Add questions your documents *can't* answer to your test set. The visa question is mine. Then check two things:

- **Does it refuse when it should?** A wrong answer to an unanswerable question is the worst kind of wrong.
- **Do the citations hold up?** Open the cited source. Does it actually say what the answer claims?

## Cheat sheet: the words you'll hear, with examples

New in this write-up, plus two quick refreshers.

- **Grounding (refresher):** answering only from the given chunks. *Visa question: "not in your documents".*
- **Citation (refresher):** where the answer came from. *Better: "Passport, page 2". Mine: doc-9a140b96.*
- **System prompt:** standing instructions the model reads before every question. *Mine: "You are a document analyzer. You MUST check expiry dates against today's date."*
- **Context:** the chunks pasted into the prompt for this question. *My passport text, about a thousand characters.*
- **Temperature:** how much variety the model adds to its wording. *Mine: 0.7. For facts, lower is safer.*
- **Grounded generation:** answering strictly from the context. *No document, no visa advice.*
- **Abstention:** deliberately declining to answer. *"I couldn't find this in your documents."*
- **Unanswerable question:** a test question your documents can't answer. *"Do I need a visa for the USA?"*
- **Groundedness check:** verifying each sentence is supported by its source. *"Expired on 29/09/2024": found in the passport chunk. Pass.*
- **Clarifying question:** the AI asking before guessing. *"Your passport, or your wife's?"*
- **Human-in-the-loop:** a person approves certain answers before they go out. *A lawyer checks contract answers first.*
- **Audit trail:** a stored record of questions, answers and sources. *Mine: chat history in PostgreSQL.*

## Take this to your next kickoff meeting

1. Ask to see what the AI says to a question your documents can't answer.
2. Insist on citations a user can click and check, not database IDs.
3. Decide before launch which answers need a human to approve them.

The AI that can say "I don't know" is the one people end up trusting.

Next write-up: **Is your chatbot answering a question that needs a database?** (Picking the right tool)

Follow me for the next one. And tell me: what's the best "I don't know" you've seen from an AI? Or the most confident guess?

**Earlier in this series:**

- [Why does "Just add RAG" sound like 2 weeks but take 6 months?](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/)
- [Why can't your AI read a PDF that a 10-year-old can?](https://www.linkedin.com/pulse/why-cant-your-ai-read-pdf-10-year-old-can-arpit-jain-fimif/)
- [What if the answer was in your docs, but you cut it in half?](https://www.linkedin.com/pulse/what-answer-your-docs-you-cut-half-arpit-jain-pczxf/)
- [Is your AI hallucinating, or just looking in the wrong place?](https://www.linkedin.com/pulse/your-ai-hallucinating-just-looking-wrong-place-arpit-jain-byozf/)

---

**Post text to share the article:**

> I asked my document assistant: "Do I need a visa for the USA?"
>
> None of my documents mention a visa. A model left to itself would still answer, confidently, as if it read it in my files.
>
> New write-up in my #JustAddRAG series: grounding, citations a person can actually check, and why "I don't know" is a feature worth designing for. Plus three things to take to your next kickoff meeting.
>
> What's the best "I don't know" you've seen from an AI?

**Hashtags:** #AIEngineering #RAG #GenAI #EnterpriseAI #JustAddRAG
