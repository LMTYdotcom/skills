# Social Listening Brief Methodology

## Counts first, posts second

LMTY counts every relevant post in a period. A read reaches a few pages of them, newest first. So the two answer different questions:

| | Answers | Covers |
| --- | --- | --- |
| The counts | How much, where, on which days, of which kind | Every matching post in the period |
| The posts read | What that looks like, and who is writing | The newest pages only |

A theme therefore starts from a count. The posts read can describe it, above a floor, and illustrate it. A theme that exists only in the posts read is three people's opinion with a heading.

## The 18 calls, signed in

| Order | Calls | For |
| --- | --- | --- |
| 1 | 1 | Which product the connection reads |
| 2 | 1 | The tracked competitors |
| 3 | 1 | The phrase list |
| 4 | 1 | The counts for the product |
| 5 | Up to 5 | The counts for each competitor |
| 6 | 1 | The dated events in the period, narrowed by kind |
| 7 | 2, held back | The public profile of the product most questions are about: one search, one read |
| 8 | The rest | Pages of posts |

With five competitors counted, six calls are left for pages: the first page of each of five kinds, and a second page for the largest. With three competitors, eight. With one or none, two pages of each kind, which is the most any kind gets.

Spend pages in this order: the first page of every kind chosen, largest first; then second pages, largest first. When the section on questions will not be written, because too few questions were read, the two calls held back go to pages. They are kept whatever the count when the user asked for the questions. A second product's profile takes two more calls, and gets them only when the pages have left them.

What the 18 reach, with five competitors counted: the period's counts for everything collected and for five competitors; 20 events of the kinds chosen; six pages of posts, which on a busy account are the newest day or two of the period; and one product's profile for the questions.

Negative user feedback has no figure of its own in the product's counts, which split by kind and by sentiment separately. Take its total from one more count narrowed to that kind when a call is left. Otherwise write "N read, total not known".

## The 8 calls, free

| Order | Calls | For |
| --- | --- | --- |
| 1 | 1 per product, up to 3 | The search for each product named |
| 2 | 1 per product | Its public posts with their counts |
| 3 | 1 | The dated events of the product the user named first |
| 4 | What is left | With three products, one call: a second product's events. With fewer, further pages of the named product's posts, then the other product's events |

Posts and events are asked for apart. Asked for together, the answer for a large product holds the posts and names the events as left unread, and the next call has to ask again.

So eight calls cover three products: the one named and two competitors. A fourth is "not read in this form". One product alone can be read to the end of the posts shown, with its events. Three products get one page of posts each: say "read the first 25 of the 100 shown" for each, and "events not read" for the product whose events were not asked for.

## The period

- default: from 00:00 UTC seven days back to the time of the read. That is seven whole days and one part day
- the part day is a count with its hours: "9 hours on the day of the read: 41 posts". It is in the total and in no average, and it is never the busiest day
- a per-day figure, if one is given at all, comes from the whole days of the daily series. Do not divide by the number of days the counts give for the period: it is rounded up
- a day missing from the daily series had no counted posts
- a whole day far below the others, under a quarter of the median of the period's whole days, is given as its count with one clause: "the record cannot tell a gap in collection from a quiet day". A pause in listening leaves no mark, so the count cannot say which it was. Never "drop", "dip" or "outage", and no reason
- the period never begins before social listening began. When it would: "the period begins on 2025-03-10, when social listening began, not on 2025-03-07". Never "monitored since": the date is when posts began to be collected, and LMTY's other record of the product can be much older
- more than 90 days back cannot be read

## A phrase added or removed in the period

It goes before any count, because it changes what the count means.

| What happened | Write, above the volume table |
| --- | --- |
| A phrase added on day 4 | "'Northwind Relay' was added on 2025-03-11. Posts before that day were not collected for it, so Northwind's count is not a full one for the first three days" |
| A phrase removed on day 2 | "'Initech Flow' was removed on 2025-03-09. The posts it matched are kept and still counted, so Initech's count covers two kinds of day" |
| A phrase paused | "'Northwind' is paused. The record does not say since when" |
| A tracked competitor has no active phrase: its phrases were removed before the period | "Initech's phrases were removed on 2025-02-13. LMTY has collected nothing for it since". Its row reads "no posts collected in the period", which is not nobody posting |
| None | "No phrase was added or removed in the period" |

A competitor whose only phrase was added inside the period has no full count at all. Give its row with that said.

## When no phrase is the product's own

An account can monitor its competitors' names and no phrase for its own product. The product can even be a category, with no name of its own to monitor. Then nothing is collected about the product itself, and "what people say about us" has no answer in this account.

