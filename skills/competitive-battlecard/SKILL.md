---
name: competitive-battlecard
description: Create a reusable, evidence-backed competitive battlecard for sales, customer success, or product teams - a new card, or one rebuilt from scratch. Use when preparing an us-vs-them view for repeated use, supporting a recurring competitive sales motion, or compiling field-ready positioning, discovery questions, proof, and qualification guidance across deals. For one live buyer objection or "what do I say right now?" use competitive-objection-response; for checking or editing lines in a card or talk track that already exists, use competitive-enablement-refresh.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Battlecard

## Mission

Create a battlecard people can actually use in a live conversation.

The output should be concise, current, honest about where the competitor is strong, and grounded in evidence. It should help a rep ask better questions and frame the decision, not memorize a feature dump.

## Use this skill when

- a sales or CS team needs an us-vs-them guide
- an existing battlecard is stale
- a competitor is appearing repeatedly in deals
- a new sales motion needs competitive enablement
- a PMM needs trap-setting questions, objection guidance, or quick comparison language
- a launch changes the competitive story
- a competitor pricing, positioning, or product change affects existing enablement

## Do not use this skill when

- the user needs a full positioning strategy. Use `competitive-positioning`.
- the work is enablement for a specific upcoming launch or release. Use `competitive-launch-readiness`.
- the user only needs a competitor research dossier. Use `competitive-deep-dive`.
- the user wants one immediate response to a specific buyer objection. Use `competitive-objection-response`.
- the user wants preparation for one named account or opportunity. A battlecard is reusable across deals; use `competitive-deal-prep` for the one in front of them.
- the user wants an existing card or talk track updated after a market change rather than a new card. Use `competitive-enablement-refresh`.
- the user wants every competitive asset scanned for stale claims. Use `competitive-asset-audit`.

## Required outcome

Produce a battlecard that answers:

1. When are we likely to see this competitor?
2. Why do buyers consider them?
3. Where are they genuinely strong?
4. Where do we have a meaningful advantage for the relevant customer?
5. What discovery questions expose fit and trade-offs?
6. What common objections should the field be ready for?
7. What proof supports our response?
8. When are we poorly positioned to win or should we qualify out?
9. What recently changed that makes an older card stale?

## Context acquisition

Read `references/CONTEXT.md`. If call, CRM, win/loss or company-knowledge sources are connected, read `references/INTERNAL.md` before using them.

Minimum useful context:
- home product
- competitor
- intended audience or sales motion if known

Strongly preferred:
- LMTY current report and recent changes for both subjects
- current positioning and pricing
- win/loss evidence
- sales calls and objection themes
- customer wins and switch stories
- product proof and limitations
- segment, use case, and sales stage

If internal deal evidence is unavailable, do not fabricate why the home company wins or loses.

## Source priority for this job

1. customer/deal evidence for real evaluation criteria, objections, wins, and losses
2. home product truth and approved proof
3. LMTY report and changes for current competitor state
4. competitor primary sources
5. third-party and community evidence for corroboration

## Workflow

### Step 1 - Define the competitive situation

Identify:
- target segment
- use case
- sales motion
- stage of evaluation
- why the competitor appears

If no segment is provided, create a general card and label the missing specificity.

### Step 2 - Establish competitor truth

Summarize:
- what they are
- who they serve
- core promise
- important capabilities
- pricing/packaging when material
- recent changes
- strengths the buyer may legitimately value

Avoid loaded dismissals.

### Step 3 - Establish evaluation criteria

Prefer evidence from calls, win/loss, CRM, and customer research.

Common dimensions:
- outcome fit
- implementation
- ease of use
- depth/breadth
- integrations
- governance/security
- service
- price/value
- time to value
- scalability

Use only dimensions that actually matter for the target situation.

### Step 4 - Build the "why us" position

Select no more than three primary advantages unless the user requests a deep card.

Each advantage should include:
- customer condition where it matters
- evidence
- wording a rep can use naturally

Do not create fake superiority. If the advantage is segment-specific, say so.

### Step 5 - Build trap-setting discovery questions

