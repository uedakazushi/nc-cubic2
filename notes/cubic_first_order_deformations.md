# 中心三次対の一次変形とPlücker障害：現行ノート

**2026-11-13 / v1。研究再開はルートの00_research_plan.md、本ノート、現行原稿の順に読む。**
入口は `papers/cubic_first_order_deformations.tex`。新しい研究成果を追加するのでなく、nc-cubicの一般次元主定理から独立した既存結果を、必要な比較証明・文献・検算とともに一つの原稿にする。

## 目標・現在の状態・次の着手

次数別有限自由な中心三次対の双対数変形について、一次MF比較、五変数の二次Plücker障害、可換点での圏論的接空間の関係を明確にする。一般次元の可換復元定理、非零Poisson一般点の忘却核、全高次形式モジュライはこの原稿の結論ではない。

本文に既存の定理・証明を保持し、双対数基底上のenhanced windowを付録で自立させた。全数学的証明の新しい独立監査、外部査読、包括的な新規性調査は未実施。次は付録のline Homの底変更、exact圏からdg商への比較、Ind圏における生成子持上げの三箇所を独立に通読する。有限計算のPASSをこれらの証明の形式検証と呼ばない。全移管を進める作業では、より一般のArtin・étale原稿の独立成果を失わないことを優先する。

## 入力と主張の位置付け

S=C[x_1,...,x_N]、N>=5、D=C[epsilon]/(epsilon^2)、Fは滑らかな射影三次超曲面を定める。剰余でSとの同定を固定した次数別有限自由なunital D代数と、Fへ特殊化する指定中心三次元を考える。同型は剰余で恒等。

`fpk:thm:infinitesimal`：HKR標識で積は mu+epsilon*Theta_pi、中心元はF+epsilon*G。中心性から[pi,F]=0。勾配Koszulの完全性と係数次数から唯一の定数trivector Xiがpi=[Xi,F]を満たす。HKR(Xi)/tのarity3の曲率付きゲージで一次の非可換積を消す。双対数では対象と射へのtwistingの和は有限で、逆写像と内部shift・指定三次周期性も比較できる。全次数formalityは使わない。標識の違いは線形導分T(F)で、残る係数はJac(F)_3に値を持つ。Jacobi条件は一次消去には不要。

`fpk:prop:tangent-pair`：一次接空間はHKR正規形で Λ³ C^N ⊕ Jac(F)_3 と表示する。Jac(F)_3の次元はbinom(N+2,3)-N²、N=5で10、N=6で20。N=5の中心対の一次接空間は20次元。

`fpk:thm:plucker-obstruction`：N=5ではJacobiatorの全係数二次式が五本のPlückerイデアルをちょうど生成する。非分解可能Xiの標準形e012+e034でJacobi条件がF_0i F_j-F_0j F_i=0となる。Euler恒等式とFの滑らかさ・既約性から矛盾を得る。Pfaffian写像alpha→alpha∧alphaの全射性によってスキーム論的な一致へ進む。このPoisson構造のGrassmannian記述は既知（Mayanskiy、Loray–Pereira–Touzet）であり、分類自体の新規性は主張しない。結合積の二次延長障害と、中心元も含む対の全高次延長障害は別である。

`fpk:thm:categorical-tangent`：N=5、滑らかな可換点における基礎dg圏へのKS写像は( Xi,[G] )→eta([G])。付録の双対数windowとJLLZ Theorem 4.4(2)のeta同型を用い、0→Λ³ C⁵→T_pair^1→HH²(Ku(X))→0を得る。rotationを忘れるのであって基礎dg圏を忘れるわけではない。核は可換点で10次元。非零Poisson一般点での7次元核、rotation付きstackそのものの接空間との同一視は結論しない。

## 証明を自立させた箇所

元のfirst_order_poisson_kernel.texにあった全22ラベルと数学的環境（定理3、命題1、系2、証明6、注意4）を保持した。元の定理の追加・削除はない。全次数比較への導入参照を除き、cft:lem:primitiveへの依存はrank4・係数次数1のKoszul cycleの短い議論を既存注意内に記して解消した。HKRとtwistingの一次資料引用を加え、圏論的KSの説明にあった曖昧な語句を訂正した。従って全文バイト一致ではないが、結果・証明の数学的内容を保持する編集である。

