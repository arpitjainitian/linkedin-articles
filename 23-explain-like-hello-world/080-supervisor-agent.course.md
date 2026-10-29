# Lesson 23.80: Supervisor agent (course companion)

*Explain It Like Hello World. Not for LinkedIn.*

## Learning objective

After this lesson, you can explain supervisor agent with a hello-world example, say how it really works in one step, and name its most common misunderstanding.

## The hello world, to retell

A film set has a director. The director doesn't hold the camera or do the lighting. They decide who does what, when, and whether the take is good.

## One step further

The supervisor reads the request, picks which specialist should handle each part (a search agent, a coding agent, a booking agent), passes them the right context, and collects what they return. It can ask for a retry or stop the team when the work goes off track.

The risk is a supervisor that becomes a bottleneck or misroutes work. Clear roles, limits on how many agents it can start, and logs of every handoff keep the team under control.

## Exercise

Explain supervisor agent to someone non-technical in under one minute, using your own everyday example (not the one from the article). Then name one product where they have already met it.

## Quiz

1. What is the hello-world example for supervisor agent? *A supervisor agent is the manager that routes work to specialist agents.*
2. What is it not? *A supervisor agent isn't automatically smarter. More agents mean more handoffs, more cost and more places for things to go wrong. Use one only when a single agent struggles.*
3. Name one place you've already met it. *Research assistants that split a question across several agents, and travel bots that hand flights and hotels to different agents.*

## Glossary

- **Supervisor:** the agent that routes and checks the work.
- **Specialist agent:** an agent built for one kind of job.
- **Handoff:** passing a task and its context to another agent.

## Further reading

- The series plan: [README.md](README.md).
