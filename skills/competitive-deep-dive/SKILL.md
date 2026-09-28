---
name: competitive-deep-dive
description: Build an evidence-backed, current understanding of a competitor or alternative, including who they serve, positioning, product, pricing, packaging, recent changes, strengths, weaknesses, customer perception, and implications for the home product. Use when a PMM needs to get fully up to speed on one company, prepare a teardown, investigate a new or rising competitor, establish a reusable competitor baseline, or make sense of a move one competitor just made - including what a price, packaging or product change of theirs means, and whether their reasons for it can be known at all.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Deep Dive

## Mission

Create a durable, decision-useful understanding of one competitor or alternative that other PMM skills can reuse.

The deep dive should explain the competitor as a business and customer choice, not merely catalog its website.

## Use this skill when

- a new competitor appears
- a PMM needs a full teardown or briefing on one company
- a competitor becomes strategically important
- a launch, positioning review, battlecard, or pricing analysis needs deeper competitor context
- leadership asks "what do we actually know about them?"
- the team needs a current baseline before tracking future changes

## Do not use this skill when

- the user only wants recent changes across the market. Use `competitive-market-briefing`.
- the user wants an us-vs-them sales artifact. Use `competitive-battlecard` after the deep dive.
- the user wants to know why deals against this competitor are won or lost, from the company's own deal evidence. Use `competitive-win-loss-analysis`.
- the user wants preparation for one account where this competitor is in the deal. Use `competitive-deal-prep`.
- the user wants a broad landscape of many companies. This skill profiles one at a time; for what the market as a whole is doing, use `competitive-market-shift-analysis` or `competitive-executive-market-brief`.

## Required outcome

Produce a deep dive that answers:

1. Who is the competitor and which customers/jobs do they focus on?
2. How do they position the product and company?
3. What do they actually offer?
4. How do they price and package it?
5. What has changed recently and over the available tracked period?
6. Where are they strong?
7. Where are there credible limitations or trade-offs?
8. What do customers/prospects appear to value or dislike?
9. How do they intersect with the home product?
10. What questions should the PMM investigate next?

## Context acquisition

Read `references/CONTEXT.md`. If call, CRM, win/loss or company-knowledge sources are connected, read `references/INTERNAL.md` before using them.

Minimum useful context:
- competitor identity
- home product identity when implications or comparison are requested

Strongly preferred:
- LMTY competitor object, current report, and changes
- primary competitor website, docs, pricing, release notes, help center
- customer reviews and communities
- sales/win-loss evidence
- analyst or industry context
- home-company product and segment priorities

If the competitor is not yet tracked in LMTY, use current research and clearly label it as a snapshot.

## Source priority for this job

1. competitor primary sources for what they claim and offer
2. LMTY evidence and history for current state and change over time
3. direct customer/deal evidence for buyer perception
4. independent third-party evidence for corroboration
5. community/social evidence for emerging sentiment, clearly labeled
6. speculation only when explicitly requested and labeled

## Workflow

### Step 1 - Establish identity and scope

Confirm:
- company/product
- relevant segment or product line
- whether the task is all-up or specific to a use case

Avoid mixing multiple products from a large company into one vague competitor profile.

### Step 2 - Explain the customer/job

Determine:
- target customer
- important use cases/jobs
- trigger situations
- core promise
- apparent GTM motion

Use customer and deal evidence when available rather than inferring the ICP solely from homepage language.

### Step 3 - Map positioning

Capture:
- category/frame
- headline promise
- value themes
- proof and trust signals
- segment cues
- important messaging changes

Distinguish company positioning from individual product messaging.

### Step 4 - Map product and experience

Focus on meaningful capabilities and workflows.

Capture:
- core product areas
- important differentiating capabilities
- integrations/ecosystem
- onboarding or usage model where observable
- enterprise/security/governance where relevant
- limitations that are actually evidenced

Do not turn this into an exhaustive feature inventory unless the user asks.

### Step 5 - Map pricing and packaging

Capture:
- public pricing
- plan structure
- free/trial motion
- usage limits
- add-ons
- enterprise/custom gates
- recent pricing/packaging changes

