---
name: competitive-market-shift-analysis
description: Determine whether a pattern of competitor, category, technology, buyer, pricing, or positioning signals represents noise, an isolated move, an emerging market shift, or an established change in expectations. Use when a PMM asks what a cluster of changes means, whether a trend is real, how much attention it deserves, or what evidence should trigger a response.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Market Shift Analysis

## Mission

Help a PMM distinguish meaningful market movement from the constant stream of competitive noise.

The output should improve orientation under uncertainty. It should not pretend to predict the future with certainty.

## Use this skill when

- multiple competitors appear to be moving in the same direction
- a new technology or behavior may be changing category expectations
- a PMM asks whether something is a real trend or just noise
- leadership is reacting to scattered competitor announcements
- a new entrant or adjacent player may be changing the market
- a team wants to know what signals deserve monitoring
- a PMM is early to a shift and does not know what it will lead to

## Do not use this skill when

- the user only wants what changed. Use `competitive-market-briefing`.
- the user wants a deep profile on one company. Use `competitive-deep-dive`.
- the user wants positioning implications as the primary output. Use `competitive-positioning` after establishing the shift.
- the question is what a change means for a specific upcoming launch. Use `competitive-launch-readiness`.
- the shift is established and the question is what product should investigate because of it. Use `competitive-roadmap-review`.

## Required outcome

Produce an analysis that answers:

1. What signals are we observing?
2. Which are independent versus copies or reactions to the same event?
3. What customer or buyer evidence supports the pattern?
4. Is this isolated noise, an emerging shift, an accelerating shift, or an established expectation?
5. What would falsify the current interpretation?
6. Which areas - product, positioning, pricing, GTM, enablement - does the shift raise a question for, and which skill owns answering it?
7. What should the team monitor next?
8. What should the team avoid overreacting to?

## Context acquisition

Read `references/CONTEXT.md`. If call, CRM, win/loss or company-knowledge sources are connected, read `references/INTERNAL.md` before using them.

Minimum useful context:
- the suspected shift or set of signals
- market/product context

Strongly preferred:
- LMTY changes across the tracked set
- LMTY current report and briefings
- customer calls, reviews, surveys, or win/loss
- adjacent-market evidence
- analyst or ecosystem data when relevant
- search, social, community, or usage signals when available
- company strategy and roadmap if implications are requested

## Source priority for this job

A shift is stronger when evidence spans different source types.

Prefer a portfolio of:
- observed competitor behavior
- customer/buyer behavior
- category or ecosystem behavior
- economic or regulatory drivers when relevant
- internal deal/product evidence

Several competitors repeating the same marketing phrase is not automatically independent evidence.

## Workflow

### Step 1 - State the hypothesis neutrally

Do this first, always, and put it in the output. Most requests arrive as a mood rather than a claim - "everyone is adding AI", "should we be worried about X" - and a mood cannot be tested. Nothing in the later steps works until the question has an answerable shape.

Convert the user's concern into a single falsifiable statement, and say what would count as evidence against it.

| Arrives as | Restate as |
| --- | --- |
| "Everyone is adding AI." | "AI features are becoming a baseline expectation in this category, such that buyers now screen for them." |
| "Is usage-based pricing taking over?" | "Usage-based pricing is displacing per-seat as the default in this category." |
| "Are we behind on integrations?" | "Integration breadth has become a primary evaluation criterion for our buyers." |

**Say that the restatement is yours.** Turning "something feels off" into a testable claim is interpretation, and it inherits the same rule as any other interpretation in this pack: label it. One line, before the analysis:

> I've read your concern as: *"buyers in this category increasingly expect consolidated platforms over point solutions."* That framing is mine, not your words - say so if it is the wrong question and I will re-run against the right one.

Then proceed on it. Do not wait for confirmation: a labeled inference the user can correct is more useful than a question they have to answer before getting anything. Only stop and ask when the request names no market, no subject and no observation at all, so there is nothing to restate.

### Step 2 - Build the signal ledger

For each signal record:
- source
- date
- subject
- observed fact
- signal type
- relevance
- independence
- evidence quality

Signal types may include:
- product
- pricing/packaging
- positioning/messaging
- buyer behavior
- customer request
- deal behavior
- capital/investment
- hiring
- partnership/channel
- regulation
- community/reputation

### Step 3 - Remove correlated noise

Identify signals that are not independent.

Examples:
- five articles reporting one vendor announcement are one underlying signal
- three competitors using the same AI vocabulary may reflect broad hype rather than buyer demand
- one analyst report repeated in social posts is not multiple confirmations

### Step 4 - Look for buyer-side confirmation

Ask whether customers are:
- requesting the capability
- changing evaluation criteria
- switching products
- changing willingness to pay
- adopting new workflows
- asking new objections
- using adjacent tools to solve the job

Buyer-side evidence often determines whether competitor activity is merely supply-side experimentation or a real demand-side shift.

### Step 5 - Classify shift maturity

Use one of five states:

- **Noise** - insufficient coherent evidence
- **Isolated move** - meaningful for one player but not a market pattern
- **Emerging shift** - multiple credible signals, buyer impact still uncertain
- **Accelerating shift** - independent supply and demand signals are reinforcing
- **Established expectation** - customers increasingly treat the change as normal or table stakes

State confidence and evidence gaps.

**Start at noise and make the evidence earn each step up.** The default answer to "is this a real shift?" is "not yet demonstrated", because that is what thin evidence supports and because the cost of the two errors is not symmetric: calling noise a shift starts roadmap arguments and burns credibility, while calling an early shift noise costs one monitoring cycle.

Each level has a bar. Do not award a level whose bar the evidence does not clear:

