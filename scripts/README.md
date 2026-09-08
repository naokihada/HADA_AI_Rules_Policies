# scripts

日本語の情報は、このページの下にあります。

Deterministic processing scripts for prompt maintenance.

AI agents perform semantic judgment (drafting, reviewing). This directory holds **deterministic, repeatable** tooling only.

## Scripts

| Script | Purpose |
|--------|---------|
| `sync_prompt_to_readme.py` | Sync `.txt` canonical prompt to `.md` display/copy mirror |
| `check_prompt_mirrors.py` | Validate `.txt` / `.md` mirror consistency within a package |

## Usage

```text
python scripts/check_prompt_mirrors.py
python scripts/sync_prompt_to_readme.py
python scripts/sync_prompt_to_readme.py --check
```

See [`prompts/README.md`](../prompts/README.md) for package layout rules.

---
# 日本語

# scripts

プロンプト保守向けの決定論的処理スクリプト。

AI エージェントは意味判断（起草、レビュー）を行う。このディレクトリは **決定論的で再現可能な** ツールのみを保持する。

## スクリプト

| スクリプト | 目的 |
|------------|------|
| `sync_prompt_to_readme.py` | 正規 `.txt` プロンプトを `.md` 表示・コピー用ミラーへ同期 |
| `check_prompt_mirrors.py` | パッケージ内の `.txt` / `.md` ミラー整合性を検証 |

## 使用方法

```text
python scripts/check_prompt_mirrors.py
python scripts/sync_prompt_to_readme.py
python scripts/sync_prompt_to_readme.py --check
```

パッケージ構成規則については [`prompts/README.md`](../prompts/README.md) を参照。
