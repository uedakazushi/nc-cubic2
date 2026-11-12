# 有限Artin基底上の残余圏とMF：現行方針・ノート

**2026-11-13 / v1。再開はルートの00_research_plan.md、本ノート、現行原稿の順。**
入口は `papers/cubic_artin_windows.tex`。一般次元の主定理から独立した既存の有限Artin比較と完備化の障害を、必要証明・文献・再現手順付きの一論文へ整理する。nc-cubicの論文A・集中化した論文Bは変更しない。

## 目標と達成基準

一変数の全有限切断R_N=C[h]/(h^(N+1))上の線束生成残余圏とgraded MFの比較を、完備底や一般点での生成性・smoothnessと区別して記述する。変数数d>=5、超曲面の次元d-2>=3。任意の局所Artin環を扱う定理ではない。

現行稿に、相対余核比較、線束HomとMF Homのproper性・底変更、Ind圏での生成子持上げ、windowとrotation、正則局所模型のArtin底変更を収録した。最後に、全Artin切断でsmoothでも完備底ではsmoothでない既存反例を証明ごと保持する。新しい研究定理を追加したものではない。元の一般Artin原稿の末尾にある全次数MF存在定理を用いた可換復元は、今回の独立稿だけで証明したとしない。

## 入力と中心結果

中央R_N-代数AはA_0=R_N、各A_j有限自由、剰余はd変数多項式環。指定した中心三次元Omegaの剰余Fは滑らかな射影三次超曲面を定める。B=A/(Omega)、a=d-3、i=1-a。

`am:thm:comparison` は、線束の厚い閉包からO,...,O(a-1)を除く右直交K_B^linとMF^Z(A,Omega)のdg Morita同値を与える。関手はstab∘(Romega -)_{>=i}で、rotation=L_O∘(1)を内部shiftへ、指定中心元の周期性をrho^3≃[2]へ移す。Artin商への底変更も保つ。全coherent圏・絶対特異圏への無条件な拡張ではない。

`comparison.tex` には元の比較の17ラベル、定義1・補題5・定理1・証明6を保持する。外部の局所模型への参照だった次数別Koszul持上げと局所cohomology計算、周期変数の二重次数を本文で説明した。三角同値だけからenhancementを宣言せず、Frobenius exact圏とdg商・有限totalizationによるzigzagを使う。Homの有限摂動、compact生成と冪等完備化を区別する。

`regular_basechange.tex` は正則局所環R上の次数別有限自由な中心三次対からR_Nへの底変更を扱う。必要なnoetherian性、有限Koszul分解、Gorenstein型、線束Homと自然な導来底変更を、既存の局所模型の証明から自立させた。元の `am:prop:Gamma-basechange` の結論を保持し、変更先のArtin環の非正則性を無視しない。全Db(qgr B)の任意の底変更の定理ではない。

## 可換MFの存在とは別の適用

`ar:cor:conditional` は、同じW_hから来る可換MFとの互換な同値が別途与えられた場合に、それを線束生成残余pairとKu_perf(Y_N/R_N)の同値へ移す系である。W_hとそのMF同値の存在をこの系で証明したものではない。可換側の有限線束生成はStacks 0BQTと09M1を使う。

元の `am:cor:formal-residual` は全次数形式MF復元の定理を入力する別の結論であり、元の `artin_residual_mf_comparison.tex` の末尾に保持する。今回それを削除したり、同じラベルのまま条件付き主張へ置き換えたりしていない。より広い形式・étale理論を移管する段階で、その入力とともに統合する。

`cg:ex:artin-singularity` は、D=C[epsilon]/epsilon²、A=D[x]、W=xについて、Q²=xを微分したcontractionから有限自由MFが可縮になる一方、絶対D_sg(D)は非零である例。周囲でperfectな相対商の必要性を示す既存例として本文に明記した。

## 完備化の障害と証明の所在

`artin_smoothness_obstruction.tex` は元の全文とGit blobが一致する（00b88867ab30b64e751160bbb8207b0f405b66da）。8ラベルと、補題3・命題1・定理1・証明5・注意1を保持する。

P_h=[O(-1) --hs--> O]は特殊ファイバーで生成し、任意の有限Artin切断でも生成するが、一般点では点pのskyscraperに等しく、射影直線全体を生成しない。出発点の変形例はSashaのMathOverflow回答にある既知の例。独自の初出を主張しない。

