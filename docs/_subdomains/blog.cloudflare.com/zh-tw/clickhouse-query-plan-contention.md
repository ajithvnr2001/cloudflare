---
url: https://blog.cloudflare.com/zh-tw/clickhouse-query-plan-contention/
title: \u6211\u5011\u7684\u5e33\u55ae\u8655\u7406\u7ba1\u9053\u7a81\u7136\u8b8a\u5f97\u975e\u5e38\u7de9\u6162\u3002\u7f6a\u9b41\u798d\u9996\u662f ClickHouse \u5167\u90e8\u4e00\u500b\u96b1\u85cf\u7684\u74f6\u9838 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:43:02.774992+00:00
---

# 我們的帳單處理管道突然變得非常緩慢。罪魁禍首是 ClickHouse 內部一個隱藏的瓶頸 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/clickhouse-query-plan-contention/

[部落格](https://blog.cloudflare.com/zh-tw/)

[ClickHouse](https://blog.cloudflare.com/zh-tw/tag/clickhouse/)[工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)[效能](https://blog.cloudflare.com/zh-tw/tag/performance/)+2顯示另外 2 個標籤

5 標籤顯示 5 個標籤

  * 文章標籤
  * [ClickHouse](https://blog.cloudflare.com/zh-tw/tag/clickhouse/)[工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)[效能](https://blog.cloudflare.com/zh-tw/tag/performance/)[資料庫](https://blog.cloudflare.com/zh-tw/tag/database/)[開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)
  * 所有標籤
  * 相符標籤
  * 找不到相符的標籤
  * [1.1.1.1](https://blog.cloudflare.com/zh-tw/tag/1-1-1-1/)
  * [Access](https://blog.cloudflare.com/zh-tw/tag/access/)
  * [可存取性](https://blog.cloudflare.com/zh-tw/tag/accessibility/)
  * [併購](https://blog.cloudflare.com/zh-tw/tag/acquisitions/)
  * [進階 DDoS](https://blog.cloudflare.com/zh-tw/tag/advanced-ddos/)
  * [智慧體就緒程度](https://blog.cloudflare.com/zh-tw/tag/agent-readiness/)
  * [代理程式](https://blog.cloudflare.com/zh-tw/tag/agents/)
  * [Agents Week](https://blog.cloudflare.com/zh-tw/tag/agents-week/)
  * [AI](https://blog.cloudflare.com/zh-tw/tag/ai/)
  * [AI 機器人](https://blog.cloudflare.com/zh-tw/tag/ai-bots/)
  * [AI Gateway](https://blog.cloudflare.com/zh-tw/tag/ai-gateway/)
  * [AI 搜尋](https://blog.cloudflare.com/zh-tw/tag/ai-search/)
  * [AI Week](https://blog.cloudflare.com/zh-tw/tag/ai-week/)
  * [AI-SPM](https://blog.cloudflare.com/zh-tw/tag/ai-spm/)
  * [Analytics](https://blog.cloudflare.com/zh-tw/tag/analytics/)
  * [API](https://blog.cloudflare.com/zh-tw/tag/api/)
  * [API 安全](https://blog.cloudflare.com/zh-tw/tag/api-security/)
  * [應用程式安全性](https://blog.cloudflare.com/zh-tw/tag/application-security/)
  * [應用程式服務](https://blog.cloudflare.com/zh-tw/tag/application-services/)
  * [攻擊](https://blog.cloudflare.com/zh-tw/tag/attacks/)
  * [稽核記錄](https://blog.cloudflare.com/zh-tw/tag/audit-logs/)
  * [自動化](https://blog.cloudflare.com/zh-tw/tag/automation/)
  * [AWS](https://blog.cloudflare.com/zh-tw/tag/aws/)
  * [測試版](https://blog.cloudflare.com/zh-tw/tag/beta/)
  * [BGP](https://blog.cloudflare.com/zh-tw/tag/bgp/)
  * [生日週](https://blog.cloudflare.com/zh-tw/tag/birthday-week/)
  * [機器人管理](https://blog.cloudflare.com/zh-tw/tag/bot-management/)
  * [機器人](https://blog.cloudflare.com/zh-tw/tag/bots/)
  * [Browser Rendering](https://blog.cloudflare.com/zh-tw/tag/browser-rendering/)
  * [Browser Run](https://blog.cloudflare.com/zh-tw/tag/browser-run/)
  * [漏洞懸賞](https://blog.cloudflare.com/zh-tw/tag/bug-bounty/)
  * [快取](https://blog.cloudflare.com/zh-tw/tag/cache/)
  * [快取清除](https://blog.cloudflare.com/zh-tw/tag/cache-purge/)
  * [CASB](https://blog.cloudflare.com/zh-tw/tag/casb/)
  * [CDN](https://blog.cloudflare.com/zh-tw/tag/cdn/)
  * [驗證頁面](https://blog.cloudflare.com/zh-tw/tag/challenge-page/)
  * [聖誕節](https://blog.cloudflare.com/zh-tw/tag/christmas/)
  * [Chrome](https://blog.cloudflare.com/zh-tw/tag/chrome/)
  * [CIO Week](https://blog.cloudflare.com/zh-tw/tag/cio-week/)
  * [ClickHouse](https://blog.cloudflare.com/zh-tw/tag/clickhouse/)
  * [無用戶端](https://blog.cloudflare.com/zh-tw/tag/clientless/)
  * [Cloud Email Security](https://blog.cloudflare.com/zh-tw/tag/cloud-email-security/)
  * [Cloudflare Access](https://blog.cloudflare.com/zh-tw/tag/cloudflare-access/)
  * [Cloudflare Calls](https://blog.cloudflare.com/zh-tw/tag/cloudflare-calls/)
  * [Cloudflare for Startups](https://blog.cloudflare.com/zh-tw/tag/cloudflare-for-startups/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/zh-tw/tag/gateway/)
  * [Cloudflare Images](https://blog.cloudflare.com/zh-tw/tag/cloudflare-images/)
  * [Cloudflare 媒體平台](https://blog.cloudflare.com/zh-tw/tag/cloudflare-media-platform/)
  * [Cloudflare 網路](https://blog.cloudflare.com/zh-tw/tag/cloudflare-network/)
  * [Cloudflare One](https://blog.cloudflare.com/zh-tw/tag/cloudflare-one/)
  * [Cloudflare Pages](https://blog.cloudflare.com/zh-tw/tag/cloudflare-pages/)
  * [Cloudflare Queues](https://blog.cloudflare.com/zh-tw/tag/cloudflare-queues/)
  * [Cloudflare Tunnel](https://blog.cloudflare.com/zh-tw/tag/cloudflare-tunnel/)
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)
  * [Cloudflare Workers KV](https://blog.cloudflare.com/zh-tw/tag/cloudflare-workers-kv/)
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/zh-tw/tag/cloudflare-zero-trust/)
  * [Cloudforce One](https://blog.cloudflare.com/zh-tw/tag/cloudforce-one/)
  * [橙色警報](https://blog.cloudflare.com/zh-tw/tag/code-orange/)
  * [Coinbase](https://blog.cloudflare.com/zh-tw/tag/coinbase/)
  * [全球連通雲](https://blog.cloudflare.com/zh-tw/tag/connectivity-cloud/)
  * [消費者服務](https://blog.cloudflare.com/zh-tw/tag/consumer-services/)
  * [容器](https://blog.cloudflare.com/zh-tw/tag/containers/)
  * [內容獨立日](https://blog.cloudflare.com/zh-tw/tag/content-independence-day/)
  * [背景資訊](https://blog.cloudflare.com/zh-tw/tag/context/)
  * [爬蟲提示](https://blog.cloudflare.com/zh-tw/tag/crawler-hints/)
  * [密碼編譯](https://blog.cloudflare.com/zh-tw/tag/cryptography/)
  * [D1](https://blog.cloudflare.com/zh-tw/tag/d1/)
  * [儀表板](https://blog.cloudflare.com/zh-tw/tag/dashboard-tag/)
  * [資料](https://blog.cloudflare.com/zh-tw/tag/data/)
  * [資料庫](https://blog.cloudflare.com/zh-tw/tag/database/)
  * [DDoS](https://blog.cloudflare.com/zh-tw/tag/ddos/)
  * [DDoS 警示](https://blog.cloudflare.com/zh-tw/tag/ddos-alerts/)
  * [DDoS 報告](https://blog.cloudflare.com/zh-tw/tag/ddos-reports/)
  * [深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)
  * [設計](https://blog.cloudflare.com/zh-tw/tag/design/)
  * [開發人員文件](https://blog.cloudflare.com/zh-tw/tag/developer-documentation/)
  * [開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)
  * [Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)
  * [開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)
  * [開發人員儲存體](https://blog.cloudflare.com/zh-tw/tag/developers-storage/)
  * [DLP](https://blog.cloudflare.com/zh-tw/tag/dlp/)
  * [DNS](https://blog.cloudflare.com/zh-tw/tag/dns/)
  * [DNSSEC](https://blog.cloudflare.com/zh-tw/tag/dnssec/)
  * [Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)
  * [Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)
  * [邊緣運算](https://blog.cloudflare.com/zh-tw/tag/edge-computing/)
  * [電子郵件安全](https://blog.cloudflare.com/zh-tw/tag/email-security/)
  * [加密](https://blog.cloudflare.com/zh-tw/tag/encryption/)
  * [工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)
  * [Forrester](https://blog.cloudflare.com/zh-tw/tag/forrester/)
  * [創始人來信](https://blog.cloudflare.com/zh-tw/tag/founders-letter/)
  * [詐欺](https://blog.cloudflare.com/zh-tw/tag/fraud/)
  * [前端](https://blog.cloudflare.com/zh-tw/tag/front-end/)
  * [完整堆疊](https://blog.cloudflare.com/zh-tw/tag/full-stack/)
  * [正式推出](https://blog.cloudflare.com/zh-tw/tag/general-availability/)
  * [生成式 AI](https://blog.cloudflare.com/zh-tw/tag/generative-ai/)
  * [Github：](https://blog.cloudflare.com/zh-tw/tag/github/)
  * [Google Cloud](https://blog.cloudflare.com/zh-tw/tag/google-cloud/)
  * [HTTP3](https://blog.cloudflare.com/zh-tw/tag/http3/)
  * [Hyperdrive](https://blog.cloudflare.com/zh-tw/tag/hyperdrive/)
  * [身分](https://blog.cloudflare.com/zh-tw/tag/identity/)
  * [影像大小調整](https://blog.cloudflare.com/zh-tw/tag/image-resizing/)
  * [影像儲存](https://blog.cloudflare.com/zh-tw/tag/image-storage/)
  * [影響](https://blog.cloudflare.com/zh-tw/tag/impact/)
  * [事件回應](https://blog.cloudflare.com/zh-tw/tag/incident-response/)
  * [基礎架構](https://blog.cloudflare.com/zh-tw/tag/infrastructure/)
  * [Intel](https://blog.cloudflare.com/zh-tw/tag/intel/)
  * [網際網路品質](https://blog.cloudflare.com/zh-tw/tag/internet-quality/)
  * [網際網路關閉](https://blog.cloudflare.com/zh-tw/tag/internet-shutdown/)
  * [網際網路流量](https://blog.cloudflare.com/zh-tw/tag/internet-traffic/)
  * [網際網路趨勢](https://blog.cloudflare.com/zh-tw/tag/internet-trends/)
  * [IPsec VPN](https://blog.cloudflare.com/zh-tw/tag/ipsec/)
  * [IPv6](https://blog.cloudflare.com/zh-tw/tag/ipv6/)
  * [核心](https://blog.cloudflare.com/zh-tw/tag/kernel/)
  * [KeyTrap](https://blog.cloudflare.com/zh-tw/tag/keytrap/)
  * [LangChain](https://blog.cloudflare.com/zh-tw/tag/langchain/)
  * [Cloudflare 生活](https://blog.cloudflare.com/zh-tw/tag/life-at-cloudflare/)
  * [Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)
  * [LLM](https://blog.cloudflare.com/zh-tw/tag/llm/)
  * [MCP](https://blog.cloudflare.com/zh-tw/tag/mcp/)
  * [Microsoft Azure](https://blog.cloudflare.com/zh-tw/tag/microsoft-azure/)
  * [Mirai](https://blog.cloudflare.com/zh-tw/tag/mirai/)
  * [模型情境通訊協定，](https://blog.cloudflare.com/zh-tw/tag/model-context-protocol/)
  * [監控](https://blog.cloudflare.com/zh-tw/tag/monitoring/)
  * [MySQL](https://blog.cloudflare.com/zh-tw/tag/mysql/)
  * [網路](https://blog.cloudflare.com/zh-tw/tag/network/)
  * [網路服務](https://blog.cloudflare.com/zh-tw/tag/network-services/)
  * [新年](https://blog.cloudflare.com/zh-tw/tag/new-year/)
  * [OAuth](https://blog.cloudflare.com/zh-tw/tag/oauth/)
  * [開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)
  * [最佳化](https://blog.cloudflare.com/zh-tw/tag/optimization/)
  * [服務中斷](https://blog.cloudflare.com/zh-tw/tag/outage/)
  * [合作夥伴](https://blog.cloudflare.com/zh-tw/tag/partners/)
  * [對等互連](https://blog.cloudflare.com/zh-tw/tag/peering/)
  * [效能](https://blog.cloudflare.com/zh-tw/tag/performance/)
  * [網路釣魚](https://blog.cloudflare.com/zh-tw/tag/phishing/)
  * [政策與法律](https://blog.cloudflare.com/zh-tw/tag/policy/)
  * [事後檢討](https://blog.cloudflare.com/zh-tw/tag/post-mortem/)
  * [後量子](https://blog.cloudflare.com/zh-tw/tag/post-quantum/)
  * [隱私權](https://blog.cloudflare.com/zh-tw/tag/privacy/)
  * [產品設計](https://blog.cloudflare.com/zh-tw/tag/product-design/)
  * [產品新聞](https://blog.cloudflare.com/zh-tw/tag/product-news/)
  * [Galileo 專案](https://blog.cloudflare.com/zh-tw/tag/project-galileo/)
  * [Prometheus](https://blog.cloudflare.com/zh-tw/tag/prometheus/)
  * [Python](https://blog.cloudflare.com/zh-tw/tag/python/)
  * [Queues](https://blog.cloudflare.com/zh-tw/tag/queues/)
  * [R2](https://blog.cloudflare.com/zh-tw/tag/r2/)
  * [R2 Super Slurper](https://blog.cloudflare.com/zh-tw/tag/r2-super-slurper/)
  * [Radar](https://blog.cloudflare.com/zh-tw/tag/cloudflare-radar/)
  * [勒索攻擊](https://blog.cloudflare.com/zh-tw/tag/ransom-attacks/)
  * [即時](https://blog.cloudflare.com/zh-tw/tag/real-time/)
  * [可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)
  * [研究](https://blog.cloudflare.com/zh-tw/tag/research/)
  * [風險管理](https://blog.cloudflare.com/zh-tw/tag/risk-management/)
  * [路由](https://blog.cloudflare.com/zh-tw/tag/routing/)
  * [路由安全性](https://blog.cloudflare.com/zh-tw/tag/routing-security/)
  * [RPKI](https://blog.cloudflare.com/zh-tw/tag/rpki/)
  * [Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)
  * [Rust Workers](https://blog.cloudflare.com/zh-tw/tag/rust-workers/)
  * [SaaS 安全性](https://blog.cloudflare.com/zh-tw/tag/saas-security/)
  * [沙箱](https://blog.cloudflare.com/zh-tw/tag/sandbox/)
  * [SASE](https://blog.cloudflare.com/zh-tw/tag/sase/)
  * [SDK](https://blog.cloudflare.com/zh-tw/tag/sdk/)
  * [安全 Web 閘道 (SWG)](https://blog.cloudflare.com/zh-tw/tag/secure-web-gateway/)
  * [安全性](https://blog.cloudflare.com/zh-tw/tag/security/)
  * [網路安全中心](https://blog.cloudflare.com/zh-tw/tag/security-center/)
  * [安全狀態管理](https://blog.cloudflare.com/zh-tw/tag/security-posture-management/)
  * [Security Week](https://blog.cloudflare.com/zh-tw/tag/security-week/)
  * [無伺服器](https://blog.cloudflare.com/zh-tw/tag/serverless/)
  * [速度](https://blog.cloudflare.com/zh-tw/tag/speed/)
  * [速度與可靠性](https://blog.cloudflare.com/zh-tw/tag/speed-and-reliability/)
  * [SQL](https://blog.cloudflare.com/zh-tw/tag/sql/)
  * [儲存](https://blog.cloudflare.com/zh-tw/tag/storage/)
  * [團隊](https://blog.cloudflare.com/zh-tw/tag/team/)
  * [威脅情報](https://blog.cloudflare.com/zh-tw/tag/threat-intelligence/)
  * [威脅行動](https://blog.cloudflare.com/zh-tw/tag/threat-operations/)
  * [威脅](https://blog.cloudflare.com/zh-tw/tag/threats/)
  * [TLS](https://blog.cloudflare.com/zh-tw/tag/tls/)
  * [流量](https://blog.cloudflare.com/zh-tw/tag/traffic/)
  * [透明度](https://blog.cloudflare.com/zh-tw/tag/transparency/)
  * [趨勢](https://blog.cloudflare.com/zh-tw/tag/trends/)
  * [TURN 伺服器](https://blog.cloudflare.com/zh-tw/tag/turn-server/)
  * [Turnstile](https://blog.cloudflare.com/zh-tw/tag/turnstile/)
  * [使用者研究](https://blog.cloudflare.com/zh-tw/tag/user-research/)
  * [漏洞](https://blog.cloudflare.com/zh-tw/tag/vulnerabilities/)
  * [WAF](https://blog.cloudflare.com/zh-tw/tag/waf/)
  * [WASM](https://blog.cloudflare.com/zh-tw/tag/wasm/)
  * [Web 應用程式防火牆](https://blog.cloudflare.com/zh-tw/tag/web-application-firewall/)
  * [WebAssembly](https://blog.cloudflare.com/zh-tw/tag/webassembly/)
  * [WebRTC](https://blog.cloudflare.com/zh-tw/tag/webrtc/)
  * [Workers AI](https://blog.cloudflare.com/zh-tw/tag/workers-ai/)
  * [Workers Launchpad](https://blog.cloudflare.com/zh-tw/tag/workers-launchpad/)
  * [Workers VPC](https://blog.cloudflare.com/zh-tw/tag/workers-vpc/)
  * [Workflows](https://blog.cloudflare.com/zh-tw/tag/workflows/)
  * [Wrangler](https://blog.cloudflare.com/zh-tw/tag/wrangler/)
  * [x402](https://blog.cloudflare.com/zh-tw/tag/x402/)
  * [年度回顧](https://blog.cloudflare.com/zh-tw/tag/year-in-review/)
  * [Zero Trust](https://blog.cloudflare.com/zh-tw/tag/zero-trust/)



[資料庫](https://blog.cloudflare.com/zh-tw/tag/database/)[開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)

[ClickHouse](https://blog.cloudflare.com/zh-tw/tag/clickhouse/)[工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)[效能](https://blog.cloudflare.com/zh-tw/tag/performance/)[資料庫](https://blog.cloudflare.com/zh-tw/tag/database/)[開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)

2026年5月14日

# 我們的帳單處理管道突然變得非常緩慢。罪魁禍首是 ClickHouse 內部一個隱藏的瓶頸

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/zh-tw/author/james-morrison/)和[Christian Endres](https://blog.cloudflare.com/zh-tw/author/christian-endres/)

閱讀時間：10 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/clickhouse-query-plan-contention/)、[日本語](https://blog.cloudflare.com/ja-jp/clickhouse-query-plan-contention/)、[한국어](https://blog.cloudflare.com/ko-kr/clickhouse-query-plan-contention/)和[简体中文](https://blog.cloudflare.com/zh-cn/clickhouse-query-plan-contention/).

![BLOG-3299 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4999A46M2F3BCY3QF5F258.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////789PLy7evs7+3t8/Hx8/Hv7ezp///////+8vL06Oju5+jv7O3y7+/x7e3s////////8vP45Ofx4eXx5+r17O707u/v////////9ff95+r14+f26Oz57/H48vP0/////////P3/7/L77fD78vT/9/j++Pn6////////////+/v//Pv//////////v/+////////////////////////////////////////////////////////////////)

在 Cloudflare，我們是開源在線分析處理 (OLAP) 資料庫 ClickHouse 的重度使用者。每天，我們會呼叫 ClickHouse 數百萬次，來計算使用者應為其使用的 Cloudflare 產品支付多少費用。如果這些作業未能及時完成，後續的發票對帳就會變得非常困難。

這個管道支撐著數億美元的用量收入、防詐騙系統等業務，因此一旦延遲，下游影響會非常嚴重。

正因如此，當 ClickHouse 的每日彙總工作（負責確保 Cloudflare 帳單正常發出）在一次遷移後明顯變慢時，就成了一個大問題。所有常見的可疑因素看起來都正常：I/O、記憶體、掃描的列數、讀取的資料分區。我們通常在 ClickHouse 查詢變慢時會檢查的一切，似乎都沒有問題。

本文將為您講述我們如何發現深藏在 ClickHouse 內部的一個隱藏瓶頸，以及我們為解決該問題而編寫的三個修補程式。

## 環境簡介：一個 PB 級的分析平台

我們在數十個叢集中使用 ClickHouse 儲存超過一百 PB 的資料。為了簡化我們眾多內部團隊的上線流程，我們在 2022 年初建立了一個名為「Ready-Analytics」的系統。

其概念很簡單：團隊不需要設計新的資料表，而是可以將資料串流到一個單一的大型資料表中。不同的資料集透過 `namespace` 來區分，每一筆記錄都使用標準的架構（例如：20 個浮點數欄位、20 個字串欄位、一個時間戳記以及一個 `indexID`）。

在 ClickHouse 中，資料的排序方式對查詢效能至關重要。這就是 `indexID` 發揮作用的地方。它是一個字串欄位，構成了主鍵的一部分，這意味著針對每個獨立的命名空間，其內部資料的排序方式都可以根據該命名空間擁有者預期的查詢模式進行最佳化。總而言之，我們最終得到一個如下所示的主鍵：(`namespace`, `indexID`, `timestamp`)。

這個系統很受歡迎，有數百個應用程式在使用。到 2024 年 12 月為止，它已經成長到超過 2PiB 的資料，且每秒有數百萬列的資料寫入。但它有一個關鍵的缺點：它的資料保留政策。

## 問題：一個保留政策統管全局

Cloudflare 使用 ClickHouse 已經很多年，早在它內建存留時間 (TTL) 功能之前就開始了。因此，我們基於分割區建立了一套自己的資料保留系統。Ready‑Analytics 資料表是以 `day` 為單位進行分割，而我們的資料保留工作就是直接刪除超過 31 天的分區。

這種「一刀切」的 31 天保留政策是一個重大限制。有些團隊因法律或合約要求需要儲存資料多年，而其他團隊可能只需要幾天。這種限制意味著這些使用情境無法採用 Ready-Analytics，必須選擇傳統的設定方式，而後者的上線流程要複雜得多。

我們需要一個允許**每個命名空間自訂保留政策** 的新系統。

## 解決方案：新的分區策略

我們考慮了兩種主要方法：

  1. **每個命名空間一個表格：** 這自然能解決保留問題，但需要大量新的自動化機制來管理數千個按需建立的表格。
  2. **新的分區鍵：** 我們可以將分區鍵從單純的 `(day)` 變更為 `(namespace, day)`。



我們選擇了第二個方案。這將使我們現有的保留系統能夠繼續管理分區，但現在可以精細到每個命名空間的粒度。

我們知道這會增加資料表中資料分區的總數量，但我們做了一個關鍵假設：**由於每個查詢都會用特定的命名空間來篩選， _因此任何單一查詢所讀取的分區數量_ 應該不會改變**。我們認為這代表效能不會受到影響。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4893FX4WFRGPEECQSTGMYN.png&w=715&h=709&f=webp&fit=cover&position=center)

 _圖示說明了我們如何變更分區方式，讓我們能以低成本刪除單一命名空間的資料_

這個新系統也讓我們能夠建立一個精密的儲存管理層。使用[ _「最大‑最小公平演算法」(max‑min fairness algorithm)_](https://en.wikipedia.org/wiki/Max-min_fairness)，我們可以設定一個目標磁碟使用率（例如 90%），並自動「共用」可用的空間。使用量低於其公平份額的命名空間，會將未使用的容量讓給更需要空間的命名空間。這讓我們能夠有信心地將叢集使用率維持在 90%。

我們在 2025 年 1 月開始進行遷移。利用 ClickHouse 的 `Merge` 資料表功能，我們將舊資料表與新資料表結合，所有新資料都寫入新的分區資料表，而舊資料則會隨著時間逐漸淘汰。

## 謎團：當帳單作業開始出問題

兩個月後，也就是 2025 年 3 月底，我們的帳單團隊回報他們每日的彙整作業變慢了。這些作業對時間非常敏感；如果它們無法完成，帳單就無法寄出。這些作業變得越來越慢，而我們正逼近最後期限。

我們進行了調查，但常見的嫌疑項目都不是問題所在。I/O 正常。記憶體正常。個別查詢的指標顯示，它們讀取的資料量或資料分區數量並 _沒有_ 比之前多。我們最初的假設看似正確，但系統卻逐漸停滯。

我們花了幾天的時間才想出一個理論。最後，我們繪製了一張查詢執行時間與叢集中 _資料分區總數_ 的關係圖。其關聯性是不容否認的。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YV50ASJA17DM0BX4JXF3.png&w=715&h=235&f=webp&fit=cover&position=center)

 _Ready Analytics ClickHouse 叢集上的平均 SELECT 查詢執行時間，顯示效能逐漸衰退。_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HY9NE8VMFT5Z5RMHRVCM.png&w=715&h=233&f=webp&fit=cover&position=center)

 _每個資料表副本的資料分區總數線性成長，這是採用新的 (namespace, day) 分區策略後的結果。_

但 _為什麼_ 會這樣？如果我們沒有 _讀取_ 更多的分區，為什麼它們的存在就會拖慢我們的速度？

## 調查：使用火焰圖追查瓶頸

我們轉向使用 ClickHouse 內建的 [`_trace_log_`](https://clickhouse.com/docs/operations/system-tables/trace_log) 來產生火焰圖。這是一個內建的資料表，會記錄執行中 ClickHouse 伺服器的追蹤資訊。它不僅記錄了正在執行的程式碼軌跡，還會將這些軌跡與特定的使用者、查詢 ID 和其他中繼資料關聯起來，這表示必要時可以篩選出相當精確的事件集合。在我們的案例中，我們特別想查看 _葉節點 SELECT 查詢_ 。由於這個資料表中提供了豐富的中繼資料，這很容易做到。

第一張基於 CPU 的火焰圖很快就證實了我們的懷疑：大量的時間花費在**查詢規劃** 階段。這是在執行 _之前_ ，ClickHouse 決定要讀取哪些分區的階段。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46RG580ZDKK07KCTRDD0MK.png&w=715&h=368&f=webp&fit=cover&position=center)

 _火焰圖顯示，葉節點查詢的 CPU 時間中有 45% 用於根據分區 ID 篩選分區向量_

火焰圖清楚顯示：45% 的採樣 CPU 時間花在一個名為 `filterPartsByPartition` 的函數上。

我們第一次嘗試修復是針對這個程式碼路徑做了一個小修補。規劃器會評估啟發式規則來修剪分區，而我們認為這些規則沒有針對我們的資料表以最佳順序進行評估。我們的修補程式改變了順序，帶來了 5% 的小幅改善。我們走在正確的路上，但錯過了真正的問題。

我們之前產生的是「CPU」追蹤，它只會對使用中的執行緒進行取樣。我們切換到「Real」追蹤，它會對 _所有_ 執行緒進行取樣，包括那些停用或正在等待的執行緒。新的火焰圖讓我們恍然大悟。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HV7ET9Z7PXF66NF9GT9Y.png&w=715&h=351&f=webp&fit=cover&position=center)

 _火焰圖顯示，葉節點查詢超過一半的執行時間都花費在等待一個保護活躍分區清單的互斥鎖 (mutex) 上_

問題不在於受 CPU 限制的工作；而在於**嚴重的鎖競爭** (lock contention)。我們查詢超過一半的時間都用來 _等待_ 取得一個保護資料表分區清單的單一互斥鎖 (`MergeTreeData`)。為了規劃一個查詢，每一個執行緒都必須：

  1. 取得這個互斥鎖的**獨佔鎖** 。
  2. 複製一份資料表中 _所有_ 分區的完整清單。
  3. 釋放鎖。
  4. 將該清單篩減至相關的分區。



當擁有數萬個分區和數百個並行查詢時，它們全都只能乖乖地排成單一佇列依序等待。

## 修復方案：三組修補程式

這項發現幫助我們規劃了一系列的最佳化措施來緩解這些熱點。與我們對 ClickHouse 所做的所有修補一樣，我們嘗試讓它們具有通用性，並最終將它們貢獻到上游的程式碼庫中。這讓我們更容易維護我們的分支，也意味著社群也能從我們的修改中受益！

### 最佳化 1：使用共用鎖

查詢規劃器並不會 _修改_ 分區清單；它只是 _讀取_ 而已。它根本沒有理由使用獨佔鎖。

**修複方法：** 我們修改程式碼，改用**共用鎖** (`std::shared_lock`)。這讓所有查詢規劃器能夠同時進入臨界區段。

**結果：** 查詢執行時間立即大幅下降。鎖競爭消失了。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CCVN8NX5N7V0Q8SYKEFN.png&w=715&h=235&f=webp&fit=cover&position=center)

 _共用鎖最佳化（最佳化 1）對平均 SELECT 查詢時間的即時影響，顯示鎖競爭已解決。_

### 最佳化 2：停止複製向量

效能雖然顯著改善，但仍未回到基準線。我們再次回到追蹤記錄，製作了另一張「Real」火焰圖。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48M55TB5PVRTEDJNTSB64J.png&w=715&h=351&f=webp&fit=cover&position=center)

 _火焰圖顯示，我們將四分之一的葉節點查詢時間用於複製所有分區的向量，另外四分之一時間用於篩選它（再次複製）。_

新的火焰圖顯示瓶頸只是轉移了。現在，即使有了共用鎖，大部分時間仍然用來 _複製_ 巨大的分區向量。直覺上，複製一個向量聽起來成本不高，但當它包含數萬個元素，並且每秒進行數百次時，累積起來就很可觀了。

**修複方法：** 我們徹底延後了複製的動作。我們建立了一個分區清單「共用副本」。唯讀操作（例如查詢規劃）直接從這個副本讀取。任何會 _修改_ 分區集合的操作（例如新的資料插入）則會重新產生快取。規劃器現在只複製它們實際需要的、已經 _篩選過_ 的分區清單。

**結果：** 又一次顯著的效能提升。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PPRSHYTZ68EXGM666V41.png&w=715&h=236&f=webp&fit=cover&position=center)

 _推出向量複製最佳化（最佳化 2）後的進一步效能提升。_

在內部看到這些巨大的節省之後，我們決定將這些變更帶給社群。在與 ClickHouse Inc. 的維護者進行了一些小的設計迭代後，我們將這些變更合併到 [_PR #85535_](https://github.com/ClickHouse/ClickHouse/pull/85535) 中 _。_ 自 [_ClickHouse 版本 25.11_](https://clickhouse.com/docs/whats-new/changelog/2025#performance-improvement-1) 起，這些變更就已可用。

### 最佳化 3：對分區進行二元搜尋

我們仍然沒有停下來。隨著分區數量增加，效能 _仍然_ 會下降，只是速度慢得多。與分區數量的關聯性仍然存在。幾個月後再次回到這個問題，新的火焰圖（看起來與圖 3 相同）顯示時間花費在篩選程式碼路徑上（我們第一次嘗試修復的那個）。這個程式碼會對所有分區進行**線性掃描** ，逐一評估每個分區的述詞。幾個月後，我們又回到了最佳化之前的查詢執行時間。

但是我們知道這個分區清單是依照分區鍵排序的。請記住，分區鍵的第一個欄位是 namespace，絕大多數的查詢都會用它來篩選，因為它用來識別「租用戶」。我們要如何利用這一點？

**修複方法：** 我們實作了一個基於分區 ID 中 `namespace` 部分的二元搜尋。這麼做之所以可行，是因為向量是已排序的，所以可以在不實際查看項目的情況下濾除很多項目。由於 `namespace` 是該排序鍵的第一部分，這種方法特別有效。在經過第一輪的二元搜尋之後，我們需要檢查的分區範圍大幅縮小，而對於這些分區，我們仍然會逐個檢查，套用與之前相同的邏輯，根據其他條件來排除分區。

**結果：** 在 2026 年 3 月部署這個修補程式之後，查詢執行時間下降了 50%（見圖 8）。更重要的是，這終於打破了查詢執行時間與分區數量之間的關聯性。不幸的是，這個解決方案對於任意的查詢條件（例如 `namespace in (5,10)` 這樣的條件）並沒有那麼通用。我們正在研究更通用的方法，例如擴展[ _查詢條件快取_](https://clickhouse.com/blog/introducing-the-clickhouse-query-condition-cache)以涵蓋分區篩選。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46ZC0AXABREP5Q1ES3D0CS.png&w=715&h=239&f=webp&fit=cover&position=center)

 _實施二元搜尋進行分區修剪（最佳化 3）後，延遲持續降低。_

## 暫時的平靜

這些最佳化解決了帳單系統眼前的危機。但這段歷程揭示了我們分區選擇所帶來的深層且不顯著的成本。

其他問題依然存在。在這篇部落格文章中，我們只描述了增加分區數量對 SELECT 執行時間造成的問題，但它也對 ZooKeeper 造成了困擾，因為 ZooKeeper 負責追蹤 ClickHouse 中所有分區的中繼資料。也許有一天我們會聊聊那個 100 GB ZooKeeper 叢集的故事。

我們為自己爭取到了寶貴的喘息空間，但根本問題依然存在：這種分區策略是長期的正確選擇嗎？或者我們最終仍需面對現實，轉向不同的架構？目前，我們的修補程式還在支撐著，但這次經歷清楚地說明了，即使是規劃周全的變更，也可能因為錯誤的假設而遭遇挫折。

當帳單團隊第一次回報這個問題時，我們每個副本有 3 萬個分區。分區數量從未停止成長，一年後我們每個副本達到了 16 萬個分區，但由於我們在這裡所做的最佳化，查詢執行時間一直保持穩定。

在 Cloudflare，我們在大規模的環境中解決複雜的工程問題。如果您覺得我們在這裡描述的偵錯與最佳化過程，聽起來像是您正在尋找的那種挑戰，歡迎看看我們正在招募的一些[ _職缺_](https://www.cloudflare.com/careers/jobs/?department=Engineering)。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fclickhouse-query-plan-contention%2F&t=%E6%88%91%E5%80%91%E7%9A%84%E5%B8%B3%E5%96%AE%E8%99%95%E7%90%86%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E8%AE%8A%E5%BE%97%E9%9D%9E%E5%B8%B8%E7%B7%A9%E6%85%A2%E3%80%82%E7%BD%AA%E9%AD%81%E7%A6%8D%E9%A6%96%E6%98%AF%20ClickHouse%20%E5%85%A7%E9%83%A8%E4%B8%80%E5%80%8B%E9%9A%B1%E8%97%8F%E7%9A%84%E7%93%B6%E9%A0%B8)[](https://x.com/intent/post?text=%E6%88%91%E5%80%91%E7%9A%84%E5%B8%B3%E5%96%AE%E8%99%95%E7%90%86%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E8%AE%8A%E5%BE%97%E9%9D%9E%E5%B8%B8%E7%B7%A9%E6%85%A2%E3%80%82%E7%BD%AA%E9%AD%81%E7%A6%8D%E9%A6%96%E6%98%AF+ClickHouse+%E5%85%A7%E9%83%A8%E4%B8%80%E5%80%8B%E9%9A%B1%E8%97%8F%E7%9A%84%E7%93%B6%E9%A0%B8&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fclickhouse-query-plan-contention%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fclickhouse-query-plan-contention%2F)[](https://bsky.app/intent/compose?text=%E6%88%91%E5%80%91%E7%9A%84%E5%B8%B3%E5%96%AE%E8%99%95%E7%90%86%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E8%AE%8A%E5%BE%97%E9%9D%9E%E5%B8%B8%E7%B7%A9%E6%85%A2%E3%80%82%E7%BD%AA%E9%AD%81%E7%A6%8D%E9%A6%96%E6%98%AF+ClickHouse+%E5%85%A7%E9%83%A8%E4%B8%80%E5%80%8B%E9%9A%B1%E8%97%8F%E7%9A%84%E7%93%B6%E9%A0%B8+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fclickhouse-query-plan-contention%2F)[](https://mastodonshare.com/?text=%E6%88%91%E5%80%91%E7%9A%84%E5%B8%B3%E5%96%AE%E8%99%95%E7%90%86%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E8%AE%8A%E5%BE%97%E9%9D%9E%E5%B8%B8%E7%B7%A9%E6%85%A2%E3%80%82%E7%BD%AA%E9%AD%81%E7%A6%8D%E9%A6%96%E6%98%AF+ClickHouse+%E5%85%A7%E9%83%A8%E4%B8%80%E5%80%8B%E9%9A%B1%E8%97%8F%E7%9A%84%E7%93%B6%E9%A0%B8&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fclickhouse-query-plan-contention%2F)[](https://www.threads.net/intent/post?text=%E6%88%91%E5%80%91%E7%9A%84%E5%B8%B3%E5%96%AE%E8%99%95%E7%90%86%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E8%AE%8A%E5%BE%97%E9%9D%9E%E5%B8%B8%E7%B7%A9%E6%85%A2%E3%80%82%E7%BD%AA%E9%AD%81%E7%A6%8D%E9%A6%96%E6%98%AF+ClickHouse+%E5%85%A7%E9%83%A8%E4%B8%80%E5%80%8B%E9%9A%B1%E8%97%8F%E7%9A%84%E7%93%B6%E9%A0%B8+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fclickhouse-query-plan-contention%2F)

## 相關標籤

[ClickHouse](https://blog.cloudflare.com/zh-tw/tag/clickhouse/)[工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)[效能](https://blog.cloudflare.com/zh-tw/tag/performance/)[資料庫](https://blog.cloudflare.com/zh-tw/tag/database/)[開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
