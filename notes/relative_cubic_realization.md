# 自己同値付きdg圏のétale局所実現とArtin切断の限界

**2026-11-13 / v2。再開はルートの研究方針、本ノート、現行原稿の順。**
組版入口は `papers/relative_cubic_realization.tex`。一般次元主定理の論文Bとは入力が異なる独立原稿である。現在の編集・移管単位では新しい数学的結果を追加しない。

## 目的・到達点・次の課題

実在するsmooth properな代数的dg族について、同値双加群の障害を自己同値の不変部分で消し、特殊ファイバーの同値をétale局所的に延長する判定法を整理する。三次超曲面のHochschild sectorと、有限Artin切断から完備基底へのsmoothnessの持上げが成立しない反例を同じ原稿に置く。主étale節は元のTeXとバイト一致で、他の節も数学的主張・証明・ラベルを保持する。

次は対象moduliの局所幾何性の適用、同値双加群の障害の自然性、自己同値とintertwinerの持上げ、sectorの次数・文字の規約を独立に通読する。証明記載、今回の本文保存・参照・組版・整数検算、全証明の独立監査を区別する。包括的新規性調査、外部査読、形式検証は未実施。

## 主張と証明の所在

`papers/relative_realization/etale_realization.tex` の `er:thm:criterion` は、smoothな有限型基底H上のsmooth proper dg族Aと自己同値rに対し、特殊ファイバーのHH^{<0}=HH^1=0とT_hH→HH^2(A)^rの全射性を仮定する。同じ特殊ファイバーを持つ別の実在するsmooth proper族について、指定同値をpointed étale近傍へ延長する。proper性だけの族や未構成の抽象Hochschild変形を対象にしない。

証明は `er:lem:obstruction` のExt^2障害、自己同値による障害の不変性、幾何的KSによるsource側の補正、`er:lem:lift` のHH^1=0によるintertwinerの持上げ、perfect対象・射のmoduliとsmooth射のétale局所sectionからなる。障害の不変性を示す時点でintertwinerの持上げを仮定してはいない。自己同値一つとそのintertwinerを指定し、rho^3≃[2]という選択や群関係のcoherenceは追加データとして含めない。

`er:lem:cubic` と `er:thm:ER` は任意のn>=3のsmooth cubicへ適用する。幾何的KSの像はrotation不変部分。fourfoldのHH^2の余分な二方向は非不変。n≠4ではrotationを入力にしない存在の系 `er:cor:unpolarized` も得るが、大域的一意性を主張しない。相対smooth proper性を仮定する本稿と、次数別flatな中心三次対から出発するnc-cubic論文Bを区別する。

`hochschild_obstructions.tex` の `ho:prop:sectors` は既知BFK公式の適用。N=n+2、Jacobian環のHilbert級数は(1+t)^Nで、恒等sectorはq=2rにJ(F)_{3r}、非恒等sectorは3|Nかつq=N/3のときに二つの一次元空間を与える。後者のrotation固有値は非自明な三乗根。従ってHH^3自体が非零なのはn=7だけで、不変部分は常に零。HH^2の不変部分はJ(F)_3。fivefoldの表示次数0,...,4の次元は(1,0,35,0,7)。形式障害の消滅から相対対角のperfect性は結論しない。

## Artin稿と共用する反例

反例の本文は **`papers/artin_windows/artin_smoothness_obstruction.tex` の一ファイルだけ**に置き、有限Artin稿と本稿の双方から読む。相対実現側へ同じ証明を複製しない。外部ラベルam:lem:generatorとcg:ex:artin-singularityへの二つの文脈参照を除き、元から書かれていた直接の証明は全て保持した。全8ラベル、補題3・命題1・定理1・証明5・注意1を保持する。共有ファイルの現行blobはfe52bb222fdc9a1d2678a10b29bfa9b97ef8f228。

`as:eq:P` はR=C[[h]]上のP=[O(-1) --hs--> O]。剰余では生成子O⊕O(-1)[1]、一般点ではskyscraperとなり生成しない。各R/(h^{N+1})ではInd圏の右直交と有限h-filtrationから生成する。

