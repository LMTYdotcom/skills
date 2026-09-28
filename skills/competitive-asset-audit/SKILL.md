---
name: competitive-asset-audit
description: Audit a body of competitive content - battlecards, sales decks, comparison and alternatives pages, enablement, training, help-center copy - against current evidence, and produce the inventory of claims that are stale, unsupported, contradicted, or newly incomplete, ranked by exposure, with the assets each lives in and the owner or skill that should fix it. Use for "audit our competitive materials", "which claims are stale", "what do we need to update across our battlecards and site", "find competitive claims we can no longer support", and any request whose deliverable is the list of claims and how each one holds up - one page or a whole library, with nothing rewritten. Not for producing the update itself - "update X because Y changed" or "fix the talk track" is competitive-enablement-refresh; a new battlecard is competitive-battlecard; whether the message differentiates is competitive-messaging-audit.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Asset Audit

## Mission

Find every competitive claim the company is currently making that it should not be, across everything that makes one, and say which matter most.

The audit enumerates assets and their material claims, classifies each claim against current evidence, dedupes claims that live in many places, separates claims a market change just broke from claims that were never supported, ranks by exposure, and routes each fix to whoever owns the asset - without rewriting any of it.

## Use this skill when

- someone asks for competitive materials to be audited, scanned, or reviewed for staleness
- a team wants to know which claims across battlecards, decks, and web pages are no longer supportable
- a periodic review of competitive content is due
- a large market change has landed and the question is what, across everything, it touched
- a request bundles the audit with rewrites - do the audit, route the rewrites (Step 8)

## Do not use this skill when

- one change or a defined enablement scope drives the work and the user wants the updated text drafted. Use `competitive-enablement-refresh`.
- one battlecard is the job. Use `competitive-battlecard`.
- the question is whether the messaging differentiates, not whether its claims are supported. Use `competitive-messaging-audit`.
- a rep needs words for one objection now. Use `competitive-objection-response`.
- the artifact is a launch brief or launch enablement and the question is whether its competitive claims hold for the launch. Use `competitive-launch-readiness`.
- prospect-facing comparison copy needs writing - that is not yet in this pack; audit the existing page here and say the rewrite is a separate job.

## Required outcome

For the asset scope in front of the user, answer:

1. Which assets are in scope, and which material competitive claims does each make?
2. For each distinct claim: supported and current, supported but stale, unsupported, contradicted, or unknown - with the evidence?
3. Which claims were always weakly sourced, as opposed to newly broken by a market change?
4. Which claims are duplicated across assets, and where?
5. Ranked by exposure and consequence, which claims need attention first?
6. Which assets are affected by each high-priority claim?
7. Who, or which skill, should fix each?
8. What evidence was used, how fresh is it, and where is coverage missing?

## Context acquisition

Read `references/CONTEXT.md` and `references/INTERNAL.md`.

### Irreducible minimum

- home product
- the asset scope: a repository, a folder, a list of URLs, a set of attached files, or a defined class of assets

Retrieve before asking. When a content repository, CMS, or enablement library is connected, enumerate the assets that mention tracked competitors rather than asking the user to list them. When LMTY is connected, the tracked set defines which competitor names to search for.

If no scope can be established and nothing was supplied, ask one question: what should be audited. Then stop.

### Strongly preferred context

- the content repository or CMS, with asset dates and owners
- current LMTY report, evidence, and change record for every competitor named in the assets
- approved home-product facts: claims, pricing, integrations, security, references
- customer and deal evidence, for assets that make win or objection-frequency claims
- asset usage data, for weighting exposure

## Source priority for this job

1. approved home-product facts for any claim about the home product
2. current LMTY evidence and state for any claim about a competitor
3. deal and customer evidence for any claim about wins, losses, or how often buyers say something
4. the assets themselves, as the thing under audit
5. usage data, for how many people a wrong claim reaches

## Workflow

### Step 1 - Enumerate assets and extract material claims

List every asset in scope with type, location, owner, and last-updated date. From each, pull the material competitive claims: statements about a competitor, about the home product relative to a competitor, about customers switching or choosing, about market position.

Material means a buyer or rep could act on it. "Northwind is where tickets go to wait" is framing; "Northwind's Standard plan is $8 per user" is a claim. Audit claims; note framing only when it rests on a claim.

### Step 2 - Classify each claim by type

