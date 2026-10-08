---
url: https://blog.cloudflare.com/zh-tw/rollbacks-for-workflows/
title: \u6211\u5011\u5982\u4f55\u70ba Cloudflare Workflows \u6253\u9020 Saga \u5fa9\u539f\u529f\u80fd | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:39.873854+00:00
---

# 我們如何為 Cloudflare Workflows 打造 Saga 復原功能 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/rollbacks-for-workflows/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Workflows](https://blog.cloudflare.com/zh-tw/tag/workflows/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)

3 標籤顯示 3 個標籤

  * 文章標籤
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Workflows](https://blog.cloudflare.com/zh-tw/tag/workflows/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)
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



[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Workflows](https://blog.cloudflare.com/zh-tw/tag/workflows/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)

2026年6月25日

# 我們如何為 Cloudflare Workflows 打造 Saga 復原功能

![Vaishnav Kavitha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMMZ8JJQ1SE783SASV4PJ.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Mia Malden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4559TC07A12MQHAEK8YM1R.jpg&w=64&h=64&f=webp&fit=cover&position=center)![André Venceslau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TZTSTWQ6JMKEC8GX38NE.png&w=64&h=64&f=webp&fit=cover&position=center)

[Vaishnav Kavitha](https://blog.cloudflare.com/zh-tw/author/vaishnav-kavitha/)、[Mia Malden](https://blog.cloudflare.com/zh-tw/author/mia/)和[André Venceslau](https://blog.cloudflare.com/zh-tw/author/andre-venceslau/)

閱讀時間：11 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/rollbacks-for-workflows/)、[日本語](https://blog.cloudflare.com/ja-jp/rollbacks-for-workflows/)、[한국어](https://blog.cloudflare.com/ko-kr/rollbacks-for-workflows/)和[简体中文](https://blog.cloudflare.com/zh-cn/rollbacks-for-workflows/).

![BLOG-3317 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMM3AX6SCQ1TVSR6M8NMX.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+P/84u3z1uPw4Onz8PP39fX07u3s////+v/+4+320+Dy1+L15ez57fD27O3u/////f//5+/509/1z9742uX85uz57O3x////////7vT+2eP50d/82OX/5ez97/D1////////+Pz/5ez+3ef/4uv/7fL/9fb6////////////9Pf/7/P/8vf/+fv//fz+/////////////////f3/////////////////////////////////////////////)

Cloudflare Workflows 讓您能夠建置持久化的多步驟應用程式，並在長時間執行的過程中內建重試機制和狀態持久化。當 [_Workflow_](https://developers.cloudflare.com/workflows/) 執行時，每個步驟都可以呼叫外部系統、重試失敗的步驟，並在重新啟動之間持續保存狀態。但如果某個步驟失敗，可能會導致先前已完成步驟的早期工作處於不一致或部分完成的狀態。

今天，我們為 Workflows 推出了 Saga 復原 (rollback) 功能，讓您可以在步驟定義中直接宣告失敗時的復原邏輯。

舉例來說，考慮一個在兩家不同銀行帳戶之間轉帳的工作流程：

  1. 從 A 銀行帳戶扣款
  2. 存入 B 銀行帳戶
  3. 傳送電子郵件確認給兩個帳戶持有人



如果第 2 步（存入 B 銀行帳戶）失敗了會怎樣？一旦在 A 銀行的扣款成功，該交易就已提交，資金已離開其系統。作為交易協調者，您無法簡單地在 A 銀行的系統中「復原」該操作。相反地，您必須透過一項在語意上與首次操作相反的新操作，將款項重新存入銀行 A 的帳戶。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WKYMHAWC2FCMBSGG1XMKT.png&w=715&h=681&f=webp&fit=cover&position=center)

  
這種「操作」與其對應「補償邏輯」的配對，即稱為 [_Saga 模式_](https://www.youtube.com/watch?v=xDuwrtwYHu8)。

在今天之前，開發人員必須在步驟的直接定義之外，自行實作補償邏輯來追蹤哪些步驟成功、哪些失敗，以及失敗時應採取哪些行動。現在，您可以在每個 `step.do()` 中，將補償邏輯作為參數定義在步驟本身內部，同時確保復原過程本身也具備 Workflow 的持久性保證。
    
    
    // track what completed so we know what to undo
    let debitA;
    let creditB;
    try {
      debitA = await step.do("debit-bank-a", () => bankA.debit(from, amount));
      creditB = await step.do("credit-bank-b", () => bankB.credit(to, amount));
      await step.do("notify", () => notifyBoth(from, to, amount));
    } catch (error) {
      // unwind in reverse. each undo is its own durable step,
      // must be idempotent, and must keep going if one fails.
      if (creditB) {
        try {
          await step.do("reverse-credit-b", () => bankB.debit(to, amount, creditB.id));
        } catch (e) {
          await alertOnCall("reverse-credit-b failed", e);
        }
      }
      if (debitA) {
        try {
          await step.do("refund-debit-a", () => bankA.credit(from, amount, debitA.id));
        } catch (e) {
          await alertOnCall("refund-debit-a failed", e);
        }
      }
      throw error;
    }

_沒有復原功能時_
    
    
     // each step ships with its own undo. add a step,
    // add its rollback right here. no growing catch
    // block, no manual ordering, no replay logic.
    await step.do("debit-bank-a", () => bankA.debit(from, amount), {
      rollback: async ({ output }) => bankA.credit(from, amount, output.id),
    });
    await step.do("credit-bank-b", () => bankB.credit(to, amount), {
      rollback: async ({ output }) => bankB.debit(to, amount, output.id),
    });
    await step.do("notify", () => notifyBoth(from, to, amount));

_使用復原功能時_

## 試用

要使用復原功能，只需將包含 `rollback` 函式的選項物件作為最後一個引數傳遞給 `step.do()` 即可。
    
    
    const debit = await step.do(
      "debit-account-a",
      async () => {
        return await bankA.debit({
          accountId: fromAccountId,
          amount,
          idempotencyKey: `${transferId}:debit-account-a`,
        });
      },
      {
        rollback: async () => {
          await bankA.credit({
            accountId: fromAccountId,
            amount,
            idempotencyKey: `${transferId}:rollback-debit-account-a`,
          });
        },
      }
    );
    
    // The idempotency keys make both the forward operations and rollback operations safe to retry without duplicating the transfer
    
    const credit = await step.do(
      "credit-account-b",
      async () => {
        return await bankB.credit({
          accountId: toAccountId,
          amount,
          idempotencyKey: `${transferId}:credit-account-b`,
        });
      },
      {
        rollback: async ({ output }) => {
          if (output === undefined) {
            return;
          }
    
          await bankB.debit({
            accountId: toAccountId,
            amount,
            idempotencyKey: `${transferId}:rollback-credit-account-b`,
          });
        },
      }
    );
    
    
    // If we fail here, we may want to revert all previous payments. Users should not have to wrap their code in complex try-catch logic just to revert two small payments (see below)
    
    await step.do("send-confirmation", async () => {
      await sendTransferConfirmation({ ... });
    });

復原函式應具備冪等性 (idempotent)，就像一般的 Workflow 步驟一樣。如果您要退還一筆費用，請使用付款服務商的冪等金鑰。如果您要釋放庫存，請確保釋放操作可以安全地被呼叫多次。

如果任何步驟失敗，復原處理器將以`步驟開始`的相反順序執行。聽起來很簡單：當有問題發生時執行復原步驟。在實務上，有一些細節使得 API 和執行模型變得很重要。

1.**失敗的步驟可能仍需要復原。** 如果一個失敗的 `step.do()` 有註冊復原處理器，它仍然可以有資格執行復原。

如果使用者程式碼捕捉到錯誤且 Workflow 繼續執行，則復原不會開始；但如果捕捉錯誤後，Workflow 後來因其他原因失敗，則先前註冊的處理器仍可執行復原，它們會以`步驟開始`的相反順序執行。

為什麼？因為該步驟可能在失敗之前已與外部系統進行了部分互動。例如，付款服務商可能已扣款成功，但步驟可能在將 `chargeId` 傳回給 Workflows 之前就失敗了。這就是為什麼復原處理器會收到 `output`，但必須處理 `output === undefined` 的情況。

2\. **復原僅在 Workflow 失敗時才啟動。** 加入復原處理器並不表示每個步驟錯誤都會觸發復原。如果使用者程式碼捕捉了錯誤並繼續執行，Workflow 就會繼續。復原會在 Workflow 本身即將最終失敗時啟動。

當復原啟動時，Workflows 會尋找符合資格的 `step.do()` 呼叫，執行它們的復原處理器，然後記錄最終的 Workflow 失敗。

3\. **執行順序必須是可預測的。** 對於循序 (sequential) Workflow，復原順序很直觀：

  1. 保留庫存。
  2. 信用卡扣款。
  3. 建立出貨單。
  4. 如果出貨失敗，就退款並釋放庫存。



但當涉及平行步驟時，情況就比較微妙。步驟的完成順序可能與開始順序不同，因此 Workflows 採用的是反向步驟開始順序，而非反向完成順序。

實際的規則是：

  1. 任何已開始或已完成且具有復原處理器的步驟都符合資格。
  2. 失敗的 `step.do()` 如果有註冊復原處理器，也符合資格。
  3. 處理器以反向步驟開始順序執行，而不是完成順序。



## API 設計過程

在確立預期的行為邏輯後，我們需要將這套新模式整合進 Workflows API。復原功能其實歷經了好幾次疊代，才最終定案為目前的 `rollback options`。

### 為什麼不是流暢式 (fluent) 或建造者 (builder) 風格的 API？

第一種方法是流暢式寫法：`step.do(...).rollback(...)`。這種寫法可讀性極佳。正向動作和補償動作並列在一起，呼叫點看起來就像一般的 JavaScript 鏈式呼叫。

問題在於，`step.do()` 已經有了一個重要的意義：它啟動一個持久化步驟，並回傳一個代表該步驟輸出的 Promise。在 Workers 中，類 Promise 的值特別重要，因為 Workers RPC 支援 [_Promise 管線化_](https://blog.cloudflare.com/capnweb-javascript-rpc-library/#chained-calls-promise-pipelining)，這是一種繼承自 [_Cap'n Proto_](https://capnproto.org/rpc.html#time-travel-promise-pipelining) 等系統的模式。

Promise 管線化讓程式碼可以在一個未來值完全回傳給呼叫者之前，就先呼叫該值上的方法。例如：
    
    
    const session = api.authenticate(apiKey);
    const name = await session.whoami();

在這裡，`session` 還不是真正的 session 物件。它比較像是一個即將存在之 session 的控制代碼 (handle)。當您呼叫 `session.whoami()` 時，Workers 可以提早將該呼叫傳送到遠端，並表示：「一旦驗證建立了 session，就在它上面呼叫 `whoami()`。」

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMVWKS68D8HCFGVRZQ2RA.png&w=715&h=476&f=webp&fit=cover&position=center)

這樣可以省去一次往返。呼叫者不需要等到 `authenticate()` 完全完成，就可以要求 `whoami()`。

我們考慮過流暢式 API：
    
    
    step.do("charge-card", chargeCard).rollback(refundCharge);

  
對讀者來說，這看起來像是「在 `charge-card` 的結果上呼叫 `.rollback()`」。但復原並不是步驟輸出的一部分。它是 `step.do()` 選項的一部分，且必須在步驟啟動前就完成註冊，這樣 Workflows 才知道若後續步驟失敗時該如何補償。

流暢式 API 也讓步驟的時序更難推理。目前，`step.do()` 在被呼叫時就會啟動步驟，所以開發人員可以啟動一個步驟、做其他工作，稍後再等待第一個步驟完成：
    
    
    const first = step.do("first", () => serviceA.call());
    
    await step.do("second", () => serviceB.call());
    
    await first;

在目前的執行模型中，`first` 會在 `second` 之前立即啟動。流暢式 API 會使情況變得複雜。Workflows 需要等待並觀察是否附加了 `.rollback()`，才能知道完整的步驟定義。這可能會延遲步驟被傳送到引擎的時間。

在前面的例子中，`first` 可能會在 `await first` 時（即 `second` 步驟完成後）才啟動，而非在 `step.do("first", ...)` 處啟動。

這使得並行 Workflow 更難以預測：步驟的時序將取決於回傳的 `Promise` 何時被使用，而不僅僅是 `step.do()` 在哪裡被呼叫。

我們也考慮過建造者風格的 API：
    
    
    const charge = await step
    	.saga("charge")
    	.do(() => chargeCard())
    	.rollback(() => refundCharge())
    	.run();

建造者 API 避免了 `Promise` 的模糊性。它也為未來的步驟層級選項提供了一個明確的位置，並清楚表明正向動作和復原動作屬於同一個 saga 步驟。

但它的儀式感太重了。每個步驟都需要一個最終的 `.run()`，但很容易忘記寫 `.run()`，且若無工具輔助難以察覺；簡單的單一步驟案例也會變得像冗長的設定鏈。它也引入了一個新的 `step.saga() `建造者，偏離了現有的 `step.<action>` 模式。最重要的是，它讓 `step.do()` 感覺像是一個較舊的 API，而不是 Workflows 的主要基本元件。復原功能的目標是擴展 `step.do()`，而不是取代它。

### 將復原作為步驟的中繼資料
    
    
    step.do(..., { rollback })

最終，我們選擇了明確的形式，將復原作為步驟的中繼資料。

這樣一來，每個復原都在正向步驟本身內部定義。每個處理器都會收到觸發復原的錯誤、[ _步驟上下文_](https://developers.cloudflare.com/workflows/build/step-context/)，以及輸出。輸出可能是正向步驟回傳的持久化值（這可能是 undefined）；若步驟在持久化數值之前就失敗，則直接為 undefined。

復原會發出生命週期事件，因此您可以知道補償是否已開始、哪個復原處理器失敗，以及復原是否成功完成。

至關重要的是，原始的 Workflow 失敗保持獨立：復原是 Workflow 在失敗之後所做的事情，而不是 Workflow 失敗的原因。

就像您可以透過 `WorkflowStepConfig` 在[ _步驟組態_](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstepconfig)中定義自訂的重試和逾時行為一樣，您也可以在 `rollbackConfig` 中加入復原專屬的值。
    
    
    {
      rollback: async ({ output }) => {
        await bankA.credit({ accountId: fromAccountId, amount, transferId: `${transferId}-reversal` });
      },
      rollbackConfig: {
        retries: { limit: 10, delay: '30 seconds', backoff: 'exponential' },
        timeout: '2 minutes',
      },
    }

這符合我們想要的生命週期事件心智模型。`step.do()` 本來就是在描述一個持久化的工作單元，Workflows 會記錄、重試該單元，並稍後在記錄中顯示。復原是針對同一個工作單元的另一個生命週期行為。它應該伴隨著步驟定義，而不是存在於單獨的包裝器 (wrapper) 或建造者中。

  * 步驟仍然在 `step.do()` 正常啟動的時候啟動。
  * 返回的 promise 仍然代表步驟的輸出。
  * 並行的 Workflow 程式碼保持相同的執行模型。
  * 復原的重試和逾時選項與復原處理器放在一起。
  * 現有的 `step.do()` 呼叫保持完全相同的運作方式。



這種形式比流暢式 API 稍微更明確一些，但這種明確性是有用的。操作及其補償仍然放在同一個地方，而且 API 沒有引入新的步驟建造者或新的 promise 類型。已經瞭解 `step.do()` 的開發人員只需要學習一個額外的 `options` 物件即可。

這雖然不那麼神奇，但更容易採用，也更容易理解。

## 底層運作原理

復原功能感覺像是一個小小的 API 新增項目，但它改變了 Workflows 需要針對每個步驟記錄的內容。

一般的 `step.do()` 已經有一個持久化的記錄。Workflows 會記錄步驟是否已啟動、是否已完成、回傳了什麼，以及如果 Workflow 稍後恢復執行，該步驟應該被跳過還是重新執行。

復原功能為該記錄增加了一件事：該步驟是否註冊了補償邏輯。

這意味著，如果 Workflow 失敗，Workflows 需要將兩項資訊結合起來。

第一項是**持久化的步驟歷程記錄** 。Workflow 引擎會儲存資料，以瞭解哪些已執行、哪些已完成、儲存了什麼輸出，以及是否已註冊復原。

第二項是**復原處理器** 本身，也就是為補償該步驟而編寫的函式。Workflows 不會將該函式的文字當作資料儲存。相反地，它會在 Workflow 執行期間，保留一個可呼叫的處理器參照。

在 Workers RPC 中，這種可呼叫的參照稱為 [**_stub_**](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle)。Stub 讓系統的一部分可以呼叫正在其他地方執行的程式碼。Stub 也具有生命週期，因此可以在呼叫或執行上下文結束時被處置 (dispose)。如果您需要在該時間點之後保留 stub，Workers RPC 提供了一個 [`_dup()_`](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle/#the-dup-method) 方法，可以建立另一個指向相同目標的控制代碼。

對於復原功能來說，這個模型很有用。持久化的步驟歷程記錄記錄了哪些需要補償。復原 stub 為 Workflows 提供了一種呼叫補償程式碼的方式。而且，由於復原處理器可能需要比註冊它們的 `step.do()` 呼叫存活更久，Workflows 會為復原階段保留自己的可呼叫處理器參照。

在常見的情況下，當 Workflow 在同一個引擎生命週期中進入復原階段時，Workflows 已經擁有它需要的復原 stub。它可以使用持久化的步驟歷程記錄來找出符合資格的步驟，然後呼叫在正向執行期間註冊的復原 stub。

當 Workflows 需要在重啟後進行**復原** 時，情況就變得比較微妙。

如果在需要執行復原時，引擎被驅逐、當機或重新啟動，Workflows 仍然擁有持久化的步驟歷程記錄，但可能不再擁有記憶體中的復原 stub。為了復原，Workflows 會使用**重播 (replay)** ：這是一種復原模式，它可以重新執行 Workflow 程式碼，但不會重新執行已完成之正向步驟的主體。

當重播遇到一個已完成的 `step.do()` 時，Workflows 會讀取持久化的結果，而不是再次執行步驟主體。對於 rollback 復原，Workflows 只需要為那些有附加復原且符合復原資格的步驟重建處理器。當遇到這些 `step.do()` 呼叫時，它們的復原選項可以再次註冊可呼叫的 stub。

這讓 Workflows 能夠復原它需要的復原處理器，而不會重複原始的外部副作用。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMK8HE1XEHVNX1B4RNK9W.png&w=715&h=699&f=webp&fit=cover&position=center)

有了這些元件，無論處理器是否仍在記憶體中可用，或者必須在復原期間重建，復原功能都能運作。

當 Workflow 即將失敗時，Workflows 不會要求您的應用程式重建發生的事情。它已經有步驟歷程記錄。它可以查看持久化的記錄，並回答重要的問題：

  * 哪些步驟已經開始？
  * 哪些步驟已完成？
  * 哪個失敗的步驟可能仍需要清理？
  * 哪個步驟註冊了復原處理器？
  * 每個復原處理器應該接收什麼輸出？
  * 補償應以什麼順序執行？



然後，Workflows 會使用復原上下文（包含原始錯誤、步驟上下文和步驟輸出（如果有被持久化））來呼叫每個復原 stub。

執行順序的細節很重要。在一般的 JavaScript 中，特別是在使用 `Promise.all()` 時，完成順序不一定與開始順序相同。如果步驟 A 先啟動，步驟 B 後啟動，步驟 B 可能會先完成。對於復原，Workflows 使用持久化的開始順序作為穩定的真實來源，然後以相反的順序展開。

復原處理器也會透過 Workflows 的正常步驟機制執行。這表示補償會獲得您對 Workflows 所預期的相同操作特性：重試、逾時、生命週期事件、記錄，以及最終的記錄結果。如果一個復原處理器在其設定的重試次數後仍持續失敗，Workflows 會將復原結果記錄為失敗，停止執行其餘的復原處理器，而 Workflow 執行個體最終會以 `Errored` 狀態結束。

這是 Saga 復原與 `catch` 區塊之間的主要差異。`catch` 區塊只知道在 JavaScript 執行到該確切時間點時，仍在記憶體中的內容。Workflows 復原則使用持久化的步驟歷程記錄來決定已經發生的事情，在常見情況下呼叫它已有的 stub，並在需要時於復原期間安全地重建遺失的 stub。

這也是為什麼該 API 將復原放在 `step.do()` 本身的原因。復原不是一個獨立的全域錯誤處理器——它是附加在 Workflows 已經理解的持久化工作單元上的中繼資料。

## 下一步驟

我們復原功能的第一個迭代版本包含：

  * 針對 `step.do()` 的明確步驟復原處理器
  * 循序復原執行
  * 補償的重試和逾時設定



接下來，我們想要探索：

  * 對 [`_waitForEvent_`](https://developers.cloudflare.com/workflows/build/events-and-parameters/#wait-for-events) 的復原支援
  * 對並行復原執行的支援
  * 對 [_Python Workflows_](https://developers.cloudflare.com/workflows/python/) 的復原支援



當一個多步驟應用程式在執行中途失敗時，最困難的部分往往不是「 _知道_ 它失敗了」，而是「知道已經發生了 _什麼_ ，以及接下來需要發生什麼」。

Saga 復原讓您可以將答案直接放在每個步驟旁邊。如果您正在使用 Workflows 建置多步驟應用程式，請試試 Saga 復原，並告訴我們您接下來還想要什麼補償模式。請參閱 [_Workflows 技術文件_](https://developers.cloudflare.com/workflows/)開始上手，並在 [_Cloudflare 社群_](https://community.cloudflare.com/)中與我們分享您的寶貴回饋。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frollbacks-for-workflows%2F&t=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E7%82%BA%20Cloudflare%20Workflows%20%E6%89%93%E9%80%A0%20Saga%20%E5%BE%A9%E5%8E%9F%E5%8A%9F%E8%83%BD)[](https://x.com/intent/post?text=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E7%82%BA+Cloudflare+Workflows+%E6%89%93%E9%80%A0+Saga+%E5%BE%A9%E5%8E%9F%E5%8A%9F%E8%83%BD&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frollbacks-for-workflows%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frollbacks-for-workflows%2F)[](https://bsky.app/intent/compose?text=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E7%82%BA+Cloudflare+Workflows+%E6%89%93%E9%80%A0+Saga+%E5%BE%A9%E5%8E%9F%E5%8A%9F%E8%83%BD+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frollbacks-for-workflows%2F)[](https://mastodonshare.com/?text=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E7%82%BA+Cloudflare+Workflows+%E6%89%93%E9%80%A0+Saga+%E5%BE%A9%E5%8E%9F%E5%8A%9F%E8%83%BD&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frollbacks-for-workflows%2F)[](https://www.threads.net/intent/post?text=%E6%88%91%E5%80%91%E5%A6%82%E4%BD%95%E7%82%BA+Cloudflare+Workflows+%E6%89%93%E9%80%A0+Saga+%E5%BE%A9%E5%8E%9F%E5%8A%9F%E8%83%BD+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Frollbacks-for-workflows%2F)

## 相關標籤

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Workflows](https://blog.cloudflare.com/zh-tw/tag/workflows/)[開發人員](https://blog.cloudflare.com/zh-tw/tag/developers/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
