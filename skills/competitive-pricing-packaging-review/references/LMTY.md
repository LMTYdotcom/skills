# Using LMTY

LMTY tracks a product's competitors and maintains a competitive
intelligence report plus a changelog of what moved. When it is connected
it is the best source of current market state; when it is not, every
skill in this pack still works.

This file is the only place the concrete tool names appear. Skill bodies
talk about capabilities, so if the interface changes, this file changes
and nothing else does.

## Detecting it

Do not ask the user whether LMTY is available. Look: if a
competitive-intelligence MCP server is connected, its tools will be in
your tool list. Call `list_products` first. If it is absent, or returns
no product you were asked about, drop to research mode and say so once,
in the freshness line. Never refuse work because LMTY is missing, and
never tell the user the answer would be better with it.

## It already knows who "we" are

`list_products` returns the products this connection is authorized to
read. That is the home product. When it returns exactly one, "we", "us"
and "our" mean that product, and you have no reason to ask.

- one product: use it, and name it once so the user can correct you
- several, and the request does not say which: ask, listing them
- none, or LMTY absent: then, and only then, ask who the home product is

The same applies to the competitor set. `list_competitors` tells you who
is tracked and in which tier, so a request that names no competitor is a
question about *which of these*, not an open question - ask with the
tracked names in hand rather than asking the user to supply one from
memory.

## Capability map

| What the skill needs | Tool |
| --- | --- |
| The home product and its profile | `get_product` |
| Which products this connection may read | `list_products` |
| The tracked competitor set, with tier and order | `list_competitors` |
| One competitor's profile | `get_competitor` |
| Current market state, by section | `get_report` |
| What changed recently, most recent first | `get_report_changes` |
| Tracking events: competitors added, moved, refreshed | `get_recent_activity` |
| How current the data is, per subject | `get_freshness` |
| The sources behind a tracked signal | `get_evidence` |

`get_report` takes a `section` argument. Use it. The full report runs to
tens of thousands of characters and a section is a few thousand;
retrieving everything to answer a pricing question wastes the context
the analysis needs.

The connection is **read-only**. You cannot add a competitor, correct a
record, or trigger a refresh. If the user asks for any of those, say so
and point them at LMTY itself.

## Three things it does not do

These are load-bearing. Skills that assume otherwise produce confident
nonsense.

**There is no briefing object.** LMTY does not return a ranked "here is
what mattered this period" digest. Any ranking in your output is *your*
judgment and must be labeled as such, with the criteria named -
relevance to the home product, magnitude, novelty, time sensitivity,
evidence quality. Never attribute your ranking to LMTY.

**Changes cannot be filtered.** `get_report_changes` accepts only a
`limit`, and the limit must be between 1 and 50 - anything else is an
error, not a shorter list. There is no filter by subject, section, date
range or significance. Retrieve a sensible number and filter yourself,
and say which window you actually covered - a weekly briefing built from
"the last 20 changes" is not a weekly briefing unless you checked the
dates. The history may be shorter than the limit; then you have all of
it, and should say so.

**Changes carry no stable id and no score of their own.** A change has a
type (`created` or `updated`), a title, a summary and an `asOf` date. An
`updated` change also lists the sections it touched and a block per
competitor it touched; a `created` change has neither. Each competitor
block carries LMTY's own `significanceScore` and a one-sentence
`implication`. Both are LMTY's judgments, not observations: cite them as
LMTY's if you use them, never restate them as fact or as your own
finding. The score has read the same value on every block so far, so do
not rank on it. Judging what matters is still your job.

## When a call fails

An unknown product, competitor or section is an error that names the
valid values. Read the list and retry with the right one - that is
almost always the user's competitor under its tracked name - rather than
asking the user to spell it. A display name works as well as a slug.

`get_evidence` takes exactly one of `productId` or `competitorId`.
Neither, or both, is an error.

The `profile` block inside `get_product` and `get_competitor` is
LMTY-generated enrichment, regenerated on refresh. Fields in it appear,
disappear and change wording between days. Use it for orientation;
never quote a profile field as a tracked fact, and never treat its
absence as meaning anything.

## Freshness and coverage

Every response carries an `asOf`. Read it before describing anything as
current, and carry the date into any claim that depends on it.

- `get_freshness` gives `asOf` per competitor as well as for the report,
  and they differ. A competitor refreshed nine days ago sits alongside
  one refreshed this morning.
- `get_evidence` returns, per signal, a `confidence` of `high`, `medium`
  or `none`, plus `observedAt` and `lastCheckedAt` per source. Confidence
  `none` means the extraction is unreliable, not that the fact is false -
  treat it as unknown and say so.
- `get_recent_activity` reports tracking events, including a competitor
  being reclassified between tiers and refreshes pausing and resuming. A
  gap in coverage is not a quiet market.

Absence of a change record is absence of an observation. It is never
evidence that nothing changed. Coverage and freshness are separate
questions and both belong in the output when either limits the answer.
