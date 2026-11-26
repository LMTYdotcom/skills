#!/usr/bin/env python3
"""Structural validation for the plugin and every skill under skills/.

Run after scripts/build_skills.py. Exits non-zero on any error.

Covers what no client reports back: Agent Skills and Agent Plugins
conformance, the submission rules Codex and Claude Code only apply at
review time, and house rules (vendored copies match their source, every
shipped file is referenced, generated files match the build).
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_skills import FILES, MARKETPLACE, MCP_URL, OPENAI_NAMESPACE, OPTIONAL_FILES, render_manifests

from playbooks import load as load_playbooks
from playbooks import render_library

try:
    import yaml  # optional locally; CI installs it
except ModuleNotFoundError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SHARED_REFERENCES = ROOT / "shared-references"

# Agent Skills: lowercase alphanumerics and single hyphens.
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# Agent Plugins 5.5: also periods; no leading, trailing or doubled separators.
PLUGIN_NAME_RE = re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")

AGENT_PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
AGENT_MCP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"

# Agent Plugins 5.2: the manifest schema is closed.
AGENT_PLUGIN_FIELDS = {
    "$schema", "name", "version", "description", "author", "homepage",
    "repository", "license", "keywords", "extensions",
}
# Agent Skills frontmatter. Claude Code accepts more; other clients reject it.
SKILL_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

# Allowed by the spec, forbidden here. `compatibility` claims an
# environment requirement and `allowed-tools` pre-approves tools; these
# skills have neither.
SKILL_FIELDS_UNUSED = ("compatibility", "allowed-tools")

# `author` survives a single-skill install, which has no LICENSE or
# README. `category` is namespaced to avoid Claude Code's and Codex's.
SKILL_METADATA = {"author", "com.lmty.category"}
# A skill's family is its name prefix, and each family has one category:
# `competitive-` works from the user's own product and its tracked
# competitors, `company-` from public profiles of any company, `social-`
# from the public posts LMTY collects for a signed-in user's product.
SKILL_FAMILIES = {"competitive": "ci", "company": "company", "social": "social"}
SKILL_CATEGORIES = set(SKILL_FAMILIES.values())
# The sentence a family's "say so once" line is keyed on: in
# shared-references/lmty.md for public profiles, in
# shared-references/social.md for social listening. A family built on a
# part of LMTY carries its sentence and no other family does;
# `competitive-` skills expect nothing.
EXPECTS = {
    "company": "expects LMTY's public profiles",
    "social": "expects LMTY's social listening",
}
# How often a skill is worth running: the first words under its Cadence
# heading, which a playbook's `cadence` and a page's badge repeat.
CADENCE_STARTS = ("On demand", "Daily", "Weekly", "Monthly", "Quarterly")
# Families whose skills each have a playbook: a short form that works
# with only the LMTY server connected. A `competitive-` skill starts from
# the user's account and their own material: those that a pasted prompt can
# carry have one, and the three that cannot have none.
PLAYBOOK_FAMILIES = {"company", "social"}
WITHOUT_PLAYBOOK = {"competitive-deep-dive", "competitive-positioning", "competitive-win-loss-analysis"}

# What Codex reads from extensions.com.openai (agent_plugin_manifest.rs)
# and what its submission validator accepts inside `interface`.
OPENAI_FIELDS = {"apps", "hooks", "interface"}
CODEX_INTERFACE = {
    "displayName", "shortDescription", "longDescription", "developerName",
    "category", "capabilities", "websiteURL", "privacyPolicyURL",
    "termsOfServiceURL", "brandColor", "composerIcon", "logo", "logoDark",
    "screenshots", "defaultPrompt", "default_prompt",
}
# The public directory's final-submission limits.
CODEX_LIMITS = {"displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80}
CODEX_CATEGORIES = {
    "Productivity", "Creativity", "Developer Tools", "Business & Operations",
    "Data & Analytics", "Communication", "Education & Research", "Security",
    "Finance", "Healthcare", "Travel", "Entertainment", "Other",
}
# Codex silently drops a longer starter prompt at load time.
CODEX_PROMPT_MAX = 128
# Narrower than Agent Plugins (no `.`); both must hold.
CODEX_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
CODEX_IMAGE_EXT = (".png", ".jpg", ".jpeg", ".webp", ".svg")

# Claude Code manifest fields; `claude plugin validate --strict` fails
# on anything else.
CLAUDE_FIELDS = {
    "$schema", "name", "displayName", "version", "description", "author",
    "homepage", "repository", "license", "keywords", "dependencies", "hooks",
    "commands", "agents", "skills", "outputStyles", "themes", "channels",
    "mcpServers", "lspServers", "monitors", "settings", "userConfig",
    "defaultEnabled", "metadata", "experimental",
}

# Must match FILES in build_skills.py.
VENDORED = {
    "TRUST.md": "trust-and-evidence.md",
    "CONTEXT.md": "context-acquisition.md",
    "DEGRADATION.md": "degradation.md",
    "QUALITY.md": "output-quality.md",
    "LMTY.md": "lmty.md",
    "INTERNAL.md": "internal-context.md",
}
# Must match OPTIONAL_FILES in build_skills.py. A skill carries one of
# these only when its SKILL.md lists the copy.
VENDORED_OPTIONAL = {
    "SOCIAL.md": "social.md",
}
# The reference a skill that reads public posts carries, and the families
# whose every skill does.
POSTS_REFERENCE = "references/SOCIAL.md"
POSTS_FAMILIES = {"social"}
# What only that reference explains: the tools that read an account's
# posts, and a profile's posts section. The section is matched in
# backticks or beside its field or the word "section", because plain
# "chatter" is also a grade.
POSTS_RE = re.compile(
    r"\b(?:list_mentions|get_mention_stats|list_tracked_keywords)\b"
    r"|`chatter`|\bchatterCounts\b|\bchatter section\b"
)

# The pack is versioned once, in plugin.json.
FORBIDDEN_METADATA = ("version",)

errors = []

for mine, theirs, label in ((VENDORED, FILES, "FILES"), (VENDORED_OPTIONAL, OPTIONAL_FILES, "OPTIONAL_FILES")):
    if {src: dest for dest, src in mine.items()} != theirs:
        errors.append(
            f"scripts/validate_skills.py: its list of vendored references does not match {label} in build_skills.py"
        )

for f in sorted(SHARED_REFERENCES.iterdir()):
    if f.is_file() and f.name not in VENDORED.values() and f.name not in VENDORED_OPTIONAL.values():
        errors.append(
            f"shared-references/{f.name}: not in FILES or OPTIONAL_FILES in build_skills.py, so no skill ships it"
        )

# A shared file is read once per conversation, so a read that stopped
# short is reused by every later skill. The fixed last line is what lets a
# model tell a whole read from a cut one.
for dest, src in {**VENDORED, **VENDORED_OPTIONAL}.items():
    path = SHARED_REFERENCES / src
    if path.is_file() and not path.read_text(encoding="utf-8").endswith(f"\n\nEnd of {dest}.\n"):
        errors.append(f"shared-references/{src}: must end with the line `End of {dest}.`, after a blank line")


def _https(v: object) -> bool:
    return isinstance(v, str) and v.startswith("https://") and len(v) > 8


def _nonempty(v: object) -> bool:
    return isinstance(v, str) and bool(v.strip())


def _load_json(path: Path, tag: str) -> dict | None:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{tag}: not valid JSON: {exc}")
        return None
    if not isinstance(obj, dict):
        errors.append(f"{tag}: must be a JSON object")
        return None
    return obj


# The MCP server authenticates with OAuth at run time; nothing shipped
# may carry a credential.
SECRET_KEY_RE = re.compile(r"authorization|cookie|token|secret|api[-_]?key|password", re.IGNORECASE)
SECRET_VALUE_RE = re.compile(r"\bBearer\s+\S{8,}|\b(?:sk|ghp|gho|xox[abp]|lmty)[-_][A-Za-z0-9]{16,}")


def _scan_secrets(obj: object, tag: str, path: str = "$") -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if SECRET_KEY_RE.search(str(k)) and isinstance(v, str) and v.strip():
                errors.append(f"{tag}: {path}.{k} looks like a credential; nothing here may carry one")
                continue
            _scan_secrets(v, tag, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _scan_secrets(v, tag, f"{path}[{i}]")
    elif isinstance(obj, str) and SECRET_VALUE_RE.search(obj):
        errors.append(f"{tag}: {path} looks like a credential; nothing here may carry one")


def check_codex_interface(iface: dict, tag: str, prefix: str, author_name: str | None) -> None:
    """OpenAI's validate_plugin.py rules, the runtime's silent limits, and
    the directory's final-submission limits."""
    for k in sorted(set(iface) - CODEX_INTERFACE):
        errors.append(f"{tag}: `{prefix}.{k}` is not accepted by Codex plugin validation")
    for k in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not _nonempty(iface.get(k)):
            errors.append(f"{tag}: `{prefix}.{k}` must be a non-empty string")
    for k, limit in CODEX_LIMITS.items():
        v = iface.get(k)
        if isinstance(v, str) and len(v) > limit:
            errors.append(f"{tag}: `{prefix}.{k}` is {len(v)} characters; the directory allows {limit}")
        if isinstance(v, str) and k != "longDescription" and "\n" in v:
            errors.append(f"{tag}: `{prefix}.{k}` must be one line")
    if author_name and _nonempty(iface.get("developerName")) and iface["developerName"] != author_name:
        errors.append(f"{tag}: `{prefix}.developerName` must match `author.name` for submission")
    if _nonempty(iface.get("category")) and iface["category"] not in CODEX_CATEGORIES:
        errors.append(f"{tag}: `{prefix}.category` {iface['category']!r} is not in the directory taxonomy")
    caps = iface.get("capabilities")
    if not isinstance(caps, list) or not caps or not all(_nonempty(c) for c in caps):
        errors.append(f"{tag}: `{prefix}.capabilities` must be a non-empty array of strings")
    elif len(caps) > 20 or any(len(c) > 120 or "\n" in c for c in caps):
        errors.append(f"{tag}: `{prefix}.capabilities` allows 20 entries of one line, 120 characters each")
    prompt = iface.get("defaultPrompt", iface.get("default_prompt"))
    if prompt is None:
        errors.append(f"{tag}: `{prefix}.defaultPrompt` is required")
    else:
        prompts = prompt if isinstance(prompt, list) else [prompt]
        if not (1 <= len(prompts) <= 3 and all(_nonempty(p) for p in prompts)):
            errors.append(f"{tag}: `{prefix}.defaultPrompt` must be 1 to 3 non-empty strings")
        normalized = [" ".join(p.split()).casefold() for p in prompts if isinstance(p, str)]
        if len(set(normalized)) != len(normalized):
            errors.append(f"{tag}: `{prefix}.defaultPrompt` entries must be distinct")
        for p in prompts:
            if not isinstance(p, str):
                continue
            if len(" ".join(p.split())) > CODEX_PROMPT_MAX or "\n" in p:
                errors.append(
                    f"{tag}: `{prefix}.defaultPrompt` entry must be one line of at most "
                    f"{CODEX_PROMPT_MAX} characters; Codex drops it at load time"
                )
            if "@" in p:
                errors.append(f"{tag}: `{prefix}.defaultPrompt` must not mention an MCP server with `@`")
    for k in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
        if k in iface and not _https(iface[k]):
            errors.append(f"{tag}: `{prefix}.{k}` must be an https URL")
    color = iface.get("brandColor")
    if color is not None and not re.fullmatch(r"#[0-9A-Fa-f]{6}", str(color)):
        errors.append(f"{tag}: `{prefix}.brandColor` must be #RRGGBB")
    # The directory requires both images; the runtime does not.
    for k in ("logo", "composerIcon"):
        if k not in iface:
            errors.append(f"{tag}: `{prefix}.{k}` is required for a directory listing")
    assets = [iface[k] for k in ("composerIcon", "logo", "logoDark") if k in iface]
    screenshots = iface.get("screenshots", [])
    if not isinstance(screenshots, list):
        errors.append(f"{tag}: `{prefix}.screenshots` must be an array")
        screenshots = []
    for a in assets + list(screenshots):
        # Codex resolves only `./` paths; the submission validator rejects `..`.
        if not isinstance(a, str) or not a.startswith("./") or ".." in a:
            errors.append(f"{tag}: asset `{a}` must be a `./` path inside the plugin")
        elif not (ROOT / a).is_file():
            errors.append(f"{tag}: asset `{a}` does not exist")
        elif not a.lower().endswith(CODEX_IMAGE_EXT):
            errors.append(f"{tag}: asset `{a}` must be png, jpg, jpeg, webp or svg")


