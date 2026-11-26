# Competitive asset audit: [scope]

**Read:** [n] of [m] assets in scope [name the ones not read and why] · evidence checked for [n] of [m] competitors named in them · change record and dated events read back to [date], [n] entries [or: to their start] [On a product with no report yet, in place of the change record: "no report yet, so no report section and no change record was read"; the dated events are still counted.] [A partial audit says "Partial audit" here, first.]
**Mode:** [account and public profiles / public profiles only / assets only / bounded input]
**As of:** [audit date] · competitor data: each competitor's own date, in "Source and freshness" · approved facts dated [date, or: none supplied]

## Summary

| | Count |
| --- | --- |
| Assets audited | [n] of [m] |
| Distinct claims | (of [N] claim instances) |
| Supported and current | |
| Supported but stale | |
| Unsupported | |
| Contradicted | |
| Unknown / insufficient coverage | |

**Stale:** the asset is behind a newer source. **Unsupported:** no proof found in a source that should hold it; it may be true. **Contradicted:** current evidence says otherwise, as of the asset's own date. **Unknown:** the sources checked do not reach it. No mark is a guess at the truth.

## High-risk claims

[The order is the assistant's judgment, by two criteria: how many people the claim reaches, and what it costs if acted on. Up to ten rows; the tables below carry the rest.]

| # | Claim | Mark | Type | Assets (reach) | Consequence if acted on | Newly broken (date, how known) / no dated change found | Route to |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Stale claims

[Leave out when empty. Evidence first seen after the asset's date makes a claim stale, not contradicted: give that date.]

| Claim | Asset's date | Current figure or wording | Source, date | Assets |
| --- | --- | --- | --- | --- |

## Unsupported claims

[Leave out when empty. Name the source checked: its silence counts only when it is the full list for its kind.]

| Claim | Source checked | What would support it | Assets |
| --- | --- | --- | --- |

## Contradicted claims

[Leave out when empty. Never on a page read outside LMTY alone. A home-product claim the approved claims deny goes here, not under "Unsupported claims".]

| Claim | Evidence against | Source, date | Assets |
| --- | --- | --- | --- |

## Unknown

[Leave out when empty.]

| Claim | What was checked | What would settle it |
| --- | --- | --- |

## Supported on one party's word

[Claims marked supported whose only support is the party they flatter: the home company about itself, or a competitor about itself, quoted in an asset. Leave out when there are none.]

| Claim | Whose word | Where, date | Assets |
| --- | --- | --- | --- |

## Claims that vary across assets

[Leave out when none vary.]

| Claim | Version A (asset) | Version B (asset) |
| --- | --- | --- |

## Home-product changes the market data does not show

[Leave out when no approved home-product facts were supplied, and say so in "Source and freshness".]

| Change | Date, and how it is known | Claims it affects |
| --- | --- | --- |

## Assets affected

[Up to 15 rows, most exposed first; then "and [n] more".]

| Asset | Type | Owner | Last updated | Reach | Claims needing attention |
| --- | --- | --- | --- | --- | --- |

## Source and freshness

[One row per competitor, with its own as-of date and whether its public profile was read; one row per other source. A page read outside LMTY in this run is a row of its own, marked "assistant's own reading", with its link and the date read.]

| Source | Used for | As of | Coverage gaps |
| --- | --- | --- | --- |

## Next owner

[Only the rows this audit needs.]

| Work | Run / owner |
| --- | --- |
| Replacement lines around [change] | `competitive-enablement-refresh` |
| Rebuild [battlecard] | `competitive-battlecard` |
| Reconsider external message | `competitive-messaging-audit` |
| Verdict on [competitor claim] | `company-claim-check` |
| Price record behind [price claim] | `company-pricing-history` |
| Certifications behind [security claim] | `company-security-claims` |
| Known customers behind [customer claim] | `company-customer-map` |
| Rewrite [comparison page] | page owner (no skill in this pack writes it) |

## Short form

[For one asset with nothing needing attention, or a thin record: the Read line, the Summary table, "Source and freshness", and one line: "No claim in this asset needs attention as of [date]." On a repeat run with nothing new: "Nothing changed standing since [date]."]