REnd(P_h)のstrict模型はdegree0がRe_-⊕Re_+、degree1がRs⊕Rt、d(e_-)=hs、d(e_+)=-hs、d(s)=d(t)=0。全Artin切断はPerf(P¹_RN)とMorita同値なので相対smoothだが、一般点ではdegree1の外積代数E=K[epsilon]/epsilon²とquasi-isomorphic。augmentation加群Kのsemifree分解からK⊗^L_E KのH⁰が無限次元となり、Eはsmoothでない。完備底上の対角がperfectなら一般点でもperfectなので矛盾する。

この例のH¹はRt⊕(R/hR)sで、cohomology-flatではない。この反例をcohomology-flat性など未検証の強い仮定まで拡大しない。特定の非可換三次商から得た残余圏のsmoothnessを否定する例でもない。

## 移管と重複の現在の状態

この独立稿の組版・参照・有限検算は完了したが、**元ソースの重複除去は未完了**。元のArtin比較はmixed_test_family、curved_gauge_comparison、kontsevich_second_jet、formal_cubic_mf_reconstruction、three_object_window等から参照される。元の最後の形式復元系も未移管であるため、元ファイルを削除しない。一般Artin・étale理論全体の移管完了ではない。

次の具体的作業は、元のrelative_formal_models.texとrelative_etale_models.texの定理の依存を抽出し、形式的持上げ・同値スタック・smoothnessの入力を明示した現行原稿へ統合すること。併せて上記のam参照を現在の比較へ接続してから、元の比較・反例の重複を整理する。論文A・一般次元の論文Bの入力を移動しない。既存の双対数稿は独立に読める状態を保つ。

## 文献と確認範囲

Chen, Module factorizations, arXiv:2402.11613v3 (2025): Theorem 2.10、Corollary 2.11、Theorem 7.2。元の文献情報と適用の区別を保持し、graded dg版をそのままの引用定理としない。Artin–Zhang (1994)とBurke–Stevenson arXiv:1507.00830v1のsection理論・古典windowも既知入力で、全証明の新しい一次資料監査は今回実施していない。

Stacks https://stacks.math.columbia.edu/tag/0BQT と https://stacks.math.columbia.edu/tag/09M1 は、有限線束生成およびqcqsスキームのcompact=perfectという適用部分の本文を確認した。既知の生成対象の変形例の参照は https://mathoverflow.net/questions/256391/is-the-property-of-being-a-dg-generator-open 。その新たな独立文献監査・包括的新規性調査・外部査読は今回行っていない。

## 再現と実際の検証

```sh
python scripts/check_cubic_artin_windows.py --calculations --build
# または組版のみ
latexmk -g -r .latexmkrc papers/cubic_artin_windows.tex
```

Python 3.10以上、SymPy、LuaLaTeX/LuaTeX-ja、latexmkが必要。今回Python 3.13.5、SymPy 1.14.0で実行した。7TeX入力、31ラベル、36参照、11引用、5文献項目に欠落・重複なし。全文13頁を既存.latexmkrcで組版し全頁を表示確認した。未解決参照・引用、文字欠落、overfull boxは0。正確なハッシュと状態は `validation_cubic_artin_windows.json`。

`verify_artin_dg_model.py` はQQ[h]上で64個の基底三つ組の結合律、16個のLeibniz則、8単位条件とd²=0を検査する。一般点と特殊点のcohomology次元、外積代数からの写像、およびN=0,1,2,3,5,8の有限切断の微分rank N・H⁰/H¹の有理次元N+2を確認した。生成性、Morita同値、全Nの対角perfect性、無限semifree分解、MF比較の形式証明ではない。出力はbuild/で再生成し、PDFとcacheはGit追跡しない。

## 一般的な研究・保存原則

重要性・新規性・理解・応用・正確性・実現可能性を総合して方針を改める。今回の目的は既存成果の編集と移管であり、新結果の追加を優先しない。証明記載、独立監査、追加仮定、未完成、予想、有限計算を区別し、誤りなら依存する本文・要約・方針を同期して直す。有効な証明を容量削減のために省略せず、現行方針・ノート・原稿・必要コードから再開できる一式とする。旧ZIP・会話・過去コミットだけを保存場所にしない。区切りで承諾を求めずGitHub mainへ保存する許可に従い、Actionsとforce pushを使わず、同時更新を保持する。Libraryは実際のpush失敗時の緊急退避のみとし既存項目を無断削除しない。生成・検算・組版・保存を別の状態として報告する。
