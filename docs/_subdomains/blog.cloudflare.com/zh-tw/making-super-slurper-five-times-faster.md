---
url: https://blog.cloudflare.com/zh-tw/making-super-slurper-five-times-faster/
title: \u85c9\u52a9 Workers\u3001 Durable Objects \u548c Queues \u8b93 Super Slurper \u901f\u5ea6\u63d0\u5347 5 \u500d | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:01.080549+00:00
---

# 藉助 Workers、 Durable Objects 和 Queues 讓 Super Slurper 速度提升 5 倍 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/making-super-slurper-five-times-faster/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Cloudflare Queues](https://blog.cloudflare.com/zh-tw/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)+4顯示另外 4 個標籤

7 標籤顯示 7 個標籤

  * 文章標籤
  * [Cloudflare Queues](https://blog.cloudflare.com/zh-tw/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[Queues](https://blog.cloudflare.com/zh-tw/tag/queues/)[R2](https://blog.cloudflare.com/zh-tw/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/zh-tw/tag/r2-super-slurper/)
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



[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[Queues](https://blog.cloudflare.com/zh-tw/tag/queues/)[R2](https://blog.cloudflare.com/zh-tw/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/zh-tw/tag/r2-super-slurper/)

[Cloudflare Queues](https://blog.cloudflare.com/zh-tw/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[Queues](https://blog.cloudflare.com/zh-tw/tag/queues/)[R2](https://blog.cloudflare.com/zh-tw/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/zh-tw/tag/r2-super-slurper/)

2025年4月10日

# 藉助 Workers、 Durable Objects 和 Queues 讓 Super Slurper 速度提升 5 倍

![Connor Maddox](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GJCDNCNMKRFZB06B4MZ6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Siddhant Sinha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XJ1R2S5DZS8B6TDZBZ25.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Prasanna Sai Puvvada](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SJHBSH635BDQ2W9VQA8G.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Connor Maddox](https://blog.cloudflare.com/zh-tw/author/connor-maddox/)、[Siddhant Sinha](https://blog.cloudflare.com/zh-tw/author/siddhant/)和[Prasanna Sai Puvvada](https://blog.cloudflare.com/zh-tw/author/prasanna-sai-puvvada/)

閱讀時間：9 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/making-super-slurper-five-times-faster/)、[Deutsch](https://blog.cloudflare.com/de-de/making-super-slurper-five-times-faster/)、[Español](https://blog.cloudflare.com/es-es/making-super-slurper-five-times-faster/)、[Français](https://blog.cloudflare.com/fr-fr/making-super-slurper-five-times-faster/)、[日本語](https://blog.cloudflare.com/ja-jp/making-super-slurper-five-times-faster/)、[한국어](https://blog.cloudflare.com/ko-kr/making-super-slurper-five-times-faster/)和[简体中文](https://blog.cloudflare.com/zh-cn/making-super-slurper-five-times-faster/).

![BLOG-2731 Feature Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49756SEE9TPQPR5FT8SAFG.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////85OjwydfryNrx2eb36u308ezr///////+3+byvtHtu9Pz0eL65u338e7t////////3OX2tM7xr8/3yuD+5e378/Hx////////3+n7ttH2sdL8y+P/5/H/9vX2////////6fH/xtz7wt3/1+v/7vf/+/r7////////9fv/3Ov/2ev/6Pb/+P7/////////////////7vf/6/f/9f7/////////////////////9Pv/8vv/+///////////)

[_Super Slurper_](https://developers.cloudflare.com/r2/data-migration/super-slurper/) 是 Cloudflare 的資料遷移工具，旨在簡化雲端物件儲存提供者與 [_Cloudflare R2_](https://developers.cloudflare.com/r2/) 之間的大規模資料傳輸。自其推出以來，成千上萬的開發人員使用 Super Slurper 將 PB 級的資料從 AWS S3、Google Cloud Storage 和[ _其他與 S3 相容的服務_](https://developers.cloudflare.com/r2/data-migration/super-slurper/#supported-cloud-storage-providers)移至 R2。

但我們看到了一個可進一步加速效能的機會。我們使用開發人員平台（在 [_Cloudflare Workers_](https://developers.cloudflare.com/workers/)、[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/) 和 [_Queues_](https://developers.cloudflare.com/queues/) 基礎上構建），從頭開始重新架構 Super Slurper，並將傳輸速度提升高達 5 倍。在這篇文章中，我們將深入探討原始架構、我們識別的效能瓶頸、我們如何解決這些瓶頸，以及這些改善對真實世界的影響。

## 初始架構與效能瓶頸

Super Slurper 最初與 [_SourcingKit_](https://developers.cloudflare.com/images/upload-images/sourcing-kit/) 共用其架構，後者是專為將影像從 AWS S3 大量匯入 [_Cloudflare Images_](https://developers.cloudflare.com/images/) 而構建的工具。SourcingKit 部署在 Kubernetes 上，與 [_Images_](https://developers.cloudflare.com/images/) 服務一起執行。當我們開始構建 Super Slurper 時，我們將其拆分為自己的 Kubernetes 命名空間，並引入了一些新的 API，使其更方便用於物件儲存使用案例。此設定運作良好，並協助成千上萬的開發人員將資料移至 R2。

然而，它並非沒有挑戰。SourcingKit 並非設計用於處理 PB 級的大規模傳輸。SourcingKit 透過延伸 Super Slurper 在位於我們其中一個核心資料中心的 Kubernetes 叢集上運作，這意味著它必須與 Cloudflare 的控制平面、分析和其他服務共用運算資源和頻寬。隨著遷移數量的增長，這些資源限制明顯成為了瓶頸。

對於在物件儲存提供者之間傳輸資料的服務來說，工作很簡單：列出來源中的物件，將其複製到目的地，然後重複操作。這正是原始 Super Slurper 的運作方式。我們列出了來源貯體中的物件，將該清單推送至基於 Postgres 的佇列 (`pg_queue`)，然後以穩定的步調從此佇列中提取物件，以將物件複製過來。考慮到物件儲存遷移的規模，頻寬用量不可避免地會很高。這使得擴展變得極具挑戰性。

為了解決僅在我們的核心資料中心運作的頻寬限制問題，我們在組合中引入了 [_Cloudflare Workers_](https://developers.cloudflare.com/workers/)。我們並非在核心資料中心處理資料複製，而是開始呼叫 Worker 來進行實際複製：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44D530YYFHF6VPDT2G2NT5.png&w=715&h=498&f=webp&fit=cover&position=center)

隨著 Super Slurper 用量的增長，我們的 Kubernetes 資源消耗亦隨之增加。在資料傳輸期間，花費了相當長的時間等待網路 I/O 或儲存，而非實際執行運算密集型任務。因此，我們需要的不是更多記憶體或更多 CPU，而是更高的並行處理能力。

為了跟上需求，我們不斷增加複本計數。但最終我們碰壁了。在數十個數量級的 Pod 上執行時，我們面臨著可擴展性挑戰，而此時我們希望增加成倍的數量級。

我們決定從首要原則開始，重新思考整個方法，而不是依賴於我們繼承的架構。在大約一週的時間裡，我們使用 [_Cloudflare Workers_](https://developers.cloudflare.com/workers/)、[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/) 和 [_Queues_](https://developers.cloudflare.com/queues/) 構建了一個粗略的概念驗證。我們列出了來源貯體中的物件，將其推送至佇列，然後取用佇列中的訊息以啟動傳輸。雖然這聽起來與我們在原始實作中所做的非常相似，但在我們的開發人員平台上構建，可讓我們自動擴展一個數量級，比之前高一個數量級。

  * **Cloudflare Queues** ：支援非同步物件傳輸和自動擴展，以滿足遷移的物件數量。
  * **Cloudflare Workers** ：在沒有 Kubernetes 開銷的情況下執行輕量型運算任務，並最佳化流程每個部分的執行位置，以降低延遲並提高效能。
  * **SQLite 支援的 Durable Objects (DO)** ：充當完全分散式資料庫，從而消除單一 PostgreSQL 執行個體的限制。
  * **Hyperdrive** ：提供從原始 PostgreSQL 資料庫快速存取歷史工作資料的服務，並將其作為封存儲存。



我們執行了一些測試，發現我們的概念驗證對於小型傳輸（幾百個物件）來說比原始實作慢，但當傳輸擴展至數百萬個物件時，其速度則相當並最終超出原始執行效能。這就是我們需要投入時間，將概念驗証投入生產的訊號。

我們消除了概念驗證障礙，竭力提升穩定性，並尋找新的方法來使傳輸擴展至更高的並行度。經過幾次反覆運算，我們取得了滿意的結果。

## 新架構：Workers、Queues 和 Durable Objects

#### 處理層：管理遷移流程

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GAXDNPXMT21H1Q8CNN7M.png&w=715&h=251&f=webp&fit=cover&position=center)

處理層的核心是**佇列、取用者和工作者** 。流程如下：

#### 啟動遷移

用戶端觸發遷移後，首先會向我們的 **API Worker** 傳送一個請求。此 Worker 或取得遷移的詳細資料，將其儲存在資料庫中，並將一則訊息新增至 **List Queue** 以啟動該流程。

#### 列出來源貯體

**List Queue Consumer** 是事情開始好轉的階段。這會從佇列中提取訊息，從來源貯體擷取物件清單，套用任何必要的篩選條件，並將重要的中繼資料儲存在資料庫中。然後，透過將物件傳輸訊息排入佇列 **Transfer Queue** 來建立新任務。

我們會立即將新的批次工作排入佇列，從而最大限度地提高並行處理能力。當發生非預期失敗時（例如，從屬系統關閉），內建的節流機制可防止我們向佇列新增更多訊息。這有助於在中斷期間維持穩定性並防止過載。

#### 高效的物件傳輸

**Transfer Queue Consumer** Workers 從佇列中提取物件傳輸訊息，透過鎖定資料庫中的物件金鑰，來確保每個物件僅被處理一次。傳輸完成後，物件即會解鎖。對於較大的物件，我們將其分解為可管理的區塊，並以多部分上傳進行傳輸。

#### 從容地處理失敗

在任何分散式系統中，失敗都是不可避免的，我們必須確保將其考慮在內。我們對暫時性失敗實作了自動重試，因此問題不會中斷遷移流程。但是，如果無法透過重試解決問題，訊息將進入 **無效信件佇列 (DLQ)** ，並在此被記錄以供日後審查和解決。

#### 工作完成與生命週期管理

在列出所有物件且傳輸在進行中後，**Lifecycle Queue Consumer** 會密切關注所有物件。它會監控進行中的傳輸，從而確保不會留下任何物件。完成所有傳輸後，工作會標記為已完成，遷移流程結束。

### 資料庫層：持久儲存與舊版資料擷取

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46PPCT7KRZD27PS744HKQT.png&w=715&h=479&f=webp&fit=cover&position=center)

在構建新架構時，我們知道，我們需要一個強大的解決方案來處理龐大的資料集，同時確保擷取歷史工作資料。這正是我們的 **Durable Objects (DO)** 和 **Hyperdrive** 組合的用武之地。

#### Durable Objects

我們為每個帳戶提供了一個專用的 Durable Object 來追蹤遷移工作。每項**工作的 DO** 會儲存重要的詳細資料，例如，貯體名稱、使用者選項和工作狀態。這可確保一切井然有序且易於管理。為了支援大型遷移，我們還新增了一個 **Batch DO** ，用於管理排入佇列的傳輸物件，儲存其傳輸狀態、物件金鑰，以及任何額外的中繼資料。

隨著遷移規模擴展至**數十億個物件** ，我們必須在儲存方面發揮創造力。我們已實作分片策略來分散要求負載，從而防止瓶頸並解決 **SQLite DO 的 10 GB** 儲存限制。隨著物件的傳輸，我們會清除其詳細資料，並在此過程中最佳化儲存空間。十億個物件金鑰需要多大的儲存空間，實在令人驚訝！

#### Hyperdrive

由於我們正在重建的系統具有多年的遷移歷史，因此我們需要一種方法，來保留和存取過去的每一個遷移詳細資料。Hyperdrive 可充當通往舊版系統的橋樑，能夠從我們的核心 **PostgreSQL** 資料庫無縫擷取歷史工作資料。它不僅是一種資料擷取機制，更是適用於復雜遷移情境的封存。

## 結果：Super Slurper 現在將資料傳輸至 R2 的速度提升高達 5 倍

那麼，在完成所有這些操作之後，我們真的實現了加速傳輸的目標嗎？

我們執行了一項測試，將 75,000 個物件從 AWS S3 遷移至 R2。在最初的實作中，遷移需要 15 分 30 秒。在我們提高效能之後，只需 3 分 25 秒即可完成相同的遷移。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW477CPDAB1K3Y0SNDE0Z0SJ.png&w=715&h=360&f=webp&fit=cover&position=center)

當生產遷移於 2 月開始使用新服務時，我們發現，在某些情況下還有更大的改善，尤其在取決於物件大小的分散時。Super Slurper 已經存在[ _大約兩年_](https://blog.cloudflare.com/r2-super-slurper-ga/)了。而效能的改善使其能夠移動更多資料 — 在 Super Slurper 複製的所有物件中，有 35% 是在過去兩個月內複製的。

## 挑戰

使用新架構時，我們面臨的最大挑戰之一是處理重複的訊息。出現重複的情況有以下幾種：

  * 佇列提供至少一次傳遞，這意味著，取用者可能會多次收到相同的訊息以保證傳遞。
  * 失敗和重試亦可能會造成明顯的重複項。例如，如果在傳輸 Durable Object 之後對 Durable Object 的要求失敗，則重試可能會重新處理同一物件。



如果處理不當，可能會導致多次傳輸同一個物件。為了解決此問題，我們實作了幾種策略，來確保每個物件都準確計入且僅轉移一次：

  1. 由於是按順序列出（例如，若要取得物件 2，您需要列出物件 1 的連續權杖），我們會為每個列出操作指派一個序列 ID。這讓我們能夠偵測重複的清單，並防止多個流程同時啟動。這之所以特別有用，是因為我們需要等待資料庫和佇列操作完成，才會列出下一個批次。如果列出清單 2 失敗，我們可以重試；如果列出清單 3 已經開始，我們可以減少不必要的重試。
  2. 每個物件在傳輸開始時都會被鎖定，從而防止平行傳輸同一物件。成功傳輸後，透過從資料庫中刪除其金鑰來解鎖該物件。如果稍後再次出現該物件的訊息，且金鑰不再存在，則我們可以放心地假設其已被傳輸。
  3. 我們依賴於資料庫交易來保持計數的準確性。如果物件解鎖失敗，其計數保持不變。同樣，如果將物件索引新增至資料庫失敗，則不會更新計數，並且稍後將重試操作。
  4. 作為最後的故障保護，我們會檢查目標貯體中是否已存在物件，以及是否在開始遷移之後發佈。如果是，我們假設其由我們的流程（或其他流程）傳輸，並且安全地略過。



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44AHGCDWRPKVF577ESK4QA.png&w=715&h=228&f=webp&fit=cover&position=center)

## Super Slurper 的下一步行動是什麼？

我們一直在探索讓 Super Slurper 更快捷、更具可擴展性且更易用的方法，而這僅僅是開始。

  * 我們最近推出了從任何 [_S3 相容儲存提供者_](https://developers.cloudflare.com/changelog/2025-02-24-r2-super-slurper-s3-compatible-support/)進行遷移的功能！
  * 資料遷移目前仍限於每個帳戶同時遷移 3 個項目，但我們希望提高該限制。這將允許對物件字首拆分為單獨的遷移項目，並且可平行執行，從而顯著提高遷移貯體的速度。如需有關 Super Slurper 以及如何將資料從現有物件儲存體遷移至 R2 的詳細資訊，請參閱我們的[ _文件_](https://developers.cloudflare.com/r2/data-migration/super-slurper/)。



附註：作為本次更新的一部分，我們將與 API 互動變得更便捷，因此，現在能夠[ _以程式設計方式來管理遷移_](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/)！

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-super-slurper-five-times-faster%2F&t=%E8%97%89%E5%8A%A9%20Workers%E3%80%81%20Durable%20Objects%20%E5%92%8C%20Queues%20%E8%AE%93%20Super%20Slurper%20%E9%80%9F%E5%BA%A6%E6%8F%90%E5%8D%87%205%20%E5%80%8D)[](https://x.com/intent/post?text=%E8%97%89%E5%8A%A9+Workers%E3%80%81+Durable+Objects+%E5%92%8C+Queues+%E8%AE%93+Super+Slurper+%E9%80%9F%E5%BA%A6%E6%8F%90%E5%8D%87+5+%E5%80%8D&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-super-slurper-five-times-faster%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-super-slurper-five-times-faster%2F)[](https://bsky.app/intent/compose?text=%E8%97%89%E5%8A%A9+Workers%E3%80%81+Durable+Objects+%E5%92%8C+Queues+%E8%AE%93+Super+Slurper+%E9%80%9F%E5%BA%A6%E6%8F%90%E5%8D%87+5+%E5%80%8D+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-super-slurper-five-times-faster%2F)[](https://mastodonshare.com/?text=%E8%97%89%E5%8A%A9+Workers%E3%80%81+Durable+Objects+%E5%92%8C+Queues+%E8%AE%93+Super+Slurper+%E9%80%9F%E5%BA%A6%E6%8F%90%E5%8D%87+5+%E5%80%8D&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-super-slurper-five-times-faster%2F)[](https://www.threads.net/intent/post?text=%E8%97%89%E5%8A%A9+Workers%E3%80%81+Durable+Objects+%E5%92%8C+Queues+%E8%AE%93+Super+Slurper+%E9%80%9F%E5%BA%A6%E6%8F%90%E5%8D%87+5+%E5%80%8D+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-super-slurper-five-times-faster%2F)

## 相關標籤

[Cloudflare Queues](https://blog.cloudflare.com/zh-tw/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-tw/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/zh-tw/tag/durable-objects/)[Queues](https://blog.cloudflare.com/zh-tw/tag/queues/)[R2](https://blog.cloudflare.com/zh-tw/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/zh-tw/tag/r2-super-slurper/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
