---
url: https://blog.cloudflare.com/zh-tw/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/
title: \u4f7f\u7528 ORIGIN Frames \u5be6\u73fe\u9023\u7dda\u5408\u4f75\uff1a\u6e1b\u5c11 DNS \u67e5\u8a62\uff0c\u6e1b\u5c11\u9023\u7dda\u6578 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:02.676252+00:00
---

# 使用 ORIGIN Frames 實現連線合併：減少 DNS 查詢，減少連線數 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/

[部落格](https://blog.cloudflare.com/zh-tw/)

[DNS](https://blog.cloudflare.com/zh-tw/tag/dns/)[HTTP2](https://blog.cloudflare.com/zh-tw/tag/http2/)[Internship Experience](https://blog.cloudflare.com/zh-tw/tag/internship-experience/)+3顯示另外 3 個標籤

6 標籤顯示 6 個標籤

  * 文章標籤
  * [DNS](https://blog.cloudflare.com/zh-tw/tag/dns/)[TLS](https://blog.cloudflare.com/zh-tw/tag/tls/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)[速度與可靠性](https://blog.cloudflare.com/zh-tw/tag/speed-and-reliability/)
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



[TLS](https://blog.cloudflare.com/zh-tw/tag/tls/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)[速度與可靠性](https://blog.cloudflare.com/zh-tw/tag/speed-and-reliability/)

[DNS](https://blog.cloudflare.com/zh-tw/tag/dns/)[HTTP2](https://blog.cloudflare.com/zh-tw/tag/http2/)[Internship Experience](https://blog.cloudflare.com/zh-tw/tag/internship-experience/)[TLS](https://blog.cloudflare.com/zh-tw/tag/tls/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)[速度與可靠性](https://blog.cloudflare.com/zh-tw/tag/speed-and-reliability/)

2023年9月4日

# 使用 ORIGIN Frames 實現連線合併：減少 DNS 查詢，減少連線數

![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Suleman Ahmad](https://blog.cloudflare.com/zh-tw/author/suleman/)、[Jonathan Hoyland](https://blog.cloudflare.com/zh-tw/author/jonathan-hoyland/)和[Sudheesh Singanamalla](https://blog.cloudflare.com/zh-tw/author/sudheesh/)

閱讀時間：13 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[Deutsch](https://blog.cloudflare.com/de-de/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[Français](https://blog.cloudflare.com/fr-fr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[日本語](https://blog.cloudflare.com/ja-jp/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[한국어](https://blog.cloudflare.com/ko-kr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)和[简体中文](https://blog.cloudflare.com/zh-cn/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/).

![Connection coalescing with ORIGIN Frames: fewer DNS queries, fewer connections](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HDJ2ZAZ6FJXTRPX0N4CN.png&w=1600&h=889&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vfi+fHe7eTV593R6+LU8OrZ7unW5eHN//vn+/Xi8Oja6uHW7eXZ8uzc8OvZ6OTS///s//ro9O3h7ubd8enf9e/i8+/f7OnX///y///u+fPn8+zj9e7l+vTo+PTl8e7d///2///z/vfr+PHn+vTq//nt/fnq9fLi///5///1//vt/PTq//ju//7x//3u+fbl///7///3//3v//fs//vw///0///w/Pnn///8///3//3v//js//zx///1///x/fno)

_本部落格報告並總結了 ACM_ [_Internet Measurement Conference_](https://conferences.sigcomm.org/imc/2022/program/) _上發表的 Cloudflare_ _[研究論文](https://research.cloudflare.com/publications/Singanamalla2022/)的內容，該論文對使用 ORIGIN Frames 實現的連線合併進行了測量和原型設計。_

有些讀者可能會驚訝地發現，對一個網頁的單次存取會導致瀏覽器進行數十次，有時甚至數百次 Web 連線。以本部落格為例。如果您是第一次存取 Cloudflare 部落格，或者距離上次存取已經有一段時間了，您的瀏覽器會進行多次連線來呈現頁面。瀏覽器將進行 DNS 查詢，以找到與 blog.cloudflare.com 相對應的 IP 位址，然後發出後續請求，以擷取為成功呈現完整頁面所需的網頁上的任何必要子資源。有多少？請看下面，在撰寫本文時，有 32 個不同的主機名稱用於載入Cloudflare 部落格。這意味著需要 32 次 DNS 查詢和_至少_ 32 個 TCP（或 QUIC）連線，除非用戶端能夠重複使用（或合併）其中的一些連線。

每個新的 Web 連線不僅會給伺服器的處理能力帶來額外負擔（在使用高峰期可能導致可擴展性挑戰），而且還會向網路暴露用戶端中繼資料，例如個人正在存取的純文字主機名稱。此類中繼資訊可能會向路徑上的網路對手和竊聽者洩露使用者的線上活動和瀏覽行為！

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - ckxTYV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47N3FXQ0TE0F5BAWC0YQTS.png&w=715&h=409&f=webp&fit=cover&position=center)

在本部落格中，我們將對「連線合併」進行更深入的探討。自 [2021 年首次研究基於 IP 的合併](https://blog.cloudflare.com/connection-coalescing-experiments/)以來，我們在網際網路上進行了進一步的大規模測量和建模，以瞭解和預測合併是否可行以及在何處最有效。由於 IP 合併難以大規模管理，因此去年我們實作並試驗了一項有前景的標準，稱為 [HTTP/2 ORIGIN Frame 延伸](https://datatracker.ietf.org/doc/rfc8336/)，我們利用該標準將連線合併到我們的邊緣，而無需擔心管理 IP 位址。

總而言之，許多大型提供者都錯失了一些機會。我們希望此部落格（以及我們在 ACM IMC 2022 上發佈的包含完整詳細資訊的[出版物](https://research.cloudflare.com/publications/Singanamalla2022/)）能邁出第一步，幫助伺服器和用戶端利用 ORIGIN Frame 標準。

### 做好準備

在高層次上，當使用者瀏覽 Web 時，瀏覽器透過擷取相關子資源來構建完整的網頁，從而呈現網頁。這一過程與工廠組裝實物產品的方式極為相似。從這個意義上說，現代網頁可以被視為一個裝配廠。它依賴於生產最終產品所需的資源「供應鏈」。

現實世界中的裝配廠可以使用一個訂單來購買不同零件，並讓供應商一次性發貨所有零件（類似於最大化價值和最小化回應時間的[配套流程](https://www.sciencedirect.com/science/article/abs/pii/092552739290109K)）；無論這些零件的製造商或產地如何，只需與供應商建立一個「連線」即可。從供應商到裝配廠的任何一輛卡車都可以裝滿來自多個製造商的零件。

Web 的設計導致瀏覽器通常會做相反的事情。要擷取網頁上的影像、JavaScript 和其他資源（零件），Web 用戶端（裝配廠）必須與伺服器（供應商）返回的 HTML 中定義的每個主機名稱（製造商）_至少_建立一個連線。與這些主機名稱的連線是否前往同一伺服器，這並沒有什麼影響，例如它們可以前往 Cloudflare 等[反向代理](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)。對於每個製造商來說，需要一輛「新」卡車將材料從同一供應商轉移到裝配廠，或者更正式地說，需要建立一個新連線，以從同一網頁上的主機名稱請求子資源。

沒有連線合併

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Without connection coalescing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46818DS1DBPGY0C4DKT15E.png&w=715&h=305&f=webp&fit=cover&position=center)

用於載入網頁的連線數量可能高得驚人。子資源還需要其他子資源也是很常見的，因此前面的連線可能還會產生新的連線。還要記住，與主機名稱的 HTTP 連線通常先於 DNS 查詢！連線合併使我們能夠使用更少的連線_，或者「重複使用」同一組卡車從單個供應商運輸來自多個製造商的零件。_

有連線合併

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![With connection coalescing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GJXTQ9MV673E7RD0JDJG.png&w=715&h=305&f=webp&fit=cover&position=center)

### 連線合併原則

連線合併[在 HTTP/2 中引入](https://datatracker.ietf.org/doc/html/rfc7540)，並延續到 [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html#name-connection-reuse) 中。我們[之前](https://blog.cloudflare.com/connection-coalescing-experiments/)曾在部落格中討論過連線合併（建議您閱讀該部落格以獲得詳細的入門知識）。雖然這個想法很簡單，但實作它可能會帶來許多工程挑戰。例如，回想一下上面的內容，（在撰寫本文時）有 32 個不同的主機名稱用於載入您現在正在閱讀的網頁。32 個主機名稱中有 16 個唯一網域（定義為「有效 [TLD+1](https://www.cloudflare.com/learning/dns/top-level-domain/)」）。我們能否為每個唯一網域建立更少的連線或「合併」現有連線？答案是「 _可以，但這取決於具體情況_ 」。

載入部落格頁面的確切連線數並不明顯，也很難知道。可能有 32 個主機名稱連接到 16 個網域，但與直覺相反，這並不意味著「有多少個唯一連線？」的答案是 16。如果所有主機名稱都可以透過一台伺服器存取，那麼真正的答案可能是只有_一個_連線；如果存取每個主機名稱都需要不同的伺服器，那麼真正的答案可能是多達 32 個獨立連線。

連線重複使用有多種形式，因此在 HTTP 領域定義「連線合併」非常重要。例如，重複使用一個主機名稱的現有 [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) 或 TLS 連線來多次請求_**同一** _主機名稱的子資源，這屬於連線重複使用，但不屬於合併。

當某些主機名稱的現有 TLS 通道可以重新調整用途或用於連接到_**不同的** _主機名稱時，就會發生合併。例如，存取 blog.cloudflare.com 時，HTML 指向 cdnjs.cloudflare.com 上的子資源。要為子資源重用相同的 TLS 連線，兩個主機名稱必須一起出現在 TLS 憑證的「[伺服器備用名稱 (SAN)](https://en.wikipedia.org/wiki/Subject_Alternative_Name)」清單中，但僅此一步不足以說服瀏覽器合併。畢竟，儘管使用相同的憑證，但可能能夠從同一伺服器存取 blog.cloudflare.com 和 cdnjs.cloudflare.com 服務，也可能無法從同一伺服器存取二者。那麼瀏覽器怎麼知道呢？僅當伺服器設定正確的條件時，合併才起作用，但用戶端必須決定是否合併——因此，瀏覽器需要一個訊號才能在憑證上的 SAN 清單之外進行合併。重溫我們的比喻，裝配廠可能會直接從製造商訂購零件，卻不知道供應商的倉庫中已經有了同樣的零件。

瀏覽器可以使用兩種明確的訊號來決定是否可以合併連線：一種是基於 IP 的訊號，另一種是基於 ORIGIN Frame 的訊號。前者要求伺服器營運商將 DNS 記錄與伺服器上可用的 HTTP 資源緊密綁定。這很難管理和部署，而且實際上會產生有風險的依賴，因為必須將所有資源放在特定的一組或單一 IP 位址後面。IP 位址影響合併決策的方式[因瀏覽器而異](https://daniel.haxx.se/blog/2016/08/18/http2-connection-coalescing/)，有些瀏覽器更保守，有些則更寬容。另外，對於伺服器來說，HTTP ORIGIN Frame 是一種更容易協調的訊號；它也很靈活，而且可以在不中斷服務的情況下優雅地失效（對於符合規範的實作）。

這兩種合併訊號之間的根本區別是：基於 IP 的合併訊號是隱含的，甚至是偶然的，並迫使用戶端推斷是否存在合併可能性。這一切都不足為奇，因為 IP 位址的設計方式，其內容與名稱[並無實際關係](https://blog.cloudflare.com/addressing-agility/)！相比之下，ORIGIN Frame 是從伺服器到用戶端的明確訊號，即無論 DNS 對任何特定主機名稱有何規定，都可以進行合併。

我們之前已經嘗試過[基於 IP 的合併](https://blog.cloudflare.com/connection-coalescing-experiments/)；在這篇部落格中，我們將更深入地探討基於 ORIGIN Frame 的合併。

### 什麼是 ORIGIN Frame 標準？

ORIGIN Frame 是 [HTTP/2](https://www.rfc-editor.org/rfc/rfc8336) 和 [HTTP/3](https://www.rfc-editor.org/rfc/rfc9412) 規範的延伸，是分別在 stream 0 或連線的控制流上傳送的特殊幀。該幀允許伺服器在已建立的_現有_ TLS 連線上向用戶端傳送「origin-set」，其中包括已授權的主機名稱，並且不會產生任何 [HTTP 421 錯誤](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/421)。origin-set 中的主機名稱也必須出現在伺服器的憑證 SAN 清單中，即使這些主機名稱是透過 DNS 在不同的 IP 位址上公告的。

具體來說，需要兩個不同的步驟：

  1. Web 伺服器必須傳送一個清單，列舉 ORIGIN Frame 延伸中的 Origin Set（給定連線可能用於的主機名稱）。
  2. Web 伺服器傳回的 TLS 憑證必須涵蓋 DNS 名稱 SAN 項目中 ORIGIN Frame 中傳回的其他主機名稱。



從高層次來看，ORIGIN Frames 是 TLS 憑證的補充，營運商可以附加該憑證來表示「嘿，用戶端，這是此連線上可用的 SAN 中的名稱——您可以合併！」由於 ORIGIN Frame 不是憑證本身的一部分，因此可以獨立變更其內容。不需要新的憑證。也不依賴於 IP 位址。對於可合併的主機名稱，現有的 TCP/QUIC+TLS 連線可以重複使用，而不需要新的連線或 DNS 查詢。

[如今許多網站](https://w3techs.com/technologies/overview/proxy)都依賴 CDN 提供的內容，例如 Cloudflare CDN 服務。使用外部 CDN 服務的做法為網站提供了速度、可靠性的優勢，並減少了其[來源伺服器](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)提供的內容負載。當網站和資源都由同一個 CDN 提供服務時，儘管主機名稱不同、屬於不同的實體，但它為 CDN 營運商提供了一些非常有趣的機會，允許重複使用和合併連線，因為他們可以控制憑證管理和代表真正的原始伺服器傳送 ORIGIN Frame 的連線請求。

遺憾的是，我們還沒有辦法將 ORIGIN Frame 帶來的可能性付諸實踐。據我們所知，到目前為止，還沒有伺服器實作支援 ORIGIN Frames。在所有瀏覽器中，只有 Firefox 支援 ORIGIN Frames。由於 IP 合併具有挑戰性，而 ORIGIN Frame 沒有部署的支援，那麼為更好地支援合併而投入的工程時間和精力是否值得？我們決定透過大規模的網際網路測量來瞭解機會和預測可能性，然後實作 ORIGIN Frame，在生產流量上進行實驗。

### 實驗 1：所需變更的規模有多大？

2021 年 2 月，我們在 100 個虛擬機器上使用修改後的[網頁測試](https://github.com/WPO-Foundation/webpagetest)收集了網際網路上 50 萬個[最受歡迎網站](https://radar.cloudflare.com/domains)的[資料](https://blog.cloudflare.com/connection-coalescing-experiments/)。每次造訪網頁時都會啟動一個自動 Chrome (v88) 瀏覽器執行個體，以消除快取效應（因為我們想要瞭解合併，而不是快取）。在成功完成每個工作階段後，我們使用 Chrome 開發人員工具擷取頁面載入資料並將其寫入 HTTP 封存格式 (HAR) 檔案，其中包含完整的事件時間線以及有關憑證及其驗證的其他資訊。此外，我們還剖析了根網頁的憑證鏈以及由子資源請求觸發的新 TLS 連接，以：(i) 識別主機名稱的憑證頒發者；(ii) 檢查主題備用名稱 (SAN) 擴充功能是否存在；以及 (iii) 驗證 DNS 名稱是否解析為所使用的 IP 位址。有關我們的方法和結果的更多詳細資訊，請參閱技術[論文](https://research.cloudflare.com/publications/Singanamalla2022/)。

第一步是瞭解網頁需要哪些資源才能成功呈現網頁內容，以及這些資源在網際網路上的位置。當子資源網域處於理想的共同位置時，連線合併就成為可能。我們透過查找相應的自發系統 (AS) 來大概確定網域的位置。例如，連接到 [cdnjs](https://cdnjs.cloudflare.com/https://cdnjs.cloudflare.com/) 的網域可透過 BGP 路由表中的 AS 13335 到達，而該 AS 號碼屬於 Cloudflare。下圖描述了完全載入一個網頁所需的網頁百分比和唯一 AS 號碼。

大約 14% 的網頁需要兩個 AS 才能完全載入，即網頁需要依賴另外一個 AI 來獲得子資源。超過 50% 的網頁需要聯絡不超過 6 個 AS 來獲取所有必需的子資源。如上圖所示，這一發現意味著相對少數的營運商提供大多數（約 50%）網站所需的子資源內容，並且任何使用 ORIGIN Frames 的情況都只需要進行少量變更就能產生預期的影響。因此，連線合併的可能性可以樂觀地估計為擷取網頁中所有子資源所需的唯一 AS 的數量。不過，在實際操作中，這可能會被 SLA 等操作因素所取代，或者受到我們[之前在 Cloudflare](https://research.cloudflare.com/publications/Fayed2021/) 處理過的通訊端、名稱和 IP 位址之間的靈活對應的幫助。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - 3Dlhpw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45X8GDMJVMT39D8F70E2T1.png&w=715&h=349&f=webp&fit=cover&position=center)

然後，我們嘗試瞭解合併對連線指標的影響。根據 CDF 匯總了載入網頁所需的 DNS 查詢和 TLS 連線的測量數量和理想數量，如下圖所示。

透過建模和大量分析，我們發現透過 ORIGIN Frames 進行連線合併可將瀏覽器建立的 DNS 和 TLS 連線數量減少 60% 以上（以中位數計算）。我們透過識別用戶端請求 DNS 記錄的次數來進行建模，並將其與要提供的理想 ORIGIN Frames 服務相結合。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - DZcmqU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48T1Y598J42C2CVMPC1M33.png&w=715&h=394&f=webp&fit=cover&position=center)

許多多來源伺服器（如 [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) 運作的伺服器）傾向於重複使用憑證，並透過多個 DNS SAN 項目提供相同的憑證。這樣，營運商就可以在建立和更新週期內管理較少的憑證。雖然從理論上講，憑證中可以包含數百萬個名稱，但建立這樣的憑證是不合理的，也很難有效管理。如下圖所示，透過繼續依賴現有憑證，我們的建模測量揭示了實現完美合併所需的變更量，同時提供了所需變更規模的資訊。

我們發現，超過 60% 的網站提供的憑證不需要任何修改，就可以從 ORIGIN Frames 中受益，而在憑證中新增不超過 10 個 DNS SAN 名稱的情況下，我們能夠成功地將連線合併到所測量網站中超過 92% 的網站。CDN 提供者可以透過在每個憑證中新增三到四個最受歡迎的請求主機名稱來進行最有效的變更。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - 3Eev4N](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47R6AZHNG2GYF9CH2S97M9.png&w=715&h=398&f=webp&fit=cover&position=center)

### 實驗 2：ORIGIN Frames 實際應用

為了驗證我們的建模預期，我們在 2022 年初採取了更積極的方法。我們的下一個實驗重點關注 5,000 個廣泛使用 _cdnjs.cloudflare.com_ 作為子資源的網站。透過修改我們的實驗性 TLS 終止端點，我們部署了 [RFC 標準](https://datatracker.ietf.org/doc/rfc8336/)中定義的 HTTP/2 ORIGIN Frame 支援。這涉及到變更 Golang 的 _net_ 和 _http_ 相依性模組的內部分支（已開放原始碼，請[參見此處](https://github.com/cloudflare/go-originframe)和[此處](https://github.com/cloudflare/net-originframe)）。

在實驗期間，連接到實驗組中的網站將在 ORIGIN Frame 中傳回 _cdnjs.cloudflare.com_ ，而控制組則傳回任意（未使用的）主機名稱。5000 個網站的所有現有邊緣憑證也被修改。對於實驗組，更新了相應的憑證，並將 _cdnjs.cloudflare.com_ 新增到 SAN。為了確保控制組和實驗組之間的完整性，還使用未被任何控制網域使用的有效且相同大小的第三方網域來更新控制組網域憑證。這樣做是為了確保憑證的相對大小變化保持恒定，避免由於不同的憑證大小而導致的潛在偏差。我們的結果是驚人的！

對實驗中從 Firefox 收到的網站請求的 1% 進行採樣，我們發現**每秒新的 TLS 連線數減少了 50%** 以上，這表明用戶端執行的加密驗證操作數量，伺服器運算開銷也減少了。正如預期的那樣，控制組沒有差異，表明 CDN 或伺服器營運商看到了連線重複使用的有效性。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - q0fWGU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45GKTR9B46ZHYNCDK42GGC.png&w=715&h=399&f=webp&fit=cover&position=center)

### 討論和見解

雖然我們的建模測量結果表明，我們可以期望一些效能改進，但實際上效能並沒有明顯改善，這表明「不會變差」才是有關效能的正確心態。資源物件大小、競爭連線和擁塞控制之間微妙的相互作用取決於網路條件。例如，隨著競爭網路連結上瓶頸資源的連線減少，瓶頸共用容量也會減少。隨著越來越多的營運商在其伺服器上部署對 ORIGIN Frames 的支援，重新研究這些測量結果將是非常有意義的。

除了效能之外，ORIGIN Frames 的一大優勢是隱私性。怎麼實現呢？嗯，每個合併連線都會隱藏用戶端中繼資料，若沒有連線合併，這些中繼資料就會從未合併的連線中洩漏出去。網頁上某些資源的載入取決於人們與網站互動的方式。這意味著對於從伺服器擷取某些資源的每個新連線，如果透過連接埠 53 上的 UDP 或 TCP 傳輸，則 [SNI](https://www.cloudflare.com/learning/ssl/what-is-sni/) 之類的 TLS 純文字中繼資料（在沒有 [Encrypted Client Hello](https://blog.cloudflare.com/encrypted-client-hello/) 的情況下）和至少一個純文字 DNS 查詢會暴露給網路。合併連線有助於消除瀏覽器開啟新 TLS 連線的需要，以及執行額外 DNS 查詢的需要。這可以防止網路監聽者洩露中繼資料。ORIGIN Frames 有助於最大限度地減少來自網路路徑的訊號，透過減少洩露給網路竊聽者的純文字資訊量來提高隱私性。

瀏覽器可以從減少驗證多個憑證所需的加密計算中獲益，但它的一個主要優勢在於，它為端點（瀏覽器和來源伺服器）的資源排程開闢了非常有趣的未來機會，例如[優先順序](https://blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/)，或最近提出的 [HTTP Early Hints](https://blog.cloudflare.com/early-hints/) 等建議，這用於提供一種用戶端體驗，使連線不會超載或競爭這些資源。如果與 [CERTIFICATE Frames](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-http2-secondary-certs-06#section-3.4) IETF 草案相結合，我們就能進一步消除手動修改憑證的需要，因為伺服器可以在建立連線後證明其對主機名稱的授權，而無需在網站的 TLS 憑證上新增任何額外的 SAN 項目。

### 總結與行動號召

總之，只需對憑證及其伺服器基礎架構稍作改動，當前的網際網路生態系統就能為連線合併提供大量機會。伺服器可將 TLS 交握的次數大幅減少約 50%，同時將封鎖 DNS 查詢的轉譯次數減少 60% 以上。此外，用戶端還可以透過減少純文字 DNS 對網路監視者的暴露來獲得隱私方面的好處。

為了協助實現這一目標，我們目前正計劃為客戶新增對 HTTP/2 和 HTTP/3 ORIGIN Frames 的支援。我們也鼓勵其他管理第三方資源的營運商採用 ORIGIN Frames 支援，以改善網際網路生態系統。我們提交的論文已被 2022 年 ACM Internet Measurement Conference 接受，[可供下載](https://research.cloudflare.com/publications/Singanamalla2022/)。如果您想參與這樣的專案，親眼見證新標準的誕生，請造訪我們的[招聘頁面](https://www.cloudflare.com/careers/)！

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F&t=%E4%BD%BF%E7%94%A8%20ORIGIN%20Frames%20%E5%AF%A6%E7%8F%BE%E9%80%A3%E7%B7%9A%E5%90%88%E4%BD%B5%EF%BC%9A%E6%B8%9B%E5%B0%91%20DNS%20%E6%9F%A5%E8%A9%A2%EF%BC%8C%E6%B8%9B%E5%B0%91%E9%80%A3%E7%B7%9A%E6%95%B8)[](https://x.com/intent/post?text=%E4%BD%BF%E7%94%A8+ORIGIN+Frames+%E5%AF%A6%E7%8F%BE%E9%80%A3%E7%B7%9A%E5%90%88%E4%BD%B5%EF%BC%9A%E6%B8%9B%E5%B0%91+DNS+%E6%9F%A5%E8%A9%A2%EF%BC%8C%E6%B8%9B%E5%B0%91%E9%80%A3%E7%B7%9A%E6%95%B8&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://bsky.app/intent/compose?text=%E4%BD%BF%E7%94%A8+ORIGIN+Frames+%E5%AF%A6%E7%8F%BE%E9%80%A3%E7%B7%9A%E5%90%88%E4%BD%B5%EF%BC%9A%E6%B8%9B%E5%B0%91+DNS+%E6%9F%A5%E8%A9%A2%EF%BC%8C%E6%B8%9B%E5%B0%91%E9%80%A3%E7%B7%9A%E6%95%B8+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://mastodonshare.com/?text=%E4%BD%BF%E7%94%A8+ORIGIN+Frames+%E5%AF%A6%E7%8F%BE%E9%80%A3%E7%B7%9A%E5%90%88%E4%BD%B5%EF%BC%9A%E6%B8%9B%E5%B0%91+DNS+%E6%9F%A5%E8%A9%A2%EF%BC%8C%E6%B8%9B%E5%B0%91%E9%80%A3%E7%B7%9A%E6%95%B8&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://www.threads.net/intent/post?text=%E4%BD%BF%E7%94%A8+ORIGIN+Frames+%E5%AF%A6%E7%8F%BE%E9%80%A3%E7%B7%9A%E5%90%88%E4%BD%B5%EF%BC%9A%E6%B8%9B%E5%B0%91+DNS+%E6%9F%A5%E8%A9%A2%EF%BC%8C%E6%B8%9B%E5%B0%91%E9%80%A3%E7%B7%9A%E6%95%B8+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)

## 相關標籤

[DNS](https://blog.cloudflare.com/zh-tw/tag/dns/)[HTTP2](https://blog.cloudflare.com/zh-tw/tag/http2/)[Internship Experience](https://blog.cloudflare.com/zh-tw/tag/internship-experience/)[TLS](https://blog.cloudflare.com/zh-tw/tag/tls/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)[速度與可靠性](https://blog.cloudflare.com/zh-tw/tag/speed-and-reliability/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Sudheesh Singanamalla](https://blog.cloudflare.com/zh-tw/author/sudheesh/)

[](https://sudheesh.info/)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
