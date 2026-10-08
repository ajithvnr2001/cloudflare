---
url: https://blog.cloudflare.com/zh-cn/migrating-cdnjs-to-serverless-with-workers-kv/
title: \u5229\u7528 Workers KV \u5c06 cdnjs \u8fc1\u79fb\u5230\u65e0\u670d\u52a1\u5668 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:48:39.024838+00:00
---

# 利用 Workers KV 将 cdnjs 迁移到无服务器 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/migrating-cdnjs-to-serverless-with-workers-kv/

[博客](https://blog.cloudflare.com/zh-cn/)

[CDNJS](https://blog.cloudflare.com/zh-cn/tag/cdnjs/)[Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)+2再显示 2 个标签

5 个标签显示 5 个标签

  * 文章标签
  * [Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)
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



[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)

[CDNJS](https://blog.cloudflare.com/zh-cn/tag/cdnjs/)[Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)

2020年9月10日

# 利用 Workers KV 将 cdnjs 迁移到无服务器

![Tyler Caslin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PE9E2K1F7K33FKX1N2NN.JPG&w=64&h=64&f=webp&fit=cover&position=center)

[Tyler Caslin](https://blog.cloudflare.com/zh-cn/author/tyler/)

阅读时间：10 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/migrating-cdnjs-to-serverless-with-workers-kv/)和[日本語](https://blog.cloudflare.com/ja-jp/migrating-cdnjs-to-serverless-with-workers-kv/).

![Migrating cdnjs to serverless with Workers KV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4576BK2TKQG81VD605TZ1W.png&w=1200&h=713&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////+9vf37/Lz8fX09vn29ffy8O/r/////Pz97e734uXz4+fx6u3x7e7u6+rp///++fj85uf41tr01dnw3uHt5ebq5+bo////+/r/5uj81Nj309fz3d/v5ubs6ejr////////7/H/4OT94OT66ev38PD08fDx/////////v//9Pf/9fn//P///////Pv6////////////////////////////////////////////////////////////////)

Cloudflare 为 [cdnjs](https://cdnjs.com/) 提供支持，这个开源项目通过利用 [Cloudflare 的网络](https://www.cloudflare.com/cdn/)提供流行的 JavaScript 库和资源，从而给网站加速。自 [12 月发布重要更新](https://blog.cloudflare.com/an-update-on-cdnjs/)以来，我们专注于改造 cdnjs 以实现可扩展性和弹性。今天，我们很高兴宣布 Cloudflare 如何利用 [Cloudflare Workers](https://developers.cloudflare.com/workers/) 以及它的键值存储 [Workers KV](https://developers.cloudflare.com/workers/reference/storage) 来交付 cdnjs（迁移到无服务器基础架构）！

什么是 cdnjs？

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - FiO5Hb](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497NYNR078HBR44EV2BV6V.png&w=715&h=213&f=webp&fit=cover&position=center)

对于感觉陌生的人来说，cdnjs 是一个描述面向 JavaScript（JS）的内容交付网络（CDN）的首字母缩写词。[CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) 是一个由地理上分散的服务器构成的网络，主要用于提供互联网内容，不论这些内容是回忆、小猫视频还是 HTML 网页。而本文所说的 CDN 是指 Cloudflare 那个由 200 多个分布于全球的数据中心构成并且[依然在不断壮大的网络](https://blog.cloudflare.com/cloudflare-network-expands-to-more-than-100-countries/)。

这与您相关的原因在于：它使页面加载时间快如闪电。您访问的每个网站基本上都需要获取 JS 库才能加载，也包括本网站。假设您要一个位于悉尼的网站，它包含一个来自 jQuery 的本地文件。jQuery 是一个流行的库，可见于 [76.2%](https://w3techs.com/technologies/details/js-jquery) 的网站。如果您位于纽约，那么可能会注意到一个延迟，因为获取这个文件所需的时间轻易会超过 300ms，更不用说 [TLS 握手](https://blog.cloudflare.com/tls-1-3-overview-and-q-and-a/)涉及的往返时间了。不过，如果该网站使用 [cdnjs.cloudflare.com](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js) 来引用 jQuery，您可以从 Cloudflare 距您最近的布法罗数据中心检索这个文件，将延迟缩短到闪电般的 20ms。

尽管 cdnjs 在幕后运作，但有[超过 11%](https://w3techs.com/technologies/overview/content_delivery) 的网站使用它，使互联网变得更加快速、更加可靠。在 7 月份，cdnjs 服务了将近 [1900 亿个请求](https://github.com/cdnjs/cf-stats/blob/master/2020/cdnjs_July_2020.md)，涉及的数据量达到了 3.46PB。

### 文件存储在哪里？

![](http://staging.blog.mrk.cfdata.org/content/images/2020/09/image5-2.png)

cdnjs 加快了互联网速度，凭借的当然不是魔法！

在过去，Cloudflare 某个核心数据中心的若干[负载均衡](https://www.cloudflare.com/load-balancing/)服务器会定期从后备存储中提取 cdnjs 文件，充当 cdnjs.cloudflare.com 的源站。有人请求了新文件时，Cloudflare 会将它[缓存](https://www.cloudflare.com/learning/cdn/what-is-caching/) ，从而能够从我们的任何数据中心快速获取到这个文件。

后备存储是 JS、CSS 和其他 Web 库的目录，采用开源 [GitHub](https://github.com/) 存储库的形式。这意味着，包括您在内的任何人都可以出力贡献，但要经过审核和其他流程。

然而，到最近为止，这些现有操作还是劳动密集型的，并且比较脆弱。

这篇博客帖子将解释为什么我们改变 cdnjs 背后的基础架构，以使其更快速、更可靠，并且更容易维护。首先，我们将讨论社区过去如何为 cdnjs 做出贡献，同时概述旧系统的痛处和问题。接着，我们将探讨迁移到 Workers KV 的好处。然后，我们将深入解析新架构，以及对网站和 cdnjs API 的升级。最后，我们将回顾 cdnjs 的历史，并且展望它的未来。

### 如果认为自己知道如何提交 PR，请再思考

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - PNpgyB](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48510XP89XK4P61KNB9N68.png&w=715&h=643&f=webp&fit=cover&position=center)

对于非技术读者，拉取请求（PR）是一种用来合并您对存储库所做更改的请求。往常的话，如果您想将自己的 JavaScript 库包含到 cdnjs 中，首先要在 GitHub 上创建对 [cdnjs/cdnjs](https://github.com/cdnjs/cdnjs) 的 PR，附上一个描述您的程序包的 JSON 文件以及您想包括的任何版本的其他文件。在您的 PR 获得我们[旧版机器人](https://github.com/PeterBot)的批准，通过了人工审核，并且被维护人员合并后，您的程序包就与 cdnjs 集成在一起了。

貌似很简单，对吧？只要复刻存储库，克隆一下并复制粘贴几个文件，不是吗？

没错。如果您有几个小时的时间来刻录一个区分大小写的文件系统，并且有几百 GB 的可用磁盘空间来 [git clone](https://git-scm.com/docs/git-clone) 300GB 的存储库，那么贡献很简单。时间不够也没问题，您随时可以利用高阶的 [git sparse-checkout](https://git-scm.com/docs/git-sparse-checkout) 知识来完成这项工作。不懂 git？只需通过 GitHub 的 UI 逐个添加文件便可。

我猜您想到点上了。我当然知道，我可是天真地花了 10 个小时克隆存储库，结果却发现 macOS 默认为不区分大小写。

但是，更新 cdnjs 不仅对贡献者来说很困难，对维护人员来说也不容易。在过去，社区能够直接贡献版本文件，这些文件有可能是恶意的。这给维护人员带来许多工作，他们需要手动检视每个文件，与官方库源文件进行[比较](https://man7.org/linux/man-pages/man1/diff.1.html)，并运行恶意软件检查。

那么，程序包在 cdnjs 中后如何更新？在描述每个程序包的 JSON 文件中，有一个可选的自动更新定义，它会告诉机器人在哪里寻找库的新版本。如果存在这个定义，那么您的程序包从 npm 或 GitHub 发布新版本时，机器人会下载新版文件，并推送至 [cdnjs/cdnjs](https://github.com/cdnjs/cdnjs)，同时将计算的[子资源完整性](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)（SRI）哈希推送到 [cdnjs/SRIs](https://github.com/cdnjs/SRIs)。如果缺少自动更新属性，那么您要负责手动提交 PR，从而用任何新的版本更新 cdnjs。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - zfYiq2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW453YW4QHFP208HT4W8AP37.png&w=715&h=271&f=webp&fit=cover&position=center)

### cdnjs 的警示

今年 4 月，在维护我们一个核心数据中心的过程中，技术人员不慎断开了一些电缆，它们提供了连到我们其他数据中心的所有外部连接，因此导致该数据中心离线约四个小时。[这个事故](https://blog.cloudflare.com/cloudflare-dashboard-and-api-outage-on-april-15-2020/)是向 cdnjs 发出的第一个警示，特别是因为受影响的数据中心承载了主要的 cdnjs 源站 Web 服务器。在这一事件中，我们确实有在外部提供商那里运行的备份，但真正救了我们的是 Cloudflare 的全球缓存，它最大程度地减少了停机的影响，只有未缓存的资产才无法加载。

我们开始思考如何才能改进 cdnjs 服务的可靠性和性能。目光直接投向了 [Cloudflare Workers](https://workers.cloudflare.com/) 这个我们自己为[边缘网络](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)上开发提供的平台。Workers 内置了功能强大的工具 [Workers KV](https://developers.cloudflare.com/workers/reference/storage)，它是一个针对高读取应用程序进行了优化的低延迟、全球分布的键值存储。

我们通过推理发现，不用拉取 [cdnjs/cdnjs](https://github.com/cdnjs/cdnjs) 存储库并从磁盘提供文件，而可以彻底告别物理服务器，将数据分布到全球并直接从边缘提供文件。这样，cdnjs 将能够从任何原始数据中心故障中恢复，同时还可以提高其可扩展性。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - e4r84j](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48943QPE0AVV66JXMBS2M4.png&w=715&h=366&f=webp&fit=cover&position=center)

### Workers KV 前来拯救

乍一看，决定使用 Workers KV 是件明摆着的事。既然 cdnjs 中的文件永不更改，但需要频繁读取，那么 Workers KV 就非常适合。

但是，在计划迁移时我们开始担心，cdnjs 中的资产数量有 700 万多，无疑会存在超过 [Workers KV 10MiB 限值](https://developers.cloudflare.com/workers/about/limits/)的文件。经过调查，我们发现数百个 cdnjs 文件大小超限，其中大多数是 [JavaScript 源映射](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map)。

后来，我们想到了一个主意。将 Cdnjs 文件的压缩版本存储在 Workers KV 中，这不仅能解决文件大小超限问题，还可优化文件的服务方式。

如果您支付过互联网账单，就会知道[带宽有多么昂贵](https://blog.cloudflare.com/the-relative-cost-of-bandwidth-around-the-world/)！因此，所有现代浏览器都会尽可能[获取压缩的 Web 内容](https://blog.cloudflare.com/efficiently-compressing-dynamically-generated-53805/)。同样在 Cloudflare，我们经常试验通过[即时压缩](https://blog.cloudflare.com/results-experimenting-brotli/)来减小我们的带宽，只要被接受，我们就将压缩后的内容提供给浏览者。结果，我们决定提前压缩所有 cdnjs 文件，并将它们以最佳的 [Brotli](https://github.com/google/brotli) 和 [gzip](https://www.gzip.org/) 形式写入 Workers KV。这样，我们可以使用比即时压缩时更高的压缩级别，因为不再有延迟方面的要求。

如此一来，我们可以更快的速度提供更小的 cdnjs 文件！

[![](http://staging.blog.mrk.cfdata.org/content/images/2020/09/image7-1.png)](http://staging.blog.mrk.cfdata.org/content/images/2020/09/image7-1.png)

### 全面改造 cdnjs

现在，如果您要将自己的 JavaScript 库包含在 cdnjs 中，首先在 GitHub 上创建一个对我们新存储库 [cdnjs/packages](https://github.com/cdnjs/packages) 的 PR。这个存储库很容易克隆，大小仅为 50MB，由数千个 JSON 文件构成，各自描述一个 cdnjs 程序包并说明如何从 npm 或 git 自动更新。当您的文件获得我们新版自动 CI 的验证（由[新版机器人](https://github.com/cdnjs/tools)提供支持），并由维护人员进行合并后，您的程序包就会自动登记到我们的自动更新服务中。

新系统优先考虑了安全性和可维护性。首先，cdnjs 版本文件由我们的机器人创建，最大程度降低了合并新版本时出现人为错误的可能。虽然 JSON 文件是由易错的人类添加到 [cdnjs/packages](https://github.com/cdnjs/packages) 中的，但会经过机器人的检查，然后再由维护人员审批。每个文件都会对照 [JSON 架构](https://github.com/cdnjs/tools/blob/master/schema_human.json)自动验证，另外也会检查在 npm 或 GitHub 上流行程度。

当机器人发现新版本时，它会将文件的 Brotli 和 gzip 压缩版本推送到 Workers KV 中的文件命名空间。对于每个条目，机器人会在 [Workers KV 中写入一些元数据](https://blog.cloudflare.com/catching-up-with-workers-kv/)，用于 [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) 和 [Last-Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified) HTTP 标头。与之前类似，机器人也会计算未压缩文件的[子资源完整性](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)（SRI）哈希，但现在将它们推送到 Workers KV 中的 SRI 命名空间。

然后，有人从 cdnjs.cloudflare.com 请求新文件时，[Cloudflare Worker](https://developers.cloudflare.com/workers/) 会检查客户端的 [Accept-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding) 标头，并从 Workers KV 中获取 Brotli 或 gzip 压缩版本及其 ETag 和 Last-Modified 元数据。当压缩文件通过 Cloudflare 返回时，它将缓存下来以备日后请求时使用，同时也根据需要即时解压缩。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - vmYm4e](https://blog.cloudflare.com/_emdash/api/media/file/01KW45K24P6V4PZD433M522FCE.gif)

目前，仍有少数文件超过了 Workers KV 的大小限制。因此，如果 Cloudflare Worker 未能从 Workers KV 检索到文件，它会从原始 git 存储库支持的源站中获取文件。在接下来几个月中，我们计划逐步移除此基础架构。

### 扩展网站和 API

除了核心 cdnjs 基础架构之外，它的许多其他组件也得到了升级！

在 cdnjs 项目的[主页](https://cdnjs.com/)上，您会看到一个漂亮的[新 Beta 网站](https://github.com/cdnjs/static-website)。这个 Beta 网站由 [Matt](https://github.com/mattipv4) 开发，采用了 [Vue](https://vuejs.org/) 和 [Nuxt](https://nuxtjs.org/)，全部通过 [cdnjs API](https://cdnjs.com/api) 提供支持。因此，它始终会更新最新的程序包信息，而且为网站服务时需要使用的资源也较少（加载第一页之后完全在客户端一侧运行），这有助于我们随着 cdnjs 的不断成长而扩展。

实际上，cdnjs API 也从采用无服务器架构中获益，加强了可扩展性，这个架构与我们在 cdnjs 和 Workers KV 中看到的非常接近。

在迁移到 Workers KV 之前，cdnjs API 依赖于一个定期计划的流程，这个流程会生成大约 300MB 元数据。然后，cdnjs API 的后端会将这个巨大的 “package.min.js”文件提取到内存中，并使用它来运行该 API。如果您好奇的话，该文件仍托管在[此处](https://storage.googleapis.com/cdnjs-assets/package.min.js)，但请注意，它可能会拖累您的浏览器！同样，文件 SRI 推送到了 [cdnjs/SRIs](https://github.com/cdnjs/SRIs)，由 API 在本地克隆以服务 SRI 响应。

在所有 cdnjs 文件（在允许的大小限制内）转移到 Workers KV 之后，这些旧流程变得不可持续，因为需要数百万次读取和不合理的时间。因此，我们决定将找到的所有元数据上传到 Workers KV 中。我们将元数据分拆到四个名称空间中：一个用于程序包级元数据，一个用于版本特定元数据，一个包含聚合元数据，另一个则用于文件 SRI。

与 cdnjs 的无服务器设计类似，Cloudflare Worker 驻留在 [metadata.speedcdnjs.com](http://metadata.speedcdnjs.com/packages) 上，使用多个公共端点来提供 Workers KV 中的数据。目前，cdnjs API 已经和这些端点完全集成，能够随着 cdnjs 的继续扩展而提供优雅的解决方案。

### 公开透明和 cdnjs 的未来

自 2011 年 1 月诞生以来，cdnjs 一直深深扎根于公开透明，从社区汲取力量。即使 cdnjs 在规模上暴增，并且其创始人 Ryan Kirkman 和 Thomas Davis [与我们在 2011 年 6 月确立合作关系](https://blog.cloudflare.com/cdnjs-community-moderated-javascript-librarie/)后，这个项目依然在 [GitHub](https://github.com/cdnjs/) 保持完全开源。

随着时间流逝，创始人越来越难以保持活跃，因此这个项目重度依赖于社区的支持。由于几乎没有任何预算，对存储库的访问也极少，核心 cdnjs 维护人员每天都面临着项目存续的挑战。

去年，这样的局面促使我们联系了创始人，[他们愉快地接受了我们对项目的协助](https://news.ycombinator.com/item?id=21416614)。随着 Cloudflare 发挥更大的作用，cdnjs 变得与往常一样稳定，拥有来自 Cloudflare 和社区的多位[活跃成员](https://cdnjs.com/about)。

但是，由于我们不再依赖旧系统，而且也将文件存储到了 Workers KV 中，人们开始担心 cdnjs 日后会转变为专有性质。不用担心，我们正在努力确保 cdnjs 保持尽可能透明和开源。为了帮助社区审核对 Workers KV 的更新，我们建立了一个新的存储库 [cdnjs/logs](https://github.com/cdnjs/logs)，供机器人用于记录所有与 Worker KV 相关的事件。此外，任何人都可通过从 cdnjs API 提取 SRI 来验证 cdnjs 文件的完整性。

### 结论

总体而言，去年对 cdnjs 来说是一个动荡的时期，但所有缺点成为了帮助我们构建更好系统的警示信号。最近，我们将 cdnjs 迁移到了无服务器基础架构，并将它的文件存储在 [Workers KV](https://developers.cloudflare.com/workers/reference/storage) 中，缓解了依赖于单一位置上物理服务器的风险。

今天，cdnjs 运作良好，不会在短期内消失。在此，我们向维护人员 [Sven](https://github.com/xtuc) 和 [Matt](https://github.com/mattipv4) 表示感谢，谢谢他们给予这个项目巨大的力量，处理从扩展 cdnjs 到编辑这篇帖文等一切工作。

展望未来，我们会致力于使 cdnjs 尽可能公开透明。在继续改进 cdnjs 的过程中，我们也会发表更多帖文，让社区掌握最新的消息。如果您有兴趣，请订阅我们的博客。毕竟，是社区造就了 cdnjs！特别感谢我们活跃的 GitHub 贡献者和 [cdnjs 社区论坛成员](https://github.com/cdnjs/cdnjs/discussions/)，感谢你们一直与我们同甘共苦！

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F&t=%E5%88%A9%E7%94%A8%20Workers%20KV%20%E5%B0%86%20cdnjs%20%E8%BF%81%E7%A7%BB%E5%88%B0%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8)[](https://x.com/intent/post?text=%E5%88%A9%E7%94%A8+Workers+KV+%E5%B0%86+cdnjs+%E8%BF%81%E7%A7%BB%E5%88%B0%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)[](https://bsky.app/intent/compose?text=%E5%88%A9%E7%94%A8+Workers+KV+%E5%B0%86+cdnjs+%E8%BF%81%E7%A7%BB%E5%88%B0%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)[](https://mastodonshare.com/?text=%E5%88%A9%E7%94%A8+Workers+KV+%E5%B0%86+cdnjs+%E8%BF%81%E7%A7%BB%E5%88%B0%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)[](https://www.threads.net/intent/post?text=%E5%88%A9%E7%94%A8+Workers+KV+%E5%B0%86+cdnjs+%E8%BF%81%E7%A7%BB%E5%88%B0%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)

## 相关标签

[CDNJS](https://blog.cloudflare.com/zh-cn/tag/cdnjs/)[Cloudflare Workers KV](https://blog.cloudflare.com/zh-cn/tag/cloudflare-workers-kv/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Tyler Caslin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PE9E2K1F7K33FKX1N2NN.JPG&w=64&h=64&f=webp&fit=cover&position=center)[Tyler Caslin](https://blog.cloudflare.com/zh-cn/author/tyler/)

[](https://github.com/tc80)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
