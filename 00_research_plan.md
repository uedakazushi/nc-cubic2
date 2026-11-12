# 研究方針：独立境界・モジュライ研究

**2026-11-12 / v4。再開時は最初に本ファイルを読む。**

## 最重要の構造結果：全次元のPoisson cubic pairの既約成分

- **新定理（既存Poisson正規形定理を入力とする）**：滑らかなcubic $n$-fold（$n\ge3$）の非零Poisson pairを同時に変形させると、基礎位相空間の既約成分は一般rank $2k$（$1\le k\le\lfloor(n+2)/3\rfloor$）について各一つ、合計 $\lfloor(n+2)/3\rfloor$ 個。各成分の次元は `papers/poisson_cubic_pair_components.tex` の閉公式で与える。$n=3,4,5,6,7$の次元は順に $(17)$、$(30,4)$、$(48,16)$、$(72,34)$、$(103,59,6)$。
- **主張の確実性**：軌道次元、係数空間、層の既約性、閉包の非包含について原稿に証明を記載。深い正規形定理は `nc-cubic/papers/sections/poisson_geometry.tex` に既存証明があるが、今回その独立再監査は未完了。全次元のPoisson schemeのgeneric reducedness・交叉のscheme構造・初出確認は未解決。
- **最優先の研究手順**：正規形定理の独立監査→各成分の接空間／非被約性→成分交叉・零切断→先行研究に基づく公表稿の再編。詳細は `notes/poisson_cubic_all_dimensions.md`。
- **保存と組版**：GitHub mainが正本、.vscodeでLaTeX Workshop + LuaLaTeX、PDFはbuildに生成してGit追跡しない。GitHub Actionsとforce pushは使わない。

## 別の研究対象：六・七次元Poisson cubicの退化スキーム

**対象：** 一般次元の正規形・量子化の主結果から独立した、
n=6,7の零点・退化scheme・数値幾何の詳細解析。
現行の独立LuaLaTeX草稿は
`papers/poisson_cubic_six_seven_geometry.tex`、
再開ノートは`notes/poisson_cubic_six_seven_geometry.md`。
一般退化イデアル・finite flat critical cover・零点完全交叉の
証明を`papers/sections/poisson_cubic_degeneracy_background.tex`へ、
n=6,7の階数2,4,6、7次元rank6のprimary分解と
embedded length 8,64およびreduced kernel長49の証明を
`papers/sections/poisson_cubic_six_seven_geometry.tex`へ、
Hodge/Chern/算術種数とFermat横断厚化を
`papers/sections/poisson_cubic_six_seven_numerical.tex`へ収録した。
元の論文Aから対応する6・7次元専用節と数値節を除き、
主定理のための一般次元退化イデアルと証明は論文Aに残した。

**価値の評価：** 階数表・標準完全交叉数値だけの公表価値は低い。
研究の核心候補は七次元rank6のscheme-theoretic primary分解と
embedded componentの長さの解明。
数学的新規性は未確認で、局所イデアル交叉の全独立監査は未完成。
本プロジェクトは`nc-cubic`の論文A一般次元の公表準備を妨げない
副次的研究として維持する。

**再現：**
`latexmk papers/poisson_cubic_six_seven_geometry.tex`、
`python3 computations/verify_poisson_cubic_six_seven_numerics.py`。
元のTeX本文の完全一致、ラベル参照の静的整合性をGitHub上で確認。
数値に対する同等のSymPy計算をローカルで実行してPASS。
新稿全体のLuaLaTeX組版・PDF表示検査は未実施。

## 新しい重点課題：Poisson cubic fourfold pairモジュライ（独立研究）

滑らかなcubic fourfold $X\subset\mathbb P^5$と非零正則Poisson構造$\pi$の組を同時に動かす相対Poisson schemeを、まず基礎位相空間の既約成分、その次にscheme構造まで分類する。Poissonスカラーを保持する。

- **現在の最重要の到達点（既存Poisson正規形定理を入力とする）**：成分数は2、rank2成分のモジュライ次元30、rank4成分の次元4。rank2は$\operatorname{Gr}(3,6)$の非零錐、rank4は二つの平面三次Jacobianブロックに由来する。証明は `papers/poisson_cubic_fourfold_moduli.tex`。
- **依存**：主リポジトリ `nc-cubic/papers/sections/poisson_geometry.tex` のPoisson正規形定理（独立再監査は未実施）。そのため、公表完成定理であるとの主張はしない。数学的な帰結の証明と定理の独立監査を区別する。
- **新たに確認した点**：rank4成分のgeneric reducednessをFermat点のJacobi微分の整数36次小行列式で証明。検算コードは `verify_poisson_cubic_fourfold_tangent.py`。
- **未解決の核心**：rank2成分のgeneric reducedness、交叉のscheme構造、零Poissonの近傍、成分の境界、および新規性の一次文献照合。
- **優先手順**：六変数で正規形の独立証明→generic tangent/obstruction計算→交叉の局所環→全scheme分類→最終稿の先行研究調査。
- **再開順**：本方針→`notes/poisson_cubic_fourfold_moduli.md`→`papers/poisson_cubic_fourfold_moduli.tex`→`computations/verify_poisson_cubic_fourfold.py`。既存の独立Pfaffian研究も保持する。

## 目的と優先順位

本リポジトリは `nc-cubic` のPoisson構造・量子化・可換復元という三主目標から独立した、Pfaffian接触、Brill–Noether境界、中心商特異性、独立モジュライ理論を整理する。研究全体の当面の最優先は**主リポジトリの可換復元**であり、この分離作業のためにそのSM証明を遅らせない。

本体：`papers/pfaffian_brill_noether_technical.tex` は独立した完成度・新規性をまだ外部査読していない大部原稿であり、重要な結果・仮定・証明を削除せず保存する。判別式は `papers/central_fiber_discriminant.tex` に証明と検算を収録した。

## 未解決

関連するPDF原本の移管は未完了。原本の一覧と移管元のGit blob識別子は `PDF_TRANSFER_PENDING.md`。バイナリの転送を確認する前に唯一の原本を削除しない。主リポジトリの定理に引用・依存する補題は、移管元に自立した証明を保持してから移す。文献の一次資料照合も追加監査が必要。

## 次の作業

1. `papers/pfaffian_brill_noether_technical.tex` を独立にLuaLaTeXで組版・検証し、主リポジトリ三目標に使う部分の依存を点検する。
2. 境界PDF原本をバイナリ同一性を保って転送し、各定理・証明をTeXと照合する。TeXで完全に再生成できるまで元のPDFを保持する。
3. 研究の現在有効な成果を分かりやすい公表用原稿へ再編する。単なる旧原稿の蓄積にしない。

## 保存原則

正本はGitHubのmain。研究ノートには現在有効な着想・反例・障害を、論文には十分な証明を保持する。証明記載、今回の照合・計算実行、未確認の新規性を区別する。日付・版番号を付けて更新し、旧ZIP・旧稿の複製・キャッシュを蓄積しない。LuaLaTeXのソースと依存物を優先し、生成PDFはGit追跡しない。明示されたGitHub push失敗時以外にLibraryへ保存しない。
