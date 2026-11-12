# 一般点復元から独立した変形論・有限復元・point scheme

**2026-11-13 / v3。点スキーム稿は単独原稿へ統合・組版済み。その他の移管・統合は未完了。**

一般次元の主定理と必要な証明は `uedakazushi/nc-cubic/papers/paper_b.tex`（B-v55）に、論文Aも引き続きnc-cubicに残す。本ディレクトリは現在有効な独立成果のためのもので、旧版のアーカイブではない。

## 点スキーム：自立した現行原稿

組版入口は [mixed_cubic_point_schemes.tex](../mixed_cubic_point_schemes.tex)、再開用の方針・ノート・計算手順は [notes/mixed_cubic_point_schemes.md](../../notes/mixed_cubic_point_schemes.md)。一般次元の可換復元定理を仮定せず、混合量子化の中心式の証明とともに、点加群の台・非被約構造・二パラメータの平坦閉包・判別式上の局所型を扱う。

- `mixed_central_family.tex`：代数と中心三次元、自由代数の3恒等式、Artin PBWの証明。元の混合族原稿の必要部分を証明ごと抽出した。
- `point_scheme_poisson_zero.tex`、`point_scheme_thickening.tex`、`point_scheme_lambda_family.tex`、`point_scheme_discriminant_boundary.tex`：4節の定理・証明を保持。lambda節の不活性なラベル文字列だけを本文内の実参照へ直した。
- `point_scheme_preamble.tex`、`point_scheme_references.tex`：この原稿だけで組版できる設定と文献。De Laetの頁範囲を244–268へ訂正し、既知結果の適用箇所を明記した。

```sh
latexmk -g -r .latexmkrc papers/mixed_cubic_point_schemes.tex
python scripts/check_mixed_point_schemes.py --calculations
```

全文12頁、8TeXファイル、47ラベル、22参照、6引用、2文献項目。全頁を表示確認し、未解決参照・引用、重複ラベル、文字欠落、overfull boxは0。4本の計算コードを実行し、自由代数恒等式・有限jet・Groebner商長・せん断・判別式上の局所環の検算を通した。検算はpoint functorの表現可能性や既知Sklyanin定理の形式証明ではない。正確な範囲とハッシュは [validation_mixed_cubic_point_schemes.json](../../validation_mixed_cubic_point_schemes.json) を参照する。

## 全文保存済みだが統合未完の2節

`first_order_poisson_kernel.tex` は双対数上の曲率付き一次消去、Jacobian接空間、五変数Plücker障害、categorical Kodaira–Spencer写像を含む。`explicit_jacobian_recovery.tex` は低rotation積の有限積分判定、射影的一意性、積分不可能な完全交差と有限検査器を含む。両節は元の現行TeXとblob一致を確認済みだが、独立原稿としての全引用・参照・関連コード・組版の閉包はまだ確認していない。`cft:*`、`am:*`等の依存を整理する前に元の本文を削除しない。

## 残る移管

Artin・étale相対理論、Sklyanin/多ブロック模型、相対対角・bar・Moritaの別構成、混合量子化の二次jet・同変復元、独立一般化と関連計算資産はなおnc-cubicの現行支持ソースにある。混合族の中心式の部分を本稿へ取り出したことを、元の混合族の全成果の移管完了と混同しない。残件はnc-cubicの `notes/paper_b_scope_and_transfer.md` と本リポジトリの `validation_reconstruction_transfer.json` に整理する。

GitHub mainを正本とし、数学的成果・証明・必要入力を保持する。旧コミットや旧ZIPの再取得を再開の前提にしない。生成・参照検査・組版・計算・数学的監査・保存を区別する。GitHub Actionsとforce pushは使わず、Library保存は実際のpush失敗時だけとする。
