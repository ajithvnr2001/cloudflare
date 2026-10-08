---
url: https://blog.cloudflare.com/zh-tw/how-waiting-room-queues/
title: Waiting Room \u5982\u4f55\u5728 Cloudflare \u7684\u9ad8\u5ea6\u5206\u6563\u5f0f\u7db2\u8def\u4e0a\u505a\u51fa\u6392\u968a\u6c7a\u7b56 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:43:25.949568+00:00
---

# Waiting Room 如何在 Cloudflare 的高度分散式網路上做出排隊決策 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/how-waiting-room-queues/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[Waiting Room](https://blog.cloudflare.com/zh-tw/tag/waiting-room/)+3顯示另外 3 個標籤

6 標籤顯示 6 個標籤

  * 文章標籤
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[網路](https://blog.cloudflare.com/zh-tw/tag/network/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)
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



[網路](https://blog.cloudflare.com/zh-tw/tag/network/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[Waiting Room](https://blog.cloudflare.com/zh-tw/tag/waiting-room/)[網路](https://blog.cloudflare.com/zh-tw/tag/network/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

2023年9月20日

# Waiting Room 如何在 Cloudflare 的高度分散式網路上做出排隊決策

![George Thomas](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48RNGYPD0NP89KE7WB4CS7.png&w=64&h=64&f=webp&fit=cover&position=center)

[George Thomas](https://blog.cloudflare.com/zh-tw/author/george/)

閱讀時間：20 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/how-waiting-room-queues/)、[Deutsch](https://blog.cloudflare.com/de-de/how-waiting-room-queues/)、[Français](https://blog.cloudflare.com/fr-fr/how-waiting-room-queues/)、[日本語](https://blog.cloudflare.com/ja-jp/how-waiting-room-queues/)和[简体中文](https://blog.cloudflare.com/zh-cn/how-waiting-room-queues/).

![How Waiting Room makes queueing decisions on Cloudflare's highly distributed network](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45Q291SVQX0YQV3V9MYAHM.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88/Pw6ujq6Ofs6+vx6+3w5+zp/////v377Ovu3d3m2tvo4eLv5unv5urp//////395+bt0dLkzdHm2Nzu4+bw5+rr////////6efy0dPnzdLq2t7y5ur07O7v////////8/L73uDy3eD06Oz78fX89Pf3////////////8/P/9PX//P7//////v//////////////////////////////////////////////////////////////////)

大約三年前，我們[推出了 Cloudflare Waiting Room](https://blog.cloudflare.com/zh-tw/cloudflare-waiting-room-zh-tw/)，以保護客戶的網站免受合法流量劇增的衝擊，這種流量劇增可能導致其網站癱瘓。Waiting Room 讓客戶即使在高流量時也能控制使用者體驗，將多餘的流量放置在可自訂的品牌 Waiting Room 中，並在網站上有空位時動態接納使用者。自 Waiting Room 推出以來，我們根據客戶的意見反應不斷擴展其功能，如[行動應用程式支援](https://blog.cloudflare.com/waiting-room-random-queueing-and-custom-web-mobile-apps/)、[分析](https://blog.cloudflare.com/understand-the-impact-of-your-waiting-rooms-settings-with-waiting-room-analytics/)、[Waiting Room 繞過規則](https://blog.cloudflare.com/waiting-room-bypass-rules/)[等](https://blog.cloudflare.com/tag/waiting-room/) 。

我們很喜歡發佈新功能，並透過擴展Waiting Room 的功能為客戶解決問題。但是今天，我們想給您一個幕後的視角，讓您瞭解我們如何發展產品的核心機制，即它如何啟動流量排隊以回應流量高峰。

## Waiting Room 是如何構建的以及面臨哪些挑戰？

下圖顯示了 Waiting Room 在客戶網站啟用後的位置概觀。

Waiting Room 建立在跨 Cloudflare 資料中心全球網路執行的 [Workers](https://workers.cloudflare.com/) 之上。對客戶網站的請求可能會轉到許多不同的 Cloudflare 資料中心。為了最佳化以減少[延遲](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)和提高效能，這些請求會被路由到地理位置最接近的資料中心。當新使用者向 Waiting Room 覆蓋的主機/路徑發出請求時，Waiting Room Worker 會決定是將使用者傳送到源站還是 Waiting Room。這一決定是利用 Waiting Room 狀態做出的，Waiting Room 狀態可提供源站上有多少使用者的資訊。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Waiting Room overview](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49ER0HAP6FBMK03EQF3R8Y.png&w=715&h=504&f=webp&fit=cover&position=center)

Waiting Room 的狀態會根據世界各地的流量不斷變化。這些資訊可以儲存在一個中央位置，或者最終可以在世界各地傳播變更。將這些資訊儲存在一個中心位置，會大大增加每次請求的延遲時間，因為中心位置可能離請求發出地非常遙遠。因此，每個資料中心都有自己的 Waiting Room 狀態，這是該時間點全球可用網站流量模式的快照。在讓使用者進入網站之前，我們不想等待來自世界其他地方的資訊，因為這會顯著增加請求的延遲時間。這就是我們選擇不設立中心位置，而是透過管道將流量變化最終傳播到世界各地的原因。

這個在後台匯總 Waiting Room 狀態的管道基於 Cloudflare [Durable Objects](https://blog.cloudflare.com/introducing-workers-durable-objects/) 構建。2021 年，我們撰寫了一篇[部落格](https://blog.cloudflare.com/building-waiting-room-on-workers-and-durable-objects/)，介紹了匯總管道的工作原理以及我們在其中採取的不同設計決策，如果您感興趣，可閱讀這篇文章。該管道可確保每個資料中心在幾秒鐘內獲得有關流量變化的最新資訊。

Waiting Room 必須根據當前看到的狀態決定是將使用者傳送到網站或還是讓他們排隊。必須在確保在正確的時間讓使用者排隊，以免客戶的網站過載。我們還必須確保不會因為誤認為出現流量高峰而讓使用者過早排隊。排隊可能會導致一些使用者放棄造訪該網站。Waiting Room 在 [Cloudflare 網路](https://www.cloudflare.com/network/)中的每台伺服器上執行，該網路覆蓋 100 多個國家/地區的 300 多座城市。我們希望確保，在決定每個新使用者是直接造訪網站還是排隊時，能夠將延遲降到最低。這也正是何時排隊成為 Waiting Room 難題的原因。在本部落格中，我們將介紹如何進行這種權衡。我們的演算法不斷發展，以減少誤判，同時繼續尊重客戶設定的限制。

## Waiting Room 如何決定何時讓使用者排隊

決定 Waiting Room 何時開始排隊的最重要因素是您配置流量設定的方式。設定 Waiting Room 時，您將設定兩個流量限制： _作用中使用者總數_和_每分鐘新使用者數_ 。_作用中使用者總數_是您希望在 Waiting Room 覆蓋的頁面上允許多少同時使用者數的目標閾值。 _每分鐘新使用者數_定義了每分鐘使用者湧入網站的最大速率的目標閾值。這兩個值中任何一個的急劇上升都可能導致排隊。影響我們計算_作用中使用者總數_的另一個設定是_工作階段持續時間_ 。由於請求是向 Waiting Room 覆蓋的任何頁面發出的，因此使用者在_工作階段持續時間_分鐘內被視為處於作用中狀態。

下圖來自我們為客戶提供的一個內部監控工具，顯示了客戶兩天內的流量模式。該客戶將其_每分鐘新使用者數_和_作用中使用者總數_限制分別設定為 200 和 200。

如果查看他們的流量，會發現使用者在 9 月 11 日 11:45 左右排隊。當時， _作用中使用者總數_約為 200 人左右。隨著_作用中使用者總數_逐漸下降（12:30 左右）_ ，_排隊使用者逐漸減少到 0。9 月 11 日 15:00 左右，作用中使用者總數達到 200 時，再次開始排隊。此時讓使用者排隊，確保了造訪該網站的流量在客戶設定的限制範圍內。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Customer traffic for 2 days between September 9th to 11th with 2 spikes in traffic](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SH6VVAQWD238ZTPDJ6F0.png&w=715&h=414&f=webp&fit=cover&position=center)

一旦使用者獲得網站存取權限，我們就會向他們提供一個加密的 [cookie](https://www.cloudflare.com/learning/privacy/what-are-cookies/)，表明他們已經獲得存取權限。cookie 的內容可能如下所示。

cookie 就像一張門票，表明 Waiting Room 的入口。 _bucketId_ 表明該使用者屬於哪個使用者叢集。 _acceptedAt_ 時間和 _lastCheckInTime_ 表明最後一次與 Workers 互動的時間。當我們將其與客戶在配置 Waiting Room 時設定的_工作階段持續時間_值進行比較時，該資訊可以表明門票是否能夠有效打開入口。如果 cookie 有效，我們會讓使用者通過，以確保網站上的使用者繼續能夠瀏覽網站。如果 cookie 無效，我們會建立一個新的 cookie，將使用者視為新使用者，如果網站上發生排隊，他們會排到佇列的後面。在下一節中，我們會介紹如何決定讓這些使用者進行排隊。
    
    
    {  
      "bucketId": "Mon, 11 Sep 2023 11:45:00 GMT",
      "lastCheckInTime": "Mon, 11 Sep 2023 11:45:54 GMT",
      "acceptedAt": "Mon, 11 Sep 2023 11:45:54 GMT"
    }

為了進一步理解這一點，讓我們來看看Waiting Room 狀態的內容。對於我們上面討論的客戶，在 "Mon, 11 Sep 2023 11:45:54 GMT" 時，狀態可能如下所示。

如上所述，客戶設定的_每分鐘新使用者數_和_作用中使用者總數_分別為 200 和 200。
    
    
    {  
      "activeUsers": 50,
    }

因此，該狀態表明，還有空間留給新使用者，因為只有 50 個作用中使用者，而作用中使用者可以達到 200 個。因此，還可以再允許 150 個使用者進入。假設這 50 個使用者分別來自聖約瑟（20 個使用者）和倫敦（30 個使用者）這兩個資料中心。我們還追蹤全球範圍內作用中的 Worker 數量以及計算狀態的資料中心的作用中 Worker 數量。聖約瑟可能計算得出下面的狀態金鑰。

試想一下，在 "`Mon, 11 Sep 2023 11:45:54 GMT`" 這個時間，我們收到一個請求，前往聖約瑟資料中心的 Waiting Room。
    
    
    {  
      "activeUsers": 50,
      "globalWorkersActive": 10,
      "dataCenterWorkersActive": 3,
      "trafficHistory": {
        "Mon, 11 Sep 2023 11:44:00 GMT": {
           San Jose: 20/200, // 10%
           London: 30/200, // 15%
           Anywhere: 150/200 // 75%
        }
      }
    }

要查看到達聖約瑟的使用者是否能前往源站，我們首先要查看過去一分鐘的流量歷程記錄，以瞭解當時的流量分佈情況。 這是因為很多網站在世界的某些地方很受歡迎。很多網站的流量往往來自相同的資料中心。

查看 "`Mon, 11 Sep 2023 11:44:00 GMT`" 這一分鐘的流量歷程記錄，我們可以看到當時聖約瑟的 200 個使用者中，有 20 個使用者前往該網站 (10%)。對於當前時間 "`Mon, 11 Sep 2023 11:45:54 GMT`"，我們按照過去一分鐘流量歷程記錄的相同比例分配網站可用的名額。因此，我們可以從聖約瑟傳送 150 個可用名額的 10%，即 15 個使用者。我們還知道，有三個作用中的 Worker，因為 "`dataCenterWorkersActive`" 為 `3`。

資料中心可用的名額數量在資料中心的 Worker 之間平均分配。因此，聖約瑟的每個 Worker 都可以向該網站傳送 15/3 的使用者。如果接收流量的 Worker 在當前分鐘內未向源站傳送任何使用者，則它們最多可以傳送_五_個使用者 (15/3)。

同時 ("`Mon, 11 Sep 2023 11:45:54 GMT`")，假設有一個請求傳送到德里的資料中心。德里資料中心的 Worker 檢查了流量歷程記錄，發現沒有為其分配名額。對於這樣的流量，我們保留了 Anywhere 名額，因為我們距離所設定的限制確實還很遠。

`Anywhere` 名額在全球所有作用中 Worker 之間劃分，相當於世界各地的任何 Worker 都可以分享這塊蛋糕。剩餘 150 個名額的 75%，即 113 個。
    
    
    {  
      "activeUsers":50,
      "globalWorkersActive": 10,
      "dataCenterWorkersActive": 1,
      "trafficHistory": {
        "Mon, 11 Sep 2023 11:44:00 GMT": {
           San Jose: 20/200, // 10%
           London: 30/200, // 15%
           Anywhere: 150/200 // 75%
        }
      }
    }

狀態金鑰還追蹤在世界各地產生的 Worker 數量 (`globalWorkersActive`)。分配的 Anywhere 名額將劃分給世界上所有作用中的 Worker（如果有）。當我們查看 Waiting Room 狀態時，`globalWorkersActive` 為 10。因此，每個作用中 Worker 最多可以傳送 113/10，即大約 11 個使用者。因此，在 `Mon, 11 Sep 2023 11:45:00 GMT` 這一分鐘內到達 Worker 的前 11 位使用者將被允許進入源站。後面的使用者需要排隊。之前討論過的聖約瑟會在 `Mon, 11 Sep 2023 11:45:00 GMT` 這一分鐘額外保留 5 個名額，確保我們可以允許來自聖約瑟的 Worker 最多 16 (5 + 11) 個使用者造訪該網站。

## 在 Worker 層級排隊可能會導致使用者在資料中心可用名額用完之前排隊

從上面的範例可以看出，我們是在 Worker 層級決定是否排隊的。前往世界各地 Worker 的新使用者數量可能並不相同。為了瞭解兩個 Worker 的流量分佈不均勻時會發生什麼情況，讓我們看看下圖。

想像一下，聖約瑟資料中心的可用名額有_十_個。有兩個 Worker 在聖約瑟執行。_七_個使用者前往 worker1，_一_個使用者前往 worker2。在這種情況下，worker1 會讓_七_個使用者中的_五_個進入網站，其中_兩_個人會排隊，因為 worker1 只有_五_個可用名額。前往 worker2 的_一_個使用者也可以前往源站。因此，實際上可以從聖約瑟資料中心傳送_十_個使用者，但在只出現了_八_個使用者時，我們卻讓_兩_個使用者進行了排隊。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Side effect of dividing slots at worker level](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4566Q054EWGNADWPDE844M.png&w=715&h=453&f=webp&fit=cover&position=center)

這種方式雖然在 Worker 之間平均分配了名額，但也導致在達到 Waiting Room 設定的流量限制之前進行排隊，通常在所設定限制的 20-30% 範圍內。我們接下來將討論這種方法的優點。 我們已經對這種方法進行了修改，以降低在 20-30% 範圍之外出現排隊的頻率，以在盡可能接近限制時再開始排隊，同時仍然確保 Waiting Room 做好應對高峰的準備。本部落格稍後將介紹我們如何透過更新配置和計算名額的方式來實現這一目標。

### 由 Worker 做出這些決定有什麼好處？

上面的範例談到了聖約瑟和德里的 Worker 如何決定是否讓使用者直達源站。在 Worker 層級做出決定的優勢在於，我們可以在不給請求增加任何明顯延遲的情況下做出決定。這是因為，在做出決定時，我們無需離開資料中心來獲取有關 Waiting Room 的資訊，因為我們始終知道資料中心的當前可用狀態。當 Worker 中的名額用完時，就開始排隊。由於沒有增加額外的延遲，客戶可以始終開啟 Waiting Room，而不必擔心使用者會受到額外延遲的影響。

Waiting Room 的首要任務是確保客戶的網站始終保持正常執行，即使面對突如其來的巨大流量也不例外。為此，Waiting Room 優先考慮保持在接近或低於客戶為該房間所設定之流量限制的位置，這一點至關重要。當全球的一個資料中心（例如聖約瑟）出現峰值時，資料中心的當地狀態將需要幾秒鐘才能到達德里。

在 Worker 之間劃分名額可確保在利用稍微過時的資料工作時不會導致嚴重超出總體限制。例如，在聖約瑟資料中心，`activeUsers` 值可能為 26，而在發生峰值的另一個資料中心，這個值可能為 100。在這個時候，從德里傳送更多的使用者可能不會超出總體限制太多，因為他們在德里只擁有一部分名額。因此，在達到總體限制之前排隊是設計的一部分，可以確保滿足總體限制。在下一節中，我們將介紹我們實施的方法，以在盡可能接近限制時排隊，又不會增加超出流量限制的風險。

## 當流量相對於 Waiting Room 限制還較低時分配更多名額

我們要解決的第一種情況是當流量距離限制較遠時開始排隊。雖然這種情況很少見，並且對於排隊的最終使用者來說通常會持續一個重新整理間隔（20 秒），但這是我們更新排隊演算法時的首要任務。為了解決這個問題，在分配名額時，我們會考慮使用率（距離流量限制有多遠），並在流量確實距離限制較遠時分配更多名額。這樣做的目的是防止在距離限制較遠時出現排隊的情況，同時還能在源站使用者增多時重新調整每個 Worker 可用的名額。

為了理解這一點，讓我們回顧一下兩個 Worker 的流量不均勻分配的范例。跟我們前面討論過的情況一樣，有下面兩個 Worker。在這種情況下，使用率很低 (10%)。 這意味著我們離限制還很遠。因此，分配的名額數 (8) 更接近聖約瑟資料中心的可用名額數 (10)。 從下圖中可以看出，在修改名額分配後，前往任一 Worker 的全部八個使用者都能造訪網站，因為我們在使用率較低的情況下為每個 Worker 提供了更多的名額。

下圖顯示了每個 Worker 配置的名額如何隨使用率（離限制有多遠）的變化而變化。如圖所示，在使用率較低的情況下，我們為每個 Worker 配置了更多名額。隨著使用率的提高，每個 Worker 配置的名額也在減少，因為它越來越接近限制，我們可以更好地為流量高峰做好準備。當使用率為 10% 時，每個 Worker 所獲得的名額將接近資料中心的可用名額。當使用率接近 100% 時，它就接近於可用名額除以資料中心的 Worker 數量。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Division of slots among workers at lower utilization](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW493CN0541Y792T082FBHJ8.png&w=715&h=453&f=webp&fit=cover&position=center)

### 如何在低使用率時獲得更多名額？

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Allotting more slots at lower limits](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45KC4XG240Q6FSQXE6FB1T.png&w=715&h=661&f=webp&fit=cover&position=center)

本節將深入探討協助我們實現這一目標的數學知識。如果您對這些細節不感興趣，請前往閱讀「超額佈建的風險」部分。

為了進一步理解這一點，讓我們回顧一下前面的範例：請求到達德里資料中心。`activeUsers` 值為 50，因此使用率為 50/200，約為 25%。

我們的想法是使用率水準較低時配置更多名額。這可以確保當流量遠離限制時，客戶不會看到意外的排隊行為。根據當地狀態金鑰，在 `Mon, 11 Sep 2023 11:45:54 GMT` 時，德里的請求使用率為 25%。
    
    
    {
      "activeUsers": 50,
      "globalWorkersActive": 10,
      "dataCenterWorkersActive": 1,
      "trafficHistory": {
        "Mon, 11 Sep 2023 11:44:00 GMT": {
           San Jose: 20/200, // 10%
           London: 30/200, // 15%
           Anywhere: 150/200 // 75%
        }
      }
    }

為了在使用率較低時配置更多可用名額，我們新增了一個 `workerMultiplier`，它與使用率成比例地移動。使用率較低時，乘數較低，使用率較高時，乘數接近於 1。

`utilization` \- 您距離限制有多遠。
    
    
    workerMultiplier = (utilization)^curveFactor
    adaptedWorkerCount = actualWorkerCount * workerMultiplier

`curveFactor` \- _curveFactor_ 是一個可以調整的指數，它決定了我們在 Worker 數量較少的情況下分配額外預算的積極程度。為了理解這一點，讓我們看一下 y = x 和 y = x^2 在值 0 和 1 之間的關係圖。

y=x 的圖形是一條經過 (0, 0) 和 (1, 1) 的直線。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph for y=x^curveFactor](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW473GSP0VZ963TYQHND0VAD.png&w=715&h=661&f=webp&fit=cover&position=center)

`y=x^2` 的圖形是一條曲線，其中當 `x < 1` 時，y 的增長速度慢於 `x`，並且經過 (0, 0) 和 (1, 1)

利用曲線工作原理的概念，我們推導出了`workerCountMultiplier` 的公式，其中_`y=workerCountMultiplier`，`x=utilization` _，_`curveFactor`_ 是可以調整的冪，它決定了我們在 Worker 數量較少的情況下分配額外預算的積極程度。當 _`curveFactor`_ 為 1 時，`workerMultiplier` 等於使用率。

讓我們回到之前討論的範例，看看曲線因數的值是多少。根據當地狀態金鑰，在 `Mon, 11 Sep 2023 11:45:54 GMT` 時，德里的請求使用率為 25%。Anywhere 名額在全球所有作用中 Worker 之間劃分，因為世界各地的任何 Worker 都可以分享這塊蛋糕，即剩餘 150 個名額的 75% (113)。

當我們查看 Waiting Room 狀態時，`globalWorkersActive` 為 10。在這種情況下，我們不會將 113 個名額除以 10，而是除以調整後的 Worker 數，即 `globalWorkersActive ***** workerMultiplier`。如果 `curveFactor` 為 `1`，則 `workerMultiplier` 等於 25% 或 0.25 的使用率。

因此，有效 `workerCount` = 10 * 0.25 = 2.5

這樣，每個作用中 Worker 最多可以傳送 113/2.5，即大約 45 個使用者。在 `Mon, 11 Sep 2023 11:45:00 GMT` 這一分鐘內到達 Worker 的前 45 個使用者將被允許進入源站，後面的使用者則需要排隊。

因此，在使用率較低時（流量離限制較遠時），每個 Worker 都會獲得更多名額。但是，如果將名額總和相加，則超過總體限制的可能性就更大。

### 超額佈建的風險

在距離限制較遠時提供更多名額的方法，可以減少在流量遠未達到限制時出現排隊的可能性。然而，在使用率水準較低時，如果世界各地一起發生流量高峰，可能會導致超過預期的使用者數進入源站。下圖顯示了這種情況，而這可能出現問題。如您所見，資料中心可用的名額有_十_個。在我們之前討論過的使用率為 10% 的情況下，每個 Worker 可以擁有_八_個名額。如果一個 Worker 中有_八_個使用者，另一個 Worker 中有_七_個使用者，那麼就會在資料中心的最大可用名額只有_十_個的情況下，向該網站傳送了_十五_個使用者。

由於我們的客戶和流量類型多種多樣，因此我們能夠看到出現這種問題的情況。從低使用率水準突然進入流量高峰可能會導致超出全域限制。這是因為我們在距離限制較遠時超額佈建，這增加了顯著超出流量限制的風險。我們需要實施一種更安全的方法，既不會導致超出限制，同時還可以減少當流量距離限制較遠時出現排隊的可能性。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Risk of over provisioning at lower utilization](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464DJ7YZVCP2T7F0R4NHWE.png&w=715&h=453&f=webp&fit=cover&position=center)

退一步思考我們的方法，我們的一個假設是，資料中心的流量與資料中心的 Worker 數量直接相關。實際上，我們發現，並非所有客戶都是如此。即使流量與 Worker 數量相關，但前往資料中心內 Worker 的新使用者可能與 Worker 數量並不相關。這是因為我們分配的名額是給新使用者的，但資料中心的流量既包括已經造訪網站的使用者，也包括試圖造訪網站的新使用者。

在下一節中，我們將討論一種不使用Worker 計數，而是讓 Worker 與資料中心內其他 Worker 進行通訊的方法。為此，我們推出了一項新服務，即 Durable Object 計數器。

## 透過引入資料中心計數器，減少劃分名額的次數

從上面的範例中，我們可以看到，Worker 層級的超額佈建可能會導致使用的名額數量多於配置給資料中心的名額數量。如果我們不在流量水準較低時超額佈建，就有可能在使用者達到所設定限制之前就出現排隊的情況，這一點我們在前面已經討論過。因此，必須有一種解決方案能夠同時解決這兩個問題。

超額佈建的目的是，當到達一群 Worker 的新使用者數量不均衡時，Worker 不會很快用完名額。如果資料中心的兩個 Worker 之間有辦法進行通訊，我們就不需要根據 Worker 的數量，在資料中心內的 Worker 之間劃分名額。為了實現這種通訊，我們引入了計數器。計數器是一組小型 Durable Object 執行個體，為資料中心的一組 Worker 進行計數。

要瞭解它如何幫助避免使用 Worker 計數，請看下圖。下面有兩個 Worker 在與_資料中心計數器_對話。就像我們之前討論的那樣，Worker 根據 Waiting Room 狀態讓使用者前往網站。通過的使用者數量儲存在 Worker 的記憶體中。引入計數器後，通過的使用者數量可以儲存在_資料中心計數器_中。每當有新使用者向 Worker 發出請求時，Worker 就會與計數器對話，以瞭解計數器的當前值。在下面的範例中，當 Worker 收到第一個新請求時，收到的計數器值是 9。在資料中心有 10 個可用名額的情況下，這意味著該使用者可以造訪網站。如果下一個 Worker 收到一個新使用者並在其後發出請求，它將得到計數器值 10，並根據該 Worker 的可用名額，讓該使用者排隊。

_資料中心計數器_充當 Waiting Room 中 Worker 的同步點。從本質上講，這使得 Worker 能夠相互對話，但無需真正直接相互對話。這與售票處的工作原理類似。每當一個 Worker 讓某人進入時，他們都會向計數器索取門票，因此另一個向計數器索取門票的 Worker 將不會獲得相同的票號。如果票值有效，新使用者就可以造訪該網站。因此，當不同的 Worker 處出現不同數量的新使用者時，我們不會為一個 Worker 超額配置或配置不足的名額，因為使用的名額數量是由資料中心的計數器計算的。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Counters helping workers communicate with each other](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MAB046HP7KBZWSNN02TT.png&w=715&h=523&f=webp&fit=cover&position=center)

下圖顯示了當數量不等的新使用者到達 Worker 處時的行為，一個 Worker 有_七_個新使用者，另一個 Worker 有_一_個新使用者。下圖中出現在 Worker 處的全部_八_個使用者都會造訪該網站，因為資料中心的可用名額為_十_個，而現在低於_十_個。

這也不會導致過多的使用者被傳送到網站，因為當計數器值等於資料中心的可用名額時，我們不會再傳送額外的使用者。在下圖中出現在 Worker 處的_十五_個使用者中，有_十_個將造訪該網站，另外_五_個將排隊，這正是我們所期望的。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Uneven number of requests to workers does not cause queueing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZCMXWDQ58PNXWYJSRCA.png&w=715&h=453&f=webp&fit=cover&position=center)

在使用率較低的情況下，也不存在超額佈建的風險，因為計數器可以幫助 Worker 相互通訊

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2026 Embedded Image - yq9u67](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48R4F31G3TC7X9GY5WM3KQ.png&w=715&h=453&f=webp&fit=cover&position=center)

