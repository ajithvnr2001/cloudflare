---
url: https://blog.cloudflare.com/zh-cn/mitigating-broadcast-address-attack/
title: QUIC \u884c\u52a8\uff1a\u4fee\u8865\u4e00\u4e2a\u5e7f\u64ad\u5730\u5740\u653e\u5927\u6f0f\u6d1e | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:58.845276+00:00
---

# QUIC 行动：修补一个广播地址放大漏洞 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/mitigating-broadcast-address-attack/

[博客](https://blog.cloudflare.com/zh-cn/)

[DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)[Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)[HTTP3](https://blog.cloudflare.com/zh-cn/tag/http3/)+3再显示 3 个标签

6 个标签显示 6 个标签

  * 文章标签
  * [DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)[Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)[HTTP3](https://blog.cloudflare.com/zh-cn/tag/http3/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[漏洞悬赏计划](https://blog.cloudflare.com/zh-cn/tag/bug-bounty/)[网络](https://blog.cloudflare.com/zh-cn/tag/network/)
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



[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[漏洞悬赏计划](https://blog.cloudflare.com/zh-cn/tag/bug-bounty/)[网络](https://blog.cloudflare.com/zh-cn/tag/network/)

[DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)[Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)[HTTP3](https://blog.cloudflare.com/zh-cn/tag/http3/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[漏洞悬赏计划](https://blog.cloudflare.com/zh-cn/tag/bug-bounty/)[网络](https://blog.cloudflare.com/zh-cn/tag/network/)

2025年2月10日

# QUIC 行动：修补一个广播地址放大漏洞

![Josephine Chow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW496EEZSG9EMYJFTHPP2Q8A.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![June Slater](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SCBXA2XSNDDC08ZYCVCS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Josephine Chow](https://blog.cloudflare.com/zh-cn/author/josephine-chow/)、[June Slater](https://blog.cloudflare.com/zh-cn/author/june-slater/)、[Bryton Herdes](https://blog.cloudflare.com/zh-cn/author/bryton/)和[Lucas Pardue](https://blog.cloudflare.com/zh-cn/author/lucas/)

阅读时间：8 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/mitigating-broadcast-address-attack/)和[繁體中文](https://blog.cloudflare.com/zh-tw/mitigating-broadcast-address-attack/).

![BLOG-2578 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44YRG2V5KTM9Y6RZ9WG963.png&w=1999&h=1126&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////87vDx4+Tt5+fx8PD28fPz7O7q////////6u312d7w2uH05uv57fD27e7t////////5+z5z9r1ztz53ej96vD57+/x////////6e/+ztz6zN3+3er/7fP+8/P1////////8fb/2uX/2ef/6PP/9fr/+fn6/////////P//6/H/7fT/+f/////////+////////////+vv//v//////////////////////////////////////////////)

Cloudflare 最近接到了一组匿名安全研究人员的联系，他们通过 [_QUIC_](https://blog.cloudflare.com/tag/quic) 互联网测量研究发现了一个广播放大漏洞。我们的团队通过公开漏洞悬赏计划与这些研究人员合作，并且已经努力完全修补了一个影响 Cloudflare 基础设施的危险漏洞。

自从收到关于此漏洞的通知以来，Cloudflare 已经实施了一项缓解措施，帮助保护我们的基础设施。根据我们的分析，Cloudflare 已经完全修补了此漏洞，广播放大攻击手段不再存在。

### 放大攻击概述

QUIC 是一种默认加密的互联网传输协议。它提供与传输控制协议 [_(TCP)_](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) 和传输层安全性协议 [_(TLS)_](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) 相同的功能，但与此同时它使用的握手序列更短，这有助于缩短建立连接的时间。QUIC 在用户数据报协议 [_(UDP)_](https://www.cloudflare.com/en-gb/learning/ddos/glossary/user-datagram-protocol-udp/) 上运行。

研究人员发现，针对广播 IP 目标地址的单个客户端 QUIC [_初始数据包_](https://datatracker.ietf.org/doc/html/rfc9000#section-17.2.2)可能会触发大量初始数据包响应。这同时表现为服务器 CPU 放大攻击和反射放大攻击。

### 传输与安全握手

如果使用 TCP 和 TLS，则有两次握手交互。首先，是 TCP 三步传输握手。客户端向服务器发送 SYN 包，服务器以 SYN-ACK 响应给客户端，然后客户端以 ACK 响应。此过程会验证客户端 IP 地址。其次，是 TLS 安全握手。客户端向服务器发送 ClientHello，服务器执行一些加密操作，然后以包含服务器证书的 ServerHello 响应。客户端验证证书，确认握手并发送应用流量，例如 HTTP 请求。

[ _QUIC_](https://datatracker.ietf.org/doc/html/rfc9000#section-7) 遵循类似的过程，只不过握手序列更短，因为传输与安全握手结合在一起。客户端向服务器发送包含 ClientHello 的初始数据包，服务器执行一些加密操作，然后以包含 ServerHello 和服务器证书的初始数据包响应。客户端验证证书，然后发送应用数据。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2578 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492CZC95G22Z2Z7ANY2TXS.png&w=715&h=512&f=webp&fit=cover&position=center)

QUIC 握手不要求首先验证客户端 IP 地址，然后开始安全握手。这意味着，攻击者可以仿冒客户端 IP，导致服务器完成加密工作并将数据发送到目标受害者 IP（也称为[ _反射攻击_](https://blog.cloudflare.com/reflections-on-reflections/)）。[ _RFC 9000_](https://datatracker.ietf.org/doc/html/rfc9000) 仔细描述了由此带来的风险，并提供了降低风险的应对机制（例如，请参阅第 [_8_](https://datatracker.ietf.org/doc/html/rfc9000#section-8) 和第 [_9.3.1_](https://datatracker.ietf.org/doc/html/rfc9000#section-9.3.1) 部分）。在验证客户端地址之前，服务器采用反放大限制，发送的字节数最多是其接收的字节数的 3 倍。此外，服务器可以通过响应一个[ _重试数据包_](https://datatracker.ietf.org/doc/html/rfc9000#section-8.1.2)来启动地址验证，然后进行加密握手。但是，这种重试机制在 QUIC 握手序列的基础上增加了额外的往返，从而抵消了其相对于 TCP 的一些优势。真实的 QUIC 部署会使用一系列策略和启发式方法，来检测流量负载并启用不同的缓解措施。

为了了解研究人员如何克服这些 QUIC 防护措施来触发放大攻击，我们首先需要深入了解 IP 广播的工作原理。

### 广播地址

在互联网协议版本 4 (IPv4) 寻址过程中，任何指定[ _子网_](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)中的最终地址都是一个特殊的广播 IP 地址，用于将数据包发送到 IP 地址范围内的每个节点。同一子网内的每个节点都会接收发送到这个广播地址的任何数据包，这让某个发送者发送一则消息后，该消息可能会被数百个相邻节点“听到”。大多数连网系统都默认启用这种行为，并且这对于发现同一 IPv4 网络中的各种设备至关重要。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2578 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HDDPSHD6HW3WNRSG3HBC.png&w=715&h=334&f=webp&fit=cover&position=center)

广播地址自然而然会带来 DDoS 放大风险；因为每发送一个数据包，就有数百个节点必须处理流量。

### 处理预期的地址广播

为了应对广播地址带来的风险，默认情况下，大多数路由器会拒绝来自其 IP 子网之外的数据包，这些数据包是针对它们本地连接的网络的广播地址。只允许在同一 IP 子网内转发广播数据包，从而防止来自互联网的攻击将全球各地的服务器作为攻击目标。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2578 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47FR1ETR6AP7J1HPMPGC5S.png&w=715&h=542&f=webp&fit=cover&position=center)

如果指定的路由器未直接连接到指定的子网，则通常不会应用相同的技术。只要地址在本地不被视为广播地址，[ _边界网关协议_](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) (BGP) 或其他路由协议会继续将来自外部 IP 的流量路由到子网中的最后一个 IPv4 地址。从本质上讲，这意味着“广播地址”仅与通过以太网连接在一起的路由器和主机的本地范围相关。对于互联网上的路由器和主机，广播 IP 地址的路由方式与任何其他 IP 相同。

### 将 IP 地址范围绑定到主机

每台 Cloudflare 服务器都应该能够为 Cloudflare 网络上的每一个网站提供内容。由于 Cloudflare 网络使用 [_Anycast_](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) 路由，因此，每台服务器必须监听我们网络中使用的每个 Anycast IP 地址（并能够从这些地址返回流量）。

为此，我们利用了每台服务器上的环回接口。与物理网络接口不同，当绑定到环回接口时，指定 IP 地址范围内的所有 IP 地址都可供主机使用（并将由内核在本地进行处理）。

其工作机制非常简单易懂。在传统路由环境中，使用[ _最长前缀匹配_](https://en.wikipedia.org/wiki/Longest_prefix_match)来选择路由。在最长前缀匹配原则下，将会优先选择更具体的 IP 地址块（例如 192.0.2.96/29，8 个地址范围）的路由，而不是较笼统的 IP 地址块（例如 192.0.2.0/24，256 个地址范围）的路由。

虽然 Linux 使用最长前缀匹配，但它在立即搜索匹配项之前会执行一个额外步骤，查询路由策略数据库 (RPDB)。RPDB 包含一个路由表列表，其中可能包含路由信息及各自的优先级。默认的 RPDB 如下所示：
    
    
    $ ip rule show
    0:	from all lookup local
    32766:	from all lookup main
    32767:	from all lookup default

Linux 将按照数字升序查询每个路由表，尝试找到匹配的路由。一旦找到，便会终止搜索并立即使用路由。

如果您以前使用过 Linux 系统中的路由规则，您可能会熟悉主表的内容。与其中存在的名为“default”的表相反，“main”表通常用作默认的查找表。它也是包含我们传统上与路由表信息关联的内容的表。
    
    
    $ ip route show table main
    default via 192.0.2.1 dev eth0 onlink
    192.0.2.0/24 dev eth0 proto kernel scope link src 192.0.2.2

但是，这并不是第一个要查询的路由表。相反，该任务落入了本地表：
    
    
    $ ip route show table local
    local 127.0.0.0/8 dev lo proto kernel scope host src 127.0.0.1
    local 127.0.0.1 dev lo proto kernel scope host src 127.0.0.1
    broadcast 127.255.255.255 dev lo proto kernel scope link src 127.0.0.1
    local 192.0.2.2 dev eth0 proto kernel scope host src 192.0.2.2
    broadcast 192.0.2.255 dev eth0 proto kernel scope link src 192.0.2.2

查看表格，我们看到两种新型路由：本地路由和广播路由。顾名思义，二者具有两种截然不同的功能：本地处理的路由，以及将导致数据包被广播的路由。本地路由提供所需的功能，即：任何包含本地路由的前缀都会由内核处理该范围内的所有 IP 地址。广播路由将导致将数据包被广播到指定范围内的所有 IP 地址。如果 IP 地址绑定到接口，则会自动添加这两种类型的路由（并且，如果某个范围绑定到环回 (lo) 接口，则该范围本身将作为本地路由添加）。

### 漏洞发现

QUIC 部署高度依赖于其所处的负载平衡和数据包转发基础设施。虽然 QUIC 的 RFC 描述了风险和缓解措施，但仍然可能存在攻击手段，具体取决于服务器部署的性质。报告漏洞的研究人员研究了互联网上的 QUIC 部署，并且发现，向 Cloudflare 的某个广播地址发送 QUIC 初始数据包会触发大量响应。响应数据的总量超过了 RFC 的 3 倍放大限制。

通过查看示例 Cloudflare 系统的本地路由表，我们发现了一个潜在的原因：
    
    
    $ ip route show table local
    local 127.0.0.0/8 dev lo proto kernel scope host src 127.0.0.1
    local 127.0.0.1 dev lo proto kernel scope host src 127.0.0.1
    broadcast 127.255.255.255 dev lo proto kernel scope link src 127.0.0.1
    local 192.0.2.2 dev eth0 proto kernel scope host src 192.0.2.2
    broadcast 192.0.2.255 dev eth0 proto kernel scope link src 192.0.2.2
    local 203.0.113.0 dev lo proto kernel scope host src 203.0.113.0
    local 203.0.113.0/24 dev lo proto kernel scope host src 203.0.113.0
    broadcast 203.0.113.255 dev lo proto kernel scope link src 203.0.113.0

在这个示例系统中，已使用标准工具将 Anycast 前缀 203.0.113.0/24 绑定到环回 (lo) 接口。该工具严格遵守 IPv4 标准，为接口分配了两种特殊类型的路由：一是用于 IP 范围本身的本地路由，二是用于该范围内最终地址的广播路由。

虽然流向 Cloudflare 路由器直连子网的广播地址的流量会按预期被过滤出去，但针对我们路由的 Anycast 前缀的广播流量仍然会到达 Cloudflare 服务器本身。通常情况下，到达环回接口的广播流量不会造成什么问题。绑定到整个地址范围内特定端口的服务，将接收发送到该广播地址的数据并继续正常运行。但遗憾的是，当期望破灭时，这种相对简单的特征就会失效。

Cloudflare 的前端由多个 Worker 进程组成，每个进程独立绑定到 UDP 端口 443 上的整个 Anycast 范围。为了使多个进程能够绑定到同一端口，我们使用 SO_REUSEPORT 套接字选项。虽然 SO_REUSEPORT [_会带来额外的好处_](https://blog.cloudflare.com/the-sad-state-of-linux-socket-balancing/)，但它也会导致发送到广播地址的流量被复制到每一个监听器。

每个 QUIC 服务器 worker 都独立运行。它们都对同一客户端初始请求做出反应，从而导致服务器端的重复工作以及生成流向客户端 IP 地址的响应流量。因此，单个数据包可能会触发一次显著的流量放大。虽然具体情况因实施而异，但在 128 核系统上，典型的每核一个监听器堆栈（发送重试消息来响应假定的超时）可能会导致为每个发送到广播地址的数据包生成并发送 384 个回复。

虽然研究人员展示了针对 QUIC 的这种攻击，但潜在漏洞可能会影响以相同方式使用套接字的其他 UDP 请求/响应协议。

### 缓解

作为一种通信方式，广播通常并不适合 Anycast 前缀。因此，缓解此问题的最简单方法就是禁用每个范围内最终地址的广播功能。

理想情况下，可以通过修改工具来实现这一点：只在本地路由表中添加本地路由，完全跳过广播路由的方式。遗憾的是，唯一可行的机制是修补和维护 Cloudflare iproute2 套件的内部分叉工具，但这是解决当前问题的一种相当笨拙的办法。

相反，我们决定专注于移除路由本身。与任何其他路由类似，可以使用标准工具将其移除：
    
    
    $ sudo ip route del 203.0.113.255 table local

为了大规模地这样做，我们对部署系统进行了微调更改：
    
    
      {%- for lo_route in lo_routes %}
        {%- if lo_route.type == "broadcast" %}
            # All broadcast addresses are implicitly ipv4
            {%- do remove_route({
            "dev": "lo",
            "dst": lo_route.dst,
            "type": "broadcast",
            "src": lo_route.src,
            }) %}
        {%- endif %}
      {%- endfor %}

如此一来，我们可以有效确保移除那些附加到环回接口的所有广播路由，从而确保以同样的方式来处理规范定义的广播地址与该范围内的其他地址，以此来缓解风险。

### 后续步骤

虽然此漏洞特别影响了我们 Anycast 范围内的广播地址，但它很可能已经扩展到 Cloudflare 基础设施之外。除非采取缓解措施，否则任何拥有满足相对狭窄标准的基础设施（多 worker、基于 UDP 服务的多监听器，该服务绑定到计算机上的所有 IP 地址并附加可路由的 IP 前缀，从而暴露广播地址）的客户都会受到影响。我们鼓励网络管理员和安全专业人员评估其各自的系统，了解可能存在局部放大攻击手段的配置。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmitigating-broadcast-address-attack%2F&t=QUIC%20%E8%A1%8C%E5%8A%A8%EF%BC%9A%E4%BF%AE%E8%A1%A5%E4%B8%80%E4%B8%AA%E5%B9%BF%E6%92%AD%E5%9C%B0%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E)[](https://x.com/intent/post?text=QUIC+%E8%A1%8C%E5%8A%A8%EF%BC%9A%E4%BF%AE%E8%A1%A5%E4%B8%80%E4%B8%AA%E5%B9%BF%E6%92%AD%E5%9C%B0%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmitigating-broadcast-address-attack%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmitigating-broadcast-address-attack%2F)[](https://bsky.app/intent/compose?text=QUIC+%E8%A1%8C%E5%8A%A8%EF%BC%9A%E4%BF%AE%E8%A1%A5%E4%B8%80%E4%B8%AA%E5%B9%BF%E6%92%AD%E5%9C%B0%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmitigating-broadcast-address-attack%2F)[](https://mastodonshare.com/?text=QUIC+%E8%A1%8C%E5%8A%A8%EF%BC%9A%E4%BF%AE%E8%A1%A5%E4%B8%80%E4%B8%AA%E5%B9%BF%E6%92%AD%E5%9C%B0%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmitigating-broadcast-address-attack%2F)[](https://www.threads.net/intent/post?text=QUIC+%E8%A1%8C%E5%8A%A8%EF%BC%9A%E4%BF%AE%E8%A1%A5%E4%B8%80%E4%B8%AA%E5%B9%BF%E6%92%AD%E5%9C%B0%E5%9D%80%E6%94%BE%E5%A4%A7%E6%BC%8F%E6%B4%9E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmitigating-broadcast-address-attack%2F)

## 相关标签

[DDoS](https://blog.cloudflare.com/zh-cn/tag/ddos/)[Edge](https://blog.cloudflare.com/zh-cn/tag/edge/)[HTTP3](https://blog.cloudflare.com/zh-cn/tag/http3/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[漏洞悬赏计划](https://blog.cloudflare.com/zh-cn/tag/bug-bounty/)[网络](https://blog.cloudflare.com/zh-cn/tag/network/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Bryton Herdes](https://blog.cloudflare.com/zh-cn/author/bryton/)

[](https://next-hopself.net/)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
