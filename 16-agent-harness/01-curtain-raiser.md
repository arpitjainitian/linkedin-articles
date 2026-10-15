# 1. You Bought a Brilliant Model. Where's the System?

![Cover](images/01-curtain-raiser-cover.png)

*We bought the brain, we're done series: the curtain raiser*

"The vendor ships the model, so we're done."

Picture an insurance company buying access to one of the best AI models available. In a demo, it reads a motor claim (photos, the repair estimate, the policy document) and explains, in perfect English, whether the claim looks covered and what's missing. The room is impressed. The model is genuinely brilliant.

The project plan says: connect the model, launch in a month.

Then the questions start. What stops it approving a 20-lakh claim on its own? What happens if the server restarts halfway through a three-day claim? Where does the team try it out without touching real payouts? Does the model even see the exclusion clause on page 14? And what happens when five small gaps line up on the same Friday?

The vendor sold an engine. Nobody ordered the car.

## Why the model isn't the system

A model is the brain: it reads, reasons and writes. Everything that turns that brain into a dependable claims process is built around it, and it's yours to build. Engineers call that surrounding system the **harness**.

- **Someone has to steer.** The model can suggest a next step. Code has to decide the order: read the claim, check the policy, request documents, approve or escalate.
- **Brakes are not optional.** Limits on amounts, and checks before money moves.
- **It has to remember where it was.** A claim takes days. If the server restarts, the agent must carry on, not start again or pay twice.
- **It needs a test track.** Practise on copies of claims, never on real payouts, and keep backups away from the system they protect.
- **It only knows what it's shown.** If the policy is cut off before the exclusion clause, the model decides without it.
- **Small gaps add up.** Broad access, no confirmation, backups in the same place: each one survivable alone, a disaster together.

The vendor supplies a world-class engine. The brakes, sat nav, windscreen, test track and crumple zones are all on your side of the parts list.

## What sits behind "we bought the model"

The model is the visible part, and the part with the press release. What makes an AI agent production-ready is the harness: keeping its place across days, a safe place to practise, control over what the model sees, and layers so that one small gap never becomes a crash. The blueprint on the cover shows which parts arrive in the box, and which don't.

## This is a series: here's what's coming

This write-up is the first in a series. Each one takes one part of the harness and goes deep, with the same claims-processing agent every time. A few of the questions it will answer:

- Where does the agent keep its place? (State and checkpoints)
- Where does it practise before touching real claims? (Sandboxes and staging)
- What does the model actually see? (Context engineering)
- What happens when five small gaps line up? (Incidents as chains)

...and a final write-up with a harness checklist.

## Take this to your next kickoff meeting

1. Draw the whole claims process on one page, and circle the parts the model doesn't do.
2. Run the agent on copies of real claims, in a separate system, before the first real payout.
3. Ask what happens if the server restarts halfway through a claim.

You can buy a brilliant brain. You still have to build the body it lives in.

Next write-up (2): **Where does the agent keep its place?** (State and checkpoints)

Follow me for the next one. And tell me: what share of your last AI project was the model, and what share was everything around it?

---

**Post text (copy and paste):**

```
"The vendor ships the model, so we're done."

The model reads an insurance claim perfectly. Then: what stops a 20-lakh approval? What if the server restarts mid-claim? Does the model even see the exclusion clause?

Treat the model as the whole system, and you pay for it:
• Risk: decisions with no brakes and no human check
• Reliability: claims restarted from scratch, or paid twice
• Accuracy: decisions made without the clause that mattered
• Safety: tests that touch real payouts

Write-up 1 in my new series, We bought the brain, we're done (#BrainNotBody): why the model isn't the system, what the harness around it does, and three things to take to your next kickoff meeting.

What share of your last AI project was the model, and what share was everything around it?

#AIEngineering #GenAI #AIAgents #InsurTech #BrainNotBody
```

**Series index (post as the first comment, then pin it):**

```
📌 We bought the brain, we're done: series index

1. You bought a brilliant model. Where's the system? (you're here)
2. Where does the agent keep its place? (next write-up)

I'll keep this comment updated with each link as it goes live.
```
