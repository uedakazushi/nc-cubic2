# 一般点復元から独立した成果の現行原稿

**2026-11-13 / v7。四つの独立原稿を整備。有限Artin稿の元ソース整理と全移管は未完了。**

一般次元の主定理と必要証明は `uedakazushi/nc-cubic/papers/paper_b.tex`（B-v55）に、論文Aもnc-cubicに保持する。現在有効な研究を整理し、旧版アーカイブを作らない。

## 点スキーム

入口は [mixed_cubic_point_schemes.tex](../mixed_cubic_point_schemes.tex)、再開は [専用ノート](../../notes/mixed_cubic_point_schemes.md)。一般点復元を仮定せず、混合中心式の証明、点加群の台・厚化、二パラメータ平坦閉包、判別式上の局所型を扱う。12頁の組版・表示と4本の有限検算の範囲は `validation_mixed_cubic_point_schemes.json`。元側の17専用ファイルを整理済み。

## 有限Jacobian復元

入口は [cubic_jacobian_recovery.tex](../cubic_jacobian_recovery.tex)、再開は [専用ノート](../../notes/cubic_jacobian_recovery.md)。低rotation積の可積分性、有限手順、射影的一意性、Fermat例と積分不可能な完全交差を扱い、方程式候補と圏同値の存在を区別する。全14数学的環境を保持。6頁の組版・表示と有理数上のrank20/24/25、核5/1/0、反例minor15872等の検算は `validation_cubic_jacobian_recovery.json`。元側の専用3ファイルを整理済み。

## 一次変形、Plücker障害、Todd補正付きHKR

入口は [cubic_first_order_deformations.tex](../cubic_first_order_deformations.tex)（v2）、再開は [専用ノート](../../notes/cubic_first_order_deformations.md)。一次MF比較、五変数Plücker障害、圏論的接空間の主本文と双対数window付録を保持する。Todd-HKRによる別証明も統合し、直接比較の内部shift・指定周期の保存と、幾何側の基礎dg圏の一次類の消滅を区別する。後者から可換方程式の一次係数を消す系は、純Poisson KSと残余制限の両立、可換復元族の存在を仮定する。

13頁、6TeX入力、36ラベル、32参照、20引用、9文献について組版・全頁表示・参照を確認。Toddの9数学的環境・8ラベルを保持し、Jacobianイデアルと商環を区別、JLLZ著者版の図式をTheorem 3.10に訂正した。既存2コードの8挿入恒等式、Jacobian rank25/36、JacobiとPlücker span rank5等の結果を保持するが、Todd統合時に再実行はしていない。状態は `validation_cubic_first_order.json`。元の専用3ファイルとTodd本文1ファイルを整理済み。

再現：`latexmk papers/cubic_first_order_deformations.tex`、`python scripts/check_cubic_first_order.py --calculations`。

## 有限Artin比較と完備化の障害

入口は [cubic_artin_windows.tex](../cubic_artin_windows.tex)、再開は [専用方針・ノート](../../notes/cubic_artin_windows.md)。本文は `papers/artin_windows/` に置く。一変数の全有限切断C[h]/h^(N+1)、d>=5変数について、線束生成残余圏とMFの比較、正則局所模型のArtin底変更、全Artin切断のsmoothnessが完備底で失われる反例を扱う。任意の局所Artin環や全coherent圏の定理と混同しない。

比較の中心部分の定義1・補題5・定理1・証明6と17ラベルを保持し、外部参照だった必要な局所計算を内部に記載した。smoothness反例は元のTeXと完全一致。可換MFへの同値は独立の入力とする条件付き適用を示すが、元の全次数形式復元系を削除・弱化したものではない。その系と存在定理は元側に残る。

```sh
python scripts/check_cubic_artin_windows.py --calculations --build
```

13頁、7TeX入力、31ラベル、36参照、11引用、5文献で未解決・重複・文字欠落・overfullは0。全文組版・全頁表示確認済み。QQ[h]上の4次元dg模型の64結合律、16Leibniz則、単位・d²、6個の有限切断のrank等を検算した。Morita同値・生成性・smoothnessの形式証明ではない。正確な範囲は `validation_cubic_artin_windows.json`。

**元ソースの重複除去は未完了。** 他の未移管原稿からのam:*参照と、元の形式復元系の依存を整理するまで、元のArtin比較・反例を保持する。一般Artin・étale理論全体の移管完了とは扱わない。

## 残件と保存方針

形式・étaleの存在理論、Sklyanin/多ブロック、対角・bar・Morita、混合量子化のjet・同変復元、独立一般化と関連資産はなお移管が必要。移管先で同時に進む原稿との重複も照合する。現在の分担はnc-cubicの `notes/paper_b_scope_and_transfer.md` と本リポジトリ `validation_reconstruction_transfer.json`。

有効な証明・入力・再現性を保持し、旧ZIPや旧コミットを再開の前提にしない。生成・検算・組版・数学的監査・保存を区別する。GitHub main正本、Actions・force pushなし。LibraryはGitHub保存の実失敗時だけの緊急退避とする。
