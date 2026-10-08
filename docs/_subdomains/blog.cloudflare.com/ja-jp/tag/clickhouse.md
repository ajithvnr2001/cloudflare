---
url: https://blog.cloudflare.com/ja-jp/tag/clickhouse/
title: \"ClickHouse\" \u30bf\u30b0\u306e\u6295\u7a3f \u2014 Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:18:23.277913+00:00
---

# "ClickHouse" タグの投稿 — Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/tag/clickhouse/

TAG

# ClickHouse

[ClickHouse RSSフィードを購読する](https://blog.cloudflare.com/ja-jp/tag/clickhouse/rss)

2026年5月14日## [請求パイプラインが突然遅くなったのです。原因はClickHouseの隠れたボトルネックでした](https://blog.cloudflare.com/ja-jp/clickhouse-query-plan-contention/)

ペタバイト規模のClickHouseクラスターのパーティショニング変更によって重要な請求ジョブが停止したとき、標準的なメトリクスは明らかなエラーは示されませんでした。この記事では、当社がClickHouseのクエリプランナーで深刻なロックコンテンツを特定し、それを修正するためのアップストリームパッチをどのように構築したかを探ります。

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/ja-jp/author/james-morrison/)、[Christian Endres](https://blog.cloudflare.com/ja-jp/author/christian-endres/)
