---
url: https://blog.cloudflare.com/zh-cn/python-workers-advancements/
title: Python Workers Redux\uff1a\u5feb\u901f\u51b7\u542f\u52a8\u3001\u8f6f\u4ef6\u5305\u548c uv \u4f18\u5148\u7684\u5de5\u4f5c\u6d41\u7a0b | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:47.020179+00:00
---

# Python Workers Redux：快速冷启动、软件包和 uv 优先的工作流程 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/python-workers-advancements/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Python](https://blog.cloudflare.com/zh-cn/tag/python/)

2 个标签显示 2 个标签

  * 文章标签
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Python](https://blog.cloudflare.com/zh-cn/tag/python/)
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



[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Python](https://blog.cloudflare.com/zh-cn/tag/python/)

2025年12月8日

# Python Workers Redux：快速冷启动、软件包和 uv 优先的工作流程

![Dominik Picheta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P5G8RRA9GKFZA6BYERZ1.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Mike Nomitch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462B7XNRB3FQ030XK95Y0H.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dominik Picheta](https://blog.cloudflare.com/zh-cn/author/dominik/)、[Hood Chatham](https://blog.cloudflare.com/zh-cn/author/hood/)和[Mike Nomitch](https://blog.cloudflare.com/zh-cn/author/mike-nomitch/)

阅读时间：10 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/python-workers-advancements/)、[日本語](https://blog.cloudflare.com/ja-jp/python-workers-advancements/)、[한국어](https://blog.cloudflare.com/ko-kr/python-workers-advancements/)和[繁體中文](https://blog.cloudflare.com/zh-tw/python-workers-advancements/).

![BLOG-2925 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SJ3N46YQKDZYJ6Q7M0S4.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////97e/z3eLu2+Lx4+n26+3y7uvp////////6u3119/w1eD04Oj56e317evs////////6O3509710eD53un96e/67e3w////////6/D+1eL61OT+4e7/7fP/8fH1////////8/j/3+v/3u3/6/b/9fn/9/b7/////////f//7fb/7fj/9/7//v////3/////////////+P//+P///////////////////////////P///P//////////////)

_注意：本帖已更新，提供了关于 AWS Lambda 的更多详情。_

去年，我们宣布了[ _对 Python Workers 的基本支持_](https://blog.cloudflare.com/python-workers/)，让 Python 开发人员能够使用单个命令，将 Python 部署到全球，并且可充分利用 [_Workers 平台_](https://workers.cloudflare.com/)。

从那时起，我们一直在努力，力求让 [_Workers 上的 Python 体验_](https://developers.cloudflare.com/workers/languages/python/)變得更加出色。我们一直专注于为平台提供套件支援，现在这已成为现实 — 具有极快的冷启动速度和原生 Python 开发体验。

这意味着软件包集成到 Python Worker 的方式发生了变化。我们现在对 [_Pyodide 支持的任何软件包_](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)都提供支持，而不是仅仅提供有限的内置软件包集。Pyodide 是为 Python Workers 提供支持的 WebAssembly 运行时。这包括所有纯 Python 软件包，以及许多依赖动态库的软件包。我们还围绕 [_uv_](https://docs.astral.sh/uv/) 构建了工具，来简化软件包安装。

此外，我们还实施了专用内存快照，以缩短冷启动时间。相比其他无服务器 Python 供应商，这些快照能够显著提升速度。在使用常见软件包的冷启动测试中，Cloudflare Workers 的启动速度比 **AWS Lambda 快 2.4 倍** **（未使用 SnapStart）** ，比 **Google Cloud Run 快 3 倍** 。

在这篇博文中，我们将阐释 Python Workers 的独特之处，并分享我们如何实现上述优势的一些技术细节。首先，对于那些可能不熟悉 Workers 或无服务器平台（特别是具有 Python 背景的开发者）的人，我们来分享一下您可能想要使用 Workers 的原因。

### 2 分钟内即可在全球部署 Python

Workers 之所以有魔力，部分原因在于其简洁的代码和便捷的全球部署。首先，我们展示如何通过快速冷启动，在全球各地部署 FastAPI 应用，全程不到两分钟。

只需几行代码，就能使用 FastAPI 实施一个简单的 Worker。
    
    
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

要部署类似内容，只需确保已安装 `uv` 和 `npm`，然后运行以下命令：
    
    
    $ uv tool install workers-py
    $ pywrangler init --template \
        https://github.com/cloudflare/python-workers-examples/03-fastapi
    $ pywrangler deploy

只需使用少量代码和 `pywrangler deploy`，您就能在 Cloudflare 的边缘网络部署您的应用，并且可扩展到 [_125 个国家/地区的 330 个位置_](https://www.cloudflare.com/network/)。无需担心基础设施或扩展。

而且，在许多使用案例中，Python Workers 完全免费。我们的免费计划每天提供 100,000 次请求，每次调用 10 毫秒的 CPU 时间。如需更多信息，请查看[ _文档中的定价页面_](https://developers.cloudflare.com/workers/platform/pricing/)。

有关更多示例，请查看 [_GitHub 中的存储库_](https://github.com/cloudflare/python-workers-examples)。请继续阅读，了解有关 Python Workers 的更多信息。

### 您可以使用 Python Workers 来做些什么呢？

现在您已经拥有了 Worker，一切皆有可能。代码由您来编写，所以决定权在您。您的 Python Worker 接收 HTTP 请求，并且在公共互联网上，向任何服务器发出请求。

您可以设置 cron 触发器，以便 Worker 定期运行。另外，如果您有更复杂的需求，您可以利用 [_Python Worker 的工作流_](https://blog.cloudflare.com/python-workflows/)，甚至使用 [_Durable Objects_](https://developers.cloudflare.com/durable-objects/get-started/) 长时间运行的 WebSocket 服务器和客户端。

以下是使用 Python Workers 可以执行的更多操作示例：

  * [ _使用诸如 Jinja 之类的库，在边缘渲染 HTML 模板，同时直接从您的服务器获取动态内容_](https://github.com/cloudflare/python-workers-examples/tree/main/03-fastapi)
  * [ _修改服务器响应。例如，您可以根据请求的内容，动态地将 opengraph 标签注入到 HTML 中。_](https://github.com/cloudflare/python-workers-examples/tree/main/11-opengraph)
  * [ _使用 Durable Objects 和 WebSockets 构建一个聊天室_](https://github.com/cloudflare/python-workers-examples/tree/main/15-chatroom)
  * [ _通过 WebSocket 连接使用数据，例如 Bluesky 的 Firehose_](https://github.com/cloudflare/python-workers-examples/tree/main/14-websocket-stream-consumer)
  * [ _使用 Pillow Python 软件包生成图像_](https://github.com/cloudflare/python-workers-examples/tree/main/12-image-gen)
  * [ _编写一个小型 Python Worker，用于公开 Python 软件包的 API，然后使用 RPC 通过 JavaScript Worker 来访问_](https://github.com/cloudflare/python-workers-examples/tree/main/13-js-api-pygments)



### 加速软件包冷启动

Workers 这类无服务器平台，仅在必要时运行您的代码，从而为您节省资金。这意味着，如果您的 Worker 没有收到请求，它可能会被关闭，并且需要在收到新请求时重新启动。这通常会产生资源开销，我们将其称为“冷启动”。请务必尽量缩短这些字符串，以最大程度地减少最终用户的延迟。

在标准 Python 中，启动运行时的成本很高，因此我们最初实施的 Python Workers 专注于加快 _运行时_ 的启动速度。但是，我们很快意识到这还不够。即使 Python 运行时启动迅速，在实际应用中，初始启动通常包括从软件包加载模块；遗憾的是，在 Python 中，许多常用的软件包可能需要几秒钟才能完成加载。

我们的目标是无论是否加载了软件包，能够快速进行冷启动。

为了测量真实的冷启动性能，我们建立了一个导入常用软件包的基准测试，以及一个使用裸 Python 运行时运行“hello world”的基准测试。Standard Lambda 能够快速[ _启动运行时_](https://cold.picheta.me/#bare)，但一旦需要导入软件包，冷启动时间就会显著增加。为了对此进行优化，以便在导入软件包的情况下加速冷启动，您可以在 Lambda 上使用 SnapStart（我们很快会将其添加到链接的基准测试中）。这样做会产生存储快照的费用，并且每次恢复时还会产生额外的费用。Python Workers 将自动针对每个 Python Worker，免费应用内存快照。

以下是加载三个常见软件包 ([_httpx_](https://www.python-httpx.org/)、[ _fastapi_](https://fastapi.tiangolo.com/) 和 [_pydantic_](https://docs.pydantic.dev/latest/)) 时的平均冷启动时间：

平台| 平均冷启动时间（秒）  
---|---  
Cloudflare Python Workers| 1.027  
AWS Lambda（不使用 SnapStart）| 2.502  
Google Cloud Run| 3.069  
  
在此案例中，**Cloudflare Python Workers 的冷启动速度比不使用 SnapStart 的 AWS Lambda 快 2.4 倍，比 Google Cloud Run 快 3 倍** 。我们使用内存快照，实现了较低的冷启动次数，我们将在后面的章节中阐释我们是如何做到这一点的。

我们会定期运行这些基准测试。[ _在此_](https://cold.picheta.me/#bare)获取最新数据，以及有关我们测试方法的更多信息。

在架构方面，我们与这些其他平台不同，也就是说，[ _Workers 是基于隔离的_](https://developers.cloudflare.com/workers/reference/how-workers-works/)。正因如此，我们的目标远大，并且正在规划零冷启动的未来。

### 与 uv 集成的软件包工具

Python 之所以如此令人惊叹，很大程度上归功于其多样化的软件包生态系统。因此，我们一直在努力，以确保在 Workers 中尽可能简单地使用软件包。

我们认为，使用现有的 Python 工具是获得出色开发体验的最佳途径。因此，我们选择了 `uv` 软件包和项目管理器，原因是其快速、成熟，并且在 Python 生态系统中发展势头迅猛。

我们围绕 `uv` 构建了称为 [_pywrangler_](https://github.com/cloudflare/workers-py#pywrangler) 的专属工具。此工具执行以下操作：

  * 读取 Worker 的 pyproject.toml 文件，以确定其中指定的依赖项。
  * 将依赖项包含在 Worker 的 `python_modules` 文件夹中。



Pywrangler 会以与 Python Workers 兼容的方式调用 `uv` 来安装依赖项，并在本地开发或部署 Workers 时调用 `wrangler`。

实际上，这意味着您只需要运行 `pywrangler dev` 和 `pywrangler` `deploy`，即可在本地测试并部署您的 Worker。

### 类型提示

您可以使用 `pywrangler types`，针对 Wrangler 配置中定义的所有[ _绑定项_](https://developers.cloudflare.com/workers/runtime-apis/bindings/)来生成类型提示。这些类型提示将适用于 [_Pylance_](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 或最新版本的 [_mypy_](https://mypy-lang.org/)。

为了生成类型，我们使用 [_wrangler types_](https://developers.cloudflare.com/workers/wrangler/commands/#types) 来创建 TypeScript 类型提示，然后使用 TypeScript 编译器为这些类型生成抽象语法树。最后，我们使用 TypeScript 提示（例如 JS 对象是否有迭代器字段），来生成与 Pyodide 外部函数接口协同工作的 `mypy` 类型提示。

### 使用快照来缩短冷启动时间

Python 启动通常非常缓慢，导入 Python 模块会触发大量工作。我们使用内存快照，避免在冷启动期间运行 Python 启动程序。

部署 Worker 时，我们会执行 Worker 的顶层作用域，然后拍摄内存快照，并将其与您的 Worker 一起存储。每当我们为 Worker 启动新的隔离时，我们会恢复内存快照，Worker 可随时处理请求，而无需预先执行任何 Python 代码。这显著改善了冷启动时间。例如，启动一个不使用快照的 Worker 且导入 `fastapi`、`httpx` 和 `pydantic` 等库大约需要 10 秒。使用快照则只需 1 秒。

Pyodide 基于 WebAssembly 构建，正是这一点使其成为可能。我们可轻松捕获运行时的完整线性内存并进行恢复。

#### 内存快照和熵

WebAssembly 运行时不需要像地址空间布局随机化这类安全功能，因此在现代操作系统上，与内存快照相关的大部分难题都不会出现。就像使用原生内存快照一样，我们仍然需要在启动时小心处理熵，以避免使用 [_XKCD 随机数生成器_](https://xkcd.com/221/)（我们[ _非常注重实际的随机性_](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)）。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2925 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW459DS22T0KYDPDJGGEAW3H.png&w=400&h=144&f=webp&fit=cover&position=center)

通过创建内存快照，我们可能会无意中锁定一个随机种子值。在这种情况下，未来对“随机”数的调用将在多个请求中始终返回相同的值序列。

由于 Python 在启动时会使用大量的熵，因此避免这种情况尤其具有挑战性。其中包括 libc 函数 `getentropy()` 和 `getrandom()`，以及从 `/dev/random` 和 `/dev/urandom` 中读取。所有这些函数与 JavaScript `crypto.getRandomValues()` 函数的实施相同。

在 Cloudflare Workers 中，`crypto.getRandomValues()`启动时始终处于禁用状态，以便将来我们可以转换为使用内存快照。遗憾的是，如果不调用此函数，Python 解释器将无法启动。而且许多软件包在启动时也需要熵。这种熵主要有两个用途：

  * 用于哈希随机化的哈希种子
  * 用于伪随机数生成器的种子



在启动时进行哈希随机化，并且我们接受每个特定 Worker 具有固定哈希种子的成本。Python 没有在启动后允许替换哈希种子的机制。

对于伪随机数生成器 (PRNG)，我们采取以下方法：

在部署时:

  1. 使用固定的“毒种子”为 PRNG 设定种子，然后记录 PRNG 的状态。
  2. 将所有调用 PRNG 的 API 替换为一项覆盖，该覆盖会因用户错误而导致部署失败。
  3. 执行用户代码的顶层作用域。
  4. 捕获快照。



运行时：

  1. 确认 PRNG 状态未更改。如果发生更改，说明我们忘记了某种方法的覆盖。部署因内部错误而失败。
  2. 恢复快照后，在执行任何处理程序之前，重新设定随机数生成器的种子。



这样，我们可以确保 Worker 在运行的同时能够使用 PRNG，但在初始化和预快照期间会阻止 Workers 使用。

#### 内存快照与 WebAssembly 状态

在 WebAssembly 上创建内存快照时，还会遇到一个额外的难题：我们保存的内存快照仅包含 WebAssembly 的线性内存；但是，Pyodide WebAssembly 实例的完整状态并未包含在线性内存中。

在此内存之外有两张表。

一张表用于保存函数指针的值。传统计算机使用“冯·诺伊曼”架构，这意味着代码与数据存在于相同的内存空间中，因此调用函数指针相当于跳转到某个内存地址。WebAssembly 具有“哈佛架构”，代码存在于单独的地址空间中。这是实现 WebAssembly 大部分安全保障的关键，特别是 WebAssembly 为何不需要地址空间布局随机化。在 WebAssembly 中，函数指针是指向函数指针表的索引。

第二张表保存了所有从 Python 引用的 JavaScript 对象。JavaScript 对象不能直接存储到内存中，因为 JavaScript 虚拟机禁止直接获取指向 JavaScript 对象的指针。而这些对象被存储在一个表中，并在 WebAssembly 中表示为该表的索引。

在将快照恢复为捕获快照时，我们需要确保这两个表的状态完全相同。

WebAssembly 实例初始化时，函数指针表始终处于相同状态。加载动态库时（例如 numpy 等原生 Python 包），动态加载器会更新该表。 

处理动态加载：

  1. 在拍摄快照时，我们会为加载器打补丁，以记录动态库的加载顺序、每个库的元数据在内存中分配的地址，以及用于调整的函数指针表基址。
  2. 恢复快照时，我们以相同的顺序重新载入动态链接库，并使用经过打补丁的内存分配器将元数据放置在相同的位置。我们确认，函数指针表的当前大小与我们为动态库记录的动态库的函数指针表基址相匹配。



所有这些确保在我们恢复快照后，每个函数指针都具有与拍摄快照时相同的含义。

为了处理 JavaScript 引用，我们实施了一个相当有限的系统。如果一个 JavaScript 对象可以通过一系列属性访问项，从 globalThis 进行访问，我们会记录这些属性访问项，并在恢复快照时回放。如果存在任何无法通过此方式访问的 JavaScript 物件参考，我们将无法部署 Worker。这已经足以处理所有支持 Pyodide 的现有 Python 软件包，这些软件包会执行顶级导入，例如：
    
    
    from js import fetch

### 使用分片来降低冷启动频率

Python Workers 性能策略的另一项重要特征是分片。[ _此外_](https://blog.cloudflare.com/eliminating-cold-starts-2-shard-and-conquer/)非常详细地介绍了其实施。简而言之，我们现在将请求路由到现有的 Worker 实例，而以前我们可能会选择启动一个新实例。

实际上首先会为 Python Workers 启用分片，并证明其是一个很好的测试平台。在 Python 中，冷启动的成本远高于 JavaScript。因此，务必确保将请求路由到已在运行的隔离区，这一点至关重要。

### 我们接下来该怎么办？

这仅仅是开始。我们有很多计划来改进 Python Workers：

  * 开发人员更便捷易用的工具
  * 利用我们的隔离架构，实现更快的冷启动
  * 支持更多软件包。
  * 支持原生 TCP 套接字、原生 WebSocket 及更多绑定项。



要了解有关 Python Workers 的更多信息，请查看[ _此处_](https://developers.cloudflare.com/workers/languages/python/)提供的文档。要获得帮助，请务必加入我们的 [_Discord_](https://discord.cloudflare.com/)。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpython-workers-advancements%2F&t=Python%20Workers%20Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%90%AF%E5%8A%A8%E3%80%81%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%20uv%20%E4%BC%98%E5%85%88%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B)[](https://x.com/intent/post?text=Python+Workers+Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%90%AF%E5%8A%A8%E3%80%81%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C+uv+%E4%BC%98%E5%85%88%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpython-workers-advancements%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpython-workers-advancements%2F)[](https://bsky.app/intent/compose?text=Python+Workers+Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%90%AF%E5%8A%A8%E3%80%81%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C+uv+%E4%BC%98%E5%85%88%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpython-workers-advancements%2F)[](https://mastodonshare.com/?text=Python+Workers+Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%90%AF%E5%8A%A8%E3%80%81%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C+uv+%E4%BC%98%E5%85%88%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpython-workers-advancements%2F)[](https://www.threads.net/intent/post?text=Python+Workers+Redux%EF%BC%9A%E5%BF%AB%E9%80%9F%E5%86%B7%E5%90%AF%E5%8A%A8%E3%80%81%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C+uv+%E4%BC%98%E5%85%88%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpython-workers-advancements%2F)

## 相关标签

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Python](https://blog.cloudflare.com/zh-cn/tag/python/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
