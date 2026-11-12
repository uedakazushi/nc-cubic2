# 自己同値付きdg圏のétale局所実現

**2026-11-13 / v2。** 入口は `papers/relative_cubic_realization.tex`、再開は `notes/relative_cubic_realization.md`、検証状態は `validation_relative_cubic_realization.json`。

実在するsmooth properな代数的dg族と自己同値についての障害消去によるétale局所実現を扱い、任意のn>=3の滑らかなcubicへ適用する。相対smooth proper性を仮定しており、一般点復元定理の代数的中心対の入力と混同しない。自己同値一つとintertwinerを指定し、三次周期性の選択や群作用のcoherenceは追加データとして含めない。

Hochschildのsector計算と、全Artin切断がsmoothでも完備底ではそうならない既存反例を収録する。反例の証明は `papers/artin_windows/artin_smoothness_obstruction.tex` を有限Artin稿と共用する。相対実現ディレクトリに重複コピーは作らない。

```sh
python3 scripts/check_relative_cubic_realization.py --calculations --build
```

現行6TeX入力・29ラベル・24参照・16引用・9文献で未解決・重複0。全文10頁を組版・全頁表示確認し、文字欠落・overfullも0。N=5,...,60の整数次数検算で元の証明書を再生成した。有限検算と全文組版は数学的証明の独立監査ではない。共用反例を用いる既存Artin稿全文は今回再組版していない。

移管元の別原稿からの依存が残るため、元の本文・コードは削除していない。広いArtin・étale理論の移管全体の完了とは区別する。GitHub mainが正本、Actions・force pushなし、PDF・中間物はbuild/で非追跡。
