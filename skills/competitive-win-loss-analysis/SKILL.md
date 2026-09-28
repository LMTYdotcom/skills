---
name: competitive-win-loss-analysis
description: Explain repeated competitive outcomes - why deals are won or lost against a competitor or across a period - from buyer and deal evidence rather than rep folklore, with the cohort defined, buyer-stated reasons separated from rep-entered ones, patterns counted without erasing the cases that contradict them, sample size and bias labeled, and hypotheses to test instead of invented causes. Use for "why are we losing to X", "analyze our wins and losses", "what do buyers actually say when they choose them", "is this objection really costing us deals", and any question about outcomes across more than one deal. Not for one competitor's public profile, one deal's prep, or one objection's response.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Win/Loss Analysis

## Mission

Tell the truth about why deals are won and lost against competitors, from what buyers said and what the record shows, at the resolution the evidence supports and no finer.

The output separates what buyers said from what reps wrote, counts what repeats without hiding what does not, says how big and how biased the sample is, connects outcomes to market changes only when the timing holds, and ends with hypotheses worth testing rather than a cause the evidence did not establish.

## Use this skill when

- someone asks why the company is losing, or winning, against a named competitor
- a team wants wins and losses over a period analyzed
- a PMM wants to know what buyers actually say when they choose or reject the home product
- someone asks whether a recurring objection is actually costing deals
- a recurring claim in the field - "we always lose on price to X" - needs checking against the record
- a request bundles the analysis with a positioning decision or an objection script - do the analysis, route the rest (Step 10)

## Do not use this skill when

- the user wants to understand a competitor from public and market evidence rather than from deal outcomes. Use `competitive-deep-dive`.
- the job is preparing one account for its next meeting. Use `competitive-deal-prep`.
- the user needs words for one objection now. Use `competitive-objection-response`.
- validated findings are in hand and the question is what position to take. Use `competitive-positioning`.
- the question is whether a market pattern is real, independent of this company's deals. Use `competitive-market-shift-analysis`.

## Required outcome

For the cohort the user cares about, answer:

1. Which deals, over which window, and how good is the evidence for each?
2. What reasons for winning repeat, in buyers' words?
3. What reasons for losing repeat, in buyers' words?
4. What is specific to each competitor?
5. Which decision criteria show up, and in what order for buyers?
6. Where do buyer-stated reasons and rep-entered reasons disagree?
7. What changed over the window, and does any market change line up with it?
8. What is the sample size, and how is it biased?
9. Which hypotheses are worth testing, and what would test them?
10. What does this imply for other PMM work, and who owns each implication?

## Context acquisition

Read `references/CONTEXT.md` and `references/INTERNAL.md`.

### Irreducible minimum

- home product
- a deal evidence set, or permission and a connected source to retrieve one

Retrieve before asking. When win/loss research, call intelligence, or opportunity data is connected, define the cohort from the user's question - competitor, window, segment - and pull it. Do not ask the user to list the deals.

A single deal can be analyzed as a single deal. It must not be presented as a pattern, and the output must say it is one observation.

If no deal evidence is connected and the user supplied none, say the analysis cannot be done from market data alone, name what would be needed - interviews, call transcripts, closed-won and closed-lost records with competitor fields - and offer to proceed on whatever they can paste.

### Strongly preferred context

- win/loss interviews: buyer quotes and interviewer paraphrase, separately
- call transcripts from the deals, especially the decision call
- opportunity records: outcome, competitor field, stage history, segment, value, dates, rep-entered reasons
- rep notes
- LMTY report and changes covering the window, for what the market did while the deals ran
- home-product pricing, packaging, and product changes during the window

## Source priority for this job

1. the buyer's own words - interview quotes, decision-call transcripts - for why they decided
2. interviewer paraphrase and call summaries, labeled as such
3. opportunity records for outcome, competitor, segment, and dates
4. rep-entered loss and win reasons, as evidence of what the team believed
5. market state and changes during the window, for context, never for cause on their own

## Workflow

### Step 1 - Define the cohort and window

State: which outcomes (won, lost, no decision), which competitor or competitors, which segment or motion, which dates, and why those bounds. Say how many deals the cohort holds and how many have buyer evidence versus record-only.

If the user's framing is "why are we losing to X", the cohort is deals against X - both outcomes. Losses without the wins cannot say what differs.

### Step 2 - Normalize identity and outcome

