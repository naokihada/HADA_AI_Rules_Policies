# Coding_Agent_Multi_Agent_Compatibility_Prompt

日本語の情報は、このページの下にあります。

HADA standard prompt package for migrating an existing project toward multi-agent coding agent compatibility.

## Purpose

Analyze a project built around a specific coding agent and restructure it so multiple coding agents (for example Cursor, Claude Code, OpenAI Codex, and other agents using project instruction files) can use the same project knowledge and rules safely and consistently.

## What the Prompt Does

Separates project specification, agent-independent project instructions, and agent-specific adapter configuration. Preserves existing project behavior while reducing single-agent dependency.

## Artifacts

| File | Role |
|------|------|
| [HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.txt](HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.txt) | Canonical artifact (JP) |
| [HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.md](HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.md) | Display/copy mirror (JP) |
| [HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.txt](HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.txt) | Canonical artifact (EN) |
| [HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.md](HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.md) | Display/copy mirror (EN) |

`.txt` files are the **canonical artifacts**. `.md` files are display/copy mirrors for GitHub viewing and copy-paste.

## Usage / Maintenance

- Edit canonical `.txt` when prompt changes are authorized.
- Run `python scripts/sync_prompt_to_readme.py` to update mirror managed regions.
- Run `python scripts/check_prompt_mirrors.py` to validate consistency.

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).

---
# 日本語

# Coding_Agent_Multi_Agent_Compatibility_Prompt

複数コーディングエージェント対応へ移行するための HADA 標準プロンプトパッケージ。

## 目的

特定のコーディングエージェントを前提とした既存プロジェクトを分析し、複数のコーディングエージェント（Cursor、Claude Code、OpenAI Codex、プロジェクト指示ファイルを利用するその他のエージェント等）が同一のプロジェクト知識とルールを安全かつ一貫して利用できる構造へ移行する。

## プロンプトの内容

プロジェクト仕様、エージェント非依存のプロジェクト指示、エージェント固有のアダプター設定を分離する。既存プロジェクトの動作を維持しつつ、単一エージェント依存を低減する。

## 成果物

| ファイル | 役割 |
|----------|------|
| [HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.txt](HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.txt) | 正規成果物（JP） |
| [HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.md](HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.md) | GitHub での表示・コピー用ミラー（JP） |
| [HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.txt](HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.txt) | 正規成果物（EN） |
| [HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.md](HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.md) | GitHub での表示・コピー用ミラー（EN） |

`.txt` ファイルは **正規成果物** である。`.md` ファイルは GitHub での閲覧およびコピー＆ペースト用のミラーである。

## 利用 / 保守

- プロンプト変更が許可された場合は正規 `.txt` を編集する。
- `python scripts/sync_prompt_to_readme.py` でミラーの managed region を更新する。
- `python scripts/check_prompt_mirrors.py` で整合性を検証する。

## ライセンス

Apache License, Version 2.0 の下でライセンス提供。詳細は [`LICENSE`](LICENSE) を参照。
