# Security Claims Methodology

## What a public record can and cannot establish

A profile's security record is what public pages said. It can establish that a claim was made, by whom, on which page, and when the page was last seen saying it. It can establish that an incident was reported, by whom, and when the report was published.

It cannot establish that a certification is held, current or in scope for the product being bought. That is established by the report or certificate itself, which is not public and not on the record. It cannot establish that no incident occurred: an incident nobody published is on no record.

So the checklist has two halves. The first is what is on record, each line with who states it. The second is what to ask the vendor for, which is where the evidence is.

## The reading budget

At most eight calls.

| Call | What it reads |
| --- | --- |
| 1 | The search. It often returns only the company or only the product |
| 2 and 3 | The overview of the profile found, then of the other one, which the first overview's closest relations name: the product a company offers, or a product's maker. Each gives the counts of timeline entries and of facts by kind |
| 4 and 5 | The certification facts of each profile that counts any |
| 6 and 7 | The timeline of each profile, newest first, the largest page the tool allows |
| 8 | A second search under the other obvious name, or one further page of whichever list is longest |

A read that a zero count makes pointless is not made, and its call goes to a further page of the timeline that holds the security entries. When the budget ends before a list does, stop and report the read as N of M. Do not describe the part that was not read, and do not go past eight to finish it: say what a second run would read.

## Reading a certification fact

A certification fact is a name with a grade and a source.

| The record gives | Write |
| --- | --- |
| The name | Exactly as recorded, in the "What is claimed" cell |
| The grade | In its own cell, and in the plain-words line under the table |
| The source's site and address | Who states it, and the page |
| The date last seen | "last seen [date]": the latest source that still said it |
| The date first seen | "first seen [date]", only in the changes, and never as when the certification was obtained |
| A start that a source states | "the vendor states since [date]" |
| An end, with how it was decided | "no longer listed as of [date]" when its pages stopped listing it; "ended, per [who]" only when a source says so |
| LMTY's own confidence, when it is uncertain or a guess | One clause in the row, cited as LMTY's |

The kind is wider than its name. It also holds laws and frameworks that a page names, such as a privacy law or a security framework. A row for one is the vendor's stated claim under its recorded name: the checklist does not call it a certification, and does not say the vendor complies.

The kind holds credentials that people hold as well, such as a security manager's or an auditor's personal credential. A vendor does not hold one: its staff do. List these apart, as "credentials held by staff, as the vendor states them", with the page and the date last seen, and never in the count of the vendor's claims. When it is unclear what a recorded name denotes, leave it in the table as recorded and say so.

One claim can be recorded under two names: "ISO 27001" and "ISO/IEC 27001", or a name with and without its type. Keep both rows as recorded and say they may be one claim. Do not merge them by guess, and do not read one spelling leaving a page as the claim leaving it.

Nothing else is on record for a claim. The five things a reviewer needs next - the report's date, the period it covers, its scope, the auditor and an expiry - are listed as not on record every time.

## The words

| Do not write | Write |
| --- | --- |
| "Northwind is SOC 2 certified." | "Northwind states SOC 2 Type II on its security page (official, last seen 2025-05-02)." |
| "Northwind is compliant with ISO 27001." | "Northwind's trust page lists ISO 27001 (official, last seen 2025-05-02). No certificate, scope or date is on record." |
| "Northwind lost its certification." | "ISO 27001 is no longer listed on Northwind's security page as of 2025-04-11. The record does not say why." |
| "Northwind has no certifications." | "No certification is on LMTY's record for Northwind or its product as of 2025-05-02." |
| "Northwind was breached in March." | "A report of unauthorized access was reported on 2025-03-04 by a trade outlet. Northwind's own pages on record do not mention it." |
| "Northwind has never had a breach." | "No incident is on LMTY's record in the 50 of 212 timeline entries read, as of 2025-05-02." |
| "Northwind recently added a new certification." | "A second certification was first seen on Northwind's security page on 2025-04-20. The record does not say when it was obtained." |
| "Northwind had a security incident on March 9." (a notice of degraded service) | "1 service notice, reported on 2025-03-09: degraded sign-in. Not a security incident by its statement." |
| "Northwind dropped ISO 27001." (a fact with no end, and a timeline entry) | "ISO 27001 is on record as a claim with no end, last seen on Northwind's security page on 2025-05-02; a timeline entry says its trust page no longer lists it as of 2025-04-11. The record holds both." |
| "Their security posture is strong." | Nothing. The checklist gives no verdict. |

## Who states it

Compare each source's site with the profile's website.

- the vendor's own site: "the vendor states"
- a certifying body's register, a marketplace or a directory: name it, and say what it is. A listing is that party's page, not the vendor's
- press: "reported by [outlet]"
- a claim graded chatter: under "One unverified source says", never in the claims table. Its source can be a related company's page, such as a parent's or an acquirer's compliance page: say whose page it is, and never give it the vendor's voice

