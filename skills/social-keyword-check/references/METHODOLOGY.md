# Keyword Check Methodology

## What the list decides

LMTY collects a post only when it matches a monitored phrase. So the phrase list decides two things that no later read can undo: what is never collected, and what is collected by accident. This check looks for both.

| Fault | What it does | Where this check finds it |
| --- | --- | --- |
| A name with no phrase | Posts under that name are not collected. The silence looks like nobody talking | The public record, set against the list |
| A phrase that is a common word | Posts about something else are collected and counted | The posts the phrase matched, read |
| A phrase nobody tends | A rival dropped from the tracked set, a competitor added with no phrase, a phrase paused and forgotten | The list itself |

## The 35 calls

The ceiling is 35 calls. Spend them in this order, and stop when they are gone.

| Order | Calls | For |
| --- | --- | --- |
| 1 | 1 | Which products the connection reads |
| 2 | 1 | The tracked competitors. Each comes with its website |
| 3 | 1 | The phrase list |
| 4 | 2 | The counts, for 90 days and for 30 |
| 5 | Up to 3, held back | One page of posts for each phrase sampled in Step 7 |
| 6 | Up to 27 | Public profiles: three reads a subject, and a fourth where a graded tie names its maker |

Five calls are fixed, three are held for sampling, and 27 are for profiles. They are nine subjects at three reads or six at four: the home product and five to eight competitors. A call that something else left goes to the next subject in order: a phrase not sampled, or a subject with no profile, which costs its one search.

Read each subject in full before starting the next. Half a read of six subjects finds the handles of all six and the product line of none. When the calls end before a subject's fourth read, say "[maker]'s products not read".

The order of subjects:

1. one the request names
2. the home product
3. on a repeat run, the tracked competitors the earlier run did not reach, in the tracked set's order
4. the other tracked competitors, in the order the tracked set gives them, a higher tier first when it carries tiers
5. a rival with phrases that is not in the tracked set

The order is not by posts matched. That order is the same every month, so the same few would be read on every run and the rest never. An earlier run is one whose coverage line is to hand, as "Repeat runs" in `references/QUALITY.md` describes: with none, start from the top of the tracked set.

Say what the calls reached, in the coverage line, by name: "read 3 subjects of 6 against the public record: Acme, and Northwind and Initech of 5 tracked competitors". Name the ones not reached. The names are what lets the next run begin where this one stopped.

### What each read returns

| Read | Returns | Does not return |
| --- | --- | --- |
| The search by name | Each profile under that name, with its type, its name and its website. A short name returns unrelated profiles too | Who makes a product. A company in the results is not its maker for sharing the name |
| The subject's overview, with its facts narrowed to former names, in one call | The website. The accounts listed, each with its platform, handle and whose the record says it is. Each former name with its grade, first seen and last seen. A count of the profile's ties by kind. A short list of relations | A maker to rely on: the relations are at most a dozen ties with no grade and no date, and can name a namesake. The products offered. The brands acquired |
| The subject's own connections, narrowed to who offers what and to acquisitions, in one call | Each tie with which way it points, its grade, a stated start when there is one, first seen and last seen. For a product: the company that offers it, where the tie points in, and the brands it acquired. For a company: every product it offers and every brand it acquired | Former names, which are facts |
| The maker's connections, narrowed the same way | Every product the maker offers and every brand it acquired, with the same fields | - |

An answer can leave out a section it had no room for, and names it: ask for that section in the next call, and count the call.

Three things follow from the table:

- **Product names with a grade and a date come from a read of ties,** not from an overview. An overview's relations show a few of a maker's products, never the whole line
- **Former names always need the facts,** because an overview only counts them. Asking for them with the overview costs no extra call
- **Read the subject before its maker.** A rename is recorded on the product, and an acquisition can be recorded on either. A maker's profile can be nearly empty where the product's is full

A read that was not made is said as counted and not read: "the overview counts 2 acquisitions: not read".

### The maker

The maker of a product is whatever company the product's own ties say offers it, and the tie has a grade. Nothing else names a maker: the record can list a namesake company among a product's relations, and a search for a short name returns companies that have nothing to do with it.

