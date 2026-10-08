---
url: https://blog.cloudflare.com/zh-tw/tag/engineering/
title: \u6a19\u7c64\u70ba\u300c\u5de5\u7a0b\u8a2d\u8a08\u300d\u7684\u6587\u7ae0 \u2014 Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:09:48.437431+00:00
---

# 標籤為「工程設計」的文章 — Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/tag/engineering/

標籤

# 工程設計

[訂閱 工程設計 RSS 摘要](https://blog.cloudflare.com/zh-tw/tag/engineering/rss)

2026年8月6日## [推出 Billable Usage API：為 Cloudflare 提供程式化的成本可視性](https://blog.cloudflare.com/zh-tw/billable-usage-api/)

Cloudflare 為帳戶推出全新 Billable Usage API，讓開發人員和 FinOps 團隊能透過單一端點程式化地查看所有自助產品的成本和使用情況。該 API 圍繞 FOCUS 規範建構，可與雲端堆疊的其餘部分一起無縫追蹤支出。

![Ryan Noel](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KZ1X993V2NQBSHZCEDTSYH99.webp&w=64&h=64&f=webp&fit=cover&position=center)![Zunayed Ali](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KZ1X7VHNGDVK1WPDK7WS7DWR.webp&w=64&h=64&f=webp&fit=cover&position=center)![Filipa Nóbrega](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KZ1X62NSE3TRWSABF7J6JR84.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Ryan Noel](https://blog.cloudflare.com/zh-tw/author/ryan-noel/)、[Zunayed Ali](https://blog.cloudflare.com/zh-tw/author/zunayed-ali/)和[Filipa Nóbrega](https://blog.cloudflare.com/zh-tw/author/filipa-nobrega/)

2026年5月18日## [Project Glasswing：Mythos 向我們展示了什麼](https://blog.cloudflare.com/zh-tw/cyber-frontier-models/)

近幾週，我們將 Mythos 及其他專注於安全的 LLM 指向了我們基礎架構關鍵部分的現行程式碼。我們分享了觀察到的現象、模型的優勢與不足之處，以及在這些技術能夠規模化應用之前，需要進行哪些相關工作。

![Grant Bourzikas](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SJJRBDYVMHZKVGKTMJ08.png&w=64&h=64&f=webp&fit=cover&position=center)

[Grant Bourzikas](https://blog.cloudflare.com/zh-tw/author/grant/)

2026年5月14日## [我們的帳單處理管道突然變得非常緩慢。罪魁禍首是 ClickHouse 內部一個隱藏的瓶頸](https://blog.cloudflare.com/zh-tw/clickhouse-query-plan-contention/)

當我們 PB 級 ClickHouse 叢集的一次分區調整，導致關鍵帳單作業陷入停滯，而標準監控指標卻毫無異常時，我們不得不深入系統內部尋找答案。本文將回顧我們如何發現 ClickHouse 查詢規劃器中嚴重的鎖競爭問題，並透過提交上游修補程式來修復該問題的完整歷程。

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/zh-tw/author/james-morrison/)和[Christian Endres](https://blog.cloudflare.com/zh-tw/author/christian-endres/)

2026年4月22日## [讓 Rust Workers 更加可靠：wasm‑bindgen 中的 panic 與 abort 復原](https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/)

過去，Rust Workers 中的 panic（恐慌）是致命的，會損毀整個執行個體。透過與上游的 wasm‑bindgen 專案合作，Rust Workers 現在支援了具韌性的關鍵錯誤復原，包括使用 WebAssembly 異常處理 (WebAssembly Exception Handling) 進行 panic unwind（恐慌展開）。

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/zh-tw/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/zh-tw/author/hood/)和[Logan Gatlin](https://blog.cloudflare.com/zh-tw/author/logan-gatlin/)

2026年2月27日## [網際網路上最常見的 UI？重新設計 Turnstile 與驗證頁面](https://blog.cloudflare.com/zh-tw/the-most-seen-ui-on-the-internet-redesigning-turnstile-and-challenge-pages/)

我們每天處理 76 億次驗證挑戰。下面介紹了我們如何運用研究、AAA 無障礙標準以及統一的架構，來重新設計這個網際網路上最常見的使用者介面。

![Leo Bacevicius](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW493S0ZBT0BV1Y08GV76K24.png&w=64&h=64&f=webp&fit=cover&position=center)![Ana Foppa](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KTZRPFJSPXK2FK8H5CSH.png&w=64&h=64&f=webp&fit=cover&position=center)![Marina Elmore](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW477HVM8X1SKDG8ADKQJ9T3.png&w=64&h=64&f=webp&fit=cover&position=center)

[Leo Bacevicius](https://blog.cloudflare.com/zh-tw/author/leo-bacevicius/)、[Ana Foppa](https://blog.cloudflare.com/zh-tw/author/ana-foppa/)和[Marina Elmore](https://blog.cloudflare.com/zh-tw/author/marina-elmore/)
