# Contributing

Issues are welcome for anything: a skill that triggered when it should
not have, an output that invented something, a client the install
instructions do not cover. Pull requests are reviewed by LMTY; small,
focused ones merge fastest.

Taking part means following the [Code of Conduct](CODE_OF_CONDUCT.md).
If you need help rather than want to change something, start with
[`SUPPORT.md`](SUPPORT.md).

## Layout

```text
skills/<name>/               a distributable skill: SKILL.md, references/, assets/
shared-references/           policy every skill vendors; edit here, never the copies
assets/                      plugin artwork used by the client listings
scripts/build_skills.py      generates everything derived from a source (below)
scripts/validate_skills.py   the gate; CI runs it on every pull request
scripts/package_release.py   builds dist/lmty-<version>.zip
scripts/requirements.in      the Python tools the scripts and CI need; edit this one
scripts/requirements.txt     compiled from it with hashes (generated)
plugin.json                  the Agent Plugins manifest and the pack version; edit this one
mcp.json .mcp.json           the LMTY MCP server (generated)
.claude-plugin/              Claude Code manifest and marketplace (generated)
.agents/plugins/             Codex and ChatGPT marketplace (generated)
gemini-extension.json        Gemini CLI extension manifest (generated)
.claude/CLAUDE.md            Claude Code project instructions; imports AGENTS.md
CHANGELOG.md                 one section per release; the release notes come from here
```

The repository root is the plugin. `skills/` is discovered by every
client; the manifests only add metadata.

## One manifest, many clients

