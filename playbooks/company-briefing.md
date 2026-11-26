---
skill: company-briefing
title: Company Briefing
audience:
- Sales
- Marketing
- Leadership
cadence: On demand
connect: public
summary: Get a one-page briefing on a company, product, or person before a meeting, with a source and date for every fact.
delivers: 'One page: what it is, the basics, who leads it, what it sells, recent changes, what''s coming, and what isn''t known. For a person: current roles, connections, and what they''ve said in public.'
inputs:
- name: COMPANY
  required: true
  description: Company, product or person to brief on
  example: Northwind
- name: PURPOSE
  required: false
  description: What the briefing is for
  example: a partnership meeting on Thursday
---

Brief me on {COMPANY}. It is for: {PURPOSE}.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Call search_profiles for "{COMPANY}". A company, its product and its people are separate profiles. If several match and I have not said which, ask. If none match, pass on the tool's hint and stop.
2. Call get_profile for the match. The overview is the default; read `counts` to see which sections hold anything.
3. Make at most 4 more reads, chosen by the purpose: the `changes` section for what moved, get_connections for founders, leaders, investors and partners, the `statements` section for what its leaders said, get_calendar for what is coming and what happened lately: both sit at the end of its list, so read from an `offset` near `total` when the first call does not return everything. If an answer names `sectionsLeft`, ask for those next. A further page of a section you are already reading is not a new read: read it to its end, or say how many entries you read and how many the record counts.
4. Write one page:
   - What it is: 3 or 4 plain sentences, from official and reported statements only
   - The basics: founded, based, headcount, funding, each with grade, date and source
   - People: who founded and leads it, and up to 3 quotes from its leaders with venue and date
   - What it sells: plans and listed prices, how many customers are known by name, and the company's own count if it states one
   - What moved: 3 to 6 dated items, newest first. A change marked `found` is first seen, not news; use only added, removed and returned. Word a calendar or timeline entry's date by its basis: published is "reported on", observed is "seen on". An entry saying what a page no longer lists or now lists is not something that happened: one line at most, as "no longer listed as of" or "now lists"
   - What is coming, with dates
   - Not observed: every empty section
   - Sources: address, publisher, date
   For a person, People is their current roles, career in order, what they founded or backed, and what they said in public.
5. If I ask only what is new with {COMPANY}, skip steps 3 and 4. Read get_calendar and the `timeline` section, newest first, back 90 days. Write one screen: "read N of M entries, back to [date]"; at most 8 entries dated occurred or published, each with date, grade and source, or "Nothing dated on LMTY's record for {COMPANY} since [date]"; apart, as counts and never as news, what LMTY only first saw (observed, and page readings); one line for what was not read.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. No motive, no prediction, and no adjective the sources did not use. If the profile is thin, write a short briefing and a long "Not observed" list. Answer from LMTY's record. Anything from outside it (a web search, a page you fetch, the company's site read directly) goes only in a last section headed "From the assistant's own web search", with its link and the date read: never in the page above it, and never in place of a figure on the record. Search only for what my purpose needs and the record lacks, and say what you searched for.
