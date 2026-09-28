# Working in this repository

This is a pack of Agent Skills. The repository root is the plugin;
`skills/<name>/` are the distributable units.

## Rules

- Edit `shared-references/`, never `skills/*/references/{TRUST,CONTEXT,DEGRADATION,QUALITY,LMTY,INTERNAL}.md`.
  Those are vendored copies; the build overwrites them and the validator
  rejects drift.
- Edit `plugin.json`, never `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`
  or `gemini-extension.json`. Those are generated from it by the build.
  Codex and ChatGPT listing metadata lives in `plugin.json` under
  `extensions.com.openai`; the marketplace name, category and MCP
  endpoint live in `scripts/build_skills.py`.
- `mcp.json` and `.mcp.json` are generated too. Change the source in
  `scripts/build_skills.py`, never the output.
- Do not add `.codex-plugin/plugin.json`: Codex reads `plugin.json` and
  ignores the legacy file when the extension is present.
- Skills live only in `skills/`. Do not add a `commands/` directory:
  every skill already has a slash command, and a command file would
  shadow it.
- Never put a token, key or secret in any file here. The MCP server
  authenticates with OAuth, discovered at run time.
- After any change under `shared-references/`, `skills/` or `plugin.json`,
  run `python3 scripts/build_skills.py` then
  `python3 scripts/validate_skills.py` and fix every error before
  finishing. Do not weaken the validator to make it pass.
- LF line endings only, everywhere.
- US English everywhere, prose and code. `cspell.config.yaml` pins
  `language: en-US` and CI enforces it. Add a genuine new term to the
  `words` list there; never silence a line.
- The pack is versioned once, in `plugin.json`, as `X.Y.Z`. Do not add
  `version` to a skill's frontmatter `metadata`, and do not put a
  version in the marketplace files.
- A version bump needs a matching `## X.Y.Z` section in `CHANGELOG.md`.
- A skill's frontmatter is `name`, `description`, `license: MIT` and
  `metadata` holding exactly `author: LMTY` and `com.lmty.category`,
  which is `ci`. Do not add `compatibility` or `allowed-tools`: the
  skills have no environment requirement and execute nothing, so either
  would claim something untrue. Any other key makes other clients
  reject the skill.
- Every file inside a skill must be referenced from its `SKILL.md` in
  backticks. Orphans fail validation.
- Every skill has a row in the README table and an entry in the
  bug-report dropdown.
- A skill's `description` is what triggers it. If you change what a
  skill owns, change the description, not just the body.
- Hand-offs name a sibling in this pack. Do not reference skills that
  do not exist here, including planned ones.
- Skills carry method, not facts. Never bake a claim about a real
  company, product or price into a skill or a template. Examples use
  fictional placeholders, consistently: `Acme Inc.` (or `Acme`) is the
  home company, `Northwind` is a competitor, `Globex` the buyer account,
  and `Initech` another competitor. The briefing example also uses
  `Vantage`, `Orbit`, `Cardinal`, `Meridian`, and `Beacon` as competitors. Real
  product names belong only in the README's compatibility list, and in
  a skill only as an output destination that claims nothing, like
  Slack or email.
- Nothing about how the skills are tested ships here beyond the summary
  in the README. Acceptance criteria, fixtures and run records live in a
  separate private repository.

See `CONTRIBUTING.md` for the full checklist.
