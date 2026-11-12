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

- `sections/pfaffian_hessian_geometry.tex`：旧Pfaffian論文IIIの§23–24から復元した五変数Hessian摂動のMilnor/Tjurina、Pfaffian graphのstrict transform・quadric fibration。親の `pfaffian_brill_noether_technical.tex` へ入力済み。独立再監査未了。

- `sections/central_pair_artin_formal_moduli.tex`：旧論文Vから、中心三次対の全Artin形式局所環・Ore局所化・偏極付き二次cover復元・固定ambientの四次元fiberを回収し、`nc_cubic_threefold_moduli.tex`から入力する。完成した外部定理の適用監査や全PDF置換はまだ未了。

- `sections/central_pair_mixed_derived_rigid.tex`：旧論文V§19–21の全混合低次数中心、偶数Veronese復元、Serre関手を使うmarking付き導来復元、固定剛体ambientの四係数非同型族。`nc_cubic_threefold_moduli.tex`から入力。正則な四係数開集合も、中心商論文の中心持上げ・Bertiniの仮定を照合して証明した。

- `central_quotient_local_models.tex`：中心商研究の独立LuaLaTeX入口。旧VIの全22節を証明付きで回収し、原PDFを追跡解除。対応表と検証範囲は `../PDF_SOURCES.md`。
- `sections/central_quotient_pbw_cy.tex`：相対PBW・自己双対解消・Koszul AS正則性・Nakayama恒等性。既知のEG一般定理との関係も明示。
- `sections/central_quotient_center_azumaya.tex`：全中心・Rees/Azumaya・中心ファイバー。Φ=0は `verify_center_phi_exact.py --backend flint --run-all --verify` で次数18までQ上実行済み。
- `sections/central_quotient_simple_representations.tex`：小表現排除・全8三次元単純表現・Ext表。`verify_central_quotient_reps.py` と `verify_central_quotient_extensions.py` で厳密再現。
- `sections/central_quotient_categories_and_twist.tex`：特異圏の局所化・完備化・三因子分解、球面twist。有限中心・境界正則性・chartのGorenstein性の証明も現行稿に収録。
- `sections/central_quotient_chart_gluing.tex`：行列因子化の分母払い、一chart・三切断の貼合せ、Serre次元。
- `sections/central_quotient_global_regularity.tex`：分離型の必要十分判別式、一般hの混合例・5-CY性、超越的中心値、固定ambientと有限位数境界の正則開集合。
- `sections/central_quotient_cayley_geometry.tex`：Cayleyコンパクト化・twisted NCCR・古典pencil/resultant・長さ24の非被約定常点。
- `sections/central_quotient_exact_tails.tex`：悪い中心値、MF二重分岐、曲面/三foldの有効な必要十分条件。`verify_quotient_exact_tails.py` で検算。
- `computations/verify_central_quotient_global_geometry.py`：一般hの中心性、判別式、Cayley変換、位数6等の厳密検算。
- `computations/verify_central_quotient_koszul.py`：全αのFrobenius証明書。`--general-h` で例外因子h(h³+1)と対合行列式を検証し、本文で例外値も処理する。

- `sections/central_pair_explicit_centers.tex`：全Hesse有限中心式、Fermatの41項自由代数恒等式、形式PBW・有限微分性・平行移動と中央スカラー差。検算は `computations/verify_central_pair_centers.py`。
- `sections/central_pair_generic_component.tex`：37次元graph成分、関数体上の重み(1,1,3)中心、41次元支配的incidence。
- `sections/central_pair_diagonal_classification.tex`：対角族の完全同型条件、反対代数、軌道次元。`computations/verify_central_pair_orbits.py` は120射影変換と150×25微分を厳密検算。
