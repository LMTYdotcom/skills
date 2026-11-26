#!/usr/bin/env python3
"""Generate everything in this repository that is derived from a source.

    shared-references/*.md  -> skills/<name>/references/{TRUST,CONTEXT,...}.md
    shared-references/social.md -> skills/<name>/references/SOCIAL.md, only
                                   where SKILL.md lists that file
    playbooks/*.md          -> library.json
    plugin.json             -> .claude-plugin/plugin.json, .claude-plugin/marketplace.json
    plugin.json             -> .agents/plugins/marketplace.json, gemini-extension.json
    MCP_SERVER              -> mcp.json, .mcp.json
    plugin.json, MCP_SERVER -> server.json

Skills get copies so a published skill directory never reaches outside
its own root. Every skill gets the references in FILES. One in
OPTIONAL_FILES goes only to a skill whose SKILL.md lists the copy, and a
copy left in a skill that no longer lists it is removed. Manifests get copies because each client reads a different
path and wants slightly different fields; symlinks do not survive a
Windows checkout or an archive install.

Root plugin.json is the Agent Plugins manifest and the only file a human
edits. Codex, ChatGPT, Copilot CLI and Cursor read it directly; only
Claude Code and Gemini CLI need their own format. The legacy Codex
manifest is not shipped; `codex_compat_manifest()` renders it for CI.

Run `validate_skills.py` afterwards.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED_REFERENCES = ROOT / "shared-references"
SKILLS = ROOT / "skills"
MANIFEST = ROOT / "plugin.json"

FILES = {
    "trust-and-evidence.md": "TRUST.md",
    "context-acquisition.md": "CONTEXT.md",
    "degradation.md": "DEGRADATION.md",
    "output-quality.md": "QUALITY.md",
    "lmty.md": "LMTY.md",
    "internal-context.md": "INTERNAL.md",
}

# Vendored only into a skill whose SKILL.md lists the copy, in backticks,
# as `references/<name>`. The rules for reading public posts are long,
# and most skills never read a post.
OPTIONAL_FILES = {
    "social.md": "SOCIAL.md",
}

# Every client installs `lmty@lmty-plugins`: plugin named for the
# product, marketplace for the catalog.
MARKETPLACE = "lmty-plugins"
MARKETPLACE_DISPLAY = "LMTY"
MARKETPLACE_DESCRIPTION = "Plugins by LMTY."
# The pack's name where a client lists it as a plugin. ChatGPT and Codex
# show the com.openai interface's displayName instead, which matches the
# ChatGPT store listing.
PACK_DISPLAY = "LMTY Skills"

# Claude Code's category is free-form; Codex's is the curated value in
# the com.openai extension.
CLAUDE_CATEGORY = "marketing"

OPENAI_NAMESPACE = "com.openai"

CLAUDE_SCHEMA = "https://json.schemastore.org/claude-code-plugin-manifest.json"
CLAUDE_MARKET_SCHEMA = "https://json.schemastore.org/claude-code-marketplace.json"

# OAuth is discovered from /.well-known/oauth-protected-resource; no
# token belongs here. The transport is spelled three ways because the
# clients differ: `streamable-http` (Agent Plugins), `http` (Claude
# Code), `httpUrl` (Gemini CLI).
MCP_SERVER = "lmty"
MCP_URL = "https://mcp.lmty.com/mcp"
MCP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"

# The server's entry in the official MCP Registry
# (registry.modelcontextprotocol.io), published from server.json with
# `mcp-publisher`. The namespace is lmty.com in reverse-DNS form, proven
# by the `v=MCPv1` TXT record on the domain's apex, and the name after
# the slash is the one the server reports in its MCP handshake. The
# title matches the handshake too.
REGISTRY_SCHEMA = "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"
REGISTRY_NAME = f"com.lmty/{MCP_SERVER}"
REGISTRY_TITLE = "LMTY"
# The registry caps the description at 100 characters.
REGISTRY_DESCRIPTION = (
    "Read-only access to your tracked competitors, market history, observed changes and sourced evidence."
)
# Served by the LMTY site, so it comes from the server's own domain.
REGISTRY_ICON = {"src": "https://lmty.com/apple-icon.png", "mimeType": "image/png", "sizes": ["180x180"]}
# GitHub's numeric id for this repository, which survives a rename:
# `gh api repos/LMTYdotcom/skills --jq .id`.
REPOSITORY_ID = "1393471039"


def dump(obj: dict) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def _manifest() -> tuple[dict, dict, dict, str]:
    """Return (base manifest, portable fields, OpenAI interface, display name)."""
    base = json.loads(MANIFEST.read_text(encoding="utf-8"))
    portable = {k: v for k, v in base.items() if k not in ("$schema", "extensions")}
    openai = (base.get("extensions") or {}).get(OPENAI_NAMESPACE) or {}
    interface = openai.get("interface") or {}
    return base, portable, interface, interface.get("displayName", base["name"])


def codex_compat_manifest() -> str:
    """The legacy `.codex-plugin/plugin.json`, rendered for CI but not shipped.

    OpenAI's validate_plugin.py only reads this layout. No `$schema`,
    because that validator rejects unknown keys.
    """
    _, portable, interface, _ = _manifest()
    codex = dict(portable)
    codex["skills"] = "./skills/"
    codex["interface"] = interface
    codex["mcpServers"] = "./.mcp.json"
    return dump(codex)


def render_manifests() -> dict[str, str]:
    """Return {relative path: file content} for every generated manifest."""
    base, portable, interface, _ = _manifest()
    display_name = PACK_DISPLAY

    # `claude plugin validate --strict` fails on `$schema` and
    # `extensions` from Agent Plugins, so they are dropped.
    claude = {"$schema": CLAUDE_SCHEMA}
    for k, v in portable.items():
        claude[k] = v
        if k == "name":
            claude["displayName"] = display_name

    # The repository is the marketplace and the plugin is its root. The
    # entry repeats the display fields because Claude Code lists them
    # before install.
    claude_market = {
        "$schema": CLAUDE_MARKET_SCHEMA,
        "name": MARKETPLACE,
        "description": MARKETPLACE_DESCRIPTION,
        "owner": base["author"],
        "plugins": [
            {
                "name": base["name"],
                "displayName": display_name,
                "source": "./",
                "description": base["description"],
                "category": CLAUDE_CATEGORY,
                "author": base["author"],
                "homepage": base["homepage"],
                "repository": base["repository"],
                "license": base["license"],
                "keywords": base["keywords"],
            }
        ],
    }

    # Shape from RawMarketplaceManifest in codex-rs/core-plugins. `./`
    # resolves to the marketplace root, so Codex reads root plugin.json
    # directly. ON_INSTALL asks for the LMTY sign-in once, up front.
    codex_market = {
        "name": MARKETPLACE,
        "interface": {"displayName": MARKETPLACE_DISPLAY},
        "plugins": [
            {
                "name": base["name"],
                "source": {"source": "local", "path": "./"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": interface.get("category", "Other"),
                "interface": {"displayName": display_name},
            }
        ],
    }

    # Gemini CLI discovers skills/ without a declaration.
    gemini = {
        "name": base["name"],
        "version": base["version"],
        "description": base["description"],
        "mcpServers": {MCP_SERVER: {"httpUrl": MCP_URL}},
    }

    # The registry lists the remote server, not the pack, so this carries
    # the endpoint and the pack's version, homepage and repository.
    registry = {
        "$schema": REGISTRY_SCHEMA,
        "name": REGISTRY_NAME,
        "title": REGISTRY_TITLE,
        "description": REGISTRY_DESCRIPTION,
        "version": base["version"],
        "websiteUrl": base["homepage"],
        "repository": {"url": base["repository"], "source": "github", "id": REPOSITORY_ID},
        "icons": [REGISTRY_ICON],
        "remotes": [{"type": "streamable-http", "url": MCP_URL}],
    }

    return {
        ".claude-plugin/plugin.json": dump(claude),
        ".claude-plugin/marketplace.json": dump(claude_market),
        ".agents/plugins/marketplace.json": dump(codex_market),
        "gemini-extension.json": dump(gemini),
        "mcp.json": dump(
            {"$schema": MCP_SCHEMA, "mcpServers": {MCP_SERVER: {"type": "streamable-http", "url": MCP_URL}}}
        ),
        ".mcp.json": dump({"mcpServers": {MCP_SERVER: {"type": "http", "url": MCP_URL}}}),
        "server.json": dump(registry),
    }


def lists_reference(skill_dir: Path, dest_name: str) -> bool:
    """Whether a skill's SKILL.md names `references/<dest_name>` in backticks."""
    skill = skill_dir / "SKILL.md"
    return skill.exists() and f"`references/{dest_name}`" in skill.read_text(encoding="utf-8")


def main() -> None:
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        ref_dir = skill_dir / "references"
        ref_dir.mkdir(parents=True, exist_ok=True)
        for src_name, dest_name in FILES.items():
            shutil.copy2(SHARED_REFERENCES / src_name, ref_dir / dest_name)
        count = len(FILES)
        for src_name, dest_name in OPTIONAL_FILES.items():
            copy = ref_dir / dest_name
            if lists_reference(skill_dir, dest_name):
                shutil.copy2(SHARED_REFERENCES / src_name, copy)
                count += 1
            elif copy.exists():
                copy.unlink()
                print(f"removed references/{dest_name}, which SKILL.md no longer lists -> {skill_dir.name}")
        print(f"vendored {count} shared references -> {skill_dir.name}")

    for rel, content in render_manifests().items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode("utf-8"))
        print(f"generated {rel}")

    # Imported here: playbooks.py needs PyYAML, which rendering the
    # manifests alone does not.
    from playbooks import render_library

    version = json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]
    (ROOT / "library.json").write_bytes(render_library(version, MCP_URL).encode("utf-8"))
    print("generated library.json")


if __name__ == "__main__":
    main()
