# Codex / AGENTS.md — nc-cubic2

> **Point scheme 研究の正本（2026-11-13）:** [uedakazushi/nc-cubic-point](https://github.com/uedakazushi/nc-cubic-point)。専用論文、証明節、研究ノート、計算器は移管済み。以下の旧記述に本repo内のpoint-schemeファイル名が現れる場合、移管先の同名パスを参照する。相対復元などの共有証明は必要な範囲で本repoにも保持する。

17次元非可換cubic moduli研究の正本は [nc-cubic-classification](https://github.com/uedakazushi/nc-cubic-classification)。主論文40頁・9入力・6本の厳密検算を独立再現し、専用15ファイルを移管した。共有の相対混合中心/Picard証明、中心対称性持上げ証明、対称性コードと証明書は本repoに保持する。既約成分性・generic reducedness・量子化の代数化と降下、全面的な証明・新規性監査は未了。




Cayley–Sklyanin研究の正本は [cayley-sklyanin](https://github.com/uedakazushi/cayley-sklyanin)、主論文は `papers/cayley-sklyanin.tex`（41頁）、中心曲面判別式の補助稿は3頁。両稿の全文組版・全頁描画とレイアウト確認、次数18の有理数Phi=0を含む必要検算を実行した。有限位数境界の正則性10個の定理・補題と完全な証明はnc-cubic-classificationの現行入力に保持する。共有検算 `verify_central_symmetry.py` は保持する。全面的な一次資料・新規性監査は未了。




Pfaffian–Brill–Noether研究の正本は [pfaffian-brill-noether](https://github.com/uedakazushi/pfaffian-brill-noether)。現行入口 `papers/pfaffian_brill_noether_technical.tex`、完全な証明と検算・研究方針を移管し、移管先で277頁の全文組版・全頁描画と表示概観、Schur/Tateの厳密検算を確認した。旧大型rank入力と一次文献の全面独立監査は未了。一般形式変形・Hesse比較・Picard/gluingを含む共有節 `papers/sections/pfaffian_formal_deformations_gluing.tex` は、混合形式比較の証明を保つため本repoにも内容を変更せず保持する。Pfaffian固有研究の正本は移管先とする。




**2026-11-13 / v9。再開時は `00_research_plan.md`、本 `AGENTS.md`、`notes/relative_reconstruction_models.md`、関連する現行TeXを最初に読む。** PDF由来の独立研究に取り組む場合だけ `CODEX_PDF_RECOVERY.md` と `PDF_SOURCES.md` を参照する。旧PDFや旧版の記録を再開の前提にしない。

## 独立成果の所在

論文Bから分離した相対理論・有限模型は `papers/relative_reconstruction_models.tex` と既存五稿に統合した。共有証明を複製せず、再現と移管の対応は `validation_reconstruction_manifest.json`・専用validation・`notes/relative_reconstruction_models.md` で確認する。

## moduli移管完了後の最優先タスク：公表向けの独立成果再構成

**移管は既に完了している。** `papers/relative_reconstruction_models.tex`（現行244頁）、独立五稿、`notes/relative_reconstruction_models.md`、`validation_reconstruction_manifest.json` を基礎として、**数学的重要性・新規性・理解・正確性・公表価値を最大化するように論文構成を再検討し、実際に改稿・検証・pushする**。固定の論文数・頁数は設定しない。機械的分割も244頁維持も目的ではない。

### 作業の順序と確認点

1. **重要な数学的監査を先に行う。** 移管時に文脈調整された9個の数学的環境を現行原稿とmanifestで特定し、元ソースコミット `ba7ec3422e53efc0f64f6d8280734296b98aacfe` と比較する。Artin比較、smoothness反例、Hochschild障害について、仮定・量化・証明・結論が弱化・強化・欠落していないか確かめる。特に全次数MF比較の存在と、同値を入力する条件付き移送、Artin上の完備化と代数化、相対smooth proper性を区別する。元コミットは証拠照合にのみ使い、旧版アーカイブを作らない。
2. **主結果の論理的なまとまりを判定する。** 41支持節と既存の点スキーム・Jacobian復元・一次変形・有限Artin・étale独立五稿の中心定理を照合する。候補の研究軸は、Artin/étale局所実現、Sklyanin/楕円多ブロック、MF/有限対角/bar/Morita、混合jet・相対proper模型・反例。これらは分割の義務ではない。重複定理の主張や同じ証明の二重全文掲載を避ける。必要なら独立した補助技術稿を維持する。
3. **公表用論文を執筆する。** 各論文の中心定理・必要仮定・従属結果を明確化し、日本語LuaLaTeXで、適切にdescriptiveな英語ファイル名を付ける。Introductionに関連一次文献、既知入力の適用条件と本研究の貢献を具体的に書く。出典や新規性の未確認点を推測で補わない。未解決の主張を完成定理として発表しない。研究ノートには現在有効な着想・反例・障害だけを残し、経緯・旧版対応表・重複の履歴を蓄積しない。
4. **完全性・再現性を検証する。** 公表価値のある定理・完全な証明・例・反例・再取得困難な入力・証明書を落とさない。各新稿の `\\input`・参照・引用を閉じ、`latexmk` で全文組版し、必要な厳密計算を再実行して出力を検証し、PDFを実際に表示確認する。完了前には現行統合稿や共有ソースを削除しない。最終的に正本を明確にし、検証済みの真の重複を整理する。
5. **現行の再開資料を更新してpushする。** `00_research_plan.md`、`notes/relative_reconstruction_models.md` と各稿の必要なvalidationを新しい正本・主張の状態・着手点へ更新する。成果ごとにGitHub `main` へ通常のfast-forward pushを行い、遠隔HEADとblobを確認する。計画を書くところで止まらない。

### 他担当との境界

**Chatは `uedakazushi/nc-cubic` の論文AのPoisson正規形・量子化、論文Bの完備MF比較・一般点降下、および両論文の一次文献・新規性の独立監査を担当する。** Codexは論文A/B、その再帰TeX入力・共通設定をこの担当で編集しない。問題を発見したら、正確な主張・仮定・反例候補・証明箇所を現行ノートに残し、Chat側へ引き継ぐ。移管済み142ファイルの再導入、PDF削除の再実施、単なる大規模ファイル移動はしない。既存の17次元モジュライと独立稿を保護する。Pfaffian専用成果は移管指示に従い、移管先の検証後にのみ移管元の真の重複を整理する。

現行統合稿の検証記録は244頁、54TeX入力、708ラベル、29有限検算だが、**全数学的証明の独立監査・新規性の確定ではない**。旧PDFのTeX移管とGit追跡解除は完了しており、`CODEX_PDF_RECOVERY.md` は必要な場合の参考指示であって現在の最優先業務ではない。

## 研究の守るべき原則

- **正確性・出典：** 定理の仮定、既知の入力、独自の寄与、証明の所在、独立監査の有無、厳密計算と経験的計算を区別する。旧原稿に定理と書いてあっても証明と依存を検査する。新しい主張には十分な証明を付ける。誤りを見つけたら依存先のabstract/Introduction/方針を含めて訂正する。先行研究は一次資料と適用範囲を確認し、未確認の書誌を作らない。
- **研究の改善：** 仮定の弱化、構造的な証明への置換、自然な一般化・系・応用、意味のある例や反例の追加を積極的に試す。数学的価値に従って論文の統合や分割を行い、旧版ごとの追記・歴史ログ・重複原稿を増やさない。重要な既存結果や証明は落とさない。
- **現在有効な記録：** 現行研究方針は `00_research_plan.md`、実際の独立成果は `papers/`、まだ論文に入れない重要な着想・障害は `notes/` に整理。論文にある証明をノートに全文重複させない。PDF固有の未移管内容と削除条件だけを `PDF_SOURCES.md` に反映する。
- **言語・再現：** 日本語LuaLaTeX、現行 `.latexmkrc`、`latexmk` を使用。コード・入力・有限証明書を最小限保持し、実行した範囲を正確に報告する。生成PDFと中間生成物は追跡しない。**有限体での等式の消滅を特性零での証明と混同しない。**
- **削除ゲート：** PDFにしか残っていない数学的価値を失わず、必要な証明・再現資産・書誌を現行TeXへ組み込み、参照・組版・計算を確認してから `git rm`。未解決の依存があるPDFは維持し、次の解決すべき数学を進める。
- **正本と保存：** `uedakazushi/nc-cubic2` のGitHub `main` が正本。変更前に最新状態を確認し、節目ごとに通常のfast-forward pushと遠隔headを検証する。force push、GitHub Actions、不要なPR、旧版ZIP、バックアップ・重複ファイルは作らない。Library保存はGitHub pushが失敗した場合の緊急避難のみ。研究bundleをLibraryに保存する一般許可はあるが、本研究ではこの具体的運用を優先する。

## 研究対象と他リポジトリとの境界

- **PDF研究**：中心商特異性、中心三次対の形式モジュライ、Pfaffian/Brill--Noether接触境界、中心三次の技術論、Sklyanin全混合量子化。詳細は `CODEX_PDF_RECOVERY.md`。
- **17次元非可換cubic threefoldモジュライ**：`https://github.com/uedakazushi/nc-cubic-classification/blob/main/papers/nc_cubic_threefold_moduli.tex` と `https://github.com/uedakazushi/nc-cubic-classification/blob/main/notes/research_notes.md`。ambient周期性と商イデアル保存を混同せず、有限係数17次元族とArtin局所の接空間次元20を混同しない。
- **一般次元Poisson構造・量子化**：正本は別リポジトリ `uedakazushi/nc-cubic` の論文A。必要証明を壊したり重複収録したりしない。
- **実務**：VS Code LaTeX Workshopは `.vscode/settings.json` でリポジトリrootを作業ディレクトリとして使用し、PDFと補助生成物は `build/` に出力。全てのTeXは必要に応じて親ファイルから入力する。

## 完了の意味

単なるTeXファイル追加は成果ではない。**主張と証明の質が高まり、旧PDFに唯一残る有用内容がなくなり、現行ソースから独立に理解・再生成できるようになったとき**に研究上の移管が完了する。未完成の計算、未読の固有節、監査不能な外部仮定が残る間はPDFを消さず、理由と次の着手を簡潔に示す。
