---
skill: social-keyword-check
title: Keyword Check
audience:
- Marketing
- Product
cadence: Monthly
when: "Monthly, and whenever you add a competitor. A repeat run should start with what changed in your keyword list since the last run."
connect: social
summary: "Check whether the keywords LMTY tracks for you still catch the right posts, and which ones catch too little or the wrong posts."
delivers: "It lists names and handles your keywords don't cover yet, keywords that match few posts or the wrong ones, and keywords to clean up, like paused ones or ones for competitors you no longer track. It also flags tracked competitors with no keywords, shows what changed in your list, and suggests up to 7 changes to make in LMTY."
inputs: []
---

Check whether the phrases LMTY monitors for my product still cover the right things.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in with Social Listening on. If a tool asks for sign-in or says it is off, tell me once and offer this instead: I paste my phrases and competitors, and you find the gaps against public profiles. At most 35 calls. Read-only: you list changes and make none.

1. Call list_products (ask which if several), then list_competitors.
2. Call list_tracked_keywords. Count the phrases by `kind`, those with `status` paused, and the `removed` list.
3. Call get_mention_stats twice, for 90 and 30 days: keep `byKeyword` and `listeningSince`. If listening began under 90 days ago, say how many days the 90-day count covers.
4. For my product, then competitors in list_competitors order (those an earlier run did not reach first), while calls last: search_profiles; get_profile on the profile with exactly that name, sections ["overview", "facts"], factKinds ["former_name"], for its `website`, its `channels` with `role` product or company, and former names; then sections ["connections"], connectionKinds ["offers", "acquired"]. A company's `offers` ties are its products. A product's `offers` tie pointing in names its maker: if graded above chatter, read the maker's connections the same way. Otherwise say "no maker on record" or give the chatter tie as such, and never take a maker or product name from `related`, the search or a shared name. Say which subjects you read of how many: the rest, any with no profile, and my product if no profile has exactly its name, are "not checked".
5. Gaps, at most 12: a thing on the record that no active or paused phrase equals or is contained in. Give its grade and date ("seen since" unless a start is stated; never "new"; "not given" for a website or channel) and the phrase to add, spelled as the record spells it. Never propose a name from memory.
6. Quiet phrases, at most 10: `byKeyword` for 30 and 90 days beside the days since `addedAt`, or since listening began if later. Under 14 days: "too new to judge". None: "no posts matched in N days of monitoring", never "dead".
7. For up to 3 phrases that look like common words: one list_mentions page each with includeLowRelevance true, and the competitorId if it is a competitor's. Keep posts whose `matchedKeywords` include the phrase and say how many are about its subject, as numbers, from their openings. A phrase you did not read is never called noisy.
8. Loose ends: `kind` competitor with `competitorId` null (the rival is not tracked now); a tracked competitor with no phrase; paused phrases. Give a pause no date.
9. What changed: phrases by `addedAt` and `removed` by `removedAt`, since my last run, or in the last 30 and 90 days, one row per batch of one day. A count that differs across such a date is a change in collection, not in conversation.
10. What to change in LMTY: at most 7 options, most useful first, each with the row it comes from and the wrong matches to expect, judged from the phrase: a domain has matched longer domains ending in it, and a short phrase has matched inside other text.

If you have run this before, lead with what changed in the list since then. An earlier run is one you can see in this conversation or in memory your client provides: do not search files or folders for one. With none, this run is the baseline.

Rules: A count is relevant posts that matched a phrase, not posts about its subject. A gap is "on LMTY's record, not among the tracked phrases". Give no reason why a phrase was added, removed or paused.
