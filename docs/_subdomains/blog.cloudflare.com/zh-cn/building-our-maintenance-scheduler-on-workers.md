---
url: https://blog.cloudflare.com/zh-cn/building-our-maintenance-scheduler-on-workers/
title: Workers \u5982\u4f55\u4e3a\u6211\u4eec\u7684\u5185\u90e8\u7ef4\u62a4\u8c03\u5ea6\u6d41\u7a0b\u63d0\u4f9b\u652f\u6301 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:45:14.434378+00:00
---

# Workers 如何为我们的内部维护调度流程提供支持 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/building-our-maintenance-scheduler-on-workers/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Prometheus](https://blog.cloudflare.com/zh-cn/tag/prometheus/)[可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)+1再显示 1 个标签

4 个标签显示 4 个标签

  * 文章标签
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Prometheus](https://blog.cloudflare.com/zh-cn/tag/prometheus/)[可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)[基础设施](https://blog.cloudflare.com/zh-cn/tag/infrastructure/)
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



[基础设施](https://blog.cloudflare.com/zh-cn/tag/infrastructure/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Prometheus](https://blog.cloudflare.com/zh-cn/tag/prometheus/)[可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)[基础设施](https://blog.cloudflare.com/zh-cn/tag/infrastructure/)

2025年12月22日

# Workers 如何为我们的内部维护调度流程提供支持

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/zh-cn/author/kevin-deems/)和[Michael Hoffmann](https://blog.cloudflare.com/zh-cn/author/michael-hoffmann/)

阅读时间：10 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/building-our-maintenance-scheduler-on-workers/)、[日本語](https://blog.cloudflare.com/ja-jp/building-our-maintenance-scheduler-on-workers/)、[한국어](https://blog.cloudflare.com/ko-kr/building-our-maintenance-scheduler-on-workers/)和[繁體中文](https://blog.cloudflare.com/zh-tw/building-our-maintenance-scheduler-on-workers/).

![BLOG-3017 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MH5G11Z4TPXRMZT8FJXD.png&w=1016&h=635&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAO1yFQGCLTWmWWXWgX36jXH2gT3OaPWWUQ2mQU3OWbIakeZSydpe5aJC3WIOrT3eeS3acYoSjhJ6zk67Ei63OdKHLYZK8XoepT3+nao+tkKq9oLvOl7nYfqvVaZrGZpCxUIOuapGzj6rAobnNmrjVhKrTbpvFZZG0TYKyY4y1hKC9l63Flq3JhqPGcJW9XYy0Sn+zWYa1dZO5ip27kJ+6hpm3cI60U4SySH6zVYO1boy3g5W2jJmzhpWwcIuvT4Cx)

Cloudflare 在全球超过 [_330 个城市设有数据中心_](https://www.cloudflare.com/network/)，因此您可能会认为我们在计划进行数据中心操作时，随时可以轻松中断其中几个而不被用户察觉。然而，现实情况是，[ _破坏性维护_](https://developers.cloudflare.com/support/disruptive-maintenance/)需要精心规划，而且随着 Cloudflare 的发展，通过我们的基础设施和网络运营专家之间的手动协调来管理这些复杂性几乎变得不可能。

人类已无法实时跟踪每一个重叠的维护请求，也无法兼顾特定于每一个客户的路由规则。我们达到了一个临界点：单靠人工监督已不足以保证，在世界某地进行的例行硬件更新不会意外地与另一地的关键路径发生冲突。

我们意识到，需要一个集中化、自动化的“大脑”来充当保障——一个能够同时洞察整个网络状态的系统。通过在 [_Cloudflare Workers_](https://workers.cloudflare.com/) 上构建这一调度器，我们创造了一种以编程方式强制执行安全约束的方法，确保无论我们推进速度多快，都不会牺牲客户所依赖服务的可靠性。

在这篇博客文章中，我们将解释它的构建过程，并分享目前的成果。

## 构建系统，以降低关键维护操作的风险

设想一台边缘路由器，它是连接公共互联网与某个大都市区域内众多 Cloudflare 数据中心的冗余网关小组中的一员。在人口密集的城市，我们必须确保位于这一小群路由器背后的多个数据中心不会因为所有路由器同时下线而被切断连接。

另一个维护挑战来自我们的 Zero Trust 产品 Dedicated CDN Egress IPs。它允许客户选择特定的数据中心，让用户的流量从这些数据中心离开 Cloudflare，并发送到地理位置靠近的源服务器，以实现低延迟。（为简洁起见，在本文中我们将该产品称为“Aegis”，这是它之前的名称。）如果客户所选的所有数据中心同时下线，他们将会遇到更高的延迟，甚至可能出现 5xx 错误，而我们必须避免这种情况。

我们的维护调度器解决了类似这样的问题。我们可以确保在某一区域内始终至少有一台边缘路由器处于活跃状态；并且在安排维护时，能够判断多个预定事件的组合是否会导致某客户的 Aegis 池中所有数据中心同时下线。

在创建调度器之前，这些同时发生的破坏性事件可能导致客户的服务中断。而现在，调度器会向内部运维人员提示潜在冲突，使我们能够提议新的时间，以避免与其他相关的数据中心维护事件重叠。

我们将这些运营场景（例如边缘路由器的可用性以及客户规则）定义为维护约束，这让我们能够规划更可预测且更安全的维护。

## 维护约束

每个约束都始于一组提议的维护项目，例如一台网络路由器或一组服务器。接着，我们会查找日历中所有与提议的维护时间窗口重叠的维护事件。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45N24BK9S5N2GJ6VGMRCGQ.png&w=715&h=385&f=webp&fit=cover&position=center)

然后，我们聚合各类产品 API，例如 Aegis 客户 IP 池列表。Aegis 会返回一组 IP 范围，这些范围对应客户要求从其特定数据中心 ID 发出流量的位置，如下图所示。
    
    
    [
        {
          "cidr": "104.28.0.32/32",
          "pool_name": "customer-9876",
          "port_slots": [
            {
              "dc_id": 21,
              "other_colos_enabled": true,
            },
            {
              "dc_id": 45,
              "other_colos_enabled": true,
            }
          ],
          "modified_at": "2023-10-22T13:32:47.213767Z"
        },
    ]

在该场景中，数据中心 21 和数据中心 45 是相互关联的，因为对于 Aegis 客户 9876 来说，我们需要至少一个数据中心保持在线，以便其能够从 Cloudflare 接收出口流量。如果我们试图同时关闭数据中心 21 和 45，调度协调器就会提醒我们，该客户的工作负载将因此受到意外影响。

最初我们尝试了一个简单的方案：将所有数据加载到单个 Worker 中。这包括所有服务器关联关系、产品配置，以及用于计算约束的产品和基础设施健康指标。但只是在概念验证阶段，我们就遇到了“内存不足”的错误。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44X5J4KQRSH4Q5YRX5JNQC.png&w=715&h=226&f=webp&fit=cover&position=center)

我们需要更加注意 Workers 的[ _平台限制_](https://developers.cloudflare.com/workers/platform/limits/)。这就要求仅加载处理约束业务逻辑所绝对必需的数据。如果收到德国法兰克福某台路由器的维护请求，我们几乎可以肯定不需要关心澳大利亚的情况，因为跨区域之间没有关联。因此，我们只应加载德国邻近数据中心的相关数据。我们需要一种更高效的方法来处理数据集中的关联关系。

## 在 Workers 上进行图处理

在分析约束时，我们发现一种规律：每个约束本质上可归结为两个概念——对象与关联。在图论中，这两类组件分别称为顶点 (vertices) 和边 (edges)。对象可以是网络路由器，而关联则可以是该数据中心内要求路由器保持在线的一组 Aegis 池。我们从 Facebook 的 [_TAO_](https://research.facebook.com/publications/tao-facebooks-distributed-data-store-for-the-social-graph/) 研究论文中获得启发，在产品与基础设施数据之上建立了一套图接口。API 示例如下：
    
    
    type ObjectID = string
    
    interface MainTAOInterface<TObject, TAssoc, TAssocType> {
      object_get(id: ObjectID): Promise<TObject | undefined>
    
      assoc_get(id1: ObjectID, atype: TAssocType): AsyncIterable<TAssoc>
    }

核心理念在于，关联是有类型的。例如，约束会调用图接口来获取 Aegis 产品数据。
    
    
    async function constraint(c: AppContext, aegis: TAOAegisClient, datacenters: string[]): Promise<Record<string, PoolAnalysis>> {
      const datacenterEntries = await Promise.all(
        datacenters.map(async (dcID) => {
          const iter = aegis.assoc_get(c, dcID, AegisAssocType.DATACENTER_INSIDE_AEGIS_POOL)
          const pools: string[] = []
          for await (const assoc of iter) {
            pools.push(assoc.id2)
          }
          return [dcID, pools] as const
        }),
      )
    
      const datacenterToPools = new Map<string, string[]>(datacenterEntries)
      const uniquePools = new Set<string>()
      for (const pools of datacenterToPools.values()) {
        for (const pool of pools) uniquePools.add(pool)
      }
    
      const poolTotalsEntries = await Promise.all(
        [...uniquePools].map(async (pool) => {
          const total = aegis.assoc_count(c, pool, AegisAssocType.AEGIS_POOL_CONTAINS_DATACENTER)
          return [pool, total] as const
        }),
      )
    
      const poolTotals = new Map<string, number>(poolTotalsEntries)
      const poolAnalysis: Record<string, PoolAnalysis> = {}
      for (const [dcID, pools] of datacenterToPools.entries()) {
        for (const pool of pools) {
          poolAnalysis[pool] = {
            affectedDatacenters: new Set([dcID]),
            totalDatacenters: poolTotals.get(pool),
          }
        }
      }
    
      return poolAnalysis
    }

在上面的代码中，我们使用了两种关联类型：

  1. DATACENTER_INSIDE_AEGIS_POOL，用于检索数据中心所在的 Aegis 客户池。
  2. AEGIS_POOL_CONTAINS_DATACENTER，用于检索 Aegis 池为流量提供服务所需的数据中心。



这两种关联互为反向索引。访问模式与之前完全相同，但现在图实现能更好地控制查询的数据量。以前我们需要将所有 Aegis 池加载到内存中，并在约束业务逻辑里进行过滤；现在我们可以直接获取与应用相关的数据。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46V747SXCQBJ3NZGGBWH72.png&w=715&h=313&f=webp&fit=cover&position=center)

该接口的强大之处在于，图实现可以在后台优化性能，而不会让业务逻辑变得更复杂。这让我们可以利用 Workers 的可扩展性以及 Cloudflare CDN 的优势，从内部系统中非常快速地获取数据。

## 获取管道

我们切换到使用新的图实现后，开始发送更具针对性的 API 请求。响应大小在一夜之间减少了 100 倍——从加载少数几个巨大的请求变为加载许多微小的请求。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48J28W9JDW5V667ENB9QRH.png&w=715&h=344&f=webp&fit=cover&position=center)

虽然这解决了一次性加载过多数据导致内存不足的问题，但我们又遇到了子请求数量过多的新问题。因为现在我们不再发起少量大型 HTTP 请求，而是发起数量级更多的微小请求，结果很快就持续突破了 Workers 的子请求限制。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45SB0HD85RBHA7KBXDD3TD.png&w=715&h=346&f=webp&fit=cover&position=center)

为了解决这个问题，我们在图实现和 `fetch` API 之间构建了一个智能中间件层。
    
    
    export const fetchPipeline = new FetchPipeline()
      .use(requestDeduplicator())
      .use(lruCacher({
        maxItems: 100,
      }))
      .use(cdnCacher())
      .use(backoffRetryer({
        retries: 3,
        baseMs: 100,
        jitter: true,
      }))
      .handler(terminalFetch);

如果您熟悉 Go 语言，可能见过 [_singleflight_](https://pkg.go.dev/golang.org/x/sync/singleflight) 包。我们借鉴了这个思路，在获取管道中的第一个中间件组件实现了对正在进行的 HTTP 请求去重，让同一 Worker 内的重复请求都等待同一个 Promise 返回数据，而不是产生重复的请求。接下来，我们使用轻量级的最近最少使用 (LRU) 缓存，在内部缓存已经请求过的数据。

完成这两项操作后，我们使用 Cloudflare 的 `caches.default.match` 函数缓存 Worker 运行所在区域的所有 GET 请求。由于我们有多个性能特征各异的数据源，因此我们谨慎地选择生存时间 (TTL) 值。例如，实时数据仅缓存 1 分钟。相对静态的基础设施数据可以根据数据类型缓存 1 到 24 小时。电源管理数据可能需要手动更改且更改频率较低，因此我们可以将其在边缘端缓存更长时间。

除了上述层级外，我们还加入了标准的指数退避 (exponential backoff)、重试 (retries) 和抖动 (jitter) 机制。这有助于减少因下游资源临时不可用而产生的无效 `fetch` 调用。通过适度退避，我们提高了下一次成功获取数据的概率；反之，如果 Worker 持续不断发送请求而不退避，当源站返回 5xx 错误时很容易突破子请求限制。

综合这些措施后，我们实现了约 99% 的缓存命中率。[ _缓存命中率_](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)是指直接从 Cloudflare 快速缓存内存（命中）返回数据的 HTTP 请求，相对于需要从控制平面数据源（未命中）发起较慢请求的百分比，计算公式为 (命中数/(命中数 + 未命中数))。高命中率意味着更好的 HTTP 请求性能和更低的成本，因为在 Worker 中从缓存查询数据的速度比从位于不同区域的源服务器获取数据快一个数量级。经过调优内存缓存和 CDN 缓存的设置后，命中率大幅提升。由于我们的工作负载很多是实时的，命中率永远达不到 100%，因为我们每分钟至少需要请求一次最新数据。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44RXG38NESXHB4QMTCNP2J.png&w=715&h=691&f=webp&fit=cover&position=center)

我们已经讨论了如何改进获取层，但尚未说明如何让源站的 HTTP 请求更快。我们的维护调度器需要实时响应网络降级和数据中心机器故障。为此，我们使用分布式 [_Prometheus_](https://blog.cloudflare.com/how-cloudflare-runs-prometheus-at-scale/) 查询引擎 Thanos，将边缘的高性能指标传递到调度器中。

## 实时 Thanos

为了说明采用图处理接口如何影响实时查询，我们来看一个例子。要分析边缘路由器的健康状况，原本我们会发送如下查询：
    
    
    sum by (instance) (network_snmp_interface_admin_status{instance=~"edge.*"})

最初，我们向存储 Prometheus 指标的 Thanos 服务请求每个边缘路由器的当前健康状况列表，并在 Worker 中手动筛选与维护相关的路由器。这种方法有很多不足之处。例如，Thanos 返回的响应大小高达数 MB，需要进行解码和编码。Worker 也需要缓存和解码这些大型 HTTP 响应，以便在处理特定维护请求时过滤掉大部分数据。由于 TypeScript 是单线程的，而解析 JSON 数据又受 CPU 限制，发送两个大型 HTTP 请求意味着一个请求会被阻塞，等待另一个请求完成解析。

现在我们改为直接使用图来查找有针对性的关联关系，例如边缘路由器与骨干路由器之间的接口链路，用 `EDGE_ROUTER_NETWORK_CONNECTS_TO_SPINE` 表示。
    
    
    sum by (lldp_name) (network_snmp_interface_admin_status{instance=~"edge01.fra03", lldp_name=~"spine.*"})

结果平均只有 1 KB，而不是数 MB，大约缩小了 1000 倍。这也大幅降低了 Worker 内部的 CPU 消耗，因为我们把大部分反序列化工作交给 Thanos 完成。正如前面所说，这意味着我们需要发起更多的小请求，但 Thanos 前的负载平衡器可以将请求均匀分散，从而提高这种用例的吞吐量。

我们的图实现与获取管道成功控制了成千上万个微小实时请求形成的“惊群效应”(thundering herd)。不过，历史分析带来了不同的 I/O 挑战——我们不再只是获取小而具体的关联关系，而是要扫描数月的数据来发现冲突的维护窗口。过去，Thanos 会对我们的对象存储 R2 发起大量随机读取，造成巨大带宽开销。为了解决这一问题又不损失性能，我们采用了 Observability 团队今年内部开发的新方法。

## 历史数据分析

我们有足够多的维护用例，必须依赖历史数据来判断我们的解决方案是否准确，以及能否随 Cloudflare 网络的扩展而扩展。我们既不想引发事故，也不希望不必要地阻碍已计划的物理维护。为了在这两个目标之间取得平衡，我们可以利用两月前甚至一年前的维护事件时间序列数据，来分析某类维护事件违反我们约束（例如边缘路由器可用性、Aegis 相关规则）的频率。今年早些时候，我们曾在博客中介绍过利用 Thanos [_自动向边缘发布及回滚软件_](https://blog.cloudflare.com/safe-change-at-any-scale/)的做法。

Thanos 主要将数据查询分发到 Prometheus，但当 Prometheus 的数据保留期不足以回答查询时，就不得不从对象存储（在我们的案例中为 R2）下载数据。Prometheus 的 TSDB 块最初是为本地 SSD 设计的，依赖随机访问模式，这在迁移到对象存储后会成为瓶颈。当我们的调度器需要分析数月的维护历史数据以识别冲突约束时，从对象存储进行随机读取会带来巨大的 I/O 开销。为解决此问题，我们实现了一个转换层，将这些 TSDB 块转换为 [_Apache Parquet_](https://parquet.apache.org/) 文件。Parquet 是一种面向大数据分析的原生列式存储格式，按列而非按行组织数据，并结合丰富的统计信息，使我们可以只获取所需的部分数据。

此外，由于我们将 TSDB 块重写为 Parquet 文件，还可以按支持少量大块依序读取数据的方式存储数据。
    
    
    sum by (instance) (hmd:release_scopes:enabled{dc_id="45"})

在上面的示例中，我们将选择元组“(__name__, dc_id)”作为主要排序键，以便名称为“hmd:release_scopes:enabled”且“dc_id”值相同的指标能够被排到一起。

我们的 Parquet 网关现在会发起精确的 R2 区间请求，仅提取与查询相关的特定列。这将有效载荷从数 MB 减少到数 KB。而且因为这些文件段是不可变的，我们可以在 Cloudflare CDN 上积极缓存它们。

这使 R2 变成了低延迟的查询引擎，让我们可以即时针对长期趋势回测复杂的维护场景，避免了原 TSDB 格式下的超时和高尾延迟问题。下图展示了一次近期的负载测试，结果显示在相同查询模式下，Parquet 的 P90 性能最高可达旧系统的 15 倍。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BX8FVSJG36HNQHC5YCNS.png&w=715&h=222&f=webp&fit=cover&position=center)

如果想深入了解 Parquet 的实现原理，可以观看 PromCon EU 2025 上的演讲 [_Beyond TSDB: Unlocking Prometheus with Parquet for Modern Scale_](https://www.youtube.com/watch?v=wDN2w2xN6bA&list=PLoz-W_CUquUlHOg314_YttjHL0iGTdE3O&index=16)。

## 为扩展而构建

通过利用 Cloudflare Workers，我们从一套会因内存不足而崩溃的系统，演进为一个能智能缓存数据并使用高效可观测性工具实时分析产品与基础设施数据的系统。我们构建了一个能在网络增长与产品性能之间取得平衡的维护调度器。

但“平衡”是个动态目标。

每天，我们都在全球增加更多硬件，而要确保维护过程中不打断客户流量，其逻辑复杂度会随着产品种类和维护操作类型的增多呈指数级上升。我们已经攻克了第一阶段的挑战，但现在正面对只有在如此大规模下才会显现的更微妙、更复杂的问题。

我们需要不怕难题的工程师。加入我们的[ _基础设施团队_](https://www.cloudflare.com/careers/jobs/?department=Infrastructure)，和我们一起构建未来吧。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fbuilding-our-maintenance-scheduler-on-workers%2F&t=Workers%20%E5%A6%82%E4%BD%95%E4%B8%BA%E6%88%91%E4%BB%AC%E7%9A%84%E5%86%85%E9%83%A8%E7%BB%B4%E6%8A%A4%E8%B0%83%E5%BA%A6%E6%B5%81%E7%A8%8B%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8C%81)[](https://x.com/intent/post?text=Workers+%E5%A6%82%E4%BD%95%E4%B8%BA%E6%88%91%E4%BB%AC%E7%9A%84%E5%86%85%E9%83%A8%E7%BB%B4%E6%8A%A4%E8%B0%83%E5%BA%A6%E6%B5%81%E7%A8%8B%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8C%81&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://bsky.app/intent/compose?text=Workers+%E5%A6%82%E4%BD%95%E4%B8%BA%E6%88%91%E4%BB%AC%E7%9A%84%E5%86%85%E9%83%A8%E7%BB%B4%E6%8A%A4%E8%B0%83%E5%BA%A6%E6%B5%81%E7%A8%8B%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8C%81+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://mastodonshare.com/?text=Workers+%E5%A6%82%E4%BD%95%E4%B8%BA%E6%88%91%E4%BB%AC%E7%9A%84%E5%86%85%E9%83%A8%E7%BB%B4%E6%8A%A4%E8%B0%83%E5%BA%A6%E6%B5%81%E7%A8%8B%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8C%81&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://www.threads.net/intent/post?text=Workers+%E5%A6%82%E4%BD%95%E4%B8%BA%E6%88%91%E4%BB%AC%E7%9A%84%E5%86%85%E9%83%A8%E7%BB%B4%E6%8A%A4%E8%B0%83%E5%BA%A6%E6%B5%81%E7%A8%8B%E6%8F%90%E4%BE%9B%E6%94%AF%E6%8C%81+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fbuilding-our-maintenance-scheduler-on-workers%2F)

## 相关标签

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Prometheus](https://blog.cloudflare.com/zh-cn/tag/prometheus/)[可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)[基础设施](https://blog.cloudflare.com/zh-cn/tag/infrastructure/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
