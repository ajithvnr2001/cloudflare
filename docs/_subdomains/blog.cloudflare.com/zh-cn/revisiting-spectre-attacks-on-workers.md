---
url: https://blog.cloudflare.com/zh-cn/revisiting-spectre-attacks-on-workers/
title: \u91cd\u65b0\u5ba1\u89c6\u9488\u5bf9 Cloudflare Workers \u7684\u8fdc\u7a0b Spectre \u653b\u51fb | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:34:48.982973+00:00
---

# 重新审视针对 Cloudflare Workers 的远程 Spectre 攻击 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/revisiting-spectre-attacks-on-workers/

[博客](https://blog.cloudflare.com/zh-cn/)

[Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)[攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)+1再显示 1 个标签

4 个标签显示 4 个标签

  * 文章标签
  * [Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)[攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)[研究](https://blog.cloudflare.com/zh-cn/tag/research/)
  * 全部标签
  * 匹配的标签
  * 未找到标签
  * [1.1.1.1](https://blog.cloudflare.com/zh-cn/tag/1-1-1-1/)
  * [滥用](https://blog.cloudflare.com/zh-cn/tag/abuse/)
  * [Access](https://blog.cloudflare.com/zh-cn/tag/access/)
  * [可访问性](https://blog.cloudflare.com/zh-cn/tag/accessibility/)
  * [收购](https://blog.cloudflare.com/zh-cn/tag/acquisitions/)
  * [高级 DDoS](https://blog.cloudflare.com/zh-cn/tag/advanced-ddos/)
  * [Aegis](https://blog.cloudflare.com/zh-cn/tag/aegis/)
  * [智能体就绪度](https://blog.cloudflare.com/zh-cn/tag/agent-readiness/)
  * [智能体](https://blog.cloudflare.com/zh-cn/tag/agents/)
  * [Agents Week](https://blog.cloudflare.com/zh-cn/tag/agents-week/)
  * [AI](https://blog.cloudflare.com/zh-cn/tag/ai/)
  * [AI 机器人](https://blog.cloudflare.com/zh-cn/tag/ai-bots/)
  * [AI Gateway](https://blog.cloudflare.com/zh-cn/tag/ai-gateway/)
  * [AI Search](https://blog.cloudflare.com/zh-cn/tag/ai-search/)
  * [AI Week](https://blog.cloudflare.com/zh-cn/tag/ai-week/)
  * [AI-SPM](https://blog.cloudflare.com/zh-cn/tag/ai-spm/)
  * [API](https://blog.cloudflare.com/zh-cn/tag/api/)
  * [API 安全](https://blog.cloudflare.com/zh-cn/tag/api-security/)
  * [应用程序安全](https://blog.cloudflare.com/zh-cn/tag/application-security/)
  * [应用程序服务](https://blog.cloudflare.com/zh-cn/tag/application-services/)
  * [攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)
  * [审计日志](https://blog.cloudflare.com/zh-cn/tag/audit-logs/)
  * [自动化](https://blog.cloudflare.com/zh-cn/tag/automation/)
  * [AWS](https://blog.cloudflare.com/zh-cn/tag/aws/)
  * [Beta](https://blog.cloudflare.com/zh-cn/tag/beta/)
  * [更好的互联网](https://blog.cloudflare.com/zh-cn/tag/better-internet/)
  * [BGP](https://blog.cloudflare.com/zh-cn/tag/bgp/)
  * [生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)
  * [Bot Management](https://blog.cloudflare.com/zh-cn/tag/bot-management/)
  * [机器人](https://blog.cloudflare.com/zh-cn/tag/bots/)
  * [Browser Rendering](https://blog.cloudflare.com/zh-cn/tag/browser-rendering/)
  * [Browser Run](https://blog.cloudflare.com/zh-cn/tag/browser-run/)
  * [漏洞悬赏计划](https://blog.cloudflare.com/zh-cn/tag/bug-bounty/)
  * [缓存](https://blog.cloudflare.com/zh-cn/tag/cache/)
  * [缓存清除](https://blog.cloudflare.com/zh-cn/tag/cache-purge/)
  * [Cap'n Proto](https://blog.cloudflare.com/zh-cn/tag/capn-proto/)
  * [CASB](https://blog.cloudflare.com/zh-cn/tag/casb/)
  * [CDN](https://blog.cloudflare.com/zh-cn/tag/cdn/)
  * [证书透明度](https://blog.cloudflare.com/zh-cn/tag/certificate-transparency/)
  * [认证](https://blog.cloudflare.com/zh-cn/tag/certification/)
  * [挑战页面](https://blog.cloudflare.com/zh-cn/tag/challenge-page/)
  * [圣诞节](https://blog.cloudflare.com/zh-cn/tag/christmas/)
  * [Chrome](https://blog.cloudflare.com/zh-cn/tag/chrome/)
  * [CIO Week](https://blog.cloudflare.com/zh-cn/tag/cio-week/)
  * [ClickHouse](https://blog.cloudflare.com/zh-cn/tag/clickhouse/)
  * [免客户端](https://blog.cloudflare.com/zh-cn/tag/clientless/)
  * [Cloud Email Security](https://blog.cloudflare.com/zh-cn/tag/cloud-email-security/)
  * [Cloudflare Access](https://blog.cloudflare.com/zh-cn/tag/cloudflare-access/)
  * [Cloudflare Calls](https://blog.cloudflare.com/zh-cn/tag/cloudflare-calls/)
  * [Cloudflare Email Service](https://blog.cloudflare.com/zh-cn/tag/cloudflare-email-services/)
  * [Cloudflare for Startups](https://blog.cloudflare.com/zh-cn/tag/cloudflare-for-startups/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/zh-cn/tag/gateway/)
  * [Cloudflare Images](https://blog.cloudflare.com/zh-cn/tag/cloudflare-images/)
  * [Cloudflare Media Platform](https://blog.cloudflare.com/zh-cn/tag/cloudflare-media-platform/)
  * [Cloudflare 网络](https://blog.cloudflare.com/zh-cn/tag/cloudflare-network/)
  * [Cloudflare One](https://blog.cloudflare.com/zh-cn/tag/cloudflare-one/)
  * [Cloudflare 页面](https://blog.cloudflare.com/zh-cn/tag/cloudflare-pages/)
  * [Cloudflare Queues](https://blog.cloudflare.com/zh-cn/tag/cloudflare-queues/)
  * [Cloudflare Tunnel](https://blog.cloudflare.com/zh-cn/tag/cloudflare-tunnel/)
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)
  * [Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/zh-cn/tag/cloudflare-zero-trust/)
  * [Cloudforce One](https://blog.cloudflare.com/zh-cn/tag/cloudforce-one/)
  * [橙色警报](https://blog.cloudflare.com/zh-cn/tag/code-orange/)
  * [Coinbase](https://blog.cloudflare.com/zh-cn/tag/coinbase/)
  * [合规性](https://blog.cloudflare.com/zh-cn/tag/compliance/)
  * [Compression](https://blog.cloudflare.com/zh-cn/tag/compression/)
  * [全球连通云](https://blog.cloudflare.com/zh-cn/tag/connectivity-cloud/)
  * [消费者服务](https://blog.cloudflare.com/zh-cn/tag/consumer-services/)
  * [容器](https://blog.cloudflare.com/zh-cn/tag/containers/)
  * [内容独立日](https://blog.cloudflare.com/zh-cn/tag/content-independence-day/)
  * [背景](https://blog.cloudflare.com/zh-cn/tag/context/)
  * [Crawler Hints](https://blog.cloudflare.com/zh-cn/tag/crawler-hints/)
  * [密码学](https://blog.cloudflare.com/zh-cn/tag/cryptography/)
  * [CVE](https://blog.cloudflare.com/zh-cn/tag/cve/)
  * [D1](https://blog.cloudflare.com/zh-cn/tag/d1/)
  * [仪表板](https://blog.cloudflare.com/zh-cn/tag/dashboard-tag/)
  * [数据](https://blog.cloudflare.com/zh-cn/tag/data/)
  * [Data Catalog](https://blog.cloudflare.com/zh-cn/tag/data-catalog/)
  * [数据保护](https://blog.cloudflare.com/zh-cn/tag/data-protection/)
  * [数据库](https://blog.cloudflare.com/zh-cn/tag/database/)
  * [DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)
  * [DDoS 警报](https://blog.cloudflare.com/zh-cn/tag/ddos-alerts/)
  * [DDoS 报告](https://blog.cloudflare.com/zh-cn/tag/ddos-reports/)
  * [深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)
  * [设计](https://blog.cloudflare.com/zh-cn/tag/design/)
  * [开发人员文档](https://blog.cloudflare.com/zh-cn/tag/developer-documentation/)
  * [开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)
  * [Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)
  * [开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)
  * [开发人员存储](https://blog.cloudflare.com/zh-cn/tag/developers-storage/)
  * [DEX](https://blog.cloudflare.com/zh-cn/tag/dex/)
  * [数据丢失防护](https://blog.cloudflare.com/zh-cn/tag/dlp/)
  * [DNS](https://blog.cloudflare.com/zh-cn/tag/dns/)
  * [DNSSEC](https://blog.cloudflare.com/zh-cn/tag/dnssec/)
  * [DoH](https://blog.cloudflare.com/zh-cn/tag/doh/)
  * [Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)
  * [Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)
  * [边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)
  * [电子邮件安全](https://blog.cloudflare.com/zh-cn/tag/email-security/)
  * [Emissions](https://blog.cloudflare.com/zh-cn/tag/emissions/)
  * [加密](https://blog.cloudflare.com/zh-cn/tag/encryption/)
  * [工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)
  * [Forrester](https://blog.cloudflare.com/zh-cn/tag/forrester/)
  * [创始人的信](https://blog.cloudflare.com/zh-cn/tag/founders-letter/)
  * [欺诈](https://blog.cloudflare.com/zh-cn/tag/fraud/)
  * [前端](https://blog.cloudflare.com/zh-cn/tag/front-end/)
  * [全栈](https://blog.cloudflare.com/zh-cn/tag/full-stack/)
  * [普遍可用](https://blog.cloudflare.com/zh-cn/tag/general-availability/)
  * [生成式 AI](https://blog.cloudflare.com/zh-cn/tag/generative-ai/)
  * [Github](https://blog.cloudflare.com/zh-cn/tag/github/)
  * [Go](https://blog.cloudflare.com/zh-cn/tag/go/)
  * [Google Cloud](https://blog.cloudflare.com/zh-cn/tag/google-cloud/)
  * [HTTP3](https://blog.cloudflare.com/zh-cn/tag/http3/)
  * [Hyperdrive](https://blog.cloudflare.com/zh-cn/tag/hyperdrive/)
  * [身份](https://blog.cloudflare.com/zh-cn/tag/identity/)
  * [IETF](https://blog.cloudflare.com/zh-cn/tag/ietf/)
  * [图像优化](https://blog.cloudflare.com/zh-cn/tag/image-optimization/)
  * [图像大小调整](https://blog.cloudflare.com/zh-cn/tag/image-resizing/)
  * [图像存储](https://blog.cloudflare.com/zh-cn/tag/image-storage/)
  * [影响](https://blog.cloudflare.com/zh-cn/tag/impact/)
  * [事件响应](https://blog.cloudflare.com/zh-cn/tag/incident-response/)
  * [基础设施](https://blog.cloudflare.com/zh-cn/tag/infrastructure/)
  * [Intel](https://blog.cloudflare.com/zh-cn/tag/intel/)
  * [Interconnection](https://blog.cloudflare.com/zh-cn/tag/interconnection/)
  * [互联网性能](https://blog.cloudflare.com/zh-cn/tag/internet-performance/)
  * [互联网质量](https://blog.cloudflare.com/zh-cn/tag/internet-quality/)
  * [互联网中断](https://blog.cloudflare.com/zh-cn/tag/internet-shutdown/)
  * [互联网流量](https://blog.cloudflare.com/zh-cn/tag/internet-traffic/)
  * [互联网趋势](https://blog.cloudflare.com/zh-cn/tag/internet-trends/)
  * [IPsec](https://blog.cloudflare.com/zh-cn/tag/ipsec/)
  * [IPv6](https://blog.cloudflare.com/zh-cn/tag/ipv6/)
  * [JavaScript](https://blog.cloudflare.com/zh-cn/tag/javascript/)
  * [内核](https://blog.cloudflare.com/zh-cn/tag/kernel/)
  * [键值](https://blog.cloudflare.com/zh-cn/tag/key-value/)
  * [KeyTrap](https://blog.cloudflare.com/zh-cn/tag/keytrap/)
  * [LangChain](https://blog.cloudflare.com/zh-cn/tag/langchain/)
  * [拉丁美洲](https://blog.cloudflare.com/zh-cn/tag/latin-america/)
  * [法律问题](https://blog.cloudflare.com/zh-cn/tag/legal/)
  * [Cloudflare 人生](https://blog.cloudflare.com/zh-cn/tag/life-at-cloudflare/)
  * [Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)
  * [实时串流](https://blog.cloudflare.com/zh-cn/tag/live-streaming/)
  * [LLM](https://blog.cloudflare.com/zh-cn/tag/llm/)
  * [恶意 JavaScript](https://blog.cloudflare.com/zh-cn/tag/malicious-javascript/)
  * [MASQUE](https://blog.cloudflare.com/zh-cn/tag/masque/)
  * [MCP](https://blog.cloudflare.com/zh-cn/tag/mcp/)
  * [Microsoft Azure](https://blog.cloudflare.com/zh-cn/tag/microsoft-azure/)
  * [Mirai](https://blog.cloudflare.com/zh-cn/tag/mirai/)
  * [移动](https://blog.cloudflare.com/zh-cn/tag/mobile/)
  * [模型上下文协议、](https://blog.cloudflare.com/zh-cn/tag/model-context-protocol/)
  * [监控](https://blog.cloudflare.com/zh-cn/tag/monitoring/)
  * [MySQL](https://blog.cloudflare.com/zh-cn/tag/mysql/)
  * [网络](https://blog.cloudflare.com/zh-cn/tag/network/)
  * [网络服务](https://blog.cloudflare.com/zh-cn/tag/network-services/)
  * [元旦](https://blog.cloudflare.com/zh-cn/tag/new-year/)
  * [NGINX](https://blog.cloudflare.com/zh-cn/tag/nginx/)
  * [NIST](https://blog.cloudflare.com/zh-cn/tag/nist/)
  * [Node.js](https://blog.cloudflare.com/zh-cn/tag/node-js/)
  * [Notebooks](https://blog.cloudflare.com/zh-cn/tag/notebooks/)
  * [OAuth](https://blog.cloudflare.com/zh-cn/tag/oauth/)
  * [开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)
  * [优化](https://blog.cloudflare.com/zh-cn/tag/optimization/)
  * [中断](https://blog.cloudflare.com/zh-cn/tag/outage/)
  * [合作伙伴](https://blog.cloudflare.com/zh-cn/tag/partners/)
  * [合作关系](https://blog.cloudflare.com/zh-cn/tag/partnerships/)
  * [密码](https://blog.cloudflare.com/zh-cn/tag/passwords/)
  * [按抓取付费](https://blog.cloudflare.com/zh-cn/tag/pay-per-crawl/)
  * [对等互连](https://blog.cloudflare.com/zh-cn/tag/peering/)
  * [性能](https://blog.cloudflare.com/zh-cn/tag/performance/)
  * [网络钓鱼](https://blog.cloudflare.com/zh-cn/tag/phishing/)
  * [Pipelines](https://blog.cloudflare.com/zh-cn/tag/pipelines/)
  * [政策与法律](https://blog.cloudflare.com/zh-cn/tag/policy/)
  * [事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)
  * [后量子](https://blog.cloudflare.com/zh-cn/tag/post-quantum/)
  * [隐私](https://blog.cloudflare.com/zh-cn/tag/privacy/)
  * [Privacy Pass](https://blog.cloudflare.com/zh-cn/tag/privacy-pass/)
  * [产品设计](https://blog.cloudflare.com/zh-cn/tag/product-design/)
  * [产品新闻](https://blog.cloudflare.com/zh-cn/tag/product-news/)
  * [Project Galileo](https://blog.cloudflare.com/zh-cn/tag/project-galileo/)
  * [Prometheus](https://blog.cloudflare.com/zh-cn/tag/prometheus/)
  * [公共部门](https://blog.cloudflare.com/zh-cn/tag/public-sector/)
  * [Python](https://blog.cloudflare.com/zh-cn/tag/python/)
  * [队列](https://blog.cloudflare.com/zh-cn/tag/queues/)
  * [QUIC](https://blog.cloudflare.com/zh-cn/tag/quic/)
  * [Quicksilver](https://blog.cloudflare.com/zh-cn/tag/quicksilver/)
  * [R2](https://blog.cloudflare.com/zh-cn/tag/r2/)
  * [R2 Super Slurper](https://blog.cloudflare.com/zh-cn/tag/r2-super-slurper/)
  * [Radar](https://blog.cloudflare.com/zh-cn/tag/cloudflare-radar/)
  * [勒索攻击](https://blog.cloudflare.com/zh-cn/tag/ransom-attacks/)
  * [实时](https://blog.cloudflare.com/zh-cn/tag/real-time/)
  * [可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)
  * [远程桌面协议 ](https://blog.cloudflare.com/zh-cn/tag/remote-desktop-protocol/)
  * [远程工作](https://blog.cloudflare.com/zh-cn/tag/remote-work/)
  * [研究](https://blog.cloudflare.com/zh-cn/tag/research/)
  * [解析器](https://blog.cloudflare.com/zh-cn/tag/resolver/)
  * [风险管理](https://blog.cloudflare.com/zh-cn/tag/risk-management/)
  * [路由](https://blog.cloudflare.com/zh-cn/tag/routing/)
  * [路由安全](https://blog.cloudflare.com/zh-cn/tag/routing-security/)
  * [RPKI](https://blog.cloudflare.com/zh-cn/tag/rpki/)
  * [Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)
  * [Rust Workers](https://blog.cloudflare.com/zh-cn/tag/rust-workers/)
  * [SaaS](https://blog.cloudflare.com/zh-cn/tag/saas/)
  * [SaaS 安全](https://blog.cloudflare.com/zh-cn/tag/saas-security/)
  * [沙盒](https://blog.cloudflare.com/zh-cn/tag/sandbox/)
  * [SASE](https://blog.cloudflare.com/zh-cn/tag/sase/)
  * [SDK](https://blog.cloudflare.com/zh-cn/tag/sdk/)
  * [安全 Web 网关（SWG）](https://blog.cloudflare.com/zh-cn/tag/secure-web-gateway/)
  * [安全](https://blog.cloudflare.com/zh-cn/tag/security/)
  * [安全中心](https://blog.cloudflare.com/zh-cn/tag/security-center/)
  * [安全态势管理](https://blog.cloudflare.com/zh-cn/tag/security-posture-management/)
  * [Security Week](https://blog.cloudflare.com/zh-cn/tag/security-week/)
  * [无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)
  * [服务器](https://blog.cloudflare.com/zh-cn/tag/servers/)
  * [速度](https://blog.cloudflare.com/zh-cn/tag/speed/)
  * [速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)
  * [SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)
  * [标准](https://blog.cloudflare.com/zh-cn/tag/standards/)
  * [存储](https://blog.cloudflare.com/zh-cn/tag/storage/)
  * [TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)
  * [团队](https://blog.cloudflare.com/zh-cn/tag/team/)
  * [威胁情报](https://blog.cloudflare.com/zh-cn/tag/threat-intelligence/)
  * [威胁运营](https://blog.cloudflare.com/zh-cn/tag/threat-operations/)
  * [威胁](https://blog.cloudflare.com/zh-cn/tag/threats/)
  * [TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)
  * [流量](https://blog.cloudflare.com/zh-cn/tag/traffic/)
  * [透明度](https://blog.cloudflare.com/zh-cn/tag/transparency/)
  * [趋势](https://blog.cloudflare.com/zh-cn/tag/trends/)
  * [信任与安全](https://blog.cloudflare.com/zh-cn/tag/trust-and-safety/)
  * [TURN 服务器](https://blog.cloudflare.com/zh-cn/tag/turn-server/)
  * [Turnstile](https://blog.cloudflare.com/zh-cn/tag/turnstile/)
  * [用户研究](https://blog.cloudflare.com/zh-cn/tag/user-research/)
  * [VDI](https://blog.cloudflare.com/zh-cn/tag/vdi/)
  * [视频](https://blog.cloudflare.com/zh-cn/tag/video/)
  * [漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)
  * [WAF](https://blog.cloudflare.com/zh-cn/tag/waf/)
  * [WARP](https://blog.cloudflare.com/zh-cn/tag/warp/)
  * [WASM](https://blog.cloudflare.com/zh-cn/tag/wasm/)
  * [Web 应用防火墙](https://blog.cloudflare.com/zh-cn/tag/web-application-firewall/)
  * [WebAssembly](https://blog.cloudflare.com/zh-cn/tag/webassembly/)
  * [WebRTC](https://blog.cloudflare.com/zh-cn/tag/webrtc/)
  * [Workers AI](https://blog.cloudflare.com/zh-cn/tag/workers-ai/)
  * [Workers Launchpad](https://blog.cloudflare.com/zh-cn/tag/workers-launchpad/)
  * [Workers VPC](https://blog.cloudflare.com/zh-cn/tag/workers-vpc/)
  * [Workflows](https://blog.cloudflare.com/zh-cn/tag/workflows/)
  * [Wrangler](https://blog.cloudflare.com/zh-cn/tag/wrangler/)
  * [x402](https://blog.cloudflare.com/zh-cn/tag/x402/)
  * [年度回顾](https://blog.cloudflare.com/zh-cn/tag/year-in-review/)
  * [Zero Trust](https://blog.cloudflare.com/zh-cn/tag/zero-trust/)



[研究](https://blog.cloudflare.com/zh-cn/tag/research/)

[Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)[攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)[研究](https://blog.cloudflare.com/zh-cn/tag/research/)

2026年9月9日

# 重新审视针对 Cloudflare Workers 的远程 Spectre 攻击

![Martin Schwarzl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q44FVCNYF3AKGF6DGP9G.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Albert Pedersen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46X1RPT45576XPREMG1CQ3.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Martin Schwarzl](https://blog.cloudflare.com/zh-cn/author/martin/)和[Albert Pedersen](https://blog.cloudflare.com/zh-cn/author/albert-pedersen/)

阅读时间：14 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/revisiting-spectre-attacks-on-workers/)和[繁體中文](https://blog.cloudflare.com/zh-tw/revisiting-spectre-attacks-on-workers/).

![](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZC7473CXRW6EF1Z69ZW.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAIQAeJwAcMQAcNwAoNwA1MgA5KQAxIQAdKQAaNgAoTDFAWURSW0hbUz5XQyhGMgApLwAUQhsyX01VcWVsdGlzaV1rVUNUPxsyMwAPSCQ1Z1ddenF1fnZ8c2lyXU1ZRCM2MwAPRiEyY1NXdmxteXFzb2RqWklSQiAyMQASPxIpVkFFZVdXaFxbYFFTTzlBOhEpLQAVNQAcRCUqTzczUjs2TDQyQCApMAAdLAAWMAAWOg4VQyEWRiUYQh4ZOAkYKwAX)

2021 年，我们评估了针对 Cloudflare Workers 的[ _远程 Spectre 攻击_](https://blog.cloudflare.com/spectre-research-with-tu-graz/)，并基于评估结果在生产环境中部署了名为[ _动态进程隔离_](https://blog.cloudflare.com/spectre-research-with-tu-graz/)（Dynamic Process Isolation，DyPrIs）的防御机制——该机制能够识别行为可疑的脚本，并将其隔离至独立进程。此后，用于稳定 Spectre 攻击的新技术不断涌现。为评估这些技术是否对 Workers 生产环境构成威胁，我们决定在内部对远程 Spectre 攻击进行重新评估。通过在生产环境中构建更新版的概念验证，我们能够在实际生产负载下对 Spectre 攻击风险进行实证评估。

在生产环境中发动成功的侧信道攻击，外部攻击者还需克服额外障碍，包括共享硬件资源上的活动、中断、上下文切换以及粗粒度计时器等。我们的研究发现了 DyPrIs 实现中的一处缺陷，并成功在 Cloudflare Workers 生产环境中演示了一次远程 Spectre 攻击，可靠地以 99% 的准确率泄露最高达 12 bit/s 的数据。基于这项研究，我们改进了 DyPrIs，集成了 V8 Sandbox 和[ _进程内隔离机制_](https://blog.cloudflare.com/safe-in-the-sandbox-security-hardening-for-cloudflare-workers/)，以进一步降低内存泄露攻击的风险。

今天，我们[ _发表了一篇论文_](https://arxiv.org/pdf/2608.17043)，详细描述了上述研究发现，论文由 Albert Pedersen、Haocheng Xiao、Sam Ainsworth、Nigel Topham 和 Martin Schwarzl 共同撰写，涵盖 2024 年至 2025 年初的研究工作。

请注意，由于 Cloudflare Workers Runtime 团队已部署相应对策，文中所描述的攻击在生产系统中已得到缓解。过去三年间，我们未发现任何主动利用的迹象。

## **Cloudflare Workers 安全模型**

Cloudflare Workers 在边缘节点上运行不受信任的 JavaScript 代码。借助 V8 隔离区提供的语言层隔离，数以万计的租户可共享同一操作系统进程。每个 Worker 拥有各自独立的 JavaScript 堆。这一设计既能降低启动延迟，又能相比完整进程隔离方案更高效地运行大量租户。在运行时层面，我们部署了多层防御机制，例如自动化 V8 补丁管道、由 Linux 命名空间和 seccomp 过滤器构成的双层沙箱、Cap'n Proto RPC，以及将特定脚本调度至独立进程沙箱的功 能。尽管如此，Worker 进程内的单个任意读取漏洞仍然 可能导致跨租户数据泄露。其中一种漏洞非常难以缓解，它利用了推测执行的特性，即进程内 **Spectre** 漏洞。

## Spectre

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA1t3TzdfRssfOi7XRb63ZgLbgrMnfz9naz9jMxNHJpb/Dd6rDVKLJba3Qn8HRxNPOydXGvc3Cmrm5ZaK1Opm4XaW+lLvCuczBy9fHv8/Dnbu4bKWxTZ2xaam2l7y7t8u81t/RzNjNr8bEjLW8e6+6jLi+qcbCwNHE5ung3eTdxtbVr8rPpcbNr8vQwdTS0NvT8vLs6+7p2ePjx9rfwdfeyNvf1ODg3eTg9/bx8PLu4Ojp0ODly97k0eHm2+Xm4ufl)![BLOG-3371 2.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZ9V2EAMVDZNCTAT5G4G.png&w=715&h=358&f=webp&fit=cover&position=center)

推测执行的原理可以用登山来类比。在某个路口，您需要预判前行方向。若预判正确，您节省了时间，可以在山间小屋享受阳光和冷饮。然而，若预判方向错误，您不得不折返。山路看起来完好如初，但您的脚印仍留在泥土里。

CPU 的推测执行与此类似。分支预测（branch prediction）会提前对分支结果作出预判，CPU 随即推测性地执行该分支。若预测正确，推测执行节省了时间；若预测错误，CPU 则需丢弃结果、回滚并执行另一分支。由于这些推测执行的指令仅在 CPU 流水线中短暂存在，从未被永久退休或提交，学术界将其称为瞬态指令（transient instructions），并将该概念概括为瞬态执行（transient execution）。

然而，瞬态执行仍会在微架构状态中留下痕迹，例如残留在 CPU 缓存中的数据。因此，攻击者可利用 Spectre 以瞬态方式越界访问内存，将单个比特的信息编码至缓存状态，并通过测量重新访问数据的延迟来推断该比特是否被置位。

为[ _缓解进程内 Spectre 攻击_](https://blog.cloudflare.com/spectre-research-with-tu-graz/)，Cloudflare Workers 冻结本地计时器，禁止多线程和共享内存，并主动检测可疑脚本、定期对内存进行随机化，同时将行为可疑的脚本隔离至独立进程。

## **攻击原语**

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA9fj/8/X97u706+rv6ezv6O7x5Ovu3+To+vz/9/f+8O/06+vv7O7x7fH06u/y5Ojr/////Pz/8vH27e3w8PHz9Pf48fX26e3v////////9/b68fHz9fb3+fz89/r78PPz/////////fz/9/f4+fz7/f///P/+9vj3/////////////f7+/P///v///v//+vz6/////////////////v///v///v///f78/////////////////////v///v///v/9)![BLOG-3371 3.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYBPHGE9QQXKZPXBAR7G.png&w=715&h=518&f=webp&fit=cover&position=center)

远程 Spectre 攻击高层概览示意图。攻击者需要一个远程计时器，用于测量探测瞬态泄露比特为"0"还是"1"所需的时间。

Cloudflare Workers 平台有意[ _限制计时器_](https://blog.cloudflare.com/mitigating-spectre-and-other-security-threats-the-cloudflare-workers-security-model/)的精度。在仅使用 CPU 执行期间，时间实际上处于冻结状态：`[Date.now](http://Date.now)()` 和 `[performance.now](http://performance.now)()` 无法提供持续推进的高精度时钟。由于没有共享内存且不支持多线程，经典的基于 `SharedArrayBuffer` 的计数线程计时器也无从使用。

要成功发动攻击，需要克服几个挑战：首先，Workers 运行时间有限，必须确保攻击者与受害者位于同一位置；其次，必须找到一个可靠的、理想情况下位于同一位置的远程计时器，以进行稳定的计时测量；其三，攻击在生产条件下运行，因此还需要额外的稳定性措施，例如可靠的 Spectre gadget 以实现瞬态 64 位越界访问、应对系统和网络噪声的稳健信号放大机制，以及可靠地将数据从缓存中驱逐的原语。

### Spectre gadget
    
    
    return probeArray[
              obj instanceof ObjP
                ? PROBEARRAY_OFFSET + ((obj.ptr[0] >> bit) & 1) * 0x800
                : 0x400
    ];

_推测类型混淆 Spectre gadget_

借助正确的 Spectre gadget（如上方代码片段所示），攻击者可以瞬态方式越界访问内存，并将单个比特编码至缓存 (`probeArray`) 中。攻击者随后测量内存访问延迟，以确认数据是否已被缓存：访问较快意味着该缓存行已缓存，对应比特为 1；访问较慢则意味着未缓存，对应比特为 0。

在我们的攻击中，使用了两种不同类型的 Spectre gadget。第一种用于泄露压缩堆指针，例如隔离区的堆基地址（根地址）；第二种则利用推测类型混淆，从攻击者精心构造的用户空间 64 位指针处读取数据。在开展研究时，V8 Sandbox 尚未在 Cloudflare Workers 上实现。在指针压缩模式下，大多数对象使用 32 位压缩指针，而 `TypedArray` 是少数仍存储原始 64 位指向其后备存储的指针的例外——这正是我们的 gadget 所利用的。

分支 `obj instanceof ObjP `执行类型检查，即一次分支操作。为误训分支预测，我们多次以真实的 `ObjP` 实例调用该 gadget，然后以具有攻击者控制内存布局的不同对象 `ObjI` 调用它。CPU 随即推测性地执行该分支，从 `obj.ptr[0]` 读取数据，尽管该对象实际上是不同类型。为泄露单个比特，我们屏蔽出一个比特位，并用其选择 `probeArray` 中的两个缓存行之一，该缓存行是否被缓存即编码了该比特。

利用堆泄露 gadget，我们映射相邻对象并定位一个攻击者控制的数组。第二个 gadget 混淆两个跨越多个缓存行的大型对象，使类型字段落在与被读取字段不同的缓存行上。驱逐类型字段可打开推测窗口，同时目标字段保持缓存状态，瞬态读取随即跟随攻击者控制的 64 位值，从而将泄露转化为任意地址读取。该技术的更详细描述可参见论文原文。

**本地演示：泄露任意 64 位地址。**

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9vf28vPy9vb2+vn59vb27u7u////////9/f38/Pz9vb2+vr69/f37+/v////////+fn59PT19/f4+/v7+fn58fHx////////+/v79/f3+vr6/v7++/z79PT0////////////+/r7/v7+////////9/f3/////////////v7+////////////+/v7/////////////////////////////f39/////////////////////////////v7+)![BLOG-3371 4.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYVFV4YVB03F4Y2GE0N8.png&w=715&h=715&f=webp&fit=cover&position=center)

推测类型混淆 gadget 内存布局示意图。精心构造的伪造 typed-array 头部使瞬态读取跟随攻击者选定的指针。

### **信号放大**

缓存命中与缓存未命中之间仅相差数纳秒，而远程计时器的噪声量级则在数微秒至数毫秒之间。因此，需要某种形式的信号放大才能区分缓存命中与未命中。Stephen Röttger 和 Artur Janc 发现了一种[ _放大单次内存访问_](https://security.googleblog.com/2021/03/a-spectre-proof-of-concept-for-spectre.html)的方法，其原理是利用 L1 缓存中基于树的伪最近最少使用（PLRU）缓存替换策略。基于树的 PLRU 将每个缓存组织为一棵二叉树，树节点指向最近最少使用的一侧，CPU 通过沿指针方向驱逐数据。利用特定的访问模式，攻击者可以在指针转向目标时持续触及其树邻居，从而使目标缓存行无限期保持缓存状态。这一思路颇为精妙：借助该行为，单次缓存事件的时序差异可被任意放大——与反向情形（大量 L1 未命中）相比，正向情形将产生大量 L1 命中（访问更快）。

下图展示了内存地址 X 是否处于缓存状态的两种情况。若未缓存，该访问模式将产生大量缓存命中；若已缓存，它占据树中的一个节点，导致四条缓存行竞争三个节点，从而引发大量 L1 未命中。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA8O/w7Ozr5uXj4uHf5OPi5uTl4uDh29nY9PP38fDy7Ovp6enl6urp6+rs6Obo4d/e+/r/+ff79PTy8vLu8vPy8/P27+7x6ufn/////////f37+/v3/P38/Pz/+fj78/Hx////////////////////////////+/r5////////////////////////////////////////////////////////////////////////////////////////////////)![BLOG-3371 5.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYH1JF2CTZE4EHYCH0K9.png&w=715&h=299&f=webp&fit=cover&position=center)

用于放大单次缓存事件（命中/未命中）的 PLRU 访问模式示意图。

### **远程计时器**

只要信号能够被放大，嘈杂的远程计时器便足以区分编码的比特。例如，连接到提供高精度时间戳的外部服务器的 WebSocket 连接即可满足需求。该计时器可托管于 Cloudflare，或部署于与运行 Worker 的目标数据中心共同部署的数据中心。Worker 请求远程计时器为某一事件标记时间戳，并在事件结束后计算另一请求的时间差。

在论文中，我们评估了多种不同的计时器配置，即便在较大的拓扑距离下，仅凭少量样本便能稳定地实现中位数亚毫秒级精度。下图展示了使用基于树的 PLRU 放大后的缓存事件。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////Pv98fDy6+rs7+7w9fT18/Ly7Orq////////9vX38vDy9vX2+/r7+fj48fDv/////////Pv9+Pf5/Pv9/////v399vX0//////////7/+/r8//7/////////+Pf3/////////v3/+vn7/v3///////7+9/b1////////+fj79vX3+vn6/v3+/Pv69PPy/////v3/9fT28fDy9fT1+vn59/b28O7t/////Pv98/L07+7w8/Lz+Pf39fT07u3s)![BLOG-3371 6.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYD0RQPYBADGE8CXEVZ5.png&w=715&h=457&f=webp&fit=cover&position=center)

50 次放大缓存命中（实线）与缓存未命中（虚线）计时测量的核密度估计图。上：网络计时器，因抖动存在重叠；下：真实值，显示清晰分离。竖线标记各自中位数。

### **可重复测量**

单次测量不足以可靠地区分时序编码数据。生产机器噪声较大，因此攻击者需要对每次测量至少重复若干次，并使用某种统计判别器。在我们的方案中，重复测量意味着每轮重置缓存状态。每轮开始前需驱逐两类数据：推测分支所依赖的值必须被驱逐，使分支解析停顿足够长的时间以打开推测窗口；编码泄露比特的探测缓存行也必须被驱逐，以便下一次瞬态访问能够重新将其缓存。

由于 JavaScript 中没有直接可用的驱逐指令，经典方法是构建驱逐集（eviction set）——一组映射到与目标相同缓存组的地址集合。以正确的模式访问这些地址可将目标从缓存中驱逐。Stephen Röttger 和 Artur Janc 在其攻击中使用驱逐列表，可靠地将数据至少驱逐至 L2 缓存。这种方法有效，但代价较高：构建精确的驱逐集需要大量时序测量，而我们的计时器是一个嘈杂的远程计时器。此前针对 Workers 的远程攻击绕过了这一搜索过程，改为在每轮中遍历一个大于 L1 和 L2 缓存之和的数组——这是一种可行方案，但速度更慢。

Dougall Johnson 在其关于[ _可移植 JavaScript Spectre 利用_](https://dougallj.wordpress.com/2021/03/16/another-approach-to-portable-javascript-spectre-exploitation/)的精彩博文中介绍了一种更优雅的方式，其思路直接源自鸽巢原理。若分配的数据量远超缓存容量，随机选取的缓存行几乎可以确定不在缓存中。对于 256 KB 的 L2 缓存，分配 64 MB 数据后，随机缓存行仍处于 L2 缓存的概率最多为 1/256。因此，无需驱逐特定缓存行，只需选取一个以压倒性概率已被驱逐的全新随机位置即可。频繁循环遍历该对象数组的副作用是产生自动驱逐效果。

为在 JavaScript 中利用这一特性，我们分配了一个超过末级缓存容量的攻击者-受害者对象对大型池。每轮测量选取一个全新的随机对，该对象的 map 指针——即推测类型检查所读取的隐藏类描述符——因此几乎可以确定已被驱逐。

### **实现攻击者与受害者隔离区位于同一位置**

要使攻击奏效，攻击者与受害者的隔离区必须被调度在同一边缘服务器的同一进程中。直觉上，这似乎并不容易——毕竟 Cloudflare 运营着数以万计的边缘服务器。然但实际上在 Cloudflare Workers 上实现二者共位相当简单。 由于 Cloudflare Workers 设计为可在任意 Cloudflare 边缘服务器上执行，在攻击者脚本中通过 `fetch("https://victim.example")` 调用受害者脚本，在大多数情况下会促使调度器在完全相同的进程中启动受害者 Worker 的实例。通过以固定时间间隔持续向受害者发送 子请求，可保持受害者隔离区持续存活。

此外，由于攻击稳定性在很大程度上取决于运行 Worker 脚本的边缘服务器的 CPU 负载，攻击者可以策略性地选择在非高 峰时段的托管数据中心发动攻击（例如在欧洲工作时间选择澳大利亚的数据中心），此时流量水平相对较低。

### **突破隔离区资源限制**

Cloudflare Workers 运行时对所有隔离区[ _强制执行一组限制_](https://developers.cloudflare.com/workers/platform/limits/)，以保护平台并防止滥用。就本次攻击而言，相关限制为每次调用 30 秒 CPU 时间和 1,000 次子请求。这些限制此后已[ _提高_](https://developers.cloudflare.com/workers/platform/limits/#account-plan-limits)，但以下原则仍然适用。

对于普通 Worker，每个 HTTP 请求（即 fetch 事件）都是一次新调用，会重置上述限制。难点在于如何让连续请求落在同一边缘服务器上——负载平衡和网络状况的变化使这一点难以保证。Durable Objects 为我们解决了这一问题。

[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/) 专为客户端间的实时协调而构建，运行时将每条传入的 WebSocket 消息视为一次新调用并重置 CPU 时间和请求限制。攻击者向一个 Durable Object Worker 建立持久 WebSocket 连接，并定期发送保活消息。这使单个隔离区持续存活，并为我们提供了一个持久的双向通道来执行攻击。

其中有一个细节耗费了我们不少时间。由于隔离区是单线程的，传入的 WebSocket 消息只有在脚本将控制权交还给事件循环时才会被处理。在同步代码执行期间，运行时不会感知到保活消息，因此不会重置 CPU 时间。若线程持续阻塞超过 30 秒，运行时将终止隔离区。这为单次同步执行突发中的放大量设定了上限。在各次突发之间定期让出控制权，使我们能够将隔离区保持存活长达 5 小时至 20 余小时。

### **综合运用**

此前的攻击主要依靠重复来放大单次缓存访问，因此泄露速率较低，约为 120 比特/小时。我们将基于树的 PLRU 放大机制与测量循环相结合：每次迭代重建缓存状态，从而累积更大的时序差异。即便某次迭代中中断破坏了缓存状态，后续迭代也能将其抵消。这使信号强度足以通过远程 WebSocket 计时器对比特进行分类。总体思路如下：
    
    
    for (let s = 0; s < SAMPLE_NUM; s++) {
      timer.mark("mark S" + s);
      for (let r = 0; r < OUTER_REP_NUM; r++) {
        setup();                   // branch mistraining and cache control
        leak(secretBit);           // transient access
        PLRU(cacheSet, INNER_REP); // amplify
      }
      timer.mark("mark E" + s);
    }
    
    delta = fetchFromServer(SAMPLE_NUM);
    return median(delta);

我们在 Cloudflare Workers 生产环境中，针对我们自己控制的 Worker，完整演示了端到端攻击。我们首先从攻击者 Worker 泄露内存，继而从一个共同部署的受害者 Worker（我们事先在其中放置了秘密数据）中泄露数据。

第一步，在攻击者 Worker、我们拥有的受害者 Worker 和远程计时器之间建立共同部署关系。Durable Objects 为我们提供了长期执行上下文，WebSocket 消息提供了可重复的时序来源，`/cdn-cgi/trace` 端点通过查看 _fl_ 字段帮助我们确认机器部署位置。

第二步，增加校准步骤，以推测可达的值探测计时器。这一步骤至关重要，因为生产机器噪声较大。逐次调用的校准使我们能够根据 0 分布和 1 分布之间的相对差异对比特进行分类，最终应产生两个可清晰区分的分布。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA8Pn76Ors0sTJuqm2sLPGus7gzdzp3dzh/f//9/j55tzf1MfQzM3Y0d/p3urw6urs////////+vP17eTp5ubq6PHz7/j49/j2////////////+/X39vb29/z6+v/9/v/8/////////////Pj6+fn5+//8/f/9/f/7/////////fv89PHz8/T19/z7+f379vf1////////8/Hz6Obp6uzv8fb48/f37+7u////////7uzu4+Hl5ejs7fP28PT26+vr)![BLOG-3371 7.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZ90GQ2H0H3WEJBQWGRH.png&w=715&h=387&f=webp&fit=cover&position=center)

第一阶段，我们从一个 Worker 泄露了隔离区根地址；在另一个 Worker 中，我们使用基于 64 位指针的推测类型混淆，从该根地址处读取数据。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAUk5OT0pDR0AsPzgsOTlINTtaMDdXKSxDTUg7S0QzRTshPzQgOjU1NjZBLzA9JiMpS0QkSUAhRTkZQTQWPzQZOzQZMy0LJx4AT0gkTkUkSj4jSDsgRzwaRDwNPTYAMigAWlRBWFE+VEs4Ukg3UUs8UEw+SkY4QjwrZ2JdZF9WX1hKW1ZLW1lZWltjV1dfUE5PcGxvbWlnZ2JXYl9YYmNsYmZ6X2N3W1pkdHB2cW1tamZbZWNdZGZyZWqCYmd/Xl9r)![BLOG-3371 8.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZB18F736T5D947HE7MH.png&w=715&h=314&f=webp&fit=cover&position=center)

作为中间验证步骤，我们通过读取 vDSO 区域的内存确认了第二个 gadget 的 64 位泄露能力。vDSO 是一个便于验证的目标，因为其中包含 `gettimeofday` 等人类可读字符串。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAUEcvTkYwSkMwRkEuRD8rRD8nRD4mQz4oVEs1Ukk1TUc1SUQyR0IuRkAqRT8oQz0oV046VU05UEk4S0Y1SUMwR0ErRT8oQjwmWU87Vk46UUk4S0UzSEEuRj8oQzwkQDkiV003VUs2TkYzSEAtRD0mQjogQDcbPDQZVEkwUUYuSkApQjkhPjUYPTIPOjAJNy0JUEQnTUElRToePTISOC0ANysANikAMycAT0IjTD8gQzcYOi8HNioANSgANCYAMSQA)![BLOG-3371 9.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYNA1R7KHD1CH00PM79K.png&w=715&h=243&f=webp&fit=cover&position=center)

**演示视频：从 JavaScript 堆泄露数据**

最终，我们在受害者 Worker 中放置了一个 JWT 令牌，并逐比特泄露。第一个字节为字符"e"，二进制表示为 0b01100101。下图展示了该字节的逐比特分类结果。分类过程使用双侧检验同时测试两种结果，并通过多数投票和基于百分位的阈值推断比特值。在生产环境中，我们实现了最高 12 bit/s 的泄露速率，准确率超过 99%。需要注意的是，更高的泄露速率以牺牲准确率为代价。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+/Pz57+7v6Ojr7e3u8/T08vPy6urq///////+8/P17e3x8vL1+Pj59vb27e3t////////+Pf78vL39/f7/f3++vr67+/x////////+/v/9vb7+/v//////f398vLz/////////Pz/9vf7+/v//////f3+8/P0////////+vv99fX5+fn8//7//fz89PT0////////+fn68vP19vb4/Pz8+/v69PT0////////+Pj58fH09fX2+/v6+/r59PT0)![BLOG-3371 10.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYQR705ERGSYCX6WAN2W.png&w=715&h=1031&f=webp&fit=cover&position=center)

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vv9+fb47+zu6ejp7Ovs8O/w7ezt5OXk//////3+9fT18PDw8vL09fb58/T26+3t/////////fz79/f3+Pr9+/7/+fz/8vb1///////////++/v7/P7//v///P//9vn5///////////9+vr5+/3//////P//9Pf3////////+/r59fTz+Pj6/P3/+fr97vDw////////9vT07+7s9PLz+vj79fT36Ojp////////9PLy7evq8vDw+fb48/L05eXm)![BLOG-3371 11.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZZAYKH16KKVQNSEYH7JX.png&w=715&h=397&f=webp&fit=cover&position=center)

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAQkIvQEEvPD0vNjgrLzAhJiYPGBgAAAMANDEbMC4ZKCYUHxwGGRQAFQ0ACQAAAAAAKR8AIxgAEwAAAAAAAAAABwAACAAAAAAANysCMyYAKhoAIgsAIAUAIwgAIQUAHAAAU0krUUcrTkQrSj8mRjkbQTMFOysANSMAbGRFbGRIbGNLaWBKYllBWU4yT0IiSDkYfnVWfnZZf3defHVddWxUaV9EXVA0U0YphHxbhX1fhn5kg3xke3Nbb2RKYVU5WEou)![BLOG-3371 12.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYH6CEXJ9WFY642FH4X9.png&w=715&h=74&f=webp&fit=cover&position=center)

逐比特分类结果图及完整泄露令牌截图

### **鲁棒性**

随着一天中时段的不同，机器利用率会显著上升，进而拖慢攻击速度——因为需要采样更多数据。然而即便在 CPU 利用率较高的情况下，攻击依然可行。

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+vr29vby7e3q5ubk5OTj5eXl5eXl4uLj/f36+vr38vLw7Ozr6urs6uru6Ojs5eXo///////9+fn39PT08vL28PD47e316enu/////////v7++fn79/f99vb/8/P87+/1////////////+vr/+fn/+/v/+fn/9PT7////////////+Pj/+fn//v7//v7/+fn+////////////9vb/9/f//////////Pz/////////////9PT/9/f//////////f3/)![BLOG-3371 13.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M00XZYB97RCM22C4N1CB9TJT.png&w=715&h=240&f=webp&fit=cover&position=center)

## **为何未被检测到？**

DyPrIs 监测硬件性能计数器，一旦脚本行为疑似 Spectre 攻击，便将其隔离至独立进程。以下两点使本次攻击得以躲避检测。

其一，DyPrIs 仅在脚本调用结束后才会触发隔离，而我们在攻击中使用的 Durable Object 保活技巧可持续运行数小时乃至一天。WebSocket 保活消息使单次调用持续开放数小时，泄露早在隔离机制介入之前便已完成。

其二，DyPrIs 通过 iTLB 访问次数对分支预测错误进行归一化处理。我们的远程计时器是一个大型 I/O 循环，WebSocket 流量会显著增加 iTLB 活动量。归一化后的比率降至检测阈值以下，使该攻击看起来与普通的 I/O 密集型 Worker 无异。

## **我们的改进措施**

我们重点从三个方面持续推进改进：V8 深度加固、提供更强的进程内隔离，以及改进检测机制。

### **V8 Sandbox**

V8 内存沙箱的最终目标是从 JavaScript 堆的大部分区域移除原始 64 位指针，从而降低众多内存破坏原语的利用价值。这也使本研究中特定推测类型混淆 gadget 的复用难度大幅提升，因为 typed-array 后备存储不再暴露相同的原始指针结构。

V8 Sandbox 并非针对 Spectre 的完整缓解方案。尽管文中所述的 64 位泄露 gadget 不再适用，但仍可能存在其他 Spectre 变体或 gadget 可被利用，以实现任意越界内存访问。

### **硬件辅助进程内隔离**

2025 年 9 月，我们为 Workers 部署了基于内存保护密钥（Memory Protection Keys，MPK）的[ _进程内隔离_](https://blog.cloudflare.com/safe-in-the-sandbox-security-hardening-for-cloudflare-workers/)机制。MPK 允许进程将内存划分为保护域，并以低成本切换访问权限。Workers 利用该机制保护每个堆，防止其被同一进程内的其他隔离区访问。

这从根本上改变了 Spectre 的风险模型。每个隔离区的堆现在受到硬件强制访问边界的保护：对受错误密钥保护的页面的内存访问，将在硬件层面被拒绝。这阻断了本研究所依赖的直接跨隔离区堆读取路径。

然而，MPK 并非缓解 Spectre 的完整答案，但它严格收窄了泄露面。其局限性包括：硬件域数量有限，以及需要谨慎管理保护密钥状态。

### **改进 DyPrIs**

我们改进了 DyPrIs，将长期执行和 I/O 密集型工作负载作为一类安全问题来处理。检测不能仅在脚本结束后才触发。Durable Object 或 WebSocket 密集型 Worker 可能运行时间很长，以至于执行后隔离机制介入时为时已晚。

我们目前正在研究是否可将远程时序行为作为 DyPrIs 的额外检测维度。尽管我们无法阻断与攻击者控制基础设施的远程通信，但时序数据揭示了极具特征性的数据泄露比特模式。更好的做法是将计算密集型代码段周围重复出现的类计时器 I/O 纳入行为信号，而非将其视为背景噪声。

## **致谢**

特别感谢爱丁堡大学的 Haocheng Xiao 及其导师 Sam Ainsworth 和 Nigel Topham，感谢他们在提升 JavaScript 中 Spectre 攻击可靠性方面所作的贡献。

## **参与邀请**

我们始终欢迎您通过我们的[ _漏洞赏金计划_](https://hackerone.com/cloudflare)提交高质量报告。运行时内存安全漏洞是高价值目标。您可以在 GitHub 上找到 [_workerd 的 Fuzzilli 集成_](https://github.com/cloudflare/workerd/pull/4917)及 [_workerd 源代码_](https://github.com/cloudflare/workerd)。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frevisiting-spectre-attacks-on-workers%2F&t=%E9%87%8D%E6%96%B0%E5%AE%A1%E8%A7%86%E9%92%88%E5%AF%B9%20Cloudflare%20Workers%20%E7%9A%84%E8%BF%9C%E7%A8%8B%20Spectre%20%E6%94%BB%E5%87%BB)[](https://x.com/intent/post?text=%E9%87%8D%E6%96%B0%E5%AE%A1%E8%A7%86%E9%92%88%E5%AF%B9+Cloudflare+Workers+%E7%9A%84%E8%BF%9C%E7%A8%8B+Spectre+%E6%94%BB%E5%87%BB&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frevisiting-spectre-attacks-on-workers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frevisiting-spectre-attacks-on-workers%2F)[](https://bsky.app/intent/compose?text=%E9%87%8D%E6%96%B0%E5%AE%A1%E8%A7%86%E9%92%88%E5%AF%B9+Cloudflare+Workers+%E7%9A%84%E8%BF%9C%E7%A8%8B+Spectre+%E6%94%BB%E5%87%BB+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frevisiting-spectre-attacks-on-workers%2F)[](https://mastodonshare.com/?text=%E9%87%8D%E6%96%B0%E5%AE%A1%E8%A7%86%E9%92%88%E5%AF%B9+Cloudflare+Workers+%E7%9A%84%E8%BF%9C%E7%A8%8B+Spectre+%E6%94%BB%E5%87%BB&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frevisiting-spectre-attacks-on-workers%2F)[](https://www.threads.net/intent/post?text=%E9%87%8D%E6%96%B0%E5%AE%A1%E8%A7%86%E9%92%88%E5%AF%B9+Cloudflare+Workers+%E7%9A%84%E8%BF%9C%E7%A8%8B+Spectre+%E6%94%BB%E5%87%BB+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frevisiting-spectre-attacks-on-workers%2F)

## 相关标签

[Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)[攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)[研究](https://blog.cloudflare.com/zh-cn/tag/research/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Martin Schwarzl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q44FVCNYF3AKGF6DGP9G.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Martin Schwarzl](https://blog.cloudflare.com/zh-cn/author/martin/)

[](https://martinschwarzl.at)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