# ---------------------------------------------------------------------------
# plugin.json and CHANGELOG.md

manifest = _load_json(ROOT / "plugin.json", "plugin.json") or {}
version = manifest.get("version", "")
if not SEMVER_RE.match(str(version)):
    errors.append(f"plugin.json: version {version!r} is not X.Y.Z; the release tag is v<version>")
changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").exists() else ""
# release.yaml lifts the release notes out by this heading.
if not re.search(rf"^## \[{re.escape(str(version))}\] - \d{{4}}-\d{{2}}-\d{{2}}$", changelog, re.MULTILINE):
    errors.append(
        f"CHANGELOG.md: no '## [{version}] - YYYY-MM-DD' heading for the version in plugin.json"
    )
if not re.search(r"^## \[Unreleased\]$", changelog, re.MULTILINE):
    errors.append("CHANGELOG.md: no '## [Unreleased]' heading; the next change has nowhere to go")
for ver in re.findall(r"^## \[(?!Unreleased)([^\]]+)\]", changelog, re.MULTILINE):
    if not re.fullmatch(r"\d+\.\d+\.\d+", ver):
        errors.append(f"CHANGELOG.md: release heading '[{ver}]' is not X.Y.Z")
    elif f"[{ver}]:" not in changelog:
        errors.append(f"CHANGELOG.md: '[{ver}]' has no link definition at the foot of the file")

