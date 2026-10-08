---
url: https://blog.cloudflare.com/zh-tw/tag/open-source/
title: \u6a19\u7c64\u70ba\u300c\u958b\u6e90\u8cc7\u6e90\u300d\u7684\u6587\u7ae0 \u2014 Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:09:55.589316+00:00
---

# 標籤為「開源資源」的文章 — Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/tag/open-source/

標籤

# 開源資源

[訂閱 開源資源 RSS 摘要](https://blog.cloudflare.com/zh-tw/tag/open-source/rss)

2026年8月10日## [Cloudflare OS：適用於智慧體、應用程式和工作的開放平台](https://blog.cloudflare.com/zh-tw/cloudflare-os/)

Cloudflare OS 是一個開放原始碼平台，讓您公司中的每個人都能建置應用程式、自動化工作，以及安全地存取內部系統，其設計充分考量您的組織的知識體系及運作方式

![Phillip Jones](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CA63Q819PPAR7M8DTNQ3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Dan Carter](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BJJATPEKV6ZZ0N22HHVH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Phillip Jones](https://blog.cloudflare.com/zh-tw/author/phillip/)和[Dan Carter](https://blog.cloudflare.com/zh-tw/author/dan-carter/)

2026年5月14日## [我們的帳單處理管道突然變得非常緩慢。罪魁禍首是 ClickHouse 內部一個隱藏的瓶頸](https://blog.cloudflare.com/zh-tw/clickhouse-query-plan-contention/)

當我們 PB 級 ClickHouse 叢集的一次分區調整，導致關鍵帳單作業陷入停滯，而標準監控指標卻毫無異常時，我們不得不深入系統內部尋找答案。本文將回顧我們如何發現 ClickHouse 查詢規劃器中嚴重的鎖競爭問題，並透過提交上游修補程式來修復該問題的完整歷程。

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/zh-tw/author/james-morrison/)和[Christian Endres](https://blog.cloudflare.com/zh-tw/author/christian-endres/)

2026年4月22日## [讓 Rust Workers 更加可靠：wasm‑bindgen 中的 panic 與 abort 復原](https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/)

過去，Rust Workers 中的 panic（恐慌）是致命的，會損毀整個執行個體。透過與上游的 wasm‑bindgen 專案合作，Rust Workers 現在支援了具韌性的關鍵錯誤復原，包括使用 WebAssembly 異常處理 (WebAssembly Exception Handling) 進行 panic unwind（恐慌展開）。

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/zh-tw/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/zh-tw/author/hood/)和[Logan Gatlin](https://blog.cloudflare.com/zh-tw/author/logan-gatlin/)

2026年2月20日## [Code Mode：用 1000 個詞元為智慧體開放整個 API](https://blog.cloudflare.com/zh-tw/code-mode-mcp/)

Cloudflare API 有超過 2500 個端點。如果將每一個端點都公開為一個 MCP 工具，將會消耗超過 200 萬個詞元。透過 Code Mode，我們將所有功能濃縮成兩個工具，只需大約 1000 個詞元的上下文。

![Matt Carey](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BHQSGCBKVGAAVQVS4V3E.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Carey](https://blog.cloudflare.com/zh-tw/author/matt-carey/)

2024年9月27日## [透過 Alexandria 專案擴展我們對開放原始碼專案的支援](https://blog.cloudflare.com/zh-tw/expanding-our-support-for-oss-projects-with-project-alexandria/)

在 Cloudflare，我們相信開放原始碼的力量。我們推出擴展的開放原始碼計畫——Alexandria 專案，協助開放原始碼專案擁有一個永續發展且可擴展的未來，並為它們提供蓬勃發展所需的工具和保護。

![Veronica Marin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45XPDEXDY26TEF5DY1BNX6.png&w=64&h=64&f=webp&fit=cover&position=center)![Gabby Shires](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H80P0HTZPWSHGB0Q9S7K.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Veronica Marin](https://blog.cloudflare.com/zh-tw/author/veronica-marin/)和[Gabby Shires](https://blog.cloudflare.com/zh-tw/author/gabby-shires/)

2024年5月22日## [AI Gateway 已正式上市：用於管理和擴展生成式 AI 工作負載的統一介面](https://blog.cloudflare.com/zh-tw/ai-gateway-is-generally-available/)

AI Gateway 是一個 AI 操作平台，可為您的 AI 應用程式提供速度、可靠性和可觀察性。只需一行程式碼，您就可以解鎖強大的功能，包括限速、自訂快取、即時記錄和跨多個提供者的聚合分析

![Kathy Liao](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45CCSZ168NDHJPTF31M9JS.png&w=64&h=64&f=webp&fit=cover&position=center)![Michelle Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44R95PPSQQ82Z92P51M550.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Phil Wittig](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BX0J00059NX1R4GGRT1.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Kathy Liao](https://blog.cloudflare.com/zh-tw/author/kathy/)、[Michelle Chen](https://blog.cloudflare.com/zh-tw/author/michelle/)和[Phil Wittig](https://blog.cloudflare.com/zh-tw/author/phil/)

2024年2月28日## [Pingora 開放原始碼：我們用於構建可程式設計網路服務的 Rust 框架](https://blog.cloudflare.com/zh-tw/pingora-open-source/)

我們用於構建可程式設計和記憶體安全網路服務的框架 Pingora 現已開放原始碼。立即開始使用 Pingora

![Yuchen Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CEA1K0ZA59ZK5J7QNRVF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Edward Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW461JESP3W5FAGRMPYV23AR.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yuchen Wu](https://blog.cloudflare.com/zh-tw/author/yuchen/)、[Edward Wang](https://blog.cloudflare.com/zh-tw/author/edward-h-wang/)和[Andrew Hauck](https://blog.cloudflare.com/zh-tw/author/andrew-hauck/)

2024年2月6日## [向 Workers AI 目錄新增新的 LLM、文字分類和程式碼產生模型](https://blog.cloudflare.com/zh-tw/february-2024-workersai-catalog-update/)

現在，Workers AI 變得更大更好，擁有 8 個新模型和改進的模型效能

![Michelle Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44R95PPSQQ82Z92P51M550.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Logan Grasby](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW477NKW4WMXFM6419VZGJXK.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michelle Chen](https://blog.cloudflare.com/zh-tw/author/michelle/)和[Logan Grasby](https://blog.cloudflare.com/zh-tw/author/logan/)
