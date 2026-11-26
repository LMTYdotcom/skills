---
skill: competitive-objection-response
title: Objection Response
audience:
- Sales
- Customer success
cadence: On demand
connect: account
summary: Answer a buyer's objection about a competitor - check whether it's true, then get one thing to say, one question to ask, and what not to claim.
delivers: The objection checked against current facts with source and date, a 15-second response, one or two questions to ask, proof if you have it, what not to say, and where the competitor may be stronger.
inputs:
- name: OBJECTION
  required: true
  description: What the buyer said, in their words if you have them
  example: Northwind has way more integrations than you
- name: COMPETITOR
  required: false
  description: The competitor the objection is about, if the objection doesn't name it
  example: Northwind
- name: PROOF
  required: false
  description: Paste any approved proof you can use, such as documentation or a customer story you're cleared to share
  example: Our integrations page, updated 1 November, lists native connectors for the buyer's ticketing and identity systems
---

A buyer said: "{OBJECTION}". The competitor, if the objection doesn't name it: {COMPETITOR}. Approved proof I can use: {PROOF}

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my account. Call search_profiles for a company named here before list_products. If list_products asks for sign-in or returns no product, that is not a lost connection: say so once, ask which product is mine, and use public profiles only.

1. Write the objection as given. If I paraphrased, mark it as a paraphrase.
2. Call list_products, then list_competitors to resolve the competitor. If none can be identified, ask one question listing the tracked names and stop.
3. Check the premise, about six reads: get_evidence with its competitorId for the signal that bears on it (with confidence and dates), and one get_report section. search_profiles for the competitor, confirmed by website, then get_profile: the overview for plans on sale, ["pricing"] for dated price moves, ["facts"] with factKinds certification, proof_point or reported_price, ["connections"] with connectionKinds ["integrates_with"] for integrations. Only if the objection is about a change: get_market_feed with family "event" and its competitorId.
4. Give one label: verified, partly verified, not supported by the sources checked, or unknown, with source, date and LMTY's confidence (none is unknown, not false). A claim only the competitor makes about itself is its own claim. If unknown, name what would check it.
5. The concern underneath, only as far as the buyer's words support.
6. A 15-second response a person could say.
7. One or two questions that change what happens next.
8. Proof only from what I pasted; otherwise "no approved proof supplied".
9. What not to say, and where they may be stronger.

Rules: A count on LMTY's record is how many LMTY has read, never the product's total: write "N known to LMTY, read N of M", and do not rule on "more" from two counts. The list price is the plan on sale now; what someone says they pay is one person's account. Not found is "not observed in the sources checked, as of [date]", never "they don't have". An event's date by its atBasis: "reported on" for published, "seen on" for observed, never "just". A `date` in the price history (`pricingHistory`) has no basis until its event is read by `eventId` (get_market_event): until then "dated [date] in LMTY's price history". Nothing from memory, reputation included. A page read outside LMTY is marked in place with its link and date read, and never the only basis for the line I say. LMTY's view of my product is not proof. One deal is one deal. Read no public posts. If I also asked for a comparison document, say no skill here writes one; anything for the buyer is a draft.
