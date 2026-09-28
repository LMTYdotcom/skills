# Competitive Asset Audit Methodology

## Core principle

An audit is complete or it is not an audit. Its value is that when it says "these are the claims we should not be making", the list is the whole list for the scope.

That is why the audit does not fix anything. Every hour spent rewriting one asset is an hour the scope was not covered, and a reader who gets three rewrites and a partial list has neither.

## Claims, typed

The unit is the claim, and the claim's type decides who can verify it:

| Type | Verified against |
| --- | --- |
| competitor capability | current competitor evidence, with confidence and date |
| competitor pricing / packaging | current competitor pricing evidence |
| competitor customers / position | current competitor evidence |
| home-product capability | approved product facts and documentation |
| home-product pricing | approved pricing |
| home-product security / compliance | approved security documentation only |
| customer reference | the approved reference list |
| win / loss / objection frequency | deal evidence: interviews, calls, records |
| comparative superlative | both sides, and a measurement if the word implies one |

A claim checked against the wrong source is not checked. A "we win on integrations" line cannot be verified by a product doc; it needs deal evidence, and usually there is none.

## The five marks

- **Supported and current** - leave it.
- **Supported but stale** - the fact holds, the words are behind. A price two revisions old, a tier renamed, a date passed. Not fine: a rep quoting it is quoting a wrong figure.
- **Unsupported** - nothing backs it. It may well be true. The company should still not be saying it, because the first buyer who asks "according to whom?" ends the conversation.
- **Contradicted** - evidence says otherwise. Highest urgency of the five.
- **Unknown / insufficient coverage** - the sources checked do not reach it. Say what would.

Keep unsupported and contradicted strictly apart. Merging them either scares the owner off true claims or lets false ones hide among merely unsourced ones.

## Absence

A competitor's public material not mentioning something is unknown, not contradicted. Competitors do not document everything; LMTY's coverage has gaps it reports; a feature can exist behind a login. An audit that marks "Northwind lacks X" as *supported* because X is absent from Northwind's site has made the same error the claim did.

## Deduplication

A claim that lives in four assets is one claim. Verify once; list the four homes. Two things fall out:

- the fix list is shorter than the instance count, which is good news for the owner
- claims that *vary* across assets - $8 here, $10 there - are found, and each variant is a defect whether or not either is right

## Always weak versus newly broken

For every claim not current, the audit says which it is:

- **Newly broken** has a dated change behind it - a competitor moved, the home product shipped, a reference churned. Normal decay. The lesson is cadence.
- **Always weak** never had a source. The change, if any, just exposed it. The lesson is process: how did an unsourced claim get into a public page?

Different owners care about each. The audit gives both.

## Home-product changes

The market record shows the competitor moving. It does not show the home product moving. A certification obtained last month makes "we are pursuing SOC 2" stale; an integration shipped makes a comparison table newly wrong in the home product's favor. The audit checks approved home-product facts against the assets' home-product claims as a distinct pass, because nothing else will surface them.

## Exposure and consequence

Rank by both:

**Exposure** - who sees it. A public comparison page, then a high-usage card, then a deck used weekly, then an archived module. Usage data if there is any; asset type as a proxy if not.

**Consequence** - what happens if someone acts on it. A price a buyer checks, a capability a buyer tests, a certification security verifies, a reference that did not consent, a superlative a competitor's lawyer reads.

A contradicted price on a public page is the top of the list. An unsupported adjective in an archived deck is the bottom, and still on the list.

## Routing

Each prioritized claim gets an owner and a destination. The audit routes; it does not draft. When the user insists on fixes in the same pass, do the audit first and completely, then say which skill does each fix and offer to run it as a separate job.

## The source and freshness table

The audit is only as good as what it checked against. The table says which sources were used, their dates, and where coverage was missing - so the reader knows an "unknown" is about the sources, and can decide whether to get better ones.

## What not to optimize for

Do not optimize for:

- fixing things
- a low count of problems
- treating every finding as equally urgent
- marking absence as contradiction to make the list look decisive

Optimize for:

- the whole scope, every material claim
- the right source for each claim's type
- unsupported kept apart from contradicted
- one entry per distinct claim, with every home
- exposure and consequence first
- a reader who knows exactly what to do next and with whom
