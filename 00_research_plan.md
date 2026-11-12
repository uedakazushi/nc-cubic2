# 研究方針：独立境界・モジュライ研究

## nc cubic threefoldの17次元モジュライ（現行の主題）

- [現行草稿](papers/nc_cubic_threefold_moduli.tex)：41次元中心三次対、17係数横断形、分離型余次元15、忘却核7（6+1）、混合中心と相対Picard障害。
- [研究ノート](notes/nc_cubic_threefold_moduli.md)：仮定・未解決の既約成分性・再現手順。
- 再現コード：`computations/independent/verify_generic17_slice.py`、`verify_generic17_center.py`、`computations/verify_split_codimension.py`。
- 一般次元ambient復元の定理と証明は `nc-cubic/papers/paper_a.tex`、本稿には同型類判定に必要な証明も保持する。
- **ambientの周期性**：`papers/nc_cubic_threefold_moduli.tex` の `papers/sections/ambient_periodicity.tex` に、正則正規次数$d$族を持つKoszul AS正則$\mathbb Z$-代数の最小周期が$\gcd(N,d)$を割る定理と証明を収録。標準5次元・三次なら1周期的。商イデアルを保存する1周期性は未証明。既知双対性からの帰結として新規性は未確認。
- 構成した17次元族がnc cubic moduli stackの既約成分であることはまだ未証明。
- **可換点の全Artin形式局所構造をTeX化**：`papers/sections/central_pair_artin_formal_moduli.tex` に、平坦な正規三次元の自動中心性、Plücker方程式のイデアル同値、形式局所環（41次元・接空間44次元、商は17次元・接空間20次元）、Ore局所化と偏極の一意性、次数付き二次cover復元、および固定ambientの四次元fiberを証明付きで収録した。Kontsevich/Yekutieli/Lowenの形式変形比較は外部入力で、今回一次文献の独立適用監査は未完了。さらに `papers/sections/central_pair_mixed_derived_rigid.tex` に§19–21の中心二次非増大、偶数Veroneseと次数1シフトなしの構造対象付き導来復元、一般混合potentialの有限同型条件、具体的剛体ambient `B_*` の証明を移した。`B_*` の中心公式はnc-cubic論文Aの普遍公式を代入して照合済み。ただし有限位数境界と非可換Bertiniに依存する正則な四次元開集合の存在は独立再監査前なので条件付き。原PDFの全係数Hesse中心元・有限証明書・周囲37次元成分の細部は未完全照合で保持する。

**2026-11-12 / v16。再開時は最初に本ファイルを読む。**

## ambient周期性の適用範囲と次の課題

正規族の消去による$d$周期と、Koszul双対の局所Frobenius対合による$N$周期を合成する。$N=5,d=3$では$2\cdot3-5=1$。定理は左右AS条件、有限最小線型解消と正則正規族を仮定し、中心性を不要とする。周期同型が三次商イデアルを保存すること、全nc cubicの中心三次表示、既約成分性は結論しない。研究ノートは`notes/nc_cubic_threefold_moduli.md`、次の着手は一般の$\mathbb Z$-代数への適用に必要な正則族とAS条件の検証。詳細証明は現行論文の節にあり、旧単独稿は再開の前提にしない。

## 一般Poisson cubicモジュライの正本

一般次元Poisson正規形、固定・相対Poissonスタック、既約成分数と次元公式、量子化は `uedakazushi/nc-cubic` の論文Aに既に証明を収録。ここに同じ一般分類の単独論文・ノート・専用計算を再収録しない。これらの証明の全面独立監査・新規性の確認は未完成。本リポジトリにはfourfoldの追加的scheme論、6/7次元固有の退化schemeと非可換モジュライ研究を残す。

## 別の研究対象：六・七次元Poisson cubicの退化スキーム

**対象：** 一般次元の正規形・量子化の主結果から独立した、
n=6,7の零点・退化scheme・数値幾何の詳細解析。
現行の独立LuaLaTeX草稿は
`papers/poisson_cubic_six_seven_geometry.tex`、
再開ノートは`notes/poisson_cubic_six_seven_geometry.md`。
一般退化イデアル・finite flat critical cover・零点完全交叉の
証明を`papers/sections/poisson_cubic_degeneracy_background.tex`へ、
n=6,7の階数2,4,6、7次元rank6のprimary分解と
embedded length 8,64およびreduced kernel長49の証明を
`papers/sections/poisson_cubic_six_seven_geometry.tex`へ、
Hodge/Chern/算術種数とFermat横断厚化を
`papers/sections/poisson_cubic_six_seven_numerical.tex`へ収録した。
元の論文Aから対応する6・7次元専用節と数値節を除き、
主定理のための一般次元退化イデアルと証明は論文Aに残した。

