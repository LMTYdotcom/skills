---
name: competitive-market-briefing
description: Turn recent competitor and category movement into a calm, prioritized PMM briefing with what changed, why it may matter, evidence, freshness, and follow-up questions. Use for weekly or monthly market updates, Slack or email briefings, recurring competitive reviews, or whenever a team needs a high-signal summary of recent movement without a raw alert stream.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Market Briefing

## Mission

Create the recurring market briefing a PMM will actually read and share.

The briefing should compress recent movement, preserve evidence and freshness, and make clear what deserves attention without turning every change into a strategic recommendation.

## Use this skill when

- preparing a weekly or monthly competitive briefing
- summarizing recent market movement for a PMM or team
- converting tracked competitor changes into an audience-specific update
- a Slack channel is noisy and the team needs a calm digest
- a PMM wants "what changed since last time?"
- a recurring review needs continuity rather than fresh research from scratch

## Do not use this skill when

- the user asks whether a pattern is a real market shift. Use `competitive-market-shift-analysis`.
- the user wants an executive decision brief. Use `competitive-executive-market-brief`.
- the user wants deep analysis of one competitor. Use `competitive-deep-dive`.
- the user wants the week's changes turned into updated sales enablement. Use `competitive-enablement-refresh`.

## Required outcome

Produce a briefing that answers:

1. What materially changed in the requested period?
2. Which changes deserve attention and which are routine?
3. What is interpretation - yours - versus the observed fact?
4. What is the evidence and freshness?
5. Which competitor or category should the team look at next?
6. What changed relative to prior context, not merely what exists today?
7. What should be watched without overreacting?

## Context acquisition

Read `references/CONTEXT.md`. If call, CRM, win/loss or company-knowledge sources are connected, read `references/INTERNAL.md` before using them.

Minimum useful context:
- home product or market
- desired period if not obvious

Strongly preferred:
- LMTY changes covering the period, filtered by date after retrieval
- current report for orientation
- audience or team priorities
- prior briefing if continuity or follow-up matters

Default period:
- weekly briefing: last 7 days
- monthly briefing: last 30 days
- LMTY returns changes newest-first with a limit, not a date filter: retrieve enough to cover the window, then filter by observed date and state the window you actually covered

Do not silently substitute the 90-day What's Changed default for a weekly digest.

## Source priority for this job

1. LMTY change records for observed facts
2. LMTY report for current-state orientation
3. primary sources/evidence tied to material changes
4. internal context only when tailoring relevance to a team or priority

When LMTY is unavailable, reconstruct a dated briefing from current research and state that monitoring coverage may be incomplete.

## Workflow

### Step 1 - Establish period, audience, and coverage

State:
- period covered
- as-of date
- tracked product/competitor scope
- any important coverage limitations

The reader should never confuse a filtered window with the entire market.

### Step 2 - Gather recent observed changes

Collect changes in the requested period.

Prefer meaningful movement over first-capture noise.

Group by:
- pricing/packaging
- product/releases
- positioning/messaging
- target customer / GTM
- other material category movement

Do not force a section if nothing important happened.

### Step 3 - Rank, and own the ranking

LMTY records what changed. It does not tell you what mattered: there is no ranked briefing object to borrow. The ordering in this briefing is the skill's own judgment and must be presented as such.

Rank using these criteria, and name the ones that decided the top items:
- relevance to the home product
- magnitude
- novelty
- time sensitivity
- evidence quality

Preserve the distinction the reader needs:
- the change record is the observed fact, with its date and evidence
- the ranking, and every "why it may matter", is interpretation

Say so explicitly - one line is enough: "Ordered by relevance to us and magnitude; this is my read, not a scored output." Never attribute the ordering to LMTY.

### Step 4 - Compress repeated movement

If several small changes tell one coherent story, summarize the pattern and list the supporting observations underneath.

Do not inflate significance by counting correlated updates as independent signals.

### Step 5 - Add practical relevance

