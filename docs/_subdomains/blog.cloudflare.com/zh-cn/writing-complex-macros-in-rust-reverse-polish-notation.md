---
url: https://blog.cloudflare.com/zh-cn/writing-complex-macros-in-rust-reverse-polish-notation/
title: \u5728Rust\u4e2d\u7f16\u5199\u590d\u6742\u7684\u5b8f\uff1a\u9006\u6ce2\u5170\u5f0f | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:21.016297+00:00
---

# 在Rust中编写复杂的宏：逆波兰式 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/writing-complex-macros-in-rust-reverse-polish-notation/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Polish](https://blog.cloudflare.com/zh-cn/tag/cloudflare-polish/)[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)+1再显示 1 个标签

4 个标签显示 4 个标签

  * 文章标签
  * [Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)
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



[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

[Cloudflare Polish](https://blog.cloudflare.com/zh-cn/tag/cloudflare-polish/)[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

2018年1月31日

# 在Rust中编写复杂的宏：逆波兰式

![Ingvar Stepanyan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HXZCX2W0E3TV8QJY1YTY.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ingvar Stepanyan](https://blog.cloudflare.com/zh-cn/author/ingvar-stepanyan/)

阅读时间：7 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/writing-complex-macros-in-rust-reverse-polish-notation/)、[Deutsch](https://blog.cloudflare.com/de-de/writing-complex-macros-in-rust-reverse-polish-notation/)、[Español](https://blog.cloudflare.com/es-es/writing-complex-macros-in-rust-reverse-polish-notation/)、[Français](https://blog.cloudflare.com/fr-fr/writing-complex-macros-in-rust-reverse-polish-notation/)和[한국어](https://blog.cloudflare.com/ko-kr/writing-complex-macros-in-rust-reverse-polish-notation/).

![Writing complex macros in Rust: Reverse Polish Notation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49FSNFEYMC4YKNMQ9ZPHFY.jpg&w=640&h=427&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAVmVuTmBtO1drNFRtQ1xzU2Z4V2p4UWl2anV+YW96TmN1Rl91VGd7ZHKCZ3aDYHN/eoSNcX2JXnCBVWp/Y3OGcn6OdoKPb3+KgYuWeIWSZnmKXnSJbHyRe4eZfouad4iVfIiZdISWZXuQYHqSboKafIyhfo+id42dbX+WaH2UXXqUXXyYaoWgd42meJCmcY6iXHORWHSRU3eVWH2bZYWjcIupcI6oaY6lU26OUXCQT3WVVn2cY4WlbYupbI2pZo6m)

（ _这是一篇[最初发表](https://rreverser.com/writing-complex-macros-in-rust/)在我个人博客上的教程摘要_）

除其他有趣的功能外，Rust还具有强大的宏系统。不幸的是，即使在阅读了《The Book》和各种教程之后，当涉及到尝试实现一个涉及处理不同元素的复杂列表的宏时，我仍然很难理解应该如何做，并且在花了一些时间后，我才突然灵光一闪，开始对所有内容使用宏 :） _(好吧，并非对所有内容我都使用宏，我使用宏不是因为我不想使用函数和特殊类型以及存在时间之类的东西——就像我所见过的一些人那样。但是在任何地方，宏都是有用的)_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Rust with a macro lens](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47AZAKFG11R2WFAJH521KV.jpg&w=640&h=427&f=webp&fit=cover&position=center)

[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) [图片](https://www.flickr.com/photos/conchur/25057125240/in/photolist-EbdjmG-8NSN1q-qXhueG-YTYnm3-odaneQ-DxCKQA-228jg4t-DU8Axz-XTQfdD-4p6nJk-UKVzbn-YFeKcW-osZ2XM-e6qefx-Tb3a6Q-dCw1zk-Et3kKh-dbAR9x-zHP8TR-a9cqw4-9JQHRy-Et1Ag5-PqFtx1-7x3Ukq-67VJc6-cvoKSo-qH2S9L-zHJAr9-XmCLsL-8AMWXX-ZV2hHh-XGPiHq-ZKpFSB-yqd2P1-23hMiaC-zETYYa-Wj7BVi-PNP4YA-LCNm6c-8AnkrZ-KA7qmt-KjYPxC-SzQsZD-Cxwvqg-GuZ3nn-J4jBaA-TzyjpB-DcYJA1-YQYNA3-My1uu8) 来自 [Conor Lawless](https://www.flickr.com/photos/conchur/)

因此，下面是我对编写这些宏背后的原理的看法。这里假设您已经阅读了《The Book》中的[宏](https://doc.rust-lang.org/book/first-edition/macros.html)章节，并且熟悉基本的宏定义和令牌类型。

在本教程中，我将以[逆波兰式](https://en.wikipedia.org/wiki/Reverse_Polish_notation)为例。它非常有趣，因为它非常简单，您可能在学校时就已经熟悉了它，但是要在编译时静态地实现它，您就需要使用递归宏方法。

逆波兰式（也称后缀式）使用堆栈进行所有操作，从而将任意操作数压入堆栈，而任何_[二进制]_操作都从堆栈中获取两个操作数，计算结果并将其放回堆栈。因此如下所示：
    
    
    2 3 + 4 *

转换为：

  1. 将2放入堆栈。
  2. 将3放入堆栈。
  3. 从堆栈中取最后两值（3和2），应用运算符+并将结果（5）放回堆栈。
  4. 将4放入堆栈。
  5. 从堆栈中取最后两值（4和5），应用运算符*（4 * 5）并将结果（20）放回堆栈。
  6. 表达式结束，堆栈上有单值（20）。



在数学和大多数现代编程语言中使用的更常见的中缀表示法中，表达式应该是(2 + 3)* 4。

因此，让我们编写一个宏，它将在编译时通过将RPN（Region Proposal Network，区域候选网络）转换成Rust能够理解的中缀表示法来计算RPN。
    
    
    macro_rules! rpn {
      // TODO
    }
    
    println!("{}", rpn!(2 3 + 4 *)); // 20

让我们先从将数字压入堆栈开始。

宏当前不允许匹配文字，并且expr对我们不起作用，因为它可能会意外地匹配序列，例如2 + 3 ......而不是仅取单个数字，因此我们将求助于tt——一种仅匹配一个标签树的通用令牌匹配器（无论它是一个原始令牌，例如literal/identifier/lifetime/等等；或一个()/[]/{}——带括号的表达式包含着更多令牌）：
    
    
    macro_rules! rpn {
      ($num:tt) => {
        // TODO
      };
    }

现在，我们需要一个用于堆栈的变量。

宏不能使用实变量，因为我们希望这个堆栈只在编译时存在。相反，这里的技巧是使用一个单独的令牌序列，它可以被传递，就像一个累加器一样。

在我们的例子中，我们将它表示为一个逗号分隔的expr序列（因为我们不仅将其用于简单数字，而且还将其用于中间的中缀表达式），并将它封装到方括号中，以便与其他输入分隔开来：
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt) => {
        // TODO
      };
    }

现在，令牌序列并不是一个真正的变量——你不能就地修改它，然后再做一些事情。相反，你可以通过必要的修改创建这个令牌序列的新副本，然后再次递归地调用相同的宏。

如果您有函数语言背景，或者曾经使用过任何提供不可变数据的库，那么你可能已经熟悉这两种方法了——通过创建修改后的副本来修改数据和使用递归处理列表：
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt) => {
        rpn!([ $num $(, $stack)* ])
      };
    }

现在，很明显，只有一个数字的情况不太可能出现，并且这对我们来说也不太有趣，因此我们需要将该数字之后的其他任何内容匹配为零个或多个tt令牌序列，这些令牌可以传递给我们下一个调用的宏，用于进一步匹配和处理：
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
          rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

到这一步，我们仍然缺少运算符支持。我们如何匹配运算符？

如果我们的RPN是一系列令牌，我们希望以完全相同的方式进行处理，则可以简单地使用像这样的列表$($token:tt)*。不幸的是，这并不能让我们遍历列表并根据每个令牌推送操作数或应用运算符。

《The Book》说，“宏系统不处理解析歧义”，这对于单个宏分支是正确的——我们不能匹配一个数字序列，后跟一个诸如$($num:tt)* +的运算符，外加，因为+也是一个有效的令牌,可以由tt组匹配，但这又正是递归宏的作用所在。

如果宏定义中有不同的分支，Rust将一一尝试，因此我们可以将运算符分支放在数字一之前，这样可以避免任何冲突：
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] + $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] - $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] * $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] / $($rest:tt)*) => {
        // TODO
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

如前所述，运算符应用于堆栈上的最后两个数字，因此我们需要分别匹配它们，“计算”结果（构造一个正则中缀表达式）并将其放回：
    
    
    macro_rules! rpn {
      ([ $b:expr, $a:expr $(, $stack:expr)* ] + $($rest:tt)*) => {
        rpn!([ $a + $b $(, $stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] - $($rest:tt)*) => {
        rpn!([ $a - $b $(, $stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] * $($rest:tt)*) => {
        rpn!([ $a * $b $(,$stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] / $($rest:tt)*) => {
        rpn!([ $a / $b $(,$stack)* ] $($rest)*)
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

我不太喜欢这种明显的重复，但是，就像文字一样，没有特殊的令牌类型可以匹配运算符。

但是，我们可以做的是添加一个负责计算的助手，并将任何显式的运算符分支委托给它。

在宏中，你不能使用外部辅助，但是唯一可以肯定的是您的宏已经在作用域内，因此通常的技巧是在同一个宏中用一些特殊的令牌序列来“标记”，然后像在常规分支中一样递归地调用它。

让我们使用@op作为标记，并在其中通过tt接受任意运算符（在这种情况下tt是明确的，因为我们只将运算符传递给这个帮助器）。

堆栈不再需要在每个单独的分支中展开——由于我们之前已将其包装在[]方括号中，因此可以将其与其他任意标签树（tt）匹配，然后传递给我们的帮助器：
    
    
    macro_rules! rpn {
      (@op [ $b:expr, $a:expr $(, $stack:expr)* ] $op:tt $($rest:tt)*) => {
        rpn!([ $a $op $b $(, $stack)* ] $($rest)*)
      };
    
      ($stack:tt + $($rest:tt)*) => {
        rpn!(@op $stack + $($rest)*)
      };
      
      ($stack:tt - $($rest:tt)*) => {
        rpn!(@op $stack - $($rest)*)
      };
    
      ($stack:tt * $($rest:tt)*) => {
        rpn!(@op $stack * $($rest)*)
      };
      
      ($stack:tt / $($rest:tt)*) => {
        rpn!(@op $stack / $($rest)*)
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

现在，所有令牌都由相应的分支处理，我们只需要处理最后一种情况，当堆栈包含一个项目时，没有剩余的令牌：
    
    
    macro_rules! rpn {
      // ...
      
      ([ $result:expr ]) => {
        $result
      };
    }

此时，如果使用空堆栈和RPN表达式调用此宏，则该宏将已产生正确的结果：

[Playground](https://play.rust-lang.org/?gist=cd56f6d7335e2d27c05e7fa89545b2cd&version=stable)
    
    
    println!("{}", rpn!([] 2 3 + 4 *)); // 20

然而，我们的堆栈是一个实现细节，我们真的不希望每个消费者传递一个空的堆栈，所以让我们在最后添加另一个通用分支作为入口点，并自动添加[]：

[Playground](https://play.rust-lang.org/?gist=d94abc0e20aa5c7f689706af06fd1923&version=stable)
    
    
    macro_rules! rpn {
      // ...
    
      ($($tokens:tt)*) => {
        rpn!([] $($tokens)*)
      };
    }
    
    println!("{}", rpn!(2 3 + 4 *)); // 20

我们的宏甚至可以用于更复杂的表达式，例如[Wikipedia页面上有关RPN的](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Example)表达式！
    
    
    println!("{}", rpn!(15 7 1 1 + - / 3 * 2 1 1 + + -)); // 5

## 错误处理

现在，对于正确的RPN表达式，一切似乎都可以正常运行，但是对于要投入生产的宏，我们需要确保它也可以处理无效输入，并带有合理的错误消息。

首先，让我们尝试在中间插入另一个数字，看看会发生什么：
    
    
    println!("{}", rpn!(2 3 7 + 4 *));

输出：
    
    
    error[E0277]: the trait bound `[{integer}; 2]: std::fmt::Display` is not satisfied
      --> src/main.rs:36:20
       |
    36 |     println!("{}", rpn!(2 3 7 + 4 *));
       |                    ^^^^^^^^^^^^^^^^^ `[{integer}; 2]` cannot be formatted with the default formatter; try using `:?` instead if you are using a format string
       |
       = help: the trait `std::fmt::Display` is not implemented for `[{integer}; 2]`
       = note: required by `std::fmt::Display::fmt`

好吧，因为它没有提供与表达式中的实际错误相关的任何信息，因此它看起来毫无用处。

为了弄清发生了什么，我们需要调试宏。为此，我们将使用[trace_macros](https://doc.rust-lang.org/unstable-book/language-features/trace-macros.html)特性（并且，与其他可选的编译器特性一样，您需要一个不稳定测试版Rust）。我们不想回溯println!调用，因此我们将我们的RPN计算分离出一个变量：

[Playground](https://play.rust-lang.org/?gist=610bc0c241aacda3d30a916f89b244cd&version=nightly)
    
    
    #![feature(trace_macros)]
    
    macro_rules! rpn { /* ... */ }
    
    fn main() {
      trace_macros!(true);
      let e = rpn!(2 3 7 + 4 *);
      trace_macros!(false);
      println!("{}", e);
    }

在输出中，我们现在将逐步查看宏的递归计算方式：
    
    
    note: trace_macro
      --> src/main.rs:39:13
       |
    39 |     let e = rpn!(2 3 7 + 4 *);
       |             ^^^^^^^^^^^^^^^^^
       |
       = note: expanding `rpn! { 2 3 7 + 4 * }`
       = note: to `rpn ! ( [  ] 2 3 7 + 4 * )`
       = note: expanding `rpn! { [  ] 2 3 7 + 4 * }`
       = note: to `rpn ! ( [ 2 ] 3 7 + 4 * )`
       = note: expanding `rpn! { [ 2 ] 3 7 + 4 * }`
       = note: to `rpn ! ( [ 3 , 2 ] 7 + 4 * )`
       = note: expanding `rpn! { [ 3 , 2 ] 7 + 4 * }`
       = note: to `rpn ! ( [ 7 , 3 , 2 ] + 4 * )`
       = note: expanding `rpn! { [ 7 , 3 , 2 ] + 4 * }`
       = note: to `rpn ! ( @ op [ 7 , 3 , 2 ] + 4 * )`
       = note: expanding `rpn! { @ op [ 7 , 3 , 2 ] + 4 * }`
       = note: to `rpn ! ( [ 3 + 7 , 2 ] 4 * )`
       = note: expanding `rpn! { [ 3 + 7 , 2 ] 4 * }`
       = note: to `rpn ! ( [ 4 , 3 + 7 , 2 ] * )`
       = note: expanding `rpn! { [ 4 , 3 + 7 , 2 ] * }`
       = note: to `rpn ! ( @ op [ 4 , 3 + 7 , 2 ] * )`
       = note: expanding `rpn! { @ op [ 4 , 3 + 7 , 2 ] * }`
       = note: to `rpn ! ( [ 3 + 7 * 4 , 2 ] )`
       = note: expanding `rpn! { [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [  ] [ 3 + 7 * 4 , 2 ] )`
       = note: expanding `rpn! { [  ] [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [ [ 3 + 7 * 4 , 2 ] ] )`
       = note: expanding `rpn! { [ [ 3 + 7 * 4 , 2 ] ] }`
       = note: to `[(3 + 7) * 4, 2]`

如果我们仔细查看回溯，就会发现问题出在以下步骤：
    
    
       = note: expanding `rpn! { [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [  ] [ 3 + 7 * 4 , 2 ] )`

由于[ 3 + 7 * 4 , 2 ] 无法匹配([$result:expr]) =>……分支来作为最终表达式，因此它最终反而被我们的($($tokens:tt)*) => ......分支全捕获，并以空堆栈[]作为前缀，然后用通用的$num:tt匹配原始的[ 3 + 7 * 4 , 2 ]，并作为单个最终值压入堆栈。

为了防止这种情况发生，让我们在最后两个分支之间插入另一个分支，它将匹配任何堆栈。

只有当我们用完令牌时，它才会被命中，但是堆栈并没有一个确切的最终值，所以我们可以将它视为编译错误，并使用内置[`compile_error!`](https://doc.rust-lang.org/std/macro.compile_error.html)宏生成更有用的错误消息。

请注意，我们不能在这种情况下使用format!（格式化函数），因为它使用运行时API来格式化字符串，所以我们必须限制自己用内置的concat!和stringify!宏来格式化消息：

[Playground](https://play.rust-lang.org/?gist=e56be9422387bcae54aab3b8405a11e7&version=stable)
    
    
    macro_rules! rpn {
      // ...
    
      ([ $result:expr ]) => {
        $result
      };
    
      ([ $($stack:expr),* ]) => {
        compile_error!(concat!(
          "Could not find final value for the expression, perhaps you missed an operator? Final stack: ",
          stringify!([ $($stack),* ])
        ))
      };
    
      ($($tokens:tt)*) => {
        rpn!([] $($tokens)*)
      };
    }

错误信息现在意义更明确了，并且至少包含一些关于当前状态评估的详细信息：
    
    
    error: Could not find final value for the expression, perhaps you missed an operator? Final stack: [ (3 + 7) * 4 , 2 ]
      --> src/main.rs:31:9
       |
    31 |         compile_error!(concat!("Could not find final value for the expression, perhaps you missed an operator? Final stack: ", stringify!([$($stack),*])))
       |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...
    40 |     println!("{}", rpn!(2 3 7 + 4 *));
       |                    ----------------- in this macro invocation

但如果，相反地，我们错过了某个数字呢？

[Playground](https://play.rust-lang.org/?gist=ce40630b8c1aa610c46b94557fdc9905&version=stable)
    
    
    println!("{}", rpn!(2 3 + *));

不幸的是，前面的做法不太奏效了：
    
    
    error: expected expression, found `@`
      --> src/main.rs:15:14
       |
    15 |         rpn!(@op $stack * $($rest)*)
       |              ^
    ...
    40 |     println!("{}", rpn!(2 3 + *));
       |                    ------------- in this macro invocation

如果您尝试使用trace_macros，即使出于某种原因它不会在这里扩大堆栈，但幸运的是，正在发生的事情是相对比较清楚的——@op对于什么应该匹配（预计至少有两个值在堆栈上）有着非常具体的条件，并且，当它匹配失败时，@会与同一个极度“贪婪”的$num:tt进行匹配，以及被压入堆栈。

为避免这种情况，再一次，我们将添加另一个分支以匹配任何@op尚未匹配的内容，并生成编译错误提示：

[Playground](https://play.rust-lang.org/?gist=8729a8f3c96fa58ed62d35804c48782d&version=stable)
    
    
    macro_rules! rpn {
      (@op [ $b:expr, $a:expr $(, $stack:expr)* ] $op:tt $($rest:tt)*) => {
        rpn!([ $a $op $b $(, $stack)* ] $($rest)*)
      };
    
      (@op $stack:tt $op:tt $($rest:tt)*) => {
        compile_error!(concat!(
          "Could not apply operator `",
          stringify!($op),
          "` to the current stack: ",
          stringify!($stack)
        ))
      };
    
      // ...
    }

让我们再试一次：
    
    
    error: Could not apply operator `*` to the current stack: [ 2 + 3 ]
      --> src/main.rs:9:9
       |
    9  |         compile_error!(concat!("Could not apply operator ", stringify!($op), " to current stack: ", stringify!($stack)))
       |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...
    46 |     println!("{}", rpn!(2 3 + *));
       |                    ------------- in this macro invocation

好多了！现在我们的宏可以在编译时对任意RPN表达式求值，并且可以正常处理最常见的错误，所以我们今天就到此为止，并声明它已经可以投入生产了 :）

我们可以添加更多的小改进，但是我想把它们留在本演示教程之外再讲。

如果这对你有帮助，或者你想[在Twitter上](https://twitter.com/RReverser)看到更好的话题，请随时告诉我！

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F&t=%E5%9C%A8Rust%E4%B8%AD%E7%BC%96%E5%86%99%E5%A4%8D%E6%9D%82%E7%9A%84%E5%AE%8F%EF%BC%9A%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F)[](https://x.com/intent/post?text=%E5%9C%A8Rust%E4%B8%AD%E7%BC%96%E5%86%99%E5%A4%8D%E6%9D%82%E7%9A%84%E5%AE%8F%EF%BC%9A%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://bsky.app/intent/compose?text=%E5%9C%A8Rust%E4%B8%AD%E7%BC%96%E5%86%99%E5%A4%8D%E6%9D%82%E7%9A%84%E5%AE%8F%EF%BC%9A%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://mastodonshare.com/?text=%E5%9C%A8Rust%E4%B8%AD%E7%BC%96%E5%86%99%E5%A4%8D%E6%9D%82%E7%9A%84%E5%AE%8F%EF%BC%9A%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://www.threads.net/intent/post?text=%E5%9C%A8Rust%E4%B8%AD%E7%BC%96%E5%86%99%E5%A4%8D%E6%9D%82%E7%9A%84%E5%AE%8F%EF%BC%9A%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)

## 相关标签

[Cloudflare Polish](https://blog.cloudflare.com/zh-cn/tag/cloudflare-polish/)[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
