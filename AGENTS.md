# nc-cubic2 AGENTS.md

**最初に `00_research_plan.md`、次に `notes/research_notes.md` を読む。**

- このリポジトリは独立境界研究の正本。三つの主目標と可換復元の最優先研究は `uedakazushi/nc-cubic` で行う。
- 研究内容を移す際は、原稿の証明全文・入力・再現コード・文献情報を含める。移管先のblob/hash/組版/計算確認を済ませるまでは移管元の唯一の原本を削除しない。
- 論文は `papers/`、ノートは `notes/`、コードは `computations/`。日本語LuaLaTeXで `.latexmkrc` を用いて再生成する。
- 原PDFは完全なTeX置換の検証前に廃棄しない。Git管理のPDF例外は本当に原本が唯一の情報源である場合だけ。
- GitHub mainへ通常fast-forwardで更新し、遠隔ファイルを再取得して確かめる。force push、PR、GitHub Actionsを通常使わない。
- LibraryはGitHub push失敗時の緊急退避のみ。旧版・重複・ログを積まない。重要な主張の確実性（証明済み・条件付き・未完成・予想・計算観察）を区別する。
