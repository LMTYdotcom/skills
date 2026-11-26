---
skill: competitive-pricing-packaging-review
title: Pricing and Packaging Review
audience:
- Marketing
- Product
- Leadership
cadence: On demand
connect: account
summary: Compare your pricing and packaging with the competitors that matter, and get the questions to settle before you change a price.
delivers: What each competitor lists today and how its prices have moved, with dates, where your offer is ahead or exposed, up to five hypotheses to test, and up to five questions for the pricing team.
inputs:
- name: DECISION
  required: true
  description: The pricing or packaging question you are deciding
  example: Whether to respond to Northwind's lower entry price
- name: HOME_PRICING
  required: false
  description: Your current plans and prices, or the change you are proposing. Paste them in
  example: 'Starter $20 per seat a month, Business $45, Enterprise on request'
- name: COMPETITORS
  required: false
  description: The competitors to compare with. Leave empty to pick from the ones you track
  example: Northwind, Initech
---

Review our pricing and packaging for this decision: {DECISION}. Our pricing: {HOME_PRICING}. Compare with: {COMPETITORS}.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in. Call search_profiles for a company named here before list_products. If list_products asks for sign-in or returns no product, that is not a lost connection: read the competitors I named from their public profiles, say there is no tracked set or change history, and take our offer from what I pasted.

1. Say what kind of decision this is: a scan, a reaction to a competitor move, a new price point, a packaging redesign, a free-to-paid boundary, an entitlement, a segment offer or launch pricing.
2. Call list_products and list_competitors. Use the ones I named, or pick at most 6 that matter; say how many of the tracked set that is and who was left out.
3. For each, call search_profiles for the product (prices sit on the product, not the company; confirm by website), then get_profile for the overview: the `pricing_plan` facts are the plans on sale, with the date last seen. Write prices as listed; do not convert units.
4. Call get_profile with sections ["pricing"] and page with offset until `more` is empty: the history is under `pricingHistory`, as `changes` and `ended`. A change's `date` has no basis: read its event by `eventId` (get_market_event) to learn whose date it is (the move's own, "reported on", or "seen on"); otherwise write "dated [date] in LMTY's price history". Say where each record begins. A plan first seen on a date was not introduced on it. Write "no change observed between" two dates, never "has not changed".
5. Call get_report with `section` "pricing_packaging", and get_report_changes with since at the start of the period I care about and limit 50, then the next page while nextCursor is not null, saying how far back you read. A change's date is when LMTY recorded it: write "recorded on".
6. Build the offer map. A capability the pricing page does not mention is "not listed on the pricing page as of" the date; a plan with no public price is "contact sales: no public price"; no pricing on record is "not observed", never "none", "free" or "custom". What people report paying (`reported_price`) goes in a note, never in a price cell.
7. Mark where our offer is a price advantage, value advantage, clearer packaging, exposed (and against whom), intentionally premium, or a false comparison, with the evidence for each.
8. At most 5 hypotheses, each with the internal evidence that would confirm or reject it, and at most 5 decision questions.
9. Say what was not read.

Write: Freshness line | Offer map (table) | Moves (table) | Our offer | Hypotheses | Decision questions | Limitations.

Rules: No price, plan or limit from memory, however well known the vendor: each comes from a tool result, from what I pasted, or from a page you read now, marked as your own reading with its link and the date read, and never in place of a price LMTY holds. A list price is what a page said on a date, not what anyone paid. No motive for a competitor's price move. Without our margins and deal data, do not answer yes or no: "do not match" and "hold" are recommendations too. Open with what the evidence shows and the question it leaves, and what would settle it. Hypotheses and diagnoses are your judgment: give the evidence each rests on.