if manifest.get("$schema") != AGENT_PLUGIN_SCHEMA:
    errors.append(f"plugin.json: `$schema` must be {AGENT_PLUGIN_SCHEMA}")
for k in sorted(set(manifest) - AGENT_PLUGIN_FIELDS):
    errors.append(
        f"plugin.json: `{k}` is not an Agent Plugins field; client-specific data goes under `extensions`"
    )
plugin_name = manifest.get("name", "")
if not (isinstance(plugin_name, str) and 1 <= len(plugin_name) <= 64 and PLUGIN_NAME_RE.match(plugin_name)):
    errors.append(f"plugin.json: name {plugin_name!r} breaks the Agent Plugins name rules")
elif not CODEX_NAME_RE.match(plugin_name):
    errors.append(
        f"plugin.json: name {plugin_name!r} breaks the OpenAI directory's name rule (letters, digits, `_`, `-`)"
    )
if not re.fullmatch(r"[A-Za-z0-9_-]+", MARKETPLACE):
    errors.append(f"build_skills.py: MARKETPLACE {MARKETPLACE!r} breaks the Codex marketplace name rule")
for k in ("version", "description", "homepage", "repository", "license"):
    if k in manifest and not _nonempty(manifest[k]):
        errors.append(f"plugin.json: `{k}` must be a non-empty string")