- say so in the brief's first lines, before any count: "LMTY monitors no phrase for Acme itself. This brief covers its 12 tracked competitors and its field: nothing in it is about Acme"
- the first row of the volume table is "everything collected", never the product
- under "Needs attention", the items that name the home product do not apply
- name `social-keyword-check` under "Next": it shows which names have no phrase

## Which subject a post matched

A post carries the phrases it matched. The phrase list says whose each phrase is.

| The matched phrase is | The post is counted under |
| --- | --- |
| One of the product's own | The home product. With no such phrase, no post is counted under it |
| A competitor's | That competitor |
| A field term | The category |
| Several | Each of them. Say once that rows overlap |
| A competitor's whose rival is not tracked now | "A rival not tracked now", named by the phrase |

Matching a phrase is not being about its subject. Read the excerpt:

- about the subject: kept
- names it in passing, in a list or a comparison: kept, and not used as an excerpt for a theme about that subject
- about something else that shares the word: "matched, about something else". Counted, dropped, and worth a line under "Needs attention" when one phrase accounts for many

## Which kinds to read

Five kinds, by LMTY's tags: leaving, looking to buy, product questions, negative user feedback, bug reports. Read them in order of their count in the product's split by tag. A kind with no posts is not read, and is named under "Not observed, and not read".

Why these five: they are the kinds where one post can call for an answer. Praise, announcements, hiring and funding are counted in the splits and not read here.

A read by kind leans toward what the tag selects. Pages of posts tagged as leaving find people leaving. Say so once.

Say "read N of M" for each kind, and the days its pages covered:

> Leaving: read 74 of 140, covering 2025-03-11 to 2025-03-14. Bug reports: read 50 of 612, covering the last 31 hours.

The second line is the usual case for a busy kind: two pages are a day and a half. The brief then describes those hours and says so. It does not describe the week from them.

## Themes

A theme has four parts:

1. **The count,** and what it is a count of: "140 posts tagged as leaving in the period, 61 of them in Northwind's count".
2. **What the posts say,** only above the floor of 20 posts read from 10 authors, only as numbers from the posts read, and with the span their pages covered in the same sentence: "of the 74 read, posted from 2025-03-11 to 2025-03-14, 41 name the price and 12 name the removed plan". The floor is a count of posts, and one morning can meet it. So the sentence carries its hours: "of the 50 read, all from the 9 hours before the read, 31 report the same error" describes a morning, and the brief does not say the week looked like it.
3. **Two excerpts,** each with its link, at most 200 characters, cut marked "[cut]". Pick two that differ: not two replies in one thread.
4. **Who is writing,** from the posts read: "58 authors: 49 unknown affiliation, 6 independent, 3 vendors".

What can be a theme:

| A count of | Example |
| --- | --- |
| A kind of post | "612 bug reports" |
| A kind for one subject | "61 posts about leaving in Northwind's count" |
| A sentiment | "1,140 of the 2,900 posts are marked negative" |
| A platform | "1,900 of the 2,900 posts are on one platform" |

What cannot: an impression from the posts read with no count behind it; a comparison with last week; a share of customers.

Order themes by their count. At most five. When fewer than five kinds have posts, there are fewer themes.

**One thread.** When the links or titles show that more than half of the posts read for a theme sit in one thread, say so and give the number without it: "38 of the 74 read are replies in one thread; without it, 36 from 31 authors". A thread is one conversation.

**No percentage on fewer than 20 posts.** Above that, a percentage may follow the two numbers, never replace them.

## Events and days

### Which events are read

The feed of a busy market holds hundreds of events a week. Read whole, its first page is routine version releases and one account's security notices, and the posts reference says why the mark of significance does not choose among them. So the one call is narrowed by kind.

The posts reference lists the kinds by what they are about. This brief asks for ten: the price change; the product launch and the product deprecated; the security incident; funding and the acquisition announced; the partnership announced; the legal action; the company shut down and the company renamed. Each is something a company did or had happen to it, which people post about, and none is a reading of a page. The last three are there because an end of life and a rename are what a reader most needs to know of a product people are posting about. A kind is a filing label: a product's end of life can be filed as a company shut down, so word the row from the statement.

The rest are left out, for three reasons:

- routine releases crowd out everything else on a page of twenty
- every kind that reports what a page lists, no longer lists or now says is LMTY's reading of a page, and can stand beside no day's posts
- hiring, leadership, earnings and a stock listing are news of the company more than of what people post about its product: `competitive-market-briefing` carries them

A user who asks for one of these gets it in a call of its own, worded as the next table says.

