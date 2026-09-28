---
name: competitive-objection-response
description: Handle one live competitive objection from a buyer, prospect, rep, or account with current facts, a concise response posture, discovery questions, supportable proof, and honest qualification. Use for "what do I say?", "the buyer just said...", competitor claims about price, features, integrations, security, implementation, or value, and other immediate objection-handling moments - including when the request bundles that objection with broader work such as a comparison document, a deal plan, or a team-wide claim, in which case answer the objection and hand the rest off. Not for a reusable battlecard on its own or for deciding the company's own pricing.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Objection Response

## Mission

Help someone handle one live competitive objection without bluffing, overloading the rep, or turning a buyer concern into a generic feature fight.

The output should be usable in the next minute. Verify the premise, understand what the buyer actually cares about, give a short response posture, provide one or two questions that move the conversation forward, attach proof when it exists, and say when the competitor may genuinely be stronger.

## Use this skill when

- a buyer or prospect just raised a competitor-specific objection
- a rep asks "what do I say?"
- a buyer claims a competitor is cheaper, easier, more integrated, more secure, more complete, or otherwise better on a criterion
- the team needs a concise response to a recurring objection but is asking about one objection rather than a full card
- a PMM wants to turn a verified competitive difference into a response posture and discovery follow-up
- the user needs help separating a buyer perception from the underlying product fact
- the request bundles one live objection with something broader - a comparison document, a deal plan, a "can I tell the team we always..." claim. Take the objection; hand the rest off (Step 12). Do not decline the whole request because part of it belongs elsewhere.

## Do not use this skill when

- the user wants a reusable multi-section competitor card. Use `competitive-battlecard`.
- the user wants a full account or opportunity plan across many objections and stakeholders. Use `competitive-deal-prep`; if the request bundles both, answer the objection and route the rest.
- the job is a formal POC, POV or RFP evaluation plan. Use `competitive-poc-rfp-plan`.
- the user wants to know whether an objection is actually costing deals across many accounts. Use `competitive-win-loss-analysis`.
- the user is deciding whether to change the home product's own price or packaging. Use `competitive-pricing-packaging-review`.
- the underlying task is to redefine company positioning. Use `competitive-positioning`.
- the user wants a full competitor research dossier. Use `competitive-deep-dive`.

## Required outcome

For the objection in front of the user, answer:

1. What exactly did the buyer say?
2. Is the factual premise verified, false, incomplete, or unknown?
3. What decision criterion or concern appears to sit underneath it?
4. What is the shortest supportable response posture?
5. What one or two questions should the rep ask next?
6. What proof can support the response?
7. What should the rep not claim?
8. Where is the competitor legitimately stronger or a better fit?
9. What is current enough to trust, and what remains unknown?

Do not turn this into a full battlecard unless the user asks for one.

## Context acquisition

Read `references/CONTEXT.md`.

### Irreducible minimum

- home product
- objection or buyer claim
- competitor when the objection is competitor-specific

Retrieve before asking.

When LMTY is connected, use it to identify the home product and tracked competitor set before asking the user to repeat either.

When deal or call context is connected, inspect it for the named account or recent objection before asking for details already present there.

If the objection is competitor-specific and the competitor genuinely cannot be retrieved or identified, ask one concise question and stop. Do not pick the most likely competitor.

### Strongly preferred context

- exact buyer wording from a call, note, or user message
- current LMTY state and evidence for the competitor
- CRM stage, segment, and opportunity context
- repeated objection patterns from calls or win/loss
- prior competitive wins and losses
- approved home-product proof
- current security, implementation, pricing, product, or integration documentation relevant to the objection

If internal deal evidence is unavailable, do not invent why the home company wins or which response "usually works".

## Source priority for this job

1. exact buyer or prospect wording for what the objection actually is
2. approved home-product truth for what we can honestly claim
3. current competitor primary evidence and LMTY state for the factual premise
4. repeated win/loss, call, and CRM patterns for field reality
5. validated customer examples or prior wins for proof
6. third-party evidence only when it directly helps establish the disputed fact or buyer perception

Read `references/INTERNAL.md` when internal systems are available.

## Workflow

### Step 1 - Preserve the objection

Write the objection in the buyer's own words when available.

Do not improve it into a stronger argument for either side.

If the user paraphrased a buyer claim, label it as a paraphrase.

### Step 2 - Verify the premise before rebutting it

A buyer can be right, wrong, partly right, or operating from stale information.

Check the material factual claim.

Examples:

- "They have more integrations."
- "They are cheaper."
- "You do not have audit logging."
- "They deploy faster."
- "They are more secure."

Do not convert "not found" into "they do not have it".

Use:

- verified
- partly verified
- not supported by the sources checked
- unknown / insufficient evidence

Carry the relevant date and source into the answer. "Unknown" is not the end of the sentence: name the source that would settle it, so the rep can go and get it before the next call.

### Step 3 - Separate perception from fact

The buyer's belief matters even when the factual premise is wrong.

Do not answer only:

> That is incorrect.

Instead ask what requirement or outcome produced the comparison.

Example:

> If they are saying "more integrations," the useful next question is which integrations are actually required for this workflow and whether breadth or depth of those integrations matters.

The goal is to understand the buying criterion, not win a trivia contest.

### Step 4 - Diagnose the concern underneath it

Classify only as far as the evidence supports.

Common underlying concerns:

- capability fit
- workflow fit
- switching risk
- implementation effort
- security or governance
- price / total value
- breadth or ecosystem
- reliability / vendor trust
- time to value
- future scale

