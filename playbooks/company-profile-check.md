---
skill: company-profile-check
title: Profile Check
audience:
- Marketing
- Leadership
cadence: Monthly
connect: public
summary: Compare what an AI assistant says about your company with the public record, and see what to fix first.
delivers: 'The assistant''s unaided answer beside the record; facts for you to confirm; possible gaps, outdated facts, and conflicting claims; and a ranked list of suggested fixes with the page each belongs on.'
inputs:
- name: COMPANY
  required: true
  description: Company, product or person (your own)
  example: Acme
---

Check what is said about {COMPANY}, which is my own company.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so first, give the unaided answer from step 1 below that, and stop: the server is `https://mcp.lmty.com/mcp`.

1. Before calling any tool, write 3 to 6 sentences answering "what is {COMPANY}?" from what you already know, with the facts you would state: what it does, where it is based, how big it is, who leads it, what it costs. If you know nothing, say exactly that. Keep this text unchanged, and label it as one assistant's answer on the date, written out, naming the assistant and model, not what "AI" says.
2. Call search_profiles for "{COMPANY}" and get_profile for the overview. No profile at all is the first finding: pass on the tool's hint and continue from web search, marked as your own research.
3. Set your unaided answer beside the record, statement by statement: where they agree, where they differ, and what you stated that the record does not hold. Say "the record does not hold it" only if you read every section with a count above 0; otherwise say "not in the sections read" and name them. Neither side is the truth; each difference is a question for me. A price or figure you remembered is your memory, not an old price on record.
4. Lay out every headline fact for me to confirm, with what the record says, its grade and "still true?". Mark the rows worth a second look: an old date, two values, a source that is not us.
5. Names and channels: the `name`, former_name facts, `website` and the overview's `channels` with each `role`, for the company and its main product. Keep apart "missing from LMTY's record" (not held, may exist; it keeps no alias list) and "missing from our own site" (only `endedBy` gone or a `removed` change). Ask me which other search matches and channels are ours.
6. Missing: for each section whose count is 0, say what a reader would expect there and both possible reasons, without choosing: LMTY has not read it, or our pages do not show it. Offer a check as a question ("does your site have a customers page?"); never say a page is missing. Customers sit on the product's profile: a company's count of 0 is not a gap until the product's was read.
7. List facts that may be out of date, and facts the record gives two values for. Put each conflict to me as a question; do not say which value is right.
8. List statements that rest on one unverified source, quoted with who and when, for me, not you, to sort into three bins: untrue and worth answering, true and uncomfortable, or harmless.
9. Fix first: up to 10 rows, ranked by how many readers each reaches and how wrong it leaves them: the change, where it belongs, who is misled, the effort.

If you have run this before for {COMPANY}, lead with findings fixed, still open and new. An earlier run is one you can see in this conversation or in memory your client provides: do not search files or folders for one. With none, say this run is the baseline and go on.

Rules: Keep every statement's grade: official means someone who speaks for one of the parties said it (check which party), reported means press or two independent sources, chatter means one unverified source and is never stated as fact. Give each fact the date it was last seen and its source address. An empty section is "not observed", never "none". A page can hold fewer entries than the limit asked for: read until `more` is empty. Never tell me a fact is wrong: tell me what the record says and where it came from. No score for the whole profile.