為了進一步理解這一點，讓我們看一下前面談到的範例，看看它是如何與實際的 Waiting Room 狀態配合使用的。

客戶的 Waiting Room 狀態如下。

目標是不在 Worker 之間劃分名額，這樣我們就不需要使用狀態提供的資訊。在 `Mon, 11 Sep 2023 11:45:54 GMT` 時，請求到達聖約瑟。因此，我們可以從聖約瑟傳送 150 個可用名額的 10%，即 15 個。
    
    
    {  
      "activeUsers": 50,
      "globalWorkersActive": 10,
      "dataCenterWorkersActive": 3,
      "trafficHistory": {
        "Mon, 11 Sep 2023 11:44:00 GMT": {
           San Jose: 20/200, // 10%
           London: 30/200, // 15%
           Anywhere: 150/200 // 75%
        }
      }
    }

每有一個新使用者到達資料中心，聖約瑟的 Durable Object 計數器就會不斷返回當前的計數器值。返回 Worker 後，數值將遞增 1。因此，前往 Worker 的前 15 個新使用者會得到一個唯一的計數器值。如果針對一個使用者收到的值小於 15，這個使用者就可以使用資料中心的名額。

一旦資料中心的可用名額用完，使用者就可以使用配置給 Anywhere 資料中心的名額，因為這些名額沒有為任何特定資料中心保留。當聖約瑟的 Worker 收到顯示為 15 的計數器值時，它就會意識到不能再使用聖約瑟的名額造訪網站。

