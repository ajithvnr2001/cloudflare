---
url: https://blog.cloudflare.com/zh-cn/randomness-101-lavarand-in-production/
title: \u968f\u673a\u6027\u7684\u5165\u95e8\u4ecb\u7ecd\uff1a\u6b63\u5728\u751f\u4ea7\u4e2d\u7684LavaRand\uff08\u4e00\u79cd\u786c\u4ef6\u968f\u673a\u6570\u53d1\u751f\u5668\uff09 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:32.951666+00:00
---

# 随机性的入门介绍：正在生产中的LavaRand（一种硬件随机数发生器） | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/randomness-101-lavarand-in-production/

[博客](https://blog.cloudflare.com/zh-cn/)

[Entropy](https://blog.cloudflare.com/zh-cn/tag/entropy/)[LavaRand](https://blog.cloudflare.com/zh-cn/tag/lavarand/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)+1再显示 1 个标签

4 个标签显示 4 个标签

  * 文章标签
  * [安全](https://blog.cloudflare.com/zh-cn/tag/security/)[密码学](https://blog.cloudflare.com/zh-cn/tag/cryptography/)
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



[密码学](https://blog.cloudflare.com/zh-cn/tag/cryptography/)

[Entropy](https://blog.cloudflare.com/zh-cn/tag/entropy/)[LavaRand](https://blog.cloudflare.com/zh-cn/tag/lavarand/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[密码学](https://blog.cloudflare.com/zh-cn/tag/cryptography/)

2017年11月6日

# 随机性的入门介绍：正在生产中的LavaRand（一种硬件随机数发生器）

![Joshua Liebow-Feeser](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498632BNFDMA5ZA3C9XP3R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Joshua Liebow-Feeser](https://blog.cloudflare.com/zh-cn/author/joshlf/)

阅读时间：8 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/randomness-101-lavarand-in-production/)、[Deutsch](https://blog.cloudflare.com/de-de/randomness-101-lavarand-in-production/)和[Español](https://blog.cloudflare.com/es-es/randomness-101-lavarand-in-production/).

![Randomness 101: LavaRand in Production](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CJA9M1R1CBQKTXX1JA8Q.jpg&w=2048&h=1152&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAh46dhYufg4ijhIemh4uliIuehIORfneFgYicgIeegIWjgYamhImlhIidgYCQfHWDeYOZeoOcfISif4amgYelgYWcfn6OenSAdYCWd4GZe4SgfoelgIijf4WafH2MeXV+doKSeIOWfIadgImjgoqhgYeYfYCKeXh+e4ePfIiTf4mbg4yghY2ehIuVgIWJe3x+gIyMgIyQgoyYhY+eiJCciI+Tg4mIfIB/go6Lgo2Pg46XhpCdiZKbiZCShIqIfYJ/)

Cloudflare大堂的熔岩灯 图片来源[@mahtin](https://twitter.com/mahtin/status/888251632550424577)

## 介绍

你们当中的一些人应该知道，我们旧金山办公室的大厅里[有一堵用于密码学的熔岩灯墙](https://www.fastcodesign.com/90137157/the-hardest-working-office-design-in-america-encrypts-your-data-with-lava-lamps)。在这篇文章中，我们将探讨它是如何工作的。本文不涉及技术背景知识。如果你想对有关技术细节做更深入的了解，请参阅 [LavaRand in Production: The Nitty-Gritty Technical Details](https://blog.cloudflare.com/lavarand-in-production-the-nitty-gritty-technical-details)。

## 背景

### 密码学中的随机性

正如我们[过去](https://blog.cloudflare.com/why-randomness-matters/)讨论过的，密码学依赖于随机数的生成能力，这些随机数既不可预测又对任何对手保密。

但“随机”是一个相当难以捉摸的术语；在不同的领域，它的意思略有不同。和所有这些领域一样，它在密码学中的应用非常精准。在某些领域，如果一个过程具有正确的统计特性，那么它就是随机的。例如，圆周率的数字被认为是随机的，因为所有的数字序列都以相同的频率出现(“15”出现的频率与“38”相同，“426”出现的频率与“297”相同，等等)。但对于加密工作来说，这还不够——随机数必须是不可预测的。

要了解不可预测的含义，就有必要知道所有加密都是基于信息的不对称性。如果您正在尝试安全地执行某些加密操作，那么您需要关心的是某个人——如一个对手——会试图破坏您的安全性。唯一能让你与对手区别开来的是你知道对手不知道的东西，加密的工作就是确保信息的这种不对称性足以让你保持安全。

举一个简单的例子。想象一下，你和朋友正准备去看电影，但你不希望你的对手知道你们要去看哪部电影（以免他出现并阻挠你观看！）。就在这周，轮到你选择电影了。一旦你做出了选择，你将需要向你的朋友发送一条信息，告诉他你选择了哪部电影，但是你需要确保即使你的对手拦截了这个信息，她也无法弄清楚信息内容。

你设计了以下方案:由于目前只有两部电影可供观看，你给其中一部贴上A的标签，另一部贴上b的标签。然后，当你的朋友在场时，你会抛硬币。你们遵循下表列出的纲领，因此您要发送取的信息内容将取决于你选择看什么电影和硬币是否出现正面(H)或反面(T)。之后一旦你做出决定看哪部电影,您将使用此表向你的朋友发送一个加密的消息，告诉他你所选择的电影。

**电影**

**硬币**

**信息**

A

H

“西班牙的降雨主要停留在平原上。”

A

Ť

“在赫特福德，赫里福德和汉普郡，飓风几乎没有发生过。”

B

H

“在赫特福德，赫里福德和汉普郡，飓风几乎没有发生过。”

B

Ť

“西班牙的降雨主要停留在平原上。”

如果你决定选B片，硬币正面朝上，你就会发出这样的信息：“在赫特福德、赫里福德和汉普郡，飓风很少发生。”因为你的朋友知道硬币是正面朝上的——抛硬币时他在场——所以他知道你一定是选了B电影。但如果从你的敌人的角度考虑这个问题。她不知道抛硬币的结果，她只知道硬币正面向上的概率是50%反面向上的概率是50%。因此，看到“在赫特福德、赫里福德和汉普郡，飓风几乎从未发生过”的信息对她一点帮助都没有!硬币正面朝上的概率是50%(暗示电影B)反面朝上的概率是50%(暗示电影A)，她知道的并不比以前多!

现在让我们回到不可预测性的概念。假设抛硬币的结果是完全可以预测的——假设你的对手布下了一枚把戏硬币，第一次总是正面朝上，第二次总是反面朝上，第三次总是正面朝上，以此类推。因为她知道第一次抛硬币出现正面的概率是100%，所以不管你发的是哪条信息，她都知道你要去看哪部电影。尽管“硬币戏法”在统计学领域仍然表现出一些“随机性”的基本特性——出现正面和反面的次数一样多——但它是可预测的，这使得它对密码学毫无用处。结论:当我们在密码学中说随机时，我们的意思是“它是不可预测的”。

## 计算中的随机性

不幸的是，对于密码学家来说，如果计算机擅长一件事，它就是可以预测的。它们可以执行相同的代码一百万次，并且只要每次给它们相同的输入，它们总是会得到相同的输出。这对可靠性非常有利，但在加密方面却很棘手 - 毕竟，我们需要的是不可预测性！

该问题的解决方案是加密安全的伪随机数发生器（CSPRNG）。CSPRNG是一种算法，它提供了一个本身不可预测的输入，产生了更大的输出流，这也是不可预测的。该流可以无限期地扩展，在将来的任何时候产生尽可能多的输出。换句话说，如果你要多次翻转一个硬币（一个已知不可预测的过程），然后使用这些硬币翻转的输出作为CSPRNG的输入，对手不能预测投掷硬币结果，就也不能预测CSPRNG的输出——无论CSPRNG消耗了多少输出。

但即使CSPRNG是一个非常强大的工具，它们也仅仅完成了方程式的一半——它们仍需要一个不可预测的输入才能运行。但正如我们所说的，计算机并非不可预测，所以我们不是又回到原点了吗？嗯，这样不太好。事实证明，计算机通常具有可以使用的不可预测性的来源，但它们非常慢。我们可以做的是将收集不可预测输入的缓慢过程与CSPRNG相结合，CSPRNG可以更快地获取输入并产生更大量的输入，同时实现了随机性！

但是即使在速度很慢的情况下，计算机可以从哪里得到这样不可预测的输入呢？答案是在现实世界。虽然计算机为程序员提供了一个很好的简化的方法，但真实的物理计算机仍然存在于真实的物理世界中。这个世界是不可预测的。计算机有从现实世界中获取输入的各种方法——温度传感器、键盘、网络接口等等。所有方法都能够对现实世界进行测量，而所有这些测量都有一定程度的固有不准确性。我们一会儿会解释，不准确性和不可预测性是一样的，而且是可用的!不可预测的随机性的常见来源包括用高精度测量CPU温度(因此精度不准确)、用高精度测量键盘上击键的时间等。要了解如何使用这个方法来产生不可预测的随机性，可以考虑这样一个问题:“我现在所在的房间的温度是多少?”他说:“你大概可以估计到几摄氏度以内，比如说，在70到75华氏度之间。但是你可能不知道精确到小数点后两位的温度是多少——是73。42度还是73。47度?通过高精度测量温度，然后只使用测量值的低阶数字，通过观察你周围的世界，你就可以得到高度不可预测的随机性。电脑也可以这样做。

所以，回顾一下：

  * 密码学中使用的随机性需要是不可预测的。
  * 通过测量环境，计算机可以慢慢地获得少量不可预测的随机性。
  * 计算机可以通过使用CSPRNG大大扩展这种随机性，CSPRNG可以迅速将其转换为大量不可预测的随机性。



## 对冲

密码学家对一件事心存警惕，这是理所当然的。密码系统的安全性通常比最初认为的要低，在什么场景下使用什么算法是安全的，我们对此的理解也在不断地更新。

因此，密码学家通常利用非常多的安全措施来对冲风险，以防他们的其中一个假设被证明是错误的。这有点像密码学家版本的工程实践，设计能够承受比他们想象中要多得多的重量、风或热的建筑物。

随机性的风险对冲通常采取混合的形式。不可预测的随机值有一个很好的特性，如果它们以正确的方式与更不可预测的随机值混合，那么结果至少与任何一个输入一样不可预测。这意味着如果你把一个高度不可预测的随机值和一个稍微可预测的随机值混合，结果将是一个高度不可预测的值。

这种混合很有用，因为你可以混合来自许多源的不可预测的随机值，如果您后来发现其中一个源的不可预测性比您最初认为的要低，那么它仍然是可用的——依托于其他源的帮助。

## LavaRand

Cloudflare在全球数据中心拥有数千台计算机，这些计算机都需要随机性加密。过去这些计算机都是使用我们运行的操作系统Linux的默认机制来获得随机性。

但作为优秀的密码学家，我们总是试着去对冲。我们希望我们的系统可以确保，即使获得随机性的默认机制存在缺陷，我们仍然是安全的。我们就是这样设计出LavaRand的。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![LavaRand in Production: The Nitty-Gritty Technical Details Embedded Image - bVykwc](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WMYM57ZP5KJSF8YP618M.jpg&w=715&h=861&f=webp&fit=cover&position=center)

来自监控相机的视图

LavaRand是一个使用熔岩灯作为生产服务器辅助随机源的系统。旧金山办公室大厅的一盏熔岩灯墙为瞄准墙壁的摄像机提供了不可预测的输入。来自摄像机的视频馈送到CSPRNG，CSPRNG提供的随机值流可以作为我们的生产服务器的额外随机源。由于在熔岩灯内 “熔岩”的流动是非常难以预测的1，­因此通过取它们的镜头“测量”灯是一种获得不可预测的随机性的好方法。计算机将图像存储为非常大的数字，因此我们可以将它们用作CSPRNG的输入，就像任何其他数字一样。

我们不是第一个这样做的人。我们的LavaRand系统的灵感来自Silicon Graphics 首先[提出并建立](https://en.wikipedia.org/wiki/Lavarand)的类似系统，该系统于1996年[获得专利](https://www.google.com/patents/US5732138)（专利现已过期）。

希望我们永远不需要用到它。希望我们的生产服务器使用的随机性的主要来源仍然是安全的，而LavaRand除了为我们的办公室增添一些花样之外几乎没有用处。但如果事实证明我们错了，而且我们生产中的随机源实际上存在缺陷，那么LavaRand将成为我们的对冲工具，让攻击Cloudflare变得更加困难。

* * *

  1. Noll, L.C. and Mende, R.G. and Sisodiya, S.,[_一种用混沌系统数字化的密码散列对接伪随机数生成器的方法_](https://www.google.com/patents/US5732138)



本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frandomness-101-lavarand-in-production%2F&t=%E9%9A%8F%E6%9C%BA%E6%80%A7%E7%9A%84%E5%85%A5%E9%97%A8%E4%BB%8B%E7%BB%8D%EF%BC%9A%E6%AD%A3%E5%9C%A8%E7%94%9F%E4%BA%A7%E4%B8%AD%E7%9A%84LavaRand%EF%BC%88%E4%B8%80%E7%A7%8D%E7%A1%AC%E4%BB%B6%E9%9A%8F%E6%9C%BA%E6%95%B0%E5%8F%91%E7%94%9F%E5%99%A8%EF%BC%89)[](https://x.com/intent/post?text=%E9%9A%8F%E6%9C%BA%E6%80%A7%E7%9A%84%E5%85%A5%E9%97%A8%E4%BB%8B%E7%BB%8D%EF%BC%9A%E6%AD%A3%E5%9C%A8%E7%94%9F%E4%BA%A7%E4%B8%AD%E7%9A%84LavaRand%EF%BC%88%E4%B8%80%E7%A7%8D%E7%A1%AC%E4%BB%B6%E9%9A%8F%E6%9C%BA%E6%95%B0%E5%8F%91%E7%94%9F%E5%99%A8%EF%BC%89&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frandomness-101-lavarand-in-production%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frandomness-101-lavarand-in-production%2F)[](https://bsky.app/intent/compose?text=%E9%9A%8F%E6%9C%BA%E6%80%A7%E7%9A%84%E5%85%A5%E9%97%A8%E4%BB%8B%E7%BB%8D%EF%BC%9A%E6%AD%A3%E5%9C%A8%E7%94%9F%E4%BA%A7%E4%B8%AD%E7%9A%84LavaRand%EF%BC%88%E4%B8%80%E7%A7%8D%E7%A1%AC%E4%BB%B6%E9%9A%8F%E6%9C%BA%E6%95%B0%E5%8F%91%E7%94%9F%E5%99%A8%EF%BC%89+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frandomness-101-lavarand-in-production%2F)[](https://mastodonshare.com/?text=%E9%9A%8F%E6%9C%BA%E6%80%A7%E7%9A%84%E5%85%A5%E9%97%A8%E4%BB%8B%E7%BB%8D%EF%BC%9A%E6%AD%A3%E5%9C%A8%E7%94%9F%E4%BA%A7%E4%B8%AD%E7%9A%84LavaRand%EF%BC%88%E4%B8%80%E7%A7%8D%E7%A1%AC%E4%BB%B6%E9%9A%8F%E6%9C%BA%E6%95%B0%E5%8F%91%E7%94%9F%E5%99%A8%EF%BC%89&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frandomness-101-lavarand-in-production%2F)[](https://www.threads.net/intent/post?text=%E9%9A%8F%E6%9C%BA%E6%80%A7%E7%9A%84%E5%85%A5%E9%97%A8%E4%BB%8B%E7%BB%8D%EF%BC%9A%E6%AD%A3%E5%9C%A8%E7%94%9F%E4%BA%A7%E4%B8%AD%E7%9A%84LavaRand%EF%BC%88%E4%B8%80%E7%A7%8D%E7%A1%AC%E4%BB%B6%E9%9A%8F%E6%9C%BA%E6%95%B0%E5%8F%91%E7%94%9F%E5%99%A8%EF%BC%89+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frandomness-101-lavarand-in-production%2F)

## 相关标签

[Entropy](https://blog.cloudflare.com/zh-cn/tag/entropy/)[LavaRand](https://blog.cloudflare.com/zh-cn/tag/lavarand/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[密码学](https://blog.cloudflare.com/zh-cn/tag/cryptography/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
