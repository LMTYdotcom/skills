---
skill: competitive-market-briefing
title: Market Briefing
audience:
- Marketing
- Sales
- Product
cadence: Weekly
connect: account
summary: Brief your team on what changed across your tracked competitors this week, ranked, with a date and a source for each item.
delivers: Up to three items, each with what changed, its date and source, and why it may matter; a short watchlist; the competitors with nothing new; and how much was read.
inputs:
- name: PRODUCT
  required: false
  description: Your product, if your LMTY account has more than one
  example: Acme
- name: PERIOD
  required: false
  description: The period to cover, if not the last 7 days
  example: the last 30 days
---

Brief me on what changed across my product's tracked competitors. Product: {PRODUCT}. Period: {PERIOD}. If either is blank: the one product on my account, the last 7 days.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my account. A sign-in request is not a lost connection: say once that this needs my account, and stop. Call list_products first. With several products and none named, list them in one line and stop. With none, ask which product and competitors to cover, and stop.

1. Look for the last briefing in this conversation or your client's memory; never search files. With one, start the period where its "Covered" line ends. With none on a scheduled run, open with "The previous briefing could not be seen: this covers [dates]" and use no continuity labels.
2. Call list_competitors, get_freshness and get_recent_activity. Note competitors not refreshed in the period, paused refreshes, and competitors added in it: their records are first captures, not changes. LMTY's record begins at the oldest get_recent_activity entry, paged to the end: if that is inside the period, say so in the first line, and what LMTY captured that day is what it held, not a change.
3. Call get_market_feed with family "event" and recordedSince at the period start, paging until nextCursor is null. Say "N events read". If the server ignores recordedSince, read the last 30 days with since and drop the eventIds the last briefing listed.
4. Call get_report_changes with since at the period start and limit 50, then the next page while nextCursor is not null. Skip `created` entries. Say how many you read and back to which date. If you stop sooner, the period is what you reached.
5. Merge entries about one change. Leave out what the last briefing reported unless it moved. Before calling an item new, check that competitor's earlier change records and profile timeline; if they hold it, say when LMTY first recorded it. Rank by relevance to my product, magnitude, novelty, time sensitivity and evidence quality, and say the order is yours.
6. At most 3 items (5 for a month). Each: what the source says, its date and how it is known, the source link (get_market_event or get_evidence), and why it may matter, marked as your reading. For a date of its own and before and after values, read the competitor's public profile: search_profiles, confirm by its website, then get_profile with sections ["pricing", "timeline"].
7. At most 3 watchlist items. Then each competitor with no change recorded, with its last refresh date.
8. End with "Covered: [start] to [end, UTC]. Event ids reported: [ids]." Nothing follows it.

If nothing new was recorded: the period, the coverage line, "No change recorded since [date]", the competitors not refreshed, the Covered line, and stop. If nothing was refreshed in the period, give the last refresh of the report and of each competitor after the period line, say the period is not covered, and end the Covered line at the latest refresh.

Rules: A change record's asOf is when LMTY recorded it: write "recorded on". Word an event's date by atBasis: occurred is when it happened, published is "reported on", observed is "seen on" and never "new" or "this week". LMTY's significance and implication are its judgments: quote them as LMTY's and never rank on them. No motives. "No change recorded" is never "quiet" or "stable". A competitor's claim about itself is its statement. Nothing from memory. A fact you read outside LMTY is marked "my own read of [page], [date]" with its link, and never replaces the record. Under 400 words outside the table.
