# 研究ノート：Poisson cubic \(n\)-fold pair の全次元既約成分

**2026-11-11 / v1。再開時は `00_research_plan.md` から始める。**

## 現時点で成立している帰結とその前提

対象は \(n\ge3\) の滑らかな \(X=V(F)\subset\mathbb P^{n+1}\) と非零のPoisson双ベクトル \(\pi\) の同時モジュライ。射影座標変換で割るが、\(\pi\) のスカラーは割らない。既約成分はschemeの基礎位相空間の意味。

**主結果（既存Poisson正規形定理を仮定する帰結）**：\(N=n+2\) とすると、非零Poisson pairの既約成分数は \(\lfloor N/3\rfloor\)。一般Poisson階数が \(2k\) の成分が \(1\le k\le\lfloor N/3\rfloor\) に各一つある。商の次元は

\[
d_{n,k}=k(3N-8)+{m+2\choose3}
+k\left(10+6m+3{m+1\choose2}\right)-N^2,\quad m=N-3k.
\]

隣接する成分の商以前の次元差は \(3(3k-1)(N-3k)+8>0\)。supportの縮約写像の階数 \(3k\) はdeterminantalな閉条件で上から制御でき、これと次元の単調性により、rankの異なる既約層の閉包は互いに包含されない。軌道・線形三次式のパラメータ空間を用いた全文証明は `papers/poisson_cubic_pair_components.tex`。

**入力**：`uedakazushi/nc-cubic/papers/sections/poisson_geometry.tex`（`thm:pg-normal`、`prop:pg-represent`、`prop:pg-jacobi-extension`）。これは既存原稿に証明記載のある定理であり、今回すべてを独立に再検証したという意味ではない。この依存が破綻した場合は全次元分類の再評価が必要。

## 関連する n=4 の深化

`papers/poisson_cubic_fourfold_moduli.tex` は rank4 成分のgeneric smoothnessを、Fermat点でのJacobi線形化の非零36次小行列式によって調べる独立稿。全次元の位相的分類は今回の一般稿に集約し、四次元原稿はscheme構造の深掘りに充てる。零Poissonについては基礎位相空間では新成分を生じない。固定Fermat fiberの多数の成分とは区別する。

## 未解決の核心・着手方法

1. Poisson正規形定理の全次元での独立監査、特にHessian空間のbase-point-free性から半単純Lie代数の$\mathfrak{sl}_2$成分への還元を検証する。
2. 各成分のgeneric reducedness、特にrank2と \(k\ge3\) の場合。特殊Fermat例でJacobi微分の接空間を計算し、次に一般性を確認する。
3. 低rank閉包と高rank閉包の交叉、零切断のscheme構造、埋め込まれた成分。
4. Poisson schemeではなく商スタックまたは粗モジュライの存在を明確に区別し、安定化群・境界・non-separated性を検討する。
5. Pymの概説と原典を含めた徹底的な一次文献の新規性照合。全次元の結論が未発表であると現時点では断言しない。

## 検算と組版

- `python3 computations/verify_poisson_cubic_pair_dimensions.py`：Python標準ライブラリだけで \(3\le n\le20\) の整数係数・次元差を検算。
- `latexmk papers/poisson_cubic_pair_components.tex`：日本語LuaLaTeX。VS CodeのLaTeX Workshopは `.vscode/settings.json` でリポジトリrootをworking directoryに固定し、`build/`へ出力する。
- `papers/poisson_cubic_fourfold_moduli.tex` は四次元のscheme的追加結果を保持。無限次元の一般Poisson理論は計算コードの対象外。

## 文献

- 現行正規形定理：<https://github.com/uedakazushi/nc-cubic/blob/main/papers/sections/poisson_geometry.tex>
- B. Pym, *Constructions and classifications of projective Poisson varieties*, Lett. Math. Phys. 108 (2018), 573–632, <https://doi.org/10.1007/s11005-017-0984-5>（概説）
- H. Matsumura, P. Monsky, *On the automorphisms of hypersurfaces*, J. Math. Kyoto Univ. 3 (1964), 347–361（書誌・適用条件の一次再確認未実施）
