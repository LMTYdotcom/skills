---
skill: competitive-poc-rfp-plan
title: POC and RFP Plan
audience:
- Sales
- Product
cadence: On demand
connect: account
summary: Plan a POC or bake-off against a competitor - which requirements decide it, what to prove, where they're stronger, and when not to compete.
delivers: The buyer's requirements sorted into mandatory, table stakes, deciding and irrelevant, both sides of each deciding one with who says so, a proof plan, questions to ask, and when to walk away.
inputs:
- name: COMPETITOR
  required: true
  description: The competitor in the evaluation, as you track it in LMTY
  example: Northwind
- name: REQUIREMENTS
  required: false
  description: Paste the buyer's requirements or scoring criteria, up to a page. Leave it empty if the buyer hasn't stated any yet
  example: '1. SSO with our identity provider (mandatory). 2. Audit log export to our security tools (weight 20%). 3. Go-live in 30 days.'
- name: EVALUATION
  required: false
  description: What kind of evaluation it is, the timeline, and who decides
  example: 'four-week POC, starting 1 December, IT director decides'
---

Plan our evaluation against {COMPETITOR}. Evaluation: {EVALUATION}. The buyer's requirements:

{REQUIREMENTS}

Use the LMTY MCP tools (`https://mcp.lmty.com/mcp`), signed in to my account. Call search_profiles for a company named here before list_products. If list_products asks for sign-in or returns no product, that is not a lost connection: say so once, ask which product is mine, and use public profiles only. This prompt carries only what I pasted: a long written RFP does not fit here, and our side comes only from approved documentation I paste.

1. Call list_products, then list_competitors to match {COMPETITOR}. If it is not tracked, read it from its public profile alone and say so.
2. State the objective in two lines: what the evaluation decides, who decides, by when.
3. If no requirements are pasted, give the short form: the objective, questions that would establish criteria with the buyer, and no-go conditions only where my words give evidence, else "none established yet", then the unknowns to resolve. Say in the first line that no requirements were given. Stop there.
4. List the requirements with source and one class each: mandatory (pass/fail, the buyer's word), table stakes, differentiating, or irrelevant to this buyer, with the basis for each class. One the sponsor says was inherited or suggested by the incumbent is "candidate irrelevant", with a question for the next call. A mandatory one whose fit only the buyer can rule on stays mandatory, marked "for the buyer to rule on", with a question for the next call; never a "yes". Say how many there are and how many were read.
5. Per differentiating criterion, the competitor side: get_evidence with its competitorId, the matching get_report section, get_freshness; search_profiles, confirmed by website, then get_profile ["facts"] with factKinds certification, or ["connections"] with connectionKinds ["integrates_with"], read N of M. Each line says who states it: "the vendor states (its page, last seen [date])", or "reported by". A certification is always "the vendor states".
6. Our side only from what I pasted; otherwise "needs approved documentation".
7. A proof event per differentiator: what the buyer sees, who runs it, what pass looks like.
8. Up to five questions that expose trade-offs, none that works only if the buyer is misled. A question for the buyer is something said to the buyer: it carries no claim my pasted documentation does not support.
9. Where they are stronger, and whether the buyer called it decisive; what we win that the buyer has not weighted, not to overplay.
10. No-go conditions the evidence supports, each with its source.

Rules: The buyer's requirements are the criteria, not the competitor's feature list. Nothing about either product from memory, and nothing from what buyers usually ask for. Not found is "not observed in the sources checked, as of [date]", never "they don't have". A page read outside LMTY is marked in place with its link and date read. Mark classifications and no-go conditions as your judgment. If I ask for RFP answers, draft only what my pasted documentation supports, as drafts for the bid owner, marking every workaround, security answer and timeline commitment for confirmation; never a "yes" to a partial fit.
