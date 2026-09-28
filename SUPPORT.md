# Support

Start here and you will usually get an answer faster than by opening an
issue.

## Installing, or a client not covered

The [Install section of the README](README.md#install) has a section per
client: Claude Code, ChatGPT and Codex, GitHub Copilot CLI, Cursor,
Gemini CLI, and everything else through the skills CLI. It also covers
the release zip and how to pin a version.

If your assistant is not listed and it supports
[Agent Skills](https://agentskills.io), `npx skills add
LMTYdotcom/skills` installs the skills into it. If that does not work,
open an issue and say which assistant you are using.

## Which skill should I use?

You should not have to choose: ask in your own words and the right skill
is selected for you. The [table in the README](README.md#what-you-can-ask)
lists every skill with an example request and what you get back, and each
skill's own "Do not use this skill when" section names the sibling that
owns the work it excludes.

## LMTY, the MCP server, or your account

Anything about LMTY itself - signing in, what the server tracks, pricing,
your account, the connection failing - belongs at
[lmty.com](https://lmty.com), not in this repository. This repository
contains only the skill files and the manifests that point your assistant
at the server.

The one exception: if the **manifests** here are wrong, say the endpoint
or the transport is misconfigured, that is a bug here. Open an issue.

## A skill behaved badly

Open a [bug report](https://github.com/LMTYdotcom/skills/issues/new?template=bug_report.yml).
The form asks which skill, which client, whether LMTY was connected, and
what you asked - all four matter, because most misbehavior is a
triggering problem rather than a content one.

Worth reporting: a skill triggered when a different one should have, a
skill invented a fact, an output came back in the wrong shape, a hand-off
pointed nowhere.

## A job these skills do not cover

Open a [skill request](https://github.com/LMTYdotcom/skills/issues/new?template=skill_request.yml).
Three or four example requests in a practitioner's own words are worth
more than a description of the feature.

## Security

Do not open a public issue. Use
[GitHub's private advisory form](https://github.com/LMTYdotcom/skills/security/advisories/new).
See [`SECURITY.md`](SECURITY.md).

## Conduct

Report a Code of Conduct concern to <contact@lmty.com>. See
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Changing something yourself

[`CONTRIBUTING.md`](CONTRIBUTING.md) covers the layout, the build and
validation loop, and what a change needs before it merges.
