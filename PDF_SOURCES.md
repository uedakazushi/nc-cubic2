# 現行PDF原資料と保持の基準（2026-11-12 / v3）

Libraryに保全されている同名・同バイトサイズのPDF原本から本文を抽出して確認した。これはGitHub上のblobそのもののバイト一致を検証したという意味ではない。原本の全定理・証明と現行TeXの完全同値性はまだ立証していない。特に旧論文III・V・VIおよび195頁のIIは、独自の結果が多数含まれる。

## 現行mainに保持する原資料（5件）

- `papers/pdf-only/ambient/central_cubic_technical.pdf`：61頁。中心三次式、点加群、有限PI中心、正則性、混合量子化等。nc-cubic論文Aや現行モジュライ原稿と重なるが、全内容の移管は未確認。
- `papers/pdf-only/ambient/central_pair_formal_moduli.pdf`：60頁。中心三次対の全Artin形式局所構造、構造代数層・斉次環比較、忘却射の4次元ファイバー。17次元モジュライとの関係が強く、重要性を優先して本文監査する。
- `papers/pdf-only/boundary/central_quotient_singularities.pdf`：61頁。中心商の正則性・判別式、A1局所模型、Cayley cubic、非可換特異圏。現行TeX `papers/central_fiber_discriminant.tex` は判別式の一部のみで、全面代替ではない。
- `papers/pdf-only/boundary/pfaffian_contact.pdf`：89頁。旧論文III。普遍同変摂動の非線形接触分類と全次数頂点核の明示結果は未移管。Hessian五変数模型（Milnor数32、Tjurina数31）・Pfaffian graph上のstrict transformと相対二次ファイブレーションは `papers/sections/pfaffian_hessian_geometry.tex` に命題・証明を復元済み。残りの主結果を移管・監査するまで削除不可。
- `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf`：195頁、旧論文II。全21混合方向の形式可換対応、臨界層とA2/A3/A4/D4型退化、点加群・種数5曲線を含む。現行TeXにない証明が多いため、現時点で最も注意して移管すべき原資料の一つ。

## 追跡解除した資料（現行bundleには不要と判断）

- `notes/pdf-only/finite_smoothness_notes.pdf`（34頁）：研究ノートとして整理・再開上の意義はあるが独立した公表論文としての価値は低い。超越的中心値での正則性、二つの中心chart、偏極付き復元、同型判定、完備dg障害について `notes/ambient_finite_smoothness_and_recovery.tex` に有効な命題・証明要点と適用仮定を統合。一般のPBW・dg反例の完全な証明はnc-cubic側が正本。数式の独立監査は未完了。
- `notes/pdf-only/categorical_boundary_notes.pdf`（16頁）：研究の辞書・主張索引・未解決課題・共通の中心三次構造の比較を主に整理した資料。新しい独立定理の存在は目次から確認できず、現在の研究方針と各repoの現行ノートの説明に比べ追加の公表価値を見込まない。
- `papers/pdf-only/boundary/brill_noether.pdf`（58頁）：主要な章は現行 `papers/pfaffian_brill_noether_technical.tex` に節・証明付きで収録される。内容の完全同値性を保証する精査ではなく、現行TeXを正本とする厳しめの保存価値判断。

Git追跡解除後も旧Git commitにはこれらのblobが存在するが、復元を前提にしたアーカイブは本bundleに作らない。

## 次に移すべき重要な内容

(1) `central_pair_formal_moduli.pdf`の全Artin形式局所比較・忘却射の幾何を `papers/nc_cubic_threefold_moduli.tex` の既存の主張と重複照合する。(2) `central_quotient_singularities.pdf`の非可換A1特異点の局所模型と特異圏を `papers/pfaffian_brill_noether_technical.tex` と照合する。(3) 未読のPfaffian/SklyaninのPDFを全文抽出して独自の定理・証明を判定する。内容の未検証な再構成はしない。

## 現行TeXの照合先（2026-11-12）

Pfaffian・Brill--Noether大部原稿の79節を、既存内容を移動するだけで5個の主題別入力に分割した。これにより`central_pair_formal_moduli.pdf`は`papers/nc_cubic_threefold_moduli.tex`と`papers/sections/pfaffian_formal_deformations_gluing.tex`、`central_quotient_singularities.pdf`は`papers/central_fiber_discriminant.tex`と比較する対象が明確になった。PDFとの完全同一性を証明したわけではないため、残る5件の論文PDFはすべて保持する。

## 旧論文IIIから追加でTeX化した重要結果

2026-11-12：旧論文III§23–24の五変数Hessian摂動のMilnor環/Tjurina環とPfaffian graph上の解消模型・相対次元5の二次ファイブレーションを `papers/sections/pfaffian_hessian_geometry.tex` に証明を添えて復元し、親原稿の `\\input` に編入した。原稿に証明を記載したことと今回の独立再監査は区別する。旧論文III§21–22の非線形接触分類、§10の `K^nor` と `E_vert` の全次数決定は別途原文・証明照合が必要。これらは現行長大TeXの最終節で未解決と扱われていたため、旧PDFの主張を無条件に論文全体の確定定理へ昇格させない。
