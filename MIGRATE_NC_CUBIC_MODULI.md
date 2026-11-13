# Codex実行指示：17次元非可換cubic threefoldモジュライ研究の独立移管

**2026-11-13 / v1。状態：移管指示のみ。論文・証明・コードの移管は未実行。**

- 移管元：`uedakazushi/nc-cubic2` の最新 `main`
- 移管先：`uedakazushi/nc-cubic-moduli` の `main`（作成済み、指示作成時点では空）
- 最重要成果：移管先に現在有効な自足した研究一式を作成・検証・pushし、その保存を確認してから移管元の真の重複だけを除去する。
- **注意：移管先は public、移管元は private。** 移管前に全原稿・計算・ノートの公開適否を確認し、認証情報、非公開の第三者資料、不要な内部資料や他プロジェクトの非公開内容を移さない。研究の公開に適さない必須素材がある場合は公開リポジトリへのpushを保留し、理由を報告する。論文の証明の削除・隠蔽による対処は禁止。
- `nc-cubic` 論文A/B、`pfaffian-brill-noether`、`cayley-sklyanin` の現行正本を変更しない。GitHub Actions、force push、履歴の書換えを行わない。

## 数学的目標と論文の位置づけ

研究の中心は**非可換cubic threefoldの真の17次元同型類族とそのモジュライ成分性**。次を明確に分ける：
1. 中心三次対の41次元既約incidence族、18次元放物型群に横断する17係数正規形、31次整数minorと同型類分離、分離型の余次元15、可換cubicへの忘却核7=6+1。
2. 固定ambientを動かす問題、混合中心元、二次包絡と偏極付き復元、固定剛体ambient上の四係数族、相対Picard障害。
3. **可換点での形式局所環は41次元・接空間44次元、商sliceは17次元・接空間20次元**。17次元の滑らかなモジュライという主張にはしない。通常の古典的Artin変形関手とderived moduliも区別する。
4. Koszul AS正則な`\mathbb Z`-代数と正則正規次数`d`超曲面から得る周期性定理（最小周期は`gcd(N,d)`を割る）：`N=5,d=3`ではambientの1周期性。ただし**中心三次商イデアルの保存・全非可換cubicの1周期化は未証明**。この結果の他論文における依存先を保護する。
5. **最重要未解決：構成した17次元族の閉包が、適切に定義した非可換cubic moduli stackの既約成分となるか。** 一般点の接空間・障害、scheme-theoretic generic reducedness、stackと粗商、相対Poisson pairからの量子化の代数化・貼合せを検討する。一般Poisson構造の分類・量子化は`nc-cubic`論文Aの既知入力であり、既に示された17次元の同型類の存在と成分性を混同しない。
6. `qgr`の偏極付き三つ組、構造対象を保つ導来同値、無標識導来圏の同値を区別する。Serre関手だけによる復元や任意のnc cubicの分類を未証明のまま完成結果にしない。

## 読むべき現行資産・移管対象

着手時に必ず最新treeと再帰`\\input`を再取得し、対象ファイルが現存することを確認する。まず以下を読んで、重要な主張・証明・例・反例・文献の依存を全て把握する：

- 主原稿：`papers/nc_cubic_threefold_moduli.tex`（現行で約40頁と記録。これを移管先で`papers/nc_cubic_threefold_moduli.tex`として再構成してよい）。
- 主研究ノート：`notes/nc_cubic_threefold_moduli.md`。
- 現行の主原稿入力：`papers/sections/central_pair_explicit_centers.tex`、`central_pair_generic_component.tex`、`central_pair_diagonal_classification.tex`、`mixed_center_picard.tex`、`ambient_periodicity.tex`、`central_pair_artin_formal_moduli.tex`、`central_pair_mixed_derived_rigid.tex`、`central_pair_finite_order_regularity.tex`。すべて`papers/sections/`以下。後者はCayley–Sklyanin移管時に**他論文の証明を保護するため残した現行の必要補題**であり、削除可否を特に慎重に判定する。
- 他論文と共有する証明：`papers/relative_reconstruction/mixed_center_picard.tex`、`papers/relative_reconstruction/central_symmetry_lifting.tex` と対応ノート。新稿への参照だけで元側の必要証明を失わせない。
- 主要計算：`computations/independent/verify_generic17_slice.py`、`computations/independent/verify_generic17_center.py`、`computations/verify_split_codimension.py`、`computations/verify_central_pair_centers.py`、`computations/verify_central_pair_orbits.py`、`computations/verify_central_symmetry.py`、`computations/central_symmetry_certificate.json`。引用・計算の呼び出しから追加の必要資産を探索する。
- `00_research_plan.md`、`README.md`、`AGENTS.md`、`papers/README.md`、`PDF_SOURCES.md`のうち17次元モジュライ固有の研究方針・証明依存・未解決事項を、**旧版記録ではなく現在有効な数学的内容として**新方針・研究ノートに統合する。

