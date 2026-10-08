---
url: https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/
title: \u8b93 Rust Workers \u66f4\u52a0\u53ef\u9760\uff1awasm\u2011bindgen \u4e2d\u7684 panic \u8207 abort \u5fa9\u539f | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:34:39.937269+00:00
---

# 讓 Rust Workers 更加可靠：wasm‑bindgen 中的 panic 與 abort 復原 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Internship Experience](https://blog.cloudflare.com/zh-tw/tag/internship-experience/)[Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)+8顯示另外 8 個標籤

11 標籤顯示 11 個標籤

  * 文章標籤
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)[Rust Workers](https://blog.cloudflare.com/zh-tw/tag/rust-workers/)[WASM](https://blog.cloudflare.com/zh-tw/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/zh-tw/tag/webassembly/)[可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)[工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)[開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)
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



[Rust Workers](https://blog.cloudflare.com/zh-tw/tag/rust-workers/)[WASM](https://blog.cloudflare.com/zh-tw/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/zh-tw/tag/webassembly/)[可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)[工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)[開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Internship Experience](https://blog.cloudflare.com/zh-tw/tag/internship-experience/)[Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)[Rust Workers](https://blog.cloudflare.com/zh-tw/tag/rust-workers/)[WASM](https://blog.cloudflare.com/zh-tw/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/zh-tw/tag/webassembly/)[可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)[工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)[開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

2026年4月22日

# 讓 Rust Workers 更加可靠：wasm‑bindgen 中的 panic 與 abort 復原

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/zh-tw/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/zh-tw/author/hood/)和[Logan Gatlin](https://blog.cloudflare.com/zh-tw/author/logan-gatlin/)

閱讀時間：9 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/making-rust-workers-reliable/)、[日本語](https://blog.cloudflare.com/ja-jp/making-rust-workers-reliable/)、[한국어](https://blog.cloudflare.com/ko-kr/making-rust-workers-reliable/)和[简体中文](https://blog.cloudflare.com/zh-cn/making-rust-workers-reliable/).

![BLOG-3145 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HQEZP84STFXFD0H3EBY7.png&w=2048&h=1152&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88O7x3uLt3eXz6e758/L19u/r//////7+5Ofzx9XuxNb01uP66ez38u7t//////7/2OH2rsjwqMj2w9j93+f77+3x////////1eL6psf0nsX6vdf/3uj/8PD2////////4Oz/t9T6sdT/y+P/5/H/9/f7////////8fr/1en/0ur/5Pb/9v7/////////////////7fr/7Pz/+P//////////////////////9///9v//////////////)

[_Rust Workers_](https://developers.cloudflare.com/workers/languages/rust/) 在 Cloudflare Workers 平台上執行時，會將 Rust 編譯為 WebAssembly，但正如我們所發現的，WebAssembly 存在一些棘手的邊緣問題。當發生 panic（恐慌）或非預期的 abort（中止）而導致問題時，執行時期可能會停留在未定義的狀態。對於 Rust Workers 的使用者來說，過去 panic 是致命的——它會損毀整個執行個體，甚至可能導致 Worker 在一段時間內完全無法運作。

雖然我們能夠偵測並減輕這些問題，但仍有微小機率導致 Rust Worker 意外失敗，並連帶使其他請求失敗。Worker 中一個未處理的 Rust abort 可能影響單一請求，進而升級為影響同級請求的更廣泛故障，甚至持續影響新進來的請求。其根本原因在於 wasm-bindgen（這個核心專案負責產生 Rust Workers 所依賴的 Rust 到 JavaScript 繫結）缺乏內建的復原語意。

在本文中，我們將分享最新版的 Rust Workers 如何處理全面的 Wasm 錯誤復原，以解決由中止導致的沙箱毒化問題。這項工作已作為我們[ _去年成立_](https://blog.rust-lang.org/inside-rust/2025/07/21/sunsetting-the-rustwasm-github-org/)的 wasm-bindgen 組織內部合作的一部分，回饋到 [_wasm-bindgen_](https://github.com/wasm-bindgen/wasm-bindgen) 專案中。首先是支援 `panic=unwind`，確保單一失敗請求永不毒化其他請求；其次是中止復原機制，保證 Wasm 上的 Rust 程式碼在中止後絕不會重新執行。 

## 初步的復原緩解措施

我們最初解決此領域可靠性的嘗試，著重於理解並控制在生產環境中 Rust Workers 因 Rust panic 與 abort 所導致的故障。我們引入了一個自訂的 Rust panic 處理器，用於追蹤 Worker 內的故障狀態，並在處理後續請求前觸發完整的應用程式重新初始化。在 JavaScript 端，這需要透過基於代理的間接層包裹 Rust-JavaScript 呼叫邊界，以確保所有進入點都被一致地封裝。我們還對產生的繫結進行了針對性修改，以便在故障後正確地重新初始化 WebAssembly 模組。

儘管這種方法依賴自訂的 JavaScript 邏輯，但它證明了可靠的復原是可以實現的，並消除了我們在實踐中所見的持續性故障模式。此解決方案自 0.6 版起已預設提供給所有 workers‑rs 使用者，並為後續章節中描述的、更通用且已貢獻給上游的 abort 復原機制奠定了基礎。

## 使用 WebAssembly 異常處理實現 `panic=unwind`

前面所述的 abort 復原機制，確保了 Worker 能夠在故障後存活下來，但代價是重新初始化整個應用程式。對於無狀態的請求處理器來說，這沒問題。但對於那些在記憶體中保存有意義狀態的工作負載（例如 Durable Objects），重新初始化就意味著完全丟失該狀態。一個請求中的單一 panic，就可能清除掉其他並行請求正在使用的記憶體狀態。

在大多數原生 Rust 環境中，panic 可以被展開 (unwind)，讓解構子 (destructor) 得以執行，程式也能在不遺失狀態的情況下復原。然而在 WebAssembly 中，情況歷來截然不同。透過 `wasm32-unknown-unknown` 編譯為 Wasm 的 Rust，預設是 `panic=abort`，因此 Rust Worker 內部的 panic 會突然觸發一個 `unreachable` 指令，然後拋出 `WebAssembly.RuntimeError`，從 Wasm 退出並回到 JavaScript。

為了在不丟棄執行個體狀態的情況下從 panic 復原，我們需要在 wasm-bindgen 中為 `wasm32-unknown-unknown` 提供 `panic=unwind` 的支援。這透過 WebAssembly 異常處理提案得以實現，該提案在 2023 年獲得了廣泛的引擎支援。

我們從編譯命令 `RUSTFLAGS='-Cpanic=unwind' cargo build -Zbuild-std` 開始，此命令以支援展開的方式重新建置標準函式庫，並產生帶有正確 panic 展開行為的程式碼。例如：
    
    
    struct HasDropA;
    struct HasDropB;
    extern "C" {
        fn imported_func();
    }
    
    fn some_func() {
        let a = HasDropA;
        let b = HasDropB;
        imported_func();
    }

編譯為 WebAssembly 程式碼後，其結構大致如下：
    
    
    try
      call <imported_func>
    catch_all
      call <drop_b>
      call <drop_a>
      rethrow
    end
    call <drop_b>
    call <drop_a>

這確保了即使 `imported_func()` 發生 panic，解構子仍會執行。類似地，`std::panic::catch_unwind(|| some_func())` 會被編譯成：
    
    
    try
      call <some_func>
      ;; set result to Ok(return value)
    catch
      try
        call <std::panicking::catch_unwind::cleanup>
        ;; set result to Err(panic payload)
      catch_all
        call <core::panicking::cannot_unwind>
        unreachable
      end
    end

要使這項功能端到端正常運作，需要對 wasm-bindgen 工具鏈進行多項變更。WebAssembly 剖析器 Walrus 原本不知道如何處理 try/catch 指令，因此我們增加了對它們的支援。描述子解釋器也需要學習如何評估包含異常處理區塊的程式碼。至此，完整的應用程式就可以用 `panic=unwind` 建構了。

最後一步是修改 wasm-bindgen 產生的匯出，使其在 Rust-JavaScript 邊界捕捉 panic，並將其表示為 JavaScript 的 `PanicError` 異常。一個細節需要注意：當在透過 `extern "C"` 函式展開時，Rust 會捕捉外來異常並中止，因此匯出需要標記為 `extern "C-unwind"` 以明確允許跨邊界展開。對於 future，panic 會拋出 `PanicError` 並拒絕 JavaScript `Promise`。

Closure（閉包）需要特別關注，以確保展開安全性被正確檢查。我們透過一個新的 `MaybeUnwindSafe` 特質來實現，該特質僅在以 `panic=unwind` 建構時才檢查 `UnwindSafe`。不過，這也迅速暴露了一個問題：許多 closure 會捕獲那些在展開後仍然存在的參照，這使得它們本質上不具備展開安全性。為了避免鼓勵使用者為了滿足編譯器而錯誤地將 closure 包裝在 `AssertUnwindSafe` 中，我們加入了 `Closure::new_aborting` 變體。在無法保證展開安全性的情況下，這些變體會在發生 panic 時終止而不是展開。

啟用 panic 展開後：

  * 在匯出的 Rust 函式中發生的 panic 會被 wasm-bindgen 捕捉
  * panic 以 PanicError 異常的形式呈現給 JavaScript
  * 非同步匯出會拋出 PanicError 並拒絕其傳回的 Promise
  * Rust 解構子正確執行
  * WebAssembly 執行個體保持有效且可重複使用



關於此方法的完整詳細資訊，以及如何在 wasm-bindgen 中使用它，請參閱最新的 [_Wasm Bindgen: Catching Panics_](https://wasm-bindgen.github.io/wasm-bindgen/reference/catch-unwind.html) 指南頁面。

## Abort 復原

即使有了 `panic=unwind` 的支援，abort 仍然會發生——記憶體不足錯誤就是一個常見的原因。由於 abort 無法展開，根本不可能進行狀態復原，但我們至少可以偵測並從 abort 中復原，以便未來的操作能夠執行，避免因無效狀態導致後續請求失敗。

Panic unwind 的支援為 abort 復原帶來了一個新問題。當我們從 Wasm 收到一個錯誤時，我們無法得知它是來自 `extern "C-unwind"` 外部函式所造成的錯誤，還是一個真正的 abort。在 WebAssembly 中，abort 可能有多種形式。

我們有兩種技術選項來解決此問題：一是標記所有確定是 abort 的錯誤，二是標記所有確定是 unwind 的錯誤。這兩者都可運作，但我們選擇了後者。由於我們的外部異常處理已直接使用原生 WAT 級別（WebAssembly 文字格式）異常處理指令，因此，我們發現外部異常的標籤實作相對簡便，從而能夠將其與那些導致中止且無法安全展開的異常區分開來。

得益於 WebAssembly 異常處理中的 `Exception.Tag` 功能，我們能夠清楚區分可復原和不可復原的錯誤，從而整合一個新的中止處理器 (abort handler) 以及中止重入防護 (abort reentrancy guards)。  
  
在初始化時，可以使用新的掛勾 `set_on_abort` 來附加一個處理器，根據平台嵌入的需求進行相應的復原。

強化 panic 和 abort 處理對於避免無效執行狀態至關重要。WebAssembly 允許深度交織的呼叫堆疊，Wasm 可以呼叫 JavaScript，而 JavaScript 也可以在任意深度重新進入 Wasm，與此同時，多個任務可以在同一個執行個體中運作。過去，在一個任務或巢狀堆疊中發生的 abort，並不保證會透過 JavaScript 使更高層的堆疊失效，這導致了未定義行為。我們需要仔細確保能夠保證執行模型，這方面的工作仍在持續進行。

雖然中止絕非理想情況，且在故障時重新初始化是最壞的狀況，但實作關鍵錯誤復原作為最後一道防線，能確保執行的正確性，並使未來操作能夠成功。無效狀態不會持續存在，確保單一故障不會引發連鎖故障。

## 擴展：為 wasm-bindgen 函式庫提供 abort 重新初始化

在進行這項工作時，我們意識到這對於被 JavaScript 使用且透過 wasm-bindgen 建置的函式庫來說，是一個常見問題。若能為其附加上中止處理器以執行復原，這些函式庫也將從中受益。

但是，當將 Wasm 建置為 ES 模組並直接匯入時（例如透過 `import { func } from 'wasm-dep'`），如果在呼叫 `func()` 時發生 Wasm abort，對於一個已經連結並初始化、正在使用者 JS 應用程式中執行的函式庫來說，目前尚不清楚其具體的復原機制應如何設計。

雖然這嚴格來說不是 Rust Workers 的使用情境，但我們的團隊也支援執行基於 Rust 的 Wasm 函式庫相依項、基於 JavaScript 的 Workers 使用者。如果我們能同時解決這個問題，這將間接惠及 Cloudflare Workers 平台上的 Wasm 使用情境。

為了支援 Wasm 函式庫使用情境的自動 abort 復原，我們在 wasm‑bindgen 中新增了對實驗性重新初始化機制 -`-reset-state-function` 的支援。這提供了一個函式，允許 Rust 應用程式在下次呼叫時，有效地請求將其內部的 Wasm 執行個體重設回初始狀態，而無需所產生之繫結的使用者重新導入或重新建立它們。來自舊執行個體的類別執行個體會因為其控制代碼 (handles) 變成孤立 (orphaned) 而拋出錯誤，但之後可以建構新的類別。使用 Wasm 函式庫的 JS 應用程式會收到錯誤，但不會完全失效。

此功能的完整技術細節，以及如何在 wasm-bindgen 中使用它，請參閱最新的 wasm-bindgen 指南章節：[ _Wasm Bindgen: Handling Aborts_](https://wasm-bindgen.github.io/wasm-bindgen/reference/handling-aborts.html)。

## 完善 Rust Wasm 異常處理生態系統

這項工作的上游貢獻並未止步於 wasm-bindgen 專案。使用 `panic=unwind` 建置 Wasm 仍然需要一個實驗性的 nightly Rust 目標，因此我們也一直在努力推動 Rust 對 WebAssembly 異常處理的 Wasm 支援，以協助其進入穩定的 Rust 版本。

在 WebAssembly 異常處理的開發過程中，一個後期的規範變更導致了兩個變體的出現：[ _舊式異常處理_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/legacy/Exceptions.md)和最終的現代異常處理 ([_exception handling "with exnref"_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md))。目前，Rust 的 WebAssembly 目標預設仍產生舊式變體的程式碼。雖然舊式異常處理獲得廣泛支援，但現已遭棄用。

自以下 JS 平台版本發布起，現代 WebAssembly 異常處理功能已正式獲得支援：

執行階段| 版本| 發布日期  
---|---|---  
v8| 13.8.1| 2025 年 4 月 28 日  
workerd| v1.20250620.0| 2025 年 6 月 19 日  
Chrome| 138| 2025 年 6 月 28 日  
Firefox| 131| 2024 年 10 月 1 日  
Safari| 18.4| 2025 年 3 月 31 日  
Node.js| 25.0.0| 2025 年 10 月 15 日  
  
在我們調查這份支援矩陣時，最令人擔憂的問題最終落在 Node.js 24 LTS 的發布排程上，這可能會使整個生態系統直到 2028 年 4 月都停留在舊式 WebAssembly 異常處理上。

發現這個差異後，我們成功將現代異常處理反向移植 (backport) 到了 Node.js 24 版本中，甚至將必要的修正反向移植到 Node.js 22 版本線，以確保對此目標的支援。這應能使現代異常處理提案在明年成為預設目標。

在未來幾個月，我們將致力於讓轉向穩定的 `panic=unwind` 和現代異常處理的過程，對終端使用者盡可能無感。

雖然這些對生態系統的長期投入需要時間，但它們有助於為整個 Rust WebAssembly 社群建立更堅實的基礎，我們很高興能夠為這些改進做出貢獻。

## 在 Rust Workers 中使用 panic unwind

自 Rust Workers 0.8.0 版起，我們新增了一個 `--panic-unwind` 旗標，可依[ _此處指示_](https://github.com/cloudflare/workers-rs?tab=readme-ov-file#panic-recovery-with---panic-unwind)將其加入建置命令。

啟用此旗標後，panic 可以被完全復原，且 abort 復原將使用新的 abort 分類與復原鉤子機制。我們強烈建議您升級並嘗試使用，以獲得更穩定的 Rust Workers 體驗，並計劃在後續版本中將 `panic=unwind` 設為預設。繼續使用 `panic=abort` 的使用者，仍然可以享有從 0.6.0 版開始提供的自訂復原包裝處理。

## 致力於 Rust Workers 的穩定性

此項工作是我們持續邁向 Rust Workers 穩定版發布的一部分。透過從根源解決 Wasm 平台基礎的這些棘手問題，並在適當之處回饋生態系統，我們不僅為自身平台，也為整個 Rust、JS 和 Wasm 生態系統建立更強大的基礎。

我們為 Rust Workers 規劃了多項未來改進，並將很快分享關於這些額外工作的更新，包括 wasm-bindgen 泛型與自動化 bindgen。我們團隊的 Guy Bedford 上個月在 [_Wasm.io 的一場關於 Rust 與 JS 互通性_](https://www.youtube.com/watch?v=zlSJY8Qv5XI)的演講中，已經預告了這些內容。

歡迎在 [_Cloudflare Discord_](https://discord.com/invite/cloudflaredev) 的 **#rust‑on‑workers** 頻道中與我們聯絡。我們也歡迎對 [_workers-rs_](https://github.com/cloudflare/workers-rs) 和 [_wasm-bindgenGitHub_](https://github.com/wasm-bindgen/wasm-bindgen) 專案的回饋與討論，並歡迎所有新的貢獻者加入。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-rust-workers-reliable%2F&t=%E8%AE%93%20Rust%20Workers%20%E6%9B%B4%E5%8A%A0%E5%8F%AF%E9%9D%A0%EF%BC%9Awasm%E2%80%91bindgen%20%E4%B8%AD%E7%9A%84%20panic%20%E8%88%87%20abort%20%E5%BE%A9%E5%8E%9F)[](https://x.com/intent/post?text=%E8%AE%93+Rust+Workers+%E6%9B%B4%E5%8A%A0%E5%8F%AF%E9%9D%A0%EF%BC%9Awasm%E2%80%91bindgen+%E4%B8%AD%E7%9A%84+panic+%E8%88%87+abort+%E5%BE%A9%E5%8E%9F&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-rust-workers-reliable%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-rust-workers-reliable%2F)[](https://bsky.app/intent/compose?text=%E8%AE%93+Rust+Workers+%E6%9B%B4%E5%8A%A0%E5%8F%AF%E9%9D%A0%EF%BC%9Awasm%E2%80%91bindgen+%E4%B8%AD%E7%9A%84+panic+%E8%88%87+abort+%E5%BE%A9%E5%8E%9F+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-rust-workers-reliable%2F)[](https://mastodonshare.com/?text=%E8%AE%93+Rust+Workers+%E6%9B%B4%E5%8A%A0%E5%8F%AF%E9%9D%A0%EF%BC%9Awasm%E2%80%91bindgen+%E4%B8%AD%E7%9A%84+panic+%E8%88%87+abort+%E5%BE%A9%E5%8E%9F&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-rust-workers-reliable%2F)[](https://www.threads.net/intent/post?text=%E8%AE%93+Rust+Workers+%E6%9B%B4%E5%8A%A0%E5%8F%AF%E9%9D%A0%EF%BC%9Awasm%E2%80%91bindgen+%E4%B8%AD%E7%9A%84+panic+%E8%88%87+abort+%E5%BE%A9%E5%8E%9F+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fmaking-rust-workers-reliable%2F)

## 相關標籤

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Internship Experience](https://blog.cloudflare.com/zh-tw/tag/internship-experience/)[Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)[Rust Workers](https://blog.cloudflare.com/zh-tw/tag/rust-workers/)[WASM](https://blog.cloudflare.com/zh-tw/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/zh-tw/tag/webassembly/)[可靠性](https://blog.cloudflare.com/zh-tw/tag/reliability/)[工程設計](https://blog.cloudflare.com/zh-tw/tag/engineering/)[開源資源](https://blog.cloudflare.com/zh-tw/tag/open-source/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)[開發人員平台](https://blog.cloudflare.com/zh-tw/tag/developer-platform/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
