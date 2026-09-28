---
name: competitive-launch-readiness
description: Prepare, pressure-test, or refresh a product or feature launch against current competitors, alternatives, market expectations, pricing, positioning, and recent market changes. Use when planning a launch, reviewing a launch brief, creating competitive launch guidance, preparing enablement, asking how a new release should be framed relative to the market, or judging whether a capability is parity, catch-up, or real differentiation.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Launch Readiness

## Mission

Help a PMM launch with an accurate picture of the market and a clear view of where the release is differentiated, expected, vulnerable, or likely to create confusion.

The skill should make the launch team better prepared without turning competitor behavior into product strategy by default.

## Use this skill when

- a product or feature launch is being planned or reviewed
- a PMM needs a competitive section for a launch brief or enablement
- a team wants to know how a release compares with current alternatives
- a launch needs pricing, packaging, positioning, or feature context
- a competitor has recently shipped something that may affect launch framing
- leadership asks whether the launch is meaningfully differentiated
- a PMM wants a final competitive readiness check before launch

## Do not use this skill when

- the user only wants a broad competitor profile with no launch decision. Use `competitive-deep-dive`.
- the user primarily wants a new positioning strategy. Use `competitive-positioning`.
- the user primarily wants a pricing decision. Use `competitive-pricing-packaging-review`.
- there is no launch, release, or product change to evaluate.
- the question is what product should build or investigate, rather than how to frame something already being shipped. Use `competitive-roadmap-review`.
- the artifact under review is the company's standing messaging, not launch framing. Use `competitive-messaging-audit`.

## Required outcome

Produce a launch-ready competitive assessment that answers:

1. What is the release and who is it for?
2. What customer expectation or job does it address?
3. Which competitors or alternatives matter for this release specifically?
4. What is table stakes, differentiated, behind, or ambiguous?
5. What changed recently that should alter the launch plan or language?
6. What claims can the team make confidently?
7. What should sales, product, marketing, and leadership be prepared for?
8. What important unknowns remain?

## Context acquisition

Read `references/CONTEXT.md` and follow it. If call, CRM, win/loss or company-knowledge sources are connected, read `references/INTERNAL.md` before using them.

Minimum useful context:
- release or feature description, spec, PRD, or launch brief
- home product identity
- relevant competitor set or permission to identify it

Strongly preferred context:
- target segment and use case
- launch goals
- current positioning and messaging
- current pricing or packaging if relevant
- LMTY report and changes
- customer calls, win/loss, research, or sales objections
- current roadmap or strategic motion

When LMTY is connected, retrieve only the report sections and changes relevant to this release. Do not dump the entire tracked market into context.

## Source priority for this job

1. release spec and product truth
2. LMTY current report and tracked changes
3. direct competitor product documentation, pricing, and launch sources
4. customer or deal evidence about the problem and alternatives
5. company positioning and strategy
6. third-party or community sources for corroboration and perception

## Workflow

### Step 1 - Define the launch claim

Translate the release into a simple statement:
- what changed in the product
- who can use it
- what job it improves
- what the company appears to want customers to believe

If the release brief contains multiple unrelated capabilities, separate them before comparing.

### Step 2 - Identify the competitive decision set

Do not compare against every tracked competitor automatically.

Choose the competitors and alternatives that matter because they:
- solve the same job
- appear in the same deals
- set customer expectations
- are strategically important for the target segment
- recently changed in a way relevant to the release

Explain why each included competitor matters.

### Step 3 - Establish current market state

For the relevant dimensions, determine:
- what each subject offers now
- how each subject describes it
- pricing or packaging if material
- availability and maturity where known
- proof or evidence
- freshness and coverage

Prefer job-relevant comparison dimensions over feature-count tables.

### Step 4 - Inspect recent movement

Look for relevant changes over the most useful period, normally 90 days unless the launch cycle or market pace suggests another window.

Ask:
- Did a competitor recently ship the same capability?
- Did packaging or pricing alter the perceived value?
- Did positioning change in a way that affects our launch language?
- Is an adjacent player creating a new customer expectation?

Separate observed changes from interpretations of their significance.

### Step 5 - Classify launch posture

For each meaningful dimension, classify the release as one of:
- **Category expectation** - customers increasingly expect this
- **Parity** - materially comparable to established alternatives
- **Differentiated** - a meaningful difference exists and matters to the target customer
- **Catch-up** - closes a known gap but should not be marketed as category-defining
- **Unproven** - the claimed advantage lacks enough customer or market evidence
- **Vulnerable** - the launch creates an obvious objection or comparison risk

