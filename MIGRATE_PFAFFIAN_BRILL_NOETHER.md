# Codex実行指示：Pfaffian–Brill–Noether独立研究の移管

**2026-11-13 / v1。作業状態：未実行（本書は作業指示であり、移管完了の報告ではない）。**
**移管元：** `uedakazushi/nc-cubic2`、`main`。
**移管先：** `uedakazushi/pfaffian-brill-noether`、`main`。
移管先は作成済みで、指示作成時点では空のGitリポジトリである。着手時に両remoteの現状を再取得し、空であれば移管先の`main`を初期化する。既にコミットがあればその内容を保護し、既存`main`に通常のfast-forwardで追加する。

## 最重要の実行目標

**計画だけで終わらず、新リポジトリに現在有効な全Pfaffian–Brill–Noetherの数学・証明・必要な計算を移し、自足的な研究継続・LuaLaTeX再生成・GitHub保存を確認した後、移管元から検証済みの真の重複だけを整理する。** 途中で両方の作業用リポジトリを編集できる環境を確保し、両remoteの`main`を確認すること。移管元のGit履歴は保存されるので、履歴保存用ZIP・旧原稿・全履歴のコピーは作らない。

この移管が終わるまで、`nc-cubic2`の相対復元244頁統合稿の公表再構成より**先に**実行する。移管完了後は旧優先課題へ戻る。`nc-cubic`の論文A/Bには変更を加えない。

## 1. 数学的資産の所在とスコープ

移管元の現行入口は `papers/pfaffian_brill_noether_technical.tex`（記録上277頁）。この親ファイルの再帰的`\\input`と`\\ref`・`\\cite`を実際に検査する。まず下記の**全て**を対象として内容を調べる（単なるファイル名のコピー判定にしない）。

- `papers/pfaffian_brill_noether_technical.tex`
- `papers/sections/pfaffian_formal_deformations_gluing.tex`（約4736行。非可換cubicの一般形式変形・残余圏・gluingとPfaffian/Brill–Noether固有部分が混在するので特に慎重に扱う）
- `papers/sections/brill_noether_boundary_geometry.tex`
- `papers/sections/pfaffian_contact_low_order.tex`
- `papers/sections/pfaffian_contact_high_order.tex`
- `papers/sections/pfaffian_vertex_structure.tex`
- `papers/sections/pfaffian_contact_classification.tex`
- `papers/sections/pfaffian_equivariant_algebraization.tex`
- `papers/sections/pfaffian_hessian_geometry.tex`
- `papers/sections/pfaffian_computation_audit.tex`
- `computations/verify_pfaffian_vertex_and_tate.py` と、**実際に現行証明を再現するため必要な**他のコード・入力・証明書

`notes/research_notes.md`、`00_research_plan.md`、`README.md`、`papers/README.md`、`PDF_SOURCES.md`、`CODEX_PDF_RECOVERY.md`のPfaffian固有の有用な数学的情報を読み、新リポジトリの現行研究ノート・研究方針・原稿へ**内容として**統合する。旧PDFや旧版対応表を新リポジトリへ移植しない。文献リストは親TeXから必要な一次資料・書誌・適用箇所を抽出し、他主題の不要な大量引用を持ち込まない。

必ず保持する主要数学：
- 三次三様体`X=V(F)⊂P^4`とKuznetsov成分の特定対象、その10次元変形・Brill–Noether境界、相対Picard・評価核・gluingとの関係。
- 六次Pfaffian接錐`H_X=V(F(q(a)))⊂P^9`、重複度6、特異部分、解消、6-jet Torelli、内在的blowupによる偏極三次三様体の復元。
- Pfaffian共変量・接触像・高次数の頂点核・Schur/Bott/Čech–Koszul比較、通常接触商の全次数、非線形形式分類・有限決定性。
- 実際の境界のTate行列分解・再帰・係数`1/96`のHessian補正、`P_F+H_{10}/96`への形式右同値と**仮定を満たす範囲での**同変代数的/解析的実現。
- 五変数`F+c det Hess(F)`のMilnor数32、非零係数のTjurina数31、Pfaffian graph・二次ファイブレーション。
- これらに不可欠な定理・完全な証明・反例・例・再現困難な整数入力/有限証明書。以前の大規模rank実行の元データが現行treeに欠けている点も明記し、未検証結果を今回検証済みにしない。

## 2. 共有成果を壊さない境界の分離

`pfaffian_formal_deformations_gluing.tex`には、Pfaffian/Brill–Noether固有ではない中心三次の形式変形空間、Poisson/量子化、Kuznetsov成分、gluing bimoduleなどの結果が混在する。**まず移管先に必要な本文を証明ごと完全に確保**すること。その上で各定理の依存先を特定する。

- Brill–Noether特有の境界・incidence・復元・Pfaffian接触の成果は移管先を唯一の現行正本とする。
- `nc-cubic2`の17次元非可換cubicモジュライ、相対復元、点スキーム・他の論文にも必要な一般結果や証明は、移管元の対応する現行原稿で**自足的に保持**する（必要なら適切な節に統合する）。単に移管先へのリンクで必要証明を代用しない。
- 最初は共有節の重複を許して可用性と組版を確立し、**両者の入力閉包と依存関係を確認した後**、数学的に真の重複だけを除去する。重要な主張を「長い」「以前の履歴にある」だけで削らない。一般Poisson分類と量子化の正本は`nc-cubic`論文Aであり、同じ一般定理を新リポジトリの独立成果と偽って再収録しない。
- 移管前の`nc-cubic2`の`main`を保護し、作業途中で同名共有ソースを削除しない。現行統合稿および`nc_cubic_threefold_moduli.tex`やその入力を不用意に変更しない。

