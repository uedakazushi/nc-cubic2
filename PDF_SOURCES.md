# PDF-onlyの現行判定（2026-11-13 / v27）

Cayley–Sklyanin研究の正本は [cayley-sklyanin](https://github.com/uedakazushi/cayley-sklyanin)、主論文は `papers/cayley-sklyanin.tex`（41頁）、中心曲面判別式の補助稿は3頁。両稿の全文組版・全頁描画とレイアウト確認、次数18の有理数Phi=0を含む必要検算を実行した。元モジュライ稿に必要な有限位数境界の正則性は `papers/sections/central_pair_finite_order_regularity.tex` に10個の定理・補題と完全な証明をローカル保存し、モジュライ稿40頁を再組版済み。共有検算 `verify_central_symmetry.py` は保持する。全面的な一次資料・新規性監査は未了。


Pfaffian–Brill–Noether研究の正本は [pfaffian-brill-noether](https://github.com/uedakazushi/pfaffian-brill-noether)。現行入口 `papers/pfaffian_brill_noether_technical.tex`、完全な証明と検算・研究方針を移管し、移管先で277頁の全文組版・全頁描画と表示概観、Schur/Tateの厳密検算を確認した。旧大型rank入力と一次文献の全面独立監査は未了。一般形式変形・Hesse比較・Picard/gluingを含む共有節 `papers/sections/pfaffian_formal_deformations_gluing.tex` は、混合形式比較の証明を保つため本repoにも内容を変更せず保持する。Pfaffian固有研究の正本は移管先とする。


**研究・TeX化・削除に関するCodexの恒久指示：** [CODEX_PDF_RECOVERY.md](CODEX_PDF_RECOVERY.md)。単純転記ではなく、証明を洗練し、重要な新しい結果の追加も目指す。以下は現行の残存PDFと削除障害の一覧であり、作業履歴のアーカイブではない。

**Git追跡PDFは0件。** 旧原PDFの固有内容は、下記の現行TeX・証明・再生成可能な計算へ統合済み。生成PDFや原PDFの別形式アーカイブは追跡しない。以後の再開に原PDFは不要である。

## 中心商特異性（旧VI、61頁）の削除判定

現行の独立入口は [central_quotient_local_models.tex](https://github.com/uedakazushi/cayley-sklyanin/blob/main/papers/cayley-sklyanin.tex)。旧PDFの本文・数式・証明・例・参考文献を照合し、以下の全22節を現行論文へ統合した。以下のファイル名は `papers/sections/` 以下である。旧PDFへの参照を証明の代わりに使わない。

| 旧節 | 保持した数学と現行の証明所在 |
| --- | --- |
| §1–2 | 混合族・記号・構成：親TeXの導入、`central_quotient_pbw_cy.tex`。PBW/CYはEGの既知一般定理の具体化と明示し、独立のsyzygy証明も保持 |
| §3 | 中心零化元のKoszul cone、twists生成、二chart貼合せ：`central_quotient_global_regularity.tex`。line objectを射影的と仮定せず、Yoneda拡大の消滅を用いる |
| §4 | 分離型二変数三次式の必要十分条件 Δ≠0、重根三型の無限射影次元、GL2同型類：同ファイル |
| §5 | 全有限hでの周囲のPBW/AS正則性・5-CY性と中心三次式：同ファイルと `central_quotient_pbw_cy.tex`。有理関数体上の証明書と例外値の対称性を区別 |
| §6 | 古典pencil、六次判別式、勾配resultantの定数・重複度：`central_quotient_cayley_geometry.tex`。Poisson積公式の一次出典を確認 |
| §7 | 導分と三切断によるperfect性：`central_quotient_chart_gluing.tex` |
| §8–9 | 一般h・超越的αの正則例、超越的中心値での有限大域次元：`central_quotient_global_regularity.tex`。最後の体拡大が代数的分離であることを明示 |
| §10–11 | 一chart、行列因子化の分母払い、Serre次元、(h,α)=(1,π)：`central_quotient_chart_gluing.tex` と一般正則性節。定常点スキームの長さ24はCayley節で独立に証明 |
| §12 | 固定した良いambientの四係数very-general正則性：`central_quotient_global_regularity.tex` |
| §13 | 有限位数楕円境界の中心持上げ・非空開な正則範囲・有理数点の稠密性、h=1の位数6：同ファイル。Rains Theorem 2.13とRSV Proposition 2.1の仮定を照合。旧後半の弱い有限例外結果は下記の有効判別式で強化 |
| §14–15 | 全中心、Φ=0、有限中心性、Rees/Azumaya、中心ファイバー判別：`central_quotient_center_azumaya.tex` |
| §16 | 悪い二中心値、非被約Rep1、MF二重分岐、正確なtails判別：`central_quotient_exact_tails.tex`。全affine中心値βでの必要十分条件も追加 |
| §17–18 | 1/2次元単純表現の排除、全8三次元表現、剛性、全一次Ext表、六次分裂元：`central_quotient_simple_representations.tex` と親TeX |
| §19 | 四つのA1局所模型、零中心値のskew group表示・大域次元2・Brauer指数6：親TeX |
| §20 | Cayley三次曲面の明示線形変換、滑らかな反標準楕円境界、twisted NCCRと既知del Pezzo研究との比較：`central_quotient_cayley_geometry.tex` |
| §21 | 21中心特異点と3ホモロジー的特異点、中心降下・分岐・Hessian・node模型：親TeX。Karoubi特異圏の三因子分解：`central_quotient_categories_and_twist.tex` |
| §22 | 球面twist、coherent導来随伴、Seidel–Thomasの条件と標識を保たない自己同値：同ファイル。標識なし復元の存在分類までは結論しない |

### 実行した検証

- `verify_center_phi_exact.py --backend flint --run-all --verify`：次数2–18の厳密有理数商、dim F18=1330、3751語のΦ=0。有限体での零を特性零の証明と混同しない。低次数ではFraction/FLINTと二つの評価方法も比較。
- 中心核・最高記号・表現行列・全Ext表・局所Hessian・正確なtails判別は現行の各 `verify_*` で実行確認。Extは代数体上のrank19/16、内的微分rank8/9まで確認。
- `verify_central_quotient_koszul.py`：全αで有効な定数pivotとFrobenius対合。`--general-h`：h(h³+1)以外に消去の例外がなく、対合行列式とNakayama恒等性を厳密確認。例外値は本文の可換性・反対代数・三乗根対称性で扱う。
- `verify_central_quotient_global_geometry.py`：一般hの重み4中心性（91語・rank69）、二変数判別式、古典resultantのnorm行列、Cayley変換、無限遠の滑らかさ、位数6、定常点の判別を厳密確認。
- LuaLaTeXで親TeXを組版し、追加部分をPDF表示で確認。未定義の論理参照・書誌参照とoverfull boxを解消。生成物・計算状態・ダウンロード文献は追跡しない。

この範囲で旧VIにしか残る有用な証明・入力はなくなったため、原PDFをGit追跡から解除する。一般h/全混合方向の有効判別式、Brauer類の大域的symbol、標識なし復元、具体式の初出・網羅的新規性は現行原稿の研究課題として残し、解決済みとしない。全混合量子化の固有証明も下記の現行稿に回収した。

## 中心三次対（旧V、60頁）の削除判定

入口は `papers/nc_cubic_threefold_moduli.tex`。旧全21節を本文・数式まで照合した。一般Poisson分類はnc-cubic論文Aを正本とし、その一般次元の証明を重複収録しない。以下は現行の証明所在（`papers/sections/`以下）。

| 旧節 | 現行の数学的な所在と検証 |
| --- | --- |
| §1–6 | 規約・射影Poissonの一意延長・忘却四係数・Poisson成分は論文Aの既知入力。中心対への適用は親TeXの導入・構成節 |
| §7–9 | 全混合相対PBW、CY5、中心の多項式持上げ、可換点近傍の平坦族：親TeXのPBW/CY/中心補題と `central_pair_explicit_centers.tex`。低次数中心の可換点での跳躍を区別 |
| §10–11 | 37次元graph成分、相対Poisson全中心、形式量子化から一般点への単射、重み(1,1,3)の一般中心、41次元incidence：`central_pair_generic_component.tex`。Pymの形式比較とPoisson成分性は既知入力 |
| §12–13 | 全Artinの自動中心性・Plückerイデアル・完備局所環・Ore局所化・偏極・二次cover：`central_pair_artin_formal_moduli.tex`。通常の標識付き変形関手でありderived stackや大域分類とは同一視しない |
| §14 | 全Hesse有限中心式・整列語minor・全六二次係数のFermat中心式・41項の自由代数恒等式・形式PBW・有限微分性・正則商・中央スカラー差：`central_pair_explicit_centers.tex`。有限gaugeと可換対応の高次幾何は下記の混合形式比較稿と平面incidence稿へ回収 |
| §15–17 | 対角族の定義・section algebraと二次包絡の復元・完全同型条件・h^6不変量・反対代数：親TeXと `central_pair_diagonal_classification.tex` |
| §18 | 一般軌道24次元、商13/17次元、忘却4次元、対角飽和余次元7：`central_pair_generic_component.tex` と `central_pair_diagonal_classification.tex` |
| §19–20 | 中心二次曲線と二重被覆による偶数Veronese復元、全混合低次数中心、構造対象付き導来復元、有限同型条件：`central_pair_mixed_derived_rigid.tex` |
| §21 | 固定周囲の中心直線の有限群商、明示剛体周囲、四次元非同型族、正則開部分、可換滑らかさとの同時実現：同ファイルとArtin節。中心持上げ・Bertiniの仮定は現行中心商論文の証明で照合 |

`verify_central_pair_centers.py`でRainsの全係数式をQ(q,t)上で検証した（339語、162関係、rank144、三交換子零）。17次minorは厳密に −q^5(q^3−t^3)^2。別の自由代数展開で三つの41項恒等式、全六係数の平行移動とRainsの中央スカラー差を確認した。数値補間・有限体の零を証明に使わない。

`verify_central_pair_orbits.py`は120個の有理射影変換を全列挙し、六点のstabilizerが自明と確認した。周囲の150×25軌道微分はQ上rank24、核は同時スカラーだけで、選択した24次minorは −480000000。既存の低次数中心rank3/6/9と31次行列式 −5538243375000も再実行した。

LuaLaTeXで親TeX全体を組版し、追加した数式をPDF表示で確認。未定義参照・書誌参照・overfullを解消した。Barmeier–Wang Theorem 10.3/Lemma 10.9のグラフ微分性を一次資料で確認した。外部formality・分類定理自体の再証明や網羅的新規性は主張しない。旧Vだけに必要な数学を残さず置換できたため、原PDFを追跡解除する。

## Pfaffian接触境界（旧III、89頁）の削除判定

現行入口は `https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/pfaffian_brill_noether_technical.tex`。原PDF全25節の固有内容を、既存の低次/高次接触・境界幾何節と以下の追加証明で置換した。

| 旧節 | 現行の証明所在（`papers/sections/`以下） |
| --- | --- |
| §1–5 | Pfaffian微分・共変量・消滅イデアル・横断射影：[現行の対応節](https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/sections/pfaffian_contact_low_order.tex) と [現行の対応節](https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/sections/pfaffian_contact_high_order.tex)。通常像と勾配イデアル、全次数分裂射影を保持 |
| §6–9 | 判別式torsion・頂点支持・有限性・巨大だが明示的な補助上界・Hessian socleとその微分：[現行の対応節](https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/sections/pfaffian_contact_high_order.tex)。全頂点加群と指定された対角成分を区別 |
| §10 | Pfaffian係数環上のSchur分解・長さ二の自由分解・Bott二行・Čech–Koszul・16生成元と乗法・全次数頂点核：[現行の対応節](https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/sections/pfaffian_vertex_structure.tex)。Hの非零性はB直和因子とFermat特殊化でも証明し、大型有限rankへの依存を除去 |
| §11–13 | 普遍勾配height3・固定三元正則列・高次Koszul homology消滅・Hessian作用の全次数簡約・normal変換則：既存高次節 |
| §14–15 | 普遍共変量と低次類、Tate再帰・評価束・incidenceのscheme同定・定数block・十次係数1/96・全滑らかFでのJacobian障害：既存低次節。実際の再帰から四blockを新コードで再構成 |
| §16–18 | 有限Tate方程式・4929補助変数・étale/収束模型・Clifford反転・偶化：既存低次/高次節。補助空間5890/4929/20330も独立に再計算 |
| §19–20 | Picard族とHesseのjによる全次数normal消滅・normal零での有限決定性：既存高次節と全次数頂点核の定理 |
| §21 | 同変近似・中心重み・零切断に沿う普遍代数化/収束・単元なし十次右同値・Plücker錐と平面ラベル・固定パラメータのArtin補論：[現行の対応節](https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/sections/pfaffian_equivariant_algebraization.tex) |
| §22 | 全普遍形式接触分類・normal比・安定化元・一意主イデアル切片・有限決定性の必要十分条件・一変数moduli・低係数・normal曲線のjが忘れるH係数：[現行の対応節](https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/sections/pfaffian_contact_classification.tex) |
| §23–24 | 五変数Hessian摂動のMilnor/Tjurina、Pfaffian graphのstrict transformと二次ファイブレーション：[現行の対応節](https://github.com/uedakazushi/pfaffian-brill-noether/blob/main/papers/sections/pfaffian_hessian_geometry.tex) |
| §25・書誌 | 固定Fの全座標分類・一般無限代表の収束・低normal次数の全頂点加群などの未解決範囲は現行本文/ノート。必要書誌は親TeX |

`verify_pfaffian_vertex_and_tate.py`は、全記号r,cのSchur Hilbert恒等式を確認し、有限Tate空間の次元5890/4929/20330を計算した。さらに旧コードをimportせず、外積/Clifford bitmaskと有理多項式で実際のTate再帰を6次まで再構成した。全MC恒等式、四つの掲載block、三次/五次blockの零性、行列式の十次係数−648、Hessian係数1/96が一致した。全次数頂点核と非線形分類は本文の構造的証明による。旧大型rankや未取得の旧JSONを実行済みとはしない。

原PDFのSchur分解・Bott・非線形分類の数式を表示確認し、現行親TeX全体（277頁）をLuaLaTeXで組版して追加部分も表示確認した。未定義の論理/書誌参照・overfullを解消。RWWのLittlewood/BottとExample 1.2を一次資料で照合した。同変近似はBierstone–Milmanの既知定理を入力とし、独立変数と未知変数の線形表現・原点での零・jet位相を本文で検査した。網羅的新規性と全証明の外部査読は未了だが、原PDFだけに依存する数学はなくなったため追跡解除する。

## 中心三次技術稿（61頁）の削除判定

全34節を現在の三論文へ統合した。重複する一般定理の新たな大部原稿は作らない。

| 旧節 | 現行の証明所在 |
| --- | --- |
| §1–13 | 一意延長・Poisson成分はnc-cubic論文A。PBW/CY、中心持上げ、一般中心、37/41次元graph/incidence、形式中心対とHesse有限中心式は `nc_cubic_threefold_moduli.tex` と `central_pair_*` 入力節 |
| §14–19 | 分離族・真の混合例・古典pencil・中心零化元・導分による三切断：`central_quotient_local_models.tex` の一般正則性・古典比較・chart貼合せ節 |
| §20–23 | 全係数長さ24平坦族と三局所環型、四係数と接空間の埋込み付き検出、genus5曲線・点因子の線形系・同時復元・ramification・次数56判別・楕円成分とshiftのscheme分解：`diagonal_cubic_point_geometry.tex` と二つの入力節 |
| §24–28 | 超越的中心値、分母払い、一般hの曲面/三fold正則例、固定良ambientのvery-general正則性：中心商論文 |
| §29–30 | section algebra・二次包絡・完全な対角同型条件と反対代数：モジュライ論文 |
| §31 | 有限位数境界の中心持上げ・Bertiniによる非空正則開集合：中心商論文の全証明 |
| §32–33 | 一般軌道24・商13/17・対角飽和余次元7・偶数Veroneseと中心二重被覆での構造対象付き導来復元：モジュライ論文 |
| §34・書誌 | 無限位数境界での全正則locus開性・無標識復元・具体式の初出は未解決として現行本文へ保持。指定一混合族の弱い有限例外結果は中心商論文の有効判別式で強化 |

点幾何の新稿では次数56と既約性を、特定の二次式だけでなく六分岐値が相異なる全範囲へ拡張した。`verify_diagonal_point_geometry.py`でmonicな一様24基底、三局所環の消去判別、pencil射影の反例恒等式、楕円graphの行列式と原点kernel、標準曲線の切断次元を厳密確認した。次数56と既約性の証明はjet incidenceとRiemann–Hurwitzにより、数値観察からは導かない。LuaLaTeX組版（5頁）・PDF表示・参照/書誌/overfull確認を終えたため、この原PDFも追跡解除する。

## 保存原則

GitHub mainが正本。現行の日本語LuaLaTeX証明と必要最小限の計算ソースを保ち、生成PDF・計算状態・旧ZIPは追跡しない。固有の有用な数学を失わずに置換できた原PDFだけを追跡解除する。

## 全混合量子化（旧II、195頁）の削除判定

全19節、第9節の57小節を証明・数式・例まで照合した。既存の分離族と重なる証明は大部稿に保ち、固有の形式比較と可換幾何は二つの独立稿へ整理した。

- **形式比較の入口：** `papers/sklyanin_mixed_formal_comparison.tex`（21頁）。
- **平面切断の入口：** `papers/marked_hesse_plane_incidence.tex`（16頁）。
- **点因子の入口：** `papers/diagonal_cubic_point_geometry.tex`（5頁）。
- **分離族・評価核・五生成元分類：** 大部稿の `papers/sections/pfaffian_formal_deformations_gluing.tex`。既に実組版済みの本文の証明を保持する。

以下の短いファイル名は `papers/sections/` 以下を指す。

| 旧節 | 有用な数学と現行の証明所在 |
| --- | --- |
| §1–2 | 対象・標識・既知の再構成入力：形式比較稿の導入・分離Hesse比較への明示参照。一般次元の再構成はnc-cubic論文Bを正本として重複しない |
| §3–7 | Fermat明示族、中心とPBW、射影正則性、楕円block、Picard共役、Hesse比較、固定残余圏補正：既存の `pfaffian_formal_deformations_gluing.tex` の各証明 |
| §8 | 実際のabelianizationの長さ24は点因子稿。一混合Hesse候補の全パラメータresultant、三/九node、c=0退化、hによる候補と規格化：`mixed_candidate_discriminant.tex`。有限hの圏同値と区別 |
| §9.1–5 | marked Fermat切片、有限群/細分次数、係数付き変形複体：`mixed_coefficient_complexes.tex`、`mixed_six_series_and_incidence.tex`。標準形式対応は分離Hesseと既知再構成を明示入力とする |
| §9.6–8 | 二行点イデアルMF、評価射、二対象生成、混合欠損・整合式と八行持上げ：`mixed_point_matrices.tex` |
| §9.9–10 | 階数32二次双対と全積、全入力の停止PBW正規化、積/曲率cocycle、Koszul制限：`mixed_quadratic_dual_and_cocycle.tex`。周囲の双対とMFの全高次模型を区別 |
| §9.11–12 | 楕円係数複体の三次元模型、グラフ核の基底直線とframe、負二回転の単元、一変数A2のcoherenceと混合sector：`mixed_coefficient_complexes.tex` |
| §9.13–16 | 二次類のgauge不変な定式化、有限arityの実MFへの移送、Artin相対window、生成子一つによる基底変換：`mixed_quadratic_dual_and_cocycle.tex`、`mixed_finite_gauge_transport.tex`、`mixed_relative_window.tex` |
| §9.17–19 | 全入力の二次積と原始、有限poset縮約、全h次数の係数線形純曲率化と一変数性：`mixed_second_order_curvature.tex`、`mixed_finite_gauge_transport.tex`、`mixed_elliptic_trace_comparison.tex` |
| §9.20–22 | 旧六次数値入力は、全次数の積/Serre traceによる b(h)^3=1+h^6/27 の証明で置換。rotation剛性、実際のcharacteristic類、二乗境界、二residue、periodicity scalarの消去：`mixed_elliptic_trace_comparison.tex`。U=1/81の独立な数値入力は不要 |
| §9.23–26 | 三中央係数/九混合係数の共通b、canonical二次jetと反例、九/十次minor、古典的優勢性と35行列：`mixed_six_series_and_incidence.tex`、`mixed_diagonal_subfamily.tex` |
| §9.27–30 | 165/56係数補空間、平行移動のPBW加法cocycleと中心規格化台帳、Weyl共変縮約、全21方向の六級数と選択則：`mixed_finite_gauge_transport.tex`、`mixed_six_series_and_incidence.tex`。未知級数の全値は求めたとしない |
| §9.31 | 155微分型/473係数の全係数二次原始、余因子公式、U_e[h²]=−1/12、S_e[h²]=1/4：`mixed_second_order_curvature.tex`。旧JSONなしで再生成 |
| §9.32 | 四次BCH縮小代表、係数射影の正当化、三次原始の不要性、全十七Jacobian列による二係数1/9・1/18：`mixed_fourth_order_curvature.tex`。170131型の全閉性と降順原始を再構成 |
| §9.33–38 | 十五係数の明示代表、全21方向の接階数、六自由方向、h固定の平面incidence同型、正確な臨界イデアル：`mixed_six_series_and_incidence.tex`、`mixed_fibre_branch_geometry.tex`、`marked_hesse_critical_geometry.tex` |
| §9.39 | 六次Hessian因子の絶対既約性・正規性・有理性、完備整域性、特異集合次元六：`marked_hesse_critical_geometry.tex` |
| §9.40–41 | 古典分岐零スキームと臨界値、元の源での相対三次jet、T一般点のMorse模型：`marked_hesse_relative_models.tex` |
| §9.42–46 | 全A2/A3点の標的versality、明示例と四次残余、cusp/swallowtailの有限正規化・導手・二稜線、核上三次の四成分と次数27/6/6/6、一ブロック核の非孤立極限：`marked_hesse_critical_geometry.tex`、`marked_hesse_discriminant_normalization.tex` |
| §9.47–48 | A4形式弧、二パラメータ内のA5障害、五次判別の正規化、D4模型と三つのA3枝、主成分の三軸局所環・非正規性・導手：`marked_hesse_higher_strata.tex` |
| §9.49–50 | 二退化因子を保つ積模型、相対/全空間の被約特異スキーム、非孤立点で二次jetは全射だが全変形はversalでないこと：`marked_hesse_relative_models.tex` |
| §9.51–56 | 同変Jacobian包含による全高次項除去、六自由方向、Fermat形式ファイバーの正規性/九成分、固定源の六/九次jetと量子寄与、忠実平坦性とArtin点非全射：`mixed_fibre_branch_geometry.tex`、`marked_hesse_relative_models.tex`、形式比較稿 |
| §9.57 | 失われたコード名の羅列は現行の下記再生成器と実行範囲へ置換。有限計算と圏論/全次数の証明の区別を各本文で保持 |
| §10–12 | 六例外ファイバー、非被約点、associated form、四つの同型類、3-isogeny：既存大部稿の射影正則性・点加群・非被約点復元の各節 |
| §13–14 | 五生成元の内在的復元、完全同型判定・自己同型群とDVRの限界、評価核の安定性・特異部分・Picard接写像・明示gluing層：既存大部稿の五生成元分類節と評価核節 |
| §15–19 | 点因子の24基底・三局所型・係数検出の反例、標準種数5曲線と次数56衝突判別、全点schemeとshift復元：点因子稿の二入力節。次数56は六分岐値が相異なる全範囲へ一般化 |

### 独立に実行した再構成

- `verify_mixed_second_order_gauge.py`：有限cobar行列から155微分型・473多項式係数の原始を毎回生成し、通常微分Leibniz挿入で全恒等式を確認。二次結合律・Casimir・対称性も全入力記号で確認。
- `verify_mixed_fourth_order_gauge.py`：実際のPBW/Weyl積からC3の90型・C4の24型を復元し、低記号を全二次積と照合。170131型のBCHを生成し閉性確認。arity6の86332型原始を除いて3443型、arity4の1607型原始を除いて46型とし、純曲率 −5(e1 x²+e2 y²)/144+e1 e2 z/24+e1 m1/48 を得た。全十七列で分解し1/9・1/18を厳密確認。外部JSON・補間・有限体の零判定は使わない。
- `verify_mixed_point_matrices.py`、`verify_mixed_trace_scalars.py`：全hの自由語商における混合欠損・整合式・評価cocycle・二乗境界、可換側射と二乗係数、二residue、scalar消去と剛性行列を確認。Serre traceの意味は本文の評価列の証明による。
- `verify_mixed_quadratic_dual.py`：Q[α,h]上で全32768結合律とHilbert級数を確認。`verify_mixed_diagonal_dominance.py`：35次行列式 −20736 と九係数minorを再生成。
- `verify_marked_hesse_geometry.py`、`verify_marked_hesse_higher_strata.py`、`verify_mixed_candidate_discriminant.py`：Hessian恒等式、明示A2/A3/A4/D4例、導手とJacobian引戻し、resultantの定数・重複度、非孤立点の二次jet行列式を厳密確認。
- `verify_mixed_fibre_branch_jets.py`：FLINTの有理数多項式で二十五軌道方程式を次数七まで解き、六変数全体の古典/量子補正済み九次分岐式と24単項式を、旧行列・旧証明書を入力せず再生成。
- 二新稿をLuaLaTeXで組版し、未定義参照・引用・欠字・overfullを解消。原PDFの可視数式と新稿の主要頁も表示確認。Burke–Stevenson一次資料の有限大域次元仮定を確認し、Artin基底では直接引用せず相対証明を保持する。既知分類・一般再構成・formalityの再証明や網羅的新規性は主張しない。

この範囲で旧IIだけに必要な数学・入力を残さず置換できたため、最後の原PDFをGit追跡解除する。原PDF/ZIPの別アーカイブは作らない。残る数学的課題は、比較核の有限hでの代数化・収束、未決定の六級数の高次値、より高い特異層と大域臨界値像・導手、無標識の圏分類、および新規性の一次文献調査である。これらは旧PDF固有の証明の欠落とは異なる。
