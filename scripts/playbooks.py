#!/usr/bin/env python3
"""Read and check playbooks/<skill>.md, and render library.json from them.

A playbook is a skill's short form: a prompt of a few dozen lines that
works in any agent with only the LMTY server connected and nothing
installed. It is what a web page offers to copy and what a bot takes as
its instructions. The skill stays the full method; the playbook must not
say anything the skill does not.

    playbooks/<skill>.md  ->  library.json

The front matter is the page's structured half (who it is for, how often
to run it, what to fill in); the body is the text to paste.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLAYBOOKS = ROOT / "playbooks"
SKILLS = ROOT / "skills"
LMTY_REFERENCE = ROOT / "shared-references" / "lmty.md"

FIELDS = ("skill", "title", "audience", "cadence", "connect", "summary", "delivers", "inputs")
# `when` replaces the skill's Cadence line on a page, addressed to the reader.
# The Cadence line stays the skill's own, written for the agent running it.
OPTIONAL_FIELDS = ("when",)
WHEN_MAX = 300
INPUT_FIELDS = {"name", "required", "description", "example"}
CADENCES = ("On demand", "Daily", "Weekly", "Monthly", "Quarterly")
# What the connection needs: nothing, a signed-in account, an account with
# Social Listening on, or nothing for a free form that an account with
# Social Listening on makes the full read.
CONNECTIONS = ("public", "account", "social", "social-optional")
AUDIENCES = ("Marketing", "Sales", "Product", "Leadership", "Customer success", "Anyone")

# A summary is a card's one line; what a playbook delivers is a page's
# full-width row, a few sentences at most.
SUMMARY_MAX = 160
DELIVERS_MAX = 350
# Long enough to carry the evidence rules, short enough to read before
# pasting. Past this it is the skill, retyped.
BODY_MAX_LINES = 45
BODY_MAX_CHARS = 3600

PLACEHOLDER_RE = re.compile(r"\{([A-Z][A-Z0-9_]*)\}")
TOOL_RE = re.compile(r"\b((?:get|list|search)_[a-z_]+)\b")
CADENCE_RE = re.compile(r"^## Cadence\n\n(.+)$", re.MULTILINE)
EXAMPLES_RE = re.compile(r"## Examples of activating requests\n\n((?:- .+\n)+)")
# The pointer a Cadence line ends with when the skill is worth repeating,
# and what it says a repeat run leads with.
REPEAT_RE = re.compile(r' On a repeat run, follow "Repeat runs" in `references/QUALITY\.md`(?:: (lead with [^.]+))?\.$')


def skill_cadence(name: str) -> str | None:
    """The first line under a skill's Cadence heading."""
    path = SKILLS / name / "SKILL.md"
    if not path.exists():
        return None
    m = CADENCE_RE.search(path.read_text(encoding="utf-8"))
    return m.group(1) if m else None


def skill_when(name: str) -> str | None:
    """A skill's Cadence line as a page can show it: no file reference."""
    line = skill_cadence(name)
    if line is None:
        return None
    m = REPEAT_RE.search(line)
    if m is None:
        return line
    head = line[: m.start()]
    return f"{head} A repeat run should {m.group(1)}." if m.group(1) else head


def known_tools() -> set[str]:
    """Tool names as shared-references/lmty.md gives them."""
    return set(re.findall(r"`((?:get|list|search)_[a-z_]+)`", LMTY_REFERENCE.read_text(encoding="utf-8")))