Tag each claim: competitor capability, competitor pricing or packaging, competitor customer or market position, home-product capability, home-product pricing, home-product security or compliance, customer reference, win or objection frequency, comparative superlative ("faster", "more", "only"). The type decides which source can verify it.

### Step 3 - Dedupe

Group identical or near-identical claims across assets into one entry with the list of homes. A price that appears in four assets is one claim to verify and four places to fix. Note where the same claim appears with different numbers - that is a finding on its own.

### Step 4 - Retrieve the evidence and mark each claim

For each distinct claim, get the source its type requires and mark:

- **supported and current** - evidence confirms it; wording and date are fine
- **supported but stale** - the fact holds; the wording, figure, or date is behind the current source
- **unsupported** - the source that would verify a claim of this type was available and does not back it; it may be true
- **contradicted** - current evidence says otherwise
- **unknown / insufficient coverage** - the source that would verify it was not available or does not reach it; this is the mark for a home-product claim when no approved facts were supplied, and for a competitor claim the evidence does not cover

Give the source and date for every mark. For competitor claims, absence from the competitor's public material is unknown, not contradicted.

### Step 5 - Separate always-weak from newly broken

For each claim not marked current, say which: was it ever backed by a source, or did a dated change break it? Use the LMTY change record and home-product change history. The two kinds have different owners and different lessons - one is a process gap in how claims get into assets, the other is normal decay.

### Step 6 - Note home-product changes the public data does not show

A home-product change - a feature shipped, a certification obtained, an integration added - can make an asset's claim about the home product stale or make a competitor comparison newly wrong, without anything in the market data moving. Check approved home-product facts against the assets' home-product claims explicitly; do not rely on the competitor record to surface this.

### Step 7 - Prioritize by exposure and consequence

Rank the non-current claims by two things: how many people it reaches (public web page over internal deck, high-usage card over archived one) and what it costs if acted on (a wrong price, a certification asserted, a capability the buyer will test, a reference that did not consent). A contradicted claim on a public comparison page is the top of the list.

### Step 8 - Route each fix

For each prioritized claim, name the owner if known and the skill or process that does the work:

| The fix is | Run |
| --- | --- |
| a defined refresh of enablement around a change | `competitive-enablement-refresh` |
| one battlecard rebuilt | `competitive-battlecard` |
| the external message reconsidered | `competitive-messaging-audit` |
| a prospect-facing comparison page rewritten | not yet in this pack; name the page and its contradicted claims for the owner |
| a competitor claim that needs deeper verification | `competitive-deep-dive` |

Do not rewrite the assets. The audit's value is that it is complete; a rewrite of three assets is neither complete nor an audit.

### Step 9 - Produce the artifact

Use `assets/asset-audit-template.md`.

Return it inline, then offer to save it. Include the source and freshness table: what evidence was used, its dates, and where coverage was missing.

## Evidence and reasoning rules

Read `references/TRUST.md` and `references/METHODOLOGY.md`.

Especially for audits:

- the asset is under audit; nothing in it is a source for anything else in it
- unsupported means no proof, not false; contradicted means evidence says otherwise; keep them apart
- absence on a competitor's site does not invalidate a claim about them
- a claim duplicated across assets is one claim; a claim that varies across assets is a defect
- "supported but stale" is not "fine" - a rep quoting a figure two versions old is quoting a wrong figure
- a win or frequency claim needs deal evidence; a reference claim needs the approved list; no other source will do
- an audit that rewrote things is an incomplete audit

## Graceful fallback

Read `references/DEGRADATION.md` and `references/LMTY.md`.

### Fully connected

Assets from the repository, competitor evidence from LMTY, home-product facts from approved sources, frequency claims checked against deal evidence.

### LMTY connected, assets supplied by the user

Audit exactly what was supplied; say the scope is the user's selection, not the repository. Competitor claims verified against LMTY; home-product claims marked unknown unless approved facts were also supplied.

### Assets connected, no LMTY

Competitor claims verified against current public evidence, point-in-time and dated; say there is no tracked change record, so "newly broken" cannot be dated.

### Bounded-input mode

Use only the assets and sources supplied, and say so at the top. Every claim the material cannot verify is unknown, with what would verify it. Do not mark a claim contradicted from memory.

## References

- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/LMTY.md`
- `references/METHODOLOGY.md`
- `references/QUALITY.md`
- `references/TRUST.md`