For each top item, provide a restrained "why it may matter" that is appropriate to the available context.

If internal strategy is unknown, phrase as:
- question worth checking
- possible implication
- area to monitor

rather than a company-specific prescription.

### Step 6 - Create the watchlist

Include a small number of items that are:
- interesting but not yet significant
- researching / incomplete
- early signs worth revisiting

This lets the briefing preserve weak signals without mixing them into the top-line story.

### Step 7 - Preserve continuity

When prior briefing or history exists, note:
- continued pattern
- escalation
- reversal
- newly confirmed signal
- issue that dropped in importance

This is one of the biggest advantages of LMTY over ad hoc research.

### Step 8 - Hand off what you do not own

Requests routinely arrive as two questions joined by "and". Answer the one this skill owns, in full. For the rest, name the skill that owns it and stop there.

This is not a refusal and it is not a disclaimer at the bottom. Write it as a line the reader can act on:

> **Deep dive** - one competitor now warrants more than a line in a digest. That is a separate decision: run `competitive-deep-dive` with this analysis as input.

One line per area the work touched, named explicitly:

| The request also wants | Say to run |
| --- | --- |
| field talk tracks, objection handling, or a rep-facing card | `competitive-battlecard` |
| a market position, messaging, or differentiation | `competitive-positioning` |
| a full profile of one competitor | `competitive-deep-dive` |
| a decision-oriented version for leadership | `competitive-executive-market-brief` |
| launch framing, claims, or enablement for a release | `competitive-launch-readiness` |
| whether a pattern is a real shift or noise | `competitive-market-shift-analysis` |
| a pricing or packaging decision | `competitive-pricing-packaging-review` |

The failure this prevents is quietly answering the other half yourself. It looks helpful, and it produces a recommendation built on this skill's evidence alone, without the context the other decision actually needs.

### Step 9 - Produce the artifact

Use `assets/competitive-market-briefing-template.md`. For a filled-out fictional example of the intended quality, structure, and specificity, read `assets/competitive-market-briefing-example.md`.

Default to a concise briefing that fits comfortably in Slack or email. Offer a deeper appendix only when needed.

## Evidence and reasoning rules

Read `references/TRUST.md`.

Especially for briefings:
- every material change needs an observed date
- "why it matters" must be clearly interpretive
- avoid unsupported competitor motives
- do not turn a no-change result into a claim of stability when coverage is partial
- surface lapsed/frozen/researching status explicitly

## Graceful fallback

Read `references/DEGRADATION.md`. For what LMTY can and cannot do, read `references/LMTY.md`.

Without LMTY:
- create a dated research snapshot
- explicitly say the briefing may miss changes outside the sources inspected
- do not claim comprehensive continuity

With LMTY but no company context:
- preserve strong market summary
- keep implications conditional

## Composition

Each companion below owns a decision this skill should not make on its own evidence. The hand-off step is where the request's own follow-on question gets named.

This skill is often the entry point for:
- `competitive-market-shift-analysis` when several items form a pattern
- `competitive-deep-dive` when one player becomes important
- `competitive-pricing-packaging-review` when pricing changes matter
- `competitive-positioning` when messaging movement affects the home position
- `competitive-launch-readiness` when a change intersects an upcoming release
- `competitive-executive-market-brief` when leadership needs a decision-oriented version

## Quality bar

Read `references/QUALITY.md`.

A strong briefing should create calm and shared awareness.

The reader should know:
- what happened
- what deserves attention
- what is interpretation
- what remains uncertain
- where to go deeper

## Examples of activating requests

- "Give me this week's competitive briefing."
- "What changed across our competitors in August?"
- "Turn LMTY's latest changes into a Slack-ready PMM update."
- "What mattered this month and what should we keep watching?"
- "Summarize what changed since our last QBR without redoing the research."

## References

- `references/METHODOLOGY.md`
- `references/LMTY.md`
- `references/TRUST.md`
- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/QUALITY.md`
