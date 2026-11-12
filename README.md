# nc-cubic2：非可換cubicの独立境界・モジュライ研究

## Codexへの現在の研究指示

**[CODEX_PDF_RECOVERY.md](CODEX_PDF_RECOVERY.md)** に、研究・TeX統合・独立検証・Git追跡解除の原則を定めた。**全原PDFの移管が完了し、Git追跡PDFは0件。**単なるPDFの転記ではなく、重要な定理を強め、証明を洗練し、必要なら新しい結果・一般化・応用を加える。実行前に [研究方針](00_research_plan.md)、[AGENTS.md](AGENTS.md)、[現行のPDF別状態](PDF_SOURCES.md) を読む。数学的成果と再現性を犠牲にしてPDFを削除しない。

## 論文Bから分離した独立成果の統合

[相対復元・有限対角・明示模型の現行稿](papers/relative_reconstruction_models.tex)へ、残る41支持節とノート固有の証明を統合した。既存の点スキーム・Jacobian・一次変形・Artin・étale稿と証明ソースを共用する。全次数MF存在と有限Artin残余復元の系も必要証明付きで保持する。

再開は [専用研究方針](notes/relative_reconstruction_models.md)、全対応は [移管manifest](validation_reconstruction_manifest.json)、組版・有限検算の実行範囲は [validation](validation_relative_reconstruction_models.json)。`python3 scripts/check_relative_reconstruction_models.py --calculations --build` で再現する。数学的な未解決条件・新規性・全独立監査と、ファイル移管の完了を区別する。元側の重複整理は保存確認後に行う。

## 論文Bから分離した点スキームの現行原稿

[混合三次非可換超曲面の点スキームとPoisson零点](papers/mixed_cubic_point_schemes.tex) は、中心三次元の閉公式・証明、点加群の台と非被約構造、平坦閉包、混合係数の衝突と判別式上の局所型をまとめた独立稿である。一般次元の可換復元定理は入力としない。研究再開は [専用ノート・方針](notes/mixed_cubic_point_schemes.md) から。

全文12頁をLuaLaTeXで組版・全頁表示確認し、8TeXファイル、47ラベル、22参照、6引用、2文献項目に未解決・重複はない。4本の有限計算スクリプトを実行し、元の3証明書を正確に再生成した。数学的な全証明の独立監査ではない。検証範囲は [validation_mixed_cubic_point_schemes.json](validation_mixed_cubic_point_schemes.json)。再現は `latexmk papers/mixed_cubic_point_schemes.tex` と `python scripts/check_mixed_point_schemes.py --calculations`。

この移管単位の保存確認後、nc-cubic側の17専用重複ファイルを除外した。論文Aと一般次元の論文Bはnc-cubicに保持し、本文を変更しない。[移管全体の現在の状態](validation_reconstruction_transfer.json) と [独立成果の入力案内](papers/reconstruction_extensions/README.md) は、各独立稿の検証範囲と全体の移管状態を区別する。

## 標識付き平面切断の臨界幾何

[現行稿](papers/marked_hesse_plane_incidence.tex) は、六次Hessian因子、A3退化の四成分、A2/A3臨界値像の導手、A4/D4の明示層、固定源係数の九次分岐式をまとめる。通常の可換幾何の証明と、量子化からの比較入力を区別する。混合形式比較の入力は [形式比較稿](papers/sklyanin_mixed_formal_comparison.tex) に証明を保持し、旧IIもPDF追跡解除済み。全対応は [PDF_SOURCES.md](PDF_SOURCES.md)。

## nc cubic threefoldの17次元モジュライ（現行の主題）

- [現行草稿](papers/nc_cubic_threefold_moduli.tex)：41次元中心三次対、17係数横断形、分離型余次元15、忘却核7（6+1）、混合中心と相対Picard障害。
- [研究ノート](notes/nc_cubic_threefold_moduli.md)：仮定・未解決の既約成分性・再現手順。
- 再現コード：`computations/independent/verify_generic17_slice.py`、`verify_generic17_center.py`、`computations/verify_split_codimension.py`。
- 一般次元ambient復元の定理と証明は `nc-cubic/papers/paper_a.tex`、本稿には同型類判定に必要な証明も保持する。
- **正則正規三次族からの1周期性**：一般$N,d$について最小周期が$\gcd(N,d)$を割る定理と5次元・三次の場合の系を、モジュライ原稿の [周期性節](papers/sections/ambient_periodicity.tex) に証明ごと統合。ambientの1周期性と、商イデアルを保つ周期性を区別する。後者と初出・新規性の確定は未了。
- 構成した17次元族がnc cubic moduli stackの既約成分であることはまだ未証明。

**2026年11月13日・v17。独立した研究内容の正本は本リポジトリの `main`。**

