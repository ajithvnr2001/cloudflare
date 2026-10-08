---
url: https://blog.cloudflare.com/zh-cn/workflows-v2/
title: \u91cd\u6784 Workflows \u63a7\u5236\u5e73\u9762\uff0c\u4ee5\u6ee1\u8db3\u667a\u80fd\u4f53\u65f6\u4ee3\u7684\u9700\u6c42 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:36.882829+00:00
---

# 重构 Workflows 控制平面，以满足智能体时代的需求 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/workflows-v2/

[博客](https://blog.cloudflare.com/zh-cn/)

[Agents Week](https://blog.cloudflare.com/zh-cn/tag/agents-week/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)+3再显示 3 个标签

6 个标签显示 6 个标签

  * 文章标签
  * [Agents Week](https://blog.cloudflare.com/zh-cn/tag/agents-week/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[智能体](https://blog.cloudflare.com/zh-cn/tag/agents/)
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



[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[智能体](https://blog.cloudflare.com/zh-cn/tag/agents/)

[Agents Week](https://blog.cloudflare.com/zh-cn/tag/agents-week/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[智能体](https://blog.cloudflare.com/zh-cn/tag/agents/)

2026年4月15日

# 重构 Workflows 控制平面，以满足智能体时代的需求

![Luís Duarte](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4768W5B20EQMM9ZD5AQMED.png&w=64&h=64&f=webp&fit=cover&position=center)![Mia Malden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4559TC07A12MQHAEK8YM1R.jpg&w=64&h=64&f=webp&fit=cover&position=center)![André Venceslau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TZTSTWQ6JMKEC8GX38NE.png&w=64&h=64&f=webp&fit=cover&position=center)

[Luís Duarte](https://blog.cloudflare.com/zh-cn/author/luis-duarte/)、[Mia Malden](https://blog.cloudflare.com/zh-cn/author/mia/)和[André Venceslau](https://blog.cloudflare.com/zh-cn/author/andre-venceslau/)

阅读时间：9 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/workflows-v2/)、[日本語](https://blog.cloudflare.com/ja-jp/workflows-v2/)、[한국어](https://blog.cloudflare.com/ko-kr/workflows-v2/)和[繁體中文](https://blog.cloudflare.com/zh-tw/workflows-v2/).

![BLOG-3116 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4613X11Z7NGW59B8JV13NE.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+fz84erz0+Dv3ebz7fH38vT06+7r////+v3/4+r10d3w09/04Or46e/16u7t/////f//6Oz40tvyytr20uP74Ov46+7w////////7/H82d/2zNv60OP+3+z87/H1////////+fn/5uj82uT/3Ov/6fP/9/f6////////////9PT/7fL/8Pf/+Pz///3///////////////3//f3/////////////////////////////////////////////)

我们在最初构建 [_Workflows_](https://developers.cloudflare.com/workflows/)（支持多步骤应用的持久化执行引擎）时，其设计理念是用于用户注册或下单等人工操作触发的工作流。对于用户引导流程等用例，工作流只需支持每人一个实例，人类用户的点击速度毕竟有限。

随着时间的推移，我们实际观察到的是工作负载和访问模式发生了量化转变：人工操作触发的工作流减少，智能体触发的工作流增加，且此类工作流以机器速度创建。

由于智能体成为持久、自主的基础设施，代表用户运行数小时或数天，它们需要一个持久、异步的执行引擎来处理其正在进行的工作。Workflows 恰好具备这项功能：每个步骤均可独立重试，可暂停工作流进行人工干预审批，并且每个实例在发生故障后仍能继续运行而不丢失进度。

此外，工作流本身用于实施智能体循环，并充当管理和维持智能体持续运行的持久工具。Cloudflare [_Agents SDK 集成_](https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/)加速了这个进程，帮助智能体轻松生成工作流实例并获取实时进度信息。现在，单个智能体会话可以启动数十个工作流，多个智能体并发运行则意味着可以在几秒钟内创建数千个实例。随着 [_Project Think_](https://blog.cloudflare.com/project-think) 的推出，我们预计创新速度将只会提高。

为了帮助开发人员在 Workflows 上扩展智能体和应用，Cloudflare 很高兴地宣布我们现在支持：

  * 50,000 个并发实例（并行运行的工作流执行数量），[ _最初为 4,500 个_](https://developers.cloudflare.com/changelog/post/2025-02-25-workflows-concurrency-increased/)
  * 每个账户每秒创建 300 个实例，之前为 100 个
  * 每个工作流支持 200 万个已加入队列实例（即：已创建或已唤醒且正在等待并发槽位的实例），之前的上限为 100 万个



我们根据使用数据和基本原理重新设计了 Workflows 控制平面，以支持这些增长。在第一版控制平面中，单个 Durable Object (DO) 可以充当整个账户的中央注册表和协调器。在第二版中，我们构建了两个新组件，以帮助横向扩展系统并缓解第一版引入的瓶颈，然后将所有客户（包括实时流量）无缝迁移到新版本。

## 第一版：Workflows 的初始架构

正如我们在[ _公开测试版博客文章_](https://blog.cloudflare.com/building-workflows-durable-execution-on-workers/#building-cloudflare-on-cloudflare)中所述，[ _Workflows_](https://www.cloudflare.com/developer-platform/products/workflows/) 完全基于 Cloudflare 开发人员平台构建。从根本上说，工作流是一系列持久步骤，每个步骤都可以单独重试，能够执行任务、等待外部事件或休眠到预定时间。
    
    
    export class MyWorkflow extends WorkflowEntrypoint {
    
      async run(event, step) {
        const data = await step.do("fetch-data", async () => {
          return fetchFromAPI();
        });
    
        const approval = await step.waitForEvent("approval", {
          type: "approval",
          timeout: "24 hours",
        });
    
        await step.do("process-and-save", async () => {
          return store(transform(data));
        });
      }
    }
    

为了触发每个实例、执行其逻辑并存储其元数据，我们利用了由 SQLite 提供支持的 [_Durable Objects_](https://www.cloudflare.com/developer-platform/products/durable-objects/)，这是分布式系统中用于协调和存储数据的一种简单却功能强大的原语。

在控制平面中，一些 Durable Objects（例如执行实际工作流实例的 _Engine_ ，包括其步骤、重试和休眠逻辑）按 1:1 的比例逐个实例启动。另一方面， _Account_ 是一个账户级持久对象，用于管理该账户的所有工作流和工作流实例。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3116 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW476HKM08WHF56TFMTT2ZRM.png&w=715&h=524&f=webp&fit=cover&position=center)

如需了解关于第一版控制平面的更多信息，请参阅我们的 [_Workflows 公告博客文章_](https://blog.cloudflare.com/building-workflows-durable-execution-on-workers/)。

在 Workflows 进入测试阶段后，我们欣喜地看到客户迅速扩展了对这款产品的使用，但我们同时也意识到，使用单个 Durable Object 来存储所有账户级信息会造成瓶颈。许多客户需要每分钟创建并执行数百个甚至数千个工作流实例，这很容易导致我们原有架构中的 _Account_ 不堪重负。最初的速率限制（4,500 个并发槽位以及每 10 秒创建 100 个实例）正是基于这一限制而设定。

在第一版控制平面上，这些限制是硬上限。所有依赖于 _Account_ 的操作都必须经过单个 DO，包括创建、更新和列出。对于拥有高并发工作负载的用户，任何时刻都可能会启动和结束数千个实例，导致 _Account_ 每秒收到数千个请求。为了解决这个问题，我们重构了工作流控制平面，使其能够横向扩展以支持更高的并发和创建速率限制。

## 第二版：横向扩展以提高吞吐量

在新版本中，我们从底层重新设计了每一个操作，目标是优化高容量工作流。归根结底，Workflows 应能够扩展以支持开发人员的需求：无论是每秒创建数千个实例，还是一次运行数百万个实例。我们还希望确保第二版考虑到灵活调整的限制，以便我们可以切换这些限制并持续提高，而不是像第一版那样设置硬上限。经过多次设计迭代，我们最终确定了新架构的以下支柱：

  * 特定实例是否存在的唯一可靠来源应该是其 _Engine_ ，而不是什么别的东西。
    * 在第一版控制平面架构中，我们缺少将实例加入队列之前的检查，以判断其 _Engine_ 是否实际存在。这导致出现了一种错误状态，即：实例可能已被加入队列，但其对应的 _Engine_ 尚未启动。
    * 实例生命周期和存活机制必须按工作流横向扩展，并分布在多个区域。
  * 新的 Account 单一实例应该只存储最小的必要元数据，并且拥有固定的最大并发请求数量。



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3116 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WPSJARNNF1HB3CZV0GKM.png&w=715&h=414&f=webp&fit=cover&position=center)

第二版控制平面中新增了两个关键组件，让我们能够提高 Workflows 的可扩展性： _SousChef_ 与 _Gatekeeper_ 。第一个组件 _SousChef_ 是 _Account_ 的“副指挥”。回想一下，前文所述的 _Account_ 管理着指定账户内所有工作流中所有实例的元数据和生命周期。引入 _SousChef_ 是为了跟踪指定工作流中实例**子集** 的元数据和生命周期。账户内分布的多个 _SousChef_ 可以更高效、更便捷地向 _Account_ 报告信息。（这种设计的另一个好处是：我们不仅实现了按账号隔离，而且还意外地在同一账户内实现了“按工作流”隔离，因为每个 _SousChef_ 仅负责一个特定的工作流。）

第二个组件 _Gatekeeper_ 是一种机制，用于将并发槽位（源自并发限制）分配给账户内的所有 _SousChef_ 。它类似于一个租赁系统。创建一个实例后，它会被随机分配给该账户内的某个 _SousChef_ 。然后， _SousChef_ 向 _Account_ 发起请求以触发该实例。账户要么为实例分配一个槽位，要么将其加入队列。获得分配的槽位后， _SousChef_ 会触发实例执行并确保该实例不会被卡住。

 _Gatekeeper_ 的作用是确保 _Engine_ 不会使 _Account_ 过载（这是第一版中一个迫在眉睫的风险）；因此， _SousChef_ 与其 _Account_ 之间的所有通信都以每秒一次的周期进行，每个周期还会批量处理所有槽位请求，以确保只进行一次 JSRPC 调用。这将确保实例创建率永远不会使最重要的组件 _Account_ 过载或受到影响（顺便说一句：如果 _SousChef_ 实例数量过高，我们会对调用请求进行速率限制，或将其分散到不同 _SousChef_ 实例，并在不同的时间段内执行）。此外，这种周期性特性让我们能够维护旧实例的公平性，并确保多个 _SousChef_ 之间实现最大-最小公平性原则，从而让所有 SousChef 都能取得进展。例如，如果某个实例被唤醒，它应优先于新建的实例获得槽位，但每个 _SousChef_ 会确保自己的实例不会被卡住。

这种架构更加分布式，因此，更具可扩展性。现在，创建一个实例后，请求路径如下：

  1. 检查控制平面版本
  2. 检查该位置是否有工作流的缓存版本以及版本详细信息可用
     1. 如果没有，则检查 _Account_ 以获取工作流名称、唯一 ID 和版本，并缓存这些信息
  3. 仅将必要的元数据（例如实例有效负载、创建日期）存储到其自身的 _Engine_



那么， _Engine_ 如何告知控制平面它已存在呢？这会在实例元数据设置完成后在后台发生。由于针对 Durable Object 的后台操作可能因清理或服务器故障而失败，因此，我们还会在创建热路径的 _Engine_ 上设置“报警”。这样一来，如果后台任务没有完成，报警会**确保** 启动实例。

[ _Durable Object 警报_](https://developers.cloudflare.com/durable-objects/api/alarms/)允许在未来的某个特定时间点以**至少一次** 的执行模型唤醒 Durable Object 实例，且内置自动重试功能。我们广泛使用这种后台“任务”与警报组合，将操作从热路径中移除，同时确保一切按计划进行。这就是我们在不牺牲可靠性的前提下，保持快速执行 _创建实例_ 等关键操作的方法。

除了扩展功能之外，第二版控制平面还意味着：

  * 实例列表性能更快，并且实际上与游标分页保持一致；
  * 针对实例执行的任何操作仅完成一个网络跳数（因为它可以直接访问其 _Engine_ ，确保用户感知的网络响应延迟尽可能小）；
  * 我们可以确保更多实例能够真正并发地正常运行（通过按时运行），以及在出现问题时进行纠正，从而确保 _Engine_ 永远不会延迟继续执行。



## 从第一版迁移到第二版

鉴于我们已拥有能够处理更高用户负载的新版 Workflows 控制平面，接下来我们需要完成“枯燥乏味”的部分：将客户和实例迁移到新系统。对于 Cloudflare 平台规模来说，这本身就是一个难题，因此，“枯燥乏味”的部分反而变成了最大的挑战。Workflows 上线不到一年，已经积累了数百万个实例和数千个客户。此外，第一版控制平面存在一些技术债务，这意味着加入队列的实例可能尚未创建自己的 _Engine_ Durable Object，这进一步加剧了问题的复杂性。

这样的迁移非常棘手，因为客户可能随时都在运行实例；我们需要一种方法将 _SousChef_ 和 _Gatekeeper_ 组件添加到旧账户，而不造成任何中断或停机。

最终，我们决定将现有 _Account_ （我们称之为 _AccountOld_ ）迁移到与 _SousChef_ 相同的行为模式。通过持久化 _Account_ DO，我们维护了实例元数据并简单地将 DO 转换成了 _SousChef_ “DO”：
    
    
    // You might be wondering what's this SousChef class? This is the SousChef DO class!
    import { SousChef } from "@repo/souschef";
    
    class AccountOld extends DurableObject {
      constructor(state: DurableObjectState, env: Env) {
        // We added the following snippet to the end of our AccountOld DO's
        // constructor. This ensures that if we want, we can use any primitive
        // that is available on SousChef DO
        if (this.currentVersion === ControlPlaneVersions.SOUS_CHEFS) {
          this.sousChef = new SousChef(this.ctx, this.env);
          await this.sousChef.setup()
        }
      }
    
      async updateInstance(params: UpdateInstanceParams) {
        if (this.currentVersion === ControlPlaneVersions.SOUS_CHEFS) {
          assert(this.sousChef !== undefined, 'SousChef must exist on v2');
          return this.sousChef.updateInstance(params);
        }
    
        // old logic remains the same
      }
    
      @RequiresVersion<AccountOld>(ControlPlaneVersions.V1)
      async getMetadata() {
        // this method can only be run if 
        // this.currentVersion === ControlPlaneVersions.V1
      }
    }

我们可以实例化 _AccountOld_ 中的 _SousChef_ 类，因为 _SousChef_ 和 _AccountOld_ DO 用于跟踪实例元数据的 SQL 表是相同的。因此，我们只需决定使用哪个版本的代码即可。如果不是这样的话，我们将不得不迁移数百万个实例的元数据，这可能会导致每个账户的迁移更加困难、耗时更长。那么，如何进行迁移呢？

首先，我们准备好切换 _AccountOld_ DO，使其行为类似于 _SousChef_ （这意味着创建一个包含上述代码片段的版本）。然后，我们按账户启用第二版控制平面，这会大致同时触发以下三个步骤：

  * 现在，所有新实例创建请求均路由到新的 _SousChef_ （收到第一个请求后创建 _SousChef_ ），新实例再也不路由到 _AccountOld_ ；
  *  _AccountOld_ DO 开始切换，使其行为类似于 _SousChef_ ；
  * 新 _Account_ DO 启动，并包含相应的元数据。



在将所有账户迁移到新版控制平面后，便可以随着 _AccountOld_ DO 实例保留期的到期将其废止。 _AccountOld_ 上所有账户的所有实例都迁移完毕之后，便可以永久关闭这些 DO。整个迁移过程零停机，就像在驾驶途中更换汽车轮胎一样。

## 立即试用

如果您是 Workflows 新手，请查看我们的[ _入门指南_](https://developers.cloudflare.com/workflows/get-started/guide/)，或者使用 Workflows [_构建第一个持久智能体_](https://developers.cloudflare.com/workflows/get-started/durable-agents/)。

如果您的用例所需限制比我们新的默认设置更高（并发限制为 50,000 个槽位，账户级创建速率限制为每秒 300 个实例，每个工作流 100 个实例），请通过客户团队或填写 [_Workers 限制请求表单_](https://forms.gle/ukpeZVLWLnKeixDu7)联系我们。您还可以在我们的 [_Discord 服务器_](https://discord.com/channels/595317990191398933/1296923707792560189)上提出反馈和功能请求，或分享您的 Workflows 使用体验。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkflows-v2%2F&t=%E9%87%8D%E6%9E%84%20Workflows%20%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%EF%BC%8C%E4%BB%A5%E6%BB%A1%E8%B6%B3%E6%99%BA%E8%83%BD%E4%BD%93%E6%97%B6%E4%BB%A3%E7%9A%84%E9%9C%80%E6%B1%82)[](https://x.com/intent/post?text=%E9%87%8D%E6%9E%84+Workflows+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%EF%BC%8C%E4%BB%A5%E6%BB%A1%E8%B6%B3%E6%99%BA%E8%83%BD%E4%BD%93%E6%97%B6%E4%BB%A3%E7%9A%84%E9%9C%80%E6%B1%82&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkflows-v2%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkflows-v2%2F)[](https://bsky.app/intent/compose?text=%E9%87%8D%E6%9E%84+Workflows+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%EF%BC%8C%E4%BB%A5%E6%BB%A1%E8%B6%B3%E6%99%BA%E8%83%BD%E4%BD%93%E6%97%B6%E4%BB%A3%E7%9A%84%E9%9C%80%E6%B1%82+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkflows-v2%2F)[](https://mastodonshare.com/?text=%E9%87%8D%E6%9E%84+Workflows+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%EF%BC%8C%E4%BB%A5%E6%BB%A1%E8%B6%B3%E6%99%BA%E8%83%BD%E4%BD%93%E6%97%B6%E4%BB%A3%E7%9A%84%E9%9C%80%E6%B1%82&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkflows-v2%2F)[](https://www.threads.net/intent/post?text=%E9%87%8D%E6%9E%84+Workflows+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%EF%BC%8C%E4%BB%A5%E6%BB%A1%E8%B6%B3%E6%99%BA%E8%83%BD%E4%BD%93%E6%97%B6%E4%BB%A3%E7%9A%84%E9%9C%80%E6%B1%82+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkflows-v2%2F)

## 相关标签

[Agents Week](https://blog.cloudflare.com/zh-cn/tag/agents-week/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[智能体](https://blog.cloudflare.com/zh-cn/tag/agents/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
