---
url: https://blog.cloudflare.com/zh-tw/tcp-resets-timeouts/
title: \u5c07\u5c0d TCP \u91cd\u8a2d\u548c\u903e\u6642\u7684\u6df1\u5165\u89e3\u6790\u5f15\u5165 Cloudflare Radar | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:16.895718+00:00
---

# 將對 TCP 重設和逾時的深入解析引入 Cloudflare Radar | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/tcp-resets-timeouts/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Radar](https://blog.cloudflare.com/zh-tw/tag/cloudflare-radar/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)[網際網路品質](https://blog.cloudflare.com/zh-tw/tag/internet-quality/)+1顯示另外 1 個標籤

4 標籤顯示 4 個標籤

  * 文章標籤
  * [Radar](https://blog.cloudflare.com/zh-tw/tag/cloudflare-radar/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)[網際網路品質](https://blog.cloudflare.com/zh-tw/tag/internet-quality/)[網際網路流量](https://blog.cloudflare.com/zh-tw/tag/internet-traffic/)
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



[網際網路流量](https://blog.cloudflare.com/zh-tw/tag/internet-traffic/)

[Radar](https://blog.cloudflare.com/zh-tw/tag/cloudflare-radar/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)[網際網路品質](https://blog.cloudflare.com/zh-tw/tag/internet-quality/)[網際網路流量](https://blog.cloudflare.com/zh-tw/tag/internet-traffic/)

2024年9月5日

# 將對 TCP 重設和逾時的深入解析引入 Cloudflare Radar

![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Luke Valenta](https://blog.cloudflare.com/zh-tw/author/luke/)

閱讀時間：20 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/tcp-resets-timeouts/)、[日本語](https://blog.cloudflare.com/ja-jp/tcp-resets-timeouts/)、[한국어](https://blog.cloudflare.com/ko-kr/tcp-resets-timeouts/)和[简体中文](https://blog.cloudflare.com/zh-cn/tcp-resets-timeouts/).

![1622-1-Hero](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW486Q2JXV8WYJ701EQQ3RW0.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////78e/v5OTn5ufo7u/s8fHt7+zp///////+7Orx3Nzp3N/r5unw7e7x7evs/////v7/6Ob11dXt09jv3+T26ez27evx////////6ej61Nbz0tj23ub86u788O73////////8PD/3eD52uL95e//8Pb/9fT8////////+vz/6u//6PH/8fv/+f///Pz/////////////9vv/9f7/+///////////////////////+v//+f//////////////)

Cloudflare 在全球範圍內每秒處理超過 6,000 萬個 HTTP 請求，其中[約 70%](https://radar.cloudflare.com/adoption-and-usage) 透過 [TCP](https://datatracker.ietf.org/doc/html/rfc9293) 連線接收（其餘為 [QUIC](https://datatracker.ietf.org/doc/html/rfc9000)/[UDP](https://datatracker.ietf.org/doc/html/rfc768)）。理想情況下，與 Cloudflare 的每個新 TCP 連線都將攜帶至少一個導致成功資料交換的請求，但這遠非事實。事實上，我們發現，在全球範圍內，[大約 20%](https://radar.cloudflare.com/security-and-attacks/#tcp-resets-and-timeouts) 的 Cloudflare 伺服器新 TCP 連線在任何請求完成之前或在初始請求之後立即逾時或被 TCP「中止」訊息關閉。

這篇文章探討了那些由於各種原因（在我們的伺服器看來）在發生任何有用資料交換之前就意外停止的連線。我們的工作表明，雖然連線通常由用戶端終止，但也可能由於第三方乾擾而關閉。今天，我們很高興地在 Cloudflare Radar 上推出新的[儀表板](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)和 [API 端點](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary)，它顯示了前往 Cloudflare 網路的 TCP 連線的近乎即時檢視，這些連線由於重設或逾時而在前 10 個輸入封包內終止，我們在本文中將其稱為 _異常_ TCP 連線。分析這種異常行為可以深入瞭解掃描、連線竄改、DoS 攻擊、連線問題和其他行為。

我們透過 Radar 產生和共用這些資料的能力源於對[連線竄改](https://blog.cloudflare.com/connection-tampering)的全球調查。請讀者閱讀同行審查[研究](https://research.cloudflare.com/publications/SundaraRaman2023/)中的技術細節，或查看其[對應的簡報](https://youtu.be/RD73IgzQMFo?si=OWvNnlNNLalbhygV&t=2984)。請繼續閱讀，瞭解如何使用和解釋資料，以及我們是如何設計和部署偵測機制的，以便其他人可以複製我們的方法。

首先，讓我們討論一下正常與異常 TCP 連線的分類。

## **TCP 連線從建立到關閉的過程**

傳輸控制通訊協定 (TCP) 是一種用於在網際網路上兩個主機之間可靠地傳輸資料的通訊協定 ([RFC 9293](https://datatracker.ietf.org/doc/rfc9293/))。TCP 連線會經歷幾個不同的階段，從連線建立到資料傳輸，再到連線關閉。

TCP 連線是透過 3 向交握建立的。當稱為用戶端的一方傳送標有「SYN」標誌的封包以初始化連線過程時，交握就開始了。伺服器以「SYN+ACK」封包回應，其中的「ACK」標誌確認用戶端的初始化「SYN」。初始化封包及其確認中包含額外的同步資訊。最後，用戶端使用最終 ACK 封包確認伺服器的 SYN+ACK 封包以完成交握。

然後，連線就可以進行資料傳輸了。通常，用戶端將在第一個包含資料的封包上設定 PSH 標誌，以通知伺服器的 TCP 堆疊，立即將資料轉寄給應用程式。雙方繼續傳輸資料並確認收到的資料，直到不再需要連線，此時連線將關閉。

[RFC 9293](https://datatracker.ietf.org/doc/html/rfc9293#section-3.6) 描述了可能關閉 TCP 連線的兩種方式：

  * 正常且平穩的 TCP 關閉序列使用 FIN 交換。任何一方都可以傳送設定了 FIN 標誌的封包，以表明它們沒有更多的資料要傳輸。在另一方確認該 FIN 封包後，該方向的連線將關閉。當確認方完成資料傳輸時，它會傳輸自己的 FIN 封包以關閉，因為連線的每個方向都必須獨立關閉。
  * 一個中止或「重設」訊號，其中一方傳輸 RST 封包，指示另一方立即關閉並捨棄任何連線狀態。重設通常會在發生某些無法復原的錯誤時傳送。



下圖展示了使用 FIN 正常關閉的連線的完整生命週期。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EYYYZCT4S29FV5WY9DFT.png&w=715&h=718&f=webp&fit=cover&position=center)

 _正常的 TCP 連線以 3 向交握開始，以 FIN 交握結束_

此外，TCP 連線可能會因[逾時](https://blog.cloudflare.com/when-tcp-sockets-refuse-to-die/)而終止，逾時指定連線在不接收資料或無確認的情況下可以處於作用中狀態的最大持續時間。例如，非作用的連線可以透過 [keepalive](https://blog.cloudflare.com/when-tcp-sockets-refuse-to-die/) 訊息保持開啟狀態。除非被覆寫，否則 RFC 9293 中指定的全域預設持續時間為五分鐘。

當 TCP 連線透過用戶端的重設或逾時關閉時，我們認為 TCP 連線是 _異常_ 的。

## **異常連線的來源**

異常 TCP 連線本身可能沒有問題，但它們可能是更大問題的徵兆，特別是當發生在 TCP 連線的早期（資料前）階段時。以下是我們可能觀察到重設或逾時的非詳盡潛在原因清單：

  * **掃描程式** ：網際網路掃描程式可能會傳送 SYN 封包來探查伺服器是否在給定連接埠上做出回應，但一旦探查引發了伺服器的回應，則無法清理連線。
  * **應用程式突然關閉** ：如果應用程式不再需要連線，可能會突然關閉開啟的連線。例如，Web 瀏覽器可能會在索引標籤關閉後傳送 RST 以終止連線，或者如果裝置斷電或連線性中斷，連線可能會逾時。
  * **網路錯誤** ：網路狀況不穩定（例如，電纜連線斷開可能導致連線逾時）
  * **攻擊** ：惡意用戶端可能會傳送顯示為異常連線的攻擊流量。例如，在 [SYN 洪水](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)（半開放）攻擊中，攻擊者重複向目標伺服器傳送 SYN 封包，以試圖在目標伺服器維持這些半開放連線時淹沒資源。
  * **竄改** ：能夠攔截用戶端和伺服器之間封包的防火牆或其他中間件可能會捨棄封包，導致通訊雙方逾時。具有深度封包偵測 (DPI) 功能的中間件還可能利用 TCP 通訊協定未經驗證和未加密的事實來[ _插入_ 封包](https://en.wikipedia.org/wiki/Packet_injection)以破壞連線狀態。有關連線竄改的更多詳細資料，請參閱我們[相關聯的部落格文章](https://blog.cloudflare.com/connection-tampering)。



瞭解異常連線的規模和根本原因，可以幫助我們減少失敗並構建一個更強大、更可靠的網路。我們希望公開分享這些見解將有助於提高全球網路的透明度和問責制。

## 如何使用資料集

在本節中，我們將透過廣泛描述三個使用案例來提供如何解釋 TCP 重設和逾時資料集的指導和範例：確認先前已知的行為、探索後續研究的新目標以及擷取網路行為隨時間變化的縱向研究。

在每個範例中，情節線對應於異常連線關閉的連線階段，這為瞭解可能導致異常的原因提供了寶貴的線索。我們將每個傳入連線置於以下其中一個階段：

**Post-SYN（交握期間）** ：伺服器收到用戶端的 SYN 封包後，連線重設或逾時。我們的伺服器已經回覆，但在重設或逾時之前，用戶端沒有傳回任何確認 ACK 封包。[封包詐騙](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/)在此連線階段很常見，因此地理位置資訊特別不可靠。

**Post-ACK（交握後立即）** ：在交握完成並成功建立連線後，連線重設或逾時。任何可能已經傳輸的後續資料都永遠不會到達我們的伺服器。

**Post-PSH（第一個資料封包之後）** ：伺服器收到設定了 PSH 標誌的資料包後連線重設或逾時。PSH 標誌表明 TCP 封包包含已準備好傳送到應用程式的資料（例如 [TLS Client Hello](https://www.cloudflare.com/en-gb/learning/ssl/what-happens-in-a-tls-handshake/#:~:text=The%20%27client%20hello%27%20message%3A) 訊息）。

**後期（在多個資料封包之後）** ：在用戶端已傳出不到 10 個封包，但伺服器已收到多個資料封包後，連線重設。

**無** ：所有其他連線。

為了將重點放在合法連線上，資料集是在 Cloudflare 的攻擊緩解系統處理和篩選連線之後構建的。有關我們如何構建資料集的更多詳細資料，請參見下文。 

### **從自我評估開始**

首先，我們鼓勵讀者造訪 [Radar 儀表板](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)，查看全球範圍以及自身所在國家/地區和 ISP 的結果。

在全球範圍內，如下所示，與 Cloudflare 網路的新 TCP 連線中，約有 20% 在用戶端傳出不到 10 個封包後因重設或逾時而關閉。雖然這個數字似乎高得驚人，但與先前的研究是一致的。正如我們將看到的，重設和逾時率因國家/地區和網路而異，並且這種差異在全球平均值中被忽略。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![2544-2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44T7FYEJ2F73EQD8Q5FAY7.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

Cloudflare 所在地[美國](https://radar.cloudflare.com/us)的異常連線率略低於全球平均水平，這主要是由於在 Post-ACK 和 Post-PSH 階段連線關閉率較低（這些階段更能反映中間件[竄改](https://blog.cloudflare.com/connection-tampering)行為）。由於掃描，Post-SYN 速率升高在大多數網路中都很常見，但可能包含掩蓋真實用戶端 IP 位址的封包。同樣，後期連線階段（初始資料交換之後，但仍在前 10 個封包內）的高連線重設率可能是由於應用程式回應人類動作，例如瀏覽器在索引標籤關閉後使用 RST 關閉不需要的 TCP 連線。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FTFP85N1QR5NH9WAPRTA.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/us?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

Cloudflare 所在 ISP [AS22773 (Cox Communications) ](https://radar.cloudflare.com/as22773)顯示的比率與整個美國相當。這是在美國營運的大多數住宅 ISP 的典型情況。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49AMA9PHB1QR5D34EVKF39.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS22773?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

將此與 [AS15169 (Google LLC)](https://radar.cloudflare.com/as15169) 進行對比，AS15169 起源於 Google 的許多[爬蟲程式和擷取程式](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)。該網路在「後期」連線階段展現出明顯較低的重設率，這可能是由於自動化流量比例較大，而不是由人類使用者動作（例如關閉瀏覽器索引標籤）驅動的。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495FNQV343X710FCAEFTSX.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS15169?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

實際上，我們的[機器人偵測系統](https://radar.cloudflare.com/traffic)將來自 AS15169 的超過 99% 的 HTTP 要求歸類為自動要求。這表明了在 Radar 上整理不同類型資料的價值。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49E8JSW82C0SBNAPXY2VX6.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/traffic/AS15169?dateStart=2024-07-28&dateEnd=2024-08-26#bot-vs-human)_

與 Radar 上出現的大多數資料集一樣，新的異常連線資料集是被動的——它只報告可觀察到的事件，而不是導致它們的原因。本著這種精神，上面的 Google 網路圖表重點表明了證實觀察結果的原因，我們接下來將討論這些原因。

## **一次檢視獲取訊號，更多檢視獲取佐證**

我們的被動測量方法適用於 Cloudflare 規模。然而，它本身並不能識別根本原因或基本事實。對於連線在特定階段關閉的原因，有許多合理的解釋，特別是當關閉是由於重設封包和逾時而導致時。若僅僅只是依靠這一資料來源來進行解釋，我們只能得到猜測的結果。

但是，可以透過結合其他資料來源（例如主動測量）來克服此限制。例如，使用 [OONI](https://ooni.org/) 或 [Censored Planet](https://censoredplanet.org/) 的報告，或者使用實地報告佐證，可以得到更全面的資訊。因此，TCP 重設和逾時資料集的主要使用案例之一是瞭解先前所記錄現象的規模和影響。

### **證實網際網路規模的測量專案**

查看 [AS398324](https://radar.cloudflare.com/as398324)，其結果表明出現了嚴重錯誤，超過一半的連線在 Post-SYN 階段顯示為異常。然而，這個網路原來是 CENSYS-ARIN-01，來自網際網路掃描公司 [Censys](https://censys.com/)。Post-SYN 異常可能是網路層掃描的結果，其中掃描程式傳送單一 SYN 封包來探查伺服器，但不完成 TCP 交握。後期異常的發生率也很高，這可能表明存在應用程式層掃描，正如接近 100% 比例的連線被歸類為自動化流量所表明的那樣。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW454E412TEX10NE8ZM0ZMNH.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS398324?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

實際上，與 AS15169 類似，我們將 AS398324 中超過 99% 的要求歸類為自動化要求。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48X1S84WNVWZ2SS95Q1E4K.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/traffic/AS398324?dateStart=2024-07-28&dateEnd=2024-08-26#bot-vs-human)_

到目前為止，我們已經研究了會產生大量指令碼或自動化流量的網路。是時候放眼更遠的地方了。

### **證實連線竄改**

此資料集的出發點是作為瞭解和偵測主動連線竄改的研究專案，本質與我們在 [HTTPS 攔截](https://blog.cloudflare.com/monsters-in-the-middleboxes)方面的工作類似。[相關聯的部落格文章](https://blog.cloudflare.com/connection-tampering)中詳細解釋了我們這樣做的原因。

強制關閉連線的一種[有據可查](https://go.gale.com/ps/anonymous?id=GALE%7CA175630128&it=r&linkaccess=abs&issn=10727825)的流行技術是[重設插入](https://www.ndss-symposium.org/wp-content/uploads/2017/09/weav.pdf)。透過重設插入，前往目的地之路徑上的中間件會檢查封包的資料部分。當中間件看到前往禁止網域名稱的封包時，它會將偽造的 TCP 重設 (RST) 封包插入一個或兩個通訊方，導致它們中止連線。如果中間件沒有先捨棄禁止的封包，則伺服器將收到觸發中間件竄改的用戶端封包（可能包含帶有[伺服器名稱指示 (SNI)](https://www.cloudflare.com/en-gb/learning/ssl/what-is-sni/) 欄位的 TLS Client Hello 訊息），隨後很快又收到偽造的 RST 封包。

在 TCP 重設和逾時資料集中，因重設插入而中斷的連線通常會顯示為 Post-ACK、Post-PSH 或後期異常（但需要注意的是，並非所有異常都是由於重設插入造成）。

例如，重設插入技術是[已知](https://go.gale.com/ps/anonymous?id=GALE%7CA175630128&it=r&linkaccess=abs&issn=10727825)的並且通常與所謂的中國防火長城 (GFW) 相關。事實上，透過查看源自[中國](https://radar.cloudflare.com/cn) IP 之連線中的 Post-PSH 異常，我們發現比率高於全球平均水平。然而，從中國的各個網路來看，Post-PSH 速率差異很大，這可能是由於承載的流量類型或實施了不同技術所造成的。相較之下，大多數中國主要自治系統的 Post-SYN 異常發生率始終很高；這可能是掃描程式、欺騙性 SYN 洪水攻擊或具有[ _附帶影響_](https://blog.cloudflare.com/zh-tw/consequences-of-ip-blocking)的[殘餘](https://www.usenix.org/conference/usenixsecurity23/presentation/wu-mingshi)[封鎖](https://gfw.report/publications/usenixsecurity23/en/)。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49730V4M2PPXSP0EYNK96R.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/cn?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

[AS4134 (CHINANET-BACKBONE)](https://radar.cloudflare.com/as4134) 的 Post-PSH 異常率低於中國其他 AS，但仍遠高於全球平均水平。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-11](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P53Z8K61Z4ZGWZNEGWVA.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS4134?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

網路 [AS9808 (CHINAMOBILE-CN)](https://radar.cloudflare.com/as9808) 和 [AS56046 (CMNET-Jiangsu-AP)](https://radar.cloudflare.com/as56046) 符合 Post-PSH 異常的連線百分比達到了兩位數。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-12](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45GQC61V9XX64FNPMXWEMZ.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS9808?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-13](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45F5HKG96EF4RWBKSG5QW4.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS56046?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

請參閱我們的[深入解讀部落格貼文](https://blog.cloudflare.com/connection-tampering)，瞭解有關連線竄改的更多資訊。

## **為後續研究尋找新的深入解析和目標**

TCP 重設和逾時資料集還可以作為識別新的或先前未充分研究的網路行為的來源，幫助找到「突出」並值得進一步研究的網路。

### **無法歸因的 ZMap 掃描**

以下是我們無法解釋的情況：每天在相同的 18 小時間隔內，來自英國用戶端超過 10% 的連線從未超過初始 SYN 封包，直接逾時。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-14](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW470YR5X0B25MKBQB5B8JDN.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/gb?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

內部檢查顯示，幾乎所有 Post-SYN 異常都來自使用 [AS396982 (GOOGLE-CLOUD-PLATFORM)](https://radar.cloudflare.com/as396982) 上的 [ZMap](https://zmap.io/) 的掃描程式，這似乎是對所有 IP 位址範圍的完整連接埠掃描。（ZMap 用戶端負責任地進行自我識別，基於稍後討論的 ZMap 負責任的自我識別。）我們看到，來自美國 AS396982 中的 IP 首碼的掃描流量與此類似。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-15](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KBSPA7F7F18Q1AB9BA2P.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS396982?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

### **行動網路零費率**

粗略看一下國家/地區層面的異常率，可以發現一些有趣的現象。例如，看看來自[墨西哥](https://radar.cloudflare.com/mx)的連線，通常與連線竄改相關的 Post-ACK 和 Post-PSH 異常的比率高於全球平均水平。墨西哥連線的情況也與該地區其他國家相似。然而，墨西哥是一個「[沒有書面證據表明政府或其他行為者封鎖或篩選網際網路內容的國家。](https://freedomhouse.org/country/mexico/freedom-net/2023)」

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-16](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47JFJXK571V3YA12NDZ0K7.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/mx?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

透過查看墨西哥 HTTP 流量排名靠前的每個 AS，我們發現來自 [AS28403（RadioMovil Dipsa，S.A. de C.V.，作為 Telcel 營運）](https://radar.cloudflare.com/as28403)的近 50% 的連線在完成 TCP 交握後（Post-ACK 連線階段）立即因重設或逾時而直接終止。在此階段，可能是有一個中間件在封包到達 Cloudflare 之前發現並捨棄了封包。

對這種行為的一種解釋可能是[零費率](https://en.wikipedia.org/wiki/Zero-rating)，在這種情況下，行動數據網路提供者允許免費存取某些資源（例如訊息傳遞或社交媒體應用程式）。當使用者超過其帳戶上的資料傳輸限制時，提供者可能仍允許流量到達零費率目的地，但會封鎖與其他資源的連線。

為了實施零費率原則，ISP 可能會使用 [TLS 伺服器名稱指示 (SNI) ](https://www.cloudflare.com/en-gb/learning/ssl/what-is-sni/)來確定是封鎖還是允許連線。在 TCP 交握後，會立即在包含資料的封包中傳送 SNI。因此，如果 ISP 捨棄包含 SNI 的封包，伺服器仍會看到來自用戶端的 SYN 和 ACK 封包，但看不到後續封包，這與 Post-ACK 連線異常一致。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-17](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48RXXVA7FGYBQDQNT95W7X.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS28403?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

轉向資料集中具有相似概況的另一個國家[秘魯](https://radar.cloudflare.com/pe)，與墨西哥相比，Post-ACK 和 Post-PSH 異常的發生率甚至更高。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-18](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XAPAT3MHKFBKXAZYVE6Q.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/pe?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

重點關注具體 AS，我們發現 [AS1222 (Claro Peru)](https://radar.cloudflare.com/as12252) 顯示出與墨西哥的 AS28403 類似的高 Post-ACK 異常率。這兩個網路均由同一家母公司 [América Móvil](https://www.americamovil.com/English/overview/default.aspx) 經營，因此它們可能採用了類似的網路原則和網路管理技術。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-19](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PXYS28W740SNP0SVACTR.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS12252?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_

有趣的是，[AS6147 (Telefónica Del Perú)](https://radar.cloudflare.com/as6147) 卻顯示出較高的 Post-PSH 連線異常率。這可能表示此網路在網路層使用不同的技術來強制執行其原則。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-20](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FGDYC7PKDTFQ0NBA3E77.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/dz?dateStart=2024-06-06&dateEnd=2024-06-19#tcp-resets-and-attacks)_

## **隨時間變化的縱向檢視**

我們的持續被動測量最強大的一個方面是能夠在較長時間內測量網路。

### **網際網路關停**

在我們 2024 年 6 月的部落格文章《[敘利亞、伊拉克和阿爾及利亞最近的考試期間網際網路關停情況](https://blog.cloudflare.com/syria-iraq-algeria-exam-internet-shutdown)》中，我們從 Cloudflare 網路的角度分享了與考試相關的全國網際網路關閉的情況。當時我們正在準備 TCP 重設和逾時資料集，這有助於確認外部報告並深入瞭解用於關閉的特定技術。

作為行為改變的範例，我們可以「回到過去」觀察與考試相關的封鎖發生的情況。在[敘利亞](https://radar.cloudflare.com/sy)，在與考試相關的關閉期間，我們看到 Post-SYN 異常的發生率激增。事實上，我們發現這些期間的[流量（包括 SYN 封包）幾乎完全停止](https://radar.cloudflare.com/traffic/sy?dateStart=2024-05-20&dateEnd=2024-06-19)。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-21](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45Y7W4YDCBVDE364FQK8XZ.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/sy?dateStart=2024-05-20&dateEnd=2024-06-19#tcp-resets-and-timeouts)_

  
從 7 月最後一週開始的[第二輪](https://x.com/CloudflareRadar/status/1816438072768078078)關停也非常突出。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-21](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463MDS7KG8T04VHR716TTD.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/sy?dateStart=2024-07-20&dateEnd=2024-08-19#tcp-resets-and-timeouts)_

查看來自[伊拉克](https://radar.cloudflare.com/iq)的連線，Cloudflare 所看到的考試相關關停情況似乎與敘利亞相似，都有多個 Post-SYN 峰值，不過沒那麼明顯。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-23](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4578CQXW66V0AFRGRAZ4XG.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/iq?dateStart=2024-05-17&dateEnd=2024-06-10#tcp-resets-and-timeouts)_

[考試關停部落格](https://blog.cloudflare.com/syria-iraq-algeria-exam-internet-shutdown)還描述了[阿爾及利亞](https://radar.cloudflare.com/dz)如何採取更細緻的方法來限制考試期間對內容的存取：有證據表明，阿爾及利亞沒有完全關閉網際網路，而是針對特定連線。事實上，在考試期間，我們發現 Post-ACK 連線異常增加。如果中間件選擇性地捨棄包含禁止內容的封包，同時保留其他封包（例如初始 SYN 和 ACK），則預計會發生這種情況。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-24](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47XSQF8ZNS4HV9G3RH6WFW.png&w=715&h=402&f=webp&fit=cover&position=center)

 _透過[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/dz?dateStart=2024-06-06&dateEnd=2024-06-19#tcp-resets-and-attacks)_

上述範例表明，這些資料在與其他訊號相關時最有用。這些資料也可以透過 [API](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary) 獲取，以便其他人可以更深入地研究。我們的偵測技術也可以轉移到其他伺服器和營運商，如下所述。

## 如何大規模偵測異常 TCP 連線

在本節中，我們將討論如何構建 TCP 重設和逾時資料集。Cloudflare 全球網路的規模為資料處理和分析帶來了獨特的挑戰。我們分享技術以幫助讀者理解我們的方法、解釋資料集，以及在其他網路或伺服器中複製這些機制。

我們的方法可以總結如下：

  1. 記錄到達我們面向用戶端的伺服器的連線樣本。此採樣系統完全是被動的，這意味著它無法解密流量，只能存取透過網路傳送的現有封包。
  2. 從擷取的封包重建連線。我們設計的一個新穎之處是只需要觀察一個方向，即從用戶端到伺服器。
  3. 將重建的連線與一組簽章進行比對，以發現因重設或逾時而終止的異常連線。這些簽章由兩部分組成： _連線階段_ 和一組 _標記_ ，這些標記表明從文獻和我們自己的觀察中得出的特定行為。



這些設計選擇可確保加密封包的安全，並且可以在任何地方複製，而無需存取目的地伺服器。

## **首先，連線範例**

我們的主要目標是設計一種可擴展的機制，並讓我們廣泛瞭解到達 Cloudflare 網路的所有連線。在每個面向用戶端的伺服器上執行流量擷取是可行的，但無法擴展。我們還需要確切地知道在哪裡以及何時進行觀察，這使得難以獲得持續見解。相反，我們對來自所有 Cloudflare 伺服器的連線進行採樣，並將它們記錄到一個集中位置，我們可以在那裡執行離線分析。

這是我們遇到的第一個障礙：Cloudflare 分析系統使用的現有封包記錄管道會記錄各個封包，但一個連線由許多封包組成。為了偵測連線異常，我們需要查看給定連線中的所有或至少足夠的封包。幸運的是，我們能夠利用 Cloudflare DoS 團隊建立的靈活記錄系統來[分析 DDoS 攻擊中涉及的封包](https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/)，並精心設計對兩個 [`iptables`](https://manpages.debian.org/bookworm/iptables/iptables.8.en.html) 規則的叫用來實現我們的目標。

第一個 `iptables` 規則隨機選擇並標記新連線進行採樣。在我們的範例中，我們決定在每 10,000 個輸入 TCP 連線中取樣一個。這個數字並沒有什麼神奇之處，但在 Cloudflare 的規模下，它在捕獲足夠資料以及不給我們的資料處理和分析管道造成壓力之間取得了平衡。`iptables` 規則僅適用於通過 DDoS 緩解系統後的封包。由於 TCP 連線可以長期存在，因此我們僅對新的 TCP 連線進行取樣。以下是用於標記待採樣連線的 `iptables` 規則：
    
    
    -t mangle -A PREROUTING -p tcp --syn -m state 
    --state NEW -m statistic --mode random 
    --probability 0.0001 -m connlabel --label <label> 
    --set -m comment --comment "Label a sample of ingress TCP connections"
    

詳細來說，該規則安裝在處理傳入封包的鏈中的 `mangle` 表中（用於修改封包）(`-A PREROUTING`)。僅考慮設定了 SYN 標誌的 TCP 封包 (`-p tcp --syn`)，其中沒有連線的先前狀態 (`--state NEW`)。篩選器從每 10,000 個 SYN 封包中選擇一個 (`-m statistic –mode random --probability 0.0001`)，並對連線套用一個標籤 (`-m connlabel --label <label> --set`)。

第二個 iptables 規則會記錄連線中的後續封包，最多記錄 10 個封包。同樣，數字 10 並沒有什麼神奇之處，但它通常足以擷取連線建立、後續請求封包和在預期之前關閉的連線上的重設。
    
    
    -t mangle -A PREROUTING -m connlabel --label 
    <label> -m connbytes ! --connbytes 11 
    --connbytes-dir original --connbytes-mode packets 
    -j NFLOG --nflog-prefix "<logging flags>" -m 
    comment --comment "Log the first 10 incoming packets of each sampled ingress connection"
    

此規則與上一個規則安裝在相同鏈中。它僅比對來自採樣連線的封包 (`-m connlabel --label <label>`)，並且僅比對來自每個連線的前 10 個封包 (`-m connbytes ! --connbytes 11 --connbytes-dir original --connbytes-mode packets`)。相符的封包被傳送到 NFLOG (`-j NFLOG --nflog-prefix "<logging flags>"`)，在那裡，它們被記錄系統選取並儲存到集中位置以供離線分析。

## **從採樣封包重建連線**

在我們分析管道的過程中，記錄在我們伺服器上的封包將插入 [ClickHouse](https://blog.cloudflare.com/tag/clickhouse/) 表中。每個記錄的封包都儲存在資料庫內自己的列中。下一個挑戰是將封包重新組裝到相應的連線中以進行進一步分析。在進一步討論之前，我們需要定義用於分析目的的「連線」是什麼。

我們使用由網路五元組 `protocol`、`source IP address`、`source port`、`destination IP address`、`destination port` 定義的連線標準定義，並進行以下調整：

  * 我們僅在連線中途的 _入口_ （用戶端到伺服器）對資料包進行採樣，因此看不到從伺服器到用戶端的相應回應封包。在大多數情況下，我們可以根據對伺服器設定方式的瞭解，推斷出伺服器回應的內容。最終，輸入封包足以用於瞭解異常 TCP 連線行為。
  * 我們以 15 分鐘的間隔查詢 ClickHouse 資料集，並將該間隔內共用相同網路 5 元組的封包分組在一起。這意味著連線可能會在查詢間隔即將結束時被截斷。分析連線逾時時，我們會排除最新封包時間戳記在查詢截止時間後 10 秒內的不完整流程。
  * 由於重設和逾時最有可能影響 _新_ 連線，因此我們僅考慮以標記新 TCP 交握開始的 SYN 封包開頭的封包序列。這樣，已有的長期連線被排除在外。
  * 記錄系統不保證精確的封包到達間隔時間戳記，因此我們僅考慮到達的封包集，而不是按到達時間排序。在某些情況下，我們可以根據 TCP 序號確定封包排序，但事實證明這不會對結果產生重大影響。
  * 我們會篩選掉一小部分具有多個 SYN 封包的連線，以減少分析中的雜訊。



有了上述定義連線的條件，我們現在可以更詳細地描述我們的分析管道。

## **將連線關閉事件對應至階段**

TCP 連線經歷從連線建立到最終關閉的一系列階段。異常連線關閉的階段提供了有關異常發生 _原因_ 的線索。根據我們在伺服器上收到的封包，我們將每個傳入連線放入四個階段之一（Post-SYN、Post-ACK、Post-PSH、後期），上文中對此進行了詳細介紹。

僅連線關閉階段就提供了對來自各種網路的異常 TCP 連線的有用見解，如今，Cloudflare Radar 上已經顯示了相關內容。但是，在某些情況下，我們可以透過將連線與更具體的簽章進行匹配來提供更深入的見解。

## **套用標記來描述更具體的連線行為**

上述將連線分組為階段的過程僅基於連線中封包的 TCP 標誌來完成。考慮到其他因素，例如封包到達間隔時間、TCP 標誌的確切組合以及其他封包欄位（IP 識別、IP TTL、TCP 序列和確認號碼、TCP 視窗大小等），可以允許更精細地匹配特定行為。

例如，流行的 [ZMap](http://zmap.io/) 掃描程式軟體在其產生的 SYN 封包中將 IP 標識欄位固定為 54321，將 TCP 視窗大小固定為 65535（[來源碼](https://github.com/zmap/zmap/blob/c88db2917612328c843561101495e5263ef7ac5b/src/probe_modules/packet.c)）。當我們看到到達網路的封包設定了這些確切的欄位時，該封包很可能是由使用 ZMap 的掃描程式產生的。

標記也可用於將連線與竄改中間件的已知簽章進行比對。大量主動測量工作（例如 [Weaver、Sommer 和 Paxson](https://www.ndss-symposium.org/wp-content/uploads/2017/09/weav.pdf)）發現，一些中間件部署在透過重設插入中斷連線時表現出一致的行為，例如設定與用戶端傳送的其他封包不同的 IP TTL 欄位，或同時傳送 RST 封包和 RST+ACK 封包。有關特定連線竄改簽章的更多詳細資料，請參閱[部落格文章](https://blog.cloudflare.com/connection-tampering)和[同行評審論文](https://research.cloudflare.com/publications/SundaraRaman2023/)。

目前，我們定義了以下標記，並計劃隨著時間的推移對其進行完善和擴展。某些標記僅與其他標記搭配使用，如下方的階層表示所示（例如，`fin` 標記僅在也設定了 `reset` 標記時才適用）。

  * `timeout`：因逾時而終止
  * `reset`：由於重設而終止（設定了 RST 標誌的封包）
    * fin：至少收到一個 FIN 封包以及一個或多個 RST 封包
    * `single_rst`：傳送單個 RST 封包後終止
    * `multiple_rsts`：傳送多個 RST 封包後終止
      * `acknumsame`：RST 封包中的確認號碼全部相同且非零
      * `acknumsame0`：RST 封包中的確認號碼全為零
      * `acknumdif`f：RST 封包中的確認號碼不同，且全部非零
      * `acknumdiff0`：RST 封包中的確認號碼不同，且有一個是零
    * `single_rstack`：傳送單個 RST+ACK 封包後終止（設定了 RST 和 ACK 標誌）
    * `multiple_rstacks`：傳送多個 RST+ACK 封包後終止
    * `rst_and_rstacks`：傳送 RST 和 RST+ACK 封包的組合後終止
  * `zmap`：SYN 封包與 ZMap 掃描程式產生的封包相符



連線標記目前在 Radar [儀表板](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)和 [API](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary) 中不可見，但我們計劃在未來發佈此額外功能。

## **接下來是什麼？**

Cloudflare 的使命是幫助構建更好的網際網路，我們認為透明度和問責制度是該使命的關鍵部分。希望我們分享的見解和工具有助於揭示世界各地的異常網路行為。

雖然目前的 TCP 重設和逾時資料集應該立即能夠對網路營運者、研究人員和全體網際網路公民帶來用處，但我們並不止於此。我們計劃在未來加入幾項改進：

  * 擴展標記集以擷取特定網路行為，並在 [API](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary) 和[儀表板](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)中公開它們。
  * 將深入解析延伸到從 Cloudflare 到客戶來源伺服器的連線。
  * 新增對 QUIC 的支援，目前在前往 Cloudflare 的連線中，全球有超過 [30% 的 HTTP 請求](https://radar.cloudflare.com/adoption-and-usage)都使用 QUIC。



如果這篇部落格文章引起了您的些許興趣，我們鼓勵您閱讀相關的[部落格文章](https://blog.cloudflare.com/connection-tampering)和[論文](https://research.cloudflare.com/publications/SundaraRaman2023/)，深入瞭解連線竄改，並探索 Cloudflare Radar 上的 TCP 重設和逾時[儀表板](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)和 [API](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary)。我們歡迎您透過 radar@cloudflare.com 與我們聯繫，提出您自己的問題和意見。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Ftcp-resets-timeouts%2F&t=%E5%B0%87%E5%B0%8D%20TCP%20%E9%87%8D%E8%A8%AD%E5%92%8C%E9%80%BE%E6%99%82%E7%9A%84%E6%B7%B1%E5%85%A5%E8%A7%A3%E6%9E%90%E5%BC%95%E5%85%A5%20Cloudflare%20Radar)[](https://x.com/intent/post?text=%E5%B0%87%E5%B0%8D+TCP+%E9%87%8D%E8%A8%AD%E5%92%8C%E9%80%BE%E6%99%82%E7%9A%84%E6%B7%B1%E5%85%A5%E8%A7%A3%E6%9E%90%E5%BC%95%E5%85%A5+Cloudflare+Radar&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Ftcp-resets-timeouts%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Ftcp-resets-timeouts%2F)[](https://bsky.app/intent/compose?text=%E5%B0%87%E5%B0%8D+TCP+%E9%87%8D%E8%A8%AD%E5%92%8C%E9%80%BE%E6%99%82%E7%9A%84%E6%B7%B1%E5%85%A5%E8%A7%A3%E6%9E%90%E5%BC%95%E5%85%A5+Cloudflare+Radar+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Ftcp-resets-timeouts%2F)[](https://mastodonshare.com/?text=%E5%B0%87%E5%B0%8D+TCP+%E9%87%8D%E8%A8%AD%E5%92%8C%E9%80%BE%E6%99%82%E7%9A%84%E6%B7%B1%E5%85%A5%E8%A7%A3%E6%9E%90%E5%BC%95%E5%85%A5+Cloudflare+Radar&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Ftcp-resets-timeouts%2F)[](https://www.threads.net/intent/post?text=%E5%B0%87%E5%B0%8D+TCP+%E9%87%8D%E8%A8%AD%E5%92%8C%E9%80%BE%E6%99%82%E7%9A%84%E6%B7%B1%E5%85%A5%E8%A7%A3%E6%9E%90%E5%BC%95%E5%85%A5+Cloudflare+Radar+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Ftcp-resets-timeouts%2F)

## 相關標籤

[Radar](https://blog.cloudflare.com/zh-tw/tag/cloudflare-radar/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)[網際網路品質](https://blog.cloudflare.com/zh-tw/tag/internet-quality/)[網際網路流量](https://blog.cloudflare.com/zh-tw/tag/internet-traffic/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Luke Valenta](https://blog.cloudflare.com/zh-tw/author/luke/)

[](https://lukevalenta.com/)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
