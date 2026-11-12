# 研究ノート：滑らかな cubic fourfold の Poisson pair モジュライ

**2026-11-11 / v1。最初に `00_research_plan.md` を読む。**

## 現時点の分類とその依存関係

対象は \(U\subset\mathbb P(\operatorname{Sym}^3\mathbb C^6)^*\) の滑らかなcubicと、非零の正則Poisson双ベクトルの組。スカラーを割らず、同時射影座標変換 \(\operatorname{PGL}_6\) で割る。商スタックおよび幾何学的モジュライの**基礎位相空間**を対象とし、nilpotentなscheme構造は区別する。

**既存の証明を入力とする帰結（新規性と独立再監査は未確認）:** `uedakazushi/nc-cubic` の `papers/sections/poisson_geometry.tex`、`thm:pg-normal` と、その前の双ベクトル表示・Jacobi定理を用いると、\(N=6\) の非零Poisson三重ベクトル \(P\) は \(k=1\) 分解可能、または \(k=2\) 二つの独立な3ブロック上の三重ベクトルの和となる。一般階数は2と4。階数二の全体は滑らかな三次式の55次元パラメータに非零Grassmann錐10次元を付けた既約65次元。階数四の \(P\) は \(\wedge^3\mathbb C^6\) の20次元開軌道、許される \(F\) は分離された二つの三変数三次式で射影19次元、合計39次元の既約族。35次元 \(\mathrm{PGL}_6\) で割り、有限安定化群により成分は**正確に2個、次元30と4**。

`papers/poisson_cubic_fourfold_moduli.tex` に分類の証明をまとめた。**今回独立に検証したのは有限例のJacobi条件・rank・整数次元計数と、この論理的な既約性の組合せであり、入力正規形定理の深いLie理論的証明そのものではない。**

## 新しい厳密計算：rank4成分のgeneric reducedness

分離Fermat点 \(F_0=\sum_i x_i^3,\ P_0=e_{123}+e_{456}\) で、Jacobi式の \(F\) 方向の微分を混合三次式の36方向に制限した \(720\times36\) 整数行列の階数は36。36次の非零小行列式は \(-39346408075296537575424\)。列は36混合三次単項式、行は20三重添字×36混合三次単項式。行番号と再現の詳細は論文命題 `prop:rank4-generically-smooth` および `computations/verify_poisson_cubic_fourfold_tangent.py`。rank4の集合論的な39次元正規形を入力すれば、Fermat点での局所接空間は39次元で滑らか。rank4成分はgeneric reduced。rank2成分と交叉のscheme構造については依然未解決。

## 複数の成分を混同しない

固定Fermat cubic fourfoldでは、6変数を二つの3変数に分割する組合せが10通り存在する。固定fiberで見えるrank4成分が、cubicを動かすと一つの既約なrank4 locusに統合される。零Poissonを含めても零切断はrank2成分に含まれる。Poissonスカラーを割れば次元は29と3となる。

## 具体的な着手方法

1. **正規形定理の独立監査**：次数二のHessian空間 \(K(P)\) の基点自由性から \(\mathfrak{sl}_2\) ブロックへ至る推論を六変数で直接再検証。必要なら六次元三重ベクトルのGL6軌道分類を用いて境界軌道を排除する。定理本体の引用だけに依存しない証明を公表稿に組み込む。
2. **rank4の局所scheme**：\(P=e_{123}+e_{456}\) で \([\pi,\pi]=0\) のJacobian線形化とPoisson deformation complexを計算し、rank4成分のgeneric reducednessを検証する。スカラー・座標群の方向と核を分離する。
3. **rank2の局所scheme**：一般\((F,P)\)でPlücker錐以外の無限小Poisson方向がないか調べる。集合論的既約性だけからreducednessを推論しない。
4. **交叉と境界**：安定三重ベクトルのquartic判別式を0へ退化させつつ \(F\) の滑らかさを保つ族を追跡し、二成分の交叉点・交叉イデアル・埋め込み成分を特定する。rank4の39次元閉包がrank2の65次元 locus全体を含むことは不可能。
5. **先行研究**：Pym 2018のサーベイ、Mayanskiy（cubic threefold）、Loray–Pereira–Touzet、および六変数三重ベクトル軌道論を一次資料で再照合。今回のweb確認では、四次元の同時Poisson-pairの成分数と次元を既に掲載する一次論文は未特定。存在しないとは断定しない。

## 再現可能性

`python3 computations/verify_poisson_cubic_fourfold.py`（SymPy必須）は分離Fermat例のJacobi 20三つ組、混合項での非Jacobi、\(F=0\) 上のアフィンrank4、成分の次元算定を有理数上で検算。生成・検算コードは証明ではなく、局所テストである。`latexmk papers/poisson_cubic_fourfold_moduli.tex` でLuaLaTeX組版、生成PDFは `build/` に置きGit追跡しない。

## 文献入口

- 主入力：<https://github.com/uedakazushi/nc-cubic/blob/main/papers/support/papers/sections/poisson_geometry.tex>（未公表の本研究原稿）
- Brent Pym, *Constructions and classifications of projective Poisson varieties*, Lett. Math. Phys. 108 (2018), 573–632, <https://doi.org/10.1007/s11005-017-0984-5>（概説、四次元の完全分類の根拠にはしない）
- E. Mayanskiy, *Poisson cohomology of two Fano threefolds*, J. Algebra 424 (2015), 21–45, <https://arxiv.org/abs/1303.5916>（三次元）
- H. Matsumura and P. Monsky, *On the automorphisms of hypersurfaces*, J. Math. Kyoto Univ. 3 (1964), 347–361（最終稿で原典の書誌・適用条件を再確認）
