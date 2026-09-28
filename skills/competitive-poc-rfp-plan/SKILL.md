---
name: competitive-poc-rfp-plan
description: Plan a head-to-head evaluation - a POC, POV, pilot, bake-off, or RFP response - against a competitor or competitive set, with the buyer's requirements mapped, table stakes separated from the criteria that will decide it, each differentiator tied to a proof event, the questions that expose real trade-offs, where the competitor is stronger, and the conditions under which the team should not proceed. Use for "we're going into a POC against X", "help us shape the RFP response", "what should we prove in the POV", "how do we set up the evaluation around what matters", and scoring or requirement matrices. Not for general deal prep, one live objection, or a reusable battlecard.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive POC / RFP Plan

## Mission

Help a team enter a formal, criteria-driven evaluation against a competitor with a plan built on what the buyer actually needs to see - not on the competitor's checklist, not on the home product's favorite demo, and not on claims nobody can prove in the room.

The plan says which requirements are table stakes, which will decide the evaluation, what proof event demonstrates each differentiator, which questions surface trade-offs the buyer has not yet considered, where the competitor will win, and when the honest advice is not to compete.

## Use this skill when

- a POC, POV, pilot, bake-off, or technical evaluation against a named competitor is starting or being scoped
- an RFP, RFI, or security questionnaire has arrived and the team wants to shape the response competitively
- someone asks what to prove, what to demonstrate, or how to set the evaluation criteria
- a buyer has sent requirements or a scoring matrix and the team needs to read it competitively
- a request bundles the evaluation plan with a live objection or an account overview - take the evaluation, route the rest (Step 10)

## Do not use this skill when

- the job is preparing for the account in general - stakeholders, deal state, next meeting. Use `competitive-deal-prep`.
- the user needs words for one objection now. Use `competitive-objection-response`.
- the user wants reusable guidance against a competitor across accounts. Use `competitive-battlecard`.
- the user wants to understand a competitor's product in depth outside an evaluation. Use `competitive-deep-dive`.
- the user is asking whether the home product's own pricing should change to win the RFP. Use `competitive-pricing-packaging-review`.

## Required outcome

For the one evaluation in front of the user, answer:

1. What is the evaluation trying to decide, for whom, by when?
2. What did the buyer state as requirements, in their words?
3. Which requirements are mandatory, which are table stakes, and which will actually differentiate?
4. For each differentiating criterion, what is verified about the competitor and the home product?
5. Where does proof matter more than a claim, and what proof event demonstrates it?
6. Which questions expose workflow, scale, governance, or implementation trade-offs the buyer should weigh?
7. Where is the competitor stronger, and is that criterion decisive?
8. Which criteria are irrelevant to this buyer and should not be overplayed?
9. Under what conditions should the team qualify out or decline to bid?
10. What is current enough to rely on, and what is unknown?

## Context acquisition

Read `references/CONTEXT.md` and `references/INTERNAL.md`.

### Irreducible minimum

- home product
- the evaluation context: what kind of evaluation, and the requirements or criteria as far as they exist
- the competitor or competitive set, when known

Retrieve before asking. When LMTY is connected it knows the home product and tracked set. When opportunity data or calls are connected, the account name finds the requirements the buyer has already stated.

If no requirements exist yet - the buyer has said "let's do a POC" and nothing more - that is a valid state, and the artifact changes shape: the objective, the questions that would establish criteria with the buyer, and the no-go conditions that already apply. No requirements map, no proof plan, no differentiator table. Filling those from what buyers "usually" want is inventing the buyer's requirements, and the plan will be built on them.

If the competitor is unknown and cannot be retrieved, plan against the tracked set the buyer is most likely evaluating and say so, or ask one question if the plan cannot proceed without it.

### Strongly preferred context

- the formal requirements document, RFP, scoring matrix, or questionnaire
- buyer priorities from calls, in their words
- current competitor capabilities from LMTY and primary evidence, with dates
- approved home-product proof, documentation, security and technical material
- prior POCs, POVs, or RFP responses against this competitor
- deal context: stage, stakeholders, timeline

## Source priority for this job

1. the buyer's stated requirements and priorities, from the document and the calls
2. approved home-product documentation for what can be demonstrated and claimed
3. current competitor evidence and LMTY state for the competitor's side of each criterion
4. prior evaluations against this competitor, labeled by how comparable they were
5. the team's read of what will matter, labeled as assumption

## Workflow

### Step 1 - State the evaluation objective

In one or two lines: what decision the evaluation feeds, who evaluates, who decides, the timeline, and the format (structured scoring, open POC, written RFP response, security review).

If the format is a written RFP, note that the competitor is answering the same questions and the buyer will compare answers side by side.

### Step 2 - Extract the stated requirements

List every requirement the buyer has stated, verbatim or closely paraphrased and labeled, with its source. Keep the buyer's numbering if there is one.

Distinguish:

- **stated in the document**
- **stated on a call** by a named stakeholder
- **implied** by the buyer's vocabulary or by a requirement's phrasing
- **assumed** by the team

Requirements written in a competitor's marketing language are a signal: note which, because they suggest who shaped the list.

### Step 3 - Classify each requirement

For each requirement, one of four classes:

