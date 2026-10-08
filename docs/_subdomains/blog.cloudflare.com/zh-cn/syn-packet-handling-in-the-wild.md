---
url: https://blog.cloudflare.com/zh-cn/syn-packet-handling-in-the-wild/
title: \u5728\u91ce\u5916\u5904\u7406SYN\u6570\u636e\u5305 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:32.566903+00:00
---

# 在野外处理SYN数据包 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/syn-packet-handling-in-the-wild/

[博客](https://blog.cloudflare.com/zh-cn/)

[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[SYN](https://blog.cloudflare.com/zh-cn/tag/syn/)[TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)

3 个标签显示 3 个标签

  * 文章标签
  * [TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)
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



[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[SYN](https://blog.cloudflare.com/zh-cn/tag/syn/)[TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)

2018年1月15日

# 在野外处理SYN数据包

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/zh-cn/author/marek-majkowski/)

阅读时间：8 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/syn-packet-handling-in-the-wild/)、[Deutsch](https://blog.cloudflare.com/de-de/syn-packet-handling-in-the-wild/)、[Español](https://blog.cloudflare.com/es-es/syn-packet-handling-in-the-wild/)、[Français](https://blog.cloudflare.com/fr-fr/syn-packet-handling-in-the-wild/)、[日本語](https://blog.cloudflare.com/ja-jp/syn-packet-handling-in-the-wild/)和[한국어](https://blog.cloudflare.com/ko-kr/syn-packet-handling-in-the-wild/).

![SYN packet handling in the wild](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WCEJR7TBWGE5H9MEV3ES.jpeg&w=480&h=265&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/f3/+vr78vHw6efl4+Dh4t/i5OPl5+fn/////Pv88/Hw6+nn6ebm6ejq6Ojq5ufm//////399fLw7+zp8O7u8/L07/Dx5ujm////////+PXy8/Dt9/b1/Pz99/j56uzq/////////Pj29/Xz/f38/////v//8fPx//////////37+/r4////////////+fr5/////////////v37//////////////////////////////79////////////////)

在Cloudflare，我们有很多在“野外”互联网上操作服务器的经验。但我们一直在提高我们对这种“妖术”的掌握。在这篇博客中，我们触及了互联网协议的多个黑暗角落：比如[理解FIN-WAIT-2](https://blog.cloudflare.com/this-is-strictly-a-violation-of-the-tcp-specification/)或[接收缓冲区调优](https://blog.cloudflare.com/the-story-of-one-latency-spike/)。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1471936772_652043cb6c_b](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW496H1VNKAW08T8YJC1NN8P.jpg&w=715&h=536&f=webp&fit=cover&position=center)

[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) [图片](https://www.flickr.com/photos/isaimoreno/1471936772/in/photolist-3f54wd-6mweJG-maUn5T-2tgqad-6YuCuM-pZ7r8T-Sa3LQ9-adTFS2-qSLQzk-sJ66Lq-71cJPS-oFU9rf-mbom12-23fVpJW-71ciCN-718DHR-j4VCQQ-71chKo-5DMBr4-5DLQFK-71cG4s-qQFjhZ-2RMBP6-718KWR-71cAFA-fAr8Ri-pe5zev-8TtDbQ-b6p5gk-qAdMqQ-qSBvUZ-qyg7oz-o5yof6-adTGvc-718xp4-5XQgJZ-bgGiwk-kf7aMc-qAjY14-718uti-smXfxF-8Kdnpx-nVVy8a-cmMJGb-puizaG-qP18i9-71cu1E-nYNfjq-718CjH-qyQM72)，作者：[Isaí Moreno](https://www.flickr.com/photos/isaimoreno/)

然而，有一个话题没有得到足够的重视——SYN洪水。我们使用Linux系统，事实证明Linux中的SYN包处理非常复杂。在这篇文章中，我们将对这个问题做一些阐述。

## 有关两个队列的故事

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![SYN packet handling in the wild](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WCEJR7TBWGE5H9MEV3ES.jpeg&w=480&h=265&f=webp&fit=cover&position=center)

首先，我们必须要了解的是，每个绑定套接字在“监听”TCP状态下有两个独立的队列：

  * SYN队列
  * Accept（接受）队列



在文献中，这些队列通常被赋予其他名称，如“reqsk_queue”、“ACK backlog”、“listen backlog”，甚至“TCP backlog”，但是为了避免混淆，我将坚持使用上面的名称。

## SYN队列

SYN队列存储入站SYN数据包[[1]](https://blog.cloudflare.com/syn-packet-handling-in-the-wild/#fn1)（具体是：[`struct inet_request_sock`](https://elixir.free-electrons.com/linux/v4.14.12/source/include/net/inet_sock.h#L73)）。它负责发送SYN + ACK数据包，并在超时时重试。在Linux上，重试次数配置为：
    
    
    $ sysctl net.ipv4.tcp_synack_retries
    net.ipv4.tcp_synack_retries = 5

这篇[文档描述了这一toggle](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt)：
    
    
    tcp_synack_retries - INTEGER
    
    	Number of times SYNACKs for a passive TCP connection attempt
    	will be retransmitted. Should not be higher than 255. Default
    	value is 5, which corresponds to 31 seconds till the last
    	retransmission with the current initial RTO of 1second. With
    	this the final timeout for a passive TCP connection will
    	happen after 63 seconds.
    

在传输SYN+ACK之后，SYN队列需要等待来自客户端的ACK包——这是三次握手中的最后一个数据包。所有接收到的ACK包必须首先与完全建立的连接表进行匹配，然后才与相关SYN队列中的数据匹配。在SYN队列匹配中，内核从SYN队列中删除该项，愉快地创建一个完全成熟的连接（具体地说是：[struct inet_sock](https://elixir.free-electrons.com/linux/v4.14.12/source/include/net/inet_sock.h#L183)），并将其添加到Accept队列中。

## Accept队列

Accept队列包含完全建立的连接：准备由应用程序获取。当进程调用accept()时，套接字被从队列中删除并传递给应用程序。

这是Linux上SYN数据包处理的一个相当简化的视图。使用`TCP_DEFER_ACCEPT`[[2]](https://blog.cloudflare.com/syn-packet-handling-in-the-wild/#fn2) `和TCP_FASTOPEN`之类的套接字toggle，事情的`运作`会稍有不同。

## 队列大小限制

Accept和SYN队列的最大允许长度来自应用程序传递给listen(2)系统调用的backlog参数。例如，这里将Accept和SYN队列大小设置为1024：
    
    
    listen(sfd, 1024)

注意：在4.3之前的内核中，[SYN队列长度的计数方式有所不同](https://github.com/torvalds/linux/commit/ef547f2ac16bd9d77a780a0e7c70857e69e8f23f#diff-56ecfd3cd70d57cde321f395f0d8d743L43)。

该SYN队列上限以前是由net.ipv4.tcp_max_syn_backlog toggle配置的，但现在不再是这种情况了。如今，net.core.somaxconn为两个队列大小设置上限。在我们的服务器上，我们将其设置为16k：
    
    
    $ sysctl net.core.somaxconn
    net.core.somaxconn = 16384

## 完美的backlog值

了解了这些之后，我们可能会问这样一个问题：什么是理想的backlog参数值？

答案是：视情况而定。对于大多数普通TCP服务器而言，这并不重要。例如，在1.11版之前，[众所周知Golang并不支持自定义backlog值](https://github.com/golang/go/issues/6079)。尽管增加这个值是有正当理由的：

  * 当传入连接的速率非常大时，即使使用高性能应用程序，入站SYN队列也可能需要更多的插槽。
  * backlog值控制SYN队列大小。这实际上可以被理解为“飞行中的ACK包”。到客户端的平均往返时间越大，使用的插槽就越多。在许多客户端远离服务器（几百毫秒之外）的情况下，增加backlog值是有意义的。
  * TCP_DEFER_ACCEPT选项会使套接字保持在SYN-RECV状态的时间更长，并导致队列进一步受限。



过度调整backlog同样也是不好的：

  * SYN队列中的每个插槽都占用一些内存。在SYN洪水时，浪费资源来存储攻击数据包是没有意义的。SYN队列中的每个struct inet_request_sock条目都在4.14内核上占用256个字节的内存。



要查看Linux上的SYN队列，我们​​可以使用ss命令并查找SYN-RECV套接字。例如，在Cloudflare的一台服务器上，我们可以看到tcp / 80的SYN队列使用了119个插槽，而tcp / 443则使用了78个插槽。
    
    
    $ ss -n state syn-recv sport = :80 | wc -l
    119
    $ ss -n state syn-recv sport = :443 | wc -l
    78

类似数据的显示也可以借助我们的[overenginered SystemTap脚本：resq.stp](https://github.com/cloudflare/cloudflare-blog/blob/master/2018-01-syn-floods/resq.stp)。

## 缓慢应用

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![full-accept-1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498CJ44WVQHNK98B0FBAFT.jpeg&w=480&h=267&f=webp&fit=cover&position=center)

如果应用程序不能足够快地跟上调用accept()的速度，会发生什么？

这时魔法发生了！当接受队列已满（大小为backlog+1）时：

  * SYN队列的入站SYN数据包将被丢弃。
  * SYN队列的入站ACK数据包将被丢弃。
  * TcpExtListenOverflows / LINUX_MIB_LISTENOVERFLOWS计数增加。
  * TcpExtListenDrops / LINUX_MIB_LISTENDROPS计数增加。



丢弃入站数据包有一个强有力的理由：这是一个回推机制。另一方迟早会重新发送SYN或ACK包，这是希望，慢速的应用程序将得以恢复。

对于几乎所有的服务器来说，这都是一种可取的行为。为了完整起见：我们可以使用全局net.ipv4.tcp_abort_on_overflow toggle进行调整，但最好还是不用它。

如果您的服务器需要处理大量的入站连接，并且难以处理accept()吞吐量，请考虑阅读我们的[Nginx调整/ Epoll工作分发](https://blog.cloudflare.com/the-sad-state-of-linux-socket-balancing/)文章以及[显示有用的SystemTap脚本的后续文章](https://blog.cloudflare.com/perfect-locality-and-three-epic-systemtap-scripts/)。

您可以通过查看nstat计数器来跟踪Accept队列的溢出状态：
    
    
    $ nstat -az TcpExtListenDrops
    TcpExtListenDrops     49199     0.0

这是一个全局计数器。这并不理想——有时我们看到它在增长，而所有的应用程序看起来都很健康！第一步始终应该使用ss命令打印Accept队列大小：
    
    
    $ ss -plnt sport = :6443|cat
    State   Recv-Q Send-Q  Local Address:Port  Peer Address:Port
    LISTEN  0      1024                *:6443             *:*

该列中的Recv-Q显示Accept队列中的套接字数，并Send-Q显示backlog参数。在这种情况下，我们没有看到待处理的套接字accept()，但ListenDrops计数器仍在增加。

结果我们的应用程序在一小段时间内卡在了。这足以让Accept队列在很短的时间内溢出。过了一会儿，它又恢复了。这种情况很难用ss调试，所以我们编写了一个[acceptq.stp SystemTap脚本](https://github.com/cloudflare/cloudflare-blog/blob/master/2018-01-syn-floods/acceptq.stp)来帮助我们。它挂载到内核并打印要丢弃的SYN数据包：
    
    
    $ sudo stap -v acceptq.stp
    time (us)        acceptq qmax  local addr    remote_addr
    1495634198449075  1025   1024  0.0.0.0:6443  10.0.1.92:28585
    1495634198449253  1025   1024  0.0.0.0:6443  10.0.1.92:50500
    1495634198450062  1025   1024  0.0.0.0:6443  10.0.1.92:65434
    ...

在这里，您可以精确地看到哪些SYN数据包受到了ListenDrops的影响。使用此脚本，我们很容易就可以了解哪个应用程序断开了连接。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![3713965419_20388fb368_b](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46D1491EAPX0MD7EBXQZG9.jpg&w=715&h=402&f=webp&fit=cover&position=center)

[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) [图片](https://www.flickr.com/photos/16339684@N00/3713965419/in/photolist-6Ec3wx-5jhnwn-bfyTRX-5jhnCa-phYcey-dxZ95n-egkTN-kwT1YH-k22LWZ-5jBUiy-bzvDWx-5jBV31-5jhnr8-5jBTkq-5jxzHk-4K3cbP-9EePyg-4e5XNt-4e5XNn-dxZ8Tn-dy5A89-dxZ6GH-cztXcJ-gF7oY-dxZ9jv-dxZ7qM-ZvSPCv-dxZ6YV-5jBTqs-5jxzaP-MvuyK-nmVwP1-5jBRhY-dxZ7YF-5jxAc2-5jBU9U-5jBTEy-ejbWe6-5jxBc6-99ENZW-99KUsi-9bWScw-5jBRow-5jxzmx-5jBTfw-r6HcW-dy5zXE-5jxzg4-5jxBYR-5jxA2B)来自[internets_dairy](https://www.flickr.com/photos/16339684@N00/)

## SYN洪水

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![full-syn-1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48RTKJJ0NBG8M0G67B5KE4.jpeg&w=480&h=268&f=webp&fit=cover&position=center)

如果Accept队列有可能会溢出，那么SYN队列必然也存在溢出的可能。在这种情况下会发生什么？

这就是[SYN洪水攻击](https://en.wikipedia.org/wiki/SYN_flood)的全部目的。过去，用伪造的SYN数据包充满SYN队列是一个真正的问题。在1996年之前，只要填满SYN队列，就可以用很少的带宽成功地拒绝几乎所有TCP服务器的服务。

解决之道是[SYN Cookies](https://lwn.net/Articles/277146/)。SYN Cookies是一种允许无状态生成SYN + ACK的结构，实际上不需要保存入站SYN并浪费系统内存。SYN Cookies不会破坏合法流量。当另一方真实存在时，它将以有效的ACK数据包进行响应，其中包括反射的序列号，该序列号可以通过密码验证。

默认情况下，SYN Cookie仅在需要时启用——用于SYN队列已满的套接字。Linux更新了SYN Cookie上的几个计数器。发送SYN Cookie时：

  * TcpExtTCPReqQFullDoCookies / LINUX_MIB_TCPREQQFULLDOCOOKIES递增。
  * TcpExtSyncookiesSent / LINUX_MIB_SYNCOOKIESSEN递增。
  * Linux以前会递增TcpExtListenDrops，但[从内核4.7开始不再如此](https://github.com/torvalds/linux/commit/9caad864151e525929d323de96cad382da49c3b2)。



当一个入站ACK进入SYN队列时，SYN Cookie被占用：

  * 密码验证成功，则TcpExtSyncookiesRecv / LINUX_MIB_SYNCOOKIESRECV递增。
  * 密码验证失败，则TcpExtSyncookiesFailed / LINUX_MIB_SYNCOOKIESFAILED递增。



sysctl net.ipv4.tcp_syncookies可以禁用SYN Cookies或强制启用它们。默认就好，无需更改。

## SYN Cookies和TCP时间戳

SYN Cookies这一“魔法”是可行的，但它也不是没有缺点的。主要的问题是，可以保存在SYN Cookie中的数据非常少。具体来说，在ACK中只返回序列号的32位。这些位元的用法如下：
    
    
    +----------+--------+-------------------+
    |  6 bits  | 2 bits |     24 bits       |
    | t mod 32 |  MSS   | hash(ip, port, t) |
    +----------+--------+-------------------+

由于MSS设置[仅被截断为4个不同的值](https://github.com/torvalds/linux/blob/5bbcc0f595fadb4cac0eddc4401035ec0bd95b09/net/ipv4/syncookies.c#L142)，因此Linux不知道对方的任何可选TCP参数。有关时间戳，ECN，选择性ACK或窗口缩放的信息会丢失，并可能导致TCP会话性能下降。

幸运的是，Linux可以解决。如果启用了TCP时间戳，则内核可以在“时间戳”字段中重新使用另一个32位插槽。它包含：
    
    
    +-----------+-------+-------+--------+
    |  26 bits  | 1 bit | 1 bit | 4 bits |
    | Timestamp |  ECN  | SACK  | WScale |
    +-----------+-------+-------+--------+

默认情况下，应启用TCP时间戳，从而验证查看sysctl：
    
    
    $ sysctl net.ipv4.tcp_timestamps
    net.ipv4.tcp_timestamps = 1

历史上有很多关于TCP时间戳有用性的讨论。

  * 在过去，时间戳会泄露服务器运行时间（这是否重要又是另一个讨论了）。这[在8个月前就被修复了](https://github.com/torvalds/linux/commit/95a22caee396cef0bb2ca8fafdd82966a49367bb)。
  * TCP时间戳占用[大量的带宽](http://highscalability.com/blog/2015/10/14/save-some-bandwidth-by-turning-off-tcp-timestamps.html)——每个数据包12字节。
  * 它们可以为数据包校验增添额外的随机性，这[可以帮助解决某些损坏的硬件](https://www.snellman.net/blog/archive/2017-07-20-s3-mystery/)。
  * 如上所述，如果启用了SYN Cookies，则TCP时间戳可以提高TCP连接的性能。



目前在Cloudflare，我们禁用了TCP时间戳。

最后，使用SYN Cookie时，一些很酷的特性将不起作用，比如[TCP_SAVED_SYN](https://lwn.net/Articles/645128/)、TCP_DEFER_ACCEPT或TCP_FAST_OPEN。

## Cloudflare规模的SYN洪水

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screen-Shot-2016-12-02-at-10.53.27-1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TFREC0S7MVSCF6F44SNY.png&w=715&h=101&f=webp&fit=cover&position=center)

SYN Cookie是一项伟大的发明，它解决了SYN小洪水的问题。但在Cloudflare，我们尽可能避免使用它们。虽然每秒发送几千个可加密验证的SYN+ACK包是可行的，但我们看到的是[每秒超过2亿个包的攻击](https://blog.cloudflare.com/the-daily-ddos-ten-days-of-massive-attacks/)。在这种规模下，我们的SYN+ACK响应就相当于在互联网上乱扔垃圾，不会带来任何好处。

相反，我们尝试在防火墙层上丢弃恶意的SYN数据包。我们使用编译到BPF（柏克莱封包过滤器）的p0f SYN指纹。您可以阅读这篇[介绍p0f BPF编译器](https://blog.cloudflare.com/introducing-the-p0f-bpf-compiler/)的博文，了解更多信息。为了检测和部署缓解措施，我们开发了一个自动化系统，称为“Gatebot（网关机器人）”。这里有我们对它的描述：[认识Gatebot——让我们能够安然入睡的机器人](https://blog.cloudflare.com/meet-gatebot-a-bot-that-allows-us-to-sleep/)。

## 不断变化的景观

有关该主题的数据稍有些过时，想要了解更多，请阅读[Andreas Veithen在2015年](https://veithen.github.io/2014/01/01/how-tcp-backlog-works-in-linux.html)给出[的出色解释](https://veithen.github.io/2014/01/01/how-tcp-backlog-works-in-linux.html)和[Gerald W. Gordon在2013年发布的综合论文](https://www.giac.org/paper/gsec/2013/syn-cookies-exploration/103486)。

Linux SYN数据包处理技术的景观在不断发展。直到最近，由于内核中的老式锁，SYN Cookies仍然很慢。这个问题在4.4中已得到解决，现在您可以依赖内核每秒发送数百万个SYN Cookie，这实际上解决了大多数用户的SYN洪水问题。通过适当的调优，我们甚至可以在不影响合法连接性能的情况下减轻最烦人的SYN洪水。

应用程序的性能也得到了极大的关注。最近的一些想法（如SO_ATTACH_REUSEPORT_EBPF）在网络堆栈中引入了一个全新的可编程层。

在这个原本停滞不前的操作系统世界里，看到创新和新鲜的想法涌入网络堆栈，真是太好了。

 _感谢Binh Le为这篇文章提供的帮助。_

* * *

 _处理Linux和NGINX的内部是不是很有趣呢？快来加入我们在伦敦，奥斯汀，旧金山的[世界著名团队](https://boards.greenhouse.io/cloudflare/jobs/589572)以及在波兰华沙的精英办公室吧。_

* * *

  1. 我在简化，从技术上讲，SYN队列存储的是尚未建立的连接，而不是SYN包本身。尽管使用TCP_SAVE_SYN就已经足够了。[↩︎](https://blog.cloudflare.com/syn-packet-handling-in-the-wild/#fnref1)
  2. 如果您不熟悉[TCP_DEFER_ACCEPT](http://man7.org/linux/man-pages/man7/tcp.7.html)，那么一定要看看FreeBSD的版本——[accept过滤器](http://www.freebsd.org/cgi/man.cgi?query=accf_http&sektion=9)。 [↩︎](https://blog.cloudflare.com/syn-packet-handling-in-the-wild/#fnref2)



本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsyn-packet-handling-in-the-wild%2F&t=%E5%9C%A8%E9%87%8E%E5%A4%96%E5%A4%84%E7%90%86SYN%E6%95%B0%E6%8D%AE%E5%8C%85)[](https://x.com/intent/post?text=%E5%9C%A8%E9%87%8E%E5%A4%96%E5%A4%84%E7%90%86SYN%E6%95%B0%E6%8D%AE%E5%8C%85&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsyn-packet-handling-in-the-wild%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsyn-packet-handling-in-the-wild%2F)[](https://bsky.app/intent/compose?text=%E5%9C%A8%E9%87%8E%E5%A4%96%E5%A4%84%E7%90%86SYN%E6%95%B0%E6%8D%AE%E5%8C%85+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsyn-packet-handling-in-the-wild%2F)[](https://mastodonshare.com/?text=%E5%9C%A8%E9%87%8E%E5%A4%96%E5%A4%84%E7%90%86SYN%E6%95%B0%E6%8D%AE%E5%8C%85&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsyn-packet-handling-in-the-wild%2F)[](https://www.threads.net/intent/post?text=%E5%9C%A8%E9%87%8E%E5%A4%96%E5%A4%84%E7%90%86SYN%E6%95%B0%E6%8D%AE%E5%8C%85+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsyn-packet-handling-in-the-wild%2F)

## 相关标签

[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[SYN](https://blog.cloudflare.com/zh-cn/tag/syn/)[TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
