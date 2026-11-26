# Portfolio Brief Methodology

## What a scan of a list can say

A scan reads a little of many profiles. It can say that a company's record holds a dated entry of a given kind, who states it and when. It cannot say how the company is doing: a public record holds what was published, and most of what decides a company's health is not.

So the brief has one job, to say where to look, and three things it never does: rank the companies, score them, or tell the reader what to do with a holding.

## The reading budget

The brief is built from each company's calendar, so the calendar is read for every company found. Nothing an overview counts says how full a calendar is: a company's timeline can be empty while its calendar, which also holds its products' entries, is long. So no count chooses which companies to read.

The base is two or three calls for each name: the search, and the calendar in one call or two. The first 30 names in the user's order are read; any beyond are named as not read, and a second run can take them. When the user says which companies matter most, those come first.

| The list holds | Searches | Calendar calls | Base | Grade reads | Base and grade reads |
| --- | --- | --- | --- | --- | --- |
| 5 | 5 | 5 to 10 | 10 to 15 | up to 10 | up to 25 |
| 15 | 15 | 15 to 30 | 30 to 45 | up to 16 | up to 61 |
| 40 | 30 | 30 to 60 | 60 to 90 | up to 16 | up to 106 |

A short calendar takes one call and a longer one two, so most lists sit near the low end. Two things add a call, each only when its condition holds:

| When | Costs |
| --- | --- |
| A name finds nothing | One more search, under its other obvious name |
| The search returned a company and a product under one name, or names that differ only by a suffix | The product's calendar: one call or two |

A grade read is for a company to be shown under "Merits attention", at most eight: one page of 50 entries from the timeline of the profile its entry is about, and one search before it when that profile is not one already found.

## Reading a calendar

A calendar lists the last 90 days earliest first, then what is announced as coming. What happened lately is at the end, so the calendar is read from the end.

- the first call asks for a small `limit`, such as 10 entries. It exists to learn the `total`. When it returned everything, the calendar is read whole
- when it did not, the second call asks for the 30 entries before `total`: the newest entries, as one unbroken run back to a date. A third call is made only when that answer was cut and `more` is not zero, as `references/LMTY.md` says of the calendar
- when that run is not the whole calendar, the coverage says so: "the newest 50 of 167 calendar entries for Northwind, back to 2025-04-28". The company is placed by what was read, with those words beside its name
- the first call's entries are the oldest in the window. They are never presented as coverage of the period, and nothing is said of the entries between

A company's calendar holds its products' entries as well as its own, and each entry's `companies` names the profile it is about. Say which profile an entry came from when it is not the company. So no product is looked up for a company whose calendar is empty: only a product the search returned under the same name, or a name that differs only by a suffix such as ".ai", "Inc" or "Labs", is read beside it, and the answer names both profiles.

## The criterion

The criterion is what turns an entry into a flag, and the reader must be able to see it.

| The user says | The criterion |
| --- | --- |
| Nothing | The default: funding, an acquisition or a sale, a leadership arrival, a price or plan change, a product launch or an end of life, a legal action, or a security incident, dated, in the last 90 days |
| "Leadership changes and funding only" | Those two, dated, in the window. A name a leadership page no longer lists is a page change, not a leadership change: it is listed apart unless the user says to count it |
| "Anything since the board meeting on March 3" | Any dated development after 2025-03-03 |
| "Hiring slowdowns" | Not testable from these reads: open roles are in a part of the record this brief does not read. Say so, name `company-hiring-signals`, and apply the default |
| "Which is in trouble?" | Not a criterion. Say the record cannot say, and apply the default |

**Releases.** A company with a changelog can hold dozens of version releases in 90 days. A routine version release does not flag a company under the default: give a company's releases as a count in one clause, "37 version releases in the window". The launch of a new product, or a release the entry itself calls major, does flag it.

Apply the criterion to what an entry's title and description say. A kind is a filing label: an entry filed as a security incident can be a notice of degraded service, which does not flag a company, and a sale of assets can be filed as an acquisition, which does.

A criterion is always about entries: what they say, their date, who states them. It is never about the company's condition.

## How a date is known

Each calendar entry carries the answer in `startsAtBasis`. "Dates" in `LMTY.md` defines the values, and says what a page reading is.

| Group | The record says | Counts as a development |
| --- | --- | --- |
| Dated by when it happened | `occurred` | Yes: "on [date]" |
| Dated by a report | `published` | Yes: "reported on [date]" |
| First seen | `observed`, or an entry that reports what a page now lists or now says, whatever its basis | No: "now lists" or "now reads", "seen on [date]" |
| No longer listed | An entry that reports a page no longer listing a name, whatever its basis | No: "no longer listed on [whose page] as of [date]" |

The basis comes from the field. Whether an entry is a page reading comes from what it reports, not from the kind it is filed under: a listing on a directory, a changed tagline and a name gone from a customers page are all LMTY's reading of a page. The date is the entry's own. A source's date is never put in its place, and a date that an entry's description states for the event is quoted as the entry's words beside the entry's date: "reported on 2025-05-19; the entry says the agreement was signed on May 16".

An upcoming entry has no basis: its date is the one announced, and it is not a development in the window.

A report's date is not the event's. A story can be reported inside the window and first reported before it, on a timeline this brief does not read. So every report-dated entry is worded "reported on [date]", and the brief says once that a flagged story may be older than the window.

Several entries about one event are one development, with the strongest basis among them and the earliest date of that basis. Ten entries about one sale are one development, and the block says ten entries are behind it.

A profile first read last week is all first-seen entries dated last week. A funding round first seen then may be three years old. That is why a first-seen entry never flags a company.

