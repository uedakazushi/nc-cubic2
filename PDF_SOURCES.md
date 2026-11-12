# PDF-onlyの現行判定（2026-11-12 / v17）

**本リポジトリの現行mainで追跡するPDF原本は以下の論文5件だけ**。研究ノート2件と旧Brill--Noether論文1件は現行TeXに価値ある内容を整理してGit追跡解除済み。旧版PDFやZIPのためのアーカイブは作らない。

| 現行PDF | TeXへの移管ができた中心結果 | 残る削除障害 |
| --- | --- | --- |
| `papers/pdf-only/boundary/central_quotient_singularities.pdf` (61頁) | 中心判別式、全中心の生成元とRees/Azumaya証明構造、A1局所模型、三次元単純表現、特異圏、球面twist、指定一混合族の正確なtails判別 | 次数6中心核はQ上で独立検証済み。重み18のrank49とΦ=0はmod101で確認したが、Q上でのΦ=0の証明、中心/貼合せの入力の独立監査、TeX実組版 |
| `papers/pdf-only/ambient/central_pair_formal_moduli.pdf` (60頁) | 全Artin形式局所環、Ore局所化、偏極と二次cover、偶数Veronese・剛体ambient | 一般Hesse中心公式と37次元ambientの有限検証、非可換Bertiniの正則開集合 |
| `papers/pdf-only/boundary/pfaffian_contact.pdf` (89頁) | Hessian摂動のMilnor/Tjurina、Pfaffian graphのstrict transform・二次ファイブレーション、高次接触計算の既存大部TeX | 普遍非線形接触分類、全次数頂点核、計算証明書の整合 |
| `papers/pdf-only/ambient/central_cubic_technical.pdf` (61頁) | nc-cubic論文Aの量子化/Poissonと本repoの17次元モジュライ、中心チャートのgeneric smoothness補題 | 点加群・有限PI中心・一般混合量子族・正則性の固有結果の完全比較 |
| `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf` (195頁) | nc-cubic論文AのSklyanin中心と全混合量子化、nc-cubic2の既存境界研究への関連部分 | 全21方向の有限式・点スキーム・臨界層・A2/A3/A4/D4型退化・種数5曲線等の固有証明 |

## 検証と再生成の現在有効な情報

- 旧VIのTeX入口は `papers/central_quotient_local_models.tex`。新しい量子的判別の証明は `papers/sections/central_quotient_exact_tails.tex`、対応する限定的な厳密記号検算は `computations/verify_quotient_exact_tails.py`。
- 旧VIの中心核について、新規 `computations/verify_center_degree7.py` と同等の有理数/法101計算を独立に実行し、次数6の中心核が厳密に6次元・`1,g,g²,U,V,W`の基底であることを確認した。`computations/verify_center_weight18_mod101.py` と同等の再帰的商空間計算で、次数18のPBW次元1330、重み18以下の50単項式の法101 rank49、Φの法101消滅を確認した。特性零での関係式の零判定と唯一性は未確立である。Azumaya結論の全面独立監査も未了。
- 旧IIIのHessian幾何は `papers/sections/pfaffian_hessian_geometry.tex`、旧Vのモジュライは `papers/sections/central_pair_artin_formal_moduli.tex` と `central_pair_mixed_derived_rigid.tex`。
- PDFの本文の比較に使用したLibraryの原資料は同名・同バイトサイズであるが、GitHubのPDFとバイト単位で一致することまでは今回検証していない。
- LuaLaTeXの実組版、全計算・全証明の独立監査、五PDFの数学的完全置換は未完了。追加削除の前に必要な証明と再現資産を現行Gitに統合する。

## 保存原則

GitHub mainが正本。日本語LuaLaTeXの現行証明、必要最小限の計算コード・入力・証明書、現行研究方針と研究ノートを保ち、古い進捗記録、旧PDF・旧ZIP・重複したTeXは追加しない。現行論文で代替できた原PDFだけをGit追跡から解除する。削除済みPDFを将来の研究再開の前提にしない。

## 次数6最高記号による全中心生成の証明

`computations/verify_center_homogeneous_symbols.py` はQ上で四つの六次最高次記号 `gr(g²),gr(U),gr(V),gr(W)` が斉次Sklyaninの次数6中心を張るrank4を検証する。既知の斉次中心定理と語長filtrationの次数下降帰納法により、非斉次全中心はg,U,V,Wで生成される。重み18以下の50単項式のrank49も斉次中心Hilbert級数からQ上で従う。残る未証明は明示的非斉次Phi=0（Q上）の係数同定であり、Azumaya議論のため原PDFは保持。

## Phiの厳密特性零検証スクリプト（未完了）

`computations/verify_center_phi_exact.py` は自由代数の関係式から次数18までの有理数商を帰納的に構成し、最後に明示Phiを厳密に零判定する。1回の実行で1次数進め、状態をGit外の一時ディレクトリに置く。同じアルゴリズムの独立ローカル実装を実行して有理数の商構成を次数13まで確認（dim560）、次数14は約130秒の時間制約により未終了。GitHub保存スクリプト自体の全次数実行は未了。したがって`--verify`のPASSは未取得であり、**PDF VIは削除しない**。これは以前の法101での零判定と別の厳密証明を目指す再現コードである。

再現計算の追加監査：現行の有理数帰納アルゴリズムをローカルで再構成して次数2–13のPBW次元を実行確認した。次数14は200秒で未完了。したがって旧VIの `Phi=0` の特性零証明は依然として未完成であり、PDFは保持する。

## 関係式の対称性による削減

`papers/sections/central_quotient_center_azumaya.tex`の`prop:quotient-parity-reduction`により、符号対称性を保つ斉次重み18関係の非斉次補正は15個の重み12以下の中心単項式に一意に限定される。標準ライブラリだけの`computations/verify_center_parity_candidates.py`で50個の重み18以下単項式、15個の偶補正、提案Phiの7個の最高次項と4個の低次項を実行確認。さらに可換化による二条件で13次元に削減した（`prop:quotient-abelianization-reduction`）。`verify_center_parity_candidates.py` は非可換中心元の可換化と `g²=-1+2yz` も整数演算で確認。**明示Phiの斉次最高記号の正確性と13係数の値は未検証**なのでPDF VIは保持する。
