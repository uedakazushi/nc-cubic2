# PDF-onlyの現行判定（2026-11-12 / v19）

**研究・TeX化・削除に関するCodexの恒久指示：** [CODEX_PDF_RECOVERY.md](CODEX_PDF_RECOVERY.md)。単純転記ではなく、証明を洗練し、重要な新しい結果の追加も目指す。以下は現行の残存PDFと削除障害の一覧であり、作業履歴のアーカイブではない。

**本リポジトリの現行mainで追跡するPDF原本は以下の論文5件だけ**。研究ノート2件と旧Brill--Noether論文1件は現行TeXに価値ある内容を整理してGit追跡解除済み。旧版PDFやZIPのためのアーカイブは作らない。

| 現行PDF | TeXへの移管ができた中心結果 | 残る削除障害 |
| --- | --- | --- |
| `papers/pdf-only/boundary/central_quotient_singularities.pdf` (61頁) | 中心判別式、全中心の生成元とRees/Azumaya証明構造、A1局所模型、三次元単純表現、特異圏、球面twist、指定一混合族の正確なtails判別 | 次数6中心核とΦ=0をQ上で実行検証し、中心商TeXを実組版済み。残る障害はAzumaya・正則性・二中心chart貼合せの入力の独立監査とPDF固有証明の全照合 |
| `papers/pdf-only/ambient/central_pair_formal_moduli.pdf` (60頁) | 全Artin形式局所環、Ore局所化、偏極と二次cover、偶数Veronese・剛体ambient | 一般Hesse中心公式と37次元ambientの有限検証、非可換Bertiniの正則開集合 |
| `papers/pdf-only/boundary/pfaffian_contact.pdf` (89頁) | Hessian摂動のMilnor/Tjurina、Pfaffian graphのstrict transform・二次ファイブレーション、高次接触計算の既存大部TeX | 普遍非線形接触分類、全次数頂点核、計算証明書の整合 |
| `papers/pdf-only/ambient/central_cubic_technical.pdf` (61頁) | nc-cubic論文Aの量子化/Poissonと本repoの17次元モジュライ、中心チャートのgeneric smoothness補題 | 点加群・有限PI中心・一般混合量子族・正則性の固有結果の完全比較 |
| `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf` (195頁) | nc-cubic論文AのSklyanin中心と全混合量子化、nc-cubic2の既存境界研究への関連部分 | 全21方向の有限式・点スキーム・臨界層・A2/A3/A4/D4型退化・種数5曲線等の固有証明 |

## 検証と削除ゲート

旧VIの入口は `papers/central_quotient_local_models.tex`。次数6中心核、最高記号rank4、三次元表現の中心指標を現行コードで再実行した。`computations/verify_center_phi_exact.py` はFLINTの厳密有理数演算で次数2–18の商を構成し、dim F18=1330とΦ=0のPASSを得た。既知の斉次中心定理と合わせて全中心表示を確定した。法101の零を特性零の証明としたものではない。次数8以下ではFraction/FLINTの全乗法・包含行列と、Horner/語ごとの評価を比較した。

中心商原稿のLuaLaTeX組版も実行した。ただしAzumaya locus・非可換Bertini・二中心chart貼合せの外部入力の独立監査、旧PDF61頁の全固有内容との照合は完了していない。したがって旧VIを削除しない。他の4PDFにも表の固有証明が残るため、5件とも保持する。

旧IIIのHessian幾何は `papers/sections/pfaffian_hessian_geometry.tex`、旧Vのモジュライは `papers/sections/central_pair_artin_formal_moduli.tex` と `central_pair_mixed_derived_rigid.tex`。これらを含む五PDF全体の数学的完全置換・組版・独立監査が完了したとは主張しない。

## 保存原則

GitHub mainが正本。現行の日本語LuaLaTeX証明と必要最小限の計算ソースを保ち、生成PDF・計算状態・旧ZIPは追跡しない。固有の有用な数学を失わずに置換できた原PDFだけを追跡解除する。
