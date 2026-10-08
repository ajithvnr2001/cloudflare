---
url: https://blog.cloudflare.com/zh-cn/programmable-packet-filtering-with-magic-firewall/
title: \u6211\u4eec\u5982\u4f55\u4f7f\u7528 eBPF \u5728 Magic Firewall \u6784\u5efa\u53ef\u7f16\u7a0b\u6570\u636e\u5305\u8fc7\u6ee4 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:15.905989+00:00
---

# 我们如何使用 eBPF 在 Magic Firewall 构建可编程数据包过滤 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/programmable-packet-filtering-with-magic-firewall/

[博客](https://blog.cloudflare.com/zh-cn/)

[CIO Week](https://blog.cloudflare.com/zh-cn/tag/cio-week/)[eBPF](https://blog.cloudflare.com/zh-cn/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/zh-cn/tag/magic-firewall/)+3再显示 3 个标签

6 个标签显示 6 个标签

  * 文章标签
  * [CIO Week](https://blog.cloudflare.com/zh-cn/tag/cio-week/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)
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



[Magic Transit](https://blog.cloudflare.com/zh-cn/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/zh-cn/tag/voip/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)

[CIO Week](https://blog.cloudflare.com/zh-cn/tag/cio-week/)[eBPF](https://blog.cloudflare.com/zh-cn/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/zh-cn/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/zh-cn/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/zh-cn/tag/voip/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)

2021年12月6日

# 我们如何使用 eBPF 在 Magic Firewall 构建可编程数据包过滤

![Chris J Arges](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4865BZM73VVEYNTQ0VZBR4.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Chris J Arges](https://blog.cloudflare.com/zh-cn/author/arges/)

阅读时间：6 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/programmable-packet-filtering-with-magic-firewall/)、[日本語](https://blog.cloudflare.com/ja-jp/programmable-packet-filtering-with-magic-firewall/)、[Bahasa Indonesia](https://blog.cloudflare.com/id-id/programmable-packet-filtering-with-magic-firewall/)和[ภาษาไทย](https://blog.cloudflare.com/th-th/programmable-packet-filtering-with-magic-firewall/).

![How We Used eBPF to Build Programmable Packet Filtering in Magic Firewall](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44K5JZN9SGZA4NJKEMXA99.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v3/9PLz7+vp8u3p9vLu8/Dv6+rs////////9fPz7+zo8e3n9fHt8/Hv7Ovt////////+Pf18e/p8u/n9fPs9PPw7u7w////////+/z59PPt9fPr+Pfw9/f08vP1////////////+vr0+vrz/f34/P379/j6///////////////8///9////////+/7/////////////////////////////////////////////////////////////////)

Cloudflare 日复一日地积极保护服务免受复杂的攻击。对于 Magic Transit 的用户，DDoS 保护能够检测并减少攻击，而 [Magic Firewall](https://www.cloudflare.com/zh-cn/magic-firewall/) 则允许自定义包级规则，使客户能够弃用硬件防火墙设备，并阻止 Cloudflare 网络上的恶意流量。攻击的类型和复杂程度在不断演变，例如最近出现的[针对](https://blog.cloudflare.com/update-on-voip-attacks/) [Session Initiation Protocol](https://en.wikipedia.org/wiki/Session_Initiation_Protocol) (SIP) 等协议的 VoIP 服务的 DDoS 和反射[攻击](https://blog.cloudflare.com/zh-cn/attacks-on-voip-providers-zh-cn/) 。要对抗这些攻击，就需要突破超越传统防火墙能力的数据包过滤的极限。为了做到这一点，我们采用了最先进的技术，并将它们以新的方式结合起来，将 Magic Firewall 变成了一个极速、完全可编程的防火墙，其甚至可以抵抗最复杂的攻击。

### **Magical Walls of Fire**

[Magic Firewall](https://blog.cloudflare.com/zh-cn/introducing-magic-firewall-zh-cn/)是一个构建在 Linux nftables 上的分布式无状态数据包防火墙。它在全世界每一个 Cloudflare 数据中心的每一台服务器上运行。为了提供隔离和灵活性，每个客户的都需要在自己的 Linux 网络命名空间中配置 nftables 规则。

这张图显示了内置 Magic Firewall 时，使用 [Magic Transit](https://blog.cloudflare.com/zh-cn/magic-transit-network-functions-zh-cn/) 的示例数据包的生命周期。首先，数据包进入服务器并应用 DDoS 保护，可以尽早地减少攻击。接下来，数据包被路由到客户特定网络命名空间，并将 nftables 规则应用于数据包。然后，数据包将通过 GRE 通道返回至源端。Magic Firewall 用户可以使用灵活的 [Wirefilter syntax](https://github.com/cloudflare/wirefilter)，利用[单个 API](https://developers.cloudflare.com/magic-firewall) 构造防火墙语句。此外，可以使用便捷的 UI 拖放元素，在 Cloudflare 仪表板中配置规则。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![This diagram shows how packets are processed by Magic Firewall on a Cloudflare server.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48R9WMZ6CW711ZX84DH9QX.png&w=715&h=372&f=webp&fit=cover&position=center)

Magic Firewall 为各种数据包参数的匹配提供了非常强大的句法，但这也仅限于 nftables 提供的匹配。虽然这对于许多用例来说已经足够了，但这并未提供足够的灵活性来实现我们想要的高级帧解析和内容匹配。我们需要更强的能力。

### **您好，eBPF，一起来认识 Nftables！**

当您希望为 Linux 网络需求添加更多功能时，扩展 Berkeley Packet Filter ([eBPF](https://ebpf.io/))是自然而然的选择。通过 eBPF，您可以插入_在内核中_执行的数据包处理程序，为您提供熟悉的编程范例的灵活性和内核内执行的速度。Cloudflare [钟爱 eBPF](https://blog.cloudflare.com/tag/ebpf/)，这项技术在实现我们的许多产品中起到了革命性的作用。当然，我们想要找到一种方法来使用 eBPF 以扩展我们在 Magic Firewall 中对 nftables 的使用。这意味着能够匹配，在表和链中使用 eBPF 程序作为规则。通过保持现有的基础结构和代码，并进一步扩展，我们也可以鱼与熊掌兼得。

如果 nftables 能够自然运用 eBPF，故事就会简单得多；不过，我们只能继续我们的探索。为了开始我们的搜索，我们知道在 iptables 中已集成了 eBPF。例如，我们可以使用 iptables 和一个固定的 eBPF 程序来删除数据包，命令如下：

这有助于我们走上正确的道路。Iptables 使用 [xt_bpf](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/netfilter/xt_bpf.c#n60) 扩展名来匹配 eBPF 程序。这一扩展使用了 BPF_PROG_TYPE_SOCKET_FILTER eBPF 程序类型，允许我们套接字缓冲区加载数据包信息，并根据我们的代码返回一个值。
    
    
    iptables -A INPUT -m bpf --object-pinned /sys/fs/bpf/match -j DROP

既然我们知道 iptables 可以使用 eBPF，为什么不直接使用它呢？Magic Firewall 目前使用了 nftables，由于它在句法和可编程接口方面的灵活性，对于我们的用例来说，nftables 是一个很好的选择。因此，我们需要找到一种方法，将 xt_bpf 扩展名应用于 nftables。

这张[图](https://developers.redhat.com/blog/2020/08/18/iptables-the-two-variants-and-their-relationship-with-nftables#using_iptables_nft)有助于解释 iptables、nftables 和内核之间的关系。nftables API 可以被 iptables 和 nft 用户空间程序使用，并且可以配置 xtables 匹配（包括 xt_bpf）和普通的 nftables 匹配。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-849 Embedded Image - BzET9q](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K5HWGDGVFGANF0A6D7MF.png&w=715&h=536&f=webp&fit=cover&position=center)

这意味着通过正确的 API 调用（netlink/netfilter 消息），我们可以在 nftables 规则中嵌入 xt_bpf 匹配。为了做到这一点，我们需要了解需要发送哪些 netfilter 消息。通过使用诸如 strace、Wireshark 等工具，特别是使用[源](https://github.com/torvalds/linux/blob/master/net/netfilter/xt_bpf.c)，我们能够构造一条消息，可以在特定的表和链中添加 eBPF 规则。

用于添加 eBPF 匹配的 netlink/netfilter 消息的结构应该类似于上面的示例。当然，这条消息需要被正确地嵌入，并包含一个有条件的步骤，例如匹配时的决定。下一步是解码“ebpf_bytes”的格式，如下例所示。
    
    
    NFTA_RULE_TABLE table
    NFTA_RULE_CHAIN chain
    NFTA_RULE_EXPRESSIONS | NFTA_MATCH_NAME
    	NFTA_LIST_ELEM | NLA_F_NESTED
    	NFTA_EXPR_NAME "match"
    		NLA_F_NESTED | NFTA_EXPR_DATA
    		NFTA_MATCH_NAME "bpf"
    		NFTA_MATCH_REV 1
    		NFTA_MATCH_INFO ebpf_bytes	

字节格式可以在 [struct xt_bpf_info_v1](https://git.netfilter.org/iptables/tree/include/linux/netfilter/xt_bpf.h#n27) 的内核数据头部定义中找到。上面的代码示例显示了该结构的相关部分。
    
    
     struct xt_bpf_info_v1 {
    	__u16 mode;
    	__u16 bpf_program_num_elem;
    	__s32 fd;
    	union {
    		struct sock_filter bpf_program[XT_BPF_MAX_NUM_INSTR];
    		char path[XT_BPF_PATH_MAX];
    	};
    };

xt_bpf 模块既支持原始字节码，也支持指向固定 eBPF 程序的路径。后一种模式是我们将 eBPF 程序与 nftables 结合所使用的技术。

有了这些信息，我们能够编写代码来创建 netlink 消息，并正确地为任何相关的数据字段排序。这种方法只是第一步，我们也在考虑将其整合到合适的工具中，以替代发送自定义的 netfilter 消息。

### **只需添加 eBPF**

现在，我们需要构建一个 eBPF 程序，并将其加载到现有的 nftables 表和链中。开始使用 eBPF 可能会有点令人生畏。我们需要使用哪些类型的程序？我们该如何编译并加载我们的 eBPF 程序？我们需要通过一些探索和研究来开始这个过程。

首先，我们构建了一个示例程序进行尝试。

上述的摘录是 eBPF 程序的一个示例，它只接受在有效负荷末尾有一个魔术字符串的数据包。这需要检查数据包的总长度，以找到从哪里开始搜索。为了清晰起见，本示例中省略了错误检查和数据头部信息。
    
    
    SEC("socket")
    int filter(struct __sk_buff *skb) {
      /* get header */
      struct iphdr iph;
      if (bpf_skb_load_bytes(skb, 0, &iph, sizeof(iph))) {
        return BPF_DROP;
      }
    
      /* read last 5 bytes in payload of udp */
      __u16 pkt_len = bswap_16(iph.tot_len);
      char data[5];
      if (bpf_skb_load_bytes(skb, pkt_len - sizeof(data), &data, sizeof(data))) {
        return BPF_DROP;
      }
    
      /* only packets with the magic word at the end of the payload are allowed */
      const char SECRET_TOKEN[5] = "xyzzy";
      for (int i = 0; i < sizeof(SECRET_TOKEN); i++) {
        if (SECRET_TOKEN[i] != data[i]) {
          return BPF_DROP;
        }
      }
    
      return BPF_OK;
    }

当我们有了程序后，下一步就是将它集成到我们的工具中。我们尝试了一些诸如 BCC、libbpf 等技术来加载程序，我们甚至创建了一个自定义加载器。最终，我们采用了[cilium eBPF 库](https://github.com/cilium/ebpf/)，因为我们使用 Golang 作为我们的控制平面程序，而该库使在生成、嵌入和加载 eBPF 程序中非常编辑。

一旦程序被编译并固定，我们就可以使用 netlink 命令将在 nftables 中添加匹配。列出规则集显示匹配的存在。这简直太棒了！我们现在可以部署自定义的 C 程序，以便在 Magic Firewall 规则集内提供高级匹配！
    
    
    # nft list ruleset
    table ip mfw {
    	chain input {
    		#match bpf pinned /sys/fs/bpf/mfw/match drop
    	}
    }

### **更多 Magic**

在我们的工具包中增加 eBPF 后，Magic Firewall 成为了一种更加灵活和强大的方法，能够保护您的网络免受不良行为的伤害。现在，我们能够更深入地研究数据包，并实现比 nftables 单独能够提供的更复杂的匹配逻辑。由于我们的防火墙在所有 Cloudflare 服务器上都以软件的形式运行，所以我们可以快速迭代和更新功能。

该项目的一个成果是 SIP 保护，目前正处于测试阶段。而这仅仅是个开始。我们目前正在探索使用 eBPF 进行协议验证、高级字段匹配、查看有效负荷，以及支持更大的 IP 列表集。

我们也欢迎您的帮助！如果您有其他用例和想法，请与您的客户团队交谈。如果您觉得这项技术很有趣，快来[加入我们的团队吧](https://www.cloudflare.com/zh-cn/careers/?__cf_chl_jschl_tk__=uSO6loXtm4qYeGBAoMYMhWW9vhOHdAiaN_NK9f3eZMY-1640592157-0-gaNycGzND9E)！

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fprogrammable-packet-filtering-with-magic-firewall%2F&t=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%20eBPF%20%E5%9C%A8%20Magic%20Firewall%20%E6%9E%84%E5%BB%BA%E5%8F%AF%E7%BC%96%E7%A8%8B%E6%95%B0%E6%8D%AE%E5%8C%85%E8%BF%87%E6%BB%A4)[](https://x.com/intent/post?text=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8+eBPF+%E5%9C%A8+Magic+Firewall+%E6%9E%84%E5%BB%BA%E5%8F%AF%E7%BC%96%E7%A8%8B%E6%95%B0%E6%8D%AE%E5%8C%85%E8%BF%87%E6%BB%A4&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://bsky.app/intent/compose?text=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8+eBPF+%E5%9C%A8+Magic+Firewall+%E6%9E%84%E5%BB%BA%E5%8F%AF%E7%BC%96%E7%A8%8B%E6%95%B0%E6%8D%AE%E5%8C%85%E8%BF%87%E6%BB%A4+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://mastodonshare.com/?text=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8+eBPF+%E5%9C%A8+Magic+Firewall+%E6%9E%84%E5%BB%BA%E5%8F%AF%E7%BC%96%E7%A8%8B%E6%95%B0%E6%8D%AE%E5%8C%85%E8%BF%87%E6%BB%A4&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://www.threads.net/intent/post?text=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8+eBPF+%E5%9C%A8+Magic+Firewall+%E6%9E%84%E5%BB%BA%E5%8F%AF%E7%BC%96%E7%A8%8B%E6%95%B0%E6%8D%AE%E5%8C%85%E8%BF%87%E6%BB%A4+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fprogrammable-packet-filtering-with-magic-firewall%2F)

## 相关标签

[CIO Week](https://blog.cloudflare.com/zh-cn/tag/cio-week/)[eBPF](https://blog.cloudflare.com/zh-cn/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/zh-cn/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/zh-cn/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/zh-cn/tag/voip/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
