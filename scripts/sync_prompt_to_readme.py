#!/usr/bin/env python3
"""Sync canonical .txt prompt artifacts into .md managed-region mirrors."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ENCODING = "utf-8"

BEGIN_MARKER = "<!-- BEGIN HADA_AI_PROMPT:"
END_MARKER = "<!-- END HADA_AI_PROMPT -->"
CANONICAL_TXT_GLOB = "HADA_AI_*.txt"
MANAGED_REGION_RE = re.compile(
    rf"{re.escape(BEGIN_MARKER)} (?P<filename>\S+) -->\n```text\n(?P<body>.*?)```\n{re.escape(END_MARKER)}",
    re.DOTALL,
)


@dataclass
class SyncError:
    package: str
    target: str
    reason: str


@dataclass
class SyncResult:
    packages_checked: int = 0
    pairs_checked: int = 0
    updated: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    errors: list[SyncError] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding=ENCODING)
    except UnicodeDecodeError as exc:
        raise ValueError(f"UTF-8 decode error: {exc}") from exc
    except OSError as exc:
        raise ValueError(f"read error: {exc}") from exc


def count_markers(content: str, marker: str) -> int:
    return content.count(marker)


def validate_managed_region(md_content: str, expected_txt_name: str) -> str | None:
    begin_count = count_markers(md_content, BEGIN_MARKER)
    end_count = count_markers(md_content, END_MARKER)

    if begin_count == 0:
        return "BEGIN marker missing"
    if end_count == 0:
        return "END marker missing"
    if begin_count != 1:
        return f"BEGIN marker must appear exactly once (found {begin_count})"
    if end_count != 1:
        return f"END marker must appear exactly once (found {end_count})"

    begin_index = md_content.find(BEGIN_MARKER)
    end_index = md_content.find(END_MARKER)
    if begin_index > end_index:
        return "BEGIN marker appears after END marker"

    match = MANAGED_REGION_RE.search(md_content)
    if not match:
        return "malformed managed region or missing ```text code fence"

    if match.group("filename") != expected_txt_name:
        return (
            f"BEGIN marker filename mismatch: expected '{expected_txt_name}', "
            f"found '{match.group('filename')}'"
        )

    return None


def replace_managed_body(md_content: str, txt_content: str) -> str:
    match = MANAGED_REGION_RE.search(md_content)
    if not match:
        raise ValueError("managed region not found")

    body_start = match.start("body")
    body_end = match.end("body")
    return md_content[:body_start] + txt_content + md_content[body_end:]


def discover_packages(prompts_dir: Path) -> list[Path]:
    if not prompts_dir.is_dir():
        return []
    return sorted(path for path in prompts_dir.iterdir() if path.is_dir())


def sync_txt_md_pair(
    package_name: str,
    txt_path: Path,
    md_path: Path,
    dry_run: bool,
) -> tuple[str, SyncError | None]:
    target = f"{package_name}/{md_path.name}"
    rel_txt = txt_path.name

    if not md_path.exists():
        return "error", SyncError(package_name, rel_txt, f"mirror .md missing: {md_path.name}")

    try:
        txt_content = read_text(txt_path)
        md_content = read_text(md_path)
    except ValueError as exc:
        return "error", SyncError(package_name, rel_txt, str(exc))

    region_error = validate_managed_region(md_content, txt_path.name)
    if region_error:
        return "error", SyncError(package_name, md_path.name, region_error)

    current_body = MANAGED_REGION_RE.search(md_content)
    assert current_body is not None
    if current_body.group("body") == txt_content:
        return "skipped", None

    new_md_content = replace_managed_body(md_content, txt_content)
    if not dry_run:
        md_path.write_text(new_md_content, encoding=ENCODING)

    return "updated", None


def sync_package(package_dir: Path, dry_run: bool) -> tuple[int, list[str], list[str], list[SyncError]]:
    package_name = package_dir.name
    updated: list[str] = []
    skipped: list[str] = []
    errors: list[SyncError] = []
    pairs_checked = 0

    txt_files = sorted(
        path for path in package_dir.glob(CANONICAL_TXT_GLOB) if path.is_file()
    )

    for txt_path in txt_files:
        md_path = txt_path.with_suffix(".md")
        pairs_checked += 1
        status, error = sync_txt_md_pair(package_name, txt_path, md_path, dry_run)
        target = f"{package_name}/{md_path.name}"

        if error:
            errors.append(error)
        elif status == "updated":
            updated.append(target)
        else:
            skipped.append(target)

    return pairs_checked, updated, skipped, errors


def sync_prompts(prompts_dir: Path, dry_run: bool) -> SyncResult:
    result = SyncResult()

    if not prompts_dir.is_dir():
        result.errors.append(
            SyncError("", str(prompts_dir), "prompts directory not found")
        )
        return result

    for package_dir in discover_packages(prompts_dir):
        result.packages_checked += 1
        pairs_checked, updated, skipped, errors = sync_package(package_dir, dry_run)
        result.pairs_checked += pairs_checked
        result.updated.extend(updated)
        result.skipped.extend(skipped)
        result.errors.extend(errors)

    return result


def default_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync canonical .txt prompts into .md managed-region mirrors."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root containing prompts/ (default: parent of scripts/)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Dry run: report planned updates without modifying files",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = args.root.resolve() if args.root else default_repo_root()
    prompts_dir = repo_root / "prompts"
    dry_run = args.check

    result = sync_prompts(prompts_dir, dry_run=dry_run)

    if not result.ok:
        print("FAIL: prompt mirror sync failed", file=sys.stderr)
        for error in result.errors:
            print(
                f"  package={error.package} target={error.target} reason={error.reason}",
                file=sys.stderr,
            )
        return 1

    mode = "CHECK" if dry_run else "SYNC"
    print(
        f"{mode}: packages={result.packages_checked} "
        f"pairs={result.pairs_checked} "
        f"updated={len(result.updated)} "
        f"skipped={len(result.skipped)}"
    )
    for target in result.updated:
        action = "would update" if dry_run else "updated"
        print(f"  {action}: {target}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
