---
url: https://blog.cloudflare.com/zh-tw/tag/clickhouse/
title: \u6a19\u7c64\u70ba\u300cClickHouse\u300d\u7684\u6587\u7ae0 \u2014 Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:09:40.250869+00:00
---

# 標籤為「ClickHouse」的文章 — Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/tag/clickhouse/

標籤

# ClickHouse

[訂閱 ClickHouse RSS 摘要](https://blog.cloudflare.com/zh-tw/tag/clickhouse/rss)

2026年5月14日## [我們的帳單處理管道突然變得非常緩慢。罪魁禍首是 ClickHouse 內部一個隱藏的瓶頸](https://blog.cloudflare.com/zh-tw/clickhouse-query-plan-contention/)

當我們 PB 級 ClickHouse 叢集的一次分區調整，導致關鍵帳單作業陷入停滯，而標準監控指標卻毫無異常時，我們不得不深入系統內部尋找答案。本文將回顧我們如何發現 ClickHouse 查詢規劃器中嚴重的鎖競爭問題，並透過提交上游修補程式來修復該問題的完整歷程。

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/zh-tw/author/james-morrison/)和[Christian Endres](https://blog.cloudflare.com/zh-tw/author/christian-endres/)
