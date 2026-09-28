---
name: competitive-positioning
description: Develop, pressure-test, or refresh product positioning against the alternatives customers actually consider. Use when defining a market position, revising positioning after competitor or category changes, preparing a positioning brief, clarifying differentiation, or testing whether current messaging still reflects customer value and the competitive landscape.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Positioning

## Mission

Help a PMM establish a credible, useful competitive position grounded in customer progress, real alternatives, current market behavior, and company strengths.

The skill should create the context that makes messaging easier. It should not jump straight to taglines.

## Use this skill when

- defining or refreshing product positioning
- a competitor or category change may have weakened the current position
- the team struggles to explain why customers should choose the product
- a new segment, product, or GTM motion needs a position
- messaging feels generic or increasingly similar to competitors
- leadership asks how the company should be framed relative to alternatives
- a launch or pricing change creates a positioning question

## Do not use this skill when

- the user only wants a competitor profile. Use `competitive-deep-dive`.
- the user wants finished campaign copy without first needing positioning analysis.
- the main question is a pricing decision. Use `competitive-pricing-packaging-review`.
- the question is about a specific upcoming launch or release, including whether a capability is parity, catch-up, or real differentiation. Use `competitive-launch-readiness`.
- the task is a one-off sales response. Use `competitive-battlecard`.
- the position is settled and the question is whether the current copy or message hierarchy still carries it. Use `competitive-messaging-audit`.
- the question is why deals are being won or lost, from deal evidence. Use `competitive-win-loss-analysis`, and bring its findings here.

## Required outcome

Produce a positioning brief that answers:

1. What alternatives do customers use or consider?
2. Which customers care most about the value we can uniquely deliver?
3. What attributes or capabilities are meaningfully different?
4. Why do those differences matter to the customer?
5. What category or frame makes those differences easiest to understand?
6. What has changed in the market that affects the position?
7. What claims are credible, ownable, and defensible enough to repeat?
8. Where is the current position vulnerable or unsupported?

## Context acquisition

Read `references/CONTEXT.md`. If call, CRM, win/loss or company-knowledge sources are connected, read `references/INTERNAL.md` before using them.

Minimum useful context:
- product or offer
- target customer or segment
- current positioning or website copy if it exists

Strongly preferred:
- LMTY competitor set, report, and relevant changes
- win/loss or customer interviews
- sales calls and objection themes
- current strategy and GTM motion
- pricing and packaging
- product strengths and proof
- category and adjacent alternatives

Do not treat the tracked competitor set as the complete alternative set. Customers may compare against manual work, adjacent products, internal builds, services, or doing nothing.

## Source priority for this job

1. customer and win/loss evidence for what matters and what alternatives are considered
2. product truth for what the home product can actually deliver
3. LMTY for current competitor state and changes over time
4. competitor primary sources for their claims and offer
5. company strategy and target segment
6. reviews, community, analysts, and third-party evidence for perception

## Workflow

### Step 1 - Frame the customer's progress

Define the functional, emotional, and social jobs when evidence supports them.

Identify:
- situation or trigger
- current struggle
- desired progress
- consequences of staying with the current alternative

Avoid demographic positioning without causal relevance.

### Step 2 - Identify competitive alternatives

List what customers would do if this product did not exist.

Separate:
- direct competitors
- adjacent alternatives
- internal or manual approaches
- status quo or no decision

Rank by actual customer/deal relevance, not market fame.

### Step 3 - Map the current market

For the alternatives that matter, establish:
- target customer
- core promise
- key capabilities
- pricing/packaging if material
- proof and trust signals
- recent positioning or product changes

Use LMTY history to distinguish a durable position from a recent messaging experiment when possible.

### Step 4 - Identify unique attributes

Find attributes the home product has that relevant alternatives do not share, or executes in a meaningfully different way.

Use these differentiation lenses where useful:
- feature/capability
- pricing/packaging
- market segment
- technology with a user-visible consequence
- channel/distribution
- customer experience

Do not label an attribute unique until the evidence supports it.

### Step 5 - Translate attributes into value themes

For each candidate attribute ask:
- who cares?
- in what situation?
- what outcome changes?
- what proof exists?
- how easy is this for a competitor to copy?

