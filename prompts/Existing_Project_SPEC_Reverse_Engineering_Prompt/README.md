# Existing_Project_SPEC_Reverse_Engineering_Prompt

日本語の情報は、このページの下にあります。

HADA standard prompt package for reverse-engineering an existing project into a reimplementation-ready specification.

## Purpose

Inspect an existing software project and reconstruct a complete specification from the current implementation so another developer or AI coding agent can independently reimplement it.

## What the Prompt Does

Treats the current implementation as the primary source of truth, builds an independent reconstruction (ReSPEC) when an existing specification exists, compares evidence sources, and produces a specification focused on accuracy and reimplementation feasibility rather than documentation summary.

## Artifacts

| File | Role |
|------|------|
| [HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_JP.txt](HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_JP.txt) | Canonical artifact (JP) |
| [HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_JP.md](HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_JP.md) | Display/copy mirror (JP) |
| [HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_EN.txt](HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_EN.txt) | Canonical artifact (EN) |
| [HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_EN.md](HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_EN.md) | Display/copy mirror (EN) |

`.txt` files are the **canonical artifacts**. `.md` files are display/copy mirrors for GitHub viewing and copy-paste.

## Usage / Maintenance

- Edit canonical `.txt` when prompt changes are authorized.
- Run `python scripts/sync_prompt_to_readme.py` to update mirror managed regions.
- Run `python scripts/check_prompt_mirrors.py` to validate consistency.

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).

---
# 日本語

# Existing_Project_SPEC_Reverse_Engineering_Prompt

既存プロジェクトを再実装可能な仕様へ復元するための HADA 標準プロンプトパッケージ。

## 目的

既存ソフトウェアプロジェクトを調査し、現在の実装から完全な仕様書を復元する。別の開発者または AI コーディングエージェントが独立して再実装できる水準を目指す。

## プロンプトの内容

現在の実装を一次資料とし、既存仕様書がある場合は独立再構成（ReSPEC）を行い、証拠源を比較して、要約ではなく正確性と再実装可能性を重視した仕様を生成する。

## 成果物

| ファイル | 役割 |
|----------|------|
| [HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_JP.txt](HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_JP.txt) | 正規成果物（JP） |
| [HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_JP.md](HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_JP.md) | GitHub での表示・コピー用ミラー（JP） |
| [HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_EN.txt](HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_EN.txt) | 正規成果物（EN） |
| [HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_EN.md](HADA_AI_Existing_Project_SPEC_Reverse_Engineering_Prompt_EN.md) | GitHub での表示・コピー用ミラー（EN） |

`.txt` ファイルは **正規成果物** である。`.md` ファイルは GitHub での閲覧およびコピー＆ペースト用のミラーである。

## 利用 / 保守

- プロンプト変更が許可された場合は正規 `.txt` を編集する。
- `python scripts/sync_prompt_to_readme.py` でミラーの managed region を更新する。
- `python scripts/check_prompt_mirrors.py` で整合性を検証する。

## ライセンス

Apache License, Version 2.0 の下でライセンス提供。詳細は [`LICENSE`](LICENSE) を参照。
