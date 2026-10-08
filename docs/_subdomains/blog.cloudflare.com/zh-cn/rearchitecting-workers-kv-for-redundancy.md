---
url: https://blog.cloudflare.com/zh-cn/rearchitecting-workers-kv-for-redundancy/
title: \u91cd\u65b0\u8bbe\u8ba1 Workers KV\uff0c\u4ee5\u63d0\u9ad8\u53ef\u7528\u6027\u548c\u66f4\u5feb\u7684\u6027\u80fd | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:58.349286+00:00
---

# 重新设计 Workers KV，以提高可用性和更快的性能 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/rearchitecting-workers-kv-for-redundancy/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)

2 个标签显示 2 个标签

  * 文章标签
  * [Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)
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



[Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)

2025年8月8日

# 重新设计 Workers KV，以提高可用性和更快的性能

![Alex Robinson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW479T0YHMKPZQQ2VAYMDQ3A.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Tyson Trautmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49JRJ6AFZ9F9S4V69Z9MFD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Robinson](https://blog.cloudflare.com/zh-cn/author/alex-robinson/)和[Tyson Trautmann](https://blog.cloudflare.com/zh-cn/author/tyson-trautmann/)

阅读时间：15 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/rearchitecting-workers-kv-for-redundancy/)和[日本語](https://blog.cloudflare.com/ja-jp/rearchitecting-workers-kv-for-redundancy/).

![BLOG-2880 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46AZKR183RVBSR2QYVMMKV.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////787/Dx4ubs4ufu6ezy7u/w7uzq//////7+7O3z3eDs2+Du5Ojz7O3y7u3s////////6+z12Nzt1tvv4OT16+z18O7w////////7u/52t3x19zz4ub57u/68/L1////////9fX+4ub24OX46+/+9fb/+fj6/////////f7/7vH87fL+9/r//v////7+////////////+Pv/+P3//////////////////////////P///f//////////////)

_此内容已使用自动机器翻译服务进行翻译，仅供您参考及阅读便利。其中可能包含错误、遗漏，或与原始英文版本存在理解方面的细微差别。如有疑问，请参考原始英文版本。_

2025 年 6 月 12 日，Cloudflare 遭遇了一次严重的服务中断，影响了我们的大量关键服务。正如我们在[ _有关该事件的博客文章_](https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/)中所解释的，原因是我们的 Workers KV 服务使用的底层存储基础设施出现故障。Workers KV 不仅为许多客户所依赖，而且还作为许多其他 Cloudflare 产品的关键基础设施，处理受影响服务的配置、身份验证和资产交付。这一基础设施的一部分由第三方云提供商提供支持，该提供商在 6 月 12 日发生了一次中断，直接影响了我们 KV 服务的可用性。

今天，我们提供对 Workers KV 改进的更新，这些改进旨在确保类似的中断不会再次发生。我们现在将所有数据存储在自己的基础设施上。除了用于冗余的任何第三方云供应商外，我们也从我们自己的基础设施满足所有请求，确保高可用性并消除单点故障。最后，这项工作显着提高了性能，并为消除对第三方提供商作为冗余备份的依赖指明了清晰的道路。

## 背景：原始架构

Workers KV 是一种全球键值存储，支持低延迟高读取量。在幕后，该服务将数据存储在区域存储中，并在 Cloudflare 的网络中缓存数据，以提供卓越的读取性能，适用于需要在全球范围内立即可用的配置数据、静态资产和用户首选项。

Workers KV 最初于 2018 年 9 月推出，其出现早于 Durable Objects 和 R2 等 Cloudflare 原生存储服务。因此，Workers KV 的原始设计利用了多个第三方云服务提供商的对象存储产品，通过提供商冗余来最大化可用性。系统以主动-主动配置运行，即使在其中一个提供商不可用、遇到错误或运行缓慢的情况下，也能成功服务请求。

对 Workers KV 的请求由 Storage Gateway Worker (SGW)处理，这是一项在 Cloudflare Workers 上运行的服务。当收到写请求时，SGW 会将键值对同时写入到两个不同的第三方对象存储提供商，确保数据始终可从多个独立的来源获得数据。对删除的处理方式类似，通过写入一个特殊的逻辑删除值来代替对象，以将键标记为已删除，这些逻辑删除随后被作为垃圾收集。

从 Workers KV 的读取通常可以从 Cloudflare 的缓存中提供，提供可靠的低延迟。对于不在缓存中读取的数据，系统会将请求与两个提供商竞速，并返回最先到达的响应，这通常来自地理位置较近的提供商。这种竞赛方法始终获得最快的响应，优化了读取延迟，同时提供针对提供商问题的恢复能力。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GEZ8SPK7ZX2PMRBEH9NF.png&w=715&h=644&f=webp&fit=cover&position=center)

鉴于使两个独立存储提供商保持同步本身就有困难，该架构包含了复杂的机制来处理后端之间的数据一致性问题。尽管有这个机制，但由于上游对象存储系统本质上不完美的可用性，以及在独立提供商之间保持完美同步面临的挑战，一致性边缘情况仍然比消费者的要求更加频繁。

多年来，系统的实现发生了显着变化，包括[ _我们去年讨论过的各种性能改进_](https://blog.cloudflare.com/faster-workers-kv/)，但基本的双提供商架构保持不变。这为 Workers KV 使用的大规模增长提供了可靠的基础，同时保持了其对全球应用程序有价值的性能特征。

## 扩展挑战和架构权衡

随着 Workers KV 使用量的激增，访问模式变得更加多样化，双提供商架构面临着越来越多的运营挑战。提供商具有截然不同的限制、故障模式、API 和操作程序，需要不断调整。

扩展问题不仅仅局限于提供商的可靠性。随着 KV 流量的增加，IOPS 总数超过了我们写入本地缓存基础设施的能力，迫使我们在从源存储获取数据时依赖于传统的缓存方法。这种转变暴露了在较小的规模上不明显的其他一致性边缘情况，因为缓存行为变得更不可预测，并且更加依赖于上游提供商的性能特征。

最终，一致性问题、提供程序可靠性差异和运营开销的组合导致我们在今年早些时候通过转移到单一对象存储提供商来降低复杂性的战略决策。做出这个决定是因为意识到了风险状况，但我们认为运营利益超过了风险，并将这视为我们开发自己的存储基础设施的一个临时的中间状态。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487STDNJZX5XSNYK30FGG9.png&w=715&h=644&f=webp&fit=cover&position=center)

不幸的是，在 2025 年 6 月 12 日，这种风险变成了现实，我们剩余的第三方云提供商经历了全球中断，导致高比例的 Workers KV 请求失败，持续时间超过两个小时。这对客户和其他 Cloudflare 服务产生了严重的影响：所有基于身份的登录均失败，Gateway 代理不可用，WARP 客户端无法连接，其他数十项服务经历了严重中断。

## 设计解决方案

事件发生后的直接目标很明确：使至少另一个完全冗余的提供商在线，以便另一个单一提供商中断不会导致 KV 关闭。新的提供商需要在几个方面处理大规模的问题：数千亿个键值对，存储的 PB 级数据，每秒数百万次的 GET 请求，每秒数万次的稳定状态 PUT/DELETE 请求，以及数千万次的高达每秒 100 亿的吞吐量，而且全部具有高可用性和低单位数毫秒内部延迟。

一个明显的选择是重新启用我们今年早些时候禁用的提供商。然而，我们不能就这样将开关拨回原来的位置。先前第三方存储提供商的双后端配置中运行的基础设施现已不复存在，代码出现了一些位腐烂，使得快速恢复到先前的双提供商设置变得不可行。

此外，另一个提供商经常成为其自身运营问题的根源，错误率相对较高，请求吞吐量限制也低得令人担忧，这使我们犹豫是否再次依赖它。最终，我们决定，我们的第二个提供商完全由 Cloudflare 所有并由 Cloudflare 运营。

下一个选项是直接在 [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/) 上构建。我们已经在 R2 上运行了一个 Workers KV 的内测版本，但这次体验帮助我们更好地了解 Workers KV 的独特存储需求。Workers KV 流量模式的特点是包含数千亿个小对象，大小中值仅 288 字节，与假定文件大小较大的典型对象存储工作负载大不相同。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48R0NVZQWBCCR3FDZ6QFNB.png&w=715&h=536&f=webp&fit=cover&position=center)