Discard differences that do not matter to the target customer.

### Step 6 - Choose the market frame

Decide which context helps the customer understand the value fastest.

Test whether the position is primarily:
- market capture in an understood category
- a focused subcategory or segment position
- market creation that requires problem education or reframing

Do not create a new category merely to sound unique.

### Step 7 - Map switching forces

For the target customer, document:
- push away from the current situation
- pull toward the new solution
- anxiety about adopting it
- habit or switching cost holding them back

Use this to reveal which parts of the position need proof, not just stronger copy.

### Step 8 - Draft the positioning core

Produce:
- target customer
- competitive alternatives
- differentiated attributes
- value themes
- market/category frame
- reasons to believe
- positioning statement for internal use
- messaging implications, not full campaign copy unless requested

### Step 9 - Pressure-test against recent change

Use relevant LMTY changes or current research to ask:
- did a competitor move into our claimed territory?
- did a new alternative change the evaluation set?
- did pricing/packaging alter how value is perceived?
- did our own product change enough to make old positioning stale?

### Step 10 - Hand off what you do not own

Requests routinely arrive as two questions joined by "and". Answer the one this skill owns, in full. For the rest, name the skill that owns it and stop there.

This is not a refusal and it is not a disclaimer at the bottom. Write it as a line the reader can act on:

> **Pricing** - the position depends on a packaging change we have not decided. That is a separate decision: run `competitive-pricing-packaging-review` with this analysis as input.

One line per area the work touched, named explicitly:

| The request also wants | Say to run |
| --- | --- |
| field talk tracks, objection handling, or a rep-facing card | `competitive-battlecard` |
| a full profile of one competitor | `competitive-deep-dive` |
| a decision-oriented version for leadership | `competitive-executive-market-brief` |
| launch framing, claims, or enablement for a release | `competitive-launch-readiness` |
| a recurring digest of what changed | `competitive-market-briefing` |
| whether a pattern is a real shift or noise | `competitive-market-shift-analysis` |
| a pricing or packaging decision | `competitive-pricing-packaging-review` |

The failure this prevents is quietly answering the other half yourself. It looks helpful, and it produces a recommendation built on this skill's evidence alone, without the context the other decision actually needs.

### Step 11 - Produce the artifact

Use `assets/positioning-brief-template.md`.

## Evidence and reasoning rules

Read `references/TRUST.md`.

Especially for positioning:
- competitor marketing copy proves what they claim, not what customers believe
- a customer quote proves one customer's perception unless repeated evidence exists
- "best", "only", and category leadership claims require strong evidence
- a technological difference matters only if it changes a customer-relevant outcome
- do not hide where a competitor is stronger

## Graceful fallback

Read `references/DEGRADATION.md`. For what LMTY can and cannot do, read `references/LMTY.md`.

Without LMTY:
- use current primary-source research for the alternatives that matter
- state that historical movement and persistence of positioning claims may be unknown

Without customer evidence:
- produce a market-grounded positioning hypothesis
- clearly mark customer-value assumptions that need validation

Without product strategy context:
- avoid prescriptive segment or category decisions

## Composition

Each companion below owns a decision this skill should not make on its own evidence. The hand-off step is where the request's own follow-on question gets named.

Common companions:
- `competitive-deep-dive`
- `competitive-market-shift-analysis`
- `competitive-pricing-packaging-review`
- `competitive-launch-readiness`
- `competitive-battlecard`
- `competitive-executive-market-brief`

## Quality bar

Read `references/QUALITY.md`.

A strong result should make it obvious:
- who the product is for
- what it replaces or competes with
- why the difference matters
- what proof makes the story believable
- how recent market movement affects the position

## Examples of activating requests

- "Help me position this product against the alternatives customers actually use."
- "Our competitors all sound like us now. Pressure-test our positioning."
- "Has the market moved enough that we should change our position?"
- "Build a positioning brief using our customer calls and LMTY data."
- "What is our strongest defensible position for enterprise buyers?"

## References

- `references/METHODOLOGY.md`
- `references/LMTY.md`
- `references/TRUST.md`
- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/QUALITY.md`