Anywhere 名額可供全球所有作用中 Worker 使用，即剩餘 150 個名額中的 75% (113)。Anywhere 名額由一個 Durable Object 處理，來自不同資料中心的 Worker 在想要使用 Anywhere 名額時可以與該 Durable Object 進行對話。即使有 128 (113 + 15) 個使用者最終前往該客戶的同一 Worker，我們也不會讓其進行排隊。這提高了 Waiting Room 處理前往世界各地 Worker 的新使用者數量不均的能力，進而協助客戶在接近所設定限制時才安排使用者排隊。

### 為什麼計數器對我們很有效？

當我們構建 Waiting Room 時，我們希望在 Worker 層級自行決定是否進入網站，而不是在請求進入網站時與其他服務對話。我們這樣做是為了避免增加使用者請求的延遲。透過在 Durable Object 計數器上引入同步點，我們偏離了這一點，引入了對 Durable Object 計數器的呼叫。

不過，資料中心的 Durable Object 仍在同一資料中心內。這將導致最小的額外延遲，通常小於 10 毫秒。對於處理 Anywhere 資料中心的 Durable Object 的呼叫，Worker 可能需要跨越海洋和長途。在這種情況下，延遲可能會達到 60 或 70 毫秒。下面顯示的第 95 百分位數值較高，因為呼叫會轉到更遠的資料中心。