An official grade means one of the parties said it. For a certification that is nearly always the vendor. When it is the other party, say so: a certifying body's own register is the stronger voice, and the row says whose page it is.

When the same claim is graded official on one profile and chatter on the other, it is one row in the claims table, on the official source, and the unverified mention is listed under its own heading as well.

## One incident, many reports

Incidents arrive on the record as timeline entries, and most are dated by when a source published a report. One incident reported by five outlets is five entries. The timeline cannot be narrowed by kind: read it, and pick the incident entries by their `kind` and `statement`.

The kind is a filing label. It also holds notices of an outage or degraded service, and the statement says which an entry is. A service notice is never a row under incidents: count them on one line, with the span of their dates, and call none of them a breach.

Merge when the entries agree on what was affected and on the event: the same named incident, the same systems or data, the same date given for it. Then:

- one row, the description in the sources' words
- the strongest basis among the merged entries, and the earliest date of that basis. Five entries dated by a report are one incident, "reported on" the earliest of the five dates
- the number of reports merged, and every one of them as a source, cited by its number in the source list
- "who reports it": the vendor's own notice, outlets, or both, kept distinguishable

Do not merge two reports because they are close in time. Two entries a week apart can be one incident reported twice or two incidents. When the entries do not settle it, keep two rows and write "may be the same incident as the row above".

A follow-up - a notice of resolution, a regulator's statement, a post-mortem - is a source on the incident's row, not a new incident.

## How a date is known

Each timeline entry carries the answer in `atBasis`. "Dates" in `LMTY.md` defines the values, and the output says which in plain words.

| Kind | The record says | Write |
| --- | --- | --- |
| The event's own date | `occurred`, on an entry that is not a page reading | "on [date]" |
| A report's date | `published` | "reported on [date]" |
| First seen | `observed`, or a statement that reports what a page now lists, whatever its basis | "first seen on [date]" for a certification or a page; "seen on [date]" otherwise |
| No longer listed | A statement that reports a page no longer listing a name, whatever its basis | "no longer listed on [page] as of [date]" |

The basis comes from the field, never from a source's own date. Whether an entry is a page reading comes from what its statement reports, not from the kind it is filed under. A profile read for the first time recently has many entries seen on one day: that is the day it was read, not a day on which anything changed.

So nothing the record first saw is "added" or "new", and a page that stopped listing a name is not a certificate that ended. Its date is the day LMTY first read the page without the name.

The page is the entry's source. A statement can end "on its trust page" whatever page was read, so take the page from the source's title or address: "no longer listed on Northwind's data-processing addendum as of 2025-04-11", when that is the source.

A certification fact is not a timeline entry and carries its own dates: first seen, last seen, and an end when its pages stopped listing it. The two can disagree: a fact with no end, last seen on one page, and a timeline entry saying another page no longer lists the name. The checklist gives both, each with its page and date, says they disagree, and leaves the question for the vendor.

The two can also be about one page: first seen there, read without the name, then seen again. A fact last seen after the entry's date, on the entry's own source, means the name came back. That is one row, "listed again as of 2025-05-02; first seen 2025-04-05, read without it on 2025-04-11", and not a disagreement between sources.

## A yes-or-no question

"Are they SOC 2 compliant, yes or no?"

> The record cannot answer that. Compliance is shown by the report itself, with its date, period, scope and auditor, and LMTY's record holds a claim and its source. What the record holds: Northwind states SOC 2 Type II on its security page (official, last seen 2025-05-02). The report to ask for is first in the list below.

"Have they been breached?"

> The record cannot answer that. It holds what was published, and an incident nobody published is on no record. What the record holds: one incident, reported on 2025-03-04 by three outlets, in the 50 of 212 timeline entries read.

With nothing on record, the second part is the short form's sentence.

## What to ask the vendor for

At most six, chosen by what is on the checklist.

| On the checklist | Ask for |
| --- | --- |
| Any claim | The report or certificate itself, under NDA where needed |
| Any claim | Its issue date and the period it covers |
| Any claim, when one product is being bought | Its scope: which products, systems and locations it covers |
| A report whose period may have ended | A bridge letter covering the time since |
| An incident on record | The post-mortem, and what changed afterward |
| A certification no longer listed | Its current status, and the current certificate if it is still held |
| Only an unverified mention | Whether the vendor states it at all |
| Nothing on record | Which reports and certificates the vendor holds, and each one's date and scope |

Name the row each item belongs to. Write things to ask for, not instructions and not conclusions.

## Length

A checklist fits on one page. The caps are 15 claims, 10 incidents, 8 changes and 6 things to ask for. A vendor with nothing on record gets about five lines.
