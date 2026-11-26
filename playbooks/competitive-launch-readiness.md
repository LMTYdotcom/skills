---
skill: competitive-launch-readiness
title: Launch Readiness
audience:
- Marketing
- Product
- Sales
cadence: On demand
connect: account
summary: Check a launch against the competitors that matter, see where it is ahead, level or behind, and which claims will hold up.
delivers: The competitors that matter and why, where the release stands on each point buyers weigh, claims to make and to qualify with their evidence, and up to five gaps to close before launch.
inputs:
- name: RELEASE
  required: true
  description: What is shipping and who it is for, in a short paragraph
  example: Audit log export for admins on the Business plan, so security teams can hand evidence to their auditors
- name: LAUNCH_DATE
  required: false
  description: The day it goes out, if one is set
  example: December 8
- name: COMPETITORS
  required: false
  description: The competitors you want it compared with. Leave empty to pick from the ones you track
  example: Northwind, Initech
---

Check this launch against the competitors that matter: {RELEASE}. Launch date: {LAUNCH_DATE}. Compare with: {COMPETITORS}.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in. Call search_profiles for the competitors I named before list_products. If list_products asks for sign-in or returns no product, that is not a lost connection: read them with get_profile, say there is no tracked set or change history, and ask who our product is if the release does not say. If {RELEASE} is only a feature's name, ask what ships and for whom, and stop.

1. Restate the release as one claim: what changed, for whom, what job it improves.
2. Call list_products, then list_competitors. Use the ones I named, or pick at most 5 that matter for this release. Say why each, how many of the tracked set that is, and who was left out.
3. Call get_report one `section` at a time for the capability, positioning and pricing. Keys: products_capabilities, positioning_differentiators, pricing_packaging. Call get_freshness for each competitor's as-of date.
4. Call get_report_changes with since 90 days back and limit 50, then the next page while nextCursor is not null. Say whether the history reaches that far, and how many were read. A change's date is when LMTY recorded it: write "recorded on".
5. For each picked competitor: get_market_feed with its competitorId, family "event" and `since` 90 days back (on a repeat run, `recordedSince` the last run's date). Then search_profiles (confirm by website), get_profile sections ["timeline", "facts"] for dated launches and its own taglines and proof points, and get_calendar with upcomingOnly for what is announced near the launch date. Word each date by its `atBasis`: occurred is the event's date, published is "reported on", observed is "seen on".
6. For each competitor capability say shipped, announced or only marketed, and who says so: "Northwind's page states", not "Northwind has".
7. Class each dimension as Category expectation, Parity, Differentiated, Catch-up, Unproven or Vulnerable, saying what the label means. Where the competitor side is only silence, write "not observed in the sources read, as of" the date, and class it Unproven.
8. At most 5 claims we can support, each with its evidence and date; at most 5 to avoid or qualify, each with what would make it supportable; at most 5 gaps before launch.
9. Say what was not read. With no source on a competitor I named, say so, and offer once, at the end, to work in what I can paste about it: its pages, release notes, deal notes.

If you have run this before for this release, lead with what moved since then and which posture or claim it changes. An earlier run is one in this conversation or your client's memory: do not search files. With none, this run is the baseline.

Write: Freshness line | The release in customer terms | Decision set (table) | Where the launch stands (table) | Claims to support | Claims to avoid or qualify | Gaps before launch | Not read.

Rules: Nothing about a competitor from memory: every price, plan, date and wording comes from a tool result, from what I gave you, or from a page you read now, marked as your own reading with its link and the date read. What was not found is "not observed", never "has no", "the only" or "first". Never say who shipped first on a recorded or first-seen date. LMTY's `implication` and `significanceScore` are its judgments: cite them as LMTY's. No motive for any competitor. A post or review is one person's account, never "customers expect". Postures and claims are your judgment: give the evidence each rests on.
