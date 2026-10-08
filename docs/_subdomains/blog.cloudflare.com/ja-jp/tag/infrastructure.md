---
url: https://blog.cloudflare.com/ja-jp/tag/infrastructure/
title: \"\u30a4\u30f3\u30d5\u30e9\u30b9\u30c8\u30e9\u30af\u30c1\u30e3\" \u30bf\u30b0\u306e\u6295\u7a3f \u2014 Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:18:40.802703+00:00
---

# "インフラストラクチャ" タグの投稿 — Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/tag/infrastructure/

TAG

# インフラストラクチャ

[インフラストラクチャ RSSフィードを購読する](https://blog.cloudflare.com/ja-jp/tag/infrastructure/rss)

2026年6月1日## [当社がコアユニットの起動時間を数時間から数分に短縮した方法](https://blog.cloudflare.com/ja-jp/optimizing-core-unit-boot-time/)

当社は、ファームウェアのアップデートによって、コアサーバーの再起動に4時間もかかる理由を調査しました。UEFIのデータ構造とiPXEの自動化を精査することで、不要なタイムアウトが排除され、起動時間を数分に短縮しました。

![Giovanni Pereira Zantedeschi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48NAJ0BZMGGKBFTQQ4C0AH.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nnamdi Ajah](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WTZG75GP6EEN6AE7KXBD.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Omar Sheikh-Omar](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HRKA5D763GGGRFFTW2GB.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Giovanni Pereira Zantedeschi](https://blog.cloudflare.com/ja-jp/author/giovanni/)、[Nnamdi Ajah](https://blog.cloudflare.com/ja-jp/author/nnamdi/)、[Omar Sheikh-Omar](https://blog.cloudflare.com/ja-jp/author/omar-sheikh-omar/)

2026年4月16日## [超大規模言語モデルを動かすための基盤構築](https://blog.cloudflare.com/ja-jp/high-performance-llms/)

Cloudflareのインフラ上で高速に大規模言語モデル（LLM）を動かすために、独自の技術スタックを構築しました。本記事では、高性能なAI推論を誰でも利用できるようにするために必要な、設計上のトレードオフや技術的な最適化について解説します。

![Michelle Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44R95PPSQQ82Z92P51M550.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Kevin Flansburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW452TM72EKFE8RQCD3JMXND.png&w=64&h=64&f=webp&fit=cover&position=center)![Vlad Krasnov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TTHCQACMZ5JZDGQP8RSQ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michelle Chen](https://blog.cloudflare.com/ja-jp/author/michelle/)、[Kevin Flansburg](https://blog.cloudflare.com/ja-jp/author/kevin-flansburg/)、[Vlad Krasnov](https://blog.cloudflare.com/ja-jp/author/vlad-krasnov/)

2026年3月26日## [年間600時間を削減した１行のKubernetes修正](https://blog.cloudflare.com/ja-jp/one-line-kubernetes-fix-saved-600-hours-a-year/)

Atlantisインスタンスが再起動に30分かかった理由を調査したところ、Kubernetesがボリューム許可を処理する方法にボトルネックがあることがわかりました。fsGroupChangePolicyを調整することで、再起動時間を30秒に短縮しました。

![Braxton Schafer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45N6SPVMSAH9848VNNQD2K.png&w=64&h=64&f=webp&fit=cover&position=center)

[Braxton Schafer](https://blog.cloudflare.com/ja-jp/author/braxton-schafer/)

2026年3月23日## [Cloudflareの第13世代サーバーのローンチ：キャッシュとコアを交換して、2倍のエッジコンピューティングパフォーマンスを実現](https://blog.cloudflare.com/ja-jp/gen13-launch/)

Cloudflareの第13世代サーバーは、キャッシュとコアのバランスを再考することで、コンピューティングスループットを2倍にしました。高コア数のAMD EPYC™ Turin CPUに移行し、大規模なL3キャッシュを犠牲にして計算密度を高めました。新しいRustベースのFL2スタックを実行することで、遅延のペナルティを完全に軽減し、パフォーマンスを2倍にしました。

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jesse Brandeburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4807Z4GQMH91EPHZ1WRAGR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/ja-jp/author/syona/)、[JQ Lau](https://blog.cloudflare.com/ja-jp/author/jq/)、[Jesse Brandeburg](https://blog.cloudflare.com/ja-jp/author/jesse-brandeburg/)

2026年2月13日## [Equinixによる古いコードの廃棄：CloudflareにおけるRustサービスのグレースフルリスタート](https://blog.cloudflare.com/ja-jp/ecdysis-rust-graceful-restarts/)

ecdysisは、ネットワークサービスのダウンタイムアップグレードを可能にするRustライブラリです。Cloudflareは、数百万の接続を5年間保護し、現在はオープンソースとなっています。

![Manuel Olguín Muñoz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MRZQBM4H5K19ZVS98WTD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Manuel Olguín Muñoz](https://blog.cloudflare.com/ja-jp/author/manuel-olguin-munoz/)

2025年12月22日## [Workersが社内メンテナンススケジュールパイプラインを強化する方法](https://blog.cloudflare.com/ja-jp/building-our-maintenance-scheduler-on-workers/)

グローバルネットワークでは、物理的なデータセンターのメンテナンスにリスクが伴います。さらに、複数のデータソースと指標パイプラインに加え、グラフインターフェイスでインフラストラクチャの状態を表示することで、スケーリングの課題を解決しながら、Workers上でサービスを停止させるような保守スケジューラーを構築しました。

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/ja-jp/author/kevin-deems/)、[Michael Hoffmann](https://blog.cloudflare.com/ja-jp/author/michael-hoffmann/)
