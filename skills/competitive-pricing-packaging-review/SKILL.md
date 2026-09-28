---
name: competitive-pricing-packaging-review
description: Analyze or pressure-test the home product's own pricing and packaging using current competitor offers, recent pricing changes, customer and deal evidence, and company context. Use when the deliverable is a monetization decision - reviewing a pricing change, planning packaging, deciding whether the company should respond to a competitor price move, or asking what market evidence should inform pricing. Not for a live buyer price objection, a pricing-news briefing, or profiling a competitor whose pricing moved.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Pricing and Packaging Review

## Mission

Help a PMM understand how current market pricing and packaging should inform a pricing decision without pretending competitor prices determine the correct price.

This is an evidence and decision-support skill, not a substitute for willingness-to-pay research, unit economics, or financial modeling.

## Use this skill when

- reviewing or planning a pricing or packaging change
- a competitor changed price, packaging, free tier, limits, or included features, and the question is what we should do about it
- someone asks what changed in competitor pricing over a period and what it means for ours
- leadership asks how the company compares on price and value
- a launch introduces a new paid capability or tier
- a team wants to understand market packaging patterns
- a PMM needs a pricing/packaging section for a strategy or launch review

## Do not use this skill when

- the user asks for a full financial model or revenue forecast
- there is no pricing, packaging, entitlement, or monetization question
- the primary question is broad positioning. Use `competitive-positioning`.
- the buyer is objecting to price in a live deal and the user needs to know what to say next. Use `competitive-objection-response`. A buyer price objection is not a monetization decision.
- the deliverable is a briefing for an audience and pricing is one subject among several. Use `competitive-market-briefing`, or `competitive-executive-market-brief` for leadership. A request that is only about pricing and ends in what we should do belongs here, however it is phrased.
- the request is to profile a competitor, or to explain why a competitor changed price. Use `competitive-deep-dive`. Pricing appearing in a request does not make it a pricing decision.

## Required outcome

Produce an analysis that answers:

1. What is the home offer today?
2. What are the relevant competitors charging and how is value packaged?
3. What changed recently?
4. Which comparison dimensions matter to customers?
5. Where is the home offer advantaged, exposed, or simply different?
6. Which pricing hypotheses are supported by market evidence?
7. What cannot be concluded without internal or primary research?
8. What decision questions should the pricing team resolve next?

## Context acquisition

Read `references/CONTEXT.md`. If call, CRM, win/loss or company-knowledge sources are connected, read `references/INTERNAL.md` before using them.

Minimum useful context:
- home product pricing/packaging or proposed change
- target segment
- competitor set or permission to identify it

Strongly preferred:
- LMTY pricing/packaging report sections and changes
- win/loss and objection data
- usage/adoption by plan
- conversion, expansion, churn, discounting, and deal data
- willingness-to-pay or pricing research
- gross margin or cost-to-serve constraints when relevant
- product roadmap and packaging goals

## Source priority for this job

1. official home-company pricing and packaging truth
2. LMTY current and historical pricing/packaging evidence
3. competitor pricing pages, docs, terms, and public sales material
4. CRM, win/loss, and sales calls for actual buyer reactions and discounting
5. usage and revenue data for internal economics
6. pricing research and customer interviews
7. third-party estimates only when clearly labeled

## Workflow

### Step 1 - Define the decision

Clarify whether the job is primarily:
- competitive scan
- reaction to a competitor move
- new price point
- packaging redesign
- free-to-paid boundary
- feature entitlement
- segment-specific offer
- launch monetization

The method and burden of proof differ.

### Step 2 - Normalize the offers

Build a comparable representation of relevant offers.

Capture where available:
- list price
- billing unit
- billing period
- minimums
- free tier or trial
- plan boundaries
- included/excluded capabilities
- usage limits
- add-ons
- enterprise/custom pricing
- contract expectations

Do not force unlike pricing models into a misleading single price-per-seat table.

### Step 3 - Inspect market movement

Use LMTY changes or historical evidence to identify:
- price increases/decreases
- free-tier removal/addition
- packaging consolidation or fragmentation
- feature movement between tiers
- new usage limits
- new add-ons
- target-segment shifts reflected in packaging

Preserve observed dates.

### Step 4 - Identify customer evaluation dimensions

Use customer and deal evidence when available to understand whether buyers care about:
- headline price
- total cost
- predictability
- procurement simplicity
- included capabilities
- scale limits
- implementation or service
- risk
- ROI or payback

