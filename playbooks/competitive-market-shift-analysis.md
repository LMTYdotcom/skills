---
skill: competitive-market-shift-analysis
title: Market Shift Analysis
audience:
- Marketing
- Product
- Leadership
cadence: On demand
connect: account
summary: Test whether a trend you are seeing across competitors is real, how far the evidence goes, and what would change the answer.
delivers: A verdict from noise to established expectation, with the bar it did not clear, a dated list of signals, what would prove it wrong, and three signals to watch next.
inputs:
- name: HYPOTHESIS
  required: true
  description: The trend you want tested, in your own words
  example: Everyone is moving AI features into their base plans
- name: COMPANIES
  required: false
  description: Companies to include beyond your tracked competitors, or the ones to read if you are not signed in
  example: Northwind, Initech
- name: BUYER_EVIDENCE
  required: false
  description: What your buyers have said or done about it, pasted in - call notes, lost-deal reasons, survey answers
  example: 4 of the last 20 enterprise RFPs asked for AI in the base plan
---

Tell me whether this is a real market shift: {HYPOTHESIS}. Also read: {COMPANIES}. Buyer evidence: {BUYER_EVIDENCE}.

What this prompt cannot do: it cannot see our deals or calls. LMTY holds no buyer evidence, so without buyer evidence pasted above the verdict cannot pass "Emerging shift". Say so in the first lines when that is the case.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`).

1. Restate the hypothesis as one falsifiable sentence and say the framing is yours. Go on without waiting.
2. For each company in the pattern, call search_profiles, confirm it by its website, and call get_profile with sections ["terms", "timeline", "pricing"] (add "hiring" or "statements" when the hypothesis is about those). Then call list_products and list_competitors; if they ask for sign-in or return nothing, that is not a lost connection: work from the companies named above.
3. Signed in: call get_report_changes with since at the period start and limit 50, then the next page while nextCursor is not null, and get_market_feed with family "event", paging to the end. Say how many records you read, back to which date, and K of M companies read. A company not read is "not read". If the oldest get_recent_activity entry, paged to the end, falls inside the period, say first that LMTY's record begins on that date.
4. Build a ledger of at most 12 signals: date and how it is known, signal, source, independent or not, evidence quality. Merge signals that trace to one event. Include signals from outside the tracked set, and say the analysis was not restricted to it.
5. Classify, starting at Noise. Isolated move: one credible dated signal. Emerging shift: independent subjects, and at least one signal from a source other than the vendors themselves (press, an analyst, a customer); a vendor's own page, docs or post is a vendor source, so several vendors each describing their own move stay Isolated move. Accelerating: that plus buyer-side evidence. Established: buyers screen for it. Cap at the weakest link.
6. Say which bar was not met and what would clear it, what would falsify the reading, and three signals to watch with where to look and when.

Rules: A change record's asOf is when LMTY recorded it, and an observed date is when LMTY first saw a thing: both count toward how many players have it, never toward timing or "accelerating". A reported-on date places the report, not the move, and shows no sequence. Say how many signals have a date of their own. A vendor's page is primary for what it offers and charges; what it says about its customers is its own claim, never buyer evidence. Posts are people saying something: count posts and authors, never customers. Noise means the evidence read shows no pattern, not that there is none. No motives. Name decisions; do not make them. Nothing from memory. A signal you read outside LMTY is marked "my own read of [page], [date]" in its source and never alone lifts the verdict.