| The product's own ties say | Do |
| --- | --- |
| A company offers it, on a tie graded above chatter | That company is the maker. Make the fourth read, and give the tie's grade and date with anything taken from it |
| A company offers it, on a tie graded chatter | Give the tie as it is: "the record ties Relay to Initech as its maker, graded chatter, seen on 2024-11-20: not read as its maker". No fourth read, and no phrase from that company's products |
| No company offers it | "No maker on LMTY's record for Relay". No fourth read, whatever the search or the relations show |
| Two companies offer it | Give both with their grades. Read the one graded above chatter when only one is. Otherwise read neither |

A company that the product is a subsidiary of, or was spun out of, is not its maker by that tie. Give it as the record words it, and offer no phrase from it.

### A subject that is a company

A tracked competitor can be a company with several products: the search returns a company under exactly its name, and products under longer names. Read the company in both places: its overview with its former names, then its own ties, where the products it offers point out from it. That is three reads, and there is no maker to look for.

Each product is a row worded "a product Northwind offers", with the tie's grade and date. A product whose name contains a phrase already monitored is "likely covered", like any longer name. The products' own profiles are not read: say so under "Not checked".

### The home product

An account's product is a name and nothing else: the connection gives it no website. It can be a product with a profile, or a category with none.

| The search for its name returns | Do |
| --- | --- |
| A product or company with exactly that name | Take it as the home product, and say in the coverage line which profile was used |
| Only a longer name that contains it, or a different one | Not the home product. "No public profile found for [product] by name: its own names were not checked" |
| Nothing | The same line. Pass on, once, where LMTY can be asked to research it |

When no phrase is the product's own and no profile carries its name, say that as well: nothing is collected under the product's own name, and the check covers its competitors.

## What a phrase could cover

| Thing | The read that holds it | Comes with | The phrase to offer |
| --- | --- | --- | --- |
| A product name | The subject's own ties when it is a company. Its maker's ties when it is a product and a graded tie names the maker | The tie's grade, and its date as "seen since" unless a start is stated | The name as the record spells it |
| A former name | The facts narrowed to former names, on the product first and then on the maker | Grade, first seen, last seen, source | The former name |
| A domain | The website on the profile, or the one the tracked set gives for the competitor. Either can be empty | Nothing: write "not given" | The host name, without the scheme or a path |
| An official handle | The accounts the overview lists, where the record says the account is the product's or the company's own | No grade, no date, no source: "not given" | The handle as listed, with its platform named beside it |
| An acquired brand | The connections narrowed to acquisitions, on the maker and on the product, where the tie points out from the subject | Grade, the stated date or "seen since", last seen | The acquired company's name |

Things that are not offered as phrases:

- a name from memory. If the record does not hold a product, this check does not know it exists
- a name taken from an overview's short list of relations with no grade or date behind it
- an account the record gives to a founder, an employee or a community
- a company that acquired the subject: a tie that points in. That is a parent, and its name matches the parent's own news
- anything from the products of a company tied to the subject as its maker only by chatter, or by a shared name
- a leader's name. People are not phrases here
- anything from the profile's written summary. It is LMTY's writing, not a list of names

The record is not complete, and it can be wrong: a product can be tied to the wrong maker, and a former name can also be listed as a rival. Give what the record holds with its grade, and when two entries disagree, give both and offer no phrase from either. Say once that the gaps are the ones the record shows.

## Covered, removed, not covered

| The thing | And the list | Write |
| --- | --- | --- |
| "Northwind Relay" | Holds "Northwind Relay", active or paused | Covered. No row |
| "Northwind Relay" | Holds "Northwind" | "Likely covered by 'Northwind'". No row unless the user asks for every name |
| "Relay" is the product's whole name | Holds nothing like it | A gap, and a common word: the wrong matches to expect are many |
| "Northwind Relay" | Holds it in the removed list | Not a gap. Under what changed: "removed on [date]" |
| "Northwind Relay" | Holds "Northwind Rely" | A gap, and a likely misspelling in the list: give both |

How LMTY matches a phrase inside longer text is not on the record. "Likely covered" is the strongest wording there is for a shorter phrase.

Compare without regard to capitals. Keep the record's spelling in the phrase offered.

