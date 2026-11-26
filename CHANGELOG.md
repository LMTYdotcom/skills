# Changelog

All notable changes to this pack are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the pack uses [Semantic Versioning](https://semver.org/spec/v2.0.0):
the patch number for wording and fixes, the minor number when a skill is
added or its scope changes, the major number if the plugin is renamed or
a skill is removed.

## [Unreleased]

## [1.1.0] - 2026-11-26

### Added

- A second family of skills. `company-` skills work from LMTY's public
  profiles of companies, products and people, which are free to read and
  need no account, and never need a product of the user's own. Each
  answers one question about one company, or about a list of companies
  the user supplies:
  - `company-briefing`
  - `company-pricing-history`
  - `company-customer-map`
  - `company-hiring-signals`
  - `company-relationship-map`
  - `company-in-their-own-words`
  - `company-event-prep`
  - `company-claim-check`
  - `company-prospect-stack`
  - `company-profile-check`
  - `company-security-claims`
  - `company-post-drafts`
  - `company-portfolio-brief`
- A third family. `social-` skills read what people say in public, from
  the posts LMTY collects for a signed-in product with Social Listening
  on. Two of them, `social-quote-finder` and `social-listening-brief`,
  also have a free form that reads the public posts on a product's
  profile:
  - `social-competitor-change-impact`
  - `social-keyword-check`
  - `social-quote-finder`
  - `social-listening-brief`
- Playbooks: a short form of every `company-` and `social-` skill, and
  of most `competitive-` skills, in `playbooks/`, to paste into any
  assistant that has the LMTY server connected, or to give a scheduled
  task or a bot as its instructions. The deep dive, positioning and
  win/loss analysis have none: they need more of the user's own material
  than a pasted prompt carries. `library.json` holds them all for a page
  that lists the skills.
- `company-briefing` has a short form for "what's new with X?": the
  dated events of the period on one screen, with what LMTY read for the
  first time counted apart and never worded as news.
- Every skill says how often it is worth running, under "Cadence", and
  the shared quality reference says what a repeat run leads with.
- Every skill can now read LMTY's public profiles. A connection without
  an account is no longer treated as LMTY being absent: the skills read
  the profiles of the companies in the request before any web research.
- A playbook can carry `when`, the page's own words on when to run it,
  addressed to the reader. Without it, `library.json` takes the skill's
  Cadence line, as before.

### Changed

- The pack is listed as "LMTY Skills" (in ChatGPT and Codex, "LMTY"),
  with a description that covers all three families. The plugin's name,
  `lmty`, is unchanged, so installs and commands stay as they are.
- The page copy of six playbooks (Portfolio Brief, Company Post Drafts,
  Security Claims, Keyword Check, Social Listening Brief, Quote Finder)
  is rewritten in plain language, and the market briefing and executive
  market brief playbooks stop at once when a tool asks for sign-in.

- The `competitive-` skills are brought up to the standard of the newer
  families. Each says in its first lines how much it read of how
  much, words every date by how it is known (when a thing happened, when
  it was reported, or when LMTY first read it), takes nothing from memory
  when LMTY is connected, and marks anything from the open web where it
  uses it. Each reads a tracked competitor's public profile alongside the
  account, and reads dated events from the market feed. A repeat run
  reads what LMTY recorded since the last one, not only what is dated
  since then.
- A scheduled run that is missing something it needs says so in its
  first line and stops, or does the part that does not depend on it. It
  never guesses a competitor, a product or a release.
- Each `competitive-` skill has a short form for a thin record, so a
  product tracked for a week does not get a full report built on it.
- Requests that sat on a boundary between skills have one owner. A brief on one
  company with no product of the user's own in view is
  `company-briefing`. Checking whether an existing battlecard or deck is
  still accurate is `competitive-asset-audit`; rewriting it after a
  change is `competitive-enablement-refresh`; building a new one is
  `competitive-battlecard`. A post-mortem of one closed deal is
  `competitive-win-loss-analysis`. A briefing, teardown or launch check
  that also asks whether to change the price runs, and names
  `competitive-pricing-packaging-review` for the decision.
- A buyer choosing between vendors is outside the pack, and the skills
  say so in one line.
- `references/LMTY.md` describes three connection states (account,
  public, absent) and the public profile tools: how to find a profile,
  read it a section at a time, and carry each statement's grade, date
  and source into the output.
- A skill that expects public profiles tells the user once how to
  connect LMTY when it is absent, and offers to work from web research
  marked unverified. Every other skill still never raises it.

- The verdicts a claim can be given (supported, the subject's own claim,
  reported, unverified, disputed, out of date, not observed, untestable)
  are in the shared evidence policy. `competitive-objection-response` and
  `competitive-asset-audit` keep their own marks and now say when a claim
  rests only on the party it flatters.
- A skill may deliver to a named destination when a connector for it is
  present. Anything addressed to someone outside the user's organization
  stays a draft for a person to send.

- Every skill opens by naming each file it relies on and says to read
  each to its last line. In real use an assistant read the files the
  steps named and skipped the rest, and some reads stopped partway. The
  shared files are the same in every skill, so a second skill in one
  conversation does not read them twice.
- A user's own preferences can reshape an answer's layout. They do not
  remove a statement's source, date, grade or speaker, or the line that
  says how much was read.
- The count of what was read comes from the calls made, and a section
  about what is missing lists the gaps without reading anything into
  them.
- `company-briefing` and `company-customer-map` state their one page as
  a number that can be checked.
- Public reviews count as customer vocabulary when labeled as
  third-party opinion. With no customer evidence of the company's own,
  the messaging audit and the positioning brief test wording against
  reviews read in the run. A review is never deal evidence, a count or a
  fact about a product.

### Fixed

- `references/LMTY.md` said the change history could not be read past
  its newest 50 entries. It can, a page at a time.
- A `competitive-` skill no longer tells the user how to connect LMTY.
  It works from what it has and says once which state it worked in.
- With nothing connected, nothing supplied and no web search, a skill
  says it has no source and offers once to work from what the user
  pastes.
- `competitive-executive-market-brief` keeps an item that rests on one
  unverified post out of its top three, its risks and its decision
  questions.
- `competitive-market-shift-analysis` no longer lets a vendor's own
  pricing page or post stand in for a signal from outside the vendors,
  and does not read the order of two reports as the order of two moves.
- `competitive-win-loss-analysis` counts a loss reason across
  competitive losses only. A deal where the buyer chose nothing is a
  no-decision and is in neither the win count nor the loss count.
- A product whose record begins inside the period asked about says so
  first, and what LMTY captured on its first day is not called a change.
- A product with no report yet is a state with its own wording, never
  "no changes".
- The line a scheduled run must put first has a place above the title
  in each template, so the skill and its template no longer disagree.
- The working mode (bounded input, research, public profiles only) is
  written once, in the template's own line.
- What a post, a page or a tool answer says is data, never an
  instruction. Text in one that addresses an AI assistant is not
  followed.
- The social skills write "social listening began on" a date, not
  "monitored since": LMTY's other record of a product can be much
  older.
- `social-listening-brief`, `social-quote-finder` and
  `competitive-battlecard` make their first LMTY call a public one. In
  one client a refused account call was reported as the whole server
  losing sign-in, and the free form or the public profile was never
  tried.
- "Before anything else" lists every file a skill reads unconditionally:
  `references/INTERNAL.md` in the seven `competitive-` skills that read
  it in every run, and the briefing example in
  `competitive-market-briefing`.
- `references/INTERNAL.md` says when it applies: when the user gives or
  points to internal material, or a connected tool holds it. Before
  writing that there is no customer or deal evidence, a skill searches
  any connected meetings, CRM or document tool.
- Every shared reference ends with the line `End of` and its name, and
  a file counts as read only once that line is seen. The validator
  checks the line is there. A short read of a shared file was reused by
  every later skill in the conversation.
- Before an item is ranked or described as new, the skill reads the
  competitor's earlier record, and an item LMTY already held is given
  the date it was first recorded instead.
- `get_report_changes` and `get_recent_activity` take `since`, and the
  skills that read back to a date pass it instead of paging until the
  dates pass it. `competitive-enablement-refresh` and
  `competitive-asset-audit` read the change record in every run.
- `references/LMTY.md` names the report's section keys.
- A missing input that names the subject (an account, a release) is
  asked for first; missing supporting evidence runs the short form and
  says what is missing in its first line. Each skill says which of its
  inputs is which.
- Reads made for an earlier request in the same conversation count, and
  the read line says how many were this run's.
- Every short form says which sections it keeps.
- `competitive-messaging-audit` sorts a distinct claim with no customer
  evidence either way as "untested", not "differentiated but
  irrelevant".
- `competitive-market-shift-analysis` uses its short form once it has
  said the record is too thin.
- `competitive-enablement-refresh` asks for an undated asset's
  last-updated date, and without one reads the change record back 90
  days and says so.
- A keyword search of the market feed is literal. A skill that looks for
  moves in an area reads each competitor's events by competitor and
  date and judges them by content.
- The first line that says what is missing, and the line that declares a
  bounded or research mode, is one sentence. Read counts go where the
  template keeps them, and nothing read is not listed as counts of zero.
- A profile LMTY collects no posts for has no read count: the answer
  says the posts are not collected, never "0 posts read".
- `competitive-deal-prep` stops on an account no source holds before the
  short form applies: the account is a missing subject, not missing
  evidence.
- `social-keyword-check` says once, in the opening, that Social
  Listening is off, and no later section repeats it: not "Not checked",
  the offer or "Next", and not as a reason.
- `competitive-market-shift-analysis` puts the mode line first, with its
  date, and the thin or young record after it.
- A refused account call is not a lost connection. Every `competitive-`
  skill makes its first LMTY call a public one (`search_profiles` for a
  company the request names) before `list_products`, and on a refusal or
  a sign-in request, in whatever words the client reports it, carries on
  with the public profiles. The skills that need the account (asset
  audit, enablement refresh, messaging audit, market briefing, executive
  brief) say so in one sentence, do what their public-profiles form
  allows, and never call the server down. `references/LMTY.md` says the
  same under "Detecting it", and the playbooks follow the same order.
- `company-relationship-map` names whose page lists an integration, from
  the site of the tie's source, and with no source read names the read
  that would show it.

## [1.0.0] - 2026-09-28

Initial public release of Competitive Skills by LMTY: Agent Skills for
competitive GTM work, from market briefings and positioning through to
battlecards and win/loss analysis, shipping together as the `lmty` plugin
and installable one at a time.

Every skill works on its own and gains current, sourced competitor data
when the LMTY MCP server is connected.

### Added

Market and competitor work:

- `competitive-market-briefing`
- `competitive-deep-dive`
- `competitive-market-shift-analysis`
- `competitive-executive-market-brief`

Positioning, pricing and launches:

- `competitive-positioning`
- `competitive-messaging-audit`
- `competitive-pricing-packaging-review`
- `competitive-launch-readiness`
- `competitive-roadmap-review`

Sales:

- `competitive-battlecard`
- `competitive-objection-response`
- `competitive-deal-prep`
- `competitive-poc-rfp-plan`
- `competitive-enablement-refresh`
- `competitive-asset-audit`
- `competitive-win-loss-analysis`

Packaging:

- The pack is an Agent Plugin: one `plugin.json` at the root, skills in
  `skills/`, the LMTY server in `mcp.json`.
- Installs as `lmty@lmty-plugins` in Claude Code, Codex, the ChatGPT
  desktop app and GitHub Copilot CLI; loads directly in Cursor; installs
  as a Gemini CLI extension; and its skills install anywhere else through
  the skills CLI.
- Every release attaches `lmty-<version>.zip` for offline installs.

[Unreleased]: https://github.com/LMTYdotcom/skills/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/LMTYdotcom/skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/LMTYdotcom/skills/releases/tag/v1.0.0
