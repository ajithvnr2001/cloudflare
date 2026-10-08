---
url: https://blog.cloudflare.com/zh-cn/cloudflare-architecture-and-how-bpf-eats-the-world/
title: Cloudflare\u67b6\u6784\u4ee5\u53caBPF\u5982\u4f55\u5360\u636e\u4e16\u754c | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:21.236615+00:00
---

# Cloudflare架构以及BPF如何占据世界 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/cloudflare-architecture-and-how-bpf-eats-the-world/

[博客](https://blog.cloudflare.com/zh-cn/)

[Anycast](https://blog.cloudflare.com/zh-cn/tag/anycast/)[eBPF](https://blog.cloudflare.com/zh-cn/tag/ebpf/)[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)+3再显示 3 个标签

6 个标签显示 6 个标签

  * 文章标签
  * [Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)
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



[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

[Anycast](https://blog.cloudflare.com/zh-cn/tag/anycast/)[eBPF](https://blog.cloudflare.com/zh-cn/tag/ebpf/)[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

2019年5月18日

# Cloudflare架构以及BPF如何占据世界

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/zh-cn/author/marek-majkowski/)

阅读时间：9 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/cloudflare-architecture-and-how-bpf-eats-the-world/)、[Deutsch](https://blog.cloudflare.com/de-de/cloudflare-architecture-and-how-bpf-eats-the-world/)、[Español](https://blog.cloudflare.com/es-es/cloudflare-architecture-and-how-bpf-eats-the-world/)和[Français](https://blog.cloudflare.com/fr-fr/cloudflare-architecture-and-how-bpf-eats-the-world/).

![Cloudflare architecture and how BPF eats the world](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4625EY4M7N1KRERTHTYMFT.jpg&w=950&h=512&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////8/Lr2cu3zrig3tHI8fDz9Pb96Ofs////8u/n1MSqyLCM282+8u/v9vb66Obn////8u7l0cCfxKp52sy29PDt+Pj56ebk////9/Pq1cWmx7GA3tG6+PXw/Pz87erm//////324NW908Oh5t7L/f34////8vLu////////7una4trF8O7h////////9/v6////////+fjw7+vg+frz/////////P///////////v748/Hp/P75/////////f//)

最近，在布拉格Linux网络会议[Netdev 0x13](https://www.netdevconf.org/0x13/schedule.html)上，我做了[一个简短的演讲，题目是“Cloudflare上的Linux”](https://netdevconf.org/0x13/session.html?panel-industry-perspectives)。[演讲](https://speakerdeck.com/majek04/linux-at-cloudflare)最后主要是关于BPF（柏克莱封包过滤器）的。似乎，不管问题是什么——BPF都是答案。

下面是这次演讲的稍作调整的笔录。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - 8PjjfZ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S032Z8BX2FVSVHN1SG1E.jpg&w=715&h=458&f=webp&fit=cover&position=center)

在Cloudflare，我们在服务器上运行Linux。我们运营两类数据中心：大型“核心”数据中心，用以处理日志，分析攻击，计算分析；以及“边缘”服务器机群，从全球180个（截至19年10月为190多个）位置交付客户内容。

在这次演讲中，我们将重点讨论“边缘”服务器。在这里，我们使用最新的Linux特性，优化性能，并深切关注DoS（拒绝服务攻击）的弹性。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - yMZ8oK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW457DSJSJ59D0H3MJMH3XD1.png&w=715&h=458&f=webp&fit=cover&position=center)

由于我们的网络配置，我们的边缘服务很特别——我们广泛使用anycast（任播）路由。任播意味着所有数据中心都公布相同的IP地址集。

这种设计有很大的优势。首先，它保证了最终用户的最佳速度。无论身处何处，您都可以到达最近的数据中心。并且，任播帮助我们分散DoS流量。在遭受攻击过程中，每个位置接收的流量仅占总流量的一小部分，因此我们可以更容易地提取和过滤掉不需要的流量。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - UmJ9T6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW473V4QZBVPZJYMTAATAPT0.jpg&w=715&h=291&f=webp&fit=cover&position=center)

任播使我们能够在所有边缘数据中心保持统一的网络设置。我们在数据中心内部应用了相同的设计——我们的软件堆栈在边缘服务器上是统一的。每一个服务器上都运行着所有的软件。

原则上，每台机器都能处理所有的任务——我们运行着许多不同的、要求很高的任务。我们有完整的HTTP栈、神奇的Cloudflare Workers、两组DNS服务器——权威DNS和解析器，以及许多其他的面向公众的应用程序，如Spectrum和Warp。

尽管每台服务器都运行着所有的软件，但请求通常也会在堆栈的旅程中跨越许多机器。例如，在处理HTTP请求的5个阶段中，每个阶段都有不同的机器进行处理。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - Nx55Rn](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW451J7QR62Z3DR15BGJ56NW.png&w=715&h=371&f=webp&fit=cover&position=center)

让我向您介绍入站数据包处理的早期阶段：

（1）首先，数据包到达我们的路由器。路由器执行ECMP（等价多路径路由），并将数据包转发到我们的Linux服务器上。我们使用ECMP将每个目标IP分布到至少16台机器上。这是一种基本的负载均衡技术。

（2）在服务器上，我们使用XDP eBPF接收数据包。在XDP中，我们执行两个阶段。首先，我们运行大容量的DoS缓解措施，丢弃属于非常大的第3层攻击的数据包。

（3）然后，同样在XDP中，我们执行第4层负载均衡。所有的非攻击包都在计算机之间重定向。这是用来解决ECMP问题的，为我们提供了精细的负载均衡，并允许我们自然而正常地关闭服务器的服务。

（4）重定向之后，数据包到达指定的机器。此时，它们被普通的Linux网络堆栈接收，通过常规的iptables防火墙，并被分派到合适的网络套接字。

（5）最后，数据包被应用程序接收。例如，HTTP连接由“协议”服务器处理，该服务器负责执行TLS加密和处理HTTP、HTTP/2和QUIC协议。

在请求处理的早期阶段，我们使用了最酷的Linux新功能。我们可以将有用的现代功能分为三类：

  * DoS处理
  * 负载均衡
  * 套接字分配



* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - LhKOKN](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45XXKSKV58CVZ3KRAQ9HS5.png&w=715&h=255&f=webp&fit=cover&position=center)