## Dates on a gap

A gap row carries the record's date, worded as the record supports:

- a stated start: "since 2023"
- no stated start: "seen since 2024-10-13", the day LMTY first saw it
- always: "last seen" when the record gives it

Many first-seen dates on one day mean that was the day the profile was first read. A product first seen this month has not thereby been launched this month. Never write "new product", "just launched" or "recently renamed" from a first-seen date.

## Counts and age

A count means something only against the days the phrase has been monitored. That is the shorter of two spans: since the phrase was added, and since social listening began.

| The phrase | Write |
| --- | --- |
| Added 3 days ago, no matches | "Too new to judge: 0 posts in the 3 days since it was added" |
| Added 20 days ago, 2 matches | "2 posts in the 20 days since it was added". The 90-day column reads "not yet 90 days" |
| Monitored for the whole 90 days, no matches | "No posts matched in 90 days of monitoring" |
| Monitored for 90 days, 4 in 90 and 0 in 30 | "4 posts in 90 days, none in the last 30". Two counts, not a decline |
| Monitored on one platform where the others are on four | Give the platforms beside the counts. Fewer platforms, fewer matches |
| Social listening began 40 days ago | Every 90-day count covers 40 days. Say so once, above the table: "Social listening began on 2025-02-03, so every 90-day count covers 40 days." Never "the product has been monitored since": a phrase is monitored, and LMTY's other record of the product can be much older |
| Paused | No judgment. It is a loose end |

Fourteen days is the line below which a phrase is "too new to judge". It is the shortest daily series the posts reference lets anything be read from.

What a low count does not show: that nobody uses the name, that the product is unimportant, or that the phrase should go. A phrase can be quiet because its subject is. The row gives the count and the days. The reader decides.

The counts are of relevant posts. Posts LMTY hid as low relevance are not in them, so a phrase that mostly collides with other meanings can show a small count and still be noisy. That is what Step 7 is for.

## Sampling a noisy phrase

Three phrases at most, one page each. Choose by what can be seen before reading:

- the phrase is a common word or a common pair of words
- the phrase is four letters or fewer
- the phrase is a domain made of a common word
- the search for its subject returned another profile under the same name
- its count is several times that of every other phrase for the same subject

Then read:

1. Ask for one page of posts, 50, with the low-relevance posts included. Narrow to the competitor when the phrase is a competitor's. Use the period of the 30-day count.
2. Keep the posts whose matched keywords include the phrase. No read can be narrowed to one phrase, so the page may hold few of them, or none.
3. Read each excerpt. Is the post about the phrase's subject? The excerpt is the opening only: when it does not settle it, count the post as "not clear from the opening".
4. Count, in three numbers: about the subject, about something else, not clear. Add how many LMTY had marked as low relevance.

Say what was read against what exists: "read 14 posts that matched the phrase, from one page of 50; the 30-day count for it is 212 relevant posts". The page holds low-relevance posts and the count does not, so the two are not a fraction of each other. Say that in one clause.

Fewer than 20 posts read is the usual case, so the answer is numbers, never a percentage. With no post for the phrase on the page: "none on the page read: not judged".

Sampling does not wait for the setup to age. When listening is younger than 14 days the counts are left out, and the sample is still read: a phrase can show five relevant posts and a page of hidden ones on its second week.

## Loose ends

| What the list shows | Means | Write |
| --- | --- | --- |
| A competitor's phrase with no competitor attached | The rival it belonged to is not in the tracked set now | "'Initech Flow' is a competitor's phrase with no tracked competitor behind it, linked to Initech. 31 posts in 30 days" |
| A tracked competitor with no phrase carrying it | Nothing is collected under its name | "Initech is tracked and has no phrase" |
| A phrase marked paused | It is not collecting. Since when is not recorded | "'Northwind' is paused. The record does not say since when" |
| A field phrase with no subject | Normal for a category term | No row |

On an older server no phrase carries a competitor at all. Then the first two rows cannot be told apart from a phrase that simply names nobody: say that loose ends could not be checked, and do not guess from the wording of a phrase.

## What changed

The list records two kinds of change: when each phrase began to be monitored, and which phrases were removed in the last 90 days, with when. It records nothing else. A phrase edited, paused or resumed leaves no date.

