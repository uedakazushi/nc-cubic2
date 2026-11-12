# 一般点復元から独立した成果の現行原稿

**2026-11-13 / v6。三つの独立原稿を統合。一次変形稿はTodd補正付きHKRの別証明も含む。全移管は未完了。**

一般次元の主定理と必要証明は `uedakazushi/nc-cubic/papers/paper_b.tex`（B-v55）に、論文Aもnc-cubicに保持する。このディレクトリは現行研究のためのもので、旧版アーカイブではない。

## 点スキーム

入口は [mixed_cubic_point_schemes.tex](../mixed_cubic_point_schemes.tex)、再開は [専用ノート](../../notes/mixed_cubic_point_schemes.md)。一般点復元を仮定せず、混合中心式の証明、点加群の台・厚化、二パラメータ平坦閉包、判別式上の局所型を扱う。全文12頁の組版・表示と4本の有限検算の範囲は `validation_mixed_cubic_point_schemes.json`。元側の17専用ファイルを整理済み。

## 有限Jacobian復元

入口は [cubic_jacobian_recovery.tex](../cubic_jacobian_recovery.tex)、再開は [専用ノート](../../notes/cubic_jacobian_recovery.md)。低rotation積の可積分性、有限手順、射影的一意性、Fermat例と積分不可能な完全交差を扱い、方程式候補と圏同値の存在を区別する。全14数学的環境を保持。全文6頁の組版・表示と有理数上のrank20/24/25、核5/1/0、反例minor15872等の検算は `validation_cubic_jacobian_recovery.json`。元側の専用3ファイルを整理済み。

## 一次変形、Plücker障害、Todd補正付きHKR

入口は [cubic_first_order_deformations.tex](../cubic_first_order_deformations.tex)（v2）、再開は [専用ノート](../../notes/cubic_first_order_deformations.md)。直接的な一次MF比較、五変数Plücker障害、圏論的接空間の既存主本文を保持し、必要な双対数windowを付録に置く。全次数formalityや一般点復元を入力にしない。

`poisson_first_order.tex` のTodd補正付きHKRによる幾何学的別証明も同じ原稿に統合した。二つの一次消滅は、入力・結論が異なる。直接比較は内部shift・指定周期を保つが、Todd側は基礎dg圏の一次類を扱う。後者から可換方程式の一次係数を消す系は、純Poisson KSと残余制限の両立、可換復元族の存在を仮定し、存在自体を結論しない。JacobianイデアルJ(F)と商環Jac(F)を区別し、JLLZ著者版の図式の番号をTheorem 3.10へ訂正した。

```sh
latexmk -g -r .latexmkrc papers/cubic_first_order_deformations.tex
python scripts/check_cubic_first_order.py
# 既存の有限検算を再実行するとき
python scripts/check_cubic_first_order.py --calculations
```

現行稿は13頁、6TeX入力、36ラベル、32参照、20引用、9文献。組版・全頁表示・参照を確認し、未解決・重複・文字欠落・overfullは0。Toddの9数学的環境と8ラベルを記法・引用の修正だけで保持した。既存の主本文・双対数付録・2算術コードは今回変更せず、算術コードも今回再実行していない。以前の8挿入恒等式、Jacobian rank25/36、二例のJacobiとPlücker span rank5等の実行記録とコードは保持する。全MF関手や全証明の形式検証ではない。

状態とハッシュは `validation_cubic_first_order.json`。直接比較の専用3ファイルとTodd本文1ファイルを、移管先保存後に元側から整理した。共有文献断片と一般Artin比較は未移管の支持節が使うため元側に保持する。

## 残件と保存方針

一般Artin・étale理論、Sklyanin/多ブロック模型、相対対角・bar・Moritaの別構成、混合量子化の二次jet・同変復元、その他の独立一般化と関連資産はなお移管が必要。移管先で同時に進む原稿との重複も照合する。必要部分の抽出を、元の広い成果全体の移管完了と扱わない。現在の分担はnc-cubicの `notes/paper_b_scope_and_transfer.md` と本リポジトリ `validation_reconstruction_transfer.json` に記す。

必要な数学的内容・入力・再現性を保持し、旧ZIPや旧コミットを再開の前提にしない。生成・検算・組版・数学的監査・保存を区別する。GitHub main正本、Actions・force pushなし。LibraryはGitHub保存の実失敗時のみの緊急退避とする。
