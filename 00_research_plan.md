# 研究方針：独立境界・モジュライ研究

> **全研究原PDFの現行TeXへの移管とGit追跡解除が完了し、追跡PDFは0件。** 今後は論文・証明・再生成可能な計算を正本として、正確性、先行研究、新規性、公表価値を高める。削除判定と全対応は [PDF_SOURCES.md](PDF_SOURCES.md)、恒久原則は [CODEX_PDF_RECOVERY.md](CODEX_PDF_RECOVERY.md)。

## nc-cubic論文Bからの独立成果：公表用再構成（Codex最優先）

**移管そのものは完了した。** 現行の `papers/relative_reconstruction_models.tex`（244頁）と独立五稿を、数学的中心結果・論理のまとまり・公表価値に照らし、必要なら分割・統合して自足した日本語LuaLaTeX論文へ改稿する。固定の論文数や頁数に合わせず、公表価値のある定理・証明・反例を削らない。まず移管時に文脈調整されたArtin比較・smoothness反例・Hochschild障害の9環境と共有証明を、現行 `validation_reconstruction_manifest.json` と元ソースに照らして監査する。未確認の新規性を断定しない。

実行の詳細と削除ゲートは `AGENTS.md`、主張の所在と未解決条件は `notes/relative_reconstruction_models.md`。各論文の完全証明、文献一次資料の適用条件、引用/TeX入力閉包、LuaLaTeX組版・必要計算、保存を確認してから旧統合稿の真の重複を整理する。現行bundleだけで再開できる正本を維持し、旧版アーカイブを作らない。

**分業：** Chatはnc-cubic論文Aの正規形・量子化、論文Bの形式MF比較・一般点への代数的降下、およびA/Bの先行研究・新規性の独立監査を行う。CodexはA/Bと再帰入力を触らず、疑義は正確な仮定・反例候補・証明箇所を明記して伝える。

## 論文Bから独立した相対復元・明示模型

`papers/relative_reconstruction_models.tex` に残る41支持節とノート固有の証明を統合した。一般Artin・étale、楕円/多ブロック、全次数MF存在、Artin残余復元、混合jet、有限対角/bar/Morita、相対proper模型を扱う。既存五稿の証明を同じTeXから共用し、A・Bの正本と必要入力はnc-cubicに保持する。再開は `notes/relative_reconstruction_models.md`、範囲は `validation_relative_reconstruction_models.json`。新規性・全独立監査、各具体模型の未証明比較は移管作業と分けて扱う。

## nc cubic threefoldの17次元モジュライ（現行の主題）

- [現行草稿](papers/nc_cubic_threefold_moduli.tex)：41次元中心三次対、17係数横断形、分離型余次元15、忘却核7（6+1）、混合中心と相対Picard障害。
- [研究ノート](notes/nc_cubic_threefold_moduli.md)：仮定・未解決の既約成分性・再現手順。
- 再現コード：`computations/independent/verify_generic17_slice.py`、`verify_generic17_center.py`、`computations/verify_split_codimension.py`。
- 一般次元ambient復元の定理と証明は `nc-cubic/papers/paper_a.tex`、本稿には同型類判定に必要な証明も保持する。
- **ambientの周期性**：`papers/nc_cubic_threefold_moduli.tex` の `papers/sections/ambient_periodicity.tex` に、正則正規次数$d$族を持つKoszul AS正則$\mathbb Z$-代数の最小周期が$\gcd(N,d)$を割る定理と証明を収録。標準5次元・三次なら1周期的。商イデアルを保存する1周期性は未証明。既知双対性からの帰結として新規性は未確認。
- 構成した17次元族がnc cubic moduli stackの既約成分であることはまだ未証明。
- **可換点の全Artin形式局所構造をTeX化**：`papers/sections/central_pair_artin_formal_moduli.tex` に、平坦な正規三次元の自動中心性、Plücker方程式のイデアル同値、形式局所環（41次元・接空間44次元、商は17次元・接空間20次元）、Ore局所化と偏極の一意性、次数付き二次cover復元、および固定ambientの四次元fiberを証明付きで収録した。Kontsevich/Yekutieli/Lowenの形式変形比較は外部入力で、今回一次文献の独立適用監査は未完了。さらに `papers/sections/central_pair_mixed_derived_rigid.tex` に§19–21の中心二次非増大、偶数Veroneseと次数1シフトなしの構造対象付き導来復元、一般混合potentialの有限同型条件、具体的剛体ambient `B_*` の証明を移した。`B_*` の中心公式はnc-cubic論文Aの普遍公式を代入して照合済み。全係数Hesse中心元・有限証明書・37次元graph成分と一般中心・剛体例の正則開集合も現行稿へ回収し、旧V全21節を照合した。原PDFは追跡解除済み。

**2026-11-13 / v39。再開時は最初に本ファイルを読む。**

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

