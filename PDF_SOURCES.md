# 現行PDF原資料と保持の基準（2026-11-12 / v7）

Libraryに保全されている同名・同バイトサイズのPDF原本から本文を抽出して確認した。これはGitHub上のblobそのもののバイト一致を検証したという意味ではない。原本の全定理・証明と現行TeXの完全同値性はまだ立証していない。特に旧論文III・V・VIおよび195頁のIIは、独自の結果が多数含まれる。

## 現行mainに保持する原資料（5件）

- `papers/pdf-only/ambient/central_cubic_technical.pdf`：61頁。中心三次式、点加群、有限PI中心、正則性、混合量子化等。nc-cubic論文Aや現行モジュライ原稿と重なるが、全内容の移管は未確認。
- `papers/pdf-only/ambient/central_pair_formal_moduli.pdf`：60頁。§12–13・§21にある中心三次対の全Artin形式局所構造（41次元・接空間44、商は17・20）、Ore局所化、斉次環/偏極の復元と固定周囲の四係数ファイバーを `papers/sections/central_pair_artin_formal_moduli.tex` に定理と証明構造を持たせて復元した。さらに§19–21の低次数中心、偶数Veronese、構造対象付き導来復元、全混合族の有限同型条件、明示的剛体ambientの四次元非同型族を `papers/sections/central_pair_mixed_derived_rigid.tex` に回収した。全Hesse混合係数の中心元の有限公式、量子周囲37次元成分の詳細、四次元正則開部分の非可換Bertini入力・整数証明書がまだ完全に整わないため保持する。
- `papers/pdf-only/boundary/central_quotient_singularities.pdf`：61頁。中心商の正則性・判別式、A1局所模型、Cayley cubic、非可換特異圏。現行TeX `papers/central_fiber_discriminant.tex` は判別式の一部のみで、全面代替ではない。
- `papers/pdf-only/boundary/pfaffian_contact.pdf`：89頁。旧論文III。普遍同変摂動の非線形接触分類と全次数頂点核の明示結果は未移管。Hessian五変数模型（Milnor数32、Tjurina数31）・Pfaffian graph上のstrict transformと相対二次ファイブレーションは `papers/sections/pfaffian_hessian_geometry.tex` に命題・証明を復元済み。残りの主結果を移管・監査するまで削除不可。
- `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf`：195頁、旧論文II。全21混合方向の形式可換対応、臨界層とA2/A3/A4/D4型退化、点加群・種数5曲線を含む。現行TeXにない証明が多いため、現時点で最も注意して移管すべき原資料の一つ。

## 追跡解除した資料（現行bundleには不要と判断）

- `notes/pdf-only/finite_smoothness_notes.pdf`（34頁）：研究ノートとして整理・再開上の意義はあるが独立した公表論文としての価値は低い。超越的中心値での正則性、二つの中心chart、偏極付き復元、同型判定、完備dg障害について `notes/ambient_finite_smoothness_and_recovery.tex` に有効な命題・証明要点と適用仮定を統合。一般のPBW・dg反例の完全な証明はnc-cubic側が正本。数式の独立監査は未完了。
- `notes/pdf-only/categorical_boundary_notes.pdf`（16頁）：研究の辞書・主張索引・未解決課題・共通の中心三次構造の比較を主に整理した資料。新しい独立定理の存在は目次から確認できず、現在の研究方針と各repoの現行ノートの説明に比べ追加の公表価値を見込まない。
- `papers/pdf-only/boundary/brill_noether.pdf`（58頁）：主要な章は現行 `papers/pfaffian_brill_noether_technical.tex` に節・証明付きで収録される。内容の完全同値性を保証する精査ではなく、現行TeXを正本とする厳しめの保存価値判断。

Git追跡解除後も旧Git commitにはこれらのblobが存在するが、復元を前提にしたアーカイブは本bundleに作らない。

## 次に移すべき重要な内容

(1) `central_pair_formal_moduli.pdf`の全Artin形式局所比較・忘却射の幾何を `papers/nc_cubic_threefold_moduli.tex` の既存の主張と重複照合する。(2) `central_quotient_singularities.pdf`の非可換A1特異点の局所模型と特異圏を `papers/pfaffian_brill_noether_technical.tex` と照合する。(3) 未読のPfaffian/SklyaninのPDFを全文抽出して独自の定理・証明を判定する。内容の未検証な再構成はしない。

## 現行TeXの照合先（2026-11-12）

Pfaffian・Brill--Noether大部原稿の79節を、既存内容を移動するだけで5個の主題別入力に分割した。これにより`central_pair_formal_moduli.pdf`は`papers/nc_cubic_threefold_moduli.tex`と`papers/sections/pfaffian_formal_deformations_gluing.tex`、`central_quotient_singularities.pdf`は`papers/central_fiber_discriminant.tex`と比較する対象が明確になった。PDFとの完全同一性を証明したわけではないため、残る5件の論文PDFはすべて保持する。

## 旧論文IIIから追加でTeX化した重要結果

