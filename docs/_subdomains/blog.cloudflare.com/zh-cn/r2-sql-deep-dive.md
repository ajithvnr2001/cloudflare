---
url: https://blog.cloudflare.com/zh-cn/r2-sql-deep-dive/
title: R2 SQL\uff1a\u6df1\u5165\u5256\u6790\u6211\u4eec\u7684\u5168\u65b0\u5206\u5e03\u5f0f\u67e5\u8be2\u5f15\u64ce | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:46.841834+00:00
---

# R2 SQL：深入剖析我们的全新分布式查询引擎 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/r2-sql-deep-dive/

[博客](https://blog.cloudflare.com/zh-cn/)

[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)+5再显示 5 个标签

8 个标签显示 8 个标签

  * 文章标签
  * [R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)[数据](https://blog.cloudflare.com/zh-cn/tag/data/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)[边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)
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



[数据](https://blog.cloudflare.com/zh-cn/tag/data/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)[边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)

[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)[数据](https://blog.cloudflare.com/zh-cn/tag/data/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)[边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)

2025年9月25日

# R2 SQL：深入剖析我们的全新分布式查询引擎

![Yevgen Safronov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW467KVZ9QVG0BC5FVHJWW7W.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)

[Yevgen Safronov](https://blog.cloudflare.com/zh-cn/author/yevgen/)、[Nikita Lapkov](https://blog.cloudflare.com/zh-cn/author/nikita-lapkov/)和[Jérôme Schneider](https://blog.cloudflare.com/zh-cn/author/jerome/)

阅读时间：13 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/r2-sql-deep-dive/).

![BLOG-2995 Hero Image ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW474JN3DJ2BJNP7T6X963ZK.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f395OPwzs7ry9Dx2N745uj17urq////////5+bz0dLuztT02uH66Ov37+zs////////6+z31tny0tr43uf+6/D78vHw////////8PL83OH32OL94+7/8Pb/9/b1////////9vn/4un83+r/6fX/9fz/+/z6////////+///6PD/5fL/7/z/+f/////+/////////v//7PX/6ff/8////f//////////////////7ff/6/n/9P///v//////)

如何在没有服务器的情况下对 PB 级数据运行 SQL 查询？

我们对此问题有应对方案：[ _R2 SQL_](https://developers.cloudflare.com/r2-sql/)，这是一种无服务器查询引擎，可筛选巨大的数据集并在数秒内返回结果。

这篇文章详细介绍了使之成为可能的架构和技术。我们将介绍我们的查询规划器，它使用 [_R2 Data Catalog_](https://developers.cloudflare.com/r2/data-catalog/) 在读取字节之前修剪数 TB 的数据，并解释我们如何在 Cloudflare 的[ _全球网络_](https://www.cloudflare.com/network)、[ _Workers_](https://developers.cloudflare.com/workers/) 和 [_R2_](https://developers.cloudflare.com/r2/) 之间分配工作，以实现大规模并行执行。

### 从目录到查询

在 2025 年 Developer Week 期间，我们[ _推出了_](https://blog.cloudflare.com/r2-data-catalog-public-beta/) R2 Data Catalog，这是一个托管的 [_Apache Iceberg_](https://iceberg.apache.org/) 目录，直接内置于您的 Cloudflare R2 存储桶中。Iceberg 是一种开放表格式，为 PB 级对象存储提供事务和架构演化等关键数据库功能。它为您提供可靠的数据目录，但不提供查询方式。

在此之前，读取 R2 数据目录需要设置单独的服务，例如 [_Apache Spark_](https://spark.apache.org/) 或 [_Trino_](https://trino.io/)。大规模运营这些引擎并非易事：您需要配置集群、管理资源使用情况并负责其可用性，而这些都无助于实现从数据中获取价值这一主要目标。

[ _R2 SQL_](https://developers.cloudflare.com/r2-sql/) 完全删除了该步骤。它是一个无服务器查询引擎，可以在数据所在的 Iceberg 表上执行检索 SQL 查询。

### 设计用于处理 PB 级数据的查询引擎

对象存储与传统数据库的存储有着根本的不同。数据库的结构是经过精心设计的；而 R2 则是一个对象的海洋，单个逻辑表可能由数百万个大小不一的独立文件组成，而且每秒都会有更多文件生成。

Apache Iceberg 在此基础上提供了强大的逻辑组织层。它通过将表的状态作为一系列不可变的快照进行管理，通过操作轻量级元数据文件（而不是重写数据文件本身）来创建可靠的、结构化的表视图。

然而，这种逻辑结构并没有改变潜在的物理挑战：高效的查询引擎仍然必须在庞大的文件集合中找到所需的特定数据，而这需要克服两个主要的技术障碍：

**I/O 问题** ：查询效率的核心挑战是最大限度地减少从存储中读取的数据量。强制读取每个对象的方法根本不可行。主要目标是只读取绝对必要的数据。

**计算难题** ：即便经过优化后，仍需读取的数据量可能依然十分庞大。我们需要一种方式，能够为那些数据量巨大的查询任务精准匹配适量的计算资源——这些任务可能仅需运行短短几秒，随后便要立即将计算资源缩减至零，从而避免任何资源浪费。

我们为 R2 SQL 设计的架构采用两阶段方案来解决这两个问题：一是利用元数据智能缩减搜索范围的**查询规划器** ，二是通过 Cloudflare 全球网络分布式处理数据的**查询执行系统** 。

## 查询规划器

最高效的数据处理方式，就是从一开始就避免读取不必要的数据。这正是 R2 SQL 查询规划器的核心策略。该规划器不会对所有文件进行详尽扫描，而是利用 R2 Data Catalog 提供的元数据结构来缩减搜索范围，也就是说，避免读取与查询无关的海量数据。

这是一项自上而下的调查，其中规划器导航 Iceberg 元数据层的层次结构，使用每个级别的**统计信息** 来构建快速计划，准确指定查询引擎需要读取的字节范围。

### 我们说的“统计信息”是什么意思？

当我们提到规划器使用“统计信息”时，指的是 Iceberg 存储的关于数据文件内容的摘要元数据。这些统计信息构建了一张数据的粗略地图，使规划器能够在无需打开文件的情况下，决定读取哪些文件而忽略哪些文件。

规划器使用两种主要的统计级别来进行裁剪：

**分区级统计信息** ：这些统计信息存储在 Iceberg 清单列表中，用于描述给定 Iceberg 清单文件中所有数据的分区值范围。以按 `day(event_timestamp)` 分区的情况为例，该统计信息会记录该清单所追踪文件中最早和最晚的日期。

**列级统计信息** ：这些更为精细的统计信息存储在清单文件中，针对每个独立的数据文件进行记录。R2 Data Catalog 中的数据文件采用 [_Apache Parquet_](https://parquet.apache.org/) 格式存储。对于 Parquet 文件的每一列，清单文件都会存储以下关键信息：

  * 最小值和最大值。如果查询要求 `http_status = 500`，而文件的统计信息显示其 `http_status` 列的最小值为 200，最大值为 404，则可以跳过整个文件。
  * 空值 (null) 的数量。当查询明确查找非空值（例如 `WHERE error_code IS NOT NULL`），且该文件的元数据显示 `error_code` 字段的所有值均为空时，规划器便可以跳过这些文件。



现在，让我们看看规划器在遍历元数据层时如何使用这些统计数据。

### 缩减搜索范围

修剪过程是一个自上而下的调查，它包含以下三个主要步骤：

  1. **表元数据和当前快照**



规划器首先向目录请求当前表元数据的位置。这是一个 JSON 文件，包含表的当前架构、分区规范以及所有历史快照的日志。然后，规划器会获取最新的快照进行处理。

2\. **清单列表和分区裁剪**

当前快照指向单个 Iceberg 清单列表文件。规划器会读取该文件，并利用每个条目的分区级统计信息执行第一阶段（也是最关键的）修剪操作——丢弃所有分区值范围不符合查询条件的清单文件。例如，对于按 `day(event_timestamp)` 分区的表，规划器可通过清单列表中的最小/最大值，直接排除所有不包含查询相关日期数据的清单文件。

3.**清单和文件级缩减**

对于剩余的清单文件，规划器会逐一读取以获取实际的 Parquet 数据文件列表。这些清单文件包含其所追踪的每个数据文件更精细的列级统计信息。基于此可以进行第二轮筛选，直接丢弃那些完全不可能包含符合查询过滤器条件的数据行的数据文件。

4\. **文件行组修剪**

最后，对于仍然是候选的特定数据文件，查询规划器使用存储在 Parquet 文件页脚内的统计信息来跳过整个行组。

这种多层修剪的结果是一份精确的 Parquet 文件列表，以及这些 Parquet 文件中的行组。这些行组将成为查询工作单元，并被调度到查询执行系统进行处理。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2972  Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48QDPK5FSXKCQSTBY5E82S.png&w=715&h=898&f=webp&fit=cover&position=center)

### 规划管道

在 R2 SQL 中，我们目前为止所描述的多层修剪并非一个单一的过程。对于包含数百万个文件的表，元数据可能太大，无法在开始任何实际工作之前处理。等待完整的计划会导致严重的延迟。

相反，R2 SQL 将规划与执行视为一个协同运行的并发管道。规划器负责持续生成工作单元流，供执行器在每个工作单元就绪后立即处理。

规划器的调查从两次获取表结构图开始：一次获取表的快照，另一次获取清单列表。

#### 尽早开始执行

从这一阶段开始，查询将以流式处理方式执行。查询规划器在读取清单文件（以及这些清单文件指向的数据文件）并进行修剪的过程中，会即时将所有匹配的数据文件或行组作为工作单元发送至执行队列。

这种管道结构能够确保计算节点几乎立即启动耗时的数据 I/O 操作，远早于规划器完成全面分析的时间。

在这个管道模型的基础上，规划器添加了一项关键优化：**“有序处理”** 。清单文件不会以任意顺序进行流式传输，相反，规划器会按照与查询语句中 `ORDER BY` 子句相匹配的顺序来处理这些文件，并依据元数据统计信息进行引导。这样可以确保最有可能包含目标结果的数据优先得到处理。

这两个概念协同工作，以解决查询管道两端的查询延迟问题。

流式规划管道让我们能够尽早开始处理数据，从而将首个字节处理前的延迟降至最低。而在管道的另一端，通过对工作任务的精心排序，我们能够在无需扫描整个数据集的情况下找到确定结果，从而提前完成任务。

下一节将解释这种“提前完成”策略背后的机制。

#### 及早停止：如何在不阅读所有内容的情况下完成

由于查询计划器按照与 `ORDER BY` 子句匹配的顺序流式传输工作单元，查询执行系统首先处理最有可能出现在最终结果集中的数据。

这种优先级排序发生在元数据分层结构的两个层级：

**清单排序** ：规划器首先会检查清单列表。通过分析每个清单文件的分区统计信息（例如该组文件中的最新时间戳），来决定优先流式传输哪些完整的清单文件。

**Parquet 文件排序策略** ：在读取每个清单文件时，系统会根据更精细的列级统计信息，确定该清单内各个 Parquet 文件的处理顺序。

这就确保了会有一个持续按优先级排序的工作单元流被输送到执行引擎。而正是这个经过优先级排序的工作单元流，让我们能够提前终止查询。

例如，对于像 `ORDER BY timestamp DESC LIMIT 5` 这样的查询，当执行引擎处理工作单元并发回结果时，计划器会同时做两件事：

它维护着迄今为止看到的最佳 5 个结果的有限堆，并不断将新结果与堆中最旧的时间戳进行比较。

它会在流本身上保留一个“高水位标记”。借助元数据，它始终知道任何尚未处理的数据文件的绝对最新时间戳。

规划器会不断将堆的状态与剩余流的水位线进行比较。当 Top 5 堆中最旧的时间戳比剩余流的高水位线更新时，整个查询就会停止。

此时，我们可以确定剩余的工作单元中不可能再包含能够进入前 5 名的结果。于是，数据处理管道将停止运行，并向用户返回一个完整且正确的结果——而此时系统往往只读取了可能匹配数据中的一小部分。

目前，R2 SQL 仅支持对表分区键中的列进行排序。我们将努力在未来解决这一限制。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2972  Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47QW04E67385X0420DX85X.png&w=715&h=1069&f=webp&fit=cover&position=center)

### 架构

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2972  Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46CHBAN8N8Y4JZY149P7SF.png&w=715&h=776&f=webp&fit=cover&position=center)

## 查询执行

查询规划器以名为“行组”的小块为单位，流式处理查询任务。单个 Parquet 文件通常包含多个行组，但大多数情况下，只有其中少数行组包含相关数据。将查询任务拆分为行组处理，能让 R2 SQL 仅读取可能高达数 GB 的 Parquet 文件中的少量部分。

接收用户请求并执行查询规划的服务器充当查询协调器的角色。它将工作分配给查询工作器，并汇总结果，然后返回给用户。

Cloudflare 的网络规模庞大，许多服务器可能同时处于维护状态。查询协调器会联系 Cloudflare 的内部 API，以确保只选择运行良好、功能齐全的服务器来执行查询。协调器和查询 Worker 之间的连接通过 [_Cloudflare Argo Smart Routing_](https://www.cloudflare.com/en-gb/application-services/products/argo-smart-routing/) 进行，以确保快速可靠的连接。

从协调器接收查询执行请求的服务器将承担查询 Worker 的角色。查询 Worker 是 R2 SQL 实现水平扩展的关键节点。通过增加查询 Worker 的数量，R2 SQL 能够将查询任务分配到多台服务器上并行处理，从而显著提升查询处理速度。这一优势在处理包含大量文件的查询时尤为明显。

协调器和查询 Worker 都在 Cloudflare 的分布式网络上运行，确保 R2 SQL 具有足够的计算能力和 I/O 吞吐量来处理分析工作负载。

每个查询 Worker 会从协调器接收一批行组数据以及待执行的 SQL 查询。此外，协调器还会发送关于包含这些行组的 Parquet 文件的序列化元数据。得益于这些元数据，查询 Worker 能够直接获知每个行组在 Parquet 文件中的精确字节偏移量，而无需从 R2 存储中读取这些信息。

### Apache DataFusion

在内部，每个查询 Worker 都借助 [_Apache DataFusion_](https://github.com/apache/datafusion) 对行组运行 SQL 查询。DataFusion 是一个用 Rust 编写的开源分析型查询引擎，其构建理念围绕分区展开。一个查询会被拆分成多个并发的独立数据流，每个数据流负责处理属于自己的那部分数据分区。

DataFusion 中的分区与 Iceberg 中的分区类似，但用途不同。在 Iceberg 中，分区是一种在对象存储上物理组织数据的方式。在 DataFusion 中，分区用于组织内存数据以进行查询处理。虽然从逻辑上讲它们很相似，都是行根据某种逻辑分组在一起，但实际上，Iceberg 中的分区并不总是与 DataFusion 中的分区相对应。

DataFusion 分区与 R2 SQL 查询 Worker 的数据模型完美映射，因为每个行组都可以被视为独立的分区。因此，每个行组都可以并行处理。

同时，由于行组通常至少包含 1000 行，R2 SQL 受益于矢量化执行。每个 DataFusion 分区流可以一次性对多行执行 SQL 查询，从而分摊查询解释的开销。

在查询执行方面，存在两种极端方式：一种是批量顺序处理所有行，另一种是并行处理每一行数据。顺序处理会形成所谓的“紧密循环”，这种方式通常更有利于 CPU 缓存利用。除此之外，由于批量处理意味着我们只需较少次数地遍历查询计划，因此能显著降低解释开销。而完全并行处理虽然无法实现上述优化，但能通过利用多核 CPU 来更快完成查询。

DataFusion 的架构使我们能够在此规模上实现平衡，从而兼顾两方面的优势。对于每个数据分区，我们获得了更好的 CPU 缓存局部性，并摊销了解释开销。同时，由于许多分区是并行处理的，我们将工作负载分配到多个 CPU 上，从而进一步缩短了执行时间。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2972  Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45AZMQ3EHHRMTRGN6HKTM9.png&w=715&h=622&f=webp&fit=cover&position=center)

除了智能查询执行模型之外，DataFusion 还提供一流的 Parquet 支持。

作为文件格式，Parquet 为查询引擎设计了多项专属优化。它采用列式存储结构——这意味着各列数据在物理上是相互分离的。这种分离特性不仅带来了更高的压缩率，还使得查询引擎能够选择性地读取特定列。例如，如果查询只涉及五列数据，我们就可以仅读取这五列，而跳过其余五十列的读取。这种方式能大幅减少从 R2 读取的数据量，同时显著降低解压缩所需的 CPU 时间。

DataFusion 正是这样做的。使用 R2 的远程读取，它可以读取 Parquet 文件中包含所需列的部分，而跳过其余部分。

DataFusion 的优化器还支持将任意过滤器下推至查询计划的底层。换句话说，我们可以在从 Parquet 文件读取数据的同时就应用过滤条件。这使得我们能够跳过那些确定不会返回给用户的结果的物化过程，从而进一步缩短查询执行时间。

### 返回查询结果

查询 Worker 计算完结果后，会通过 [_gRPC 协议_](https://grpc.io/)将其返回给协调者。

R2 SQL 使用 [_Apache Arrow_](https://arrow.apache.org/) 在内部表示查询结果。Arrow 是一种内存格式，可以高效地表示结构化数据数组。DataFusion 在查询执行期间也使用它来表示数据分区。

除了作为内存中的数据格式外，Arrow 还定义了 [_Arrow IPC_](https://arrow.apache.org/docs/format/Columnar.html#format-ipc) 序列化格式。Arrow IPC 并非用于数据的长期存储，而是专为进程间通信设计——这正是查询 Worker 与协调器通过网络进行交互时所采用的方式。查询 Worker 会将所有结果序列化为 Arrow IPC 格式，并嵌入到 gRPC 响应中。随后，协调器会对这些结果进行反序列化，并继续处理 Arrow 数组。

## 未来计划

虽然 R2 SQL 目前在执行过滤查询方面表现相当出色，但我们计划在未来几个月内快速添加新功能。这包括但不限于：

  * 以分布式和可扩展的方式支持复杂汇总；
  * 用于提高查询执行可见性的工具，以帮助开发人员优化性能；
  * 支持 Apache Iceberg 所支持的许多配置选项。



此外，我们计划通过允许用户从 Cloudflare 仪表板使用 R2 SQL 查询其 R2 Data Catalog，来改善开发人员体验。

鉴于 Cloudflare 的分布式计算、网络功能和开发人员工具生态系统，我们有机会在此构建真正独特的产品。我们正在探索不同类型的索引，以进一步提高 R2 SQL 查询的速度，并提供更多功能，例如全文搜索、地理空间查询等。

## 马上试试吧！

R2 SQL 目前尚处于早期阶段，但我们非常期待用户能够亲自体验。R2 SQL 今日正式开启公开测试！欢迎访问我们的[ _入门指南_](https://developers.cloudflare.com/r2-sql/get-started/)，了解如何构建端到端的数据管道——该管道能够处理事件并将结果传输至 R2 Data Catalog 表，之后您可以通过 R2 SQL 对这些数据进行查询。

  
我们对于您将要构建的产品充满期待！欢迎在我们的[ _开发人员 Discord_](http://discord.cloudflare.com/) 上与我们分享您的反馈。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-deep-dive%2F&t=R2%20SQL%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%89%96%E6%9E%90%E6%88%91%E4%BB%AC%E7%9A%84%E5%85%A8%E6%96%B0%E5%88%86%E5%B8%83%E5%BC%8F%E6%9F%A5%E8%AF%A2%E5%BC%95%E6%93%8E)[](https://x.com/intent/post?text=R2+SQL%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%89%96%E6%9E%90%E6%88%91%E4%BB%AC%E7%9A%84%E5%85%A8%E6%96%B0%E5%88%86%E5%B8%83%E5%BC%8F%E6%9F%A5%E8%AF%A2%E5%BC%95%E6%93%8E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-deep-dive%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-deep-dive%2F)[](https://bsky.app/intent/compose?text=R2+SQL%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%89%96%E6%9E%90%E6%88%91%E4%BB%AC%E7%9A%84%E5%85%A8%E6%96%B0%E5%88%86%E5%B8%83%E5%BC%8F%E6%9F%A5%E8%AF%A2%E5%BC%95%E6%93%8E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-deep-dive%2F)[](https://mastodonshare.com/?text=R2+SQL%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%89%96%E6%9E%90%E6%88%91%E4%BB%AC%E7%9A%84%E5%85%A8%E6%96%B0%E5%88%86%E5%B8%83%E5%BC%8F%E6%9F%A5%E8%AF%A2%E5%BC%95%E6%93%8E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-deep-dive%2F)[](https://www.threads.net/intent/post?text=R2+SQL%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%89%96%E6%9E%90%E6%88%91%E4%BB%AC%E7%9A%84%E5%85%A8%E6%96%B0%E5%88%86%E5%B8%83%E5%BC%8F%E6%9F%A5%E8%AF%A2%E5%BC%95%E6%93%8E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fr2-sql-deep-dive%2F)

## 相关标签

[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[SQL](https://blog.cloudflare.com/zh-cn/tag/sql/)[数据](https://blog.cloudflare.com/zh-cn/tag/data/)[无服务器](https://blog.cloudflare.com/zh-cn/tag/serverless/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)[边缘计算](https://blog.cloudflare.com/zh-cn/tag/edge-computing/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
