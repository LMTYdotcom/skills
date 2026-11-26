---
skill: company-portfolio-brief
title: Portfolio Brief
audience:
- Leadership
- Customer success
- Anyone
cadence: Weekly
when: "Weekly or monthly for a list you're watching. A repeat run should start with developments dated since the last run, and say so when there's no earlier run to compare with."
connect: public
summary: "Scan your list of companies for recent developments worth a look, with the evidence, dates, and one follow-up question for each."
delivers: "A line saying how much of your list it read. Then up to 8 companies with something worth following up on, each with the evidence, its date, and one question to ask. Every other company is listed with why it wasn't flagged: nothing dated, nothing that met what you asked, not read, or not identified."
inputs:
- name: COMPANIES
  required: true
  description: The list of companies to scan
  example: Northwind, Initech, Globex
- name: CRITERION
  required: false
  description: "What to look for"
  example: leadership changes and funding
---

Which of these companies merit my attention, and what should I follow up on? {COMPANIES}

What counts as needing attention: {CRITERION}. If I gave none, use this default and say so: funding, an acquisition or a sale, a leadership arrival, a price or plan change, a product launch or an end of life, a legal action, or a security incident, dated, in the last 90 days. Go by what an entry says, not its kind: an outage or a routine version release alone does not count; give releases as a count.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

Work only from my list. Never look up a fund's holdings: ask for the list.

1. Call search_profiles for each of the first 30 names; name any beyond as not read. A name several profiles match: do not pick, put it under "Could not confirm". No match: search once more under the other obvious name, and show a profile found that way under both names.
2. For every company found, call get_calendar with profileType, profileId and a small limit: it gives `total`. The list runs earliest first: if there is more, read the 30 entries before `total` (read on if `more` > 0), and say "the newest N of M entries, back to [date]". If the search also returned a product under the same name, or one differing only by a suffix such as ".ai", read its calendar too and name both.
3. Group each entry by `startsAtBasis`: occurred is "on [date]", published is "reported on [date]", observed is first seen. A page reading (what a page no longer lists or now lists) is "no longer listed as of [date]", naming whose page, or "now lists", whatever its basis. Only occurred and published entries are developments. Several entries about one event are one, with the strongest basis and its earliest date.
4. For each company to be shown, take the entry's grade and sources from get_profile with sections ["timeline"] and limit 50 for the profile its `companies` names (search_profiles for that name if needed). If it is not on that page, write "grade not read".
5. Write:
   - Coverage, first: of how many given, how many were read in full, read in part, not read, and not found. Then the criterion and whose it is
   - Merits attention (at most 8 companies, by date, and say so): the development and who states it; its grade and date; the entry and criterion it met, nothing else; one follow-up question on what it leaves unstated. Say once that a report's date is not the event's
   - Dated entries, none met the criterion; Nothing dated on record: names, one line each
   - No longer listed: one line; one page's names at once are one item with a count. Never a loss
   - Not read; Could not confirm, with the question that settles each
   Every name appears in exactly one place.

If none meets the criterion, write the coverage and criterion lines, one sentence saying so, and the one-line sections.

If you ran this before for this list (in this conversation or your client's memory, not a file search), lead with entries dated after that run; if not, say there is no earlier run to compare with.

Rules: Keep every statement's grade; chatter means one unverified source, is never stated as fact and never alone flags a company. No ranking, score, verdict or advice on a holding. If I ask which is in trouble, say the record cannot say. No motive, no forecast, nothing from memory. An absence is "nothing dated on LMTY's record", never "nothing happened". Anything from outside LMTY goes only in a last section, "From the assistant's own web search", with link and date.
