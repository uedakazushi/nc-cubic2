# 研究ノート：境界研究の現在の知識と障害

**2026-11-12 / v10**

- 独立の大部原稿は `papers/pfaffian_brill_noether_technical.tex` にTeXソースで存在する。旧79節を一字も削らず5個の `papers/sections/` ファイルへ分割した。主論文A・Cから直接入力されない一方、内容上の引用・既知結果への依存は今後も監査する。
- 中心三次曲面
  \[
  F_H(U,V,W)=49U^3-(13H+14)U^2+(H+1)^2U+(11U-H-1)VW+V^3-W^3
  \]
  の滑らかさの必要十分条件が \(H(H+1)(27H+28)\neq0\) であることは `papers/central_fiber_discriminant.tex` に証明されている。追加の変数変換で \((\alpha^3+9)(28\alpha^3+243)\) が現れる。記号計算は `computations/verify_central_fiber_discriminant.py` に保持する。**中心曲面の判別式から非可換tailsの正則性・Azumaya性までは自動的に導かない。**
- Brill–Noetherの形式変形・gluing object・相対Picard・六次境界・Torelliおよび二段階解消は `papers/pfaffian_brill_noether_technical.tex` に現行の証明を置く。旧`brill_noether.pdf`は章見出しの大部分がこれに対応するため追跡解除した（PDF本文との定理ごとの同値性を監査したものではない）。
- PDF-onlyの残る独立候補：`central_pair_formal_moduli.pdf`の中心三次対の全Artin局所構造、`central_quotient_singularities.pdf`の非可換A1局所模型と特異圏、`central_cubic_technical.pdf`の点加群・正則性、`pfaffian_contact.pdf`のcontact境界、`sklyanin_mixed_quantization.pdf`の量子化。原資料の本文全体は検査できていないため、未移管の重要な証明がないとは判定しない。
- `finite_smoothness_notes.pdf`のdg perfectness反例に関する独立TeX再構成は `nc-cubic/notes/source_recovery/dg_perfectness_counterexamples.tex` に存在するが、元PDF第23節以外の内容のTeX置換は未確認。従って当面保持する。
- 先行研究の新規性・各証明の外部監査は未完了。未確認の内容を定理として拡張しない。

## 最優先の制約

主リポジトリの可換復元（特に相対残余対角のperfectness）を妨げない。必要なdg perfectness反例や中心正則性補題は `nc-cubic` 側に残し、この独立研究のために主論文A/Cを削除・書き換えない。

## 同時Poisson cubic fourfold の現行知識

専用の研究方針・正規形依存の2成分分類・未解決事項は `notes/poisson_cubic_fourfold_moduli.md` と `papers/poisson_cubic_fourfold_moduli.tex` にまとめた。証明や研究課題は専用ファイルに集約し、ここで重複しない。

## Pfaffian接触計算の現在有効な制約

現行の高次接触正規形と横断Hessianの数学的証明は `papers/sections/pfaffian_contact_low_order.tex`、`papers/sections/pfaffian_contact_high_order.tex` にある。形式normal消滅・頂点支持・有限決定性の主張が証明本文にあることと、その計算証明書を独立に再実行したことは別であり、再実行は未了。旧版別の計算記録は現行の `papers/sections/pfaffian_computation_audit.tex` に必要な範囲のみ統合した。

18次の94+60方向、20次の164接触方向と359 Koszul方向、22次の429方向、24次の1091方向という旧版記録の計算規模は、元の完全入力・整数証明書・driverが現行repoにないため`実行済みの再現可能な証明書`として扱わない。特に `E_vert=t^{10}`、`K_26^nor=0`、26次項の消去、無限形式変換の収束・代数化は未解決。今後の着手は現行本文の定義から整数行列と証明書を再構成して低次の非零minorから検証し、必要最小限の入力とコードのみGitHubに加える。

## PDF整理のためにTeX化した有限正則性の有効な数学

