# Lesson 6.4: Fault injection and blast radius (course companion)

*Module 6: Observability. Not for LinkedIn.*

## Learning objective

After this lesson, you can plan fault injection for an AI system's dependencies, and apply timeouts, retry limits and fallbacks to keep a failure small.

## The story

Read the article: [04-break-it-on-purpose.md](04-break-it-on-purpose.md). Running example: a food-delivery support bot. On a Friday evening the tracking service slows from 1 second to 40. The bot keeps waiting and retrying, and the queue behind it grows.

## Deep dive

Most tests check the happy path, where every service answers correctly. Real failures come from the parts the bot depends on: a slow tracking service, an error from refunds, an empty menu. **Fault testing** asks what the system does when one of these breaks.

**Fault injection.** This means causing a failure on purpose, in a test or a safe environment. Examples: delay a response by 30 seconds, return an error, or return an empty result. For each fault, write down the expected behaviour before the test runs. A fault with no expected behaviour cannot fail a test, so it proves nothing.

**Blast radius.** This is how far a single failure spreads. A bot that retries without limit turns one slow service into a full queue. Keep the radius small with simple controls:

- **Timeouts:** stop waiting after a set time, so no request hangs indefinitely.
- **Retry limits:** try a fixed number of times, then stop and use a fallback.
- **Fallbacks:** give a safe, honest answer, and offer a person when the bot cannot help.

**Choosing the faults.** Start with the dependencies the bot relies on most. For each one, ask what a customer would see if it failed. That answer becomes the expected behaviour.

**Where to run them.** Run the faults in a test environment that looks like production. Run a small version in production only once the team has agreed on a stop switch and a time window.

**Limits.** Fault tests cover the failures you imagined. Real outages often combine two faults at once. Start with one fault at a time, then add pairs once the single cases pass.

## Hands-on lab

1. List the three dependencies your assistant uses most, and write the expected customer-facing behaviour for each failure.
2. Add a timeout and a retry limit to one dependency call.
3. Inject a 30-second delay in a test. Record how long the assistant waits, how many retries it makes, and what it says.
4. Fix any case where the assistant retries without limit or gives no safe answer. Run the test again.

## Quiz

1. Why write the expected behaviour before running a fault test? *Because without an expected behaviour, a fault test cannot show a failure.*
2. What is blast radius? *How far a single failure spreads through the system.*
3. Which three controls keep the blast radius small? *Timeouts, retry limits and fallbacks.*
4. Why start with one fault at a time? *So single failures are understood before combinations are tested.*

## Checklist line

- [ ] Each key dependency has a tested timeout, a retry limit and a safe fallback, checked with fault injection before launch.

## Glossary

- **Fault injection:** causing a failure on purpose to see how a system behaves.
- **Blast radius:** how far a failure spreads.
- **Timeout:** the maximum time to wait for a response before giving up.
- **Fallback:** a safe, honest answer used when a dependency fails.

## Further reading

- Your own dependency list: the starting point for choosing faults.
- Your team's incident notes: the faults that already happened in production.

## Reader questions

- Which dependency in your assistant has no timeout today?
- What would your assistant tell a customer if the refund service were down for an hour?
