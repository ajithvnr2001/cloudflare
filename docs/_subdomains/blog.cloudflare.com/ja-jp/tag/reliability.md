---
url: https://blog.cloudflare.com/ja-jp/tag/reliability/
title: \"\u4fe1\u983c\u6027\" \u30bf\u30b0\u306e\u6295\u7a3f \u2014 Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:18:54.532643+00:00
---

# "信頼性" タグの投稿 — Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/tag/reliability/

TAG

# 信頼性

[信頼性 RSSフィードを購読する](https://blog.cloudflare.com/ja-jp/tag/reliability/rss)

2026年4月22日## [Rust Workersを信頼性を高める：Wasm-bindgenでのパニックと回復を中断する](https://blog.cloudflare.com/ja-jp/making-rust-workers-reliable/)

Rust Workersのパニックは以前は致命的で、インスタンス全体が汚染されていました。Rust Workersは、Wasm-bindgenプロジェクトでアップストリームと共同作業することによって、WebAssembly Integration 全体を使用したパニックからの解消を含む、回復力のある重大なエラーの復旧をサポートするようになりました。

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/ja-jp/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/ja-jp/author/hood/)、[Logan Gatlin](https://blog.cloudflare.com/ja-jp/author/logan-gatlin/)

2025年12月22日## [Workersが社内メンテナンススケジュールパイプラインを強化する方法](https://blog.cloudflare.com/ja-jp/building-our-maintenance-scheduler-on-workers/)

グローバルネットワークでは、物理的なデータセンターのメンテナンスにリスクが伴います。さらに、複数のデータソースと指標パイプラインに加え、グラフインターフェイスでインフラストラクチャの状態を表示することで、スケーリングの課題を解決しながら、Workers上でサービスを停止させるような保守スケジューラーを構築しました。

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/ja-jp/author/kevin-deems/)、[Michael Hoffmann](https://blog.cloudflare.com/ja-jp/author/michael-hoffmann/)

2024年3月4日## [CISAのセキュア・バイ・デザイン原則による業界の変化](https://blog.cloudflare.com/ja-jp/secure-by-design-principles/)

セキュリティの考慮はソフトウェア設計時の必須要素とすべきであり、後から考えるべきではありません。CloudflareがどのようにCISAのセキュア・バイ・デザイン原則を遵守し、業界を変革しているかについて説明します

![Kristina Galicova](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SE6FVY39NNKJ8GYZXBZN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Edo Royker](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NPG0HKPB45GKW757SAW2.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kristina Galicova](https://blog.cloudflare.com/ja-jp/author/kristina-galicova/)、[Edo Royker](https://blog.cloudflare.com/ja-jp/author/edo-royker/)

2018年9月24日## [暗号化か喪失か。SNI暗号化の仕組みについて](https://blog.cloudflare.com/ja-jp/encrypted-sni/)

Cloudflareが本日サポートを発表した、暗号化SNIは、拡張版TLS 1.3プロトコルであり、ISP、カフェ店主、ファイアウォールなどのパス上のオブザーバーが、TLS Server Name Indication（SNI）拡張子を傍受し、これを利用してユーザーの訪問先のWebサイトを特定することを防止し、インターネットユーザーのプライバシーを向上させます。

![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alessandro Ghedini](https://blog.cloudflare.com/ja-jp/author/alessandro-ghedini/)

2017年9月25日## [定額制DDoS軽減：無制限のDDoS攻撃対策](https://blog.cloudflare.com/ja-jp/unmetered-mitigation/)

Cloudflare 7回目のバースデーウィークです。週の毎日、一連の製品を発表し、お客様に大きな新しいメリットをもたらすことが恒例になっています。まずは、特に自信のあるものからご紹介します。定額制の軽減です

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/ja-jp/author/matthew-prince/)

2016年6月29日## [「Go net/http タイムアウト」の完全ガイド](https://blog.cloudflare.com/ja-jp/the-complete-guide-to-golang-net-http-timeouts/)

GoでHTTPサーバーまたはクライアントを書くとき、タイムアウトは、最も間違えやすく、そして最も軽微な間違えです。選択する対象が数多くあり、間違えても、ネットワークの不具合やプロセスがハングアップするまで、長い間、何の影響もありません。

![Filippo Valsorda](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GAVR9Z506KS1WDKSMTBM.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Filippo Valsorda](https://blog.cloudflare.com/ja-jp/author/filippo/)
