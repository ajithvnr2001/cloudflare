---
url: https://blog.cloudflare.com/ja-jp/tag/rust/
title: \"Rust\" \u30bf\u30b0\u306e\u6295\u7a3f \u2014 Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:18:56.838671+00:00
---

# "Rust" タグの投稿 — Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/tag/rust/

TAG

# Rust

[Rust RSSフィードを購読する](https://blog.cloudflare.com/ja-jp/tag/rust/rss)

2026年5月12日## [「idle」がアイドルではない場合：Linuxカーネルの最適化がQUICバグになった経緯](https://blog.cloudflare.com/ja-jp/quic-death-spiral-fix/)

CUBICの輻輳ウィンドウが最小フロアでピン留めとなり、パフォーマンスが低下するバグを調査しました。この修正には、RTT待機時間と実際のアプリケーションのアイドル状態を区別するために、アイドル時間を正しく測定することが含まれていました。

![Esteban Carisimo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VSSKPEBK3K5ND6JZ67YP.webp&w=64&h=64&f=webp&fit=cover&position=center)![Antonio Vicente](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487NFE7AY4B70WNGYX9WZ9.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Esteban Carisimo](https://blog.cloudflare.com/ja-jp/author/esteban-carisimo/)、[Antonio Vicente](https://blog.cloudflare.com/ja-jp/author/antonio-vicente/)

2026年4月22日## [Rust Workersを信頼性を高める：Wasm-bindgenでのパニックと回復を中断する](https://blog.cloudflare.com/ja-jp/making-rust-workers-reliable/)

Rust Workersのパニックは以前は致命的で、インスタンス全体が汚染されていました。Rust Workersは、Wasm-bindgenプロジェクトでアップストリームと共同作業することによって、WebAssembly Integration 全体を使用したパニックからの解消を含む、回復力のある重大なエラーの復旧をサポートするようになりました。

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/ja-jp/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/ja-jp/author/hood/)、[Logan Gatlin](https://blog.cloudflare.com/ja-jp/author/logan-gatlin/)

2026年4月17日## [Agents Week：ネットワークパフォーマンスの最新情報](https://blog.cloudflare.com/ja-jp/network-performance-agents-week/)

リクエスト処理レイヤーをFL2と呼ばれるRustベースのアーキテクチャに移行することで、Cloudflareは、世界のトップネットワークの60%につながるパフォーマンスを向上させました。当社は、実際のユーザーの測定値や接続解析を使用して、インターネット上で利用者の実際の体験を反映したデータを提供します。

![Lai Yi Ohlsen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DGMNXAW2CZQQAX92W97V.png&w=64&h=64&f=webp&fit=cover&position=center)

[Lai Yi Ohlsen](https://blog.cloudflare.com/ja-jp/author/lai-yi-ohlsen/)

2026年3月23日## [Cloudflareの第13世代サーバーのローンチ：キャッシュとコアを交換して、2倍のエッジコンピューティングパフォーマンスを実現](https://blog.cloudflare.com/ja-jp/gen13-launch/)

Cloudflareの第13世代サーバーは、キャッシュとコアのバランスを再考することで、コンピューティングスループットを2倍にしました。高コア数のAMD EPYC™ Turin CPUに移行し、大規模なL3キャッシュを犠牲にして計算密度を高めました。新しいRustベースのFL2スタックを実行することで、遅延のペナルティを完全に軽減し、パフォーマンスを2倍にしました。

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jesse Brandeburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4807Z4GQMH91EPHZ1WRAGR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/ja-jp/author/syona/)、[JQ Lau](https://blog.cloudflare.com/ja-jp/author/jq/)、[Jesse Brandeburg](https://blog.cloudflare.com/ja-jp/author/jesse-brandeburg/)

2026年2月13日## [Equinixによる古いコードの廃棄：CloudflareにおけるRustサービスのグレースフルリスタート](https://blog.cloudflare.com/ja-jp/ecdysis-rust-graceful-restarts/)

ecdysisは、ネットワークサービスのダウンタイムアップグレードを可能にするRustライブラリです。Cloudflareは、数百万の接続を5年間保護し、現在はオープンソースとなっています。

![Manuel Olguín Muñoz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MRZQBM4H5K19ZVS98WTD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Manuel Olguín Muñoz](https://blog.cloudflare.com/ja-jp/author/manuel-olguin-munoz/)

2025年12月18日## [R2 SQLでのGROUP BY、SUM、その他の集約クエリのサポートを発表](https://blog.cloudflare.com/ja-jp/r2-sql-aggregations/)

Cloudflareの分散クエリエンジンであるCloudflareのR2 SQLが集約をサポートするようになりました。スキャバージャーとシャッフル戦略を用いて、R2データカタログ上で直接分析を実行する方法をご覧ください。

![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Marc Selwan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455H274J0ZYJ6K4KHKJT25.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jérôme Schneider](https://blog.cloudflare.com/ja-jp/author/jerome/)、[Nikita Lapkov](https://blog.cloudflare.com/ja-jp/author/nikita-lapkov/)、[Marc Selwan](https://blog.cloudflare.com/ja-jp/author/marc-selwan/)

2025年10月28日## [インターネットの高速性と安全性を維持：Merkle Tree Certificatesの導入](https://blog.cloudflare.com/ja-jp/bootstrap-mtc/)

Cloudflareでは、パフォーマンスを低下させたり、WebPKIの信頼関係を変更することなく、高速でスケーラブル、かつ量子対応のMerkleツリー証明書を評価するための実験を、Chromeで開始します。

![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Christopher Patton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471WT491ZC11M0S5HA34X3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Vânia Gonçalves](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48DQDQ26SRVKPGYTBWBHMD.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bas Westerbaan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46N3BWJ6WS6790KRRJ4RWD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Luke Valenta](https://blog.cloudflare.com/ja-jp/author/luke/)、[Christopher Patton](https://blog.cloudflare.com/ja-jp/author/christopher-patton/)、[Vânia Gonçalves](https://blog.cloudflare.com/ja-jp/author/vania/)、[Bas Westerbaan](https://blog.cloudflare.com/ja-jp/author/bas/)

2025年9月26日## [CloudflareがRustによってさらに高速かつ安全に](https://blog.cloudflare.com/ja-jp/20-percent-internet-upgrade/)

Cloudflareは、NGINXを使った原コアシステムを、新しくRustベースのモジュールプロキシへリプレースしました。 

![Richard Boulton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WPC6H4PY51ETZPAGBKZ9.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Steve Goldsmith](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497YX7768BEJGS24P0FMX8.png&w=64&h=64&f=webp&fit=cover&position=center)![Maurizio Abba](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45R40JSMY4JX26YZV11150.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Matthew Bullock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ABWPJWE9RP8CPZF1G4F5.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Richard Boulton](https://blog.cloudflare.com/ja-jp/author/richard/)、[Steve Goldsmith](https://blog.cloudflare.com/ja-jp/author/steve-goldsmith/)、[Maurizio Abba](https://blog.cloudflare.com/ja-jp/author/maurizio-abba/)、[Matthew Bullock](https://blog.cloudflare.com/ja-jp/author/matthew-bullock/)

2025年7月24日## [Serverless Statusphere：Cloudflareの開発者プラットフォーム上でサーバーレスATProtoアプリケーションを構築する手順](https://blog.cloudflare.com/ja-jp/serverless-atproto/)

Cloudflare Workersで、リアルタイムの分散型認証転送プロトコル（ATProto）アプリを構築し、デプロイしましょう。

![Inanna Malick](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SJ7VTDH3QFFKFA26KM6J.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Inanna Malick](https://blog.cloudflare.com/ja-jp/author/inanna-malick/)

2024年2月28日## [Pingoraのオープンソース化：プログラマブルなネットワークサービスを構築するためのRustフレームワーク](https://blog.cloudflare.com/ja-jp/pingora-open-source/)

プログラマブルでメモリ安全性の高いネットワークサービスを構築するためのフレームワーク、Pingoraがオープンソース化されました。今すぐPingoraの使用を開始しましょう

![Yuchen Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CEA1K0ZA59ZK5J7QNRVF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Edward Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW461JESP3W5FAGRMPYV23AR.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yuchen Wu](https://blog.cloudflare.com/ja-jp/author/yuchen/)、[Edward Wang](https://blog.cloudflare.com/ja-jp/author/edward-h-wang/)、[Andrew Hauck](https://blog.cloudflare.com/ja-jp/author/andrew-hauck/)
