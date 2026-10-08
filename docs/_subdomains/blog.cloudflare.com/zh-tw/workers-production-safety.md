---
url: https://blog.cloudflare.com/zh-tw/workers-production-safety/
title: \u7528\u65bc\u5be6\u73fe\u751f\u7522\u5b89\u5168\u7684\u65b0\u5de5\u5177\uff1aGradual Deployments\u3001\u4f86\u6e90\u5c0d\u61c9\u3001\u9650\u901f\u548c\u65b0 SDK | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:27.606748+00:00
---

# 用於實現生產安全的新工具：Gradual Deployments、來源對應、限速和新 SDK | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/workers-production-safety/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)[Observability](https://blog.cloudflare.com/zh-tw/tag/observability/)+2顯示另外 2 個標籤

5 標籤顯示 5 個標籤

  * 文章標籤
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)[SDK](https://blog.cloudflare.com/zh-tw/tag/sdk/)
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



[Rate Limiting](https://blog.cloudflare.com/zh-tw/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/zh-tw/tag/sdk/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)[Observability](https://blog.cloudflare.com/zh-tw/tag/observability/)[Rate Limiting](https://blog.cloudflare.com/zh-tw/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/zh-tw/tag/sdk/)

2024年4月4日

# 用於實現生產安全的新工具：Gradual Deployments、來源對應、限速和新 SDK

![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanushree Sharma](https://blog.cloudflare.com/zh-tw/author/tanushree/)和[Jacob Bednarz](https://blog.cloudflare.com/zh-tw/author/jacob-bednarz/)

閱讀時間：11 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/workers-production-safety/)、[Deutsch](https://blog.cloudflare.com/de-de/workers-production-safety/)、[Español](https://blog.cloudflare.com/es-es/workers-production-safety/)、[Français](https://blog.cloudflare.com/fr-fr/workers-production-safety/)、[日本語](https://blog.cloudflare.com/ja-jp/workers-production-safety/)、[한국어](https://blog.cloudflare.com/ko-kr/workers-production-safety/)和[简体中文](https://blog.cloudflare.com/zh-cn/workers-production-safety/).

![New tools for production safety — Gradual deployments, Source maps, Rate Limiting, and new SDKs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FR4MNGHSCH0P7DD7P68W.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+//769vXz8fDw8vHx9PLy8u7u6+fl/////vz98vT16+7y6+7z7u/17ezw5+Tm/////f3/8PP55u315ez36O356Orz5OPq////////8vb+5/D65e/85+/+6Oz55Obv////////+f3/7/f/7Pb/7fb/7fL/6uz2////////////+///+P7/9/7/9fr/8vT8/////////////////////////P//+Pv/////////////////////////////+/3/)

2024 年 Developer Week 的重點在於生產就緒。4 月 1 日（星期一），我們[宣布](https://blog.cloudflare.com/zh-tw/making-full-stack-easier-d1-ga-hyperdrive-queues-zh-tw/) [D1](https://developers.cloudflare.com/d1/)、[Queues](https://developers.cloudflare.com/queues/)、[Hyperdrive](https://developers.cloudflare.com/hyperdrive/) 和 [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) 已準備好進入生產規模且正式上市。4 月 2 日（星期二），我們[宣布](https://blog.cloudflare.com/zh-tw/workers-ai-ga-huggingface-loras-python-support-zh-tw/)我們的推理平台 [Workers AI](https://developers.cloudflare.com/workers-ai/) 已正式上市。但我們並不會止步於此。

不過，生產就緒不僅僅是關於您構建時所使用的服務的規模和可靠性。您還需要工具來安全可靠地進行變更。您不僅依賴 Cloudflare 提供的功能，還依賴其根據應用程式需求精確控制和自訂 Cloudflare 行為方式的能力。

今天，我們宣布了五項更新，為您提供更強功能：Gradual Deployments、Tail Workers 中的來源對應堆疊追蹤、新的限速 API、全新的 API SDK 以及 Durable Objects 的更新，每一項更新的構建都將任務關鍵型生產服務納入了考量。我們使用 Workers 建立自己的產品，包括 [Access](https://developers.cloudflare.com/cloudflare-one/policies/access/)、[R2](https://developers.cloudflare.com/r2/)、[KV](https://developers.cloudflare.com/kv/)、[Waiting Room](https://developers.cloudflare.com/waiting-room/)、[Vectorize](https://developers.cloudflare.com/vectorize/)、[Queues](https://developers.cloudflare.com/queues/)、[Stream](https://developers.cloudflare.com/stream/) 等。我們依靠每一項新功能來確保我們已做好生產準備，現在我們很高興將它們帶給每個人。

### 對 Workers 和 Durable Objects 逐步部署變更

部署 Worker 幾乎瞬時就可完成——只需幾秒鐘，您的變更就會[無處不在](https://www.cloudflare.com/network/)。

當您達到生產規模時，您所做的每項變更都會帶來更大的風險，無論是在數量還是預期方面。您需要滿足 99.99% 的可用性 SLA，或擁有雄心勃勃的 P90 延遲 SLO。一個糟糕的部署如果針對全部流量持續 45 秒，可能意味著數以百萬計的請求失敗。如果一次全部推出，一個細微的程式碼變更可能會導致對不堪重負的後端進行大量的重試。這些都是我們針對自己基於 Workers 的服務所需要考量並緩解的風險。

減輕這些風險的方法是逐步部署變更——通常稱為滾動部署：

  1. 您的應用程式的當前版本在生產環境中執行。
  2. 您將應用程式的新版本部署到生產環境，但僅將一小部分流量路由到這個新版本，並等待它「浸泡」在生產環境中，監視遞歸和漏洞。如果發生不良情況，您可以在一小部分（例如 1%）流量中儘早發現並可以快速復原。
  3. 您逐漸增加流量百分比，直到新版本接收 100% 的流量，此時它已完全推出。



今天，我們開放了一個一流的方法，透過 [Cloudflare API](https://developers.cloudflare.com/api/operations/worker-deployments-list-deployments)、[Wrangler CLI](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-wrangler) 或 [Workers 儀表板](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-the-cloudflare-dashboard)將程式碼變更逐漸部署到 Workers 和 Durable Objects。Gradual Deployments 正在進入公開測試階段，您可以將 Gradual Deployments 與 [Workers Free 方案](https://developers.cloudflare.com/workers/platform/pricing/#workers)中的任何 Cloudflare 帳戶一起使用，而在不久之後，您將可以開始將 Gradual Deployments 與 [Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/#workers) 和企業方案中的 Cloudflare 帳戶一起使用。一旦您的帳戶具有存取權限，您就會在 Workers 儀表板上看到橫幅。

當 Worker 或 Durable Object 有兩個版本在生產中同時執行時，您肯定會希望能夠按版本篩選指標、異常和記錄。將新版本僅推出到一小部分流量，可以幫助您及早發現生產問題，或在按 50/50 分配流量時比較效能指標。我們還在我們的平台上新增了版本層級的可觀察性：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Splitting traffic between different versions of a Worker.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4792EFMEWR5SFVJAMDC49A.png&w=715&h=353&f=webp&fit=cover&position=center)

  * 您可以在 Workers 儀表板中以及透過 [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) 按版本篩選分析。
  * [Workers Trace Events](https://developers.cloudflare.com/workers/observability/logging/logpush/) 和 [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/) 事件包含 Worker 的版本 ID，以及可選的版本訊息和版本標記欄位。
  * 使用 [Wrangler tail](https://developers.cloudflare.com/workers/wrangler/commands/#tail) 檢視即時記錄時，可以檢視特定版本的記錄。
  * 您可以透過設定[版本中繼資料綁定](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/)，從 Worker 程式碼中存取版本 ID、訊息和標籤。



您可能還想確保每個用戶端或使用者始終看到您的 Worker 的同一個版本。我們新增了 [Version Affinity](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity)，以便與特定識別碼（例如使用者、工作階段或任何唯一 ID）關聯的請求始終由同一版本的 Worker 處理。當 [Session Affinity](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity) 與[規則集引擎](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#setting-cloudflare-workers-version-key-using-ruleset-engine)一起使用時，可讓您完全控制用於確保「黏性」的機制和識別碼。

Gradual Deployments 正在進入公開測試階段。隨著我們邁向正式版，我們正在加倍努力，以支援：

  * **版本覆寫。**叫用特定版本的 Worker，以便在其提供任何生產流量之前進行測試。這將允許您建立藍綠部署 (Blue-Green Deployments)。
  * **Cloudflare Pages。**讓 Cloudflare Pages 中的 CI/CD 系統自動代表您進行部署。
  * **自動復原。**當新版 Worker 錯誤率激增時，自動復原部署。



我們期待聽到您的意見反應！請透過[此](https://www.cloudflare.com/lp/developer-week-deployments/)意見反應表單告訴我們您的想法，或透過 #workers-gradual-deployments-beta 頻道中的[開發人員 Discord](https://discord.gg/HJvPcPcN) 聯絡我們。

### Tail Workers 中的來源對應堆疊追蹤

生產就緒意味著追蹤錯誤和異常，並努力將其減少到零。發生錯誤時，最先需要查看的就是錯誤的[堆疊追蹤](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack)——呼叫的具體函數、呼叫順序、來自哪行和檔案以及使用哪些引數。

大多數 JavaScript 程式碼（不管是在 Workers 上，還是其他各個平台上）首先會被捆綁，通常會被轉譯，然後在部署到生產環境之前進行縮製。這是在幕後完成的，目的是建立更小的套件以最佳化效能，並在需要時從 Typescript 轉換為 Javascript。

如果您曾經看到過異常傳回堆疊追蹤，例如：/src/index.js:1:342，這表示錯誤發生在函數縮製程式碼的第 342 個字元上。這對於偵錯顯然沒有多大幫助。

[來源對應](https://web.dev/articles/source-maps)解決了這個問題，它們將編譯和縮製程式碼對應回您編寫的原始程式碼。來源對應與 JavaScript 執行階段傳回的堆疊追蹤相結合，為您提供人類可讀的堆疊追蹤。例如，以下堆疊追蹤顯示 Worker 在 down.ts 檔案的第 30 行收到意外的空值。這是一個有用的偵錯起點，您可以向下移動堆疊追蹤，以瞭解被設定為產生空值的所呼叫函數。

其運作方式如下：
    
    
    Unexpected input value: null
      at parseBytes (src/down.ts:30:8)
      at down_default (src/down.ts:10:19)
      at Object.fetch (src/index.ts:11:12)

  1. 當您在 [wrangler.toml](https://developers.cloudflare.com/workers/wrangler/configuration/) 中設定 upload_source_maps = true 時，Wrangler 會在您執行 [wrangler deploy](https://developers.cloudflare.com/workers/wrangler/commands/#deploy) 或 [wrangler versions upload](https://developers.cloudflare.com/workers/wrangler/commands/#versions) 時自動產生並上傳任何來源對應檔案。
  2. 當您的 Worker 拋出未擷取的異常時，我們會擷取來源對應，並使用它將異常的堆疊追蹤對應回 Worker 的原始來源程式碼行。
  3. 然後，您可以在[即時記錄](https://developers.cloudflare.com/workers/observability/logging/real-time-logs/)或 [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/) 中檢視這個反混淆的堆疊追蹤。



從今天開始，在公開測試版中，您可以在部署 Worker 時將來源對應上傳到 Cloudflare。[請閱讀文件以開始使用](https://developers.cloudflare.com/workers/observability/source-maps)。從 4 月 15 日開始，Workers 執行階段將開始使用來源對應來反混淆堆疊追蹤。當來源對應堆疊追蹤可用時，我們將在 Cloudflare 儀表板中發布通知，並在我們的 [Cloudflare Developers X 帳戶](https://twitter.com/CloudflareDev?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)上發布通知。

### Workers 中的新限速 API

API 僅在具有合理的[速率限制](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)時才可用於生產。隨著您的成長，您需要執行的限制的複雜性和多樣性也會增加，以平衡特定客戶的需求、保護服務的健康狀況或在特定場景中執行和調整限制。Cloudflare 自己的 API 面臨著這項挑戰——我們數十種產品中的每一種產品（每種產品都有許多 API 端點）可能都需要強制執行不同的速率限制。

自 2017 年以來，您就可以在 Cloudflare 上設定[限速規則](https://developers.cloudflare.com/waf/rate-limiting-rules/)。但在今天之前，仍是只能在 Cloudflare 儀表板中或透過 Cloudflare API 控制此操作。無法在_執行階段_定義行為，也無法在 Worker 中編寫直接與速率限制互動的程式碼——您只能在請求到達 Worker 之前控制其是否受到速率限制。

今天，我們推出了一個新 API 的開放測試版，讓您可以從 Worker 直接存取速率限制。它速度快如閃電，由 memcached 提供支援，並且可以輕鬆新增到您的 Worker 中。例如，以下設定定義了 60 秒內 100 個請求的速率限制：

然後，在您的 Worker 中，您可以呼叫 RATE_LIMITER 綁定上的限制方法，並提供您選擇的鍵。對於上面的設定，一旦在 60 秒內對特定路徑發出超過 100 個請求，此程式碼將傳回 [HTTP 429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) 回應狀態碼：
    
    
    [[unsafe.bindings]]
    name = "RATE_LIMITER"
    type = "ratelimit"
    namespace_id = "1001" # An identifier unique to your Cloudflare account
    
    # Limit: the number of tokens allowed within a given period, in a single Cloudflare location
    # Period: the duration of the period, in seconds. Must be either 60 or 10
    simple = { limit = 100, period = 60 } 

現在，Workers 可以直接連接到像 memcached 這樣的資料存放區，我們還能提供什麼？計數器？鎖？[記憶體內快取](https://github.com/cloudflare/workerd/pull/1666)？限速是我們試圖在 Workers 中提供的許多基本元件中的第一個，它解決了我們多年來一直遇到的問題，即跨多個 Worker [隔離群](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates)的臨時共用狀態應該存在於哪裡。如果您現在依賴於將狀態放入 Worker 的全域範圍內，我們正在研究專為特定使用案例建置的更好的基元。
    
    
    export default {
      async fetch(request, env) {
        const { pathname } = new URL(request.url)
    
        const { success } = await env.RATE_LIMITER.limit({ key: pathname })
        if (!success) {
          return new Response(`429 Failure – rate limit exceeded for ${pathname}`, { status: 429 })
        }
    
        return new Response(`Success!`)
      }
    }

Workers 中的限速 API 處於公開測試階段，您可以透過[閱讀文件](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit)來開始使用。

### 為 Cloudflare API 自動產生的新 SDK

生產就緒意味著可以透過點擊儀表板中的按鈕進行變更，也可以使用 [Terraform](https://github.com/cloudflare/terraform-provider-cloudflare) 或 [Pulumi](https://github.com/pulumi/pulumi-cloudflare) 等基礎架構即程式碼方法，或直接發出 API 呼叫（自行或透過 SDK）的方法，以程式設計方式進行變更。

[Cloudflare API](https://developers.cloudflare.com/api/)規模龐大，並且不斷增加新功能——我們平均[每天要更新 API 架構 20 到 30 次](https://github.com/cloudflare/api-schemas/activity)。但迄今為止，我們的 API SDK 都是手動建置和維護的，因此我們迫切需要將其自動化。

我們已經做到了這一點，今天我們宣布推出適用於 Cloudflare API 的新用戶端 SDK，支援三種語言（[Typescript](https://github.com/cloudflare/cloudflare-typescript)、[Python](https://github.com/cloudflare/cloudflare-python) 和 [Go](https://github.com/cloudflare/cloudflare-go)），並且即將推出更多語言。

每個 SDK 都是使用 [Stainless API](https://www.stainlessapi.com/) 自動產生的，基於定義每個 API 端點的結構和功能的 [OpenAPI 結構描述](https://github.com/cloudflare/api-schemas)。這意味著，當我們在任何 Cloudflare 產品中向 Cloudflare API 新增任何新功能時，這些 API SDK 都會自動重新產生並發布新版本，以確保它們正確且最新。

您可以透過執行以下命令之一來安裝 SDK：

如果您使用 Terraform 或 Pulumi，在底層，Cloudflare 的 Terraform Provider 目前使用現有的非自動化 [Go SDK](https://github.com/cloudflare/cloudflare-go)。當您執行 terraform apply 時，Cloudflare Terraform Provider 會決定以什麼順序進行哪個 API 呼叫，並使用 Go SDK 執行這些操作。
    
    
    // Typescript
    npm install cloudflare
    
    // Python
    pip install cloudflare
    
    // Go
    go get -u github.com/cloudflare/cloudflare-go/v2

利用自動產生的新 Go SDK，可以為所有 Cloudflare 產品提供更全面的 Terraform 支援，其提供了一組可以信賴的基本工具，這些工具恰到好處，且與最新的 API 變更保持同步。我們正在努力實現這樣一個未來：每當 Cloudflare 的產品團隊建立透過 Cloudflare API 提供的新功能時，SDK 都會自動支援它。預計 2024 年將有更多相關更新。

### Durable Object 命名空間分析和 WebSocket Hibernation 正式上市

我們自己的許多產品，包括 [Waiting Room](https://developers.cloudflare.com/waiting-room/)、[R2](https://developers.cloudflare.com/r2/) 和 [Queues](https://developers.cloudflare.com/queues/)，以及 [PartyKit](https://www.partykit.io/) 等平台，都是使用 [Durable Objects](https://developers.cloudflare.com/durable-objects/) 建構的。Durable Objects 在全球範圍內部署，且新增了對 Oceania 的支援，您可以將其視為可以提供單點協調和[持久狀態](https://developers.cloudflare.com/durable-objects/api/transactional-storage-api/)的單獨 Workers。它們非常適合需要即時使用者協調的應用程式，例如互動式聊天或協作編輯。Atlassian 對此的評價是：

>  _我們的一個新功能是_ _[Confluence 白板](https://www.atlassian.com/software/confluence/whiteboards)，它提供了一種自由方式來擷取非結構化工作，例如腦力激盪法和團隊正式記錄之前的早期規劃。團隊考慮了多種即時協作選項，最終決定使用 Cloudflare 的 Durable Objects。事實證明，Durable Objects 非常適合這個問題領域，它具有獨特的功能組合，使我們能夠大大簡化基礎架構並輕鬆擴展到大量使用者。-[Atlassian](https://www.atlassian.com/software/confluence/whiteboards)_

我們之前沒有在儀表板中公開相關的分析趨勢，因此很難理解 [Durable Objects 命名空間](https://developers.cloudflare.com/durable-objects/configuration/access-durable-object-from-a-worker/#generate-ids-randomly)中的使用模式和錯誤率，除非您直接使用 [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)。[Durable Objects 儀表板](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)現已改進，讓您可以深入瞭解指標，並根據需要進行更深度的鑽研。

從[第一天](https://blog.cloudflare.com/introducing-workers-durable-objects)起，Durable Objects 就支援 [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)，允許許多用戶端直接連接到 Durable Object 來傳送和接收訊息。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2305 Embedded Image - tUWMOW](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45NGJQ7SMHCNME7M5TATPN.png&w=715&h=557&f=webp&fit=cover&position=center)

然而，有時用戶端應用程式會開啟 WebSocket 連線，最後卻沒有執行任何操作。就好比您 5 個小時前在瀏覽器中開啟了一個索引標簽，卻並沒有使用過它。如果該用戶端使用 WebSocket 傳送和接收訊息，那麼它實際上擁有一個長期存在的 TCP 連線，該連線未用於任何用途。如果此連線指向一個 Durable Object，那麼該 Durable Object 必須保持執行，等待發生某些操作，在此過程中，這會消耗記憶體並花費您的金錢。

我們首先[引入了 WebSocket Hibernation](https://blog.cloudflare.com/workers-pricing-scale-to-zero) 來解決這個問題，今天，我們宣布該功能已經結束測試並正式上市。透過 WebSocket Hibernation，您可以設定在休眠時使用的自動回應，並序列化狀態，使其在休眠狀態下繼續存在。這可以為 Cloudflare 提供我們為維持來自用戶端的開啟 WebSocket 連線所需的輸入，同時「休眠」Durable Object，使其不主動執行，並且您無需為閒置時間付費。結果是，當您實際需要時，您的狀態始終在記憶體中可用，但在不需要時，也不會不必要地保留在記憶體中。只要您的 Durable Object 處於休眠狀態，即使仍有作用中用戶端透過 WebSocket 連接，也不會按持續時間向您收費。

此外，我們也聽取了開發人員關於向 Durable Objects 傳入 WebSocket 訊息的成本的意見反應，以便利於更小、更頻繁的即時通訊訊息。從今天開始，傳入的 WebSocket 訊息將按請求的 1/20 進行計費（而不是之前的 1 個訊息相當於 1 個請求）。以下是[定價範例](https://developers.cloudflare.com/durable-objects/platform/pricing/#example-4)：

.tg {border-collapse:collapse;border-color:#ccc;border-spacing:0;} .tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top} .tg .tg-4kyp{color:#0E101A;text-align:left;vertical-align:top} .tg .tg-bhdc{color:#0E101A;font-weight:bold;text-align:left;vertical-align:top}

| WebSocket Connection Requests | Incoming WebSocket Messages | Billed Requests | Request Billing  
---|---|---|---|---  
Before | 10K | 432M | 432,010,000 | $64.65  
After | 10K | 432M | 21,610,000 | $3.09  
  
WebSocket 連線請求

傳入的 WebSocket 訊息數

計費請求數

請求計費

之前

10K

432M

432,010,000

$64.65

之後

10K

432M

21,610,000

$3.09

### 生產就緒，沒有生產複雜性

在上一代雲端平台上做好生產準備意味著放慢發布速度。這意味著將許多互不相關的工具拼接在一起，或讓整個團隊在內部平台上工作。您必須將自己的生產力層遷移到無障礙的平台上。

Cloudflare 開發人員平台已經成熟，已準備好投入生產，並致力於成為一個整合式平台，產品可以直觀地協同工作，不需要 10 種方法來做同樣的事情，也不需要相容性矩陣來幫助瞭解哪些產品可以一起工作。這些更新中的每一個都展示了這一點，新功能在不同產品和不同的 Cloudflare 平台部分中進行了整合。

為此，我們不僅希望聽到您對未來產品的期待，也希望聽到您關於如何簡化產品的意見，或者您認為我們的產品可以在哪些方面更好地協同工作。如果您對我們有任何改進意見，請告訴我們，[Cloudflare 開發人員 Discord](https://discord.cloudflare.com/) 始終開放。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fworkers-production-safety%2F&t=%E7%94%A8%E6%96%BC%E5%AF%A6%E7%8F%BE%E7%94%9F%E7%94%A2%E5%AE%89%E5%85%A8%E7%9A%84%E6%96%B0%E5%B7%A5%E5%85%B7%EF%BC%9AGradual%20Deployments%E3%80%81%E4%BE%86%E6%BA%90%E5%B0%8D%E6%87%89%E3%80%81%E9%99%90%E9%80%9F%E5%92%8C%E6%96%B0%20SDK)[](https://x.com/intent/post?text=%E7%94%A8%E6%96%BC%E5%AF%A6%E7%8F%BE%E7%94%9F%E7%94%A2%E5%AE%89%E5%85%A8%E7%9A%84%E6%96%B0%E5%B7%A5%E5%85%B7%EF%BC%9AGradual+Deployments%E3%80%81%E4%BE%86%E6%BA%90%E5%B0%8D%E6%87%89%E3%80%81%E9%99%90%E9%80%9F%E5%92%8C%E6%96%B0+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fworkers-production-safety%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fworkers-production-safety%2F)[](https://bsky.app/intent/compose?text=%E7%94%A8%E6%96%BC%E5%AF%A6%E7%8F%BE%E7%94%9F%E7%94%A2%E5%AE%89%E5%85%A8%E7%9A%84%E6%96%B0%E5%B7%A5%E5%85%B7%EF%BC%9AGradual+Deployments%E3%80%81%E4%BE%86%E6%BA%90%E5%B0%8D%E6%87%89%E3%80%81%E9%99%90%E9%80%9F%E5%92%8C%E6%96%B0+SDK+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fworkers-production-safety%2F)[](https://mastodonshare.com/?text=%E7%94%A8%E6%96%BC%E5%AF%A6%E7%8F%BE%E7%94%9F%E7%94%A2%E5%AE%89%E5%85%A8%E7%9A%84%E6%96%B0%E5%B7%A5%E5%85%B7%EF%BC%9AGradual+Deployments%E3%80%81%E4%BE%86%E6%BA%90%E5%B0%8D%E6%87%89%E3%80%81%E9%99%90%E9%80%9F%E5%92%8C%E6%96%B0+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fworkers-production-safety%2F)[](https://www.threads.net/intent/post?text=%E7%94%A8%E6%96%BC%E5%AF%A6%E7%8F%BE%E7%94%9F%E7%94%A2%E5%AE%89%E5%85%A8%E7%9A%84%E6%96%B0%E5%B7%A5%E5%85%B7%EF%BC%9AGradual+Deployments%E3%80%81%E4%BE%86%E6%BA%90%E5%B0%8D%E6%87%89%E3%80%81%E9%99%90%E9%80%9F%E5%92%8C%E6%96%B0+SDK+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fworkers-production-safety%2F)

## 相關標籤

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)[Observability](https://blog.cloudflare.com/zh-tw/tag/observability/)[Rate Limiting](https://blog.cloudflare.com/zh-tw/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/zh-tw/tag/sdk/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Jacob Bednarz](https://blog.cloudflare.com/zh-tw/author/jacob-bednarz/)

[](https://jacobbednarz.com)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
