# PDF-onlyの現行判定（2026-11-13 / v22）

**研究・TeX化・削除に関するCodexの恒久指示：** [CODEX_PDF_RECOVERY.md](CODEX_PDF_RECOVERY.md)。単純転記ではなく、証明を洗練し、重要な新しい結果の追加も目指す。以下は現行の残存PDFと削除障害の一覧であり、作業履歴のアーカイブではない。

**本リポジトリの現行mainで追跡するPDF原本は以下の論文4件だけ**。中心商特異性（旧VI、61頁）は全22節の固有内容を現行TeXへ統合した。研究ノート2件と旧Brill--Noether論文1件も現行TeXに価値ある内容を整理してGit追跡解除済み。旧版PDFやZIPのためのアーカイブは作らない。

| 現行PDF | TeXへの移管ができた中心結果 | 残る削除障害 |
| --- | --- | --- |
| `papers/pdf-only/ambient/central_pair_formal_moduli.pdf` (60頁) | 全Artin形式局所環、Ore局所化、偏極と二次cover、偶数Veronese・剛体ambient | 一般Hesse中心公式と37次元ambientの有限検証、非可換Bertiniの正則開集合 |
| `papers/pdf-only/boundary/pfaffian_contact.pdf` (89頁) | Hessian摂動のMilnor/Tjurina、Pfaffian graphのstrict transform・二次ファイブレーション、高次接触計算の既存大部TeX | 普遍非線形接触分類、全次数頂点核、計算証明書の整合 |
| `papers/pdf-only/ambient/central_cubic_technical.pdf` (61頁) | nc-cubic論文Aの量子化/Poissonと本repoの17次元モジュライ、中心チャートのgeneric smoothness補題 | 点加群・有限PI中心・一般混合量子族・正則性の固有結果の完全比較 |
| `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf` (195頁) | nc-cubic論文AのSklyanin中心と全混合量子化、nc-cubic2の既存境界研究への関連部分 | 全21方向の有限式・点スキーム・臨界層・A2/A3/A4/D4型退化・種数5曲線等の固有証明 |

## 中心商特異性（旧VI、61頁）の削除判定

現行の独立入口は [central_quotient_local_models.tex](papers/central_quotient_local_models.tex)。旧PDFの本文・数式・証明・例・参考文献を照合し、以下の全22節を現行論文へ統合した。以下のファイル名は `papers/sections/` 以下である。旧PDFへの参照を証明の代わりに使わない。

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

この範囲で旧VIにしか残る有用な証明・入力はなくなったため、原PDFをGit追跡から解除する。一般h/全混合方向の有効判別式、Brauer類の大域的symbol、標識なし復元、具体式の初出・網羅的新規性は現行原稿の研究課題として残し、解決済みとしない。他の4PDFは下記の固有証明を回収するまで保持する。

旧IIIのHessian幾何は `papers/sections/pfaffian_hessian_geometry.tex`、旧Vのモジュライは `papers/sections/central_pair_artin_formal_moduli.tex` と `central_pair_mixed_derived_rigid.tex`。これらを含む残る四PDF全体の数学的完全置換・組版・独立監査が完了したとは主張しない。

## 保存原則

GitHub mainが正本。現行の日本語LuaLaTeX証明と必要最小限の計算ソースを保ち、生成PDF・計算状態・旧ZIPは追跡しない。固有の有用な数学を失わずに置換できた原PDFだけを追跡解除する。
