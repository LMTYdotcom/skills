# Competitive Skills by LMTY

[![Installs](https://skills.sh/b/LMTYdotcom/skills)](https://skills.sh/LMTYdotcom/skills)
[![Validate](https://github.com/LMTYdotcom/skills/actions/workflows/validate.yaml/badge.svg)](https://github.com/LMTYdotcom/skills/actions/workflows/validate.yaml)
[![Release](https://img.shields.io/github/v/release/LMTYdotcom/skills?label=release)](https://github.com/LMTYdotcom/skills/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Use your AI assistant for competitive work you already do: researching
competitors and market shifts, building positioning and messaging, reviewing
pricing and launches, creating battlecards, preparing deals, analyzing wins
and losses, and keeping sales enablement current.

Add the pack once, then ask in plain English, "Give me this week's
competitive briefing." Your assistant selects the matching skill and follows
a repeatable method for completing the work. The skills work in Claude Code,
ChatGPT and Codex, GitHub Copilot, Cursor, Gemini CLI and any assistant that
supports [Agent Skills](https://agentskills.io); the pack itself is an
[Agent Plugin](https://agent-plugins.org).

Every skill works on its own. Connect [LMTY](https://lmty.com) and each one
starts from your tracked competitors, kept current with what has changed and
the evidence behind it, instead of a blank page.

## What you can ask

| Skill | Ask something like | You get |
| --- | --- | --- |
| [`competitive-market-briefing`](skills/competitive-market-briefing/SKILL.md) | "Give me this week's competitive briefing." | A calm digest of what actually changed, and what to watch |
| [`competitive-deep-dive`](skills/competitive-deep-dive/SKILL.md) | "Get me fully up to speed on Northwind." | One competitor, understood and evidenced |
| [`competitive-market-shift-analysis`](skills/competitive-market-shift-analysis/SKILL.md) | "Everyone is adding AI. Is this a real shift or just noise?" | A verdict: noise, one move, an emerging shift, or a new expectation |
| [`competitive-executive-market-brief`](skills/competitive-executive-market-brief/SKILL.md) | "Board meeting Friday. What market changes could blindside me?" | What leadership must decide, with the uncertainty shown |
| [`competitive-positioning`](skills/competitive-positioning/SKILL.md) | "Our competitors all sound like us now. Pressure-test our positioning." | A position tested against the alternatives buyers really consider |
| [`competitive-messaging-audit`](skills/competitive-messaging-audit/SKILL.md) | "Does our homepage still differentiate us?" | What still works, what went generic, what buyers would say instead |
| [`competitive-pricing-packaging-review`](skills/competitive-pricing-packaging-review/SKILL.md) | "Northwind raised prices. What should we look at before changing ours?" | The market evidence a pricing decision needs, and the decision named |
| [`competitive-launch-readiness`](skills/competitive-launch-readiness/SKILL.md) | "Here's the PRD. What do I need to know before we launch?" | Whether it's parity, catch-up or real differentiation, and how to frame it |
| [`competitive-battlecard`](skills/competitive-battlecard/SKILL.md) | "Build a battlecard for us vs Northwind." | A card a rep can use with two minutes before a call |
| [`competitive-objection-response`](skills/competitive-objection-response/SKILL.md) | "The buyer just said Northwind is cheaper. What do I say?" | The facts checked, a response, and the question to ask next |
| [`competitive-deal-prep`](skills/competitive-deal-prep/SKILL.md) | "Prep me for the Globex call tomorrow - we're up against Northwind." | One deal, prepared for the next meeting |
| [`competitive-poc-rfp-plan`](skills/competitive-poc-rfp-plan/SKILL.md) | "We're going into a POC against Northwind. What should we prove?" | An evaluation planned around the criteria that will decide it |
| [`competitive-enablement-refresh`](skills/competitive-enablement-refresh/SKILL.md) | "Northwind changed their pricing. What in our talk tracks is now wrong?" | The lines that changed, with proof and date |
| [`competitive-asset-audit`](skills/competitive-asset-audit/SKILL.md) | "Audit our competitive materials. Which claims are stale?" | Every competitive claim, marked and ranked by exposure |
| [`competitive-win-loss-analysis`](skills/competitive-win-loss-analysis/SKILL.md) | "Why are we losing to Northwind?" | What buyers actually said, counted, with the exceptions kept |
| [`competitive-roadmap-review`](skills/competitive-roadmap-review/SKILL.md) | "Competitors keep adding this. Does it matter for our roadmap?" | Product questions from market and customer evidence, not a copied feature list |

You do not pick a skill; the right one is chosen for you. If a request needs
more than one, the assistant does the part that fits and tells you which
skill to run next.

You can also call a skill directly: `/lmty:competitive-battlecard Northwind`
in Claude Code and GitHub Copilot, `$competitive-battlecard` in Codex, `@`
in ChatGPT.

## Connect LMTY

Without LMTY, a skill researches the competitor from scratch each time and
tells you the answer is a snapshot. With LMTY connected, it already knows
your product, your tracked competitors, what changed and when, and the
sources behind each claim.

| Without LMTY | With LMTY |
| --- | --- |
| Asks who "we" are and which competitor | Already knows your product and your competitor set |
| Researches a snapshot, dated today | Reads tracked market state with a history of changes |
| "Not observed" | "Not observed, last checked on `<date>`" |
| Sources are whatever it found this session | Every claim carries its sources and how fresh they are |

[LMTY](https://lmty.com) tracks a product's competitors and keeps a current
report plus a log of what moved.

The connection is already set up for you. This pack ships with the LMTY
server configured, so in Claude Code, ChatGPT and Codex, GitHub Copilot CLI,
Cursor and Gemini CLI your assistant will ask you to sign in, in your
browser - ChatGPT and Codex as part of installing, the others the first time
you open a session with the plugin enabled. Approve it once and every skill
here uses it from then on.

No skill needs LMTY to run, and none will refuse work without it. If you
never connect, the skills research from scratch and say so.

<details>
<summary>Connecting by hand, or with an API token</summary>

If your assistant installed the skills through `npx skills add`, it did not
see the server. Add it to your assistant's MCP configuration as a Streamable
HTTP server at `https://mcp.lmty.com/mcp`; sign-in is discovered
automatically.

If you would rather not use the browser sign-in, LMTY can issue a token from
your account settings. Add the server to your own configuration with an
`Authorization: Bearer <token>` header rather than relying on the bundled
one.

</details>

## Install

Each install below is the LMTY plugin: the full skill pack plus the LMTY
connection. Start with the tool you already use.

### ChatGPT and Codex

In the ChatGPT desktop app, the LMTY marketplace appears as a source in the
Plugins Directory once it has been added; install the plugin from there and
it is available in Codex and in ChatGPT Work.

To add the marketplace, from the Codex CLI:

```bash
codex plugin marketplace add LMTYdotcom/skills
codex plugin add lmty@lmty-plugins
```

Skills are invoked as `$competitive-battlecard` in Codex and with `@` in
ChatGPT.

### Claude Code

Inside a Claude Code session, type `/plugin marketplace add
LMTYdotcom/skills`, then `/plugin install lmty@lmty-plugins`.

Or run these two commands in your terminal:

```bash
claude plugin marketplace add LMTYdotcom/skills
claude plugin install lmty@lmty-plugins
```

To get a newer version later:

```bash
claude plugin marketplace update lmty-plugins
claude plugin update lmty@lmty-plugins
```

To try it without installing, download the release zip and run
`claude --plugin-dir lmty-<version>.zip`.

### More tools and the command line

<details>
<summary>GitHub Copilot, Cursor, Gemini CLI, and any other assistant</summary>

#### GitHub Copilot CLI

```bash
copilot plugin marketplace add LMTYdotcom/skills
copilot plugin install lmty@lmty-plugins
```

Or install straight from the repository, without a marketplace:

```bash
copilot plugin install LMTYdotcom/skills
```

#### Cursor

Cursor loads the pack as an Agent Plugin. Clone or unzip it into
`~/.cursor/plugins/local/lmty`, restart Cursor, and the skills appear under
**Customize**. Teams and Enterprise workspaces can add the repository as a
team marketplace instead, from **Dashboard -> Plugins**.

#### Gemini CLI

```bash
gemini extensions install https://github.com/LMTYdotcom/skills
```

#### OpenCode, Antigravity, Windsurf, Amp, Kiro, Cline and the rest

The [skills CLI](https://github.com/vercel-labs/skills) installs the skills
into whichever assistants it finds on your machine:

```bash
npx skills add LMTYdotcom/skills
```

That asks which skills and which assistants you want. To take the whole pack
into every assistant it finds without being asked, add `--all`, which is
shorthand for `--skill '*' --agent '*' -y`:

```bash
npx skills add LMTYdotcom/skills --all
```

To install just one skill, add `--skill` and its name:

```bash
npx skills add LMTYdotcom/skills --skill competitive-battlecard
```

This route installs the skills only. To also connect LMTY, add the MCP
server to your assistant by hand; see [Connect LMTY](#connect-lmty).

#### Download

Every release on the [releases page](https://github.com/LMTYdotcom/skills/releases/latest)
includes `lmty-<version>.zip`. Unzip it and point your assistant at the
folder, or copy a single folder out of `skills/` into wherever your
assistant keeps skills (for example `~/.claude/skills/`). Each skill is
self-contained.

</details>

<details>
<summary>Versions and updates</summary>

Most installs track the `main` branch, not a release, and every client
decides for itself when to pull a change:

| Client | Installs from | Updates when |
| --- | --- | --- |
| Claude Code | `main` | you run `claude plugin update`, and the version has changed |
| ChatGPT and Codex | `main` | you refresh the marketplace |
| GitHub Copilot CLI | `main` | you run `copilot plugin update` |
| Cursor | the branch the marketplace tracks | that branch moves |
| Gemini CLI | the latest release | a newer release is published |
| skills CLI | `main` | you run `npx skills update` |

`main` is always a releasable state - every push is validated - so tracking
it is the intended default.

To pin to a release instead, name it at install time:

```bash
npx skills add LMTYdotcom/skills#v1.0.0
gemini extensions install https://github.com/LMTYdotcom/skills --ref=v1.0.0
codex plugin marketplace add LMTYdotcom/skills --ref v1.0.0
```

In the skills CLI, `#` takes a tag, branch or commit, while `@` picks a
skill, so `LMTYdotcom/skills#v1.0.0@competitive-battlecard` is one skill
at one version. `npx skills update` then keeps re-checking the ref you
pinned rather than moving you forward.

</details>

## How the skills behave

Competitive work goes wrong in a few repeatable ways. Most of what is in
these skills exists to stop one of them.

- **Absence is not evidence.** A pricing page that does not mention audit
  logging says something about the page, not the product. The skills write
  "not observed in the sources checked, as of a date," never "does not
  have."
- **No invented motive.** A competitor raised prices; why is unknowable
  without a statement from them, and the skills say so instead of guessing.
- **Dates travel with claims.** Every material fact carries the date it was
  observed, and coverage is tracked separately from freshness.
- **Fact and interpretation are kept apart.** Observed fact, interpretation,
  implication, and action are labeled, and any ranking is marked as the
  skill's own judgment.
- **Recommendations name the decision, not the answer.** Without your
  internal numbers and deal evidence, the useful output is the question and
  the evidence needed to settle it.
- **Empty sections stay empty.** "No validated objections yet - pull the
  last 20 calls where this competitor was named" is more useful than three
  plausible ones.
- **They hand off.** A request that straddles two skills gets the half this
  skill owns and the name of the one that owns the rest.

## How they were tested

Every skill was run against three models from different vendors, with a
fourth model grading the output against written criteria, and then run live
in Claude Code against the real LMTY server. Across the pack, the right
skill is chosen for 95% of example requests, including the ones written to
sit on the boundary between two neighbors.

The test criteria are kept out of this repository on purpose: a skill should
not ship with its own answer key.

## Contributing

Bug reports and suggestions are welcome as
[issues](https://github.com/LMTYdotcom/skills/issues). If you want to change
a skill, [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how the repository is
laid out and what a change needs before it merges. Taking part means
following the [Code of Conduct](CODE_OF_CONDUCT.md).

Need help rather than a change? [`SUPPORT.md`](SUPPORT.md) says where to ask.

## License

MIT. See [`LICENSE`](LICENSE).
