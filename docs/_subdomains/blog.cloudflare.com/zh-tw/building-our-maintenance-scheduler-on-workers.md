---
url: https://blog.cloudflare.com/zh-tw/building-our-maintenance-scheduler-on-workers/
title: Workers \u5982\u4f55\u70ba\u6211\u5011\u7684\u5167\u90e8\u7dad\u8b77\u8abf\u5ea6\u7ba1\u7dda\u63d0\u4f9b\u652f\u63f4 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:45:15.178374+00:00
---

# Workers 如何為我們的內部維護調度管線提供支援 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/building-our-maintenance-scheduler-on-workers/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Prometheus](https://blog.cloudflare.com/zh-tw/tag/prometheus/)[可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)+1顯示另外 1 個標籤

4 標籤顯示 4 個標籤

  * 文章標籤
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Prometheus](https://blog.cloudflare.com/zh-tw/tag/prometheus/)[可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)[基礎架構](https://blog.cloudflare.com/zh-tw/tag/infrastructure/)
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



[基礎架構](https://blog.cloudflare.com/zh-tw/tag/infrastructure/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Prometheus](https://blog.cloudflare.com/zh-tw/tag/prometheus/)[可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)[基礎架構](https://blog.cloudflare.com/zh-tw/tag/infrastructure/)

2025年12月22日

# Workers 如何為我們的內部維護調度管線提供支援

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/zh-tw/author/kevin-deems/)和[Michael Hoffmann](https://blog.cloudflare.com/zh-tw/author/michael-hoffmann/)

閱讀時間：10 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/building-our-maintenance-scheduler-on-workers/)、[日本語](https://blog.cloudflare.com/ja-jp/building-our-maintenance-scheduler-on-workers/)、[한국어](https://blog.cloudflare.com/ko-kr/building-our-maintenance-scheduler-on-workers/)和[简体中文](https://blog.cloudflare.com/zh-cn/building-our-maintenance-scheduler-on-workers/).

![BLOG-3017 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MH5G11Z4TPXRMZT8FJXD.png&w=1016&h=635&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAO1yFQGCLTWmWWXWgX36jXH2gT3OaPWWUQ2mQU3OWbIakeZSydpe5aJC3WIOrT3eeS3acYoSjhJ6zk67Ei63OdKHLYZK8XoepT3+nao+tkKq9oLvOl7nYfqvVaZrGZpCxUIOuapGzj6rAobnNmrjVhKrTbpvFZZG0TYKyY4y1hKC9l63Flq3JhqPGcJW9XYy0Sn+zWYa1dZO5ip27kJ+6hpm3cI60U4SySH6zVYO1boy3g5W2jJmzhpWwcIuvT4Cx)

Cloudflare 在[ _全球超過 330 座城市_](https://www.cloudflare.com/network/)設有資料中心，因此您可能會認為我們在計劃進行資料中心操作時，隨時可以輕鬆中斷其中幾個而不被使用者察覺。然而，現實情況是，[ _破壞性維護_](https://developers.cloudflare.com/support/disruptive-maintenance/)需要精心規劃，而且隨著 Cloudflare 的發展，透過我們的基礎架構和網路營運專家之間的手動協調來管理這些複雜性幾乎變得不可能。

人類已無法即時追蹤每一個重疊的維護請求，也無法兼顧特定于每一個客戶的路由規則。我們達到了一個臨界點：單靠人工監督已不足以保證，在世界某地進行的例行硬體更新不會意外地與另一地的關鍵路徑發生衝突。

我們意識到，需要一個集中化、自動化的「大腦」來充當保障——一個能夠同時洞察整個網路狀態的系統。透過在 [_Cloudflare Workers_](https://workers.cloudflare.com/) 上建立這一排程器，我們創造了一種以程式設計方式強制執行安全約束的方法，確保無論我們推進速度多快，都不會犧牲客戶所依賴服務的可靠性。

在這篇部落格文章中，我們將說明它的建立過程，並分享目前的成果。

## 建立系統，以降低關鍵維護操作的風險

設想一台邊緣路由器，它是連接公用網際網路與某個大都市區域內眾多 Cloudflare 資料中心的備援閘道群組中的一員。在人口密集的城市，我們必須確保位於這一小群路由器背後的多個資料中心不會因為所有路由器同時下線而被切斷連線。

另一個維護挑戰來自我們的 Zero Trust 產品 Dedicated CDN Egress IPs。它允許客戶選擇特定的資料中心，讓使用者的流量從這些資料中心離開 Cloudflare，並傳送到地理位置靠近的來源伺服器，以實現低延遲。（為簡潔起見，在本文中我們將該產品稱為「Aegis」，這是它之前的名稱。）如果客戶所選的所有資料中心同時下線，他們將會遇到更高的延遲，甚至可能出現 5xx 錯誤，而我們必須避免這種情況。

我們的維護排程器解決了類似這樣的問題。我們可以確保在某一區域內始終至少有一台邊緣路由器處於活躍狀態；並且在安排維護時，能夠判斷多個預定事件的組合是否會導致某客戶的 Aegis 集區中所有資料中心同時下線。

在建立排程器之前，這些同時發生的破壞性事件可能導致客戶的服務中斷。而現在，排程器會向內部運維人員提示潛在衝突，使我們能夠提議新的時間，以避免與其他相關的資料中心維護事件重疊。

我們將這些營運場景（例如邊緣路由器的可用性以及客戶規則）定義為維護約束，這讓我們能夠規劃更可預測且更安全的維護。

## 維護約束

每個約束都始於一組提議的維護項目，例如一台網路路由器或一組伺服器。接著，我們會查找行事曆中所有與提議的維護時間視窗重疊的維護事件。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45N24BK9S5N2GJ6VGMRCGQ.png&w=715&h=385&f=webp&fit=cover&position=center)

然後，我們彙總各類產品 API，例如 Aegis 客戶 IP 集區清單。Aegis 會傳回一組 IP 範圍，這些範圍對應客戶要求從其特定資料中心 ID 發出流量的位置，如下圖所示。
    
    
    [
        {
          "cidr": "104.28.0.32/32",
          "pool_name": "customer-9876",
          "port_slots": [
            {
              "dc_id": 21,
              "other_colos_enabled": true,
            },
            {
              "dc_id": 45,
              "other_colos_enabled": true,
            }
          ],
          "modified_at": "2023-10-22T13:32:47.213767Z"
        },
    ]

在該場景中，資料中心 21 和資料中心 45 是相互關聯的，因為對於 Aegis 客戶 9876 來說，我們需要至少一個資料中心保持線上，以便其能夠從 Cloudflare 接收輸出流量。如果我們試圖同時關閉資料中心 21 和 45，協調器就會提醒我們，該客戶的工作負載將因此受到意外影響。

最初我們嘗試了一個簡單的方案：將所有資料載入到單個 Worker 中。這包括所有伺服器關係、產品組態，以及用於計算約束的產品和基礎架構健康指標。但只是在概念驗證階段，我們就遇到了「記憶體不足」的錯誤。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44X5J4KQRSH4Q5YRX5JNQC.png&w=715&h=226&f=webp&fit=cover&position=center)

我們需要更加注意 Workers 的[ _平台限制_](https://developers.cloudflare.com/workers/platform/limits/)。這就要求僅載入處理約束業務邏輯所絕對必需的資料。如果收到德國法蘭克福某台路由器的維護請求，我們幾乎可以肯定不需要關心澳大利亞的情況，因為跨區域之間沒有關聯。因此，我們只應載入德國鄰近資料中心的相關資料。我們需要一種更高效的方法來處理資料集中的關係。

## 在 Workers 上進行圖形處理

在分析約束時，我們發現一種規律：每個約束本質上可歸結為兩個概念——物件與關聯。在圖論中，這兩類元件分別稱為頂點 (vertices) 和邊 (edges)。物件可以是網路路由器，而關聯則可以是該資料中心內要求路由器保持線上的一組 Aegis 集區。我們從 Facebook 的 [_TAO_](https://research.facebook.com/publications/tao-facebooks-distributed-data-store-for-the-social-graph/) 研究論文中獲得啟發，在產品與基礎架構資料之上建立了一套圖形介面。API 範例如下：
    
    
    type ObjectID = string
    
    interface MainTAOInterface<TObject, TAssoc, TAssocType> {
      object_get(id: ObjectID): Promise<TObject | undefined>
    
      assoc_get(id1: ObjectID, atype: TAssocType): AsyncIterable<TAssoc>
    }

核心理念在於，關聯是有類型的。例如，約束會呼叫圖形介面來擷取 Aegis 產品資料。
    
    
    async function constraint(c: AppContext, aegis: TAOAegisClient, datacenters: string[]): Promise<Record<string, PoolAnalysis>> {
      const datacenterEntries = await Promise.all(
        datacenters.map(async (dcID) => {
          const iter = aegis.assoc_get(c, dcID, AegisAssocType.DATACENTER_INSIDE_AEGIS_POOL)
          const pools: string[] = []
          for await (const assoc of iter) {
            pools.push(assoc.id2)
          }
          return [dcID, pools] as const
        }),
      )
    
      const datacenterToPools = new Map<string, string[]>(datacenterEntries)
      const uniquePools = new Set<string>()
      for (const pools of datacenterToPools.values()) {
        for (const pool of pools) uniquePools.add(pool)
      }
    
      const poolTotalsEntries = await Promise.all(
        [...uniquePools].map(async (pool) => {
          const total = aegis.assoc_count(c, pool, AegisAssocType.AEGIS_POOL_CONTAINS_DATACENTER)
          return [pool, total] as const
        }),
      )
    
      const poolTotals = new Map<string, number>(poolTotalsEntries)
      const poolAnalysis: Record<string, PoolAnalysis> = {}
      for (const [dcID, pools] of datacenterToPools.entries()) {
        for (const pool of pools) {
          poolAnalysis[pool] = {
            affectedDatacenters: new Set([dcID]),
            totalDatacenters: poolTotals.get(pool),
          }
        }
      }
    
      return poolAnalysis
    }

在以上程式碼中，我們使用了兩種關聯類型：

  1. DATACENTER_INSIDE_AEGIS_POOL，擷取資料中心所在的 Aegis 客戶集區。
  2. AEGIS_POOL_CONTAINS_DATACENTER，擷取 Aegis 集區服務流量所需的資料中心。



這兩種關聯互為反向索引。存取模式與之前完全相同，但現在圖形實作能更好地控制查詢的資料量。以前我們需要將所有 Aegis 集區載入到記憶體中，並在約束業務邏輯裡進行篩選；現在我們可以直接擷取與應用程式相關的資料。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46V747SXCQBJ3NZGGBWH72.png&w=715&h=313&f=webp&fit=cover&position=center)

該介面的強大之處在於，圖形實作可以在後台提升效能，而不會讓業務邏輯變得更複雜。這讓我們可以利用 Workers 的可擴展性以及 Cloudflare CDN 的優勢，從內部系統中非常快速地擷取資料。

## 擷取管線

我們切換到使用新的圖形實作後，開始傳送更具針對性的 API 請求。回應大小在一夜之間減少了 100 倍——從載入少數幾個巨大的請求變為載入許多微小的請求。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48J28W9JDW5V667ENB9QRH.png&w=715&h=344&f=webp&fit=cover&position=center)

雖然這解決了一次性載入過多資料導致記憶體不足的問題，但我們又遇到了子請求數量過多的新問題。因為現在我們不再發起少量大型 HTTP 請求，而是發起數量級更多的微小請求，結果很快就持續突破了 Workers 的子請求限制。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45SB0HD85RBHA7KBXDD3TD.png&w=715&h=346&f=webp&fit=cover&position=center)

為了解決這個問題，我們在圖形實作和 `fetch` API 之間建立了一個智慧中介軟體層。
    
    
    export const fetchPipeline = new FetchPipeline()
      .use(requestDeduplicator())
      .use(lruCacher({
        maxItems: 100,
      }))
      .use(cdnCacher())
      .use(backoffRetryer({
        retries: 3,
        baseMs: 100,
        jitter: true,
      }))
      .handler(terminalFetch);

如果您熟悉 Go 語言，可能見過 [_singleflight_](https://pkg.go.dev/golang.org/x/sync/singleflight) 包。我們借鑒了這個思路，在擷取管線中的第一個中介軟體元件實現了對正在進行的 HTTP 請求去重，讓同一 Worker 內的重複請求都等待同一個 Promise 傳回資料，而不是產生重複的請求。接下來，我們使用羽量級的最近最少使用 (LRU) 快取，在內部快取已經請求過的資料。

完成這兩項操作後，我們使用 Cloudflare 的 `caches.default.match` 函數快取 Worker 執行所在區域的所有 GET 請求。由於我們有多個效能特徵各異的資料來源，因此我們謹慎地選擇存留時間 (TTL) 值。例如，即時資料僅快取 1 分鐘。相對靜態的基礎架構資料可以根據資料類型快取 1 到 24 小時。電源管理資料可能需要手動變更且變更頻率較低，因此我們可以將其在邊緣端快取更長時間。

除了上述層外，我們還加入了標準的指數退避 (exponential backoff)、重試 (retries) 和抖動 (jitter) 機制。這有助於減少因下游資源臨時不可用而產生的無效 `fetch` 呼叫。透過適度退避，我們提高了下一次成功擷取資料的概率；反之，如果 Worker 持續不斷傳送請求而不退避，當源站傳回 5xx 錯誤時很容易突破子請求限制。

綜合這些措施後，我們實現了約 99% 的快取命中率。[ _快取命中率_](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)是指直接從 Cloudflare 快速快取記憶體（命中）傳回資料的 HTTP 請求，相對於需要從控制平面資料來源（未命中）發起較慢請求的百分比，計算公式為 (命中數/(命中數 + 未命中數))。高命中率意味著更好的 HTTP 請求效能和更低的成本，因為在 Worker 中從快取查詢資料的速度比從位於不同區域的來源伺服器擷取資料快一個數量級。經過調優記憶體快取和 CDN 快取的設定後，命中率大幅提升。由於我們的工作負載很多是即時的，命中率永遠達不到 100%，因為我們每分鐘至少需要請求一次最新資料。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44RXG38NESXHB4QMTCNP2J.png&w=715&h=691&f=webp&fit=cover&position=center)

我們已經討論了如何改進擷取層，但尚未說明如何讓源站的 HTTP 請求更快。我們的維護排程器需要即時回應網路降級和資料中心機器故障。為此，我們使用分散式 [_Prometheus_](https://blog.cloudflare.com/how-cloudflare-runs-prometheus-at-scale/) 查詢引擎 Thanos，將邊緣的高效能指標傳遞到排程器中。

## 即時 Thanos

為了說明採用圖形處理介面如何影響即時查詢，我們來看一個範例。要分析邊緣路由器的健康狀況，原本我們會傳送如下查詢：
    
    
    sum by (instance) (network_snmp_interface_admin_status{instance=~"edge.*"})

最初，我們向儲存 Prometheus 指標的 Thanos 服務請求每個邊緣路由器的當前健康狀況清單，並在 Worker 中手動篩選與維護相關的路由器。這種方法有很多不足之處。例如，Thanos 傳回的回應大小高達數 MB，需要進行解碼和編碼。Worker 也需要快取和解碼這些大型 HTTP 回應，以便在處理特定維護請求時濾除大部分資料。由於 TypeScript 是單執行緒的，而剖析 JSON 資料又受 CPU 限制，傳送兩個大型 HTTP 請求意味著一個請求會被封鎖，等待另一個請求完成剖析。

現在我們改為直接使用圖形來查找有針對性的關係，例如邊緣路由器與骨幹路由器之間的介面連結，用 `EDGE_ROUTER_NETWORK_CONNECTS_TO_SPINE` 表示。
    
    
    sum by (lldp_name) (network_snmp_interface_admin_status{instance=~"edge01.fra03", lldp_name=~"spine.*"})

結果平均只有 1 KB，而不是數 MB，大約縮小了 1000 倍。這也大幅降低了 Worker 內部的 CPU 消耗，因為我們把大部分反序列化工作交給 Thanos 完成。正如前面所說，這意味著我們需要發起更多的小請求，但 Thanos 前的負載平衡器可以將請求均勻分散，從而提高這種用例的輸送量。

我們的圖形實作與擷取管線成功控制了成千上萬個微小即時請求形成的「驚群效應」(thundering herd)。不過，歷史分析帶來了不同的 I/O 挑戰——我們不再只是擷取小而具體的關係，而是要掃描數月的資料來發現衝突的維護視窗。過去，Thanos 會對我們的物件儲存 R2 發起大量隨機讀取，造成巨大頻寬開銷。為了解決這一問題又不損失效能，我們採用了 Observability 團隊今年內部開發的新方法。

## 歷史資料分析

我們有足夠多的維護用例，必須依賴歷史資料來判斷我們的解決方案是否準確，以及能否隨 Cloudflare 網路的擴展而擴展。我們既不想引發事故，也不希望不必要地阻礙已計劃的實體維護。為了在這兩個目標之間取得平衡，我們可以利用兩月前甚至一年前的維護事件時間序列資料，來分析某類維護事件違反我們約束（例如邊緣路由器可用性、Aegis 相關規則）的頻率。今年早些時候，我們曾在部落格中介紹過利用 Thanos [_自動向邊緣發佈及回滾軟體_](https://blog.cloudflare.com/safe-change-at-any-scale/)的做法。

Thanos 主要將資料查詢分發到 Prometheus，但當 Prometheus 的資料保留期不足以回答查詢時，就不得不從物件儲存體（在我們的案例中為 R2）下載資料。Prometheus 的 TSDB 區塊最初是為本地 SSD 設計的，依賴隨機存取模式，這在遷移到物件儲存體後會成為瓶頸。當我們的排程器需要分析數月的維護歷史資料以識別衝突約束時，從物件儲存體進行隨機讀取會帶來巨大的 I/O 開銷。為解決此問題，我們實現了一個轉換層，將這些 TSDB 區塊轉換為 [_Apache Parquet_](https://parquet.apache.org/) 檔案。Parquet 是一種面向大資料分析的原生欄式儲存格式，按欄而非按列組織資料，並結合豐富的統計資訊，使我們可以只擷取所需的部分資料。

此外，由於我們將 TSDB 區塊重寫為 Parquet 檔案，還可以按支援少量大塊依序讀取資料的方式儲存資料。
    
    
    sum by (instance) (hmd:release_scopes:enabled{dc_id="45"})

在上面的範例中，我們將選擇元組「(__name__, dc_id)」作為主要排序鍵，以便名稱為「hmd:release_scopes:enabled」且「dc_id」值相同的指標能夠被排到一起。

我們的 Parquet 閘道現在會發起精確的 R2 區間請求，僅提取與查詢相關的特定欄。這將有效載荷從數 MB 減少到數 KB。而且因為這些檔案段是不可變的，我們可以在 Cloudflare CDN 上積極快取它們。

這使 R2 變成了低延遲的查詢引擎，讓我們可以即時針對長期趨勢回測複雜的維護場景，避免了原 TSDB 格式下的逾時和高尾延遲問題。下圖展示了一次近期的負載測試，結果顯示在相同查詢模式下，Parquet 的 P90 效能最高可達舊系統的 15 倍。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BX8FVSJG36HNQHC5YCNS.png&w=715&h=222&f=webp&fit=cover&position=center)

如果想深入瞭解 Parquet 的實作原理，可以觀看 PromCon EU 2025 上的演講 [_Beyond TSDB: Unlocking Prometheus with Parquet for Modern Scale_](https://www.youtube.com/watch?v=wDN2w2xN6bA&list=PLoz-W_CUquUlHOg314_YttjHL0iGTdE3O&index=16)。

## 為擴展而建置

透過利用 Cloudflare Workers，我們從一套會因記憶體不足而崩潰的系統，演進為一個能智慧快取資料並使用高效可觀測性工具即時分析產品與基礎架構資料的系統。我們建立了一個能在網路增長與產品效能之間取得平衡的維護排程器。

但「平衡」是個動態目標。

每天，我們都在全球增加更多硬體，而要確保維護過程中不打斷客戶流量，其邏輯複雜度會隨著產品種類和維護操作類型的增多呈指數級上升。我們已經攻克了第一階段的挑戰，但現在正面對只有在如此大規模下才會顯現的更微妙、更複雜的問題。

我們需要不畏艱難的工程師。加入我們的[ _基礎架構團隊_](https://www.cloudflare.com/careers/jobs/?department=Infrastructure)，和我們一起建立未來吧。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fbuilding-our-maintenance-scheduler-on-workers%2F&t=Workers%20%E5%A6%82%E4%BD%95%E7%82%BA%E6%88%91%E5%80%91%E7%9A%84%E5%85%A7%E9%83%A8%E7%B6%AD%E8%AD%B7%E8%AA%BF%E5%BA%A6%E7%AE%A1%E7%B7%9A%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8F%B4)[](https://x.com/intent/post?text=Workers+%E5%A6%82%E4%BD%95%E7%82%BA%E6%88%91%E5%80%91%E7%9A%84%E5%85%A7%E9%83%A8%E7%B6%AD%E8%AD%B7%E8%AA%BF%E5%BA%A6%E7%AE%A1%E7%B7%9A%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8F%B4&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://bsky.app/intent/compose?text=Workers+%E5%A6%82%E4%BD%95%E7%82%BA%E6%88%91%E5%80%91%E7%9A%84%E5%85%A7%E9%83%A8%E7%B6%AD%E8%AD%B7%E8%AA%BF%E5%BA%A6%E7%AE%A1%E7%B7%9A%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8F%B4+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://mastodonshare.com/?text=Workers+%E5%A6%82%E4%BD%95%E7%82%BA%E6%88%91%E5%80%91%E7%9A%84%E5%85%A7%E9%83%A8%E7%B6%AD%E8%AD%B7%E8%AA%BF%E5%BA%A6%E7%AE%A1%E7%B7%9A%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8F%B4&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://www.threads.net/intent/post?text=Workers+%E5%A6%82%E4%BD%95%E7%82%BA%E6%88%91%E5%80%91%E7%9A%84%E5%85%A7%E9%83%A8%E7%B6%AD%E8%AD%B7%E8%AA%BF%E5%BA%A6%E7%AE%A1%E7%B7%9A%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8F%B4+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fbuilding-our-maintenance-scheduler-on-workers%2F)

## 相關標籤

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Prometheus](https://blog.cloudflare.com/zh-tw/tag/prometheus/)[可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)[基礎架構](https://blog.cloudflare.com/zh-tw/tag/infrastructure/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