Root `plugin.json` follows the [Agent Plugins](https://agent-plugins.org)
specification and is the only manifest a human edits. Clients that read
the standard - Codex and ChatGPT, GitHub Copilot CLI, Cursor - load it
directly. The others get a generated copy in the place they look:

| Client | Reads | Generated |
| --- | --- | --- |
| Claude Code | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.mcp.json` | all three |
| Codex, ChatGPT | `plugin.json`, `mcp.json`, `.agents/plugins/marketplace.json` | marketplace, `mcp.json` |
| GitHub Copilot CLI | `plugin.json`, `mcp.json`, `.claude-plugin/marketplace.json` | marketplace, `mcp.json` |
| Cursor | `plugin.json`, `mcp.json` | `mcp.json` |
| Gemini CLI | `gemini-extension.json` | yes |
| Everything else | `skills/*/SKILL.md` via the skills CLI | - |

The Agent Plugins schema is closed: the only top-level fields are the
ones in the specification, and anything client-specific goes under
`extensions`, keyed by reverse-domain namespace. The Codex and ChatGPT
listing (display name, descriptions, category, starter prompts, logo)
lives at `extensions.com.openai.interface`. Codex reads it from there
and ignores a legacy `.codex-plugin/plugin.json` when it is present, so
none is shipped; the validator rejects one. The public directory holds
the listing to tighter limits than the runtime (a 30-character display
name and short description, a fixed category list, matching developer
and author names), and `validate_skills.py` applies those limits to the
source. The marketplace name, the Claude Code category and the MCP
endpoint are constants in `scripts/build_skills.py`.

The generated files are real files rather than symlinks because
symlinks do not survive a default Windows checkout or an archive
install. Edit `plugin.json`, run the build, commit everything it
touched. The validator rejects a generated file that differs from what
the build produces, so a hand edit cannot survive a pull request.

## The MCP server

The LMTY server is declared once in `scripts/build_skills.py` and
written three ways, because the clients spell the transport differently:
Agent Plugins says `type: streamable-http` (`mcp.json`), Claude Code
says `type: http` (`.mcp.json`), Gemini CLI says `httpUrl`
(`gemini-extension.json`).

Authentication is OAuth, discovered from the server's
`/.well-known/oauth-protected-resource`. **No token belongs in any file
in this repository.** The validator scans every shipped config for
anything that looks like a credential. A bearer token is supported for
advanced use, but that is a user's own configuration, not something we
ship.

When the sign-in happens is the client's decision, not the package's,
with one exception: the Codex marketplace entry sets
`policy.authentication`, and it is `ON_INSTALL`, so ChatGPT and Codex
ask for the LMTY sign-in as part of installing. Every other client
connects at the start of a session and prompts from its MCP menu.

## Schemas

Root `plugin.json`, `mcp.json` and both Claude Code files declare their
schema inline. CI checks each against it with
[`check-jsonschema`](https://github.com/python-jsonschema/check-jsonschema),
along with the workflow, Dependabot and issue-form files. To run the
same checks locally:

```bash
pip install -r scripts/requirements.txt
check-jsonschema --schemafile https://agent-plugins.org/schemas/1.0.0/plugin.schema.json plugin.json
check-jsonschema --schemafile https://agent-plugins.org/schemas/1.0.0/mcp.schema.json mcp.json
check-jsonschema --builtin-schema vendor.github-workflows .github/workflows/*.yaml
```

The workflow schema does not check expression contexts, so CI also runs
[actionlint](https://github.com/rhysd/actionlint). A context used where
it is not available passes the schema and then fails at GitHub before
any job starts, with no log to read. CI downloads the release and checks
its sha256 before running it; to move to a newer actionlint, bump the
version and the hash together in `validate.yaml`, taking the hash from
the release's `checksums.txt`. Locally, run `actionlint` from your PATH.

[zizmor](https://docs.zizmor.sh) then audits the same files for the
ways a workflow gets exploited: template injection, a dangerous trigger,
a credential left in the checkout, an unpinned action. CI runs it
through `zizmorcore/zizmor-action`, which pins the zizmor build by
container digest, so Dependabot's bump of the action is how zizmor is
upgraded. Run it locally with `pip install zizmor` and
`zizmor .github/workflows/`. An install that is unpinned on purpose
carries a `# zizmor: ignore[...]` comment saying why; do not add one to
make a finding go away.

`.agents/plugins/marketplace.json` and `gemini-extension.json` have no
published schema; `validate_skills.py` checks their shape against the
Codex source and the Gemini extension reference instead.

## Testing an install

If you install the pack to try a change, set these first:

```bash
export DO_NOT_TRACK=1 DISABLE_TELEMETRY=1
```

`npx skills add` reports an `install` event that feeds the public
install count, and a test install is not a real one. Both variable names
are read by its telemetry gate, and Claude Code honors them too. The
CI workflows set them at the top of the file for the same reason.

In Claude Code, `claude --plugin-dir .` loads the checkout directly
without installing. Cursor loads a copy placed in
`~/.cursor/plugins/local/lmty`. Codex and Copilot CLI add the checkout
as a local marketplace: `codex plugin marketplace add .` or
`copilot plugin marketplace add .`, then install `lmty@lmty-plugins`.

## The loop

```bash
python3 scripts/build_skills.py       # vendor shared-references, regenerate every client file
python3 scripts/validate_skills.py    # must pass before you open a PR
```

Python 3.11 or later. `pip install -r scripts/requirements.txt` installs
PyYAML, check-jsonschema and skills-ref, the only tools the scripts and
CI use. PyYAML is optional but recommended: with it the validator parses
every frontmatter as real YAML, which is what the skills CLI does.

`requirements.txt` is compiled from `requirements.in` by pip-compile,
with a hash for every package, and CI installs with `--require-hashes`
so a substituted package fails the build. To add or change a tool, edit
`requirements.in` and run
`pip-compile --generate-hashes --strip-extras scripts/requirements.in`;
Dependabot keeps the compiled file current otherwise.

The validator is the test suite, and it grows with the pack: a change
that adds a requirement on a skill or a manifest comes with a rule in
`validate_skills.py` that enforces it, in the same pull request. The
validator is never weakened to let a change through.

`validate_skills.py` fails on: a `plugin.json` field outside the Agent
Plugins schema, a name that breaks its rules or the OpenAI directory's,
a `com.openai` interface that OpenAI's validator or the public directory
would reject, an `mcp.json` server outside the specification's
variants, anything that looks like a credential in a shipped config, a
`CLAUDE.md`, `commands/` or `.codex-plugin/` at the plugin root,
frontmatter that is not valid YAML (an unquoted description containing
a colon followed by a space is the usual cause), a frontmatter key
outside the four the skills use, a `compatibility` or `allowed-tools`
field, a `metadata` block that is not exactly `author` and
`com.lmty.category`, a category other than `ci`, a frontmatter `name`
that does not match its directory, a description outside 1-1024
characters, a `license` that is not the pack's, a shipped file that
`SKILL.md` never references, a vendored reference that differs from its
`shared-references/` origin, a generated file that differs from what the
build produces, workflow steps not numbered `1..n`, CRLF line endings
anywhere, a hand-off to a skill that is not in the pack, a
`metadata.version` key, a skill missing from the README table, a README
that does not show the current install id, a `plugin.json` version that
is not `X.Y.Z` or has no `CHANGELOG.md` section, and a skill that no
sibling routes toward in its "Do not use this skill when" section.

## What CI runs

Every pull request runs `.github/workflows/validate.yaml`: the loop
above, a dry run of the release zip, every manifest against its JSON
schema, `editorconfig-checker`, `markdownlint-cli2` (config in
`.editorconfig` and `.markdownlint-cli2.yaml`; `npx markdownlint-cli2
--fix` handles most of what it flags), `cspell`, the official `skills-ref
validate` from agentskills.io, OpenAI's `validate_plugin.py` against a
scratch copy carrying the legacy Codex manifest it expects (derived
from `plugin.json` the way OpenAI's portal derives it), `claude plugin
validate --strict` on both Claude Code files (the check the
community-marketplace review runs), and two install smoke tests - a
Claude Code marketplace add and install from the checkout, and `npx
skills add . --list`. Weekly, `links.yaml` checks every link in the
Markdown, `live-install.yaml` installs from GitHub the way a user
would, and `scorecard.yaml` runs the
[OpenSSF Scorecard](https://scorecard.dev), whose findings land in the
Security tab and whose score is published at
[scorecard.dev](https://scorecard.dev/viewer/?uri=github.com/LMTYdotcom/skills).

Two workflows handle pull requests rather than checking them.
`labeler.yaml` labels a pull request from the paths it touches, using
`.github/labeler.yaml`; a label there must already exist in the
repository, because the action never creates one and silently skips a
name it cannot find. `dependabot-automerge.yaml` turns on GitHub's
auto-merge for a Dependabot pull request, but only for a patch or minor
update - a major bump stays a human decision. Auto-merge is a wait, not
a bypass: `main` requires the Validate jobs to pass, and without that
protection auto-merge would land the update immediately instead of
holding it until CI agrees.

YAML files use the `.yaml` extension, which is the one the YAML spec
recommends. The three files under `.github/ISSUE_TEMPLATE/` are the
exception and must stay `.yml`: GitHub documents only that spelling for
issue forms and for the template chooser's `config.yml`, and a name it
does not recognize fails silently - the form simply stops appearing.
Workflows and `dependabot.yaml` are documented to accept either.

## Spelling

The pack is written in US English, and `cspell.config.yaml` pins
`language: en-US` so it stays that way. Dialect drift is the reason the
check exists: mixed spellings read fine line by line and are close to
invisible in review, but the prose is the product here, so a stray
British ending on a verb or a noun ships in a skill a user reads.

Run it locally with:

```bash
npx cspell lint --dot "**/*.{md,py,json,yaml,yml}"
```

`--dot` is not optional. Without it the glob skips every path beginning
with a dot, which is the workflows and the issue forms a reporter
reads; CI passes `check_dot_files` for the same reason.

If it flags a real term rather than a typo, add the word to the `words`
list in `cspell.config.yaml`, in the section it belongs to, rather than
silencing the line. Keep the list short: a dictionary that absorbs
everything stops catching anything. The config skips generated manifests
and the vendored copies under `skills/*/references/`, because those are
byte-identical to their sources and `validate_skills.py` already proves
it - fix the spelling in `plugin.json` or `shared-references/` and
rebuild.

## Shared policy

The policy files in `shared-references/` are maintained once and copied into
every skill as `references/TRUST.md`, `CONTEXT.md`, `DEGRADATION.md`,
`QUALITY.md`, `LMTY.md` and `INTERNAL.md`. Edit the source, run the
build, commit both. A pull request that edits a vendored copy directly
will fail validation. The list lives in `FILES` in
`scripts/build_skills.py`; the validator reads the same list.

`shared-references/lmty.md` is the only place LMTY's tool names appear.
Skill bodies talk about capabilities, so an interface change touches one
file.

## Changing a skill

- `SKILL.md` stays under 500 lines and roughly 5,000 tokens. Detail goes
  in `references/`, templates in `assets/`.
- The frontmatter is four fields and no others:

  ```yaml
  name: competitive-battlecard
  description: ...
  license: MIT
  metadata:
    author: LMTY
    com.lmty.category: ci
  ```

  Claude Code accepts more, but claude.ai uploads, the Skills API and
  other clients reject a skill that uses anything outside the six the
  Agent Skills spec defines, so the skills stay inside it.
- `com.lmty.category` is `ci` - the only group the pack has today. The
  key is namespaced because the spec asks for keys unlikely to collide,
  and both Claude Code and Codex have a `category` of their own nearby.
  A second value means the pack's shape changed; that is a decision to
  make deliberately, so the validator rejects one.
- The two remaining spec fields stay unused, and the validator rejects
  them. `compatibility` states an environment requirement, and these
  skills have none: no scripts, no packages, no required product, and
  `shared-references/degradation.md` makes prompt-and-documents a
  supported mode, so both web access and the LMTY server are optional.
  `allowed-tools` pre-approves tools, and no skill executes anything.
  Either one would claim something untrue, and a client or reviewer
  reading it as a prerequisite is a real risk for a pack whose whole
  portability rests on needing nothing.
- The `description` does the triggering. If a skill should claim a kind
  of request, the vocabulary of that request has to be in the
  description, not just the body. A description that does not name what
  its own examples say is the usual cause of a skill not triggering.
  Front-load the trigger words: Codex shortens descriptions when many
  skills are installed.
- "Do not use this skill when" names the sibling that owns the excluded
  work. Every skill must be named by at least one sibling there.
- Workflow steps are `### Step N - Title`, numbered contiguously.
- Every file in the skill directory is referenced from `SKILL.md` in
  backticks, as `references/X.md` or `assets/X.md`.
- No `version` in frontmatter metadata. The pack is versioned as a
  whole in `plugin.json`.
- Skill text is provider-neutral. Say "the model" or "your assistant",
  not the name of one client.
- LF line endings. `.gitattributes` enforces it, and so does the
  validator.

## Adding a skill

Create `skills/<name>/SKILL.md` with the four frontmatter fields above,
run the build so it gets the vendored references, add a row to the
table in `README.md`, add the skill to the dropdown in
`.github/ISSUE_TEMPLATE/bug_report.yml`, and have at least one existing
skill point to it from its "Do not use this skill when" section. The
validator will tell you what is missing.

## Releasing

Releases are tagged `vX.Y.Z` and published by `.github/workflows/release.yaml`.

1. Set `version` in `plugin.json` and run the build so the client
   manifests pick it up.
2. Move the `## [Unreleased]` entries in `CHANGELOG.md` under a new
   `## [X.Y.Z] - YYYY-MM-DD` heading, leave `## [Unreleased]` empty above
   it, and add the two link definitions at the foot. The body between
   that heading and the next one becomes the release notes, so the
   heading has to be exact; the validator checks its shape and the date.
3. Run the loop; `python3 scripts/package_release.py` should produce
   `dist/lmty-X.Y.Z.zip`.
4. Commit, tag `vX.Y.Z`, push the tag. The workflow validates, rebuilds
   the zip, signs its build provenance, and creates the GitHub Release
   with it attached.

Releases are immutable. Once published, the zip and the tag cannot be
changed or deleted, and the tag name can never be reused, so a mistake
in a release is fixed by publishing the next patch version, not by
editing the one that shipped. Release notes stay editable.

Every release carries two attestations. `gh release verify vX.Y.Z -R
LMTYdotcom/skills` proves the zip is the one attached to that release;
`gh attestation verify lmty-X.Y.Z.zip -R LMTYdotcom/skills` proves it
was built by `release.yaml` from the tagged commit.

Bump the patch version for wording and fixes, the minor version when a
skill is added or its scope changes, the major version if the plugin is
renamed or a skill is removed.

Three separate things carry a version, and a release is only coherent
when all three move together:

- **`plugin.json` `version`** is what Claude Code compares to decide an
  update exists. Forget it and nobody on Claude Code ever sees the
  change, however many commits land.
- **The git tag** is the only signal Gemini CLI has: it asks the GitHub
  API for the latest *release* and ignores the manifest version entirely.
  No tag, no update.
- **The default branch** is what everyone else installs, including
  `npx skills add`, which resolves `HEAD` rather than any release. `main`
  is therefore always live, which is why the validator gates every push.

The release zip doubles as the Gemini extension archive, so
`gemini-extension.json` has to stay at the root of it. If you change what
`package_release.py` puts in the archive, keep that file at the top
level. The zip must also stay the release's only asset: Gemini CLI
uses a generic asset only when exactly one is attached, and falls back
to the source archive otherwise. Do not attach a checksum file or a
second archive format.

## What we will not merge

- Vendored copies edited directly
- Skills whose acceptance criteria or test fixtures are shipped inside
  the skill
- Claims about competitors, products or markets baked into a skill;
  the skills carry method, not facts
- A real company or product named inside a skill or template. Examples
  use fictional placeholders, and the same ones throughout: `Acme Inc.`
  (or `Acme`) is the home company, `Northwind` is a competitor, `Globex`
  the buyer account, and `Initech` another competitor. The briefing
  example also uses `Vantage`, `Orbit`, `Cardinal`, `Meridian`, and
  `Beacon` as fictional competitors. A real name dates the content and
  reads as a claim about a company that never agreed to appear. The
  exceptions are the README's compatibility list, which is a statement
  of fact about clients, and a plain output destination such as Slack
  or email, which claims nothing about the destination
- Anything that makes a skill refuse work because LMTY is not connected
