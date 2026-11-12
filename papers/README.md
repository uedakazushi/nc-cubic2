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

- `sections/central_pair_mixed_derived_rigid.tex`：旧論文V§19–21の全混合低次数中心、偶数Veronese復元、Serre関手を使うmarking付き導来復元、固定剛体ambientの四係数非同型族。`nc_cubic_threefold_moduli.tex`から入力。正則な四係数開集合は依存する非可換Bertiniの適用を未監査。

- `central_quotient_local_models.tex`：旧論文VIの非可換A1局所模型、四つの中心特異点、局所skew group、Brauer指数、21中心点と三homological singularityの条件付き解析。LuaLaTeX独立入口。検算：`python3 computations/verify_central_quotient_local_hessian.py`（SymPy）。全中心表示・Azumaya locus・小表現排除は未移管の入力として明記。

- `sections/central_quotient_simple_representations.tex`：旧論文VI§17–18から1/2次元単純表現排除、軸上2個と非軸上6個の三次元表現、六次分裂元の最小多項式を回収。親の `central_quotient_local_models.tex` から入力する。`python3 computations/verify_central_quotient_reps.py` は明示行列・三関係式・G1=0をQ[t]/(q)とQ[ω]/(ω²+ω+1)上で厳密検算する。全中心・Azumaya locus・Ext ranksは未完。

- `sections/central_quotient_categories_and_twist.tex`：旧論文VI§21–22の射影特異圏の二段局所化と三つの通常二重点への完備化・Knörrer同値、および標識を保たない3-spherical twist。`central_quotient_local_models.tex`から入力。`sections/central_quotient_simple_representations.tex`は軸上3次元表現の無限小剛性の整数証明書を新設した。有限中心・tailsの正則性の完全証明はまだ未統合。

- `sections/central_quotient_center_azumaya.tex`：旧VI§14–15。全中心四生成元・唯一の関係とRees退化を用いるAzumaya locus、中心ファイバーによる大域次元の条件付き判定。旧有限語証明書を独立再実行していない。