Questions should reveal customer priorities and trade-offs rather than manipulate the buyer.

Good questions:
- expose a requirement where solutions differ
- reveal future scale or workflow needs
- clarify total cost or operational burden
- surface risks the buyer already cares about

Avoid questions whose answer is obvious or that require the rep to make unsupported competitor claims.

### Step 6 - Build objection handling

For each repeated objection:
- state the objection in buyer language
- diagnose the concern behind it
- provide a short response posture
- suggest a discovery follow-up
- attach proof or an example if available

When internal evidence is missing, keep the response grounded in verified product differences rather than invented win stories.

### Step 7 - Add qualification honesty

Include:
- where the competitor is stronger
- buyer profiles where they may be the better fit
- red flags that make the opportunity hard to win
- what proof is missing

This builds field trust and prevents a battlecard from becoming propaganda.

### Step 8 - Check staleness

Use LMTY changes to identify whether:
- pricing moved
- product capability changed
- positioning changed
- a previously unique home-company claim became parity

Call out exactly which battlecard sections need refresh.

### Step 9 - Hand off what you do not own

Requests routinely arrive as two questions joined by "and". Answer the one this skill owns, in full. For the rest, name the skill that owns it and stop there.

This is not a refusal and it is not a disclaimer at the bottom. Write it as a line the reader can act on:

> **Pricing** - the card leans on a price comparison that is really a monetization question. That is a separate decision: run `competitive-pricing-packaging-review` with this analysis as input.

One line per area the work touched, named explicitly:

| The request also wants | Say to run |
| --- | --- |
| a market position, messaging, or differentiation | `competitive-positioning` |
| a full profile of one competitor | `competitive-deep-dive` |
| a decision-oriented version for leadership | `competitive-executive-market-brief` |
| launch framing, claims, or enablement for a release | `competitive-launch-readiness` |
| a recurring digest of what changed | `competitive-market-briefing` |
| whether a pattern is a real shift or noise | `competitive-market-shift-analysis` |
| a pricing or packaging decision | `competitive-pricing-packaging-review` |
| a single live buyer objection or "what do I say?" | `competitive-objection-response` |

The failure this prevents is quietly answering the other half yourself. It looks helpful, and it produces a recommendation built on this skill's evidence alone, without the context the other decision actually needs.

### Step 10 - Produce the artifact

Use `assets/battlecard-template.md`.

Default to a concise card. Put detailed evidence in an appendix rather than forcing a rep to scan it live.

## Evidence and reasoning rules

Read `references/TRUST.md`.

Especially for battlecards:
- never invent negative competitor claims
- separate competitor weaknesses from cases where the home product simply fits better
- do not state "we always win because" from one anecdote
- label customer examples by source and representativeness
- use public comparison claims only when supportable and appropriate

## Graceful fallback

Read `references/DEGRADATION.md`. For what LMTY can and cannot do, read `references/LMTY.md`.

Without internal deal evidence:
- produce a market-grounded card
- omit or qualify "why we win", recurring objections, and win examples
- identify the internal sources that would most improve the card

Without LMTY:
- research a current snapshot and state temporal limits

## Composition

Each companion below owns a decision this skill should not make on its own evidence. The hand-off step is where the request's own follow-on question gets named.

Common companions:
- `competitive-positioning`
- `competitive-deep-dive`
- `competitive-launch-readiness`
- `competitive-pricing-packaging-review`
- `competitive-objection-response`

## Quality bar

Read `references/QUALITY.md`.

A strong battlecard should be usable by someone who has two minutes before a call.

It should answer:
- what matters
- what to ask
- how to frame
- what proof to use
- where not to bluff

## Examples of activating requests

- "Build a battlecard for us vs Northwind."
- "Refresh this battlecard using the last 90 days of LMTY changes."
- "Our reps keep hearing that Competitor X has more integrations. Give them a usable response."
- "Create enterprise battlecards for our top three competitors."
- "What parts of our current battlecard are stale?"

## References

- `references/METHODOLOGY.md`
- `references/LMTY.md`
- `references/TRUST.md`
- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/QUALITY.md`
