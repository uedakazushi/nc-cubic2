# 混合三次超曲面の点スキーム：現行ノート

**2026-11-13 / v1。再開時はリポジトリの00_research_plan.mdと、このノートを読む。**
公表用原稿は `papers/mixed_cubic_point_schemes.tex`。本文の証明は `papers/reconstruction_extensions/` 内の混合中心式および4本のpoint_scheme節にある。一般次元の可換復元定理はnc-cubic論文Bに残し、この原稿はそれを仮定しない。

## 目標・達成基準と次の作業

指定された二パラメータ混合族の点スキーム、零変形への平坦閉包、混合係数による衝突を、仮定と証明が自立した一論文にまとめる。現行結果の新たな追加より、点加群の表現関手、楕円成分の横方向の消去、Poisson零点の埋め込みスキームとしての同定を独立に監査することを優先する。本文中の証明、今回実施した有限計算、既知Sklyanin定理への依存を混同しない。全初出・新規性の確定は未了。

次の着手は `ps39:thm:global` と `psl:thm:universal-flat` の証明を、任意の可換試験環上の点列の記述と各チャートの理想の等式へ分けて検査すること。h^6=-27の退化Sklyanin成分、複数activeブロック、多中心変数および任意の非可換cubicへの一般化はこの原稿の結論ではない。lambda=0の有限部分の衝突とlambda^3=-3上の有限環の局所型は、既に本文に証明を記載しており未解決課題に戻さない。

## 現行結果と証明の所在

F_lambda=(x^3+y^3+z^3)/3+u^3+v^3+lambda*uxy。lambda^3+3 != 0で可換特殊ファイバーは滑らか。中心三次元の閉公式、自由代数内の3恒等式、Artin切断でのPBW性は `mixed_central_family.tex` の `mt:prop:center` と `mt:lem:artin-pbw` に証明を収める。元の混合族原稿の二次jet・同変復元の部分は本論文の入力ではない。

h != 0, h^6+27 != 0の点スキームは、E_h=V(u,v,x^3+y^3+z^3+h^2xyz)と有限部分Sの非交和。E_hはlambdaに依らず、その点列shiftは非自明なtranslation。中心座標が非零なら多重線形化した交換関係により点列が定数となり、可換化で表される。E_h上では隣接点の2次小行列が局所的に単元となるので中心座標の冪零的な厚化も消える（`ps39:thm:global`）。Sklyanin曲線と中心三次元の既知定理は本論文の独自成果ではない。

u=1での有限環は R[x,y,z,v]/(x^2+lambda*y,y^2+lambda*x,z^2,1+v^3+lambda*xy/3+h^2*z*(lambda^2/6-2xy/3))。x^a*y^b*z^c*v^d（a,b,c=0,1; d=0,1,2）を基底とする自由rank24。t=xy, t^2=lambda^2*t、(1+lambda*t/3)^(-1)=1-lambda*t/(3+lambda^3)からvの可逆性を得る。v'=v+h^2*z*(lambda^2/6-2xy/3)/(3v^2)が抽象スキームのh方向の自明化を与える（`psl:lem:free`）。射影空間内の接方向はh=0と異なり得る（`ps39:thm:comparison`）。

lambda != 0では12個の長さ2の点、lambda=0では3個のC[x,y,z]/(x^2,y^2,z^2)となる。後者の長さは8、極大イデアルの次数に関するHilbert関数は(1,3,3,1)。全長24を保つ（`psl:cor:collision`）。h=0への平坦閉包はPoisson零点スキームと射影的な埋め込みも含めて一致し、Hilbert多項式は3t+24（`psl:thm:universal-flat`）。ただしB_0自身のpoint schemeは可換三次超曲面全体であり、この平坦極限と異なる。

lambda^3=-3では可換超曲面が特異なのでsmooth Poisson零点の定理を適用しない。一方、有限環は分母を用いずC[lambda,h]上自由rank24に延長する（`pdb:thm:flat`）。h != 0では3個の二重点と3個のC[v]/(v^6)、h=0の後者はC[v,z]/(v^3,z^2)で、埋め込み次元はそれぞれ1と2。delta=lambda^3+3、非零x,yの枝ではh != 0の局所模型が(v^3+delta/3)^2=0となる（`pdb:thm:sixfold`、`pdb:cor:double-cubic`）。

点スキーム全体が復元可換cubicに埋め込まれるとは主張しない。本文で示す比較用三次式は制限式の照合にのみ用い、その圏同値の存在を結論しない。

## 一次資料と確認範囲

Smith–Tate, K-Theory 8 (1994), 19–63, Section 1 (pp.20–21): https://sites.math.washington.edu/~smith/Research/tate.pdf 。中心三次元による楕円曲線のtwisted homogeneous coordinate ringへの商を使用し、後半の有限位数を仮定した全中心分類は使用しない。

De Laet, Journal of Algebra 487 (2017), 244–268, DOI 10.1016/j.jalgebra.2017.05.032; arXiv:1612.06158v1, Definition 4.1, Sections 4.1–4.2, Theorem 4.4。点曲線とtranslation、中心三次元による点加群の消去に対応する本文を確認した。文献PDFのスクリーンショット取得は失敗したため文献の視覚確認済みとはしない。文献PDFはリポジトリに収録しない。

## 再現と検証の境界

リポジトリルートから次を実行する。Python 3.10以上とSymPy、LuaLaTeX/LuaTeX-ja/latexmkが必要。今回の計算はPython 3.13.5とSymPy 1.14.0で実行した。

```sh
latexmk -g -r .latexmkrc papers/mixed_cubic_point_schemes.tex
python computations/verify_mixed_test_family.py --output build/mixed_test_family_certificate.json
python computations/verify_point_scheme_thickening.py --output build/point_scheme_thickening_certificate.json
python computations/verify_lambda_point_scheme.py --output build/lambda_point_scheme_certificate.json
python computations/verify_lambda_discriminant.py --output build/lambda_discriminant_certificate.json
```

実行済み：自由代数の3恒等式、mod h^3,h^4,h^5,h^9のPBW/中心性と負例、有理数上の3+12個の長さ24のGroebner商、せん断の記号計算、標数11における判別式上の3例と長さ6の局所商。標数11の検算を標数零の一般証明の代用にしない。コードはpoint functorの表現可能性や既知Sklyanin定理を形式検証しない。容易に再生成できる出力はbuild/へ置く。

全文12頁を組版し全頁を表示確認した。参照・引用・重複ラベル・欠落文字・overfull boxは0。原稿の8TeXファイルと検算スクリプトのハッシュ、および正確な状態は `validation_mixed_cubic_point_schemes.json` に記す。全数学的証明の新しい独立監査、包括的な新規性調査、外部査読は未実施。

## 運用上の一般原則

数学的重要性・新規性・正確性・実現可能性を総合して方針を改めるが、推敲・移管中は新成果の追加を優先しない。証明済み、追加仮定付き、未完成、予想、計算的観察を区別し、誤りを見つけた場合は依存する本文・要約を更新する。研究方針・ノート・論文・必要最小限のコードから再開できる現行一式を保ち、旧版ZIP・履歴・重複証明で代用しない。GitHub mainを正本とし区切りごとに保存する。GitHub Actionsとforce pushは使わない。Library保存は実際のpush失敗時に限り、既存Library項目を無断削除しない。
