---
skill: competitive-battlecard
title: Battlecard
audience:
- Sales
- Marketing
- Customer success
cadence: On demand
connect: account
summary: Build a battlecard against one competitor - where they're strong, where you differ, what to ask, and when to walk away.
delivers: 'A one-page card: the competitor''s facts with sources and dates, up to three differences, discovery questions, objections only from your deal notes, and what the card is missing.'
inputs:
- name: COMPETITOR
  required: true
  description: The competitor the card is for, as you track it in LMTY
  example: Northwind
- name: SEGMENT
  required: false
  description: The buyers the card is for, if it's for one segment
  example: mid-market IT teams
- name: DEAL_EVIDENCE
  required: false
  description: Paste call notes, win/loss interviews or approved proof. Without them the card leaves out objections and win reasons
  example: 'Three lost deals in Q3: each buyer said Northwind''s audit trail decided it'
---

Build a battlecard for my product against {COMPETITOR}, for {SEGMENT}. My deal evidence: {DEAL_EVIDENCE}

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my account. Call search_profiles for a company named here before list_products. If list_products asks for sign-in or returns no product, that is not a lost connection: say so once, ask which product is mine, and use public profiles only. This prompt reaches no calls, CRM or win/loss: why buyers choose, object and decide comes only from what I pasted above.

1. Call list_products and name my product once.
2. Call list_competitors and match {COMPETITOR} to its tracked name. If it is not tracked, say so and read it from its public profile alone.
3. If tracked: get_competitor (its profile block is for orientation only), get_freshness for its as-of date, get_evidence with its competitorId for confidence and dates, and get_report one section at a time for positioning, pricing and capabilities, taking keys from the answer.
4. Call search_profiles for {COMPETITOR}, confirm it by website, then get_profile: the overview for plans on sale now, sections ["pricing"] for dated price moves, ["facts"] with factKinds tagline, category_claim, proof_point and certification, and ["timeline"]. Where profile and report disagree, give both with dates.
5. Call get_market_feed with family "event" and its competitorId, and get_report_changes with since 90 days back (on a rebuild, the old card's date) and limit 50, then the next page while nextCursor is not null. Say how many were read and the dates they span.
6. Where they are strong: each line says who states it ("per its pricing page", "reported by"). A number only they state is their own claim.
7. Up to three differences, each with source, date and basis (N deals, one deal, or a hypothesis from public differences). None rests on something not found on their side. LMTY's view of my product is not proof.
8. Up to five discovery questions that expose trade-offs, none depending on a claim that they lack something.
9. Objections and win reasons only from what I pasted, with how many calls or deals. Otherwise one line each: what is missing and what would fill it. No "likely" objections.
10. Recent changes, up to five: an event's date by its atBasis ("reported on" for published, "seen on" for observed, never "new"); a report change "recorded on". Skip created changes.
11. When we may not be the best fit, and what the card lacks.

Write a first line saying what was read, then: 30-second read, why us, questions, objections, where they are strong, when we may not fit, recent changes, what the card lacks.

Rules: Nothing about either company from memory. Not found is "not observed in the sources checked, as of [date]", never "they don't have". A page read outside LMTY is marked in place with its link and date read, never replaces a figure LMTY holds, and is never the only basis for a line a rep says. Mark any recommendation as your judgment. Read no public posts. The card is internal: a comparison document for a buyer is not something this writes.
