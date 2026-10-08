---
url: https://blog.cloudflare.com/zh-tw/revisiting-spectre-attacks-on-workers/
title: \u91cd\u65b0\u5be9\u8996\u91dd\u5c0d Cloudflare Workers \u7684\u9060\u7aef Spectre \u653b\u64ca | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:34:48.725664+00:00
---

# 重新審視針對 Cloudflare Workers 的遠端 Spectre 攻擊 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/revisiting-spectre-attacks-on-workers/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)[攻擊](https://blog.cloudflare.com/zh-tw/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-tw/tag/vulnerabilities/)+1顯示另外 1 個標籤

4 標籤顯示 4 個標籤

  * 文章標籤
  * [Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)[攻擊](https://blog.cloudflare.com/zh-tw/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-tw/tag/vulnerabilities/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)
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



[研究](https://blog.cloudflare.com/zh-tw/tag/research/)

[Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)[攻擊](https://blog.cloudflare.com/zh-tw/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-tw/tag/vulnerabilities/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)

2026年9月9日

# 重新審視針對 Cloudflare Workers 的遠端 Spectre 攻擊

![Martin Schwarzl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q44FVCNYF3AKGF6DGP9G.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Albert Pedersen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46X1RPT45576XPREMG1CQ3.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Martin Schwarzl](https://blog.cloudflare.com/zh-tw/author/martin/)和[Albert Pedersen](https://blog.cloudflare.com/zh-tw/author/albert-pedersen/)

閱讀時間：14 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/revisiting-spectre-attacks-on-workers/)和[简体中文](https://blog.cloudflare.com/zh-cn/revisiting-spectre-attacks-on-workers/).

![](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZC7473CXRW6EF1Z69ZW.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAIQAeJwAcMQAcNwAoNwA1MgA5KQAxIQAdKQAaNgAoTDFAWURSW0hbUz5XQyhGMgApLwAUQhsyX01VcWVsdGlzaV1rVUNUPxsyMwAPSCQ1Z1ddenF1fnZ8c2lyXU1ZRCM2MwAPRiEyY1NXdmxteXFzb2RqWklSQiAyMQASPxIpVkFFZVdXaFxbYFFTTzlBOhEpLQAVNQAcRCUqTzczUjs2TDQyQCApMAAdLAAWMAAWOg4VQyEWRiUYQh4ZOAkYKwAX)

2021 年，我們評估了針對 Cloudflare Workers 的[ _遠端 Spectre 攻擊_](https://blog.cloudflare.com/spectre-research-with-tu-graz/)，並基於評估結果在生產環境中部署了名為[ _動態處理序隔離_](https://blog.cloudflare.com/spectre-research-with-tu-graz/)（Dynamic Process Isolation，DyPrIs）的防禦機制——該機制能夠識別行為可疑的指令碼，並將其隔離至獨立的處理序。此後，用於穩定 Spectre 攻擊的新技術不斷湧現。為評估這些技術是否對 Workers 生產環境構成威脅，我們決定在內部重新評估遠端 Spectre 攻擊。透過在生產環境中建構更新版的概念驗證，我們能夠在實際生產負載下對 Spectre 攻擊風險進行實證評估。

在生產環境中發動成功的側信道攻擊，外部攻擊者還需克服額外障礙，包括共用硬體資源上的活動、中斷、情境切換以及粗粒度計時器等。我們的研究發現了 DyPrIs 實作中的一項限制，並成功在 Cloudflare Workers 生產環境中示範了一次遠端 Spectre 攻擊，能夠穩定地洩漏資料，速度可達每秒 12 位元，準確率高達 99%。基於這項研究，我們改進了 DyPrIs，整合了 V8 Sandbox 和處理序[ _內隔離機制_](https://blog.cloudflare.com/safe-in-the-sandbox-security-hardening-for-cloudflare-workers/)，以進一步降低記憶體洩漏攻擊的風險。

今天，我們[ _發表了一篇論文_](https://arxiv.org/pdf/2608.17043)，詳細描述了上述研究發現，論文由 Albert Pedersen、Haocheng Xiao、Sam Ainsworth、Nigel Topham 和 Martin Schwarzl 共同撰寫，涵蓋 2024 年至 2025 年初的研究工作。

請注意，由於 Cloudflare Workers Runtime 團隊已部署相應對策，文中所描述的攻擊在生產系統中已得到緩解。過去三年間，我們未發現任何主動利用的跡象。

## **Cloudflare Workers 安全模型**

Cloudflare Workers 在邊緣節點上執行不受信任的 JavaScript 程式碼。借助 V8 隔離區（isolate）提供的語言層隔離，數以萬計的租用戶可共用同一作業系統處理序處理序。每個 Worker 擁有各自獨立的 JavaScript 堆積。這一設計既能降低啟動延遲，又能相比完整處理序隔離方案更高效地執行大量租用戶。在執行階段層面，我們部署了多層防禦機制，包括：自動化 V8 修補程式管線、由 Linux 命名空間和 seccomp 篩選器構成的雙層沙箱、Cap'n Proto RPC，以及將特定指令碼排程至獨立處理序沙箱的能力。儘管如此，Worker 處理序內的單一任意讀取漏洞仍可導致跨租用戶資料洩漏。其中最難以緩解的漏洞利用了推測執行（speculative execution）的特性，即處理序內的**Spectre** 。

## Spectre

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA1t3TzdfRssfOi7XRb63ZgLbgrMnfz9naz9jMxNHJpb/Dd6rDVKLJba3Qn8HRxNPOydXGvc3Cmrm5ZaK1Opm4XaW+lLvCuczBy9fHv8/Dnbu4bKWxTZ2xaam2l7y7t8u81t/RzNjNr8bEjLW8e6+6jLi+qcbCwNHE5ung3eTdxtbVr8rPpcbNr8vQwdTS0NvT8vLs6+7p2ePjx9rfwdfeyNvf1ODg3eTg9/bx8PLu4Ojp0ODly97k0eHm2+Xm4ufl)![BLOG-3371 2.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZ9V2EAMVDZNCTAT5G4G.png&w=715&h=358&f=webp&fit=cover&position=center)

推測執行的原理可以用健行來類比。在某個岔路口，您需要預判前行方向。若預判正確，您節省了時間，可以在山間小屋享受陽光和消暑飲料。然而，若預判方向錯誤，您不得不折返。山路看起來完好如初，但您的腳印仍留在泥土裡。

CPU 的推測執行與此類似。分支預測（branch prediction）會提前對分支結果作出預判，CPU 隨即推測性地執行該分支。若預測正確，推測執行節省了時間；若預測錯誤，CPU 則需捨棄結果、回溯並執行另一分支。由於這些推測執行的指令僅在 CPU 管線中短暫存在，從未被永久退出或提交，學術界將其稱為瞬態指令（transient instructions），並將此概念概括為瞬態執行（transient execution）。

然而，瞬態執行仍會在微架構狀態中留下痕跡，例如殘留在 CPU 快取中的資料。因此，攻擊者可利用 Spectre 以瞬態方式越界存取記憶體，將單一位元的資訊編碼至快取狀態，並透過測量重新存取資料的延遲來推斷該位元是否被設定。

為[ _緩解處理序內 Spectre 攻擊_](https://blog.cloudflare.com/spectre-research-with-tu-graz/)，Cloudflare Workers 凍結本機計時器、禁止多執行緒和共用記憶體，並主動偵測可疑指令碼、定期對記憶體進行隨機化，同時將行為可疑的指令碼隔離至獨立處理序。

## **攻擊原語**

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA9fj/8/X97u706+rv6ezv6O7x5Ovu3+To+vz/9/f+8O/06+vv7O7x7fH06u/y5Ojr/////Pz/8vH27e3w8PHz9Pf48fX26e3v////////9/b68fHz9fb3+fz89/r78PPz/////////fz/9/f4+fz7/f///P/+9vj3/////////////f7+/P///v///v//+vz6/////////////////v///v///v///f78/////////////////////v///v///v/9)![BLOG-3371 3.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYBPHGE9QQXKZPXBAR7G.png&w=715&h=518&f=webp&fit=cover&position=center)

遠端 Spectre 攻擊高層概覽示意圖。攻擊者需要一個遠端計時器，用於測量探測瞬態洩漏位元為「0」還是「1」所需的時間。

Cloudflare Workers 平台有意[ _限制計時器_](https://blog.cloudflare.com/mitigating-spectre-and-other-security-threats-the-cloudflare-workers-security-model/)的精度。在僅使用 CPU 執行期間，時間實際上處於凍結狀態：`Date.now()` 和 `performance.now()` 無法提供持續推進的高精度時鐘。由於沒有共用記憶體且不支援多執行緒，經典的基於 `SharedArrayBuffer` 的計數執行緒計時器也無從使用。

要成功發動攻擊，需要解決以下幾個挑戰：其一，Workers 執行階段的資源受限，必須確保攻擊者與受害者實現共同部署（co-location）；其二，需要找到一個可靠的（且好與目標共同部署的）遠端計時器，以實現穩定的時間測量；其三，攻擊在生產條件下執行，因此還需要額外的穩定性保障，包括：一個可靠的 Spectre gadget（利用小工具）以實現瞬態 64 位元越界存取、應對系統和網路噪音的強健訊號放大機制，以及可靠地將資料從快取中驅逐的原語。

### Spectre gadget
    
    
    return probeArray[
              obj instanceof ObjP
                ? PROBEARRAY_OFFSET + ((obj.ptr[0] >> bit) & 1) * 0x800
                : 0x400
    ];

_推測型別混淆 Spectre gadget_

借助正確的 Spectre gadget（如上方程式碼片段所示），攻擊者可以瞬態方式越界存取記憶體，並將單一位元編碼至快取（`probeArray`）中。攻擊者隨後測量記憶體存取延遲，以確認資料是否已被快取：存取較快表示該快取行已快取，對應位元為 1；存取較慢則表示未快取，對應位元為 0。

在我們的攻擊中，使用了兩種不同類型的 Spectre gadget。第一種用於洩漏壓縮堆積指標，例如隔離區的堆積基底位址（根位址）；第二種則利用推測型別混淆，從攻擊者精心構造的使用者空間 64 位元指標處讀取資料。在開展研究時，V8 Sandbox 尚未在 Cloudflare Workers 上實作。在指標壓縮模式下，大多數物件使用 32 位元壓縮指標，而 `TypedArray` 是少數仍儲存指向其後備儲存體原始 64 位元指標的例外——這正是我們的 gadget 所利用的。

分支 `obj instanceof ObjP` 執行型別檢查，即一次分支操作。為誤導分支預測，我們多次以真實的 `ObjP` 實例呼叫該 gadget，然後以具有攻擊者控制記憶體配置的不同物件 `ObjI` 呼叫它。CPU 隨即推測性地執行該分支，從 `obj.ptr[0]` 讀取資料，儘管該物件實際上是不同類型。為洩漏單一位元，我們遮蔽出一個位元位，並用其選擇 `probeArray` 中的兩條快取行之一。該快取行是否被快取，即編碼了該位元的值。

利用堆積洩漏 gadget，我們對應相鄰物件並定位一個攻擊者控制的陣列。第二個 gadget 混淆兩個跨越多條快取行的大型物件，使型別欄位落在與被讀取欄位不同的快取行上。驅逐型別欄位可打開推測視窗，同時目標欄位保持快取狀態，瞬態讀取隨即跟隨攻擊者控制的 64 位元值，從而將洩漏轉化為任意位址讀取。該技術的更詳細描述可參見論文原文。

**本機示範：洩漏任意 64 位元位址。**

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9vf28vPy9vb2+vn59vb27u7u////////9/f38/Pz9vb2+vr69/f37+/v////////+fn59PT19/f4+/v7+fn58fHx////////+/v79/f3+vr6/v7++/z79PT0////////////+/r7/v7+////////9/f3/////////////v7+////////////+/v7/////////////////////////////f39/////////////////////////////v7+)![BLOG-3371 4.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYVFV4YVB03F4Y2GE0N8.png&w=715&h=715&f=webp&fit=cover&position=center)

推測型別混淆 gadget 記憶體配置示意圖。精心構造的偽造 typed-array 標頭使瞬態讀取跟隨攻擊者選定的指標

### **訊號放大**

快取命中與快取未命中之間僅相差數奈秒，而遠端計時器的噪音量級則在數微秒至數毫秒之間。因此，需要某種形式的訊號放大才能區分快取命中與未命中。Stephen Röttger 和 Artur Janc 發現了一種[ _放大單次記憶體存取_](https://security.googleblog.com/2021/03/a-spectre-proof-of-concept-for-spectre.html)的方法，其原理是利用 L1 快取中基於樹狀結構的偽最近最少使用（PLRU）快取替換策略。基於樹狀結構的 PLRU 將每個快取組織為一棵二元樹，樹節點指向最近最少使用的一側，CPU 透過沿指標方向驅逐資料。利用特定的存取模式，攻擊者可以在指標轉向目標時持續觸及其樹鄰居，從而使目標快取行無限期保持快取狀態。這一思路頗為精巧：借助該行為，單次快取事件的時序差異可被任意放大——與反向情形（大量 L1 未命中）相比，正向情形將產生大量 L1 命中（存取更快）。

下圖展示了記憶體位址 X 是否處於快取狀態的兩種情況。若未快取，該存取模式將產生大量快取命中；若已快取，它占據樹中的一個節點，導致四條快取行競爭三個節點，從而引發大量 L1 未命中。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA8O/w7Ozr5uXj4uHf5OPi5uTl4uDh29nY9PP38fDy7Ovp6enl6urp6+rs6Obo4d/e+/r/+ff79PTy8vLu8vPy8/P27+7x6ufn/////////f37+/v3/P38/Pz/+fj78/Hx////////////////////////////+/r5////////////////////////////////////////////////////////////////////////////////////////////////)![BLOG-3371 5.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYH1JF2CTZE4EHYCH0K9.png&w=715&h=299&f=webp&fit=cover&position=center)

用於放大單次快取事件（命中/未命中）的 PLRU 存取模式示意圖。

### **遠端計時器**

只要訊號能夠被放大，嘈雜的遠端計時器便足以區分編碼的位元。例如，連接到提供高精度時間戳記的外部伺服器的 WebSocket 連線即可滿足需求。該計時器可託管於 Cloudflare，或部署於與執行 Worker 的目標資料中心共同部署的資料中心。Worker 請求遠端計時器為某一事件標記時間戳記，並在事件結束後計算另一請求的時間差。

在論文中，我們評估了多種不同的計時器設定，即便在較大的拓撲距離下，僅憑少量樣本便能穩定地實現中位數亞毫秒級精度。下圖展示了使用基於樹狀結構的 PLRU 放大後的快取事件。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////Pv98fDy6+rs7+7w9fT18/Ly7Orq////////9vX38vDy9vX2+/r7+fj48fDv/////////Pv9+Pf5/Pv9/////v399vX0//////////7/+/r8//7/////////+Pf3/////////v3/+vn7/v3///////7+9/b1////////+fj79vX3+vn6/v3+/Pv69PPy/////v3/9fT28fDy9fT1+vn59/b28O7t/////Pv98/L07+7w8/Lz+Pf39fT07u3s)![BLOG-3371 6.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYD0RQPYBADGE8CXEVZ5.png&w=715&h=457&f=webp&fit=cover&position=center)

50 次放大快取命中（實線）與快取未命中（虛線）計時測量的核密度估計圖。上：網路計時器，因抖動存在重疊；下：真實值，顯示清晰分離。豎線標記各自中位數。

### **可重複測量**

單次測量不足以可靠地區分時序編碼資料。生產機器噪音較大，因此攻擊者需要對每次測量至少重複若干次，並使用某種統計判別器。在我們的方案中，重複測量意味著每輪重設快取狀態。每輪開始前需驅逐兩類資料：推測分支所依賴的值必須被驅逐，使分支解析停滯足夠長的時間以打開推測視窗；編碼洩漏位元的探測快取行也必須被驅逐，以便下一次瞬態存取能夠重新將其快取。

由於 JavaScript 中沒有直接可用的驅逐指令，經典方法是建構驅逐集（eviction set）——一組對應至與目標相同快取組的位址集合。以正確的模式存取這些位址可將目標從快取中驅逐。Stephen Röttger 和 Artur Janc 在其攻擊中使用驅逐清單，可靠地將資料至少驅逐至 L2 快取。這種方法有效，但代價較高：建構精確的驅逐集需要大量時序測量，而我們的計時器是一個嘈雜的遠端計時器。此前針對 Workers 的遠端攻擊繞過了這一搜尋過程，改為在每輪中遍歷一個大於 L1 和 L2 快取之和的陣列——這是一種可行方案，但速度更慢。

Dougall Johnson 在其關於[ _可攜式 JavaScript Spectre 利用_](https://dougallj.wordpress.com/2021/03/16/another-approach-to-portable-javascript-spectre-exploitation/)的精彩部落格文章中介紹了一種更優雅的方式，其思路直接源自鴿巢原理。若分配的資料量遠超快取容量，隨機選取的快取行幾乎可以確定不在快取中。對於 256 KB 的 L2 快取，分配 64 MB 資料後，隨機快取行仍處於 L2 快取的機率最多為 1/256。因此，無需驅逐特定快取行，只需選取一個以壓倒性機率已被驅逐的全新隨機位置即可。頻繁循環遍歷該物件陣列的副作用是會產生自動驅逐效果。

為在 JavaScript 中利用這一特性，我們分配了一個超過末級快取容量的攻擊者-受害者物件對大型集區。每輪測量選取一個全新的隨機配對，因此，該物件的 map 指標（即推測型別檢查所讀取的隱藏類別描述符）幾乎可以肯定已經被逐出快取。

### **實現攻擊者與受害者隔離區的共同部署**

要使攻擊奏效，攻擊者與受害者的隔離區必須被排程至同一邊緣伺服器的同一處理序中。直覺上，這似乎並不容易——畢竟 Cloudflare 營運著數以萬計的邊緣伺服器。然而在 Cloudflare Workers 上，實現共同部署實際上相當簡單。由於 Cloudflare Workers 被設計為可在任意 Cloudflare 邊緣伺服器上執行，在攻擊者指令碼中透過 `fetch("https://victim.example")` 呼叫受害者指令碼，在大多數情況下會促使排程器在完全相同的處理序中啟動受害者 Worker 的執行個體。透過以固定時間間隔持續向受害者發起子請求，可使受害者隔離區持續存活。

此外，由於攻擊穩定性在很大程度上取決於執行 Worker 指令碼的邊緣伺服器的 CPU 負載，攻擊者可以策略性地選擇在離峰時段的資料中心（colo）發動攻擊（例如在歐洲工作時間選擇澳大利亞的資料中心），此時流量水準相對較低。

### **突破隔離區資源限制**

Cloudflare Workers 執行階段對所有隔離區[ _強制執行一組限制_](https://developers.cloudflare.com/workers/platform/limits/)，以保護平台並防止濫用。就本次攻擊而言，相關限制為每次呼叫 30 秒 CPU 時間和 1,000 次子請求。這些限制後來有所[ _提升_](https://developers.cloudflare.com/workers/platform/limits/#account-plan-limits)，但以下原則仍然適用。

對於一般 Worker，每個 HTTP 請求（即 fetch 事件）都是一次新呼叫，會重設上述限制。難點在於如何讓連續請求落在同一邊緣伺服器上——負載平衡和網路狀況的變化使這一點難以保證。Durable Objects 為我們解決了這一問題。

[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/) 專為用戶端間的即時協調而建構，執行階段將每條傳入的 WebSocket 訊息視為一次新呼叫並重設 CPU 時間和請求限制。攻擊者向一個 Durable Object Worker 建立持久 WebSocket 連線，並定期傳送保活訊息。這使單一隔離區持續存活，並為我們提供了一個持久的雙向頻道來執行攻擊。

其中有一個細節耗費了我們不少時間。由於隔離區是單執行緒的，傳入的 WebSocket 訊息只有在指令碼將控制權交還給事件迴圈時才會被處理。在同步程式碼執行期間，執行階段不會感知到保活訊息，因此不會重設 CPU 時間。若執行緒持續封鎖超過 30 秒，執行階段將終止隔離區。這為單次同步執行突發中的放大量設定了上限。在各次突發之間定期讓出控制權，使我們能夠將隔離區保持存活長達 5 小時至 20 餘小時。

### **綜合運用**

此前的攻擊主要依靠重複次數來放大單次快取存取，因此洩漏速率較低，約為 120 bit/h。我們將基於樹狀結構的 PLRU 放大機制與測量迴圈相結合：每次迭代重建快取狀態，從而累積更大的時序差異。即便某次迭代中中斷破壞了快取狀態，後續迭代也能將其抵消。這使訊號強度足以透過遠端 WebSocket 計時器對位元進行分類。總體思路如下：
    
    
    for (let s = 0; s < SAMPLE_NUM; s++) {
      timer.mark("mark S" + s);
      for (let r = 0; r < OUTER_REP_NUM; r++) {
        setup();                   // branch mistraining and cache control
        leak(secretBit);           // transient access
        PLRU(cacheSet, INNER_REP); // amplify
      }
      timer.mark("mark E" + s);
    }
    
    delta = fetchFromServer(SAMPLE_NUM);
    return median(delta);

我們在 Cloudflare Workers 生產環境中，針對我們自己控制的 Worker，完整示範了端到端攻擊。我們首先從攻擊者 Worker 洩漏記憶體，繼而從一個共同部署的受害者 Worker（我們事先在其中放置了機密資料）中洩漏資料。

第一步，在攻擊者 Worker、我們擁有的受害者 Worker 和遠端計時器之間建立共同部署關係。Durable Objects 為我們提供了長期執行環境，WebSocket 訊息提供了可重複的時序來源，`/cdn-cgi/trace` 端點透過查看 _fl_ 欄位幫助我們確認機器部署位置。

第二步，增加校準步驟，以推測可達的值探測計時器。這一步驟至關重要，因為生產機器噪音較大。逐次呼叫的校準使我們能夠根據 0 分布和 1 分布之間的相對差異對位元進行分類，最終應產生兩個可清晰區分的分布。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA8Pn76Ors0sTJuqm2sLPGus7gzdzp3dzh/f//9/j55tzf1MfQzM3Y0d/p3urw6urs////////+vP17eTp5ubq6PHz7/j49/j2////////////+/X39vb29/z6+v/9/v/8/////////////Pj6+fn5+//8/f/9/f/7/////////fv89PHz8/T19/z7+f379vf1////////8/Hz6Obp6uzv8fb48/f37+7u////////7uzu4+Hl5ejs7fP28PT26+vr)![BLOG-3371 7.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZ90GQ2H0H3WEJBQWGRH.png&w=715&h=387&f=webp&fit=cover&position=center)

第一階段，我們從一個 Worker 洩漏了隔離區根位址；在另一個 Worker 中，我們使用基於 64 位元指標的推測型別混淆，從該根位址處讀取資料。 

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAUk5OT0pDR0AsPzgsOTlINTtaMDdXKSxDTUg7S0QzRTshPzQgOjU1NjZBLzA9JiMpS0QkSUAhRTkZQTQWPzQZOzQZMy0LJx4AT0gkTkUkSj4jSDsgRzwaRDwNPTYAMigAWlRBWFE+VEs4Ukg3UUs8UEw+SkY4QjwrZ2JdZF9WX1hKW1ZLW1lZWltjV1dfUE5PcGxvbWlnZ2JXYl9YYmNsYmZ6X2N3W1pkdHB2cW1tamZbZWNdZGZyZWqCYmd/Xl9r)![BLOG-3371 8.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZB18F736T5D947HE7MH.png&w=715&h=314&f=webp&fit=cover&position=center)

作為中間驗證步驟，我們透過讀取 vDSO 區域的記憶體確認了第二個 gadget 的 64 位元洩漏能力。vDSO 是一個便於驗證的目標，因為其中包含 `gettimeofday` 等人類可讀字串。 

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAUEcvTkYwSkMwRkEuRD8rRD8nRD4mQz4oVEs1Ukk1TUc1SUQyR0IuRkAqRT8oQz0oV046VU05UEk4S0Y1SUMwR0ErRT8oQjwmWU87Vk46UUk4S0UzSEEuRj8oQzwkQDkiV003VUs2TkYzSEAtRD0mQjogQDcbPDQZVEkwUUYuSkApQjkhPjUYPTIPOjAJNy0JUEQnTUElRToePTISOC0ANysANikAMycAT0IjTD8gQzcYOi8HNioANSgANCYAMSQA)![BLOG-3371 9.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYNA1R7KHD1CH00PM79K.png&w=715&h=243&f=webp&fit=cover&position=center)

**示範影片：從 JavaScript 堆積洩漏資料**

最終，我們在受害者 Worker 中放置了一個 JWT 權杖，並逐位元洩漏。第一個位元組為字元「e」，二進位表示為 0b01100101。下圖展示了該位元組的逐位元分類結果。分類過程使用雙側檢定同時測試兩種結果，並透過多數決和基於百分位的閾值推斷位元值。在生產環境中，我們實現了最高 12 bit/s 的洩漏速率，準確率超過 99%。請注意，若以犧牲準確率為代價，則可達成更高的洩漏速率。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+/Pz57+7v6Ojr7e3u8/T08vPy6urq///////+8/P17e3x8vL1+Pj59vb27e3t////////+Pf78vL39/f7/f3++vr67+/x////////+/v/9vb7+/v//////f398vLz/////////Pz/9vf7+/v//////f3+8/P0////////+vv99fX5+fn8//7//fz89PT0////////+fn68vP19vb4/Pz8+/v69PT0////////+Pj58fH09fX2+/v6+/r59PT0)![BLOG-3371 10.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYQR705ERGSYCX6WAN2W.png&w=715&h=1031&f=webp&fit=cover&position=center)

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vv9+fb47+zu6ejp7Ovs8O/w7ezt5OXk//////3+9fT18PDw8vL09fb58/T26+3t/////////fz79/f3+Pr9+/7/+fz/8vb1///////////++/v7/P7//v///P//9vn5///////////9+vr5+/3//////P//9Pf3////////+/r59fTz+Pj6/P3/+fr97vDw////////9vT07+7s9PLz+vj79fT36Ojp////////9PLy7evq8vDw+fb48/L05eXm)![BLOG-3371 11.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZAYKH16KKVQNSEYH7JX.png&w=715&h=397&f=webp&fit=cover&position=center)

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAQkIvQEEvPD0vNjgrLzAhJiYPGBgAAAMANDEbMC4ZKCYUHxwGGRQAFQ0ACQAAAAAAKR8AIxgAEwAAAAAAAAAABwAACAAAAAAANysCMyYAKhoAIgsAIAUAIwgAIQUAHAAAU0krUUcrTkQrSj8mRjkbQTMFOysANSMAbGRFbGRIbGNLaWBKYllBWU4yT0IiSDkYfnVWfnZZf3defHVddWxUaV9EXVA0U0YphHxbhX1fhn5kg3xke3Nbb2RKYVU5WEou)![BLOG-3371 12.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYH6CEXJ9WFY642FH4X9.png&w=715&h=74&f=webp&fit=cover&position=center)

逐位元分類結果圖及完整洩漏權杖截圖

### **強健性**

隨著一天中時段的不同，機器使用率會顯著上升，進而拖慢攻擊速度——因為需要採樣更多資料。然而即便在 CPU 使用率較高的情況下，攻擊依然可行。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+vr29vby7e3q5ubk5OTj5eXl5eXl4uLj/f36+vr38vLw7Ozr6urs6uru6Ojs5eXo///////9+fn39PT08vL28PD47e316enu/////////v7++fn79/f99vb/8/P87+/1////////////+vr/+fn/+/v/+fn/9PT7////////////+Pj/+fn//v7//v7/+fn+////////////9vb/9/f//////////Pz/////////////9PT/9/f//////////f3/)![BLOG-3371 13.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYB97RCM22C4N1CB9TJT.png&w=715&h=240&f=webp&fit=cover&position=center)

## **為何未被偵測到？**

DyPrIs 監測硬體效能計數器，一旦指令碼行為疑似 Spectre 攻擊，便將其隔離至獨立處理序。以下兩點使本次攻擊得以躲避偵測。

其一，DyPrIs 僅在指令碼呼叫結束後才會觸發隔離，而我們在攻擊中使用的 Durable Object 保活技巧可持續執行數小時乃至一天。WebSocket 保活訊息使單次呼叫持續開放數小時，洩漏早在隔離機制介入之前便已完成。

其二，DyPrIs 透過 iTLB 存取次數對分支預測錯誤進行正規化處理。我們的遠端計時器是一個大型 I/O 迴圈，WebSocket 流量會顯著增加 iTLB 活動量。正規化後的比率降至偵測閾值以下，使該攻擊看起來與普通的 I/O 密集型 Worker 無異。

## **我們的改進措施**

我們重點從三個方面持續推進改進：V8 深度強化、提供更強的處理序內隔離，以及改進偵測機制。

### **V8 Sandbox**

V8 記憶體沙箱的最終目標是從 JavaScript 堆積的大部分區域移除原始 64 位元指標，從而降低眾多記憶體損毀原語的利用價值。這也使本研究中特定推測型別混淆 gadget 的重用難度大幅提升，因為 typed-array 後備儲存體不再暴露相同的原始指標結構。

V8 Sandbox 並非針對 Spectre 的完整緩解方案。儘管文中所述的 64 位元洩漏 gadget 不再適用，但仍可能存在其他 Spectre 變體或 gadget 可被利用，以實現任意越界記憶體存取。

### **硬體輔助處理序內隔離**

2025 年 9 月，我們為 Workers 部署了基於記憶體保護金鑰（Memory Protection Keys，MPK）的[ _處理序內隔離_](https://blog.cloudflare.com/safe-in-the-sandbox-security-hardening-for-cloudflare-workers/)機制。MPK 允許處理序將記憶體劃分為保護網域，並以低成本切換存取權限。Workers 利用該機制保護每個堆積，防止其被同一處理序內的其他隔離區存取。

這從根本上改變了 Spectre 的風險模型。每個隔離區的堆積現在受到硬體強制存取邊界的保護：對受錯誤金鑰保護的頁面的記憶體存取，將在硬體層面被拒絕。這阻斷了本研究所依賴的直接跨隔離區堆積讀取路徑。

然而，MPK 並非緩解 Spectre 的完整答案，但它嚴格收窄了洩漏面。其限制包括：硬體網域數量有限，以及需要謹慎管理保護金鑰狀態。

### **改進 DyPrIs**

我們改進了 DyPrIs，將長期執行和 I/O 密集型工作負載作為一類安全問題來處理。偵測不能僅在指令碼結束後才觸發。Durable Object 或 WebSocket 密集型 Worker 可能執行時間很長，以至於執行後隔離機制介入時為時已晚。

我們目前正在研究是否可將遠端時序行為作為 DyPrIs 的額外偵測維度。儘管我們無法阻斷與攻擊者控制基礎架構的遠端通訊，但時序資料揭示了極具特徵性的資料外洩位元模式。更好的做法是將計算密集型程式碼段周圍重複出現的類計時器 I/O 納入行為訊號，而非將其視為背景雜訊。

## **致謝**

特別感謝愛丁堡大學的 Haocheng Xiao 及其指導教授 Sam Ainsworth 和 Nigel Topham，感謝他們在提升 JavaScript 中 Spectre 攻擊可靠性方面所作的貢獻。

## **參與邀請**

我們始終歡迎透過我們的[ _漏洞賞金計畫_](https://hackerone.com/cloudflare)提交高品質報告。執行階段層的記憶體安全漏洞是高價值目標。您可以在 GitHub 上找到 [_workerd 的 Fuzzilli 整合_](https://github.com/cloudflare/workerd/pull/4917)及 [_workerd 原始碼_](https://github.com/cloudflare/workerd)。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frevisiting-spectre-attacks-on-workers%2F&t=%E9%87%8D%E6%96%B0%E5%AF%A9%E8%A6%96%E9%87%9D%E5%B0%8D%20Cloudflare%20Workers%20%E7%9A%84%E9%81%A0%E7%AB%AF%20Spectre%20%E6%94%BB%E6%93%8A)[](https://x.com/intent/post?text=%E9%87%8D%E6%96%B0%E5%AF%A9%E8%A6%96%E9%87%9D%E5%B0%8D+Cloudflare+Workers+%E7%9A%84%E9%81%A0%E7%AB%AF+Spectre+%E6%94%BB%E6%93%8A&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frevisiting-spectre-attacks-on-workers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frevisiting-spectre-attacks-on-workers%2F)[](https://bsky.app/intent/compose?text=%E9%87%8D%E6%96%B0%E5%AF%A9%E8%A6%96%E9%87%9D%E5%B0%8D+Cloudflare+Workers+%E7%9A%84%E9%81%A0%E7%AB%AF+Spectre+%E6%94%BB%E6%93%8A+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frevisiting-spectre-attacks-on-workers%2F)[](https://mastodonshare.com/?text=%E9%87%8D%E6%96%B0%E5%AF%A9%E8%A6%96%E9%87%9D%E5%B0%8D+Cloudflare+Workers+%E7%9A%84%E9%81%A0%E7%AB%AF+Spectre+%E6%94%BB%E6%93%8A&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frevisiting-spectre-attacks-on-workers%2F)[](https://www.threads.net/intent/post?text=%E9%87%8D%E6%96%B0%E5%AF%A9%E8%A6%96%E9%87%9D%E5%B0%8D+Cloudflare+Workers+%E7%9A%84%E9%81%A0%E7%AB%AF+Spectre+%E6%94%BB%E6%93%8A+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frevisiting-spectre-attacks-on-workers%2F)

## 相關標籤

[Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)[攻擊](https://blog.cloudflare.com/zh-tw/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-tw/tag/vulnerabilities/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Martin Schwarzl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q44FVCNYF3AKGF6DGP9G.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Martin Schwarzl](https://blog.cloudflare.com/zh-tw/author/martin/)

[](https://martinschwarzl.at)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
