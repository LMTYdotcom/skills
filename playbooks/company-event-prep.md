---
skill: company-event-prep
title: Event Prep
audience:
- Sales
- Marketing
- Product
- Leadership
cadence: Weekly
connect: public
summary: Get ready for a company's upcoming launches, earnings calls, and events, based on what came up last time.
delivers: 'A dated list of upcoming events. For each one: what''s been announced, what came up the last few times, what to have ready, and two or three announcements to watch for.'
inputs:
- name: COMPANY
  required: true
  description: The company with the upcoming event
  example: Northwind
- name: ROLE
  required: false
  description: Who is preparing, such as sales, product, marketing, or leadership
  example: sales
---

Prepare me for what {COMPANY} has coming up. I am preparing as: {ROLE}.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Call search_profiles for "{COMPANY}". A product's dates may sit with its maker, and a subsidiary's earnings with its listed parent; say whose calendar each date came from. Before saying whether there is a listed parent, read the ownership ties: get_connections with kinds ["subsidiary_of", "acquired"]. Otherwise write "parent not checked", never "no listed parent".
2. Call get_calendar with profileType, profileId and upcomingOnly true for what is coming, which sits at the end of the list. For the last 90 days, call it without upcomingOnly and read from an `offset` near `total`. A past entry's `startsAtBasis` says how its date is known: published is "reported on", observed is "seen on". An entry saying what a page no longer lists or now lists is not something that happened: give those in one line, as "no longer listed as of" or "now lists".
3. Call get_profile with sections ["occasions"] for its earnings calls and keynotes as read: tone, themes, and sentences of direction with quotes.
4. Something announced as coming with no date ("coming soon") gets no block: list it under "Announced without a date", with who said it and when. For each coming date write:
   - Stated: what a source says will happen, each line with its source
   - Expected: only a count of what past occasions of this kind carried, dated ("on 3 of the last 4 calls, pricing was discussed"), never what will be said. With fewer than 3 distinct occasions, say there are too few and quote what was said as precedent
   - Last time: the last 2 or 3 occasions of the same kind, with date, tone, themes and what was announced. How one landed: only from posts in get_profile sections ["chatter"] dated after it that name it, quoted and unverified. With none, write "no public reaction recorded"; never from memory or from the announcement itself
   - Prep: what to have current before, who watches on the day, what to check within a day after
   - Tripwires: 2 or 3 specific statements that could trigger work, such as "a list price for the new tier"
   Write every prep and tripwire line as an option or a check I may choose ("Option: ...", "Worth checking: ..."), never as an instruction.
5. Note a rhythm only with 3 or more past occasions, as a count with dates. Several recordings of one call are one occasion: count occasions, not entries. A release note or changelog entry is not an occasion.

With no announced date, or no profile, leave the per-date blocks out and print no empty table. Do not open with "nothing": say no date is announced in LMTY's sources as of the read date, written out, which is not nothing planned.

If you have run this before for {COMPANY}, lead with dates that were added, moved or passed since then. An earlier run is one in this conversation or in memory your client provides, never one you search files for. With none, say this run is the baseline.

Rules: Keep every statement's grade; chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". An announced date is a fact; what will be said on it is not: write "the last three did", never "so they will". A date that passed with nothing recorded is "outcome not observed". Web finds go only in a last section, "From the assistant's own web search", with link and date.