- **Mandatory** - the buyer scores it pass/fail, whatever the products do. Keep the buyer's own label. A mandatory requirement the home product meets is proved fast and without drama; one it does not meet, or meets only by a workaround, goes straight to the no-go conditions (Step 9) - it is not "differentiating", it is the evaluation.
- **Table stakes** - weighted, but both products meet it and the buyer has not signalled it matters. Prove it efficiently; do not spend evaluation time winning it.
- **Differentiating** - weighted; the products meet it differently, or one does not; and the buyer has signalled it matters, or the weight says so.
- **Irrelevant to this buyer** - in the list, but nothing the buyer has said suggests it will weigh, and the weight is low. Do not overplay it, even if the home product wins it. A requirement the sponsor has flagged as inherited or suggested by the incumbent is a candidate for this class - and a question for the next call, not a unilateral demotion.

Say which classification rests on buyer evidence (the document's own type and weight, a stakeholder's words) and which on the team's read.

### Step 4 - Verify both sides of each differentiating criterion

For each differentiating criterion:

- home product: what approved documentation says can be demonstrated, and any limits
- competitor: what current evidence shows, with confidence and date

Use verified / partly verified / not observed in the sources checked / unknown. A competitor capability not observed on their public material is unknown, not absent - and in a POC the buyer will find out.

### Step 5 - Decide where proof beats claims

For each differentiating criterion the home product is strong on, decide whether it will be won by a claim, a document, or a demonstration. Prefer demonstration wherever the buyer could reasonably doubt the claim or the competitor could make the same one.

### Step 6 - Map each differentiator to a proof event

Build the proof plan: for each differentiating criterion, the specific thing the buyer will see or do - a live configuration, a data set run, a workflow walked end to end, a document delivered, a reference call - who runs it, what "pass" looks like, and what it depends on.

A differentiator with no proof event is a claim. Either design one or stop leaning on it.

### Step 7 - Design the questions that expose trade-offs

Write questions for the buyer that surface what a checklist hides: workflow fit, scale behavior, governance, implementation effort, migration cost, what happens at the edges.

These questions must be buyer-centered - they help the buyer evaluate well. They are not traps that only work if the buyer does not understand their own requirement. Do not write questions whose value depends on the buyer being misled about the competitor.

### Step 8 - Name where the competitor is stronger

For each differentiating criterion the competitor wins, say so, say whether the buyer has signalled it as decisive, and say what the honest response is: a workaround with its real cost, a reframe the buyer's own priorities support, or acknowledgment.

Then the criteria the home product wins that this buyer has not said they care about: list them, and say not to overplay them.

### Step 9 - Set the qualification and no-go conditions

State the conditions under which the team should qualify out, decline to bid, or scope down: a mandatory requirement the home product cannot meet, an evaluation designed around the competitor's strengths that the buyer will not adjust, a timeline the proof plan cannot fit, a buyer whose decision has already been made.

Write these before the evaluation starts. They are much harder to write honestly afterwards.

### Step 10 - Hand off broader work

| The user also wants | Run |
| --- | --- |
| the account picture beyond this evaluation | `competitive-deal-prep` |
| words for one objection now | `competitive-objection-response` |
| a reusable card for this competitor | `competitive-battlecard` |
| the competitor understood in depth | `competitive-deep-dive` |
| whether our price or packaging should change to win | `competitive-pricing-packaging-review` |

### Step 11 - Produce the artifact

Use `assets/evaluation-plan-template.md`.

Return it inline, then offer to save it. If the user asked for RFP answer text, draft only answers approved documentation supports. Mark for an owner's confirmation - product, security, or legal - every answer that describes a workaround for a requirement the product does not meet natively, every security or compliance answer, and every answer that commits to a timeline or a migration outcome. An answer that says "via the public API" to a mandatory requirement is a commitment the product team has to be willing to stand behind in week two.

## Evidence and reasoning rules

Read `references/TRUST.md` and `references/METHODOLOGY.md`.

Especially for evaluations:

- the buyer's requirements are the criteria; the competitor's feature list is not
- a claim that cannot be demonstrated in the evaluation is a liability, not an asset
- unknown is a state; in a POC the buyer will resolve it, so plan for that
- a question that only works if the buyer is misled is not a question this skill writes
- the user asking for a claim the evidence cannot support gets a refusal and the supportable version, not a softer wording of the false one
- a prior evaluation against this competitor is one evaluation; say how comparable it was

## Graceful fallback

Read `references/DEGRADATION.md` and `references/LMTY.md`.

### Fully connected

Requirements from the document and the calls, competitor side from LMTY and evidence, home side from approved documentation, history from prior evaluations.

### LMTY connected, no internal context

Competitor side is current; requirements and home-product proof come from the user. Label every requirement as user-reported and every home claim as needing confirmation against approved documentation.

### Research mode

Competitor side from current public evidence, point-in-time, dated. Say there is no tracked history and that the competitor's capabilities are as observed, not verified.

### Bounded-input mode

Use only the supplied material - typically the RFP and whatever the user attached - and say so at the top. Do not add competitor capabilities, home-product claims, or proof from memory. Where the material cannot verify a requirement on either side, write unknown and what would resolve it.

## References

- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/LMTY.md`
- `references/METHODOLOGY.md`
- `references/QUALITY.md`
- `references/TRUST.md`
