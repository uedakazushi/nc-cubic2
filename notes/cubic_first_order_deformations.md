# 中心三次対の一次変形とPlücker障害：現行ノート

**2026-11-13 / v2。再開はルートの00_research_plan.md、本ノート、現行原稿の順。**
入口は `papers/cubic_first_order_deformations.tex`。一般次元の主定理から独立した既存の一次変形論を、直接的なMF比較、幾何学的なTodd補正付きHKRの別証明、双対数window、文献・検算とともに一論文へ統合する。新しい研究結果は追加しない。

## 目標・現在の状態・次の着手

次数別有限自由な中心三次対の双対数変形について、一次MF比較、五変数Plücker障害、可換点の圏論的接空間を扱う。一般次元の可換復元定理、非零Poisson一般点の忘却核、全高次形式モジュライはこの原稿の結論ではない。

直接比較とTodd補正による幾何側の消滅を並べ、仮定と結論の強さを区別した。後者は基礎dg圏の一次類を扱い、rotationを含む全データの自明化や可換復元の存在を示すものではない。既存の双対数window付録と一次・二次変形の主本文は変更していない。

次は付録のline Homの底変更、exact圏からdg商への比較、Ind圏における生成子持上げを独立に通読する。Todd側の適用では、具体的な量子化のKS類が通常HKRの純bivector方向であることと、残余圏への制限との両立性を検証する。有限計算・組版のPASSを圏同値の形式検証や全証明の独立監査とは呼ばない。一般Artin・étale原稿に残る成果も保持する。

## 主張と依存する結果

S=C[x_1,...,x_N]、N>=5、D=C[epsilon]/epsilon²、Fは滑らかな射影三次超曲面。剰余でSとの同定を固定した次数別有限自由unital D代数と指定中心三次元を考え、同型は剰余で恒等とする。

`fpk:thm:infinitesimal`：HKR標識で積はmu+epsilon*Theta_pi、中心元はF+epsilon*G。中心性から[pi,F]=0、勾配Koszulと次数から唯一の定数trivector Xiでpi=[Xi,F]。HKR(Xi)/tのarity3曲率付きゲージが一次の非可換積を消す。双対数では対象・射へのtwistingが有限で、逆関手、内部shift、指定三次周期を保つ。全次数formalityは使わず、Jacobi条件も一次消去には不要。標識変更は線形導分T(F)で、残る係数はJac(F)_3に値を持つ。

`fpk:prop:tangent-pair`：一次接空間はΛ³ C^N ⊕ Jac(F)_3。Jac(F)_3の次元はbinom(N+2,3)-N²、N=5で10、N=6で20。N=5の中心対の接空間は20次元。

`fpk:thm:plucker-obstruction`：N=5ではJacobiatorの係数二次式が五本のPlückerイデアルをちょうど生成する。非分解可能Xiの標準形e012+e034で条件をF_0i F_j-F_0j F_i=0へ帰着し、EulerとFの滑らかさ・既約性から矛盾を得る。Pfaffian写像alpha→alpha∧alphaの全射性でイデアルの同一性を得る。Poisson構造とGrassmannianの対応は既知（Mayanskiy、Loray–Pereira–Touzet）で、分類自体の新規性は主張しない。結合積の二次延長と、中心元も含む全高次延長は別である。

`fpk:thm:categorical-tangent`：N=5の可換点の基礎dg圏へのKSは(Xi,[G])→eta([G])。双対数windowとJLLZ Theorem 4.4(2)から0→Λ³ C⁵→T_pair^1→HH²(Ku(X))→0。rotationを忘れるのであり基礎dg圏を忘れるのではない。核10は可換点の結論で、非零Poisson一般点の核7やrotation付きstackの全接空間を同定したものではない。局所次元17と接空間20、固定Fの錐の次元7と頂点接空間10を区別する。

## Todd補正による幾何側の別証明

`papers/reconstruction_extensions/poisson_first_order.tex` はnc-cubicの同名節を証明ごと統合した。全8ラベル、補題2・命題1・系1・証明4・注意1を保持。本文は宣言した記法・引用の置換だけを行い、数学的内容を削らない。既存節ではJ(F)がJacobianイデアルを表すため、移管節で商環を表していたJ(F)をJac(F)へ統一した。共通マクロを標準TeX表記へ展開し、JLLZERを既存のJLLZへ統一した。

`pf:lem:chern`：局所体積形式mu_iに対しi_(D_i)mu_i=d(i_pi mu_i)と置く。mu_j=g_ij mu_iからD_j-D_iが±pi-sharp(d log g_ij)となり、pi-sharp c1(K)はCech境界。Jacobi条件は不要。

`pf:lem:todd`：sqrt(td)=1+c1/4+theta2+...のbivectorへの縮約を調べる。一次補正は前補題、二次はH²(O_X)=0で消え、高次は次数上縮約できない。三次三様体の純bivectorでは通常HKRと補正付きHKRが一致する。

