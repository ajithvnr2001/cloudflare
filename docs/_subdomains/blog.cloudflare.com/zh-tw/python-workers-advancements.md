---
url: https://blog.cloudflare.com/zh-tw/python-workers-advancements/
title: Python Workers Redux\uff1a\u5feb\u901f\u51b7\u555f\u52d5\u3001\u5957\u4ef6\u4ee5\u53ca uv \u512a\u5148\u5de5\u4f5c\u6d41\u7a0b | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:47.397590+00:00
---

# Python Workers Redux：快速冷啟動、套件以及 uv 優先工作流程 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/python-workers-advancements/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Python](https://blog.cloudflare.com/zh-tw/tag/python/)

2 標籤顯示 2 個標籤

  * 文章標籤
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Python](https://blog.cloudflare.com/zh-tw/tag/python/)
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



[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Python](https://blog.cloudflare.com/zh-tw/tag/python/)

2025年12月8日

# Python Workers Redux：快速冷啟動、套件以及 uv 優先工作流程

![Dominik Picheta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P5G8RRA9GKFZA6BYERZ1.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Mike Nomitch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462B7XNRB3FQ030XK95Y0H.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dominik Picheta](https://blog.cloudflare.com/zh-tw/author/dominik/)、[Hood Chatham](https://blog.cloudflare.com/zh-tw/author/hood/)和[Mike Nomitch](https://blog.cloudflare.com/zh-tw/author/mike-nomitch/)

閱讀時間：10 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/python-workers-advancements/)、[日本語](https://blog.cloudflare.com/ja-jp/python-workers-advancements/)、[한국어](https://blog.cloudflare.com/ko-kr/python-workers-advancements/)和[简体中文](https://blog.cloudflare.com/zh-cn/python-workers-advancements/).

![BLOG-2925 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SJ3N46YQKDZYJ6Q7M0S4.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////97e/z3eLu2+Lx4+n26+3y7uvp////////6u3119/w1eD04Oj56e317evs////////6O3509710eD53un96e/67e3w////////6/D+1eL61OT+4e7/7fP/8fH1////////8/j/3+v/3u3/6/b/9fn/9/b7/////////f//7fb/7fj/9/7//v////3/////////////+P//+P///////////////////////////P///P//////////////)

_注意：本篇貼文已更新，新增了關於 AWS Lambda 的更多詳細資訊。_

去年，我們宣布了對 [_Python Workers 的基本支援_](https://blog.cloudflare.com/python-workers/)，這讓 Python 開發人員能夠透過單一命令在全球範圍運用 Python，發揮 [_Workers 平台_](https://workers.cloudflare.com/)的優勢。

時至今日，我們一直努力讓 [_Workers 上的 Python 體驗_](https://developers.cloudflare.com/workers/languages/python/)感覺很棒。我們一直致力於將套件支援引入平台，現在這一目標已經實現 — 具有極快的冷啟動速度和 Python 原生開發人員體驗。

這意味著套件整合至 Python Worker 的方式發生了變化。現在，我們並非僅提供有限的內建套件，而是能夠針對 [_Pyodide（讓 Python Workers 運作的 WebAssembly 執行階段）支援的任何套件_](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)來提供支援。這包括所有純 Python 套件，以及許多依賴於動態連結庫的許多套件。我們還圍繞 [_uv_](https://docs.astral.sh/uv/) 建置了工具，以便簡化套件安裝。

此外，我們還實作了專用記憶體快照功能，以縮短冷啟動時間。相較於其他無伺服器 Python 供應商，這些快照可大幅提升速度。在使用常見套件的冷啟動測試中，Cloudflare Workers 的啟動速度比**未採用 SnapStart** 的 **AWS Lambda 快 2.4 倍** ，比 **Google Cloud Run 快 3 倍** 。

在這篇部落格文章中，我們將說明 Python Workers 的獨特之處，並分享我們如何實現上述目標的一些技術詳細資料。首先，對於那些可能不熟悉 Workers 或無伺服器平台的人，特別是具有 Python 背景的人，我們將分享您為什麼可能需要使用 Workers。

### 2 分鐘內即可在全球部署 Python

Workers 之所以有魔力，部分原因在於其簡潔的程式碼和便利的全球部署。我們先來看看如何透過快速冷啟動，在不到兩分鐘的時間內，將 FastAPI 應用程式部署到全球各地。

只需幾行程式碼，即可使用 FastAPI 實作一個簡單的 Worker。
    
    
    from fastapi import FastAPI
    from workers import WorkerEntrypoint
    import asgi
    
    app = FastAPI()
    
    @app.get("/")
    async def root():
       return {"message": "This is FastAPI on Workers"}
    
    class Default(WorkerEntrypoint):
       async def fetch(self, request):
           return await asgi.fetch(app, request.js_object, self.env)

若要部署類似的項目，只需確保您已安裝 `uv` 和 `npm`，然後執行以下命令。
    
    
    $ uv tool install workers-py
    $ pywrangler init --template \
        https://github.com/cloudflare/python-workers-examples/03-fastapi
    $ pywrangler deploy

只需少量程式碼和 `pywrangler deploy`，您現在能夠在 Cloudflare 遍及 [_125 個國家/地區 330 個地點_](https://www.cloudflare.com/network/)的邊緣網路部署應用程式。無需擔心基礎架構或擴展問題。

在許多使用案例中，Python Workers 完全免費。我們的免費方案提供每天 100,000 個請求，每次調用 10 毫秒 CPU 時間。如需詳細資訊，請參閱[ _說明文件中的定價頁面_](https://developers.cloudflare.com/workers/platform/pricing/)。

如需更多範例，請參閱 [_GitHub 中的存放庫_](https://github.com/cloudflare/python-workers-examples)。繼續閱讀以深入瞭解 Python Workers。

### 您可以使用 Python Workers 做些什麼呢？

現在已經有了 Worker，幾乎一切都變得可能。程式碼由您撰寫，所以決定權在您。您的 Python Worker 接收 HTTP 請求，並且可以向公共網際網路上的任何伺服器傳送請求。

您可以設定 Cron 觸發程序，讓您的 Worker 定期執行。此外，如果您有更複雜的要求，您可以使用 [_Workflows for Python Workers_](https://blog.cloudflare.com/python-workflows/)，甚至是 [_使用 Durable Objects_](https://developers.cloudflare.com/durable-objects/get-started/) 的長期執行 WebSocket 伺服器和用戶端。

以下是更多您可以使用 Python Workers 執行的各種操作範例：

  * [ _藉助 Jinja 這類程式庫，在邊緣轉譯 HTML 範本，同時直接從您的伺服器擷取動態內容_](https://github.com/cloudflare/python-workers-examples/tree/main/03-fastapi)
  * [ _修改您的伺服器做出的回應 — 您可以根據請求的內容，將 opengraph 標籤動態地插入到您的 HTML 之中。_](https://github.com/cloudflare/python-workers-examples/tree/main/11-opengraph)
  * [ _使用 Durable Objects 和 WebSocket 建置聊天室_](https://github.com/cloudflare/python-workers-examples/tree/main/15-chatroom)
  * [ _透過 WebSocket 連線取用資料，例如 Bluesky firehose_](https://github.com/cloudflare/python-workers-examples/tree/main/14-websocket-stream-consumer)
  * [ _使用 Pillow Python 套件生成映像_](https://github.com/cloudflare/python-workers-examples/tree/main/12-image-gen)
  * [ _編寫一個小型 Python Worker，以公開 Python 套件的 API，然後使用 RPC 透過您的 JavaScript Worker 存取_](https://github.com/cloudflare/python-workers-examples/tree/main/13-js-api-pygments)



### 加速套件冷啟動

無伺服器平台（如 Workers）僅在必要時執行程式碼，從而為您節省資金。這意味著，如果您的 Worker 沒有收到請求，可能會被關閉，並需要在收到新請求時重新啟動。通常，這會產生我們稱為「冷啟動」的資源開銷。務必盡可能縮短這些時間，以盡量減少終端使用者的延遲。

在標準 Python 中，啟動執行階段的成本很高，因此 Python Workers 的初始實作著重於加快 _執行階段_ 的啟動速度。然而，我們很快就意識到這還不夠。即使 Python 執行階段啟動迅速，在實際情況中，初始啟動通常也包括從套件載入模組。並且遺憾的是，在 Python 中，許多常用的套件可能需要數秒才能載入。

我們的目標是無論是否載入套件，都能讓冷啟動快速執行。

為了測量實際的冷啟動效能，我們建立了一項用於匯入常見套件的基準，以及使用裸 Python 執行階段來執行「hello world」的基準。標準 Lambda 能夠快速[ _僅啟動執行階段_](https://cold.picheta.me/#bare)，但一旦您需要匯入套件，冷啟動時間就會迅速增加。為了實現最佳化，以便在匯入套件的情況下加速冷啟動，您可在 Lambda 上使用 SnapStart（我們稍後會將其新增至連結的基準測試中）。這會產生儲存快照的費用，並且每次還原都會產生額外費用。Python Workers 會自動針對每個 Python Worker，免費套用記憶體快照。

以下是載入三個常用套件 ([_httpx_](https://www.python-httpx.org/)、[ _fastapi_](https://fastapi.tiangolo.com/) 和 [_pydantic_](https://docs.pydantic.dev/latest/)) 時的平均冷啟動時間：

平台| 平均冷啟動（秒）  
---|---  
Cloudflare Python Workers| 1.027  
AWS Lambda（不使用 SnapStart）| 2.502  
Google Cloud Run| 3.069  
  
在此案例中，**Cloudflare Python Workers 的冷啟動速度比不使用 SnapStart 的 AWS Lambda 快 2.4 倍，也比 Google Cloud Run 快 3 倍** 。我們藉由使用記憶體快照，實現了這些較低的冷啟動數字。我們將在後面的章節中說明我們是如何做到的。

我們會定期執行這些基準。前往[ _此處_](https://cold.picheta.me/#bare)，瞭解有關我們測試方法的最新資料和更多資訊。

我們在架構上與這些其他平台不同，即 [_Workers 以隔離為基礎_](https://developers.cloudflare.com/workers/reference/how-workers-works/)。正因如此，我們的目標遠大，並且正為實現零冷啟動的未來而努力。

### 與 uv 整合的套件工具

Python 之所以如此出色，主要原因是採用多樣化的套件生態系統。因此，我們一直在努力確保在 Workers 中盡可能簡單地使用套件。

我們瞭解到，使用現有的 Python 工具是實現卓越開發體驗的最佳途徑。因此，我們選擇了 `uv` 套件和專案管理器，因其速度快、成熟，並且在 Python 生態系統中發展勢頭良好。

我們圍繞 `uv` 建置自己的工具，稱為 [_pywrangler_](https://github.com/cloudflare/workers-py#pywrangler)。此工具主要執行以下操作：

  * 讀取您的 Worker 的 pyproject.toml 檔案，以確定其中指定的相依項。
  * 在 Worker 的 `python_modules` 資料夾中新增您的相依項



Pywrangler 呼叫 `uv`，以與 Python Workers 相容的方式來安裝相依項，並在本地開發或部署 Workers 時呼叫 `wrangler`。

實際上，這意味著您只需執行 `pywrangler dev` 和 `pywrangler` `deploy`，即可在本地測試您的 Worker 並進行部署。 

### 類型提示

您可以使用 `pywrangler types`，針對在您的 Wrangler 中定義的[ _繫結項_](https://developers.cloudflare.com/workers/runtime-apis/bindings/)來生成類型提示。這些類型提示將適用於 [_Pylance_](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 或最新版本的 [_mypy_](https://mypy-lang.org/)。

如需生成類型，使用 [_wrangler types_](https://developers.cloudflare.com/workers/wrangler/commands/#types) 來建立 typescript 類型提示，然後使用 typescript 編譯器，針對這些類型生成抽象語法樹。最後，我們使用 TypeScript 提示（例如 JS 物件是否具有迭代器欄位），來生成與 Pyodide 外部函數介面搭配使用的 `mypy` 類型提示。

### 使用快照來縮短冷啟動時間

Python 啟動通常很慢，並且匯入 Python 模組可能會觸發大量工作。因此，使用記憶體快照，避免在冷啟動期間執行 Python 啟動。

部署 Worker 時，我們會執行 Worker 的頂層作用域，接著擷取記憶體快照，並將其與您的 Worker 一起儲存。每當我們為 Worker 啟動新的隔離程序時，我們會還原記憶體快照，並且 Worker 可隨時處理請求，而無需在準備階段執行任何 Python 程式碼。這能大幅縮短冷啟動時間。例如，在沒有快照的情況下，啟動一個匯入 `fastapi`、`httpx` 和 `pydantic` 的 Worker 大約需要 10 秒鐘。使用快照時，則只需 1 秒鐘。

由於 Pyodide 在 WebAssembly 基礎上建置，讓這一點得以實現。我們可輕鬆擷取執行階段的完整線性記憶體並加以還原。 

#### 記憶體快照與熵

WebAssembly 執行階段並不需要位址空間配置隨機化之類的功能來確保安全性，因此在現代作業系統上，記憶體快照的大部分困難都不會發生。就像原生記憶體快照一樣，我們仍然必須在啟動時仔細處理熵，以避免使用 [_XKCD 隨機數生成器_](https://xkcd.com/221/)（我們[ _非常注重實際隨機性_](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)）。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2925 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW459DS22T0KYDPDJGGEAW3H.png&w=400&h=144&f=webp&fit=cover&position=center)

藉由拍攝記憶體快照，我們可能會不小心鎖定隨機性的種子值。在這種情況下，未來對「隨機」數字的呼叫會在多個請求中持續傳回相同的值序列。

避免這種情況特別困難，因為 Python 在啟動時會使用大量的熵。這些包括 libc 函數 `getentropy()` 和 `getrandom()`，以及從 `/dev/random` 和 `/dev/urandom` 讀取。所有這些函數與 JavaScript `crypto.getRandomValues()` 函數的實作相同。

在 Cloudflare Workers 中，`crypto.getRandomValues()`啟動時一直停用，以便將來能夠轉換為使用記憶體快照。遺憾的是，Python 解譯器若不呼叫此函數就無法啟動。而且許多套件在啟動時也需要熵。這種熵主要有兩個用途：

  * 用於雜湊隨機化的雜湊種子
  * 用於偽隨機數字生成器的種子



我們在啟動時執行雜湊隨機化操作，並接受每個特定 Worker 具有固定雜湊種子的成本。Python 沒有在啟動之後允許取代雜湊種子的機制。

對於虛擬亂數生成器 (PRNG)，我們採取以下方法：

部署時：

  1. 使用固定的「毒種」為 PRNG 植入種子，然後記錄 PRNG 狀態。
  2. 將所有呼叫 PRNG 的 API 取代為一個覆蓋層，該覆蓋層會因使用者錯誤而導致部署失敗。
  3. 執行使用者程式碼的頂層範圍。
  4. 擷取快照。



執行時：

  1. 確認 PRNG 狀態未變更。若發生變更，表示我們忘記了某些方法的覆疊。部署失敗，且發生內部錯誤。
  2. 還原快照之後，為隨機數生成器重新植入種子，然後再執行任何處理程式。



這樣，我們可確保在 Workers 執行時可以使用 PRNG，但會阻止 Worker 在初始化和預快照期間使用它們。

#### 記憶體快照與 WebAssembly 狀態

在 WebAssembly 上建立記憶體快照時，會出現其他難題：我們要儲存的記憶體快照僅包含 WebAssembly 線性記憶體，但 Pyodide WebAssembly 執行個體的完整狀態並未包含在線性記憶體中。

在這個記憶體之外有兩個資料表。

一個資料表儲存函數指標的值。傳統電腦使用「馮·諾伊曼」架構，這意味著程式碼與資料存在於相同的記憶體空間中，因此，呼叫函數指標就是跳轉到某個記憶體位址。WebAssembly 具有「哈佛架構」，其中程式碼位於獨立的位址空間中。這是實現 WebAssembly 大部分安全性保證的關鍵，尤其說明了 WebAssembly 為何不需要位址空間配置隨機化。在 WebAssembly 中，函數指標是指向函數指標表的索引。

第二個資料表包含所有從 Python 參照的 JavaScript 物件。JavaScript 物件不能直接儲存到記憶體中，因為 JavaScript 虛擬機禁止直接取得指向 JavaScript 物件的指標。取而代之的是，這些物件會儲存到一個資料表中，並在 WebAssembly 中表示為資料表的索引。

我們需要確保這兩個資料表在還原快照之後，處於與我們擷取快照時完全相同的狀態。

函數指標資料表在 WebAssembly 執行個體初始化時始終處於相同的狀態。我們載入動態函式庫（例如 numpy 這類的原生 Python 套件）時，動態載入程式會更新此資料表。

若要處理動態載入：

  1. 拍攝快照時，我們會套用修補程式至載入器，以記錄動態函式庫的載入順序、記憶體中每個函式庫的中繼資料位址，以及重新配置的函式指標表基底位址。 
  2. 還原快照時，我們會以相同的順序重新載入動態程式庫，並使用修補過的記憶體配置器，將中繼資料放置在相同的位置。我們確認，函數指標表的目前大小與我們為動態程式庫記錄的函數指標表基底相符。



所有這些都確保在還原快照之後，每個函式指標都具有與拍攝快照時相同的含義。

為了處理 JavaScript 參考，我們實作了一個相當有限的系統。如果 JavaScript 物件可透過一系列屬性存取項從 globalThis 存取，則我們會記錄這些屬性存取項，並在還原快照時重播這些屬性存取項。如果存在任何無法透過此方式存取的 JavaScript 物件參考，則我們將無法部署 Worker。這足以處理所有具有 Pyodide 支援的現有 Python 套件，這些套件會執行頂層匯入，例如：
    
    
    from js import fetch

### 使用分片來降低冷啟動的頻率

Python Workers 效能策略的另一項重要特徵是分片。[ _此處_](https://blog.cloudflare.com/eliminating-cold-starts-2-shard-and-conquer/)有非常詳細的實作說明。簡而言之，我們現在會將請求路由到現有的 Worker 執行個體，而在此之前，我們可能會選擇啟動新的執行個體。

實際上首先會為 Python Workers 啟用分片，並證明其是很好的測試平台。相較於 JavaScript，Python 的冷啟動成本遠高於 JavaScript，因此確保將請求路由到已在執行的隔離環境至關重要。

### 接下來我們該怎麼辦？

這才剛剛開始。我們有很多計畫來改善 Python Workers：

  * 更便於開發人員使用的工具
  * 利用我們的隔離架構，實現更快的冷啟動速度
  * 支援更多套件
  * 支援原生 TCP 通訊端、原生 WebSocket 及更多繫結項



若要瞭解有關 Python Workers 的詳細資訊，請參閱[ _此處_](https://developers.cloudflare.com/workers/languages/python/)提供的文件。如需獲得協助，請務必加入我們的 [_Discord_](https://discord.cloudflare.com/)。

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpython-workers-advancements%2F&t=Python%20Workers%20Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%95%9F%E5%8B%95%E3%80%81%E5%A5%97%E4%BB%B6%E4%BB%A5%E5%8F%8A%20uv%20%E5%84%AA%E5%85%88%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B)[](https://x.com/intent/post?text=Python+Workers+Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%95%9F%E5%8B%95%E3%80%81%E5%A5%97%E4%BB%B6%E4%BB%A5%E5%8F%8A+uv+%E5%84%AA%E5%85%88%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpython-workers-advancements%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpython-workers-advancements%2F)[](https://bsky.app/intent/compose?text=Python+Workers+Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%95%9F%E5%8B%95%E3%80%81%E5%A5%97%E4%BB%B6%E4%BB%A5%E5%8F%8A+uv+%E5%84%AA%E5%85%88%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpython-workers-advancements%2F)[](https://mastodonshare.com/?text=Python+Workers+Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%95%9F%E5%8B%95%E3%80%81%E5%A5%97%E4%BB%B6%E4%BB%A5%E5%8F%8A+uv+%E5%84%AA%E5%85%88%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpython-workers-advancements%2F)[](https://www.threads.net/intent/post?text=Python+Workers+Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%95%9F%E5%8B%95%E3%80%81%E5%A5%97%E4%BB%B6%E4%BB%A5%E5%8F%8A+uv+%E5%84%AA%E5%85%88%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fpython-workers-advancements%2F)

## 相關標籤

[Cloudflare Workers](https://blog.cloudflare.com/zh-tw/tag/workers/)[Python](https://blog.cloudflare.com/zh-tw/tag/python/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