新增計數器的設計決定會給造訪網站的新使用者增加一點額外的延遲。我們認為這種權衡是可以接受的，因為這樣可以減少在達到限制前排隊的使用者數量。此外，只有在新使用者嘗試進入網站時才需要計數器。一旦新使用者到達源站，他們就可以直接從 Worker 處獲得進入許可權，因為可以在客戶附帶的 cookie 中找到進入證明，我們可以根據該證明讓他們進入。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph showing percentile distribution of counter latencies from our production dashboard](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CKWXRKRVYN9H44AMMH6P.png&w=715&h=307&f=webp&fit=cover&position=center)

計數器實際上是一種簡單的服務，只進行簡單的計數，不做其他任何事情。這樣，計數器佔用的記憶體和 CPU 空間就非常小。此外，我們還在全球範圍內設立了大量計數器，處理一部分 Worker 之間的協調工作，這有助於計數器成功處理來自 Worker 的同步要求負載。這些因素加在一起，使計數器成為我們使用案例中的一個可行解決方案。

## 概述

在設計 Waiting Room 時，我們的首要考量是確保客戶的網站保持正常執行，無論合法流量的數量或增長情況如何。Waiting Room 在 Cloudflare 網路中的每台伺服器上執行，該網路覆蓋 100 多個國家的 300 多座城市。我們希望確保在最短時間內為每一個新使用者做出決定，是去網站還是去排隊。這是一個艱難的決定，因為在資料中心排隊太早可能會導致我們排隊的時間早于客戶設定的限制。而排隊太晚又會導致我們超出客戶設定的限制。

