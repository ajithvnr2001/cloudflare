---
url: https://blog.cloudflare.com/zh-cn/how-cloudflare-implemented-fido2-and-zero-trust/
title: Cloudflare \u5982\u4f55\u5b9e\u65bd FIDO2 \u548c Zero Trust \u786c\u4ef6\u5bc6\u94a5\u6765\u9632\u6b62\u7f51\u7edc\u9493\u9c7c\u5462\uff1f | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:40:33.870195+00:00
---

# Cloudflare 如何实施 FIDO2 和 Zero Trust 硬件密钥来防止网络钓鱼呢？ | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/how-cloudflare-implemented-fido2-and-zero-trust/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Zero Trust](https://blog.cloudflare.com/zh-cn/tag/cloudflare-zero-trust/)[Zero Trust](https://blog.cloudflare.com/zh-cn/tag/zero-trust/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)+1再显示 1 个标签

4 个标签显示 4 个标签

  * 文章标签
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/zh-cn/tag/cloudflare-zero-trust/)[Zero Trust](https://blog.cloudflare.com/zh-cn/tag/zero-trust/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)
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



[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)

[Cloudflare Zero Trust](https://blog.cloudflare.com/zh-cn/tag/cloudflare-zero-trust/)[Zero Trust](https://blog.cloudflare.com/zh-cn/tag/zero-trust/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)

2022年9月29日

# Cloudflare 如何实施 FIDO2 和 Zero Trust 硬件密钥来防止网络钓鱼呢？

![Evan Johnson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47BS1WVZYVJDW7MV0RH2BM.png&w=64&h=64&f=webp&fit=cover&position=center)![Derek Pitts](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46384YHDK7BZNAPKRR6A3X.png&w=64&h=64&f=webp&fit=cover&position=center)

[Evan Johnson](https://blog.cloudflare.com/zh-cn/author/evan-johnson/)和[Derek Pitts](https://blog.cloudflare.com/zh-cn/author/derek-pitts/)

阅读时间：7 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/how-cloudflare-implemented-fido2-and-zero-trust/)、[Deutsch](https://blog.cloudflare.com/de-de/how-cloudflare-implemented-fido2-and-zero-trust/)、[Español](https://blog.cloudflare.com/es-es/how-cloudflare-implemented-fido2-and-zero-trust/)、[Français](https://blog.cloudflare.com/fr-fr/how-cloudflare-implemented-fido2-and-zero-trust/)、[日本語](https://blog.cloudflare.com/ja-jp/how-cloudflare-implemented-fido2-and-zero-trust/)、[한국어](https://blog.cloudflare.com/ko-kr/how-cloudflare-implemented-fido2-and-zero-trust/)和[繁體中文](https://blog.cloudflare.com/zh-tw/how-cloudflare-implemented-fido2-and-zero-trust/).

![How Cloudflare implemented hardware keys with FIDO2 and Zero Trust to prevent phishing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW449SQG6FZK347ME5C2QNBQ.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////+8vHs7Ofe8Ovf9vPn9fXu7vDu////////8fDs6OTe6+fd8/Dl9fTt8PHw////////8fHv5eLe6OTc8u7l9vTu8/Ty////////9PTz5+Tj6eXg9PDp+ffy9/j3////////+vr67evr8Ozp+vfx/v35+/z8////////////9/T0+fbz///7/////////////////////vz7///8///////////////////////////+////////////////)

几年前，Cloudflare 的安全架构是一个经典的“城堡+护城河” VPN 架构。员工使用企业 VPN 连接到所有内部应用程序和服务器来完成他们的工作。我们使用基于时间的一次性密码(TOTP)执行双因素身份验证，在登录到 VPN 时使用 Google Authenticator 或 Authy 等身份验证应用，但只有少数内部应用程序具有第二层身份验证。这种架构貌似强大，但安全模型非常弱。最近，我们[对一次被我们挫败的网络钓鱼攻击的机制](https://blog.cloudflare.com/zh-cn/2022-07-sms-phishing-attacks-zh-cn/)做了详细介绍， 其中说明了攻击者如何尝试入侵被 TOTP 等第二因素身份验证方法“保护”的应用程序。幸运的是，我们早就放弃了 TOTP，取而代之的是硬件安全密钥和 Cloudflare Access。本文详细介绍了我们是如何做到的。

网络钓鱼问题的解决方案是通过一个名为 _FIDO2/WebAuthn_ 的[多因素身份验证 (MFA)](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/)协议。所有 Cloudflare 员工都使用我们的 Zero Trust 产品，以 FIDO2 作为安全多因素和身份验证来登录我们的系统。我们的新架构具备防网络钓鱼能力，允许我们更容易地实施最少特权访问控制。

### 简单介绍一下安全密钥术语以及我们所用的安全密钥

在 2018，我们希望迁移到防网络钓鱼的 MFA 机制。我们看到 [evilginx2](https://github.com/kgretzky/evilginx2) 以及基于网络钓鱼推送到移动验证器的成熟程度，还有 TOTP。唯一能够抵御社会工程和凭据窃取攻击的防钓鱼 MFA 是采用 FIDO 标准的安全密钥。基于 FIDO2 的 MFA 引入了新的术语，如 FIDO2、WebAuthn、硬(件)密钥、安全密钥，特别是 YubiKey (一家知名硬件密钥制造商的名称)。我们将在本文中引用这些术语。

**WebAuthn** 指 [Web 身份验证标准](https://www.w3.org/TR/webauthn-2/)，当我们在 [Cloudflare 仪表板中推出对安全密钥的支持时](https://blog.cloudflare.com/cloudflare-now-supports-security-keys-with-web-authentication-webauthn/)，我们曾撰文深入介绍过这种协议的工作原理。

**CTAP1(U2F) 和 CTAP2** 指客户端到验证器协议，其中详细说明了软件或硬件设备如何与执行 WebAuthn 协议的平台交互。

**FIDO2** 以上两种用于身份验证的协议的集合。区别并不重要，但这种命名法可能引起困惑。

最重要的是要知道，所有这些协议和标准都是为了创建开放的身份验证协议而开发的，这些协议可以防范网络钓鱼，并可通过硬件设备实施。在软件方面，它们是通过 Face ID、Touch ID、Windows Assistant 或类似功能实施的。硬件方面，YubiKey 或其他单独的物理设备通过 USB、雷电接口或 NFC 用于身份验证。

FIDO2 可以防范网络钓鱼的，因为它实施加密安全的挑战/响应，而且挑战协议包含了用户进行身份验证的特定网站或域。用户合法登录到 example.net 和 example.com 时，安全密钥产生的响应是不相同的。

Cloudflare 多年来向员工发放了多种类型的安全密钥，但目前我们向所有员工发放两种不同的 FIPS 验证安全密钥。第一种是 YubiKey 5 Nano 或 YubiKey 5C Nano，旨在一直插在员工笔记本电脑的 USB 插槽中。第二种是 YubiKey 5 NFC 或 YubiKey 5C NFC，可以通过 NFC 或 USB-C 在台式机和移动设备上使用。

2018 年底，我们在一次公司全体活动中分发了安全密钥。在一个简短的研讨会上，我们要求所有员工登记他们的密钥，用它们进行身份验证，并询问有关设备的问题。这个计划取得了巨大的成功，但仍有不完善之处，部分应用程序不兼容 WebAuthn。当时我们还没有准备好全面实施安全密钥，在我们解决问题时需要一些中间解决方案。

### 开始：Cloudflare Zero Trust 的选择性安全密钥实施

我们负责维护数千个应用程序和服务器，它们由我们的 VPN 保护。我们开始将所有这些应用程序迁移到我们的 Zero Trust 访问代理，同时向员工发放了一组安全密钥。

Cloudflare Access 允许我们的员工安全地访问以往受 VPN 保护的站点。每个内部服务都将检查一个签名凭据，以验证用户的身份，并确保用户已通过我们的身份提供者登录。Cloudflare Access 对我们的安全密钥推出_是必要的_，因为它为我们提供了一个工具，可以选择性地对最初少数几个内部应用程序执行安全密钥验证。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - Zc8fCw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4937A2KW8CQJPZ0GXKQB78.png&w=715&h=343&f=webp&fit=cover&position=center)

将应用程序加入 Zero Trust 产品时，我们使用了 Terraform，这是我们首次强制使用安全密钥的 Cloudflare Access 策略。在与我们的身份提供者集成时，我们设置 Cloudflare Access 以使用 OAuth2。作为 OAuth 工作流程的一部分， 该身份提供者告知 Access 所使用的第二因素类型。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - RPatyG](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458G8SCJEBMHZKPA8RDBH0.png&w=624&h=325&f=webp&fit=cover&position=center)

在我们的例子中， [swk](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-amr-values-04) 是拥有安全钥匙的证明。如果有人登录时没有使用安全密钥，就会看到一条有用的错误消息，告知他再次登录，并在看到提示时按下安全密钥。

选择性实施立即改变了我们安全密钥推出的轨迹。我们于 2020 年 7 月 29 日在单一服务上开始实施，在接下来的两个月里，使用安全密钥的身份验证大幅增加了。这一步是至关重要的，给我们的员工提供了一个熟悉新技术的机会。选择性实施的窗口期应该是至少一个月，以考虑度假的人，但事后看来，不需要比这个时间长太多。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - LBAlSU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48JEQF1XSNFJVFDNB8C7ZB.png&w=715&h=193&f=webp&fit=cover&position=center)

通过应用程序切换到使用我们的 Zero Trust 产品并放弃 VPN，我们还获得了其他哪些安全方面的好处呢？对于传统应用程序或未实施 SAML 的应用程序，这种迁移对于执行基于角色的访问控制和最小权限原则是必要的。VPN 将对您的网络流量进行身份验证，但您的所有应用程序都不知道网络流量属于谁。我们的应用程序难以执行多级权限，并且每个权限都必须重新构建自己的认证方案。

加入到 Cloudflare Access 时，我们创建了执行 RBAC 的组，并告诉我们的应用程序每个人应该拥有什么样的权限级别。

这是一个只有 ACL-CFA-CFDATA-argo-config-admin-svc 组成员才可以访问的站点。它强制员工在登录时使用他们的安全密钥，并且不需要复杂的 OAuth 或 SAML 集成。我们有超过 600 个内部站点使用相同的模式，全部都强制使用安全密钥。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - Z0NvTw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WCWVWGR5TXY3KNPVJS2Y.png&w=715&h=754&f=webp&fit=cover&position=center)

### 可选状态的结束：Cloudflare 完全放弃 TOTP

2021 年 2 月，我们的员工开始向我们的安全团队报告社会工程攻击尝试。他们接到了自称是我们 IT 部门人员打来的电话，引起了我们的警觉。我们决定开始要求所有身份验证都使用安全密钥，以防止任何员工成为社会工程攻击的受害者。

在禁用了所有其他形式的 MFA (SMS, TOTP 等)后，除了 WebAuthn，我们开始正式仅使用 FIDO2。然而，如上图显示，“软令牌”（TOTP）使用并非完全为零。这是因为，对于那些丢失安全密钥或被锁定帐户，需要经历一个安全离线恢复过程的人，替代方法可以帮助其完成这一过程。最佳做法是为员工分发多个安全密钥，以便在出现这种情况时作为备份。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - qj40tH](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48CB24MZPBFMS83XK33K5Z.png&w=715&h=295&f=webp&fit=cover&position=center)

现在所有的员工都在使用他们的 YubiKey 执行防钓鱼 MFA，我们已经大功告成了吗？对了，SSH 和非 HTTP 协议如何处理呢？我们需要一种统一的身份和访问管理方法，因此将安全密钥引入任意其他协议是我们的下一个考虑。

### 为 SSH 使用安全密钥

为了支持将安全密钥引入到 SSH 连接，我们将 [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/) 部署到所有的生产基础设施。Cloudflare Tunnel 与 Cloudflare Access 无缝集成，无论通过隧道的是什么协议，同时运行隧道需要隧道客户端 [cloudflared](https://github.com/cloudflare/cloudflared)。这意味着我们可以将 cloudflared 二进制文件部署到我们所有的基础设施中，并创建到每台机器的隧道，在需要安全密钥的地方创建 Cloudflare Access 策略，SSH 连接将开始通过 Cloudflare Access 要求使用安全密钥。

在实践中，这些步骤并没有听起来那么令人生畏，Zero Trust 开发文档中包含有关做到这一点的[优秀教程](https://developers.cloudflare.com/cloudflare-one/tutorials/ssh-cert-bastion/) 。我们的每个服务器都有启动隧道所需的配置文件。Systemd 调用 cloudflared，后者在启动隧道时使用这个(或类似的)配置文件。

当操作员需要使用 SSH 接入我们的基础设施时，他们使用 ProxyCommand SSH 指令调用 cloudflared，用 Cloudflare Access 进行身份验证，然后通过 Cloudflare 转发 SSH 连接。我们员工的 SSH 配置有一个类似这样的条目，可以用 cloudflared 中的 helper 命令生成：
    
    
    tunnel: 37b50fe2-a52a-5611-a9b1-ear382bd12a6
    credentials-file: /root/.cloudflared/37b50fe2-a52a-5611-a9b1-ear382bd12a6.json
    
    ingress:
      - hostname: <identifier>.ssh.cloudflare.com
        service: ssh://localhost:22
      - service: http_status:404

值得注意的是，OpenSSH 从 [8.2 版](https://www.openssh.com/txt/release-8.2)开始支持 FIDO2，但我们发现使用统一的访问控制方法(所有的访问控制列表都在单一地方维护)是有好处的。
    
    
    Host *.ssh.cloudflare.com
        ProxyCommand /usr/local/bin/cloudflared access ssh –hostname %h.ssh.cloudflare.com

### 我们的收获以及我们的经验如何帮助你

经过这几个月，毫无疑问，身份验证的未来是 FIDO2 和 WebAuthn。这个过程总共花了我们几年的时间，我们希望这些经验能够对其他希望使用基于 FIDO 的认证进行现代化的组织有所帮助。

如果您有意在自己的组织推出安全密钥，或者对 Cloudflare 的 Zero Trust 产品感兴趣，欢迎通过 [securitykeys@cloudflare.com](mailto:securitykeys@cloudflare.com)联系我们。我们的预防措施帮助抵御了最新一轮的网络钓鱼和社会工程攻击，让我们非常高兴，但我们的[安全团队](https://www.cloudflare.com/careers/jobs/?department=Security)仍在不断成长，以帮助预防接下来发生的任何事情。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F&t=Cloudflare%20%E5%A6%82%E4%BD%95%E5%AE%9E%E6%96%BD%20FIDO2%20%E5%92%8C%20Zero%20Trust%20%E7%A1%AC%E4%BB%B6%E5%AF%86%E9%92%A5%E6%9D%A5%E9%98%B2%E6%AD%A2%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E5%91%A2%EF%BC%9F)[](https://x.com/intent/post?text=Cloudflare+%E5%A6%82%E4%BD%95%E5%AE%9E%E6%96%BD+FIDO2+%E5%92%8C+Zero+Trust+%E7%A1%AC%E4%BB%B6%E5%AF%86%E9%92%A5%E6%9D%A5%E9%98%B2%E6%AD%A2%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E5%91%A2%EF%BC%9F&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)[](https://bsky.app/intent/compose?text=Cloudflare+%E5%A6%82%E4%BD%95%E5%AE%9E%E6%96%BD+FIDO2+%E5%92%8C+Zero+Trust+%E7%A1%AC%E4%BB%B6%E5%AF%86%E9%92%A5%E6%9D%A5%E9%98%B2%E6%AD%A2%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E5%91%A2%EF%BC%9F+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)[](https://mastodonshare.com/?text=Cloudflare+%E5%A6%82%E4%BD%95%E5%AE%9E%E6%96%BD+FIDO2+%E5%92%8C+Zero+Trust+%E7%A1%AC%E4%BB%B6%E5%AF%86%E9%92%A5%E6%9D%A5%E9%98%B2%E6%AD%A2%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E5%91%A2%EF%BC%9F&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)[](https://www.threads.net/intent/post?text=Cloudflare+%E5%A6%82%E4%BD%95%E5%AE%9E%E6%96%BD+FIDO2+%E5%92%8C+Zero+Trust+%E7%A1%AC%E4%BB%B6%E5%AF%86%E9%92%A5%E6%9D%A5%E9%98%B2%E6%AD%A2%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E5%91%A2%EF%BC%9F+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)

## 相关标签

[Cloudflare Zero Trust](https://blog.cloudflare.com/zh-cn/tag/cloudflare-zero-trust/)[Zero Trust](https://blog.cloudflare.com/zh-cn/tag/zero-trust/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
