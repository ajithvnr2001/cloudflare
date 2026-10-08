---
url: https://blog.cloudflare.com/zh-cn/r2-sql-aggregations/
title: \u9686\u91cd\u5ba3\u5e03 R2 SQL \u652f\u6301 GROUP BY\u3001SUM \u548c\u5176\u4ed6\u805a\u5408\u67e5\u8be2 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:46.225568+00:00
---

# 隆重宣布 R2 SQL 支持 GROUP BY、SUM 和其他聚合查询 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/r2-sql-aggregations/

[博客](https://blog.cloudflare.com/zh-cn/)

[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)+3再显示 3 个标签

6 个标签显示 6 个标签

  * 文章标签
  * [R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)[数据](https://blog.cloudflare.com/zh-cn/tag/data/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)
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



[数据](https://blog.cloudflare.com/zh-cn/tag/data/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)

[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)[数据](https://blog.cloudflare.com/zh-cn/tag/data/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)

2025年12月18日

# 隆重宣布 R2 SQL 支持 GROUP BY、SUM 和其他聚合查询

![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Marc Selwan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455H274J0ZYJ6K4KHKJT25.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jérôme Schneider](https://blog.cloudflare.com/zh-cn/author/jerome/)、[Nikita Lapkov](https://blog.cloudflare.com/zh-cn/author/nikita-lapkov/)和[Marc Selwan](https://blog.cloudflare.com/zh-cn/author/marc-selwan/)

阅读时间：9 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/r2-sql-aggregations/)、[日本語](https://blog.cloudflare.com/ja-jp/r2-sql-aggregations/)、[한국어](https://blog.cloudflare.com/ko-kr/r2-sql-aggregations/)和[繁體中文](https://blog.cloudflare.com/zh-tw/r2-sql-aggregations/).

![BLOG-3082 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45417DV5EYZK6BB5T2Z60B.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f395OPwzs7ry9Dx2N745uj17urq////////5+bz0dLuztT02uH66Ov37+zs////////6+z31tny0tr43uf+6/D78vHw////////8PL83OH32OL94+7/8Pb/9/b1////////9vn/4un83+r/6fX/9fz/+/z6////////+///6PD/5fL/7/z/+f/////+/////////v//7PX/6ff/8////f//////////////////7ff/6/n/9P///v//////)

在处理大量数据时，快速获取概览是非常有帮助的——这正是 SQL 中的聚合所提供的功能。聚合，也被称为“GROUP BY 查询”，能提供鸟瞰式的视角，让您能迅速从海量数据中获得洞察。

正因如此，我们非常激动地宣布：[ _R2 SQL_](https://blog.cloudflare.com/r2-sql-deep-dive/) 现已支持聚合功能。R2 SQL 是 Cloudflare 推出的无服务器、分布式分析查询引擎，能够对存储在 [_R2 Data Catalog_](https://developers.cloudflare.com/r2/data-catalog/) 中的数据进行 SQL 查询。聚合功能将帮助 [_R2 SQL_](https://developers.cloudflare.com/r2-sql/) 用户发现数据中的重要趋势与变化、生成报告，并在日志中找出异常。

此次发布基于已支持的过滤查询功能，后者是分析工作负载的基础，允许用户在 [_Apache Parquet_](https://parquet.apache.org/) 文件的大量数据中找到所需的信息。

在本文中，我们将详细介绍聚合功能的用途和特点，然后深入探讨我们如何扩展 R2 SQL 以支持在存储在 R2 Data Catalog 中的海量数据上运行此类查询。

## 分析中聚合的重要性

聚合也称为“GROUP BY 查询”，可以生成底层数据的简要汇总。

一个常见的聚合用例是生成报告。假设有一个名为“sales”的表，其中包含某组织在各个国家/地区和部门的历史销售数据。我们可以使用如下聚合查询轻松生成按部门统计的销售报告：
    
    
    SELECT department, sum(value)
    FROM sales
    GROUP BY department

  
我们可以使用“GROUP BY”语句，将表中的行划分为多个存储桶。每个存储桶都有一个标签，对应一个特定部门。当所有行被划分进各自的存储桶后，我们就可以对每个存储桶中的所有行计算“sum(value)”，从而得到该部门的总销售量。

对于某些报告，我们可能只关心销售量最高的部门。这时，“ORDER BY”语句就派上用场了：
    
    
    SELECT department, sum(value)
    FROM sales
    GROUP BY department
    ORDER BY sum(value) DESC
    LIMIT 10

这里我们指示查询引擎按照各部门的总销售量降序排列，并仅返回前 10 个销售量最高的部门。

最后，我们有时可能希望过滤掉异常数据。例如，我们只想在报告中包含总销售量大于 5 的部门。我们可以轻松地通过“HAVING”语句实现这一点：
    
    
    SELECT department, sum(value), count(*)
    FROM sales
    GROUP BY department
    HAVING count(*) > 5
    ORDER BY sum(value) DESC
    LIMIT 10

我们在查询中添加了一个新的聚合函数“count(*)”，它用于计算每个存储桶中有多少行。这直接对应于该部门的销售次数，因此我们也在“HAVING”子句中添加了一个条件，确保只保留那些行数大于 5 的存储桶。

## 两种聚合方式：早计算还是晚计算

聚合查询有一个有趣的特性：它们可以引用并不实际存在于原始数据中的列。以“sum(value)”为例：这个列是由查询引擎在运行时动态计算出来的，而像“department”这样的列则是直接从存储在 R2 上的 Parquet 文件中读取的。这个细微差别意味着，任何引用了如“sum”、“count”等聚合函数的查询，都需要分成两个阶段来处理。

第一阶段是计算新列。如果我们要使用“ORDER BY”语句按“count(*)”列对数据进行排序，或使用“HAVING”语句基于该列过滤行，我们需要知道该列的值。一旦知道“count(*)”等列的值，我们就可以继续执行查询的其余部分。

请注意，如果查询在“HAVING”或“ORDER BY”子句中没有引用聚合函数，但仍在“SELECT”子句中使用它们，我们可以使用一种技巧。由于我们直到最后才需要聚合函数的值，因此我们可以部分计算它们，并在准备向用户返回结果之前再合并结果。

这两种方法之间的关键区别在于我们何时计算聚合函数：是提前算好，以便后续做更多处理；还是按需即时计算，边处理边构建最终结果。

首先，我们来探讨“即时构建结果”的方式——我们称之为“分散-聚集聚合”(scatter-gather aggregations)。接着在此基础上，我们会介绍“洗牌式聚合”(shuffling aggregations)，它支持在聚合函数之上执行额外的操作，例如“HAVING”和“ORDER BY”。

## 分散-聚集聚合

没有使用“HAVING”和“ORDER BY”子句的聚合查询能够以类似于过滤查询的方式执行。对于过滤查询，R2 SQL 会选择一个节点作为查询执行的协调节点。该节点分析查询内容，并查阅 R2 Data Catalog，以确定哪些 Parquet 行组可能包含与查询相关的数据。每一个 Parquet 行组代表一个相对较小的任务单元，可由单个计算节点处理。协调节点将任务分发给多个工作节点，收集结果并返回给用户。

为了执行聚合查询，我们遵循相同的步骤，将小任务分发给工作节点。但这一次，工作节点不仅要依据 WHERE 子句中的条件过滤行，还要计算**“预聚合”(pre-aggregates)** 。

预聚合是聚合过程的中间状态。它是对一部分数据做部分聚合后的不完整结果。多个预聚合可以被合并，以计算出聚合函数的最终值。将聚合函数拆分为多个预聚合，使我们可以水平扩展聚合计算，充分利用 Cloudflare 网络中的庞大计算资源。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45BPPXJKC47WPRR8TQZR5H.png&w=715&h=674&f=webp&fit=cover&position=center)

例如，“count(*)”的预聚合结果就是一个数字，代表数据子集中行的数量。计算最终的“count(*)”就像将这些数字相加一样简单。“avg(value)”的预聚合结果包含两个数字：“sum(value)”和“count(*)”。然后，可以通过将所有“sum(value)”值相加，将所有“count(*)”值相加，最后将第一个数字除以第二个数字来计算“avg(value)”的值。

当工作节点完成预聚合的计算后，会将结果流式传输给协调节点。协调节点收集所有结果，根据预聚合计算出聚合函数的最终值，并将最终结果返回给用户。

## 洗牌机制：超越分散-聚集

当协调节点可以通过合并来自各个工作节点的小型、部分状态来计算最终结果时，分散-聚合的方式非常高效。如果您执行类似 `SELECT sum(sales) FROM orders` 这样的查询，协调节点会从每个工作节点收到一个单一数值并相加。无论 R2 中存储了多少数据，协调节点的内存占用都可以忽略不计。

然而，当查询需要根据聚合 _结果_ 进行排序或过滤时，这种方式就会变得低效。考虑下面这个查询——它用于找出销售额最高的前两个部门：
    
    
    SELECT department, sum(sales)
    FROM sales
    GROUP BY department
    ORDER BY sum(sales) DESC
    LIMIT 2

要正确确定全局的前 2 名，需要知道整个数据集中每个部门的销售总额。由于数据在底层 Parquet 文件中是随机分布的，某个特定部门的销售记录很可能分散在许多不同的工作节点上。一个部门在每个单独的工作节点上的销售额可能都很低，因此不会进入任何本地的“前 2”列表，但在全局汇总后却可能是销售额最高的部门。

下图展示了分散-聚合方法为何不适用于此查询。“Dept A”是全球销售额冠军，但由于它的销售记录均匀分布在多个工作节点上，它没有进入某些本地的前 2 列表，最终被协调节点丢弃。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463ZP69R3N5R25QG4E9T0V.png&w=715&h=674&f=webp&fit=cover&position=center)

因此，当查询按全局聚合结果排序时，协调节点无法依赖来自工作节点的预筛选结果。它必须向 _每个_ 工作节点请求 _每个_ 部门的销售总额，以便在计算全局总数后进行排序。如果按高基数列（如 IP 地址或用户 ID）进行分组，这就会迫使协调节点接收并合并数百万行数据，从而在单个节点上造成资源瓶颈。

为了解决这个问题，我们需要引入**洗牌 (shuffling)** ——一种在最终聚合发生之前，将特定分组的数据重新聚集到一起的方法。

### 聚合数据的洗牌

为了解决数据随机分布带来的挑战，我们引入了一个**洗牌阶段** 。工作节点不再将结果发送给协调节点，而是直接相互交换数据，根据分组键将行数据进行归类。

这种路由依赖于**确定性哈希分区** 。当工作节点处理一行数据时，它会对 `GROUP BY` 列进行哈希计算，以确定目标工作节点。由于该哈希是确定性的，集群中的每个工作节点都能独立地就特定数据应发送到哪里达成一致。例如，如果“Engineering”的哈希值指向工作节点 5，那么所有工作节点都知道应将“Engineering”相关的行路由到工作节点 5。无需中央注册表。

下图展示了这一流程。注意“Dept A”最初位于工作节点 1、2 和 3 上。因为哈希函数将“Dept A”映射到工作节点 1，所有工作节点都会将这些行路由到同一个目标节点。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45ZD7B5A4ZRR0NG4HHEKV4.png&w=715&h=622&f=webp&fit=cover&position=center)

洗牌聚合能够产生正确的结果。然而，这种“全部对全部”(all-to-all) 的数据交换会引入时序依赖。如果工作节点 1 在工作节点 3 尚未完成发送其“Dept A”数据份额时就提前开始计算最终总额，那么结果将是不完整的。

为了解决这个问题，我们强制执行严格的**同步屏障** 。协调节点跟踪整个集群的进度，而工作节点则缓冲它们的输出数据，并通过 [_gRPC_](https://grpc.io/) 流刷新到对等节点。只有当每个工作节点确认已完成输入文件的处理并已刷新完洗牌缓冲区时，协调节点才会发出继续执行的命令。这一屏障保证在进入下一阶段时，每个工作节点上的数据集都是完整且准确的。

### 本地最终化

一旦同步屏障解除，每个工作节点都持有其被分配组的完整数据集。此时，工作节点 1 拥有“Dept A”100% 的销售记录，并能确定地计算出最终总额。

这使得我们可以将过滤、排序等计算逻辑下推到工作节点执行，而不必让协调节点承担这些负担。例如，如果查询包含 `HAVING count(*) > 5`，工作节点可以在聚合完成后立即过滤掉不满足该条件的分组。

在此阶段的末尾，每个工作节点会为它所负责的分组生成一个已排序的最终结果流。

### 流式归并

最后一块拼图是协调节点。在分散-聚合模型中，协调节点需要承担对整个数据集进行聚合与排序的高开销任务。而在洗牌模型中，它的角色发生了变化。

由于工作节点已经在本地计算出了最终的聚合结果并完成了排序，协调节点只需执行一次 **k 路归并 (k-way merge)** 。它会为每个工作节点打开一个数据流，逐行读取结果；比较每个工作节点当前行的排序值，根据排序规则选出“胜出者”，并将其加入即将返回给用户的最终查询结果中。

这种方法对于 `LIMIT` 查询尤其高效。如果用户请求前 10 个部门，协调节点会在归并过程中找到前 10 条记录后立即停止处理，而无需加载或归并剩余的数百万行数据。这样可以在不大量消耗计算资源的前提下，支持更大规模的操作。

## 用于处理海量数据集的强大引擎

随着聚合功能的加入，[ _R2 SQL_](https://developers.cloudflare.com/r2-sql/?cf_target_id=84F4CFDF79EFE12291D34EF36907F300) 从一个擅长过滤数据的工具，转变为能够在海量数据集上进行数据处理的强大引擎。这得益于我们实现了诸如“分散-聚合”与“洗牌”等分布式执行策略，使我们能够将计算推送到数据存储的位置，充分利用 Cloudflare 的全球计算与网络规模。

无论您是要生成报表、监控大批量日志以发现异常，还是仅仅想从数据中洞察趋势，现在都可以在 Cloudflare 开发人员平台内轻松完成这一切，而无需承担管理复杂 OLAP 基础设施的开销，也不必将数据移出 R2。

## 马上试试吧

R2 SQL 的聚合功能现已可用。我们非常期待看到您使用这些新功能处理 R2 Data Catalog 中的数据。

  * **快速开始：** 请查看我们的[ _文档_](https://developers.cloudflare.com/r2-sql/sql-reference/)，获取运行聚合查询的示例与语法指南。
  * **加入讨论：** 如果您有任何问题、反馈，或想要分享您正在构建的项目，欢迎加入 Cloudflare [_开发人员 Discord_](https://discord.com/invite/cloudflaredev) 与我们交流。



本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-aggregations%2F&t=%E9%9A%86%E9%87%8D%E5%AE%A3%E5%B8%83%20R2%20SQL%20%E6%94%AF%E6%8C%81%20GROUP%20BY%E3%80%81SUM%20%E5%92%8C%E5%85%B6%E4%BB%96%E8%81%9A%E5%90%88%E6%9F%A5%E8%AF%A2)[](https://x.com/intent/post?text=%E9%9A%86%E9%87%8D%E5%AE%A3%E5%B8%83+R2+SQL+%E6%94%AF%E6%8C%81+GROUP+BY%E3%80%81SUM+%E5%92%8C%E5%85%B6%E4%BB%96%E8%81%9A%E5%90%88%E6%9F%A5%E8%AF%A2&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-aggregations%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-aggregations%2F)[](https://bsky.app/intent/compose?text=%E9%9A%86%E9%87%8D%E5%AE%A3%E5%B8%83+R2+SQL+%E6%94%AF%E6%8C%81+GROUP+BY%E3%80%81SUM+%E5%92%8C%E5%85%B6%E4%BB%96%E8%81%9A%E5%90%88%E6%9F%A5%E8%AF%A2+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-aggregations%2F)[](https://mastodonshare.com/?text=%E9%9A%86%E9%87%8D%E5%AE%A3%E5%B8%83+R2+SQL+%E6%94%AF%E6%8C%81+GROUP+BY%E3%80%81SUM+%E5%92%8C%E5%85%B6%E4%BB%96%E8%81%9A%E5%90%88%E6%9F%A5%E8%AF%A2&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-aggregations%2F)[](https://www.threads.net/intent/post?text=%E9%9A%86%E9%87%8D%E5%AE%A3%E5%B8%83+R2+SQL+%E6%94%AF%E6%8C%81+GROUP+BY%E3%80%81SUM+%E5%92%8C%E5%85%B6%E4%BB%96%E8%81%9A%E5%90%88%E6%9F%A5%E8%AF%A2+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-aggregations%2F)

## 相关标签

[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)[数据](https://blog.cloudflare.com/zh-cn/tag/data/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
