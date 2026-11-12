# nc-cubic2：非可換cubicの独立境界・モジュライ研究

## Codexへの現在の研究指示

**[CODEX_PDF_RECOVERY.md](CODEX_PDF_RECOVERY.md)** に、残るpdf-onlyの研究・TeX統合・独立検証・Git追跡解除の手順を定めた。単なるPDFの転記ではなく、重要な定理を強め、証明を洗練し、必要なら新しい結果・一般化・応用を加える。実行前に [研究方針](00_research_plan.md)、[AGENTS.md](AGENTS.md)、[現行のPDF別状態](PDF_SOURCES.md) を読む。数学的成果と再現性を犠牲にしてPDFを削除しない。

## nc cubic threefoldの17次元モジュライ（現行の主題）

- [現行草稿](papers/nc_cubic_threefold_moduli.tex)：41次元中心三次対、17係数横断形、分離型余次元15、忘却核7（6+1）、混合中心と相対Picard障害。
- [研究ノート](notes/nc_cubic_threefold_moduli.md)：仮定・未解決の既約成分性・再現手順。
- 再現コード：`computations/independent/verify_generic17_slice.py`、`verify_generic17_center.py`、`computations/verify_split_codimension.py`。
- 一般次元ambient復元の定理と証明は `nc-cubic/papers/paper_a.tex`、本稿には同型類判定に必要な証明も保持する。
- **正則正規三次族からの1周期性**：一般$N,d$について最小周期が$\gcd(N,d)$を割る定理と5次元・三次の場合の系を、モジュライ原稿の [周期性節](papers/sections/ambient_periodicity.tex) に証明ごと統合。ambientの1周期性と、商イデアルを保つ周期性を区別する。後者と初出・新規性の確定は未了。
- 構成した17次元族がnc cubic moduli stackの既約成分であることはまだ未証明。

**2026年11月12日・v13。独立した研究内容の正本は本リポジトリの `main`。**

## 六・七次元Poisson cubicの独立なscheme幾何

論文Aの一般次元の主定理に不要な、n=6,7の退化スキーム・
primary分解・Calabi--Yau完全交叉の数値計算を、
[独立LuaLaTeX草稿](papers/poisson_cubic_six_seven_geometry.tex)
へ整理した。7次元rank6で、被約joinと非被約な
embedded primary componentsの横断長8・64、
被約化との差の横断長49が主要な独立研究課題。
[研究ノート](notes/poisson_cubic_six_seven_geometry.md)に
仮定・依存・計算・未解決事項を整理し、退化イデアルの
一般補題・証明全文を同じリポジトリの`papers/sections/`に収録した。
主リポジトリの論文Aには一般次元の結果と依存証明を保持している。

組版：`latexmk papers/poisson_cubic_six_seven_geometry.tex`
数値検算：`python3 computations/verify_poisson_cubic_six_seven_numerics.py`。
移管本文の一致と参照の静的検査、同等のSymPy数値計算を確認。
新稿のLuaLaTeX実組版・PDF目視は未確認。
新規性・primary decompositionの独立監査は未完。

## 全次元Poisson分類の所在

