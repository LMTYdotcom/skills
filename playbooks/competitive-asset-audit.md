---
skill: competitive-asset-audit
title: Asset Audit
audience:
- Marketing
- Sales
cadence: Quarterly
connect: account
summary: Check the competitive claims in your battlecards, decks or pages against current evidence, and see which to fix first.
delivers: Each claim marked current, stale, unsupported, contradicted or unknown, with its source and date, ranked by who sees it and what it costs if acted on, and who should fix it.
inputs:
- name: ASSETS
  required: true
  description: Paste the battlecards, decks or pages to check, or give their public web addresses
  example: Our Northwind battlecard, pasted below
- name: APPROVED_FACTS
  required: false
  description: Your approved facts about your own product, such as prices, certifications and references. Without them, claims about your product are marked unknown
  example: SOC 2 Type II since March 2026; Pro plan $12 per user
---

Check the competitive claims in these assets against current evidence and list how each holds up. Rewrite nothing.

Assets: {ASSETS}
Approved facts about our product: {APPROVED_FACTS}

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my LMTY account. A sign-in request is not a lost connection: say once that this needs my account, and stop. This audits what I gave you, not every asset we have: say so in the first line.

1. Call list_products and list_competitors. List the material claims (a buyer or rep could act on them; framing is not a claim), one entry per claim with every asset it sits in. A claim that varies across assets is a finding.
2. For each competitor named: get_freshness for its own as-of date, get_report one section at a time for the claim's subject, get_evidence for source, confidence and dates. Confidence none is unknown.
3. For a price, plan, certification, customer or wording claim, and for a competitor I do not track: search_profiles, confirm by website, then get_profile with the sections the claim needs (overview for plans on sale, pricing for the price history, customers, facts for taglines and proof points). Where profile and report differ, give both with dates.
4. Mark each claim supported and current | supported but stale | unsupported | contradicted | unknown, with source and date. A figure behind a newer source is stale when the asset is older than the source. Unsupported only when a full list for its kind (approved claims, references, prices) is silent; a partial source that is silent means unknown. Claims about our product are unknown without approved facts, and contradicted, not unsupported, when the approved facts deny them. A supported claim whose only voice is the party it flatters is that party's own claim: say whose.
5. Always call get_report_changes with since at the oldest asset's date and limit 50, then the next page while nextCursor is not null, and get_market_feed with family "event" for each competitor. A report change is dated by when LMTY recorded it: write "recorded on". An event's date is the change's own only when atBasis is occurred; published is "reported on", observed "seen on". Several entries about one move are one change. With no change found, write "no dated change found between [date] and [date]", never "always weak".
6. Rank what needs attention by how many people see it and what acting on it costs, and say the order is your judgment. Name who should fix each.

Open with: read [n] of [m] assets; evidence checked for [n] of [m] competitors; changes read back to [date], [n] entries. Then a count by mark, the ranked claims (up to ten), the rest by mark, and one row per competitor with its as-of date.

If you have audited these assets before, lead with claims that changed standing since then, reading events with recordedSince from that date. With no earlier run in view, say this one is the baseline.

Rules: No mark is a guess: never "likely holds" or "probably true"; say what was checked and what would settle it. Nothing from memory: a competitor's price, plan, customer, certification or date comes only from a tool result, my material, or a page read now. A page read outside LMTY is marked as your own reading with its link and date read, never replaces a figure LMTY holds, and is never the only basis for stale or contradicted. Not found is "not on LMTY's record as of [date]", never "they have no" or "removed". A public post never supports a claim about customers or how many.
