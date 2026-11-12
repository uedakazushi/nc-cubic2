# 研究ノート：滑らかな cubic fourfold の Poisson pair モジュライ

**2026-11-12 / v2。最初に `00_research_plan.md` を読む。**

## 既存研究（主リポジトリ）の入力

一般次元Poisson cubic pairの集合論的成分分類・商次元、固定/相対stackの代数性は`uedakazushi/nc-cubic`論文Aの`papers/support/papers/sections/fermat_relative_poisson_components.tex`と`poisson_moduli_stacks.tex`が正本。本稿ではその証明を繰り返さない。fourfoldのrank2/rank4の2成分（商次元30/4）はその特殊化。正規形の独立監査と新規性確認は未完了。

## 新しい厳密計算：rank4成分のgeneric reducedness

分離Fermat点 \(F_0=\sum_i x_i^3,\ P_0=e_{123}+e_{456}\) で、Jacobi式の \(F\) 方向の微分を混合三次式の36方向に制限した \(720\times36\) 整数行列の階数は36。36次の非零小行列式は \(-39346408075296537575424\)。列は36混合三次単項式、行は20三重添字×36混合三次単項式。行番号と再現の詳細は論文命題 `prop:rank4-generically-smooth` および `computations/verify_poisson_cubic_fourfold_tangent.py`。rank4の集合論的な39次元正規形を入力すれば、Fermat点での局所接空間は39次元で滑らか。rank4成分はgeneric reduced。rank2成分と交叉のscheme構造については依然未解決。

## 具体的な着手方法

1. **正規形定理の独立監査**：次数二のHessian空間 \(K(P)\) の基点自由性から \(\mathfrak{sl}_2\) ブロックへ至る推論を六変数で直接再検証。必要なら六次元三重ベクトルのGL6軌道分類を用いて境界軌道を排除する。定理本体の引用だけに依存しない証明を公表稿に組み込む。
2. **rank4の局所scheme**：\(P=e_{123}+e_{456}\) で \([\pi,\pi]=0\) のJacobian線形化とPoisson deformation complexを計算し、rank4成分のgeneric reducednessを検証する。スカラー・座標群の方向と核を分離する。
3. **rank2の局所scheme**：一般\((F,P)\)でPlücker錐以外の無限小Poisson方向がないか調べる。集合論的既約性だけからreducednessを推論しない。
4. **交叉と境界**：安定三重ベクトルのquartic判別式を0へ退化させつつ \(F\) の滑らかさを保つ族を追跡し、二成分の交叉点・交叉イデアル・埋め込み成分を特定する。rank4の39次元閉包がrank2の65次元 locus全体を含むことは不可能。
5. **先行研究**：Pym 2018のサーベイ、Mayanskiy（cubic threefold）、Loray–Pereira–Touzet、および六変数三重ベクトル軌道論を一次資料で再照合。今回のweb確認では、四次元の同時Poisson-pairの成分数と次元を既に掲載する一次論文は未特定。存在しないとは断定しない。

## 再現可能性

`python3 computations/verify_poisson_cubic_fourfold_tangent.py`（SymPy必須）は追加の36次小行列式の検算。原稿に証明があることと今回の再実行を区別し、今回の再実行は未実施。`latexmk papers/poisson_cubic_fourfold_moduli.tex` でLuaLaTeX組版、生成PDFは `build/` に置きGit追跡しない。

## 文献入口

- 主入力：<https://github.com/uedakazushi/nc-cubic/blob/main/papers/support/papers/sections/poisson_geometry.tex>（未公表の本研究原稿）
- Brent Pym, *Constructions and classifications of projective Poisson varieties*, Lett. Math. Phys. 108 (2018), 573–632, <https://doi.org/10.1007/s11005-017-0984-5>（概説、四次元の完全分類の根拠にはしない）
- E. Mayanskiy, *Poisson cohomology of two Fano threefolds*, J. Algebra 424 (2015), 21–45, <https://arxiv.org/abs/1303.5916>（三次元）
- H. Matsumura and P. Monsky, *On the automorphisms of hypersurfaces*, J. Math. Kyoto Univ. 3 (1964), 347–361（最終稿で原典の書誌・適用条件を再確認）