一般次元Poisson pairの成分数・次元公式・固定/相対stackの証明は[主リポジトリ論文A](https://github.com/uedakazushi/nc-cubic/blob/main/papers/paper_a.tex)にある。重複した全次元論文・ノート・専用検算は本リポジトリから除外する。

## VS Code / LaTeX Workshop

リポジトリをVS Codeで**フォルダとして開き**、TeX LiveとLaTeX Workshopを導入する。`.vscode/settings.json` の既定recipeは `latexmk (LuaLaTeX, repository root)`。どの `papers/*.tex` を開いても、リポジトリrootを作業ディレクトリにしてルートの `.latexmkrc` を明示的に読み、生成物は `build/` に置く。TeXを保存するとビルド、手動では `LaTeX Workshop: Build LaTeX project`。ルートから `latexmk papers/nc_cubic_threefold_moduli.tex` などを実行できる。LaTeX Workshopの設定だけではTeX Live自体はインストールされない。

## 新プロジェクト：Poisson cubic fourfold の同時モジュライ

- [研究方針](00_research_plan.md) → [研究ノート](notes/poisson_cubic_fourfold_moduli.md) → [日本語LuaLaTeX草稿](papers/poisson_cubic_fourfold_moduli.tex)
- **集合論的分類はnc-cubic論文Aが正本**。fourfold稿は独自のrank4 generic scheme smoothnessを扱う。
- rank4成分はFermat点のJacobi線形化の階数36からgeneric reducednessも確認。重要な残課題は入力定理の独立検証、rank2と成分交叉のscheme構造、新規性の照合。検算：`python3 computations/verify_poisson_cubic_fourfold_tangent.py`（SymPy）。
- LuaLaTeX：`latexmk papers/poisson_cubic_fourfold_moduli.tex`。GitHub Actions不使用、PDFは生成物としてbuild/へ。

## 現在の研究内容

- `papers/pfaffian_brill_noether_technical.tex`：境界・モジュライ・Pfaffian・Brill–Noether等の大部技術原稿。79節の数学的内容を5個の`papers/sections/`入力へ分割。親TeXが唯一の組版入口。分割の静的内容一致は確認したが、組版・独立証明検証は未実施。
- `papers/central_fiber_discriminant.tex`：中心三次曲面の必要十分判別式・特異点の解析。対応する正確な記号計算は `computations/verify_central_fiber_discriminant.py`。
- `notes/research_notes.md`：現行の数学的状態、欠けている入力、研究再開手順。

初期移管の対象は**完全なTeXソースがGitHub APIで転送・blob一致検証できた部分のみ**。PDF原資料は5点保持する。有限smoothnessの研究ノートは重要な内容を [現行LuaLaTeXノート](notes/ambient_finite_smoothness_and_recovery.tex) と `nc-cubic` の対応原稿へ整理し、PDF追跡を解除した。残る論文PDFについては、未収録の結果・証明があるため保全し、順にTeX化する。詳細は `PDF_SOURCES.md`。

## 再現

リポジトリルートから：

```sh
latexmk papers/pfaffian_brill_noether_technical.tex
latexmk papers/central_fiber_discriminant.tex
python3 -m pip install sympy
python3 computations/verify_central_fiber_discriminant.py
```

LuaLaTeX、LuaTeX-ja、HaranoAji日本語フォント、標準数学パッケージが必要。PDF・補助ファイルは `build/` に生成しGit追跡しない。今回のGitHub APIによる配置確認と実際の組版実行は区別する。

## nc-cubicとの関係

[uedakazushi/nc-cubic](https://github.com/uedakazushi/nc-cubic) は **① Poisson構造の構造定理、② AS-regular代数による代数的量子化、③ rotation付き可換復元** の三目標に限定し、特に③の相対smoothness (SM) に集中する。

三目標の定理に必要な証明・反例・検算は、移管先だけへの参照で代用せず `nc-cubic` の現行論文またはノートへ自立的に保持する。境界研究の完全な本体は本リポジトリへ整理する。構成の整理を可換復元の研究の妨げにしない。

GitHub Actionsは使用しない。force pushをしない。Libraryはpush失敗時の緊急避難に限る。

### 中心商特異性のTeX化と特異圏・球面ツイスト

旧論文VIの非可換A1局所模型とBrauer障害、二中心chartの21中心特異点を[独立LuaLaTeX原稿](papers/central_quotient_local_models.tex)へ部分回収し、さらに[旧§17–18の三次元表現・六次分裂元](papers/sections/central_quotient_simple_representations.tex)を証明付きで統合した。対応する厳密有理数検算は`computations/verify_central_quotient_local_hessian.py`。元の全中心表示・Azumaya locus・小単純表現の分類は条件付き入力として明記し、独立再監査していない。特異圏・twistの回収が完了するまでは原PDFを残す。

旧論文VIの§21–22を `papers/sections/central_quotient_categories_and_twist.tex` に移植した。三中心nodeのKaroubi特異圏と3-spherical twistの証明は、中心有限性・Azumaya locusと正則性の既存入力を明示している。三次元表現の剛性は `computations/verify_central_quotient_reps.py` の法29の非零19次小行列式で再現可能。

中心商原稿には、[非斉次四中心元・Azumaya locusの証明構造](papers/sections/central_quotient_center_azumaya.tex)も回収した。旧有限語計算は現行コードで再構成し、下記の厳密有理数検証を実行した。Azumaya入力の監査はこれと区別する。

旧論文VI§16の正確な量子的tails判別と二重分岐の有限射影行列因子化の証明は [central_quotient_exact_tails.tex](papers/sections/central_quotient_exact_tails.tex) に回収。可換化・分岐・判別式の厳密検算は `python3 computations/verify_quotient_exact_tails.py`。中心関係は下記の厳密計算で確定したが、貼合せ等の監査が残るため原PDFは保持。

中心商の有限中心計算は `computations/verify_center_degree7.py`（Q上の6中心元・交換子rank78）と `computations/verify_center_phi_exact.py`（FLINT厳密有理数演算で次数18・dim1330・Φ=0）を実行確認した。既知の斉次中心定理を入力として全中心表示を確定し、中心商原稿をLuaLaTeXで組版済み。Azumaya・二中心chart貼合せの入力監査と旧稿固有内容の全照合が残るため、原PDF VIは維持する。再現：`python computations/verify_center_phi_exact.py --backend flint --run-all --verify`（python-flintが必要）。