## 六・七次元Poisson cubicの独立なscheme幾何

論文Aの一般次元の主定理に不要な、n=6,7の退化スキーム・
primary分解・Calabi--Yau完全交叉の数値計算を、
[独立LuaLaTeX草稿](papers/poisson_cubic_six_seven_geometry.tex)
へ整理した。7次元rank6で、被約joinと非被約な
embedded primary componentsの横断長8・64、
被約化との差の横断長49が主要な独立研究課題。
[研究ノート](notes/poisson_cubic_six_seven_geometry.md)に
仮定・依存・計算・未解決事項を整理し、退化イデアルの
一般補題・証明全文を同じリポジトリの`papers/sections/`に収録した。
主リポジトリの論文Aには一般次元の結果と依存証明を保持している。

組版：`latexmk papers/poisson_cubic_six_seven_geometry.tex`
数値検算：`python3 computations/verify_poisson_cubic_six_seven_numerics.py`。
移管本文の一致と参照の静的検査、同等のSymPy数値計算を確認。
新稿のLuaLaTeX実組版・PDF目視は未確認。
新規性・primary decompositionの独立監査は未完。

## 全次元Poisson分類の所在

一般次元Poisson pairの成分数・次元公式・固定/相対stackの証明は[主リポジトリ論文A](https://github.com/uedakazushi/nc-cubic/blob/main/papers/paper_a.tex)にある。重複した全次元論文・ノート・専用検算は本リポジトリから除外する。

## VS Code / LaTeX Workshop

リポジトリをVS Codeで**フォルダとして開き**、TeX LiveとLaTeX Workshopを導入する。`.vscode/settings.json` の既定recipeは `latexmk (LuaLaTeX, repository root)`。どの `papers/*.tex` を開いても、リポジトリrootを作業ディレクトリにしてルートの `.latexmkrc` を明示的に読み、生成物は `build/` に置く。TeXを保存するとビルド、手動では `LaTeX Workshop: Build LaTeX project`。ルートから `latexmk papers/nc_cubic_threefold_moduli.tex` などを実行できる。LaTeX Workshopの設定だけではTeX Live自体はインストールされない。

## 新プロジェクト：Poisson cubic fourfold の同時モジュライ

- [研究方針](00_research_plan.md) → [研究ノート](notes/poisson_cubic_fourfold_moduli.md) → [日本語LuaLaTeX草稿](papers/poisson_cubic_fourfold_moduli.tex)
- **集合論的分類はnc-cubic論文Aが正本**。fourfold稿は独自のrank4 generic scheme smoothnessを扱う。
- rank4成分はFermat点のJacobi線形化の階数36からgeneric reducednessも確認。重要な残課題は入力定理の独立検証、rank2と成分交叉のscheme構造、新規性の照合。検算：`python3 computations/verify_poisson_cubic_fourfold_tangent.py`（SymPy）。
- LuaLaTeX：`latexmk papers/poisson_cubic_fourfold_moduli.tex`。GitHub Actions不使用、PDFは生成物としてbuild/へ。

## 現在の研究内容

- `papers/pfaffian_brill_noether_technical.tex`：境界・モジュライ・Pfaffian・Brill–Noether等の大部技術原稿。形式変形・接触分類・Hessian幾何を入力節へ整理し、全次数頂点核と非線形接触分類・同変代数化を追加した。親TeX全体277頁の組版と追加部分の表示、Tate再帰の有理数再構成を確認済み。全証明の外部査読とは区別する。
- `papers/central_fiber_discriminant.tex`：中心三次曲面の必要十分判別式・特異点の解析。対応する正確な記号計算は `computations/verify_central_fiber_discriminant.py`。
- `notes/research_notes.md`：現行の数学的状態、欠けている入力、研究再開手順。

初期の完全TeX転送に加え、PDFにしかなかった固有の証明・反例・再現入力も全件回収した。中心商、中心三次対、Pfaffian接触、全混合量子化を現行論文と厳密計算へ統合し、追跡PDFは0件。有限smoothnessノートも [現行LuaLaTeXノート](notes/ambient_finite_smoothness_and_recovery.tex) と `nc-cubic` に統合済み。対応と実行範囲は `PDF_SOURCES.md`。

## 再現

リポジトリルートから：

```sh
latexmk papers/pfaffian_brill_noether_technical.tex
latexmk papers/central_fiber_discriminant.tex
python3 -m pip install sympy
python3 computations/verify_central_fiber_discriminant.py
```

LuaLaTeX、LuaTeX-ja、HaranoAji日本語フォント、標準数学パッケージが必要。PDF・補助ファイルは `build/` に生成しGit追跡しない。各原稿の配置確認・実組版・数学的監査の状態を区別する。

## nc-cubicとの関係

[uedakazushi/nc-cubic](https://github.com/uedakazushi/nc-cubic) には、論文A（一般次元Poisson構造・代数的量子化）と、論文B（一般次元の中心三次変形の一般点可換復元および必要証明）を保持する。一般点での同値と、特殊点を含む相対smoothness・相対同値の問題は区別する。

主定理に必要な証明は移管先だけへの参照で代用せず、nc-cubicに自立的に保持する。独立した境界・変形論・具体模型は本リポジトリへ、数学的内容と再現性を保って整理する。現行の独立成果は上記統合稿と既存五稿に揃えた。元の重複は移管先保存・入力閉包の確認後に整理する。

GitHub Actionsは使用しない。force pushをしない。Libraryはpush失敗時の緊急避難に限る。

### 中心商特異性・chart貼合せ・特異圏

[中心商原稿](papers/central_quotient_local_models.tex)に、全中心、四つの非可換A1局所模型とBrauer指数6、二中心chartの21特異点と三つのホモロジー的特異点、Karoubi特異圏、球面twist、指定一混合族の正確なtails判別式を整理した。[PBW/CY節](papers/sections/central_quotient_pbw_cy.tex)に定数項変形と周囲の基礎性質も証明した。斉次Sklyaninの標準的性質と楕円境界は既知入力として明示する。

[全中心とAzumaya locus](papers/sections/central_quotient_center_azumaya.tex)では、Rees退化の一般補題と一次文献の仮定を照合した。`computations/verify_center_degree7.py` はQ上の6中心元と交換子rank78、`computations/verify_center_phi_exact.py` は次数18・dim1330・Φ=0を厳密有理数演算で実行確認済み。再現：`python computations/verify_center_phi_exact.py --backend flint --run-all --verify`（python-flintが必要）。

[chart貼合せの証明](papers/sections/central_quotient_chart_gluing.tex)は、行列因子化の分母払いと導分による三切断への帰着を与える。二重étale中心降下、rank6 monic比較、分岐位置、15通常二重点のHessianも明示計算した。検算：`computations/verify_central_quotient_local_hessian.py` と `computations/verify_quotient_exact_tails.py`。

[三次元表現](papers/sections/central_quotient_simple_representations.tex)と[特異圏・twist](papers/sections/central_quotient_categories_and_twist.tex)では、軸上剛性の法29の19次minor、境界正則性、chartのIwanaga–Gorenstein性を現行証明に保持する。全8単純表現のExt表も構造的に証明し、`computations/verify_central_quotient_extensions.py`で代数体上の厳密rankを再実行した。Nakayama twist恒等性は`computations/verify_central_quotient_koszul.py`の全αで有効なFrobenius証明書から従う。

[正確なtails判別](papers/sections/central_quotient_exact_tails.tex)の原稿をLuaLaTeXで組版済み。[一般正則性](papers/sections/central_quotient_global_regularity.tex)と[Cayley幾何](papers/sections/central_quotient_cayley_geometry.tex)も証明・厳密計算付きで回収した。全22節の固有内容を置換できたため、原PDF VI（61頁）を追跡解除した。[削除判定の対応表](PDF_SOURCES.md)を参照。全混合量子化も固有証明と計算を回収してPDF追跡解除済み。

中心三次対（旧V、60頁）も全21節を現行モジュライ論文に統合してPDF追跡解除済み。全係数中心式・規格化の恒等式、軌道rank24、同型判定を厳密検算し、親TeXを組版した。全研究原PDFの移管が完了した。

Pfaffian接触境界（89頁）は全次数頂点核・非線形接触分類・同変代数化を回収し、中心三次技術稿（61頁）は点因子/標準種数5曲線の新稿へ固有部分を回収して、両PDFを追跡解除した。全混合量子化（旧II、195頁）も全19節・§9の57小節を現行ソースへ統合し、最後の原PDFを追跡解除した。

## 混合形式比較の再現

[形式比較稿](papers/sklyanin_mixed_formal_comparison.tex)（21頁）は有限gauge・Artin相対window・積/Serre trace・六級数と平面incidenceを扱う。SymPyで二次原始155型/473係数を毎回生成し、python-flintで四次BCH170131型の閉性・原始・係数1/9と1/18を確認した。旧JSONは入力に使わない。

```sh
latexmk papers/sklyanin_mixed_formal_comparison.tex
latexmk papers/marked_hesse_plane_incidence.tex
python computations/verify_mixed_second_order_gauge.py
python computations/verify_mixed_fourth_order_gauge.py
python computations/verify_mixed_quadratic_dual.py
python computations/verify_mixed_fibre_branch_jets.py
```

生成PDFは `build/` に出力しGit追跡しない。有限hでの比較核の代数化・収束、未知六級数の高次値、無標識分類、新規性の全面調査は継続課題である。
