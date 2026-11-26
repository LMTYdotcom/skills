---
skill: company-pricing-history
title: Pricing History
audience:
- Marketing
- Product
- Sales
cadence: On demand
connect: public
summary: See how a product's prices and plans have changed over time, with dates and the overall pattern.
delivers: The current price list, a dated timeline of moves, plans no longer listed, what people report paying, and the pattern in plain numbers.
inputs:
- name: PRODUCT
  required: true
  description: The product you want the pricing history for
  example: Northwind
---

Show me how {PRODUCT}'s prices and plans have changed.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

1. Call search_profiles for "{PRODUCT}". Prices sit on the product's profile, not its maker's. When a company and a product share a name, read the product.
2. Call get_profile with sections ["overview", "pricing"]. The plans on sale now are the overview facts of kind pricing_plan. In `pricingHistory`, `changes` are dated moves with before and after values, and `ended` are plans no longer listed. Page with offset until `more` is empty.
3. Build a timeline, oldest first: the date, the move (new plan, price up, price down, plan retired, closed to new buyers, allowance changed, model changed), from what, to what, and the grade and source where the record gives them. A move with no source of its own is marked "from LMTY's price record" and takes the date it was observed. A move the record words as reported keeps "reportedly" in the move itself.
4. Say when the record begins, as two dates when they differ: the earliest dated entry, and the date the current plans were first read. Nothing before the earlier is known, and a plan first seen on the later was not introduced on it.
5. Facts of kind reported_price are what people say they pay. List them apart, with who said it and when. Never use one to correct a listed price. Posts in get_profile sections ["chatter"] are a second place a price may be mentioned, unverified: read them only when there are no reported_price facts or I ask. Before writing that the profile has no reported prices, say which of the two you read, with counts.
6. Describe the pattern in 2 to 4 sentences, each with a count and dates: how many moves in what period, which way the entry price and the top price went, and whether prices or allowances moved.

Write: On sale now (table) | Timeline (table) | No longer listed | What people report paying | The pattern | What the record does not show.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. A listed price is what the page said on a date, not what anyone paid. Write "no longer listed as of", not "discontinued". Never say why a price changed unless the company said why. With no history on record, give the current list and say the record starts now. The price list and the timeline hold only what LMTY's record holds. A price or a move from outside it (a web search, a page you fetch) goes only in a last section headed "From the assistant's own web search", with its link and the date read: never a row in either, and never in place of a price on the record. Do not reconstruct past prices from memory or undated pages.
