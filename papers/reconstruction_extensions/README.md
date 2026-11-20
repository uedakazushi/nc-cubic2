# 論文Bから独立した成果の現行原稿

> **Point scheme 研究の正本（2026-11-13）:** [uedakazushi/nc-cubic-point](https://github.com/uedakazushi/nc-cubic-point)。専用論文、証明節、研究ノート、計算器は移管済み。以下の旧記述に本repo内のpoint-schemeファイル名が現れる場合、移管先の同名パスを参照する。相対復元などの共有証明は必要な範囲で本repoにも保持する。

2026-11-13。既存の五単位と、残る相対理論・有限模型を統合した現行稿がある。

| 入口 | 内容 |
| --- | --- |
| `papers/mixed_cubic_point_schemes.tex` | 混合中心式、点加群、平坦閉包、判別式 |
| `papers/cubic_jacobian_recovery.tex` | 有限可積分性、一意性、反例 |
| `papers/cubic_first_order_deformations.tex` | 一次MF比較、Plücker障害、Todd-HKR |
| `papers/cubic_artin_windows.tex` | 全一変数有限切断の線束残余/MF比較と反例 |
| `papers/relative_cubic_realization.tex` | 実在するsmooth proper族のétale局所実現 |
| `papers/relative_reconstruction_models.tex` | 一般Artin形式理論、楕円・多ブロック、全次数MF存在、混合jet、有限対角・bar・Morita、相対proper模型 |

共通の証明は既存のTeXを直接inputする。統合稿では `am:cor:formal-residual` とその全次数存在入力を保持し、条件付き移送だけでは代用しない。最小混合中心式とArtin PBWも点スキーム稿のソースを共用する。再開は `notes/relative_reconstruction_models.md`、再現は `python3 scripts/check_relative_reconstruction_models.py --calculations --build`。

移管対象・原稿と共有ファイルの対応は `validation_reconstruction_manifest.json`、今回の検証範囲は `validation_relative_reconstruction_models.json`。移管元の専用重複142ファイルは移管先main保存後に整理済み。一般点可換復元（旧論文B）の必要証明はnc-cubic、Poisson正規形・量子化論文Aはpoisson-cubicを正本として保持する。新規性と全証明の独立監査は別の未了課題である。
