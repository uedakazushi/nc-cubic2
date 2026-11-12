# Codex / AGENTS.md — nc-cubic2

**2026-11-13 / v7。Codexは最初に `00_research_plan.md`、続いて `CODEX_PDF_RECOVERY.md` と `PDF_SOURCES.md` を読む。** 研究の現行詳細は `notes/research_notes.md` と各論文のTeXにある。古い会話や旧PDFだけを再開の前提にしない。

## 独立成果の所在

論文Bから分離した相対理論・有限模型は `papers/relative_reconstruction_models.tex` と既存五稿に統合した。共有証明を複製せず、再現と移管の対応は `validation_reconstruction_manifest.json`・専用validation・`notes/relative_reconstruction_models.md` で確認する。

## 現在の最優先タスク

原PDFの全移管は完了し、Git追跡PDFは0件。今後は現行TeXと再生成可能な計算を正本として、**必要なら新しい研究成果を加え、より重要で厳密かつ理解しやすい論文へ発展させる**こと。**単純なPDF→TeXの逐語変換、ページ数合わせ、PDF削除数の最大化は目的ではない。**

完全な具体的手順、研究主題ごとの数学的課題、検証と削除の条件は **`CODEX_PDF_RECOVERY.md`** に定める。短い計画だけで止まらず、可能な限り証明・計算・執筆・実際のpushまで進める。数学的重要性、先行研究、新規性、理解の深化、応用可能性、正確性、実現可能性を考えて研究方針を柔軟に調整する。

中心商特異性（旧VI）の全22節は現行TeXと厳密検算へ統合済み。原PDFは追跡解除済み。中心三次対（旧V）の全21節もTeXと厳密検算に統合済み。Pfaffian接触境界と中心三次技術稿も固有証明を回収して追跡解除済み。全混合量子化（旧II、195頁）も有限gauge・四次計算・平面切断幾何を回収して追跡解除済み。削除判定の全対応表は `PDF_SOURCES.md` にある。

## nc-cubicからの独立成果移管：並行作業の優先境界

**2026-11-13 の移管担当Codexセッションでは、上記の一般的な新研究課題に先立ち、`uedakazushi/nc-cubic/AGENTS.md` と `notes/paper_b_scope_and_transfer.md` を読み、論文Bから分離した独立成果の移管・統合を優先する。** これは既存の17次元モジュライ研究などを廃止する意味ではない。Chat側が `nc-cubic` 論文A・Bの独立監査・改良・先行研究調査を進めているので、Codexはそれらの本文・依存ファイルに手を付けない。

現行の受け皿は `papers/mixed_cubic_point_schemes.tex`、`papers/cubic_jacobian_recovery.tex`、`papers/cubic_first_order_deformations.tex`、`papers/cubic_artin_windows.tex`、`papers/relative_cubic_realization.tex` である。すでに移管・整理済みの成果を重複生成しない。未完了なのは形式・étale・Artinの残存参照閉包、Sklyanin/多ブロック、対角/bar/Morita、混合・jetなど。既存の独立稿に統合できるものは統合し、別稿にすべきものは中心結果・論理のまとまり・投稿価値から判断する。

**引き継ぎの完了条件：** 主張の仮定・証明・反例・文献・検算資産を保持し、TeX入力/参照/引用閉包と必要なLuaLaTeX組版・有限検算を実行して成否を明記した上で、まず本リポジトリ `main` へ通常pushし遠隔HEAD/blobを確認する。これが完了する前に移管元のソースを消してはいけない。移管元のA/Bが読むファイルや別の未移管原稿が参照するファイルも消してはいけない。旧版ZIP・移管対応一覧・作業ログを増やさず、現行原稿、研究ノート、簡潔な検証情報を更新する。両repoとも他作業者の変更を上書きせず、force push・Actionsを禁止する。

## 研究の守るべき原則

- **正確性・出典：** 定理の仮定、既知の入力、独自の寄与、証明の所在、独立監査の有無、厳密計算と経験的計算を区別する。旧原稿に定理と書いてあっても証明と依存を検査する。新しい主張には十分な証明を付ける。誤りを見つけたら依存先のabstract/Introduction/方針を含めて訂正する。先行研究は一次資料と適用範囲を確認し、未確認の書誌を作らない。
- **研究の改善：** 仮定の弱化、構造的な証明への置換、自然な一般化・系・応用、意味のある例や反例の追加を積極的に試す。数学的価値に従って論文の統合や分割を行い、旧版ごとの追記・歴史ログ・重複原稿を増やさない。重要な既存結果や証明は落とさない。
- **現在有効な記録：** 現行研究方針は `00_research_plan.md`、実際の独立成果は `papers/`、まだ論文に入れない重要な着想・障害は `notes/` に整理。論文にある証明をノートに全文重複させない。PDF固有の未移管内容と削除条件だけを `PDF_SOURCES.md` に反映する。
- **言語・再現：** 日本語LuaLaTeX、現行 `.latexmkrc`、`latexmk` を使用。コード・入力・有限証明書を最小限保持し、実行した範囲を正確に報告する。生成PDFと中間生成物は追跡しない。**有限体での等式の消滅を特性零での証明と混同しない。**
- **削除ゲート：** PDFにしか残っていない数学的価値を失わず、必要な証明・再現資産・書誌を現行TeXへ組み込み、参照・組版・計算を確認してから `git rm`。未解決の依存があるPDFは維持し、次の解決すべき数学を進める。
- **正本と保存：** `uedakazushi/nc-cubic2` のGitHub `main` が正本。変更前に最新状態を確認し、節目ごとに通常のfast-forward pushと遠隔headを検証する。force push、GitHub Actions、不要なPR、旧版ZIP、バックアップ・重複ファイルは作らない。Library保存はGitHub pushが失敗した場合の緊急避難のみ。研究bundleをLibraryに保存する一般許可はあるが、本研究ではこの具体的運用を優先する。

## 研究対象と他リポジトリとの境界

- **PDF研究**：中心商特異性、中心三次対の形式モジュライ、Pfaffian/Brill--Noether接触境界、中心三次の技術論、Sklyanin全混合量子化。詳細は `CODEX_PDF_RECOVERY.md`。
- **17次元非可換cubic threefoldモジュライ**：`papers/nc_cubic_threefold_moduli.tex` と `notes/nc_cubic_threefold_moduli.md`。ambient周期性と商イデアル保存を混同せず、有限係数17次元族とArtin局所の接空間次元20を混同しない。
- **Poisson cubic fourfoldのscheme構造・6/7次元固有の退化幾何**：各対応原稿と研究ノートを参照。一般次元のPoisson成分分類・量子化・ambient復元・rotation付き可換復元の正本は別リポジトリ `uedakazushi/nc-cubic` の論文A/Bである。既存証明を壊したり同じ一般定理を無用に重複収録したりしない。
- **実務**：VS Code LaTeX Workshopは `.vscode/settings.json` でリポジトリrootを作業ディレクトリとして使用し、PDFと補助生成物は `build/` に出力。全てのTeXは必要に応じて親ファイルから入力する。

## 完了の意味

単なるTeXファイル追加は成果ではない。**主張と証明の質が高まり、旧PDFに唯一残る有用内容がなくなり、現行ソースから独立に理解・再生成できるようになったとき**に研究上の移管が完了する。未完成の計算、未読の固有節、監査不能な外部仮定が残る間はPDFを消さず、理由と次の着手を簡潔に示す。
