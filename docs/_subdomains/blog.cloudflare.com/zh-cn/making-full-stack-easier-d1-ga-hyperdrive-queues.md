---
url: https://blog.cloudflare.com/zh-cn/making-full-stack-easier-d1-ga-hyperdrive-queues/
title: \u4f7f\u7528\u6b63\u5f0f\u53d1\u5e03\u7684 D1 \u4ee5\u53ca Hyperdrive\u3001Queues \u548c Workers Analytics Engine \u66f4\u65b0\uff0c\u7b80\u5316\u72b6\u6001\u7ba1\u7406 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:32.492659+00:00
---

# 使用正式发布的 D1 以及 Hyperdrive、Queues 和 Workers Analytics Engine 更新，简化状态管理 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/making-full-stack-easier-d1-ga-hyperdrive-queues/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[D1](https://blog.cloudflare.com/zh-cn/tag/d1/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)+4再显示 4 个标签

7 个标签显示 7 个标签

  * 文章标签
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[D1](https://blog.cloudflare.com/zh-cn/tag/d1/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Hyperdrive](https://blog.cloudflare.com/zh-cn/tag/hyperdrive/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[队列](https://blog.cloudflare.com/zh-cn/tag/queues/)
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



[Hyperdrive](https://blog.cloudflare.com/zh-cn/tag/hyperdrive/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[队列](https://blog.cloudflare.com/zh-cn/tag/queues/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[D1](https://blog.cloudflare.com/zh-cn/tag/d1/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Hyperdrive](https://blog.cloudflare.com/zh-cn/tag/hyperdrive/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[队列](https://blog.cloudflare.com/zh-cn/tag/queues/)

2024年4月1日

# 使用正式发布的 D1 以及 Hyperdrive、Queues 和 Workers Analytics Engine 更新，简化状态管理

![Rita Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4775C0A7PYM3T9XKH4PH9J.png&w=64&h=64&f=webp&fit=cover&position=center)![Matt Silverlock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492M11VMJ0WCWAND287DEN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Rita Kozlov](https://blog.cloudflare.com/zh-cn/author/rita/)和[Matt Silverlock](https://blog.cloudflare.com/zh-cn/author/silverlock/)

阅读时间：8 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/making-full-stack-easier-d1-ga-hyperdrive-queues/)、[Deutsch](https://blog.cloudflare.com/de-de/making-full-stack-easier-d1-ga-hyperdrive-queues/)、[Español](https://blog.cloudflare.com/es-es/making-full-stack-easier-d1-ga-hyperdrive-queues/)、[Français](https://blog.cloudflare.com/fr-fr/making-full-stack-easier-d1-ga-hyperdrive-queues/)、[日本語](https://blog.cloudflare.com/ja-jp/making-full-stack-easier-d1-ga-hyperdrive-queues/)、[한국어](https://blog.cloudflare.com/ko-kr/making-full-stack-easier-d1-ga-hyperdrive-queues/)和[繁體中文](https://blog.cloudflare.com/zh-tw/making-full-stack-easier-d1-ga-hyperdrive-queues/).

![BLOG-2364 Embedded Image - fDxNpJ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HYDH0RZZC9WHRKRSM26Y.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f398vLy7Ozt7+/w9PT18/Ty7O3p/////f//7vD15Obv5+nz7/H38fP17e/s////////6+/53uHz4eX27O/78fT47vLw////////7vL93+P44ub77vL/9Pj98vb0////////9vn/6e396+//9vr/+/7/+Pz5////////////9/r/+vz////////////9////////////////////////////////////////////////////////////////)

### 让全栈开发更简单

虽然今天是愚人节，而且我们也和其他人一样喜欢玩乐，但我们希望在今天发布一些严肃的公告。事实上，截至今天，已有超过 200 万开发者在 Cloudflare 平台上进行开发——这绝对不是开玩笑！

作为本届 Developer Week 的序幕，我们宣布三个产品进入“生产就绪”状态： [D1 ——我们的无服务器 SQL 数据库](https://developers.cloudflare.com/d1/)；[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)——使您的_现有_数据库运行犹如分布式（而且更快！）；以及 [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)——我们的时间序列数据库。

一段时间以来，我们一直致力于让开发人员将他们的整个技术栈迁移到 Cloudflare 上，但在 Cloudflare 上构建的应用程序会是什么样子呢?

这个图表本身看起来应该与您已经熟悉的工具没有太大差异：您需要一个[数据库](https://developers.cloudflare.com/d1/)用于存储核心用户数据。[对象存储](https://developers.cloudflare.com/r2/)用于存储资产和用户内容。也许一个[队列](https://developers.cloudflare.com/queues/)用于处理后台任务，例如电子邮件或上传处理。一个[快速键值存储](https://developers.cloudflare.com/kv/)用于运行时配置。也许甚至一个[时间序列数据库](https://developers.cloudflare.com/analytics/analytics-engine/)聚合用户事件和/或性能数据。我们甚至还没有涉及到 [AI（人工智能）](https://developers.cloudflare.com/workers-ai/)——它正日益成为许多应用程序在搜索、推荐和/或图像分析任务（最低限度！）中的一个核心部分。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2364 Embedded Image - aTgEZg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW479EMR1AFCVACFCMNEZBTB.png&w=715&h=365&f=webp&fit=cover&position=center)

而且，无需多想，这种架构需要运行在全球范围内，意味着它是可扩展、可靠和快速的，全部开箱即用。

### D1 ****正式版：生产就绪****

核心数据库是基础设施中最关键的组成部分之一。它需要高度可靠，不能丢失数据，需要能够扩展。因此，在过去的一年里，我们一直全力以赴使 D1 达到生产就绪状态。现在，我们隆重宣布 D1 —— [我们的全球、无服务器 SQL 数据库](https://developers.cloudflare.com/d1/) —— 现在已经正式发布。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2296 Embedded Image - awnaGg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45EJA1JGK06GE1ACZ10FHD.png&w=715&h=283&f=webp&fit=cover&position=center)

D1 的正式发布带来了一些备受期待的功能，包括：

  * 支持 10 GB 数据库——以及每个账户 5 万个数据库；
  * 全新数据导出功能；以及
  * 增强查询调试功能（我们称之为“D1 Insights”）——以便您了解哪些查询消耗了最多的时间、成本，或者哪些查询效率低下……



……旨在赋能开发人员以利用 D1 构建满足其所有关系型 SQL 需求的生产就绪应用程序。而且重要的是，在“免费计划”或“爱好型计划”显然面临风险的情况下，我们无意取消 D1 的免费级，也不打算降低 5 美元/月 Workers Paid 计划包含的 _250 亿行读取_配额：

计划

Plan| Rows Read| Rows Written| Storage  
---|---|---|---  
Workers Paid| First 25 billion / month included  
  
\+ $0.001 / million rows| First 50 million / month included  
  
\+ $1.00 / million rows| First 5 GB included  
\+ $0.75 / GB-mo  
Workers Free| 5 million / day| 100,000 / day | 5 GB (total)  
  
读取行数

写入行数

存储
    
    
    export default {
      async fetch(request: Request, env: Env) {
        const {pathname} = new URL(request.url);
        let resp = null;
        let session = env.DB.withSession(token); // An optional commit token or mode
    
        // Handle requests within the session.
        if (pathname === "/api/orders/list") {
          // This statement is a read query, so it will work against any
          // replica that has a commit equal or later than `token`.
          const { results } = await session.prepare("SELECT * FROM Orders");
          resp = Response.json(results);
        } else if (pathname === "/api/orders/add") {
          order = await request.json();
    
          // This statement is a write query, so D1 will send the query to
          // the primary, which always has the latest commit token.
          await session.prepare("INSERT INTO Orders VALUES (?, ?, ?)")
            .bind(order.orderName, order.customer, order.value);
            .run();
    
          // In order for the application to be correct, this SELECT
          // statement must see the results of the INSERT statement above.
          //
          // D1's new Session API keeps track of commit tokens for queries
          // within the session and will ensure that we won't execute this
          // query until whatever replica we're using has seen the results
          // of the INSERT.
          const { results } = await session.prepare("SELECT COUNT(*) FROM Orders")
            .run();
          resp = Response.json(results);
        }
    
        // Set the token so we can continue the session in another request.
        resp.headers.set("x-d1-token", session.latestCommitToken);
        return resp;
      }
    }

Workers Paid

包含 250 亿行/月

\+ 0.001 美元/百万行

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2364 Embedded Image - JgQNPX](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GHX0J9GWSTXQJJ84R6B3.png&w=715&h=257&f=webp&fit=cover&position=center)

包含 5000 万行/月

\+ 1.00 美元/百万行

包含 5 GB
    
    
    // Use the popular 'pg' driver? Easy. Hyperdrive just exposes a connection string
    // to your Worker.
    const client = new Client({ connectionString: env.HYPERDRIVE.connectionString });
    await client.connect();
    
    // Prefer using an ORM like Drizzle? Use it with Hyperdrive too.
    // https://orm.drizzle.team/docs/get-started-postgresql#node-postgres
    const client = new Client({ connectionString: env.HYPERDRIVE.connectionString });
    await client.connect();
    const db = drizzle(client);

+0.75 美元/GB/月

Workers Free

500 万/日

Plan| Price per query| Connection Pooling  
---|---|---  
Workers Paid| $0 | $0  
  
100,000 /日

5 GB（总计）

 _如果您从一开始就关注 D1：这与我们在[公开测试版](https://blog.cloudflare.com/d1-open-beta-is-here)时宣布的价格一致_

但正式发布并不意味着我们的工作停顿下来：我们计划为 D1 推出一些重大全新功能，包括全球读复制，甚至更大的数据库，更多 [Time Travel](https://developers.cloudflare.com/d1/reference/time-travel/) 功能，以便您对数据库进行分支；以及用于动态查询和/或从 Worker 中动态创建新数据库的全新 API。
    
    
    // Pull and acknowledge messages from a Queue using any HTTP client
    $  curl "https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull" -X POST --data '{"visibilityTimeout":10000,"batchSize":100}}' \
         -H "Authorization: Bearer ${QUEUES_TOKEN}" \
         -H "Content-Type:application/json"
    
    // Ack the messages you processed successfully; mark others to be retried.
    $ curl "https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/ack" -X POST --data '{"acks":["lease-id-1", "lease-id-2"],"retries":["lease-id-100"]}' \
         -H "Authorization: Bearer ${QUEUES_TOKEN}" \
         -H "Content-Type:application/json"

D1 的读复制会根据需要自动部署读副本，使数据更靠近您的用户：而且无需您启动或管理扩展，也不会遇到一致性（复制滞后）问题。让我们提前一窥 D1 即将推出的 Replication API 是什么模样：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2364 Embedded Image - wugVmp](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45B7NBF5P56KNNM3F230EK.png&w=715&h=238&f=webp&fit=cover&position=center)

重要的是，我们将使开发人员能够维持基于会话的一致性，以便用户既能看到自己的更改得到反映，同时仍然能够享受复制带来的性能和延迟优势。
    
    
    // Apply a delay to a message when sending it
    await env.YOUR_QUEUE.send(msg, { delaySeconds: 3600 })
    
    // Delay a message (or a batch of messages) when marking it for retry
    for (const msg of batch.messages) {
    	msg.retry({delaySeconds: 300})
    } 

如需进一步了解 D1 读复制的底层工作原理，欢迎阅读[我们的深入探讨文章](https://blog.cloudflare.com/building-d1-a-global-database/)。如果您希望立即开始使用 D1 进行构建，请[浏览我们的开发人员文档](https://developers.cloudflare.com/d1/)以创建您的第一个数据库。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2364 Embedded Image - QLnQH8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44J0FZR4G6X03ET7QNEKRJ.png&w=715&h=161&f=webp&fit=cover&position=center)

### Hyperdrive: ****正式发布****

我们在[去年 9 月的生日周](https://blog.cloudflare.com/hyperdrive-making-regional-databases-feel-distributed)期间推出 Hyperdrive 的公测版，现已正式发布，换句话说，这个产品经过实战测试并已生产就绪。

如果您还不了解 Hyperdrive 是什么，它旨在使您已有的中心化数据库给人分布式的感觉。我们使用我们的[全球网络](https://www.cloudflare.com/network/)来获得到您的数据库的更快路径，保持连接池处于最佳状态，并在尽可能接近用户的地方缓存您最频繁执行的查询。

重要的是，Hyperdrive 开箱就支持最流行的驱动程序和 ORM（对象关系映射）库，因而您无需重新学习或重写您的查询：

但是有关 Hyperdrive 的工作不会因为正式发布而停下来。接下来的几个月内，我们将为_另一个_部署最广泛的数据库引擎提供支持：MySQL。我们还将支持通过 [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) 和 [Magic WAN](https://developers.cloudflare.com/magic-wan/) 连接到专用网络（包括云 VPC 网络）内的数据库。除此之外，我们计划推出围绕失效和缓存策略的配置选项，以便您能就性能与数据新鲜度做出更细致的决策。

当我们考虑如何为 Hyperdrive 定价时，我们意识到对其收费似乎并不合适。毕竟，Hyperdrive 不仅带来显著的的性能提升，而且对于连接传统数据库引擎至关重要。如果没有 Hyperdrive，每个连接和查询数据库的请求都需要支付 6 次以上往返的延迟开销，这样做显然是不合理的。

因此，我们很高兴地宣布：**对于任何订阅 Workers Paid 计划的开发人员，Hyperdrive 均免费使用** 。 这包括查询缓存和连接池，以及创建多个 Hyperdrive 的能力——以区分不同的应用程序、生产环境与测试环境，或提供不同的配置（例如，缓存与不缓存）。

Plan| Data points written| Read queries  
---|---|---  
Workers Paid| 10 million included per month  
+$0.25 per additional million| 1 million included per month  
+$1.00 per additional million  
Workers Free| 100,000 included per day| 10,000 included per day  
  
计划

每次查询的价格

连接池

Workers Paid

$0 

$0

要开始使用 Hyperdrive，请[查看文档](https://developers.cloudflare.com/hyperdrive/)以了解如何连接您的现有数据库并开始从您的 Workers 进行查询。

### Queues：从任何地方拉取

对于构建现代全栈应用而言，任务队列是越来越关键的一个部分。这正是我们[最初宣布](https://blog.cloudflare.com/cloudflare-queues-open-beta)推出 [Queues](https://developers.cloudflare.com/queues/) 公测时所考虑的因素。自那以后，我们一直在开发几个重要的 Queues 特性，并在本周推出其中的两个：基于拉取的消费者和新的消息传递控制。

任何支持HTTP的客户端[现在都可以从一个队列中拉取消息](https://developers.cloudflare.com/queues/reference/pull-consumers/)：调用一个队列的新 /pull 端点以请求一批消息，并在成功处理每条消息（或每批消息）后调用 /ack 端点以进行确认：

基于拉取的消费者可以在任何地方运行，允许您与现有的传统云基础设施一同运行队列消费者。Cloudflare的内部团队很早就采用了这种方式，其中一个用例专注于从我们的 [310+数据中心](https://www.cloudflare.com/network/)写入设备遥测数据到队列，并在一些在Kubernetes上运行的后台基础设施中进行消费。重要的是，我们全球分布的队列基础设施意味着消息保留在队列中，直到消费者准备好处理它们。

Queues [现在也支持推迟消息](https://developers.cloudflare.com/queues/reference/batching-retries/#delay-messages)， 包括在发送到队列时和在标记消息以便重试时。这个功能适用于为将来对任务进行排队，以及如果上游 API 或基础设施有速率限制，需要您控制处理消息的速度，用于应用退避机制。

在未来几个月中，我们还将大幅提高每个队列的吞吐量，以便将 Queues 到正式发布。对我们来说，Queues 的 _高度_可靠性非常重要：丢失或掉落的消息意味着用户收不到订单确认邮件，密码重置通知，和/或他们的上传未被处理的反馈——每一种情况都会对用户产生影响且难以恢复。

### Workers Analytics Engine ****正式发布****

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) 通过内置 API 从 Workers 写入数据点，并通过 SQL API 查询那些数据，提供了大规模的无限基数分析。

Workers Analytics Engine 背后是 Cloudflare 已经依赖多年、基于 ClickHouse 的系统。我们用它来观察自己服务的健康状况，捕获产品使用数据进行计费，以及回答有关特定客户使用模式的问题。几乎每一个对 Cloudflare 网络的请求都会向这个系统写入至少一个数据点。Workers Analytics Engine 让您可以使用同样的基础设施构建自己的自定义分析，同时我们为您管理那些困难的部分。

自从[推出测试版](https://blog.cloudflare.com/workers-analytics-engine)以来， 从大型企业到诸如 [Counterscale](https://github.com/benvinegar/counterscale/) 的开源项目，开发人员都开始依赖 Workers Analytics Engine 来处理这些相同的用例以及其他。Workers Analytics Engine 已经以生产规模运行了数年，处理任务关键性工作负载 —— 但直到今天，我们还没有分享过任何关于定价的信息。

我们使 Workers Analytics Engine 的定价保持简单，基于两个指标：

  1. ****写入数据点**** —— 每次在一个 Worker 中调用 [writeDataPoint()](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#3-write-data-from-your-worker)，都会算作写入一个数据点。每个数据点的成本相同 —— 与其他平台不同，我们不会因为增加维度或基数而额外收费，也不需要预测压缩数据点的大小和成本可能是—多少。
  2. ****读取查询**** —— 每次向 Workers Analytics Engine [SQL API](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/) 发出 POST 请求，就算作一次读查询。每次查询的成本相同 —— 与其他平台不同，我们不会因为查询复杂性而额外收费，也不需要考虑每次查询将读取的数据行数。



Workers Free 和 Workers Paid 都将包括一定数量的数据点写入和读取查询，额外使用量的定价如下：

计划

写入数据点

读取查询

Workers Paid

包含 1000 万/月

\+ 0.25 美元/每增加 100 万

包含 1000 万/月

+1.00 美元/每增加 100 万

Workers Free

包含 10 万/日

包含 1 万/日

根据这一定价，通过计算在 Worker 中调用函数的次数，以及向 HTTP API 端点发出请求的次数，即可回答 “Workers Analytics Engine 会花费我多少钱？” 的问题。计算简单明了，无需使用电子表格。

这一定价将在未来几个月内向所有人开放。在那以前，Workers Analytics Engine 继续免费提供使用。您[今天就可以开始从 Worker 中写入数据点](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#limits) ——只需要短短几分钟，不到 10 行代码，即可开始捕获数据。我们期待听到您的反馈。

### **本周才刚刚开始**

欢迎关注我们将在 Developer Week 第二天为您准备的精彩内容。如有任何问题，或者希望展示您已经构建的炫酷作品，欢迎加入我们的 [_Discord_](https://discord.cloudflare.com/) 服务器。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-full-stack-easier-d1-ga-hyperdrive-queues%2F&t=%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%E7%9A%84%20D1%20%E4%BB%A5%E5%8F%8A%20Hyperdrive%E3%80%81Queues%20%E5%92%8C%20Workers%20Analytics%20Engine%20%E6%9B%B4%E6%96%B0%EF%BC%8C%E7%AE%80%E5%8C%96%E7%8A%B6%E6%80%81%E7%AE%A1%E7%90%86)[](https://x.com/intent/post?text=%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%E7%9A%84+D1+%E4%BB%A5%E5%8F%8A+Hyperdrive%E3%80%81Queues+%E5%92%8C+Workers+Analytics+Engine+%E6%9B%B4%E6%96%B0%EF%BC%8C%E7%AE%80%E5%8C%96%E7%8A%B6%E6%80%81%E7%AE%A1%E7%90%86&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-full-stack-easier-d1-ga-hyperdrive-queues%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-full-stack-easier-d1-ga-hyperdrive-queues%2F)[](https://bsky.app/intent/compose?text=%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%E7%9A%84+D1+%E4%BB%A5%E5%8F%8A+Hyperdrive%E3%80%81Queues+%E5%92%8C+Workers+Analytics+Engine+%E6%9B%B4%E6%96%B0%EF%BC%8C%E7%AE%80%E5%8C%96%E7%8A%B6%E6%80%81%E7%AE%A1%E7%90%86+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-full-stack-easier-d1-ga-hyperdrive-queues%2F)[](https://mastodonshare.com/?text=%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%E7%9A%84+D1+%E4%BB%A5%E5%8F%8A+Hyperdrive%E3%80%81Queues+%E5%92%8C+Workers+Analytics+Engine+%E6%9B%B4%E6%96%B0%EF%BC%8C%E7%AE%80%E5%8C%96%E7%8A%B6%E6%80%81%E7%AE%A1%E7%90%86&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-full-stack-easier-d1-ga-hyperdrive-queues%2F)[](https://www.threads.net/intent/post?text=%E4%BD%BF%E7%94%A8%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%E7%9A%84+D1+%E4%BB%A5%E5%8F%8A+Hyperdrive%E3%80%81Queues+%E5%92%8C+Workers+Analytics+Engine+%E6%9B%B4%E6%96%B0%EF%BC%8C%E7%AE%80%E5%8C%96%E7%8A%B6%E6%80%81%E7%AE%A1%E7%90%86+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-full-stack-easier-d1-ga-hyperdrive-queues%2F)

## 相关标签

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[D1](https://blog.cloudflare.com/zh-cn/tag/d1/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Hyperdrive](https://blog.cloudflare.com/zh-cn/tag/hyperdrive/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[队列](https://blog.cloudflare.com/zh-cn/tag/queues/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