`dual_number_window.tex` は、元のartin_residual_mf_comparison.texの必要部分をD=C[epsilon]/epsilon²へ特殊化し、外部の局所模型への参照を本文の証明に置き換えたもの。相対Koszulと中心元正則性、MF余核とFrobenius exact圏のdg商、曲率付き有限totalizationの縮約、線束sectionと底変更、MF Homの有限摂動、Ind圏での生成性、windowとrotationを記載する。主本文が使うam:thm:comparisonはこの付録で証明される。一般Artin基底の全理論を移管したものではなく、元の広いArtin原稿は残す。

## 確実性・文献・重複する結果の境界

KontsevichのHKR、Căldăraru–Tuのtwisted complex、Chenの余核定理、Artin–Zhangのsection理論、Orlov/Burke–Stevensonの古典window、JLLZの接空間同型は既知入力。主張の初出は未確定。Mayanskiy arXiv:1303.5916のTheorem 1はLoray–Pereira–Touzetの結果として述べられ、Section 2に係数計算がある。一次資料本文を確認した。JLLZ著者PDF https://ajacovskis.github.io/hochschild_only_2.pdf の印刷p.15、Theorem 4.4(2)のeta同型をページ画像でも確認した。Chen arXiv:2402.11613v3 HTMLのTheorem 2.10、Corollary 2.11、Theorem 7.2の仮定・結論を確認し、三角同値だけからenhancementを宣言しない構成を付録に残した。他の引用の全箇所を今回新規に独立再監査したわけではない。

17次元モジュライの既存稿との関係では、局所次元17と可換点接空間20を区別する。固定FのPlücker錐の次元7、頂点接空間10という二次障害の説明は、全高次形式局所環の決定ではない。今後の相対KSの課題を可換点の完全列で代用しない。

## 再現手順と実施範囲

```sh
latexmk -g -r .latexmkrc papers/cubic_first_order_deformations.tex
python scripts/check_cubic_first_order.py --calculations
```

Python 3とSymPy、LuaLaTeX/LuaTeX-ja/latexmkを使用する。今回Python 3.13.5、SymPy 1.14.0。元の2本の検算コードはバイト一致で移した。一次コードは5・6変数で8個のHKR挿入恒等式とJacobian次数3のrank25・36を検算し、商次元10・20を得た。二次コードはFermat・混合三次式でJacobi係数二次式20本・56本の張る空間がいずれもrank5で、五つのPlücker式を加えてもrank5であることを確認し、非分解可能Xiの負例を検出した。有限の明示例であり、一般定理やMF関手の計算機形式証明ではない。

5TeX入力・28ラベル・24参照・13引用・8文献項目の参照検査を実施した。移管先と同一blobの.latexmkrcで全文10頁を組版し、全頁を表示確認した。未解決引用・参照、重複ラベル、文字欠落、overfull boxは0。ltjsarticleの文字サイズに対するmicrotypeの警告は残るが欠落文字ではない。正確なハッシュと検証状態はvalidation_cubic_first_order.json。PDF・中間物・計算結果はbuild/へ生成し、Git追跡しない。

## 一般的な保存・運用原則

研究価値・正確性・実現可能性を総合して方針を改めるが、今回の目的は既存原稿の編集と移管である。証明済み、追加仮定付き、未完成、予想、計算的観察を区別し、誤りなら依存する本文・要約・方針も更新する。公表価値のある証明を軽量化のために削らない。現行方針・ノート・論文・必要コードだけから再開できる一式を保ち、会話記録や旧ZIPに依存しない。区切りごとのGitHub mainへの保存を許可済みとし、Actionsとforce pushは使わない。Libraryは実際のpush失敗時のみの緊急退避で、既存Library項目を無断削除しない。生成・検算・組版・独立監査・保存は別の状態として記録する。