Say what was read as the posts reference words it, with the span the entries cover, and "more not read" whenever the answer says more are left: "20 events read of a feed not counted, from 15:40 on 2025-03-14 back to 08:10 on 2025-03-13; more not read". Twenty events of a busy market are a day or two, not the period: the span says so. Never write "the week's events".

### Which may stand beside a day's posts

| The entry | In the brief |
| --- | --- |
| A reading of a page: it reports what a page no longer lists, now lists or now says | Worded as `references/LMTY.md` says under "Dates": "Northwind's customer page no longer lists Globex as of 2025-03-12." Never beside a day's posts |
| Any other entry, dated by the event's own date | "On 2025-03-12, the day Northwind's new plans took effect, 48 posts were in Northwind's count. The other six whole days had 9, 11, 12, 14, 15 and 17" |
| Any other entry, dated by when a source published it | "Reported on 2025-03-12 by [source]. The event's own date is not on the record, so no day is set beside it" |
| Any other entry, dated by when LMTY first saw it | "First seen by LMTY on 2025-03-12. No date of its own" |

The first row is checked first: on an older server such an entry can carry the basis of an event with a date of its own, and it is a page reading all the same.

**When no event read carries a date of its own,** which is the usual case, the section is one line and a list. The line: "None of the 20 events read carries a date of its own, so no day's count is set beside any." The list: up to five events, each with its date worded as reported or first seen. Nothing emptier: the events are still listed. Nothing fuller: no columns of "not set", no counts of the period's days, and no sentence about what was posted around them.

### Which are shown

At most five. Events about a competitor in the volume table come first, then the others, newest first within each. Several reports of one incident are one event: list it once, with its earliest date and how many reports there are. One account's notices published in the same minute are one row.

The sentence gives the numbers and stops. It does not say the day was high, and it does not say why. Seven days are too few to call any day unusual, and the same day can hold a launch, an outage and one long thread.

## Needs attention

Five items at most. The list is a judgment, and the brief says so. The rule, in order:

| What was seen | Why it is listed | Where it goes next |
| --- | --- | --- |
| Posts about leaving, or a fault, that name the home product | Someone may be owed an answer | The owner of the product area; the posts are linked |
| A question about the home product that the record does not answer | The public record cannot answer it for the next person either | Whoever owns that page; `company-profile-check` |
| A claim about the home product repeated in several posts | It is being repeated, true or not | `company-claim-check` |
| An event at a competitor with a date of its own and posts on the same days | The reaction can be read before and after | `social-competitor-change-impact` |
| A phrase most of whose posts read were about something else | The counts above include its noise | `social-keyword-check` |
| Praise of the home product, counted and not read | Leads someone could follow up | `social-quote-finder` |

Each item is one line: what, the number behind it, where next. No instruction, no deadline, no forecast.

The first three rows are about the home product. They apply only when a phrase is the product's own. Otherwise nothing was collected about it, and the list is about competitors and wrong matches.

When nothing fits the rule, write "Nothing met the rule for this list" and leave it at that. A brief does not need a list of five to be complete.

## The three sections above the floor

Each needs 20 posts of its kind read, from 10 authors. The posts come from the pages already read: no extra read is made for them.

**A direct request is not held to the floor.** "Any questions about Acme we haven't answered?" asks for the questions, and seven are an answer. List the ones read, say "read 7 of 7 product questions that matched Acme's phrases, posted from 2025-03-08 to 2025-03-14", mark each, and read the one profile the calls allow. Word nothing as a theme: below the floor the questions are listed, not summarized. The same holds for a direct request for the comparisons or the uses.

**Comparisons and switching.** From posts about leaving and buying. Which products are named in one post, counted by pair. Direction only where the post states it, as "says they moved from A to B" or "says they are looking at B". A product named in a reply is somebody's suggestion.

**How people say they use it.** Uses stated in the posts, in the authors' words, counted. Not a segment, not a persona: a list of what people said they do with it.

**Questions people ask.** At most five, the most repeated first. For each, look for the answer on the public profile of the product the question is about. That is usually a competitor's: a question in Northwind's count is about Northwind, and the home product's profile does not answer it.

Two calls are held for this: a search and one read, of the section the questions point to, for the product most of the questions are about. A second product gets two more only when the pages have left them. A dated event already read about the product can answer as well, worded as its date allows.

| The record holds | Write |
| --- | --- |
| A fact that answers it | "Answered on the record: [the fact], [grade], as of [date], per [source]" |
| A fact that half answers it | "Partly on the record: [the fact]. Not on the record: [what is missing]" |
| Nothing | "Not on the record" |
| Only the written summary mentions it | "Not on the record". The summary is LMTY's writing, not a fact |
| The question is about a product whose profile was not read | "Not looked up: [product]'s profile was not read in this conversation" |