| To claim | You need |
| --- | --- |
| Isolated move | One credible, dated signal about one player |
| Emerging shift | Signals from **independent** subjects, not one event reported repeatedly, and at least one that is not a vendor announcement |
| Accelerating shift | Independent supply-side signals **plus** buyer-side evidence - questions asked, requirements written, deals lost |
| Established expectation | Buyer-side evidence that the capability is screened for rather than asked about |

Three vendor announcements in one quarter is supply-side coherence with no demand evidence: that is an emerging shift at most, never an accelerating one. Say plainly which bar was not met and what evidence would clear it.

**Independence is necessary, not sufficient.** Two signals can be independent of each other and both still be weak. Before awarding a level, check what each signal actually is:

| Evidence | Weight |
| --- | --- |
| The subject's own pricing page, changelog, docs, filing | Primary. Full weight. |
| A tracked change record with a source and an observed date | Primary. Full weight. |
| Third-party description of what a vendor did - blog post, article, roundup | Second-hand. Supports "something may have happened", not "this is what happened". |
| Opinion or speculation about where the category is going | Not evidence of a shift. Evidence that someone is talking about one. |
| Recollection, "I think I saw", conference hearsay | Not evidence. Record it as a question to verify. |

**Cap the classification at the weakest link.** A level needs signals that actually clear its bar, not signals that would clear it if verified:

- if every signal for a subject is second-hand, that subject supports **at most** an isolated move, however many outlets carried it
- in bounded-input mode, or where nothing can be verified, cap at **isolated move** unless the supplied material includes primary sources
- two second-hand descriptions plus one customer question is not an emerging shift. It is an isolated move with a clear next step: verify the two vendors' primary sources and ask the other customers.

Under-classifying costs a monitoring cycle. Over-classifying sends a roadmap conversation after a blog post.

### Step 6 - Explain the mechanism

Describe what may be changing in customer progress or market structure.

Possible mechanisms:
- cost or speed threshold changed
- new technology removed friction
- buyer expectation shifted
- distribution changed
- regulation changed requirements
- new pricing model changed adoption
- adjacent category entered the job

Do not infer competitor motives.

### Step 7 - Map implications by time horizon

Separate:
- now - immediate awareness, claims, enablement, launch risk
- next - experiments, research, roadmap questions
- later - structural position, category, moat, business-model questions

Do not recommend large irreversible moves from early-stage evidence without internal context.

An implication names a decision that is now worth making. It does not make it. "This raises whether our positioning should lead on governance" is an implication; two paragraphs of recommended messaging is a positioning artifact, and this skill does not produce one.

### Step 8 - Hand off what you do not own

Requests routinely arrive as two questions joined by "and": *is this a real shift, and what should our positioning be?* Answer the first in full. For the second, name the skill that owns it and stop.

This is not a refusal, and it is not a disclaimer at the bottom. Write it as a line the reader can act on:

> **Positioning** - this raises whether we should lead on usage-based value framing. That is a positioning decision, not a shift question: run `competitive-positioning` with this analysis as input.

One line per area the analysis touched, named explicitly:

| The request also wants | Say to run |
| --- | --- |
| a market position, messaging, or differentiation | `competitive-positioning` |
| a pricing or packaging decision | `competitive-pricing-packaging-review` |
| launch framing, claims, or enablement for a release | `competitive-launch-readiness` |
| field talk tracks, objections, or a rep-facing card | `competitive-battlecard` |
| a full profile of one of the competitors involved | `competitive-deep-dive` |
| a version for leadership | `competitive-executive-market-brief` |

The failure this prevents: silently answering the positioning half yourself. It looks helpful, and it produces a positioning recommendation built on shift evidence alone, without the customer, product and company context that a positioning decision needs.

### Step 9 - Define the monitoring plan

Specify:
- signals that would strengthen the thesis
- signals that would weaken it
- subjects or sources to watch
- useful review window

When LMTY is connected, translate this into filters/sections that can be queried repeatedly.

### Step 10 - Produce the artifact

Use `assets/market-shift-template.md`.

## Evidence and reasoning rules

Read `references/TRUST.md`.

Especially for shifts:
- distinguish signal count from independent evidence
- distinguish supply-side activity from customer demand
- do not use confident trend language from a single company move
- name falsifying evidence
- prediction is allowed only as clearly labeled scenario or speculation

## Graceful fallback

Read `references/DEGRADATION.md`. For what LMTY can and cannot do, read `references/LMTY.md`.

Without LMTY:
- research current and dated historical sources where possible
- be explicit when the time series is incomplete

Without buyer evidence:
- classify supply-side movement separately
- avoid calling the shift established

## Composition

This skill establishes whether something is happening. It does not decide what to do about it: each companion below owns a decision that would be wrong to make from shift evidence alone. Step 8 is where the request's own follow-on question gets named.

Common companions:
- `competitive-market-briefing`
- `competitive-deep-dive`
- `competitive-positioning`
- `competitive-launch-readiness`
- `competitive-pricing-packaging-review`
- `competitive-executive-market-brief`

## Quality bar

Read `references/QUALITY.md`.

A strong result should calm reactive teams by showing:
- which facts matter
- how much evidence exists
- what is still uncertain
- what would change the conclusion
- which responses are proportionate to the evidence

## Examples of activating requests

- "Everyone is adding AI. Is this actually a market shift or just noise?"
- "Three competitors changed packaging. What is happening?"
- "Are we seeing a real move upmarket in this category?"
- "What would have to happen before we treat this as table stakes?"
- "Analyze the last 90 days of changes and tell me which patterns are real."

## References

- `references/METHODOLOGY.md`
- `references/LMTY.md`
- `references/TRUST.md`
- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/QUALITY.md`
