# Codex実行指示：Cayley–Sklyanin研究の独立移管

**2026-11-13 / v1。未実施の移管指示。正本移転・組版・検算・削除は本書の作成だけでは完了しない。**

- 移管元：`uedakazushi/nc-cubic2` の `main`
- 移管先：`uedakazushi/cayley-sklyanin` の `main`
- 現時点で移管先は作成済み・空のGit repository。着手時に再確認し、必要なら `main` を通常初期化する。
- 移管後の主論文の入口は **`papers/cayley-sklyanin.tex`** とする。原稿の日本語題目はまず「Cayley三次曲面とSklyanin代数」、将来の英文題目候補は *The Cayley Cubic Surface and a Sklyanin Algebra*。タイトルの確定より数学的内容の精査を優先する。

## 実行目標と優先度

**本書を読むだけで終わらず、必要なTeX・完全な証明・再現コード・文献情報・研究方針を移管先に構成してGitHub `main` にpushする。移管先から自足的に再生成できると確認した後に限り、移管元の真の重複を整理して両方の `main` を整合させる。** 不完全なコピーや中間状態を「移管完了」と呼ばない。

Pfaffian–Brill–Noether研究は既に `uedakazushi/pfaffian-brill-noether` に移管済みであり、`nc-cubic2` の共有 `pfaffian_formal_deformations_gluing.tex` は他研究の証明のため保持されている。**今回Pfaffian研究を再移管・削除・改稿しない。** `nc-cubic` 論文A/Bとその必要入力は変更しない。今回の移管を `nc-cubic2` 側の公表再構成より先に実行し、終了後は残る相対復元・非可換三次三様体モジュライ研究に戻る。

## 移管する数学とスコープ

主入口は現行 `papers/central_quotient_local_models.tex`（日本語LuaLaTeX）。その再帰 `\\input` に含まれる次の節を**証明を損なわず**移す。

- `papers/sections/central_quotient_pbw_cy.tex`：三変数Sklyanin定数項変形のPBW、3-CY自己双対解消、指定混合一パラメータ族のKoszul AS正則性とNakayama恒等性。
- `papers/sections/central_quotient_center_azumaya.tex`：四つの中心元・次数18の唯一の関係、Rees退化、Azumaya locus。
- `papers/sections/central_quotient_simple_representations.tex`：1/2次元単純表現の排除、3次元単純表現とExt、中心指標・分裂元。
- `papers/sections/central_quotient_cayley_geometry.tex`：零中心ファイバーのCayley三次曲面と滑らかな反標準楕円境界、Brauer指数6のtwisted NCCR、古典判別式・非被約点加群。
- `papers/sections/central_quotient_categories_and_twist.tex`：四つの局所非可換A1模型、三つのホモロジー的特異点、Karoubi完備な特異圏の三因子分解、3-spherical対象と球面twist。
- `papers/sections/central_quotient_chart_gluing.tex`：行列因子化の縮約、中心chartの貼合せ、導分を用いたperfect性とSerre次元。
- `papers/sections/central_quotient_global_regularity.tex`：分離族の判別式、一般混合・超越的中心値、有限位数楕円境界の正則な開集合。
- `papers/sections/central_quotient_exact_tails.tex`：一混合族の正確な判別式 `(alpha^3+9)(28 alpha^3+243)`、零点での無限大域次元、全affine中心値の条件。

必要な独立した補助論文 `papers/central_fiber_discriminant.tex`（中心曲面の滑らかさの必要十分条件と特異点）も統合・別稿維持の価値を判断して証明を保持する。**`cayley-sklyanin.tex` は新しい論文入口とし、旧親原稿を参照するだけで代用しない。**

必ず保全する主要な数式・結果：
1. `R_1=C<X,Y,Z>/([X,Y]-Z²,[Y,Z]-X²-1,[Z,X]-Y²)` と中心 `Z(R_1)=C[g,U,V,W]/(Phi)` の厳密な全中心同定。楕円Sklyaninの既知斉次中心定理と新しい有理数計算を区別。
2. `D_0=R_1/(g)` の中心がCayley三次曲面の反標準楕円曲線補集合であり、四つのA1点で `Mat_3(End_R(R⊕I))` / `Mat_3(C[[a,b]]⋊{±1})` となること。
3. 一般中心分数体上の次数6の斜体、Brauer指数6、通常の`End_C(M)`型ではないtwisted NCCR。
4. 混合族の二中心chartでの**21個の中心特異点と3個のホモロジー的特異点の不一致**、15個はnode、残る6点はHessian rank1であること。
5. 特殊パラメータ `28 alpha³+243=0` での `D_sg(qgr A_alpha)^Kar ≅ Perf_{Z/2}(C)^⊕3` の正確な圏の定義、Karoubi完備化、三因子の所在・K₀。
6. 指定一混合項族に対する`qgr C_alpha`大域次元2／`qgr A_alpha`大域次元3の必要十分な判別式、古典三次三様体の滑らかさだけでは検出できない量子正則性の障害。
7. `alpha=1`での3-spherical objectと、構造対象をどの`O(m)[r]`にも移さないtwist。これは「標識なしの非可換三次超曲面の完全復元が不可能」という主張とは異なる。
8. 証明に依存するPBW/CY、rank6の中心平坦比較、二重étale基底変更、Iwanaga–Gorenstein性・局所化と有限射影行列因子化・完備化・Knörrer周期性の**必要仮定と証明**。

## 計算・参考文献・実行環境

移管元の以下のコードを調査し、現行結果の再現に必要な最小集合を移管先の `computations/` へ持つ：

