# 研究ノート：境界研究の現在の知識と障害

> **Point scheme 研究の正本（2026-11-13）:** [uedakazushi/nc-cubic-point](https://github.com/uedakazushi/nc-cubic-point)。専用論文、証明節、研究ノート、計算器は移管済み。以下の旧記述に本repo内のpoint-schemeファイル名が現れる場合、移管先の同名パスを参照する。相対復元などの共有証明は必要な範囲で本repoにも保持する。

17次元非可換cubic moduli研究の正本は [nc-cubic-classification](https://github.com/uedakazushi/nc-cubic-classification)。主論文40頁・9入力・6本の厳密検算を独立再現し、専用15ファイルを移管した。共有の相対混合中心/Picard証明、中心対称性持上げ証明、対称性コードと証明書は本repoに保持する。既約成分性・generic reducedness・量子化の代数化と降下、全面的な証明・新規性監査は未了。


Cayley–Sklyanin研究の正本は [cayley-sklyanin](https://github.com/uedakazushi/cayley-sklyanin)、主論文は `papers/cayley-sklyanin.tex`（41頁）、中心曲面判別式の補助稿は3頁。両稿の全文組版・全頁描画とレイアウト確認、次数18の有理数Phi=0を含む必要検算を実行した。有限位数境界の正則性10個の定理・補題と完全な証明はnc-cubic-classificationの現行入力に保持する。共有検算 `verify_central_symmetry.py` は保持する。全面的な一次資料・新規性監査は未了。


Pfaffian–Brill–Noether研究の正本は [pfaffian-brill-noether](https://github.com/uedakazushi/pfaffian-brill-noether)。現行入口 `papers/pfaffian_brill_noether_technical.tex`、完全な証明と検算・研究方針を移管し、移管先で277頁の全文組版・全頁描画と表示概観、Schur/Tateの厳密検算を確認した。旧大型rank入力と一次文献の全面独立監査は未了。一般形式変形・Hesse比較・Picard/gluingを含む共有節 `papers/sections/pfaffian_formal_deformations_gluing.tex` は、混合形式比較の証明を保つため本repoにも内容を変更せず保持する。Pfaffian固有研究の正本は移管先とする。


**2026-11-13 / v17**

- 独立の大部原稿は `https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/pfaffian_brill_noether_technical.tex` にTeXソースで存在する。旧79節を一字も削らず5個の `papers/sections/` ファイルへ分割した。主論文A・Cから直接入力されない一方、内容上の引用・既知結果への依存は今後も監査する。
- 中心三次曲面
  \[
  F_H(U,V,W)=49U^3-(13H+14)U^2+(H+1)^2U+(11U-H-1)VW+V^3-W^3
  \]
  の滑らかさの必要十分条件が \(H(H+1)(27H+28)\neq0\) であることは `https://github.com/uedakazushi/cayley-sklyanin/blob/main/papers/central_fiber_discriminant.tex` に証明されている。追加の変数変換で \((\alpha^3+9)(28\alpha^3+243)\) が現れる。記号計算は `https://github.com/uedakazushi/cayley-sklyanin/blob/main/computations/verify_central_fiber_discriminant.py` に保持する。**中心曲面の判別式から非可換tailsの正則性・Azumaya性までは自動的に導かない。**
- Brill–Noetherの形式変形・gluing object・相対Picard・六次境界・Torelliおよび二段階解消は `https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/pfaffian_brill_noether_technical.tex` に現行の証明を置く。旧`brill_noether.pdf`は章見出しの大部分がこれに対応するため追跡解除した（PDF本文との定理ごとの同値性を監査したものではない）。
- 原PDF移管は全件完了。全混合形式比較・平面切断幾何・点因子の現行稿と厳密再生成器を入口とし、原PDFへ戻らない。
- `finite_smoothness_notes.pdf`のdg perfectness反例に関する独立TeX再構成は `papers/relative_reconstruction/dg_perfectness_counterexamples.tex` に存在するが、有用な残部も現行ノートへ統合してPDF追跡を解除した。全主張を独立監査したという意味ではない。
- 先行研究の新規性・各証明の外部監査は未完了。未確認の内容を定理として拡張しない。

## 最優先の制約

nc-cubicの可換復元（特に相対残余対角のperfectness）を妨げない。必要なdg perfectness反例や中心正則性補題は 各現行正本に残し、この独立研究のために関連主原稿を削除・書き換えない。

## Pfaffian接触分類の現行到達点

Schur分解と二行のBott/Čech–Koszul比較で全次数頂点核 `K^nor=C[H10]`、`E_vert=t^10` を証明した。非線形形式接触分類と一意な主イデアル切片、有限決定性の必要十分条件、実際の境界の `P+H10/96` への同変代数化も現行TeXにある。旧大型rankや旧JSONを再実行したとはしない。実際のTate再帰は新コードで6次まで再構成し、MC恒等式と四block、係数1/96を厳密再確認した。

残るのは、固定Fで任意の座標変更を許す分類、一般の無限一意代表の収束性、全頂点加群の低normal次数部分とその乗法、二次ファイブレーションと大域Brill–Noether幾何の接続である。原PDF IIIは全25節を置換して追跡解除済み。

## PDF整理のためにTeX化した有限正則性の有効な数学

`notes/ambient_finite_smoothness_and_recovery.tex` に、全21混合方向の一様PBWの適用範囲、超越的な中心値での有限大域次元の補題、良い中心chartと滑らかな量子的境界からのtails大域次元3、具体的な `(h,α)=(1,π)` の混合例（非被約な長さ24の点加群スキーム）、偏極付き圏からの二次ambientと中心三次元の復元、対角混合族のnormalizer、Artin perfectnessから完備smoothnessへの誤った推論をまとめた。一般Poisson・PBWとdg反例の十分な証明は `poisson-cubic` 論文Aと独立ノートを正本とする。原PDF研究ノートは長大な公表用論文としての価値が低いため追跡を解除した。本文の全主張を独立監査したという意味ではない。

追跡PDFは0件。旧VIの非可換A1局所模型・Brauer指数6・三因子特異圏だけでなく、初期の一般正則性定理とCayley幾何も現行論文へ回収し、原PDFを追跡解除した。判定は `PDF_SOURCES.md` に集約する。

## Pfaffian旧論文IIIの現行回復の状態

旧論文III§23–24から、五変数Hessian摂動 `g_{F,c}=F+c det Hess(F)` の孤立特異点に対するMilnor数32、Tjurina数31（`c≠0`）、Milnor環の初期正則列とsocleによる証明、およびPfaffian graphを通したstrict transformと相対次元5の二次ファイブレーションを `https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/sections/pfaffian_hessian_geometry.tex` に証明付きで統合した。これは五変数モデルの数学であり、十変数境界との接触同値の証明とは別である。

旧III§10・§21–22の固有証明も三つの新しい入力節に回収した。従来の未確定記述は全次数構造定理と同変近似の証明で解消した。詳細な対応・実行範囲は `PDF_SOURCES.md`。

## 旧論文VI：中心商の現行到達点と残る入力

中心表示のΦ=0は次数18までの厳密有理数商で実行確認した。中心核・最高次記号・三次元表現の中心指標も現行コードで再現できる。補正候補への表現条件はQ(p)=P18(p)というアフィン条件であり、旧零条件を使わない。

現行の `https://github.com/uedakazushi/cayley-sklyanin/blob/main/papers/cayley-sklyanin.tex` に、Rees非Azumaya locusの次元上界、PBWからの大域次元3と中心正規性、一次文献の仮定を照合したAzumaya locus、中心のrank6有限平坦比較と二重étale降下、四つのconifold局所模型・零ファイバーのskew group表示・Brauer指数6を収録した。21中心特異点中15点のHessian非退化性を有理数上で検算した。残る6点のHessianはrank1であり、これらを通常二重点と呼ばない。中心の特異点21個と代数のホモロジー的特異点3個を区別する。

`https://github.com/uedakazushi/cayley-sklyanin/blob/main/papers/sections/central_quotient_chart_gluing.tex` に、行列因子化の縮約、中心chartの分母払い、導分による三切断への帰着、perfect性とSerre双対性による正確な次元を整理した。境界正則性とchartのIwanaga–Gorenstein性も証明し、特異圏の三因子分解への余分な条件を除いた。有限大域次元のaffine PI代数のsmoothnessにはRSV Lemmas 3.4–3.5の適用条件を明示した。

`https://github.com/uedakazushi/cayley-sklyanin/blob/main/papers/sections/central_quotient_pbw_cy.tex`にBGのPBW条件、被約基底上の相対PBW性、R1の自己双対な3-CY解消、指定混合族のKoszul AS正則性を証明した。Koszul双対の有限証明書は全pivotが非零有理定数で、全αへの特殊化が可能。全Frobenius対合detが±1となり、Nakayama twist恒等性を確定した。一次Ext表も局所模型のrad/rad²で説明し、独立にQQ[t]/qとQQ[ω]上でrankを再実行した。対角0・非対角2、中心切断前後で同じである。

初期§1–13の中心零化元、分離型判別式、超越的中心値、良い一般ambient、有限位数境界の正則開集合を `central_quotient_global_regularity.tex` に証明付きで統合した。Rainsの体上の中心定理を被約基底へ持ち上げる有限行列の議論と、RSVの相対smoothnessの仮定を明示する。`central_quotient_cayley_geometry.tex` には明示Cayley変換、反標準楕円境界、twisted NCCR、古典resultantと非被約定常点を収録した。

一般hの中心性と5-CY性は有理関数体上の厳密有限証明書と例外値の対称性で確認した。旧VI全22節の固有内容を現行論文で置換できたため原PDFを追跡解除した。残る研究課題は一般混合の有効判別式、Brauer類のsymbol/stack表示、標識なし復元、具体式の初出照合である。全原PDFの削除ゲートは達成済み。生成PDF・計算状態・ダウンロード文献は追跡しない。

## 中心三次対の現行到達点

旧V全21節は現行モジュライ論文と三つの新しい入力節へ統合し、PDF追跡解除済み。全Hesse式と全六二次係数の中心恒等式、中央スカラー差、37次元graph成分と関数体上の全中心、対角族の完全同型条件、剛体周囲の正則四次元非同型族を保持する。計算と対応表は `PDF_SOURCES.md`。一般の無標識分類・可換対応の大域化・網羅的新規性は未解決である。

## 対角点因子の新しい一般化

`papers/diagonal_cubic_point_geometry.tex` に、次数24の点因子・標準種数5曲線・全点スキームのshift付き分解を整理した。衝突判別式の既約性と次数56は六分岐値が相異なる全範囲で証明した。抽象点スキームの無標識復元やtails判別式との一致は主張しない。旧技術稿全34節も置換して原PDF追跡を解除した。

## 混合形式比較の継続課題

有限cochain縮約・相対window・積/trace・全21方向六級数は `papers/sklyanin_mixed_formal_comparison.tex` に、可換平面incidenceは `papers/marked_hesse_plane_incidence.tex` に整理した。155型/473係数の二次原始、170131型の四次BCHと1/9・1/18、32768結合律、固定源の九次分岐式を旧入力ファイルなしで厳密再生成した。全節照合と組版・表示確認を経て最後の原PDFも追跡解除した。

未解決なのは、有限hでの比較核の代数化・収束、未決定六級数の高次値、大域臨界値像・導手、より高い特異層、無標識の圏分類と新規性の一次調査である。原PDF固有の証明の欠落ではない。一般formalityや再構成入力の全面的な独立再監査・外部査読を完了したとはしない。
