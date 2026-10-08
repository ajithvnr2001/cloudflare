---
url: https://blog.cloudflare.com/zh-tw/post-mortem-on-cloudflare-control-plane-and-analytics-outage/
title: Cloudflare \u63a7\u5236\u5e73\u9762\u548c\u5206\u6790\u670d\u52d9\u4e2d\u65b7\u7684\u4e8b\u5f8c\u5206\u6790 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:39:46.170830+00:00
---

# Cloudflare 控制平面和分析服務中斷的事後分析 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/post-mortem-on-cloudflare-control-plane-and-analytics-outage/

[部落格](https://blog.cloudflare.com/zh-tw/)

[事後檢討](https://blog.cloudflare.com/zh-tw/tag/post-mortem/)[服務中斷](https://blog.cloudflare.com/zh-tw/tag/outage/)

2 標籤顯示 2 個標籤

  * 文章標籤
  * [事後檢討](https://blog.cloudflare.com/zh-tw/tag/post-mortem/)[服務中斷](https://blog.cloudflare.com/zh-tw/tag/outage/)
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



[事後檢討](https://blog.cloudflare.com/zh-tw/tag/post-mortem/)[服務中斷](https://blog.cloudflare.com/zh-tw/tag/outage/)

2023年11月4日

# Cloudflare 控制平面和分析服務中斷的事後分析

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/zh-tw/author/matthew-prince/)

閱讀時間：13 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Deutsch](https://blog.cloudflare.com/de-de/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Español](https://blog.cloudflare.com/es-es/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Français](https://blog.cloudflare.com/fr-fr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[日本語](https://blog.cloudflare.com/ja-jp/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[한국어](https://blog.cloudflare.com/ko-kr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[简体中文](https://blog.cloudflare.com/zh-cn/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)和[Português](https://blog.cloudflare.com/pt-br/post-mortem-on-cloudflare-control-plane-and-analytics-outage/).

![Post mortem on the Cloudflare Control Plane and Analytics Outage](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FSBWC0D25T68JD98V477.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vz/8e/v7Obi7ujj8u3q8O7u6ent/////f7/8+7q7eLa7+Ta9Ozk8u/s7Ozt////////9u7n8ODT8uPT9+3h9vLs8fDv////////+/Lq9OPU9+bV/PLk/Pfw9vXz//////////ny++zf/e/h//rv//74/Pr5///////////+//fv//vy///9///////////////////////9////////////////////////////////////////////////)

從世界標准時 2023 年 11 月 2 日（星期四）11:43 開始，Cloudflare 的控制平面和分析服務經歷了一次服務中斷。Cloudflare 的控制平面主要包括我們所有服務（包括網站和 API）面向客戶的介面。我們的分析服務包括日誌記錄和分析報告。

事件從世界標準時 11 月 2 日 11:44 持續到世界標準時 11 月 4 日 04:25。截至世界標准時 11 月 2 日 17:57，我們在災難復原設施中恢復了大部分控制平面。在災難復原設施上線後，許多客戶在使用我們的大多數產品時沒有再遇到問題。不過，其他服務的恢復時間較長，在我們完全解決該事件之前，使用這些服務的客戶可能會遇到一些問題。在事件發生期間，大多數客戶無法使用我們的原始記錄服務。

現在已為所有客戶恢復服務。在整個事件過程中，Cloudflare 的網路和安全服務仍舊按預期運作。雖然有一段時間客戶無法對這些服務進行變更，但通過我們網路的流量並未受到影響。

這篇文章概述了導致此事件的原因、我們為防止此類問題而設立的架構、失敗的地方、生效的地方和原因，以及我們根據過去 36 小時內吸取的教訓而正在做出的改變。

首先，這本不應該發生。我們原本相信，即使我們的一個核心資料中心提供者發生災難性故障，我們的高可用性系統也能阻止這樣的服務中斷。然而，雖然許多系統確實按照設計保持線上狀態，但一些關鍵系統具有不明顯的相依性，導致它們不可用。對於此次事件以及它給我們的客戶和團隊帶來的痛苦，我感到非常抱歉和難堪。

### 設計意圖

Cloudflare 的控制平面和分析系統主要在俄勒岡州希爾斯伯勒附近三個資料中心的伺服器上執行。這三個資料中心相互獨立，每個資料中心都有多個市電電源，每個資料中心都有多個獨立的備援網路連線。

我們對這些設施的位置進行了慎重選擇，有意使其相距一定距離，以最大限度地減少一場自然災害使這三個設施全部受到影響的可能性，同時又足夠近，以便它們都可以執行主動-主動備援資料叢集。這意味著這三個設施之間在不斷同步資料。根據設計，如果任何一個設施停運，其餘的設施都能繼續運作。

這是我們四年前開始實施的系統設計。雖然我們的大多數關鍵控制平面系統都已遷移到高可用性叢集，但一些服務，特別是一些較新產品的服務，尚未新增到高可用性叢集中。

此外，我們有意未將日誌記錄系統作為高可用性叢集的一部分。該決定的邏輯是，日誌記錄已經是一個分散式問題，記錄在我們的網路邊緣排隊，然後傳送回俄勒岡州的核心（或使用區域服務進行日誌記錄的客戶的另一個區域設施）。如果我們的日誌記錄設施離線，那麼分析記錄就會在網路邊緣排隊，直到它重新上線。我們認為分析延誤是可以接受的。

### Flexential 資料中心電源故障

俄勒岡州三個設施中最大的一個由 Flexential 執行。我們將該設施稱為「PDX-DC04」。Cloudflare 在 PDX-04 租用了空間，我們最大的分析叢集以及高可用性叢集三分之一以上的機器都在這裡。尚未加入我們高可用性叢集的服務也預設放在此處。我們是該設施一個相對較大的客戶，使用了其總容量的約 10%。

世界標準時 11 月 2 日 08:50，為 PDX-04 提供服務的市電公司 Portland General Electric (PGE) 發生了一次計畫外維護事件，影響了其大樓的一個獨立供電電源。該事件關閉了 PDX-04 的一路電源。資料中心擁有多個具有一定程度獨立性的電源，可以為設施供電。不過，Flexential 啟動了發電機，來有效補充減少的電源。

遺憾的是，Flexential 沒有通知 Cloudflare 他們已容錯移轉為發電機供電，這並不是最佳做法。我們的可觀察性工具都無法偵測到電力來源發生了變化。如果他們通知了我們，我們就會成立一個小組，密切監視該設施，並在其降級時將依賴於該設施的控制平面服務轉移出去。

Flexential 同時執行發電機和一路剩餘市電來進行供電，這種做法也很罕見。當電力需求較高時，市電公司要求資料中心脫離電網，完全依靠發電機執行，這種情況比較常見。Flexential 營運著 10 台發電機，包括備援機組，能夠在滿負荷的情況下為設施提供支援。Flexential 公司也可以僅利用剩餘的市電來執行該設施。他們為什麼要同時使用市電和發電機供電，我們尚未得到明確的答案。

### 對後續事情的知情推測

從這個決定開始，我們還沒有從 Flexential 那裡弄清根本原因或他們做出的某些決定或發生的事件。在從 Flexential 和 PGE 處獲得有關所發生事件的更多資訊後，我們將更新這篇文章。以下部分內容是根據最有可能發生的一系列事件以及個別 Flexential 員工向我們透露的非官方資訊做出的推測。

他們讓市電線路繼續執行的一個可能原因是，Flexential 是 PGE 一項名為 DSG 的計畫的一部分。DSG 允許當地市電公司執行一個資料中心的發電機，幫助向電網提供額外電力。作為交換，電力公司幫助維護發電機並提供燃料。我們無法找到 Flexential 向我們通知 DSG 計畫的任何記錄。我們曾詢問 DSG 計畫當時是否處於作用狀態，但尚未收到答覆。我們不知道是否是這一計畫促成了 Flexential 所做的決定，但它可以解釋為什麼在發電機啟動後，市電線路仍在運作。

世界標准時 11:40 左右，PDX-04 的 PGE 變壓器發生接地故障。我們認為（但尚未從 Flexential 或 PGE 得到證實），是為第二路電源電網降壓的一台變壓器發生了故障，而第二路電源在進入資料中心時仍在執行。雖然我們無法向 Flexential 或 PGE 確認，但接地故障很可能是 PGE 正在進行的計畫外維護造成的，正是這一維護影響了第一路電源。又或者，這只是一個非常不幸的巧合。

高壓（12,470 伏）電線的接地故障非常嚴重。電氣系統設計為可在發生接地故障時迅速關閉，以防止損壞。不幸的是，在這種情況下，保護措施也關閉了 PDX-04 的所有發電機。這意味著該設施的兩個發電來源——備援市電線路和 10 台發電機——均已斷電。

幸運的是，除了發電機，PDX-04 還擁有一組 UPS 電池。據稱，這些電池足以為該設施提供約 10 分鐘的電力。這段時間足以彌補電力中斷和發電機自動啟動之間的差距。如果 Flexential 能在 10 分鐘內恢復發電機或市電供電，那麼就不會出現中斷。但實際上，根據我們從自己的設備故障中觀察到的情況，電池只用了 4 分鐘就開始失效。而 Flexential 恢復發電機所花的時間遠不止 10 分鐘。

### 嘗試恢復供電

雖然我們還沒有得到官方證實，但員工告訴我們，有三件事阻礙了發電機的重新啟動。首先，由於接地故障導致電路跳閘，因此需要實際進入並手動重新啟動。其次，Flexential 的存取控制系統沒有備用電池供電，因此處於離線狀態。第三，現場的夜班人員中沒有經驗豐富的操作或電氣專家——夜班人員包括保安和一名無人陪伴的技術人員，這名技術人員才剛剛上崗一週。

世界標准時 11:44 至 12:01 期間，由於發電機沒有完全重新啟動，UPS 電池耗盡，資料中心的所有客戶都斷電了。在整個過程中，Flexential 從未告知 Cloudflare 該設施存在任何問題。世界標准時 11:44，連接資料中心與世界其他地方的兩台路由器離線，我們這才得知資料中心出現問題。當我們無法直接或透过頻外管理連線路由器時，我們嘗試聯絡 Flexential，並派遣我們的當地團隊親自前往該設施。世界標准時 12:28，Flexential 向我們傳送了第一條表示他們遇到問題的訊息。

>  _目前，我們的 [PDX-04] 遇到電源問題，該問題始於太平洋時間上午 05:00 [世界標准時 12:00] 左右。工程師們正在積極解決問題並恢復服務。我們將每 30 分鐘通報一次進展情況，或在獲得更多資訊時通報預計恢復時間。感謝您的耐心和理解。_

### 針對資料中心級故障所做的設計

雖然 PDX-04 的設計在施工前已通過 Tier III 認證，並有望提供高可用性 SLA，但我們仍計劃了它可能離線的可能性。即使是營運良好的設施也會有不順利的時候。我們也為此做了計劃。如若發生此類事件，我們的預期情況是：我們的分析將處於離線狀態，記錄將在邊緣排隊並延遲，並且未整合到我們高可用性叢集中的某些較低優先順序服務將暫時離線，直到可以在另一個設施中恢復。

在該地區執行的另外兩個資料中心將接管高可用性叢集的責任，並保持關鍵服務處於上線狀態。一般來講，這可以按計劃進行。不幸的是，我們發現本應在高可用性叢集上執行的部分服務依賴於僅在 PDX-04 中執行的服務。

特別是，處理記錄並為我們的分析提供支援的兩個關鍵服務——Kafka 和 ClickHouse——僅在 PDX-04 中可用，但有依賴於它們的服務在高可用性叢集中執行。這些相依性本不應該如此緊密，本應該更體面地失效，我們本應該發現這些相依性。

我們對高可用性叢集進行過測試，將另外兩個資料中心設施分別和同時完全關閉。我們還測試過將 PDX-04 的高可用性部分離線。但是，我們從未測試過完全關閉整個 PDX-04 設施。因此，我們忽略了資料平面上某些相依性的重要性。

在要求新產品及其關聯資料庫與高可用性叢集整合方面，我們也過於鬆懈。Cloudflare 允許多個團隊快速創新。因此，產品往往會以不同的方式進入初始測試階段。雖然隨著時間的推移，我們的做法是將這些服務的後端遷移到我們的最佳做法位置，但在產品宣佈普遍可用 (GA) 之前，我們並沒有正式要求這樣做。這是一個錯誤，因為這意味著我們的備援保護措施會因產品不同而效果不一。

此外，我們有太多的服務依賴於核心設施的可用性。雖然這是許多軟體服務的建立方式，但它並沒有發揮 Cloudflare 的優勢。我們擅長分散式系統。在整個事件過程中，我們的全球網路仍舊按預期運作。雖然我們的一些產品和功能可以透過網路邊緣進行設定和維護，而無需核心，但如今，如果核心不可用，會有太多產品和功能失效。我們需要使用我們為所有客戶提供的分散式系統產品來提供我們的所有服務，這樣，即使我們的核心設施受到干擾，它們也能繼續正常運作。

### 災難復原

世界標准時 12:48，Flexential 重新啟動了發電機。設施內的部分場所恢復供電。為了避免系統不堪重負，當資料中心恢復供電時，通常是一次接通一條電路，逐步恢復供電。就像住宅中的電路斷路器一樣，每個客戶都由備援斷路器提供服務。當 Flexential 試圖重新開機 Cloudflare 的電路時，發現斷路器出現故障。我們不知道斷路器是由於接地故障或者是由於事故造成的其他浪湧而失靈，還是斷路器之前就壞了，只是在斷電後才被發現。

Flexential 開始更換故障斷路器。這就要求他們採購新的斷路器，因為壞的斷路器比他們設施內現有的還要多。由於離線的服務比我們預期的要多，而且 Flexential 無法給出恢復服務的時間，因此在世界標准時 13:40，我們決定向 Cloudflare 位於歐洲的災難復原網站進行容錯移轉。值得慶幸的是，我們只需要對 Cloudflare 整體控制平面的一小部分進行容錯移轉。我們的大部分服務繼續在兩個作用中的核心資料中心的高可用性系統上執行。

世界標准時 13:43，我們在災難復原網站上啟動了第一批服務。Cloudflare 的災難復原網站可在發生災難時提供關鍵的控制平面服務。不過，災難復原網站不支援我們的某些記錄處理服務，其旨在支援我們控制平面的其他部分。

在那裡啟動服務後，我們遇到了驚群問題，此前一直失敗的 API 呼叫一下子使我們的服務不堪重負。我們實施了速率限制，以控制請求量。在此期間，大多數產品的客戶在透過我們的儀表板或API 進行修改時都會出現間歇性錯誤。截至世界標准時 17:57，已成功轉移到災難復原網站的服務趨於穩定，大多數客戶不再受到直接影響。然而，在我們恢復 PDX-04 之前，一些系統仍然需要手動設定（如 Magic WAN），其他一些服務（主要與記錄處理和一些客製 API 有關）仍然無法使用。

### 部分產品和功能延遲重新啟動

在我們的災難復原網站上，有少數產品沒有正常啟動。這些往往是較新的產品，我們還沒有完全實作和測試災難復原程序。其中包括我們用於上傳新影片的 Stream 服務和其他一些服務。為了恢復這些服務，我們的團隊同時開展了兩項工作：1) 在我們的災難復原網站上重新實作這些服務；2) 將它們遷移到我們的高可用性叢集。

Flexential 更換了發生故障的斷路器，恢復了兩路市電供應，並在世界標准時 22:48 確認電力供應正常。我們的團隊全員到崗，在緊急情況下工作了一整天，因此我決定讓我們大多數人休息一下，明天一早開始返回 PDX-04。這個決定推遲了我們的全面恢復，但我認為，它降低了我們因其他人為錯誤而使情況更加複雜的可能性。

從 11 月 3 日一早開始，我們的團隊就開始在 PDX-04 恢復服務。首先是實際啟動我們的網路設備，然後啟動數千台伺服器並恢復其服務。資料中心的服務狀態尚不清楚，因為我們認為事件期間可能發生了多次電源迴圈。我們唯一安全的復原程序就是對整個設施進行全面啟動。

這需要人工將我們的設定管理伺服器連線，以開始恢復設施。這個過程花了 3 個小時。之後，我們的團隊就能夠啟動其餘伺服器的重建工作，為我們的服務提供動力。每台伺服器的重建時間從 10 分鐘到 2 小時不等。雖然我們可以對多台伺服器同時執行這個過程，但服務之間存在固有的相依性，需要按順序恢復一些服務的運作。

截至世界標准時 2023 年 11 月 4 日 04:25，服務已全面恢復。由於我們還將分析資料儲存在歐洲核心資料中心中，因此對於大多數客戶而言，他們在我們的儀表板和 API 中的資料都不會有損失。然而，一些未在歐盟複製的資料集將存在持續的差距。對於使用我們的記錄推送功能的客戶，在事件持續的大部分時間裡，您的記錄都未得到處理，因此，您未收到的內容也將無法恢復。

### 教訓和補救

我們有許多問題需要 Flexential 解答。但是，我們也必須預料到整個資料中心可能會發生故障。Google 有一個程序，當發生重大事件或危機時，他們可以發出「黃色警報」或「紅色警報」。在這些情況下，大部分或所有工程資源都被轉移到解決當前問題上。

我們過去沒有這樣的程序，但今天我們顯然需要實作一個我們自己的版本：橙色警報。我們正在轉移所有非關鍵工程功能，著重於確保控制平面的高可靠性。作為該過程的一部分，我們預計會有以下變化：

  * 消除所有服務的控制平面設定對核心資料中心的依賴，盡可能首先由我們的分散式網路提供動力
  * 確保即使我們所有的核心資料中心都處於離線狀態，網路上執行的控制平面仍能繼續運作
  * 要求所有指定為「普遍可用」的產品和功能必須依賴于高可用性叢集（如果它們依賴於我們的任何核心資料中心），而不對特定設施有任何軟體依賴
  * 要求所有指定為「普遍可用」的產品和功能都具有經過測試的可靠災難復原計畫
  * 測試系統故障的影響範圍，最大程度地減少受故障影響的服務數量
  * 對所有資料中心功能實作更嚴格的混沌測試，包括完全關閉我們的每個核心資料中心設施
  * 對所有核心資料中心進行徹底稽核，並制定重新稽核計畫以確保它們符合我們的標準
  * 確立日誌記錄和分析災難復原計畫，確保即使我們的所有核心設施都發生故障，也不會丟失任何記錄



正如我之前所說，我對這次事件以及它給我們的客戶和團隊帶來的痛苦感到抱歉和尷尬。我們已經建立了正確的系統和程序，能夠承受我們在資料中心提供者處看到的一連串故障，但我們需要更加嚴格地執行這些系統和程序，並對未知的相依性進行測試。在今年餘下的時間裡，我和我們團隊的大部分成員都將全力以赴。過去幾天的痛苦會讓我們變得更好。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F&t=Cloudflare%20%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8B%99%E4%B8%AD%E6%96%B7%E7%9A%84%E4%BA%8B%E5%BE%8C%E5%88%86%E6%9E%90)[](https://x.com/intent/post?text=Cloudflare+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8B%99%E4%B8%AD%E6%96%B7%E7%9A%84%E4%BA%8B%E5%BE%8C%E5%88%86%E6%9E%90&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://bsky.app/intent/compose?text=Cloudflare+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8B%99%E4%B8%AD%E6%96%B7%E7%9A%84%E4%BA%8B%E5%BE%8C%E5%88%86%E6%9E%90+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://mastodonshare.com/?text=Cloudflare+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8B%99%E4%B8%AD%E6%96%B7%E7%9A%84%E4%BA%8B%E5%BE%8C%E5%88%86%E6%9E%90&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://www.threads.net/intent/post?text=Cloudflare+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8B%99%E4%B8%AD%E6%96%B7%E7%9A%84%E4%BA%8B%E5%BE%8C%E5%88%86%E6%9E%90+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)

## 相關標籤

[事後檢討](https://blog.cloudflare.com/zh-tw/tag/post-mortem/)[服務中斷](https://blog.cloudflare.com/zh-tw/tag/outage/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
