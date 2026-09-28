---
name: competitive-enablement-refresh
description: Work out what existing competitive sales enablement needs to change now - after a competitor move, a run of field questions, a request from sales, or on a cadence - and draft the update. The deliverable is the changed lines with their proof and date, for a single battlecard, talk track or deck as readily as a set - checks whether sections still hold up, classifies each as current, stale, unsupported or incomplete, prioritizes by what it would cost a rep to say, drafts the smallest useful change, and separates content fixes from distribution problems. Use for "what enablement is stale after this change", "update our talk tracks", "is the Northwind battlecard still accurate", "sales wants this line added - can we say it", "what should sales learn this week". When the deliverable is only the inventory of which claims hold up, with nothing to draft, that is competitive-asset-audit. Not for a new battlecard from scratch or a live objection.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Enablement Refresh

## Mission

Keep what the field says about competitors true, one change at a time.

Given a market change, a pattern of field questions, or a review cadence, find the enablement it touches, say exactly which sections are now stale, unsupported, or incomplete and why, draft the smallest edit that makes them true again, and say separately what has to happen for reps to actually see it.

## Use this skill when

- a competitor change has landed and someone asks what enablement it invalidates
- reps keep asking a question the current assets do not answer
- a PMM wants to refresh the competitive section of a deck, playbook, or training for this week or this quarter
- someone asks what sales should learn from recent market movement
- an existing talk track needs updating rather than rewriting from scratch
- a request bundles the refresh with a broad audit or a new card - take the refresh, route the rest (Step 9)

## Do not use this skill when

- the job is a broad inventory and staleness scan across every competitive asset, with no specific change or scope driving it. Use `competitive-asset-audit`.
- one battlecard is the entire job and it is being written, not refreshed. Use `competitive-battlecard`.
- a rep needs words for one objection now. Use `competitive-objection-response`.
- the user wants to know what changed in the market this week, without an enablement artifact in scope. Use `competitive-market-briefing`.
- the artifact under review is external messaging, not sales enablement. Use `competitive-messaging-audit`.

## Required outcome

For the scope in front of the user, answer:

1. What changed - in the market, in the field, or in the home product - that drives this refresh?
2. Which enablement assets and sections does it touch?
3. For each touched section: current, stale, unsupported, or incomplete - and why, with the evidence?
4. Which changes matter most, by what it would cost a rep to say the old line?
5. What is the smallest update that makes each section true?
6. What proof backs each new line?
7. Where a new line reverses an old one, what does the rep need to know about the history?
8. What can stay as it is?
9. Is the real problem content, or that reps are not seeing the content that exists?

## Context acquisition

Read `references/CONTEXT.md` and `references/INTERNAL.md`.

### Irreducible minimum

- home product
- the enablement scope: which assets, or which change or question set defines them

Retrieve before asking. When LMTY is connected, the change that drives the refresh is usually in its change record. When an enablement repository is connected, find the assets that mention the competitor or claim rather than asking the user to list them.

If neither the scope nor a driving change can be established, ask one question - and offer the likely answer with it, so the user can confirm rather than compose: "I can start with the Northwind talk track and battlecard, since those are the assets the last month's rep questions touched - or name the change or assets you mean." Then stop.

### Strongly preferred context

- LMTY report and change record for the competitors in scope
- the existing enablement: battlecards, talk tracks, decks, playbooks, training modules, with dates
- recent calls and rep questions mentioning the competitors or claims in scope
- asset usage or sales feedback, when available
- approved claims, proof, references, and pricing

## Source priority for this job

1. approved company proof for what any new line may claim
2. current LMTY state and change record for what is true of the competitor now
3. the existing assets, as the thing being verified
4. field questions from calls and channels for what the assets fail to answer
5. asset usage data for whether the problem is content or reach

## Workflow

### Step 1 - Inventory the enablement in scope

List each asset the scope covers: name, type, owner if known, last updated, and the sections that make competitive claims. Pull the claims out as short statements so they can be checked one at a time.

If the same claim appears in several assets, record it once with the list of where it lives.

### Step 2 - Identify the changes that could invalidate it

From the LMTY change record and the home product's own changes over the relevant window: which changes touch a claim in the inventory? Name each change with its date and source, and the claims it bears on.

Include home-product changes. A new integration, a price change, or a certification on the home side invalidates enablement as surely as a competitor move.

