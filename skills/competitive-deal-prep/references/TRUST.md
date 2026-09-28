# Trust and Evidence Policy

This policy is shared by every LMTY-authored PMM skill.

## Core epistemic model

Every material statement belongs to one of four classes.

1. **Observed fact**
   - Directly supported by a source, an LMTY report item, an LMTY change record, or another connected system.
   - Preserve dates, scope, source, and freshness.

2. **Interpretation**
   - A reasoned reading of one or more observed facts.
   - State the inference explicitly and attach confidence when the interpretation could materially affect a decision.

3. **Implication**
   - A consequence the user may want to investigate because of the facts and interpretation.
   - Do not present an implication as a known business outcome unless internal evidence supports it.

4. **Action option**
   - A possible next move conditioned on goals, constraints, and company context.
   - Do not imply the action is correct merely because a competitor acted.

The required sequence is:

**fact -> interpretation -> implication -> action option**

A skill may stop at any earlier stage when evidence is insufficient.

## Never infer motive without evidence

Do not claim why a competitor changed pricing, positioning, packaging, product, or target segment unless a reliable source states or strongly supports the motive.

Bad:
- "Competitor A raised prices because growth is slowing."

Acceptable:
- "Competitor A raised the Pro plan from $49 to $69. One plausible implication is that buyers may re-evaluate value at that tier. The available evidence does not establish why the company made the change."

## Freshness is part of the claim

Treat freshness as first-class data, not metadata to hide in a footnote.

When LMTY is available, inspect and preserve:
- product as-of date
- last successful refresh
- coverage period
- observed date for changes
- capture or last-seen date for evidence
- stale, frozen, lapsed, researching, or partial states

When LMTY is not available:
- state the source collection date or the document dates
- never imply longitudinal coverage from a point-in-time web scan
- distinguish "not found" from "did not happen"

## Coverage is separate from freshness

A source can be fresh and incomplete. Treat these separately.

Recommended coverage labels:
- complete enough for the requested decision
- partial
- researching
- unknown

When coverage is partial, say what is missing and how that limits the conclusion.

## Source hierarchy

Use source relevance, directness, and recency rather than prestige alone.

Typical order for external competitive claims:
1. primary competitor source for what the competitor says or ships
2. LMTY structured evidence tied to the claim
3. public product documentation, pricing, changelog, release notes, filings, official posts
4. direct customer or prospect evidence when the question is about perception, win/loss, or usage
5. internal deal evidence and call transcripts for field reality
6. independent third-party evidence for corroboration
7. community or social evidence for sentiment and emerging signals, clearly labeled

For company-specific conclusions, internal truth often outranks external truth. For example, a CRM loss reason or buyer interview may matter more than a competitor homepage when answering why the user's company loses.

## Contradictions

When sources conflict:
- do not average them into a false certainty
- identify the contradiction
- prefer the source closest to the claim being made
- preserve dates, because the conflict may reflect a change over time
- reduce confidence if the conflict cannot be resolved

## Evidence density

Every material competitive claim in a decision artifact should have enough provenance that a user can inspect why it is there.

For compact artifacts, group citations at the bullet, row, or section level rather than making the output unreadable.

## Confidence

Use confidence only where it adds decision value.

Suggested meanings:
- **High**: directly evidenced, current enough, and coverage is strong
- **Medium**: supported by multiple signals or one strong signal but with a meaningful gap
- **Low**: plausible and useful to consider, but evidence is thin, indirect, or conflicting

Do not convert confidence into fake percentages unless the underlying method genuinely supports them.

## Recommendations

A recommendation is permitted only when the skill has enough context about the user's goals, constraints, product, and relevant evidence.

If company context is missing, prefer:
- "consider"
- "investigate"
- "pressure-test"
- "this creates a question worth answering"

rather than:
- "you should"
- "the company must"
- "the correct move is"

This is a rule about the verb, not the tone. A confident, well-argued paragraph that ends in "we should move to usage-based pricing" is a directive, however many caveats surround it. If the internal economics, customer evidence and company goals are not in front of you, the honest output is the decision and the evidence needed to make it - not the decision made on your behalf.

Rewrite a directive as the question it was hiding:

| Do not write | Write |
| --- | --- |
| "We should match their price cut." | "This raises whether to match. Deciding it needs our margin at the lower price and whether price is the stated loss reason in recent deals." |
| "Lead with governance in the positioning." | "Governance is the differentiator this evidence supports. Worth pressure-testing against win/loss before it becomes the lead." |
| "Drop the free tier." | "Their free-tier removal makes ours a live question. What share of paid conversions start free?" |

## Confidence, and when to lower it

State confidence where it changes what someone would do with the claim.

Lower it explicitly, and say why, whenever:

- two sources disagree and the conflict is unresolved - do not average them into a middle number that no source supports
- the only evidence is second-hand, or is a single account
- the data is stale relative to the decision, or coverage is partial
- the claim depends on an inference rather than an observation

Name the reason in the same sentence: "medium confidence - two of the three sources trace back to the same press release" is useful; "medium confidence" alone is not.

## Never fill a gap with a plausible sentence

The strongest pull in this work is toward completeness: a section with nothing in it looks like a failure, so it gets filled. Every invented objection, customer example, segment detail or win story in this pack's outputs arrived that way.

If a section has no evidence, say what is missing and what would fill it. A card that says "no validated objections yet - pull the last 20 calls where this competitor was named" is more useful than three plausible objections, and it cannot mislead a rep in front of a buyer.

## Customer and deal evidence

Never generalize one anecdote into a market truth. Label:
- single account signal
- repeated pattern
- quantified pattern

A compelling call clip can be excellent evidence for an objection, but it is not automatically representative of the market.

## Output requirement

Every skill output that contains material reasoning should make it possible to answer:
- What do we know?
- How current is it?
- What is interpretation rather than observation?
- What important evidence is missing?
- What could we do next?
