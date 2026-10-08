---
url: https://blog.cloudflare.com/zh-tw/tag/rust/
title: \u6a19\u7c64\u70ba\u300cRust\u300d\u7684\u6587\u7ae0 \u2014 Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:09:59.887655+00:00
---

# 標籤為「Rust」的文章 — Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/tag/rust/

標籤

# Rust

[訂閱 Rust RSS 摘要](https://blog.cloudflare.com/zh-tw/tag/rust/rss)

2026年4月22日## [讓 Rust Workers 更加可靠：wasm‑bindgen 中的 panic 與 abort 復原](https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/)

過去，Rust Workers 中的 panic（恐慌）是致命的，會損毀整個執行個體。透過與上游的 wasm‑bindgen 專案合作，Rust Workers 現在支援了具韌性的關鍵錯誤復原，包括使用 WebAssembly 異常處理 (WebAssembly Exception Handling) 進行 panic unwind（恐慌展開）。

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/zh-tw/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/zh-tw/author/hood/)和[Logan Gatlin](https://blog.cloudflare.com/zh-tw/author/logan-gatlin/)

2026年1月27日## [建置無伺服器的後量子 Matrix Homeserver](https://blog.cloudflare.com/zh-tw/serverless-matrix-homeserver-workers/)

作為概念驗證，我們成功將 Matrix Homeserver 移植至 Cloudflare Workers 平台，在邊緣實現了自帶後量子加密的即時通訊系統。

![Nick Kuntz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48M0V4GPMAV2E12FH7VT98.png&w=64&h=64&f=webp&fit=cover&position=center)

[Nick Kuntz](https://blog.cloudflare.com/zh-tw/author/nick-kuntz/)

2025年12月18日## [宣佈 R2 SQL 開始支援 GROUP BY、SUM 和其他彙總查詢](https://blog.cloudflare.com/zh-tw/r2-sql-aggregations/)

Cloudflare 的分散式查詢引擎 R2 SQL 現在支援彙總功能。瞭解我們如何建立分散式的 GROUP BY 執行機制，利用分散-彙總與洗牌策略，直接在您的 R2 Data Catalog 上執行分析。

![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Marc Selwan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455H274J0ZYJ6K4KHKJT25.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jérôme Schneider](https://blog.cloudflare.com/zh-tw/author/jerome/)、[Nikita Lapkov](https://blog.cloudflare.com/zh-tw/author/nikita-lapkov/)和[Marc Selwan](https://blog.cloudflare.com/zh-tw/author/marc-selwan/)

2024年2月28日## [Pingora 開放原始碼：我們用於構建可程式設計網路服務的 Rust 框架](https://blog.cloudflare.com/zh-tw/pingora-open-source/)

我們用於構建可程式設計和記憶體安全網路服務的框架 Pingora 現已開放原始碼。立即開始使用 Pingora

![Yuchen Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CEA1K0ZA59ZK5J7QNRVF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Edward Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW461JESP3W5FAGRMPYV23AR.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yuchen Wu](https://blog.cloudflare.com/zh-tw/author/yuchen/)、[Edward Wang](https://blog.cloudflare.com/zh-tw/author/edward-h-wang/)和[Andrew Hauck](https://blog.cloudflare.com/zh-tw/author/andrew-hauck/)

2022年9月14日## [如何構建 Pingora 以將 Cloudflare 連線至網際網路代理](https://blog.cloudflare.com/zh-tw/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/)

今天，我們滿懷欣喜之情來談論 Pingora，這是我們使用 Rust 在內部構建的全新 HTTP 代理程式 ，其平均每天可處理超過 1 萬億個請求

![Yuchen Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CEA1K0ZA59ZK5J7QNRVF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yuchen Wu](https://blog.cloudflare.com/zh-tw/author/yuchen/)和[Andrew Hauck](https://blog.cloudflare.com/zh-tw/author/andrew-hauck/)
