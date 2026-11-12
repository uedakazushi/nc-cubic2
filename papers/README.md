# 論文と再生成

全次元の集合論的Poisson pair成分分類：一般次元Poisson成分分類の正本はnc-cubicの論文Aにある。四次元の`poisson_cubic_fourfold_moduli.tex`にはgeneric rank4 smoothnessの厳密小行列式計算も残す。両稿の検証状態を混同しない。


Poisson cubic fourfoldの追加的scheme論：`poisson_cubic_fourfold_moduli.tex`。集合論的分類はnc-cubic論文Aに一元化し、rank4のgeneric smoothnessを扱う。ルートから `latexmk papers/poisson_cubic_fourfold_moduli.tex` を実行する。


独立の主原稿：`pfaffian_brill_noether_technical.tex`。中心判別式の独立補論：`central_fiber_discriminant.tex`。ルートから `latexmk papers/pfaffian_brill_noether_technical.tex` と `latexmk papers/central_fiber_discriminant.tex` を実行する。生成PDFは `build/` にあり、Git追跡しない。大部の原稿には一次資料・適用仮定の再監査が残る。

六次元・七次元のPoisson退化スキームと数値幾何：
`poisson_cubic_six_seven_geometry.tex`。
一般退化イデアル背景、詳細な6/7 geometry、Chern/Hodge数と
Fermat厚化を`papers/sections/`下の三つのTeX節に分割。
リポジトリルートで`latexmk papers/poisson_cubic_six_seven_geometry.tex`。
主要な数学的独立課題は七次元rank6のprimary分解・embedded componentの再監査。
計算は`python3 computations/verify_poisson_cubic_six_seven_numerics.py`。
最新の再開ノートは`notes/poisson_cubic_six_seven_geometry.md`。

## nc cubic threefoldの17次元モジュライ（現行の主題）

- [現行草稿](papers/nc_cubic_threefold_moduli.tex)：41次元中心三次対、17係数横断形、分離型余次元15、忘却核7（6+1）、混合中心と相対Picard障害。
- [研究ノート](notes/nc_cubic_threefold_moduli.md)：仮定・未解決の既約成分性・再現手順。
- 再現コード：`computations/independent/verify_generic17_slice.py`、`verify_generic17_center.py`、`computations/verify_split_codimension.py`。
- 一般次元ambient復元の定理と証明は `nc-cubic/papers/paper_a.tex`、本稿には同型類判定に必要な証明も保持する。
- 構成した17次元族がnc cubic moduli stackの既約成分であることはまだ未証明。


## Pfaffian・Brill--Noether大部原稿の入力構成（2026-11-12）

親ファイルは`pfaffian_brill_noether_technical.tex`であり、以下のファイルを順番に`\\input`する。旧79節のうち主定理・証明に当たる§1–74は字句上無損失で移動し、ラベル・引用と順序を維持した。旧版別検証記録§75–79は、現行の検証状態と未解決事項を記す一節に置換した。

- `sections/pfaffian_formal_deformations_gluing.tex`：形式変形、Kuznetsov、gluing、点加群、Picard（旧§1–20）。
- `sections/brill_noether_boundary_geometry.tex`：境界の三次錐、六次Torelli、二段階解消（旧§21–24）。
- `sections/pfaffian_contact_low_order.tex`：普遍共変量とTate、低次から20次の接触正規形（旧§25–41）。
- `sections/pfaffian_contact_high_order.tex`：20–26次、Koszul、横断Hessian、有限決定性（旧§42–74）。
- `sections/pfaffian_computation_audit.tex`：検算の現行依存関係、整数証明書の状態、未解決の26次問題（旧§75–79を置換）。旧 `verification/` と `source_vNN/` は現行mainに存在せず、独立追試は未実施。

親ファイルだけを `latexmk papers/pfaffian_brill_noether_technical.tex` で組版する。今回の検証は文字列単位の内容保持に限られ、LuaLaTeXの実行と証明の独立監査は行っていない。