**価値の評価：** 階数表・標準完全交叉数値だけの公表価値は低い。
研究の核心候補は七次元rank6のscheme-theoretic primary分解と
embedded componentの長さの解明。
数学的新規性は未確認で、局所イデアル交叉の全独立監査は未完成。
本プロジェクトは`nc-cubic`の論文A一般次元の公表準備を妨げない
副次的研究として維持する。

**再現：**
`latexmk papers/poisson_cubic_six_seven_geometry.tex`、
`python3 computations/verify_poisson_cubic_six_seven_numerics.py`。
元のTeX本文の完全一致、ラベル参照の静的整合性をGitHub上で確認。
数値に対する同等のSymPy計算をローカルで実行してPASS。
新稿全体のLuaLaTeX組版・PDF表示検査は未実施。

## 新しい重点課題：Poisson cubic fourfold pairモジュライ（独立研究）

滑らかなcubic fourfold $X\subset\mathbb P^5$と非零正則Poisson構造$\pi$の組を同時に動かす相対Poisson schemeを、既知の集合論的分類の先のscheme構造を解析する。Poissonスカラーを保持する。

- **既知入力**：rank2/rank4の2成分と商次元30/4はnc-cubic論文Aの結果であり、ここでは再証明しない。
- **依存**：主リポジトリ `nc-cubic/papers/support/papers/sections/poisson_geometry.tex` のPoisson正規形定理（独立再監査は未実施）。そのため、公表完成定理であるとの主張はしない。数学的な帰結の証明と定理の独立監査を区別する。
- **新たに確認した点**：rank4成分のgeneric reducednessをFermat点のJacobi微分の整数36次小行列式で証明。検算コードは `verify_poisson_cubic_fourfold_tangent.py`。
- **未解決の核心**：rank2成分のgeneric reducedness、交叉のscheme構造、零Poissonの近傍、成分の境界、および新規性の一次文献照合。
- **優先手順**：六変数で正規形の独立証明→generic tangent/obstruction計算→交叉の局所環→全scheme分類→最終稿の先行研究調査。
- **再開順**：本方針→`notes/poisson_cubic_fourfold_moduli.md`→`papers/poisson_cubic_fourfold_moduli.tex`→`computations/verify_poisson_cubic_fourfold_tangent.py`。既存の独立Pfaffian研究も保持する。

## 目的と優先順位

本リポジトリは `nc-cubic` のPoisson構造・量子化・ambient復元・可換復元という主目標から独立した、Pfaffian接触、Brill–Noether境界、中心商特異性、独立モジュライ理論を整理する。研究全体の当面の最優先は**主リポジトリの可換復元**であり、この分離作業のためにそのSM証明を遅らせない。

本体：`papers/pfaffian_brill_noether_technical.tex` の79節を形式変形・Brill–Noether境界・低次/高次接触計算・検証範囲の5節ファイルへ、証明本文を失わずに分割した。独立した完成度・新規性はまだ外部査読していない。旧版別5節の計算履歴を現行の検証範囲・再現不能箇所の1節へ整理し、本文の主定理・証明は保持する。旧検算コードと整数入力は現行treeに欠落するため計算的証明の独立追試は未了。判別式は `papers/central_fiber_discriminant.tex` に証明と検算を収録した。

## 未解決

pdf-onlyの整理を最優先とし、有限正則性研究ノートの有効な数学的内容を `notes/ambient_finite_smoothness_and_recovery.tex` と `nc-cubic` の対応原稿へ統合したため、当該PDFの追跡を解除する。残るPDF原資料は5件で、各論文に未収録の重要な結果があるため本文照合・TeX化が済むまで保持する（`PDF_SOURCES.md`）。主リポジトリの定理に引用・依存する補題は、移管元に自立した証明を保持してから移す。文献の一次資料照合も追加監査が必要。

## 次の作業：PDFの追跡解除を最優先

