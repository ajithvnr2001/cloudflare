---
url: https://blog.cloudflare.com/zh-tw/protecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov/
title: \u4f7f\u7528\u5e8f\u5217\u5b78\u7fd2\u548c\u53ef\u8b8a\u968e\u6578\u99ac\u723e\u53ef\u592b\u93c8 (Markov chain) \u4fdd\u8b77 API \u514d\u906d\u6feb\u7528 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:15.517449+00:00
---

# 使用序列學習和可變階數馬爾可夫鏈 (Markov chain) 保護 API 免遭濫用 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/protecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov/

[部落格](https://blog.cloudflare.com/zh-tw/)

[AI](https://blog.cloudflare.com/zh-tw/tag/ai/)[API Gateway](https://blog.cloudflare.com/zh-tw/tag/api-gateway/)[API Shield](https://blog.cloudflare.com/zh-tw/tag/api-shield/)+1顯示另外 1 個標籤

4 標籤顯示 4 個標籤

  * 文章標籤
  * [AI](https://blog.cloudflare.com/zh-tw/tag/ai/)[API 安全](https://blog.cloudflare.com/zh-tw/tag/api-security/)
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



[API 安全](https://blog.cloudflare.com/zh-tw/tag/api-security/)

[AI](https://blog.cloudflare.com/zh-tw/tag/ai/)[API Gateway](https://blog.cloudflare.com/zh-tw/tag/api-gateway/)[API Shield](https://blog.cloudflare.com/zh-tw/tag/api-shield/)[API 安全](https://blog.cloudflare.com/zh-tw/tag/api-security/)

2024年9月12日

# 使用序列學習和可變階數馬爾可夫鏈 (Markov chain) 保護 API 免遭濫用

![Peter Foster](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49C4WHJ49XAY0Y7W28JXND.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Peter Foster](https://blog.cloudflare.com/zh-tw/author/peter-foster/)

閱讀時間：10 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/protecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov/)和[简体中文](https://blog.cloudflare.com/zh-cn/protecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov/).

![Protecting APIs from abuse using sequence learning and variable order Markov chains](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49E9PFJZ83SWJQSE269H6S.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v778u/u6ePl6OLn7Ojt7evv6urr///////+8/Dw6eTn6ePp7env7uzx6+vt////////9vP07Ofr7Obt8Ozz8e/07e3x////////+vj68Ozx8ezy9fL49vT58vH2//////////7/9/T3+PT5/fn+/fv/+Pf7/////////////fv+//z//////////v7/////////////////////////////////////////////////////////////////)

考慮一下惡意行為者試圖透過 API 插入、剽竊、收集或外洩資料的情況。此類惡意活動通常以攻擊者向 API 端點發起請求的特定順序為特徵。此外，單獨使用容量技術通常不容易偵測到此類惡意活動，因為攻擊者可能會故意緩慢地執行 API 請求，以試圖阻止容量濫用防護。因此，為了可靠地防止此類惡意活動，我們需要考慮 API 請求的順序。我們使用術語「**順序濫用** 」來指稱惡意 API 請求行為。因此，我們的基本目標包括區分惡意 API 請求序列和良性 API 請求序列。

在這篇部落格文章中，您將瞭解我們如何應對挑戰，幫助客戶保護其 API 免遭順序濫用。為此，我們將展示目前支援我們 [Sequence Analytics](https://developers.cloudflare.com/api-shield/security/sequence-analytics/) 產品的統計機器學習 (ML) 技術。我們將以[ _先前的部落格文章_](https://blog.cloudflare.com/zh-tw/api-sequence-analytics)中提供的 Sequence Analytics 進階介紹為基礎。

### **API 工作階段**

在上一篇部落格文章中提及了一個理念，即考慮由特定使用者發起的一系列按時間排序的 HTTP API 請求。這在使用者與服務互動的過程中發生，例如在瀏覽網站或使用行動應用程式時。我們將使用者按時間排序的一系列 API 請求稱為工作階段。選擇一個熟悉的範例，客戶與銀行服務互動的工作階段可能如下所示：

時間順序 | 方式 | 路徑 | 描述  
---|---|---|---  
1 | POST | /api/v1/auth | 驗證使用者  
2 | GET | /api/v1/accounts/{account_id} | 顯示帳戶餘額，其中 account_id 是屬於使用者的帳戶  
3 | POST | /api/v1/transferFunds | 包含一個請求正文，其中詳細說明了要從中轉移資金的帳戶、要向其轉移資金的帳戶以及要轉移的金額  
  


我們的目標之一是透過自動建議適用於我們的 [Sequence Mitigation](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/) 產品的規則來強制執行所需的序列行為，從而使我們的客戶能夠[保護他們的 API](https://www.cloudflare.com/learning/security/api/what-is-api-security/)。如果我們強制執行預期的行為，我們就可以防止不必要的順序行為。在我們的範例中，所需的順序行為可能需要 /api/v1/auth 必須始終位於 /api/v1/accounts/{account_id} 之前。

我們必須解決的一個重要挑戰是，[ _可能的工作階段數量會隨著工作階段時長的增加而快速增長_](https://blog.cloudflare.com/zh-tw/api-sequence-analytics)。為了瞭解原因，我們可以考慮使用者與範例銀行服務互動的其他方式：例如，使用者可以以任何順序執行多次轉帳和/或檢查多個帳戶的餘額。假設有 3 個可能的**端點** ，下圖說明了使用者與銀行服務互動時可能的工作階段：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1975-IMG-1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47HKPRTNJ34BT7WX77HPYN.png&w=715&h=402&f=webp&fit=cover&position=center)

由於可能存在大量工作階段，建議緩解規則要求我們從過去的工作階段資料中總結順序行為作為中間步驟。在範例中，我們將工作階段中的一系列連續端點（例如 /api/v1/accounts/{account_id} → /api/v1/transferFunds）稱為**序列** 。具體來說，我們需要解決的一個挑戰是，與建立規則相關的順序行為並不一定僅從數量本身就顯而易見：例如，考慮 /api/transferFunds 幾乎總是在 /api/v1/accounts/{account_id} 之前，而且與序列 /api/v1/auth → /api/v1/accounts/{account_id} 相比，序列 /api/v1/accounts/{account_id} → /api/v1/transferFunds 可能相對很少出現。因此，可以想像，如果我們僅根據數量進行總結，我們可能會認為序列 /api/v1/accounts/{account_id} → /api/v1/transferFunds 不重要，而實際上我們應該將其視為潛在的規則。

### **從 API 工作階段學習重要序列**

適用於順序資料的廣泛應用的建模方法是[**馬爾可夫鏈**](https://en.wikipedia.org/wiki/Markov_chain)，其中工作階段資料中每個端點的機率僅取決於固定數量的前面端點。首先，我們將展示如何將標準馬爾可夫鏈套用至我們的工作階段資料，同時指出它們的一些限制。其次，我們將展示如何使用不太知名但功能強大的馬可夫鏈類型來確定重要序列。

出於說明目的，我們假設工作階段資料中有 3 個可能的端點。我們將使用字母 _a_ 、 _b_ 和 _c_ 來表示這些端點：

  *  _a_ : /api/v1/auth
  *  _b_ : /api/v1/accounts/{account_id}
  * _c_ : /api/v1/transferFunds



最簡單的馬爾可夫鏈不過是一個表格，告訴我們在知道了前一個字母的情況下，出現下一個字母的概率。如果我們使用最簡單的馬爾可夫鏈對過去的工作階段資料進行建模，最終可能會得到如下表格：

工作階段中已知的前面端點 | 工作階段中下一個端點的估計機率  
---|---  
a | b | c  
a | 0.10 (1555) | 0.89 (13718) | 0.01 (169)  
b | 0.03 (9618) | 0.63 (205084) | 0.35 (113382)  
c | 0.02 (3340) | 0.67 (109896) | 0.31 (51553)  
表 1   


表 1 列出了馬爾可夫鏈的參數，即在已知工作階段中緊鄰的前一個端點的情況下，觀察到 _a_ 、 _b_ 或 _c_ 作為工作階段中下一個端點的估計機率。例如，第三列單元格的值為 0.67 表示，如果已知前面緊鄰的端點為 _c_ ，則不論 _c_ 前面的端點是什麼，觀察到 _b_ 作為工作階段中下一個端點的估計機率為 67%。因此，表格中的每個項目對應於兩個端點的序列。括號中的值是我們在過去的工作階段資料中看到每一個二端點序列的次數，用於計算表格中的機率。例如，值 0.01 是計算分數 169/(1555+13718+169) 的結果。這種估計機率的方法稱為[最大似然估計](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)。

為了確定重要的序列，我們依靠[可信區間](https://en.wikipedia.org/wiki/Credible_interval)來估計機率，而不是最大似然估計。可信區間不是產生單點估計值（如上所示），而是代表合理的機率範圍。此範圍反映了可用資料量，即每列中序列出現的總數。資料越多，可信區間越窄（確定性程度越高），相反；資料越少，可信區間越寬（確定性程度越低）。根據上表中括號內的數值，我們可以得到以下可信區間（粗體部分將在後面進一步解釋）：

工作階段中已知的前面端點 | 工作階段中下一個端點的估計機率  
---|---  
a | b | c  
a | **0.09-0.11 (1555)** | **0.88-0.89 (13718)** | **0.01-0.01 (169)**  
b | 0.03-0.03 (9618) | 0.62-0.63 (205084) | 0.34-0.35 (113382)  
c | 0.02-0.02 (3340) | 0.66-0.67 (109896) | 0.31-0.32 (51553)  
表 2   


為簡潔起見，我們不會在這裡示範如何手動計算出可信區間（它們涉及評估 [beta 分佈](https://en.wikipedia.org/wiki/Beta_distribution)的[分位數函數](https://en.wikipedia.org/wiki/Quantile_function)）。儘管如此，修訂後的表格表明了更多資料可如何縮小可信區間：請注意，第一列總共出現 15442 次，而第二列總共出現 328084 次。

為了確定重要的序列，我們使用比上面那些稍微複雜一些的馬爾可夫鏈。作為中間步驟，讓我們首先考慮每個表格項目對應於 3 個端點序列（而不是如上所示的 2 個端點）的情況，如下表所示：

工作階段中已知的前面端點 | 工作階段中下一個端點的估計機率  
---|---  
a | b | c  
aa | **0.09-0.13 (173)** | **0.86-0.90 (1367)** | **0.00-0.02 (13)**  
ba | **0.09-0.11 (940)** | **0.88-0.90 (8552)** | **0.01-0.01 (109)**  
ca | **0.09-0.12 (357)** | **0.87-0.90 (2945)** | **0.01-0.02 (35)**  
ab | 0.02-0.02 (272) | 0.56-0.58 (7823) | 0.40-0.42 (5604)  
bb | 0.03-0.03 (6067) | 0.60-0.60 (122796) | 0.37-0.37 (75801)  
cb | 0.03-0.03 (3279) | 0.68-0.68 (74449) | 0.29-0.29 (31960)  
ac | 0.01-0.09 (6) | 0.77-0.91 (144) | 0.06-0.19 (19)  
bc | 0.02-0.02 (2326) | 0.77-0.77 (87215) | 0.21-0.21 (23612)  
cc | 0.02-0.02 (1008) | 0.43-0.44 (22527) | 0.54-0.55 (27919)  
表 3   


表 3 列出了在已知工作階段中緊鄰的前 2 個端點（而不是像之前那樣緊鄰的前 1 個端點）的情況下，觀察到 _a_ 、 _b_ 或 _c_ 作為工作階段中下一個端點的估計機率。也就是說，第三列單元格的間隔為 0.09-0.13 表示，如果知道前面緊鄰的端點為 _ca_ ，則無論 _ca_ 之前的端點是什麼，觀察到 _a_ 作為下一個端點的機率為 9% 到 13% 的可信區間。換句話說，我們說上表表示一個 **2 階** 馬爾可夫鏈。這是因為表格中的項目表示，在**已知** 緊鄰的前 2 個端點的情況下，觀察到下一個端點的機率。

作為一種特殊情況，0 階馬爾可夫鏈僅表示工作階段中端點的分佈。我們可以將與「空上下文」對應的單列相關的機率製成如下表格：

工作階段中已知的前面端點 | 工作階段中下一個端點的估計機率  
---|---  
a | b | c  
| 0.03-0.03 (15466) | 0.64-0.65 (328732) | 0.32-0.33 (165117)  
表 4   


請注意，表 4 中的機率並不僅僅代表工作階段中沒有前面端點的情況。這些機率是工作階段中端點出現的機率，適用於我們不知道前面的端點且無論前面出現了多少個端點的一般情況。 

回到我們識別重要序列的任務，一種可能的方法是簡單地使用某個固定階數 _N_ 的馬爾可夫鏈。例如，如果我們對表 3 中可信區間的下限套用閾值 0.85，那麼我們將總共保留 3 個序列。另一方面，這種方法有兩個值得注意的局限性：

  1. 我們需要一種方法來為模型階數 _N_ 選擇合適的值。
  2. 由於模型階數保持固定，因此識別的序列全都具有相同的長度 _N_ +1。



### **可變階數馬爾可夫鏈**

**可變階數馬爾可夫鏈** (VOMC) 是所述固定階數馬爾可夫鏈的更強大擴展，可解決前面所說的局限性。VOMC 利用了這樣一個事實，即對於固定階數 _N_ 的馬爾可夫鏈中的某些選定值，機率表可能包含統計上多餘的資訊：讓我們比較上面的表 3 和表 2，並考慮表 3 中對應於上下文 _aa_ 、 _ba_ 、 _ca_ （這 3 個上下文都共用 _a_ 作為尾碼）的粗體列。

對於全部 3 個可能的下一個端點 _a、b、c_ ，這些列指定了可信區間，這些區間與表 2 中對應於上下文 _a_ 的相應估計值重疊（也以粗體表示）。我們可以將這些重疊區間解釋為，在已知前面的端點為 _a_ 的情況下，機率估計值之間沒有明顯差異。由於 _a_ 之前的端點對下一個端點的機率沒有明顯影響，我們可以認為表 3 中的這 3 列是多餘的：

我們可以將這 3 列替換為表 2 中與上下文 _a_ 相對應的列，從而將其「折疊」。

按照上文所述修改表 3，結果如下所示（新行以粗體顯示）：

工作階段中已知的前面端點 | 工作階段中下一個端點的估計機率  
---|---  
a | b | c  
a | **0.09-0.11 (1555)** | **0.88-0.89 (13718)** | **0.01-0.01 (169)**  
ab | 0.02-0.02 (272) | 0.56-0.58 (7823) | 0.40-0.42 (5604)  
ac | 0.03-0.03 (6067) | 0.60-0.60 (122796) | 0.37-0.37 (75801)  
bb | 0.03-0.03 (3279) | 0.68-0.68 (74449) | 0.29-0.29 (31960)  
bc | 0.01-0.09 (6) | 0.77-0.91 (144) | 0.06-0.19 (19)  
cb | 0.02-0.02 (2326) | 0.77-0.77 (87215) | 0.21-0.21 (23612)  
cc | 0.02-0.02 (1008) | 0.43-0.44 (22527) | 0.54-0.55 (27919)  
表 5   


表 5 代表一個 VOMC，因為上下文長度會變化：在範例中，我們有上下文長度 1 和 2。因此，表中的項目表示長度在 2 到 3 個端點之間變化的序列，具體取決於上下文長度。概括所描述的折疊上下文的方法，可得出以下用於在離線環境中學習 VOMC 的演算法概略：

`(1) 定義一個表格 _T_ ，其中包含在給定工作階段中 _0、1、2、…、N_max_ 個前面端點的情況下，該工作階段中下一個端點的估計機率。也就是說，透過連接對應於固定階數 _0、1、2、…、N_max_ 的馬爾可夫鏈的列，形成一個表格。`

`(2) is_modified := true `

`(3) DO WHILE is_modified`

` (4) _D_ := all contexts in _T_ which are not suffixes of at least 1 other context in _T_`

` (5) is_modified = false`

` (6) FOR _ctx_ IN _C_`

` (7) IF length(_ctx_) > 0`

` (8) _parent_ctx_ := the context obtained by deleting the leftmost endpoint in _ctx_`

` (9) IF is_collapsible(_ctx_ , _parent_ctx_)`

` (10) Modify _T_ by discarding _ctx_`

` (11) is_modified = true`

在上面的虛擬程式碼中，length(_ctx_) 是上下文 _ctx_ 的長度。在第 9 行，is_collapsible() 涉及以產生表 5 所描述的方式比較上下文 _ctx_ 和 _parent_ctx_ 的可信區間：當且僅當我們在為每個可能的下一個端點分別比較上下文 _ctx_ 和 _parent_ctx_ 時觀察到所有可信區間重疊時，is_collapsible() 計算結果才為 true。最大序列長度為 _N_max_ +1 _，_ 其中 _N_max_ 為某個常數。在第 4 行，如果我們可以透過在 _q_ 前面加上零個或多個端點來形成 _p_ ，則我們說上下文 _q_ 是另一個上下文 _p_ 的**尾碼** 。（根據這個定義，上述的 0 階模型的「空上下文」是 _T_ 中所有上下文的尾碼。）上面的演算法概略是 Rissanen [[1](https://ieeexplore.ieee.org/abstract/document/1056741/)]、Ron [[2](https://link.springer.com/article/10.1023/A:1026490906255)] 等人首先提出的想法的變體。

最後，我們將結果表 _T_ 中的項目作為重要序列。因此，套用 VOMC 的結果是我們認為重要的一組序列。然而，對於 Sequence Analytics，我們認為對序列進行排名也是有用的。為此，我們計算一個介於 0.0 和 1.0 之間的「優先順序分數」，該分數是序列的出現次數除以序列中最後一個端點的出現次數。因此，接近 1.0 的優先順序分數表示，給定端點幾乎總是優先於序列中的其餘端點。這樣，對最高分數的序列進行手動檢查是一種半自動的啟發式方法，可用於在我們的 Sequence Mitigation 產品中建立優先順序規則。

### **大規模學習序列**

前述內容為我們在 Sequence Analytics 中使用的統計機器學習技術的高度概觀。在實踐中，我們設計了一種有效的演算法，這種演算法不需要前期訓練步驟，而是在資料到達時不斷更新模型，並產生重要序列的頻繁更新摘要。這種方法使我們能夠克服本部落格文章中未提及的記憶體成本方面的其他挑戰。最重要的是，直接執行上面的演算法概略仍然會導致表格列（內容）的數量隨著最大序列長度的增加而爆炸式增長。我們必須解決的另一個挑戰是，如何確保我們的系統能夠處理高流量 API，而不會對 CPU 負載產生不利影響。我們預先使用可水平擴展的適應性採樣策略，以便對大容量 API 套用更積極的採樣。然後，我們的演算法會使用採樣的 API 請求流。在客戶部署後，序列會隨著時間的推移組裝和學習，因此重要序列的當前摘要代表一個回顧間隔約為 24 小時的滑動時段。Sequence Analytics 進一步將序列儲存在 [Clickhouse](https://blog.cloudflare.com/tag/clickhouse/) 中，並透過 [GraphQL API](https://developers.cloudflare.com/analytics/graphql-api/) 和 [Cloudflare 儀表板](https://dash.cloudflare.com/)公開它們。想要強制執行序列規則的客戶可以使用 [Sequence Mitigation](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/)。Sequence Mitigation 負責確保在 Cloudflare 全球網路上以分散式方式共用和比對規則，這是另一個令人興奮的主題，我們將在未來的部落格文章中詳述！

### **下一步驟**

現在您已對我們如何展示重要的 API 請求序列有了更深入的瞭解，請繼續關注本系列未來的部落格文章，我們將介紹如何找到客戶可能想要阻止的異常 API 請求序列。目前，API Gateway 客戶可以透過兩種方式開始使用：使用 [Sequence Analytics](https://developers.cloudflare.com/api-shield/security/sequence-analytics/) 來探索重要的 API 請求序列，使用 [Sequence Mitigation](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/) 來強制執行 API 請求序列。尚未購買 API Gateway 的 Enterprise 方案客戶可以透過在 Cloudflare 儀表板內[啟用 API Gateway 試用版](https://dash.cloudflare.com/?to=/:account/:zone/security/api-shield)或聯絡客戶經理來開始使用。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fprotecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov%2F&t=%E4%BD%BF%E7%94%A8%E5%BA%8F%E5%88%97%E5%AD%B8%E7%BF%92%E5%92%8C%E5%8F%AF%E8%AE%8A%E9%9A%8E%E6%95%B8%E9%A6%AC%E7%88%BE%E5%8F%AF%E5%A4%AB%E9%8F%88%20%28Markov%20chain%29%20%E4%BF%9D%E8%AD%B7%20API%20%E5%85%8D%E9%81%AD%E6%BF%AB%E7%94%A8)[](https://x.com/intent/post?text=%E4%BD%BF%E7%94%A8%E5%BA%8F%E5%88%97%E5%AD%B8%E7%BF%92%E5%92%8C%E5%8F%AF%E8%AE%8A%E9%9A%8E%E6%95%B8%E9%A6%AC%E7%88%BE%E5%8F%AF%E5%A4%AB%E9%8F%88+%28Markov+chain%29+%E4%BF%9D%E8%AD%B7+API+%E5%85%8D%E9%81%AD%E6%BF%AB%E7%94%A8&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fprotecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fprotecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov%2F)[](https://bsky.app/intent/compose?text=%E4%BD%BF%E7%94%A8%E5%BA%8F%E5%88%97%E5%AD%B8%E7%BF%92%E5%92%8C%E5%8F%AF%E8%AE%8A%E9%9A%8E%E6%95%B8%E9%A6%AC%E7%88%BE%E5%8F%AF%E5%A4%AB%E9%8F%88+%28Markov+chain%29+%E4%BF%9D%E8%AD%B7+API+%E5%85%8D%E9%81%AD%E6%BF%AB%E7%94%A8+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fprotecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov%2F)[](https://mastodonshare.com/?text=%E4%BD%BF%E7%94%A8%E5%BA%8F%E5%88%97%E5%AD%B8%E7%BF%92%E5%92%8C%E5%8F%AF%E8%AE%8A%E9%9A%8E%E6%95%B8%E9%A6%AC%E7%88%BE%E5%8F%AF%E5%A4%AB%E9%8F%88+%28Markov+chain%29+%E4%BF%9D%E8%AD%B7+API+%E5%85%8D%E9%81%AD%E6%BF%AB%E7%94%A8&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fprotecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov%2F)[](https://www.threads.net/intent/post?text=%E4%BD%BF%E7%94%A8%E5%BA%8F%E5%88%97%E5%AD%B8%E7%BF%92%E5%92%8C%E5%8F%AF%E8%AE%8A%E9%9A%8E%E6%95%B8%E9%A6%AC%E7%88%BE%E5%8F%AF%E5%A4%AB%E9%8F%88+%28Markov+chain%29+%E4%BF%9D%E8%AD%B7+API+%E5%85%8D%E9%81%AD%E6%BF%AB%E7%94%A8+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fprotecting-apis-from-abuse-using-sequence-learning-and-variable-order-markov%2F)

## 相關標籤

[AI](https://blog.cloudflare.com/zh-tw/tag/ai/)[API Gateway](https://blog.cloudflare.com/zh-tw/tag/api-gateway/)[API Shield](https://blog.cloudflare.com/zh-tw/tag/api-shield/)[API 安全](https://blog.cloudflare.com/zh-tw/tag/api-security/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
