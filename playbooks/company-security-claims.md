---
skill: company-security-claims
title: Security Claims
audience:
- Sales
- Leadership
- Anyone
cadence: On demand
when: "On demand, or quarterly for each vendor you review. A repeat run should start with anything LMTY spotted for the first time, or that's no longer listed, since the last run."
connect: public
summary: "Check the public evidence of a vendor's security and compliance: the certifications it claims, reported incidents, and what to ask the vendor for."
delivers: "The certifications the vendor claims, where each claim comes from, and which details LMTY's sources don't show. Then any reported security incidents, each counted once, what has changed, and up to 6 questions to ask the vendor. It's a checklist of public evidence, not a security approval."
inputs:
- name: COMPANY
  required: true
  description: The company or product under review
  example: Northwind
- name: PURPOSE
  required: false
  description: What the review is for
  example: a vendor security review
---

List the public evidence of {COMPANY}'s security and compliance. It is for: {PURPOSE}.

Use the LMTY MCP tools. Its public profiles need no sign-in. If the tools are not available, say so and stop: the server is `https://mcp.lmty.com/mcp`.

At most 8 tool calls.

1. Call search_profiles for "{COMPANY}". A certification can sit on the company's profile or its product's: take both. If the search returns one, the other is among its overview's closest relations. If several match, ask which.
2. Call get_profile for each: `factKinds` counts the certification facts and `counts` the timeline entries.
3. For each profile that counts any, call get_profile with sections ["facts"] and factKinds ["certification"]. A fact is a name, a grade and a source: add no type, year, auditor or scope. The kind also holds laws and frameworks (list them as stated claims, not certifications) and credentials people hold (list them apart, as held by staff). Two spellings stay two rows.
4. For each profile, call get_profile with sections ["timeline"] and limit 50. Pick by `kind` and `statement` the entries on a security incident, a certification no longer listed, or a certification or trust page first seen.
5. Write, in order:
   - Title and first line: a checklist of public evidence, not a security approval
   - Coverage: profiles read, facts read of how many, timeline entries read of how many
   - If I asked yes or no ("are they compliant?"): "The record cannot answer that", why, then what the record holds
   - Claims (at most 15): what is claimed, who states it, the page, the grade, last seen. Every row is "the vendor states", or the other party by name, never "is certified" or "is compliant". Say in one line what official and reported mean
   - One unverified source says: any claim graded chatter, apart, never in the table
   - Not on record for each claim: the report's date, the period covered, the scope, the auditor, an expiration date. Always listed
   - Incidents on record (at most 10): one row per incident, not per report, with every report as a source. Date it by `atBasis` (published is "reported on"); a merged row takes the strongest basis and its earliest date. Unsure if two are one: two rows, saying so. Outages filed as incidents: one line of their own, never called a breach
   - Changes (at most 8): "first seen on", never added or new, for a first sighting or a page that now lists a name; "no longer listed as of", never lost or revoked, when a page stopped listing a name (take the page from the entry's source, not its statement). If a fact and the timeline disagree, give both and say so; on one page, with the fact seen later, write "listed again as of"
   - What to ask the vendor for (at most 6), each tied to a row: the report itself, its date and scope, a bridge letter, an incident's post-mortem

With no certification fact and no security entry, write only what was read, that nothing is on LMTY's record, and what to ask the vendor for.

If you ran this before for {COMPANY} (in this conversation or your client's memory, never a file search), lead with what was first seen or is no longer listed since then. With none, say this run is the baseline.

Rules: Keep every statement's grade; chatter means one unverified source and is never stated as fact. Nothing from memory: no certification, framework, auditor or breach not on the record. An absence is "not on LMTY's record", never "has none" or "no breaches". No verdict, score or advice. Anything from outside LMTY goes only in a last section, "From the assistant's own web search", with link and date.
