# 六・七次元Poisson cubicの退化スキームと完全交叉

**2026-11-12 / v1。再開時は 00_research_plan.md を先に読む。**
本研究の原稿は `papers/poisson_cubic_six_seven_geometry.tex`。
同一リポジトリ内の次の3つの節原稿を入力する。

- `papers/sections/poisson_cubic_degeneracy_background.tex`：
  一般の退化イデアル、finite flat critical covers、零点完全交叉の証明
- `papers/sections/poisson_cubic_six_seven_geometry.tex`：
  六・七次元の階数二・四・六、退化スキームのprimary分解、長さ計算
- `papers/sections/poisson_cubic_six_seven_numerical.tex`：
  Chern類・Hodge数・算術種数の計算、Fermat型厚化

主リポジトリ `uedakazushi/nc-cubic` の論文Aは
全次元Poisson正規形・退化スキームの一般定理・量子化・モジュライを扱う。
本草稿は特定次元の詳細な幾何を扱う**別の研究対象**であり、
論文Aの主定理の証明には必要ない。

## 有効な数学的内容と評価

**六次元・階数二：** 一般のactive三次元部分空間に対し
`D_0(pi_X)=C sqcup Y`、`Y=(2,2,2,3) in P^7`は
滑らかな一般型三次元多様体。degree=24、
`K_Y=H`、`K_Y^3=24`、`p_g=8`、
`h^{1,1}=1`、`h^{2,1}=246`、Euler=-504。
これらは完全交叉の標準的公式からの帰結なので、
数値だけでは独立論文としての強い新規性は主張できない。

**七次元・階数二：**
`Y=(2,2,2,3) in P^8`は滑らかなCalabi--Yau四次元多様体。
degree=24、Euler=1152、
`h^{1,1}=1`、`h^{2,1}=0`、
`h^{3,1}=183`、`h^{2,2}=780`。
Calabi--Yauの標準的な完全交叉数値だが、
Poisson零点の成分として現れることには幾何学的意味がある。

**階数四：** 共通中心変数m=2,3のcritical coverは
それぞれ有限平坦degree=64。
`Z=(2^6,3)`はdegree=192。
n=6では一般に192個の被約点、n=7では種数577の滑らかな曲線。
`K_s=(2,2,2)`はn=6でdegree8・genus5の曲線、
n=7ではdegree8のK3曲面。
底上の平坦な三次曲面族を通じて退化部分の幾何を記述する。

**七次元・階数六（本草稿で最も優先する独立課題）：**
`F=f(a)+g(b)+h(c)`、各`f,g,h`は滑らかな平面三次曲線。
高次退化`D_4(pi_X)`のprimary分解では
`J_3`が被約成分、他の3つの三次四次元成分の
generic transverse lengthが8。
`D_2(pi_X)`の分解には曲線`E_f,E_g,E_h`を台とする
embedded primary componentsがあり、それぞれの横断長は64。
被約化の核の横断長は49で、64と区別する。
**本文には具体的なイデアル交叉等式と証明を保持。**
ただしprimary性と平坦な局所化の議論の独立再監査・
先行研究上の新規性の照合はまだ必要。
独立論文を狙う価値があるのは主にこのscheme-theoretic部分である。

**Fermat特異な零点厚化：**
n=6,k=2,m=2では中心P¹上の3点の各々が横断長64、
n=7,k=2,m=3では中心P²のFermat楕円曲線に
横断長64の厚みが生じる。
一般データとdegreeや算術種数は一致しても
被約性と滑らかさは異なる。
本稿の数値計算節に独立の説明を収録した。

## 証明への依存と検証状態

1. 一般Poisson正規形 `thm:pg-normal` は
   主リポジトリ `uedakazushi/nc-cubic` の
   `papers/support/papers/sections/poisson_geometry.tex` に
   証明のある**既存入力定理**。本草稿は定理を明記して使うが
   そのLie代数補題の独立再監査は未完成。
2. 本稿で使う一般退化イデアル・critical cover・零点完全交叉の
   命題と証明は、TeX節に全文収録済み。
   正規形を除き、当該幾何を理解するために旧版bundleは必要ない。
3. 移管時、一般背景、六・七次元の節、数値計算節の本文は
   元の論文Aの該当テキストと**逐字一致**することをGitHub取得結果で確認。
   Fermatの6/7特殊化とAS数値例は数値計算節に加えて保持。
   その後、論文Aから専用節を除外した。
4. 数値の厳密再計算 `computations/verify_poisson_cubic_six_seven_numerics.py`
   はSymPyによって各完全交叉のChern類・Euler・Hodge数・
   算術種数・長さの整合性を検算する。
   同等のSymPyコードをローカル実行してPASS。
   これはprimaryイデアルの全計算を実行したという意味ではない。
5. TeXの参照ラベル・入力パス・文献キーの静的整合性を確認。
   **新しい統合稿のLuaLaTeX実組版・PDF目視は未実施**。
   書誌と重要先行研究の一次資料照合は未完了。
6. ファイルの存在、TeXの生成、静的検査、計算の実行、
   mainへの保存、PDF組版の各状態を区別して扱う。

## 優先する次の研究課題

第一に、七次元階数六の`D_4,D_2`の局所primary分解と
embedded componentのgeneric lengthを、手計算・CASを併用して独立監査する。
第二に、退化スキームのembedded associated primesの
一般次元における構造との関係を調べる。
第三に先行研究の一次資料との比較で公表価値を確定し、
価値が確認できた場合のみ独立論文化を進める。
その間、論文Aの一般次元正規形・量子化・スタックの公表準備を優先する。

## 再生成・再現

リポジトリのルートから

```sh
latexmk papers/poisson_cubic_six_seven_geometry.tex
python3 computations/verify_poisson_cubic_six_seven_numerics.py
```

TeX Live/LuaLaTeX、`ltjsarticle`、`luatexja-fontspec`、
`amsmath`、`amsthm`、`booktabs`、日本語フォントHaranoAji、
およびSymPyが必要。
PDFはbuild/へ生成してGit追跡しない。
GitHub mainが正本。GitHub Actions・force pushを使わない。
GitHub保存に成功した場合はLibraryへ二重保存しない。