1. 主題別に分割した`papers/pfaffian_brill_noether_technical.tex`をLuaLaTeXで実組版し、本稿をLuaLaTeXで実組版し、接触計算の必要な整数入力・証明書を現行repoから自立的に再構成する。
2. LibraryにあるPDF原本をコンテナで本文抽出できることを確認した。特に `pfaffian_contact.pdf` の旧論文III後半（Milnor/TjurinaとPfaffian graphの解消については `papers/sections/pfaffian_hessian_geometry.tex` に証明を復元済み。未移管の普遍非線形接触分類と全次数頂点核）、`central_quotient_singularities.pdf` のA1局所模型・Brauer指数・特異圏、`central_pair_formal_moduli.pdf`の§12–13・§21の回収済み部分以外の固有結果（全混合中心元の有限公式と剛体周囲の正則四係数族）を照合し、数値証明書がないものを条件付きに整理して原PDF追跡解除を判定する。
3. 研究の現在有効な成果を分かりやすい公表用原稿へ再編する。単なる旧原稿の蓄積にしない。

## 一般研究原則と保存許可

数学的重要性・新規性・理解の深化・応用・正確性・実現可能性を総合して方針を更新する。証明済み、条件付き、未完成、予想、計算観察を区別し、主張の依存・証明・監査状態を明記する。一次資料を調べ、論文には完全な証明、研究ノートには有用な障害や未収録結果を残す。過去版の蓄積を避け現行資産から再開する。研究bundleは研究の区切りごとに承諾なしでLibraryに保存可能という一般許可があるが、本研究はGitHub mainを正本としpush失敗の場合だけLibraryへ緊急退避する具体運用を優先する。

## 保存原則

正本はGitHubのmain。研究ノートには現在有効な着想・反例・障害を、論文には十分な証明を保持する。証明記載、今回の照合・計算実行、未確認の新規性を区別する。日付・版番号を付けて更新し、旧ZIP・旧稿の複製・キャッシュを蓄積しない。LuaLaTeXのソースと依存物を優先し、生成PDFはGit追跡しない。明示されたGitHub push失敗時以外にLibraryへ保存しない。

## 中心商特異性PDFのTeX回収（2026-11-12）

`papers/central_quotient_local_models.tex`に、旧論文VI§19の中心零ファイバー四つのA1点、conifold局所のrank-one corner・modifying generator、局所skew group algebra、中心値零の大域次元2と八つの三次元単純表現、Brauer指数6を、入力の仮定を明示して再構成した。旧§21の21中心特異点と3つのhomological singularityも条件付きで移した。`computations/verify_central_quotient_local_hessian.py`の厳密有理数Hessian・Gröbner検算をローカル実行してPASS。旧論文VIの全中心・Azumaya性およびtails正則性の必要十分条件の完全な独立監査は未完了。特異圏同値・球面twistの条件付き証明は `papers/sections/central_quotient_categories_and_twist.tex` に移植し、三次元表現の剛性を法29の19次非零小行列式で独立検証した。LuaLaTeX実組版は未実施。原PDFは削除しない。PDF削除が本研究の最優先である。

## 旧論文VIの有限次元表現と六次分裂元（2026-11-12）

旧論文VI§17–18の一次・二次元単純表現の不存在、軸上の多項式族の二つの三次元単純表現、非軸上の六表現、六次分裂元 `Z` の最小多項式 `T^6-gT^3+U` を `papers/sections/central_quotient_simple_representations.tex` に証明付きで収録し、`papers/central_quotient_local_models.tex` から入力した。`computations/verify_central_quotient_reps.py` の軸上 `Q[t]/(q)` と非軸上 `Q[ω]/(ω²+ω+1)` の正確な行列関係・`G1=0` 検算を独立に実行してPASS。これにより旧局所模型が仮定していた小次元単純表現排除・六次最小多項式を、中心正規性と中心恒等式 `U=Z³(g-Z³)`の入力の下で内部証明へ変更した。中心の生成元 `V,W` と全Azumaya locusの証明、Ext¹の27変数rank証明書はなお未回収。従ってPDF VIは保持し、これらのTeX化を優先する。

### PDF VIの追加回収：特異圏・球面ツイスト

中心二段局所化とIwanaga--Gorenstein完備化によるKaroubi特異圏の三分解、Knörrer周期性を通じた `Perf_{Z/2}(C)^⊕3`、剛体三次元表現のcoherent化と3-spherical twistを `papers/sections/central_quotient_categories_and_twist.tex` に再構成した。`computations/verify_central_quotient_reps.py` に軸上表現のJacobi行列の法29非零19次小行列式（値15）を追加しローカル実行PASS。`q(t)`の法3既約性も検算。これにより旧§17の自己Ext1消滅は独立の計算証明を持つ。残る障害は `R_1` とtailsの正則性判定、中心の有限生成・Azumaya同定、全非可換中心値での大域次元の証明。これらの未移管部分があるのでPDF VIはまだ追跡する。
