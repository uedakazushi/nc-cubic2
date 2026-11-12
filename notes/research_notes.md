# 研究ノート：境界研究の現在の知識と障害

**2026-11-12 / v3**

- 独立の大部原稿は `papers/pfaffian_brill_noether_technical.tex` に完全なTeXソースで存在する。移管元の `papers/boundary/pfaffian_brill_noether_technical.tex` と**Git blob一致**を確認した。主論文A・Cから直接 `\\input` されない一方、内容上の引用・既知結果への依存は今後も監査する。
- 中心三次曲面
  \[
  F_H(U,V,W)=49U^3-(13H+14)U^2+(H+1)^2U+(11U-H-1)VW+V^3-W^3
  \]
  の滑らかさの必要十分条件が \(H(H+1)(27H+28)\neq0\) であることは `papers/central_fiber_discriminant.tex` に証明されている。追加の変数変換で \((\alpha^3+9)(28\alpha^3+243)\) が現れる。記号計算は `computations/verify_central_fiber_discriminant.py` に保持する。**中心曲面の判別式から非可換tailsの正則性・Azumaya性までは自動的に導かない。**
- Brill–Noetherの形式変形・gluing object・相対Picard・六次境界・Torelliおよび二段階解消は `papers/pfaffian_brill_noether_technical.tex` に現行の証明を置く。旧`brill_noether.pdf`は章見出しの大部分がこれに対応するため追跡解除した（PDF本文との定理ごとの同値性を監査したものではない）。
- PDF-onlyの残る独立候補：`central_pair_formal_moduli.pdf`の中心三次対の全Artin局所構造、`central_quotient_singularities.pdf`の非可換A1局所模型と特異圏、`central_cubic_technical.pdf`の点加群・正則性、`pfaffian_contact.pdf`のcontact境界、`sklyanin_mixed_quantization.pdf`の量子化。原資料の本文全体は検査できていないため、未移管の重要な証明がないとは判定しない。
- `finite_smoothness_notes.pdf`のdg perfectness反例に関する独立TeX再構成は `nc-cubic/notes/source_recovery/dg_perfectness_counterexamples.tex` に存在するが、元PDF第23節以外の内容のTeX置換は未確認。従って当面保持する。
- 先行研究の新規性・各証明の外部監査は未完了。未確認の内容を定理として拡張しない。

## 最優先の制約

主リポジトリの可換復元（特に相対残余対角のperfectness）を妨げない。必要なdg perfectness反例や中心正則性補題は `nc-cubic` 側に残し、この独立研究のために主論文A/Cを削除・書き換えない。

## 同時Poisson cubic fourfold の現行知識

専用の研究方針・正規形依存の2成分分類・未解決事項は `notes/poisson_cubic_fourfold_moduli.md` と `papers/poisson_cubic_fourfold_moduli.tex` にまとめた。証明や研究課題は専用ファイルに集約し、ここで重複しない。