Do not force every dimension into a positive frame.

### Step 6 - Build the launch narrative implications

Determine:
- which claims are safe and supportable
- which claims are weak or generic
- which competitor comparisons should be avoided
- what customer problem should lead the story
- whether the release changes the company's broader competitive position

Do not invent a new positioning strategy unless needed. Flag when the launch exposes a positioning problem and recommend `competitive-positioning` as the next job.

### Step 7 - Prepare cross-functional guidance

Produce concise guidance for the teams that need it.

Typical guidance:
- Product - unresolved gaps or questions worth validating
- Sales - expected objections and the evidence-backed response posture
- Customer Success - migration, adoption, or expectation questions
- Marketing - claims, proof, comparison angles, content needs
- Leadership - what is strategically notable and what is not

### Step 8 - Identify readiness gaps

List only gaps that could materially hurt the launch, such as:
- unsupported differentiation claim
- stale competitive assumption
- pricing conflict
- missing proof
- unclear target segment
- known competitor strength with no response
- customer expectation not reflected in the release

### Step 9 - Hand off what you do not own

Requests routinely arrive as two questions joined by "and". Answer the one this skill owns, in full. For the rest, name the skill that owns it and stop there.

This is not a refusal and it is not a disclaimer at the bottom. Write it as a line the reader can act on:

> **Pricing** - the competitor bundled this capability into their base plan. That is a separate decision: run `competitive-pricing-packaging-review` with this analysis as input.

One line per area the work touched, named explicitly:

| The request also wants | Say to run |
| --- | --- |
| field talk tracks, objection handling, or a rep-facing card | `competitive-battlecard` |
| a market position, messaging, or differentiation | `competitive-positioning` |
| a full profile of one competitor | `competitive-deep-dive` |
| a decision-oriented version for leadership | `competitive-executive-market-brief` |
| a recurring digest of what changed | `competitive-market-briefing` |
| whether a pattern is a real shift or noise | `competitive-market-shift-analysis` |
| a pricing or packaging decision | `competitive-pricing-packaging-review` |

The failure this prevents is quietly answering the other half yourself. It looks helpful, and it produces a recommendation built on this skill's evidence alone, without the context the other decision actually needs.

### Step 10 - Produce the artifact

Use `assets/launch-readiness-template.md` unless the user asks for another format.

## Evidence and reasoning rules

Read `references/TRUST.md` and follow it.

Especially for launches:
- competitor existence is not evidence of customer demand
- a feature match is not proof of parity in experience or outcome
- a recent competitor launch is not automatically a reason to change the roadmap
- do not infer competitor motive
- do not label something a differentiator unless the difference is both real and relevant to the target customer

## Graceful fallback

Read `references/DEGRADATION.md`. For what LMTY can and cannot do, read `references/LMTY.md`.

Without LMTY:
- perform a current snapshot using available primary sources if web access exists
- clearly say that the analysis does not establish longitudinal change unless historical evidence is available
- ask the user to supply internal customer/deal context only when it would materially alter the launch posture

With no external research:
- pressure-test only against supplied materials
- label the market assessment as bounded to those materials

## Composition

Each companion below owns a decision this skill should not make on its own evidence. The hand-off step is where the request's own follow-on question gets named.

This skill commonly composes with:
- `competitive-deep-dive` for a new or poorly understood competitor
- `competitive-market-shift-analysis` when the launch is responding to a broader change
- `competitive-positioning` when the release changes the value story
- `competitive-pricing-packaging-review` when monetization is part of launch readiness
- `competitive-battlecard` to turn the launch assessment into field enablement
- `competitive-executive-market-brief` for launch reviews with leadership

## Quality bar

Read `references/QUALITY.md`.

A strong result should make a PMM comfortable answering, in one meeting:
- why this launch matters now
- where it really stands relative to alternatives
- what the team should and should not claim
- which objections are predictable
- what still needs proof

## Examples of activating requests

- "Pressure-test this launch against our competitors."
- "Here is the PRD. What do I need to know competitively before we launch?"
- "Build the competitive section of my launch brief."
- "Northwind just shipped something similar. Does that change how we should launch this?"
- "Tell me whether this is parity, catch-up, or real differentiation."

## References

- `references/METHODOLOGY.md`
- `references/LMTY.md` for detailed launch analysis guidance
- `references/TRUST.md` for evidence rules
- `references/CONTEXT.md` for context acquisition
- `references/DEGRADATION.md`
- `references/INTERNAL.md` for fallback behavior
- `references/QUALITY.md` for output standards