def load() -> tuple[list[dict], list[str]]:
    """Return (playbooks, errors). A playbook with an error is still returned when it parsed."""
    books: list[dict] = []
    errors: list[str] = []
    if not PLAYBOOKS.exists():
        return books, errors
    tools = known_tools()
    for path in sorted(PLAYBOOKS.glob("*.md")):
        tag = f"playbooks/{path.name}"
        raw = path.read_bytes()
        if b"\r\n" in raw:
            errors.append(f"{tag}: has CRLF line endings, must be LF")
        text = raw.decode("utf-8")
        if not text.startswith("---\n") or text.count("\n---\n") < 1:
            errors.append(f"{tag}: missing front matter")
            continue
        _, front, body = text.split("---\n", 2)
        try:
            meta = yaml.safe_load(front)
        except yaml.YAMLError as exc:
            errors.append(f"{tag}: front matter is not valid YAML: {str(exc).splitlines()[0]}")
            continue
        if not isinstance(meta, dict):
            errors.append(f"{tag}: front matter is not a mapping")
            continue
        body = body.strip("\n")

        for key in sorted(set(meta) - set(FIELDS) - set(OPTIONAL_FIELDS)):
            errors.append(f"{tag}: unknown field `{key}`")
        for key in FIELDS:
            if key not in meta:
                errors.append(f"{tag}: missing field `{key}`")
        skill = str(meta.get("skill", ""))
        if skill != path.stem:
            errors.append(f"{tag}: `skill` is {skill!r} but the file is named for {path.stem!r}")
        if not (SKILLS / skill / "SKILL.md").exists():
            errors.append(f"{tag}: no skill named {skill!r}")

        cadence = meta.get("cadence")
        if cadence not in CADENCES:
            errors.append(f"{tag}: `cadence` must be one of {list(CADENCES)}")
        else:
            line = skill_cadence(skill)
            if line is not None and not line.startswith(cadence):
                errors.append(f"{tag}: `cadence` is {cadence!r} but the skill's Cadence section begins {line[:40]!r}")
            if line is not None and "repeat run" in line and REPEAT_RE.search(line) is None:
                errors.append(f"{tag}: the skill's Cadence section mentions a repeat run in a form library.json cannot restate")
        when = meta.get("when")
        if when is not None:
            if not isinstance(when, str) or not (1 <= len(when) <= WHEN_MAX):
                errors.append(f"{tag}: `when` must be 1 to {WHEN_MAX} characters")
            elif cadence in CADENCES and not when.startswith(cadence):
                errors.append(f"{tag}: `when` must begin with the cadence, {cadence!r}")
        if meta.get("connect") not in CONNECTIONS:
            errors.append(f"{tag}: `connect` must be one of {list(CONNECTIONS)}")
        audience = meta.get("audience")
        if not isinstance(audience, list) or not audience or not set(audience) <= set(AUDIENCES):
            errors.append(f"{tag}: `audience` must be a list drawn from {list(AUDIENCES)}")
        for key, limit in (("summary", SUMMARY_MAX), ("delivers", DELIVERS_MAX)):
            value = meta.get(key)
            if not isinstance(value, str) or not (1 <= len(value) <= limit):
                errors.append(f"{tag}: `{key}` must be 1 to {limit} characters")

        inputs = meta.get("inputs")
        declared: list[str] = []
        if not isinstance(inputs, list):
            errors.append(f"{tag}: `inputs` must be a list (empty when there is nothing to fill in)")
            inputs = []
        for i, item in enumerate(inputs):
            if not isinstance(item, dict) or set(item) != INPUT_FIELDS:
                errors.append(f"{tag}: inputs[{i}] must have exactly {sorted(INPUT_FIELDS)}")
                continue
            if not isinstance(item["required"], bool):
                errors.append(f"{tag}: inputs[{i}].required must be true or false")
            declared.append(str(item["name"]))
        used = set(PLACEHOLDER_RE.findall(body))
        for name in sorted(used - set(declared)):
            errors.append(f"{tag}: the playbook uses {{{name}}}, which `inputs` does not declare")
        for name in sorted(set(declared) - used):
            errors.append(f"{tag}: `inputs` declares {name}, which the playbook never uses")

        lines = body.splitlines()
        if len(lines) > BODY_MAX_LINES:
            errors.append(f"{tag}: {len(lines)} lines > {BODY_MAX_LINES}; a playbook is the short form")
        if len(body) > BODY_MAX_CHARS:
            errors.append(f"{tag}: {len(body)} characters > {BODY_MAX_CHARS}; a playbook is the short form")
        for tool in sorted(set(TOOL_RE.findall(body)) - tools):
            errors.append(f"{tag}: names the tool `{tool}`, which shared-references/lmty.md does not")

        books.append({**meta, "playbook": body, "_path": tag})
    return books, errors


def example_requests(skill: str) -> list[str]:
    path = SKILLS / skill / "SKILL.md"
    if not path.exists():
        return []
    m = EXAMPLES_RE.search(path.read_text(encoding="utf-8"))
    if not m:
        return []
    return [line[2:].strip().strip('"') for line in m.group(1).splitlines()]


def render_library(version: str, mcp_url: str) -> str:
    """library.json: every playbook with what a page needs to show it."""
    books, _ = load()
    entries = []
    for book in books:
        skill = str(book.get("skill", ""))
        entries.append(
            {
                "skill": skill,
                "family": skill.split("-", 1)[0],
                "title": book.get("title"),
                "audience": book.get("audience"),
                "cadence": book.get("cadence"),
                "when": book.get("when") or skill_when(skill),
                "connect": book.get("connect"),
                "summary": book.get("summary"),
                "delivers": book.get("delivers"),
                "inputs": book.get("inputs"),
                "examples": example_requests(skill),
                "playbook": book.get("playbook"),
            }
        )
    return json.dumps({"version": version, "server": mcp_url, "playbooks": entries}, indent=2, ensure_ascii=False) + "\n"