Competitive price differences matter only in the context of perceived value and buying process.

### Step 5 - Diagnose the home offer

Classify meaningful observations:
- **price advantage** - lower comparable price on a dimension buyers care about
- **value advantage** - stronger outcome or bundle at comparable/higher price
- **packaging clarity advantage** - easier to understand or buy
- **exposure** - material disadvantage likely to appear in evaluation
- **intentional premium** - higher price with evidence-backed reason to believe
- **false comparison** - superficially similar pricing that serves different jobs or segments

### Step 6 - Generate hypotheses, not fake certainty

Examples:
- competitor bundling may increase pressure on a paid add-on
- removal of a free tier may create an acquisition opening
- a usage-based model may reduce entry friction but increase predictability anxiety

Label each as interpretation and state what internal evidence would confirm or reject it.

### Step 7 - Assess switching forces

For a contemplated pricing change, map:
- push created by current pricing friction
- pull of the proposed offer
- anxiety about cost, lock-in, or unpredictability
- habit and switching costs

### Step 8 - Produce decision questions

A strong review ends with the questions the team actually needs to resolve, such as:
- Are we monetizing a capability customers already view as table stakes?
- Is a competitor price change appearing in loss reasons or only in internal anxiety?
- Does our packaging map to how customers buy and expand?
- Are we deliberately premium or accidentally expensive?

### Step 9 - Hand off what you do not own

Requests routinely arrive as two questions joined by "and". Answer the one this skill owns, in full. For the rest, name the skill that owns it and stop there.

This is not a refusal and it is not a disclaimer at the bottom. Write it as a line the reader can act on:

> **Positioning** - the real question is what we stand for, not what we charge. That is a separate decision: run `competitive-positioning` with this analysis as input.

One line per area the work touched, named explicitly:

| The request also wants | Say to run |
| --- | --- |
| one live buyer objection or "what do I say?" | `competitive-objection-response` |
| a reusable rep-facing card | `competitive-battlecard` |
| a market position, messaging, or differentiation | `competitive-positioning` |
| a full profile of one competitor | `competitive-deep-dive` |
| a decision-oriented version for leadership | `competitive-executive-market-brief` |
| launch framing, claims, or enablement for a release | `competitive-launch-readiness` |
| a recurring digest of what changed | `competitive-market-briefing` |
| whether a pattern is a real shift or noise | `competitive-market-shift-analysis` |

The failure this prevents is quietly answering the other half yourself. It looks helpful, and it produces a recommendation built on this skill's evidence alone, without the context the other decision actually needs.

### Step 10 - Produce the artifact

Use `assets/pricing-review-template.md`.

## Evidence and reasoning rules

Read `references/TRUST.md`.

Especially for pricing:
- public list price may not equal realized price
- missing public pricing does not imply higher or lower pricing
- competitor price moves do not prove elasticity, growth problems, or strategy
- do not recommend price changes solely to match competitors
- separate market evidence from internal economics and willingness-to-pay evidence

## Graceful fallback

Read `references/DEGRADATION.md`. For what LMTY can and cannot do, read `references/LMTY.md`.

Without LMTY:
- create a point-in-time offer map from primary sources
- do not claim when a price changed without dated evidence

Without internal revenue/deal data:
- stop at market hypotheses and decision questions
- do not make a definitive pricing recommendation

## Composition

Each companion below owns a decision this skill should not make on its own evidence. The hand-off step is where the request's own follow-on question gets named.

Common companions:
- `competitive-positioning`
- `competitive-launch-readiness`
- `competitive-market-shift-analysis`
- `competitive-deep-dive`
- `competitive-executive-market-brief`

## Quality bar

Read `references/QUALITY.md`.

A strong result helps a pricing team distinguish:
- what competitors charge
- how value is packaged
- what buyers appear to care about
- what recently changed
- what that may imply
- what only internal or primary research can answer

## Examples of activating requests

- "Northwind raised prices. What should we examine before changing ours?"
- "Compare our packaging against these six competitors and pressure-test our new plan structure."
- "Are we charging separately for something the market treats as table stakes?"
- "Build a pricing and packaging review for the exec team."
- "What changed in competitor pricing over the last quarter and what questions should it raise for us?"

## References

- `references/METHODOLOGY.md`
- `references/LMTY.md`
- `references/TRUST.md`
- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/QUALITY.md`
