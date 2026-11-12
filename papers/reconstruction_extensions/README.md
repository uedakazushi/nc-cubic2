# 一般点復元から独立した成果の現行原稿

**2026-11-13 / v5。点スキーム・有限Jacobian復元・一次変形を独立原稿に統合。全移管は未完了。**

一般次元の主定理と必要証明は `uedakazushi/nc-cubic/papers/paper_b.tex`（B-v55）に、論文Aもnc-cubicに残す。このディレクトリは現在の研究のためのもので、旧版アーカイブではない。

## 点スキーム

入口は [mixed_cubic_point_schemes.tex](../mixed_cubic_point_schemes.tex)、再開は [専用ノート](../../notes/mixed_cubic_point_schemes.md)。一般点可換復元を仮定せず、混合中心式の証明、点加群の台・厚化、二パラメータ平坦閉包、判別式上の局所型を収録する。全文12頁の組版・表示確認と4本の有限検算の状態は `validation_mixed_cubic_point_schemes.json`。元側の17専用重複ファイルを整理済み。

## 有限Jacobian復元

入口は [cubic_jacobian_recovery.tex](../cubic_jacobian_recovery.tex)、再開は [専用ノート](../../notes/cubic_jacobian_recovery.md)。低rotation積の可積分性、有限手順、射影的一意性、Fermat例と積分不可能な完全交差を扱い、候補の抽出と圏同値の存在を区別する。全14数学的環境を保持。全文6頁の組版・表示と有理数上のrank20,24,25、核5,1,0、反例minor15872等の検算は `validation_cubic_jacobian_recovery.json`。元の専用3ファイルを整理済み。

## 一次変形とPlücker障害

入口は [cubic_first_order_deformations.tex](../cubic_first_order_deformations.tex)、再開は [専用ノート・方針](../../notes/cubic_first_order_deformations.md)。`first_order_poisson_kernel.tex` の既存結果を保持し、`dual_number_window.tex` に必要な相対比較の証明を収めた。全次数formalityや一般点復元を仮定しない。一次の曲率付き消去はN>=5、Plücker二次障害と圏論的接空間の完全列はN=5の主張である。

```sh
latexmk -g -r .latexmkrc papers/cubic_first_order_deformations.tex
python scripts/check_cubic_first_order.py --calculations
```

全文10頁、5TeX入力、28ラベル、24参照、13引用、8文献項目を検査した。全頁表示確認済み、未解決参照・引用、重複、欠落文字、overfull boxは0。元と完全一致の2本の検算を実行し、8挿入恒等式、Jacobian rank25/36、二例のJacobi係数空間とPlücker式のrank5を確認した。正確な状態は `validation_cubic_first_order.json`。これは全MF関手や全数学的証明の計算機形式検証ではない。

元の本文の全ラベルと数学的環境を保持したが、独立原稿化のため引用・説明・小補題の記載を調整したので全文バイト一致ではない。広いArtin比較全体の移管ではなく、元側の一般Artin原稿は保持する。元側の専用重複の整理状態は `validation_reconstruction_transfer.json` を参照する。

## 残件と保存方針

Artin・étale相対理論、Sklyanin/多ブロック模型、対角・bar・Moritaの別構成、混合量子化の二次jet・同変復元、独立一般化と関連資産はnc-cubicの現行支持ソースに残る。中心式や双対数比較の必要部分を抽出したことを、元の広い成果全体の移管完了とは扱わない。現在の分担はnc-cubicの `notes/paper_b_scope_and_transfer.md` と本リポジトリ `validation_reconstruction_transfer.json` に記す。

GitHub mainを正本とし、必要な数学的内容・入力・再現性を保持する。旧ZIPや旧コミットを再開の前提にせず、生成・検算・組版・数学的監査・保存を区別する。GitHub Actions・force pushは使わず、Library保存は実際のpush失敗時のみとする。
