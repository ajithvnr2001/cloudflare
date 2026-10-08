---
url: https://blog.cloudflare.com/zh-cn/clickhouse-query-plan-contention/
title: \u6211\u4eec\u7684\u8ba1\u8d39\u6d41\u7a0b\u7ba1\u9053\u7a81\u7136\u53d8\u6162\u4e86\u3002\u95ee\u9898\u7684\u8d77\u56e0\u5728\u4e8e ClickHouse \u4e2d\u9690\u85cf\u7684\u74f6\u9888 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:43:02.633478+00:00
---

# 我们的计费流程管道突然变慢了。问题的起因在于 ClickHouse 中隐藏的瓶颈 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/clickhouse-query-plan-contention/

[博客](https://blog.cloudflare.com/zh-cn/)

[ClickHouse](https://blog.cloudflare.com/zh-cn/tag/clickhouse/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)+2再显示 2 个标签

5 个标签显示 5 个标签

  * 文章标签
  * [ClickHouse](https://blog.cloudflare.com/zh-cn/tag/clickhouse/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)[性能](https://blog.cloudflare.com/zh-cn/tag/performance/)[数据库](https://blog.cloudflare.com/zh-cn/tag/database/)
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



[性能](https://blog.cloudflare.com/zh-cn/tag/performance/)[数据库](https://blog.cloudflare.com/zh-cn/tag/database/)

[ClickHouse](https://blog.cloudflare.com/zh-cn/tag/clickhouse/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)[性能](https://blog.cloudflare.com/zh-cn/tag/performance/)[数据库](https://blog.cloudflare.com/zh-cn/tag/database/)

2026年5月14日

# 我们的计费流程管道突然变慢了。问题的起因在于 ClickHouse 中隐藏的瓶颈

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/zh-cn/author/james-morrison/)和[Christian Endres](https://blog.cloudflare.com/zh-cn/author/christian-endres/)

阅读时间：10 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/clickhouse-query-plan-contention/)、[日本語](https://blog.cloudflare.com/ja-jp/clickhouse-query-plan-contention/)、[한국어](https://blog.cloudflare.com/ko-kr/clickhouse-query-plan-contention/)和[繁體中文](https://blog.cloudflare.com/zh-tw/clickhouse-query-plan-contention/).

![BLOG-3299 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4999A46M2F3BCY3QF5F258.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////789PLy7evs7+3t8/Hx8/Hv7ezp///////+8vL06Oju5+jv7O3y7+/x7e3s////////8vP45Ofx4eXx5+r17O707u/v////////9ff95+r14+f26Oz57/H48vP0/////////P3/7/L77fD78vT/9/j++Pn6////////////+/v//Pv//////////v/+////////////////////////////////////////////////////////////////)

我们在 Cloudflare 内部大量使用 ClickHouse，这是一个开源的联机分析处理 (OLAP) 数据库。每天，我们会向 ClickHouse 发出数百万次调用，以确定应该向使用 Cloudflare 产品的用户收取多少费用。如果我们不及时完成这些任务，将很难进行发票对账。

此管道为数亿美元的使用收入、反欺诈系统等提供支持，因此其延迟会对后续流程产生重大影响。

正因如此，当 ClickHouse 中负责确保 Cloudflare 账单正常发出的每日汇总任务处理速度在迁移后显著减缓时，我们才意识到这是一个严重问题。所有常见检查指标看起来都正常：I/O、内存、扫描的行数、读取的片段。这些我们通常会在 ClickHouse 查询速度变慢时检查的所有指标似乎都正常。

本文将概述我们如何发现 ClickHouse 内部深处隐藏的瓶颈，以及我们编写了哪三个补丁来修复。

## 设置：PB 级分析平台

我们使用 ClickHouse 在数十个集群中存储超过一百 PB 的数据。为了简化众多内部团队的引导流程，我们在 2022 年初构建了一个名为“Ready-Analytics”的系统。

前提很简单：团队无需设计新表，即可将数据流式传输到单张超大表。数据集通过 `namespace` 来消除歧义，每条记录使用标准模式（例如，20 个浮点字段、20 个字符串字段、一个时间戳，以及一个 `indexID`）。

在 ClickHouse 中，数据排序方式对于查询性能至关重要。`indexID` 正好可以发挥这方面的作用。它是一个字符串字段，构成主键的一部分，也就是说，每个命名空间可以按照其所有者预期的运行情况，优化查询数据的排序方式。最终得到的主键如下所示：（`namespace`、`indexID`、`timestamp`）。

这个系统广受欢迎，数百个应用程序都使用它。截至 2024 年 12 月，其数据量已超过 2PiB，数据摄取速率高达每秒数百万行。但它有一个严重缺陷：数据保留策略。

## 问题：单一的保留策略适用于所有情况

Cloudflare 多年来一直使用 ClickHouse，甚至在其具有原生生存时间 (TTL) 功能之前就已开始使用。因此，我们基于数据分区机制构建了自己的保留系统。Ready-Analytics 表按 `day` 分区，因此，我们的保留作业会简单地删除超过 31 天的分区。

这种“一刀切”的 31 天保留期是一个重大限制。有些团队由于法律或合同义务需要存储数据多年，而另一些团队只需存储数据几天。这种限制意味着这些用例无法使用 Ready-Analytics，而而不得不选择传统的部署方案，其引导流程也复杂得多。

我们需要一个支持**按命名空间保留数据** 的新系统。

## 解决方法：全新的分区方案

我们考虑了两种主要方法：

  1. **每个命名空间一张表：** 这自然可以解决数据保留问题，但需要大量新的自动化功能来按需管理数千张表。
  2. **新的分区键：** 我们可以将分区键从简单的 `(day)` 修改为 `(namespace, day)`。



我们选择了第二个选项。这样一来，现有的保留系统可以继续管理分区，但如今我们还可以按命名空间进行精细化管理。

我们知道这将增加表中片段的总数量，但我们做了一个关键假设：**由于按特定命名空间过滤每个查询， _任何单个查询读取的片段数量_ 不应改变**。我们认为，这意味着性能不会受到影响。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4893FX4WFRGPEECQSTGMYN.png&w=715&h=709&f=webp&fit=cover&position=center)

 _这显示了我们是如何更改分区方式，从而能够经济实惠地删除单个命名空间的数据_

这个新系统也让我们能够构建一个复杂的存储管理层。利用[ _最大最小公平算法_](https://en.wikipedia.org/wiki/Max-min_fairness)，我们可以设置目标磁盘利用率（例如 90%），并自动“共享”可用空间。使用率低于其公平份额的命名空间，可以将其未使用的容量让给那些需要更多容量的命名空间。这样一来，我们能够自信地将集群的运行利用率提高到 90%。

2025 年 1 月，我们开始了迁移。我们使用 ClickHouse 的 `Merge` 表功能合并了新旧表，从而将所有新数据写入新的分区表，旧数据逐渐超过保存期限。

## 谜团：计费系统何时开始出现问题

两个月后，也就是 2025 年 3 月下旬，我们的计费团队报告说每日汇总任务处理速度变慢了。这些任务对时间要求很高；如果不完成，便无法发出账单。任务的处理速度越来越慢，而我们不断接近最后期限。

我们进行了调查，但所有常见检查指标看起来都很正常。I/O 正常。内存正常。单个查询的指标显示，其读取的数据和片段数量并 _不_ 比以前更多。我们的初步假设似乎是正确的，但系统却开始缓慢运行。

我们花了好几天时间才找到一套理论来解释这个问题。最终，我们绘制了查询持续时间与 _总片段数_ 的关系图。结果显示，两者之间存在明显的关联。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YV50ASJA17DM0BX4JXF3.png&w=715&h=235&f=webp&fit=cover&position=center)

 _Ready Analytics ClickHouse 集群上的平均 SELECT 查询持续时间，显示性能逐渐下降。_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HY9NE8VMFT5Z5RMHRVCM.png&w=715&h=233&f=webp&fit=cover&position=center)

 _采用新的 (namespace, day) 分区方案后，每表副本的数据片段总数呈线性增长。_

但是， _为什么_ 会这样呢？如果没有 _读取_ 额外的片段，为什么它们的存在会减缓运行？

## 调查：使用火焰图查找瓶颈

我们转为利用 ClickHouse 内置的 [`_trace_log_`](https://clickhouse.com/docs/operations/system-tables/trace_log) 来生成火焰图。这是一个内置表，用于记录正在运行的 ClickHouse 服务器的跟踪信息。它不仅包含正在执行的代码跟踪信息，还将这些信息与特定用户、查询 ID 和其他元数据关联，这意味着可以根据需要筛选出相当精确的事件集。在我们的用例，我们专门查看了 _末端节点 SELECT 查询_ 。由于表中提供了元数据，因此很容易做到这一点。

第一个基于 CPU 的火焰图迅速证实了我们的怀疑：**查询规划** 耗费了大量时间。这是执行 _之前_ 的阶段，此时 ClickHouse 会决定要读取哪些片段。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46RG580ZDKK07KCTRDD0MK.png&w=715&h=368&f=webp&fit=cover&position=center)

 _火焰图，显示末端节点查询 45% 的 CPU 时间用于根据分区 ID 来过滤片段向量_

火焰图清晰地表明：45% 采样的 CPU 时间用于执行一个名为 `filterPartsByPartition` 的函数。

我们最初尝试的修复方法是对这个确切的代码路径打一个小补丁。规划器评估启发式算法以减少片段，但我们认为没有按最优顺序来进行评估。我们的补丁调整了顺序，从而提升了 5% 的性能。我们找到了正确的方向，但忽略了真正的问题。

我们一直生成的是“CPU”跟踪信息，这些跟踪信息只对活动线程进行采样。后来我们切换为“真实”跟踪信息，这些跟踪信息会对 _所有_ 线程进行采样，包括那些处于非活动状态或等待状态的线程。新的火焰图给我们很大的启示。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HV7ET9Z7PXF66NF9GT9Y.png&w=715&h=351&f=webp&fit=cover&position=center)

 _火焰图，显示超过一半的末端节点查询持续时间用于等待保护活动片段列表的互斥锁_

问题不在于 CPU 密集型任务；而是**大规模锁争用** 。超过一半的查询持续时间都花在 _等待_ 获取保护表片段列表的单个互斥锁 (`MergeTreeData`)。若要规划查询，每个线程都必须：

  1. 获取此互斥锁的**独占锁** 。
  2. 完整复制表中 _所有_ 片段列表。
  3. 释放该锁。
  4. 过滤列表，将其缩小到相关片段。



由于有数万个片段和数百个并发查询，它们就像排成一列一样，等待执行。

## 解决方法：三个补丁

这一发现帮助我们规划了一系列优化措施来缓解这些性能瓶颈。与针对 ClickHouse 所做的所有补丁一样，我们力求使这些措施具有通用性，并最终将其贡献到上游代码库。这让我们可以更轻松地更容易维护自己的分支，意味着社群也能从我们所做的改变中受益！

### 优化措施 1：使用共享锁

查询规划器不会 _修改_ 片段列表；它只是 _读取_ 。因此，没有理由使用独占锁。

**解决方法：** 我们修改了代码，以获取**共享锁** (`std::shared_lock`)。这使得所有查询规划器可以同时进入临界区。

**结果：** 查询持续时间立即显著下降。锁争用问题消失了。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CCVN8NX5N7V0Q8SYKEFN.png&w=715&h=235&f=webp&fit=cover&position=center)

 _使用共享锁优化（优化措施 1）对平均 SELECT 查询持续时间的即时影响，表明解决了锁争用问题。_

### 优化措施 2：停止复制向量

性能虽已显著改善，但仍未恢复到基准水平。我们重新查看了跟踪日志，并绘制了另一个“真实”的火焰图。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48M55TB5PVRTEDJNTSB64J.png&w=715&h=351&f=webp&fit=cover&position=center)

 _火焰图，显示四分之一的末端节点查询持续时间用于复制所有片段向量，另外四分之一的末端节点查询持续时间用于过滤（再次复制）。_

新的火焰图显示，瓶颈只是发生了转移。现在，即使使用了共享锁，仍然会花费时间 _复制_ 庞大的片段向量。凭直觉，复制向量似乎很省时，但当它包含成千上万个元素且每秒执行数百次时，时间就会累加。

**解决方法：** 我们完全推迟了复制操作。我们创建了一个片段列表的“共享副本”。只读操作（例如查询规划）直接从该副本读取数据。任何 _修改_ 片段集合（例如插入新片段）的操作都会重新生成缓存。现在，规划器只复制其真正需要的 _已过滤_ 片段列表。

**结果：** 又一次显著的性能提升。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PPRSHYTZ68EXGM666V41.png&w=715&h=236&f=webp&fit=cover&position=center)

 _推出向量复制优化（优化措施 2）后，进一步提升了性能。_

