---
url: https://blog.cloudflare.com/zh-cn/workers-production-safety/
title: \u751f\u4ea7\u5b89\u5168\u65b0\u5de5\u5177\u2014\u2014\u6e10\u8fdb\u5f0f\u90e8\u7f72\u3001\u6e90\u7801\u6620\u5c04\u3001\u901f\u7387\u9650\u5236\u548c\u5168\u65b0 SDK | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:27.729824+00:00
---

# 生产安全新工具——渐进式部署、源码映射、速率限制和全新 SDK | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/workers-production-safety/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Observability](https://blog.cloudflare.com/zh-cn/tag/observability/)+2再显示 2 个标签

5 个标签显示 5 个标签

  * 文章标签
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[SDK](https://blog.cloudflare.com/zh-cn/tag/sdk/)
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



[Rate Limiting](https://blog.cloudflare.com/zh-cn/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/zh-cn/tag/sdk/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Observability](https://blog.cloudflare.com/zh-cn/tag/observability/)[Rate Limiting](https://blog.cloudflare.com/zh-cn/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/zh-cn/tag/sdk/)

2024年4月4日

# 生产安全新工具——渐进式部署、源码映射、速率限制和全新 SDK

![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanushree Sharma](https://blog.cloudflare.com/zh-cn/author/tanushree/)和[Jacob Bednarz](https://blog.cloudflare.com/zh-cn/author/jacob-bednarz/)

阅读时间：11 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/workers-production-safety/)、[Deutsch](https://blog.cloudflare.com/de-de/workers-production-safety/)、[Español](https://blog.cloudflare.com/es-es/workers-production-safety/)、[Français](https://blog.cloudflare.com/fr-fr/workers-production-safety/)、[日本語](https://blog.cloudflare.com/ja-jp/workers-production-safety/)、[한국어](https://blog.cloudflare.com/ko-kr/workers-production-safety/)和[繁體中文](https://blog.cloudflare.com/zh-tw/workers-production-safety/).

![New tools for production safety — Gradual deployments, Source maps, Rate Limiting, and new SDKs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FR4MNGHSCH0P7DD7P68W.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+//769vXz8fDw8vHx9PLy8u7u6+fl/////vz98vT16+7y6+7z7u/17ezw5+Tm/////f3/8PP55u315ez36O356Orz5OPq////////8vb+5/D65e/85+/+6Oz55Obv////////+f3/7/f/7Pb/7fb/7fL/6uz2////////////+///+P7/9/7/9fr/8vT8/////////////////////////P//+Pv/////////////////////////////+/3/)

2024 年度 Developer Week 聚焦于生产就绪性。4 月 1 日（星期一），我们[宣布](https://blog.cloudflare.com/zh-cn/making-full-stack-easier-d1-ga-hyperdrive-queues-zh-cn/) [D1](https://developers.cloudflare.com/d1/)、[Queues](https://developers.cloudflare.com/queues/)、[Hyperdrive](https://developers.cloudflare.com/hyperdrive/) 和 [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) 已生产就绪并正式发布。4 月 2 日（星期二），我们[宣布](https://blog.cloudflare.com/zh-cn/workers-ai-ga-huggingface-loras-python-support-zh-cn/)我们的推理平台 —— [Workers AI](https://developers.cloudflare.com/workers-ai/) —— 生产就绪。而我们还远远没有结束呢。

生产就绪性不仅仅关乎您用于构建的服务的规模和可靠性。您还需要一些工具来安全、可靠地进行更改。 您不仅要依靠 Cloudflare 提供的服务，还要能够根据应用程序的需求精确控制和定制 Cloudflare 的行为。

今天，我们隆重宣布五项更新，为您提供一些更强有力的工具——渐进式部署、Tail Workers 中的源码映射堆栈跟踪、新的速率限制 API、全新的 API SDK 以及 Durable Objects 更新——每一项都是针对任务关键型生产服务而构建的。我们使用 Workers 构建自己的产品，包括 [Access](https://developers.cloudflare.com/cloudflare-one/policies/access/)、 [R2](https://developers.cloudflare.com/r2/)、 [KV](https://developers.cloudflare.com/kv/)、 [Waiting Room](https://developers.cloudflare.com/waiting-room/)、 [Vectorize](https://developers.cloudflare.com/vectorize/)、 [Queues](https://developers.cloudflare.com/queues/)、 [Stream](https://developers.cloudflare.com/stream/) 等。我们自己依靠以上每一个新功能来确保我们生产就绪，现在我们很高兴能将它们提供给每一个人使用。

### 逐步部署更改到 Workers 和 Durable Objects

部署 Worker 几乎是瞬时的事情——只需几秒钟，您的更改就会在[每一个地方](https://www.cloudflare.com/network/)生效。

当您达到生产规模时，您所做的每一次改变具有更大的风险，无论是在数量上还是在期望上。 您需要满足 99.99% 的可用性 SLA，或雄心勃勃的 P90 延迟 SLO。 一个不良部署若在 100% 的流量中上线运行 45 秒，可能意味着数百万个请求失败。即使是一个微小的代码更改，如果一次性推出，都有可能会导致大量重试请求，导致后端不堪重负。对于我们自己使用 Workers 构建的服务，都会考虑和缓解这些风险。

减轻这些风险的方法是逐步部署更改——通常称为滚动部署：

  1. 当前版本的应用程序在生产环境中运行。
  2. 将应用程序的新版本部署到生产环境中，但只将一小部分流量路由到这个新版本，并等待它在生产环境中 “浸泡”，检测是否出现性能退化和错误。 如果发生了问题，可在一小部分（例如 1%）的流量中及早发现并可以快速回滚。
  3. 逐步增加流量百分比，直到新版本的流量达到 100%，然后再全面推出。



今天，我们将推出一种一流的方式，通过 [Cloudflare API](https://developers.cloudflare.com/api/operations/worker-deployments-list-deployments)、[Wrangler CLI](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-wrangler) 或 [Workers 仪表板](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-the-cloudflare-dashboard)将更改逐步部署到 Workers 和 Durable Objects。渐进式部署现已开启公测——您可以在订阅 [Workers Free 计划](https://developers.cloudflare.com/workers/platform/pricing/#workers)任何账户中使用渐进式部署，很快您就可以在订阅 [Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/#workers) 和 Enterprise 计划的 Cloudflare 账户上开始使用渐进式部署。 一旦您的账户可以访问，您将在 Workers 仪表板上看到横幅通知。

当在生产中同时拥有 Worker 或 Durable Object 的两个版本时，您几乎一定希望能按版本过滤指标、异常和日志。 这可以帮助您在新版本只推出给一小部分流量时提前发现问题，或者在按 50/50 比例分割流量时比较性能指标。我们还在整个平台上增加了版本级别的可观察性：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Splitting traffic between different versions of a Worker.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4792EFMEWR5SFVJAMDC49A.png&w=715&h=353&f=webp&fit=cover&position=center)

  * 您可以在 Workers 仪表板中或通过 [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) 按版本过滤分析结果。
  * [Workers Trace Events](https://developers.cloudflare.com/workers/observability/logging/logpush/) 和 [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/) 事件包括 Worker 的版本 ID，以及可选的版本信息和版本标记字段。
  * 使用 [wrangler tail](https://developers.cloudflare.com/workers/wrangler/commands/#tail) 查看实时日志时 ，可以查看特定版本的日志。
  * 通过配置[版本元数据绑定](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/)，您可以在 Worker 代码中访问版本 ID、消息和标签 。



您可能还希望确保每个客户端或用户只能看到 Worker 的一个一致版本。我们新推出[版本亲和性](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity)功能，以便与特定标识符（例如用户、会话或任何 ID）相关联的请求将始终由 Worker 的一致版本处理。 [会话亲和力](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity)与[规则集引擎](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#setting-cloudflare-workers-version-key-using-ruleset-engine)一起使用时 ，您可以完全控制用于确保“粘性”的机制和标识符。

渐进式部署进入公测阶段。 随着我们向正式版推进，我们正在努力以提供如下支持：

  * **版本覆盖。**调用 Worker 的特定版本，以便在其服务任何生产流量之前进行测试。这样将允许您创建蓝绿部署。
  * **Cloudflare Pages.**让 Cloudflare Pages 中的 CI/CD 系统代表您自动推进部署。
  * **自动回滚。** 当新版 Worker 的错误率激增时，自动回滚部署。



我们期待听到您的反馈！请通过[此](https://www.cloudflare.com/lp/developer-week-deployments/)反馈表单或[开发人员 Discord](https://discord.gg/HJvPcPcN)的 #workers-gradual-deployments-beta 频道 告诉我们您的想法。

### Tail Workers 中的源码映射堆栈跟踪

生产就绪意味着要跟踪错误和异常，并努力将其降至零。发生错误时，通常首先要查看的是错误的[堆栈跟踪](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack)，即调用的具体函数、调用顺序、调用的行和文件以及参数。

大多数 JavaScript 代码（不仅是 Workers 上的代码，还包括是各种平台的代码）在部署到生产环境之前，通常会先进行打包，常会转译，然后再进行压缩。这个过程是在幕后进行的，以创建更小的包来优化性能，并在需要时将 Typescript 转换为 Javascript。

如果您见过一个异常返回这样的堆栈跟踪：/src/index.js:1:342，这意味着错误发生在函数压缩代码的第 342 个字符上。这显然对调试没有什么帮助。

[源码映射](https://web.dev/articles/source-maps)解决了这个问题——它将编译和精简后的代码映射回您编写的原始代码。源码映射与 JavaScript 运行时返回的堆栈跟踪相结合，为您提供人类可读的堆栈跟踪。例如，下面的堆栈跟踪显示 Worker 在 down.ts 文件的第 30 行收到了一个意外的空值。这是一个有用的调试起点，您可以沿着堆栈跟踪向下查看，以了解导致空值的函数调用设置。

工作方式如下：
    
    
    Unexpected input value: null
      at parseBytes (src/down.ts:30:8)
      at down_default (src/down.ts:10:19)
      at Object.fetch (src/index.ts:11:12)

  1. 在 [Wrangler.toml](https://developers.cloudflare.com/workers/wrangler/configuration/) 中设置 upload_source_maps = true 后 ，当运行 [Wrangler 部署](https://developers.cloudflare.com/workers/wrangler/commands/#deploy)或 [Wrangler 版本上传](https://developers.cloudflare.com/workers/wrangler/commands/#versions)时，将自动生成并上传任何源码映射文件 。
  2. 当您的 Worker 抛出未捕获异常时，我们会获取源码映射，并使用它将异常的堆栈跟踪映射回 Worker 的原始源代码行。
  3. 然后，您就可以在[实时日志](https://developers.cloudflare.com/workers/observability/logging/real-time-logs/) 或 [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/) 中查看经过反混淆的堆栈跟踪 。



从今天开始，通过公测版，您可以在部署 Worker 时将源码映射上传到 Cloudflare —— [欢迎阅读文档以开始使用](https://developers.cloudflare.com/workers/observability/source-maps) 。从 4 月 15 日开始，Workers 运行时将开始使用源码映射来反混淆堆栈跟踪。 当源码映射堆栈跟踪可用时 ， 我们将在 Cloudflare 仪表板上发布通知，并在 [Cloudflare 开发人员 X 账户](https://twitter.com/CloudflareDev?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)公布。

### Workers 中的新速率限制 API

仅在具有合理的[速率限制](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)时，API 才算是生产就绪。随着业务发展，需要执行的限制也会日益复杂和多样化，以平衡特定客户的需求、保护服务正常运行或在特定情况下执行和调整限制。Cloudflare 自己的 API 就面临着这样的挑战——我们数十种产品的每一种都有许多 API 端点，可能需要执行不同的速率限制。

自 2017 年以来，您就可以在 Cloudflare 上配置[速率限制规则](https://developers.cloudflare.com/waf/rate-limiting-rules/)。但直到今天，控制这个功能的唯一方式是通过 Cloudflare 仪表板或 Cloudflare API。不可能在_运行时_上定义行为，或在 Worker 中编写直接与访问速率限制交互的代码——您只能控制一个请求在到达您的 Worker 之前是否执行速率限制。

今天，我们推出了新 API 的公测版，让您可以从 Worker 直接访问速率限制。 它的速度快如闪电，由 memcached 支持，添加到 Worker 中非常简单。 例如，以下配置定义了 60 秒内 100 个请求的速率限制：

然后，您可以在 Worker 中调用 RATE_LIMITER 绑定的 limit 方法，提供您选择的键值。根据上述配置， 一旦在 60 秒内向特定路径发出的请求超过 100 个，代码就会返回 [HTTP 429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) 响应状态码：
    
    
    [[unsafe.bindings]]
    name = "RATE_LIMITER"
    type = "ratelimit"
    namespace_id = "1001" # An identifier unique to your Cloudflare account
    
    # Limit: the number of tokens allowed within a given period, in a single Cloudflare location
    # Period: the duration of the period, in seconds. Must be either 60 or 10
    simple = { limit = 100, period = 60 } 

既然 Workers 现在可以直接连接到 memcached 这样的数据存储，我们还能提供什么呢？计数器？锁？ [内存缓存](https://github.com/cloudflare/workerd/pull/1666)？ 我们正在探索在 Workers 中提供很多基元，以解决多年来一直存在的问题，即跨多个 Worker 的临时共享状态[隔离](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates)应存放在何处，速率限制就是其中一个。 如果您现在依赖于将状态放在 Worker 的全局范围内，我们正在开发更好的基元，这些基元是为特定用例而专门构建的。
    
    
    export default {
      async fetch(request, env) {
        const { pathname } = new URL(request.url)
    
        const { success } = await env.RATE_LIMITER.limit({ key: pathname })
        if (!success) {
          return new Response(`429 Failure – rate limit exceeded for ${pathname}`, { status: 429 })
        }
    
        return new Response(`Success!`)
      }
    }

Workers 速率限制 API 目前处于公测阶段，您可以通过[阅读文档](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit)开始使用。

### 为 Cloudflare 的 API 自动生成新的 SDK

生产就绪意味着从通过点击仪表板上的按钮进行更改，转变为使用 [Terraform](https://github.com/cloudflare/terraform-provider-cloudflare) 或 [Pulumi](https://github.com/pulumi/pulumi-cloudflare) 等基础架构即代码方法 ，或自行/通过 SDK 直接发出 API 请求，以编程方式进行更改 。

[Cloudflare API](https://developers.cloudflare.com/api/) 规模庞大，并不断增加新功能——我们平均[每天更新 API 模式 20 到 30 次](https://github.com/cloudflare/api-schemas/activity) 。但迄今为止，我们的 API SDK 都是手动构建和维护的，因此我们迫切需要实现自动化。

我们已经做到了这一点，今天，我们宣布为 Cloudflare API 提供 [Typescript](https://github.com/cloudflare/cloudflare-typescript)、 [Python](https://github.com/cloudflare/cloudflare-python) 和 [Go](https://github.com/cloudflare/cloudflare-go)三种语言的新客户端 SDK，更多语言即将推出。

每个 SDK 都是根据定义我们每个 API 端点结构和功能的 [OpenAPI 模式](https://github.com/cloudflare/api-schemas)[， 使用 Stainless API](https://www.stainlessapi.com/) 自动生成的。 这意味着，当我们为 Cloudflare API 添加任何新功能时，对于 Cloudflare 的任何产品，都会自动重新生成这些 API SDK 并发布新版本，以确保其正确和最新。

运行以下命令之一即可安装这些 SDK：

如果使用 Terraform 或 Pulumi，Cloudflare 的 Terraform Provider 目前使用现有的非自动化 [Go SDK](https://github.com/cloudflare/cloudflare-go)。当你运行 terraform apply 时 ，Cloudflare Terraform Provider 会决定以何种顺序进行哪些 API 调用，并使用 Go SDK 执行这些操作。
    
    
    // Typescript
    npm install cloudflare
    
    // Python
    pip install cloudflare
    
    // Go
    go get -u github.com/cloudflare/cloudflare-go/v2

全新的自动生成 Go SDK 为实现对所有 Cloudflare 产品的更全面 Terraform 支持铺平了道路，提供了一套可依赖的基础工具，能正确且及时跟上最新的 API 变化。 我们正在朝着这样的目标努力：每当 Cloudflare 产品团队构建一个通过 Cloudflare API 公开的新功能时，就会自动得到 SDK 的支持。2024 年将推出更多更新，敬请期待。

### Durable Object 命名空间分析和 WebSocket Hibernation 正式发布

我们自己的许多产品，包括 [Waiting Room](https://developers.cloudflare.com/waiting-room/) 、 [R2](https://developers.cloudflare.com/r2/) 和 [Queues](https://developers.cloudflare.com/queues/) 以及 [PartyKit](https://www.partykit.io/) 等平台都使用 [Durable Objects](https://developers.cloudflare.com/durable-objects/)。Durable Objects 部署到全球，包括新增的大洋洲支持，您可以将其想象成单一实例 Workers ，它可以提供单点协调和[持久状态](https://developers.cloudflare.com/durable-objects/api/transactional-storage-api/) 。它们非常适合需要实时用户协调的应用程序 ， 如交互式聊天或协作编辑 。请听 Atlassian 的感言：

>  _我们的新功能之一是_ _[Confluence 白板](https://www.atlassian.com/software/confluence/whiteboards)，它提供了一种自由的方式来捕捉非结构化的工作，如头脑风暴和早期规划，然后再由团队进行更正式的记录。团队考虑了很多实时协作的方案，最终决定使用 Cloudflare 的 Durable Objects。事实证明，Durable Objects 非常适合这一问题领域，它独特的功能组合使我们能够大大简化基础架构，并轻松扩展到大量用户。_ [_\- Atlassian_](https://www.atlassian.com/software/confluence/whiteboards)

我们以前没有在仪表板中显示相关的分析趋势，因此除非您直接使用 [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)， 否则很难了解 [Durable Objects 命名空间](https://developers.cloudflare.com/durable-objects/configuration/access-durable-object-from-a-worker/#generate-ids-randomly)中的使用模式和错误率 。 现在，我们对 [Durable Objects 仪表板](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)进行了改进，让您可以根据需要深入查看指标。

从[第一天](https://blog.cloudflare.com/introducing-workers-durable-objects)起，Durable Objects 就支持 [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)，允许许多客户端直接连接到持久对象以发送和接收消息。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2305 Embedded Image - tUWMOW](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45NGJQ7SMHCNME7M5TATPN.png&w=715&h=557&f=webp&fit=cover&position=center)

不过，有时客户端应用程序打开一个 WebSocket 连接后，最终会停下来......不进行任何操作。 想一想您的浏览器中打开了5小时但没有碰过的标签。如果它使用 WebSocket 发送和接收信息，那么它实际上就拥有了一个长时间存在的 TCP 连接，而这个连接并没有被用于任何其他用途。 如果这个连接的目标是一个 Durable Object，这个 Durable Object 就必须一直运行，等待某种操作发生，从而消耗内存，并花费您的成本。

我们最初[推出 WebSocket Hibernation](https://blog.cloudflare.com/workers-pricing-scale-to-zero) 就是为了解决这个问题，今天我们宣布该功能已完成测试并正式发布。通过 WebSocket Hibernation，您可以设置休眠时使用的自动响应，并将状态序列化，使其能够在休眠状态下保持。这为 Cloudflare 提供了所需的输入，在“休眠” Durable Object（使其不处于活动运行状态）同时保持来自客户端的开放 WebSocket 连接，而且您不需要为空闲时间付费。结果是，当您真正需要时，您的状态始终在内存中可用，但在不需要时不会被无谓保留。只要您的 Durable Object 处于休眠状态，即使仍有活动的客户端通过 WebSocket 连接，您也不会被计费。

此外，我们还听取了开发人员就传入 WebSocket 消息到 Durable Objects 的费用提出的反馈意见，这倾向于使用更小、更频繁的消息进行实时通信。从今天起，传入 WebSocket 消息将按相当于 1/20 个请求计费（而不是到现在为止那样 1 个消息相当于 1 个请求）。下面是一个[定价示例](https://developers.cloudflare.com/durable-objects/platform/pricing/#example-4)：

.tg {border-collapse:collapse;border-color:#ccc;border-spacing:0;} .tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top} .tg .tg-4kyp{color:#0E101A;text-align:left;vertical-align:top} .tg .tg-bhdc{color:#0E101A;font-weight:bold;text-align:left;vertical-align:top}

| WebSocket Connection Requests | Incoming WebSocket Messages | Billed Requests | Request Billing  
---|---|---|---|---  
Before | 10K | 432M | 432,010,000 | $64.65  
After | 10K | 432M | 21,610,000 | $3.09  
  
WebSocket 连接请求

传入 WebSocket 信息

计费的请求

请求费用

使用之前

10K

432M

432,010,000

$64.65

使用之后

10K

432M

21,610,000

$3.09

### 生产就绪，但没有生产的复杂性

要在上一代云平台上达到生产就绪状态，意味着要减慢发布速度。它意味着要将许多独立的工具拼凑起来，或者组建整个团队在内部平台上开展工作。 您不得不改造自己的生产力工具组合，已部署到障碍重重的平台。

Cloudflare 开发人员平台已经成熟并生产就绪，致力于成为一个集成平台，其上各种产品直观地协同工作，不会有十种不同的方法来完成同样的工作，不需要通过复杂的兼容性列表来帮助了解什么可以一同工作。这些更新都充分体现了这一点，将新功能整合到 Cloudflare 平台的各种产品和组成部分中。

为此，我们期待听到您的意见，不仅是您希望看到接下来推出什么产品和功能，还包括您认为我们在哪些方面可以做得更简单，或者您认为我们的产品在哪些方面可以更好地协同工作。请告诉我们您认为我们在哪些方面可以做得更多—— [Cloudflare 开发人员 Discord](https://discord.cloudflare.com/) 的大门始终敞开。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkers-production-safety%2F&t=%E7%94%9F%E4%BA%A7%E5%AE%89%E5%85%A8%E6%96%B0%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94%E6%B8%90%E8%BF%9B%E5%BC%8F%E9%83%A8%E7%BD%B2%E3%80%81%E6%BA%90%E7%A0%81%E6%98%A0%E5%B0%84%E3%80%81%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6%E5%92%8C%E5%85%A8%E6%96%B0%20SDK)[](https://x.com/intent/post?text=%E7%94%9F%E4%BA%A7%E5%AE%89%E5%85%A8%E6%96%B0%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94%E6%B8%90%E8%BF%9B%E5%BC%8F%E9%83%A8%E7%BD%B2%E3%80%81%E6%BA%90%E7%A0%81%E6%98%A0%E5%B0%84%E3%80%81%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6%E5%92%8C%E5%85%A8%E6%96%B0+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkers-production-safety%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkers-production-safety%2F)[](https://bsky.app/intent/compose?text=%E7%94%9F%E4%BA%A7%E5%AE%89%E5%85%A8%E6%96%B0%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94%E6%B8%90%E8%BF%9B%E5%BC%8F%E9%83%A8%E7%BD%B2%E3%80%81%E6%BA%90%E7%A0%81%E6%98%A0%E5%B0%84%E3%80%81%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6%E5%92%8C%E5%85%A8%E6%96%B0+SDK+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkers-production-safety%2F)[](https://mastodonshare.com/?text=%E7%94%9F%E4%BA%A7%E5%AE%89%E5%85%A8%E6%96%B0%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94%E6%B8%90%E8%BF%9B%E5%BC%8F%E9%83%A8%E7%BD%B2%E3%80%81%E6%BA%90%E7%A0%81%E6%98%A0%E5%B0%84%E3%80%81%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6%E5%92%8C%E5%85%A8%E6%96%B0+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkers-production-safety%2F)[](https://www.threads.net/intent/post?text=%E7%94%9F%E4%BA%A7%E5%AE%89%E5%85%A8%E6%96%B0%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94%E6%B8%90%E8%BF%9B%E5%BC%8F%E9%83%A8%E7%BD%B2%E3%80%81%E6%BA%90%E7%A0%81%E6%98%A0%E5%B0%84%E3%80%81%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6%E5%92%8C%E5%85%A8%E6%96%B0+SDK+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fworkers-production-safety%2F)

## 相关标签

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Observability](https://blog.cloudflare.com/zh-cn/tag/observability/)[Rate Limiting](https://blog.cloudflare.com/zh-cn/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/zh-cn/tag/sdk/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Jacob Bednarz](https://blog.cloudflare.com/zh-cn/author/jacob-bednarz/)

[](https://jacobbednarz.com)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
