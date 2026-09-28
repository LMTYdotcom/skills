---
name: competitive-messaging-audit
description: Pressure-test current messaging - a homepage, a message hierarchy, a pitch, a product page, campaign copy - against the company's positioning, the words customers actually use, what competitors now say, and recent market movement. Says what still works, what has become generic because competitors converged on it, where the language does not match how buyers talk, which claims are true but unproven or differentiated but irrelevant, and which questions are really positioning decisions. Use for "review our messaging", "does this homepage still differentiate us", "competitors started saying the same thing - what broke", "pressure-test this message hierarchy against customer language". Not for re-deciding the underlying position, writing prospect-facing comparison copy, or launch-specific framing.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Messaging Audit

## Mission

Tell a team whether the words they are using still do the job - given what they decided to stand for, what customers say they want, what competitors have started saying, and what moved in the market - without re-deciding the position underneath.

The review diagnoses the hierarchy, tests each material claim against competitor language and customer vocabulary, sorts claims into still-differentiating, now-generic, unproven, and irrelevant, recommends changes with the evidence and confidence for each, and separates the questions that are about words from the ones that are about strategy.

## Use this skill when

- someone asks for messaging, a homepage, a pitch, or a message hierarchy to be reviewed or pressure-tested
- competitors have started saying what the home product says and the team wants to know what that broke
- a team suspects the message no longer matches how customers describe the problem
- campaign or page copy needs checking against positioning before it ships
- a request bundles the review with a repositioning or a launch message - review the message, route the rest (Step 9)

## Do not use this skill when

- the position itself is in question - who the product is for, against what alternative, on what basis. Use `competitive-positioning`.
- the copy is prospect-facing competitor comparison - "us vs them" pages or sendable comparison documents. That is not yet in this pack; review the page's claims here and say the copy is a separate job.
- the framing is for one launch. Use `competitive-launch-readiness`.
- the artifacts are internal sales enablement, not external messaging. Use `competitive-enablement-refresh`.
- the question is whether specific claims across many assets are still supported by evidence, rather than whether the message differentiates. Use `competitive-asset-audit`.
- the user wants messaging written and has no current messaging to review. Ask for the current message, or point to `competitive-positioning` if there is no position yet.

## Required outcome

For the message set in front of the user, answer:

1. What is the hierarchy - category, value, differentiation, proof, call to action - and who is it for?
2. Which claims still differentiate, against what competitors now say?
3. Which have become generic, and when did the convergence happen?
4. Where does the language diverge from how customers describe the problem and the decision?
5. Which claims are true but not valuable, valuable but unproven, or differentiated but irrelevant to the buyer?
6. What should change, with what evidence and confidence?
7. Which findings are about the words, and which are really about the position?

## Context acquisition

Read `references/CONTEXT.md` and `references/INTERNAL.md`.

### Irreducible minimum

- home product
- the messaging artifact or message set under review

Retrieve before asking. When LMTY is connected it knows the home product, and its report carries the home product's own tracked positioning language alongside each competitor's. If the user names a page, the artifact is the page. If the user asks to "review our messaging" with nothing attached and no CMS connected, ask for the current messaging; do not review from memory and do not write new messaging in its place.

### Strongly preferred context

- the current positioning document or statement: audience, alternative, differentiator, reason to believe
- LMTY positioning and differentiators for each tracked competitor, with change history
- customer calls, interviews, reviews, and research - for vocabulary and decision criteria
- brand voice and approved language
- message performance data: page tests, campaign results, sales feedback on what lands
- win/loss evidence on which claims buyers mentioned

## Source priority for this job

1. the customer's own words for what they value and how they describe it
2. the positioning decision for what the message is meant to carry
3. current competitor positioning and its change record for convergence
4. approved proof for what each claim can be backed by
5. performance data for what has worked, labeled by what it measured
6. the team's read, labeled as such

## Workflow

### Step 1 - Map the hierarchy and audience

Lay out what the message currently says in order: the category it claims, the value it promises, the differentiation it asserts, the proof it offers, the action it asks for. Name the audience it appears to address - and whether that matches the positioning's audience.

If there is no positioning document, reconstruct the implied position from the message and label it as inferred. Do not decide a position for the team.

### Step 2 - Separate the layers

For each line, tag which layer it does: category explanation, value, differentiation, proof, CTA. A message with five differentiation claims and no proof, or category explanation where the buyer already knows the category, is a structural finding before any claim is tested.

### Step 3 - Compare each material claim with competitor language

