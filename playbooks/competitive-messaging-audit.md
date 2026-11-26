---
skill: competitive-messaging-audit
title: Messaging Audit
audience:
- Marketing
- Product
cadence: Quarterly
connect: account
summary: Test whether your homepage or message still sets you apart from what competitors now say, and see which questions are really about positioning.
delivers: Your message laid out by layer, each claim marked still distinct, converged or parity, with competitors' wording quoted and dated, what was not tested, and up to seven changes to consider.
inputs:
- name: MESSAGE
  required: true
  description: Paste the homepage, message hierarchy, pitch or campaign copy to test
  example: Our homepage hero and the three sections under it, pasted below
- name: COMPETITORS
  required: false
  description: The competitors to compare against. Leave it empty to use the ones you track in LMTY
  example: Northwind, Initech
---

Audit this message against what competitors now say. Do not rewrite it.

Message: {MESSAGE}
Competitors to compare against: {COMPETITORS}

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my LMTY account. A sign-in request is not a lost connection: say once that this needs my account, and stop.

1. Call list_products and list_competitors. Lay the message out by layer: category, value, differentiation, proof, call to action, and the audience it seems to address. Note structural findings, such as differentiation with no proof.
2. For each competitor (the ones I named, else the tracked set): get_freshness for its own as-of date, and get_report one section at a time, starting with positioning and differentiators (take the key from the answer).
3. For each one's own wording: search_profiles, confirm by website, then get_profile for the overview, then the facts section with factKinds ["tagline", "category_claim", "proof_point", "boilerplate"], and the terms section. A competitor I do not track is read from its profile alone.
4. For each differentiation and value claim: who else says it, quoted with page and date, out of how many competitors read. Mark it still distinct (not found in the [n] of [m] read, as of their dates) | converged | parity stated as difference.
5. Give "since" only from a date of the wording's own: the earliest known use of a term, the end date of wording it replaced, a dated launch. Otherwise write "on record since [date]; when they began is not known". get_report_changes and get_market_feed with family "event" show what moved, dated by when LMTY recorded or read it: never say who said it first from that order.
6. Where wording converged, do the products still differ? A capability known only from a competitor's own pages is "unknown: their own claim only".
7. Customer fit: test the message's words against calls or interviews I pasted. With none, and if you can open review-site pages now, test against public reviews of my product and these competitors: each quote labeled "third-party opinion: review on [site], [date], one reviewer's account", never "customers say" or a count of customers, and say the customer side rests on public reviews alone. With neither, say it was not tested and what would test it.
8. Up to seven changes to consider, labeled as your judgment, each with its evidence and a confidence with its reason. List separately the findings that are really about the position, for competitive-positioning.

Open with: competitor wording read for [n] of [m] tracked competitors; customer evidence: [what I gave you, or none]; public reviews: [n read and on which sites, or none].

If you have audited this message before, lead with claims whose mark changed since then and wording first recorded since then, reading events with recordedSince from that date. With no earlier run in view, say this one is the baseline.

Rules: Convergence is about words, not products. Quote competitor wording as written, with page and date, and say whether it came from the report or the profile. Nothing from memory: wording or dates only from a tool result, my material or a page read now; a page read outside LMTY is marked as your own reading with its link and date read, and never replaces wording LMTY holds. "Still distinct" is about the competitors read, never the market. A contradicted claim names the source that contradicts it; whether to remove it is my call. Do not re-decide the position, and do not read public posts unless I ask.