在内部看到了这些显著的性能提升后，我们决定将这些更改拓展到社群。经过与 ClickHouse Inc. 维护人员进行多次微小的设计迭代后，我们在[ _PR #85535_](https://github.com/ClickHouse/ClickHouse/pull/85535) __ 中合并了这些更改。这些更改自 [_ClickHouse 25.11 版本_](https://clickhouse.com/docs/whats-new/changelog/2025#performance-improvement-1)以来一直可用。

### 优化措施 3：利用二分搜索，查找片段

事情还没有结束。随着片段数量的增加，性能 _仍然_ 会下降，只是下降速度变得更慢。与片段数量的关联仍然存在。几个月后，我们重新审视了这个问题，新的火焰图（与图 3 相同）显示了过滤代码路径（我们首先尝试修复的路径）所花费的时间。该代码对所有片段执行**线性扫描** ，从而针对每个片段评估谓词。在几个月之后，我们又回到了优化前的 SELECT 持续时间。

但我们知道，这个片段列表是按分区键排序。请记住，分区键的第一列是命名空间，绝大多数查询会根据它来过滤，因为它会标识“租户”。我们如何利用这一点？

**解决方法：** 我们根据分区 ID 的 `namespace` 片段，实施了二分搜索。之所以有效，是因为向量已排序，用户无需实际查看即可过滤许多条目。因为 `namespace` 是该排序键的第一个片段，所以这种方法特别有效。经过第一轮二分搜索后，我们需要检查的片段范围显著缩小，对于这些片段，我们仍然会逐个检查，应用与之前相同的逻辑，根据其他条件排除某些片段。

**结果：** 在 2026 年 3 月部署此补丁后，查询持续时间减少了 50%（参见图 8）。更重要的是，这最终打破了查询持续时间与片段数量之间的关联。但遗憾的是，这个解决方法对于任意查询条件（例如，`namespace in (5,10)` 等条件）的通用性并不强。我们正在研究更通用的方法，例如扩展[ _查询条件缓存_](https://clickhouse.com/blog/introducing-the-clickhouse-query-condition-cache)来涵盖片段过滤。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46ZC0AXABREP5Q1ES3D0CS.png&w=715&h=239&f=webp&fit=cover&position=center)

 _实施二分搜索以减少片段后，延迟持续降低（优化措施 3）。_

## 暂时缓解

这些优化措施暂时解决了计费系统的问题。但这次经历也暴露了我们分区方案选择带来的深远且不易察觉的代价。

依然存在其他问题。在这篇博客文章中，我们只描述了片段数量增加对 SELECT 持续时间产生的影响，但它也导致了 ZooKeeper 问题，ZooKeeper 负责跟踪 ClickHouse 中所有片段的元数据。或许有一天，我们会概述 100 GB ZooKeeper 集群的情况。

虽然我们获得了足够的喘息空间，但根本问题仍然存在：这种分区方案是否是正确的长期选择？或者，我们最终需要硬着头皮，迁移到不同的架构？目前，我们的补丁暂时有效，但这次经历清楚地表明，即使是精心策划的变更也可能因为错误的假设而失败。

计费团队首次报告该问题时，我们每个副本有 30,000 个片段。片段数量持续增长，一年后每个副本的片段数量达到了 16 万个，但由于我们现阶段的优化措施，查询持续时间一直保持稳定。

Cloudflare 致力于解决复杂的大规模工程难题。如果您认为本文描述的调试和优化正是您寻求的挑战，请查看[ _空缺职位_](https://www.cloudflare.com/careers/jobs/?department=Engineering)，了解我们的一些招聘信息。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fclickhouse-query-plan-contention%2F&t=%E6%88%91%E4%BB%AC%E7%9A%84%E8%AE%A1%E8%B4%B9%E6%B5%81%E7%A8%8B%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E5%8F%98%E6%85%A2%E4%BA%86%E3%80%82%E9%97%AE%E9%A2%98%E7%9A%84%E8%B5%B7%E5%9B%A0%E5%9C%A8%E4%BA%8E%20ClickHouse%20%E4%B8%AD%E9%9A%90%E8%97%8F%E7%9A%84%E7%93%B6%E9%A2%88)[](https://x.com/intent/post?text=%E6%88%91%E4%BB%AC%E7%9A%84%E8%AE%A1%E8%B4%B9%E6%B5%81%E7%A8%8B%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E5%8F%98%E6%85%A2%E4%BA%86%E3%80%82%E9%97%AE%E9%A2%98%E7%9A%84%E8%B5%B7%E5%9B%A0%E5%9C%A8%E4%BA%8E+ClickHouse+%E4%B8%AD%E9%9A%90%E8%97%8F%E7%9A%84%E7%93%B6%E9%A2%88&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fclickhouse-query-plan-contention%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fclickhouse-query-plan-contention%2F)[](https://bsky.app/intent/compose?text=%E6%88%91%E4%BB%AC%E7%9A%84%E8%AE%A1%E8%B4%B9%E6%B5%81%E7%A8%8B%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E5%8F%98%E6%85%A2%E4%BA%86%E3%80%82%E9%97%AE%E9%A2%98%E7%9A%84%E8%B5%B7%E5%9B%A0%E5%9C%A8%E4%BA%8E+ClickHouse+%E4%B8%AD%E9%9A%90%E8%97%8F%E7%9A%84%E7%93%B6%E9%A2%88+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fclickhouse-query-plan-contention%2F)[](https://mastodonshare.com/?text=%E6%88%91%E4%BB%AC%E7%9A%84%E8%AE%A1%E8%B4%B9%E6%B5%81%E7%A8%8B%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E5%8F%98%E6%85%A2%E4%BA%86%E3%80%82%E9%97%AE%E9%A2%98%E7%9A%84%E8%B5%B7%E5%9B%A0%E5%9C%A8%E4%BA%8E+ClickHouse+%E4%B8%AD%E9%9A%90%E8%97%8F%E7%9A%84%E7%93%B6%E9%A2%88&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fclickhouse-query-plan-contention%2F)[](https://www.threads.net/intent/post?text=%E6%88%91%E4%BB%AC%E7%9A%84%E8%AE%A1%E8%B4%B9%E6%B5%81%E7%A8%8B%E7%AE%A1%E9%81%93%E7%AA%81%E7%84%B6%E5%8F%98%E6%85%A2%E4%BA%86%E3%80%82%E9%97%AE%E9%A2%98%E7%9A%84%E8%B5%B7%E5%9B%A0%E5%9C%A8%E4%BA%8E+ClickHouse+%E4%B8%AD%E9%9A%90%E8%97%8F%E7%9A%84%E7%93%B6%E9%A2%88+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fclickhouse-query-plan-contention%2F)

## 相关标签

[ClickHouse](https://blog.cloudflare.com/zh-cn/tag/clickhouse/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)[性能](https://blog.cloudflare.com/zh-cn/tag/performance/)[数据库](https://blog.cloudflare.com/zh-cn/tag/database/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