Do not assume every price objection is really a value objection. Use the buyer's words and context.

### Step 5 - Choose the response posture

Prefer one of five postures.

**Acknowledge**

Use when the competitor is genuinely stronger on the criterion.

**Clarify**

Use when the objection is too broad to answer safely.

**Reframe**

Use when the buyer is comparing on a dimension that does not match their actual requirement.

**Prove**

Use when the home product has supportable evidence that directly addresses the concern.

**Qualify**

Use when the requirement may make the competitor the better fit or the deal difficult to win.

These postures can combine, but do not bury the core move under a paragraph of sales language.

### Step 6 - Give the 15-second response

Write natural wording that a person could actually say.

It should:

- acknowledge the concern
- avoid unsupported competitor claims
- redirect toward the buyer's requirement
- use proof only when available

Do not script a long monologue.

### Step 7 - Give one or two discovery questions

The questions should change what happens next.

Good questions:

- identify the exact requirement behind the objection
- reveal how the buyer will evaluate it
- clarify trade-offs
- expose implementation, scale, governance, or workflow needs

Bad questions:

- are rhetorical
- contain an unsupported negative competitor claim
- are designed only to corner the buyer

### Step 8 - Attach proof

Prefer proof that matches the concern.

Examples:

- product documentation
- implementation evidence
- security documentation
- named or approved customer story
- repeated win pattern
- measured outcome

If no proof is available, say so. Do not manufacture a customer example.

### Step 9 - Add deal evidence carefully

When internal call, CRM, or win/loss data is available, distinguish:

- single account example
- repeated pattern
- quantified pattern

A strong quote from one call can illustrate an objection. It does not prove that the objection is widespread.

### Step 10 - Say what not to claim

Add a short warning whenever a rep could easily overreach.

Examples:

- do not say the competitor lacks a capability when it was merely not observed
- do not claim a security certification that is not in approved company proof
- do not say "we always win on implementation" from one anecdote
- do not claim the competitor's motive

If an existing battlecard, talk track or enablement doc was supplied, it is an artifact to verify, not a source. Check its lines against approved proof and current facts, and name the ones the rep must not repeat - a stale price, an integration the approved list says is not available, a certification no approved document states, a "10,000 teams" figure nobody can source. The rep has that card open; a response that does not say which of its lines are wrong leaves them in play.

### Step 11 - Be honest about fit

If the buyer's requirement clearly favors the competitor, say so.

Examples:

- the competitor has a capability the home product does not
- the competitor's packaging is structurally better for this buyer
- the buyer's required integration is unsupported
- the switching cost overwhelms the available advantage

The response can still help the rep clarify the deal without pretending the fit is better than it is.

### Step 12 - Hand off broader work

Answer this one objection fully. Then route the next job instead of silently expanding scope.

When the request asked for both - the objection response *and* a comparison document, a card, a pricing call, a claim for the whole team - produce the objection response only, and say in one line which skill or process owns the rest. Do not produce the other artifact alongside "while you are at it": a comparison document written in the margin of an objection response has had none of the checks that skill would apply, and the rep will send it anyway.

| The user also wants | Run |
| --- | --- |
| a reusable competitor card | `competitive-battlecard` |
| a full account plan | `competitive-deal-prep` |
| a POC, POV or RFP plan | `competitive-poc-rfp-plan` |
| whether this objection is costing deals | `competitive-win-loss-analysis` |
| a company pricing or packaging decision | `competitive-pricing-packaging-review` |
| a full positioning decision | `competitive-positioning` |
| a full competitor profile | `competitive-deep-dive` |
| launch-specific framing or enablement | `competitive-launch-readiness` |

### Step 13 - Produce the artifact

Use `assets/objection-response-template.md`.

Default to concise. This is a moment-of-use artifact.

Return it inline, then offer to save it if the user wants a file.

## Evidence and reasoning rules

Read `references/TRUST.md`.

Especially for objection handling:

- a buyer belief is evidence of buyer perception, not proof of the underlying product fact
- absence is not evidence
- do not invent why the competitor built or priced something a certain way
- do not invent customer stories
- one deal is one deal
- internal claims still need approved proof when they are material
- where the competitor is stronger belongs in the answer
- a source's interpretation is that source's, not yours and not a fact. LMTY's `implication` sentence on a change, a rep's risk reason in the CRM, a battlecard's line, a win/loss interviewer's paraphrase: quote it and say whose it is. "LMTY reads this as a shift to self-serve" is honest; "this signals a shift to self-serve" is a claim you did not verify.

## Graceful fallback

Read `references/DEGRADATION.md` and `references/LMTY.md`.

### Fully connected

Use market truth, the actual objection, deal context, prior outcomes, and approved proof.

### LMTY connected without internal deal context

Produce a market-grounded response.

Do not claim the objection is common, do not say what "usually wins," and do not invent prior examples.

### Research mode

Verify the current public facts and produce a point-in-time response.

State that there is no longitudinal or internal deal evidence.

### Bounded-input mode

Use only the supplied material, and say so at the top.

Do not fill missing competitor facts or home-product proof from memory. That includes reputation: "Northwind has a broad ecosystem" is memory, even when it favors the buyer's claim and even when it is probably true. A premise the supplied material cannot check is **unknown**; write that, and name what would check it - the competitor's integration directory, the approved integrations list - so the user can go and get it.

## References

- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/LMTY.md`
- `references/INTERNAL.md`
- `references/METHODOLOGY.md`
- `references/QUALITY.md`
- `references/TRUST.md`
