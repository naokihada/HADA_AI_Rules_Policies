# Character_Face_Reference_Image_Generation_Prompt

日本語の情報は、このページの下にあります。

HADA standard prompt package for character face reference image generation.

## Purpose

Generate a character reference sheet from an attached source image, prioritizing facial visual information to improve character reproducibility across generated images.

## What the Prompt Generates

A 16:9 character reference layout with one front full-body reference panel and four large face reference panels (front, 3/4, profile, low-angle), plus hair, eye, and skin color specifications derived from the attached image.

## Artifacts

| File | Role |
|------|------|
| [HADA_AI_Character_Face_Reference_Image_Generation_Prompt_JP.txt](HADA_AI_Character_Face_Reference_Image_Generation_Prompt_JP.txt) | Canonical artifact (JP) |
| [HADA_AI_Character_Face_Reference_Image_Generation_Prompt_JP.md](HADA_AI_Character_Face_Reference_Image_Generation_Prompt_JP.md) | Display/copy mirror (JP) |
| [HADA_AI_Character_Face_Reference_Image_Generation_Prompt_EN.txt](HADA_AI_Character_Face_Reference_Image_Generation_Prompt_EN.txt) | Canonical artifact (EN) |
| [HADA_AI_Character_Face_Reference_Image_Generation_Prompt_EN.md](HADA_AI_Character_Face_Reference_Image_Generation_Prompt_EN.md) | Display/copy mirror (EN) |

`.txt` files are the **canonical artifacts**. `.md` files are display/copy mirrors for GitHub viewing and copy-paste.

## Usage / Maintenance

- Edit canonical `.txt` when prompt changes are authorized.
- Run `python scripts/sync_prompt_to_readme.py` to update mirror managed regions.
- Run `python scripts/check_prompt_mirrors.py` to validate consistency.

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).

---
# 日本語

# Character_Face_Reference_Image_Generation_Prompt

キャラクター顔リファレンス画像生成用の HADA 標準プロンプトパッケージ。

## 目的

添付画像を基準に、顔の視覚情報を優先してキャラクター設定資料を生成し、生成画像におけるキャラクター再現性を高める。

## 生成内容

16:9 のキャラクター設定資料レイアウト。正面全身基準立ち絵 1 枚と、正面・3/4・側面・ローアングルの顔基準画像 4 枚（大型表示）、および添付画像から導出した髪色・瞳色・肌色の色指定。

## 成果物

| ファイル | 役割 |
|----------|------|
| [HADA_AI_Character_Face_Reference_Image_Generation_Prompt_JP.txt](HADA_AI_Character_Face_Reference_Image_Generation_Prompt_JP.txt) | 正規成果物（JP） |
| [HADA_AI_Character_Face_Reference_Image_Generation_Prompt_JP.md](HADA_AI_Character_Face_Reference_Image_Generation_Prompt_JP.md) | GitHub での表示・コピー用ミラー（JP） |
| [HADA_AI_Character_Face_Reference_Image_Generation_Prompt_EN.txt](HADA_AI_Character_Face_Reference_Image_Generation_Prompt_EN.txt) | 正規成果物（EN） |
| [HADA_AI_Character_Face_Reference_Image_Generation_Prompt_EN.md](HADA_AI_Character_Face_Reference_Image_Generation_Prompt_EN.md) | GitHub での表示・コピー用ミラー（EN） |

`.txt` ファイルは **正規成果物** である。`.md` ファイルは GitHub での閲覧およびコピー＆ペースト用のミラーである。

## 利用 / 保守

- プロンプト変更が許可された場合は正規 `.txt` を編集する。
- `python scripts/sync_prompt_to_readme.py` でミラーの managed region を更新する。
- `python scripts/check_prompt_mirrors.py` で整合性を検証する。

## ライセンス

Apache License, Version 2.0 の下でライセンス提供。詳細は [`LICENSE`](LICENSE) を参照。