对于以这种规模的低于 1KB 的对象为主的工作负载，数据库存储比传统的对象存储显着提高效率和成本效益。当您需要以最小的每个值开销存储数十亿个非常小的值时，数据库在架构上是最适合的。我们正在努力针对 R2 进行优化，例如使用元数据内联小对象，以消除额外的检索跃点，从而提高小对象的性能，但对于我们的直接需求，由数据库支持的解决方案提供了最有希望的前进路径。

在对各种可能方案进行全面评估后，我们决定使用 Cloudflare 生产中已经投入使用的一个分布式数据库。R2 和 Durable Objects 在幕后使用同一个数据库，这给了我们几项关键优势：我们拥有深厚的内部专业知识和现有的部署和运营自动化，而且我们知道可以大规模依赖其可靠性和性能特征.

我们将数据分布到多个数据库集群，每个集群都配置三向复制，以提高持久性和可用性。这种方法使我们能够水平扩展容量，同时在每个分片内保持强大的一致性保证。我们选择运行多个集群而不是一个庞大的系统，以避免在任何集群变得不健康时产生更小的影响范围，并避免在 Workers KV 继续增长时单集群可扩展性的实际极限。

## 实施解决方案

在实施这个系统时，我们遇到的一个直接挑战是连接性。SGW 需要与我们的核心数据中心中运行的数据库集群进行通信，但数据库通常通过持久的 TCP 连接使用二进制协议，而不是在我们的全球网络中高效工作、基于 HTTP 的通信模式。