`notes/ambient_finite_smoothness_and_recovery.tex` に、全21混合方向の一様PBWの適用範囲、超越的な中心値での有限大域次元の補題、良い中心chartと滑らかな量子的境界からのtails大域次元3、具体的な `(h,α)=(1,π)` の混合例（非被約な長さ24の点加群スキーム）、偏極付き圏からの二次ambientと中心三次元の復元、対角混合族のnormalizer、Artin perfectnessから完備smoothnessへの誤った推論をまとめた。一般Poisson・PBWとdg反例の十分な証明は `nc-cubic` 論文Aと独立ノートを正本とする。原PDF研究ノートは長大な公表用論文としての価値が低いため追跡を解除した。本文の全主張を独立監査したという意味ではない。

残る5本のPDFは論文資料である。特に旧論文IIIの後半（非線形接触分類、五変数HessianモデルのMilnor/Tjurina数、Pfaffian graphの相対二次ファイブレーション）は現行大部TeXに対応節を確認できず、未移管の重要結果候補。旧論文VIには中心値零の `Mat_3(C[[a,b]]⋊{±1})` 型局所模型とBrauer指数6、特異圏 `Perf_{Z/2}(C)^⊕3` などの結果があり、これらも単なる判別式TeXで代替できない。独立検証と原文のTeX移植を先行する。

## Pfaffian旧論文IIIの現行回復の状態

旧論文III§23–24から、五変数Hessian摂動 `g_{F,c}=F+c det Hess(F)` の孤立特異点に対するMilnor数32、Tjurina数31（`c≠0`）、Milnor環の初期正則列とsocleによる証明、およびPfaffian graphを通したstrict transformと相対次元5の二次ファイブレーションを `papers/sections/pfaffian_hessian_geometry.tex` に証明付きで統合した。これは五変数モデルの数学であり、十変数境界との接触同値の証明とは別である。

同じ旧論文IIIの§21–22には普遍同変形式摂動の非線形接触分類・代数的/収束的な十次正規形の独立した証明があり、§10・§25には頂点核 `K^nor=C[H]` と `E_vert=t^10` を決定したとの原稿主張がある。従来の現行高次TeXはこれらを未解決としている。したがって旧論文IIIの仮定・局所同値関係・全次数の証明を原文で照合し、矛盾を解消するまでは成果を証明済みと扱わない。優先度は高い。

## 旧論文VI：中心商非可換A1とBrauer障害（2026-11-12）

現行の`papers/central_quotient_local_models.tex`で、中心`C=ℂ[g,U,V,W]/(Φ)`の`g=0`上の四特異点、Hessian非退化とconifold局所模型を明示した。元の代数の六次分裂元`Z`の最小多項式、中心有限性・Azumaya locus、1・2次元単純表現不存在を条件付き入力とし、`Mat_3 End_R(R⊕I)`、切断の`Mat_3(ℂ[[a,b]]⋊{±1})`、八つの三次元単純表現と一般Brauer指数6の導出を収録した。二中心chartの中心21特異点（12+6+3）の有限計算と、三つのhomological singularityも条件付きで復元。正確な中心のHessianとH=0,-1,-28/27のGröbner基底は独立に計算済み。局所分裂と大域Brauer分裂は異なる。特異圏のKaroubi完備化と球面twistは別途証明移植が必要。原PDFは保持する。

## 中心商の小次元表現：現行証明と検算

`papers/sections/central_quotient_simple_representations.tex` に旧論文VI§17–18からPauli分解による2次元単純表現不存在、q(t) の軸上二表現、ω 行列による非軸上六表現、6次分裂元の最小多項式を移植した。行列関係と `G1=0` を `computations/verify_central_quotient_reps.py` と同等のSymPy実装で標数零の正確な多項式剰余として再計算した。六次最小多項式の証明は全中心が正規で `U=Z³(g-Z³)` という既存の入力に依存する。`V,W`の中心指標とExt¹ rank19/16・内部微分rank8/9の完全証明書は未再計算、いずれも独立検証済みとは扱わない。旧論文VIの削除条件はこの残余の証明のTeX化である。

## 中心商論文VIのカテゴリー的回収と有限検算（2026-11-12）

旧§21–22の射影特異圏を中心uとt=v/uで二段局所化し、有限中心上のIwanaga–Gorenstein代数のstable Homの有限長性と完備化から三つの4変数nodeへ分解する議論を `papers/sections/central_quotient_categories_and_twist.tex` に収録。KnörrerによりKaroubi完備な特異圏は `Perf_{Z/2}(C)^⊕3`（K0=Z³）となる。旧§22の構造対象の標識を保たない3-spherical twistは、軸上の3次元単純表現の自己Ext1=0を用いて構成する。`verify_central_quotient_reps.py`に法29で19次minor=15という厳密な剛性証明書を追加し実行済み。正確なtails正則判別・Azumaya locus・有限中心の全証明は未移植であり、この部分を無条件の独立定理とは扱わない。

