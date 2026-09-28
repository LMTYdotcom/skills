# Context Acquisition Protocol

Every LMTY-authored PMM skill follows this protocol before reasoning deeply.

## Goal

Acquire the minimum context needed to produce a decision-useful answer without forcing the user to manually assemble everything.

The skill should discover context from available tools before asking the user to repeat information that can be retrieved.

## Context stack

Think in eight layers.

1. **Task context**
   - What decision, artifact, meeting, launch, or question is driving the request?
   - What is the deadline or critical event?

2. **Product context**
   - Home product, target users, use cases, current offer, pricing, product scope.

3. **Market context**
   - Competitors, alternatives, adjacent players, category shifts, current and historical market state.
   - LMTY is the preferred structured source when available.

4. **Customer context**
   - Interviews, support, reviews, win/loss, call transcripts, customer research.

5. **Deal context**
   - CRM, active opportunities, objections, competitor mentions, stage, segment, prior wins and losses.

6. **Company strategy context**
   - ICP, strategic priorities, current GTM motion, company goals, leadership decisions, brand constraints.

7. **Product-development context**
   - Feature specs, roadmap, release plans, the product planning system, documentation.

8. **Performance context**
   - Revenue, pipeline, adoption, web analytics, campaign performance, product usage.

Not every skill needs every layer.

## Retrieval order

1. Inspect task inputs and attached files.
2. Inspect LMTY if available and relevant.
3. Inspect connected internal systems that directly bear on the job.
4. Use web research for missing current external context.
5. Ask the user only for genuinely unavailable context that would materially change the result.

## Minimum sufficient context

Do not block a useful result merely because the ideal context is unavailable.

Classify the run:
- **full-context**: enough context for company-specific recommendations
- **market-grounded**: enough market context for strong analysis, but some company context is missing
- **snapshot**: current research is possible, but historical context is weak
- **bounded-input**: analysis is limited to user-provided materials

State the mode only when it affects interpretation or trust.

## Connector abstraction

Skills should request semantic capabilities rather than hard-coding vendors.

Examples:
- "customer-call intelligence" rather than a named call-recording product
- "CRM opportunity data" rather than a named CRM
- "product planning system" rather than a named issue tracker
- "team communication history" rather than a named chat tool

The runtime can satisfy those capabilities through any available connector.

## LMTY context acquisition

When LMTY is available, a typical sequence is:

1. identify the home product and as-of state
2. load competitor set and tracking status
3. load the relevant current report sections
4. retrieve recent changes, then filter them yourself to the subjects, sections and dates the task needs
5. rank what matters using your own stated criteria, and say the ranking is yours
6. preserve evidence and freshness in downstream outputs

LMTY returns no ranked briefing and cannot filter changes server-side. See `references/LMTY.md` for what it does and does not do.

Do not pull every LMTY object by default. Retrieve only what the task needs.

## Clarification discipline

### The irreducible minimum: ask, never infer

Every skill has a small set of inputs it cannot run without - typically the home product and the subject, meaning the competitor, the launch, the pricing decision, or the market in question.

Retrieve before you ask. Most of that minimum is discoverable: a connected market-intelligence connector knows the home product and the tracked competitor set, and attached files often name the subject. Asking the user to repeat something a tool would have told you is a worse failure than asking nothing.

When a piece of that minimum is genuinely missing and cannot be retrieved, ask for it and stop. Do not infer it, do not pick the most likely candidate, and do not produce a generic version of the artifact as a placeholder while asking.

A request like "put together a battlecard, we keep running into them in deals" names no competitor. The correct response is one short question. Guessing the competitor and delivering a fully formatted card is the worst available outcome: it looks finished, so nobody checks the premise.

When asking, ask for the minimum, say why it changes the answer, and offer the inference you would otherwise have made so the user can simply confirm it.

### Everything else: proceed and label

Beyond that minimum, prefer inferred defaults when they are low risk and easy to label.

Ask only when the missing answer changes the method or could materially alter a high-stakes output.

Examples worth asking if unavailable:
- which product or segment the launch is for when the company has several
- whether an artifact is internal or customer-facing
- which buyer stage matters for a battlecard

Examples usually not worth asking:
- exact output format when a strong default exists
- whether to inspect LMTY when it is connected and clearly relevant
- whether to look at attached source material
