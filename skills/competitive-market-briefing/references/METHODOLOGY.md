# Market Briefing Methodology

## Briefing versus alerting

An alert answers "something happened."

A briefing answers:
- what changed over a period
- which changes matter most
- how they relate to one another
- what remains unresolved

The value is compression and continuity, not notification volume.

## Significance criteria

LMTY gives no ranking, and its own significance marks are not one to borrow. Consider:
- customer relevance
- impact on differentiation
- pricing/value impact
- target-segment movement
- novelty
- strategic proximity
- magnitude
- confidence

## Calm briefing posture

Avoid:
- "Northwind is coming for us"
- "We must respond immediately"
- every item labeled urgent

Prefer:
- observed movement
- calibrated relevance
- evidence
- watch conditions

## Briefing continuity patterns

Useful labels:
- **first reported here** - first appearance in this run of briefings, written with the earlier briefing's date: "first reported here, not in the briefing of [date]". It says nothing about when the competitor moved
- **continuing** - pattern persists
- **accelerating** - stronger or more frequent evidence
- **reversing** - movement changed direction
- **confirmed** - earlier weak signal now has stronger evidence
- **cooling** - previously important item has not continued

These labels require historical evidence: an earlier briefing the run can see, or change history that shows the earlier movement. Give the earlier date with the label. A scheduled run that cannot see its earlier briefing uses none of them.

## Matching against the last briefing

- a feed event by its `eventId`, which is the only stable key either source offers
- a change record by competitor, title and the date it was recorded
- an item reported before comes back only when it moved: reversed, confirmed, or gained a date of its own

The "Covered" line at the foot of each briefing (the dates and the event ids reported) is what makes this possible for the next run.
