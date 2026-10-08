---
url: https://blog.cloudflare.com/zh-tw/inside-geo-key-manager-v2/
title: \u5728 Geo Key Manager v2 \u5167\u90e8\uff1a\u91cd\u65b0\u69cb\u60f3\u5206\u6563\u5f0f\u7cfb\u7d71\u7684\u5b58\u53d6\u63a7\u5236 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:05.549795+00:00
---

# 在 Geo Key Manager v2 內部：重新構想分散式系統的存取控制 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/inside-geo-key-manager-v2/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Geo Key Manager](https://blog.cloudflare.com/zh-tw/tag/geo-key-manager/)[密碼編譯](https://blog.cloudflare.com/zh-tw/tag/cryptography/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)

3 標籤顯示 3 個標籤

  * 文章標籤
  * [密碼編譯](https://blog.cloudflare.com/zh-tw/tag/cryptography/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)
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



[Geo Key Manager](https://blog.cloudflare.com/zh-tw/tag/geo-key-manager/)[密碼編譯](https://blog.cloudflare.com/zh-tw/tag/cryptography/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)

2023年1月27日

# 在 Geo Key Manager v2 內部：重新構想分散式系統的存取控制

![Tanya Verma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47170PNYASHP8A1SE0TRRY.png&w=64&h=64&f=webp&fit=cover&position=center)

[Tanya Verma](https://blog.cloudflare.com/zh-tw/author/tanya/)

閱讀時間：21 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/inside-geo-key-manager-v2/)、[Deutsch](https://blog.cloudflare.com/de-de/inside-geo-key-manager-v2/)、[Français](https://blog.cloudflare.com/fr-fr/inside-geo-key-manager-v2/)和[简体中文](https://blog.cloudflare.com/zh-cn/inside-geo-key-manager-v2/).

![Inside Geo Key Manager v2: re-imagining access control for distributed systems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FPJ48CR9XS13HETAZF9V.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAlkMilkclmFEtmlgznFg2mlIzk0criz0gm0cknVMxomdHpnBVpmtXoVtPmEs9kEUloEslpF06rHlYsYRrsHpuqGJinU9KlkwppEwkqGE9sYBft4tytYB1rGVooVBOmU8qpEshqF45sHpYtYVrs3ptq2FhoU5Imk0oo0ccpVUuqmpGrXNVrWtWp1hMn0k5mEcioEMWoUofo1cspV00plk0o04tnUQjlkAan0ETn0UWn00aoVIbolAYoUoUnEIUlD0X)

2022 年 12 月，我們宣佈推出了新版本 [Geo Key Manager](https://blog.cloudflare.com/zh-tw/configurable-and-scalable-geo-key-manager-closed-beta-zh-tw/) 的封閉測試版。Geo Key Manager v2 (GeoV2) 是我們旅程中的下一步，旨在為客戶提供一種安全靈活的方式，來按地理位置控制其私密金鑰的分佈。我們的原始系統 [Geo Key Manager v1](https://blog.cloudflare.com/introducing-cloudflare-geo-key-manager/) 於 2017 年作為一項研究專案推出，但隨著客戶需求的演變和公司規模的擴大，我們意識到，我們必須做出重大改進，以便提供更好的使用者體驗。

Geo Key Manager v1 (GeoV1) 面臨的一個主要挑戰是我們的存取控制原則缺乏彈性。客戶通常出於監管方面的考量，需要更豐富的資料當地語系化。而在內部，諸如烏克蘭衝突之類的事件則增強了能夠快速限制敏感性金鑰資料存取的需求。Geo Key Manager v1 的基礎密碼編譯將身分識別型廣播加密和身分識別型撤銷組合起來，模擬了屬性型加密 (ABE) 所提供的一小部分功能。透過以既定的 ABE 配置取代它，不僅幫助我們解決了存取控制原則缺乏彈性的問題，還為我們的系統提供了更安全的基礎。

我們之前的配置一開始就凍結了參與的資料中心和原則集，從而限制了未來的彈性，與之相反，使用 ABE 讓系統能夠輕鬆適應未來的需求。它使我們能夠善加運用具現化後添加的其他資料中心所帶來的效能提升，大大簡化了處理屬性和原則變更的流程。此外，GeoV1 還面臨著一些令人困擾的效能問題，這些問題導致了較高的尾部延遲和令人痛苦的手動金鑰變換程序。我們希望透過 GeoV2 來解決 GeoV1 的這些挑戰和限制。

雖然此部落格重點介紹我們的地理金鑰管理解決方案，但這裡的經驗教訓也可以適用於其他存取控制需求。傳統上，我們會使用高可用的中央授權單位來監督資源存取，從而實作存取控制解決方案。正如我們將看到的那樣，ABE 讓我們避開了這個單一失敗點。由於我們不瞭解任何大規模的基於 ABE 的存取控制系統，因此，希望我們的討論能夠幫助工程師考慮使用 ABE 作為存取控制的替代方案，以最大程度減少對集中式授權單位的依賴。為了實現這一目標，我們在 [CIRCL](https://pkg.go.dev/github.com/cloudflare/circl@v1.3.0/abe/cpabe/tkn20)（我們的開放原始碼的密碼編譯程式庫）中加入了 ABE 的實作。

## 不滿意的解決方案嘗試

在回到 Geov2 之前，我們稍微繞行一下，先來看看我們正在嘗試解決的問題。

想一下這個例子：一間歐洲大型銀行希望僅在歐盟境內儲存 TLS 私密金鑰。這間銀行是 Cloudflare 的客戶，這意味著我們代表他們執行 TLS 交握。我們需要為他們終止 TLS 的原因是，為了我們能夠提供最佳保護來抵禦 DDoS 攻擊、透過快取提高效能、支援 Web 應用程式防火牆等。

為了終止 TLS，我們需要存取他們的 TLS 私密金鑰1。用於處理 API 流量的控制平面，使用在全球所有機器之間共用的主要公開金鑰對客戶上傳的私密金鑰進行加密。然後，它將金鑰放入分佈在全球範圍內的 KV 存放區，[Quicksilver](https://blog.cloudflare.com/introducing-quicksilver-configuration-distribution-at-internet-scale/)。這表示世界各地每個資料中心的每台機器都有此客戶 TLS 私密金鑰的本機複本。因此，每個資料中心的每台機器都會有每個客戶的私密金鑰的一個複本。

客戶上傳 TLS 憑證和私密金鑰以儲存在所有資料中心

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Customer uploading their TLS certificate and private key to be stored in all data centers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FTCBM0SR76XMQ75E237R.png&w=715&h=326&f=webp&fit=cover&position=center)

但是，該銀行希望其金鑰僅儲存在歐盟境內的資料中心。為了滿足這個需求，我們提供了三個選項。

第一個選項是確保只有歐盟資料中心可以收到此金鑰並終止交握。所有其他機器都會將 TLS 要求透過代理傳送至歐盟伺服器進行處理。這將需要為每台機器僅提供 Quicksilver 中儲存的整個金鑰集的子集，這對 Cloudflare 多年來做出的核心設計決策而言真是極大的挑戰，該決策假設每台機器上都複寫了整個資料集。

將客戶金鑰限制於歐盟資料中心

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Restricting customer keys to EU data centers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48EP2G5XHPY6M5QY9M3EJ2.png&w=715&h=326&f=webp&fit=cover&position=center)

另一個選項是將金鑰儲存在核心資料中心，而不是 Quicksilver。這可讓我們每次都強制執行適當的存取控制原則，確保只有特定機器才能存取特定金鑰。但是，這會讓擁有全球網路的首要目的落空：減少延遲並避免核心出現單一失敗點。

將金鑰儲存在執行複雜商務邏輯以強制執行原則的核心資料中心

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Storing keys in core data center where complicated business logic runs to enforce policies](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45EZTWBBMTZZDNKHF133B0.png&w=715&h=309&f=webp&fit=cover&position=center)

第三個選項是使用公開金鑰密碼編譯。每個資料中心都擁有自己的金鑰組，而不是擁有主要金鑰組。核心使用允許使用它的每個資料中心的金鑰對客戶的私密金鑰進行加密。在此範例中，只有歐盟境內的機器才能存取該金鑰。假設有 500 個資料中心，各有 50 台機器。在這 500 個資料中心中，假設 200 個在歐盟境內。其中 100 個 1kB 的金鑰總共耗用了 100 x 500 x 50 x 1 kB（全球），現在它們的耗用量將是原來的 200 倍，在最糟糕的情況下，最多可達 500 倍。這會讓每台機器上儲存金鑰所需的空間以一個全新的因數增長——之前，儲存空間僅僅是一個有關註冊了多少個客戶金鑰的函數；現在，儲存空間仍然是客戶金鑰數量的函數，但還要乘以資料中心的數量。

為每個資料中心指派唯一金鑰，並使用歐盟資料中心金鑰包裝客戶金鑰

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Assigning unique keys to each data center and wrapping customer key with EU data center keys](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45YZP73MZRMD30GJP0R9QZ.png&w=715&h=334&f=webp&fit=cover&position=center)

遺憾的是，這三個選項都有各自的問題，不能令人滿意。它們要么需要改變我們對 Cloudflare 架構所做的基本假設，從而放棄使用高度分散的網路的優勢，要么讓此功能使用的儲存空間以二次方增長。

深入研究第三個選項後發現——為什麼不建立兩個金鑰組而不是每個資料中心都有一個唯一的？一組在所有歐盟資料中心通用，一組用於所有非歐盟資料中心。如此一來，核心只需要加密客戶的金鑰兩次，而不需要為每個歐盟資料中心加密。對於歐盟銀行來說，這是一個很好的解決方案，但是在我們開始添加其他原則後，它無法擴展。想想這個例子：紐約市的資料中心可以擁有一個金鑰用於「`country: US`」原則，另一個金鑰用於「`country: US or region: EU`」，再一個金鑰用於「`not country: RU`」，等等... 您已經可以看到這會變得相當笨重低效。而且每次佈建新的資料中心，都必須重新評估所有原則並指派適當的金鑰。

每項原則及其否定的金鑰

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A key for each policy and its negation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44NAQRAAP1BPH05FQGS6HE.png&w=715&h=326&f=webp&fit=cover&position=center)

## Geo Key Manager v1：身分識別型加密和廣播加密

1978 年 RSA 的發明開啟了現代公開金鑰密碼編譯的時代，但是任何使用 GPG 或與憑證授權單位有關的人都可以證明，管理將金鑰連接到使用者身分識別的公開金鑰基礎結構是非常困難的。1984 年，Shamir 提出是否有可能建立公開金鑰加密系統，讓公開金鑰可以是任何字串。他提出這個問題的動機在於簡化電子郵件管理。Alice 不能使用 Bob 的公開金鑰將電子郵件加密給 Bob，而是可以將其加密到 Bob 的身分識別 [`bob@institution.org`](mailto:bob@institution.org)。最後，2001 年，[Boneh 和 Franklin](https://crypto.stanford.edu/~dabo/papers/bfibe.pdf) 實現了這個想法。

廣播加密是由 [Fiat 和 Naor](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/broad.pdf) 於 1993 年首次提出的。它讓您可以向所有人傳送相同的加密訊息，但只有具有正確金鑰的人才能對其進行解密。回顧第三個選項，我們並不是用每個歐盟資料中心的金鑰包裝客戶的金鑰，而是可以使用廣播加密對客戶的金鑰建立單一加密，只有位於歐盟的資料中心才能解密。這將解決儲存空間的問題。

Geo Key Manager v1 透過組合身分識別型廣播加密和身分識別型撤銷來實作存取控制。簡而言之，會為每個地區和每個資料中心位置指定一個身分識別集。然後，每台機器都會針對其地區和位置發出身分識別型私密金鑰。有了這個功能，可以使用三個資料集來控制對客戶金鑰的存取：加密到的地區集、要排除的地區內位置集，以及要包含的地區外位置集。例如，客戶的金鑰經過加密後，除了幾個特定位置以外，在所有地區內均可使用，也可以在這些地區以外的幾個位置使用。本篇部落格文章將討論有關這種方法的所有[細節](https://blog.cloudflare.com/geo-key-manager-how-it-works/)。

遺憾的是，此配置未能充分滿足客戶的需求；初始密碼編譯設定期間使用的參數（例如地區、資料中心及其屬性的清單）已經嵌入到系統中，無法輕易變更。而在英國退歐後將英國排除在歐盟地區之外，或者根據客戶需要的最新合規性標準支援新地區，更是難上加難。使用預先決定的靜態位置清單也很難快速撤銷機器存取權。此外，解密金鑰也無法指派給在設定後佈建的新資料中心，以防止它們加快要求速度。這些限制共同推動了將屬性型加密 (ABE) 整合到 Geo Key Manager 中的進程。

## 屬性型加密

2004 年，Amit Sahai 和 Brent Waters 提出了一種基於存取原則的新加密系統，稱為屬性型加密 (ABE)。本質上，訊息是根據存取原則而不是身分識別進行加密。根據使用者的屬性為其核發私密金鑰，而且只有在使用者的屬性符合原則時，才能解密訊息。與傳統的加密方法相比，這個系統實現了更靈活、更細緻的存取控制。

公開金鑰加密的簡要時間表

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Brief timeline of Public Key Encryption](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44ASAN03TC6BG7VMS8AJ6W.png&w=715&h=159&f=webp&fit=cover&position=center)

原則可以連結到金鑰或加密文字，導致 ABE 的兩種變體：金鑰原則屬性型加密 (KP-ABE) 和加密文字原則屬性型加密 (CP-ABE)。它們之間存在取捨，但在功能上是等同的，因為它們是一體兩面。我們將重點介紹 CP-ABE，這是因為它更符合真實世界的存取控制。想像一下，在一間醫院裡，醫生具有「`role: doctor`」和「`region: US`」屬性，而護士具有「`role: nurse`」和「`region: EU`」屬性。根據原則「`role: doctor or region: EU`」加密的文件可以由醫生和護士解密。換言之，ABE 就像一把神奇的鎖，只對具有正確屬性的人開啟。

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top} .tg .tg-0lax{text-align:left;vertical-align:top}

Policy | Semantics  
---|---  
country: US or region: EU | Decryption is possible either in the US or in the European Union  
not (country: RU or country: US) | Decryption is not possible in Russia and US  
country: US and security: high | Decryption is possible only in data centers within the US that have a high level of security (for some security definition established previously)  
  
原則

語意

country: US or region: EU

可以在美國或歐盟境內解密

not (country: RU or country: US)

在俄羅斯和美國無法解密

country: US and security: high
    
    
    publicKey, masterSecretKey := cpabe.Setup()
    
    policy := cpabe.Policy{}
    policy.FromString("country: US or region: EU")
    
    ciphertext := publicKey.Encrypt(policy, []byte("secret message"))
    
    attrsParisDC := cpabe.Attributes{}
    attrsParisDC.FromMap(map[string]string{"country": "FR", "region": "EU"}
    
    secretKeyParisDC := masterSecretKey.KeyGen(attrsParisDC)
    
    plaintext := secretKeyParisDC.Decrypt(ciphertext)
    
    assertEquals(plaintext, "secret message")

只有在美國境內具有高度安全性的資料中心才能解密（針對先前建立的某些安全性定義）

ABE 配置多種多樣，內容各異。我們選擇的配置必須滿足以下幾點要求：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Image: Key Distribution](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455Q09PHSB6PJAQT882QV2.png&w=715&h=326&f=webp&fit=cover&position=center)

  1. **否定** 我們希望能夠支援由 **AND** 、**OR** 和 **NOT** 組成的布林值公式，亦稱非單純布林值公式。雖然實際上每個配置都會處理 **AND** 和 **OR** ，但很少能找到 **NOT** 。藉助否定，封鎖某些國家/地區或機器會更輕鬆。
  2. **重複屬性** 看一下原則「`organization: executive or (organization: weapons and clearance: top-secret)`」。屬性「`organization`」在原則中重複了兩次。支援重複的配置大大增加了撰寫原則的可表達性和靈活性。
  3. **應對選擇加密文字攻擊的安全性** 大多數配置都是只在攻擊者不選擇要解密的訊息時才能確保安全（[CPA](https://en.wikipedia.org/wiki/Chosen-plaintext_attack)）。有一些[標準方法](https://www.cs.umd.edu/~jkatz/papers/id-cca-mac.pdf)可以將此類配置轉換為即使攻擊者操縱加密文字 ([CCA](https://en.wikipedia.org/wiki/Ciphertext_indistinguishability#Indistinguishability_under_chosen_ciphertext_attack/adaptive_chosen_ciphertext_attack_\(IND-CCA1,_IND-CCA2\))) 也可保證安全的配置，但它不是自動的。我們將眾所周知的 [Boneh-Katz 轉換](https://www.iacr.org/archive/pkc2011/65710074/65710074.pdf)應用於我們選擇的配置，以確保其在應對這類攻擊時的安全性。我們會在即將發表的白皮書中提供端對端配置的安全證明。



特別是否定，很值得讓我們多說幾句。若要讓屬性在否定時符合要求，名稱必須保持不變，但值必須不同。就像資料中心在說：「我有一個國家/地區，但它絕對不是日本」，而不是「我沒有國家/地區」。這似乎是反直覺的，但它可支援在不檢查每個屬性值的情況下進行解密。它還可以安全地逐步推出屬性。根據以上準則，我們最終選擇了 [Tomida 等人（2021 年）](https://eprint.iacr.org/2019/966)的配置。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Encryption using Master Public Key](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW470VSRWCKWA7W4ZET84JJS.png&w=715&h=326&f=webp&fit=cover&position=center)

實作諸如此類的複雜密碼編譯配置非常具有挑戰性。作為傳統公開金鑰密碼編譯基礎的離散記錄假設不足以滿足 ABE 的安全性需求。ABE 配置必須保護加密文字型和屬性型金鑰，而傳統的公開金鑰密碼編譯僅對加密文字施加安全性限制，而祕密金鑰僅僅是一個整數。為了實現這一目標，大多數 ABE 配置都是使用稱為雙線性配對的數學運算建構的。

我們執行配對運算的速度決定了我們的實作的基準效能。在解密過程中，配對運算的效率特別令人滿意，它們用於將屬性型祕密金鑰與加密文字相結合，以復原純文字。為此，我們依靠密碼編譯套件 CIRCL（有關詳細資訊，請參閱[之前的部落格](https://blog.cloudflare.com/circl-pairings-update/)）的開放原始碼程式庫中的高度最佳化的配對實作。此外，嵌入存取結構的各種金鑰、屬性和加密文字會以矩陣和向量表示。我們撰寫了線性代數常式來處理矩陣運算，例如乘法、轉置、逆矩陣等，這些運算是根據需要操作結構所必需的。我們還添加了序列化、廣泛測試和基準測試。最後，我們實作了向 [CCA2 安全](https://en.wikipedia.org/wiki/Adaptive_chosen-ciphertext_attack)配置的轉換。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Decryption using Attribute-based Secret Key \(Simplified\)](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48XC1EA0NR1HCDNVA650KZ.png&w=715&h=384&f=webp&fit=cover&position=center)

除了核心密碼編譯外，我們還必須決定如何表達和表示原則。最終，我們決定在我們的 API 中使用字串。雖然對於程式來說可能不太方便，但我們的配置的使用者無論如何都必須實作剖析器。由我們來替他們做這件事似乎可以讓介面變得更穩定。這意味著我們的原則語言的前端是由布林運算式組成的字串，例如「`country: JP or (not region: EU)`」，而後端是由電線和閘組成的_單純_布林電路。單純布林電路僅包括 AND 和 OR 閘。為了處理 NOT 閘，我們為電線指派了正值或負值。每個 NOT 閘都可以直接放在電線上，是因為[德摩根律](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)允許轉換「`not (X and Y)” into “not X or not Y`」這樣的公式，同樣也可進行析取。

以下是 API 示範。中央授權單位會執行安裝程式，以產生主要公開金鑰和主要祕密金鑰。任何人都可以使用主要公開金鑰透過存取原則來加密訊息。由中央授權單位持有的主要祕密金鑰，用於根據使用者的屬性為使用者產生祕密金鑰。屬性本身可以在頻外提供。在我們的案例中，我們依靠機器佈建資料庫來提供和驗證屬性。這些屬性型祕密金鑰會安全地散發給使用者，例如透過 TLS，並用於解密加密文字。該 API 還包括 helper 函數，用於檢查解密功能並從加密文字中擷取原則以提高可用性。

Solution | Flexible policies | Fault Tolerant | Efficient Space | Low Latency | Collusion-resistant | Changes to machines  
---|---|---|---|---|---|---  
Different copies of Quicksilver in data centers | ✅ |  | ✅ | ✅ | ✅ | ✅  
Complicated Business Logic in Core | ✅ |  | ✅ |  | ✅ | ✅  
Encrypt customer keys with each data center’s unique keypair | ✅ | ✅ |  | ✅ | ✅ |   
Encrypt customer keys with a policy-based keypair, where each data center has multiple policy-based keypairs |  | ✅ |  | ✅ | ✅ |   
Identity-Based Broadcast Encryption + Identity-Based Negative Broadcast Encryption(Geo Key Manager v1) |  | ✅ | ✅ | ✅ |  |   
Attribute-Based Encryption(Geo Key Manager v2) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅  
  
現在，我們回到原來的例子。這一次，中央授權單位持有主要祕密金鑰。每個資料中心中的每台機器都會向中央授權單位提供一組屬性，經過一些驗證後，會為該台特定機器產生唯一的屬性型祕密金鑰。當機器第一次啟動時，如果必須變換金鑰，或者屬性已變更，但絕不在 TLS 交握的關鍵路徑中，則會發出金鑰。此解決方案也可防止串通，這意味著兩台沒有適當屬性的機器無法合併其金鑰來解密無法單獨解密的密碼。例如，一台機器具有屬性「`country: US`」，另一台具有「`security: high`」。這兩台機器無法串通在一起，以使用「`country: US and security: high`」原則來解密資源。

至關重要的是，此解決方案可以無縫擴展並回應機器的變更。如果添加了一台新機器，中央授權單位可以為其發出一個祕密金鑰，因為該配置的參與者不必在安裝時預先決定，這與我們之前的身分識別廣播配置不同。

Scheme | Secret key(bytes) | Public key(bytes) | Overhead of encrypting 23 bytes  
(ciphertext length - message length) | Overhead of encrypting 10k bytes  
(ciphertext length - message length)  
---|---|---|---|---  
RSA-2048 | 1190 (PKCS#1) | 256 | 233 | 3568  
X25519 | 32 | 32 | 48 | 48  
GeoV1 scheme | 4838 | 4742 | 169 | 169  
GeoV2 ABE scheme | 33416 | 3282 | 19419 | 19419  
  
金鑰分佈

Scheme | Generating keypair | Encrypting 23 bytes | Decrypting 23 bytes  
---|---|---|---  
RSA-2048 | 117 ms | 0.043 ms | 1.26 ms  
X25519 | 0.045 ms | 0.093 ms | 0.046 ms  
GeoV1 scheme | 75 ms | 10.7 ms | 13.9 ms  
GeoV2 ABE scheme | 1796 ms | 704 ms | 62.4 ms  
  
當客戶上傳 TLS 憑證後，他們可以指定原則，而中央授權單位會根據指定的原則，使用主要公開金鑰來加密私密金鑰。然後，經過加密的客戶金鑰會寫入 Quicksilver，以便分佈到所有資料中心。在實踐中，這裡會有一個間接層，我們將在後面的章節中進行討論。

使用主要公開金鑰的加密

當使用者造訪客戶的網站時，位於先收到要求的資料中心的 TLS 終止服務會從 Quicksilver 擷取客戶的加密私密金鑰。如果服務的屬性不符合原則，解密就會失敗，並會將要求透過代理傳送到最近的符合原則的資料中心。無論哪一個資料中心可以成功解密金鑰，都會執行簽章以完成 TLS 交握。

使用屬性型祕密金鑰的解密（簡化）

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top}

解決方案

靈活的原則

容錯

高效的空間

Key | Purpose | CA in core | Core | Network  
---|---|---|---|---  
Master Public Key | Encrypts private policy keys over an access policy | Generate | Read |   
Master Secret Key | Generates secret keys for machines based on their attributes | Generate,Read |  |   
Machine Secret Key / Attribute-Based Secret Key | Decrypts private policy keys stored in global KV store, Quicksilver | Generate |  | Read  
Customer TLS Private Key | Performs digital signature necessary to complete TLS handshake to the customer’s website |  | Read (transiently on upload) | Read  
Public Policy Key | Encrypts customers’ TLS private keys |  | Generate,  
Read |   
Private Policy Key | Decrypts customer’s TLS private keys | Read (transiently during key rotation) | Generate | Read  
  
低延遲

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Policy Keys](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47QCNDER825G9PZ0MDJ5J5.png&w=715&h=359&f=webp&fit=cover&position=center)

防串通

機器變更

資料中心內不同的 Quicksilver 複本

✅

✅

✅

✅

✅

核心中複雜的商務邏輯

✅

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The results of fixing RPC failures in remote colo in Australia](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P0EAX61DPFTQ5T2Y1VEH.png&w=666&h=514&f=webp&fit=cover&position=center)

✅

✅

✅

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph: Uptime by Key Profile across US and EU for GeoV1 and GeoV2, and IN for GeoV2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YPQQY5WFS9F6QCC9RP6C.png&w=715&h=301&f=webp&fit=cover&position=center)

使用每個資料中心的唯一金鑰組來加密客戶金鑰

✅

✅

✅

✅

使用原則型金鑰組來加密客戶金鑰，每個資料中心都有多個原則型金鑰組

✅

✅

✅

身分識別型廣播加密 + 身分識別型負廣播加密(Geo Key Manager v1)

✅

✅

✅

屬性型加密(Geo Key Manager v2)

✅

✅

✅

✅

✅

✅

### 效能特性

我們描述了我們的配置在受 [ECRYPT](https://bench.cr.yp.to/results-encrypt.html) 啟發的措施上的效能。我們**將屬性大小設為 50** ，這對於大多數應用程式而言都明顯高於必要的值，但對於基準測試而言，它是最差的情況。我們在搭載 Intel Core i7-10610U CPU @ 1.80GHz 的筆記型電腦上進行測量，並將結果與提供 2048 位安全性的 RSA、X25519 以及我們以前的配置進行比較。

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top}

配置

祕密金鑰（位元組數）

公開金鑰（位元組數）

加密 23 個位元組的開銷（加密文字長度-訊息長度）

加密 1 萬個位元組的開銷（加密文字長度-訊息長度）

RSA-2048

1190 (PKCS#1)

256

233

3568

X25519

32

32

48

48

GeoV1 配置

4838

4742

169

169

GeoV2 ABE 配置

33416

3282

19419

19419

不同的屬性型加密配置可針對不同的效能設定檔進行最佳化。有些可能會快速產生金鑰，而另一些則可能優先考慮快速解密。在我們的案例中，我們只關心快速解密，因為它是該過程中唯一位於要求關鍵路徑中的部分。其他一切都發生在頻外，其中額外的開銷是可以接受的。

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top}

配置

產生金鑰組

加密 23 個位元組

解密 23 個位元組

RSA-2048

117 毫秒

0.043 毫秒

1.26 毫秒

X25519

0.045 毫秒

0.093 毫秒

0.046 毫秒

GeoV1 配置

75 毫秒

10.7 毫秒

13.9 毫秒

GeoV2 ABE 配置

1796 毫秒

704 毫秒

62.4 毫秒

### 有關屬性型存取控制 (ABAC) 的簡要說明

我們已經使用屬性型加密來實作通常所說的[屬性型存取控制 (ABAC)](https://csrc.nist.gov/Projects/Attribute-Based-Access-Control)。

ABAC 是較為熟悉的[角色型存取控制 (RBAC)](https://csrc.nist.gov/Projects/Role-Based-Access-Control) 的擴充。若要瞭解為什麼 ABAC 意義重大，我們先來簡單地討論一下它的起源。1970 年，美國國防部推出了判別存取控制 (DAC)。DAC 是 Unix 檔案系統的實作方式。但是，DAC 並不足以限制重新分享，因為資源的擁有者可以授與其他使用者權限，讓他們能夠以中央系統管理員不同意的方式存取資源。為了解決這個問題，國防部推出了強制存取控制 (MAC)。DRM 是 MAC 的一個很好的例子。即使您擁有該檔案，也沒有權利將其分享給其他人。

RBAC 實作了 MAC 的某些方面。ABAC 是 RBAC 的擴充，由 NIST 於 2017 年定義，以解決不限於角色之使用者日益增加的特性，例如一天中的時間、使用者代理程式等。

然而，RBAC/ABAC 只是一個規格。雖然傳統的實作方法是使用中央授權單位來監督對某些資源的存取，但事實未必如此。屬性型加密是在分散式系統中實作 ABAC 的絕佳機制。

## 金鑰變換

雖然可能會禁不住將所有失敗都歸咎於 DNS，但變更金鑰才是這場比賽中另一個強有力的競爭者。熬過了 Geo Key Manager v1 相當容易出錯的手動金鑰變換程序之後，我們學會了如何在不影響可用性的情況下進行可靠且簡單的金鑰變換，這是 Geo Key Manager v2 的明確設計目標。

為了促進金鑰變換並改善效能，我們在客戶金鑰包裝（加密）程序中引入了一個間接層。當客戶上傳 TLS 私密金鑰時，我們不會使用主要公開金鑰進行加密，而是會產生一個稱為_原則金鑰_ 的 X25519 金鑰組。然後，中央授權單位會將這個新產生的原則金鑰組的公用部分及其關聯的原則標籤新增至資料庫。然後，它會透過關聯的存取原則，使用主要公開金鑰來加密原則金鑰組的私密部分。客戶的私密金鑰會使用公開原則金鑰加密，並儲存到 Quicksilver 中。

當使用者存取客戶的網站時，位於接收要求的資料中心的 TLS 終止服務會擷取與客戶存取原則相關聯的加密原則金鑰。如果機器的屬性不符合原則，解密就會失敗，並會將要求轉送至最近的符合原則的資料中心。如果解密成功，則會使用原則金鑰來解密客戶的私密金鑰並完成交握。

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top}

金鑰

用途

核心中的 CA

核心

網路

主要公開金鑰

透過存取原則加密私密原則金鑰

產生

閱讀

主要祕密金鑰

根據機器的屬性為機器產生祕密金鑰

產生、讀取

機器祕密金鑰/屬性型祕密金鑰

解密儲存在全球 KV 存放區 Quicksilver 中的私密原則金鑰

產生

閱讀

客戶 TLS 私密金鑰

對客戶網站執行必要的數位簽章，以完成 TLS 交握

讀取（上傳時，暫時）

閱讀

公開原則金鑰

加密客戶的 TLS 私密金鑰

產生、讀取

私密原則金鑰

解密客戶的 TLS 私密金鑰

讀取（金鑰變換期間，暫時）

產生

閱讀

然而，並不會為每個客戶的憑證上傳產生原則金鑰。如下圖所示，如果客戶要求系統中已存在的原則，從而具有相關聯的原則金鑰，則會重複使用該原則金鑰。由於大多數客戶使用相同的少數原則，例如限於一個國家/地區或限於歐盟，因此，與客戶金鑰數量相比，原則金鑰的數量要小幾個數量級。

原則金鑰

這種原則金鑰共用機制對於金鑰變換非常有用。變換主要金鑰（以及機器祕密金鑰）時，只有少數用來控制客戶金鑰存取的原則金鑰需要重新加密，而不是每一個客戶的金鑰加密。如此便可減少運算和頻寬需求。此外，TLS 終止服務中的快取原則金鑰可減少關鍵路徑中頻繁解密的需求，進而改善效能。

這類似於混合式加密，其中使用公開金鑰密碼編譯來建立共用對稱金鑰，然後再用它來加密資料。不同之處在於，原則金鑰不是對稱的，而是 X25519 金鑰組，這是以橢圓曲線為基礎的非對稱配置。雖然速度沒有 AES 這樣的對稱配置那麼快，但傳統的橢圓曲線密碼編譯比屬性型加密要快得多。其優勢在於，中央服務不需要存取祕密金鑰資料即可加密客戶金鑰。

若要實現可靠的金鑰變換，還涉及到維護多個金鑰版本。最新的金鑰世代用於加密，但最新版本和舊版可用於解密。我們使用一個狀態系統來管理金鑰轉換和舊金鑰安全刪除。我們也部署了廣泛的監控，以便在任何機器未使用適當的金鑰世代時提醒我們。

## 規模的長尾效應

Geo Key Manager 受到較高的尾部延遲的影響，該延遲偶爾會影響可用性。Jeff Dean 的論文[《規模的長尾效應》](https://research.google/pubs/pub40801/)是一篇啟發性說明，闡述了即便是 Cloudflare 規模的 p99 延遲提高也會造成損壞。儘管對我們的服務的伺服器和用戶端元件進行了改進，但 p99 延遲並沒有任何讓步。這些改進（例如，從工作者集區切換到每個要求一個 goroutine）確實簡化了服務，因為它們移除了成千上萬行程式碼。分散式追蹤能夠固定延遲：它們發生在傳送要求的用戶端和接收要求的伺服器之間。但是，我們的研究只能到此為止了。去年，我們甚至撰寫了一篇部落格，來描述我們的[偵錯努力](https://blog.cloudflare.com/scaling-geo-key-manager/)，但並沒有產生具體的解決方案。

最後，我們意識到用戶端和伺服器之間存在一定的間接性。我們在世界各地的資料中心規模截然不同。為了避免連線將規模較小的資料中心淹沒，規模較大的資料中心會使用 Go net/rpc 程式庫，將透過代理傳送要求至其他資料中心的工作指派給個別的中繼機器。

一旦我們將中繼伺服器上的轉送功能納入追踪，問題就變得清晰了。發出要求和處理要求之間存在很長時間的延遲。然而，程式碼只是對內建的程式庫函數進行調用。為什麼會導致要求延遲呢？

最終，我們發現在序列化要求時保留了一個鎖。net/rpc 套件不支援資料流，但是我們在 GRPC 出現之前撰寫的封包導向的自訂應用程式通訊協定卻支援資料流。為了彌合這個差距，我們在序列化函數中執行了一個要求，並等待回應。雖然這是撰寫程式碼的權宜之計，但由於一次只能轉送一個要求，因此造成了效能瓶頸。

我們的解決方案是利用通道進行協調，讓多個要求在我們等待回應到達時執行。在推出該解決方案後，我們看到尾部延遲明顯降低了。

修正澳大利亞遠端共置中 RPC 失敗的結果

遺憾的是，我們（還）無法加快光速。如果客戶希望僅在美國境內保留金鑰，而其網站使用者位於澳大利亞（或紐西蘭）境內，則他們將不得不在我們進行跨太平洋航行時忍受一些延遲。但是多虧了工作階段票證，這些延遲只會影響新的連線。

運作時間也大大增加了。在密碼編譯初始化之後佈建的資料中心現在可以參與該系統，這也表示不符合特定原則的資料中心擁有了更廣泛的符合原則的鄰居，可以將簽署要求轉送給這些鄰居。這大大增強了系統的備援能力，尤其是那些位於沒有最佳網際網路連線的地區的資料中心會因此獲益。下圖顯示了在兩天時間內對全球每一台機器的成功探查。對於 GeoV1，我們看到美國和歐盟地區使用原則的網站一度降至 98％ 以下，而對於 GeoV2，運作時間很少低於 4 個 9 的可用性。

依金鑰設定檔的運作時間（使用 GeoV1 和 GeoV2 的美國和歐盟，以及使用 GeoV2 的印度）

## 結論

親愛的讀者，恭喜您走到了這一步。就像您一樣，應用密碼編譯已經走了很長一段路，但只有有限的一小部分能夠打破研究和實際採用之間的障礙。而彌合這種差距將有助於啟用新功能來保護敏感性資料。在過去幾年中，屬性型加密本身變得更高效，更有特點。我們希望這篇文章能夠促使您考慮採用 ABE 來滿足自己的存取控制需求，特別是如果您處理分散式系統且不想依賴高可用性的中央授權單位。我們已經在 [CIRCL](https://github.com/cloudflare/circl/tree/main/abe/cpabe/tkn20) 中開放了 CP-ABE 實作的程式碼，並計劃發佈白皮書來探討其他詳細資訊。

我們期待這項全新的密碼編譯基礎能夠為 Geo Key Manager 產品帶來巨大的改進。我們計劃使用這種基於 ABE 的機制，不僅儲存私密金鑰，而且還儲存其他類型的資料。我們正在努力提升它的便利性和普及性，以供內部服務使用。

## 特別感謝

我們要感謝 Watson Ladd 在 Cloudflare 任職期間對本專案的付出和貢獻。

......

1雖然對大多數客戶來說都是如此，但我們確實提供[無金鑰 SSL](https://www.cloudflare.com/ssl/keyless-ssl/)，讓可以執行自己的金鑰伺服器的客戶，能夠在內部部署儲存私密金鑰

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Finside-geo-key-manager-v2%2F&t=%E5%9C%A8%20Geo%20Key%20Manager%20v2%20%E5%85%A7%E9%83%A8%EF%BC%9A%E9%87%8D%E6%96%B0%E6%A7%8B%E6%83%B3%E5%88%86%E6%95%A3%E5%BC%8F%E7%B3%BB%E7%B5%B1%E7%9A%84%E5%AD%98%E5%8F%96%E6%8E%A7%E5%88%B6)[](https://x.com/intent/post?text=%E5%9C%A8+Geo+Key+Manager+v2+%E5%85%A7%E9%83%A8%EF%BC%9A%E9%87%8D%E6%96%B0%E6%A7%8B%E6%83%B3%E5%88%86%E6%95%A3%E5%BC%8F%E7%B3%BB%E7%B5%B1%E7%9A%84%E5%AD%98%E5%8F%96%E6%8E%A7%E5%88%B6&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Finside-geo-key-manager-v2%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Finside-geo-key-manager-v2%2F)[](https://bsky.app/intent/compose?text=%E5%9C%A8+Geo+Key+Manager+v2+%E5%85%A7%E9%83%A8%EF%BC%9A%E9%87%8D%E6%96%B0%E6%A7%8B%E6%83%B3%E5%88%86%E6%95%A3%E5%BC%8F%E7%B3%BB%E7%B5%B1%E7%9A%84%E5%AD%98%E5%8F%96%E6%8E%A7%E5%88%B6+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Finside-geo-key-manager-v2%2F)[](https://mastodonshare.com/?text=%E5%9C%A8+Geo+Key+Manager+v2+%E5%85%A7%E9%83%A8%EF%BC%9A%E9%87%8D%E6%96%B0%E6%A7%8B%E6%83%B3%E5%88%86%E6%95%A3%E5%BC%8F%E7%B3%BB%E7%B5%B1%E7%9A%84%E5%AD%98%E5%8F%96%E6%8E%A7%E5%88%B6&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Finside-geo-key-manager-v2%2F)[](https://www.threads.net/intent/post?text=%E5%9C%A8+Geo+Key+Manager+v2+%E5%85%A7%E9%83%A8%EF%BC%9A%E9%87%8D%E6%96%B0%E6%A7%8B%E6%83%B3%E5%88%86%E6%95%A3%E5%BC%8F%E7%B3%BB%E7%B5%B1%E7%9A%84%E5%AD%98%E5%8F%96%E6%8E%A7%E5%88%B6+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Finside-geo-key-manager-v2%2F)

## 相關標籤

[Geo Key Manager](https://blog.cloudflare.com/zh-tw/tag/geo-key-manager/)[密碼編譯](https://blog.cloudflare.com/zh-tw/tag/cryptography/)[研究](https://blog.cloudflare.com/zh-tw/tag/research/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
