# Changelog

All notable changes to this pack are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the pack uses [Semantic Versioning](https://semver.org/spec/v2.0.0):
the patch number for wording and fixes, the minor number when a skill is
added or its scope changes, the major number if the plugin is renamed or
a skill is removed.

## [Unreleased]

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

[Unreleased]: https://github.com/LMTYdotcom/skills/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/LMTYdotcom/skills/releases/tag/v1.0.0
