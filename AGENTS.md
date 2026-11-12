# nc-cubic2 AGENTS.md

**最初に `00_research_plan.md` を読む。一般次元Poisson分類はnc-cubic論文Aを正本とする。fourfoldのscheme構造は `notes/poisson_cubic_fourfold_moduli.md`、非可換三次三様体の17次元モジュライは `notes/nc_cubic_threefold_moduli.md` と `papers/nc_cubic_threefold_moduli.tex` を読む。それ以外は `notes/research_notes.md` を読む。**

- **6/7次元Poisson cubic幾何**：`notes/poisson_cubic_six_seven_geometry.md`、
  `papers/poisson_cubic_six_seven_geometry.tex`、
  `computations/verify_poisson_cubic_six_seven_numerics.py` を使用。
  旧main論文Aから専用節を移し、原文の完全一致を確認済み。
  一般退化イデアルの証明も移管先に保持し、
  主リポジトリAには一般次元の定理・証明を残す。
  一般rank/成分数より独立な価値の候補は七次元rank6の
  primary分解とembedded componentsの長さ。
  独立監査と新規性確認は未完成。
- 本リポジトリは独立モジュライ・境界研究の正本。17次元nc cubic moduli研究を統合し、構成族の既約成分性・接空間と障害理論を未解決の主課題とする。Poisson構造・代数量子化・一般次元ambient復元・rotation付き可換復元の主論文A/Cは `uedakazushi/nc-cubic` にある。
- 17次元nc cubicの41次元incidence、31次行列式、分離型余次元15、忘却核7、Picard障害は現行 `papers/nc_cubic_threefold_moduli.tex` と `papers/sections/mixed_center_picard.tex` に収録した。横断性・中心・分離型の計算ソースは `computations/independent/` と `computations/verify_split_codimension.py`。独立監査・LuaLaTeX実組版・本移管後のスクリプト再実行は未了。一般次元ambient復元は主リポジトリAに統合し、旧Bに依存しない。
- 研究内容を移す際は、原稿の証明全文・入力・再現コード・文献情報を含める。移管先のblob/hash/組版/計算確認を済ませるまでは移管元の唯一の原本を削除しない。
- 論文は `papers/`、ノートは `notes/`、コードは `computations/`。日本語LuaLaTeXで `.latexmkrc` を用いて再生成する。
- 原PDFは完全なTeX置換の検証前に廃棄しない。Git管理のPDF例外は本当に原本が唯一の情報源である場合だけ。
- GitHub mainへ通常fast-forwardで更新し、遠隔ファイルを再取得して確かめる。force push、PR、GitHub Actionsを通常使わない。
- LibraryはGitHub push失敗時の緊急退避のみ。旧版・重複・ログを積まない。重要な主張の確実性（証明済み・条件付き・未完成・予想・計算観察）を区別する。

- Poisson cubic fourfold の同時モジュライは、集合論的既約成分分類（正規形定理依存）と、未解決のscheme構造・新規性を厳密に区別する。Poissonスカラーを割るか保持するかを常に明記する。入力定理の独立監査を最優先し、既存のnc-cubicの可換復元作業は変更しない。

- 一般次元Poisson成分分類・次元公式はnc-cubic論文Aを正本とし、本リポジトリでは重複させない。fourfold稿には追加的scheme smoothnessを保持する。
- VS Code LaTeX Workshopは `.vscode/settings.json` の明示的なcwdとルート `.latexmkrc` を使用する。TeXはLuaLaTeX、出力はbuild、生成PDFは追跡しない。

- The 79 sections of `papers/pfaffian_brill_noether_technical.tex` have been divided losslessly among five thematic `papers/sections/` inputs; the parent `.tex` is the sole entry point. The final verification input contains legacy version records and may refer to missing computation files; audit before treating them as reproducible. See `papers/README.md`.

- The former five version-specific verification-history sections have been replaced by one current proof-dependency and reproducibility section. Missing `verification/` and `source_vNN/` are NOT valid current reproduction commands. Preserve actual theorems in the two contact-normal-form inputs; rebuild only essential certificates. No GitHub Actions.

- Highest immediate priority: eliminate remaining pdf-only files by proving their valuable results in current Japanese LuaLaTeX and then removing tracked originals. Do NOT delete the five research-paper PDFs just on heading correspondence. Library has matching-size source PDFs; the old III contains additional nonlinear contact / Hessian / Pfaffian graph results absent from the current long TeX. The now-consolidated finite-smoothness research note is in `notes/ambient_finite_smoothness_and_recovery.tex`. Keep GitHub main canonical and no Actions.

- `papers/sections/pfaffian_hessian_geometry.tex` now contains the restored proofs of the Hessian 5-variable Milnor/Tjurina and Pfaffian graph strict transform/quadric fibration. Do not conflate these with the full nonlinear-contact classification and vertex-kernel claims in the old PDF paper III; those remain unincorporated and require independent audit before removing `pfaffian_contact.pdf`.

- The PDF V's valuable Artin-local moduli comparison has been restored in `papers/sections/central_pair_artin_formal_moduli.tex`, included from `papers/nc_cubic_threefold_moduli.tex`. The 17-dimensional **topological** family is distinct from the obstructed Artin-local ring (dimension 17, tangent space 20). External Kontsevich/Yekutieli/De Deken--Lowen inputs need independent auditing. Do not delete PDF V until its mixed-center, rigid ambient example, and finite certificates are compared.

- Additional current source `papers/sections/central_pair_mixed_derived_rigid.tex` contains all-mixed low centers, even Veronese, derived O-marked reconstruction, and an explicit rigid ambient. Correctly distinguish a four-dimensional **pairwise nonisomorphic** family (under THCR input) from the stronger assertion of an open family with smooth tails, which has unverified Rains/RSVdB dependencies. Do not remove PDF V until its general Hesse center and certificate content is reconciled.

- Continue deletion-first PDF recovery: old paper VI now has `papers/central_quotient_local_models.tex` and `computations/verify_central_quotient_local_hessian.py` (four A1 points, Brauer index six, 21 central vs three homological singularities). Key finite-center, Azumaya, representation exclusion and singular-category proofs remain to be incorporated. Preserve original PDF until all valuable results are independently auditable. Other repository's paper V Artin-local source is already in `papers/sections/central_pair_artin_formal_moduli.tex`; avoid duplicating it.
