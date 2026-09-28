---
name: competitive-executive-market-brief
description: Prepare a concise, decision-oriented market and competitive brief for executives, leadership reviews, QBRs, board preparation, strategy discussions, or major planning moments. Use when leadership needs the few market changes, competitor moves, risks, opportunities, and decision questions that matter, with evidence and explicit uncertainty rather than a long CI report.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Executive Market Brief

## Mission

Turn market context into an executive decision surface.

The brief should tell leadership what changed, why it matters to the company's current priorities, what is uncertain, and which decisions or questions deserve attention.

It should not be a compressed competitor newsletter.

## Use this skill when

- preparing for a board or leadership meeting
- creating a QBR competitive section
- briefing a CEO, CMO, CPO, CRO, or product leader
- a strategic planning cycle needs market context
- leadership asks "what changed and what should I care about?"
- a PMM wants to prevent being blindsided in an executive conversation
- a launch, pricing decision, or strategic shift needs executive market context

## Do not use this skill when

- the audience primarily wants operational weekly updates. Use `competitive-market-briefing`.
- the user needs a full competitor teardown. Use `competitive-deep-dive`.
- the user needs a detailed position, pricing, or launch work product. Use the corresponding skill, then summarize here.

## Required outcome

Produce a brief that answers:

1. What materially changed in the relevant period?
2. Which changes matter to current company priorities?
3. What market pattern or strategic implication is worth leadership attention?
4. What is likely noise or not yet decision-relevant?
5. What risks could surprise the company?
6. What opportunities or openings may exist?
7. Which assumptions are weak?
8. What decisions, research, or monitoring should leadership authorize or discuss?

## Context acquisition

Read `references/CONTEXT.md`. If call, CRM, win/loss or company-knowledge sources are connected, read `references/INTERNAL.md` before using them.

Minimum useful context:
- company/product
- meeting or audience
- relevant time period if different from a sensible default

Strongly preferred:
- company priorities, goals, or strategic motion
- LMTY briefing and significant changes
- current market report
- product roadmap or launch context
- revenue/deal/customer signals
- prior leadership decisions when available

If current company priorities cannot be retrieved, ask only if the answer would materially alter the brief. Otherwise create a market-grounded brief and label the missing internal lens.

## Source priority for this job

1. current company priorities and decision context
2. LMTY significant changes and briefing
3. internal customer, deal, product, and revenue signals
4. current report and competitor evidence
5. external corroboration for material claims

## Workflow

### Step 1 - Identify the executive decision context

Determine:
- audience
- meeting type
- current strategic priorities
- decisions likely to be made
- time horizon

A board brief and a product leadership QBR should select different market facts.

### Step 2 - Gather significant market movement

Use LMTY briefing and change filters when available.

Prioritize:
- pricing/packaging moves affecting economics or buyer expectations
- product launches affecting differentiation or roadmap assumptions
- positioning shifts affecting category narrative
- target-customer movement
- new entrants with actual evidence of relevance
- market patterns supported by multiple signals

### Step 3 - Link market movement to internal reality

When internal sources exist, ask:
- Are these changes appearing in deals?
- Are customers asking for them?
- Do they affect current launches or roadmap?
- Do they affect strategic assumptions?
- Do they alter the company's position or pricing narrative?

This step is what separates an executive brief from a news summary.

### Step 4 - Prioritize by decision consequence

Rank items using:
- potential business impact
- relevance to current priority
- evidence strength
- time sensitivity
- reversibility of a wrong decision

Do not rank by headline size or competitor fame.

### Step 5 - Separate signal from noise

Include a short "not yet worth reacting to" section when the market is noisy.

This is useful executive value, especially when a Slack channel or news cycle is creating anxiety.

### Step 6 - Surface risks and openings

Risks should be specific and evidence-linked.

Openings should be framed as hypotheses or questions unless customer/company evidence makes them stronger.

### Step 7 - Create decision questions

A strong executive brief ends with a small number of questions such as:
- Does this change an assumption behind our current pricing plan?
- Do we need customer research before committing roadmap capacity?
- Should we change launch language because our claimed difference is now parity?
- Is this entrant appearing in enough deals to warrant active tracking?

Avoid generic "keep monitoring" as the only action.

### Step 8 - Hand off what you do not own

Requests routinely arrive as two questions joined by "and". Answer the one this skill owns, in full. For the rest, name the skill that owns it and stop there.

This is not a refusal and it is not a disclaimer at the bottom. Write it as a line the reader can act on:

> **Pricing** - the board question is really whether to change our pricing. That is a separate decision: run `competitive-pricing-packaging-review` with this analysis as input.

One line per area the work touched, named explicitly:

| The request also wants | Say to run |
| --- | --- |
| field talk tracks, objection handling, or a rep-facing card | `competitive-battlecard` |
| a market position, messaging, or differentiation | `competitive-positioning` |
| a full profile of one competitor | `competitive-deep-dive` |
| launch framing, claims, or enablement for a release | `competitive-launch-readiness` |
| a recurring digest of what changed | `competitive-market-briefing` |
| whether a pattern is a real shift or noise | `competitive-market-shift-analysis` |
| a pricing or packaging decision | `competitive-pricing-packaging-review` |

The failure this prevents is quietly answering the other half yourself. It looks helpful, and it produces a recommendation built on this skill's evidence alone, without the context the other decision actually needs.

### Step 9 - Produce the artifact

Use `assets/executive-brief-template.md`.

Default length:
- one page for leadership/QBR
- up to two pages for board or strategy prep

Put source detail in an appendix.

## Evidence and reasoning rules

Read `references/TRUST.md`.

Especially for executive briefs:
- increase burden of proof as the decision consequence rises
- do not hide contradictions
- label speculative scenarios
- distinguish "competitor moved" from "we need to respond"
- preserve dates and freshness for material claims

## Graceful fallback

Read `references/DEGRADATION.md`. For what LMTY can and cannot do, read `references/LMTY.md`.

Without company priorities:
- produce a market-grounded brief
- replace strong recommendations with decision questions

Without LMTY:
- research a current snapshot and cite collection dates
- avoid implying comprehensive monitored coverage

## Composition

Each companion below owns a decision this skill should not make on its own evidence. The hand-off step is where the request's own follow-on question gets named.

Common inputs from:
- `competitive-market-briefing`
- `competitive-market-shift-analysis`
- `competitive-positioning`
- `competitive-pricing-packaging-review`
- `competitive-launch-readiness`
- `competitive-deep-dive`

## Quality bar

Read `references/QUALITY.md`.

An executive should understand the decision landscape in under five minutes.

Every included item should answer "why is this in front of me?"

## Examples of activating requests

- "Prepare the competitive section for our QBR."
- "I have a board meeting Friday. What market changes could blindside me?"
- "Brief the CPO on what changed this quarter and the roadmap questions it raises."
- "Turn this month's LMTY activity into a CEO-ready one-pager."
- "What should leadership discuss based on the last 90 days of competitor movement?"

## References

- `references/METHODOLOGY.md`
- `references/LMTY.md`
- `references/TRUST.md`
- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/QUALITY.md`
