---
url: https://blog.cloudflare.com/zh-cn/post-mortem-on-cloudflare-control-plane-and-analytics-outage/
title: Cloudflare \u63a7\u5236\u5e73\u9762\u548c\u5206\u6790\u670d\u52a1\u4e2d\u65ad\u7684\u4e8b\u540e\u5206\u6790 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:39:46.461295+00:00
---

# Cloudflare 控制平面和分析服务中断的事后分析 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/post-mortem-on-cloudflare-control-plane-and-analytics-outage/

[博客](https://blog.cloudflare.com/zh-cn/)

[中断](https://blog.cloudflare.com/zh-cn/tag/outage/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)

2 个标签显示 2 个标签

  * 文章标签
  * [中断](https://blog.cloudflare.com/zh-cn/tag/outage/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)
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



[中断](https://blog.cloudflare.com/zh-cn/tag/outage/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)

2023年11月4日

# Cloudflare 控制平面和分析服务中断的事后分析

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/zh-cn/author/matthew-prince/)

阅读时间：13 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Deutsch](https://blog.cloudflare.com/de-de/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Español](https://blog.cloudflare.com/es-es/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Français](https://blog.cloudflare.com/fr-fr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[日本語](https://blog.cloudflare.com/ja-jp/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[한국어](https://blog.cloudflare.com/ko-kr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[繁體中文](https://blog.cloudflare.com/zh-tw/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)和[Português](https://blog.cloudflare.com/pt-br/post-mortem-on-cloudflare-control-plane-and-analytics-outage/).

![Post mortem on the Cloudflare Control Plane and Analytics Outage](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FSBWC0D25T68JD98V477.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vz/8e/v7Obi7ujj8u3q8O7u6ent/////f7/8+7q7eLa7+Ta9Ozk8u/s7Ozt////////9u7n8ODT8uPT9+3h9vLs8fDv////////+/Lq9OPU9+bV/PLk/Pfw9vXz//////////ny++zf/e/h//rv//74/Pr5///////////+//fv//vy///9///////////////////////9////////////////////////////////////////////////)

从协调世界时 2023 年 11 月 2 日（星期四）11:43 开始，Cloudflare 的控制平面和分析服务经历了一次中断。Cloudflare 的控制平面主要包括我们所有服务（包括网站和 API）面向客户的界面。我们的分析服务包括日志记录和分析报告。

事件从协调世界时 11 月 2 日 11:44 持续到协调世界时 11 月 4 日 04:25。截至协调世界时 11 月 2 日 17:57，我们在灾难恢复设施中恢复了大部分控制平面。在灾难恢复设施上线后，许多客户在使用我们的大多数产品时没有再遇到问题。不过，其他服务的恢复时间较长，在我们完全解决该事件之前，使用这些服务的客户可能会遇到一些问题。在事件发生期间，大多数客户无法使用我们的原始日志服务。

现在已针对所有客户恢复服务。在整个事件过程中，Cloudflare 的网络和安全服务仍旧按预期运行。虽然有一段时间客户无法对这些服务进行更改，但通过我们网络的流量并未受到影响。

这篇文章概述了导致此事件的原因、我们为防止此类问题而设立的架构、失败的地方、生效的地方和原因，以及我们根据过去 36 小时内吸取的教训而正在做出的改变。

首先，这本不应该发生。我们原本相信，即使我们的一个核心数据中心提供商发生灾难性故障，我们的高可用性系统也能阻止这样的服务中断。然而，虽然许多系统确实按照设计保持在线状态，但一些关键系统具有不明显的依赖性，导致它们不可用。对于此次事件以及它给我们的客户和团队带来的痛苦，我感到非常抱歉和难堪。

### 设计意图

Cloudflare 的控制平面和分析系统主要在俄勒冈州希尔斯伯勒附近三个数据中心的服务器上运行。这三个数据中心相互独立，每个数据中心都有多个市电电源，每个数据中心都有多个独立的冗余网络连接。

我们对这些设施的位置进行了慎重选择，有意使其相距一定距离，以最大限度地减少一场自然灾害使这三个设施全部受到影响的可能性，同时又足够近，以便它们都可以运行主动-主动冗余数据集群。这意味着这三个设施之间在不断同步数据。根据设计，如果任何一个设施停运，其余的设施都能继续运行。

这是我们四年前开始实施的系统设计。虽然我们的大多数关键控制平面系统都已迁移到高可用性集群，但一些服务，特别是一些较新产品的服务，尚未添加到高可用性集群中。

此外，我们有意未将日志记录系统作为高可用性集群的一部分。该决定的逻辑是，日志记录已经是一个分布式问题，日志在我们的网络边缘排队，然后发送回俄勒冈州的核心（或使用区域服务进行日志记录的客户的另一个区域设施）。如果我们的日志记录设施离线，那么分析日志就会在网络边缘排队，直到它重新上线。我们认为分析延误是可以接受的。

### Flexential 数据中心停电

俄勒冈州三个设施中最大的一个由 Flexential 运营。我们将该设施称为“PDX-DC04”。Cloudflare 在 PDX-04 租用了空间，我们最大的分析集群以及高可用性集群三分之一以上的机器都在这里。尚未加入我们高可用性集群的服务也默认放在此处。我们是该设施一个相对较大的客户，使用了其总容量的约 10%。

世界标准时间 11 月 2 日 08:50，为 PDX-04 提供服务的市电公司 Portland General Electric (PGE) 发生了一次计划外维护事件，影响了其大楼的一个独立供电电源。该事件关闭了 PDX-04 的一路电源。数据中心拥有多个具有一定程度独立性的电源，可以为设施供电。不过，Flexential 启动了发电机，来有效补充减少的电源。

遗憾的是，Flexential 没有通知 Cloudflare 他们已故障转移为发电机供电，这并不是最佳做法。我们的可观察性工具都无法检测到电力来源发生了变化。如果他们通知了我们，我们就会成立一个小组，密切监视该设施，并在其降级时将依赖于该设施的控制平面服务转移出去。

Flexential 同时运行发电机和一路剩余市电来进行供电，这种做法也很罕见。当电力需求较高时，市电公司要求数据中心脱离电网，完全依靠发电机运行，这种情况比较常见。Flexential 运营着 10 台发电机，包括冗余机组，能够在满负荷的情况下为设施提供支持。Flexential 公司也可以仅利用剩余的市电来运行该设施。他们为什么要同时使用市电和发电机供电，我们尚未得到明确的答案。

### 对后续事情的知情推测

从这个决定开始，我们还没有从 Flexential 那里弄清根本原因或他们做出的某些决定或发生的事件。在从 Flexential 和 PGE 处获得有关所发生事件的更多信息后，我们将更新这篇文章。以下部分内容是根据最有可能发生的一系列事件以及个别 Flexential 员工向我们透露的非官方信息做出的推测。

他们让市电线路继续运行的一个可能原因是，Flexential 是 PGE 一项名为 DSG 的计划的一部分。DSG 允许当地市电公司运行一个数据中心的发电机，帮助向电网提供额外电力。作为交换，电力公司帮助维护发电机并提供燃料。我们无法找到 Flexential 向我们通知 DSG 计划的任何记录。我们曾询问 DSG 计划当时是否处于执行状态，但尚未收到答复。我们不知道是否是这一计划促成了 Flexential 所做的决定，但它可以解释为什么在发电机启动后，市电线路仍然在线。

协调世界时 11:40 左右，PDX-04 的 PGE 变压器发生接地故障。我们认为（但尚未从 Flexential 或 PGE 得到证实），是为第二路电源电网降压的一台变压器发生了故障，而第二路电源在进入数据中心时仍在运行。虽然我们无法向 Flexential 或 PGE 确认，但接地故障很可能是 PGE 正在进行的计划外维护造成的，正是这一维护影响了第一路电源。又或者，这只是一个非常不幸的巧合。

高压（12,470 伏）电线的接地故障非常严重。电气系统设计为可在发生接地故障时迅速关闭，以防止损坏。不幸的是，在这种情况下，保护措施也关闭了 PDX-04 的所有发电机。这意味着该设施的两个发电来源——备用市电线路和 10 台发电机——均已断电。

幸运的是，除了发电机，PDX-04 还拥有一组 UPS 电池。据称，这些电池足以为该设施提供约 10 分钟的电力。这段时间足以弥补电力中断和发电机自动启动之间的差距。如果 Flexential 能在 10 分钟内恢复发电机或市电供电，那么就不会出现中断。但实际上，根据我们从自己的设备故障中观察到的情况，电池只用了 4 分钟就开始失效。而 Flexential 恢复发电机所花的时间远不止 10 分钟。

### 尝试恢复供电

虽然我们还没有得到官方证实，但员工告诉我们，有三件事阻碍了发电机的重新启动。首先，由于接地故障导致电路跳闸，因此需要实际进入并手动重新启动。其次，Flexential 的访问控制系统没有备用电池供电，因此处于离线状态。第三，现场的夜班人员中没有经验丰富的操作或电气专家——夜班人员包括保安和一名无人陪伴的技术人员，这名技术人员才刚刚上岗一周。

协调世界时 11:44 至 12:01 期间，由于发电机没有完全重新启动，UPS 电池耗尽，数据中心的所有客户都断电了。在整个过程中，Flexential 从未告知 Cloudflare 该设施存在任何问题。协调世界时 11:44，连接数据中心与世界其他地方的两台路由器离线，我们这才得知数据中心出现问题。当我们无法直接或通过带外管理访问路由器时，我们尝试联系 Flexential，并派遣我们的当地团队亲自前往该设施。协调世界时 12:28，Flexential 向我们发送了第一条表示他们遇到问题的消息。

>  _目前，我们的 [PDX-04] 遇到电源问题，该问题始于太平洋时间上午 05:00 [协调世界时 12:00] 左右 。工程师们正在积极解决问题，恢复服务。我们将每 30 分钟通报一次进展情况，或在获得更多信息时通报预计恢复时间。感谢您的耐心和理解。_

### 针对数据中心级故障所做的设计

虽然 PDX-04 的设计在施工前已通过 Tier III 认证，并有望提供高可用性 SLA，但我们仍计划了它可能离线的可能性。即使是运营良好的设施也会有不顺利的时候。我们也为此做了计划。如若发生此类事件，我们的预期情况是：我们的分析将处于离线状态，日志将在边缘排队并延迟，并且未集成到我们高可用性集群中的某些较低优先级服务将暂时离线，直到可以在另一个设施中恢复。

在该地区运行的另外两个数据中心将接管高可用性集群的责任，并保持关键服务在线。一般来讲，这可以按计划进行。不幸的是，我们发现本应在高可用性集群上运行的部分服务依赖于仅在 PDX-04 中运行的服务。

特别是，处理日志并为我们的分析提供支持的两个关键服务——Kafka 和 ClickHouse——仅在 PDX-04 中可用，但有依赖于它们的服务在高可用性集群中运行。这些依赖关系本不应该如此紧密，本应该更体面地失效，我们本应该发现这些依赖关系。

我们对高可用性集群进行过测试，将另外两个数据中心设施分别和同时完全关闭。我们还测试过将 PDX-04 的高可用性部分离线。但是，我们从未测试过完全关闭整个 PDX-04 设施。因此，我们忽略了数据平面上某些依赖关系的重要性。

在要求新产品及其关联数据库与高可用性集群集成方面，我们也过于松懈。Cloudflare 允许多个团队快速创新。因此，产品往往会以不同的方式进入初始测试阶段。虽然随着时间的推移，我们的做法是将这些服务的后端迁移到我们的最佳实践位置，但在产品宣布普遍可用 (GA) 之前，我们并没有正式要求这样做。这是一个错误，因为这意味着我们的备用保护措施会因产品不同而效果不一。

此外，我们有太多的服务依赖于核心设施的可用性。虽然这是许多软件服务的创建方式，但它并没有发挥 Cloudflare 的优势。我们擅长分布式系统。在整个事件过程中，我们的全球网络仍旧按预期运行。虽然我们的一些产品和功能可以通过网络边缘进行配置和维护，而无需核心，但如今，如果核心不可用，会有太多产品和功能失效。我们需要使用我们为所有客户提供的分布式系统产品来提供我们的所有服务，这样，即使我们的核心设施受到干扰，它们也能继续正常运行。

### 灾难恢复

协调世界时 12:48，Flexential 重新启动了发电机。设施内的部分场所恢复供电。为了避免系统不堪重负，当数据中心恢复供电时，通常是一次接通一条电路，逐步恢复供电。就像住宅中的电路断路器一样，每个客户都由冗余断路器提供服务。当 Flexential 试图重新启动 Cloudflare 的电路时，发现断路器出现故障。我们不知道断路器是由于接地故障或者是由于事故造成的其他浪涌而失灵，还是断路器之前就坏了，只是在断电后才被发现。

Flexential 开始更换故障断路器。这就要求他们采购新的断路器，因为坏的断路器比他们设施内现有的还要多。由于离线的服务比我们预期的要多，而且 Flexential 无法给出恢复服务的时间，因此在协调世界时 13:40，我们决定向 Cloudflare 位于欧洲的灾难恢复站点进行故障转移。值得庆幸的是，我们只需要对 Cloudflare 整体控制平面的一小部分进行故障转移。我们的大部分服务继续在两个运行中的核心数据中心的高可用性系统上运行。

协调世界时 13:43，我们在灾难恢复站点上启动了第一批服务。Cloudflare 的灾难恢复站点可在发生灾难时提供关键的控制平面服务。不过，灾难恢复站点不支持我们的某些日志处理服务，其旨在支持我们控制平面的其他部分。

在那里启动服务后，我们遇到了惊群问题，此前一直失败的 API 调用一下子使我们的服务不堪重负。我们实施了速率限制，以控制请求量。在此期间，大多数产品的客户在通过我们的仪表板或API 进行修改时都会出现间歇性错误。截至协调世界时 17:57，已成功转移到灾难恢复站点的服务趋于稳定，大多数客户不再受到直接影响。然而，在我们恢复 PDX-04 之前，一些系统仍然需要手动配置（如 Magic WAN），其他一些服务（主要与日志处理和一些定制 API 有关）仍然无法使用。

### 部分产品和功能延迟重启

在我们的灾难恢复站点上，有少数产品没有正常启动。这些往往是较新的产品，我们还没有完全实施和测试灾难恢复程序。其中包括我们用于上传新视频的 Stream 服务和其他一些服务。为了恢复这些服务，我们的团队同时开展了两项工作：1) 在我们的灾难恢复站点上重新实施这些服务；2) 将它们迁移到我们的高可用性集群。

Flexential 更换了发生故障的断路器，恢复了两路市电供应，并在协调世界时 22:48 确认电力供应正常。我们的团队全员到岗，在紧急情况下工作了一整天，因此我决定让我们大多数人休息一下，明天一早开始返回 PDX-04。这个决定推迟了我们的全面恢复，但我认为，它降低了我们因其他人为错误而使情况更加复杂的可能性。

从 11 月 3 日一早开始，我们的团队就开始在 PDX-04 恢复服务。首先是物理启动我们的网络设备，然后启动数千台服务器并恢复其服务。数据中心的服务状况尚不清楚，因为我们认为事件期间可能发生了多次电源循环。我们唯一安全的恢复程序就是对整个设施进行全面启动。

这需要人工将我们的配置管理服务器联机，以开始恢复设施。这个过程花了 3 个小时。之后，我们的团队就能够启动其余服务器的重建工作，为我们的服务提供动力。每台服务器的重建时间从 10 分钟到 2 小时不等。虽然我们可以对多台服务器同时执行这个过程，但服务之间存在固有的依赖性，需要按顺序恢复一些服务的运行。

截至协调世界时 2023 年 11 月 4 日 04:25，服务已全面恢复。由于我们还将分析数据存储在欧洲核心数据中心中，因此对于大多数客户而言，他们在我们的仪表板和 API 中的数据都不会有损失。然而，一些未在欧盟复制的数据集将存在持续的差距。对于使用我们的日志推送功能的客户，在事件持续的大部分时间里，您的日志都未得到处理，因此，您未收到的内容也将无法恢复。

### 教训和补救

我们有许多问题需要 Flexential 解答。但是，我们也必须预料到整个数据中心可能会发生故障。Google 有一个程序，当发生重大事件或危机时，他们可以发出“黄色警报”或“红色警报”。在这些情况下，大部分或所有工程资源都被转移到解决当前问题上。

我们过去没有这样的程序，但今天我们显然需要实施一个我们自己的版本：橙色警报。我们正在转移所有非关键工程功能，着重于确保控制平面的高可靠性。作为该过程的一部分，我们预计会有以下变化：

  * 消除所有服务的控制平面配置对核心数据中心的依赖，尽可能首先由我们的分布式网络提供动力
  * 确保即使我们所有的核心数据中心都处于离线状态，网络上运行的控制平面仍能继续运作
  * 要求所有指定为“普遍可用”的产品和功能必须依赖于高可用性集群（如果它们依赖于我们的任何核心数据中心），而不对特定设施有任何软件依赖
  * 要求所有指定为“普遍可用”的产品和功能都具有经过测试的可靠灾难恢复计划
  * 测试系统故障的影响范围，最大程度地减少受故障影响的服务数量
  * 对所有数据中心功能实施更严格的混沌测试，包括完全关闭我们的每个核心数据中心设施
  * 对所有核心数据中心进行彻底审计，并制定重新审计计划以确保它们符合我们的标准
  * 确立日志记录和分析灾难恢复计划，确保即使我们的所有核心设施都发生故障，也不会丢失任何日志



正如我之前所说，我对这次事件以及它给我们的客户和团队带来的痛苦感到抱歉和尴尬。我们已经建立了正确的系统和程序，能够承受我们在数据中心提供商处看到的一连串故障，但我们需要更加严格地执行这些系统和程序，并对未知的依赖性进行测试。在今年余下的时间里，我和我们团队的大部分成员都将全力以赴。过去几天的痛苦会让我们变得更好。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F&t=Cloudflare%20%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8A%A1%E4%B8%AD%E6%96%AD%E7%9A%84%E4%BA%8B%E5%90%8E%E5%88%86%E6%9E%90)[](https://x.com/intent/post?text=Cloudflare+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8A%A1%E4%B8%AD%E6%96%AD%E7%9A%84%E4%BA%8B%E5%90%8E%E5%88%86%E6%9E%90&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://bsky.app/intent/compose?text=Cloudflare+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8A%A1%E4%B8%AD%E6%96%AD%E7%9A%84%E4%BA%8B%E5%90%8E%E5%88%86%E6%9E%90+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://mastodonshare.com/?text=Cloudflare+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8A%A1%E4%B8%AD%E6%96%AD%E7%9A%84%E4%BA%8B%E5%90%8E%E5%88%86%E6%9E%90&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://www.threads.net/intent/post?text=Cloudflare+%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2%E5%92%8C%E5%88%86%E6%9E%90%E6%9C%8D%E5%8A%A1%E4%B8%AD%E6%96%AD%E7%9A%84%E4%BA%8B%E5%90%8E%E5%88%86%E6%9E%90+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)

## 相关标签

[中断](https://blog.cloudflare.com/zh-cn/tag/outage/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
