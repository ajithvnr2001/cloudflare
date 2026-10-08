---
url: https://blog.cloudflare.com/zh-tw/live-patch-security-vulnerabilities-with-ebpf-lsm/
title: \u4f7f\u7528 eBPF Linux Security Module \u5373\u6642\u4fee\u88dc Linux \u6838\u5fc3\u5167\u7684\u5b89\u5168\u6027\u6f0f\u6d1e | Cloudflare \u90e8\u843d\u683c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:50:35.546355+00:00
---

# 使用 eBPF Linux Security Module 即時修補 Linux 核心內的安全性漏洞 | Cloudflare 部落格

> Source: https://blog.cloudflare.com/zh-tw/live-patch-security-vulnerabilities-with-ebpf-lsm/

[部落格](https://blog.cloudflare.com/zh-tw/)

[Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)[Programming](https://blog.cloudflare.com/zh-tw/tag/programming/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)+1顯示另外 1 個標籤

4 標籤顯示 4 個標籤

  * 文章標籤
  * [Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)
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



[深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)

[Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)[Programming](https://blog.cloudflare.com/zh-tw/tag/programming/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)

2022年6月29日

# 使用 eBPF Linux Security Module 即時修補 Linux 核心內的安全性漏洞

![Frederick Lawler](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YV7KWFD5VEJ5KEDXS2R1.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Frederick Lawler](https://blog.cloudflare.com/zh-tw/author/frederick/)

閱讀時間：6 分鐘

複製網址

這篇文章亦提供 [English](https://blog.cloudflare.com/live-patch-security-vulnerabilities-with-ebpf-lsm/)和[简体中文](https://blog.cloudflare.com/zh-cn/live-patch-security-vulnerabilities-with-ebpf-lsm/).

![Live-patching security vulnerabilities inside the Linux kernel with eBPF Linux Security Module](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BF72JMBAWG18TW78WAGE.png&w=1894&h=947&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA9/j/9PX87+/y7Ozt8O/u8vLy7+/w6Onp+Pr/9fb/7u7z7Ovq7+7r8vHv8PDv6Onr+/3/9/n/8PD07evp8O7p9PLu8fHx6uvv/////P7/9PT58O7t9PHs+Pbx9fX17e/0////////+/v/9/X0+/j0//35+/v88/T5//////////////79///+////////+fr//////////////////////////////v7/////////////////////////////////)

[Linux Security Module](https://www.kernel.org/doc/html/latest/admin-guide/LSM/index.html) (LSM) 是一個基於勾點的架構，用於在 Linux 核心中實作安全性原則及強制存取控制。直到前不久，期望實作安全性原則的使用者還只有兩個選項：即設定 AppArmor 或 SELinux 等現有 LSM 模組，或編寫自訂核心模組。

[Linux 5.7](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.7) 推出了第三種方法︰[LSM 延伸柏克萊封包篩選 (eBPF)](https://docs.kernel.org/bpf/prog_lsm.html)（簡稱為 LSM BPF）。使用 LSM BPF，開發人員無需設定或載入核心模組即可編寫精細原則。LSM BPF 程式在載入時進行驗證，然後在呼叫路徑中連線 LSM 勾點時執行。

## 我們來解決一個實際問題

現代作業系統提供的設施允許對核心資源進行「分割」。例如，FreeBSD 有「jail」，Solaris 有「zone」。Linux 則有所不同，它提供一組看似獨立的設施，每個設施都允許隔離特定的資源。這些設施被稱為「命名空間」，並且已經在核心中不斷發展了很多年。它們是 Docker、lxc 或 firejail 等熱門工具的基礎。許多命名空間毫無爭議，比如 UTS 命名空間，它允許主機系統隱藏其主機名稱和時間。另一些則既複雜又直白——眾所週知，NET 和 NS (mount) 命名空間令人很難理解。最後，還有這個非常特殊、非常奇怪的 USER 命名空間。

USER 命名空間非常特殊，因為它允許擁有者在其內部以「root」身分進行操作。雖然其工作原理不在本部落格貼文所討論的範圍之內，但可以說，正是因為有它作為基礎，才會有 Docker 這樣不以真正的 root 身分操作的工具，以及無根容器這樣的物件。

由於其性質，允許無權限使用者存取 USER 命名空間總是會帶來很大的安全風險。權限提升就是這樣一種風險。

權限提升是常見的作業系統攻擊面。使用者獲得權限的一種方法就是透過 unshare [syscall](https://en.wikipedia.org/wiki/System_call) 將其命名空間對應至根命名空間，並指定 _CLONE_NEWUSER_ 旗標。這告訴 unshare 建立一個具有完整權限的新使用者命名空間，並將新使用者及群組 ID 對應至之前的命名空間。您可以使用 [unshare(1)](https://man7.org/linux/man-pages/man1/unshare.1.html) 程式將 root 對應至原始命名空間：

在大多數情况下，使用 unshare 並無危害，並且預定以較低的權限執行。但是，此 syscall 已被發現用於[提升權限](https://nvd.nist.gov/vuln/detail/CVE-2022-0492)。
    
    
    $ id
    uid=1000(fred) gid=1000(fred) groups=1000(fred) …
    $ unshare -rU
    # id
    uid=0(root) gid=0(root) groups=0(root),65534(nogroup)
    # cat /proc/self/uid_map
             0       1000          1

Syscalls _clone_ 和 _clone3_ 很是值得研究，因為它們還具有 _CLONE_NEWUSER_ 的能力。然而，在這篇貼文中，我們將重點討論 unshare。

Debian 透過這個[「add sysctl to disallow unprivileged CLONE_NEWUSER by default」](https://sources.debian.org/patches/linux/3.16.56-1+deb8u1/debian/add-sysctl-to-disallow-unprivileged-CLONE_NEWUSER-by-default.patch/)修補程式解決了這個問題，但它不是主流。另一個類似的修補程式[「sysctl: allow CLONE_NEWUSER to be disabled」](https://lore.kernel.org/all/1453502345-30416-3-git-send-email-keescook@chromium.org/)試圖成為主流，但遭到了排擠。一種批評意見是針對特定的應用程式[無法切換此功能](https://lore.kernel.org/all/87poq5y0jw.fsf@x220.int.ebiederm.org/)。在《[Controlling access to user namespaces](https://lwn.net/Articles/673597/)》（控制對使用者命名空間的存取權）這篇文章中，作者寫道「...the current patches do not appear to have an easy path into the mainline（現有修補程式似乎很難成為主流）。」我們可以看到，這些修補程式最終並沒有包含在 vanilla 核心中。

## 我們的解決方案 — LSM BPF

由於似乎無法選擇使用上游程式碼來限制 USER 命名空間，我們决定使用 LSM BPF 來規避這些問題。使用這種方法，不僅無需修改核心，還可以體現複雜的規則來保護存取。

### 追蹤適當的候選勾點

首先，我們來追蹤目標 syscall。我們可以在 [_include/linux/syscalls.h_](https://elixir.bootlin.com/linux/v5.18/source/include/linux/syscalls.h#L608) 檔案中找到原型。這在其中並不太容易進行追蹤，但這一行：

為我們提供了接下來在 [_kernel/fork.c_](https://elixir.bootlin.com/linux/v5.18/source/kernel/fork.c#L3201) 中的何處進行尋找的線索。在那裡對 [_ksys_unshare()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/fork.c#L3082) 進行了呼叫。透過該函式進行挖掘，我們找到了對 [_unshare_userns()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/fork.c#L3129) 的呼叫。這看起來很有希望成功。
    
    
    /* kernel/fork.c */

到目前為止，我們已經確定了 syscall 實作，但下一個問題是我們可以使用哪些勾點？因為我們透過[手冊頁](https://man7.org/linux/man-pages/man2/unshare.2.html)知道 unshare 用於變動工作，所以我們在 [_include/linux/lsm_hooks.h_](https://elixir.bootlin.com/linux/v5.18/source/include/linux/lsm_hooks.h#L605) 中查看基於工作的勾點。回到函式 [_unshare_userns()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/user_namespace.c#L171)，我們看到對 [_prepare_creds()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/cred.c#L252) 進行了呼叫。這對 [_cred_prepare_](https://elixir.bootlin.com/linux/v5.18/source/include/linux/lsm_hooks.h#L624) 勾點來說非常熟悉。為了透過 [_prepare_creds()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/cred.c#L291) 驗證我們有自己的配對，我們看到對安全性勾點 [_security_prepare_creds()_](https://elixir.bootlin.com/linux/v5.18/source/security/security.c#L1706) 的呼叫，其最終呼叫了勾點：

無需詳細探究細節，我們也知道這是一個很好用的勾點，因為 _prepare_creds()_ 剛好在 _create_user_ns()_ （位於 [_unshare_userns()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/user_namespace.c#L181) 中）前進行了呼叫，後者是我們嘗試封鎖的操作。
    
    
    …
    rc = call_int_hook(cred_prepare, 0, new, old, gfp);
    …

### LSM BPF 解決方案

我們將使用 [eBPF compile once-run everywhere (CO-RE)](https://nakryiko.com/posts/bpf-core-reference-guide/#defining-own-co-re-relocatable-type-definitions) 方法進行編譯。透過這種方法，我們可以在一個架構上進行編譯，在另一個架構中進行載入。但我們將專門以 x86_64 為目標。適用於 ARM64 的 LSM BPF 仍在開發中，以下程式碼將無法在該架構上執行。關注 [BPF 郵寄名單](https://lore.kernel.org/bpf/)以追蹤進度。

此解決方案在具有以下設定且版本 >= 5.15 的核心上進行了測試：

可能需要開機選項 `lsm=bpf`（若是 `CONFIG_LSM` 在名單中不包含「bpf」的話）。
    
    
    BPF_EVENTS
    BPF_JIT
    BPF_JIT_ALWAYS_ON
    BPF_LSM
    BPF_SYSCALL
    BPF_UNPRIV_DEFAULT_OFF
    DEBUG_INFO_BTF
    DEBUG_INFO_DWARF_TOOLCHAIN_DEFAULT
    DYNAMIC_FTRACE
    FUNCTION_TRACER
    HAVE_DYNAMIC_FTRACE

我們從前序編碼開始：

 _deny_unshare.bpf.c_ ：

接下來，我們透過以下方式為 CO-RE 重新配置建立必要的結構：
    
    
    #include <linux/bpf.h>
    #include <linux/capability.h>
    #include <linux/errno.h>
    #include <linux/sched.h>
    #include <linux/types.h>
    
    #include <bpf/bpf_tracing.h>
    #include <bpf/bpf_helpers.h>
    #include <bpf/bpf_core_read.h>
    
    #define X86_64_UNSHARE_SYSCALL 272
    #define UNSHARE_SYSCALL X86_64_UNSHARE_SYSCALL

 _deny_unshare.bpf.c_ ：

我們不需要完全充實結構；我們只需要提供程式運作所需的絕對最少資訊即可。CO-RE 將採取任何必要的動作來為您的核心執行重新配置。因此，編寫 LSM BPF 程式就變得特別簡單！
    
    
    …
    
    typedef unsigned int gfp_t;
    
    struct pt_regs {
    	long unsigned int di;
    	long unsigned int orig_ax;
    } __attribute__((preserve_access_index));
    
    typedef struct kernel_cap_struct {
    	__u32 cap[_LINUX_CAPABILITY_U32S_3];
    } __attribute__((preserve_access_index)) kernel_cap_t;
    
    struct cred {
    	kernel_cap_t cap_effective;
    } __attribute__((preserve_access_index));
    
    struct task_struct {
        unsigned int flags;
        const struct cred *cred;
    } __attribute__((preserve_access_index));
    
    char LICENSE[] SEC("license") = "GPL";
    
    …

 _deny_unshare.bpf.c_ ：

建立程式是第一步，第二步是載入程式並將其連接到所需的勾點。可以採取幾種方法來完成這一步：[Cilium ebpf](https://github.com/cilium/ebpf) 專案、[Rust 繫結](https://github.com/libbpf/libbpf-rs)以及 [ebpf.io](https://ebpf.io/projects/) 專案橫向頁面上的其他幾個專案。我們將使用原生 libbpf。
    
    
    SEC("lsm/cred_prepare")
    int BPF_PROG(handle_cred_prepare, struct cred *new, const struct cred *old,
                 gfp_t gfp, int ret)
    {
        struct pt_regs *regs;
        struct task_struct *task;
        kernel_cap_t caps;
        int syscall;
        unsigned long flags;
    
        // If previous hooks already denied, go ahead and deny this one
        if (ret) {
            return ret;
        }
    
        task = bpf_get_current_task_btf();
        regs = (struct pt_regs *) bpf_task_pt_regs(task);
        // In x86_64 orig_ax has the syscall interrupt stored here
        syscall = regs->orig_ax;
        caps = task->cred->cap_effective;
    
        // Only process UNSHARE syscall, ignore all others
        if (syscall != UNSHARE_SYSCALL) {
            return 0;
        }
    
        // PT_REGS_PARM1_CORE pulls the first parameter passed into the unshare syscall
        flags = PT_REGS_PARM1_CORE(regs);
    
        // Ignore any unshare that does not have CLONE_NEWUSER
        if (!(flags & CLONE_NEWUSER)) {
            return 0;
        }
    
        // Allow tasks with CAP_SYS_ADMIN to unshare (already root)
        if (caps.cap[CAP_TO_INDEX(CAP_SYS_ADMIN)] & CAP_TO_MASK(CAP_SYS_ADMIN)) {
            return 0;
        }
    
        return -EPERM;
    }

_deny_unshare.c_ ：

最後，我們使用下列 Makefile 進行編譯：
    
    
    #include <bpf/libbpf.h>
    #include <unistd.h>
    #include "deny_unshare.skel.h"
    
    static int libbpf_print_fn(enum libbpf_print_level level, const char *format, va_list args)
    {
        return vfprintf(stderr, format, args);
    }
    
    int main(int argc, char *argv[])
    {
        struct deny_unshare_bpf *skel;
        int err;
    
        libbpf_set_strict_mode(LIBBPF_STRICT_ALL);
        libbpf_set_print(libbpf_print_fn);
    
        // Loads and verifies the BPF program
        skel = deny_unshare_bpf__open_and_load();
        if (!skel) {
            fprintf(stderr, "failed to load and verify BPF skeleton\n");
            goto cleanup;
        }
    
        // Attaches the loaded BPF program to the LSM hook
        err = deny_unshare_bpf__attach(skel);
        if (err) {
            fprintf(stderr, "failed to attach BPF skeleton\n");
            goto cleanup;
        }
    
        printf("LSM loaded! ctrl+c to exit.\n");
    
        // The BPF link is not pinned, therefore exiting will remove program
        for (;;) {
            fprintf(stderr, ".");
            sleep(1);
        }
    
    cleanup:
        deny_unshare_bpf__destroy(skel);
        return err;
    }

_Makefile_ ：

### 結果
    
    
    CLANG ?= clang-13
    LLVM_STRIP ?= llvm-strip-13
    ARCH := x86
    INCLUDES := -I/usr/include -I/usr/include/x86_64-linux-gnu
    LIBS_DIR := -L/usr/lib/lib64 -L/usr/lib/x86_64-linux-gnu
    LIBS := -lbpf -lelf
    
    .PHONY: all clean run
    
    all: deny_unshare.skel.h deny_unshare.bpf.o deny_unshare
    
    run: all
    	sudo ./deny_unshare
    
    clean:
    	rm -f *.o
    	rm -f deny_unshare.skel.h
    
    #
    # BPF is kernel code. We need to pass -D__KERNEL__ to refer to fields present
    # in the kernel version of pt_regs struct. uAPI version of pt_regs (from ptrace)
    # has different field naming.
    # See: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=fd56e0058412fb542db0e9556f425747cf3f8366
    #
    deny_unshare.bpf.o: deny_unshare.bpf.c
    	$(CLANG) -g -O2 -Wall -target bpf -D__KERNEL__ -D__TARGET_ARCH_$(ARCH) $(INCLUDES) -c $< -o $@
    	$(LLVM_STRIP) -g $@ # Removes debug information
    
    deny_unshare.skel.h: deny_unshare.bpf.o
    	sudo bpftool gen skeleton $< > $@
    
    deny_unshare: deny_unshare.c deny_unshare.skel.h
    	$(CC) -g -Wall -c $< -o $@.o
    	$(CC) -g -o $@ $(LIBS_DIR) $@.o $(LIBS)
    
    .DELETE_ON_ERROR:

在新的終端機視窗中執行：

在另一個終端機視窗中，我們被成功封锁！
    
    
    $ make run
    …
    LSM loaded! ctrl+c to exit.

該原則還有一個額外功能，可以永遠允許權限通過：
    
    
    $ unshare -rU
    unshare: unshare failed: Cannot allocate memory
    $ id
    uid=1000(fred) gid=1000(fred) groups=1000(fred) …

在無權限情况下，syscall 會提前中止。在有權限情况下，會對效能產生什麼影響呢？
    
    
    $ sudo unshare -rU
    # id
    uid=0(root) gid=0(root) groups=0(root)

### 測量效能

我們將使用一行 unshare 來對應使用者命名空間，並在其中執行一個命令進行測量：

透過解析 syscall unshare 進入/結束的 CPU 週期數，我們將以 root 使用者身分進行下列測量：
    
    
    $ unshare -frU --kill-child -- bash -c "exit 0"

  1. 在無原則情况下執行命令
  2. 在有原則情况下執行命令



我們將使用 [ftrace](https://docs.kernel.org/trace/ftrace.html) 來記錄測量值：

此時，我們專門為 unshare 啟用了 syscall 進入和結束追蹤。現在我們設定進入/結束呼叫的時間解析來計算 CPU 週期數：
    
    
    $ sudo su
    # cd /sys/kernel/debug/tracing
    # echo 1 > events/syscalls/sys_enter_unshare/enable ; echo 1 > events/syscalls/sys_exit_unshare/enable

接下來，我們開始進行測量：
    
    
    # echo 'x86-tsc' > trace_clock 

在新的終端機視窗中執行原則，然後執行下一個 syscall：
    
    
    # unshare -frU --kill-child -- bash -c "exit 0" &
    [1] 92014

現在我們對兩個呼叫進行比較：
    
    
    # unshare -frU --kill-child -- bash -c "exit 0" &
    [2] 92019

unshare-92014 使用了 63294 個週期。
    
    
    # cat trace
    # tracer: nop
    #
    # entries-in-buffer/entries-written: 4/4   #P:8
    #
    #                                _-----=> irqs-off
    #                               / _----=> need-resched
    #                              | / _---=> hardirq/softirq
    #                              || / _--=> preempt-depth
    #                              ||| / _-=> migrate-disable
    #                              |||| /     delay
    #           TASK-PID     CPU#  |||||  TIMESTAMP  FUNCTION
    #              | |         |   |||||     |         |
             unshare-92014   [002] ..... 762950852559027: sys_unshare(unshare_flags: 10000000)
             unshare-92014   [002] ..... 762950852622321: sys_unshare -> 0x0
             unshare-92019   [007] ..... 762975980681895: sys_unshare(unshare_flags: 10000000)
             unshare-92019   [007] ..... 762975980752033: sys_unshare -> 0x0
    

unshare-92019 使用了 70138 個週期。

在兩次測量之間有 6844 (~10%) 個週期的差值。結果還不錯！

這些數字是針對單個 syscall 的，並且程式碼呼叫頻率越高，這些數字加起來的總和就會越大。unshare 通常在建立工作時進行呼叫，而不是在程式正常執行期間反覆呼叫。您的使用案例需要仔細考量和測量。

## 結尾

我們瞭解了 LSM BPF 是什麼，如何使用 unshare 將使用者對應至 root，以及如何透過在 eBPF 中實作解決方案來解决實際問題。追蹤適當的勾點並不容易，不僅需要有相關經驗，還需要大量的核心程式碼。所幸，這是最難的部分。因為原則是用 C 語言編寫的，所以我們可以根據我們的問題對原則進行細微地調整。這意味著可以使用允許清單來延伸此原則，以允許某些程式或使用者繼續使用無權限的 unshare。最後，我們瞭解了此程式對效能的影響，發現用於封锁攻擊手段的開支是非常值得的。

「Cannot allocate memory」（無法配置記憶體）不是拒絕權限的明確錯誤訊息。我們提出了一個[修補程式](https://lore.kernel.org/all/20220608150942.776446-1-fred@cloudflare.com/)，來傳播 _cred_prepare_ 中的錯誤碼以連結呼叫堆疊。最終我們得出結論：新勾點更適合解決此問題。敬請期待！

本頁目錄

線上討論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F&t=%E4%BD%BF%E7%94%A8%20eBPF%20Linux%20Security%20Module%20%E5%8D%B3%E6%99%82%E4%BF%AE%E8%A3%9C%20Linux%20%E6%A0%B8%E5%BF%83%E5%85%A7%E7%9A%84%E5%AE%89%E5%85%A8%E6%80%A7%E6%BC%8F%E6%B4%9E)[](https://x.com/intent/post?text=%E4%BD%BF%E7%94%A8+eBPF+Linux+Security+Module+%E5%8D%B3%E6%99%82%E4%BF%AE%E8%A3%9C+Linux+%E6%A0%B8%E5%BF%83%E5%85%A7%E7%9A%84%E5%AE%89%E5%85%A8%E6%80%A7%E6%BC%8F%E6%B4%9E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)[](https://bsky.app/intent/compose?text=%E4%BD%BF%E7%94%A8+eBPF+Linux+Security+Module+%E5%8D%B3%E6%99%82%E4%BF%AE%E8%A3%9C+Linux+%E6%A0%B8%E5%BF%83%E5%85%A7%E7%9A%84%E5%AE%89%E5%85%A8%E6%80%A7%E6%BC%8F%E6%B4%9E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)[](https://mastodonshare.com/?text=%E4%BD%BF%E7%94%A8+eBPF+Linux+Security+Module+%E5%8D%B3%E6%99%82%E4%BF%AE%E8%A3%9C+Linux+%E6%A0%B8%E5%BF%83%E5%85%A7%E7%9A%84%E5%AE%89%E5%85%A8%E6%80%A7%E6%BC%8F%E6%B4%9E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)[](https://www.threads.net/intent/post?text=%E4%BD%BF%E7%94%A8+eBPF+Linux+Security+Module+%E5%8D%B3%E6%99%82%E4%BF%AE%E8%A3%9C+Linux+%E6%A0%B8%E5%BF%83%E5%85%A7%E7%9A%84%E5%AE%89%E5%85%A8%E6%80%A7%E6%BC%8F%E6%B4%9E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-tw%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)

## 相關標籤

[Linux](https://blog.cloudflare.com/zh-tw/tag/linux/)[Programming](https://blog.cloudflare.com/zh-tw/tag/programming/)[安全性](https://blog.cloudflare.com/zh-tw/tag/security/)[深入解讀](https://blog.cloudflare.com/zh-tw/tag/deep-dive/)

追蹤社群媒體

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 訂閱以接收新文章通知

電子郵件

我們絕不會分享您的電子郵件地址。

訂閱

感謝訂閱！請查看收件匣以確認。
