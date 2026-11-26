---
skill: company-customer-map
title: Customer Map
audience:
- Sales
- Marketing
- Product
cadence: On demand
connect: public
summary: Find a product's publicly named customers by industry, company size, and country, and where each name comes from.
delivers: The best-evidenced customers, how each is known, counts by segment, which customer names were added to or dropped from public lists, and what else they use.
inputs:
- name: PRODUCT
  required: true
  description: The product you want to see customers for
  example: Northwind
---

Map the publicly named customers of {PRODUCT}.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Call search_profiles for "{PRODUCT}". Customers are recorded on the product's profile. If the company's profile shows none, read the product's before saying none are known.
2. Call get_profile for the overview. `counts.customers` is how many are publicly named. A count the company claims for itself is a fact of kind proof_point or financial: look in both before saying there is none. Report both numbers; neither corrects the other. A claimed figure stored as a bare value and label with no sentence is reported as stored, both in quotation marks, with its source and date: say the record does not hold its sentence, and do not complete it.
3. Call get_profile with sections ["customers"] and page with offset until `more` is empty or you have read 100. Say how many you read out of how many. If the count is 0 or there is no product profile, call get_connections with focusType and focusId of the product or company and kinds ["customer_of", "uses"], and report the ties that point at it as publicly named customers. Say they came from ties and carry no evidence kind, sector or size, and write "who makes the claim: not read".
4. For each customer you name, say who makes the claim and how it is known (`evidence`): the vendor ("Northwind names Globex as a customer on its customers page"), the customer itself (its own job ad or site), or a third party. A customer list is the vendor's own claim unless the customer or an independent source says so. Write "publicly named customers", never "its customers", "customers include" or "uses". `since` is a real start only when `sinceStated` is true; otherwise write "seen since".
5. Count the ones you read by sector, by size band and by country, with a row for "not given". Write "of the N read", never a share of all customers.
6. Report movement only where a source shows it: entries marked `ended`, and `alsoUses` entries with `moved` set. Two products for one customer is "recorded with both" unless the order of events is known. Give no reason for a removal unless a source states one.
7. Count which other products the same customers are recorded with (`alsoUses`). That entry does not say who makes the claim.

Write: The three numbers (claimed, publicly named, read) | Publicly named customers, best evidenced first (table, with who makes each claim) | How the claims are known | By sector, size, country | Movement | Other products the same customers are recorded with | What the publicly named set leaves out.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. Known is a floor, not a total. A logo proves the vendor claims the customer, not that they still use it. A company missing from the list is "not observed as a customer", never "not a customer". Answer from LMTY's record. Anything from outside it (a web search, a fetched page) goes only in a last section, "From the assistant's own web search", with link and date read: never in the three numbers, the table or a count.
