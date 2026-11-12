# PDF-onlyの現行判定（2026-11-12 / v10）

**本リポジトリの現行mainで追跡するPDF原本は以下の論文5件だけ**。研究ノート2件と旧Brill--Noether論文1件は現行TeXに価値ある内容を整理してGit追跡解除済み。旧版PDFやZIPのためのアーカイブは作らない。

| 現行PDF | TeXへの移管ができた中心結果 | 残る削除障害 |
| --- | --- | --- |
| `papers/pdf-only/boundary/central_quotient_singularities.pdf` (61頁) | 中心判別式、全中心の生成元とRees/Azumaya証明構造、A1局所模型、三次元単純表現、特異圏、球面twist、指定一混合族の正確なtails判別 | 旧有限語計算の中心核・関係式rank証明書、中心/貼合せの入力の独立監査、TeX実組版 |
| `papers/pdf-only/ambient/central_pair_formal_moduli.pdf` (60頁) | 全Artin形式局所環、Ore局所化、偏極と二次cover、偶数Veronese・剛体ambient | 一般Hesse中心公式と37次元ambientの有限検証、非可換Bertiniの正則開集合 |
| `papers/pdf-only/boundary/pfaffian_contact.pdf` (89頁) | Hessian摂動のMilnor/Tjurina、Pfaffian graphのstrict transform・二次ファイブレーション、高次接触計算の既存大部TeX | 普遍非線形接触分類、全次数頂点核、計算証明書の整合 |
| `papers/pdf-only/ambient/central_cubic_technical.pdf` (61頁) | nc-cubic論文Aの量子化/Poissonと本repoの17次元モジュライ、中心チャートのgeneric smoothness補題 | 点加群・有限PI中心・一般混合量子族・正則性の固有結果の完全比較 |
| `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf` (195頁) | nc-cubic論文AのSklyanin中心と全混合量子化、nc-cubic2の既存境界研究への関連部分 | 全21方向の有限式・点スキーム・臨界層・A2/A3/A4/D4型退化・種数5曲線等の固有証明 |

## 検証と再生成の現在有効な情報

- 旧VIのTeX入口は `papers/central_quotient_local_models.tex`。新しい量子的判別の証明は `papers/sections/central_quotient_exact_tails.tex`、対応する限定的な厳密記号検算は `computations/verify_quotient_exact_tails.py`。
- 旧VIの全中心の有限計算（次数6中心核rank78、次数18中心rank49）は**旧PDFの記述**であり、現行コード・入力・証明書による再実行は未了。中心表示とそれに依存するAzumaya結論の全面独立監査も未了。
- 旧IIIのHessian幾何は `papers/sections/pfaffian_hessian_geometry.tex`、旧Vのモジュライは `papers/sections/central_pair_artin_formal_moduli.tex` と `central_pair_mixed_derived_rigid.tex`。
- PDFの本文の比較に使用したLibraryの原資料は同名・同バイトサイズであるが、GitHubのPDFとバイト単位で一致することまでは今回検証していない。
- LuaLaTeXの実組版、全計算・全証明の独立監査、五PDFの数学的完全置換は未完了。追加削除の前に必要な証明と再現資産を現行Gitに統合する。

## 保存原則

GitHub mainが正本。日本語LuaLaTeXの現行証明、必要最小限の計算コード・入力・証明書、現行研究方針と研究ノートを保ち、古い進捗記録、旧PDF・旧ZIP・重複したTeXは追加しない。現行論文で代替できた原PDFだけをGit追跡から解除する。削除済みPDFを将来の研究再開の前提にしない。