2026-11-12：旧論文III§23–24の五変数Hessian摂動のMilnor環/Tjurina環とPfaffian graph上の解消模型・相対次元5の二次ファイブレーションを `papers/sections/pfaffian_hessian_geometry.tex` に証明を添えて復元し、親原稿の `\\input` に編入した。原稿に証明を記載したことと今回の独立再監査は区別する。旧論文III§21–22の非線形接触分類、§10の `K^nor` と `E_vert` の全次数決定は別途原文・証明照合が必要。これらは現行長大TeXの最終節で未解決と扱われていたため、旧PDFの主張を無条件に論文全体の確定定理へ昇格させない。

## 旧論文Vの全Artin形式比較を現行モジュライ論文に統合

旧論文Vの第12–13節（pp.19–30）と第21節（pp.51–58）を読んで、平坦正規三次商の中心性、相対CasimirのKoszul表示、Jacobiイデアルと五つのPlückerイデアルの一致、Kontsevich中心写像と形式局所環、Ore局所化による構造代数層、偏極の一意性、二次包絡の全Artin復元、固定ambientの射影四次元fiberを `papers/sections/central_pair_artin_formal_moduli.tex` に組み込んだ。外部formality、Ore変形比較、De Deken–Lowenの適用は独立に一次資料監査したものではない。旧§21の剛体周囲 `B_*` の有限整数証明書は現行GitHubで再現できず、実在を今回証明済みと扱っていない。PDF自体は残す。

## 旧論文Vの追加回収（第19–21節）

偶数Veroneseからの環復元、全混合族における二次中心の非増大、構造対象付き導来同値の適用範囲、potentialのblock座標変換判定、具体的剛体ambient `B_*` と相互に非同型な四係数中心商を `papers/sections/central_pair_mixed_derived_rigid.tex` に回収した。有限計算の数値証明書がGitHubにない箇所は既知の普遍中心式に帰着させた。`B_*`の中心の一次係数は普遍式への代入を独立にSymPyで確認した。ただしTHCR平行移動の位数6の一次資料監査、generic smoothnessの非可換Bertiniの適用、一般Hesse中心元の全21方向の有限式の移管は未完了。従ってこのPDFは依然として唯一の証明の所在となる可能性があり、まだ削除しない。

## 旧論文VIからの局所模型回収（2026-11-12）

`papers/central_quotient_local_models.tex`に旧論文VIの§19と§21の一部を命題と証明付きで回収：中心値零での四A1点、完備局所のconifold/非可換A1代数、skew groupの大域次元2、Brauer指数6、21個の中心特異点と条件付き三homological singularity。`computations/verify_central_quotient_local_hessian.py`に有理数Hessian・critical-fiberのGröbner基底検算を保持。従来の判別式論文は可換曲面の部分結果であり、今回の非可換局所模型と区別する。全中心の有限表示・Azumaya locusは旧論文VIの別節からの入力。小次元単純表現の不存在と六次分裂元は新たに `papers/sections/central_quotient_simple_representations.tex` に証明付きで回収し、対応する明示行列を厳密検算済み。特異圏のKaroubi完備な三分解とspherical twistの証明は `papers/sections/central_quotient_categories_and_twist.tex` に回収した。軸上三次元表現の自己Ext1消滅も `computations/verify_central_quotient_reps.py` の法29非零19次小行列式で独立確認した。ただし中心の全表示、Azumaya locus、正確なtails判別式の完全証明が残るため原PDFを保持する。局所数学の新規性は未確認。

## VIの旧§17–18をTeXに統合（2026-11-12）

軸上の `q(t)=7t^6+21t^4+14t²+1` に付随する二つの三次元単純表現、非軸上の六つの三次元単純表現、Pauli行列による二次元単純表現不存在、中心零ファイバーでの一次元表現不存在、正規中心を仮定した `Z` の次数六最小多項式を `papers/sections/central_quotient_simple_representations.tex` に回収した。`computations/verify_central_quotient_reps.py` の厳密な代数的代入で両組の行列関係・`G1=0`を検証済み。これによりconifoldへの `rank-one corner` の入力を弱められた。未回収の中核：全中心生成元 `V,W` の明示式とその中心性/尽くし、Rees degenerationからのAzumaya locus証明、一次拡大の正確な整数rank証明書、正確なtails判別式への昇格、特異圏とspherical twist。これらがTeX化されるまでPDFを削除しない。

## VIのカテゴリー論的結果の追加回収（2026-11-12）

旧論文VIの第21・22節（中心二段局所化、孤立した完備行列nodeでの特異圏分解、Knörrer周期性、3-spherical twist）を `papers/sections/central_quotient_categories_and_twist.tex` に移した。3次元単純表現の自己Ext1の消滅は `papers/sections/central_quotient_simple_representations.tex` と `computations/verify_central_quotient_reps.py` の法29の非零19次行列式（15 mod29）により証明と計算を追加した。旧PDFの独立の正則性判定（§14–16）とAzumaya locusの証明がまだ回収できていないのでGit追跡は解除しない。Karoubi完備化なしの圏同値やKuznetsov成分との同値は主張しない。