## Pages that no longer list a name

An entry can say that a leadership page no longer lists a person, or a customers page a company. Its date is the day LMTY first read the page without the name. It is not the day anyone left.

- one line for the whole list, apart from the developments: "No longer listed: 8 names on Northwind's leadership page, as of 2025-05-02"
- several names off one page at one moment are one item with a count, never that many departures
- when the page is another company's, say whose: "Initech's customers page no longer lists Globex, as of 2025-05-04". Globex did nothing on that date
- a company whose only entries are these is under "Nothing dated on record", with "page changes only"
- under the user's own criterion they may flag a company. The wording stays "no longer listed as of"

## Grade and sources

A calendar entry carries neither. They are on the timeline of the profile the entry is about.

| The entry's `companies` names | Read |
| --- | --- |
| The company | The company's timeline, one page of 50 entries |
| A product the search already returned | That product's timeline, one page of 50 entries |
| Another profile | A search for the name `companies` gives, then that profile's timeline. The `offers` relation in an overview often does not show the product |

When the entry is on no timeline page read, the Evidence line says "grade not read" and gives the calendar entry's own address. Never give a grade that was not read.

Go by the grade the record gives. An entry graded chatter stays unverified when its one source is a page the source list tiers official: the grade is LMTY's reading of the entry, and it does not flag a company alone.

## Writing a company's block

> **Northwind** - from the calendar of its product, Northwind Cloud
>
> - Development: Northwind agreed to sell its reporting product to Initech, reported on 2025-05-02 by two outlets and stated by Initech. Ten calendar entries are about this sale.
> - Evidence: reported, dated by a report, a trade outlet's article.
> - Why it merits attention: a sale reported on 2025-05-02, inside the last 90 days; the default criterion.
> - Follow-up question: Which assets and which staff does the sale cover, and has Northwind stated the terms?

The same block, done wrong:

| Do not write | Because |
| --- | --- |
| "Northwind is winding down." | A judgment, from one entry |
| "Why it merits attention: asset sales often precede a shutdown." | A forecast and a motive |
| "Follow-up: consider whether to keep the board seat." | Advice on the holding |
| "Northwind recently raised a Series B." (first seen last week) | A first-seen entry given as a development |
| "Northwind's CEO left on May 2." (a leadership page no longer lists the name) | A page change turned into an event |
| "Globex lost Initech as a customer." (Initech's page no longer lists Globex) | Another company's page, read backwards |
| "Northwind had a security incident." (a notice of degraded service) | The kind read, not the entry |
| "Initech: no news, stable." | An absence read as a fact about the company |

## Follow-up questions

A good question asks for what the entry leaves unstated.

| The entry | A question |
| --- | --- |
| A funding round, reported | What were the amount and the lead, and has the company stated either? |
| An acquisition or a sale | What does it cover, and on what terms? |
| A leadership arrival | Who held the role before, and from what date does the change take effect? |
| A price change | Which plans and which customers does it apply to, and from when? |
| A product launch, stated by the company | Is it generally available, and to which plans? |
| A security incident, reported | What was affected, and has the company published a post-mortem? |

One per company. No question that presumes its answer ("why is growth slowing?"), and none that is advice with a question mark.

## Names

| What the search returns | Do |
| --- | --- |
| One clear profile | Read it |
| Several profiles the name does not settle | "Could not confirm": list them with type and website, and ask which |
| The same profile for two names on the list | Read once, show both names, ask the user to confirm they are one company |
| Different profiles for two names that look like one company | Two entries, and the question |
| A company and a product under one name, or names that differ only by a suffix such as ".ai", "Inc" or "Labs" | Read the company's calendar and the product's, name both profiles, and say which one each entry came from |
| Nothing under the name given, a profile under its other obvious name | Read it, and show both: "Northwind Labs (found as Northwind)" |
| Nothing, after one retry | "Not found on LMTY". It says nothing about the company |

Never pick the likeliest namesake, and never merge two names because they look alike.

## A fund's holdings

"What are Initech Ventures' holdings?" asks the record for something it holds only in part. The ties LMTY has recorded around an investor are those a source happened to publish, and a list built from them would present a few known ties as the portfolio.

So the skill does not look them up. It says so in one or two sentences, asks for the list, and names `company-relationship-map` for a reader who wants the recorded ties as ties.

## Every company accounted for

Before writing, count the places: merits attention, dated entries that did not meet the criterion, nothing dated, not read, could not confirm. The five counts add up to the number of names given. A name that appears nowhere is the error this step prevents.

The coverage line counts the reads the same way: read in full, read in part, not read, not found or not confirmed.

## The short form

A list of three, nothing dated:

> Of 3 companies given, 3 were read in full on 2025-05-20; window: the last 90 days.
> Criterion: the default - funding, an acquisition or a sale, a leadership arrival, a price or plan change, a product launch or an end of life, a legal action, or a security incident, dated, in the last 90 days.
>
> No company read has a dated entry on LMTY's record that meets the criterion.
>
> **Nothing dated on record:** Northwind (first-seen entries only), Initech (page changes only), Globex (no entry in the window).
>
> **No longer listed:** Globex's customers page no longer lists Initech, as of 2025-05-04.

That is the whole brief.

## Repeat runs

A repeat run leads with entries dated after the earlier run, matched by the entry's own address, or by its title and date. An entry the earlier run reported is not reported again unless it changed. With no earlier run to compare with, say so in one line: this run is the baseline.

An entry first seen since the last run is still first seen. It is not new because it is new to the record.

## Length

At most eight company blocks of four lines each, and one line for each of the other sections. A brief on 40 companies is still one page.
