# 未移管のPDF原本と安全条件

2026-11-10。GitHub APIのテキスト処理ではPDFの非UTF-8バイナリを取得できず、異なるリポジトリ間でblob SHAをそのまま利用する操作も失敗した。下記は**nc-cubic2へ未転送**であり、元リポジトリ `uedakazushi/nc-cubic` の `main` が引き続き原本の保管先である。

| 原本（nc-cubic内） | Git blob SHA | 内容 |
|---|---|---|
| `papers/pdf-only/boundary/brill_noether.pdf` | `be40e4f4861a152e2e63f0d0e8f53dd536f644f1` | Brill–Noether境界 |
| `papers/pdf-only/boundary/pfaffian_contact.pdf` | `bdc41bf0b01b4f4b0bbeefd77c85c2afc5a297a3` | Pfaffian/contact |
| `papers/pdf-only/boundary/central_quotient_singularities.pdf` | `990fcfd2ff6890cb3317759252a1470bd6acdd97` | 中心商特異圏、Azumaya・Brauer |
| `notes/pdf-only/categorical_boundary_notes.pdf` | `7f8dffabc6dcc72327d69ab427251491ebd5210f` | 圏論的境界とgluing |

**転送手順：** 認証したGitクライアントで両リポジトリをcloneし、原本を移管先にコピーしてGit SHAを比較する。新しい場所からファイルが読み取れることを確認してから、旧側の追跡解除を検討する。なお可換復元に必要な部分を先に `nc-cubic` の研究ノートと原稿へ統合する。

PDFを整理することより主リポジトリの残余smoothness (SM) と可換復元を優先する。PDFにしかない定理・証明はTeX化の完了前には失われないよう保持する。
