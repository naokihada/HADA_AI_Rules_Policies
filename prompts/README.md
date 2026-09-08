# prompts

日本語の情報は、このページの下にあります。

Parent directory for prompt and policy packages.

## Role

- **Canonical content:** `.txt` files (authoritative prompt artifact)
- **Display/copy mirror:** `.md` files (for GitHub viewing and copy-paste)
- **Package metadata:** `README.md`, `LICENSE`, `NOTICE` per package

Version is managed **inside prompt body text**, not in filenames.

## Package Layout

Each prompt package is a self-contained directory, copyable standalone:

```
Prompt_Name/
├── LICENSE
├── NOTICE
├── README.md
├── HADA_AI_Prompt_JP_xxx.txt   # Canonical (JP)
├── HADA_AI_Prompt_JP_xxx.md    # Mirror (JP)
├── HADA_AI_Prompt_EN_xxx.txt   # Canonical (EN)
└── HADA_AI_Prompt_EN_xxx.md    # Mirror (EN)
```

## Packages

- [`Prompt_Maintenance_Rules/`](Prompt_Maintenance_Rules/) — prompt maintenance rules (JP/EN)

Conventions: see Package Layout above.

Deterministic sync and validation: [`scripts/`](../scripts/)

---
# 日本語

# prompts

プロンプトおよびポリシーパッケージの親ディレクトリ。

## 役割

- **正規コンテンツ:** `.txt` ファイル（権威あるプロンプト成果物）
- **表示・コピー用ミラー:** `.md` ファイル（GitHub での閲覧およびコピー＆ペースト用）
- **パッケージメタデータ:** 各パッケージの `README.md`、`LICENSE`、`NOTICE`

バージョンは **プロンプト本文内** で管理され、ファイル名では管理しない。

## パッケージ構成

各プロンプトパッケージは自己完結型のディレクトリであり、単体でコピー可能:

```
Prompt_Name/
├── LICENSE
├── NOTICE
├── README.md
├── HADA_AI_Prompt_JP_xxx.txt   # 正規（JP）
├── HADA_AI_Prompt_JP_xxx.md    # ミラー（JP）
├── HADA_AI_Prompt_EN_xxx.txt   # 正規（EN）
└── HADA_AI_Prompt_EN_xxx.md    # ミラー（EN）
```

## パッケージ

- [`Prompt_Maintenance_Rules/`](Prompt_Maintenance_Rules/) — プロンプト保守ルール（JP/EN）

規約: 上記 Package Layout を参照。

決定論的な同期および検証: [`scripts/`](../scripts/)
