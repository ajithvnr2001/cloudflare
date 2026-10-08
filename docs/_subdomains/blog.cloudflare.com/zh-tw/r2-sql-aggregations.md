---
url: https://blog.cloudflare.com/zh-tw/r2-sql-aggregations/
title: \u5ba3\u4f48 R2 SQL \u958b\u59cb\u652f\u63f4 GROUP BY\u3001SUM \u548c\u5176\u4ed6\u5f59\u7e3d\u67e5\u8a62 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:46.069023+00:00
---

# 宣佈 R2 SQL 開始支援 GROUP BY、SUM 和其他彙總查詢 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/r2-sql-aggregations/

[部落格](https://blog.cloudflare.com/zh-tw/)

[R2](https://blog.cloudflare.com/zh-tw/tag/r2/)[Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)[SQL](https://blog.cloudflare.com/zh-tw/tag/sql/)+3顯示另外 3 個標籤

6 標籤顯示 6 個標籤

  * 文章標籤
  * [R2](https://blog.cloudflare.com/zh-tw/tag/r2/)[Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)[SQL](https://blog.cloudflare.com/zh-tw/tag/sql/)[無伺服器](https://blog.cloudflare.com/zh-tw/tag/serverless/)[資料](https://blog.cloudflare.com/zh-tw/tag/data/)[邊緣運算](https://blog.cloudflare.com/zh-tw/tag/edge-computing/)
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



[無伺服器](https://blog.cloudflare.com/zh-tw/tag/serverless/)[資料](https://blog.cloudflare.com/zh-tw/tag/data/)[邊緣運算](https://blog.cloudflare.com/zh-tw/tag/edge-computing/)

[R2](https://blog.cloudflare.com/zh-tw/tag/r2/)[Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)[SQL](https://blog.cloudflare.com/zh-tw/tag/sql/)[無伺服器](https://blog.cloudflare.com/zh-tw/tag/serverless/)[資料](https://blog.cloudflare.com/zh-tw/tag/data/)[邊緣運算](https://blog.cloudflare.com/zh-tw/tag/edge-computing/)

2025年12月18日

# 宣佈 R2 SQL 開始支援 GROUP BY、SUM 和其他彙總查詢

![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Marc Selwan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455H274J0ZYJ6K4KHKJT25.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jérôme Schneider](https://blog.cloudflare.com/zh-tw/author/jerome/)、[Nikita Lapkov](https://blog.cloudflare.com/zh-tw/author/nikita-lapkov/)和[Marc Selwan](https://blog.cloudflare.com/zh-tw/author/marc-selwan/)

閱讀時間：9 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/r2-sql-aggregations/)、[日本語](https://blog.cloudflare.com/ja-jp/r2-sql-aggregations/)、[한국어](https://blog.cloudflare.com/ko-kr/r2-sql-aggregations/)和[简体中文](https://blog.cloudflare.com/zh-cn/r2-sql-aggregations/).

![BLOG-3082 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45417DV5EYZK6BB5T2Z60B.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f395OPwzs7ry9Dx2N745uj17urq////////5+bz0dLuztT02uH66Ov37+zs////////6+z31tny0tr43uf+6/D78vHw////////8PL83OH32OL94+7/8Pb/9/b1////////9vn/4un83+r/6fX/9fz/+/z6////////+///6PD/5fL/7/z/+f/////+/////////v//7PX/6ff/8////f//////////////////7ff/6/n/9P///v//////)

在處理大量資料時，快速獲取概觀是非常有幫助的——這正是 SQL 中的彙總所提供的功能。彙總，也被稱為「GROUP BY 查詢」，能提供鳥瞰式的視角，讓您能迅速從海量資料中獲得見解。

正因如此，我們非常激動地宣佈：[ _R2 SQL_](https://blog.cloudflare.com/r2-sql-deep-dive/) 現已支援彙總功能。R2 SQL 是 Cloudflare 推出的無伺服器、分散式分析查詢引擎，能夠對儲存在 [_R2 Data Catalog_](https://developers.cloudflare.com/r2/data-catalog/) 中的資料進行 SQL 查詢。彙總功能將協助 [_R2 SQL_](https://developers.cloudflare.com/r2-sql/) 使用者發現資料中的重要趨勢與變化、產生報告，並在記錄中找出異常。

此次發佈基於已支援的篩選查詢功能，後者是分析工作負載的基礎，允許使用者在 [_Apache Parquet_](https://parquet.apache.org/) 檔案的大量資料中找到所需的資訊。

在本文中，我們將詳細介紹彙總功能的用途和特點，然後深入探討我們如何擴展 R2 SQL 以支援在儲存在 R2 Data Catalog 中的海量資料上執行此類查詢。

## 彙總於分析的重要性

彙總也稱為「GROUP BY 查詢」，可以產生底層資料的簡要匯總。

一個常見的彙總用例是產生報告。假設有一個名為「sales」的表格，其中包含某組織在各個國家/地區和部門的歷史銷售資料。我們可以使用如下彙總查詢輕鬆產生按部門統計的銷售報告：
    
    
    SELECT department, sum(value)
    FROM sales
    GROUP BY department

  
我們可以使用「GROUP BY」陳述式，將表中的列劃分為多個儲存桶。每個儲存桶都有一個標籤，對應一個特定部門。當所有列被劃分進各自的儲存桶後，我們就可以對每個儲存桶中的所有列計算「sum(value)」，從而得到該部門的總銷售量。

對於某些報告，我們可能只關心銷售量最高的部門。這時，「ORDER BY」陳述式就派上用場了：
    
    
    SELECT department, sum(value)
    FROM sales
    GROUP BY department
    ORDER BY sum(value) DESC
    LIMIT 10

這裡我們指示查詢引擎按照各部門的總銷售量降序排列，並僅返回前 10 個銷售量最高的部門。

最後，我們有時可能希望濾除異常資料。例如，我們只想在報告中包含總銷售量大於 5 的部門。我們可以輕鬆地透過「HAVING」陳述式實現這一點：
    
    
    SELECT department, sum(value), count(*)
    FROM sales
    GROUP BY department
    HAVING count(*) > 5
    ORDER BY sum(value) DESC
    LIMIT 10

我們在查詢中添加了一個新的彙總函式「count(*)」，它用於計算每個儲存桶中有多少列。這直接對應於該部門的銷售次數，因此我們也在「HAVING」陳述式中新增了一個條件，確保只保留那些列數大於 5 的儲存桶。

## 兩種彙總方式：早計算還是晚計算

彙總查詢有一個有趣的特性：它們可以參照並不實際存在於原始資料中的欄。以「sum(value)」為例：這個欄是由查詢引擎在執行時動態計算出來的，而像「department」這樣的欄則是直接從儲存在 R2 上的 Parquet 檔案中讀取的。這個細微差別意味著，任何參照了如「sum」、「count」等彙總函式的查詢，都需要分成兩個階段來處理。

第一階段是計算新欄。如果我們要使用「ORDER BY」陳述式按「count(*)」欄對資料進行排序，或使用「HAVING」陳述式基於該欄篩選列，我們需要知道該欄的值。一旦知道「count(*)」等欄的值，我們就可以繼續執行查詢的其餘部分。

請注意，如果查詢在「HAVING」或「ORDER BY」子句中沒有參照彙總函式，但仍在「SELECT」子句中使用它們，我們可以使用一種技巧。由於我們直到最後才需要彙總函式的值，因此我們可以部分計算它們，並在準備向使用者傳回結果之前再合併結果。

這兩種方法之間的關鍵區別在於我們何時計算彙總函式：是提前算好，以便後續做更多處理；還是按需即時計算，邊處理邊建立最終結果。

首先，我們來探討「即時建立結果」的方式——我們稱之為「分散-聚集彙總」(scatter-gather aggregations)。接著在此基礎上，我們會介紹「洗牌式彙總」(shuffling aggregations)，它支持在彙總函式之上執行額外的操作，例如「HAVING」和「ORDER BY」。

## 分散-聚集彙總

沒有使用「HAVING」和「ORDER BY」子句的彙總查詢能夠以類似於篩選查詢的方式執行。對於篩選查詢，R2 SQL 會選擇一個節點作為查詢執行的協調節點。該節點分析查詢內容，並查閱 R2 Data Catalog，以確定哪些 Parquet 列群組可能包含與查詢相關的資料。每一個 Parquet 列群組代表一個相對較小的任務單元，可由單個計算節點處理。協調節點將任務分發給多個工作節點，收集結果並傳回給使用者。

為了執行彙總查詢，我們遵循相同的步驟，將小任務分發給工作節點。但這一次，工作節點不僅要依據「WHERE」陳述式中的條件篩選列，還要計算**「預彙總」(pre-aggregates)** 。

預彙總是彙總過程的中間狀態。它是對一部分資料做部分彙總後的不完整結果。多個預彙總可以被合併，以計算出彙總函式的最終值。將彙總函式拆分為多個預彙總，使我們可以水平擴展彙總計算，充分利用 Cloudflare 網路中的龐大計算資源。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45BPPXJKC47WPRR8TQZR5H.png&w=715&h=674&f=webp&fit=cover&position=center)

例如，「count(*)」的預彙總結果就是一個數字，代表資料子集中列的數量。計算最終的「count(*)」就像將這些數字相加一樣簡單。「avg(value)」的預彙總結果包含兩個數字：「sum(value)」和「count(*)」。然後，可以透過將所有「sum(value)」值相加，將所有「count(*)」值相加，最後將第一個數位除以第二個數位來計算「avg(value)」的值。

當工作節點完成預彙總的計算後，會將結果資料流給協調節點。協調節點收集所有結果，根據預彙總計算出彙總函式的最終值，並將最終結果傳回給使用者。

## 洗牌機制：超越分散-聚集

當協調節點可以透過合併來自各個工作節點的小型、部分狀態來計算最終結果時，分散-彙總的方式非常高效。如果您執行類似 `SELECT sum(sales) FROM orders` 這樣的查詢，協調節點會從每個工作節點收到一個單一數值並相加。無論 R2 中儲存了多少資料，協調節點的記憶體佔用都可以忽略不計。

然而，當查詢需要根據彙總 _結果_ 進行排序或篩選時，這種方式就會變得低效。考慮下面這個查詢——它用於找出銷售額最高的前兩個部門：
    
    
    SELECT department, sum(sales)
    FROM sales
    GROUP BY department
    ORDER BY sum(sales) DESC
    LIMIT 2

要正確確定全域的前 2 名，需要知道整個資料集中每個部門的銷售總額。由於資料在底層 Parquet 檔案中是隨機分佈的，某個特定部門的銷售記錄很可能分散在許多不同的工作節點上。一個部門在每個單獨的工作節點上的銷售額可能都很低，因此不會進入任何本地的「前 2」清單，但在全域匯總後卻可能是銷售額最高的部門。

下圖展示了分散-彙總方法為何不適用於此查詢。「Dept A」是全球銷售額冠軍，但由於它的銷售記錄均勻分佈在多個工作節點上，它沒有進入某些本地的前 2 清單，最終被協調節點丟棄。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463ZP69R3N5R25QG4E9T0V.png&w=715&h=674&f=webp&fit=cover&position=center)

因此，當查詢按全域彙總結果排序時，協調節點無法依賴來自工作節點的預篩選結果。它必須向 _每個_ 工作節點請求 _每個_ 部門的銷售總額，以便在計算全域總數後進行排序。如果按高基數欄（如 IP 位址或使用者 ID）進行分組，這就會迫使協調節點接收並合併數百萬列資料，從而在單個節點上造成資源瓶頸。

為了解決這個問題，我們需要引入**洗牌 (shuffling)** ——一種在最終彙總發生之前，將特定分組的資料重新聚集到一起的方法。

### 彙總資料的洗牌

為了解決資料隨機分佈帶來的挑戰，我們引入了一個**洗牌階段** 。工作節點不再將結果傳送給協調節點，而是直接相互交換資料，根據分組鍵將列資料進行歸類。

這種路由依賴於**確定性雜湊分區** 。當工作節點處理一列資料時，它會對 `GROUP BY` 列進行雜湊計算，以確定目標工作節點。由於該雜湊是確定性的，叢集中的每個工作節點都能獨立地就特定資料應傳送到哪裡達成一致。例如，如果「Engineering」的雜湊值指向工作節點 5，那麼所有工作節點都知道應將「Engineering」相關的列路由到工作節點 5。無需中央註冊表。

下圖展示了這一流程。注意「Dept A」最初位於工作節點 1、2 和 3 上。因為雜湊函數將「Dept A」對應到工作節點 1，所有工作節點都會將這些列路由到同一個目的地。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45ZD7B5A4ZRR0NG4HHEKV4.png&w=715&h=622&f=webp&fit=cover&position=center)

洗牌彙總能夠產生正確的結果。然而，這種「全部對全部」(all-to-all) 的資料交換會引入時序依賴。如果工作節點 1 在工作節點 3 尚未完成傳送其「Dept A」資料份額時就提前開始計算最終總額，那麼結果將是不完整的。

為了解決這個問題，我們強制執行嚴格的**同步屏障** 。協調節點追蹤整個叢集的進度，而工作節點則緩衝它們的輸出資料，並透過 [_gRPC_](https://grpc.io/) 流刷新到對等節點。只有當每個工作節點確認已完成輸入檔案的處理並已刷新完洗牌緩衝區時，協調節點才會發出繼續執行的命令。這一屏障保證在進入下一階段時，每個工作節點上的資料集都是完整且準確的。

### 本地最終化

一旦同步屏障解除，每個工作節點都持有其被指派群組的完整資料集。此時，工作節點 1 擁有「Dept A」100% 的銷售記錄，並能確定地計算出最終總額。

這使得我們可以將篩選、排序等計算邏輯下推到工作節點執行，而不必讓協調節點承擔這些負擔。例如，如果查詢包含 `HAVING count(*) > 5`，工作節點可以在彙總完成後立即濾除不滿足該條件的群組。

在此階段的末尾，每個工作節點會為它所負責的群組產生一個已排序的最終結果流。

### 流式歸併

最後一塊拼圖是協調節點。在分散-彙總模型中，協調節點需要承擔對整個資料集進行彙總與排序的高開銷任務。而在洗牌模型中，它的角色發生了變化。

由於工作節點已經在本地計算出了最終的彙總結果並完成了排序，協調節點只需執行一次 **k 路歸併 (k-way merge)** 。它會為每個工作節點打開一個資料流程，逐列讀取結果；比較每個工作節點當前列的排序值，根據排序規則選出「勝出者」，並將其加入即將傳回給使用者的最終查詢結果中。

這種方法對於 `LIMIT` 查詢尤其高效。如果使用者請求前 10 個部門，協調節點會在歸併過程中找到前 10 條記錄後立即停止處理，而無需載入或歸併剩餘的數百萬行資料。這樣可以在不大量消耗計算資源的前提下，支援更大規模的操作。

## 用於處理海量資料集的強大引擎

隨著彙總功能的加入，[ _R2 SQL_](https://developers.cloudflare.com/r2-sql/?cf_target_id=84F4CFDF79EFE12291D34EF36907F300) 從一個擅長篩選資料的工具，轉變為能夠在海量資料集上進行資料處理的強大引擎。這得益于我們實現了諸如「分散-彙總」與「洗牌」等分散式執行策略，使我們能夠將計算推送到資料儲存的位置，充分利用 Cloudflare 的全球計算與網路規模。

無論您是要產生報表、監控大批量記錄以發現異常，還是僅僅想從資料中洞察趨勢，現在都可以在 Cloudflare 開發人員平台內輕鬆完成這一切，而無需承擔管理複雜 OLAP 基礎架構的開銷，也不必將資料移出 R2。

## 立即嘗試

R2 SQL 的彙總功能現已可用。我們非常期待看到您使用這些新功能處理 R2 Data Catalog 中的資料。

  * **開始使用：** 查看我們的[ _文件_](https://developers.cloudflare.com/r2-sql/sql-reference/)，獲取有關執行彙總查詢的範例和語法指南。
  * **加入對話：** 如果您有任何問題、回饋，或想要分享您正在建置的專案，歡迎加入 Cloudflare [_開發人員 Discord_](https://discord.com/invite/cloudflaredev) 與我們交流。



本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fr2-sql-aggregations%2F&t=%E5%AE%A3%E4%BD%88%20R2%20SQL%20%E9%96%8B%E5%A7%8B%E6%94%AF%E6%8F%B4%20GROUP%20BY%E3%80%81SUM%20%E5%92%8C%E5%85%B6%E4%BB%96%E5%BD%99%E7%B8%BD%E6%9F%A5%E8%A9%A2)[](https://x.com/intent/post?text=%E5%AE%A3%E4%BD%88+R2+SQL+%E9%96%8B%E5%A7%8B%E6%94%AF%E6%8F%B4+GROUP+BY%E3%80%81SUM+%E5%92%8C%E5%85%B6%E4%BB%96%E5%BD%99%E7%B8%BD%E6%9F%A5%E8%A9%A2&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fr2-sql-aggregations%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fr2-sql-aggregations%2F)[](https://bsky.app/intent/compose?text=%E5%AE%A3%E4%BD%88+R2+SQL+%E9%96%8B%E5%A7%8B%E6%94%AF%E6%8F%B4+GROUP+BY%E3%80%81SUM+%E5%92%8C%E5%85%B6%E4%BB%96%E5%BD%99%E7%B8%BD%E6%9F%A5%E8%A9%A2+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fr2-sql-aggregations%2F)[](https://mastodonshare.com/?text=%E5%AE%A3%E4%BD%88+R2+SQL+%E9%96%8B%E5%A7%8B%E6%94%AF%E6%8F%B4+GROUP+BY%E3%80%81SUM+%E5%92%8C%E5%85%B6%E4%BB%96%E5%BD%99%E7%B8%BD%E6%9F%A5%E8%A9%A2&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fr2-sql-aggregations%2F)[](https://www.threads.net/intent/post?text=%E5%AE%A3%E4%BD%88+R2+SQL+%E9%96%8B%E5%A7%8B%E6%94%AF%E6%8F%B4+GROUP+BY%E3%80%81SUM+%E5%92%8C%E5%85%B6%E4%BB%96%E5%BD%99%E7%B8%BD%E6%9F%A5%E8%A9%A2+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fr2-sql-aggregations%2F)

## 相關標籤

[R2](https://blog.cloudflare.com/zh-tw/tag/r2/)[Rust](https://blog.cloudflare.com/zh-tw/tag/rust/)[SQL](https://blog.cloudflare.com/zh-tw/tag/sql/)[無伺服器](https://blog.cloudflare.com/zh-tw/tag/serverless/)[資料](https://blog.cloudflare.com/zh-tw/tag/data/)[邊緣運算](https://blog.cloudflare.com/zh-tw/tag/edge-computing/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