我们构建了 KV 存储代理（KVSP）来弥补这一不足。KVSP 服务提供了一个 HTTP 接口，我们的 SGW 可以使用这个接口在幕后管理复杂的数据库连接、身份验证和分片路由。KVSP 使用一致的哈希值在多个集群之间条带化命名空间，防止形成热点（即流行的命名空间可能压垮单个集群），消除嘈杂的邻居问题，并确保容量限制是分布式的，而不是集中的。

使用分布式数据库来存储 Workers KV 的最大缺点是，虽然它擅长处理在 KV 流量中占主导地位的小对象，但对于偶尔存储高达 25 MiB 的大值（有些用户有高达 25 MiB）的情况而言，这并不是最佳选择。我们对任一用例都不妥协，而是扩展了 KVSP，使其自动将较大的对象路由到 Cloudflare R2，从而创建一种混合存储架构，根据对象特征优化后端选择。从 SGW 的角度来看，这种复杂性是完全透明的——相同的 HTTP API 适用于所有对象，无论大小如何。

我们还恢复了 KV 先前架构中的存储提供商之间的双提供商功能，并对它们进行了调整，使其能够很好地与 KV 降级为单一提供商以来对 KV 实施进行的更改协同工作。修改后的系统现在通过同时向两个后端进行竞时写入来运行，但一旦第一个后端确认写入，就会将成功返回给客户端。

这一改进可以最大限度地减少延迟，同时确保在两个系统上的持久性。当一个后端成功而另一个后端失败时——由于临时网络问题、速率限制或服务降级——失败的写入将排队等待后台协调，这是我们同步机制的一部分，下文将详细介绍。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45KJ2Y35VN07E7C94MJZV8.png&w=715&h=882&f=webp&fit=cover&position=center)

## 部署解决方案

实施混合架构后，我们开始了一个谨慎的推出流程，旨在验证新系统的同时维持服务可用性。

第一步是从 SGW 向新的 Cloudflare 后端引入后台写入。这使我们能够验证实际生产负载下的写入性能和错误率，而不影响读取流量或用户体验。这也是将所有数据复制到新后端的必要步骤。

