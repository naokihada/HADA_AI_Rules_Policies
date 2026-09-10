<!-- BEGIN HADA_AI_PROMPT: HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.txt -->
```text
// HADA AI コーディングエージェント複数対応化プロンプト Ver.1.0.1.20260909
// (C) Hada | HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_JP.txt

[目的]
特定のコーディングエージェントを前提に構築された既存プロジェクトを分析し、複数のコーディングエージェントから安全かつ一貫して利用できる構造へ移行する。対象:Cursor,Claude Code,OpenAI Codex,AGENTS.md等のプロジェクト指示ファイルを利用するその他のエージェント。目的は特定エージェント設定の削除ではなく、「プロジェクト固有の知識・開発ルール」と「エージェント固有の設定・操作方法」を分離し、複数エージェントが同じプロジェクトの意図・仕様・制約を理解できる状態にする。

[基本原則]
既存プロジェクトの動作を壊さない,既存仕様・設計・開発ルールを変更しない,特定エージェント固有情報と共通情報を分離,共通情報は可能な限りエージェント非依存形式で保存,エージェント固有設定は必要な場合のみアダプターとして残す,同一情報を複数箇所へ重複記述しない,既存ファイルを機械的に統合・上書きしない,不明な仕様を推測しない,作業範囲を拡大しない,変更後は元プロジェクトと比較し意図しない変更がないことを確認する。重要:「Cursor対応を削除して別エージェント対応にする」のではなく「Cursorを含む複数エージェントが同じプロジェクト情報を共有できる構造にする」。

[エージェント非依存の基本構造]
原則として3層に分離する。

[Layer 1 — Project Specification]
プロジェクトそのものの仕様。目的,要件,アーキテクチャ,ディレクトリ構造,データ構造,API仕様,ビルド方法,テスト仕様,入出力,設計上の不変条件,セキュリティ要件,正しい実装状態,リリース条件。特定エージェント用情報ではなく、可能な限りSPEC.md等のエージェント非依存ファイルに整理する。

[Layer 2 — Agent-Independent Project Instructions]
AIコーディングエージェントが作業時に守る共通ルール。作業範囲,編集禁止領域,実装ルール,テストルール,Gitルール,セキュリティルール,作業前後の確認,変更範囲,停止条件,人間による承認が必要な操作,完了条件,レポート方法。原則AGENTS.md等に整理し、「どのエージェントを使うか」ではなく「AIエージェントがこのプロジェクトでどう行動するか」を記述する。

[Layer 3 — Agent-Specific Adapter]
特定エージェントのみが必要とする設定。`.cursor/`,Cursor Rules,Claude Code固有設定,Codex固有設定,その他エージェント固有設定。プロジェクト本質の仕様を保持する場所ではなく、必要に応じLayer 1/2を参照する薄いアダプターとして使用する。共通情報を各エージェント用ファイルへコピーしない。

[最初に行うこと]
変更前に既存プロジェクトを調査し、最初からファイルを書き換えない。

[プロジェクト構造]
確認対象:ルートディレクトリ,ソースコード,設定,テスト,ドキュメント,CI/CD,ビルド,スクリプト,AI関連ファイル,Git設定,エージェント固有設定。

[AI / Coding Agent 関連ファイル]
探索対象:AGENTS.md,CLAUDE.md,.cursor/,.cursor/rules/,Cursor Rules,Codex関連設定,Claude Code関連設定,README内のAI向け指示,その他AIエージェント用指示ファイル,AI用プロンプト,開発ルール,作業手順,自動化スクリプト。

[Git状態]
作業開始前にbranch,HEAD,uncommitted changes,staged changes,untracked filesを確認する。既存変更を自分の変更と判断しない。既存変更を削除,reset,restore,rebase等で失わない。

[現在のエージェント依存状態を分析]
プロジェクト内のAI関連情報をProject Specification,Project-wide Agent Instruction,Agent-specific Instruction,Temporary Task Information,Historical Information,Redundant Informationに分類する。Cursor固有ルール内にプロジェクト仕様が混在していないか確認する。Cursor Rulesにプロジェクトの重要な設計ルール,コーディング規約,テスト条件,セキュリティ制約,ディレクトリ構造,Git運用,禁止事項,完了条件等が存在する場合は単純削除せず、プロジェクト共通情報として抽出する。

[情報の移動ルール]
既存情報を移動するときは意味を変えない。「移動」は「再設計」ではない。既存ルールの意味を保ったまま適切な層へ移動する。例:Cursor Rule「実装前にテストを確認し、変更後に全テストを実行する」→AGENTS.mdへ同義の共通ルールとして移動。一方「Cursorではこの画面からRuleを確認する」のような操作方法はCursor固有情報として残す。

[AGENTS.mdの役割]
可能な限り複数エージェントが利用できる共通プロジェクト指示書として設計する。必要に応じProject Purpose,Scope,Architecture Overview,Important Directories,Implementation Rules,Safety Rules,Testing Rules,Validation Rules,Git Rules,Stop Conditions,Human Approval Conditions,Completion Conditions,Reporting Requirementsを含める。ただしプロジェクト仕様のすべてを重複記載しない。詳細仕様がSPEC.mdにある場合は参照する。

[SPEC.mdの役割]
存在する場合は内容を尊重する。「AIに作業方法を教えるファイル」ではなく「このプロジェクトが正しく存在するための仕様」として扱い、仕様とAI運用ルールを混在させない。存在しない場合、必要性を分析せず勝手に作成しない。仕様再構成が必要ならユーザー承認が必要な変更として扱う。

[Cursor固有情報の扱い]
既存`.cursor/`を無条件に削除しない。内容を調査して分類する。
A. Project-common:複数エージェントで共有すべき情報→AGENTS.md/SPEC.md/その他適切な共通ファイルへ移行。
B. Cursor-specific:Cursorのみで必要→`.cursor/`に残す。
C. Redundant:共通ファイルへ移行済みの重複情報→既存動作への影響を確認してから削除候補とする。
D. Unknown:意味・用途不明→推測削除せず必要に応じ`REVIEW_REQUIRED`とする。

[他エージェントへの対応]
複数エージェント対応時も特定エージェントの完全な設定を無理に統一しない。例:
Project
├── SPEC.md
├── AGENTS.md
├── README.md
├── .cursor/
│   └── ...
├── .claude/
│   └── ...
└── その他のAgent Adapter
共通情報→Agent-independent files、エージェント固有設定→Agent-specific adaptersの依存関係にする。共通情報をCursorだけに依存させない。

[エージェント固有ファイルを作る場合]
新しいエージェント用設定を作成する前に共通情報の存在を確認する。共通情報があれば参照し、同じルールを複数ファイルへコピーしない。共通ルールのSingle Source of Truthを維持する。

[README.mdの扱い]
README.mdは通常ユーザー・開発者向けドキュメントとする。AI専用の詳細な作業ルールを大量に追加しない。プロジェクト利用に必要な基本情報は残す。例:プロジェクト概要,Installation,Usage,Build,Test,Contribution,License。AI向け情報は必要に応じAGENTS.md/SPEC.mdを参照する。

[作業範囲]
明示目的以外を変更しない。禁止:大規模リファクタリング,コード品質改善,依存ライブラリ更新,ファイル名変更,ディレクトリ構造再設計,README全面改稿,CI/CD変更,Git履歴変更,不要な設定削除,将来機能追加。複数エージェント対応に不要な変更は行わない。

[既存動作の保護]
原則として「AI運用構造の変更」でありアプリケーション機能変更ではない。source code,runtime behavior,API behavior,UI behavior,data format,build output等を変更する必要がない場合は変更しない。変更が必要になった場合は理由を明示し、作業を停止して確認する。

[変更前のBaseline]
可能な限りGit status,Git branch,HEAD,テスト結果,Build結果,Validator結果,AI関連ファイル一覧,重要な設定ファイル,プロジェクト構造を記録する。既存テストがある場合は変更前に実行することを優先する。

[実装]
分析と計画完了後に変更する。変更は最小限にする。優先順位:1.共通情報を識別 2.共通情報を適切な場所へ整理 3.エージェント固有情報をアダプターとして整理 4.不要な重複を最小限に整理 5.既存動作を検証。一度に大量のファイルを書き換えない。

[検証]
[Structure]共通ルールが特定エージェントだけに依存していないか,Agent-specific filesが適切に分離されているか,重複が増えていないか。
[Consistency]AGENTS.mdとSPEC.mdに矛盾がないか,Agent adapterと共通ルールに矛盾がないか,READMEとの重大な矛盾がないか。
[Project Tests]既存テストを実行する。
[Build]既存Build手順がある場合は実行する。
[Git Diff]必ず変更差分を確認し、想定外のファイル変更,ソースコード変更,不要な改行変更,不要なフォーマット変更,不要なファイル移動,不要な削除がないことを確認する。

[複数エージェントでの確認]
可能なら複数エージェントからプロジェクト情報を認識できることを確認する。確認対象:Project purpose,Important constraints,Architecture,Implementation rules,Testing rules,Git rules,Stop conditions。ただし各エージェントの完全な動作を無理に自動検証しない。検証困難な場合はその事実をレポートする。

[停止条件]
以下の場合は推測で進めず停止する:既存ルールの意味が不明,同一ルールが複数箇所で矛盾,SPECと実装が大きく矛盾,Cursor固有か共通ルールか判断不能,削除で既存動作へ影響する可能性,大規模ファイル変更が必要,source code変更が必要,セキュリティ上の問題を発見,credentials / secretsを発見,Git履歴変更が必要,production環境変更が必要,ユーザー意図の確認なしでは安全に判断できない。この場合`REVIEW_REQUIRED`として停止する。

[Git操作]
変更前後でGit状態を確認する。特にreset,restore,checkoutによる変更破棄,rebase,force push,branch削除等、既存変更や履歴に影響する操作はユーザーの明示的承認なしに実行しない。commit/pushはプロジェクトのGit運用ルールに従い、明示的に許可されていない場合は自動実行しない。

[完了条件]
共通情報とエージェント固有情報が適切に分離されている,既存仕様の意味を意図せず変更していない,既存プロジェクトの機能を変更していない,不要な重複を増やしていない,必要なAgent adapterが整理されている,テストがPASSまたは既存テストなしを確認,BuildがPASSまたはBuild不要を確認,Git diffを確認,作業範囲外の変更がない,未解決事項を明示している。

[レポート]
完了時は長大な実行ログを出力せず要点のみ報告する。
[STATUS]
COMPLETE / REVIEW_REQUIRED / BLOCKED / FAILED
[ANALYSIS]
既存プロジェクトのエージェント依存状態の概要
[CHANGED]
変更したファイルと変更内容
[COMMON]
共通情報として整理した内容
[AGENT_SPECIFIC]
エージェント固有情報として残した内容
[TEST]
テスト結果
[BUILD]
Build結果
[DIFF]
変更範囲の確認結果
[ISSUES]
未解決事項
[NEXT]
次に必要な作業

[最終原則]
目的は「すべてのコーディングエージェントを同じものにする」ことではなく、「プロジェクトの知識とルールを特定のコーディングエージェントから独立させる」ことである。プロジェクトの本質はAgent-independentとし、Cursor,Claude Code,Codex,その他のエージェントは異なるインターフェースとして扱う。
Project Specification
↓
Agent-Independent Project Rules
↓
Agent-Specific Adapters
↓
Individual Coding Agent
という依存関係を基本とする。逆に、
Project
↓
Cursor Rules
↓
Other Agents
という単一エージェント依存構造を作らない。既存プロジェクトの価値を維持し、将来エージェントが変わってもプロジェクトの知識・仕様・運用ルールを継続利用できる状態を最終目標とする。
```
<!-- END HADA_AI_PROMPT -->