# Optional in Agent Plugins; required by every client that lists the plugin.
for k in ("version", "description"):
    if not _nonempty(manifest.get(k)):
        errors.append(f"plugin.json: `{k}` is required by every client that lists the plugin")
if isinstance(manifest.get("description"), str) and len(manifest["description"]) > 1024:
    errors.append("plugin.json: `description` over 1024 characters; the OpenAI directory rejects it")
for k in ("homepage", "repository"):
    if k in manifest and not _https(manifest[k]):
        errors.append(f"plugin.json: `{k}` must be an https URL")
author = manifest.get("author")
if not isinstance(author, dict) or not _nonempty(author.get("name")):
    errors.append("plugin.json: `author.name` is required (Claude Code and Codex both require it)")
else:
    for k in sorted(set(author) - {"name", "email", "url"}):
        errors.append(f"plugin.json: `author.{k}` is not allowed; Agent Plugins permits name, email, url")
    for k, v in author.items():
        if not _nonempty(v):
            errors.append(f"plugin.json: `author.{k}` must be a non-empty string")
    if "url" in author and not _https(author["url"]):
        errors.append("plugin.json: `author.url` must be an https URL")
keywords = manifest.get("keywords")
if keywords is not None:
    if not isinstance(keywords, list) or not all(_nonempty(k) for k in keywords):
        errors.append("plugin.json: `keywords` must be an array of non-empty strings")
    elif len(set(keywords)) != len(keywords):
        errors.append("plugin.json: `keywords` contains a duplicate")

extensions = manifest.get("extensions")
if extensions is not None and not isinstance(extensions, dict):
    errors.append("plugin.json: `extensions` must be an object")
    extensions = None
for ns, val in (extensions or {}).items():
    if not re.fullmatch(r"[a-z0-9-]+(?:\.[a-z0-9-]+)+", ns):
        errors.append(f"plugin.json: extension namespace `{ns}` must be reverse-domain (com.example.client)")
    if not isinstance(val, dict):
        errors.append(f"plugin.json: `extensions.{ns}` must be an object")

openai = (extensions or {}).get(OPENAI_NAMESPACE)
if not isinstance(openai, dict):
    errors.append(f"plugin.json: `extensions.{OPENAI_NAMESPACE}` is required for the Codex listing")
else:
    for k in sorted(set(openai) - OPENAI_FIELDS):
        errors.append(f"plugin.json: `extensions.{OPENAI_NAMESPACE}.{k}` is not read by Codex")
    iface = openai.get("interface")
    if not isinstance(iface, dict):
        errors.append(f"plugin.json: `extensions.{OPENAI_NAMESPACE}.interface` is required for submission")
    else:
        check_codex_interface(
            iface, "plugin.json", f"extensions.{OPENAI_NAMESPACE}.interface",
            author.get("name") if isinstance(author, dict) else None,
        )
_scan_secrets(manifest, "plugin.json")

# A root CLAUDE.md is never loaded as plugin context and fails --strict.
if (ROOT / "CLAUDE.md").exists():
    errors.append("CLAUDE.md: must not sit at the plugin root; move it to .claude/CLAUDE.md")
# Claude Code loads commands/ as skills; a file there would shadow one.
if (ROOT / "commands").exists():
    errors.append("commands/: must not exist; skills/ is the only skill location")

# ---------------------------------------------------------------------------
# mcp.json (Agent Plugins spec 7.2)

mcp = _load_json(ROOT / "mcp.json", "mcp.json")
if mcp is not None:
    tag = "mcp.json"
    if set(mcp) != {"$schema", "mcpServers"}:
        errors.append(f"{tag}: top-level fields must be exactly `$schema` and `mcpServers`")
    if mcp.get("$schema") != AGENT_MCP_SCHEMA:
        errors.append(f"{tag}: `$schema` must be {AGENT_MCP_SCHEMA}")
    # Spec 10.1: both files target one Agent Plugins version.
    plugin_ver = re.search(r"/schemas/([^/]+)/", str(manifest.get("$schema", "")))
    mcp_ver = re.search(r"/schemas/([^/]+)/", str(mcp.get("$schema", "")))
    if plugin_ver and mcp_ver and plugin_ver.group(1) != mcp_ver.group(1):
        errors.append(f"{tag}: targets Agent Plugins {mcp_ver.group(1)} but plugin.json targets {plugin_ver.group(1)}")
    servers = mcp.get("mcpServers")
    if not isinstance(servers, dict):
        errors.append(f"{tag}: `mcpServers` must be an object")
        servers = {}
    for sname, s in servers.items():
        where = f"{tag}: mcpServers.{sname}"
        if not isinstance(s, dict):
            errors.append(f"{where} must be an object")
            continue
        t = s.get("type")
        if t in ("streamable-http", "sse"):
            for k in sorted(set(s) - {"type", "url", "headers"}):
                errors.append(f"{where}.{k} is not a field of the `{t}` variant")
            url = s.get("url")
            parts = urlsplit(url) if isinstance(url, str) else None
            if parts is None or parts.scheme not in ("http", "https") or not parts.netloc:
                errors.append(f"{where}.url must be an absolute http(s) URL")
            else:
                if parts.username or parts.password or parts.fragment:
                    errors.append(f"{where}.url must not carry user information or a fragment")
                host = parts.hostname or ""
                loopback = host == "localhost" or host.startswith("127.") or host == "::1"
                if parts.scheme == "http" and not loopback:
                    errors.append(f"{where}.url must use https for a non-loopback host")
            headers = s.get("headers")
            if headers is not None and (
                not isinstance(headers, dict) or not all(isinstance(v, str) for v in headers.values())
            ):
                errors.append(f"{where}.headers must be an object of strings")
        elif t == "stdio":
            for k in sorted(set(s) - {"type", "command", "args", "env", "cwd"}):
                errors.append(f"{where}.{k} is not a field of the `stdio` variant")
            if not _nonempty(s.get("command")):
                errors.append(f"{where}.command is required")
            for k in ("PLUGIN_ROOT", "PLUGIN_DATA"):
                if k in (s.get("env") or {}):
                    errors.append(f"{where}.env.{k} is reserved for the client")
        else:
            errors.append(f"{where}.type must be stdio, streamable-http or sse")
    _scan_secrets(mcp, tag)

