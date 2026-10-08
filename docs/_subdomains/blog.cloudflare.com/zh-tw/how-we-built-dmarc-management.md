---
url: https://blog.cloudflare.com/zh-tw/how-we-built-dmarc-management/
title: \u6211\u5011\u5982\u4f55\u904b\u7528 Cloudflare Workers \u6253\u9020 DMARC \u7ba1\u7406\u529f\u80fd | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:17.962946+00:00
---

# 我們如何運用 Cloudflare Workers 打造 DMARC 管理功能 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/how-we-built-dmarc-management/

[部落格](https://blog.cloudflare.com/zh-tw/)

[DMARC](https://blog.cloudflare.com/zh-tw/tag/dmarc/)[Security Week](https://blog.cloudflare.com/zh-tw/tag/security-week/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)+1顯示另外 1 個標籤

4 標籤顯示 4 個標籤

  * 文章標籤
  * [Security Week](https://blog.cloudflare.com/zh-tw/tag/security-week/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[電子郵件安全](https://blog.cloudflare.com/zh-tw/tag/email-security/)
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



[電子郵件安全](https://blog.cloudflare.com/zh-tw/tag/email-security/)

[DMARC](https://blog.cloudflare.com/zh-tw/tag/dmarc/)[Security Week](https://blog.cloudflare.com/zh-tw/tag/security-week/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[電子郵件安全](https://blog.cloudflare.com/zh-tw/tag/email-security/)

2023年3月17日

# 我們如何運用 Cloudflare Workers 打造 DMARC 管理功能

![André Cruz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FAFHK5DDQ0GQPPQ92C3B.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nelson Duarte](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P72CGQX08FQC903Q0E4F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[André Cruz](https://blog.cloudflare.com/zh-tw/author/andre-cruz/)和[Nelson Duarte](https://blog.cloudflare.com/zh-tw/author/nelson-duarte/)

閱讀時間：8 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/how-we-built-dmarc-management/)、[Deutsch](https://blog.cloudflare.com/de-de/how-we-built-dmarc-management/)、[Español](https://blog.cloudflare.com/es-es/how-we-built-dmarc-management/)、[Français](https://blog.cloudflare.com/fr-fr/how-we-built-dmarc-management/)、[日本語](https://blog.cloudflare.com/ja-jp/how-we-built-dmarc-management/)、[한국어](https://blog.cloudflare.com/ko-kr/how-we-built-dmarc-management/)和[简体中文](https://blog.cloudflare.com/zh-cn/how-we-built-dmarc-management/).

![How we built DMARC Management using Cloudflare Workers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VEZPBHGFF89NHRCXR27K.png&w=1201&h=676&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vvo+fbi7uvV6ObO6ujQ7+3W7+zW6ebQ//vp+vXj7ujW5uDO6OPR7ujX7+nW6uTQ//3r/fbl7+bX5tzP6N3S7uXY8OfY7OTR///v//jo8+ja6dzS6t3V8OXb8+jb8ObU///z//3s+O7f7uPX7+TZ9evf+O7f9evZ///3///x/vXk9ezc9u7e/PPj/fXj+vHe///6///0//zo+vXg/Pbh//vm//vn/ffi///7///2//7p/fjh/vrj//3o//3o//jj)

### 什麼是 DMARC 報告

[DMARC](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/) 代表網域型郵件認證、報告和符合性。它是一項電子郵件認證通訊協定，可幫助防範電子郵件[網路釣魚](https://www.cloudflare.com/en-gb/learning/access-management/phishing-attack/)和[詐騙](https://www.cloudflare.com/en-gb/learning/email-security/what-is-email-spoofing/)。

傳送電子郵件時，DMARC 允許網域擁有者設定 DNS 記錄，指定用於驗證電子郵件真實性的認證方法，如 [SPF](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/)（寄件者原則架構）和 [DKIM](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/)（網域金鑰識別郵件）等。當電子郵件未通過這些認證檢查時，DMARC 會指示收件者的電子郵件提供者如何處理郵件：隔離郵件或直接拒絕郵件。

如今，在網際網路中，電子郵件網路釣魚和詐騙攻擊越來越複雜且普遍，因此 DMARC 的重要性也日漸提升。透過實作 DMARC，網域擁有者能夠保護他們的品牌和客戶不受這些攻擊的負面影響，包括失去信任、信譽損害和經濟損失。

除了針對網路釣魚和詐騙攻擊提供保護，DMARC 還提供[報告](https://www.rfc-editor.org/rfc/rfc7489)功能。網域擁有者能夠接收有關電子郵件認證活動的報告，其中包括哪些訊息通過了 DMARC 檢查，哪些未通過，以及這些訊息的來源。

DMARC 管理功能涉及設定和維護網域的 DMARC 原則。若要實現有效的 DMARC 管理功能，需對電子郵件認證活動進行持續的監控和分析，以及能夠根據需要對 DMARC 原則進行調整和更新。

以下為有效 DMARC 管理功能的幾個關鍵組成部分：

  * 設定 DMARC 原則：此操作涉及設定網域的 DMARC 記錄，以指定合適的認證方法和原則，用於處理未通過認證檢查的訊息。以下展示了 DMARC DNS 記錄外觀：



`v=DMARC1; p=reject; rua=mailto:dmarc@example.com`

這指定了我們將使用 DMARC 版本 1，我們的原則是拒絕未通過 DMARC 檢查的電子郵件，以及提供者應向其傳送 DMARC 報告的電子郵件地址。

  * 監控電子郵件認證活動：DMARC 報告對於網域擁有者來說是一項重要工具，有助於他們確保電子郵件的網路安全和可寄送性以及符合行業標準和法規。透過定期監控並分析 DMARC 報告，網域擁有者能夠識別電子郵件威脅、最佳化電子郵件活動，並改進電子郵件認證的整體效果。
  * 根據需要進行調整：根據 DMARC 報告的分析結果，網域擁有者可能需要調整 DMARC 原則或認證方法，以確保能夠正確認證電子郵件訊息，免受網路釣魚和詐騙攻擊。
  * 與電子郵件提供者和協力廠商合作：若要實現有效的 DMARC 管理功能，可能需要與電子郵件提供者和協力廠商協同合作，以確保 DMARC 原則得到正確地實作和執行。



現在，我們推出了 [DMARC 管理功能](https://blog.cloudflare.com/dmarc-management)。以下說明了它的建構方式。

### 如何構建

Cloudflare 作為雲端式網路安全和效能解決方案的領先提供者，採取了特定的方法來測試我們的產品。我們「吃自產的狗糧」，這表示我們使用自己的工具和服務來執行我們的商業方案。這有助於我們提前識別任何問題或錯誤，避免它們影響到客戶。

我們在內部使用自己的產品，例如 [Cloudflare Workers](https://workers.cloudflare.com/)，這是一個無伺服器平台，允許開發者在我們的全球網路上執行他們的程式碼。自 2017 年推出以來，Workers 生態系統發展迅速。如今，有成千上萬的開發者在該平台上建構和部署應用程式。Workers 生態系統的強大之處在於，它能夠讓開發者建構複雜的應用程式，而這些應用程式之前的執行不可能距離用戶端如此近（或不切實際）。Workers 可用於建構 API、產生動態內容、最佳化影像、執行即時處理等等。可能性幾乎是無限的。我們使用 Workers 為 [Radar 2.0](https://blog.cloudflare.com/zh-tw/technology-behind-radar2-zh-tw/) 等服務或 [Wildebeest](https://blog.cloudflare.com/zh-tw/welcome-to-wildebeest-the-fediverse-on-cloudflare-zh-tw/) 等軟體套件提供支援。

最近，我們的 [Email Routing](https://developers.cloudflare.com/email-routing/) 產品與 Workers 聯手，可以透過 Workers 指令碼[處理傳入的電子郵件](https://blog.cloudflare.com/announcing-route-to-workers/)。正如[文件](https://developers.cloudflare.com/email-routing/email-workers/)所述：「借助 Email Workers，您可以利用 Cloudflare Workers 的強大功能來實作處理電子郵件和建立複雜規則所需的任何邏輯。這些規則決定了收到電子郵件時會執行的操作。」規則和驗證的地址都可以透過我們的 [API](https://developers.cloudflare.com/api/operations/email-routing-destination-addresses-list-destination-addresses) 設定。

以下展示了簡單的 Email Worker 外觀：

很簡單，對吧？
    
    
    export default {
      async email(message, env, ctx) {
        const allowList = ["friend@example.com", "coworker@example.com"];
        if (allowList.indexOf(message.headers.get("from")) == -1) {
          message.setReject("Address not allowed");
        } else {
          await message.forward("inbox@corp");
        }
      }
    }

鑒於能夠以程式設計方式處理傳入的電子郵件，它似乎是以可擴展和高效的方式處理傳入 DMARC 報告電子郵件的最佳方式，讓 Email Routing 和 Workers 完成接收全球無數電子郵件的繁重工作。以下是對我們所需操作的詳細說明：

  1. 接收電子郵件並擷取報告
  2. 將相關詳細資料發佈到分析平台
  3. 儲存原始報告



憑藉 Email Workers，我們能夠輕鬆完成 #1。我們只需建立一個帶有 email() 處理常式的 Worker。此處理常式將接收 [SMTP](https://www.rfc-editor.org/rfc/rfc5321) 信封元素、預解析版本的電子郵件標頭以及用於讀取整個原始電子郵件的資料流。

對於 #2，我們還可以查看 Workers 平台並找到 [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)。我們只需要定義一個合適的架構，這取決於報告中的內容和我們計劃稍後進行的查詢。之後我們可以使用 [GraphQL](https://developers.cloudflare.com/analytics/graphql-api/) 或 [SQL](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/) API 查詢資料。

對於 #3，我們只需要使用我們的 [R2](https://www.cloudflare.com/en-gb/products/r2/) 物件儲存體。從 Worker 存取 R2 [非常簡單](https://developers.cloudflare.com/r2/examples/demo-worker/)。從電子郵件中擷取報告之後，我們會將這些報告儲存在 R2 中。

我們將其建構為您可以在您的區域啟用的託管服務，為方便起見，還新增了一個儀表板介面，但實際上所有工具都可供您使用，以在您自己的帳戶中在 Cloudflare Workers 之上部署您自己的 DMARC 報告處理器 ，無需擔心伺服器、可擴展性或效能。

### 架構

[Email Workers](https://developers.cloudflare.com/email-routing/email-workers/) 是我們 Email Routing 產品的一項功能。Email Routing 元件在我們所有的節點中執行，因此它們中的任何一個都能夠處理傳入郵件，這很重要，因為我們從所有數據中心公佈了電子郵件輸入 BGP 首碼。向 Email Worker 傳送電子郵件就像在 Email Routing 儀表板中設定規則一樣簡單。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1751 Embedded Image - qUt3Zo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW465JK1BXGCB56J3DVNFMVG.png&w=715&h=410&f=webp&fit=cover&position=center)

當 Email Routing 元件收到一封電子郵件，該郵件與要傳遞給 Worker 的規則相匹配時，它將聯絡我們最近開源的 [workerd](https://github.com/cloudflare/workerd) 執行階段的內部版本，該執行階段也在所有節點上執行。管理此互動的 RPC 架構在 [Capnproto](https://github.com/capnproto/capnproto) 架構中定義，並允許在閱讀電子郵件正文時將其流式傳輸到 Edgeworker。如果 Worker 指令碼決定轉送此電子郵件，Edgeworker 將使用原始請求中傳送的功能聯絡 Email Routing。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1751 Embedded Image - xo7GIP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW472EZF80K47ZMXFN76TXDC.png&w=715&h=139&f=webp&fit=cover&position=center)

在 DMARC 報告的內容中，以下是我們處理傳入電子郵件的方式：
    
    
    jsg::Promise<void> ForwardableEmailMessage::forward(kj::String rcptTo, jsg::Optional<jsg::Ref<Headers>> maybeHeaders) {
      auto req = emailFwdr->forwardEmailRequest();
      req.setRcptTo(rcptTo);
    
      auto sendP = req.send().then(
          [](capnp::Response<rpc::EmailMetadata::EmailFwdr::ForwardEmailResults> res) mutable {
        auto result = res.getResponse().getResult();
        JSG_REQUIRE(result.isOk(), Error, result.getError());
      });
      auto& context = IoContext::current();
      return context.awaitIo(kj::mv(sendP));
    }
    

  1. 擷取正在處理的電子郵件的收件者，這是使用的 RUA。RUA 是一個 DMARC 設定參數，指示應在何處報告與某個網域相關的彙總 DMARC 處理回饋意見。可以在訊息的「to」屬性中找到此收件者。
  2. const ruaID = message.to
  3. 由於我們處理無數網域的 DMARC 報告，因此我們使用 Workers KV 來儲存每個網域的一些相關資訊，並在 RUA 上鍵入這些資訊。透過該操作，我們也能知道是否應該接收這些報告。
  4. const accountInfoRaw = await env.KV_DMARC_REPORTS.get(dmarc:${ruaID})
  5. 此時，我們想要將整封電子郵件讀入 arrayBuffer 以便對其進行解析。根據報告的大小，我們可能會受到免費 Workers 計劃的限制。如果發生這種情況，建議您切換到 [Workers Unbound](https://www.cloudflare.com/en-gb/workers-unbound-beta/) 資源模型，該模型不會出現此問題。
  6. const rawEmail = new Response(message.raw)  
const arrayBuffer = await rawEmail.arrayBuffer()
  7. 解析原始電子郵件包括解析其 MIME 部分等。有多個可用的庫可執行此操作。例如，您可以使用 [postal-mime](https://www.npmjs.com/package/postal-mime)：
  8. const parser = new PostalMime.default()  
const email = await parser.parse(arrayBuffer)
  9. 解析電子郵件後，現在我們可以存取其附件。這些附件是 DMARC 報告本身，可以被壓縮。我們要做的第一件事是將它們以壓縮形式儲存在 [R2](https://developers.cloudflare.com/r2/data-access/workers-api/workers-api-usage/) 中以進行長期儲存。稍後重新處理或調查目標報告時可能會用到它們。此操作就像在 R2 繫結上叫用 put() 一樣簡單。為了便於以後擷取，建議您將報告檔案按目前時間分佈在不同的目錄中。
  10. await env.R2_DMARC_REPORTS.put(  
`${date.getUTCFullYear()}/${date.getUTCMonth() + 1}/${attachment.filename}`,  
attachment.content  
)
  11. 現在我們需要查看附件 mime 類型。DMARC 報告的原始格式是 XML，但它們可以被壓縮。在這種情況下，我們需要先解壓它們。DMARC 報告程式檔案可以使用多種壓縮算法。我們使用 MIME 類型來了解使用哪一種。[Zlib](https://en.wikipedia.org/wiki/Zlib) 壓縮報告可以使用 [pako](https://www.npmjs.com/package/pako) ，而對於 ZIP 壓縮報告，[unzipit](https://www.npmjs.com/package/unzipit) 是一項不錯的選擇。
  12. 獲得報告的原始 XML 格式後，[fast-xml-parser](https://www.npmjs.com/package/fast-xml-parser) 在解析它們時效果很好。以下展示了 DMARC 報告 XML 外觀：
  13. 現在，我們可以輕鬆取得報告中的所有資料。後續我們要執行的動作在很大程度上取決於我們想要如何呈現資料。我們的目標是在儀表板中顯示從報告中擷取的有意義的資料。因此，我們需要一個分析平台，可以在其中推送豐富的資料。進入 [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)。Analytics 引擎非常適合這項工作，因為透過該引擎，我們可以從 Worker 向它[傳送](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#3-write-data-from-your-worker)資料，然後公開 [GraphQL API](https://developers.cloudflare.com/analytics/graphql-api/) 以與資料互動。這就是我們獲取資料以在儀表板中顯示的方式。



未來，我們還會考慮在工作流程中整合 [Queues](https://developers.cloudflare.com/queues/)，以異步處理報告，避免等待用戶端完成此過程。
    
    
    const ruaID = message.to

我們成功地僅依靠 Workers 基礎結構端到端地實作了這個專案，證明了建構重要應用程式的可能性和優勢，而不必擔心可擴展性、效能、儲存和網路安全問題。
    
    
    const accountInfoRaw = await env.KV_DMARC_REPORTS.get(dmarc:${ruaID})

### 開源
    
    
    const rawEmail = new Response(message.raw)
    const arrayBuffer = await rawEmail.arrayBuffer()

正如我們之前提到的，我們建構了一個您可以啟用和使用的託管服務，我們將為您管理它。但是，我們所做的一切也可以由您在您的帳戶中部署，以便您可以管理自己的 DMARC 報告。過程簡單，而且免費。為了幫助您執行此操作，我們發佈了一個開源版本的 Worker，它以上述方式處理 DMARC 報告：<https://github.com/cloudflare/dmarc-email-worker>
    
    
    const parser = new PostalMime.default()
    const email = await parser.parse(arrayBuffer)

如果您沒有用於顯示資料的儀表板，您還可以從 Worker [查詢](https://developers.cloudflare.com/analytics/analytics-engine/worker-querying/) Analytics Engine。或者，如果您想將它們儲存在關係資料庫中，則可以使用 [D1](https://developers.cloudflare.com/d1/platform/client-api/)。可能性是無限的，我們期待看到您將使用這些工具建構什麼。
    
    
    await env.R2_DMARC_REPORTS.put(
        `${date.getUTCFullYear()}/${date.getUTCMonth() + 1}/${attachment.filename}`,
        attachment.content
      )

請分享您自己的想法，我們洗耳恭聽。
    
    
    <feedback>
      <report_metadata>
        <org_name>example.com</org_name>
        <emaildmarc-reports@example.com</email>
       <extra_contact_info>http://example.com/dmarc/support</extra_contact_info>
        <report_id>9391651994964116463</report_id>
        <date_range>
          <begin>1335521200</begin>
          <end>1335652599</end>
        </date_range>
      </report_metadata>
      <policy_published>
        <domain>business.example</domain>
        <adkim>r</adkim>
        <aspf>r</aspf>
        <p>none</p>
        <sp>none</sp>
        <pct>100</pct>
      </policy_published>
      <record>
        <row>
          <source_ip>192.0.2.1</source_ip>
          <count>2</count>
          <policy_evaluated>
            <disposition>none</disposition>
            <dkim>fail</dkim>
            <spf>pass</spf>
          </policy_evaluated>
        </row>
        <identifiers>
          <header_from>business.example</header_from>
        </identifiers>
        <auth_results>
          <dkim>
            <domain>business.example</domain>
            <result>fail</result>
            <human_result></human_result>
          </dkim>
          <spf>
            <domain>business.example</domain>
            <result>pass</result>
          </spf>
        </auth_results>
      </record>
    </feedback>

### 結束語

我們希望這篇文章能加深您對 Workers 平台的理解。如今，Cloudflare 利用此平台建構了我們的大部分服務，我們認為您也應該這麼做。

歡迎使用我們的開源版本，向我們展示您可以使用它實現哪些目的。

Email Routing 也在努力擴展 Email Workers API 的功能，我們很快會在另一篇部落格文章中進行介紹。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-we-built-dmarc-management%2F&t=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E9%81%8B%E7%94%A8%20Cloudflare%20Workers%20%E6%89%93%E9%80%A0%20DMARC%20%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD)[](https://x.com/intent/post?text=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E9%81%8B%E7%94%A8+Cloudflare+Workers+%E6%89%93%E9%80%A0+DMARC+%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-we-built-dmarc-management%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-we-built-dmarc-management%2F)[](https://bsky.app/intent/compose?text=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E9%81%8B%E7%94%A8+Cloudflare+Workers+%E6%89%93%E9%80%A0+DMARC+%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-we-built-dmarc-management%2F)[](https://mastodonshare.com/?text=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E9%81%8B%E7%94%A8+Cloudflare+Workers+%E6%89%93%E9%80%A0+DMARC+%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-we-built-dmarc-management%2F)[](https://www.threads.net/intent/post?text=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E9%81%8B%E7%94%A8+Cloudflare+Workers+%E6%89%93%E9%80%A0+DMARC+%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fhow-we-built-dmarc-management%2F)

## 相關標籤

[DMARC](https://blog.cloudflare.com/zh-tw/tag/dmarc/)[Security Week](https://blog.cloudflare.com/zh-tw/tag/security-week/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[電子郵件安全](https://blog.cloudflare.com/zh-tw/tag/email-security/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
