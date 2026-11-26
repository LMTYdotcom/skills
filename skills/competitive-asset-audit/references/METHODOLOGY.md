# Competitive Asset Audit Methodology

## Core principle

An audit is complete for the scope it names, or it says which part it read. Its value is that when it says "these are the claims we should not be making", the list is the whole list for that scope. When a run can read only part of it, the first line says "partial", with [n] of [m] assets read and which were not: a partial audit presented as whole is the worst outcome, because nobody checks the rest.

That is why the audit does not fix anything. Every hour spent rewriting one asset is an hour the scope was not covered, and a reader who gets three rewrites and a partial list has neither.

## Claims, typed

The unit is the claim, and the claim's type decides who can verify it:

| Type | Verified against |
| --- | --- |
| competitor capability | current competitor evidence, with confidence and date |
| competitor pricing / packaging | the report's pricing section, and the public profile's plans on sale and price history |
| competitor customers / position | current competitor evidence, and the public profile's known customers with how each is known |
| competitor security / compliance | the certifications the public profile records, with who states each |
| home-product capability | approved product facts and documentation |
| home-product pricing | approved pricing |
| home-product security / compliance | approved security documentation only |
| customer reference | the approved reference list |
| win / loss / objection frequency | deal evidence: interviews, calls, records |
| comparative superlative | both sides, and a measurement if the word implies one |

A claim checked against the wrong source is not checked. A "we win on integrations" line cannot be verified by a product doc; it needs deal evidence, and usually there is none.

## The five marks

- **Supported and current** - leave it.
- **Supported but stale** - the words are behind a newer source. A price two revisions old, a tier renamed, a date passed. Not fine: a rep quoting it is quoting a wrong figure.
- **Unsupported** - a source that should hold it does not. It may be true. The company should still not be saying it, because the first buyer who asks "according to whom?" ends the conversation.
- **Contradicted** - evidence opposes it as of the asset's own date. Highest urgency of the five.
- **Unknown / insufficient coverage** - the sources checked do not reach it. Say what would.

**Stale or contradicted.** A figure behind a newer source is stale when the asset is dated earlier than the source: "the asset (dated 2026-03-02) says $7.75; the current source says $7.91 as of 2026-10-14". Nobody has to prove the old figure was once right. Where the competitor's price history holds the earlier value, cite it. Contradicted is for a claim the evidence opposes as of the asset's own date, such as a plan the asset names that the price history shows was never offered. A claim of absence follows the same rule: when an asset says a competitor is "not SOC 2 certified" and the competitor's statement of a SOC 2 report was first seen after the asset's date, the claim is stale, with that date said. It is contradicted only when the evidence against it was already there on the asset's own date.

**Unsupported or unknown.** In a bounded audit, a claim for which no source of the needed kind was supplied (a price claim when no pricing source was given) is unknown / insufficient coverage, not unsupported. When a source of the right kind is there and silent: unsupported if that source is the full list for its kind (the approved claims, the approved references, the approved price list), because not being on it is the finding; unknown if the source is partial by nature (a report section, a product document, a competitor's profile or pages).

**No guess beside a mark.** Never write "likely holds", "probably still true" or "almost certainly" beside unknown, unsupported or stale. A reader takes the guess and drops the mark. Say what was checked and what would settle it.

Keep unsupported and contradicted strictly apart. Merging them either scares the owner off true claims or lets false ones hide among merely unsourced ones. The approved claims are the one source that is complete for the home product, so a home-product claim they deny is contradicted, not unsupported: unsupported is for a claim they are silent on.

## Absence

A competitor's public material not mentioning something is unknown, not contradicted. Competitors do not document everything; LMTY's coverage has gaps it reports; a feature can exist behind a login. An audit that marks "Northwind lacks X" as *supported* because X is absent from Northwind's site has made the same error the claim did.

Write what was not found as "not on LMTY's record as of [date]" or "not found on [page] as of [date]". A plan or logo a page stopped listing is "no longer listed as of [date]", never "removed", "dropped" or "churned", unless a source says so.

## Deduplication

A claim that lives in four assets is one claim. Verify once; list the four homes. Two things fall out:

- the fix list is shorter than the instance count, which is good news for the owner
- claims that *vary* across assets - $8 here, $10 there - are found, and each variant is a defect whether or not either is right

## Newly broken versus no dated change found

For every claim not current, the audit says which it is:

- **Newly broken** has a dated change behind it - a competitor moved, the home product shipped, a reference stopped being listed. Normal decay. The lesson is cadence.
- **No dated change found** means no change in the window read bears on it. That is a statement about the window, not the claim's history: a change record read ten entries deep, or one that began last month, finds no change for anything. Call it **always weak** only when the asset's owner or its history confirms it never had a source. Then the lesson is process: how did an unsourced claim get into a public page?

Different owners care about each. The audit gives both.

**Dates.** A change-record entry carries the date LMTY recorded it, not the date the competitor moved: write "recorded on". A dated event or a price history entry carries the change's own date only when its basis says the date is when it happened; a published date is "reported on", an observed one "seen on". Several entries about one move are one change.

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

The audit is only as good as what it checked against. The table says which sources were used, their dates, and where coverage was missing - so the reader knows an "unknown" is about the sources, and can decide whether to get better ones. Each competitor gets its own row and its own as-of date, because one refreshed nine days ago sits beside one refreshed this morning. A page read outside LMTY in the run is a row of its own, marked as the assistant's own reading, with its link and the date read.

## Exposure is a judgment

The ranking is the assistant's, by the two criteria above. Say so above the table. LMTY records changes; it does not rank what matters to these assets.

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