`as:prop:dg-model` は次数0にe_-,e_+、次数1にs,t、d(e_-)=hs、d(e_+)=-hsを持つ階数四のstrict dg模型。一般点は次数1の外積代数K[epsilon]/epsilon^2に準同型であり、無限semifree resolutionから非smooth。各Artin切断は相対P^1のperfect圏とMorita同値でsmooth。H^0=R、H^1=Rt⊕(R/hR)sなので、cohomologyの底上flatnessを満たす反例ではない。中心三次商の特別な残余模型が非smoothだという主張でもない。

共有反例を用いるArtin稿も現行ソースで全文組版・有限dg検算を再実行した。統合稿でも同じ反例を共用し、今回の状態は専用validationに記録する。

## 一次文献と確認範囲

以下の確認は前回の原稿整備時の範囲を継承し、今回全てを再監査したとはしない。

Toën–Vaquié, Moduli of objects in dg-categories, Ann. Sci. Éc. Norm. Supér. 40 (2007),387–444。Theorem 3.6、Corollaries 3.15,3.17,3.19,3.21の本文を確認した。刊行PDFの画像取得は失敗し、視覚確認済みとはしない。https://www.math.univ-toulouse.fr/~vaquie/marque/vaquie_AnnEns40.pdf ; arXiv:math/0503269。

Lowen, Hochschild cohomology, the characteristic morphism and derived deformations, Compos. Math.144 (2008),1557–1580、arXiv:0707.2602v1 Theorem4.8と§4.4。線形圏の一次変形に関する特徴作用・対象障害の本文と画像を確認。任意小拡大のdg双加群版が同じ形で引用元に書かれているとはせず、本文のbarによる説明を別に置く。

Stacks Tags02HX,055Uの無限小smoothness判定とsmooth射のétale局所section、SashaのMathOverflow回答（2016-12-05）Is the property of being a dg generator open? の原投稿を確認した。https://mathoverflow.net/questions/256391/is-the-property-of-being-a-dg-generator-open 。strict dg表示とArtin切断との対比の初出は未確認。

Lin–Zhang, Categorical Torelli and Fourier–Mukai partners of hypersurfaces, arXiv:2611.05915v1は一次メタデータのみを確認し、PDF/HTML取得失敗のためTheorem2.2・Proposition2.4の詳細は再確認していない。関連研究として挙げ、主判定法の証明をその未確認箇所に依存させない。BFK、Huybrechts–Rennemo、JLLZ、Huybrechtsの参照箇所は元稿から保持する。書誌情報と箇所は現行references.texに収録し、外部PDFは保存しない。

## 再現と実際の検証

```sh
python3 scripts/check_relative_cubic_realization.py --calculations --build
```

Python3.10以上の標準ライブラリ、LuaLaTeX、LuaTeX-ja、latexmkを用いる。現行6TeXファイルで29ラベル・24参照・16引用・9文献を検査し未解決・重複は0。移管先と同じ.latexmkrcで10頁を組版し、最終ソースと一致する全頁を画像で確認した。overfull・文字欠落・未解決参照は0。

既存コードverify_hochschild_sectors.pyは元と同じblob9b97c8932b221258a98384115c7fcf378a3920c0。N=5,...,60の整数次数検算を再実行し、出力は元の証明書blob8e7a35337e43b45fc26b04c11414554732213ea4と完全一致した。引用するsector公式の整数計算であり、公式自体や圏論的証明の形式検証ではない。再生成可能な出力はbuild/に置く。正確なソースハッシュとビルド状態は `validation_relative_cubic_realization.json`。

## 移管の状態と一般的運用

一般Artin形式理論とétaleスタックの証明、rotation_saturation等の参照元を `papers/relative_reconstruction_models.tex` に統合済み。移管先main保存後に元の専用本文・コードを整理し、現行独立成果の移管を完了した。A・Bの26入力は保護した。

数学的重要性・新規性・理解・正確性・実現可能性を総合して方針を更新するが、現作業では推敲と移管を優先する。証明済み・仮定付き・未完成・予想・計算的観察を区別し、誤りなら依存する本文と方針も訂正する。有効な証明を軽量化の名目で削らず、旧ZIP・会話・過去コミットなしで現行一式から再開できるようにする。区切りで承諾を求めずmainへfast-forward保存する許可を保持する。Actions・force pushは禁止、Libraryは実際のpush失敗時だけの緊急退避とし、既存項目を無断削除しない。生成・検算・組版・独立監査・保存を分けて記録する。