接下来，我们将现有数据从第三方提供商复制到在 Cloudflare 基础设施上运行的新后端，并通过 KVSP 路由数据。这为我们带来了一个关键的里程碑：现在，如果发生另一个提供商中断的情况，我们可以在几分钟内手动将所有操作故障转移到新的后端。导致 6 月事件的单点故障已经消除。

出于对故障转移能力的信心，我们开始以主动-主动模式启用我们的首批命名空间，从内部 Cloudflare 服务开始，我们对那里的工作负载进行了复杂的监控和深入了解。我们谨慎地比较了后端之间的结果，非常缓慢地增加流量。事实上，SGW 可以在向用户返回响应后，能够异步地查看来自两个后端的响应，让我们能够执行详细的比较并捕捉任何差异，而不影响面向用户的延迟。

在测试过程中，与单一提供商的设置相比，我们发现了一个重要的一致性倒退，这导致我们短暂地回滚了将命名空间置于主动-主动模式的更改。虽然 Workers KV[ _在设计上是最终一致的_](https://developers.cloudflare.com/kv/concepts/how-kv-works/)，随着缓存版本超时，更改需要最多 60 秒时间传播到全球，但对于通过相同 Cloudflare 入网点路由的请求，我们无意中降低了自写（RYOW）一致性。 .

在之前的双提供商主动-主动设置中，我们在每个 PoP 中提供 RYOW，因为我们将 PUT 操作直接写入本地缓存，而不是依赖于上游存储之前的传统缓存系统。然而，KV 吞吐量超过了缓存基础设施可以支持的 IOPS 数量，因此我们不能再依赖这种方法了。这并非 Workers KV 的文档属性，但某些客户在其应用程序中开始依赖这种行为。

为了了解这个问题的范围，我们创建了一个对抗性测试框架，通过从世界各地的少数几个位置快速分散对一小组键的读写，来最大化达到一致性边缘情况的可能性。这个框架让我们能够衡量观察到 RYOW 一致性违规的读取百分比：来自同一入网点的写入操作之后紧接着的读取操作，将返回过期数据，而不是刚刚写入的值。这允许我们设计并验证一种新的方法来 KV 如何填充和使缓存中的数据失效，它恢复了客户期望的 RYOW 行为，同时保持了使 Workers KV 有效处理高读工作负载的性能特征。

## KV 如何保持跨多个后端的一致性

由于写入竞相传输到两个后端，以及读取可能返回不同结果，在独立存储提供商之间维护数据一致性需要一种复杂的多层方法。虽然细节上随着时间的推移而不断演变，但 KV 始终采用相同的基本方法，即三种互补的机制相互配合，以减少出现不一致的可能性，并最小化数据发散的窗口。

第一道防线在写操作期间发生。当 SGW 同时向两个后端发送写入时，一旦任何一个提供商确认持久性，我们就会认为该写入成功。然而，如果一个写入在一个提供商上成功，但在另一个上失败——由于网络问题、速率限制或暂时的服务降级——失败的写入被捕获并将发送到后台协调系统。该系统会删除失败密钥的重复数据，并启动同步过程以解决不一致问题。

第二种机制在读操作期间激活。当 SGW 与两个提供商进行读取竞赛并获得不同的结果时，它会触发相同的后台同步过程。这有助于确保使变得不一致的键在首次访问时恢复对齐，而不是无限期地保持分歧。

第三层由后台爬虫组成，它们持续扫描两家提供商的数据，识别并修复被前面的机制遗漏的任何不一致性。这些爬虫还提供了关于一致性偏移率的宝贵数据，帮助我们了解密钥有多频繁地通过反应机制并解决任何根本问题。

同步过程本身依赖于我们附加到每个键值对的版本元数据。每次写入都会自动生成一个新版本，由一个高精度时间戳和一个随机数组成，并与实际数据一起存储。在比较提供商之间的值时，我们可以根据这些时间戳确定哪个版本更高。然后，将较新的值复制到具有旧版本的提供商。

在时间戳之间的偏差在毫秒以内的极少数情况下，时钟偏差在理论上可能会导致错误的排序，但考虑到我们通过[ _Cloudflare 时间服务_](https://www.cloudflare.com/time/)对时钟维护的严格范围，以及典型的写入延迟，此类冲突只有在几乎同时进行重叠写入操作时才会发生。

为了防止同步期间的数据丢失，我们使用条件写入，在写入之前验证最后的时间戳是否较旧，而不是盲目地覆盖值。如果距离很近的请求成功发送到不同的后端，并且同步过程将旧值复制到较新的值，这样我们就可以避免引入新的不一致问题。

同样，我们不能在用户请求时就删除数据，因为如果删除只在一个后端成功，同步过程会将此视为丢失数据，并从另一个后端复制。相反，我们使用具有较新时间戳的逻辑删除而非实际数据来覆盖该值。只有在双方都获得了逻辑删除之后，我们才会继续实际从存储中移除密钥。

这种分层一致性架构并不能保证强一致性，但在实践中，它确实消除了后端之间的大多数不匹配情况，同时保持了一个性能特征，这使 Workers KV 对延迟敏感的高读取工作负载具有吸引力，同时还提供了任何后端不匹配时的高可用性。后端错误。用分布式系统的术语来说，KV 选择了[ _CAP 定理_](https://en.wikipedia.org/wiki/CAP_theorem)中的可用性 (AP) 而不是一致性 (CP)，更有趣的是，在没有分区的情况下，它在[ _PACELC 定理_](https://en.wikipedia.org/wiki/PACELC_design_principle)下选择延迟而不是一致性，这意味着它是 PA/EL 。通过反应机制，大多数不一致问题都能在几秒钟内解决，而后台爬虫确保即使是边缘情况通常也会随着时间的推移得到纠正。

上述描述适用于我们历史的双提供商设置和今天的实施，但当前架构中的两项关键改进显着改善了一致性。首先，与我们之前的第三方提供商相比，KVSP 保持了低得多的稳定状态错误率，从而减少了造成不一致的写入失败的频率。其次，我们现在对两个后端进行所有读取竞赛，而之前的系统通过在初始学习期后优先将读取操作路由到单个提供商来优化成本和延迟。

在原始双提供商架构中，每个 SGW 实例最初将与两个提供商进行读取竞赛，以确定基准性能特征。一旦实例确定一个提供商在其地理区域内始终优于另一个提供商，它就会将后续的读取专门路由到更快的提供商，仅在主服务器发生故障或异常延迟时回退到较慢的提供商。虽然这种方法有效控制了第三方提供商的成本并优化了读取性能，但它在我们的一致性检测机制中造成了一个重大盲点——如果始终仅从一个后端提供读取服务，则提供商之间的不一致性可能会无限期地存在。

## 结果：性能和可用性提升

凭借这些一致性机制，以及通过内部服务验证的谨慎部署策略，我们继续将主动-主动操作扩展到跨内部和外部工作负载的更多命名空间，所看到的效果让我们感到非常兴奋。新架构不仅为 Workers KV 提供了所需的更高可用性，还带来了显着的性能提升。

作为我们新存储后端的所在地，这些性能提升在欧洲尤其明显，但其好处远远超出了仅地理位置所能解释的范围。与我们并行写入的第三方对象存储相比，内部延迟改善非常显着。

例如，KVSP 读取的 p99 内部延迟低于 5 毫秒。相比之下，在对传输时间进行标准化以进行同类比较后，从我们最近的位置对第三方对象存储进行的非缓存读取通常约为 80 毫秒，第 50 名和第 99 位为 200 毫秒。

下图显示了我们能得到的最接近的同类比较：我们观察到的对 KVSP 的请求的内部延迟，与对缓存未命中并最终从 DNS 转发到外部服务提供商的请求的观察到的延迟。的延迟，其中包括额外的 5-10 毫秒请求传输时间。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW483RS4DV6QADAXAD3G6HBA.png&w=715&h=413&f=webp&fit=cover&position=center)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46DHWAAT9MQMN1437121N6.png&w=715&h=417&f=webp&fit=cover&position=center)

这些性能改进直接转化为许多依赖 Workers KV 的内部 Cloudflare 服务的响应时间更快，为我们的平台创造了连锁反应。事实证明，经过数据库优化的存储对于在 Workers KV 流量中占主导地位的小对象访问模式特别有效。

在看到这些积极的结果后，我们继续扩大推广，为内部和外部客户复制数据并启用命名空间组。可用性增强与性能优化的结合验证了我们的架构方法，并展示了在我们自有平台上构建关键基础设施的价值。

## 接下来？

我们近期的计划重点是扩展这种混合架构，为 Workers KV 提供更强大的韧性和性能。我们正在将 KVSP 解决方案推广到更多地点，创建一个真正的全球分布式后端，它可以完全从我们自己的基础设施服务流量，同时努力进一步加快我们在提供商之间以及在写入后在缓存中达到一致性的速度。

我们的最终目标是完全消除我们现存的第三方存储依赖，实现 Workers KV 完全独立于基础设施。这将消除导致 6 月事件的外部单点故障，同时让我们完全控制存储层的性能和可靠性特征。

除了 Workers KV 之外，该项目还展示了混合架构的强大功能，这种架构结合了不同存储技术的最佳方面。我们开发的模式（使用 KVSP 作为转换层，根据大小特征自动路由对象，以及利用我们现有的数据库专业知识）可以被其他需要平衡全球规模与强一致性要求的服务利用。从单一提供商设置到在 Cloudflare 基础设施上运行的弹性混合架构的历程，表明深思熟虑的工程团队能够将运营挑战转化为竞争优势。凭借显着提高的性能和主动冗余，Workers KV 已做好准备为越来越多依赖它的客户提供一个更可靠的基础。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frearchitecting-workers-kv-for-redundancy%2F&t=%E9%87%8D%E6%96%B0%E8%AE%BE%E8%AE%A1%20Workers%20KV%EF%BC%8C%E4%BB%A5%E6%8F%90%E9%AB%98%E5%8F%AF%E7%94%A8%E6%80%A7%E5%92%8C%E6%9B%B4%E5%BF%AB%E7%9A%84%E6%80%A7%E8%83%BD)[](https://x.com/intent/post?text=%E9%87%8D%E6%96%B0%E8%AE%BE%E8%AE%A1+Workers+KV%EF%BC%8C%E4%BB%A5%E6%8F%90%E9%AB%98%E5%8F%AF%E7%94%A8%E6%80%A7%E5%92%8C%E6%9B%B4%E5%BF%AB%E7%9A%84%E6%80%A7%E8%83%BD&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frearchitecting-workers-kv-for-redundancy%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frearchitecting-workers-kv-for-redundancy%2F)[](https://bsky.app/intent/compose?text=%E9%87%8D%E6%96%B0%E8%AE%BE%E8%AE%A1+Workers+KV%EF%BC%8C%E4%BB%A5%E6%8F%90%E9%AB%98%E5%8F%AF%E7%94%A8%E6%80%A7%E5%92%8C%E6%9B%B4%E5%BF%AB%E7%9A%84%E6%80%A7%E8%83%BD+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frearchitecting-workers-kv-for-redundancy%2F)[](https://mastodonshare.com/?text=%E9%87%8D%E6%96%B0%E8%AE%BE%E8%AE%A1+Workers+KV%EF%BC%8C%E4%BB%A5%E6%8F%90%E9%AB%98%E5%8F%AF%E7%94%A8%E6%80%A7%E5%92%8C%E6%9B%B4%E5%BF%AB%E7%9A%84%E6%80%A7%E8%83%BD&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frearchitecting-workers-kv-for-redundancy%2F)[](https://www.threads.net/intent/post?text=%E9%87%8D%E6%96%B0%E8%AE%BE%E8%AE%A1+Workers+KV%EF%BC%8C%E4%BB%A5%E6%8F%90%E9%AB%98%E5%8F%AF%E7%94%A8%E6%80%A7%E5%92%8C%E6%9B%B4%E5%BF%AB%E7%9A%84%E6%80%A7%E8%83%BD+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frearchitecting-workers-kv-for-redundancy%2F)

## 相关标签

[Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
