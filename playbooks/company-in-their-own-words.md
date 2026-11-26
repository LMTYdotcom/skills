---
skill: company-in-their-own-words
title: In Their Own Words
audience:
- Marketing
- Product
cadence: On demand
connect: public
summary: 'Collect how a company describes itself, word for word: its headlines, category, proof points, and what its leaders say.'
delivers: 'Its wording by page, the category it claims, the evidence and figures it cites, how its wording has changed, and up to 10 dated quotes from its leaders. For a person: what they''ve said in public.'
inputs:
- name: COMPANY
  required: true
  description: Company, product or person you want to quote
  example: Northwind
---

Show me how {COMPANY} describes itself, in its own words, and how that has changed.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Call search_profiles for "{COMPANY}". Read the company's profile and, when it has a main product, the product's. Say which words came from which.
2. Call get_profile with sections ["facts"] and factKinds ["tagline", "category_claim", "proof_point", "boilerplate", "page_meta", "milestone"]. Copy each wording exactly, with its page and the date last seen. Leave out button labels: stored as taglines, they are not messaging. A count of customers or users it claims can also sit under kind financial: look there before saying it cites none. The overview's `about` text is LMTY's writing: never quote it as the company's words. With no heading, tagline or category term on record, write "not observed in LMTY's sources" and move nothing else into that slot: wording read on the site or by search goes only in a last section, "From the assistant's own web search", with link and date.
3. Call get_profile with sections ["terms"] for the category terms its pages use and the earliest use known of each.
4. Call get_profile with sections ["statements"] for what its founders and executives said in public. Keep the speaker, the venue and the date. A statement graded official can be another company's leader speaking: check the speaker's employer. A statement by another company's leader about {COMPANY} is not its own words: leave it out and say in one line how many there are. A leader's remark that names no company (on the market, hiring, technology) is that person's: quote it under their name and role, and call it the company's position only if it is about the company's own product, customers or plans, or they say they speak for it.
5. A wording with an end date was replaced. Pair old and new only where they held the same page and heading, and give both dates. Wording first seen when the page was first read is not new wording. Give no reason for a change unless a source states one: write "no source states why".

If {COMPANY} is a person (search_profiles gives type person): do only step 4, on that person's profile, and write only their statements, newest first, and what the words do not show. Say which company they speak for, from their current roles, and that the company's own wording is a separate read. What others said about them is not their words: leave it out and count it. A person has no headline, tagline, category or boilerplate: leave those parts out, not empty.

Write: What it says it is (page, heading, line beneath, last seen) | The category it claims | The proof it cites | How the wording has moved | What its leaders say (up to 10 quotes, newest first) | Do the voices agree (its pages against its leaders) | What the words do not show.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. Quote, never paraphrase; mark any summary as yours. A company's statement proves only that it said so. Describe a change in words ("'for small teams' no longer appears in the heading"), never as intent ("moving upmarket"). Do not tidy a spoken quote.
