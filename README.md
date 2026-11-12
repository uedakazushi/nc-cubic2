# nc-cubic2：非可換cubicの独立境界・モジュライ研究

## nc cubic threefoldの17次元モジュライ（現行の主題）

- [現行草稿](papers/nc_cubic_threefold_moduli.tex)：41次元中心三次対、17係数横断形、分離型余次元15、忘却核7（6+1）、混合中心と相対Picard障害。
- [研究ノート](notes/nc_cubic_threefold_moduli.md)：仮定・未解決の既約成分性・再現手順。
- 再現コード：`computations/independent/verify_generic17_slice.py`、`verify_generic17_center.py`、`computations/verify_split_codimension.py`。
- 一般次元ambient復元の定理と証明は `nc-cubic/papers/paper_a.tex`、本稿には同型類判定に必要な証明も保持する。
- **正則正規三次族からの1周期性**：一般$N,d$について最小周期が$\gcd(N,d)$を割る定理と5次元・三次の場合の系を、モジュライ原稿の [周期性節](papers/sections/ambient_periodicity.tex) に証明ごと統合。ambientの1周期性と、商イデアルを保つ周期性を区別する。後者と初出・新規性の確定は未了。
- 構成した17次元族がnc cubic moduli stackの既約成分であることはまだ未証明。

**2026年11月12日・v6。独立した研究内容の正本は本リポジトリの `main`。**

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

## Poisson cubic $n$-fold pair の全次元分類

**既存Poisson正規形定理を入力とする結果**：滑らかなcubic $n$-fold（$n\ge3$）を動かし、非零Poissonスカラーを保持したpair moduliの既約成分は $\lfloor(n+2)/3\rfloor$ 個。成分の次元閉公式は [全次元の論文草稿](papers/poisson_cubic_pair_components.tex)、仮定・未解決課題は [全次元研究ノート](notes/poisson_cubic_all_dimensions.md)、検算は `python3 computations/verify_poisson_cubic_pair_dimensions.py`。

## VS Code / LaTeX Workshop

リポジトリをVS Codeで**フォルダとして開き**、TeX LiveとLaTeX Workshopを導入する。`.vscode/settings.json` の既定recipeは `latexmk (LuaLaTeX, repository root)`。どの `papers/*.tex` を開いても、リポジトリrootを作業ディレクトリにしてルートの `.latexmkrc` を明示的に読み、生成物は `build/` に置く。TeXを保存するとビルド、手動では `LaTeX Workshop: Build LaTeX project`。ルートから `latexmk papers/poisson_cubic_pair_components.tex` でも同じ原稿を組版できる。LaTeX Workshopの設定だけではTeX Live自体はインストールされない。

## 新プロジェクト：Poisson cubic fourfold の同時モジュライ

- [研究方針](00_research_plan.md) → [研究ノート](notes/poisson_cubic_fourfold_moduli.md) → [日本語LuaLaTeX草稿](papers/poisson_cubic_fourfold_moduli.tex)
- **既存のPoisson正規形定理に基づく分類**：滑らかなcubicと非零Poisson構造の組のモジュライは基礎位相空間として2既約成分、次元30（rank2）と4（rank4）。
- rank4成分はFermat点のJacobi線形化の階数36からgeneric reducednessも確認。重要な残課題は入力定理の独立検証、rank2と成分交叉のscheme構造、新規性の照合。検算：`python3 computations/verify_poisson_cubic_fourfold.py`（SymPy）。
- LuaLaTeX：`latexmk papers/poisson_cubic_fourfold_moduli.tex`。GitHub Actions不使用、PDFは生成物としてbuild/へ。

## 現在の研究内容

- `papers/pfaffian_brill_noether_technical.tex`：独立した大部の境界・モジュライ・Pfaffian・Brill–Noether等の技術原稿。移管元と完全に同じGit blobで保存した。独立LuaLaTeX原稿（65件のbibliography項目を含む）。
- `papers/central_fiber_discriminant.tex`：中心三次曲面の必要十分判別式・特異点の解析。対応する正確な記号計算は `computations/verify_central_fiber_discriminant.py`。
- `notes/research_notes.md`：現行の数学的状態、欠けている入力、研究再開手順。

初期移管の対象は**完全なTeXソースがGitHub APIで転送・blob一致検証できた部分のみ**。PDF原本は転送できておらず、`PDF_TRANSFER_PENDING.md` に移管元と障害を記載している。欠落したPDFが移管されたと主張しない。

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
