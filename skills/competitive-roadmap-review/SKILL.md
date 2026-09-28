---
name: competitive-roadmap-review
description: Turn market and customer evidence into product questions worth investigating - for a product area or a roadmap under review - without treating competitor features as a roadmap. Establishes what competitors actually did and whether it is independent and buyer-relevant, pulls the company's own customer evidence for the same need, checks whether the problem is already solved another way, and frames each gap as table-stakes risk, differentiator opportunity, copycat noise, or evidence gap, with the evidence still needed before anyone prioritizes. Use for "what should product investigate based on the market", "competitors keep adding this - does it matter for our roadmap", "review this roadmap against market and customer evidence", "are we missing something". Not for deciding whether a market pattern is real, framing a launch, or making the priority call.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Roadmap Review

## Mission

Help product see what the market and customers are saying about a product area, sharply enough to investigate the right things - and stop the review from becoming a list of competitor features to copy.

The output is questions worth investigating, each grounded in what competitors did, what the company's own customers said and did, and what the home product already does; each classified honestly as a table-stakes risk, a differentiation opportunity, copycat noise, or an evidence gap; and each with the evidence named that would have to exist before it could be prioritized. The review does not rank the roadmap.

## Use this skill when

- product or PMM asks what the market suggests product should look into
- competitors keep adding something and someone asks whether it matters for the roadmap
- a roadmap or product area is to be reviewed against market and customer evidence
- someone asks "are we missing something important?" about a product area
- a request bundles the review with a shift verdict or a launch plan - review the area, route the rest (Step 9)

## Do not use this skill when

- the first question is whether the market pattern is real at all - one move or a shift. Use `competitive-market-shift-analysis`, and bring its answer here.
- the feature is already being launched and needs competitive framing. Use `competitive-launch-readiness`.
- the question is what the whole company should do in response to a validated market move - pricing, sales, marketing, product together. That is not yet in this pack; give product's part here and say the cross-functional plan is a separate job.
- the question is a company pricing or packaging decision. Use `competitive-pricing-packaging-review`.
- the user wants one competitor understood in depth. Use `competitive-deep-dive`.

## Required outcome

For the product area or roadmap scope in front of the user, answer:

1. What product decision or area is under review, and who owns it?
2. What have competitors actually done here, when, and is the movement independent?
3. Is it buyer-relevant - is there evidence buyers care, beyond the competitors doing it?
4. What do the company's own customers say and do about the same need?
5. Is the problem already solved another way in the home product?
6. What are the questions worth investigating, framed as customer problems or strategic questions?
7. For each: table-stakes risk, differentiator opportunity, copycat noise, or evidence gap?
8. What evidence is missing before anything here could be prioritized?

## Context acquisition

Read `references/CONTEXT.md` and `references/INTERNAL.md`.

### Irreducible minimum

- home product
- the product area or roadmap scope

Retrieve before asking. When LMTY is connected it knows the home product and the competitors' current state and change history for any area. When product planning, analytics, or customer research sources are connected, the area name finds the roadmap items, the usage data, and the customer evidence.

If the scope is the whole roadmap, that is a valid scope; work area by area and say which areas the evidence reached.

If neither a product area nor a roadmap can be established, ask one question. Then stop.

### Strongly preferred context

- LMTY report, evidence, and change record for the area, per competitor
- the roadmap, specs, or PRDs for the area
- customer research, calls, interviews, and support themes touching the need
- product analytics: adoption and usage of the relevant capabilities, including the existing alternative in the home product
- win/loss evidence where the need appears in buyer criteria
- company strategy or priorities, when the user can share them

## Source priority for this job

1. the company's own customer evidence - calls, research, support, win/loss - for whether the need is real for its customers
2. product analytics for what customers do, as distinct from what they say
3. current competitor evidence and change record for what competitors did and when
4. the roadmap and specs for what is already planned or built
5. the team's read, labeled as such

## Workflow

### Step 1 - Name the decision under review

State the product area, the decision the review feeds (invest, investigate, deprioritize, defend), who owns it, and when it is being made. If the user's framing is a competitor feature ("they added X"), restate the area as the customer need X serves, and review that.

### Step 2 - Establish competitor movement

From the change record and current state: which competitors did what in this area, when, from what evidence. Distinguish shipped from announced from marketed. Note the tier or plan it landed in.

### Step 3 - Judge independence and buyer relevance

Independence: did several competitors move separately, or did one move and others follow, or did one move and the rest only talk? A pattern that is one vendor plus echoes is one vendor.

