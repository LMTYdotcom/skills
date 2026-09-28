---
name: competitive-deal-prep
description: Prepare an account team for one specific competitive opportunity - the deal state, who they are actually up against, what the buyer said matters in their own words, the three questions that decide the next meeting, proof that fits this account, and the risks and unknowns - from current market truth plus CRM, call, and account context. Use for "prep me for this deal", "we're up against Northwind at Globex", "I have a call with this account tomorrow", "what should the team know before the next meeting", and any request about one named account or opportunity. Not for one live objection on its own, a reusable battlecard, or the design of a formal POC or RFP evaluation.
license: MIT
metadata:
  author: LMTY
  com.lmty.category: ci
---

# Competitive Deal Prep

## Mission

Get an account team ready for the next meeting on one competitive deal without inventing what the buyer wants, what the competitor has, or how the deal will go.

The output is preparation, not a close plan. It says where the deal stands, who is really in it, what the buyer has actually said matters, what the next meeting has to establish, which proof fits, and where the team is exposed - each line traceable to a call, a record, a market source, or labeled as an assumption.

## Use this skill when

- a rep or PMM asks to be prepared for a named account, opportunity or meeting
- the team is "up against" a named or unnamed competitor in one deal
- someone wants to know what matters before the next call with this account
- a deal has stalled and the team wants to understand the competitive picture in it
- a request bundles deal prep with one objection or a proof ask - take the account, and route the pieces that belong elsewhere (Step 10)

## Do not use this skill when

- the user has one live objection and needs words now. Use `competitive-objection-response`.
- the user wants reusable guidance for many accounts against one competitor. Use `competitive-battlecard`.
- the main job is designing or responding to a formal evaluation - a POC, POV, or RFP with stated criteria. Use `competitive-poc-rfp-plan`.
- the user wants to understand a competitor in general rather than in this deal. Use `competitive-deep-dive`.
- the user wants to know why deals like this are won or lost across many accounts. Use `competitive-win-loss-analysis`.

## Required outcome

For the one account in front of the user, answer:

1. Where does the deal stand, and what is the next event that matters?
2. Which competitors and alternatives are actually in this deal, on what evidence?
3. What has the buyer said they care about, in their words?
4. Which evaluation criteria are confirmed by the buyer, and which are the rep's assumptions?
5. Against those criteria, where is each competitor currently stronger or weaker?
6. What are the three questions the next meeting must answer?
7. What proof fits this account's stated concerns?
8. What are the risks, unknowns, and places the team is poorly positioned?
9. What changed recently on the competitor's side that this account would notice?
10. What should the team do before the meeting?

## Context acquisition

Read `references/CONTEXT.md` and `references/INTERNAL.md`.

### Irreducible minimum

- home product
- the account or opportunity

Retrieve before asking. When LMTY is connected it knows the home product and the tracked competitor set. When opportunity data is connected, the account name is enough to find the record; do not ask the user to paste stage, value or the competitor field.

The competitor is not an irreducible input. Retrieve it from the opportunity's competitor field, the calls, the notes, or the tracked set. If several are active and the request names none, show the observed set with the evidence for each - do not pick one.

If the account cannot be found in any connected source and the user has supplied nothing about it, ask one question: which account, or paste what you have. Then stop.

### Strongly preferred context

- opportunity record: stage, value, segment, stakeholders, competitor fields, next step, dates of last update
- recent calls and meeting notes for this account, with the buyer's wording
- team communication about the account
- current LMTY state, evidence and recent changes for each competitor in the deal
- prior objections raised in this account and whether they were resolved
- approved proof, references and customer examples
- product usage or trial telemetry for this account, when permissioned

## Source priority for this job

1. what the buyer said, from calls and notes, for priorities and criteria
2. the opportunity record for state, stakeholders, and dates - with its last-updated dates
3. approved company proof for what can be claimed
4. current competitor evidence and LMTY state for the competitive picture
5. rep notes and team communication for assumptions and history, labeled as such
6. prior deal outcomes only when they exist and are labeled by representativeness

## Workflow

### Step 1 - Establish the deal state

From the opportunity record and the most recent call or note:

- stage, and when it was last changed
- proposed value and seat count, if recorded
- stakeholders named so far, with roles as recorded
- the next critical event: a meeting, a security review, a procurement deadline, a bake-off
- how current each of those is

State the date of the newest evidence. A record untouched for weeks describes the deal as it was; say so rather than presenting it as today.

### Step 2 - Identify who is actually in the deal

List every competitor or alternative with the evidence that puts it there:

- named by the buyer on a call
- in the opportunity's competitor field, with the date it was set
- mentioned in notes or team channels
- the status quo or "do nothing", when the buyer has said as much

A competitor the rep assumed is in the deal is an assumption. When several are active, keep all of them; when none is evidenced, say the deal's competitive set is unknown and what would establish it.

