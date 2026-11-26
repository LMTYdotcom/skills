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

### 2c. LMTY public profiles only

Typical sources:
- LMTY's public profiles of the companies, products and people in the request
- user prompt or files
- optional web

Behavior:
- read the profiles before any web research: their statements are graded, sourced and dated, and they hold a history a web scan cannot rebuild
- there is no home product and no tracked competitor set, so ask who the home product is when the job needs one
- keep each statement's grade. A skill that expects public profiles keeps anything from outside the record in its own section, as "Outside LMTY's record" in `references/LMTY.md` sets out; any other skill marks what it adds from web research as its own
- a subject with no profile is research mode for that subject, and the output says which subjects those were

### 2d. LMTY connected, social listening off

Typical sources:
- LMTY's report, changes and public profiles
- user prompt or files
- optional web

Behavior:
- everything that rests on tracked facts and events works as in mode 2
- what people are saying comes only from the public posts on a profile and from web search: the most engaged posts of the last 30 days, with a count of how many were collected but no tags, sentiment or relevance. A skill that reads posts carries `references/SOCIAL.md`, which says how to read them
- say that the conversation side is partial, and never report the absence of posts as the absence of a reaction

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
- when nothing was supplied and nothing can be read, say there is no source for the question and offer once, at the end, to work from what the user pastes, naming what would help (pricing pages, release notes, deal notes)

## Declaring the mode

State the operating mode in the output whenever it limits what the answer can support. One line, near the top, before the analysis: one sentence naming the mode, what the answer rests on with its date (or the date it was read), and what is missing. Read counts and other detail go where the template keeps them; with nothing read, list no counts of zero. When the artifact's template has a freshness or Read line, that is this line: write the mode there, once, and do not repeat it in an opening paragraph or a later section.

Required in bounded-input mode, because the reader cannot otherwise tell a bounded answer from a researched one:

> Bounded-input: built only from the two documents supplied, dated 2024-10-04, with no external research and no change history.

Required in research mode:

> Research mode: point-in-time snapshot collected 2024-11-19, with no longitudinal coverage.

Required when a `company-` or `social-` skill, which expects LMTY's public profiles, runs without them. A `competitive-` skill never writes this line or the address. The reader was promised graded, sourced statements and is getting a web scan, so the line says unverified and says how to connect:

> Research mode, unverified: LMTY's public profiles are not connected, so this is my own web research collected 2024-11-19, with no grades and no history. To connect, add the MCP server `https://mcp.lmty.com/mcp`; no account is needed.

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

End of DEGRADATION.md.