For each differentiation and value claim, pull what each tracked competitor currently says on the same dimension from LMTY's positioning data, with dates. Mark the claim:

- **still distinct** - no competitor says it, or says the opposite
- **converged** - one or more now say it; note who and since when from the change record
- **parity stated as difference** - the claim was never distinct

Convergence is a fact about the words, not the product. A competitor saying "AI-native" does not make the home product's AI claim false; it makes it generic.

### Step 4 - Check whether differentiation is now parity

Where competitors have converged on the language, ask whether the underlying capability or value still differs. Use current product evidence on both sides. Three outcomes: the words converged and so did the products (real parity); the words converged and the products did not (the message needs sharper proof, not a new claim); or the words diverged and the claim is safe.

### Step 5 - Compare with customer vocabulary and decision criteria

From calls, interviews, reviews, and win/loss: how do customers describe the problem, the outcome they want, and the criteria they decide on? Set the message's words beside theirs. Note:

- terms the message uses that customers never do
- terms customers use that the message never does
- criteria customers decide on that the message does not address
- claims the message leads with that no customer mentioned

Where performance data shows a message working that diverges from interview language, report both. The data measured something; say what, and do not assume the interviews are wrong.

### Step 6 - Sort the claims

Every material claim into one of:

- **differentiated, valued, proven** - keep
- **true but not valuable** - customers do not decide on it; consider demoting
- **valuable but unproven** - customers care, the message asserts, nothing backs it; find or state proof
- **differentiated but irrelevant** - distinct, and no customer evidence it matters; consider demoting
- **generic** - converged; needs sharper proof or a different angle
- **contradicted** - evidence says it is not true; remove

Say the evidence behind each sort.

### Step 7 - Preserve the position

Recommend message changes that serve the existing positioning decision. If the evidence calls the position itself into question - the audience is wrong, the alternative has changed, the differentiator is gone - say that plainly as a finding, and route it. Do not quietly reposition inside a copy review.

### Step 8 - Recommend changes, with evidence and confidence

For each recommended change: what, why, the evidence, and how confident the evidence allows you to be. Suggested wording is welcome where the change is about words; where it is about proof or position, the recommendation is to get the proof or make the decision, not new copy.

### Step 9 - Separate word questions from strategy questions, and hand off

List separately the findings that are really positioning questions, and route them:

| The finding is really | Run |
| --- | --- |
| who this is for, against what, on what basis | `competitive-positioning` |
| how to frame a specific launch | `competitive-launch-readiness` |
| whether the claims across sales assets are supported | `competitive-asset-audit` |
| an internal enablement update | `competitive-enablement-refresh` |
| whether the market convergence is a real shift | `competitive-market-shift-analysis` |
| prospect-facing comparison copy | not yet in this pack; name the page and what it needs |

### Step 10 - Produce the artifact

Use `assets/competitive-messaging-audit-template.md`.

Return it inline, then offer to save it.

## Evidence and reasoning rules

Read `references/TRUST.md` and `references/METHODOLOGY.md`.

Especially for messaging:

- convergence of language is a fact about words; check the products before calling it parity
- customer vocabulary comes from customers - calls, interviews, reviews - not from the team's memory of customers
- performance data measured what it measured; it does not overrule interview language, and interviews do not overrule it
- a claim can be true, distinct, and worthless to the buyer; all three tests apply
- the position is the team's decision; the review tests whether the words carry it
- in bounded-input mode, competitor language and customer vocabulary come only from the supplied material
- the user asking for a rewrite before supplying current messaging gets a request for the messaging, not a rewrite of nothing

## Graceful fallback

Read `references/DEGRADATION.md` and `references/LMTY.md`.

### Fully connected

Competitor language and change history from LMTY, customer vocabulary from calls and research, proof from approved sources, performance from analytics.

### LMTY connected, no customer or performance data

Convergence can be tested; customer-language fit cannot. Say so, and mark every vocabulary finding as untested rather than inferring what customers say.

### Customer data connected, no LMTY

Vocabulary fit can be tested; convergence is checked against current public competitor copy, point-in-time and dated, with no history of when it converged.

### Research mode

Competitor language from current public pages, dated; customer vocabulary from public reviews only, labeled as such. Say the review has no internal customer evidence.

### Bounded-input mode

Use only the supplied messaging and any supplied competitor or customer material, and say so at the top. Do not add competitor claims or customer language from memory. Where a test cannot be run from the material, say which and what would run it.

## References

- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/LMTY.md`
- `references/METHODOLOGY.md`
- `references/QUALITY.md`
- `references/TRUST.md`
