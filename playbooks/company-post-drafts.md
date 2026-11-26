---
skill: company-post-drafts
title: Company Post Drafts
audience:
- Marketing
- Sales
- Leadership
cadence: Weekly
when: "Weekly for a company you post about, otherwise on demand. A repeat run should draft only from developments dated since the last run."
connect: public
summary: 'Draft a short post about one company''s recent developments, with two or three angles and a source on every claim.'
delivers: "Two or three angles, each with the developments behind it, and one draft for you to review, with a source after every claim. It also says how much it read, what it left out, and why."
inputs:
- name: COMPANY
  required: true
  description: "The company to write about"
  example: Northwind
- name: DESTINATION
  required: false
  description: Where the post is going
  example: a newsletter
- name: AUDIENCE
  required: false
  description: Who the post is for
  example: operations leaders
---

What could I post about {COMPANY}'s recent developments? It is going to: {DESTINATION}. It is for: {AUDIENCE}.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

At most 8 tool calls. One company at a time: if I named a market or several, ask which one.

1. Call search_profiles for "{COMPANY}". If several match, ask which.
2. Call get_calendar with profileType, profileId and a small limit: it gives `total`. The list runs earliest first: if there is more, read the 30 entries before `total` (read on if `more` > 0), and report "the newest N of M entries, back to [date]".
3. For grades and sources, call get_profile with sections ["timeline"] and limit 50 for the profile the entries' `companies` names, often the product (search_profiles for that name if needed). An entry not on that page is "grade not read".
4. Put every entry in one group, by its `startsAtBasis` or `atBasis`:
   - dated by when it happened (occurred)
   - dated by a report (published): write "reported on [date] by [source]"
   - first seen (observed), and any page reading (what a page now lists, now says or no longer lists): write "now lists" or "no longer listed as of [date]", never "new", a departure or a loss. Left out and counted
5. Merge reports of one story: it takes the strongest basis among its entries (occurred, then published, then observed) and the earliest date of that basis, never a source's date. Then set aside any story first dated before the last 90 days.
6. Keep what the company said apart from what others said: "{COMPANY} says" or "announced on [date]" for its own source, "reported on [date] by" for press.
7. Write:
   - Coverage: entries read of how many, and how many are in each group
   - Angles: 2 or 3, or 1 when the record supports 1. Each is one sentence with the entries behind it, leading with a story dated by when it happened or by a report: choose by what the story is and how well it is supported, then newest first, and say how you chose. If its grade was not read, say "grade not read" and write no draft from it unless I ask
   - Draft, for the first angle only: at most 120 words for a social post, 250 for a newsletter item, every claim followed by its source in brackets with the source's own date, or "date not given". First line: "Draft, for a person to review before it is posted. Nothing has been posted or sent." Where it needs my view, leave "[YOUR VIEW: ...]": never write my company in as fact. For a hot take, write the same draft and say the opinion is mine to add
   - Left out and why (with counts): first-seen entries, page readings, merged reports, entries graded chatter, entries announced as coming, older stories

If no story is dated by when it happened or by a report, write "Nothing on record carries a date of its own", list the first-seen entries as "now lists", count the page changes, and write no angles and no draft.

If you ran this before for {COMPANY} (in this conversation or your client's memory, never a file search), use only entries dated after that run, or say "nothing new". With none, say this run is the baseline.

Rules: Keep every statement's grade; chatter means one unverified source, is never stated as fact and is in no angle. No motive, forecast or superlative of your own, and no claim the sources do not make. Nothing from memory. Post or send nothing. Anything from outside LMTY goes only in a last section, "From the assistant's own web search", with its link and the date read.