让我们更详细地讨论DoS处理。如前所述，ECMP路由之后的第一步是Linux的XDP堆栈，其中，我们运行DoS缓解措施。

从历史上看，我们对容量攻击的缓解是用经典的BPF和iptables样式的语法表示的。最近，我们对它们进行了调整，从而在XDP eBPF环境中执行，事实证明这非常困难。一起来看看我们冒险的经历吧：

  * [L4Drop: XDP DDoS缓解](https://blog.cloudflare.com/l4drop-xdp-ebpf-based-ddos-mitigations/)
  * [xdpcap: XDP数据包捕获](https://blog.cloudflare.com/xdpcap/)
  * Arthur Fabre的演讲：[基于XDP的DoS缓解](https://netdevconf.org/0x13/session.html?talk-XDP-based-DDoS-mitigation)
  * [实践中的XDP：将XDP集成到我们的DDoS缓解通道中](https://netdevconf.org/2.1/papers/Gilberto_Bertin_XDP_in_practice.pdf) (PDF)



在这个项目中，我们遇到了许多eBPF/XDP限制。其中之一是缺乏并发原语。实现无竞争令牌桶之类的东西非常困难。后来，我们发现[Facebook工程师Julia Kartseva](http://vger.kernel.org/lpc-bpf2018.html#session-9)遇到了同样的问题。在2月份，这个问题已经通过引入bpf_spin_lock helper得到了解决。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - WuSEbO](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW457FM8E07AEFEMGNVWSCNK.png&w=715&h=251&f=webp&fit=cover&position=center)

虽然我们现代的容量DoS防御是在XDP层完成的，但我们仍然依赖iptables来减轻应用层（第7层）的影响。在这里，更高级别防火墙的特性起着很大的作用：connlimit、hashlimit和ipset。我们还使用xt_bpf iptables模块在iptables中运行cBPF，从而匹配数据包有效负载。我们以前讨论过这个问题：

  * [抵御不可抗力的经验教训](https://speakerdeck.com/majek04/lessons-from-defending-the-indefensible) (PPT)
  * [介绍BPF工具](https://blog.cloudflare.com/introducing-the-bpf-tools/)



* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - mLDecw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48SS2ZE7FC30R5AKRSDFV9.png&w=715&h=370&f=webp&fit=cover&position=center)

在XDP和iptables之后，我们有了最后一个内核端DoS防御层。

考虑UDP缓解失败的情况。在这种情况下，可能会有大量的数据包到达应用程序UDP套接字。这可能会使套接字溢出，导致数据包丢失。这是有问题的——好的数据包和坏的数据包都会被随意丢弃。对于DNS这样的应用程序来说，这一后果是灾难性的。在过去，为了减少危害，我们为每个IP地址运行了一个UDP套接字。无法缓解的洪水攻击是很糟糕的，但至少它没有影响到其他服务器IP地址的流量。

如今，这种架构已不再适用。我们正在运行30,000多个DNS IP，并且运行同样数量的UDP套接字是不可行的。我们现代的解决方案是运行一个带有复杂eBPF套接字过滤器的UDP套接字——使用SO_ATTACH_BPFsocket选项。我们在以前的博客文章中讨论过在网络套接字上运行eBPF：

  * eBPF，套接字，跳段距离，手动编写eBPF程序集
  * [SOCKMAP——未来的TCP粘合](https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/)



上面提到的eBPF速率限制了数据包。它将状态（数据包计数）保存在eBPF映射中。我们可以确保一个被“淹没”的IP不会影响其他流量。这种做法效果很好，尽管在进行此项目期间，我们在eBPF验证程序中发现了一个令人担忧的错误：

  * [eBPF无法计数](https://blog.cloudflare.com/ebpf-cant-count/)？！



我猜在UDP套接字上运行eBPF并不如往常般简单。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - qUqTiR](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48N4A8AJ8A882QX9ZJW00H.png&w=715&h=224&f=webp&fit=cover&position=center)

除了DoS，在XDP中我们还运行了第4层负载均衡器层。这是一个新项目，我们还没作过多的谈论。无需深入探讨：在某些情况下，我们需要从XDP执行套接字查找。

这个问题相对简单——我们的代码需要查找从数据包中提取的5元组的“套接字”内核结构。这通常很简单——可以借助bpf_sk_lookup helper。不出所料的是，这里出现了一些复杂情况。其中有个问题是，当启用SYN cookie时，无法验证接收到的ACK包是否是三方握手的有效部分。我的同事Lorenz Bauer正在为这个特殊情况提供额外支持。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - Z5AQj3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AZSQVK6GMC8GCG3QWTPE.png&w=715&h=232&f=webp&fit=cover&position=center)

经过DoS和负载均衡层之后，数据包将被传递到通常的Linux TCP / UDP堆栈上。在这里，我们进行套接字分配——例如，将进入端口53的数据包传递到属于我们的DNS服务器的套接字上。

我们尽力使用原始Linux功能，但是当您在服务器上使用数千个IP地址时，事情会变得复杂。

使用[“AnyIP”技巧](https://blog.cloudflare.com/how-we-built-spectrum)使Linux能够正确地路由数据包是相对比较容易的。但确保数据包被分发到正确的应用程序则是另一回事。不幸的是，标准的Linux套接字分派逻辑不够灵活，不能满足我们的需要。对于TCP/80这样的流行端口，我们希望在多个应用程序之间共享端口，每个应用程序在不同的IP范围内处理它。Linux不支持此功能。您可以在特定的IP或所有（使用0.0.0.0）的IP地址上调用bind()。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - UyelYs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW454X48JSVW3F7W532P8XA0.png&w=715&h=260&f=webp&fit=cover&position=center)

为了解决这个问题，我们开发了一个自定义内核补丁，其中添加了[一个`SO_BINDTOPREFIX`socket选项](http://patchwork.ozlabs.org/patch/602916/)。顾名思义——它允许我们在选定的IP前缀上调用bind()。这解决了多个应用程序共享流行端口（如53或80）的问题。

然后我们遇到另一个问题。对于我们的Spectrum产品，我们需要监听所有总共65535个端口。运行这么多监听套接字不是一个好主意（请参阅[我们过去的战争故事博客](https://blog.cloudflare.com/revenge-listening-sockets/)），因此我们不得不寻找另一种方法。经过一些实验，我们学会了使用一个鲜有人知的iptables模块——TPROXY——来达到这个目的。点击这里进行阅读：

  * [滥用Linux防火墙：允许我们构建Spectrum的黑客行为](https://blog.cloudflare.com/how-we-built-spectrum/)



这个设置起到了作用，但我们不喜欢额外的防火墙规则。我们正在努力正确地解决这个问题——实际上我们扩展了套接字调度逻辑。您猜对了——我们希望利用eBPF扩展套接字分派逻辑。敬请期待我们的一些补丁。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - ii0Zd0](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KF3RTD2RE4TT91W3GYVE.png&w=715&h=370&f=webp&fit=cover&position=center)

然后还有一种使用eBPF改进应用程序的方法。最近，我们对使用SOCKMAP进行TCP粘合很感兴趣：

  * [SOCKMAP——未来的TCP粘合](https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/)



这项技术在改善我们许多软件堆栈的尾部延迟方面具有巨大潜力。当前的SOCKMAP实施尚未准备好完全发挥其作用，但它的潜力是巨大的。

同样，新的[TCP-BPF又名BPF_SOCK_OPS](https://netdevconf.org/2.2/papers/brakmo-tcpbpf-talk.pdf)挂载为检查TCP流的性能参数提供了一种很好的方法。此功能对我们的性能表现团队非常有用。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - uXroGK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FV0YJYWWZR3691CB3DMV.jpg&w=715&h=458&f=webp&fit=cover&position=center)

一些Linux特性没有很好地发展成熟，我们需要解决它们。例如，我们正在突破网络指标的限制。不要误解我的意思——网络指标非常棒，但遗憾的是它们不够精细。像TcpExtListenDrops和TcpExtListenOverflows之类的事物被称为全局计数器，而我们需要在每个应用程序的基础上了解它。

我们的解决方案是使用eBPF探针直接从内核中抽取数字。我的同事Ivan Babrou编写了一个名为“ebpf_exporter”的Prometheus指标导出器，以便进行此操作。了解更多请继续阅读：

  * [ebpf_exporter简介](https://blog.cloudflare.com/introducing-ebpf_exporter/)
  * <https://github.com/cloudflare/ebpf_exporter>



使用“ebpf_exporter”，我们可以生成所有形式的详细指标。它非常强大，并在许多情况下极大地帮助了我们。

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - iWWQYL](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TQR7YWXSSVZCMA3HPKBA.png&w=715&h=280&f=webp&fit=cover&position=center)

在本次演讲中，我们讨论了在边缘服务器上运行的6层BPF：

  * 正在XDP eBPF上运行的批量DoS缓解措施
  * 用于应用层攻击的Iptables xt_bpf cBPF
  * 用于UDP套接字速率限制的SO_ATTACH_BPF
  * 在XDP上运行的负载均衡器
  * 用于运行应用帮助进程的eBPF，例如用于TCP套接字粘合的SOCKMAP和用于TCP测量的TCP-BPF
  * 用于获取精细指标的“ebpf_exporter”



我们才刚刚开始!很快，我们将在基于eBPF的套接字调度、在[Linux TC（](https://linux.die.net/man/8/tc)流量控制）层上运行的eBPF以及与控制组eBPF挂载的更多集成上完成更多的工作。然后，我们的SRE团队将维护不断增长的[BCC脚本](https://github.com/iovisor/bcc)列表，这些脚本对于调试非常有用。

感觉就像Linux停止了开发新的API一样，所有的新特性都要通过eBPF挂载和帮助进程来实现。这很好，并且具有强大的优势。升级eBPF程序比重新编译内核模块更容易、更安全。如果没有eBPF，那么像TCP-BPF之类展现大量性能跟踪数据的东西可能是无法实现的。

有的人说：“软件正在占据世界”，但我想说：“BPF正在占据软件”。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F&t=Cloudflare%E6%9E%B6%E6%9E%84%E4%BB%A5%E5%8F%8ABPF%E5%A6%82%E4%BD%95%E5%8D%A0%E6%8D%AE%E4%B8%96%E7%95%8C)[](https://x.com/intent/post?text=Cloudflare%E6%9E%B6%E6%9E%84%E4%BB%A5%E5%8F%8ABPF%E5%A6%82%E4%BD%95%E5%8D%A0%E6%8D%AE%E4%B8%96%E7%95%8C&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://bsky.app/intent/compose?text=Cloudflare%E6%9E%B6%E6%9E%84%E4%BB%A5%E5%8F%8ABPF%E5%A6%82%E4%BD%95%E5%8D%A0%E6%8D%AE%E4%B8%96%E7%95%8C+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://mastodonshare.com/?text=Cloudflare%E6%9E%B6%E6%9E%84%E4%BB%A5%E5%8F%8ABPF%E5%A6%82%E4%BD%95%E5%8D%A0%E6%8D%AE%E4%B8%96%E7%95%8C&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://www.threads.net/intent/post?text=Cloudflare%E6%9E%B6%E6%9E%84%E4%BB%A5%E5%8F%8ABPF%E5%A6%82%E4%BD%95%E5%8D%A0%E6%8D%AE%E4%B8%96%E7%95%8C+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)

## 相关标签

[Anycast](https://blog.cloudflare.com/zh-cn/tag/anycast/)[eBPF](https://blog.cloudflare.com/zh-cn/tag/ebpf/)[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[TCP](https://blog.cloudflare.com/zh-cn/tag/tcp/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
