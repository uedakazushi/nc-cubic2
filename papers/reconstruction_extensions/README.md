# 一般点復元から独立した成果の現行原稿

**2026-11-13 / v4。点スキーム稿と有限Jacobian復元稿を統合・組版済み。全移管は未完了。**

一般次元の主定理と必要証明は `uedakazushi/nc-cubic/papers/paper_b.tex`（B-v55）に、論文Aも引き続きnc-cubicに残す。本ディレクトリは現行研究のためのもので、過去版のアーカイブではない。

## 点スキーム

入口は [mixed_cubic_point_schemes.tex](../mixed_cubic_point_schemes.tex)、再開用の方針・ノートは [notes/mixed_cubic_point_schemes.md](../../notes/mixed_cubic_point_schemes.md)。一般点の可換復元を仮定せず、混合中心式の証明、点加群の台・厚化、二パラメータ平坦閉包、判別式上の局所型を収録する。必要本文は `mixed_central_family.tex` と4本の `point_scheme_*.tex`、設定・文献は `point_scheme_preamble.tex` と `point_scheme_references.tex`。

全文12頁の組版・表示確認と4本の有限計算の実行範囲は `validation_mixed_cubic_point_schemes.json` に記録している。この単位の元リポジトリの17専用重複ファイルは除外済み。

## 有限Jacobian復元

入口は [cubic_jacobian_recovery.tex](../cubic_jacobian_recovery.tex)、研究再開は [notes/cubic_jacobian_recovery.md](../../notes/cubic_jacobian_recovery.md)。`explicit_jacobian_recovery.tex` の全定理・証明・反例を保持し、必要な記法・文献・コードを備えた単独原稿にした。一般次元の低rotation積、有限可積分性、射影的一意性、Fermatの非一意性、積分不可能な完全交差を扱う。方程式候補の存在と圏同値の存在を区別し、低積から圏同値を結論しない。

```sh
latexmk -g -r .latexmkrc papers/cubic_jacobian_recovery.tex
python scripts/check_cubic_jacobian_recovery.py --calculations
```

全文6頁を組版・全頁表示確認。4TeX入力、17ラベル、19参照、7引用、4文献項目に未解決・重複はない。有理数上の3例の可積分性rankは20,24,25、核次元は5,1,0。反例の25×25小行列式15872と非対称入力の棄却を検算した。元の証明書は変更前コードの実行で完全再生成した。原稿・コードのハッシュと検証範囲は `validation_cubic_jacobian_recovery.json`。数学的な全証明の独立監査ではない。

## 保存済みだが統合未完の一次変形・障害

`first_order_poisson_kernel.tex` は双対数上の曲率付き一次消去、Jacobian接空間、五変数Plücker障害、categorical Kodaira--Spencer写像を含む。元の全文を保持しているが、`cft:*`、`am:*`等の依存、文献と計算資産を整理し、既存17次元モジュライ論と照合する作業が残る。移管先の原稿として閉じるまで元の本文を削除しない。

## その他の残件と保存原則

Artin・étale相対理論、Sklyanin/多ブロック模型、対角・bar・Moritaの別構成、混合量子化の二次jet・同変復元、独立一般化と関連資産はnc-cubicの現行支持ソースに残る。中心式を点スキーム稿へ抽出したことを、混合族全体の移管完了とは扱わない。現在の分担はnc-cubicの `notes/paper_b_scope_and_transfer.md` と本リポジトリ `validation_reconstruction_transfer.json` に記す。

GitHub mainを正本とし、必要な数学的内容・入力・検証可能性を保持する。旧ZIPや旧コミットを再開の前提にせず、生成・検算・組版・数学的監査・保存を区別する。GitHub Actionsとforce pushを使わず、Library保存は実際のpush失敗時のみとする。