Buyer relevance: is there evidence - customer calls, buyer criteria in win/loss, analyst or review language, LMTY evidence of buyer-facing emphasis - that buyers weigh this? Competitors doing something is evidence that competitors think buyers want it, not that they do.

If the question of whether the pattern is real is the whole question, stop and route to `competitive-market-shift-analysis`.

### Step 4 - Pull the company's own customer evidence

For the same need: what have this company's customers and prospects said - in calls, interviews, support tickets, feature requests, win/loss? Count it and date it. Note where the vocabulary matches the competitor's feature and where customers describe the problem differently.

A single customer asking is one customer. A repeated request across a stated number is a pattern in requests. Neither is yet demand.

### Step 5 - Check what customers do

From analytics where available: is the need already being met another way in the home product - a workaround, an integration, an adjacent capability - and how many use it? Does usage support or contradict the stated demand? A loudly requested capability whose existing workaround nobody uses is a finding; so is a quietly used workaround nobody requested.

Where telemetry contradicts stated demand, report both and do not resolve it by preferring one. Say what would resolve it.

### Step 6 - Check whether the problem is already solved

Against the roadmap and current product: is the need addressed, planned, addressed differently by design, or absent? A competitor feature the home product serves through a different mechanism is not a gap; it may be a messaging or proof gap.

### Step 7 - Frame the questions and classify each

Write each finding as a question product could investigate, phrased as a customer problem or a strategic question - not as "build X". Classify:

- **table-stakes risk** - buyers increasingly expect it; competitors have it; evidence that its absence costs deals or renewals
- **differentiator opportunity** - customers describe a problem competitors have not solved well, or solved in a way that leaves the home product's approach distinct
- **noise / copycat risk** - competitor movement without buyer evidence; investing would be following
- **evidence gap** - the question is real but the evidence to classify it does not exist yet

Say the evidence behind each classification. Many will be evidence gaps; that is an honest result.

### Step 8 - Name the evidence missing before prioritization

For each question: what would have to be known - customer interviews in a segment, a usage study, a win/loss cut, a cost estimate, a strategic call - before product could weigh it against everything else. Do not rank the questions. Ranking needs company priorities, economics, and capacity the review does not have; if the user supplies them, rank only within what they cover and say so.

### Step 9 - Hand off

| The user also wants | Run |
| --- | --- |
| a verdict on whether the market pattern is real | `competitive-market-shift-analysis` |
| competitive framing for a feature being launched | `competitive-launch-readiness` |
| the company's cross-functional response | not yet in this pack; give product's part and say so |
| a pricing or packaging decision this touches | `competitive-pricing-packaging-review` |
| one competitor's product understood in depth | `competitive-deep-dive` |

### Step 10 - Produce the artifact

Use `assets/roadmap-review-template.md`.

Return it inline, then offer to save it.

## Evidence and reasoning rules

Read `references/TRUST.md` and `references/METHODOLOGY.md`.

Especially for roadmap work:

- competitors shipping something is evidence about competitors; buyer relevance needs buyer evidence
- one competitor is one competitor; one move plus marketing echoes is still one move
- requests are what customers say; telemetry is what they do; a conflict between them is a finding, not a tie-break
- a need the home product meets another way is not a gap
- the review frames questions; it does not rank a roadmap, and it does not write "build X"
- the evidence a classification rests on is stated; "table stakes" without deal or renewal evidence is an opinion
- motive - why a competitor built something - is unknown unless sourced

## Graceful fallback

Read `references/DEGRADATION.md` and `references/LMTY.md`.

### Fully connected

Competitor movement from LMTY, customer evidence from research and calls, behavior from analytics, plan from the roadmap.

### LMTY connected, no internal sources

Competitor movement and buyer-facing emphasis can be established; the company's own customer evidence cannot. Every question is at best an evidence gap. Say so, and do not infer this company's customer demand from the market.

### Internal sources connected, no LMTY

Customer evidence and behavior can be established; competitor movement comes from current public evidence, point-in-time and dated, with no history. Independence over time cannot be judged.

### Research mode

Competitor movement from public sources, dated. No customer evidence. The review can list what competitors did and the questions that raises; it cannot classify beyond evidence gap.

### Bounded-input mode

Use only the supplied roadmap, research, and market material, and say so at the top. Do not add competitor moves or customer evidence from memory. Classify only where the material supports it.

## References

- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/LMTY.md`
- `references/METHODOLOGY.md`
- `references/QUALITY.md`
- `references/TRUST.md`
