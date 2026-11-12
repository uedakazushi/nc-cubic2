# 研究ノート：境界研究の現在の知識と障害

**2026-11-13 / v15**

- 独立の大部原稿は `papers/pfaffian_brill_noether_technical.tex` にTeXソースで存在する。旧79節を一字も削らず5個の `papers/sections/` ファイルへ分割した。主論文A・Cから直接入力されない一方、内容上の引用・既知結果への依存は今後も監査する。
- 中心三次曲面
  \[
  F_H(U,V,W)=49U^3-(13H+14)U^2+(H+1)^2U+(11U-H-1)VW+V^3-W^3
  \]
  の滑らかさの必要十分条件が \(H(H+1)(27H+28)\neq0\) であることは `papers/central_fiber_discriminant.tex` に証明されている。追加の変数変換で \((\alpha^3+9)(28\alpha^3+243)\) が現れる。記号計算は `computations/verify_central_fiber_discriminant.py` に保持する。**中心曲面の判別式から非可換tailsの正則性・Azumaya性までは自動的に導かない。**
- Brill–Noetherの形式変形・gluing object・相対Picard・六次境界・Torelliおよび二段階解消は `papers/pfaffian_brill_noether_technical.tex` に現行の証明を置く。旧`brill_noether.pdf`は章見出しの大部分がこれに対応するため追跡解除した（PDF本文との定理ごとの同値性を監査したものではない）。
- PDF-onlyの残る独立候補：`central_pair_formal_moduli.pdf`の中心三次対の全Artin局所構造、`central_cubic_technical.pdf`の点加群・正則性、`pfaffian_contact.pdf`のcontact境界、`sklyanin_mixed_quantization.pdf`の量子化。原資料の本文全体は検査できていないため、未移管の重要な証明がないとは判定しない。
- `finite_smoothness_notes.pdf`のdg perfectness反例に関する独立TeX再構成は `nc-cubic/notes/source_recovery/dg_perfectness_counterexamples.tex` に存在するが、有用な残部も現行ノートへ統合してPDF追跡を解除した。全主張を独立監査したという意味ではない。
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

残る4本のPDFは論文資料であり、未移管の固有証明を回収するまで保持する。旧VIの非可換A1局所模型・Brauer指数6・三因子特異圏だけでなく、初期の一般正則性定理とCayley幾何も現行論文へ回収し、原PDFを追跡解除した。判定は `PDF_SOURCES.md` に集約する。

## Pfaffian旧論文IIIの現行回復の状態

旧論文III§23–24から、五変数Hessian摂動 `g_{F,c}=F+c det Hess(F)` の孤立特異点に対するMilnor数32、Tjurina数31（`c≠0`）、Milnor環の初期正則列とsocleによる証明、およびPfaffian graphを通したstrict transformと相対次元5の二次ファイブレーションを `papers/sections/pfaffian_hessian_geometry.tex` に証明付きで統合した。これは五変数モデルの数学であり、十変数境界との接触同値の証明とは別である。

同じ旧論文IIIの§21–22には普遍同変形式摂動の非線形接触分類・代数的/収束的な十次正規形の独立した証明があり、§10・§25には頂点核 `K^nor=C[H]` と `E_vert=t^10` を決定したとの原稿主張がある。従来の現行高次TeXはこれらを未解決としている。したがって旧論文IIIの仮定・局所同値関係・全次数の証明を原文で照合し、矛盾を解消するまでは成果を証明済みと扱わない。優先度は高い。

## 旧論文VI：中心商の現行到達点と残る入力

中心表示のΦ=0は次数18までの厳密有理数商で実行確認した。中心核・最高次記号・三次元表現の中心指標も現行コードで再現できる。補正候補への表現条件はQ(p)=P18(p)というアフィン条件であり、旧零条件を使わない。

現行の `papers/central_quotient_local_models.tex` に、Rees非Azumaya locusの次元上界、PBWからの大域次元3と中心正規性、一次文献の仮定を照合したAzumaya locus、中心のrank6有限平坦比較と二重étale降下、四つのconifold局所模型・零ファイバーのskew group表示・Brauer指数6を収録した。21中心特異点中15点のHessian非退化性を有理数上で検算した。残る6点のHessianはrank1であり、これらを通常二重点と呼ばない。中心の特異点21個と代数のホモロジー的特異点3個を区別する。

`papers/sections/central_quotient_chart_gluing.tex` に、行列因子化の縮約、中心chartの分母払い、導分による三切断への帰着、perfect性とSerre双対性による正確な次元を整理した。境界正則性とchartのIwanaga–Gorenstein性も証明し、特異圏の三因子分解への余分な条件を除いた。有限大域次元のaffine PI代数のsmoothnessにはRSV Lemmas 3.4–3.5の適用条件を明示した。

`papers/sections/central_quotient_pbw_cy.tex`にBGのPBW条件、被約基底上の相対PBW性、R1の自己双対な3-CY解消、指定混合族のKoszul AS正則性を証明した。Koszul双対の有限証明書は全pivotが非零有理定数で、全αへの特殊化が可能。全Frobenius対合detが±1となり、Nakayama twist恒等性を確定した。一次Ext表も局所模型のrad/rad²で説明し、独立にQQ[t]/qとQQ[ω]上でrankを再実行した。対角0・非対角2、中心切断前後で同じである。

初期§1–13の中心零化元、分離型判別式、超越的中心値、良い一般ambient、有限位数境界の正則開集合を `central_quotient_global_regularity.tex` に証明付きで統合した。Rainsの体上の中心定理を被約基底へ持ち上げる有限行列の議論と、RSVの相対smoothnessの仮定を明示する。`central_quotient_cayley_geometry.tex` には明示Cayley変換、反標準楕円境界、twisted NCCR、古典resultantと非被約定常点を収録した。

一般hの中心性と5-CY性は有理関数体上の厳密有限証明書と例外値の対称性で確認した。旧VI全22節の固有内容を現行論文で置換できたため原PDFを追跡解除した。残る研究課題は一般混合の有効判別式、Brauer類のsymbol/stack表示、標識なし復元、具体式の初出照合である。他の4PDFは削除ゲート未達。生成PDF・計算状態・ダウンロード文献は追跡しない。
