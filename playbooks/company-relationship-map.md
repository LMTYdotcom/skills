---
skill: company-relationship-map
title: Relationship Map
audience:
- Sales
- Marketing
- Leadership
cadence: On demand
connect: public
summary: Map who leads, funds, and partners with a company, who it competes with, and who says so.
delivers: A company's leaders, investors and owners, partners, and competitors, each with who states it, since when, and whether it has ended.
inputs:
- name: COMPANY
  required: true
  description: Company, product or person at the center
  example: Northwind
---

Map who {COMPANY} is tied to and how.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Call search_profiles for "{COMPANY}". Investors and owners attach to the company, integrations usually to its product; read both when I ask about both.
2. Call get_connections with focusType and focusId, includeEnded true, and `kinds` narrowed to one group at a time:
   - People: founded, leads, board_member, advises
   - Money and ownership: invested_in, acquired, subsidiary_of
   - Working ties: partners_with, integrates_with
   - Rivals: competes_with
   Add the number of edges returned to offset and call again until `more` is 0. Say how many of each of these kinds exist and how many you read. Give no count for a kind you did not ask for, such as customers or employment.
3. Call get_profile with sections ["facts"] and factKinds ["funding_round", "valuation", "funding_total"]. Pair an investor with a round only where a source names that investor in that round; otherwise list investors and rounds separately, never paired by nearest date.
4. For every tie you show, say who states it. A get_connections edge carries a grade and a source count, not its sources or whether its `since` is a stated start: for those, call get_profile with sections ["connections"], which carries both. A partnership listed by one side only is that side's claim. An integration in a directory shows a connector exists. A competitor on a comparison page is who that company chose to be compared with. Edges of kind competes_with, integrates_with and partners_with are stored in an arbitrary order: their direction does not show who named the rival, listed the integration or announced the partnership. Compare each source's site with each party's. With no source read, write the tie as existing between the two, "stated by: not read".
5. Date each tie: "since" only for a start a source states, otherwise "seen since". Mark ended ties and how the end is known.

Write: In short (3 or 4 sentences) | People | Money and ownership | Working ties | Rivals | Ended ties | Not on the map (stakes, terms) | From the assistant's own web search (anything from outside LMTY, only here, with link and date). Show every tie that bears on the question with its grade: an unverified tie is shown, labeled unverified. For a kind with more than 10 ties, give the count for each grade, name a grade group of 3 or fewer in full, show a larger group's best-sourced few, and give the rest as a number, never as names; count ended ties separately. Leave out a section with nothing in it. The "Not on the map" line names each of the 4 groups with no tie: "not observed in LMTY's sources" if the kind was read and empty, "not read" if it was not asked for; never "not assessed", "none" or "has no". A profile with 3 ties or fewer gets its freshness line, those ties (both parties named, with grades) and that line, in about 150 words, and nothing else.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. A tie is as strong as its weaker end. A shared investor or board member is a path, not an alliance. No motive for a deal unless a party stated one.
