---
url: https://blog.cloudflare.com/zh-tw/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/
title: \u5c0b\u627e Linux \u6838\u5fc3\u4e2d\u639b\u8d77\u5de5\u4f5c\u7684\u539f\u56e0 | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:50:05.937650+00:00
---

# 尋找 Linux 核心中掛起工作的原因 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)[核心](https://blog.cloudflare.com/zh-tw/tag/kernel/)[深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)+1顯示另外 1 個標籤

4 標籤顯示 4 個標籤

  * 文章標籤
  * [Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)[核心](https://blog.cloudflare.com/zh-tw/tag/kernel/)[深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)[監控](https://blog.cloudflare.com/zh-tw/tag/monitoring/)
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



[監控](https://blog.cloudflare.com/zh-tw/tag/monitoring/)

[Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)[核心](https://blog.cloudflare.com/zh-tw/tag/kernel/)[深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)[監控](https://blog.cloudflare.com/zh-tw/tag/monitoring/)

2025年2月14日

# 尋找 Linux 核心中掛起工作的原因

![Oxana Kharitonova](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462M0EFJXTMW95T83V5454.png&w=64&h=64&f=webp&fit=cover&position=center)![Jesper Brouer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW499RS2WW80VBYFGEW0TADD.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Oxana Kharitonova](https://blog.cloudflare.com/zh-tw/author/oxana/)和[Jesper Brouer](https://blog.cloudflare.com/zh-tw/author/jesper-brouer/)

閱讀時間：8 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/)和[简体中文](https://blog.cloudflare.com/zh-cn/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/).

![BLOG-2660 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46Y20YJ525ZDYYEE488MY4.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vv+193owMvdzNfl5ezy7/Lz6unq/////f7/29/rxMzez9jm5uzz8fP17Ozt////////4eTuytDh1Nro6u/19Pb48fDx////////6er00tbn2uDu7/P6+fv99vb3////////8PL829/w4uj29fr//v//+/v8////////9vn/4un56fH++///////////////////+/7/6O//7vf//////////////////////P//6vL/8Pr/////////////)

根據您的設定，Linux 核心可能在其記錄中產生掛起工作警告訊息。搜尋網際網路和核心文件，您可以找到一個簡短的解釋，即核心處理序卡在不可中斷狀態，並且在意外長的時間內沒有被排程到 CPU 上執行。這解釋了警告的含義，但沒有提供它發生的原因。在這篇部落格文章中，我們將探討掛起工作警告的工作原理、它為什麼會發生、這是 Linux 核心還是應用程式本身的錯誤，以及是否值得對其進行監控。

### INFO：工作 XXX:1495882 被封鎖超過 YYY 秒。

核心記錄中的掛起工作訊息如下所示：
    
    
    INFO: task XXX:1495882 blocked for more than YYY seconds.
         Tainted: G          O       6.6.39-cloudflare-2024.7.3 #1
    "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
    task:XXX         state:D stack:0     pid:1495882 ppid:1      flags:0x00004002
    . . .

Linux 中的處理序可以處於不同的狀態。一些處理序正在執行或準備在 CPU 上執行——它們處於 [`_TASK_RUNNING_`](https://elixir.bootlin.com/linux/v6.12.6/source/include/linux/sched.h#L99) 狀態。另一些處理序正在等待某些訊號或事件發生，例如網路封包到達或來自使用者的終端輸入。它們處於 `TASK_INTERRUPTIBLE` 狀態，並且可以在此狀態下停留任意長的時間，直到被訊號喚醒。關於這些狀態，最重要的一點是它們仍然可以接收訊號，並被訊號終止。相較之下，處於 `TASK_UNINTERRUPTIBLE` 狀態的處理序只等待某些特殊類型的事件將其喚醒，並且不能被訊號中斷。直到處理序退出此狀態後，才會傳送訊號，只有系統重新開機才能清除處理序。在上面顯示的記錄中，它用字母 `D` 標記。

如果這個喚醒事件沒有發生或者發生時有顯著延遲，會怎麼樣？（「顯著延遲」可能是幾秒或幾分鐘，具體取決於系統。）那麼我們的依存性處理序就會以這個狀態掛起。如果這個依存性處理序持有某個鎖並阻止其他處理序獲取該鎖，會怎麼樣？或者如果我們看到許多處理序處於 D 狀態，又會怎麼樣？它可能會告訴我們，一些系統資源不堪重負或無法正常工作。同時，這種狀態非常有價值，特別是當我們想保留處理序記憶體時。如果部分資料寫入磁碟，而另一部分仍在處理序記憶體中，這種狀態就很有用——我們不希望磁碟上的資料不一致。或者，當出現錯誤時，我們可能想要處理序記憶體的快照。為了保留此行為，但使其更受控制，核心中引入了一種新狀態：[` _TASK_KILLABLE_`](https://lwn.net/Articles/288056/)——它仍然保護處理序，但允許使用致命訊號終止處理序。

### Linux 如何識別掛起的處理序

Linux 核心有一個特殊的執行緒，稱為 `khungtaskd`。它會根據設定定期執行，反覆運算所有處於 `D` 狀態的處理序。如果一個處理序處於這種狀態超過 YYY 秒，我們將在核心記錄中看到一條訊息。您可以根據意願對這個精靈的一些設定進行變更：
    
    
    $ sudo sysctl -a --pattern hung
    kernel.hung_task_all_cpu_backtrace = 0
    kernel.hung_task_check_count = 4194304
    kernel.hung_task_check_interval_secs = 0
    kernel.hung_task_panic = 0
    kernel.hung_task_timeout_secs = 10
    kernel.hung_task_warnings = 200

在 Cloudflare，我們將通知閾值 `kernel.hung_task_timeout_secs` 從預設的 120 秒變更為 10 秒。您可以根據設定以及此延遲對您的重要性來調整系統的值。如果處理序在 D 狀態下停留的時間超過 `hung_task_timeout_secs` 秒，則會寫入記錄項目，並且我們的內部監控系統會根據此記錄發出警示。這裡的另一個重要設定是 `kernel.hung_task_warnings`：將傳送到記錄的訊息總數。我們將其限制為 200 筆訊息，並每 15 分鐘重設一次。這讓我們不會被同一個問題所困擾，同時不會讓我們的監控停止太久。您可以透過[ _將值設定為「-1」_](https://docs.kernel.org/admin-guide/sysctl/kernel.html#hung-task-warnings)來使其無限制。

為了更好地理解掛起工作的根本原因以及系統會受到怎樣的影響，我們來看幾個更詳細的範例。

### 範例 1：XFS

通常，記錄中會顯示一個有意義的處理序或應用程式名稱，但有時您可能會看到這樣的內容：
    
    
    INFO: task kworker/13:0:834409 blocked for more than 11 seconds.
     	Tainted: G      	O   	6.6.39-cloudflare-2024.7.3 #1
    "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
    task:kworker/13:0	state:D stack:0 	pid:834409 ppid:2   flags:0x00004000
    Workqueue: xfs-sync/dm-6 xfs_log_worker

在這筆記錄中，`kworker` 是核心執行緒。它用作一種推遲機制，即某項工作將排程在未來執行。在 `kworker` 下，工作是從不同的工作中匯總而來的，這使得很難判斷哪個應用程式正在經歷延遲。幸運的是，`kworker` 會伴隨著 [`_Workqueue_`](https://docs.kernel.org/core-api/workqueue.html) 行出現。`Workqueue` 是一個連結清單，通常在核心中預先定義，這些工作將由 `kworker` 新增到佇列中並按照新增順序執行。`Workqueue` 名稱 `xfs-sync` 及[ _其指向的函數_](https://elixir.bootlin.com/linux/v6.12.6/source/kernel/workqueue.c#L6096)`xfs_log_worker`，可能提供了很好的線索。在這裡，我們可以假設 [_XFS_](https://en.wikipedia.org/wiki/XFS) 承受壓力並檢查相關指標。它協助我們發現，由於某些設定變更，我們忘記了前段時間為[ _加快 Linux 磁碟加密速度_](https://blog.cloudflare.com/speeding-up-linux-disk-encryption/)而引入的 `no_read_workqueue`/`no_write_workqueue` 標誌。

 _總結_ ：這種情況下，系統沒有發生任何嚴重的問題，但是掛起工作警告提醒我們，檔案系統的速度已經變慢。

### 範例 2：Coredump

我們來看看下一個掛起工作記錄及其解碼的堆疊追蹤：
    
    
    INFO: task test:964 blocked for more than 5 seconds.
          Not tainted 6.6.72-cloudflare-2025.1.7 #1
    "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
    task:test            state:D stack:0     pid:964   ppid:916    flags:0x00004000
    Call Trace:
    <TASK>
    __schedule (linux/kernel/sched/core.c:5378 linux/kernel/sched/core.c:6697) 
    schedule (linux/arch/x86/include/asm/preempt.h:85 (discriminator 13) linux/kernel/sched/core.c:6772 (discriminator 13)) 
    [do_exit (linux/kernel/exit.c:433 (discriminator 4) linux/kernel/exit.c:825 (discriminator 4)) 
    ? finish_task_switch.isra.0 (linux/arch/x86/include/asm/irqflags.h:42 linux/arch/x86/include/asm/irqflags.h:77 linux/kernel/sched/sched.h:1385 linux/kernel/sched/core.c:5132 linux/kernel/sched/core.c:5250) 
    do_group_exit (linux/kernel/exit.c:1005) 
    get_signal (linux/kernel/signal.c:2869) 
    ? srso_return_thunk (linux/arch/x86/lib/retpoline.S:217) 
    ? hrtimer_try_to_cancel.part.0 (linux/kernel/time/hrtimer.c:1347) 
    arch_do_signal_or_restart (linux/arch/x86/kernel/signal.c:310) 
    ? srso_return_thunk (linux/arch/x86/lib/retpoline.S:217) 
    ? hrtimer_nanosleep (linux/kernel/time/hrtimer.c:2105) 
    exit_to_user_mode_prepare (linux/kernel/entry/common.c:176 linux/kernel/entry/common.c:210) 
    syscall_exit_to_user_mode (linux/arch/x86/include/asm/entry-common.h:91 linux/kernel/entry/common.c:141 linux/kernel/entry/common.c:304) 
    ? srso_return_thunk (linux/arch/x86/lib/retpoline.S:217) 
    do_syscall_64 (linux/arch/x86/entry/common.c:88) 
    entry_SYSCALL_64_after_hwframe (linux/arch/x86/entry/entry_64.S:121) 
    </TASK>

堆疊追蹤顯示處理序或應用程式 `test` 被封鎖 `for more than 5 seconds`。我們可以透過名稱認出這個使用者空間應用程式，但它為什麼被封鎖了？在查找原因時，檢查堆疊追蹤總是有幫助的。這裡最值得注意的一行是 `do_exit (linux/kernel/exit.c:433 (discriminator 4) linux/kernel/exit.c:825 (discriminator 4))`。[ _來源程式碼_](https://elixir.bootlin.com/linux/v6.6.67/source/kernel/exit.c#L825)指向 `coredump_task_exit` 函數。此外，檢查處理序指標發現，應用程式在記錄中出現警告訊息時崩潰。當處理序基於某些訊號集（異常）終止時，[ _Linux 核心可以提供核心傾印檔案_](https://man7.org/linux/man-pages/man5/core.5.html)（如果啟用）。「當處理序終止時，核心會在退出之前為處理序記憶體建立快照，並將其寫入檔案或透過通訊端傳送到另一個處理常式」——這樣的機制可以是 [_systemd-coredump_](https://systemd.io/COREDUMP/) 或由您自訂。發生這種情況時，核心會將處理序移至 `D` 狀態以保留其記憶體並提前終止。處理序記憶體使用率越高，獲取核心傾印檔案所需的時間就越長，並且收到掛起工作警告的可能性就越高。

讓我們用一個小型 Go 程式來觸發它，以驗證我們的假設。我們將使用預設的 Linux coredump 處理常式，並將掛起工作閾值降低至 1 秒。

Coredump 設定：
    
    
    $ sudo sysctl -a --pattern kernel.core
    kernel.core_pattern = core
    kernel.core_pipe_limit = 16
    kernel.core_uses_pid = 1

您可以對 [_sysctl_](https://man7.org/linux/man-pages/man8/sysctl.8.html) 進行變更：
    
    
    $ sudo sysctl -w kernel.core_uses_pid=1

掛起工作設定：
    
    
    $ sudo sysctl -a --pattern hung
    kernel.hung_task_all_cpu_backtrace = 0
    kernel.hung_task_check_count = 4194304
    kernel.hung_task_check_interval_secs = 0
    kernel.hung_task_panic = 0
    kernel.hung_task_timeout_secs = 1
    kernel.hung_task_warnings = -1

Go 程式：
    
    
    $ cat main.go
    package main
    
    import (
    	"os"
    	"time"
    )
    
    func main() {
    	_, err := os.ReadFile("test.file")
    	if err != nil {
    		panic(err)
    	}
    	time.Sleep(8 * time.Minute) 
    }

此程式會將 10 GB 的檔案讀取到處理序記憶體中。我們來建立檔案：
    
    
    $ yes this is 10GB file | head -c 10GB > test.file

最後一步是建置 Go 程式，使其崩潰，並觀察我們的核心記錄：
    
    
    $ go mod init test
    $ go build .
    $ GOTRACEBACK=crash ./test
    $ (Ctrl+\)

太棒了！我們可以看到掛起工作警告：
    
    
    $ sudo dmesg -T | tail -n 31
    INFO: task test:8734 blocked for more than 22 seconds.
          Not tainted 6.6.72-cloudflare-2025.1.7 #1
          Blocked by coredump.
    "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
    task:test            state:D stack:0     pid:8734  ppid:8406   task_flags:0x400448 flags:0x00004000

順便問一下，您注意到記錄中的 `Blocked by coredump.` 行了嗎？它最近被新增到[ _上游_](https://git.kernel.org/pub/scm/linux/kernel/git/akpm/mm.git/commit/?h=mm-nonmm-stable&id=23f3f7625cfb55f92e950950e70899312f54afb7)程式碼中，以提高可見性並消除處理序本身的責任。該修補程式還新增了 `task_flags` 資訊，因為透過標誌 [`_PF_POSTCOREDUMP_`](https://elixir.bootlin.com/linux/v6.13.1/source/include/linux/sched.h#L1675) 偵測到 `Blocked by coredump`，瞭解所有工作標誌對於進一步分析根本原因很有用。

 _總結_ ：此範例表明，即使所有跡象都表明問題出在應用程式上，但真正的根本原因可能是其他內容——在此範例中是 `coredump`。

### 範例 3：rtnl_mutex

這個問題很難偵錯。通常，警示僅限於一兩個不同的處理序，這意味著只有特定的應用程式或子系統遇到問題。在這個範例中，我們看到數十個不相關的工作掛起數分鐘，而且隨著時間的推移並沒有任何改進。記錄中沒有其他內容，大多數系統指標都沒有問題，並且現有流量得到服務，但無法透過 ssh 連接到伺服器。新的 Kubernetes 容器建立也停滯不前。初始分析不同工作的堆疊追蹤表明，所有追蹤都僅限於三個函數：
    
    
    rtnetlink_rcv_msg+0x9/0x3c0
    dev_ethtool+0xc6/0x2db0 
    bonding_show_bonds+0x20/0xb0

進一步調查顯示，所有這些函數都在等待獲取 [`_rtnl_lock_`](https://elixir.bootlin.com/linux/v6.6.74/source/net/core/rtnetlink.c#L76)。看起來某個應用程式獲取了 `rtnl_mutex` 但沒有釋放它。所有其他處理序都處於 `D` 狀態，等待此鎖。

RTNL 鎖主要由核心網路子系統用於與網路相關的設定，包括寫入和讀取。RTNL 是一個全域 **mutex** 鎖，但正在進行[ _上游工作_](https://lpc.events/event/18/contributions/1959/)來按網路命名空間 (netns) 拆分 RTNL。

從掛起工作報告中，我們可以觀察到因等待鎖而停滯的「受害者」，但我們如何識別持有此鎖時間過長的工作？為了解決這個問題，我們透過 `bpftrace` 指令碼利用 `BPF`，因為這使我們能夠檢查正在執行的核心狀態。[ _核心的 mutex 實作_](https://elixir.bootlin.com/linux/v6.6.75/source/include/linux/mutex.h#L67)有一個名為 `owner` 的結構體成員。它包含一個指標，從擁有 mutex 的處理序指向 [`_task_struct_`](https://elixir.bootlin.com/linux/v6.6.75/source/include/linux/sched.h#L746)，只不過它被編碼為 `atomic_long_t` 類型。這是因為 mutex 實作將一些狀態資訊存儲在此指標的低 3 位元（遮罩 0x7）中。因此，要讀取和取消引用此 `task_struct` 指標，我們必須首先遮罩低位元 (0x7)。

用於確定誰持有 mutex 的 `bpftrace` 指令碼如下所示：
    
    
    #!/usr/bin/env bpftrace
    interval:s:10 {
      $rtnl_mutex = (struct mutex *) kaddr("rtnl_mutex");
      $owner = (struct task_struct *) ($rtnl_mutex->owner.counter & ~0x07);
      if ($owner != 0) {
        printf("rtnl_mutex->owner = %u %s\n", $owner->pid, $owner->comm);
      }
    }

在此指令碼中，`rtnl_mutex` 鎖是一個全域鎖，其位址可透過 `/proc/kallsyms` 公開——使用 `bpftrace` 協助程式 `kaddr()`，我們可以從 `kallsyms` 存取 struct mutex 指標。因此，我們可以定期（透過 `interval:s:10`）檢查是否有處理序持有此鎖。

輸出如下：
    
    
    rtnl_mutex->owner = 3895365 calico-node

這使我們能夠快速識別出 `calico-node` 是持有 RTNL 鎖時間過長的處理序。為了快速觀察此處理序本身停滯的位置，可以透過 `/proc/3895365/stack` 獲取呼叫堆疊。這向我們表明，根本原因是 Wireguard 設定變更，函數 `wg_set_device()` 持有 RTNL 鎖，而 `peer_remove_after_dead()` 等待 `napi_disable()` 呼叫的時間過長。我們繼續透過一個名為 [`_drgn_`](https://drgn.readthedocs.io/en/latest/user_guide.html#stack-traces) 的工具進行偵錯，這是一個可程式設計的偵錯工具，可以透過類似 Python 的互動式 shell 偵錯正在執行的核心。我們仍然沒有發現 Wireguard 問題的根本原因，並[ _向上游尋求_](https://lore.kernel.org/lkml/CALrw=nGoSW=M-SApcvkP4cfYwWRj=z7WonKi6fEksWjMZTs81A@mail.gmail.com/)幫助，這就是另一個故事了。

 _總結_ ：掛起工作訊息是我們在核心記錄中唯一擁有的訊息。這些訊息的每個堆疊追蹤都是唯一的，但透過仔細分析，我們可以發現相似之處，並繼續使用其他工具進行偵錯。

### 結語

您的系統可能有不同的掛起工作警告，我們也有許多其他情況未在此處提及。每種情況都是獨一無二的，並沒有標準的偵錯方法。但希望這篇部落格文章能幫助您更好地理解為什麼需要啟用這些警告、它們如何工作，以及它們背後的含義。我們也試圖為偵錯過程提供一些指導：

  * 分析堆疊追蹤可能是一個不錯的偵錯起點，即使所有訊息看起來都不相關，就像我們在範例 3 中看到的那樣
  * 請記住，警示可能會產生誤導，指向受害者而不是犯罪者，如範例 2 和範例 3 中所示
  * 如果核心沒有將應用程式排程到 CPU 上，而是將其置於 D 狀態並發出警告——真正的問題可能存在于應用程式碼中



祝您偵錯順利，並希望本資料對您的這段旅程有所幫助！

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F&t=%E5%B0%8B%E6%89%BE%20Linux%20%E6%A0%B8%E5%BF%83%E4%B8%AD%E6%8E%9B%E8%B5%B7%E5%B7%A5%E4%BD%9C%E7%9A%84%E5%8E%9F%E5%9B%A0)[](https://x.com/intent/post?text=%E5%B0%8B%E6%89%BE+Linux+%E6%A0%B8%E5%BF%83%E4%B8%AD%E6%8E%9B%E8%B5%B7%E5%B7%A5%E4%BD%9C%E7%9A%84%E5%8E%9F%E5%9B%A0&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)[](https://bsky.app/intent/compose?text=%E5%B0%8B%E6%89%BE+Linux+%E6%A0%B8%E5%BF%83%E4%B8%AD%E6%8E%9B%E8%B5%B7%E5%B7%A5%E4%BD%9C%E7%9A%84%E5%8E%9F%E5%9B%A0+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)[](https://mastodonshare.com/?text=%E5%B0%8B%E6%89%BE+Linux+%E6%A0%B8%E5%BF%83%E4%B8%AD%E6%8E%9B%E8%B5%B7%E5%B7%A5%E4%BD%9C%E7%9A%84%E5%8E%9F%E5%9B%A0&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)[](https://www.threads.net/intent/post?text=%E5%B0%8B%E6%89%BE+Linux+%E6%A0%B8%E5%BF%83%E4%B8%AD%E6%8E%9B%E8%B5%B7%E5%B7%A5%E4%BD%9C%E7%9A%84%E5%8E%9F%E5%9B%A0+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)

## 相關標籤

[Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)[核心](https://blog.cloudflare.com/zh-tw/tag/kernel/)[深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)[監控](https://blog.cloudflare.com/zh-tw/tag/monitoring/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
