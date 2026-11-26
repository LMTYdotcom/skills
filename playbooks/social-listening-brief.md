---
skill: social-listening-brief
title: Social Listening Brief
audience:
- Marketing
- Product
- Leadership
cadence: Weekly
when: "Weekly, on a schedule if you prefer. A repeat run should start with what changed since the last brief, and say so when there's no earlier one to compare with."
connect: social-optional
summary: "Brief your team on what people posted this week about your product, your competitors, and your category, plus what needs attention."
delivers: "How many posts and authors there were for your product and each competitor, up to 5 themes with linked excerpts, any dated events that fell on the same days, the questions people ask, and up to 5 things that need attention."
inputs:
- name: PRODUCT
  required: true
  description: Your own product
  example: Acme
- name: COMPETITORS
  required: false
  description: "If you're not signed in, up to two competitors to read"
  example: Northwind, Initech
---

Brief me on what people posted in public about {PRODUCT}, my product, its competitors and our category in the last 7 days.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`). Call search_profiles for {PRODUCT} first, then list_products. If it returns {PRODUCT} and Social Listening is on, do A, in at most 18 calls. Otherwise do B, in at most 8, without asking me to sign in.

A. Signed in:

1. Call list_competitors and list_tracked_keywords. If no phrase has `kind` own_brand, say so before any number: LMTY monitors no phrase for {PRODUCT} itself, so the brief covers competitors. Before any count, name each phrase whose `addedAt` or `removedAt` falls in the period.
2. Call get_mention_stats since 00:00 UTC seven days ago, never before `listeningSince`. Then for up to 5 competitors by competitorId, those with most posts in `byKeyword`.
3. Volume, one row each: `totalRelevantMentions`, `distinctAuthors`, the largest of `byPlatform`, the busiest whole day of `byDay`. Never "spike", "drop" or "quiet": for a whole day under a quarter of the median, say a gap in collection cannot be told from a quiet day.
4. Call list_mentions for the largest tags in `byTag` among churn_intent, buy_intent, product_question, bug_report and negative user_feedback: a page each, then second pages. For each say "read N of M" and the days covered. Say which subject each post matched, from `matchedKeywords` and the phrase list. Drop posts about something else, the subjects' own, promotion and AI-written ones.
5. Themes, at most 5: each a count over all matching posts, with two linked excerpts and the author groups (company, vendor, partner, independent, unknown). Say what the posts say only from 20 or more read by 10 or more authors, as numbers with the days or hours they cover; otherwise list them and write "floor not met".
6. Call get_market_feed once, family "event", kinds price_changed, product_launched, product_deprecated, security_incident, funding_announced, acquisition_announced, partnership_announced, legal_action, company_shutdown, company_renamed. Say "N events read of a feed not counted, from [time] back to [time]"; show at most 5. Set a day's count beside one only if its `atBasis` is occurred. Otherwise "reported on" (published) or "first seen on" (observed); if none is occurred, say so.
7. Needs attention, at most 5: what, why, where next. Questions people ask, above the same floor or when I ask for them: "answered on the record" with the fact, grade and date from get_profile for the product asked about, "not on the record", or "not looked up".

B. Not signed in: for {PRODUCT} and up to 2 of {COMPETITORS}, call search_profiles, then get_profile with sections ["chatter"], then ["timeline"] in its own call, {PRODUCT} first. One row each from `chatterCounts`: if null, "LMTY collects no posts for it" (not "0 posts"); if `posts` is 0, "none collected in the last 30 days" Quote at most 10 posts, by author group: the most engaged of 30 days, not a sample. No themes below the floor. Events: at most 3 each, worded as in step 6; "not read" if not asked for. Say once what an account would add.

If you have run this before, lead with what differs. An earlier run is one in this conversation or your client's memory: never search files. With none, this is the baseline. Call volume a rise or a fall only if both periods began after listening did, with the same platforms and phrases, over whole days.

Rules: Counts are posts that matched a phrase and their authors, never customers or users. Nothing from memory or the web. End with what was not read, with both numbers.