for rel in (".mcp.json", "gemini-extension.json"):
    obj = _load_json(ROOT / rel, rel) if (ROOT / rel).exists() else None
    if obj is not None:
        _scan_secrets(obj, rel)

# ---------------------------------------------------------------------------
# Every skill

skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
if not skill_dirs:
    errors.append("no skills found under skills/")

for d in skill_dirs:
    p = d / "SKILL.md"
    if not p.exists():
        errors.append(f"{d.name}: missing SKILL.md")
        continue
    raw = p.read_bytes()
    text = raw.decode("utf-8")
    lines = text.splitlines()
    if len(lines) > 500:
        errors.append(f"{d.name}: {len(lines)} lines > 500 recommended")
    if not text.startswith("---\n"):
        errors.append(f"{d.name}: missing YAML frontmatter")
        continue
    try:
        _, fm, body = text.split("---", 2)
    except ValueError:
        errors.append(f"{d.name}: invalid frontmatter delimiters")
        continue
    # Strict parsers reject an unquoted ": " in a value; lenient ones
    # load it, so the skill silently vanishes from some clients.
    parsed: dict | None = None
    if yaml is not None:
        try:
            parsed = yaml.safe_load(fm)
            if not isinstance(parsed, dict):
                raise TypeError("frontmatter is not a mapping")
        except Exception as exc:
            errors.append(f"{d.name}: frontmatter is not valid YAML: {str(exc).splitlines()[0]}")
            continue
    else:
        for m in re.finditer(r"^(name|description):\s*(.*)$", fm, re.MULTILINE):
            v = m.group(2)
            if not v.startswith(('"', "'", ">", "|")) and ": " in v:
                errors.append(f"{d.name}: {m.group(1)} contains ': ' and is unquoted; strict YAML parsers reject it")

    keys = set(parsed) if parsed is not None else set(re.findall(r"^([A-Za-z][\w-]*):", fm, re.MULTILINE))
    for k in sorted(keys - SKILL_FIELDS):
        errors.append(f"{d.name}: frontmatter key `{k}` is not in the Agent Skills spec; other clients reject it")

    name_m = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
    desc_m = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
    if not name_m or not desc_m:
        errors.append(f"{d.name}: missing name or description")
        continue
    name = name_m.group(1).strip().strip('"')
    desc = desc_m.group(1).strip().strip('"')
    if name != d.name:
        errors.append(f"{d.name}: frontmatter name mismatch {name}")
    if len(name) > 64 or not NAME_RE.match(name):
        errors.append(f"{d.name}: invalid name")
    if not (1 <= len(desc) <= 1024):
        errors.append(f"{d.name}: description length {len(desc)} invalid")
    approx_tokens = len(text.split()) * 1.33
    if approx_tokens > 5000:
        errors.append(f"{d.name}: approx {approx_tokens:.0f} tokens > 5000 recommended")

    # A single-skill install carries no LICENSE file.
    lic_m = re.search(r"^license:\s*(.+)$", fm, re.MULTILINE)
    lic = lic_m.group(1).strip().strip('"') if lic_m else ""
    if lic != manifest.get("license"):
        errors.append(f"{d.name}: frontmatter license {lic!r} must be {manifest.get('license')!r}, the pack license")
    for key in SKILL_FIELDS_UNUSED:
        if key in keys:
            errors.append(
                f"{d.name}: `{key}` must not be set; these skills have no environment "
                "requirement and execute nothing, so any value would claim something untrue"
            )

    meta = parsed.get("metadata") if parsed is not None else None
    if parsed is not None:
        if not isinstance(meta, dict):
            errors.append(f"{d.name}: metadata is required and must be a mapping")
        else:
            if not all(isinstance(v, str) for v in meta.values()):
                errors.append(f"{d.name}: metadata must map string keys to string values (Agent Skills spec)")
            for k in sorted(set(meta) - SKILL_METADATA):
                errors.append(f"{d.name}: metadata.{k} is not one of {sorted(SKILL_METADATA)}")
            for k in sorted(SKILL_METADATA - set(meta)):
                errors.append(f"{d.name}: metadata.{k} is missing")
            cat = meta.get("com.lmty.category")
            if cat is not None and cat not in SKILL_CATEGORIES:
                errors.append(
                    f"{d.name}: metadata.com.lmty.category {cat!r} is not one of "
                    f"{sorted(SKILL_CATEGORIES)}; a new group is a decision, not a typo"
                )
            family = name.split("-", 1)[0]
            if family not in SKILL_FAMILIES:
                errors.append(
                    f"{d.name}: name must start with one of "
                    f"{sorted(f + '-' for f in SKILL_FAMILIES)}; a new family is a decision, not a typo"
                )
            elif cat in SKILL_CATEGORIES and cat != SKILL_FAMILIES[family]:
                errors.append(
                    f"{d.name}: metadata.com.lmty.category must be {SKILL_FAMILIES[family]!r} "
                    f"for a `{family}-` skill, not {cat!r}"
                )

    for key in FORBIDDEN_METADATA:
        if re.search(rf"^  {key}:", fm, re.MULTILINE):
            errors.append(f"{d.name}: metadata.{key} must not be set; the pack is versioned in plugin.json")

    refs = set(re.findall(r"`((?:references|assets|scripts)/[^`]+)`", text))
    for ref in sorted(refs):
        if not (d / ref).exists():
            errors.append(f"{d.name}: missing referenced file {ref}")

    # An unreferenced file is dead weight that still costs activation budget.
    shipped = {
        str(f.relative_to(d)).replace("\\", "/")
        for f in d.rglob("*")
        if f.is_file() and f.name != "SKILL.md"
    }
    for orphan in sorted(shipped - refs):
        errors.append(f"{d.name}: {orphan} ships but SKILL.md never references it")

    # A skill must not ship its own answer key.
    if (d / "references" / "EVALS.md").exists():
        errors.append(
            f"{d.name}: references/EVALS.md must not ship; acceptance criteria "
            "are kept out of this repository"
        )

    for dest, src in VENDORED.items():
        copy = d / "references" / dest
        if not copy.exists():
            errors.append(f"{d.name}: missing vendored references/{dest}")
        elif copy.read_bytes() != (SHARED_REFERENCES / src).read_bytes():
            errors.append(
                f"{d.name}: references/{dest} differs from shared-references/{src}; "
                "edit shared-references and run scripts/build_skills.py"
            )

    # An optional reference ships only where SKILL.md lists it. A copy
    # that is not listed is caught above as an unreferenced file.
    for dest, src in VENDORED_OPTIONAL.items():
        rel = f"references/{dest}"
        copy = d / rel
        if rel not in refs:
            continue
        if not copy.exists():
            errors.append(f"{d.name}: SKILL.md lists {rel} but the copy is missing; run scripts/build_skills.py")
        elif copy.read_bytes() != (SHARED_REFERENCES / src).read_bytes():
            errors.append(
                f"{d.name}: {rel} differs from shared-references/{src}; "
                "edit shared-references and run scripts/build_skills.py"
            )

    own_family = name.split("-", 1)[0]
    carries_posts = POSTS_REFERENCE in refs
    if own_family in POSTS_FAMILIES and not carries_posts:
        errors.append(
            f"{d.name}: a `{own_family}-` skill must list `{POSTS_REFERENCE}` in SKILL.md; "
            "it holds the rules for reading posts"
        )
    if not carries_posts:
        vendored_names = set(VENDORED) | set(VENDORED_OPTIONAL)
        for f in sorted(d.rglob("*")):
            if not f.is_file() or (f.parent.name == "references" and f.name in vendored_names):
                continue
            m = POSTS_RE.search(f.read_text(encoding="utf-8", errors="ignore"))
            if m:
                errors.append(
                    f"{d.name}: {f.relative_to(d).as_posix()} names {m.group(0)!r}, a tool or a profile section "
                    f"that reads public posts, but SKILL.md does not list `{POSTS_REFERENCE}`; a skill that reads "
                    "posts carries that reference (the grade is written as plain chatter, not in backticks)"
                )

    for family, sentence in EXPECTS.items():
        says = sentence in body
        if family == own_family and not says:
            errors.append(
                f"{d.name}: a `{family}-` skill must say it {sentence!r}, "
                "which is what lets it tell the user what is missing"
            )
        elif family != own_family and says:
            errors.append(
                f"{d.name}: only a `{family}-` skill may say it {sentence!r}; "
                "no other skill tells the user what to connect or turn on"
            )

    cadence = re.search(r"^## Cadence\n\n(.+)$", body, re.MULTILINE)
    if cadence is None:
        errors.append(f"{d.name}: missing a `## Cadence` section saying how often the skill is worth running")
    elif not cadence.group(1).startswith(CADENCE_STARTS):
        errors.append(f"{d.name}: the Cadence section must begin with one of {list(CADENCE_STARTS)}")

    numbers = [int(n) for n in re.findall(r"^### Step (\d+) -", body, re.MULTILINE)]
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        errors.append(f"{d.name}: workflow steps are numbered {numbers}")

    for f in sorted(d.rglob("*")):
        if f.is_file() and b"\r\n" in f.read_bytes():
            errors.append(f"{d.name}: {f.relative_to(d).as_posix()} has CRLF line endings, must be LF")

    print(f"{d.name:30} lines={len(lines):3d} words={len(text.split()):4d} desc={len(desc):3d}")


