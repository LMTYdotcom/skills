---
skill: company-prospect-stack
title: Prospect Stack
audience:
- Sales
cadence: On demand
connect: public
summary: Find out which tools a prospect is publicly known to use, split into what to mention and what to ask on the call.
delivers: A table of known tools with who says so and since when, each labeled Mention or Ask, and 3 to 5 questions for the call.
inputs:
- name: ACCOUNT
  required: true
  description: The company you are about to speak to
  example: Globex
- name: WE_SELL
  required: false
  description: Your product or category, so the relevant tools come first
  example: project tracking software
---

List the publicly evidenced tools for {ACCOUNT}. I sell: {WE_SELL}.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Call search_profiles for "{ACCOUNT}" and settle the company by its website. If two companies could be the one meant, ask which and wait: a stack for the wrong company is worse than none. If one matches and its profile has no website, do not guess one: give the stack for that match, say which profile you used and ask me to confirm it.
2. Call get_connections with focusType "company", the focusId, kinds ["customer_of", "uses"] and includeEnded true. Add the number of edges returned to offset and call again until `more` is 0.
3. An edge does not say how the use is known. For a product whose use matters to the call, read the evidence where it exists: get_profile on {ACCOUNT} with sections ["connections"], or on that product with sections ["customers"] for the entry about {ACCOUNT}. For the others write "how it is known: not read". Then say who makes the claim:
   - Shown by the account: found on its own site or code, or named in its own job ad
   - Said by both: only when the account itself says it uses the tool (its own page or code, or a quote from a named person there). A case study only the vendor published is the vendor's claim
   - Claimed by the vendor: a logo or a name on the vendor's page. An official grade here means the vendor said so, not that the account confirmed it
   - Reported: an article says so
4. Date each one: "since" only for a start a source states, otherwise "seen since", and always the date last seen.
5. Bin each: Mention (the account's own side shows it, seen in the last few months), Ask (vendor-claimed, reported, or not seen lately), or leave out (ended long ago). An item graded chatter, or marked "how it is known: not read", is an Ask: raise it as a question, and never write it as "also uses" or "is known to use".
6. Write 3 to 5 questions for the call, each tied to one item: confirm an "ask" item, find who owns a tool, learn when it renews, probe a category where nothing is observed.
7. If what I sell is a category and names no product, list no likely incumbents from integrates_with ties: an integration says two products connect, not that {ACCOUNT} uses either. Say so, give any such tie in one line as "connects with, use not evidenced", and make it a question.

Write the questions first, then the table, headed "Publicly evidenced tools" and never "its stack" or "the tools it uses" (product, maker, who makes the claim, evidence, since, last seen, bin), then what the list leaves out.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. "Known to use" is the strongest phrase for one item, and only with who makes the claim beside it. Not listed is not "does not use": most tools leave no public trace. Do not decide from memory who competes with whom. Do not look up any individual at the account. Anything from outside LMTY (a web search, a fetched page or job ad) goes only in a last section, "From the assistant's own web search", with link and date read: never in the questions, the table or a bin.