`verify_center_degree7.py`, `verify_center_homogeneous_symbols.py`, `verify_center_phi_exact.py`, `verify_central_fiber_discriminant.py`, `verify_central_quotient_reps.py`, `verify_central_quotient_extensions.py`, `verify_central_quotient_local_hessian.py`, `verify_central_quotient_koszul.py`, `verify_central_quotient_global_geometry.py`, `verify_quotient_exact_tails.py`。他に親原稿が依存する `verify_center_parity_candidates.py`, `verify_center_weight18_mod101.py`, `verify_central_symmetry.py` 等も内容を確認して必要なら取り込む。共通コードが他論文でも使われる場合は**元側に保持**し、移管先の独立再現に必要なら最小限複製する。大規模中間出力・旧版・キャッシュは不要。既存コードが報告する過去のPASSを今回の独立実行済みと混同しない。

`nc-cubic2` の `README.md`, `papers/README.md`, `notes/research_notes.md`, `00_research_plan.md`, `PDF_SOURCES.md` の中心商固有の数学・未解決点・書誌参照を、新しい現行研究方針／研究ノート／論文へ**内容として統合**する。旧PDF・旧版対応表は移さない。参考文献はRains、Etingof–Ginzburg、Walton–Wang–Yakimov、Iyama–Wemyss、Van den Bergh、Orlov/Knörrer等の**一次資料を適用条件つきで**調査し、初出・新規性が未確認なら明記する。先行研究の結果を本研究固有の定理として誤表示しない。

新リポジトリに `00_research_plan.md`, `AGENTS.md`, `notes/research_notes.md`, `README.md`, `papers/cayley-sklyanin.tex`, 共通入力節、検算コード・実行手順、最小限の文献情報、`.latexmkrc`, `.vscode/settings.json`, `.gitignore` を整備する。日本語LuaLaTeX／LuaTeX-ja、`latexmk papers/cayley-sklyanin.tex`、`build/`出力、SyncTeX有効、PDFは非追跡。GitHub Actionsなし。

## 移管元に残すべき数学と厳格な削除ゲート

- `papers/nc_cubic_threefold_moduli.tex` と `papers/sections/central_pair_*.tex`、`papers/mixed_cubic_point_schemes.tex`、`papers/diagonal_cubic_point_geometry.tex`、`papers/relative_reconstruction_models.tex` 等の**現行の独立論文**を保護する。中心商論文のPBW/中心性/Bertini/有限正則性の証明を、これらが必要とする場合は移管元の適切な節に証明ごと保全する。移管先への外部リンクだけで主論文の必要証明を置換しない。
- `nc-cubic`論文A/Bとの既存のスコープを維持する。一般Poisson分類／全次元量子化を再移管しない。
- `nc-cubic2`の現行TeX全文を検索し、`\\input`、`\\ref`、`\\cite`、計算の呼び出し、数学的な直接依存を確認。削除可能と判断する前に、残存する論文単独で入力閉包が成立するよう補題や証明を**内容として統合**しておく。
- **移管先のmainに全数学を保存・確認できる前に、元の原稿・節・計算コードを消さない。** その後も、他論文が依存しているファイルを不用意に削除しない。Gitの履歴は残るが、研究の再開を履歴復元に依存させない。
- 参照・式番号・bibliography・`latexmk`全組版・必要な厳密計算を検査する。証明記載・今回の独立監査・実行した計算・PDF表示を区別して報告し、未実施なら未実施と明示する。
- 新しい正本への移管後、`nc-cubic2`の `AGENTS.md`、`00_research_plan.md`、`README.md`、`papers/README.md`、`notes/research_notes.md`、`PDF_SOURCES.md`、`CODEX_PDF_RECOVERY.md` を現行状態に整理する。過去の移管履歴を日誌として蓄積せず、必要最小限の現行所在・再現情報だけを残す。

## 実行順序と成果物の検証

1. 両repoの最新 `main` と実際の`git ls-files`を読み、移管先が空なら初回コミットで初期化。移管元にこの指示以外の未コミット変更があれば内容を保護する。
2. `cayley-sklyanin` に自足した現行研究bundleを作り、構造的・静的入力検査を行う。**まず移管先`main`へ通常fast-forward pushし、遠隔HEAD/blobを確認。**
3. 現行論文・検算を必要な範囲で実行。完全な出典監査が未了でもその状態を正直に記録し、原稿の証明・再現性を損なわない。
4. 移管元に残る他論文の証明依存を確保し、実際に真の重複になった専用ファイルだけを削除。残存TeX／計算の参照・組版を再検査して`nc-cubic2/main`へpush。
5. 両repoの遠隔HEAD、現行入口、削除／保持ファイル、検査の実行結果、数学の未監査項目を報告。移管先へのpush失敗時は移管元の削除を停止し、失敗を明記する。

**禁止：** force push、GitHub Actions、履歴書換え、旧版ZIP・入れ子アーカイブ、不要なPDFのGit追跡、完了を装う報告。LibraryはGitHub pushに実際に失敗したときの緊急退避に限る。

## 移管後の研究方針

中心的な論文として `cayley-sklyanin.tex` を磨く。優先する監査は（i）全中心とAzumaya証明、（ii）21対3の局所モデルと特異圏の三因子分解、（iii）正確な量子的判別式と球面twist、（iv）一次資料の新規性。次の研究課題は一般混合係数の判別式、Brauer類のsymbol／stack表示、標識なし復元。目標や論文構成は数学的重要性・新規性・理解・正確性・実現可能性に応じて柔軟に更新する。原稿は現行成果を理解しやすく配置し、証明を削らない。