本リポジトリは `nc-cubic` のPoisson構造・量子化・ambient復元・可換復元という主目標から独立した、Pfaffian接触、Brill–Noether境界、中心商特異性、独立モジュライ理論を整理する。**現行のCodex最優先は相対復元統合稿の公表向け再構成と証明の保全監査**である。PDF-only資料のTeX統合と追跡解除は既に完了しており、繰り返さない。主リポジトリ `nc-cubic` の可換復元（特にSM証明）は独立の優先研究として尊重し、その証明を壊したり不用意に移転・重複収録したりしない。

本体：`papers/pfaffian_brill_noether_technical.tex` の79節を形式変形・Brill–Noether境界・低次/高次接触計算・検証範囲の5節ファイルへ、証明本文を失わずに分割した。独立した完成度・新規性はまだ外部査読していない。旧版別5節の計算履歴を現行の検証範囲・再現不能箇所の1節へ整理し、本文の主定理・証明は保持する。旧検算コードと整数入力は現行treeに欠落するため計算的証明の独立追試は未了。判別式は `papers/central_fiber_discriminant.tex` に証明と検算を収録した。

## 未解決

全原PDFの有用内容を現行論文・計算へ統合し、追跡PDFは0件となった。有限正則性ノートも `notes/ambient_finite_smoothness_and_recovery.tex` と `nc-cubic` の対応原稿へ統合済み（`PDF_SOURCES.md`）。主リポジトリの定理に引用・依存する補題は、移管元に自立した証明を保持してから移す。文献の一次資料照合も追加監査が必要。

## 一般研究原則と保存許可

数学的重要性・新規性・理解の深化・応用・正確性・実現可能性を総合して方針を更新する。証明済み、条件付き、未完成、予想、計算観察を区別し、主張の依存・証明・監査状態を明記する。一次資料を調べ、論文には完全な証明、研究ノートには有用な障害や未収録結果を残す。過去版の蓄積を避け現行資産から再開する。研究bundleは研究の区切りごとに承諾なしでLibraryに保存可能という一般許可があるが、本研究はGitHub mainを正本としpush失敗の場合だけLibraryへ緊急退避する具体運用を優先する。

## 保存原則

正本はGitHubのmain。研究ノートには現在有効な着想・反例・障害を、論文には十分な証明を保持する。証明記載、今回の照合・計算実行、未確認の新規性を区別する。日付・版番号を付けて更新し、旧ZIP・旧稿の複製・キャッシュを蓄積しない。LuaLaTeXのソースと依存物を優先し、生成PDFはGit追跡しない。明示されたGitHub push失敗時以外にLibraryへ保存しない。

## 原PDF移管の完了と現行資産

**現行状態：** Git追跡PDFは0件。証明・反例・計算入力・書誌は現行TeXと再生成器に置く。原PDFの別アーカイブは作らず、生成物は `build/` に出力して追跡しない。GitHub mainを正本とする。

### 1. 中心商特異性（旧論文VI、PDF追跡解除済み）

現行原稿：`papers/central_quotient_local_models.tex`。以下の現在有効な証明を `papers/sections/` に保持する。

- `central_quotient_center_azumaya.tex`：非斉次四中心元、中心超曲面、Rees退化・Azumaya locus。**次数6の全中心核を独立に厳密検証済み**（`computations/verify_center_degree7.py`、Q上で6中心元が独立・中心、F7=120, F6=84、mod101の交換子rank78ゆえQ上もrank78）。重み18はF18=1330を有理数上で構成し、`computations/verify_center_phi_exact.py`のFLINT厳密有理数演算で**Φ=0を実行確認した**。中心単項式rank49は既知の斉次中心定理と最高記号rank4から特性零で従う。
- `central_quotient_simple_representations.tex`：低次元単純表現の排除、二種の三次元単純表現、六次分裂元、軸上表現の一次剛性。法29非零19次小行列式は `computations/verify_central_quotient_reps.py` に保存。
- `central_quotient_categories_and_twist.tex`：Karoubi完備な特異圏の3因子分解と構造対象の標識を保たない球面ツイスト。同原稿内の有限中心・Azumaya・正則性の証明を用いる。
- `central_quotient_exact_tails.tex`：一次元表現の長さ3非被約局所環、真に悪い中心値、有限射影行列因子化と二重分岐、曲面・三様体のtails正則性の必要十分判別
  `(alpha^3+9)(28alpha^3+243)`。有限中心・PBW/CY・中心chart貼合せの証明も同原稿に収録。小計算は `computations/verify_quotient_exact_tails.py`、BGVの一次論文（JNCG 10 (2016), Theorems 6.3, 6.6, 6.7, Corollary 6.8）を確認した。