我們最初採用的方法是在 Worker 之間平均分配名額，有時排隊時間過早，但在尊重客戶設定的限制方面做得很好。我們的後面一個方法是在低使用率（與客戶限制相比較低的流量水準）時提供更多名額，這很好地解決了在遠早于客戶所設限制時排隊的情況，因為每個 Worker 都有更多的名額可以使用。但正如我們所看到的，當流量在一段低使用率時期後突然激增時，我們更容易超出限制。

有了計數器，我們就可以避免按 Worker 數量來劃分名額，從而獲得兩全其美的效果。利用計數器，我們能夠確保根據客戶設定的限制，不會過早或過晚排隊。這樣做的代價是，新使用者的每個請求都會有一點延遲，但我們發現這種延遲可以忽略不計，而且比提前排隊獲得更好的使用者體驗。

我們不斷改進我們的方法，以確保我們總是在正確的時間讓使用者排隊，以及最重要的是——保護您的網站。隨著越來越多的客戶使用 Waiting Room，我們對不同類型的流量有了更多的瞭解，這有助於產品更好地服務於每個人。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-waiting-room-queues%2F&t=Waiting%20Room%20%E5%A6%82%E4%BD%95%E5%9C%A8%20Cloudflare%20%E7%9A%84%E9%AB%98%E5%BA%A6%E5%88%86%E6%95%A3%E5%BC%8F%E7%B6%B2%E8%B7%AF%E4%B8%8A%E5%81%9A%E5%87%BA%E6%8E%92%E9%9A%8A%E6%B1%BA%E7%AD%96)[](https://x.com/intent/post?text=Waiting+Room+%E5%A6%82%E4%BD%95%E5%9C%A8+Cloudflare+%E7%9A%84%E9%AB%98%E5%BA%A6%E5%88%86%E6%95%A3%E5%BC%8F%E7%B6%B2%E8%B7%AF%E4%B8%8A%E5%81%9A%E5%87%BA%E6%8E%92%E9%9A%8A%E6%B1%BA%E7%AD%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-waiting-room-queues%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-waiting-room-queues%2F)[](https://bsky.app/intent/compose?text=Waiting+Room+%E5%A6%82%E4%BD%95%E5%9C%A8+Cloudflare+%E7%9A%84%E9%AB%98%E5%BA%A6%E5%88%86%E6%95%A3%E5%BC%8F%E7%B6%B2%E8%B7%AF%E4%B8%8A%E5%81%9A%E5%87%BA%E6%8E%92%E9%9A%8A%E6%B1%BA%E7%AD%96+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-waiting-room-queues%2F)[](https://mastodonshare.com/?text=Waiting+Room+%E5%A6%82%E4%BD%95%E5%9C%A8+Cloudflare+%E7%9A%84%E9%AB%98%E5%BA%A6%E5%88%86%E6%95%A3%E5%BC%8F%E7%B6%B2%E8%B7%AF%E4%B8%8A%E5%81%9A%E5%87%BA%E6%8E%92%E9%9A%8A%E6%B1%BA%E7%AD%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-waiting-room-queues%2F)[](https://www.threads.net/intent/post?text=Waiting+Room+%E5%A6%82%E4%BD%95%E5%9C%A8+Cloudflare+%E7%9A%84%E9%AB%98%E5%BA%A6%E5%88%86%E6%95%A3%E5%BC%8F%E7%B6%B2%E8%B7%AF%E4%B8%8A%E5%81%9A%E5%87%BA%E6%8E%92%E9%9A%8A%E6%B1%BA%E7%AD%96+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-waiting-room-queues%2F)

## 相關標籤

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[Waiting Room](https://blog.cloudflare.com/zh-tw/tag/waiting-room/)[網路](https://blog.cloudflare.com/zh-tw/tag/network/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
