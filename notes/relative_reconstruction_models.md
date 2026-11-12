# 相対復元・有限対角・明示模型の研究方針

2026-11-13。現行稿は `papers/relative_reconstruction_models.tex`。全入力は同repo内で閉じる。

## 読み方と証明所在

1. 第I部：一般の局所Artin基底のmarked pairと、実在するsmooth proper族のétale実現を区別する。
2. 第II部：一楕円ブロックと、有限中心条件付き多ブロック。二つ以上の無限位数因子の全生成は未解決。
3. 第III部：次数別完備curved移送、全有限切断でのMF存在、相対window、全次数残余復元、混合jet。
4. 第IV部：有限対角・bar積・sector・片側Morita代数化。kernel作用の全忠実性とH^0底変更の条件を残す。
5. 第V部：一般点復元に対する別構成と飽和。nc-cubic論文Bに必要な証明は元に保持し、この部分を独立の新定理として重ねて数えない。
6. 第VI部：従来ノートだけにあった相対proper模型・PI生成子・有限bar判定・perfect性反例を証明付きで本文化した。

Artin比較、étale、Hochschild、smoothness反例、一次変形とJacobianの基礎は、既存の独立稿と同じTeXソースを入力する。最小混合族の中心式・PBWも点スキーム稿の正本を共用する。証明を短縮して置き換えない。

## 現在残る数学

`notes/relative_reconstruction/` の各主題ノートと `finite_models_and_obstacles.md` に、具体的な有限模型の条件、非可換積との未証明比較、同変高次係数、Artinから完備底への障害、有限対角証明書の課題を保持する。これらはファイル移管の残件ではない。新規性の一次資料全面調査と全証明の独立監査は未了。

`python3 scripts/check_relative_reconstruction_models.py --calculations --build` で参照閉包・組版・有限検算を再現する。生成物はbuild/に置きGit追跡しない。検算は圏論的な同値の形式検証ではない。

## 現行の公表準備単位と重点監査

`papers/proper_dg_smoothness_and_artin_limits.tex` は、反例と底変更誤差を中心に自足した6頁稿。新しい主張と完全証明は `papers/artin_windows/algebraic_smoothness_locus.tex`、基礎反例は既存TeXを共用する。検証は `validation_proper_dg_smoothness_and_artin_limits.json`。

9環境の重点照合・独立稿の位置づけ・未確認の外部入力は `notes/artin_comparison_context_audit.md`。次の数学的課題はrelative stabilizationからwindow同値へ進むdg関手の検証。統合稿を残し、全体の再構成と新規性確認を完了扱いしない。

再現：`python3 scripts/check_cubic_artin_windows.py --entry papers/proper_dg_smoothness_and_artin_limits.tex --calculations --build`。
