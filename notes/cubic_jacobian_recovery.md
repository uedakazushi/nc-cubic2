# 低次数積からの三次方程式の有限復元

**2026-11-13 / v1。最初に研究方針を読み、このノートから再開する。**
現行論文は `papers/cubic_jacobian_recovery.tex`、証明全文は `papers/reconstruction_extensions/explicit_jacobian_recovery.tex`。一般次元の存在定理を扱うnc-cubic論文Bとは独立に、有限次元の積から方程式候補を抽出する条件と反例を扱う。

## 現在の目標と達成基準

既存の有限復元原理を、必要な既知結果・完全な証明・例と反例・再現コードを備えた短い独立稿にする。新しい定理の追加を優先しない。勾配空間の復元・積分解の非一意性の一般原理は既知であり、本稿の具体的検査器と循環完全交差反例の初出は未確認である。投稿可能性は独立監査と文献調査を経て判断する。

次の着手は、低次数の導来自然変換と合成を計算する実際の非可換入力を一例選ぶこと。ただし今回の作業は移管と推敲であり、この計算は実行していない。対象族の第一候補は混合族 F_lambda=(x^3+y^3+z^3)/3+u^3+v^3+lambda*uxy（点スキーム稿 `papers/mixed_cubic_point_schemes.tex` に中心元の定義と証明あり）、次に非楕円二成分である。

## 現在有効な結果・仮定・依存

V=H^0 RHom(C^e)(Delta,P)、W=H^0 RHom(C^e)(Delta,P tensor_C P)と積muを、dg双加群の導来自然変換として扱う。三角圏の通常の自然変換で代用しない。任意のn>=3の可換三次超曲面では、既知のsector計算によってV=Jac(F)_1、W=Jac(F)_2。非恒等sectorはN=n+2が偶数のとき内部次数N/2にのみ現れ、1,2には寄与しない。積の対称性と全射性からK=ker(Sym^2 V -> W)が勾配空間になる（`prop:ej-geometric-low-degree`）。

任意のN次元二次式空間K=<q_a>に対し、L_Kは partial_j(sum_a A_ia q_a)=partial_i(sum_a A_ja q_a) を満たすN×N行列の線形空間。Kが共通射影零点を持たず、L_Kに可逆行列が存在することが、滑らかな三次式の勾配空間であるための必要十分条件である。F_A=sum x_i A_ia q_a/3 が積分を与える（`thm:ej-effective-recovery`）。線形核、determinantの多項式恒等判定、有限格子、Groebner基底による有限手順は `cor:ej-finite-algorithm`。この有限性は最適計算量を意味しない。

同じ勾配空間を持つ滑らかな三次式は複素数体上で射影同型（`prop:ej-projective-uniqueness`）。対称三重線形形式のsymmetrizer代数の可換性、nilpotentの排除、固有空間分解と各成分の三乗根による座標変換を本文で証明する。基礎体上の同型は結論していない。Fermatの場合、L_KはN次元の対角行列全体であり、固定座標でscalar倍だけの一意性はない。

5変数のq_i=x_i^2+x_(i+1)x_(i+2)（添字mod5）は原点以外に共通零点を持たず、Hilbert級数(1+t)^5の完全交差だがL_K=0（`prop:ej-nonintegrable-ci`）。Hilbert関数・完全交差性・低次数の次元だけでは積分可能性を保証しない。実際の非可換残余圏がこの反例を生むと主張しない。

全条件を満たしても、得るのは圏論的模型が存在するときの唯一の方程式候補であり、同値双加群と逆は構成していない（`cor:ej-candidate`）。残余dg代数Gammaとrotation双加群Pから RHom_(Gamma^e)(Gamma,P) と RHom_(Gamma^e)(Gamma,P tensor_Gamma P) のH^0・合成を計算する必要がある。線束Homの階数、Poisson一次項、ambient関係式を直接代入してはならない。候補抽出後の同値核の構成、smoothnessの確認を伴うetale実現との比較、相対対角のperfect性は別問題である。

