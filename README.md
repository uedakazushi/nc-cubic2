# nc-cubic2：非可換cubicの独立境界・モジュライ研究

**2026年11月11日・v2。独立した研究内容の正本は本リポジトリの `main`。**

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
