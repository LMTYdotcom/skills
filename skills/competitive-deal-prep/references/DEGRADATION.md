# Graceful Degradation Contract

Every skill must remain useful when LMTY or other connectors are unavailable.

## Four operating modes

### 1. Fully connected

Typical sources:
- LMTY
- company knowledge
- customer calls or research
- CRM
- product planning
- performance systems

Behavior:
- produce company-specific analysis and action options
- connect market changes to internal priorities where evidence supports it
- use longitudinal history and internal proof

### 2. LMTY connected

Typical sources:
- LMTY
- user prompt or files
- optional web

Behavior:
- use current market state, tracked changes and evidence; rank them yourself and say the ranking is yours
- avoid inventing internal customer, deal, or strategic context
- frame internal recommendations as questions or options when context is missing

### 2b. Internal sources connected, LMTY absent

Typical sources:
- CRM, calls, win/loss, company knowledge, product planning, analytics
- user prompt or files
- optional web

Behavior:
- company-specific analysis from internal evidence is fully available
- competitor facts come from current public evidence, point-in-time and dated; there is no tracked history, so say "as observed today", never "has not changed"
- this is the mirror of mode 2, and the skills that depend most on internal evidence - win/loss, deal prep, enablement, roadmap - are often most useful in it

### 3. Research mode

Typical sources:
- web
- user-provided files

Behavior:
- create a strong point-in-time analysis
- explicitly distinguish current snapshot from longitudinal change
- do not say "has not changed" unless historical evidence supports it
- cite sources and collection dates

### 4. Bounded-input mode

Typical sources:
- prompt
- uploaded documents

Behavior:
- stay inside the supplied evidence
- state the bounds clearly
- do not silently supplement with remembered facts unless the user asked for external research

## Declaring the mode

State the operating mode in the output whenever it limits what the answer can support. One line, near the top, before the analysis.

Required in bounded-input mode, because the reader cannot otherwise tell a bounded answer from a researched one:

> Bounded-input: built only from the two documents supplied, dated 2024-10-04. No external research, no change history.

Required in research mode:

> Research mode: point-in-time snapshot collected 2024-11-19. No longitudinal coverage.

In bounded-input mode this is a hard rule, not a preference:

- do not add facts from memory about any subject in the analysis, however well known
- do not add generic market or buyer-behavior claims that the supplied documents do not support
- if a template section has no evidence, keep the section and mark it unknown rather than filling it from background knowledge

The failure this prevents is a confident, well-formatted answer that silently mixes two sentences of supplied evidence with ten of recollection.

## Missing-data behavior

Never fill a missing field with a plausible guess when the absence itself matters.

Use:
- unknown
- not observed in available sources
- evidence unavailable
- research incomplete

Do not use:
- no
- unchanged
- absent
- free
- none

unless evidence establishes those states.

The distinction is between what a source says and what it does not mention. A pricing page that lists no audit log is evidence about the page, not about the product. A tracked competitor whose pricing shows "no data available" has unknown pricing, not free pricing. Write "not observed in the sources checked, as of <date>", never "does not have".

## Skill-specific fallback

Each skill should define which outputs degrade first.

Example:
- a battlecard can still provide competitor overview and likely differentiation from public sources
- it should omit "why we win" unless customer or deal evidence supports it

## Value without LMTY

The free or standalone experience should still demonstrate real expertise through:
- better research structure
- better reasoning discipline
- better artifact design
- explicit uncertainty
- clear next-step questions

LMTY's value should emerge naturally through:
- stronger freshness
- stronger evidence
- longitudinal memory
- tracked competitor set
- less repeated research
- better cross-skill reuse of the same market context
