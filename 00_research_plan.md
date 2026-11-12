# 研究方針：独立境界・モジュライ研究

## nc cubic threefoldの17次元モジュライ（現行の主題）

- [現行草稿](papers/nc_cubic_threefold_moduli.tex)：41次元中心三次対、17係数横断形、分離型余次元15、忘却核7（6+1）、混合中心と相対Picard障害。
- [研究ノート](notes/nc_cubic_threefold_moduli.md)：仮定・未解決の既約成分性・再現手順。
- 再現コード：`computations/independent/verify_generic17_slice.py`、`verify_generic17_center.py`、`computations/verify_split_codimension.py`。
- 一般次元ambient復元の定理と証明は `nc-cubic/papers/paper_a.tex`、本稿には同型類判定に必要な証明も保持する。
- **ambientの周期性**：`papers/nc_cubic_threefold_moduli.tex` の `papers/sections/ambient_periodicity.tex` に、正則正規次数$d$族を持つKoszul AS正則$\mathbb Z$-代数の最小周期が$\gcd(N,d)$を割る定理と証明を収録。標準5次元・三次なら1周期的。商イデアルを保存する1周期性は未証明。既知双対性からの帰結として新規性は未確認。
- 構成した17次元族がnc cubic moduli stackの既約成分であることはまだ未証明。

**2026-11-12 / v9。再開時は最初に本ファイルを読む。**

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

本体：`papers/pfaffian_brill_noether_technical.tex` の79節を形式変形・Brill–Noether境界・低次/高次接触計算・検証範囲の5節ファイルへ、証明本文を失わずに分割した。独立した完成度・新規性はまだ外部査読していない。重要な結果・仮定・証明を削除せず保持する。判別式は `papers/central_fiber_discriminant.tex` に証明と検算を収録した。

## 未解決

PDF資料のうち、内容目次の比較で既存TeXへ実質的に集約済みと判定した2点の追跡を解除した。残る6点は独自の結果が存在する可能性があり、本文全体の照合まで保持する（`PDF_SOURCES.md`）。主リポジトリの定理に引用・依存する補題は、移管元に自立した証明を保持してから移す。文献の一次資料照合も追加監査が必要。

## 次の作業

1. 主題別に分割した`papers/pfaffian_brill_noether_technical.tex`をLuaLaTeXで実組版し、旧版計算記録内の参照が現行コードで再現可能かを確認する。
2. 残るPDF原資料の本文をTeXに照合し、独自の重要結果があれば証明とともに現行論文に統合する。大きなPDFのGitHub API上の本文抽出は今回未達で、名前だけで削除しない。
3. 研究の現在有効な成果を分かりやすい公表用原稿へ再編する。単なる旧原稿の蓄積にしない。

## 一般研究原則と保存許可

数学的重要性・新規性・理解の深化・応用・正確性・実現可能性を総合して方針を更新する。証明済み、条件付き、未完成、予想、計算観察を区別し、主張の依存・証明・監査状態を明記する。一次資料を調べ、論文には完全な証明、研究ノートには有用な障害や未収録結果を残す。過去版の蓄積を避け現行資産から再開する。研究bundleは研究の区切りごとに承諾なしでLibraryに保存可能という一般許可があるが、本研究はGitHub mainを正本としpush失敗の場合だけLibraryへ緊急退避する具体運用を優先する。

## 保存原則

正本はGitHubのmain。研究ノートには現在有効な着想・反例・障害を、論文には十分な証明を保持する。証明記載、今回の照合・計算実行、未確認の新規性を区別する。日付・版番号を付けて更新し、旧ZIP・旧稿の複製・キャッシュを蓄積しない。LuaLaTeXのソースと依存物を優先し、生成PDFはGit追跡しない。明示されたGitHub push失敗時以外にLibraryへ保存しない。
