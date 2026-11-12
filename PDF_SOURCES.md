# 現行PDF原資料と保持の基準（2026-11-12 / v1）

本文の軽い検査は、GitHubから取得可能な6 PDFの目次（PDF outline）と現行TeXの節・見出しの照合に基づく。PDFの全数式・証明・図の本文突合は実施していない。1MBを超える2 PDFはGitHub contents APIの制限でbase64本文を取得できず、内容を検査できなかった。本文未確認のまま数学的に独立な成果がないとは推論しない。

## 現行mainに保持する原資料（6件）

- `notes/pdf-only/finite_smoothness_notes.pdf`：34頁。PBW/中心/相対正則性と非連結dg加群のperfectness反例。反例第23節はnc-cubicの`notes/source_recovery/dg_perfectness_counterexamples.tex`に独立TeX化済みだが、残余のTeX完全収録を未確認。
- `papers/pdf-only/ambient/central_cubic_technical.pdf`：61頁。中心三次式、点加群、有限PI中心、正則性、混合量子化等。nc-cubic論文Aや現行モジュライ原稿と重なるが、全内容の移管は未確認。
- `papers/pdf-only/ambient/central_pair_formal_moduli.pdf`：60頁。中心三次対の全Artin形式局所構造、構造代数層・斉次環比較、忘却射の4次元ファイバー。17次元モジュライとの関係が強く、重要性を優先して本文監査する。
- `papers/pdf-only/boundary/central_quotient_singularities.pdf`：61頁。中心商の正則性・判別式、A1局所模型、Cayley cubic、非可換特異圏。現行TeX `papers/central_fiber_discriminant.tex` は判別式の一部のみで、全面代替ではない。
- `papers/pdf-only/boundary/pfaffian_contact.pdf`：約1.1MB。本文取得・詳細確認は未完了。Pfaffian/contactの独自成果がある可能性を残し、削除不可。
- `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf`：約2.0MB。本文取得・詳細確認は未完了。混合Sklyanin量子化の独自証明がある可能性を残し、削除不可。

## 追跡解除した資料（現行bundleには不要と判断）

- `notes/pdf-only/categorical_boundary_notes.pdf`（16頁）：研究の辞書・主張索引・未解決課題・共通の中心三次構造の比較を主に整理した資料。新しい独立定理の存在は目次から確認できず、現在の研究方針と各repoの現行ノートの説明に比べ追加の公表価値を見込まない。
- `papers/pdf-only/boundary/brill_noether.pdf`（58頁）：主要な章は現行 `papers/pfaffian_brill_noether_technical.tex` に節・証明付きで収録される。内容の完全同値性を保証する精査ではなく、現行TeXを正本とする厳しめの保存価値判断。

Git追跡解除後も旧Git commitにはこれらのblobが存在するが、復元を前提にしたアーカイブは本bundleに作らない。

## 次に移すべき重要な内容

(1) `central_pair_formal_moduli.pdf`の全Artin形式局所比較・忘却射の幾何を `papers/nc_cubic_threefold_moduli.tex` の既存の主張と重複照合する。(2) `central_quotient_singularities.pdf`の非可換A1特異点の局所模型と特異圏を `papers/pfaffian_brill_noether_technical.tex` と照合する。(3) 未読のPfaffian/SklyaninのPDFを全文抽出して独自の定理・証明を判定する。内容の未検証な再構成はしない。

## 現行TeXの照合先（2026-11-12）

Pfaffian・Brill--Noether大部原稿の79節を、既存内容を移動するだけで5個の主題別入力に分割した。これにより`central_pair_formal_moduli.pdf`は`papers/nc_cubic_threefold_moduli.tex`と`papers/sections/pfaffian_formal_deformations_gluing.tex`、`central_quotient_singularities.pdf`は`papers/central_fiber_discriminant.tex`と比較する対象が明確になった。PDFとの完全同一性を証明したわけではないため、残る6件のPDFはすべて保持する。
