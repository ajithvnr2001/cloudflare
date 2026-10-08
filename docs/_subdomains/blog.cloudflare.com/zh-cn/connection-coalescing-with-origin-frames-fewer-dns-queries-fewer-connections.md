---
url: https://blog.cloudflare.com/zh-cn/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/
title: \u4f7f\u7528 ORIGIN Frames \u5b9e\u73b0\u8fde\u63a5\u5408\u5e76\uff1a\u51cf\u5c11 DNS \u67e5\u8be2\uff0c\u51cf\u5c11\u8fde\u63a5\u6570 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:03.021427+00:00
---

# 使用 ORIGIN Frames 实现连接合并：减少 DNS 查询，减少连接数 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/

[博客](https://blog.cloudflare.com/zh-cn/)

[DNS](https://blog.cloudflare.com/zh-cn/tag/dns/)[HTTP2](https://blog.cloudflare.com/zh-cn/tag/http2/)[Internship Experience](https://blog.cloudflare.com/zh-cn/tag/internship-experience/)+3再显示 3 个标签

6 个标签显示 6 个标签

  * 文章标签
  * [DNS](https://blog.cloudflare.com/zh-cn/tag/dns/)[TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)[研究](https://blog.cloudflare.com/zh-cn/tag/research/)[速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)
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



[TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)[研究](https://blog.cloudflare.com/zh-cn/tag/research/)[速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)

[DNS](https://blog.cloudflare.com/zh-cn/tag/dns/)[HTTP2](https://blog.cloudflare.com/zh-cn/tag/http2/)[Internship Experience](https://blog.cloudflare.com/zh-cn/tag/internship-experience/)[TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)[研究](https://blog.cloudflare.com/zh-cn/tag/research/)[速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)

2023年9月4日

# 使用 ORIGIN Frames 实现连接合并：减少 DNS 查询，减少连接数

![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Suleman Ahmad](https://blog.cloudflare.com/zh-cn/author/suleman/)、[Jonathan Hoyland](https://blog.cloudflare.com/zh-cn/author/jonathan-hoyland/)和[Sudheesh Singanamalla](https://blog.cloudflare.com/zh-cn/author/sudheesh/)

阅读时间：13 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[Deutsch](https://blog.cloudflare.com/de-de/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[Français](https://blog.cloudflare.com/fr-fr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[日本語](https://blog.cloudflare.com/ja-jp/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[한국어](https://blog.cloudflare.com/ko-kr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)和[繁體中文](https://blog.cloudflare.com/zh-tw/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/).

![Connection coalescing with ORIGIN Frames: fewer DNS queries, fewer connections](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HDJ2ZAZ6FJXTRPX0N4CN.png&w=1600&h=889&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vfi+fHe7eTV593R6+LU8OrZ7unW5eHN//vn+/Xi8Oja6uHW7eXZ8uzc8OvZ6OTS///s//ro9O3h7ubd8enf9e/i8+/f7OnX///y///u+fPn8+zj9e7l+vTo+PTl8e7d///2///z/vfr+PHn+vTq//nt/fnq9fLi///5///1//vt/PTq//ju//7x//3u+fbl///7///3//3v//fs//vw///0///w/Pnn///8///3//3v//js//zx///1///x/fno)

_本博客报告并总结了 ACM_ [_Internet Measurement Conference_](https://conferences.sigcomm.org/imc/2022/program/) _上发表的 Cloudflare_ _[研究论文](https://research.cloudflare.com/publications/Singanamalla2022/)的内容，该论文对使用 ORIGIN Frames 实现的连接合并进行了测量和原型设计。_

有些读者可能会惊讶地发现，对一个网页的单次访问会导致浏览器进行数十次，有时甚至数百次 Web 连接。以本博客为例。如果您是第一次访问 Cloudflare 博客，或者距离上次访问已经有一段时间了，您的浏览器会进行多次连接来呈现页面。浏览器将进行 DNS 查询，以找到与 blog.cloudflare.com 相对应的 IP 地址，然后发出后续请求，以检索为成功呈现完整页面所需的网页上的任何必要子资源。有多少？请看下面，在撰写本文时，有 32 个不同的主机名用于加载Cloudflare 博客。这意味着需要 32 次 DNS 查询和_至少_ 32 个 TCP（或 QUIC）连接，除非客户端能够重复使用（或合并）其中的一些连接。

每个新的 Web 连接不仅会给服务器的处理能力带来额外负担（在使用高峰期可能导致可扩展性挑战），而且还会向网络暴露客户端元数据，例如个人正在访问的明文主机名。此类元信息可能会向路径上的网络对手和窃听者泄露用户的在线活动和浏览行为！

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - ckxTYV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47N3FXQ0TE0F5BAWC0YQTS.png&w=715&h=409&f=webp&fit=cover&position=center)

在本博客中，我们将对“连接合并”进行更深入的探讨。自 [2021 年首次研究基于 IP 的合并](https://blog.cloudflare.com/connection-coalescing-experiments/)以来，我们在互联网上进行了进一步的大规模测量和建模，以了解和预测合并是否可行以及在何处最有效。由于 IP 合并难以大规模管理，因此去年我们实施并试验了一项有前景的标准，称为 [HTTP/2 ORIGIN Frame 扩展](https://datatracker.ietf.org/doc/rfc8336/)，我们利用该标准将连接合并到我们的边缘，而无需担心管理 IP 地址。

总而言之，许多大型供应商都错失了一些机会。我们希望此博客（以及我们在 ACM IMC 2022 上发布的包含完整详细信息的[出版物](https://research.cloudflare.com/publications/Singanamalla2022/)）能迈出第一步，帮助服务器和客户端利用 ORIGIN Frame 标准。

### 做好准备

在高层次上，当用户浏览 Web 时，浏览器通过检索相关子资源来构建完整的网页，从而呈现网页。这一过程与工厂组装实物产品的方式极为相似。从这个意义上说，现代网页可以被视为一个装配厂。它依赖于生产最终产品所需的资源“供应链”。

现实世界中的装配厂可以使用一个订单来购买不同零件，并让供应商一次性发货所有零件（类似于最大化价值和最小化响应时间的[配套流程](https://www.sciencedirect.com/science/article/abs/pii/092552739290109K)）；无论这些零件的制造商或产地如何，只需与供应商建立一个“连接”即可。从供应商到装配厂的任何一辆卡车都可以装满来自多个制造商的零件。

Web 的设计导致浏览器通常会做相反的事情。要检索网页上的图像、JavaScript 和其他资源（零件），Web 客户端（装配厂）必须与服务器（供应商）返回的 HTML 中定义的每个主机名（制造商）_至少_建立一个连接。与这些主机名的连接是否前往同一服务器，这并没有什么影响，例如它们可以前往 Cloudflare 等[反向代理](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)。对于每个制造商来说，需要一辆“新”卡车将材料从同一供应商转移到装配厂，或者更正式地说，需要建立一个新连接，以从同一网页上的主机名请求子资源。

没有连接合并

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Without connection coalescing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46818DS1DBPGY0C4DKT15E.png&w=715&h=305&f=webp&fit=cover&position=center)

用于加载网页的连接数量可能高得惊人。子资源还需要其他子资源也是很常见的，因此前面的连接可能还会产生新的连接。还要记住，与主机名的 HTTP 连接通常先于 DNS 查询！连接合并使我们能够使用更少的连接_，或者“重复使用”同一组卡车从单个供应商运输来自多个制造商的零件。_

有连接合并

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![With connection coalescing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GJXTQ9MV673E7RD0JDJG.png&w=715&h=305&f=webp&fit=cover&position=center)

### 连接合并原则

连接合并[在 HTTP/2 中引入](https://datatracker.ietf.org/doc/html/rfc7540)，并延续到 [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html#name-connection-reuse) 中。我们[之前](https://blog.cloudflare.com/connection-coalescing-experiments/)曾在博客中讨论过连接合并（建议您阅读该博客以获得详细的入门知识）。虽然这个想法很简单，但实施它可能会带来许多工程挑战。例如，回想一下上面的内容，（在撰写本文时）有 32 个不同的主机名用于加载您现在正在阅读的网页。32 个主机名中有 16 个唯一域（定义为“有效 [TLD+1](https://www.cloudflare.com/learning/dns/top-level-domain/)”）。我们能否为每个唯一域创建更少的连接或“合并”现有连接？答案是“ _可以，但这取决于具体情况_ ”。

加载博客页面的确切连接数并不明显，也很难知道。可能有 32 个主机名连接到 16 个域名，但与直觉相反，这并不意味着“有多少个唯一连接？”的答案是 16。如果所有主机名都可以通过一台服务器访问，那么真正的答案可能是只有_一个_连接；如果访问每个主机名都需要不同的服务器，那么真正的答案可能是多达 32 个独立连接。

连接重复使用有多种形式，因此在 HTTP 领域定义“连接合并”非常重要。例如，重复使用一个主机名的现有 [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) 或 TLS 连接来多次请求_**同一** _主机名的子资源，这属于连接重复使用，但不属于合并。

当某些主机名的现有 TLS 通道可以重新调整用途或用于连接到_**不同** _的主机名时，就会发生合并。例如，访问 blog.cloudflare.com 时，HTML 指向 cdnjs.cloudflare.com 上的子资源。要为子资源重用相同的 TLS 连接，两个主机名必须一起出现在 TLS 证书的“[服务器备用名称 (SAN)](https://en.wikipedia.org/wiki/Subject_Alternative_Name)”列表中，但仅此一步不足以说服浏览器合并。毕竟，尽管使用相同的证书，但可能能够从同一服务器访问 blog.cloudflare.com 和 cdnjs.cloudflare.com 服务，也可能无法从同一服务器访问二者。那么浏览器怎么知道呢？仅当服务器设置正确的条件时，合并才起作用，但客户端必须决定是否合并——因此，浏览器需要一个信号才能在证书上的 SAN 列表之外进行合并。重温我们的比喻，装配厂可能会直接从制造商订购零件，却不知道供应商的仓库中已经有了同样的零件。

浏览器可以使用两种明确的信号来决定是否可以合并连接：一种是基于 IP 的信号，另一种是基于 ORIGIN Frame 的信号。前者要求服务器运营商将 DNS 记录与服务器上可用的 HTTP 资源紧密绑定。这很难管理和部署，而且实际上会产生有风险的依赖，因为必须将所有资源放在特定的一组或单一 IP 地址后面。IP 地址影响合并决策的方式[因浏览器而异](https://daniel.haxx.se/blog/2016/08/18/http2-connection-coalescing/)，有些浏览器更保守，有些则更宽容。另外，对于服务器来说，HTTP ORIGIN Frame 是一种更容易协调的信号；它也很灵活，而且可以在不中断服务的情况下优雅地失效（对于符合规范的实施）。

这两种合并信号之间的根本区别是：基于 IP 的合并信号是隐含的，甚至是偶然的，并迫使客户端推断是否存在合并可能性。这一切都不足为奇，因为 IP 地址的设计方式，其内容[与名称并无实际关系](https://blog.cloudflare.com/zh-cn/addressing-agility-zh-cn/)！相比之下，ORIGIN Frame 是从服务器到客户端的明确信号，即无论 DNS 对任何特定主机名有何规定，都可以进行合并。

我们之前已经尝试过[基于 IP 的合并](https://blog.cloudflare.com/connection-coalescing-experiments/)；在这篇博客中，我们将更深入地探讨基于 ORIGIN Frame 的合并。

### 什么是 ORIGIN Frame 标准？

ORIGIN Frame 是 [HTTP/2](https://www.rfc-editor.org/rfc/rfc8336) 和 [HTTP/3](https://www.rfc-editor.org/rfc/rfc9412) 规范的扩展，是分别在 stream 0 或连接的控制流上发送的特殊帧。该帧允许服务器在已建立的_现有_ TLS 连接上向客户端发送“origin-set”，其中包括已授权的主机名，并且不会产生任何 [HTTP 421 错误](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/421)。origin-set 中的主机名也必须出现在服务器的证书 SAN 列表中，即使这些主机名是通过 DNS 在不同的 IP 地址上公告的。

具体来说，需要两个不同的步骤：

  1. Web 服务器必须发送一个列表，枚举 ORIGIN Frame 扩展中的 Origin Set（给定连接可能用于的主机名）。
  2. Web 服务器返回的 TLS 证书必须涵盖 DNS 名称 SAN 条目中 ORIGIN Frame 中返回的其他主机名。



从高层次来看，ORIGIN Frames 是 TLS 证书的补充，运营商可以附加该证书来表示“嘿，客户端，这是此连接上可用的 SAN 中的名称——您可以合并！”由于 ORIGIN Frame 不是证书本身的一部分，因此可以独立更改其内容。不需要新的证书。也不依赖于 IP 地址。对于可合并的主机名，现有的 TCP/QUIC+TLS 连接可以重复使用，而不需要新的连接或 DNS 查询。

[如今许多网站](https://w3techs.com/technologies/overview/proxy)都依赖 CDN 提供的内容，例如 Cloudflare CDN 服务。使用外部 CDN 服务的做法为网站提供了速度、可靠性的优势，并减少了其[源服务器](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)提供的内容负载。当网站和资源都由同一个 CDN 提供服务时，尽管主机名不同、属于不同的实体，但它为 CDN 运营商提供了一些非常有趣的机会，允许重用和合并连接，因为他们可以控制证书管理和代表真正的源服务器发送 ORIGIN Frame 的连接请求。

遗憾的是，我们还没有办法将 ORIGIN Frame 带来的可能性付诸实践。据我们所知，到目前为止，还没有服务器实施支持 ORIGIN Frames。在所有浏览器中，只有 Firefox 支持 ORIGIN Frames。由于 IP 合并具有挑战性，而 ORIGIN Frame 没有部署的支持，那么为更好地支持合并而投入的工程时间和精力是否值得？我们决定通过大规模的互联网测量来了解机会和预测可能性，然后实施 ORIGIN Frame，在生产流量上进行实验。

### 实验 1：所需更改的规模有多大？

2021 年 2 月，我们在 100 个虚拟机上使用修改后的[网页测试](https://github.com/WPO-Foundation/webpagetest)收集了互联网上 50 万个[最受欢迎网站](https://radar.cloudflare.com/domains)的[数据](https://blog.cloudflare.com/connection-coalescing-experiments/)。每次访问网页时都会启动一个自动 Chrome (v88) 浏览器实例，以消除缓存效应（因为我们想要了解合并，而不是缓存）。在成功完成每个会话后，我们使用 Chrome 开发人员工具检索页面加载数据并将其写入 HTTP 存档格式 (HAR) 文件，其中包含完整的事件时间线以及有关证书及其验证的其他信息。此外，我们还解析了根网页的证书链以及由子资源请求触发的新 TLS 连接，以：(i) 识别主机名的证书颁发者；(ii) 检查主题备用名称 (SAN) 扩展是否存在；以及 (iii) 验证 DNS 名称是否解析为所使用的 IP 地址。有关我们的方法和结果的更多详细信息，请参阅技术[论文](https://research.cloudflare.com/publications/Singanamalla2022/)。

第一步是了解网页需要哪些资源才能成功呈现网页内容，以及这些资源在互联网上的位置。当子资源域处于理想的共同位置时，连接合并就成为可能。我们通过查找相应的自治系统 (AS) 来大概确定域的位置。例如，连接到 [cdnjs](https://cdnjs.cloudflare.com/https://cdnjs.cloudflare.com/) 的域可通过 BGP 路由表中的 AS 13335 到达，而该 AS 号码属于 Cloudflare。下图描述了完全加载一个网页所需的网页百分比和唯一 AS 号码。

大约 14% 的网页需要两个 AS 才能完全加载，即网页需要依赖另外一个 AI 来获得子资源。超过 50% 的网页需要联系不超过 6 个 AS 来获取所有必需的子资源。如上图所示，这一发现意味着相对少数的运营商提供大多数（约 50%）网站所需的子资源内容，并且任何使用 ORIGIN Frames 的情况都只需要进行少量更改就能产生预期的影响。因此，连接合并的可能性可以乐观地估计为检索网页中所有子资源所需的唯一 AS 的数量。不过，在实际操作中，这可能会被 SLA 等操作因素所取代，或者受到我们[之前在 Cloudflare](https://research.cloudflare.com/publications/Fayed2021/) 处理过的套接字、名称和 IP 地址之间的灵活映射的帮助。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - 3Dlhpw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45X8GDMJVMT39D8F70E2T1.png&w=715&h=349&f=webp&fit=cover&position=center)

然后，我们尝试了解合并对连接指标的影响。根据 CDF 汇总了加载网页所需的 DNS 查询和 TLS 连接的测量数量和理想数量，如下图所示。

通过建模和大量分析，我们发现通过 ORIGIN Frames 进行连接合并可将浏览器建立的 DNS 和 TLS 连接数量减少 60% 以上（以中位数计算）。我们通过识别客户端请求 DNS 记录的次数来进行建模，并将其与要提供的理想 ORIGIN Frames 服务相结合。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - DZcmqU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48T1Y598J42C2CVMPC1M33.png&w=715&h=394&f=webp&fit=cover&position=center)

许多多源服务器（如 [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) 运行的服务器）倾向于重复使用证书，并通过多个 DNS SAN 条目提供相同的证书。这样，运营商就可以在创建和更新周期内管理较少的证书。虽然从理论上讲，证书中可以包含数百万个名称，但创建这样的证书是不合理的，也很难有效管理。如下图所示，通过继续依赖现有证书，我们的建模测量揭示了实现完美合并所需的更改量，同时提供了所需更改规模的信息。

我们发现，超过 60% 的网站提供的证书不需要任何修改，就可以从 ORIGIN Frames 中受益，而在证书中添加不超过 10 个 DNS SAN 名称的情况下，我们能够成功地将连接合并到测量的网站中超过 92% 的网站。CDN 提供商可以通过在每个证书中添加三到四个最受欢迎的请求主机名来进行最有效的更改。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - 3Eev4N](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47R6AZHNG2GYF9CH2S97M9.png&w=715&h=398&f=webp&fit=cover&position=center)

### 实验 2：ORIGIN Frames 实际应用

为了验证我们的建模预期，我们在 2022 年初采取了更积极的方法。我们的下一个实验重点关注 5,000 个广泛使用 _cdnjs.cloudflare.com_ 作为子资源的网站。通过修改我们的实验性 TLS 终止端点，我们部署了 [RFC 标准](https://datatracker.ietf.org/doc/rfc8336/)中定义的 HTTP/2 ORIGIN Frame 支持。这涉及到更改 Golang 的 _net_ 和 _http_ 依赖模块的内部分支（已开源，请参阅[此处](https://github.com/cloudflare/go-originframe)和[此处](https://github.com/cloudflare/net-originframe)）。

在实验期间，连接到实验组中的网站将在 ORIGIN Frame 中返回 _cdnjs.cloudflare.com_ ，而控制组则返回任意（未使用的）主机名。5000 个网站的所有现有边缘证书也被修改。对于实验组，更新了相应的证书，并将 _cdnjs.cloudflare.com_ 添加到 SAN。为了确保控制组和实验组之间的完整性，还使用未被任何控制域使用的有效且相同大小的第三方域来更新控制组域证书。这样做是为了确保证书的相对大小变化保持恒定，避免由于不同的证书大小而导致的潜在偏差。我们的结果是惊人的！

对实验中从 Firefox 收到的网站请求的 1% 进行采样，我们发现**每秒新的 TLS 连接数减少了 50%** 以上，这表明客户端执行的加密验证操作数量减少，服务器计算开销也减少了。正如预期的那样，控制组没有差异，表明 CDN 或服务器运营商看到了连接重用的有效性。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - q0fWGU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45GKTR9B46ZHYNCDK42GGC.png&w=715&h=399&f=webp&fit=cover&position=center)

### 讨论和见解

虽然我们的建模测量结果表明，我们可以期望一些性能改进，但实际上性能并没有明显改善，这表明“不会变差”才是有关性能的正确心态。资源对象大小、竞争连接和拥塞控制之间微妙的相互作用取决于网络条件。例如，随着竞争网络链路上瓶颈资源的连接减少，瓶颈共享容量也会减少。随着越来越多的运营商在其服务器上部署对 ORIGIN Frames 的支持，重新研究这些测量结果将是非常有意义的。

除了性能之外，ORIGIN Frames 的一大优势是隐私性。怎么实现呢？嗯，每个合并连接都会隐藏客户端元数据，若没有连接合并，这些元数据就会从未合并的连接中泄漏出去。网页上某些资源的加载取决于人们与网站交互的方式。这意味着对于从服务器检索某些资源的每个新连接，如果通过端口 53 上的 UDP 或 TCP 传输，则 [SNI](https://www.cloudflare.com/learning/ssl/what-is-sni/) 之类的 TLS 明文元数据（在没有 [Encrypted Client Hello](https://blog.cloudflare.com/encrypted-client-hello/) 的情况下）和至少一个明文 DNS 查询会暴露给网络。合并连接有助于消除浏览器打开新 TLS 连接的需要，以及执行额外 DNS 查询的需要。这可以防止网络监听者泄露元数据。ORIGIN Frames 有助于最大限度地减少来自网络路径的信号，通过减少泄露给网络窃听者的明文信息量来提高隐私性。

浏览器可以从减少验证多个证书所需的加密计算中获益，但它的一个主要优势在于，它为端点（浏览器和源服务器）的资源调度开辟了非常有趣的未来机会，例如[优先级](https://blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/)，或最近提出的 [HTTP 早期提示](https://blog.cloudflare.com/early-hints/)等建议，这用于提供一种客户端体验，使连接不会超载或竞争这些资源。如果与 [CERTIFICATE Frames](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-http2-secondary-certs-06#section-3.4) IETF 草案相结合，我们就能进一步消除手动修改证书的需要，因为服务器可以在建立连接后证明其对主机名的授权，而无需在网站的 TLS 证书上添加任何额外的 SAN 条目。

### 总结与行动号召

总之，只需对证书及其服务器基础设施稍作改动，当前的互联网生态系统就能为连接合并提供大量机会。服务器可将 TLS 握手的次数大幅减少约 50%，同时将阻塞 DNS 查询的渲染次数减少 60% 以上。此外，客户端还可以通过减少明文 DNS 对网络监视者的暴露来获得隐私方面的好处。

为了帮助实现这一目标，我们目前正计划为客户添加对 HTTP/2 和 HTTP/3 ORIGIN Frames 的支持。我们也鼓励其他管理第三方资源的运营商采用 ORIGIN Frames 支持，以改善互联网生态系统。我们提交的论文已被 2022 年 ACM Internet Measurement Conference 接受，[可供下载](https://research.cloudflare.com/publications/Singanamalla2022/)。如果您想参与这样的项目，亲眼见证新标准的诞生，请访问我们的[招聘页面](https://www.cloudflare.com/careers/)！

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F&t=%E4%BD%BF%E7%94%A8%20ORIGIN%20Frames%20%E5%AE%9E%E7%8E%B0%E8%BF%9E%E6%8E%A5%E5%90%88%E5%B9%B6%EF%BC%9A%E5%87%8F%E5%B0%91%20DNS%20%E6%9F%A5%E8%AF%A2%EF%BC%8C%E5%87%8F%E5%B0%91%E8%BF%9E%E6%8E%A5%E6%95%B0)[](https://x.com/intent/post?text=%E4%BD%BF%E7%94%A8+ORIGIN+Frames+%E5%AE%9E%E7%8E%B0%E8%BF%9E%E6%8E%A5%E5%90%88%E5%B9%B6%EF%BC%9A%E5%87%8F%E5%B0%91+DNS+%E6%9F%A5%E8%AF%A2%EF%BC%8C%E5%87%8F%E5%B0%91%E8%BF%9E%E6%8E%A5%E6%95%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://bsky.app/intent/compose?text=%E4%BD%BF%E7%94%A8+ORIGIN+Frames+%E5%AE%9E%E7%8E%B0%E8%BF%9E%E6%8E%A5%E5%90%88%E5%B9%B6%EF%BC%9A%E5%87%8F%E5%B0%91+DNS+%E6%9F%A5%E8%AF%A2%EF%BC%8C%E5%87%8F%E5%B0%91%E8%BF%9E%E6%8E%A5%E6%95%B0+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://mastodonshare.com/?text=%E4%BD%BF%E7%94%A8+ORIGIN+Frames+%E5%AE%9E%E7%8E%B0%E8%BF%9E%E6%8E%A5%E5%90%88%E5%B9%B6%EF%BC%9A%E5%87%8F%E5%B0%91+DNS+%E6%9F%A5%E8%AF%A2%EF%BC%8C%E5%87%8F%E5%B0%91%E8%BF%9E%E6%8E%A5%E6%95%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://www.threads.net/intent/post?text=%E4%BD%BF%E7%94%A8+ORIGIN+Frames+%E5%AE%9E%E7%8E%B0%E8%BF%9E%E6%8E%A5%E5%90%88%E5%B9%B6%EF%BC%9A%E5%87%8F%E5%B0%91+DNS+%E6%9F%A5%E8%AF%A2%EF%BC%8C%E5%87%8F%E5%B0%91%E8%BF%9E%E6%8E%A5%E6%95%B0+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)

## 相关标签

[DNS](https://blog.cloudflare.com/zh-cn/tag/dns/)[HTTP2](https://blog.cloudflare.com/zh-cn/tag/http2/)[Internship Experience](https://blog.cloudflare.com/zh-cn/tag/internship-experience/)[TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)[研究](https://blog.cloudflare.com/zh-cn/tag/research/)[速度和可靠性](https://blog.cloudflare.com/zh-cn/tag/speed-and-reliability/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Sudheesh Singanamalla](https://blog.cloudflare.com/zh-cn/author/sudheesh/)

[](https://sudheesh.info/)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
