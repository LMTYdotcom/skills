---
skill: company-claim-check
title: Claim Check
audience:
- Sales
- Marketing
- Anyone
cadence: On demand
connect: public
summary: 'Check a claim about a company: who''s making it, since when, and whether the evidence holds up.'
delivers: The claim restated so it can be tested, one of eight fixed verdicts (such as Supported, Unverified, or Out of date), who says so, the gap between claim and evidence, and what would settle it.
inputs:
- name: CLAIM
  required: true
  description: The exact wording of the claim
  example: Northwind has 10,000 customers
- name: COMPANY
  required: true
  description: Who the claim is about
  example: Northwind
---

Check this claim about {COMPANY}: "{CLAIM}".

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Restate the claim so it can be tested: who, what, how much, as of when. Split a compound claim into its parts. Keep the original words beside your restatement, and say what you assumed.
2. Call search_profiles for "{COMPANY}" and for any second party the claim names, such as a customer, a partner or an investor. The second party's side is often the better evidence.
3. Read where this kind of claim lives: get_profile for the overview, the `facts` section narrowed with factKinds, the `customers` or `pricing` section, or get_connections. Collect every statement that bears on the claim, not only the one that matches it.
4. For each statement note its grade, LMTY's confidence, and each source's publisher, tier and dates. A get_connections edge carries a source count, not its sources: do not say where a set of ties comes from, or that none has a source of a given kind, unless you read get_profile with sections ["connections"] for them. Then ask: is the only voice the subject itself?
5. Give exactly one of these eight verdicts, worded as here, and one sentence of reasons naming sources and dates:
   Supported | The subject's own claim | Reported, not confirmed by the subject | Unverified | Disputed | Out of date | Not observed | Untestable
   Supported needs a source in a position to know (a register, a filing, the other party's own statement) or the subject plus an independent source; press alone is Reported. For a claim that one company uses another's product, the interested party is the vendor: write "The subject's own claim" as "The vendor's own claim". It is the same verdict, not a ninth.
6. State the gap: the unit ("customers" where the page says "users"), the scope, the tense, a rounder number. Two figures that count different things do not conflict; say what each counts.
7. Name the one or two things that would settle it: a filing, a register, the customer's own statement.
8. End with "Before repeating it": the form of the claim the evidence supports, attributed and dated.
9. If I ask you to correct the claim, draft 1 to 3 sentences only when the record holds an official, dated source on the same claim, plan and scope that says otherwise: quote it with its source and date, as a draft for a person to review. If not, write "No correction drafted" and which part failed, with no suggested response.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. Never write "true" or "false"; the verdict describes the evidence. No word about anyone's motive: no "misleading", no "inflated". Nothing found is "Not observed", which is not evidence against the claim. Check the claim that was made, not a nearby one that is easier. The verdict comes from LMTY's record. Anything from outside it (a web search, a page you fetch, the company's site read directly) goes only in a last section headed "From the assistant's own web search", with its link and the date read: it never changes the verdict, and a claim the record does not hold stays "Not observed".