## 3. 移管先の独立した研究構成

`pfaffian-brill-noether`には、再開時に最初に読む`00_research_plan.md`、必要十分な`notes/research_notes.md`、`AGENTS.md`、`README.md`、論文ソース、引用文献・計算コード/入力、LuaLaTeX・LaTeX Workshopの`.latexmkrc`と`.vscode/settings.json`、`.gitignore`を整備する。日時・版番号・主張の状態・具体的な再現コマンドを整合させる。PDF/SyncTeX/build等は`build/`に生成し、Gitで追跡しない。GitHub Actionsは使用しない。

論文の自然な候補は
(a) `papers/brill_noether_boundary_torelli.tex`：Brill–Noether境界の接錐、特異性・解消・6-jet/内在Torelli、
(b) `papers/pfaffian_contact_normal_forms.tex`：全次数接触分類・頂点核・Tate/Hessian補正・代数化。
ただし**二本という固定ノルマではない**。数学的重要性・論理的まとまり・証明の自足性を優先し、初期段階で現行親TeXをそのまま動作可能にしてもよい。分割はその後に行い、中心定理・必要証明・有用な具体例を一切失わない。日本語LuaLaTeXで、論文は研究史の追記ではなく読者に理解しやすい構成へ改稿する。

公表用論文のIntroductionでは、既知の三次三様体categorical Torelli、安定対象モジュライ、Pfaffian/Pfaffian local cohomology、Artin近似、接触分類の一次資料と本研究固有の貢献を正確に区別する。既知結果から自動的に従う部分や新規性未確認の部分を明記し、未確認の出典・定理番号を推測しない。

## 4. 数学的監査と再現性の関門

- 原稿に証明があること／今回その証明を独立に点検したこと／計算を実際に再実行したこと／組版・PDF表示を確認したことを別々に記録する。
- 全次数接触商と頂点核のSchur分解、Pieri・Bott、局所コホモロジー、Čech–Koszul比較、非被約係数基底の扱いを優先して独立監査する。特に相対Picardと評価核、二段blowup、6-jet Torelli、`1/96`、Artin/Bierstone–Milman近似の**正確な仮定**を照合する。
- 旧高次rankの巨大行列・整数証明書は現行treeに欠けているものがある。新しい再現器が証明に必要なら最小限のコード・入力/厳密証明書を作るか、数学的証明だけに依存する箇所を明確にする。有限体での非零minorは特性零の下界であり、有限体での零だけを普遍恒等式の証明としない。
- `latexmk`による**移管先の全論文入口の実組版**（可能な場合）、再帰`\\input`・`\\ref`・`\\cite`・`\\bibitem`の閉包、PDF全頁の欠損/可読性、必要な計算の実実行を確認する。実行できない環境・失敗は明示する。以前の277頁の成功記録を移管先での成功と混同しない。
- 簡潔な現行validation/再現手順だけを保持する。過去の版、移管作業日誌、巨大な中間出力、旧PDF、キャッシュ、ZIP、不要な重複は追跡しない。移管履歴はGitが保持する。

## 5. 保存と移管元の削除ゲート（必ず順番を守る）

1. 両リポジトリの最新`main`を取得。移管先が空なら`main`を通常初期化し、既存内容がある場合はその上へ統合する。認証済みの両remoteに書き込めることを事前確認する。
2. 移管先で必要TeX・文献・ノート・計算資産と指示一式を構成し、内容の完全性と最低限の静的検証を確認し、**最初の成果を移管先`main`へfast-forward pushして遠隔blob/HEADを確認**する。GitHub上の存在確認は必須。
3. 移管先で必要な組版・計算を行い、欠落/参照切れを修正し、数学の依存監査状況を明記して再度pushする。未監査が残っても正確に区別し、証明本文を削らない。
4. この時点で、移管元のPfaffian専用原稿・節・検算などから**他の現行論文に必要な内容を分離・保存したことを検証したファイルだけ**を`git rm`する。移管元の`README.md`・`00_research_plan.md`・`AGENTS.md`・`notes/research_notes.md`・`papers/README.md`・`PDF_SOURCES.md`・`CODEX_PDF_RECOVERY.md`の該当箇所を現行の正本所在へ整合的に更新する。不要な移管指示も両リポジトリの今後の再開に不要なら整理する。
5. 移管元の残る論文入口の入力閉包・静的チェック・必要組版を再検査し、`nc-cubic2`の`main`へ通常のfast-forward push。移管元・移管先の遠隔HEADと削除/保持ファイルを再確認する。**移管先へのpushや検証が失敗したなら、元の専用ファイルを削除しない。**

GitHub Actions禁止、force push/履歴書換え禁止、ユーザー確認待ちで停止せず可能な範囲で実作業を進める。リポジトリの権限・ネットワーク・組版環境で実行不能なら、失敗の位置と残した安全な状態を正確に報告する。Library保存はGitHub pushに実際に失敗したときだけの緊急退避とする。

## 6. 完了報告の要件

`pfaffian-brill-noether/main`と`nc-cubic2/main`の**実際に確認したコミットSHA**、現行二論文（または妥当な再構成）の中心結果と参照先、移管元から削除したもの／一般証明として保持したもの、TeX組版・必要計算の実行結果、未監査・欠けた証明書・文献の残課題を簡潔に報告する。新リポジトリが空のまま、コピーのみ、または元の削除のみで「移管完了」としない。
