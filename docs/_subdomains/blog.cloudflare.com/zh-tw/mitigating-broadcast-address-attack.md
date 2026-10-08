---
url: https://blog.cloudflare.com/zh-tw/mitigating-broadcast-address-attack/
title: QUIC \u52d5\u4f5c\uff1a\u4fee\u88dc\u5ee3\u64ad\u4f4d\u5740\u653e\u5927\u6f0f\u6d1e | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:59.069670+00:00
---

# QUIC 動作：修補廣播位址放大漏洞 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/mitigating-broadcast-address-attack/

[部落格](https://blog.cloudflare.com/zh-tw/)

[DDoS](https://blog.cloudflare.com/zh-tw/tag/ddos/)[Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)[HTTP3](https://blog.cloudflare.com/zh-tw/tag/http3/)+3顯示另外 3 個標籤

6 標籤顯示 6 個標籤

  * 文章標籤
  * [DDoS](https://blog.cloudflare.com/zh-tw/tag/ddos/)[Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)[HTTP3](https://blog.cloudflare.com/zh-tw/tag/http3/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[漏洞懸賞](https://blog.cloudflare.com/zh-tw/tag/bug-bounty/)[網路](https://blog.cloudflare.com/zh-tw/tag/network/)
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



[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[漏洞懸賞](https://blog.cloudflare.com/zh-tw/tag/bug-bounty/)[網路](https://blog.cloudflare.com/zh-tw/tag/network/)

[DDoS](https://blog.cloudflare.com/zh-tw/tag/ddos/)[Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)[HTTP3](https://blog.cloudflare.com/zh-tw/tag/http3/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[漏洞懸賞](https://blog.cloudflare.com/zh-tw/tag/bug-bounty/)[網路](https://blog.cloudflare.com/zh-tw/tag/network/)

2025年2月10日

# QUIC 動作：修補廣播位址放大漏洞

![Josephine Chow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW496EEZSG9EMYJFTHPP2Q8A.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![June Slater](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SCBXA2XSNDDC08ZYCVCS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Josephine Chow](https://blog.cloudflare.com/zh-tw/author/josephine-chow/)、[June Slater](https://blog.cloudflare.com/zh-tw/author/june-slater/)、[Bryton Herdes](https://blog.cloudflare.com/zh-tw/author/bryton/)和[Lucas Pardue](https://blog.cloudflare.com/zh-tw/author/lucas/)

閱讀時間：8 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/mitigating-broadcast-address-attack/)和[简体中文](https://blog.cloudflare.com/zh-cn/mitigating-broadcast-address-attack/).

![BLOG-2578 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44YRG2V5KTM9Y6RZ9WG963.png&w=1999&h=1126&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////87vDx4+Tt5+fx8PD28fPz7O7q////////6u312d7w2uH05uv57fD27e7t////////5+z5z9r1ztz53ej96vD57+/x////////6e/+ztz6zN3+3er/7fP+8/P1////////8fb/2uX/2ef/6PP/9fr/+fn6/////////P//6/H/7fT/+f/////////+////////////+vv//v//////////////////////////////////////////////)

一組匿名安全研究人員最近聯絡了 Cloudflare，他們透過 [_QUIC_](https://blog.cloudflare.com/tag/quic) 網際網路衡量研究發現了一個廣播放大漏洞。我們的團隊透過網際網路「公開漏洞懸賞」計畫與這些研究人員合作，努力全面修補影響我們基礎架構的危險漏洞。

收到有關該漏洞的通知後，我們實施了緩解措施來幫助保護我們的基礎架構。根據我們的分析，我們已完全修補此漏洞，且放大媒介不再存在。

### 放大攻擊摘要

QUIC 是一種預設加密的網際網路傳輸通訊協定。它提供與 [_TCP_](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)（傳輸控制通訊協定）和 [_TLS_](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (Transport Layer Security) 等效的功能，同時使用更短的交握序列，幫助減少連線建立時間。QUIC 透過 [_UDP_](https://www.cloudflare.com/en-gb/learning/ddos/glossary/user-datagram-protocol-udp/) (User Datagram Protocol) 執行。

研究人員發現，以廣播 IP 目的地位址為目標的單一用戶端 QUIC [_初始封包_](https://datatracker.ietf.org/doc/html/rfc9000#section-17.2.2)可能會觸發大量初始封包回應。這表現為伺服器 CPU 放大攻擊和反射放大攻擊。

### 傳輸和安全性交握

使用 TCP 和 TLS 時，有兩次交握互動。首先是 TCP 3 向傳輸交握。用戶端向伺服器傳送 SYN 封包，伺服器使用 SYN-ACK 回應用戶端，然後用戶端使用 ACK 進行回應。此過程會驗證用戶端 IP 位址。第二次是 TLS 安全性交握。用戶端將 ClientHello 傳送至伺服器，伺服器執行一些加密操作，並以包含伺服器憑證的 ServerHello 進行回應。用戶端會驗證憑證、確認交握並傳送應用程式流量（例如 HTTP 要求）。

[ _QUIC_](https://datatracker.ietf.org/doc/html/rfc9000#section-7) 遵循類似的過程，但是由於傳輸和安全性交握結合在一起，因此序列更短。用戶端向伺服器傳送包含 ClientHello 的初始封包，伺服器執行一些加密操作，並使用包含具有伺服器憑證之 ServerHello 的初始封包進行回應。用戶端驗證憑證，然後傳送應用程式資料。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2578 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492CZC95G22Z2Z7ANY2TXS.png&w=715&h=512&f=webp&fit=cover&position=center)

QUIC 交握在開始安全性交握之前不需要驗證用戶端 IP 位址。這意味著存在攻擊者可能偽造用戶端 IP 並導致伺服器執行加密工作並將資料傳送到目標受害者 IP（又稱[ _反射攻擊_](https://blog.cloudflare.com/reflections-on-reflections/)）的風險。[ _RFC 9000_](https://datatracker.ietf.org/doc/html/rfc9000) 仔細描述了這種風險並提供了降低風險的機制（請參閱[ _第 8 節_](https://datatracker.ietf.org/doc/html/rfc9000#section-8)和[ _第 9.3.1 節_](https://datatracker.ietf.org/doc/html/rfc9000#section-9.3.1)）。在用戶端位址得到驗證之前，伺服器採用反放大限制，傳送的位元組數最多為所接收位元組數的 3 倍。此外，伺服器可以透過[ _重試封包_](https://datatracker.ietf.org/doc/html/rfc9000#section-8.1.2)進行回應，在進行加密交握之前啟動位址驗證。然而，重試機制為 QUIC 交握序列增加了額外的往返，從而抵消了其與 TCP 相比的一些優勢。現實世界的 QUIC 部署使用一系列策略和啟發式方法來偵測流量負載並啟用不同的緩解措施。

為了瞭解研究人員如何在已有這些 QUIC 防護機制的情況下觸發放大攻擊，我們首先需要深入瞭解 IP 廣播的運作方式。

### 廣播位址

在網際網路通訊協定版本 4 (IPv4) 定址中，任何給定[ _子網路_](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)中的最終位址都是特殊的廣播 IP 位址，用於向 IP 位址範圍內的每個節點傳送封包。同一子網路內的每個節點都會接收傳送到廣播位址的任何封包，使一個傳送者傳送的訊息可能被數百個相鄰節點「聽到」。大多數連線網路的系統預設會啟用此行為，這對於發現相同 IPv4 網路內的裝置至關重要。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2578 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HDDPSHD6HW3WNRSG3HBC.png&w=715&h=334&f=webp&fit=cover&position=center)

廣播位址本質上存在 DDoS 放大風險；每傳送一個封包，都有數百個節點需要處理流量。

### 處理預期廣播

為了對抗廣播位址帶來的風險，大多數路由器預設拒絕來自其 IP 網路外部的封包，這些封包以它們本機連接之網路的廣播位址為目標。廣播封包只允許在同一個 IP 子網路內轉寄，防止來自網際網路的攻擊針對全球的伺服器。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2578 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47FR1ETR6AP7J1HPMPGC5S.png&w=715&h=542&f=webp&fit=cover&position=center)

當給定路由器未直接連接到給定子網路時，通常不會套用相同的技術。只要位址在本機不被視為廣播位址，[ _邊界閘道通訊協定_](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) (BGP) 或其他路由通訊協定就會繼續將來自外部 IP 的流量路由到子網路中的最後一個 IPv4 位址。本質上，這意味著「廣播位址」僅在透過乙太網路連接在一起的路由器和主機的本機範圍內相關。對於網際網路上的路由器和主機來說，廣播 IP 位址的路由方式與任何其他 IP 的路由方式相同。

### 將 IP 位址範圍繫結到主機

每個 Cloudflare 伺服器都應能夠從 Cloudflare 網路中的每個網站提供內容。由於我們的網路使用 [_Anycast_](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) 路由，每個伺服器都必須監聽我們網路上使用的每個 Anycast IP 位址（並能夠從其傳回流量）。

為此，我們利用每個伺服器上的回送介面。與實體網路介面不同，當繫結至回送介面時，給定 IP 位址範圍內的所有 IP 位址都可供主機使用（並將由核心在本機處理）。

其運作機制很簡單。在傳統的路由環境中，採用[ _最長前置詞比對_](https://en.wikipedia.org/wiki/Longest_prefix_match)來選擇路由。在最長前置詞比對下，將選擇指向更具體的 IP 位址區塊（例如 192.0.2.96/29，8 個位址範圍）的路由，而不是指向不太具體的 IP 位址區塊（例如 192.0.2.0/24，256 個位址範圍）的路由。

雖然 Linux 使用最長前置詞比對，但它會在立即搜尋相符項之前查閱額外的步驟：路由原則資料庫 (RPDB)。RPDB 包含路由表清單，其中可能包含路由資訊及其各自的優先順序。預設 RPDB 如下所示：
    
    
    $ ip rule show
    0:	from all lookup local
    32766:	from all lookup main
    32767:	from all lookup default

Linux 將按數字升序查詢每個路由表，以嘗試找到相符的路由。找到一個之後，將終止搜尋並立即使用該路由。

如果您以前使用過 Linux 上的路由規則，那麼您可能很熟悉 main 表格的內容。與名為「default」的資料表相反，「main」通常充當預設查閱表格。它也包含傳統上與路由表資訊相關的內容：
    
    
    $ ip route show table main
    default via 192.0.2.1 dev eth0 onlink
    192.0.2.0/24 dev eth0 proto kernel scope link src 192.0.2.2

然而，這並不是給定查找將查閱的第一個路由表，第一個路由表是本機表格：
    
    
    $ ip route show table local
    local 127.0.0.0/8 dev lo proto kernel scope host src 127.0.0.1
    local 127.0.0.1 dev lo proto kernel scope host src 127.0.0.1
    broadcast 127.255.255.255 dev lo proto kernel scope link src 127.0.0.1
    local 192.0.2.2 dev eth0 proto kernel scope host src 192.0.2.2
    broadcast 192.0.2.255 dev eth0 proto kernel scope link src 192.0.2.2

在表格中，我們看到了兩種新類型的路由——本機路由和廣播路由。顧名思義，這些路由決定了兩個截然不同的功能：在本機處理的路由和將導致廣播封包的路由。本機路由提供所需的功能——任何帶有本機路由的前置詞都會具有核心處理的範圍內的所有 IP 位址。廣播路由將導致封包被廣播到給定範圍內的所有 IP 位址。當 IP 位址繫結到介面時，會自動新增這兩種類型的路由（並且，當範圍繫結到回送 (lo) 介面時，範圍本身將被新增為本機路由）。

### 發現漏洞

QUIC 的部署高度依賴於它們所在的負載平衡和封包轉寄基礎架構。儘管 QUIC 的 RFC 描述了風險和緩解措施，但根據伺服器部署的性質，仍然可能存在攻擊媒介。報告研究人員研究了網際網路上的 QUIC 部署，發現向 Cloudflare 的一個廣播位址傳送 QUIC 初始封包會觸發大量回應。回應資料總量超過了 RFC 的 3 倍放大限制。

查看 Cloudflare 範例系統的本機路由表，我們發現了一個潛在的罪魁禍首：
    
    
    $ ip route show table local
    local 127.0.0.0/8 dev lo proto kernel scope host src 127.0.0.1
    local 127.0.0.1 dev lo proto kernel scope host src 127.0.0.1
    broadcast 127.255.255.255 dev lo proto kernel scope link src 127.0.0.1
    local 192.0.2.2 dev eth0 proto kernel scope host src 192.0.2.2
    broadcast 192.0.2.255 dev eth0 proto kernel scope link src 192.0.2.2
    local 203.0.113.0 dev lo proto kernel scope host src 203.0.113.0
    local 203.0.113.0/24 dev lo proto kernel scope host src 203.0.113.0
    broadcast 203.0.113.255 dev lo proto kernel scope link src 203.0.113.0

在此範例系統上，Anycast 前置詞 203.0.113.0/24 已透過使用標準工具繫結到回送介面 (lo)。該工具嚴格遵循 IPv4 標準，為介面指派了兩種特殊類型的路由：用於 IP 範圍本身的本機路由和用於範圍內最終位址的廣播路由。

雖然會按預期對前往我們路由器直連子網路廣播位址的流量進行篩選，但針對我們路由之 Anycast 前置詞的廣播流量仍會自行到達我們的伺服器。通常，到達回送介面的廣播流量幾乎不會引起問題。繫結到整個範圍內特定連接埠的服務將接收傳送到廣播位址的資料並繼續正常運作。不幸的是，當打破正常的預期時，這個相對簡單的特性就會失效。

Cloudflare 的前端由多個 Worker 處理序組成，每個處理序獨立地繫結至 UDP 連接埠 443 上的整個 Anycast 範圍。為了讓多個處理序能夠繫結到同一個連接埠，我們使用 SO_REUSEPORT 通訊端選項。雖然 SO_REUSEPORT [_有其他好處_](https://blog.cloudflare.com/the-sad-state-of-linux-socket-balancing/)，但它也會導致傳送到廣播位址的流量被複製到每個接聽程式。

每個 QUIC 伺服器 Worker 都獨立運作。每一個都對同一個用戶端 Initial 做出反應，在伺服器端重複工作並向用戶端的 IP 位址產生回應流量。因此，單個封包就可能觸發顯著的放大。雖然具體情況會因實作而異，但在 128 核心系統上，典型的每個核心一個接聽程式堆疊（這會為回應假定的逾時而傳送重試）可能導致對傳送到廣播位址的每個封包產生並傳送 384 個回覆。

儘管研究人員展示了針對 QUIC 的這種攻擊，但底層漏洞可能會影響以相同方式使用通訊端的其他 UDP 要求/回應通訊協定。

### 緩解

作為一種通訊方法，廣播通常不適合用於 Anycast 前置詞。因此，緩解該問題的最簡單方法就是針對每個範圍中的最終位址停用廣播功能。

理想情況下，這可以透過修改我們的工具來實現，僅在本機路由表中新增本機路由，而完全跳過廣播路由的包含。不幸的是，執行此操作的唯一可行機制是修補和維護我們自己的 iproute2 套件內部分支，但這對於當前的問題來說是一個相當麻煩的解決方案。

因此，我們決定專注於移除路由本身。與任何其他路由類似，可以使用標準工具將其移除：
    
    
    $ sudo ip route del 203.0.113.255 table local

為了大規模實現這一點，我們對部署系統進行了相對較小的變更：
    
    
      {%- for lo_route in lo_routes %}
        {%- if lo_route.type == "broadcast" %}
            # All broadcast addresses are implicitly ipv4
            {%- do remove_route({
            "dev": "lo",
            "dst": lo_route.dst,
            "type": "broadcast",
            "src": lo_route.src,
            }) %}
        {%- endif %}
      {%- endfor %}

這樣做之後，我們可以有效地確保移除連接到回送介面的所有廣播路由，確保同等對待規範定義的廣播位址與範圍內的任何其他位址，從而降低風險。

### 後續步驟

雖然該漏洞明確影響了我們 Anycast 範圍內的廣播位址，但它可能會擴展到我們的基礎架構之外。如果未採取緩解措施，那麼只要基礎架構符合特定的嚴格技術標準（基於 UDP 的多 Worker、多接聽程式服務，繫結到附加了可路由 IP 前置詞之機器上的所有 IP 位址，並以這樣的方式暴露廣播位址），就會受到影響。我們鼓勵網路管理員和安全專業人員評估他們的系統，尋找可能存在本機放大攻擊媒介的設定。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmitigating-broadcast-address-attack%2F&t=QUIC%20%E5%8B%95%E4%BD%9C%EF%BC%9A%E4%BF%AE%E8%A3%9C%E5%BB%A3%E6%92%AD%E4%BD%8D%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E)[](https://x.com/intent/post?text=QUIC+%E5%8B%95%E4%BD%9C%EF%BC%9A%E4%BF%AE%E8%A3%9C%E5%BB%A3%E6%92%AD%E4%BD%8D%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmitigating-broadcast-address-attack%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmitigating-broadcast-address-attack%2F)[](https://bsky.app/intent/compose?text=QUIC+%E5%8B%95%E4%BD%9C%EF%BC%9A%E4%BF%AE%E8%A3%9C%E5%BB%A3%E6%92%AD%E4%BD%8D%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmitigating-broadcast-address-attack%2F)[](https://mastodonshare.com/?text=QUIC+%E5%8B%95%E4%BD%9C%EF%BC%9A%E4%BF%AE%E8%A3%9C%E5%BB%A3%E6%92%AD%E4%BD%8D%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmitigating-broadcast-address-attack%2F)[](https://www.threads.net/intent/post?text=QUIC+%E5%8B%95%E4%BD%9C%EF%BC%9A%E4%BF%AE%E8%A3%9C%E5%BB%A3%E6%92%AD%E4%BD%8D%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmitigating-broadcast-address-attack%2F)

## 相關標籤

[DDoS](https://blog.cloudflare.com/zh-tw/tag/ddos/)[Edge](https://blog.cloudflare.com/zh-tw/tag/edge/)[HTTP3](https://blog.cloudflare.com/zh-tw/tag/http3/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[漏洞懸賞](https://blog.cloudflare.com/zh-tw/tag/bug-bounty/)[網路](https://blog.cloudflare.com/zh-tw/tag/network/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Bryton Herdes](https://blog.cloudflare.com/zh-tw/author/bryton/)

[](https://next-hopself.net/)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
