# 研究ノート：境界研究の現在の知識と障害

**2026-11-10 / v1**

- 独立の大部原稿は `papers/pfaffian_brill_noether_technical.tex` に完全なTeXソースで存在する。移管元の `papers/boundary/pfaffian_brill_noether_technical.tex` と**Git blob一致**を確認した。主論文A・Cから直接 `\\input` されない一方、内容上の引用・既知結果への依存は今後も監査する。
- 中心三次曲面
  \[
  F_H(U,V,W)=49U^3-(13H+14)U^2+(H+1)^2U+(11U-H-1)VW+V^3-W^3
  \]
  の滑らかさの必要十分条件が \(H(H+1)(27H+28)\neq0\) であることは `papers/central_fiber_discriminant.tex` に証明されている。追加の変数変換で \((\alpha^3+9)(28\alpha^3+243)\) が現れる。記号計算は `computations/verify_central_fiber_discriminant.py` に保持する。**中心曲面の判別式から非可換tailsの正則性・Azumaya性までは自動的に導かない。**
- Brill–Noether、Pfaffian接触、Azumaya/Brauer、noncommutative tailsの独立結果は、移管元のPDF原本にしかない部分がある。完全なTeXで置き換わったとは判断しない。
- 先行研究の新規性・各証明の外部監査は未完了。未確認の内容を定理として拡張しない。

## 最優先の制約

主リポジトリの可換復元（特に相対残余対角のperfectness）を妨げない。必要なdg perfectness反例や中心正則性補題は `nc-cubic` 側に残し、この独立研究のために主論文A/Cを削除・書き換えない。