Nothing here is answered from memory. "Not on the record" does not mean the company has no answer. It means LMTY's sources do not hold one.

## The free form

What a public profile gives: how many posts LMTY collected about the product in the last 30 days, from how many authors, by platform and by day, when LMTY began collecting posts for it, and at most the 100 most engaged posts, with no tags and no sentiment.

| The product | The read |
| --- | --- |
| Large: thousands of posts collected | The 100 shown are a sliver, and the most engaged: announcements, large accounts, arguments. Give the counts, ten posts, and say what the ten are. A theme "among the 100 most engaged posts" only above the floor |
| Small: a few dozen collected | The posts shown may be all of them: say "all 37". The floor is rarely met: list, do not summarize |
| No count at all, or a count of zero | Two different rows, each worded as the posts reference gives it. The second: "LMTY collected no posts for Acme in the last 30 days. LMTY began collecting posts for it on 2024-11-02; the record does not say it continues." A profile cannot show that its phrases were removed. Signed in, the phrase list says whether they were, and when |
| No profile | "No public profile on LMTY", and where LMTY can be asked to research it, once |

The ten posts: sort authors into groups first, then take the most engaged from each group, the independent posters and unknown affiliation first. Give likes and comments as the post carries them. They show reach, not agreement.

Events come from a profile's dated events, read in a call of their own, at most three per product. A profile's events cannot be narrowed by kind: read the first page and pick the kinds this brief asks for, by what each statement reports. Word each as that section says. A product whose events were not read says "events not read", never "none".

The free form compares nothing between products beyond the row each one gets. Two products' counts rest on different phrases collected since different days.

## Repeat runs

The earlier run is the one in the destination the brief goes to: the channel, the document, the conversation. With none to hand, say so and call this run the baseline.

What differs is said in terms of what was reported:

- a theme present now and not then, or gone
- an item under "Needs attention" that is new, still open, or gone
- an event that was not on the record at the last run
- a phrase added or removed since

Volume is the hard one. Two weekly counts invite "up 30%". Before any such word, run the four checks under "Before comparing two periods" in the posts reference and say what each found. If all four hold, give the two counts and the difference. If any fails, give the two counts side by side, say which check failed, and call nothing a rise or a fall.

## In a channel

When the brief goes to a chat channel: the three lines of "In short", the items under "Needs attention", and where the full brief is. Nothing else. The tables do not survive a chat message, and nobody reads them there.

## What not to write

| Do not write | Because | Write |
| --- | --- | --- |
| "Sentiment is down this week." | One period, and a sentiment mark is LMTY's reading | "1,140 of the 2,900 posts are marked negative." |
| "Customers are frustrated with the new limits." | Posts are not customers, and three posts are not a mood | "12 posts read report hitting the new limit." |
| "Mentions spiked after the announcement." | A spike needs a baseline, and after is not because | "On 2025-03-12, the day of the announcement, 48 posts. The other whole days: 9 to 17." |
| "People are switching to Northwind." | Stated intent, counted | "7 posts say the author moved or is moving to Northwind." |
| "A quiet week." | One period | "212 posts in the period." |
| "Mentions dropped on Thursday." | Nothing marks a gap in collection | "Thursday: 12 posts. The other whole days: 180 to 240. The record cannot tell a gap in collection from a quiet day." |
| "Northwind lost Globex as a customer on 2025-03-12." | A page reading, not an event | "Northwind's customer page no longer lists Globex as of 2025-03-12." |
| "People are frustrated with Acme this week." (no phrase is Acme's own) | Nothing was collected about Acme | "LMTY monitors no phrase for Acme itself." |
| "Acme supports single sign-on." (from memory) | Not read from the record | "Answered on the record: single sign-on is listed on the Business plan (official, as of 2025-02-20)." |
| "The top theme is pricing." (from six posts) | A theme needs a count | "6 posts read name the price. Floor not met: they are listed below." |

## Length

One page. Outside the tables, under 500 words. Five themes, five items, five questions, five events; three products and ten posts in the free form.

Short forms:

- a quiet period, where no kind of post reaches 20 read from 10 authors: the coverage line, the volume table, the posts read under one heading, and "nothing met the floor"
- nothing collected in the period: the coverage line and one sentence, "no posts were collected for [product] in the period, which is not the same as nobody posting"
- a repeat run with nothing different: "nothing differs from the run of [date]" and the volume table
