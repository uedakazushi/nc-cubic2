# 非可換三次三様体の17次元モジュライ族

**2026年11月12日 / v2。再開時はまず ../00_research_plan.md を読む。GitHub mainが正本。**

## 現在の目標と到達点
中心三次対の41次元incidence族から17次元の真の非可換同型類を構成し、適切なモジュライスタックでその閉包が既約成分となるか決定する。現行原稿 `papers/nc_cubic_threefold_moduli.tex` に相対Jacobian型の構成、17係数正規形、31次行列式、分離型余次元15、忘却核7=6+1、相対Picard障害と同型類復元の帰結を証明付きで収録した。

## 仮定・主張の確実性
- 17係数の真の同型類次元：原稿に証明あり。一般有限な有理商と二次包絡による同型類判定に依存。独立再監査・新規性の網羅的調査は未完了。
- 量子中心の存在と正則性：相対PBWと中心の定数rankの議論、Mori--Smith等の既存結果を入力とする。論文Aの普遍公式・計算結果との仮定の突き合わせを継続。
- 三次商からambientの復元：一般次元の定理と圏論的証明はnc-cubicの論文Aへ統合。本稿は17次元性に必要な短い証明を自立的に収録。
- **正則正規超曲面と周期性**：`papers/sections/ambient_periodicity.tex` に$\mathbb Z$-代数の一般定理（最小周期$p\mid\gcd(N,d)$）と証明を収録。正規族による$d$周期、AS/Koszul双対の局所Frobenius対合による$N$周期を使う。5次元・三次では$\theta=\rho^{-1}\sigma^2$による1周期同型を構成する。ただし1周期同型の商イデアル不変性は未証明で、相対moduliの結論に直結しない。低次数核の判定には$\dim I_{i,i+3}=1,\dim I_{i,i+4}=5$と各三次生成元の左右正則性が必要。既知入力はBondal--Polishchuk (1994, Proposition 4.1, §5, DOI 10.1070/IM1994v042n02ABEH001536)とChan--Nyman (arXiv:2211.12465, Definition 8.6)。包括的新規性調査と全証明の独立監査は未完了。
- 未証明：17次元族がnc cubic moduli stackの既約成分をなすこと、全nc cubicの分類、全係数に一様な可換復元、無標識導来圏からの復元。

## 優先研究
Poisson cubic pairの17次元成分との局所比較を行い、まず中心三次対と次数付き商代数の変形複体を明示する。一般点の接空間と障害を計算し、既約成分性とgeneric reducednessを検証する。Poisson pairからnc cubic moduliへの大域的量子化射は存在が未証明なので、有限チャートの対応と降下条件を分けて扱う。

## 必要な再現資産
- `papers/nc_cubic_threefold_moduli.tex`、`papers/sections/mixed_center_picard.tex`、`papers/sections/ambient_periodicity.tex`（数式と証明・文献）
- `computations/independent/verify_generic17_slice.py`（31次整数行列式）
- `computations/independent/verify_generic17_center.py`（三変数中心の次数別計算）
- `computations/verify_split_codimension.py`（分離型と忘却核の接空間計算）

組版はrootから `latexmk papers/nc_cubic_threefold_moduli.tex`。検算はPython 3 + SymPyで各スクリプトを直接実行。今回GitHubのソース転送と参照検査を行ったが、新原稿のLuaLaTeX全組版と移管後コードの実行は未確認。

## 可換点における全Artin局所構造と未解決の大域化（2026-11-12）

旧中心三次対PDFの主要な§12–13・§21を `papers/sections/central_pair_artin_formal_moduli.tex` として現行モジュライ原稿に統合。滑らかな三次Fの標識付き対では、中心三次直線とArtin形式量子化の比較から形式局所環 `k[[s_1..s_34,a_{01}..a_{34}]]/(five Plücker quadrics)`、局所次元41/接空間44を得る。PGL5の24方向を除いたsliceでは17/20であり、**17次元の滑らかな変形空間を得たという意味ではない**。一次非分解可能なaは二次で障害を持つ。Ore局所化・偏極の一意性・二次coverの全Artin復元を通じ、偏極付き古典的変形関手の比較を条件付きで論じる。Yekutieli/De Deken–Lowen/Kontsevichの適用の独立監査、Kuznetsov側から定める可換対応との一致は未解決。元PDFの全成果を代替できていないため原資料は保留する。

## 全混合族の二次中心と固定剛体ambientの例

`papers/sections/central_pair_mixed_derived_rigid.tex` へ、旧論文V§19–21の低次数中心、偶数Veronese復元、構造対象を固定した導来復元（Serre functor=(-2)[3]）、一般混合potentialのblock同型判定を移植した。具体例 `F_*=(x^3+y^3+z^3)/3+uxy+vyz+(u+v)zx` の周囲 `B_*` に対し、全三次中心元 `G_*` の多項式公式をnc-cubic論文Aの普遍公式と係数ごとに照合した。その上で境界THCRの平行移動の位数6を入力とする条件下で `Aut_gr(B_*)=k^×` と固定周囲内の四係数非同型族を示す。正則なtailsを持つ非空開集合の存在はRSVdB/Rainsの一次資料と有限中心性の独立監査が未了なので追加条件付きであり、既に証明された無条件の定理とは扱わない。
