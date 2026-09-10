# HADA_AI_Rules_Policies

日本語の情報は、このページの下にあります。

Public repository for HADA AI rules, policies, prompts, and related tooling.

## Purpose

Reusable AI rules, policies, prompt packages, and deterministic maintenance scripts for public use.

## Directory Overview

| Path | Purpose |
|------|---------|
| [`prompts/`](prompts/) | Prompt packages (`.txt` = canonical; `.md` = display/copy mirror) |
| [`scripts/`](scripts/) | Deterministic validation and sync scripts |
| [`LICENSE`](LICENSE) | Apache License 2.0 |
| [`NOTICE`](NOTICE) | Project provenance pointer |

## Prompt Packages

Each package under `prompts/` is self-contained and copyable standalone.

- [`Prompt_Maintenance_Rules/`](prompts/Prompt_Maintenance_Rules/) — prompt maintenance rules (JP/EN)
- [`Coding_Agent_Operations_Maintenance_Policy/`](prompts/Coding_Agent_Operations_Maintenance_Policy/) — AI coding agent operations and maintenance policy (JP/EN)
- [`Character_Face_Reference_Image_Generation_Prompt/`](prompts/Character_Face_Reference_Image_Generation_Prompt/) — character face reference image generation prompt (JP/EN)
- [`Coding_Agent_Multi_Agent_Compatibility_Prompt/`](prompts/Coding_Agent_Multi_Agent_Compatibility_Prompt/) — coding agent multi-agent compatibility prompt (JP/EN)
- [`Existing_Project_SPEC_Reverse_Engineering_Prompt/`](prompts/Existing_Project_SPEC_Reverse_Engineering_Prompt/) — existing project SPEC reverse engineering prompt (JP/EN)
- [`GitHub_Release_Template_Upgrade_Prompt/`](prompts/GitHub_Release_Template_Upgrade_Prompt/) — GitHub release template upgrade prompt (JP/EN)

See [`prompts/README.md`](prompts/README.md) for structure and naming rules.

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).

Individual prompt packages may include their own `LICENSE` and `NOTICE` when distributed standalone.

---
# 日本語

# HADA_AI_Rules_Policies

HADA AI ルール、ポリシー、プロンプト、関連ツールの公開リポジトリ。

## 目的

公開利用向けの再利用可能な AI ルール、ポリシー、プロンプトパッケージ、および決定論的な保守スクリプト。

## ディレクトリ概要

| パス | 用途 |
|------|------|
| [`prompts/`](prompts/) | プロンプトパッケージ（`.txt` = 正規；`.md` = 表示・コピー用ミラー） |
| [`scripts/`](scripts/) | 決定論的な検証・同期スクリプト |
| [`LICENSE`](LICENSE) | Apache License 2.0 |
| [`NOTICE`](NOTICE) | プロジェクトの由来情報へのポインタ |

## プロンプトパッケージ

`prompts/` 配下の各パッケージは、自己完結型で単体コピー可能。

- [`Prompt_Maintenance_Rules/`](prompts/Prompt_Maintenance_Rules/) — プロンプト保守ルール（JP/EN）
- [`Coding_Agent_Operations_Maintenance_Policy/`](prompts/Coding_Agent_Operations_Maintenance_Policy/) — AI コーディングエージェント運用・保守ポリシー（JP/EN）
- [`Character_Face_Reference_Image_Generation_Prompt/`](prompts/Character_Face_Reference_Image_Generation_Prompt/) — キャラクター顔リファレンス画像生成プロンプト（JP/EN）
- [`Coding_Agent_Multi_Agent_Compatibility_Prompt/`](prompts/Coding_Agent_Multi_Agent_Compatibility_Prompt/) — コーディングエージェント多エージェント互換プロンプト（JP/EN）
- [`Existing_Project_SPEC_Reverse_Engineering_Prompt/`](prompts/Existing_Project_SPEC_Reverse_Engineering_Prompt/) — 既存プロジェクト SPEC 逆解析プロンプト（JP/EN）
- [`GitHub_Release_Template_Upgrade_Prompt/`](prompts/GitHub_Release_Template_Upgrade_Prompt/) — GitHub Release テンプレートアップグレードプロンプト（JP/EN）

構造および命名規則については [`prompts/README.md`](prompts/README.md) を参照。

## ライセンス

Apache License, Version 2.0 の下でライセンス提供。詳細は [`LICENSE`](LICENSE) を参照。

個別のプロンプトパッケージは、単体配布時に独自の `LICENSE` および `NOTICE` を含むことがある。
