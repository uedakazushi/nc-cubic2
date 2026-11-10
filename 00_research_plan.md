# 研究方針：独立境界・モジュライ研究

**2026-11-11 / v2。再開時は最初に本ファイルを読む。**

## 新しい重点課題：Poisson cubic fourfold pairモジュライ（独立研究）

滑らかなcubic fourfold $X\subset\mathbb P^5$と非零正則Poisson構造$\pi$の組を同時に動かす相対Poisson schemeを、まず基礎位相空間の既約成分、その次にscheme構造まで分類する。Poissonスカラーを保持する。

- **現在の最重要の到達点（既存Poisson正規形定理を入力とする）**：成分数は2、rank2成分のモジュライ次元30、rank4成分の次元4。rank2は$\operatorname{Gr}(3,6)$の非零錐、rank4は二つの平面三次Jacobianブロックに由来する。証明は `papers/poisson_cubic_fourfold_moduli.tex`。
- **依存**：主リポジトリ `nc-cubic/papers/sections/poisson_geometry.tex` のPoisson正規形定理（独立再監査は未実施）。そのため、公表完成定理であるとの主張はしない。数学的な帰結の証明と定理の独立監査を区別する。
- **未解決の核心**：各成分のgeneric reducedness、交叉のscheme構造、零Poissonの近傍、成分の境界、および新規性の一次文献照合。
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