`pf:prop:vanishing`：JLLZの作用の可換図式とgammaの単射性を使う。bivectorのH¹(Omega²)への縮約はH¹(O)=0に値を持つので、HH²(Ku(X))への制限は零。実際の残余変形に適用するには、KS類がこの制限で与えられることを別に確認する。

`pf:cor:second-order`：可換復元族とenhanced同値が既に存在し、その一次類が純Poissonであるなら、F_h=F+hG+O(h²)の[G]はJac(F)_3で零。etaの単射性、法束・Euler列からG=sum ell_i partial_i Fとなり、一次の線形座標変換で消える。可換復元の存在、G_2の値や非零性、すべての奇数次項の消滅は結論しない。半古典交換子だけからKSの純粋性を推論しない。

## 比較証明の自足性と保持する情報

既存のfirst_order_poisson_kernel.texの全22ラベル・定理3・命題1・系2・証明6・注意4は保持されている。この統合ではその本文blob `9b63fcd60612d504461eb9ee39babfcc8bf69b1d` を変更しない。全次数比較の参照を解消したKoszul原像のrank4・係数次数1の議論、HKR/twisting引用、基礎dg圏とrotationの区別を保つ。

`dual_number_window.tex`（blob `67d0728503eded03d70d25d4ccc88964ddd00343`）も変更しない。相対Koszulと正則中心商、MF余核とFrobenius exact圏のdg商、有限totalizationの曲率付き縮約、線束sectionと底変更、MF Homの有限摂動、Ind圏の生成性、windowとrotationを証明する。主本文のam:thm:comparisonはこの付録で閉じる。より一般のArtin基底の成果は元リポジトリに残し、付録の自足性と一般理論全体の移管を混同しない。

## 一次文献の参照箇所

Calaque–Rossi–Van den Bergh, Ann. of Math. 176 (2012), 865–923, doi:10.4007/annals.2012.176.2.4。刊行PDF https://annals.math.princeton.edu/wp-content/uploads/annals-v176-n2-p04-p.pdf のTheorem 1.4（p.872）を本文と画像で確認し、Todd補正付きHKRの加群構造との両立を照合した。

JLLZ著者版 https://ajacovskis.github.io/hochschild_only_2.pdf （2022年9月25日）では、作用の図式はTheorem 3.10（p.9）、その根拠はLemma 3.13（pp.10–11）。Theorem 4.4(2)（p.15）は三次三様体のeta同型とgamma単射を与える。pp.9,15を画像でも確認した。旧節の「Theorem 3.11」はこの著者版の番号と一致しないため3.10へ訂正した。Lemma 3.13の本文は確認したがp.11の追加画像取得は失敗した。

KontsevichのHKR、Căldăraru–Tuのtwisted complex、Chenの余核、Artin–Zhangのsection、Orlov/Burke–Stevensonの古典windowは既知入力。Mayanskiy arXiv:1303.5916のTheorem 1のLPTへの帰属、Section 2の係数計算とChen arXiv:2402.11613v3のTheorem 2.10、Corollary 2.11、Theorem 7.2は既存の移管で確認した箇所として保持する。この更新でそれら全箇所を再監査したわけではない。包括的新規性調査・外部査読・全証明の形式化は未実施。

## 再現と検証の境界

```sh
latexmk -g -r .latexmkrc papers/cubic_first_order_deformations.tex
python scripts/check_cubic_first_order.py
# 既存の一次・二次の有限検算を再実行する場合
python scripts/check_cubic_first_order.py --calculations
```

統合稿は6TeXファイル・36ラベル・32参照・20引用・9文献項目。移管先と同じ.latexmkrcで全文13頁を組版し、全頁を表示確認した。未解決引用・参照、重複ラベル、文字欠落、overfull boxは0。ltjsarticleの文字サイズに対するmicrotype警告は欠落文字ではない。正確なハッシュと実施状態は `validation_cubic_first_order.json`。

今回の更新では新しい計算コードは追加せず、既存の2本の算術コードは変更・再実行していない。既存の実行結果は、8個のHKR挿入恒等式、Jacobian次数3のrank25/36・商次元10/20、Fermat・混合例のJacobi二次式20本/56本とPlückerを合わせたspan rank5、非分解可能Xiの負例。これらは有限例でありMF関手の形式証明ではない。コードとチェック入口は現行treeに保持する。PDF・中間物・検算出力はbuild/に生成してGit追跡しない。

## 一般的な保存・運用原則

重要性・新規性・理解・正確性・実現可能性を総合して研究方針を改めるが、現作業の目的は既存成果の編集と移管である。証明済み、仮定付き、未完成、予想、計算的観察を区別し、誤りなら依存する本文・要約・方針も更新する。有効な証明を軽量化のために削らず、現在の方針・ノート・論文・必要コードだけから再開できる一式を保つ。過去の会話・旧ZIPに依存せず、区切りごとのmain保存を許可済みとする。GitHub Actionsとforce pushは使わない。Libraryは実際のpush失敗時だけの緊急退避で、既存項目を無断削除しない。生成・検算・組版・独立監査・保存を別々に記録する。