# Hand-offs must point both ways. A skill nothing signposts toward
# collects its neighbors' requests.
SKILL_LIKE_RE = re.compile(
    r"^(competitive|competitor|company|social|market|launch|pricing|executive|sales|messaging|roadmap|win-loss|poc)-"
)
names = {d.name for d in skill_dirs}
points_to: dict[str, set[str]] = {}
for d in skill_dirs:
    text = (d / "SKILL.md").read_text(encoding="utf-8")
    section = re.search(r"## Do not use this skill when\n(.*?)\n## ", text, re.DOTALL)
    found = set(re.findall(r"`([a-z][a-z0-9-]+)`", section.group(1))) if section else set()
    points_to[d.name] = (found & names) - {d.name}

    for n in sorted(set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", text)) - names):
        if SKILL_LIKE_RE.match(n):
            errors.append(f"{d.name}: names `{n}`, which is not a skill in this pack")

for name in sorted(names):
    if len(names) > 1 and not any(name in targets for targets in points_to.values()):
        errors.append(
            f"{name}: no sibling's 'Do not use this skill when' points to it; "
            "nothing routes requests away from its neighbors toward it"
        )

# ---------------------------------------------------------------------------
# Playbooks

playbooks, playbook_errors = load_playbooks()
errors.extend(playbook_errors)
with_playbook = {str(book.get("skill")) for book in playbooks}
for name in sorted(names):
    if name.split("-", 1)[0] in PLAYBOOK_FAMILIES and name not in with_playbook:
        errors.append(f"{name}: no playbooks/{name}.md; every skill of its family has a short form")
    if name in WITHOUT_PLAYBOOK and name in with_playbook:
        errors.append(f"{name}: has a playbook; it depends on material a pasted prompt cannot carry")
library_path = ROOT / "library.json"
library_expected = render_library(str(manifest.get("version")), MCP_URL)
if not library_path.exists():
    errors.append("library.json: missing; run scripts/build_skills.py")
elif library_path.read_bytes() != library_expected.encode("utf-8"):
    errors.append("library.json: differs from what the build generates; run scripts/build_skills.py")
for book in playbooks:
    for url in re.findall(r"https?://[^\s`)\"']+", str(book.get("playbook", ""))):
        if url.rstrip(".,;") != MCP_URL:
            errors.append(f"{book['_path']}: links {url}; a playbook names only the LMTY server, {MCP_URL}")

# ---------------------------------------------------------------------------
# README

readme = (ROOT / "README.md").read_text(encoding="utf-8")
listed = set(re.findall(r"^\| \[`([a-z0-9-]+)`\]\(skills/\1/SKILL\.md\)", readme, re.MULTILINE))
for n in sorted(names - listed):
    errors.append(f"README.md: skill table does not list {n}")
for n in sorted(listed - names):
    errors.append(f"README.md: skill table lists {n}, which does not ship")
install_id = f"{plugin_name}@{MARKETPLACE}"
if install_id not in readme:
    errors.append(f"README.md: never mentions the install id `{install_id}`")
if names and f"/{plugin_name}:" not in readme:
    errors.append(f"README.md: never shows the slash-command namespace `/{plugin_name}:`")

# ---------------------------------------------------------------------------
# Generated files

generated = render_manifests()
for rel, expected in generated.items():
    path = ROOT / rel
    if not path.exists():
        errors.append(f"{rel}: missing; run scripts/build_skills.py")
    elif path.read_bytes() != expected.encode("utf-8"):
        errors.append(f"{rel}: differs from what the build generates; run scripts/build_skills.py")

# The MCP Registry entry. Its name must sit in the namespace the lmty.com
# TXT record proves, and the registry rejects a description over 100
# characters or a remote that is not the public endpoint.
REGISTRY_NAME_RE = re.compile(r"^[a-zA-Z0-9.-]+/[a-zA-Z0-9._-]+$")
SERVER_JSON = ROOT / "server.json"
reg = _load_json(SERVER_JSON, "server.json") if SERVER_JSON.exists() else None
if reg is not None:
    tag = "server.json"
    name = str(reg.get("name", ""))
    if not REGISTRY_NAME_RE.match(name) or not name.startswith("com.lmty/"):
        errors.append(f"{tag}: `name` must be `com.lmty/<server>`")
    desc = reg.get("description")
    if not _nonempty(desc) or len(desc) > 100:
        errors.append(f"{tag}: `description` must be 1 to 100 characters")
    if reg.get("version") != manifest.get("version"):
        errors.append(f"{tag}: `version` must match plugin.json")
    remotes = reg.get("remotes")
    if not isinstance(remotes, list) or [r.get("url") for r in remotes] != [MCP_URL]:
        errors.append(f"{tag}: `remotes` must list exactly the LMTY server, {MCP_URL}")
    for i, icon in enumerate(reg.get("icons") or []):
        if not _https(icon.get("src")):
            errors.append(f"{tag}: icons[{i}].src must be an https URL")

CLAUDE_MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
cm_claude = _load_json(CLAUDE_MANIFEST, ".claude-plugin/plugin.json") if CLAUDE_MANIFEST.exists() else None
if cm_claude is not None:
    for k in sorted(set(cm_claude) - CLAUDE_FIELDS):
        errors.append(f".claude-plugin/plugin.json: `{k}` is not a Claude Code manifest field; --strict fails on it")
    if not _nonempty(cm_claude.get("name")):
        errors.append(".claude-plugin/plugin.json: `name` is required")

if (ROOT / ".codex-plugin").exists():
    errors.append(".codex-plugin/: must not exist; Codex reads plugin.json and extensions.com.openai")

# Shape from RawMarketplaceManifest in codex-rs/core-plugins; there is
# no published schema.
CODEX_MARKET = ROOT / ".agents" / "plugins" / "marketplace.json"
mk = _load_json(CODEX_MARKET, ".agents/plugins/marketplace.json") if CODEX_MARKET.exists() else None
if mk is not None:
    tag = ".agents/plugins/marketplace.json"
    if not _nonempty(mk.get("name")):
        errors.append(f"{tag}: `name` is required")
    if "interface" in mk and not _nonempty((mk["interface"] or {}).get("displayName")):
        errors.append(f"{tag}: `interface.displayName` must be a non-empty string")
    plugins = mk.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append(f"{tag}: `plugins` must be a non-empty array")
    else:
        for i, entry in enumerate(plugins):
            where = f"{tag}: plugins[{i}]"
            if not _nonempty(entry.get("name")):
                errors.append(f"{where}.name is required")
            src = entry.get("source")
            if isinstance(src, dict):
                kind = src.get("source")
                need = {"local": ("path",), "url": ("url",), "git-subdir": ("url", "path"), "npm": ("package",)}
                if kind not in need:
                    errors.append(f"{where}.source.source must be one of {sorted(need)}")
                else:
                    for k in need[kind]:
                        if not _nonempty(src.get(k)):
                            errors.append(f"{where}.source.{k} is required for source `{kind}`")
                    if kind in ("url", "git-subdir") and not _https(src["url"]):
                        errors.append(f"{where}.source.url must be an https URL")
                    src_path = str(src.get("path"))
                    if kind == "local" and not (src_path in (".", "./") or src_path.startswith("./")):
                        errors.append(f"{where}.source.path must start with `./`")
            elif not _nonempty(src):
                errors.append(f"{where}.source must be a path string or an object")
            policy = entry.get("policy") or {}
            if policy.get("installation", "AVAILABLE") not in ("NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"):
                errors.append(f"{where}.policy.installation has an unknown value")
            if policy.get("authentication", "ON_INSTALL") not in ("ON_INSTALL", "ON_USE"):
                errors.append(f"{where}.policy.authentication has an unknown value")
            products = policy.get("products")
            if products is not None and (
                not isinstance(products, list) or not set(products) <= {"CHATGPT", "CODEX", "ATLAS"}
            ):
                errors.append(f"{where}.policy.products must list only CHATGPT, CODEX or ATLAS")
            if not _nonempty(entry.get("category")):
                errors.append(f"{where}.category is required for listing")

# No shipped copy may count the skills; the number goes stale. The
# first pattern needs "skills" within two words; the second catches a
# large written-out number anywhere, which in this copy can only be the
# tally. Small numbers stay legal ("a request that spans two skills").
COUNT_RE = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|\d+)\s+"
    r"(?:\w+\s+){0,2}?skills\b",
    re.IGNORECASE,
)
copy_sources = {
    "plugin.json": [json.dumps(manifest)],
    "README.md": [readme.split("## What you can ask")[0]],
    "CHANGELOG.md": [changelog],
}
for rel, content in generated.items():
    copy_sources[rel] = [content]
for where, blobs in copy_sources.items():
    for blob in blobs:
        m = COUNT_RE.search(blob)
        if m:
            errors.append(
                f"{where}: copy counts the skills ({m.group(0)!r}). "
                "The number goes stale; describe what they do instead"
            )

TALLY_RE = re.compile(
    r"\b(ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|"
    r"eighteen|nineteen|twenty|thirty|forty|fifty)\b",
    re.IGNORECASE,
)
tally_sources = dict(copy_sources)
tally_sources["README.md"] = [readme]
for where, blobs in tally_sources.items():
    for blob in blobs:
        m = TALLY_RE.search(blob)
        if m:
            errors.append(
                f"{where}: copy spells out a number ({m.group(0)!r}) that "
                "can only be the skill count. Name what they do instead"
            )

if errors:
    print("\nERRORS:")
    for e in errors:
        print("-", e)
    sys.exit(1)
print(f"\nAll {len(skill_dirs)} skills passed structural validation.")
