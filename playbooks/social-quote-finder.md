---
skill: social-quote-finder
title: Quote Finder
audience:
- Marketing
- Sales
cadence: Weekly
when: "Weekly, or monthly for a product with few posts. A repeat run should list only posts dated since the last run."
connect: social-optional
summary: "Find public posts that praise your product, and what to check before you follow up."
delivers: "Up to 10 posts quoted word for word, most specific praise first. Each comes with the author, the link, and what still needs checking: their employer, whether they're a customer, and permission to reuse. It also lists what it set aside and why."
inputs:
- name: PRODUCT
  required: true
  description: Your own product
  example: Acme
---

Find public posts that praise {PRODUCT}, my own product, and might be worth quoting.

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), at most 12 calls. Call search_profiles for {PRODUCT} first, then list_products. If it returns {PRODUCT} and Social Listening is on, do A. Otherwise (sign-in asked for, no product, or Social Listening off) do B without asking me to sign in, and say once that an account with Social Listening on adds every collected post, with sentiment and tags.

A. Signed in: call list_tracked_keywords. With no phrase of `kind` own_brand, say LMTY monitors no phrase for {PRODUCT} itself, so praise of it is not collected through this account (and when its own were removed, from `removed`), and do B. Else call get_mention_stats for 30 days with ownOnly true: M is `bySentiment.positive`. Get {PRODUCT}'s `channels` as in B. Call list_mentions with ownOnly true, sentiment positive and limit 50, up to 7 pages. Say "read N of M positive posts that matched my own phrases". If I point at posts instead (a link, an author, a day): read those days with list_mentions, ownOnly only if I have own phrases, and judge only them by steps 1 to 3, with no wider count.

B. Not signed in: call search_profiles for "{PRODUCT}" and take the product's profile (ask if several match). Call get_profile for its overview and its company's: keep `channels`. Call get_profile with sections ["chatter"] for the product, paging until `more` is empty, and for the company only if its overview counts posts. Say "read N of M", M from `chatterCounts.posts`: the most engaged posts of 30 days, not a sample; praise is judged by reading. If `chatterCounts` is null, say LMTY collects no public posts for {PRODUCT}, which is not nobody praising it, and stop. If `posts` is 0, say LMTY collected none in the last 30 days, and stop.

Then, either way:

1. Keep a post only if its excerpt itself praises {PRODUCT}: not praise of someone else that only names it, a kind word inside a complaint, or praise that may come after the cut.
2. Sort each author: the company (a handle in `channels` under any role but community, or one who says they work there), a partner or vendor, an independent poster, or unknown affiliation. Only the last two are candidates. Other employees cannot be identified: say so once. No handle: "no handle given", unknown affiliation.
3. Candidates, at most 10, most specific praise first, never by followers. For each: the excerpt exactly as returned, with "may continue" if cut (A: exactly 400 characters; B: ends in an ellipsis after a word; a link ending in one is not a cut); handle and display name; platform; date; link; engagement; author group; why it is worth a look; and "not verified: employer, whether a customer, permission to reuse".
4. Set aside, as counts, one example each: the company's own posts; partners and vendors; promotional and AI-written posts (by their tags in A, by reading in B); praise mainly of someone else; not praise when read.
5. End with: these are leads, and before reuse a person asks the author and waits for a yes in writing.

If you have run this before for {PRODUCT}, list only posts dated after that run. An earlier run is one in this conversation or your client's memory: do not search files.

Rules: Never complete, tidy, translate or join an excerpt, and add no quote from memory or the web. Nobody is a customer or a user unless the post says so. A display name that includes a company is not an employer. Never look an author up. With none, write "no candidates in the N posts read" and which reason removed the most.
