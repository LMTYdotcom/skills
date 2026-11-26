---
skill: social-competitor-change-impact
title: Competitor Change Impact
audience:
- Marketing
- Sales
- Product
cadence: On demand
connect: social
summary: 'See how a competitor''s change is landing in public: who''s reporting problems, who says they''re switching, and who''s unaffected.'
delivers: The change and its date, post counts before and after where collection allows, quoted posts sorted into experience, intent, questions, and opinion, and what it could cause beside what posts report.
inputs:
- name: COMPETITOR
  required: true
  description: A competitor you track in LMTY
  example: Northwind
- name: CHANGE
  required: true
  description: The change to trace
  example: closing the cheapest plan to new customers
---

Show me how this change at {COMPETITOR} is landing in public: {CHANGE}.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in with Social Listening on. If a tool asks for sign-in or says it is off, tell me once and stop.

1. Call list_products and list_competitors: if {COMPETITOR} is not tracked, say its posts were not collected; stop.
2. Date the change: get_market_feed with the competitorId and family "event", then get_market_event for its sources. A published date can be a commentator's: if search_profiles finds {COMPETITOR}, check get_profile sections ["pricing", "changes"] for an earlier one. Use the earliest date a source supports (the first stage if staged); give its source and `atBasis`, and say so if my date differs. Only observed, or only commentators as sources: no before and after, just posts since then. Not in the feed: use my description, date unconfirmed.
3. Count After: get_mention_stats with the competitorId, from 00:00 UTC on the change's day to now, max 30 days. If the answer's `competitorId` is null it counted my whole product: say so, no period counts. Collection began on the latest `since` in `platformsSince` among platforms with a tenth or more of `byPlatform`. No period begins before that or over 90 days back: move After's start there and say so. Before is as long and ends where After begins: if too early, shorten both; if none is left, leave it empty and call nothing a rise or a fall.
4. Show both periods: `totalRelevantMentions`, `distinctAuthors`, `bySentiment`, `byTag`, and a per-day average over whole UTC days of `byDay`, never `windowDays`; a part day is a count with its hours. If a platform with a tenth or more of After has none before, name it, give counts only, call nothing a rise. No percentage if either is under 20; no cause. These are keyword matches, not posts about {COMPETITOR}, and a floor.
5. Read list_mentions with the competitorId over After before shortening: at most 5 pages per filter, never splitting the period. Untagged first: 2 pages if over 5 pages. If `nextCursor` is not null, add the `byTag` tags with most posts that bear on the change. One untagged Before page for topics if Before is comparable. For each, say the hours or days covered and "read N of M": N mentions received, M that filter's count. Keep only posts whose `matchedKeywords` name {COMPETITOR}.
6. Keep posts whose excerpt names the change. Keep as "inferred from timing and content", counted apart, only those describing its direct effect without naming it. Same topic, another reason or none: "same topic, change not named", not reaction; give both counts. Drop tags first_party, directory, promotional_post and ai_generated.
7. Group each kept post once: Reported experience (first-hand, good or bad) | Stated intent (leaving, evaluating, seeking an alternative) | Question | Opinion or prediction | Unaffected or in favor. Quote up to 5 a group, max 200 characters, with platform, date, link and `author`. Write intent as "says they cancelled", never as the act.
8. Table: what a change like this could cause | what posts report, with counts or empty. Say if one thread holds over half.

Rules: a post is one person's account, an author a handle: count posts and authors, never customers. No motive for the competitor, no churn forecast. Nothing found is "not observed in what LMTY collects", never "no reaction". Web search only for the change on {COMPETITOR}'s own pages; never count web posts. Contact nobody: a reply I ask for is a draft. With few or no posts, give only the counts, days read and what was not observed.
