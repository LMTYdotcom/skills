---
skill: competitive-executive-market-brief
title: Executive Market Brief
audience:
- Marketing
- Leadership
cadence: Quarterly
connect: account
summary: Prepare leadership for a meeting with the few competitor moves that matter, the risks and openings, and the questions to decide.
delivers: A one-page brief - three moves with dates and sources, why each may matter, up to three risks and openings, what is not worth reacting to yet, and the questions for leadership.
inputs:
- name: MEETING
  required: true
  description: Who the brief is for and what the meeting will decide
  example: Q4 board meeting, deciding next year's pricing and launch plan
- name: PRIORITIES
  required: false
  description: Your company's current priorities, pasted in. Without them the brief asks questions instead of linking moves to your plans
  example: Move upmarket to 500+ seat accounts; ship the AI assistant in Q1
- name: PERIOD
  required: false
  description: The period to cover, if not the last 90 days
  example: since July 1
- name: PRODUCT
  required: false
  description: Your product, if your LMTY account has more than one
  example: Acme
---

Prepare an executive market brief for {MEETING}. Our priorities: {PRIORITIES}. Period: {PERIOD}. Product: {PRODUCT}. A blank period is the last 90 days; a blank product is the one on my account.

What this prompt cannot do: it cannot see our deals, calls or roadmap. It links market moves to the priorities pasted above and nothing else. With no priorities pasted, say so in the first line, and write decision questions, not recommendations.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my account. A sign-in request is not a lost connection: say once that this needs my account, and stop.

1. Call list_products, then list_competitors and get_freshness. With several products and none named, list them in one line and stop.
2. Call get_report_changes with since at the period start and limit 50, then the next page while nextCursor is not null; skip `created` entries. Call get_market_feed with family "event" and since at the period start, paging to the end. If an earlier brief of this kind is visible and the period starts where it ended, use recordedSince there, not since: an event LMTY found late has an older date of its own. If the server ignores recordedSince, read the last 30 days with since and drop the eventIds that brief listed. Say how many of each you read, back to which date, and which competitors were not refreshed in the period. If the latest refresh is more than a week before the period ends, give its date in the first line and say nothing after it is covered.
3. Pick the three items that touch the priorities, or without them that rank highest on business impact, evidence strength, time sensitivity and how costly a wrong call would be. Say the selection is yours and what decided it.
4. For each, call get_evidence or get_market_event, and read the competitor's public profile (search_profiles, then get_profile with sections ["timeline", "pricing"]) for a date of the move's own and its values.
5. Write: a Read line with the counts; the answer in 3 to 5 sentences; three items, each with what happened (who says it, the date and how it is known), why it matters marked as your reading, the source, and a decision question naming the evidence that would answer it.
6. Then at most three risks, each tied to an item; at most three openings, worded as hypotheses; what is not yet worth reacting to, which is the only place for an item resting on one unverified post, with what would settle it; an appendix of claim, source, date and confidence.
7. If nothing in the period touches the priorities, say so in one sentence and give only what is not worth reacting to and the questions that stand regardless.

Rules: A change record's asOf is when LMTY recorded it: "recorded on". It does not place a move in this quarter. Word an event's date by atBasis: occurred is when it happened, published "reported on", observed "seen on". LMTY's significance and implication are its judgments, cited as LMTY's. No motives. No "we should" or "do not": write the decision and the evidence it needs. A competitor's own figure is its claim. "No change recorded" is not "stable". Nothing from memory. A fact you read outside LMTY is marked "my own read of [page], [date]" and never replaces the record. One page; two for a board.