- repeat run: phrases added since the last run and phrases removed since then. Give the date of the run compared against
- first run: the baseline. Phrases added in the last 30 days, and everything in the removed list

A list is often changed in batches: a setup seeds dozens of phrases in one minute, and someone removes ten suggestions a few minutes later. Ten rows of single phrases would show the newest batch and hide the rest. So a row is a batch: the phrases added, or removed, on the same day with the same kind and the same origin. Give how many, name up to three, and say when one batch followed another within minutes: "10 field terms suggested by AI, removed on 2025-03-02 within minutes of being added: 'invoice matching', 'expense reports', 'spend approval' and 7 more". A phrase changed alone is a row alone.

Three sentences that belong beside any count that spans one of these dates:

- a phrase added on a date collected nothing before it
- a removed phrase's posts are kept and still counted
- so a count that differs across that date differs because collection changed

## Ranking the changes

Seven at most. The order is a judgment, and the answer says so. The rule:

1. A tracked competitor, or the home product, with no phrase at all.
2. A product name in current use with no phrase, the home product's first.
3. A former name, or an acquired brand.
4. A phrase sampled and found mostly about something else.
5. A competitor's phrase with no tracked competitor behind it.
6. A domain or a handle.

A paused phrase is listed as a question ("still meant to be paused?"), below these.

Each change carries the wrong matches it could bring, judged from the phrase:

| The phrase | Say |
| --- | --- |
| A distinctive name of two words or more | "Few wrong matches expected" |
| A single common word | "A common word: expect many posts about something else. A longer form would be narrower" |
| A short name, four letters or fewer | "A short name: expect collisions" |
| A name another profile shares | "LMTY's record holds another [company or product] under this name" |
| A domain | "Matches links as well as mentions, and has matched longer domains that end in it" |

Two kinds of wrong match have shown up in posts read, and are worth saying when the phrase invites them. How LMTY matches in general is not on the record: these are what the posts showed.

- **A domain matched other domains that end in it.** A phrase like "relay.example" brought in posts linking to "great-relay.example" and "my-relay.example", which are other sites
- **A short phrase matched inside other text.** A phrase of a few letters brought in posts where those letters sat inside a longer word or inside the code a platform writes for a character such as "&", in posts about something else

This is a judgment before the fact. Say "expect", say it is judged from the phrase, and promise no number.

Write each change as an option. This skill does not know the plan's limit on phrases, or what the team has already tried.

## The pasted-list form

With no account, the user can paste their phrases and name their competitors. Then:

- read the public profiles as in Step 4, which needs no sign-in
- find the gaps as in Step 5
- leave out counts, sampling, loose ends and changes: none can be read without the account
- head the answer "Gaps only: checked against a list you pasted on [date]"

## What not to write

| Do not write | Because | Write |
| --- | --- | --- |
| "This keyword is dead." | No matches in a period is a count, and the period may be three days | "No posts matched in the 3 days since it was added." |
| "You are missing Northwind's new product." | First seen is not new | "LMTY's record lists Northwind Relay (seen since 2024-09-12). No phrase covers it." |
| "Add 'Northwind Vault', their storage product." | The record does not hold it; that is memory | Nothing. Or: "Not on LMTY's record." |
| "'pilot' is a noisy keyword." | Not read | "'pilot' looks like a common word: not read." |
| "Mentions of Initech dropped in March." | A phrase was removed in March | "Initech's count differs across 2025-03-04, the day 'Initech Flow' was removed: a change in collection." |
| "The keyword was paused two weeks ago." | A pause has no date | "The phrase is paused. The record does not say since when." |
| "You should remove these five keywords." | An instruction, and this skill does not know why they are there | "Option: pause 'pilot'. 11 of the 14 posts read were about something else." |

## Length

The tables carry the check. Outside them, under 400 words.

Short forms:

- nothing to report in a section: leave the section out and name it on the "Nothing to report under" line
- social listening began less than 14 days ago: the list, the gaps, the loose ends and any phrase sampled, with one line in place of the counts
- no gap, no quiet phrase, no loose end: say so in two lines with what was read, and stop. A clean list is a finding
