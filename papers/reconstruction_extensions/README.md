# 一般点復元から独立した変形論・有限復元・point scheme

**2026-11-12 / v2。6節の本文保存済み。独立原稿への統合と全移管は未完了。**

一般次元の中心三次非可換変形の可換復元の主定理と、その必要な証明は `uedakazushi/nc-cubic/papers/paper_b.tex`（B-v55）に集約した。論文Aも引き続きnc-cubicに残し、今回変更していない。本ディレクトリは、Bの主証明に不要な有効な成果を本リポジトリの現行研究へ統合するためのもので、過去版のアーカイブではない。

## 全文の一致を確認した6節

- `first_order_poisson_kernel.tex`：双対数上の曲率付き一次消去、Jacobian接空間、五変数Plücker二次障害、可換点のcategorical Kodaira--Spencer写像。
- `explicit_jacobian_recovery.tex`：低rotation積の有限積分判定、射影的一意性、積分不可能な完全交差の反例、有限検査器。
- `point_scheme_poisson_zero.tex`：指定混合族の点加群の台とPoisson零点との比較。
- `point_scheme_thickening.tex`：孤立二重点、楕円成分、平坦閉包とPoisson零点スキームの一致。
- `point_scheme_lambda_family.tex`：混合係数も動かす有限平坦族、12個の二重点から3個の八重点への衝突。
- `point_scheme_discriminant_boundary.tex`：判別式上の有限自由性、三個の二重点と三個の六重点、衝突の局所環。

全6節は元の現行TeXと同じGit blobである。定理・証明の削除や要約による保存ではない。ただし、これは本文一致の確認であり、数学的な独立再監査をしたという意味ではない。

## 現在の未完了事項

独立LuaLaTeX原稿への組込み、全引用・参照の解決、関連する検算コードと必要証明書の移管、組版は未完了である。`cft:*` は主リポジトリの完備MF比較、`am:*` は相対Artin比較、`mt:*` は混合族の中心元構成を参照する。一般復元定理の引用と、このリポジトリ内で保持すべき独立証明を整理する。

残るArtin・étale理論、Sklyanin/多ブロック模型、相対対角・bar・Moritaの別構成、混合量子化の二次jet、関連文献・計算資産は、なおnc-cubicの現行支持ソースに残している。全移管・統合を完了したとは扱わず、移管先の完全性を確認する前に元の本文を削除しない。nc-cubicの `notes/paper_b_scope_and_transfer.md` に残件と現在の所在を記す。

一次変形・障害は既存の17次元モジュライ論との整合を確認して統合し、point schemeは混合族の中心元の証明と共に独立稿へ整理する。入力・証明・反例を現行稿に収録することで再開可能にし、旧ZIPや過去コミットの取得を前提にしない。

生成・本文保存・静的検査・組版・数学的監査を区別する。GitHub Actionsとforce pushは使用しない。
