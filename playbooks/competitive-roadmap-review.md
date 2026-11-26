---
skill: competitive-roadmap-review
title: Roadmap Review
audience:
- Product
- Marketing
cadence: Quarterly
connect: account
summary: Turn what competitors did in one product area, and what your customers say, into questions product can investigate, with what is still unknown.
delivers: What competitors did in the area, with dates, your customer evidence beside it, and up to seven questions, each marked as expected, a chance to stand out, noise, or not yet known.
inputs:
- name: PRODUCT_AREA
  required: true
  description: The part of your product to review
  example: reporting and dashboards
- name: CUSTOMER_EVIDENCE
  required: false
  description: What your customers have said or done about this area. Paste feature requests, interview notes or usage figures, with how many you looked through
  example: 'Reporting came up in 6 of 40 support tickets in October; 3 of 12 lost deals named it'
---

Review {PRODUCT_AREA} against what competitors did and what our customers say. Our customer evidence: {CUSTOMER_EVIDENCE}.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in. Call search_profiles for any competitor I name first. If list_products asks for sign-in or returns no product, that is not a lost connection: read their public profiles, say there is no tracked set, and ask which product is ours. LMTY holds the market side only: our customers' side is what I pasted. Without it, every question is an evidence gap.

1. Restate the area as the customer need it serves, not as a competitor feature.
2. Call list_products and list_competitors. Say how many of the tracked set you read.
3. Call get_report with the `section` that covers the area (products_capabilities, positioning_differentiators, pricing_packaging, gtm_motion, partnerships_ecosystem, customers_solutions or compliance_trust), then get_report_changes with since about a quarter back and limit 50, then the next page while nextCursor is not null; say whether the history reaches that far and how many were read. A change's date is when LMTY recorded it: write "recorded on".
4. For each tracked competitor: get_market_feed with its competitorId, family "event" and since a quarter back (on a repeat run, `recordedSince` the last run's date), judging each event by its content: search matches words literally and misses a release named otherwise, so use it only to narrow. For each that moved, call search_profiles (confirm by website) and get_profile sections ["timeline", "pricing", "hiring"]. Say shipped, announced or only marketed, the plan it landed in, and each date by its `atBasis`: occurred is the event's date, published is "reported on", observed is "seen on".
5. Say whether order of movement can be established. On recorded or first-seen dates write "order not established" and do not say who followed whom.
6. Set my customer evidence beside it, counted, with how many were searched and what that sample cannot speak to.
7. At most 7 questions, each a customer problem, never "build X". Mark each: table-stakes risk (needs evidence that its absence costs deals or renewals), differentiator opportunity, copycat noise (competitors moving, no buyer evidence), or evidence gap. If our product meets the need differently and my evidence supports that, say so; it is not a gap.
8. For each, the evidence missing before anyone could prioritize it. Do not rank the questions.
9. Say what was not read.

If you have run this before for {PRODUCT_AREA}, lead with competitor movement since then and any question whose mark changed. An earlier run is one in this conversation or your client's memory: do not search files. With none, this run is the baseline.

Write: Read line | Market signals (table) | Our customer evidence | Questions (table: question, mark, evidence, evidence missing) | Not read.

Rules: Nothing about a competitor from memory: each move comes from a tool result, from what I pasted, or from a page you read now, marked as your own reading with its link and the date read. How hard a vendor sells something (its pricing page, a tier gate, its own customer stories) is its own claim, not buyer evidence. A review or post is one person's account: count reviews, never buyers, and label a review "third-party opinion: review on [site], [date], one reviewer's account". Never infer our customers' demand from competitors. "Competitors have not solved it" needs a source; otherwise "not observed in the sources read". No motive for any competitor. Every mark is your judgment: give its evidence.
