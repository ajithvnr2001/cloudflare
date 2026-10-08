---
url: https://blog.cloudflare.com/zh-tw/durable-object-facets-dynamic-workers/
title: Dynamic Workers \u4e2d\u7684 Durable Objects\uff1a\u70ba\u6bcf\u500b AI \u7522\u751f\u7684\u61c9\u7528\u7a0b\u5f0f\u63d0\u4f9b\u5176\u81ea\u5df1\u7684\u8cc7\u6599\u5eab | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:15.422334+00:00
---

# Dynamic Workers 中的 Durable Objects：為每個 AI 產生的應用程式提供其自己的資料庫 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/durable-object-facets-dynamic-workers/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Agents Week](https://blog.cloudflare.com/zh-tw/tag/agents-week/)[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)+3顯示另外 3 個標籤

6 標籤顯示 6 個標籤

  * 文章標籤
  * [Agents Week](https://blog.cloudflare.com/zh-tw/tag/agents-week/)[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[儲存](https://blog.cloudflare.com/zh-tw/tag/storage/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)
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



[儲存](https://blog.cloudflare.com/zh-tw/tag/storage/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

[Agents Week](https://blog.cloudflare.com/zh-tw/tag/agents-week/)[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[儲存](https://blog.cloudflare.com/zh-tw/tag/storage/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

2026年4月13日

# Dynamic Workers 中的 Durable Objects：為每個 AI 產生的應用程式提供其自己的資料庫

![Kenton Varda](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44DEXVTQSPFW8ZSKE70KPZ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kenton Varda](https://blog.cloudflare.com/zh-tw/author/kenton-varda/)

閱讀時間：5 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/durable-object-facets-dynamic-workers/)、[Deutsch](https://blog.cloudflare.com/de-de/durable-object-facets-dynamic-workers/)、[Español](https://blog.cloudflare.com/es-es/durable-object-facets-dynamic-workers/)、[Español (Latinoamérica)](https://blog.cloudflare.com/es-la/durable-object-facets-dynamic-workers/)、[Français](https://blog.cloudflare.com/fr-fr/durable-object-facets-dynamic-workers/)、[Italiano](https://blog.cloudflare.com/it-it/durable-object-facets-dynamic-workers/)、[日本語](https://blog.cloudflare.com/ja-jp/durable-object-facets-dynamic-workers/)、[한국어](https://blog.cloudflare.com/ko-kr/durable-object-facets-dynamic-workers/)、[简体中文](https://blog.cloudflare.com/zh-cn/durable-object-facets-dynamic-workers/)和[Nederlands](https://blog.cloudflare.com/nl-nl/durable-object-facets-dynamic-workers/).

![BLOG-3211 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CV5V84QNX5FKMPG3AE9N.png&w=2400&h=1350&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAAABcEQ9oS1Z+ZHGLZ3aLWGiDN1B7ADV5KgBPSz9pdHiRi5arjpuxfo2nY3KVRVeESxw+ZlZpj4+gp7DEqrfOmqjDf4uqZG2OVikyb1xml5ajsLfKs7/XorDMh5OwbXOQTh40ZlJfi4iXoqi7pbHIlqS/fIimYWiINQBBSjJXa2V8f4OXg42idoSdXWuMPUl4AABMDwBQNSdaSUpkT1lsRFdvIkBrAABmAABQAABNAABFFAlCIzJIFjhSABtaAABd)

幾週前，我們宣佈推出 [_Dynamic Workers_](https://blog.cloudflare.com/dynamic-workers/)，這是 Workers 平台的一項新功能，可讓您將 Worker 程式碼動態載入至安全的沙箱中。本質上，Dynamic Worker Loader API 提供對 Workers 一直以來作為基礎的基本運算隔離原語的直接存取：隔離，而非容器。隔離環境比容器要輕得多，因此能夠使用 1/10 的記憶體將載入速度提升 100 倍。它們非常高效，並且可視為「一次性產品」：啟動一個並執行幾行程式碼，然後將其丟棄。就像 eval() 的安全版本。 

Dynamic Workers 有多種用途。在最初的公告中，我們重點介紹了如何將其用於執行 AI 智慧體生成的程式碼，以替代工具呼叫。在此使用案例中，AI 智慧體可編寫並執行幾行程式碼，藉此依據使用者的請求來執行動作。該程式碼是一次性的，預期一次執行一項任務，執行後立即將其丟棄。

但是，如果您希望 AI 生成更持久的程式碼，該怎麼辦？如果您希望 AI 建置一個具有使用者可與之互動的自訂 UI 的小型應用程式，該怎麼辦？如果您希望應用程式具有長期存留狀態，該怎麼辦？但是，當然您仍希望其在安全的沙箱中執行。

一種方法是使用 Dynamic Workers，並為 Worker 提供一個 [_RPC_](https://developers.cloudflare.com/workers/runtime-apis/rpc/) API，讓其能夠存取儲存體。您可使用[ _繫結_](https://developers.cloudflare.com/dynamic-workers/usage/bindings/)，為 Dynamic Worker 提供一個 API，使其指向您的遠端 SQL 資料庫（可能由 [_Cloudflare D1_](https://developers.cloudflare.com/d1/) 提供支援，或透過 [_Hyperdrive_](https://developers.cloudflare.com/hyperdrive/) 存取的 Postgres 資料庫，這取決於您。

但是，Workers 還有一種獨特且極快的儲存體類型，可能非常適合此使用案例：[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/)。Durable Object 是一種特殊的 Worker，具有唯一的名稱，且每個名稱有一個全域執行個體。該執行個體附加了一個 SQLite 資料庫，其位於 Durable Object 執行所在機器的 _本機磁碟_ 上。這使得儲存體存取速度極快：實際上是[ _零延遲_](https://blog.cloudflare.com/sqlite-in-durable-objects/)。

那麼，也許您真正想要的是讓 AI 為 Durable Object 編寫程式碼，然後您希望在 Dynamic Worker 中執行該程式碼。

## **但是該如何做？**

這就提出了一個奇怪的問題。通常，若要使用 Durable Objects，您必須：

  1. 編寫一個擴展 `DurableObject` 的類別。
  2. 從 Worker 的主模組中將其匯出。
  3. [ _在 Wrangler 組態中指定_](https://developers.cloudflare.com/durable-objects/get-started/#5-configure-durable-object-class-with-sqlite-storage-backend)，應為此類別佈建儲存體。這會建立一個指向類別的 Durable Object 命名空間，以處理傳入的請求。
  4. [ _宣告 Durable Object 命名空間繫結_](https://developers.cloudflare.com/durable-objects/get-started/#4-configure-durable-object-bindings)指向您的命名空間（或使用 [_ctx.exports_](https://developers.cloudflare.com/workers/runtime-apis/context/#exports)），並將其用於向您的 Durable Object 發出請求。



這不會自然地延伸至 Dynamic Workers。首先，有一個明顯的問題：程式碼是動態的。您完全不需要叫用 Cloudflare API 即可執行。但 Durable Object 儲存體必須透過 API 佈建，且命名空間必須指向實作類別。其不能指向您的 Dynamic Worker。

但有一個更深層次的問題：即使您能以某種方式將 Durable Object 命名空間設定為直接指向 Dynamic Worker，您是否願意這樣做？您是否希望代理程式（或使用者）能夠建立一個充滿 Durable Objects 的完整命名空間？要使用分佈於世界各地的無限儲存體嗎？

您可能不需要。您可能需要某些控制權。您可能想要限制或至少追蹤其建立的物件數量。也許您想要將其限制為僅一個物件（對於 Vibe 編碼的個人應用程式可能已經足夠）。您可能想要新增記錄和其他可觀測性，包括指標、計費等等

為此，您真正需要的是，讓這些針對 Durable Objects 的請求 _首先_ 到達 _您的_ 程式碼，在此您可完成所有的「後勤作業」， _然後_ 將請求轉傳至代理程式的程式碼中。您想要編寫一個在每個 Durable Object 中執行的 _監督員_ 。

## **解決方案：Durable Object Facets**

今天，我們以公開測試版的形式發布了可解決此問題的功能。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3211 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49HKZJANBGF7YV1BB7BZMD.png&w=715&h=396&f=webp&fit=cover&position=center)

[ _Durable Object Facets_](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) 可讓您動態載入及具現化 Durable Object 類別，同時為其提供 SQLite 資料庫以用於儲存。使用 Facet：

  * 首先，您建立一個普通的 Durable Object 命名空間，指向 _您_ 編寫的一個類別。
  * 在該類別中，您將代理程式的程式碼作為 Dynamic Worker 載入，並對其進行呼叫。
  * Dynamic Worker 的程式碼可直接實作 Durable Object 類別。也就是說，其可逐字彙出一個宣告為`延伸 DurableObject` 的類別。
  * 您正在將該類別具現化為您自己的 Durable Object 的「面向」。
  * 該面向有自己的 SQLite 資料庫，可透過一般的 Durable Object 儲存 API 來使用該資料庫。此資料庫與監督員的資料庫分開，但兩者作為同一個 Durable Object 的一部分儲存在一起。



## **運作方式**

以下是動態載入和執行 Durable Object 類別的應用程式平台的簡單且完整的實作：
    
    
    import { DurableObject } from "cloudflare:workers";
    
    // For the purpose of this example, we'll use this static
    // application code, but in the real world this might be generated
    // by AI (or even, perhaps, a human user).
    const AGENT_CODE = `
      import { DurableObject } from "cloudflare:workers";
    
      // Simple app that remembers how many times it has been invoked
      // and returns it.
      export class App extends DurableObject {
        fetch(request) {
          // We use storage.kv here for simplicity, but storage.sql is
          // also available. Both are backed by SQLite.
          let counter = this.ctx.storage.kv.get("counter") || 0;
          ++counter;
          this.ctx.storage.kv.put("counter", counter);
    
          return new Response("You've made " + counter + " requests.\\n");
        }
      }
    `;
    
    // AppRunner is a Durable Object you write that is responsible for
    // dynamically loading applications and delivering requests to them.
    // Each instance of AppRunner contains a different app.
    export class AppRunner extends DurableObject {
      async fetch(request) {
        // We've received an HTTP request, which we want to forward into
        // the app.
    
        // The app itself runs as a child facet named "app". One Durable
        // Object can have any number of facets (subject to storage limits)
        // with different names, but in this case we have only one. Call
        // this.ctx.facets.get() to get a stub pointing to it.
        let facet = this.ctx.facets.get("app", async () => {
          // If this callback is called, it means the facet hasn't
          // started yet (or has hibernated). In this callback, we can
          // tell the system what code we want it to load.
    
          // Load the Dynamic Worker.
          let worker = this.#loadDynamicWorker();
    
          // Get the exported class we're interested in.
          let appClass = worker.getDurableObjectClass("App");
    
          return { class: appClass };
        });
    
        // Forward request to the facet.
        // (Alternatively, you could call RPC methods here.)
        return await facet.fetch(request);
      }
    
      // RPC method that a client can call to set the dynamic code
      // for this app.
      setCode(code) {
        // Store the code in the AppRunner's SQLite storage.
        // Each unique code must have a unique ID to pass to the
        // Dynamic Worker Loader API, so we generate one randomly.
        this.ctx.storage.kv.put("codeId", crypto.randomUUID());
        this.ctx.storage.kv.put("code", code);
      }
    
      #loadDynamicWorker() {
        // Use the Dynamic Worker Loader API like normal. Use get()
        // rather than load() since we may load the same Worker many
        // times.
        let codeId = this.ctx.storage.kv.get("codeId");
        return this.env.LOADER.get(codeId, async () => {
          // This Worker hasn't been loaded yet. Load its code from
          // our own storage.
          let code = this.ctx.storage.kv.get("code");
    
          return {
            compatibilityDate: "2026-04-01",
            mainModule: "worker.js",
            modules: { "worker.js": code },
            globalOutbound: null,  // block network access
          }
        });
      }
    }
    
    // This is a simple Workers HTTP handler that uses AppRunner.
    export default {
      async fetch(req, env, ctx) {
        // Get the instance of AppRunner named "my-app".
        // (Each name has exactly one Durable Object instance in the
        // world.)
        let obj = ctx.exports.AppRunner.getByName("my-app");
    
        // Initialize it with code. (In a real use case, you'd only
        // want to call this once, not on every request.)
        await obj.setCode(AGENT_CODE);
    
        // Forward the request to it.
        return await obj.fetch(req);
      }
    }
    

在此範例中：

  * `AppRunner` 是由平台開發人員（您）編寫的「標準」Durable Object。
  * `AppRunner` 的每個執行個體管理一個應用程式。其儲存應用程式碼並隨需載入。
  * 應用程式本身會實作並匯出一個 Durable Object 類別，平台預期將其命名為 `App`。
  * `AppRunner` 使用 Dynamic Workers 載入應用程式程式碼，然後將該程式碼作為 Durable Object Facet 執行。
  * `AppRunner` 的每個執行個體都是一個 Durable Object，由 _兩個_ SQLite 資料庫組成：一個屬於父項（`AppRunner` 本身），另一個屬於面向（`App`）。這些資料庫是隔離的：應用程式無法讀取 `AppRunner` 的資料庫，只能讀取自己的資料庫。



若要執行範例，請將上面的程式碼複製到檔案 `worker.js` 中，將其與下列 `wrangler.jsonc` 配對，並使用 `npx wrangler dev` 在本機執行。
    
    
    // wrangler.jsonc for the above sample worker.
    {
      "compatibility_date": "2026-04-01",
      "main": "worker.js",
      "migrations": [
        {
          "tag": "v1",
          "new_sqlite_classes": [
            "AppRunner"
          ]
        }
      ],
      "worker_loaders": [
        {
          "binding": "LOADER",
        },
      ],
    }
    

## **開始建置**

Facet 是 Dynamic Workers 的一項功能，目前提供測試版，可供 Workers 付費方案使用者使用。

請查閱文件以瞭解有關 [_Dynamic Workers_](https://developers.cloudflare.com/dynamic-workers/) 和 [_Facets_](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) 的詳細資訊。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fdurable-object-facets-dynamic-workers%2F&t=Dynamic%20Workers%20%E4%B8%AD%E7%9A%84%20Durable%20Objects%EF%BC%9A%E7%82%BA%E6%AF%8F%E5%80%8B%20AI%20%E7%94%A2%E7%94%9F%E7%9A%84%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F%E6%8F%90%E4%BE%9B%E5%85%B6%E8%87%AA%E5%B7%B1%E7%9A%84%E8%B3%87%E6%96%99%E5%BA%AB)[](https://x.com/intent/post?text=Dynamic+Workers+%E4%B8%AD%E7%9A%84+Durable+Objects%EF%BC%9A%E7%82%BA%E6%AF%8F%E5%80%8B+AI+%E7%94%A2%E7%94%9F%E7%9A%84%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F%E6%8F%90%E4%BE%9B%E5%85%B6%E8%87%AA%E5%B7%B1%E7%9A%84%E8%B3%87%E6%96%99%E5%BA%AB&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fdurable-object-facets-dynamic-workers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fdurable-object-facets-dynamic-workers%2F)[](https://bsky.app/intent/compose?text=Dynamic+Workers+%E4%B8%AD%E7%9A%84+Durable+Objects%EF%BC%9A%E7%82%BA%E6%AF%8F%E5%80%8B+AI+%E7%94%A2%E7%94%9F%E7%9A%84%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F%E6%8F%90%E4%BE%9B%E5%85%B6%E8%87%AA%E5%B7%B1%E7%9A%84%E8%B3%87%E6%96%99%E5%BA%AB+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fdurable-object-facets-dynamic-workers%2F)[](https://mastodonshare.com/?text=Dynamic+Workers+%E4%B8%AD%E7%9A%84+Durable+Objects%EF%BC%9A%E7%82%BA%E6%AF%8F%E5%80%8B+AI+%E7%94%A2%E7%94%9F%E7%9A%84%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F%E6%8F%90%E4%BE%9B%E5%85%B6%E8%87%AA%E5%B7%B1%E7%9A%84%E8%B3%87%E6%96%99%E5%BA%AB&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fdurable-object-facets-dynamic-workers%2F)[](https://www.threads.net/intent/post?text=Dynamic+Workers+%E4%B8%AD%E7%9A%84+Durable+Objects%EF%BC%9A%E7%82%BA%E6%AF%8F%E5%80%8B+AI+%E7%94%A2%E7%94%9F%E7%9A%84%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F%E6%8F%90%E4%BE%9B%E5%85%B6%E8%87%AA%E5%B7%B1%E7%9A%84%E8%B3%87%E6%96%99%E5%BA%AB+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fdurable-object-facets-dynamic-workers%2F)

## 相關標籤

[Agents Week](https://blog.cloudflare.com/zh-tw/tag/agents-week/)[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[儲存](https://blog.cloudflare.com/zh-tw/tag/storage/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