**削除ゲート達成：** 全22節を本文の証明・数式まで照合し、初期の一般正則性諸定理とCayley幾何を現行論文へ統合した。一般hの中心性・5-CY性、古典判別式、Cayley変換、定常点の長さ24も厳密検算し、LuaLaTeX組版を確認した。原PDFを追跡解除し、対応表は `PDF_SOURCES.md` に保持する。未解決の一般有効判別式・Brauer symbol・標識なし復元を解決済みとはしない。

**全混合量子化の移管も完了：** 旧II全19節と§9の57小節を照合し、形式比較・平面切断幾何・点因子の三稿と既存大部稿へ配置した。四次量子係数1/9・1/18も実際のPBW/Weyl積と170131型BCHから再生成した。

### 2. 全混合量子化の現行資産

- 中心三次対（旧V）は全21節の固有内容を現行モジュライ論文に統合してPDF追跡解除済み。
- Pfaffian接触境界は全25節を回収してPDF追跡解除済み。全次数頂点核・非線形分類・同変代数化を現行稿で証明した。
- 中心三次技術稿は全34節をモジュライ論文・中心商論文・点因子の新稿に統合してPDF追跡解除済み。
- 旧IIの全混合量子化・臨界層・点スキーム・種数5曲線は `sklyanin_mixed_formal_comparison.tex`、`marked_hesse_plane_incidence.tex`、`diagonal_cubic_point_geometry.tex` と既存大部稿へ整理し、PDF追跡解除済み。

詳細な証明と未解決箇所は各現行論文・`notes/research_notes.md`、PDF固有の対応は`PDF_SOURCES.md`に置く。**主張の証明が原稿にあること、独立に監査されたこと、有限計算が実行されたこと、組版が成功したことを区別する。**

### 非斉次中心関係の確定と次の監査

`computations/verify_center_phi_exact.py`で次数2–18の有理数商を構成し、dim F18=1330と、自由語3751項に展開したΦの剰余が厳密に零であることを確認した。python-flint 0.9.0のfmpqを任意の高速backendとし、標準Fraction版を維持する。次数8までの全基底・包含・左乗法行列は両backendで一致し、Horner評価と語ごとの評価も比較した。有限体での零から特性零へ推論していない。

次数6中心核・最高次記号rank4・三次元表現の中心指標も再実行済み。既知の斉次Sklyanin中心定理を入力として、全中心生成と唯一の関係Φを確定した。証明は `papers/sections/central_quotient_center_azumaya.tex` に集約する。表現評価による9自由係数への削減は、零条件ではなく **Q(p)=P18(p)** というアフィン条件に訂正した。具体的な評価値は軸上1/7、非軸上−1である。

Rees退化による非Azumaya locusの次元上界を一般補題にし、WWY Theorem 1.3/Lemma 5.4、Levasseur Proposition 3.2(ii)、Brown–Macleod Theorems 3.13/4.8の本文と仮定を照合した。PBWと既知Sklyanin入力からR1の大域次元3、中心の正規性、Azumaya locus同定を導く。二重étale被覆とrank6 monic式から中心降下と分岐位置を証明し、21特異点中15点の非零Hessianを厳密検算した。IW Theorem 5.1(1)の二素因子のflag分類から四点の局所模型を得る。

`papers/sections/central_quotient_chart_gluing.tex`に、CCKMの行列因子化同値、分母払い、導分の中心因子、Chen/Yekutieli–Zhangの双対性による正確な次元を収録した。指定混合族の判別式の貼合せは追加仮定から除いた。chartのIwanaga–Gorenstein性も中心正則商と忠実平坦降下から証明する。`papers/sections/central_quotient_pbw_cy.tex`にBGの三次syzygy条件、被約基底での相対PBW、自己双対な双加群解消、周囲のKoszul AS正則性を証明した。Koszul双対をQ[α]上で計算し、全pivotが非零有理定数、Frobenius対合のdetが±1であることから全αでNakayama twistが恒等と確定した（`computations/verify_central_quotient_koszul.py`）。全8三次元単純表現のExt1表は構造的に証明し、代数体上のrank19/16・内的微分rank8/9も厳密再実行した（`computations/verify_central_quotient_extensions.py`）。初期諸節とCayley幾何も全照合して現行TeXへ統合した。全原PDFは有用内容を置換して追跡解除済み。生成物は追跡しない。

## 混合研究の到達点と次の数学

形式比較稿（21頁）、平面incidence稿（16頁）、点因子稿（5頁）を組版済み。二次原始155型/473係数、四次BCH170131型と閉性・二段の原始、階数32双対の32768結合律、固定源の九次分岐式を厳密再構成した。全原PDFの削除ゲートは達成した。

今後の研究課題は、比較核の有限hでの代数化・収束、未決定の六級数の高次値、A5以上の層、大域臨界値像と導手、無標識分類と新規性の一次調査である。各証明の独立査読・一般再構成/formalityの再監査の範囲は引き続き区別する。
