---
skill: company-hiring-signals
title: Hiring Signals
audience:
- Marketing
- Sales
- Leadership
cadence: Weekly
connect: public
summary: Read a company's open roles and leadership changes, and what to check next.
delivers: Open roles now and, where available, 30 and 90 days ago, the mix by function and country, key role titles, leadership changes, and up to three readings, each with what was seen and what to check next.
inputs:
- name: COMPANY
  required: true
  description: The company to research
  example: Northwind
---

Tell me what {COMPANY}'s open roles and leadership changes show.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Call search_profiles for "{COMPANY}" and take the company's profile. Open roles are recorded on the company, not its products.
2. Call get_profile with sections ["overview", "hiring", "trends", "people"]. If the answer names `sectionsLeft`, ask for those next.
3. Before any number, say what was read and when: `hiring.source.kind` is `board` (the whole list), `careers_page` (what one page showed) or `linkedin` (a sample, with the real `total` beside it), and `readAt` is the date.
4. Give open roles now, 30 days ago and 90 days ago, and how many are new in the last 30 days. A null earlier count means the record does not reach back: write "no earlier count", never "unchanged". Then the counts by function and by country.
5. Quote 5 or 6 role titles exactly, the ones that name a product, a market, a language or a first hire in a function. Give a posted date only when the record has one; otherwise write "not given" and call no role "newest". Where no role has a posted date, write "roles observed as of" the read date.
6. Call get_connections with kinds ["founded", "leads", "board_member", "works_at"] and includeEnded true. List who leads it, and who joined or left with the date and how it is known. An edge's `since` may be when LMTY first saw the role: write "as of", not "joined" or "became", unless a stated start was read. The stated start and ended roles are on the works_at ties and in get_profile with sections ["connections"]. With no dated arrival or departure on record, write "no arrivals or departures on record since" the date the leadership entries were first seen, never "stable", "unchanged" or a span of years.
7. For up to 3 things you noticed, write: Seen (the count, the titles, the dates) | Consistent with (one reading, named as a reading) | Would confirm (what to check next).

If you have run this before for {COMPANY}, lead with what changed since then, and say "nothing new" in one line when nothing did. An earlier run is one you can see in this conversation or in memory your client provides: do not search files or folders for one. With none, say there is no earlier run, so this one is the baseline, and go on.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. An open role is an intent to hire on a date, not a hire. Fewer open roles is not layoffs. Never give a reason for a departure unless it was stated. Roles, employers, dates and public statements only: nothing about anyone's private life. Answer from LMTY's record. Anything from outside it (a web search, a careers page you read yourself) goes only in a last section headed "From the assistant's own web search", with its link and the date read: never in a count, the mix or a signal.