### Step 3 - Identify what the field is asking that the assets do not answer

From calls, channels, and rep questions: the recurring questions and objections about these competitors, with counts where possible. Match each against the inventory. A question with no answering section is an incompleteness; a question the section answers wrongly is worse.

### Step 4 - Classify each section

For every section in the inventory:

- **current** - the claim is supported by approved proof or current evidence, and the wording is right
- **stale** - the claim was true and is now out of date: a price that moved, a tier that was removed, a date that passed
- **unsupported** - the claim was never backed by approved proof or evidence; the change did not break it, it was always exposed
- **incomplete** - the section is correct as far as it goes and does not answer what the field is now asked

Give the evidence for each classification. "Stale" without the change that staled it, or "unsupported" without saying what proof is missing, is an opinion.

### Step 5 - Prioritize by field consequence

Order the changes by what happens if a rep says the old line to a buyer today: a wrong price quoted, a capability claimed the buyer will disprove in the demo, a certification asserted that security will deny. Edit volume is not priority. One wrong number in a talk track outranks ten cosmetic updates in a deck.

The order is your judgment. Say so - LMTY reports changes; it does not rank what matters to this team's enablement, and the artifact must not read as if it did.

### Step 6 - Draft the smallest useful update

For each section that needs to change, write the replacement text: the new line, the proof it rests on, and the date. Change only what the evidence requires. Do not rewrite the asset around the update, and do not add claims the refresh was not asked for.

If sales has asked for a line the evidence cannot support, say so and give the supportable version. Do not soften the unsupported claim into a vaguer unsupported claim.

### Step 7 - Preserve history where a claim reverses

When a new line contradicts what the asset said before - "they now publish enterprise pricing" replacing "their enterprise pricing is sales-gated" - note the reversal, the date, and the source. Reps who learned the old line will otherwise reconcile the two by ignoring one.

### Step 8 - Separate content from distribution

Answer separately: is the field asking this because the asset is wrong, or because the right asset exists and nobody opens it? Use usage data if there is any; otherwise say the question is open. A distribution or training problem gets a training note, a channel post, or a session, not another paragraph in a document nobody reads.

### Step 9 - Say what stays, and hand off the rest

List the sections that are current and need no change. That is part of the deliverable - it tells the owner what not to touch.

Route what is not this job:

| The user also wants | Run |
| --- | --- |
| every competitive asset audited, with no driving change | `competitive-asset-audit` |
| a battlecard written from scratch | `competitive-battlecard` |
| a response to one objection now | `competitive-objection-response` |
| the week's market movement on its own | `competitive-market-briefing` |
| the external message reviewed | `competitive-messaging-audit` |

### Step 10 - Produce the artifact

Use `assets/enablement-refresh-template.md`.

Return it inline, then offer to save it or to produce the edited sections as separate snippets ready to paste.

## Evidence and reasoning rules

Read `references/TRUST.md` and `references/METHODOLOGY.md`.

Especially for enablement:

- an existing asset is the thing being verified, never a source
- a change that does not touch any claim in the inventory changes nothing; say so rather than manufacturing an update
- "unsupported" is a classification about proof, not about truth - a true claim with no approved proof is still one a rep cannot safely make
- absence on a competitor's site is not evidence a claim about them is now false
- a new line carries its proof and its date
- a reversal carries its history
- the field asking a question is evidence of a gap; it is not evidence that the answer they want is true

## Graceful fallback

Read `references/DEGRADATION.md` and `references/LMTY.md`.

### Fully connected

Changes from LMTY and home-product sources, assets from the repository, field questions from calls, proof from approved claims.

### LMTY connected, no repository or field data

The user supplies the assets. Classify against current market state; say that field questions and usage were not available, so incompleteness and distribution cannot be assessed.

### Repository connected, no LMTY

Classify against current public evidence, point-in-time and dated; say there is no tracked change record, so "stale" rests on the evidence checked today.

### Bounded-input mode

Use only the assets and changes supplied, and say so at the top. Classify against what was supplied. Do not add competitor facts or home-product proof from memory; where a claim cannot be checked against the material, mark it unknown and name what would check it.

## References

- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/LMTY.md`
- `references/METHODOLOGY.md`
- `references/QUALITY.md`
- `references/TRUST.md`
