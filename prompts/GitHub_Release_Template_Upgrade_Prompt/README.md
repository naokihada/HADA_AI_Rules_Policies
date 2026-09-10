# GitHub_Release_Template_Upgrade_Prompt

日本語の情報は、このページの下にあります。

HADA standard prompt package for safely upgrading an existing project to a newer official GitHub Release template version.

## Purpose

Migrate an existing customized project to a newer template version using a three-way comparison model (previous template, current project, new template) while preserving user data, customizations, and project history.

## What the Prompt Does

Uses an official GitHub Release as the target template source, distinguishes template-owned changes from project-owned changes, applies only safe migrations automatically, and reports preserved items, applied changes, and items requiring human review.

## Artifacts

| File | Role |
|------|------|
| [HADA_AI_GitHub_Release_Template_Upgrade_Prompt_JP.txt](HADA_AI_GitHub_Release_Template_Upgrade_Prompt_JP.txt) | Canonical artifact (JP) |
| [HADA_AI_GitHub_Release_Template_Upgrade_Prompt_JP.md](HADA_AI_GitHub_Release_Template_Upgrade_Prompt_JP.md) | Display/copy mirror (JP) |
| [HADA_AI_GitHub_Release_Template_Upgrade_Prompt_EN.txt](HADA_AI_GitHub_Release_Template_Upgrade_Prompt_EN.txt) | Canonical artifact (EN) |
| [HADA_AI_GitHub_Release_Template_Upgrade_Prompt_EN.md](HADA_AI_GitHub_Release_Template_Upgrade_Prompt_EN.md) | Display/copy mirror (EN) |

`.txt` files are the **canonical artifacts**. `.md` files are display/copy mirrors for GitHub viewing and copy-paste.

## Usage / Maintenance

- Edit canonical `.txt` when prompt changes are authorized.
- Run `python scripts/sync_prompt_to_readme.py` to update mirror managed regions.
- Run `python scripts/check_prompt_mirrors.py` to validate consistency.

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).

---
# 日本語

# GitHub_Release_Template_Upgrade_Prompt

既存プロジェクトを新しい公式 GitHub Release テンプレートへ安全に移行するための HADA 標準プロンプトパッケージ。

## 目的

三者比較モデル（旧テンプレート、現行プロジェクト、新テンプレート）を用い、ユーザーデータ、カスタマイズ、プロジェクト履歴を保持しながら、既存プロジェクトを新しいテンプレート版へ移行する。

## プロンプトの内容

公式 GitHub Release をターゲットテンプレート源とし、テンプレート側の変更とプロジェクト側の変更を区別し、安全と判断できる変更のみを自動適用し、保持項目、適用変更、人間レビューが必要な項目を報告する。

## 成果物

| ファイル | 役割 |
|----------|------|
| [HADA_AI_GitHub_Release_Template_Upgrade_Prompt_JP.txt](HADA_AI_GitHub_Release_Template_Upgrade_Prompt_JP.txt) | 正規成果物（JP） |
| [HADA_AI_GitHub_Release_Template_Upgrade_Prompt_JP.md](HADA_AI_GitHub_Release_Template_Upgrade_Prompt_JP.md) | GitHub での表示・コピー用ミラー（JP） |
| [HADA_AI_GitHub_Release_Template_Upgrade_Prompt_EN.txt](HADA_AI_GitHub_Release_Template_Upgrade_Prompt_EN.txt) | 正規成果物（EN） |
| [HADA_AI_GitHub_Release_Template_Upgrade_Prompt_EN.md](HADA_AI_GitHub_Release_Template_Upgrade_Prompt_EN.md) | GitHub での表示・コピー用ミラー（EN） |

`.txt` ファイルは **正規成果物** である。`.md` ファイルは GitHub での閲覧およびコピー＆ペースト用のミラーである。

## 利用 / 保守

- プロンプト変更が許可された場合は正規 `.txt` を編集する。
- `python scripts/sync_prompt_to_readme.py` でミラーの managed region を更新する。
- `python scripts/check_prompt_mirrors.py` で整合性を検証する。

## ライセンス

Apache License, Version 2.0 の下でライセンス提供。詳細は [`LICENSE`](LICENSE) を参照。
