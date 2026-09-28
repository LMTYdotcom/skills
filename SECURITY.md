# Security

## Supported versions

The latest release is the only supported version. Skills are content
rather than a deployed service, so there is no back-porting: a fix lands
on `main` and goes out in the next release. If you are pinned to an older
tag, moving to the latest one is the upgrade path.

## Repository scope

This repository contains Markdown skill files, JSON manifests, and the
small Python scripts under `scripts/` used only at development time.
Nothing here runs at install or at skill-activation time, and nothing
here holds credentials or talks to LMTY directly. The manifests point
your assistant at the LMTY MCP server, which authenticates you with
OAuth in your browser and is a separate product with its own security
process.

If you find something that matters anyway - a skill instruction that
could be used to exfiltrate context, a script that does something it
should not, a manifest pointing somewhere it should not - report it
privately through GitHub:

**[Report a vulnerability](https://github.com/LMTYdotcom/skills/security/advisories/new)**

Please do not open a public issue for security reports. We will
acknowledge within five working days.
