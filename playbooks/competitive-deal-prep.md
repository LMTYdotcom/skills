---
skill: competitive-deal-prep
title: Deal Prep
audience:
- Sales
cadence: On demand
connect: account
summary: Prep for the next meeting on one competitive deal - who you're up against, what the buyer said matters, and the three questions to answer.
delivers: Who is in the deal and on what evidence, the buyer's priorities in their words, the competitor's side with dates, the three questions for the meeting, proof to bring, and the risks.
inputs:
- name: ACCOUNT
  required: true
  description: The account or opportunity you're preparing for
  example: Globex
- name: DEAL_NOTES
  required: true
  description: Paste what you have on the deal - what the buyer said and who said it, the stage, the next meeting. The prep can only be as good as these notes
  example: 'Discovery call 12 Nov with Globex IT lead: "if we can''t pass the security review nothing else matters". Next meeting Thursday with procurement.'
- name: COMPETITORS
  required: false
  description: The competitors you believe are in the deal, if you know
  example: Northwind
---

Prep me for the next meeting on the {ACCOUNT} deal. Competitors I believe are in it: {COMPETITORS}. My notes:

{DEAL_NOTES}

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my account. Call search_profiles for a company named here before list_products. If list_products asks for sign-in or returns no product, that is not a lost connection: say so once, ask which product is mine, and use public profiles only. This prompt cannot reach my CRM or call recordings: the deal side comes only from my notes above. If {ACCOUNT} names no account ("a bank" is a kind of company, not an account), ask which account and stop. If my notes hold nothing the buyer said, give the short form and say so in its first line: the deal as I report it, who is in it, the three questions, risks and unknowns, competitor changes, and before the meeting. No criteria, objections or proof list.

1. Call list_products and name my product once.
2. Who is in the deal, from my notes, each with its evidence: buyer named it, CRM field, my note, or assumed. A vendor listing {ACCOUNT} as a customer is its claim: assumed, and a question.
3. Call list_competitors to match each to its tracked name. One not tracked: search_profiles, confirmed by website, and say it was read from its profile alone.
4. Quote what the buyer said, with who and when. Split criteria into confirmed by the buyer and assumed by the team; where my notes disagree, show both.
5. Per tracked competitor: get_evidence with its competitorId and get_freshness for its as-of date; get_report only for sections bearing on the confirmed criteria. From get_profile: sections ["pricing"], ["facts"] with factKinds certification, and ["timeline"]. Say where it is stronger, where we are (with proof from my notes only), and where neither is known. A strength only it states is its own claim.
6. get_market_feed with family "event" and its competitorId, and get_report_changes with since at the last meeting and limit 50, then the next page while nextCursor is not null. Keep only changes this account would notice, up to five, with N of M read.
7. The three questions the meeting must answer: which requirement is hard, who decides and against what, what the buyer already believes about a competitor.
8. Objections only if my notes show this account raised them. Proof only from what I pasted, otherwise "no approved proof".
9. Risks and unknowns, never empty, and a short checklist for before the meeting.

Write a first line saying what was read (my notes, which competitors, how many changes, as-of dates), then the prep.

Rules: The buyer's words outrank my notes about them. Nothing about the buyer, the competitor or past deals from memory. Not found is "not on LMTY's record" or "not observed, as of [date]", never "they don't have". An event's date by its atBasis: "reported on" for published, "seen on" for observed, never "new"; a report change "recorded on"; skip created changes. A page read outside LMTY is marked in place with its link and date read, and never replaces a figure LMTY holds. Mark recommendations as your judgment. One deal is one deal.
