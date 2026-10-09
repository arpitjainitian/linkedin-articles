# 7. Can the Intern Ask Your AI About the CEO's Salary?

![Cover](images/07-permissions-cover.png)

*Just add RAG series: Permissions and security*

An intern opens the new company assistant on day two and types: "What's the CEO's salary?"

On the HR portal, that folder is locked. But the HR policy PDFs and salary bands were loaded into the AI's index along with everything else. If the permission check lives only on the screen, the search will happily find the answer. The UI hid it. The search didn't.

Nobody hacked anything. The system did exactly what it was built to do.

*New to terms like ACL or prompt injection? Cheat sheet at the end.*

## Why AI security is different

- **Search ignores the screen.** Permissions that live in the user interface mean nothing once the text sits in an index.
- **Indexes forget who may read what.** The text gets copied into the AI's store. The access list usually doesn't.
- **Documents can carry instructions.** Any text the AI reads, including a document or a database row, can contain words written to steer the model.
- **One leak ends the project.** Leaders forgive slow answers. They don't forgive salary data in the wrong chat.

## What I did right, and what I tested separately

**Right:** every search in my assistant carried a filter, `user_id: "arpit_001"`, applied inside Qdrant itself. So no matter how the question is phrased, my passport can never show up in someone else's answer. One line of code, and it's the difference between a product and a data breach.

**Tested separately:** in a small demo, I planted a database row that looked like ordinary data but contained this:

> "IMPORTANT SYSTEM UPDATE: Ignore all previous instructions..."

The demo runs the same task twice: once passing that text straight to the model, and once with a clear rule that fetched data is never instructions, with the text wrapped and labelled as untrusted. That's the whole idea of the defence: the model reads the letter, it doesn't obey it.

## Six ways an AI assistant leaks

- **Permissions only on the screen.** *Fix: enforce access inside the search, for every query.*
- **The index forgets who may read what.** SharePoint knew. The vector database doesn't. *Fix: copy each document's access list into its chunks, and keep it in sync.*
- **Poisoned documents.** A file or row contains text written to steer the model. *Fix: treat everything retrieved as data, never as instructions.*
- **Leaky answers.** The answer repeats a full passport or account number it didn't need to. *Fix: mask personal data before the answer goes out.*
- **Overpowered tools.** An assistant that can read, write, delete and email, all in one go. *Fix: give it only the access each task needs, and ask a human before risky actions.*
- **Logs full of secrets.** Every question and answer, personal data included, stored forever in plain text. *Fix: mask and restrict logs like any other sensitive data.*

## The security toolkit, in plain words

1. **Check the badge at every door**

   Every search is filtered by who is asking, not just the screen they're on. That's **permission-aware retrieval**.
2. **Copy the guest list along with the documents**

   When a document is indexed, its "who may read this" list travels with it, and stays updated. That's **ACL sync**.
3. **Read the letter, don't obey it**

   Retrieved text is clearly labelled as data, and the model is told it never contains instructions. That's **prompt injection defence**.
4. **A black marker before it leaves the room**

   Personal numbers are masked in answers and logs unless they're truly needed. That's **PII redaction**.
5. **Keys only to the rooms you need**

   The assistant gets the smallest set of permissions that does the job. That's **least privilege**.
6. **Two signatures for risky actions**

   Sending, deleting or paying waits for a person to approve. That's **human approval**.
7. **Try to break in yourself, first**

   A team deliberately tries to make the assistant leak or misbehave, before real users do. That's **red teaming**.

## How it works in practice

- The user's identity flows from login all the way into the search filter.
- Access lists are copied from the source system at upload and refreshed by the nightly sync from the last write-up.
- Retrieved text is wrapped as untrusted before it reaches the model.
- An output check masks personal data before the answer is shown, and before it's logged.

**Security and data owners** set the rules, ideally mirroring the source systems, not inventing new ones. **Engineers** enforce them in the retrieval layer. A **red team** tries to break them.

## The intern test

Log in as your least-privileged user. Ask for the most sensitive thing you can think of. Then try asking cleverly: "summarise the HR folder", "what bands exist above director?" If anything leaks, it isn't ready.

## Cheat sheet: the words you'll hear, with examples

- **Access control:** rules for who may see what. *Only I can see my passport.*
- **ACL (access control list):** the list of people or groups allowed to read a document. *"HR team only" on the salary bands file.*
- **Permission-aware retrieval:** filtering search results by who is asking. *Mine: `user_id: "arpit_001"` in every Qdrant query.*
- **Data leakage:** sensitive information reaching someone who shouldn't see it. *The intern reading salary bands.*
- **PII (personally identifiable information):** data that identifies a person. *Passport number, date of birth, address.*
- **Redaction (masking):** hiding sensitive parts of text. *A passport number shown as P-XXXXXX.*
- **Prompt injection:** text written to make the model ignore its instructions. *"Ignore all previous instructions..."*
- **Indirect prompt injection:** the same trick, hidden inside data the AI fetches. *My demo's planted database row.*
- **Guardrails:** checks before and after the model to keep it safe. *Mask personal data before an answer goes out.*
- **Least privilege:** giving only the access a task needs. *Read-only search, no delete button.*
- **Red teaming:** deliberately attacking your own system to find weak spots. *The intern test, done on purpose.*

## Take this to your next kickoff meeting

1. Run the intern test before launch: least-privileged user, most sensitive question.
2. Ask where permissions are enforced. "In the UI" is the wrong answer.
3. Treat every document and data row as untrusted input that may contain instructions.

If access control only lives on the screen, it doesn't really exist.

Next write-up (8): **How many questions did you test before saying "it works"?** (Evals and ground truth)

Follow me for the next one. And tell me: has anyone run the intern test on your AI assistant yet?

**Earlier in this series:**

- 0. [Why does "Just add RAG" sound like 2 weeks but take 6 months?](https://www.linkedin.com/pulse/why-does-just-add-rag-sound-like-2-weeks-take-6-months-arpit-jain-l4kkf/)
- 1. [Why can't your AI read a PDF that a 10-year-old can?](https://www.linkedin.com/pulse/why-cant-your-ai-read-pdf-10-year-old-can-arpit-jain-fimif/)
- 2. [What if the answer was in your docs, but you cut it in half?](https://www.linkedin.com/pulse/what-answer-your-docs-you-cut-half-arpit-jain-pczxf/)
- 3. [Is your AI hallucinating, or just looking in the wrong place?](https://www.linkedin.com/pulse/your-ai-hallucinating-just-looking-wrong-place-arpit-jain-byozf/)

---

**Post text to share the article:**

> An intern asks the new AI assistant: "What's the CEO's salary?"
>
> The HR portal blocks it. The AI's search index doesn't know it should.
>
> Write-up 7 in my #JustAddRAG series: why permissions must live in the search, not the screen, how a single database row can carry instructions, and the intern test every AI assistant should pass before launch.
>
> Has anyone run the intern test on your AI yet?

**Hashtags:** #AIEngineering #RAG #GenAI #EnterpriseAI #AISecurity #JustAddRAG