## 文献の確認範囲と新規性

Lin–Zhang, arXiv:2310.09927v2 (2024), https://arxiv.org/html/2310.09927v2 : Theorem 2.2（dg Orlovとshift）、Theorem 3.5・Remark 3.6（sectorと積）、Proposition 3.7・Section 5をHTMLで確認した。gcd(N,3)=1はSerre代数表示に関する条件と区別する。

Hwang, *Symmetrizer group of a projective hypersurface*, JMSJ 78 (2026), 55–62, doi:10.2969/jmsj/93469346, https://arxiv.org/html/2501.08633v1 : Theorems 1.5–1.6、Proposition 2.2をHTMLで確認。巻・頁は数学会の当該巻目次で確認した。

Ueda–Yoshinaga, Hokkaido Math. J. 38 (2009), 409–415, doi:10.14492/hokmj/1258553970, https://arxiv.org/abs/0802.2133 : Lemma 3をPDF抽出本文で確認。Huybrechts–Rennemo, Algebraic Geometry 6 (2019), 76–99, doi:10.14231/AG-2019-005, https://content.algebraicgeometry.nl/2019-1/2019-1-005.pdf : abstractとTheorem 1.1の仮定を確認し、本稿の全次元の低次数同定を直接その定理に帰さない。両PDFのweb画像取得は失敗したため、文献PDFを画像確認済みとは記載しない。外部文献PDFはリポジトリに収録しない。

## 再現・実施状態

```sh
latexmk -g -r .latexmkrc papers/cubic_jacobian_recovery.tex
python scripts/check_cubic_jacobian_recovery.py --calculations
python computations/verify_explicit_jacobian_recovery.py --output build/explicit_jacobian_certificate.json
```

Python 3.10以上、SymPy、LuaLaTeX/LuaTeX-ja/latexmkを用いる。今回Python 3.13.5、SymPy 1.14.0で実行した。3例の50×25可積分性行列のrankは20,24,25、核次元は5,1,0。Hilbert関数はすべて(1,5,10,10,5,1,0)。反例の指定25×25小行列式は15872。非対称の積をSym^2へ降ろす前に棄却する負例もPASS。既存コードを変更前に実行した出力は元の証明書blob 84f51d6c288c7c2c202e01173ee7c4363a8e3c41 と一致した。移管後はソースパス、build出力先、日付・版だけを改め、全数値部分の一致を再検査した。

これらは可換多項式の商と線形代数の検算であり、非可換dg Homや圏同値の計算ではない。コードは明示3例の検証用で、任意入力に対する最適な一般復元実装ではない。容易に再生成できる証明書はbuild/に生成しGit追跡しない。

全文6頁を組版し、全頁を画像で確認した。4TeXファイル・17ラベル・19参照・7引用・4文献項目に未解決・重複なし。ログの文字欠落・overfull boxも0。元の節の全14個の定理・証明・例・注意の環境ブロックはバイト一致し、本文で変更したのは最後の研究予定を本文に依存しない射程の記述へ置き換えた箇所だけである。具体的な着手方法は上に保持した。実施範囲とハッシュは `validation_cubic_jacobian_recovery.json`。

## 常設原則・保存許可

数学的重要性・新規性・正確性・実現可能性を総合して目標を調整する。証明記載、独立監査、追加仮定、未完成、予想、計算的観察を区別し、誤りがあれば依存する本文と要約も修正する。公表価値のある結果と証明を軽量化のために削らず、研究方針・ノート・現行論文・最小限のコードと入力から再開できる状態を保つ。旧版ZIP・会話履歴・重複証明を再開の前提にしない。GitHub mainを正本とし、ユーザーの保存許可に基づき区切りで承諾を求めず保存する。Actions・force pushを使わず、Libraryは実際のpush失敗時のみ緊急退避とする。生成・検算・組版・保存は別々の状態として報告する。
