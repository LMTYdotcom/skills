---
skill: competitive-enablement-refresh
title: Enablement Refresh
audience:
- Marketing
- Sales
cadence: On demand
connect: account
summary: Update a battlecard or talk track after a competitor changes something, with proof and a date for every new line.
delivers: The change and how its date is known, each claim in your card marked current, stale, unsupported or incomplete, new lines with their proof and date, and what can stay as it is.
inputs:
- name: ASSET
  required: true
  description: Paste the battlecard, talk track or deck section to update
  example: Our Northwind talk track, pasted below
- name: COMPETITOR
  required: true
  description: The competitor the asset is about, as you track it in LMTY
  example: Northwind
- name: CHANGE
  required: false
  description: The change that prompted this, if you know it. Leave it empty to have recent changes checked
  example: Northwind raised its Standard plan price
---

Update this enablement about {COMPETITOR} so it is true again, changing only what the evidence requires.

Asset: {ASSET}
Change that prompted it: {CHANGE}

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my LMTY account. Call search_profiles for {COMPETITOR} before list_products. A sign-in request is not a lost connection: say once that this needs my account, and stop. I have pasted the asset, so field questions and whether reps open it were not checked: say so in one line. If the asset carries no last-updated date, ask me for it; if I do not know, read back 90 days and say so.

1. Call list_products and list_competitors to resolve {COMPETITOR}. Pull the claims out of the asset as short statements, one per claim.
2. Call get_report_changes with since at the asset's last-updated date and limit 50, then the next page while nextCursor is not null, and keep the entries about {COMPETITOR}; then get_market_feed with family "event" and its competitorId. Several entries about one move are one change. Say how far back you read.
3. For what is true now: get_freshness for its as-of date, get_report one section at a time, get_evidence for proof and dates. For a price, plan, certification or customer line: search_profiles, confirm by website, then get_profile (overview for plans on sale, pricing for the price history with before-and-after values).
4. Class each claim current | stale | unsupported | incomplete, with why. Stale needs the change that staled it. Claims about our own product are "not checked" unless I pasted approved proof. One that my approved proof denies is unsupported, with the reason "denied by the approved claims" first, and gets no new line, not even "once approved...".
5. Order the lines by what it would cost a rep to say the old one to a buyer today. Say the order is your judgment.
6. For each line to change: Was | Now | Proof | Date, and how it is known. The change's own date only where an event's atBasis is occurred, or the price history or announcement states it; "reported on" for a published date; "LMTY recorded it on" for a report change. Where a new line reverses an old one, add a history note that never says "on [date] they did" from a recorded date.
7. List what stays unchanged (up to ten lines). If no claim is touched, say so in one sentence and stop.

Start with: changes read back to [date], [n] entries; [n] claims in the asset.

Rules: A new line says no more than its evidence. A plan, logo or page no longer shown is "no longer listed as of [date]", never "removed", "dropped" or "churned". Nothing from memory: a figure or date comes only from a tool result, my material or a page read now; a page read outside LMTY is marked as your own reading with link and date read, never replaces what LMTY holds, and never alone carries a line a rep will say. What a competitor says about itself is worded as their statement, with page and date. If a line I want cannot be supported, give the supportable version; do not soften it into a vaguer claim. Posts count as what posts say, never as what customers do.
