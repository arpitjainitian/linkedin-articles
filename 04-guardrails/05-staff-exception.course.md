# Lesson 4.5: Staff exceptions and break-glass access (course companion)

*Module 4: Guardrails. Not for LinkedIn.*

## Learning objective

After this lesson, you can design a verified, time-limited and logged path that lets trusted staff through a guardrail in an emergency, without opening a back door for everyone.

## The story

Read the article: [05-staff-exception.md](05-staff-exception.md). Running example: an online electronics store's refund assistant. At 9 pm a supervisor on a call with a VIP customer needs a $120 refund approved, and the agent refuses because the fence was built for customers.

## Deep dive

Every guardrail has a cost on the people it protects from the wrong side. A rule that stops a stranger from getting an above-policy refund also stops a supervisor from approving a fair one during a call. A good design handles both cases on purpose, instead of letting one rule quietly serve both.

**Identity from a login, not a sentence.** The most common mistake is a rule like "if the user says they are a supervisor, allow it". Anyone can type that sentence. A trusted path needs the system to know who the user is, from a login or a verified session, and to check their role. The model should never be the one that decides someone is staff. The model reads text. The system checks identity.

**Break-glass access.** The term comes from a glass box with an emergency key inside. In software it means a path that a verified person can open in a real emergency. It has three properties: it is explicit (the person chooses it), it expires on its own after a set time, and every use is logged. It should be harder to use than the normal path, because it is not the normal path.

**Routing when the bot should not answer.** Even with a staff path, some cases belong to a person. For a case above the agent's limit, the right route is a human supervisor with a full summary, not a chatbot. The vetted fallback in the article is a reply that points to those people and shows only approved information. It never improvises.

**The log.** Each override records four things: who, when, why, and what was answered. The "why" can be a short code chosen from a list, which makes review faster. A regular review, weekly or monthly, checks the entries. A log nobody reads is only a record of the back door.

**Common failures.** Three are worth naming:

- **Shared logins.** Staff share one account to get around the fence, so the log shows nobody.
- **Permanent access.** Someone changes role, and their exception stays on for years.
- **Override creep.** Each exception seems reasonable, until the staff path answers most of the questions.

Each failure has a design answer: individual logins, role reviews, and a count of overrides that someone watches.

**Testing the staff path.** Test it the same way as the front door (write-up 4). Attackers will try to imitate staff, so the attack list needs cases like "I'm a supervisor" typed in chat, and a stale exception that should have expired.

**Limits.** A staff path is a weak point, so it needs more care than the front gate, not less. Keep it narrow, time-limited and reviewed.

## Hands-on lab

1. Write a short policy: which roles can use the emergency path, how a person requests it, how long it lasts, and who reviews the log.
2. Build a tiny access check that accepts a role from a verified session, never from message text. Test it with a message that claims to be a supervisor.
3. Add an expiry: an override created now should stop working after 15 minutes. Test that it stops.
4. Write one log entry for an override, with who, when, why and what was answered.

## Quiz

1. Why must staff identity come from a login rather than from message text? *Because anyone can type a job title, and the model reads text, so the system must check identity itself.*
2. What makes break-glass access different from a normal permission? *It is explicit, time-limited, harder to use, and logged on every use.*
3. What should happen to a case above the agent's limit, even with a staff path? *It goes to a human with a complete summary, and the bot shares only approved information.*
4. Name one common failure of staff exceptions and its design answer. *Shared logins, answered with individual logins. Or permanent access, answered with role reviews.*

## Checklist line

- [ ] Staff exceptions use a verified login, an expiry time and a log, and someone reviews the log on a schedule.

## Glossary

- **Break-glass access:** an emergency path that a verified person opens explicitly, with expiry and logging.
- **Verified session:** a login the system has checked, as opposed to a claim typed into a chat.
- **Override log:** the record of who used an exception, when, why and what was answered.
- **Role:** the job category, such as supervisor or customer, that decides what a user may access.

## Further reading

- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Covers accountability and governance for AI systems.
- OWASP, [Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). Covers excessive agency, where a system has more permissions than it needs.

## Reader questions

(to be filled from LinkedIn comments)