Reconcile competitor names across sources (the CRM's "Northwind Corp", the call's "Northwind Track", the interview's "their current tool"). Reconcile outcomes: a "closed lost" whose buyer chose nothing is a no-decision, not a competitive loss. Note deals whose competitor is unrecorded or ambiguous and keep them in a separate bucket.

### Step 3 - Separate buyer-stated from rep-entered reasons

For each deal, list reasons in two columns: what the buyer said (source, date) and what the rep recorded (field, date). Do not merge them.

Where only one column exists, say so. A deal with a rep reason and no buyer evidence is a deal whose reason is unknown.

### Step 4 - Extract decision criteria and objection themes

From the buyer column, code the criteria and objections that appear, in the buyer's vocabulary. Keep the buyer's ordering when they gave one ("first speed, then integrations, then price").

Code the rep column the same way, separately.

Keep the buyer's specific mechanism when coding. Three losses a rep would all call "familiarity" may be three different things - the security paperwork already on file, the team already trained, the compliance function already trusting the incumbent - with three different responses. Flattening them into one theme makes the count look stronger and the finding weaker.

### Step 5 - Count what repeats, and keep what contradicts

Count each criterion and theme across deals: appears in N of M deals with buyer evidence. Show the counts. Then show the cases that run against each pattern - the deal lost on price where the buyer said price did not matter, the win where the "usual" advantage was absent.

A pattern is a count with its exceptions attached. A pattern with its exceptions removed is a story.

### Step 6 - Segment when the sample supports it

Split by segment, size, motion, use case, or stage only when each bucket has enough deals with buyer evidence to say anything. Say the threshold you used. Two deals in a bucket is two deals, not a segment finding.

### Step 7 - Connect to market changes only when timing holds

Lay the window against LMTY's change record and the home product's own changes. A market change may explain outcomes only if it happened before the affected deals decided, and the buyer evidence mentions it or its effect. A competitor price cut in September does not explain a loss in June. Say when the timing does not hold.

### Step 8 - Locate the evidence across the usual causes

For each of product, positioning, sales execution, price, implementation, trust, and incumbency: where does the buyer evidence put weight, where does the rep evidence put weight, and where do they disagree? The disagreement column is usually the finding.

### Step 9 - Label the sample

State: total deals, deals with buyer evidence, deals record-only, the window, and every bias you can see - enterprise-heavy, one region, only deals a particular rep flagged, only losses interviewed, interviews conducted by the vendor rather than a third party. Say what the sample cannot speak to.

### Step 10 - Hypotheses, implications, and handoffs

Frame what the evidence suggests as hypotheses with the test that would settle each: more interviews in a segment, a specific question added to discovery, a check of a product claim. Do not write causes the evidence did not establish.

When the user has bundled a second job onto the analysis - a script for the repeated objection, a positioning call - deliver the analysis and route the second job by name. Do not append a draft of it; a script written at the bottom of a win/loss report has had none of the checks the objection skill applies.

Then implications, each routed:

| Implication | Run |
| --- | --- |
| a repeated objection needs a field response | `competitive-objection-response` |
| validated findings should change the position | `competitive-positioning` |
| a competitor needs understanding beyond these deals | `competitive-deep-dive` |
| pricing or packaging appears in the buyer evidence | `competitive-pricing-packaging-review` |
| enablement is teaching what the buyer evidence contradicts | `competitive-enablement-refresh` |
| a market pattern may be real beyond our deals | `competitive-market-shift-analysis` |

### Step 11 - Produce the artifact

Use `assets/win-loss-template.md`.

Return it inline, then offer to save it. Account names and contract values appear only where the reader needs them; quotes are attributed by role, not name, unless the user's audience already has access.

## Evidence and reasoning rules

Read `references/TRUST.md` and `references/METHODOLOGY.md`.

Especially for win/loss:

- the buyer's words are the evidence for why the buyer decided; the rep's field is evidence of what the rep believed
- three deals are three observations
- correlation across a window is not cause; a market change explains a deal only if it preceded it and the buyer connects them
- a pattern's exceptions are part of the pattern
- interviews the vendor conducted are biased toward what the buyer was willing to say to the vendor; say so
- a loss reason of "price" recorded by a rep is the most common folklore in the field, and the buyer evidence usually says something else; check every one
- an interviewer's paraphrase is the interviewer's

## Graceful fallback

Read `references/DEGRADATION.md` and `references/LMTY.md`.

### Fully connected

Cohort from records, reasons from interviews and calls, market context from LMTY.

### Internal sources connected, no LMTY

The analysis proceeds; market context comes from what the buyers said and public evidence. Say there is no tracked record of what the market did during the window.

### LMTY connected, no internal sources

There is no deal evidence to analyze. Say so plainly. Offer what LMTY can say - what changed in the market over the window - as context for an analysis the user could run once evidence is available, not as a substitute for it.

### Bounded-input mode

Use only the supplied deals and documents, and say so at the top. The cohort is exactly what was supplied; label it as such and name its biases. Do not add market changes, competitor facts, or "typical" reasons from memory.

## References

- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/LMTY.md`
- `references/METHODOLOGY.md`
- `references/QUALITY.md`
- `references/TRUST.md`
