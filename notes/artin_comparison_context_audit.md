# Artin比較・smoothness反例・Hochschild障害の重点監査

2026-11-13。対象はnc-cubic2の現行共有ソース。元の照合証拠はnc-cubicの `ba7ec3422e53efc0f64f6d8280734296b98aacfe`。元A/Bとその入力は編集しない。

## 文脈調整された9環境の判定

| 環境 | 仮定・証明の照合と判定 |
| --- | --- |
| Artin比較・線束Homの証明 | local cohomologyの固定内部次数における集中を本文に展開した。相対Gorenstein計算と次数別自由性を使い、絶対特異圏には置き換えていない。 |
| Artin比較・MF Homの証明 | 周期変数の二重次数を明記した。nilpotent perturbationは有限和であり、無界な項別自由複体のK-flat性を先取りせず、有限自由複体へのhomotopy同値から得る。 |
| am:prop:Gamma-basechange の主張 | 元の正則局所模型という入力を `ar:lem:regular-hom` の明示的仮定に置き換えた。対象は線束生成部分であり、全coherent残余圏の底変更とはしていない。 |
| 同命題の証明 | 自然な線束Homの底変更を有限evaluation coneと直和因子へ延長する。任意の局所Artin基底に無条件で拡張した主張ではない。 |
| Artin比較末尾の注意 | 形式MF存在・Artin window・形式残余系の接続は統合稿で保持する。短い稿の条件付き移送だけで全次数存在を置き換えない。 |
| as:lem:artin-generation の証明 | 元の生成補題への参照をInd圏での直接証明に展開した。有限相対Beilinson模型により任意のInd対象へのHom底変更が成立し、底環の有限剰余体filtrationで保守性を得る。完備底ではこの有限filtrationを使えない。 |
| smoothness反例末尾の注意 | MFと絶対特異圏の別の例への参照を除いたが、cohomology非flat性という制限と、特別なcubic族を反証していないという範囲を保持した。 |
| ho:cor:fivefold | 「二つの滑らかな五次元特殊ファイバー」から全滑らかなcubic fivefoldへの表現変更は直前の全Nのsector公式をN=7へ代入する直接の帰結。Jacobian Hilbert級数(1+t)^7により1,35,7を得る。 |
| ho:rem:barrier | 一般点復元の未証明という旧文脈を、étale判定法の入力として相対smoothnessを検証するという主張へ整理した。HH^3の消滅を対角perfect性の証明に使っていない。 |

これは9箇所の文脈変更の論理照合であり、Chenのgraded dg enhancement、section–torsion比較、BFK公式とrotation作用の一次資料上の全面監査が完了したという意味ではない。特に相対stabilizationからwindow関手への全忠実性・本質的全射性と、そのdg模型の構成は次の重点監査対象とする。

## 実際に通読・検算した反例と新しい整理

`papers/proper_dg_smoothness_and_artin_limits.tex` は、三次超曲面の復元を入力せずに読める独立稿である。元の反例の全証明は `papers/artin_windows/artin_smoothness_obstruction.tex` をそのまま共用し、コピーを作らない。

今回この反例について、幾何的生成性、endomorphism dg模型の符号と積、外積代数へのquasi-isomorphism、無限semifree分解による非smooth性を確認した。SashaのMathOverflow回答本文を取得し、O⊕O(-1)[1]からskyscraperへの変形が既知の出発例であることを照合した。

追加の代数的定式化とTor計算の証明は `papers/artin_windows/algebraic_smoothness_locus.tex` に置く。任意の局所Artin環への入力は有限長のfiltrationで扱い、一変数切断だけの検算で一般性を主張しない。有限行列検算は既存dg模型の恒等式に加え、自然なH^0底変更写像の階数、追加cycle、Tor次元を検査する。一般のMorita同値やsmoothnessは本文の証明による。

## 公表構成の判断と残る数学

反例と底変更誤差は、形式MF存在や有限パラメータのSklyanin比較と別の問題を説明するため、上記の短い稿を公表準備の独立単位とした。244頁統合稿は技術的参照先として保持する。他の重要な証明・反例を落としておらず、全体の分割を完了したとはしない。

本例はH^1にtorsionを持つ。cohomology-flatな特別の線束模型についてのsmoothness検出を否定しない。strict有限表示とhomotopical有限表示の関係、関連するmoduli定理の仮定、追加した整理の初出・公表上の新規性は引き続き調べる。新規性を確定したとはしない。
