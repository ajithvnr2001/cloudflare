---
url: https://blog.cloudflare.com/ja-jp/tag/performance/
title: \"\u30d1\u30d5\u30a9\u30fc\u30de\u30f3\u30b9\" \u30bf\u30b0\u306e\u6295\u7a3f \u2014 Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:18:50.130399+00:00
---

# "パフォーマンス" タグの投稿 — Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/tag/performance/

TAG

# パフォーマンス

[パフォーマンス RSSフィードを購読する](https://blog.cloudflare.com/ja-jp/tag/performance/rss)

2026年5月14日## [請求パイプラインが突然遅くなったのです。原因はClickHouseの隠れたボトルネックでした](https://blog.cloudflare.com/ja-jp/clickhouse-query-plan-contention/)

ペタバイト規模のClickHouseクラスターのパーティショニング変更によって重要な請求ジョブが停止したとき、標準的なメトリクスは明らかなエラーは示されませんでした。この記事では、当社がClickHouseのクエリプランナーで深刻なロックコンテンツを特定し、それを修正するためのアップストリームパッチをどのように構築したかを探ります。

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/ja-jp/author/james-morrison/)、[Christian Endres](https://blog.cloudflare.com/ja-jp/author/christian-endres/)

2026年4月17日## [Agents Week：ネットワークパフォーマンスの最新情報](https://blog.cloudflare.com/ja-jp/network-performance-agents-week/)

リクエスト処理レイヤーをFL2と呼ばれるRustベースのアーキテクチャに移行することで、Cloudflareは、世界のトップネットワークの60%につながるパフォーマンスを向上させました。当社は、実際のユーザーの測定値や接続解析を使用して、インターネット上で利用者の実際の体験を反映したデータを提供します。

![Lai Yi Ohlsen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DGMNXAW2CZQQAX92W97V.png&w=64&h=64&f=webp&fit=cover&position=center)

[Lai Yi Ohlsen](https://blog.cloudflare.com/ja-jp/author/lai-yi-ohlsen/)

2026年4月17日## [Flagshipのご紹介：AI時代に対応した機能フラグ](https://blog.cloudflare.com/ja-jp/flagship/)

Cloudflareの世界中のネットワーク上に構築された、ネイティブな機能フラグサービス「Flagship」を提供開始します。これにより、サードパーティプロバイダーの遅延を解消できます。また、KVやDurable Objectsを活用することで、1ミリ秒未満の高速なフラグ判定が可能になります。

![Rohan Mukherjee](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GNP12MJKQ0J7WAPF316S.webp&w=64&h=64&f=webp&fit=cover&position=center)![Abhishek Kankani](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FNB9JVR6RAPTZN4YR8XM.png&w=64&h=64&f=webp&fit=cover&position=center)

[Rohan Mukherjee](https://blog.cloudflare.com/ja-jp/author/rohan-mukherjee/)、[Abhishek Kankani](https://blog.cloudflare.com/ja-jp/author/abhishek-kankani/)

2026年3月23日## [Cloudflareの第13世代サーバーのローンチ：キャッシュとコアを交換して、2倍のエッジコンピューティングパフォーマンスを実現](https://blog.cloudflare.com/ja-jp/gen13-launch/)

Cloudflareの第13世代サーバーは、キャッシュとコアのバランスを再考することで、コンピューティングスループットを2倍にしました。高コア数のAMD EPYC™ Turin CPUに移行し、大規模なL3キャッシュを犠牲にして計算密度を高めました。新しいRustベースのFL2スタックを実行することで、遅延のペナルティを完全に軽減し、パフォーマンスを2倍にしました。

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jesse Brandeburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4807Z4GQMH91EPHZ1WRAGR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/ja-jp/author/syona/)、[JQ Lau](https://blog.cloudflare.com/ja-jp/author/jq/)、[Jesse Brandeburg](https://blog.cloudflare.com/ja-jp/author/jesse-brandeburg/)

2026年2月27日## [JavaScript用のより優れたStream APIに値する](https://blog.cloudflare.com/ja-jp/a-better-web-streams-api/)

Web Streams APIはJavaScriptランタイムでユビキタスになりましたが、これは時代遅れです。最新のストリーミングAPIは次のようになります（あるべきか？）は以下のようなものです。

![James M Snell](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47K5PBRD0MV43BH5TR121F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[James M Snell](https://blog.cloudflare.com/ja-jp/author/jasnell/)

2026年2月24日## [CloudflareがAIを活用してNext.jsを1週間で再構築した方法](https://blog.cloudflare.com/ja-jp/vinext/)

あるエンジニアは、AIを使用してVite上でNext.jsを1週間で再構築しました。vinextは、最高4倍速く構築し、57%小さいバンドルを生成し、単一のコマンドでCloudflare Workersにデプロイできます。

![Steve Faulkner](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47EEQ3VXY2MHT2H3PH52N8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Steve Faulkner](https://blog.cloudflare.com/ja-jp/author/steve-faulkner/)

2026年2月3日## [R2 Local Uploadsでグローバルアップロードのパフォーマンスを向上](https://blog.cloudflare.com/ja-jp/r2-local-uploads/)

R2へのローカルアップロードは、アップロードのリクエスト時間を最大75%短縮します。オブジェクトデータを近くのロケーションに書き込み、非同期にバケットにコピーします。データはすぐに利用可能です。 

![Frank Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45M7GJAFCCK19BX1XRJMG6.webp&w=64&h=64&f=webp&fit=cover&position=center)![Rahul Suresh](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BG5QN16EADBCQVAZZMWT.webp&w=64&h=64&f=webp&fit=cover&position=center)![Anni Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4618C573MJFB0RNKW6K68R.png&w=64&h=64&f=webp&fit=cover&position=center)

[Frank Chen](https://blog.cloudflare.com/ja-jp/author/frank-chen/)、[Rahul Suresh](https://blog.cloudflare.com/ja-jp/author/rahul-suresh/)、[Anni Wang](https://blog.cloudflare.com/ja-jp/author/anni/)

2025年10月21日## [BPF LPMのパフォーマンスと最適化を深掘り](https://blog.cloudflare.com/ja-jp/a-deep-dive-into-bpf-lpm-trie-performance-and-optimization/)

この記事では、IPマッチングに使用される重要なデータ構造であるBPF LPM試行のパフォーマンスについて説明します。 

![Matt Fleming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469GS9NZP4VYY003HA8XEA.webp&w=64&h=64&f=webp&fit=cover&position=center)![Jesper Brouer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW499RS2WW80VBYFGEW0TADD.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Fleming](https://blog.cloudflare.com/ja-jp/author/matt-fleming/)、[Jesper Brouer](https://blog.cloudflare.com/ja-jp/author/jesper-brouer/)

2025年9月29日## [より良いインターネットの構築を支援して15年：バースデーウィーク2025を振り返る](https://blog.cloudflare.com/ja-jp/birthday-week-2025-wrap-up/)

Rustを使ったコアシステム、ポスト量子アップグレード、学生向けの開発者プラットフォームアクセス、PlanetScaleとの統合、オープンソースパートナーシップ、そして史上最大のインターンシッププログラム（2026年に1111名のインターンを採用）。

![Nikita Cano](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AJSY9DYK5N26JP1Q24B7.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Korinne Alpers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47JYW3RAS2PS81KW2DNQWC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nikita Cano](https://blog.cloudflare.com/ja-jp/author/nikita/)、[Korinne Alpers](https://blog.cloudflare.com/ja-jp/author/korinne-alpers/)

2025年9月17日## [RUMダイアリー：Web Analyticsをデフォルトで有効化](https://blog.cloudflare.com/ja-jp/the-rum-diaries-enabling-web-analytics-by-default/)

2025年10月15日、Cloudflareはすべての無料ドメインでWeb Analyticsを有効にします。これにより、お客様は個人データを収集することなく、世界中のサイトのパフォーマンスをリアルタイムで把握できます。

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Tim Kadlec](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4508R0MVBXV7ZRDA6TK2C2.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/ja-jp/author/alex/)、[Tim Kadlec](https://blog.cloudflare.com/ja-jp/author/tim-kadlec/)

2025年8月5日## [プライバシープロキシで、遅延を40ミリ秒から1ミリ秒未満に低減](https://blog.cloudflare.com/ja-jp/reducing-double-spend-latency-from-40-ms-to-less-than-1-ms-on-privacy-proxy/)

「二重支出」チェックで40ミリ秒の遅延を修正し、プライバシープロキシサービスを大幅に高速化しました。

![Ben Yang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495TVKCM4J39JXG32VTCNG.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ben Yang](https://blog.cloudflare.com/ja-jp/author/ben-yang/)

2025年7月23日## [Jetflowの構築：Cloudflareにおける柔軟で高性能なデータパイプラインのフレームワーク](https://blog.cloudflare.com/ja-jp/building-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare/)

大規模なデータ取り込みの課題に直面して、CloudflareのBusiness IntelligenceチームはJetflowと呼ばれる新しいフレームワークを構築しました。

![Harry Hough](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47C0JMBM7Y7F2GNX2R8X3Q.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Rebecca Walton-Jones](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47P62GPSPWQJMX49XBJ9PK.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andy Fan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WD6HZHWZDZ6D51EB2YHJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Ricardo Margalhau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4692VQ40ERSW2HS1VWGJ06.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Uday Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45ZJ46DGX82MAJPNK0SWE0.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Harry Hough](https://blog.cloudflare.com/ja-jp/author/harry-hough/)、[Rebecca Walton-Jones](https://blog.cloudflare.com/ja-jp/author/rebecca-walton-jones/)、[Andy Fan](https://blog.cloudflare.com/ja-jp/author/andy-fan/)、[Ricardo Margalhau](https://blog.cloudflare.com/ja-jp/author/ricardo-margalhau/)、[Uday Sharma](https://blog.cloudflare.com/ja-jp/author/uday-sharma/)

2025年4月1日## [「すべてのユーザーがパージを利用できます！」—すべてのお客様が、すべてのパージ方法を利用できるようになりました](https://blog.cloudflare.com/ja-jp/instant-purge-for-all/)

業界最速のパージに続き、すべてのCloudflareプランでインスタントパージのクォータを引き上げました。 

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Connor Harwood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PA3429BFXAR99YP0Z2ZX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Zaidoon Abd Al Hadi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VAC8T0NPDPFZ06GAZW3H.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/ja-jp/author/alex/)、[Connor Harwood](https://blog.cloudflare.com/ja-jp/author/connor-harwood/)、[Zaidoon Abd Al Hadi](https://blog.cloudflare.com/ja-jp/author/zaidoon/)

2024年10月31日## [BaselimeをAWSからCloudflareへ移行：よりシンプルなアーキテクチャでより優れたパフォーマンスを実現し、クラウドコストを80%以上削減](https://blog.cloudflare.com/ja-jp/80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare/)

CloudflareはBaselimeを買収後、BaselimeをAWSからCloudflare開発者プラットフォームへと移行し、その過程でクエリー時間を改善し、データ取り込みを簡素化し、現在ではコストを削減しながら、はるかに多くのイベントを処理できるようになりました。この記事では、Cloudflareのネットワーク上で最新の高性能可観測性プラットフォームを構築した方法をご紹介します。 

![Boris Tane](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4776DVTF41B4B1HEER22V8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Boris Tane](https://blog.cloudflare.com/ja-jp/author/boris-tane/)

2024年9月30日## [バースデーウィークの総まとめ](https://blog.cloudflare.com/ja-jp/birthday-week-2024-wrap-up/)

2024年のバースデーウィーク中に行ったすべての大型発表を要約します。

![Kelly May Johnston](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46WM5TMV3Y8S91FG1PQJ01.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Brendan Irvine-Broque](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H9641F9RZN2BA8BPX7HK.JPG&w=64&h=64&f=webp&fit=cover&position=center)

[Kelly May Johnston](https://blog.cloudflare.com/ja-jp/author/kelly-may-johnston/)、[Brendan Irvine-Broque](https://blog.cloudflare.com/ja-jp/author/brendan-irvine-broque/)

2024年2月28日## [Pingoraのオープンソース化：プログラマブルなネットワークサービスを構築するためのRustフレームワーク](https://blog.cloudflare.com/ja-jp/pingora-open-source/)

プログラマブルでメモリ安全性の高いネットワークサービスを構築するためのフレームワーク、Pingoraがオープンソース化されました。今すぐPingoraの使用を開始しましょう

![Yuchen Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CEA1K0ZA59ZK5J7QNRVF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Edward Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW461JESP3W5FAGRMPYV23AR.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yuchen Wu](https://blog.cloudflare.com/ja-jp/author/yuchen/)、[Edward Wang](https://blog.cloudflare.com/ja-jp/author/edward-h-wang/)、[Andrew Hauck](https://blog.cloudflare.com/ja-jp/author/andrew-hauck/)

2023年10月24日## [Cache Rulesの一般提供開始：キャッシュの詳細かつ精密な制御](https://blog.cloudflare.com/ja-jp/cache-rules-go-ga/)

本日、Cache Rulesと他のいくつかのRules製品の同時一般公開（GA）をお知らせできることを嬉しく思います。しかし、それだけではありません。Cache Rulesの新しい設定オプションも追加されました

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/ja-jp/author/alex/)

2023年6月23日## [Cloudflare Radarのインターネット品質ページのご紹介](https://blog.cloudflare.com/ja-jp/introducing-radar-internet-quality-page/)

Cloudflare Radarに搭載された新しいパフォーマンスページは、ベンチマークテストのデータとspeed.cloudflare.comのテスト結果をもとにした、インターネット接続のパフォーマンス (帯域幅) と品質 (レイテンシ、ジッタ) について、国レベルとネットワーク (自律システム) レベルの両方についての長期的なインサイトを提供します

![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Carlos Rodrigues](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P9VMTDZ2R4BDYEPSPMX4.png&w=64&h=64&f=webp&fit=cover&position=center)

[David Belson](https://blog.cloudflare.com/ja-jp/author/david-belson/)、[Carlos Rodrigues](https://blog.cloudflare.com/ja-jp/author/carlos-rodrigues/)

もっと読み込む