Label unknown realized pricing.

### Step 6 - Build the change timeline

When LMTY history exists, summarize the most material observed changes by date.

Look for:
- pricing/packaging
- product launches
- positioning
- target customer
- partnerships/channel
- major proof or customer changes when evidence exists

The timeline is factual. Interpretations belong in a separate section.

### Step 7 - Assess strengths and trade-offs

Strengths should be framed from a buyer's perspective.

Trade-offs may include:
- breadth versus depth
- simplicity versus flexibility
- low entry price versus expansion cost
- integrated suite versus specialist quality
- enterprise depth versus self-serve speed

Do not invent weaknesses from silence or absence of public information.

### Step 8 - Add customer and field reality

When evidence exists, summarize:
- common reasons buyers consider them
- common positive perceptions
- recurring objections or drawbacks
- win/loss themes
- switching stories

Separate repeated patterns from anecdotes.

### Step 9 - Explain intersection with the home product

If a home product is in scope, describe:
- direct overlap
- adjacent overlap
- where customer jobs differ
- where the competitor sets expectations even without direct head-to-head deals
- which changes are most relevant to monitor

Do not force an adversarial framing when the competitor is mostly adjacent.

### Step 10 - Hand off what you do not own

Requests routinely arrive as two questions joined by "and". Answer the one this skill owns, in full. For the rest, name the skill that owns it and stop there.

This is not a refusal and it is not a disclaimer at the bottom. Write it as a line the reader can act on:

> **Enablement** - this profile is being read to arm a sales team. That is a separate decision: run `competitive-battlecard` with this analysis as input.

One line per area the work touched, named explicitly:

| The request also wants | Say to run |
| --- | --- |
| field talk tracks, objection handling, or a rep-facing card | `competitive-battlecard` |
| a market position, messaging, or differentiation | `competitive-positioning` |
| a decision-oriented version for leadership | `competitive-executive-market-brief` |
| launch framing, claims, or enablement for a release | `competitive-launch-readiness` |
| a recurring digest of what changed | `competitive-market-briefing` |
| whether a pattern is a real shift or noise | `competitive-market-shift-analysis` |
| a pricing or packaging decision | `competitive-pricing-packaging-review` |

The failure this prevents is quietly answering the other half yourself. It looks helpful, and it produces a recommendation built on this skill's evidence alone, without the context the other decision actually needs.

### Step 11 - Produce the artifact

Use `assets/competitive-deep-dive-template.md`.

## Evidence and reasoning rules

Read `references/TRUST.md`.

Especially for deep dives:
- primary source proves the competitor's claim, not customer truth
- do not infer strategy from a single webpage change
- do not treat missing public functionality as proof it does not exist
- label product access limitations
- distinguish company facts from analyst interpretation

## Graceful fallback

Read `references/DEGRADATION.md`. For what LMTY can and cannot do, read `references/LMTY.md`.

Without LMTY:
- use primary-source web research for a point-in-time baseline
- create a dated source table
- omit claims about change over time unless historical evidence exists

Without home-company context:
- deliver the competitor baseline
- omit prescriptive us-vs-them implications

## Composition

Each companion below owns a decision this skill should not make on its own evidence. The hand-off step is where the request's own follow-on question gets named.

This is a foundational skill commonly used by:
- `competitive-positioning`
- `competitive-launch-readiness`
- `competitive-battlecard`
- `competitive-pricing-packaging-review`
- `competitive-market-shift-analysis`
- `competitive-executive-market-brief`

## Quality bar

Read `references/QUALITY.md`.

A strong deep dive should allow another skilled PMM or agent to begin downstream work without repeating basic competitor research.

## Examples of activating requests

- "Get me fully up to speed on Northwind."
- "Build a teardown of Initech for our PMM team."
- "This company just started appearing in deals. Tell me what we know and what we don't."
- "Give me a baseline competitor profile we can track over time."
- "What has materially changed at Competitor X since we started tracking them?"

## References

- `references/METHODOLOGY.md`
- `references/LMTY.md`
- `references/TRUST.md`
- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/QUALITY.md`
