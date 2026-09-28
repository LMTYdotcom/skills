#!/usr/bin/env python3
"""Build the release artifact: dist/<name>-<version>.zip

The plugin directory as a client would install it: every manifest, the
license, the README, skills/ and assets/. Left out: shared-references/
(the skills carry vendored copies), scripts/, .github/ and .claude/.

Deterministic: entries sorted, one fixed timestamp. Pass --check-tag
vX.Y.Z to fail if it does not match plugin.json.
"""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
FIXED_DATE = (2026, 1, 1, 0, 0, 0)

TOP_LEVEL = (
    "plugin.json",
    "mcp.json",
    ".mcp.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
    "gemini-extension.json",
    "LICENSE",
    "README.md",
    "CHANGELOG.md",
)

TREES = ("skills", "assets")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-tag", help="fail unless this equals v<plugin.json version>")
    args = ap.parse_args()

    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    plugin, version = manifest["name"], manifest["version"]
    if args.check_tag and args.check_tag != f"v{version}":
        print(f"tag {args.check_tag} does not match plugin.json version {version}", file=sys.stderr)
        return 1

    files: list[tuple[str, bytes]] = [(name, (ROOT / name).read_bytes()) for name in TOP_LEVEL]
    for tree in TREES:
        for path in sorted((ROOT / tree).rglob("*")):
            if path.is_file():
                files.append((path.relative_to(ROOT).as_posix(), path.read_bytes()))

    problems = []
    for name, blob in files:
        if name.endswith("EVALS.md"):
            problems.append(f"{name}: acceptance criteria must not ship")
        if name.endswith(".zip"):
            problems.append(f"{name}: nested archive")
        if b"\r\n" in blob and not name.startswith("assets/"):
            problems.append(f"{name}: CRLF line endings")
    if problems:
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1

    DIST.mkdir(exist_ok=True)
    out = DIST / f"{plugin}-{version}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, blob in sorted(files):
            info = zipfile.ZipInfo(name, date_time=FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, blob)

    skills = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
    size = out.stat().st_size
    print(out.relative_to(ROOT).as_posix())
    print(f"  {len(files)} files, {size:,} bytes ({size / 1024:.0f} KB)")
    print(f"  {len(skills)} skills: {', '.join(skills)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