## 論文VIの中心全表示・Azumaya locusの依存

`papers/sections/central_quotient_center_azumaya.tex` に、`R_1`の完全中心 `Z(R_1)=C[g,U,V,W]/(Φ)` の具体的な非可換単語による `U,V,W` の表示と、Rees環・GK/Cohen–Macaulay/height-one Azumayaによる中心smooth locus同定の証明構造を復元した。旧稿では次数7以下の3280語・6015本の関係、次数6中心核の84変数rank78、次数18の50単項式rank49の有理行簡約を行っている。この再現コード・入力・証明書はまだ現行GitHubに存在しないため、有限計算を今回行ったとは報告しない。これらを再構成して中心完全表示を確立し、旧論文VIの§16の正確なtails正則性判別と結びつけることが最重要。

## 指定混合族の量子的判別式（2026-11-12）

旧論文VI§16の正確なtails判別 `(α³+9)(28α³+243)` を `papers/sections/central_quotient_exact_tails.tex` に条件付き定理として移植。悪い中心値の一次元表現環は `C[y,z]/(y²,yz,z²)`（長さ3、接空間2）で、単純表現の滑らかさに関するBGVの一次文献を使用。三foldの非正則性は、`b(s)-β0=(s³-s0³)²/(s0⁶s³)` の二重分岐と非縮約行列因子化に依存する。局所恒等式はSymPyで検証済み。これらは形式的な中心判別だけからtails判別が従うという主張ではなく、有限中心と貼合せの仮定を必要とする。旧PDF VIの行簡約証明書、Azumaya比較、中心chart十分条件の全監査は未完成。

## 非斉次中心の証明と残る関係式の同定

**検証済みの有限次数：** 定義関係の3280語・6015倍を有理数上で消去すると`dim F7=120`、`dim F6=84`。中心性と独立性を有理数上で確認した`1,g,g²,U,V,W`により交換子rankは高々78、法101でrank78だから特性零でもrank78。斉次Sklyanin中心定理と最高記号rank4により全中心生成`Z(R1)=C[g,U,V,W]`が従い、重み18以下の50単項式の特性零rankは49。

**新しい数学的簡約：** 同時符号反転は代数自己同型で、`g`は奇、`U,V,W`は偶。斉次中心の重み18の関係`P18`をこの対称性に沿って持ち上げると、その像は最高次記号が消えた後、重み17以下の偶中心となる。既知の中心Hilbert級数では次数18未満の偶中心のgraded部分は0,6,12だけなので、像は`F12`に入る。補正候補は`1,g²,U,V,W`と`g²,U,V,W`の二次単項式10個の計15個。これらは重み18未満で一次独立なので補正は一意。さらに可換化は `R1^ab=C[x,y,z]/(x²+1,y²,z²)` で `g²=-1+2yz`、`U=V=W=0`。最高次候補がU,V,Wを含む場合、補正の純粋なg部分は `c(g²+1)²` に限られる。二つの独立な条件から補正候補は13次元に減る。原稿の命題 `prop:quotient-abelianization-reduction` を参照。元の候補`Phi=P18-(14U²-2g²U-U+VW)`が正しいかは、`P18`の斉次同定と補正係数の特性零検証に依存する。命題・証明は`papers/sections/central_quotient_center_azumaya.tex`。組合せチェックは`computations/verify_center_parity_candidates.py`で実行済み（50候補、15補正、内訳1+4+10、提案Phiの偶性）。**これだけではPhi=0を証明しない。**

**計算上の障害：** `verify_center_phi_exact.py`は有理数の全filtered商を構成するが、同じ再帰アルゴリズムのローカル実行では次数13（次元560）まで確認、次数14は200秒で未終了。GitHubにあるコードそのものの全次数実行とLuaLaTeX組版は未了。今後は重み18全商の構築ではなく可換化の二条件を課した13補正係数の厳密確定を目指す。旧PDFの元有理数証明書は未発見。PDF VIは保持する。
