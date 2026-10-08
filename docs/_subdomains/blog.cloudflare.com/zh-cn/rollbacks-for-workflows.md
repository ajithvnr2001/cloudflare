---
url: https://blog.cloudflare.com/zh-cn/rollbacks-for-workflows/
title: \u6211\u4eec\u5982\u4f55\u6784\u5efa\u9002\u7528\u4e8e Cloudflare Workflows \u7684 saga \u56de\u6eda | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:40.656161+00:00
---

# 我们如何构建适用于 Cloudflare Workflows 的 saga 回滚 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/rollbacks-for-workflows/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Workflows](https://blog.cloudflare.com/zh-cn/tag/workflows/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

3 个标签显示 3 个标签

  * 文章标签
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Workflows](https://blog.cloudflare.com/zh-cn/tag/workflows/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)
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



[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Workflows](https://blog.cloudflare.com/zh-cn/tag/workflows/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

2026年6月25日

# 我们如何构建适用于 Cloudflare Workflows 的 saga 回滚

![Vaishnav Kavitha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMMZ8JJQ1SE783SASV4PJ.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Mia Malden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4559TC07A12MQHAEK8YM1R.jpg&w=64&h=64&f=webp&fit=cover&position=center)![André Venceslau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TZTSTWQ6JMKEC8GX38NE.png&w=64&h=64&f=webp&fit=cover&position=center)

[Vaishnav Kavitha](https://blog.cloudflare.com/zh-cn/author/vaishnav-kavitha/)、[Mia Malden](https://blog.cloudflare.com/zh-cn/author/mia/)和[André Venceslau](https://blog.cloudflare.com/zh-cn/author/andre-venceslau/)

阅读时间：10 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/rollbacks-for-workflows/)、[日本語](https://blog.cloudflare.com/ja-jp/rollbacks-for-workflows/)、[한국어](https://blog.cloudflare.com/ko-kr/rollbacks-for-workflows/)和[繁體中文](https://blog.cloudflare.com/zh-tw/rollbacks-for-workflows/).

![BLOG-3317 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMM3AX6SCQ1TVSR6M8NMX.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+P/84u3z1uPw4Onz8PP39fX07u3s////+v/+4+320+Dy1+L15ez57fD27O3u/////f//5+/509/1z9742uX85uz57O3x////////7vT+2eP50d/82OX/5ez97/D1////////+Pz/5ez+3ef/4uv/7fL/9fb6////////////9Pf/7/P/8vf/+fv//fz+/////////////////f3/////////////////////////////////////////////)

Cloudflare Workflows 支持您构建持久可靠的多步骤应用，内置重试机制和状态持久化功能，确保进程长时间运行。执行[ _工作流程_](https://developers.cloudflare.com/workflows/)时，每个步骤都可以调用外部系统，重试失败操作，并在重启后保持状态。但如果某个步骤失败，可能会导致之前已完成步骤的工作处于不一致或不完整的状态。

今天，我们推出了适用于 Workflows 的 saga 回滚功能，支持您在步骤中声明回滚逻辑，以防发生故障。

例如，思考一下在两个不同银行之间转账的工作流程：

  1. 从银行 A 的账户扣款
  2. 存入银行 B 的账户
  3. 向两个账户的所有者发送电子邮件确认函



如果步骤 2（存入银行 B 的账户）失败，会发生什么？一旦银行 A 的账户扣款成功执行，交易即被提交，资金已离开其系统。作为交易的协调者，您无法简单地在银行 A 的系统中“撤销”该操作。相反，这笔钱必须通过语义上逆转第一次操作顺序的新操作，退回到 A 银行的账户。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WKYMHAWC2FCMBSGG1XMKT.png&w=715&h=681&f=webp&fit=cover&position=center)

  
这种将操作与其补偿逻辑相结合的方式称为 [_saga 模式_](https://www.youtube.com/watch?v=xDuwrtwYHu8)。

在此之前，开发人员必须在步骤的直接定义之外，实施其补偿逻辑来跟踪哪些操作成功、哪些操作失败，以及失败后应该采取哪些措施。现在，您可以将每个 `step.do()` 的补偿逻辑定义为步骤中的一个参数，同时也维持回滚工作流的持久性。
    
    
    // track what completed so we know what to undo
    let debitA;
    let creditB;
    try {
      debitA = await step.do("debit-bank-a", () => bankA.debit(from, amount));
      creditB = await step.do("credit-bank-b", () => bankB.credit(to, amount));
      await step.do("notify", () => notifyBoth(from, to, amount));
    } catch (error) {
      // unwind in reverse. each undo is its own durable step,
      // must be idempotent, and must keep going if one fails.
      if (creditB) {
        try {
          await step.do("reverse-credit-b", () => bankB.debit(to, amount, creditB.id));
        } catch (e) {
          await alertOnCall("reverse-credit-b failed", e);
        }
      }
      if (debitA) {
        try {
          await step.do("refund-debit-a", () => bankA.credit(from, amount, debitA.id));
        } catch (e) {
          await alertOnCall("refund-debit-a failed", e);
        }
      }
      throw error;
    }

_不包含回滚_
    
    
     // each step ships with its own undo. add a step,
    // add its rollback right here. no growing catch
    // block, no manual ordering, no replay logic.
    await step.do("debit-bank-a", () => bankA.debit(from, amount), {
      rollback: async ({ output }) => bankA.credit(from, amount, output.id),
    });
    await step.do("credit-bank-b", () => bankB.credit(to, amount), {
      rollback: async ({ output }) => bankB.debit(to, amount, output.id),
    });
    await step.do("notify", () => notifyBoth(from, to, amount));

_包含回滚_

## 立即试用

若要使用回滚功能，只需将包含 `rollback` 函数的选项对象作为最后一个参数传递给 `step.do()`。
    
    
    const debit = await step.do(
      "debit-account-a",
      async () => {
        return await bankA.debit({
          accountId: fromAccountId,
          amount,
          idempotencyKey: `${transferId}:debit-account-a`,
        });
      },
      {
        rollback: async () => {
          await bankA.credit({
            accountId: fromAccountId,
            amount,
            idempotencyKey: `${transferId}:rollback-debit-account-a`,
          });
        },
      }
    );
    
    // The idempotency keys make both the forward operations and rollback operations safe to retry without duplicating the transfer
    
    const credit = await step.do(
      "credit-account-b",
      async () => {
        return await bankB.credit({
          accountId: toAccountId,
          amount,
          idempotencyKey: `${transferId}:credit-account-b`,
        });
      },
      {
        rollback: async ({ output }) => {
          if (output === undefined) {
            return;
          }
    
          await bankB.debit({
            accountId: toAccountId,
            amount,
            idempotencyKey: `${transferId}:rollback-credit-account-b`,
          });
        },
      }
    );
    
    
    // If we fail here, we may want to revert all previous payments. Users should not have to wrap their code in complex try-catch logic just to revert two small payments (see below)
    
    await step.do("send-confirmation", async () => {
      await sendTransferConfirmation({ ... });
    });

回滚函数应该像常规工作流程步骤一样具有幂等性。如果退款，请使用支付提供商的幂等密钥。如果释放库存，请确保可以安全地多次调用释放操作。

如果任何步骤失败，回滚处理程序将按 ` step-start` 的逆序执行。这听起来很简单：如果出现故障，执行撤销步骤。实际上，有一些细节使得 API 和执行模型至关重要。

1.**失败的步骤可能仍需回滚。** 如果失败的 `step.do()` 已注册回滚处理程序，则该步骤仍然有资格进行回滚。

如果用户代码捕获了错误且继续执行工作流程，则不会启动回滚；如果捕获到步骤错误但工作流程稍后由于其他原因失败，则仍然可以对之前已注册的处理程序执行回滚，这些处理程序按 `step-start` 的逆序执行。

为什么？因为该步骤在失败之前可能已与外部系统进行了部分交互。例如，支付提供商可能捕获了一笔费用，但在将 `chargeId` 返回给 Workflows 之前，该步骤可能会失败。这就是为什么回滚处理程序会接收 `output`，但必须处理 `output === undefined` 的情况。

2\. **仅当工作流程失败时启动回滚。** 添加回滚处理程序并不意味着每个步骤错误都会触发回滚。如果用户代码捕获了错误并继续操作，则工作流程将继续执行。当工作流程本身即将彻底失败时，启动回滚。

回滚启动时，Workflows 会找到符合条件的 `step.do()`调用，运行其回滚处理程序，然后记录最终的工作流程失败。

3\. **订单必须是可预测的。** 对于顺序执行的 Workflows，回滚顺序很明确：

  1. 预留库存。
  2. 信用卡扣款。
  3. 创建发货。
  4. 如果发货失败，则退款并释放库存。



并行步骤使回滚变得更加微妙。完成顺序可能与开始顺序不同，因此，Workflows 使用 step-start 的逆序，而不是完成顺序的逆序。

实际规则如下：

  1. 任何已启动或已完成且包含回滚处理程序的步骤均符合条件。
  2. 如果失败的 `step.do()` 已注册回滚处理程序，则也符合条件。
  3. 处理程序按 step-start 的逆序运行，而不是完成顺序运行。



## API 设计方法

确定预期行为后，我们需要将这种新模式添加到 Workflows API。回滚机制经过多次迭代，才最终确定 `rollback options`。

### 为什么不采用流畅或构建器 API？

第一种方法是流畅形式：`step.do(...).rollback(...)`，这种写法易于阅读。前向操作和补偿操作彼此相邻，调用位置看起来像普通的 JavaScript 链式调用。

问题在于 `step.do()` 已经具有重要意义：它启动一个持久步骤，并返回一个 Promise 作为步骤输出。在 Workers 中，类似 promise 的值尤其重要，因为 Workers RPC 支持[ _promise 管道_](https://blog.cloudflare.com/capnweb-javascript-rpc-library/#chained-calls-promise-pipelining)，这种模式继承自 [_Cap'n Proto_](https://capnproto.org/rpc.html#time-travel-promise-pipelining) 等系统。

Promise 管道支持代码在值完全返回给调用者之前，调用 future 值的方法。例如：
    
    
    const session = api.authenticate(apiKey);
    const name = await session.whoami();

在这里，`session` 并不是真正的会话对象。它更像是一个即将存在的会话的句柄。当您调用 `session.whoami()` 时，Workers 可以提前将该调用发送到远程端，并告知：“一旦身份验证创建了会话，就对其调用 `whoami()`。”

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMVWKS68D8HCFGVRZQ2RA.png&w=715&h=476&f=webp&fit=cover&position=center)

这样可以节省一次往返通信。调用者无需等待 `authenticate()` 完全结束即可请求 `whoami()`。

我们考虑了一种流畅 API：
    
    
    step.do("charge-card", chargeCard).rollback(refundCharge);

  
对于读者来说，这看起来可能像是“针对 `charge-card` 的结果调用 `.rollback()`”。但回滚操作不是该步骤的输出的一部分。它是 `step.do()` 的一部分，在步骤开始前已注册，以便 Workflows 知道如果后续步骤失败，应该如何补偿步骤。

流畅 API 也使得步骤的执行时间更加难以理解。目前，`step.do()` 会在调用后启动步骤，因此，开发人员可以启动一个步骤，执行其他工作，然后等待第一步完成：
    
    
    const first = step.do("first", () => serviceA.call());
    
    await step.do("second", () => serviceB.call());
    
    await first;

在当前的执行模型中，`first` 会立即启动，早于 `second`。流畅 API 会使情况变得复杂。Workflows 需要等待，并查看 `.rollback()` 是否已附加，才能了解完整的步骤定义。这可能会延迟将步骤发送到引擎的时间。

在前面的示例中，`first` 可能会在 `await first` 点启动，而不是在 `step.do("first", ...)` 点启动，即使 `second` 已完成。

这导致更加难以推理并发 Workflows 步骤：步骤的执行时间取决于何时使用返回的 `Promise`，而不仅仅是 `step.do()` 的调用位置。

我们也考虑了一种构建器 API：
    
    
    const charge = await step
    	.saga("charge")
    	.do(() => chargeCard())
    	.rollback(() => refundCharge())
    	.run();

构建器 API 可以避免 `Promise` 模糊不清。它还提供了一个清晰的位置来添加未来的步骤级选项，并清楚地表明前向操作和回滚操作属于同一个 saga 步骤。

但它也增加了繁琐的流程。每个步骤都需要一个最终的 `.run()`，如果没有工具辅助，则很容易发生忘记 `.run()` 的情况，以及简单的一步用例也会变得像配置链那样复杂。它还引入了一个新的 `step.saga()` 构建器，打破现有的 `step.<action>` 模式。最重要的是，它让 `step.do()` 感觉更像是一个较旧的 API，而不是主要的 Workflows 基础组件。回滚的目标是扩展 `step.do()`，而不是取代它。

### 回滚作为步骤元数据
    
    
    step.do(..., { rollback })

最终，我们选择了显式形式，其中回滚作为步骤的元数据。

这样，每个回滚都在前向步骤本身中定义。每个处理程序都会接收导致回滚开始的错误、[ _步骤上下文_](https://developers.cloudflare.com/workflows/build/step-context/)和输出，输出可能是前向步骤返回的持久值（可以未定义），或者如果步骤在持久化值之前失败，则为未定义值。

回滚会触发生命周期事件，因此，您可以判断补偿是否已开始、哪个回滚处理程序失败，以及回滚是否已成功完成。

至关重要的是，原始工作流程故障仍然是独立的：回滚是 Workflows 在故障后执行的操作，而不是工作流程故障的原因。

正如您可以通过 `WorkflowStepConfig` 在[ _步骤配置_](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstepconfig)中定义自定义重试和超时行为一样，您可以在 `rollbackConfig` 中添加回滚特定值。
    
    
    {
      rollback: async ({ output }) => {
        await bankA.credit({ accountId: fromAccountId, amount, transferId: `${transferId}-reversal` });
      },
      rollbackConfig: {
        retries: { limit: 10, delay: '30 seconds', backoff: 'exponential' },
        timeout: '2 minutes',
      },
    }

这符合我们想要的生命周期事件心智模型。`step.do()` 已经描述了 Workflows 会记录、重试，以及稍后显示在日志中的持久化工作单元。回滚是同一工作单元的另一种生命周期行为。它应该与步骤定义一起移动，而不是存在于单独的封装器或构建器中。

  * `step.do()` 正常启动后，该步骤仍然会启动。
  * 返回的 promise 仍然代表步骤输出。
  * 并发工作流程代码保持相同的执行模型。
  * 实时重试和超时选项位于回滚处理程序旁边。
  * 现有的 `step.do()` 调用方式保持不变。



这种形式比流畅 API 更明显一些，但这种明确性很有用。操作及其补偿仍然位于同一位置，而且 API 没有引入新的步骤构建器或新的 Promise 类型。已经掌握 `step.do()` 的开发人员只需要学习一个额外的 `options` 对象。

这虽然不如魔法般神奇，但更易于采用，也更清晰易懂。

## 底层工作原理

回滚机制看似只是一个微小的 API 新增功能，但它改变了 Workflows 需要记录的每个步骤信息。

常规的 `step.do()` 已经包含持久化记录。Workflows 会记录步骤何时启动、是否完成、返回值，以及如果工作流程稍后恢复，是否应跳过该步骤而不是重复执行。

回滚在该记录中添加另一项信息：步骤是否已注册补偿逻辑。

这意味着，如果 Workflows 失败，则需要整合两项信息。

首先是**持久化步骤历史记录** 。Workflow 引擎会存储数据，以了解哪些步骤运行、哪些步骤已完成、保存了哪些输出，以及是否已注册回滚。

其次是**回滚处理程序** 本身，这是为补偿该步骤而编写的函数。Workflows 不会将该函数的文本保存为数据。相反，它会在工作流程运行时保留对该处理程序的可调用引用。

在 Workers RPC 中，这种可调用引用称为[** _存根_**](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle)。存根支持系统的一部分调用在其他地方运行的代码。存根也具有生命周期，因此，可以在调用或执行上下文结束时进行处置。如果需要在此之后继续保留存根，Workers RPC 提供 [`_dup()_`](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle/#the-dup-method) 方法，此方法会创建指向同一目标的另一个句柄。

对于回滚，这种模型非常有用。持久化步骤历史记录会记录需要补偿的操作。回滚存根为 Workflows 提供了一种调用补偿。由于回滚处理程序可能需要比注册它们的 `step.do()` 调用本身更长的生命周期，Workflows 会保留对处理程序的可调用引用，以备回滚阶段之用。

通常情况下，当工作流程在同一引擎生命周期中进入回滚阶段时，Workflows 已经拥有所需的回滚存根。它可以利用持久化步骤历史记录来查找符合条件的步骤，然后调用在前向执行期间注册的回滚存根。

当 Workflows 需要在重启后**恢复** 时，情况会变得更加复杂。

如果在需要回滚时引擎被驱逐、崩溃或重启，Workflows 仍然拥有持久化步骤历史记录，但它可能不再拥有内存中的回滚存根。为了恢复，Workflows 使用**重放** ：这是一种恢复模式，它可以重新运行工作流程代码，而无需重新执行已完成的前向步骤主体。

当重放模式达到一个已完成的 `step.do()` 步骤时，Workflows 会读取持久化结果，而不是再次运行步骤主体。对于回滚恢复，Workflows 只需为已附加回滚选项且符合回滚条件的步骤重建处理程序。当遇到这些 `step.do() `调用时，它们的回滚选项可以再次注册可调用存根。

这让 Workflows 能够恢复所需的回滚处理程序，而不复制原始外部副作用。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMK8HE1XEHVNX1B4RNK9W.png&w=715&h=699&f=webp&fit=cover&position=center)

借助这些部署到位的组件，无论处理程序是否仍在内存中，或者在恢复过程中必须重建，回滚都能正常工作。

当工作流程即将失败时，Workflows 不会要求您的应用重建已发生的事件。它已经拥有步骤历史记录。它可以查看持久化记录并回答以下重要问题：

  * 哪些步骤已启动？
  * 哪些步骤已完成？
  * 哪些失败的步骤可能仍然需要清理？
  * 哪些步骤已注册回滚处理程序？
  * 每个回滚处理程序应该接收什么输出？
  * 补偿操作应该按什么顺序运行？



然后，Workflows 会使用回滚上下文调用每个回滚存根：原始错误、步骤上下文，以及步骤输出（如果已持久化）。

顺序细节至关重要。在常规的 JavaScript 中，尤其是使用 `Promise.all()` 时，完成顺序并不总是与开始顺序相同。如果步骤 A 率先开始，步骤 B 紧随其后，步骤 B 可能先完成。对于回滚，Workflows 使用持久化启动顺序作为稳定的真实数据源，然后反向回滚。

回滚处理程序也会通过 Workflows 的正常步骤机制运行。这意味着，补偿操作拥有与 Workflows 相同的操作属性：重试、超时、生命周期事件、事件日志，以及最终记录的结果。如果回滚处理程序在配置的重试次数之后仍然失败，Workflows 会将回滚结果记录为失败，停止运行剩余的回滚处理程序，并且 Workflow 实例最终会处于 `Errored` 状态。

这是 saga 回滚与 `catch` 块之间的主要区别。`catch` 块只知道在 JavaScript 执行到它所在的确切位置时内存中仍然还有哪些内容。Workflows 回滚会利用持久化步骤历史记录来确定已发生的事件，通常情况下调用已有的存根，以及根据需要，在恢复期间安全地重建丢失的存根。

这也是为什么 API 将回滚逻辑封装在 `step.do()` 中。回滚并不是一个独立的全局错误处理程序，而是附加在 Workflows 已理解的持久化工作单元上的元数据。

## 下一步

我们的第一版回滚功能包括：

  * 适用 `step.do()` 的显式步骤回滚处理程序
  * 顺序回滚执行
  * 用于补偿的重试和超时配置



接下来，我们希望探索：

  * 对 [`_waitForEvent_`](https://developers.cloudflare.com/workflows/build/events-and-parameters/#wait-for-events) 的回滚支持
  * 支持并行回滚执行
  * 对 [_Python Workflows_](https://developers.cloudflare.com/workflows/python/) 的回滚支持



当一个多步骤应用在执行过程中失败时，最难的部分往往不是知道 _它_ 失败了。而是知道 _已经_ 发生的事情，以及接下来需要做什么。

Saga 回滚功能让您可以将答案直接添加到每个步骤旁边。如果您正在使用 Workflows 构建多步骤应用，请尝试使用 saga 回滚功能，并告诉我们您接下来希望采用哪些补偿模式。阅读 [_Workflows 文档_](https://developers.cloudflare.com/workflows/)，了解入门信息，并在 [_Cloudflare 社区_](https://community.cloudflare.com/)分享反馈。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frollbacks-for-workflows%2F&t=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%9E%84%E5%BB%BA%E9%80%82%E7%94%A8%E4%BA%8E%20Cloudflare%20Workflows%20%E7%9A%84%20saga%20%E5%9B%9E%E6%BB%9A)[](https://x.com/intent/post?text=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%9E%84%E5%BB%BA%E9%80%82%E7%94%A8%E4%BA%8E+Cloudflare+Workflows+%E7%9A%84+saga+%E5%9B%9E%E6%BB%9A&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frollbacks-for-workflows%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frollbacks-for-workflows%2F)[](https://bsky.app/intent/compose?text=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%9E%84%E5%BB%BA%E9%80%82%E7%94%A8%E4%BA%8E+Cloudflare+Workflows+%E7%9A%84+saga+%E5%9B%9E%E6%BB%9A+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frollbacks-for-workflows%2F)[](https://mastodonshare.com/?text=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%9E%84%E5%BB%BA%E9%80%82%E7%94%A8%E4%BA%8E+Cloudflare+Workflows+%E7%9A%84+saga+%E5%9B%9E%E6%BB%9A&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frollbacks-for-workflows%2F)[](https://www.threads.net/intent/post?text=%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%9E%84%E5%BB%BA%E9%80%82%E7%94%A8%E4%BA%8E+Cloudflare+Workflows+%E7%9A%84+saga+%E5%9B%9E%E6%BB%9A+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Frollbacks-for-workflows%2F)

## 相关标签

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Workflows](https://blog.cloudflare.com/zh-cn/tag/workflows/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