### Step 3 - Extract buyer priorities in their own words

Pull what the buyer said matters, quoted or closely paraphrased and labeled, with who said it and when.

Keep the buyer's framing. "If we can't get through the security review nothing else matters" is a priority statement; do not translate it into "security is a concern".

Note when different stakeholders said different things.

### Step 4 - Separate confirmed criteria from rep assumptions

Build two lists:

- **Confirmed by the buyer**: a criterion the buyer stated or a requirement they named
- **Assumed by the team**: anything from rep notes, the CRM risk reason, or the user's framing that no buyer statement supports

When the record and the calls disagree - the CRM says price, the call says security review - show the conflict, say which source is stronger for the question, and do not blend them.

### Step 5 - Map competitors to the criteria

For each confirmed criterion, and each competitor in the deal, state from current evidence:

- where the competitor is stronger
- where the home product is stronger, with approved proof
- where neither is established - unknown, not "they don't have it"

Use LMTY evidence with its confidence and date. A capability not observed on a competitor's public site is not a gap. Say what would check it.

### Step 6 - Name the three questions the next meeting must answer

Not discovery questions in general: the three things that, unanswered, leave the team unable to position. Typically:

- which requirement is hard and which is preference
- who decides, and against what
- what the buyer has already concluded about a competitor and from what

Each should change what the team does next.

### Step 7 - Prepare likely objections, only when grounded

Include an objection only if this account raised it, or repeated evidence across a stated number of similar deals shows it. Label which.

For each: the buyer's words, the verified premise, a short posture, and what not to claim. For a full treatment of one objection, hand off to `competitive-objection-response`.

Do not generate a list of objections the competitor "usually" draws from memory.

### Step 8 - Select proof that fits this account

Match approved proof to the confirmed criteria:

- documentation for a stated requirement
- a customer reference in the same segment or with the same concern, only from the approved list
- a measured outcome relevant to a named priority

Name what proof is missing for a confirmed criterion. Do not fill it with a plausible story.

### Step 9 - Risks, unknowns, and where the team is exposed

Be plain:

- requirements the competitor meets and the home product does not, or not yet verified
- stakeholders unmet or unheard
- a stale record, a champion who went quiet, a review not started
- assumptions the plan currently rests on
- anything that suggests the deal may be a poor fit

A prep that has no risks section has not been done.

### Step 10 - Recommend preparation, and hand off the rest

Give a short checklist: what to verify, what to bring, who to involve, what to ask first. Actions, not a guaranteed path to a close.

Route what is not this job:

| The user also wants | Run |
| --- | --- |
| words for one objection right now | `competitive-objection-response` |
| a reusable card for this competitor | `competitive-battlecard` |
| the design of the POC, POV or RFP | `competitive-poc-rfp-plan` |
| a full profile of the competitor | `competitive-deep-dive` |
| why we win or lose deals like this in general | `competitive-win-loss-analysis` |

### Step 11 - Produce the artifact

Use `assets/deal-prep-template.md`.

Return it inline, then offer to save it. Keep account detail to what the team needs; this document travels.

## Evidence and reasoning rules

Read `references/TRUST.md` and `references/METHODOLOGY.md`.

Especially for deal prep:

- the buyer's words outrank the rep's notes for what the buyer wants
- a CRM field is what was recorded, on the date it was recorded
- a competitor is in the deal when evidence puts it there, not when it is the usual suspect
- unknown is a state; write it, and what would resolve it
- one prior deal is one prior deal
- private account data stays in this artifact; it does not become a market claim anywhere else
- a source's interpretation - the rep's risk reason, LMTY's implication sentence, an interviewer's paraphrase - is quoted as that source's

## Graceful fallback

Read `references/DEGRADATION.md` and `references/LMTY.md`.

### Fully connected

Deal state from the record, priorities from the calls, competitive picture from LMTY, proof from approved sources.

### LMTY connected, no deal context

The user supplies the account situation. Prepare from what they give and current market state. Label every buyer priority as reported by the user, and say the prep has no independent view of the account.

### Deal context connected, no LMTY

Deal state and priorities from internal sources; competitor facts from current public evidence, point-in-time, with dates. Say there is no tracked history.

### Research mode

Neither connected. Prepare from what the user supplies and public evidence. State that the prep rests entirely on the user's account of the deal.

### Bounded-input mode

Use only the supplied material, and say so at the top. Do not add competitor facts, proof, or deal history from memory. Where the material cannot answer a question the meeting needs, write the question, not a guess.

## References

- `references/CONTEXT.md`
- `references/DEGRADATION.md`
- `references/INTERNAL.md`
- `references/LMTY.md`
- `references/METHODOLOGY.md`
- `references/QUALITY.md`
- `references/TRUST.md`
