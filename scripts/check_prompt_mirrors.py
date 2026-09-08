#!/usr/bin/env python3
"""Validate canonical .txt prompt artifacts against .md display/copy mirrors."""

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
class CheckError:
    package: str
    target: str
    reason: str


@dataclass
class CheckResult:
    packages_checked: int = 0
    pairs_checked: int = 0
    errors: list[CheckError] = field(default_factory=list)

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


def summarize_mismatch(expected: str, actual: str) -> str:
    if expected == actual:
        return "content matches"
    summary = f"length expected={len(expected)} actual={len(actual)}"
    min_len = min(len(expected), len(actual))
    for index in range(min_len):
        if expected[index] != actual[index]:
            line = expected[:index].count("\n") + 1
            return f"{summary}; first difference at line {line}, column {index - expected.rfind(chr(10), 0, index)}"
    return f"{summary}; one side is a prefix of the other"


def extract_managed_body(md_content: str, expected_txt_name: str) -> tuple[str | None, str | None]:
    begin_count = count_markers(md_content, BEGIN_MARKER)
    end_count = count_markers(md_content, END_MARKER)

    if begin_count == 0:
        return None, "BEGIN marker missing"
    if end_count == 0:
        return None, "END marker missing"
    if begin_count != 1:
        return None, f"BEGIN marker must appear exactly once (found {begin_count})"
    if end_count != 1:
        return None, f"END marker must appear exactly once (found {end_count})"

    begin_index = md_content.find(BEGIN_MARKER)
    end_index = md_content.find(END_MARKER)
    if begin_index > end_index:
        return None, "BEGIN marker appears after END marker"

    match = MANAGED_REGION_RE.search(md_content)
    if not match:
        return None, "malformed managed region or missing ```text code fence"

    referenced_name = match.group("filename")
    if referenced_name != expected_txt_name:
        return None, (
            f"BEGIN marker filename mismatch: expected '{expected_txt_name}', "
            f"found '{referenced_name}'"
        )

    return match.group("body"), None


def validate_txt_md_pair(package_name: str, txt_path: Path, md_path: Path) -> list[CheckError]:
    errors: list[CheckError] = []
    target = txt_path.name

    if not txt_path.exists():
        return [CheckError(package_name, target, "canonical .txt missing")]

    if not md_path.exists():
        return [CheckError(package_name, target, f"mirror .md missing: {md_path.name}")]

    try:
        txt_content = read_text(txt_path)
        md_content = read_text(md_path)
    except ValueError as exc:
        return [CheckError(package_name, target, str(exc))]

    body, parse_error = extract_managed_body(md_content, txt_path.name)
    if parse_error:
        return [CheckError(package_name, md_path.name, parse_error)]

    assert body is not None
    if body != txt_content:
        errors.append(
            CheckError(
                package_name,
                md_path.name,
                f"content mismatch ({summarize_mismatch(txt_content, body)})",
            )
        )

    return errors


def discover_packages(prompts_dir: Path) -> list[Path]:
    if not prompts_dir.is_dir():
        return []
    return sorted(path for path in prompts_dir.iterdir() if path.is_dir())


def validate_package(package_dir: Path) -> tuple[int, list[CheckError]]:
    package_name = package_dir.name
    errors: list[CheckError] = []
    pairs_checked = 0

    txt_files = sorted(
        path for path in package_dir.glob(CANONICAL_TXT_GLOB) if path.is_file()
    )

    for txt_path in txt_files:
        md_path = txt_path.with_suffix(".md")
        pairs_checked += 1
        errors.extend(validate_txt_md_pair(package_name, txt_path, md_path))

    for md_path in sorted(package_dir.glob("HADA_AI_*.md")):
        if not md_path.is_file():
            continue
        try:
            md_content = read_text(md_path)
        except ValueError as exc:
            errors.append(CheckError(package_name, md_path.name, str(exc)))
            continue

        if BEGIN_MARKER not in md_content:
            continue

        begin_count = count_markers(md_content, BEGIN_MARKER)
        if begin_count != 1:
            errors.append(
                CheckError(
                    package_name,
                    md_path.name,
                    f"BEGIN marker must appear exactly once (found {begin_count})",
                )
            )
            continue

        match = re.search(rf"{re.escape(BEGIN_MARKER)} (\S+) -->", md_content)
        if not match:
            errors.append(CheckError(package_name, md_path.name, "malformed BEGIN marker"))
            continue

        referenced_txt = package_dir / match.group(1)
        if not referenced_txt.exists():
            errors.append(
                CheckError(
                    package_name,
                    md_path.name,
                    f"referenced canonical .txt missing: {match.group(1)}",
                )
            )

    return pairs_checked, errors


def validate_prompts(prompts_dir: Path) -> CheckResult:
    result = CheckResult()

    if not prompts_dir.is_dir():
        result.errors.append(
            CheckError("", str(prompts_dir), "prompts directory not found")
        )
        return result

    for package_dir in discover_packages(prompts_dir):
        result.packages_checked += 1
        pairs_checked, errors = validate_package(package_dir)
        result.pairs_checked += pairs_checked
        result.errors.extend(errors)

    return result


def default_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate canonical .txt prompts against .md managed-region mirrors."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root containing prompts/ (default: parent of scripts/)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = args.root.resolve() if args.root else default_repo_root()
    prompts_dir = repo_root / "prompts"

    result = validate_prompts(prompts_dir)

    if result.ok:
        print(
            "PASS: "
            f"packages={result.packages_checked} "
            f"pairs={result.pairs_checked}"
        )
        return 0

    print("FAIL: prompt mirror validation failed", file=sys.stderr)
    for error in result.errors:
        print(
            f"  package={error.package} target={error.target} reason={error.reason}",
            file=sys.stderr,
        )
    return 1


if __name__ == "__main__":
    sys.exit(main())