非可換cubicの一般Poisson分類・ambient復元の正本は`nc-cubic`論文A、一般点可換復元は同論文Bにある。移管先の主原稿が自足するために必要な補題・証明は保持するが、別原稿の独立主結果を新規発見として重複収録しない。一次文献の実物から仮定・適用箇所を確認する。新規性が未確認の定理・書誌は未確認と記載する。

## 移管先の構成と研究の継続

`nc-cubic-moduli`の`main`を必要なら初期化し、研究再開の入口として`00_research_plan.md`、`AGENTS.md`、`README.md`、`notes/research_notes.md`と必要な専用ノート、完成形を意識した日本語LuaLaTeX主論文を配置する。主論文の推奨入口は`papers/nc_cubic_threefold_moduli.tex`。ファイル名は簡潔でdescriptiveに保ち、論文の数を固定せず、公表価値で構成を再検討する。論文には中心結果・正確な仮定・完全な証明・一次文献との比較を置く。研究ノートには未完成の着想・本質的障害・有用な反例・計算のみを整理し、本文の証明を重複させない。

`.latexmkrc`、`.vscode/settings.json`（VS Code LaTeX Workshop、LuaLaTeX、SyncTeX、root起点build）、`.gitignore`、再現に不可欠な最小限の`computations/`・入力・証明書を整える。生成PDF・中間生成物・旧ZIP・過去版はGitで追跡しない。外部GitHub Actionsを使用せず、ローカルまたはCodex環境で`latexmk papers/nc_cubic_threefold_moduli.tex`を実行できるようにする。

## 厳密な移管・削除ゲート

1. **移管先を先に構築してpush：** 両repoの最新`main`を読み、空repoなら初期化する。主原稿・全必要入力・完全証明・研究ノート・文献・計算を移管し、まず`nc-cubic-moduli/main`へ通常のfast-forward push。遠隔HEAD、tree、blobを確認する。独立した検証記録を保存する。
2. **移管先で検査：** 再帰`\\input`、`\\ref`、`\\cite`、bibliographyとファイル実在性を調べる。LuaLaTeX全組版・PDFの可読性と主要数学箇所、31次minor、中心恒等式、群作用、接空間・変形計算等の厳密再現コードを**実際に動かし**検証する。未実行・失敗は明確に残す。コード計算と全数学的証明の独立監査を区別し、未証明部分は正直に記載する。今までの計算記録を今回の検証結果と取り違えない。
3. **依存調査：** `nc-cubic2`の残る主原稿（特に相対復元244頁、点スキーム、Jacobian復元、一次変形、Artin・étale、混合形式比較）から移管対象への`\\input`／`\\ref`・コード実行・数学的依存を全文検索。新たに残すべき結果・証明は元側の適切な原稿・ノートへ保持する。共有証明を削除せず、移管先へのリンクを証明の代用としない。
4. **元側を整理：** 移管先の独立再現・pushを確認してから、専用原稿・ノート・専用検算等の**真の重複だけ**を元側から除去する。元側`README.md`、`00_research_plan.md`、`AGENTS.md`、`papers/README.md`、`notes/research_notes.md`、必要な検証資料を、新たな正本所在と残存する研究の優先順位に整合させる。元の他の論文を再組版・再検証し、`nc-cubic2/main`へ通常fast-forward push。
5. **最終確認：** 両repoの最終HEAD SHA、移管先の論文・ソース・計算の実在、移管元の削除・残存、実際に実行した組版と計算、主張の状態・未監査箇所を報告。移管先のpush/検証が失敗したら、移管元からの削除を停止する。

**禁止事項：** force push、GitHub Actions、不要なPR、PDF追跡、入れ子ZIP、履歴書換え、移管済み旧版のアーカイブ化、計算の実行結果や証明の監査済み状態の捏造。GitHubの最新mainを正本にし、LibraryはGitHub pushに実際に失敗した時だけ緊急退避。研究の大きな方向変更が必要な場合、現方針と元の目標の達成／未解決を簡潔に整理して現行研究方針を書き直し、作業日誌を蓄積しない。

## 移管後の最優先研究課題

まず17次元の`nc cubic`同型類族がモジュライの既約成分になるか、必要なstackの定義と代数性、一般点での変形障害・接空間、量子化からの相対族の貼合せ・降下を調べる。真の中心三次対のモジュライと無標識`qgr`モジュライの違い、可換点の非被約・特異な局所構造と一般点のgeneric reducednessを切り分ける。研究全体の数学的重要性・新規性・正確性・実現性を評価しながら、論文の中心定理と優先順位を更新する。ユーザーの再確認待ちで停止せず、できる範囲の検証・pushまで実行する。
