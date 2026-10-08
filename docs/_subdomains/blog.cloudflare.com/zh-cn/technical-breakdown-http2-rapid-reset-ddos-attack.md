---
url: https://blog.cloudflare.com/zh-cn/technical-breakdown-http2-rapid-reset-ddos-attack/
title: HTTP/2 Rapid Reset\uff1a\u89e3\u6784\u8fd9\u573a\u7834\u7eaa\u5f55\u7684\u653b\u51fb | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:17.432328+00:00
---

# HTTP/2 Rapid Reset：解构这场破纪录的攻击 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/technical-breakdown-http2-rapid-reset-ddos-attack/

[博客](https://blog.cloudflare.com/zh-cn/)

[DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)+2再显示 2 个标签

5 个标签显示 5 个标签

  * 文章标签
  * [DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)[趋势](https://blog.cloudflare.com/zh-cn/tag/trends/)
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



[漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)[趋势](https://blog.cloudflare.com/zh-cn/tag/trends/)

[DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)[趋势](https://blog.cloudflare.com/zh-cn/tag/trends/)

2023年10月10日

# HTTP/2 Rapid Reset：解构这场破纪录的攻击

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Julien Desgats](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490NXEPS0Y3GYM6MEBDP98.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/zh-cn/author/lucas/)和[Julien Desgats](https://blog.cloudflare.com/zh-cn/author/julien-desgats/)

阅读时间：16 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/)、[Deutsch](https://blog.cloudflare.com/de-de/technical-breakdown-http2-rapid-reset-ddos-attack/)、[Español](https://blog.cloudflare.com/es-es/technical-breakdown-http2-rapid-reset-ddos-attack/)、[Français](https://blog.cloudflare.com/fr-fr/technical-breakdown-http2-rapid-reset-ddos-attack/)、[日本語](https://blog.cloudflare.com/ja-jp/technical-breakdown-http2-rapid-reset-ddos-attack/)、[한국어](https://blog.cloudflare.com/ko-kr/technical-breakdown-http2-rapid-reset-ddos-attack/)和[繁體中文](https://blog.cloudflare.com/zh-tw/technical-breakdown-http2-rapid-reset-ddos-attack/).

![BLOG-2023 Embedded Image - mLN7qf](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48WDXXVR9MBXJX2BC6M78M.png&w=1600&h=901&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9PLz5+br4uPt5Ofz6O3z6+/v////////7Orx19bm0NHn2Nvu5Ojx6+/w////////5OPxxsXivsDiztHq4eTx7fDy////////4+P0wcHkurzjztDs5Of08fT2////////7Oz6z9Dty8zt29307fD69/r7////////+vr/5uf65OX67/D/+fz//v//////////////+vv/+fr/////////////////////////////////////////////)

从 2023 年 8 月 25 日开始，我们开始注意到一些异常大量的 HTTP 攻击袭击了我们的许多客户。我们的自动化 DDoS 系统检测到并缓解了这些攻击。然而，没过多久，它们就开始达到破纪录的规模 - 最终达到了每秒 2.01 亿次请求的峰值。此数量几乎是我们[以前最大攻击记录数量](https://blog.cloudflare.com/zh-cn/cloudflare-mitigates-record-breaking-71-million-request-per-second-ddos-attack-zh-cn/)的 3 倍。

 _受到攻击或需要额外保护？[单击此处获取帮助](https://www.cloudflare.com/h2/)。_  


而更令人担忧的是，攻击者能够利用一个只有 20,000 台机器的僵尸网络发起这样的攻击。而如今有的僵尸网络由数十万或数百万台机器组成。整个 web 网络通常每秒处理10-30 亿个请求，因此使用此方法可以将整个 web 网络的请求数量等级集中在少数目标上，而这并非不可想象。

## 检测和缓解

这是一种规模空前的新型攻击手段，Cloudflare 现有的保护措施在很大程度上能够抵御这种攻击的冲击。虽然最初我们看到了对客户流量的一些影响（在第一波攻击期间影响了大约1% 的请求），但今天我们已经能够改进我们的缓解方法，以阻止任何针对Cloudflare 客户的攻击，并保证自身的系统正常运行。

我们注意到这些攻击的同时，谷歌和 AWS 这两大行业巨头也发现了同样的情况。我们努力加固 Cloudflare 的系统，以确保目前我们所有的客户都能免受这种新的 DDoS 攻击方法的影响，而不会对客户造成任何影响。我们还与谷歌和 AWS 共同参与了向受影响的供应商和关键基础设施提供商披露攻击事件的协调工作。

这种攻击是通过滥用 HTTP/2 协议的某些功能和服务器实施详细信息实现的（详情请参见 [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487)）。由于该攻击滥用了 HTTP/2 协议中的一个潜在弱点，我们认为实施了 HTTP/2 的任何供应商都会受到攻击。这包括所有现代网络服务器。我们已经与谷歌和 AWS 一起向网络服务器供应商披露了攻击方法，我们希望他们能够实施补丁。与此同时，最好的防御方法是在任何面向网络的 Web 服务器或 API 服务器前面使用诸如 Cloudflare 之类的 DDoS 缓解服务。

这篇文章深入探讨了 HTTP/2 协议的详细信息、攻击者利用来实施这些大规模攻击的功能，以及我们为确保所有客户受到保护而采取的缓解策略。我们希望通过公布这些详细信息，其他受影响的 Web 服务器和服务能够获得实施缓解策略所需的信息。此外，HTTP/2 协议标准团队以及开发未来 Web 标准的团队可以更好地设计这些标准，以防止此类攻击。

## RST 攻击详细信息

HTTP 是为 Web 提供支持的应用协议。[HTTP 语义](https://www.rfc-editor.org/rfc/rfc9110.html)对于所有版本的 HTTP 都是通用的 — 整体架构、术语和协议方面，例如请求和响应消息、方法、状态代码、标头和尾部字段、消息内容等等。每个单独的 HTTP 版本都定义了如何将语义转换为“有线格式”以通过 Internet 进行交换。例如，客户端必须将请求消息序列化为二进制数据并发送，然后服务器将其解析回它可以处理的消息。

[HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html) 使用文本形式的序列化。请求和响应信息以 ASCII 字符流的形式进行交换，通过可靠的传输层（如 TCP）发送，使用以下[格式](https://www.rfc-editor.org/rfc/rfc9112.html#section-2.1)（其中 CRLF 表示回车和换行）：
    
    
     HTTP-message   = start-line CRLF
                       *( field-line CRLF )
                       CRLF
                       [ message-body ]

例如，对于 `https://blog.cloudflare.com/` 的一个非常简单的 GET 请求在线路上将如下所示：

`GET / HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLF`

响应将如下所示：

`HTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>`

这种格式在线路上构造消息，这意味着可以使用单个 TCP 连接来交换多个请求和响应。但是，该格式要求每条消息都完整发送。此外，为了正确地将请求与响应关联起来，需要严格的排序；这意味着消息是串行交换的并且不能多路复用。`https://blog.cloudflare.com/` 和 `https://blog.cloudflare.com/page/2/` 的两个 GET 请求将是：

`GET / HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLFGET /page/2/ HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLF`

响应如下：

`HTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>CRLFHTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>`

Web 页面需要比这些示例更复杂的 HTTP 交互。访问 Cloudflare 博客时，您的浏览器将加载多个脚本、样式和媒体资产。如果您使用 HTTP/1.1 访问首页，然后很快决定导航到第 2 页，您的浏览器可以从两个选项中进行选择。要么在第 2 页开始之前等待对您不再需要的页面的所有已排入队列的响应，要么通过关闭 TCP 连接并打开一个新连接来取消进行中的请求。这两种方法都不太实用。浏览器往往通过管理 TCP 连接池（每台主机最多 6 个连接）并在池上实现复杂的请求分派逻辑来绕过这些限制。

[HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) 解决了 HTTP/1.1 的许多问题。每个 HTTP 消息都被序列化为一组 **HTTP/2 帧** ，这些帧具有类型、长度、标志、流标识符 (ID) 和有效负载。流 ID 清楚地表明线路上的哪些字节适用于哪个消息，从而允许安全的多路复用和并发。流是双向的。客户端发送帧，服务器使用相同的 ID 回复帧。

在 HTTP/2 中，我们对 `https://blog.cloudflare.com` 的 GET 请求将通过流 ID 1 交换，客户端发送一个 [HEADERS](https://www.rfc-editor.org/rfc/rfc9113#name-headers) 帧，服务器使用一个 HEADERS 帧进行响应，后跟一个或多个 [DATA](https://www.rfc-editor.org/rfc/rfc9113#name-data) 帧。客户端请求始终使用奇数流 ID，因此后续请求将使用流 ID 3、5 等。可以以任何顺序提供响应，并且来自不同流的帧可以交织。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - x9QxRg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49B9T4FFZW2YJF9EFMJGRE.png&w=715&h=221&f=webp&fit=cover&position=center)

流多路复用和并发是 HTTP/2 的强大功能。它们可以更有效地使用单个 TCP 连接。HTTP/2 优化了资源获取，尤其是在与[优先排序](https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/)相结合时。另一方面，与 HTTP/1.1 相比，让客户端更容易启动大量并行工作会增加对服务器资源的峰值需求。这显然是拒绝服务的一个载体。

为了提供一些防护措施，HTTP/2 提供了最大活动[并发流](https://www.rfc-editor.org/rfc/rfc9113#section-5.1.2)的概念。[SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_FRAME_SIZE) 参数允许服务器公布其并发限制。例如，如果服务器声明限制为 100，那么任何时候都最多只能有 100 个请求处于活动状态。如果客户端试图打开超过此限制的流，服务器一定会使用 [RST_STREAM](https://www.rfc-editor.org/rfc/rfc9113#section-6.4) 帧拒绝它。流拒绝不会影响连接上的其他正在进行中的流。

真实情况要复杂一些。流有[生命周期](https://www.rfc-editor.org/rfc/rfc9113#section-5.1)。下面是 HTTP/2 流状态机的示意图。客户端和服务器管理各自的流状态视图。当发送或接收 HEADERS、DATA 和 RST_STREAM 帧时，它们会触发转换。虽然流状态的视图是独立的，但它们是同步的。

HEADERS 和 DATA 帧包含一个 END_STREAM 标志，当设置为 1 (true) 时，可触发状态转换。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - dgpLal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45G749M08PSFAAXZRQE5DQ.png&w=715&h=515&f=webp&fit=cover&position=center)

让我们通过一个没有消息内容的 GET 请求示例来解决这个问题。客户端以 HEADERS 帧的形式发送请求，并将 END_STREAM 标志设置为 1。客户端首先将流从**空闲状态** 转换为**打开状态** ，然后立即转换为**半关闭** 状态。客户端半关闭状态意味着它不能再发送HEADERS或DATA，只能发送 [WINDOW_UPDATE](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.9)、[PRIORITY](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.3) 或 RST_STREAM 帧。然而，它可以接收任何帧。

一旦服务器接收并解析了 HEADERS 帧，它就会将流状态从空闲转变为打开，然后半关闭，因此它与客户端匹配。服务器半关闭状态意味着它可以发送任何帧，但只能接收 WINDOW_UPDATE、PRIORITY 或 RST_STREAM 帧。

对 GET 的响应包含消息内容，因此服务器发送 END_STREAM 标志设置为 0 的 HEADERS，然后发送 END_STREAM 标志设置为 1 的 DATA。DATA 帧触发服务器上流从**半关闭** 到**关闭** 的转换。当客户端收到它时，它也会转换为关闭状态。一旦流关闭，就无法发送或接收任何帧。

将此生命周期应用回并发上下文中，HTTP/2 [指出](https://www.rfc-editor.org/rfc/rfc9113#section-5.1.2-2)：

 _处于“打开”状态或任一种“半关闭”状态的流计入允许端点打开的最大流数量。处于这三种状态中任何一种状态的流都将计入在_ [_SETTINGS_MAX_CONCURRENT_STREAMS_](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_CONCURRENT_STREAMS) 设置中公布的限制。

理论上，并发限制是有用的。不过，也有一些实际因素会影响它的效果，我们将在这篇博文的后面部分讲述。

### HTTP/2 请求取消

在前文中，我们谈到了客户端取消正在进行的请求的问题。与 HTTP/1.1 相比，HTTP/2 支持这种方式的效率要高得多。客户端无需中断整个连接，只需针对单个流发送一个 RST_STREAM 帧。这将指示服务器停止处理该请求并中止响应，从而释放服务器资源并避免浪费带宽。

让我们来看看前面 3 个请求的例子。这一次，客户端在发送完所有 HEADERS 帧后，取消了针对流 1 的请求。服务器在准备好提供响应之前，会解析此 RST_STREAM 帧，并改为只响应流 3 和流 5：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - alylDM](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48VGZF708M4TQDMQVJN3F2.png&w=715&h=225&f=webp&fit=cover&position=center)

取消请求是一个非常有用的功能。例如，当滚动包含多个图像的网页时，网络浏览器可以取消落在视口之外的图像，这意味着进入视口的图像可以更快地加载。与 HTTP/1.1 相比，HTTP/2 使这种行为更加高效。

被取消的请求流会快速过渡整个流生命周期。 END_STREAM 标志设置为 1 的客户端 HEADERS 状态从**空闲状态** 转换为**打开** 状态再到**半关闭** 状态，然后 RST_STREAM 立即导致从**半关闭** 状态转换为**关闭** 状态。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - FOxdTz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SPXM07R6QG2B8FEXJCHJ.png&w=715&h=515&f=webp&fit=cover&position=center)

回想一下，只有处于打开或半关闭状态的流才会影响流并发限制。当客户端取消流时，它立即能够在其位置打开另一个流，并可以立即发送另一个请求。这就是 [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487) 能够发挥作用的关键所在。

### 快速重置导致拒绝服务

HTTP/2 请求取消可能被滥用来快速重置无限数量的流。当 HTTP/2 服务器能够足够快地处理客户端发送的 RST_STREAM 帧并拆除状态时，这种快速重置不会导致问题。当整理工作出现任何延误或滞后时，问题就会开始出现。客户端可能会处理大量请求，从而导致工作积压，从而导致服务器上资源的过度消耗。

常见的 HTTP 部署架构会在其他组件前面运行 HTTP/2 代理或负载平衡器。当客户端请求到达时，它会被快速分派，而实际工作则作为异步活动在其他地方完成。这样，代理就能非常高效地处理客户端流量。然而，这种关注点的分离会使代理难以整理正在处理的作业。因此，这些部署更有可能遇到快速重置造成的问题。

Cloudflare 的[反向代理](https://www.rfc-editor.org/rfc/rfc9110#section-3.7-6)处理传入的 HTTP/2 客户端流量时，会将数据从连接的套接字复制到缓冲区，并按顺序处理缓冲的数据。在读取每个请求（HEADERS 和 DATA 帧）时，它会被分派到上游服务。读取 RST_STREAM 帧时，请求的本地状态会被删除，并通知上游请求已被取消。如此循环往复，直到整个缓冲区中的数据处理完毕。然而，这种逻辑可能会被滥用：当恶意客户端开始发送大量请求链，并在连接开始时重置时，我们的服务器就会迫不及待地读取所有请求，给上游服务器造成压力，以至于无法处理任何新的传入请求。

需要强调的是，流并发本身并不能缓解快速重置。无论服务器选择的 [SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_CONCURRENT_STREAMS) 值是多少，客户端可以不断发送请求以创建高请求率。

### 快速重置剖析

以下是使用概念验证客户端尝试发出总共 1000 个请求的快速重置示例。我使用了现成的服务器，没有任何缓解措施； 在测试环境中侦听端口 443。为了清楚起见，使用 Wireshark 剖析流量并进行过滤以仅显示 HTTP/2 流量。[下载 pcap](http://staging.blog.mrk.cfdata.org/content/images/rapidreset.pcapng) 以进行后续操作。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - WbJayy](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46CJJHBWXXWMSQCY94SYWG.png&w=715&h=35&f=webp&fit=cover&position=center)

要看清楚有点难，因为有很多帧。我们可以通过 Wireshark 的“统计 > HTTP2”工具快速获得摘要：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - hiRPjv](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44JCSEZW1GJBEZC3CJVBK1.png&w=715&h=219&f=webp&fit=cover&position=center)

在此跟踪中，数据包 14 中的第一个帧是服务器的 SETTINGS 帧，它标明最大流并发为 100。在数据包 15 中，客户端发送了几个控制帧，然后开始发出会快速重置的请求。第一个 HEADERS 帧长 26 字节，而随后的所有 HEADERS 帧都只有 9 字节。这种大小差异是由于一种名为 [HPACK](https://blog.cloudflare.com/hpack-the-silent-killer-feature-of-http-2/) 的压缩技术造成。数据包 15 总共包含 525 个请求，最高可达 1051 个流。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - 4zuXCV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497JBM72881G9RYDWRT2C6.png&w=619&h=593&f=webp&fit=cover&position=center)

有趣的是，流 1051 的 RST_STREAM 帧并未包含在数据包 15 中，因此在数据包 16 中，我们看到服务器传回 404 响应。然后，在数据包 17 中，客户端发送 RST_STREAM，然后继续发送余下的 475 个请求。

请注意，虽然服务器声明有 100 个并发流，但客户端发送的两个数据包的 HEADERS 帧数远超此值。客户端无需等待服务器的任何返回流量，它只受限于它可以发送的数据包大小。在此跟踪中未发现服务器 RST_STREAM 帧，表明服务器未发现并发流违规。

## 对客户的影响

如上所述，当请求被取消时，上游服务会收到通知，并中止请求以免浪费过多资源。这次攻击就是这种情况，大多数恶意请求从未被转发到源服务器。然而，这些攻击的规模很大，确实造成了一些影响。

首先，当传入请求的速度达到前所未有的峰值时，我们收到了客户端发现 502 错误增多的报告。这种情况发生在我们受影响最大的数据中心，彼时它们正在努力处理所有请求。虽然我们的网络可以应对大规模攻击，但这一特殊漏洞暴露了我们基础设施中的薄弱环节。让我们深入探讨一下详细信息，重点关注当传入的请求到达我们的数据中心之一时如何处理：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - ZsURSu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45571VPJA9ST5WBRH9KPG8.png&w=715&h=269&f=webp&fit=cover&position=center)

我们可以看到我们的基础设施由一系列具有不同职责的不同代理服务器组成。特别是，当客户端连接到 Cloudflare 发送 HTTPS 流量时，它首先会命中我们的 TLS 解密代理：它解密 TLS 流量，处理 HTTP 1、2 或 3 流量，然后将其转发到我们的“业务逻辑”代理。它负责加载每个客户的所有设置，然后将请求正确路由到其他上游服务 - 更重要的是，在我们的例子中，**它还负责安全功能** 。这是处理 L7 攻击缓解的地方。

这种攻击手段的问题在于，它能在每个连接中快速发送大量请求。每个请求都必须转发到业务逻辑代理，我们才有机会阻止它。当请求吞吐量超过我们代理的处理能力时，连接这两项服务的管道在我们的一些服务器中达到了饱和水平。

当发生这种情况时，TLS 代理就无法再连接到其上游代理，因此在最严重的攻击中，一些客户端会看到“502 Bad Gateway”错误。值得注意的是，到目前为止，用于创建 HTTP 分析的日志也是由我们的业务逻辑代理发布的。这样做的后果是，在 Cloudflare 仪表板中看不到这些错误。我们的内部仪表板显示，在最初的攻击浪潮中（在我们实施缓解措施之前），约有 1% 的请求受到影响，在 8 月 29 日最严重的一次攻击中，有几秒钟的峰值达到了约 12%。下图显示了出现这种情况时的两小时内这些错误的比率：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - cDLXgV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H86FX527NRYXEFG5HNZH.png&w=715&h=442&f=webp&fit=cover&position=center)

在接下来的几天里，我们努力大幅减少了这一数字，详见本帖下文。由于我们的堆栈发生了变化，而且我们的缓解措施大大降低了这些攻击的规模，如今这一数字实际上为零。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - AfViXl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW484F1GN0TB062910TF1AD8.png&w=715&h=442&f=webp&fit=cover&position=center)

### 499 错误和 HTTP/2 流并发挑战

一些客户报告的另一个症状是 499 错误增加。造成这种情况的原因有些不同，与本贴前面详述的 HTTP/2 连接中的最大流并发相关。

HTTP/2 设置在连接开始时使用 SETTINGS 帧进行交换。如果没有收到明确的参数，则会使用默认值。客户端建立 HTTP/2 连接后，可以等待服务器的 SETTINGS（慢），也可以使用默认值开始发出请求（快）。对于 SETTINGS_MAX_CONCURRENT_STREAMS，默认值实际上是无限的（流 ID 使用 31 位数字空间，请求使用奇数，因此实际限制是 1073741824）。规范建议服务器提供不少于 100 个数据流。客户端通常偏向于速度，因此不会等待服务器设置，这就造成了一些竞争情况。客户端会赌服务器可能选择的限制；如果客户端赌错了，请求将被拒绝，并且客户端必须重试。在 1073741824 个流上赌有点傻。取而代之，许多客户端决定将自己限制在发布 100 个并发流，希望服务器遵循规范建议。如果服务器选择低于 100 的数值，则客户端赌错了，流将被重置。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - VLKjcD](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46456QGGZGE6J54D0S0W49.png&w=715&h=246&f=webp&fit=cover&position=center)

服务器重置超出并发限制的流的原因有很多。HTTP/2 是严格的，在出现解析或逻辑错误时会要求关闭流。在 2019 年，Cloudflare 针对 [HTTP/2 DoS 漏洞](https://blog.cloudflare.com/on-the-recent-http-2-dos-attacks/)开发了多个缓解措施。其中几个漏洞是由客户端行为不当导致服务器重置流造成的。遏制此类客户端的一个非常有效的策略是对在连接期间服务器重置的次数进行计数，当次数超过某个阈值时，就使用 [GOAWAY](https://www.rfc-editor.org/rfc/rfc9113#section-6.8) 帧关闭连接。合法客户可能会在一次连接中犯一两个错误，这是可以接受的。如果客户端犯错误的次数过多，它很可能是损坏的客户端或恶意客户端，关闭连接可以解决这两种情况。

在应对由 [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487) 引发的 DoS 攻击时，Cloudflare 将最大流并发降至 64。在进行此更改之前，我们并不知道客户端不会等待 SETTINGS，而是假设并发为 100。某些 Web 页面（如图片库）确实会导致浏览器在连接开始时立即发送 100 个请求。不幸的是，超过限制的 36 个流都需要重置，这触发了我们的计数缓解措施。这意味着我们关闭了合法客户端的连接，导致页面加载完全失败。我们意识到这个互操作性问题后，立即将最大流并发更改为 100。

## Cloudflare 方面的行动

在 2019 年，发现了几个与 HTTP/2 实现相关的 [DoS 漏洞](https://blog.cloudflare.com/on-the-recent-http-2-dos-attacks/)。作为回应，Cloudflare 开发并部署了一系列检测和缓解措施。[CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487) 是 HTTP/2 漏洞的另一种表现形式。不过，为了缓解它，我们能够扩展现有的保护，以监控客户端发送的 RST_STREAM 帧，并在它们被用于滥用时关闭连接。客户端对 RST_STREAM 的合法使用不受影响。

除了直接修复外，我们还对服务器的 HTTP/2 帧处理和请求分派代码进行了多项改进。此外，业务逻辑服务器还改进了队列和分派，减少了不必要的工作，提高了对取消操作的响应速度。这些措施多管齐下，减轻了各种潜在滥用模式的影响，并为服务器在饱和前处理请求提供了更多空间。

### 尽早缓解攻击

Cloudflare 已经部署了一套系统，可以通过成本较低的方法有效缓解超大型攻击。其中一个系统名为 IP Jail。对于超容量攻击，该系统会收集参与攻击的客户端 IP，并阻止它们连接到受攻击的财产（无论是在 IP 级别还是在我们的 TLS 代理中）。然而，该系统需要几秒钟才能完全生效； 在这宝贵的几秒钟内，源头已经受到保护，但我们的基础设施仍然需要吸收所有 HTTP 请求。由于这种新的僵尸网络实际上没有启动期，因此我们需要能够在攻击成为问题之前将其消灭。

为此，我们扩展了 IP Jail 系统，以保护我们的整个基础设施：一旦一个 IP 被“监禁”，它不仅会被阻止连接到受攻击的资产，我们还会禁止相应的 IP 在一段时间内使用 HTTP/2 连接到 Cloudflare 上的任何其他域。因此，无法通过使用 HTTP/1.x 来滥用协议。这就限制了攻击者实施大规模攻击的能力，而共用同一 IP 的任何合法客户端在此期间只会看到非常小的性能下降。基于 IP 的缓解措施是一种非常笨拙的工具 - 这就是为什么我们在这种规模下使用它们时必须非常小心，并尽可能避免误报。此外，僵尸网络中给定 IP 的寿命通常很短，因此任何长期缓解措施都可能弊大于利。下图显示了我们目睹的攻击中 IP 的变化情况：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - zEcUBs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BMWNAXCMETHFB5FB79WB.png&w=715&h=348&f=webp&fit=cover&position=center)

我们可以看到，在某一天发现的许多新 IP 后来很快就消失了。

由于所有这些操作都在 HTTPS 管道开始时在我们的 TLS 代理中发生，因此与常规的 L7 缓解系统相比，可以节省大量资源。这使我们能够更顺利地应对这些攻击，现在这些僵尸网络造成的随机 502 错误数量已降至零。

### 攻击可观测性改进

我们正在改变的另一个方面是可观察性。将错误返回到客户端但在客户分析中不可见这种情况令人不满。幸运的是，早在最近的袭击发生之前，就有一个项目正在对这些系统进行全面检查。它最终将允许我们基础设施中的每个服务记录自己的数据，而不是依赖我们的业务逻辑代理来整合和发布日志数据。这次事件凸显了这项工作的重要性，我们将加倍努力。

我们也在努力改进连接层面的日志记录，使我们能够更快地发现此类协议滥用，从而提高我们的 DDoS 缓解能力。

## 总结

虽然这是最近一次破纪录的攻击，但我们知道这不会是最后一次。随着攻击的不断复杂化，Cloudflare 坚持不懈地努力，积极主动地识别新的威胁，并在我们的全球网络中部署应对措施，使我们的数百万客户能够立即自动地受到保护。

自从 2017 年以来，Cloudflare 一直为我们的所有客户提供免费、不计量且无限制的 DDoS 防护。此外，我们还提供一系列附加安全功能，以满足各种规模组织的需求。如果您不确定自己是否受到保护，或想了解如何才能受到保护，请[联系我们](https://www.cloudflare.com/h2)。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F&t=HTTP%2F2%20Rapid%20Reset%EF%BC%9A%E8%A7%A3%E6%9E%84%E8%BF%99%E5%9C%BA%E7%A0%B4%E7%BA%AA%E5%BD%95%E7%9A%84%E6%94%BB%E5%87%BB)[](https://x.com/intent/post?text=HTTP%2F2+Rapid+Reset%EF%BC%9A%E8%A7%A3%E6%9E%84%E8%BF%99%E5%9C%BA%E7%A0%B4%E7%BA%AA%E5%BD%95%E7%9A%84%E6%94%BB%E5%87%BB&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://bsky.app/intent/compose?text=HTTP%2F2+Rapid+Reset%EF%BC%9A%E8%A7%A3%E6%9E%84%E8%BF%99%E5%9C%BA%E7%A0%B4%E7%BA%AA%E5%BD%95%E7%9A%84%E6%94%BB%E5%87%BB+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://mastodonshare.com/?text=HTTP%2F2+Rapid+Reset%EF%BC%9A%E8%A7%A3%E6%9E%84%E8%BF%99%E5%9C%BA%E7%A0%B4%E7%BA%AA%E5%BD%95%E7%9A%84%E6%94%BB%E5%87%BB&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://www.threads.net/intent/post?text=HTTP%2F2+Rapid+Reset%EF%BC%9A%E8%A7%A3%E6%9E%84%E8%BF%99%E5%9C%BA%E7%A0%B4%E7%BA%AA%E5%BD%95%E7%9A%84%E6%94%BB%E5%87%BB+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)

## 相关标签

[DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[攻击](https://blog.cloudflare.com/zh-cn/tag/attacks/)[漏洞](https://blog.cloudflare.com/zh-cn/tag/vulnerabilities/)[趋势](https://blog.cloudflare.com/zh-cn/tag/trends/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
