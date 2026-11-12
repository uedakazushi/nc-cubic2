# 論文と再生成

全次元の集合論的Poisson pair成分分類：`poisson_cubic_pair_components.tex`（正規形定理依存）。`latexmk papers/poisson_cubic_pair_components.tex`。四次元の`poisson_cubic_fourfold_moduli.tex`にはgeneric rank4 smoothnessの厳密小行列式計算も残す。両稿の検証状態を混同しない。


Poisson cubic fourfold同時モジュライの現行草稿：`poisson_cubic_fourfold_moduli.tex`。正規形定理を入力とする集合論的2成分分類（次元30,4）であり、scheme構造・新規性の検証は未完成。ルートから `latexmk papers/poisson_cubic_fourfold_moduli.tex` を実行する。


独立の主原稿：`pfaffian_brill_noether_technical.tex`。中心判別式の独立補論：`central_fiber_discriminant.tex`。ルートから `latexmk papers/pfaffian_brill_noether_technical.tex` と `latexmk papers/central_fiber_discriminant.tex` を実行する。生成PDFは `build/` にあり、Git追跡しない。大部の原稿には一次資料・適用仮定の再監査が残る。

六次元・七次元のPoisson退化スキームと数値幾何：
`poisson_cubic_six_seven_geometry.tex`。
一般退化イデアル背景、詳細な6/7 geometry、Chern/Hodge数と
Fermat厚化を`papers/sections/`下の三つのTeX節に分割。
リポジトリルートで`latexmk papers/poisson_cubic_six_seven_geometry.tex`。
主要な数学的独立課題は七次元rank6のprimary分解・embedded componentの再監査。
計算は`python3 computations/verify_poisson_cubic_six_seven_numerics.py`。
最新の再開ノートは`notes/poisson_cubic_six_seven_geometry.md`。
