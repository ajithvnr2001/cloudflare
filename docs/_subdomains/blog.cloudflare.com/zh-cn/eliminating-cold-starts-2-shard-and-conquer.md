---
url: https://blog.cloudflare.com/zh-cn/eliminating-cold-starts-2-shard-and-conquer/
title: \u6d88\u9664\u51b7\u542f\u52a8\u95ee\u9898 2\uff1a\u5206\u7247\u653b\u514b\u6cd5 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:44.554349+00:00
---

# 消除冷启动问题 2：分片攻克法 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/eliminating-cold-starts-2-shard-and-conquer/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cap'n Proto](https://blog.cloudflare.com/zh-cn/tag/capn-proto/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)+2再显示 2 个标签

5 个标签显示 5 个标签

  * 文章标签
  * [Cap'n Proto](https://blog.cloudflare.com/zh-cn/tag/capn-proto/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)
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



[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)

[Cap'n Proto](https://blog.cloudflare.com/zh-cn/tag/capn-proto/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)

2025年9月26日

# 消除冷启动问题 2：分片攻克法

![Harris Hancock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H05HT7CQGVFMPCZBNF6H.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Harris Hancock](https://blog.cloudflare.com/zh-cn/author/harris-hancock/)

阅读时间：16 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/eliminating-cold-starts-2-shard-and-conquer/).

![BLOG-2971 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW484T9DE9T06QXYNTCGR8CT.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////Pz+8/Lz7Ovs6+vw7e717O306Oju/////v7/9PPz6+rs6Ojv6ur06+z06urv////////9vb16+ru5ubw6On17Oz27u7x////////+vr57u7x6urz7Oz48fH58/P1////////////9vb38/P59vX++fj++fn6/////////////v/+/v7///////////7+////////////////////////////////////////////////////////////////)

五年前，我们宣布我们[ _利用 Cloudflare Workers 消除冷启动_](https://blog.cloudflare.com/eliminating-cold-starts-with-cloudflare-workers/)。在那篇文章中，我们介绍了一种在 Workers 首次请求的 [_TLS 握手_](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)期间预热 Workers 的技术。该技术利用了 [_TLS 服务器名称指示 (SNI)_](https://www.cloudflare.com/learning/ssl/what-is-sni/) 在 TLS 握手的第一个消息中发送这一事实。有了 SNI，我们通常就掌握了足够的信息来预热请求的目标 Worker。

通过在 TLS 握手期间预热 [_Workers_](https://www.cloudflare.com/developer-platform/products/workers/) 来消除冷启动对我们来说是一个巨大的进步，但“消除”这个词用得有点夸张。当时，Workers 的规模还相对较小，冷启动也受到一些限制（本文后面将进行解释）。现在我们已经放宽了这些限制，用户经常在 Workers 上部署复杂的应用程序，并且经常用 Workers 来替代源服务器。与此同时，TLS 握手的速度并没有变慢。事实上，[ _TLS 1.3_](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3/) 只需要一次往返即可完成握手（相比之下，TLS 1.2 需要三次往返），而且它的使用范围比 2021 年更广。

本月初，我们完成了一项新技术的部署，旨在进一步提升冷启动缩减的性能。这项新技术（或者说旧技术，取决于您的视角）利用一致性哈希环来充分利用我们的全球[ _网络_](https://www.cloudflare.com/network)。我们将这种机制称为“Worker 分片”。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46CGHDEQ0Q01G067YGQ2MY.png&w=715&h=337&f=webp&fit=cover&position=center)

### 什么是冷启动？

Worker 是我们[ _无服务器计算_](https://www.cloudflare.com/learning/serverless/what-is-serverless/)平台的基本计算单元。它的生命周期很简单。我们从源代码（通常是 JavaScript）实例化它，让它处理一系列请求（通常是 HTTP 请求，但不总是如此），并在它停止接收流量一段时间后将其关闭，以便将其资源重新分配给其他 Worker。我们将这个关闭过程称为“驱逐”。

Worker 生命周期中最耗时的部分是初始实例化和首次请求调用。我们称这部分为“冷启动”。冷启动包含几个阶段：获取脚本源代码、编译源代码、执行生成的 JavaScript 模块的顶层代码，以及最终执行首次请求以处理触发整个事件序列的传入 HTTP 请求。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46WDGQ7QE827RW2Z0S3ZZ4.png&w=715&h=520&f=webp&fit=cover&position=center)

### 冷启动已变得比 TLS 握手更长

从根本上讲，我们的 TLS 握手技术依赖于握手持续时间长于冷启动时间。这是因为无论如何，TLS 握手的持续时间都是访问者必须等待的时间，因此，如果我们在这段时间内尽可能多地执行工作，对所有人都有好处。如果我们能在握手仍在进行时在后台运行 Worker 的冷启动，并且冷启动在握手完成 _之前_ 完成，那么请求最终将不会感受到任何冷启动延迟。另一方面，如果冷启动持续时间 _长于_ TLS 握手，那么请求将感受到一部分冷启动延迟——尽管该技术仍然有助于减少这种可见的延迟。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW476B6XQSEFQ7EKYG3D4K4G.png&w=715&h=528&f=webp&fit=cover&position=center)

在早期阶段，TLS 握手耗时超过 Worker 冷启动时间几乎是板上钉钉的事，而冷启动通常会更快完成。在我们早期的一篇[ _解释平台工作原理的博客文章_](https://blog.cloudflare.com/cloud-computing-without-containers/#cold-starts)中曾提到冷启动时间为 5 毫秒——这在当时确实是准确的！

对于我们设置的每一项限制，用户都会要求我们放宽。冷启动时间也不例外。

影响冷启动时间的两个关键限制是：Worker 脚本大小和启动 CPU 时间限制。虽然我们当时没有大张旗鼓地宣布，但自上一篇博文 _《消除冷启动》_ 发布以来，我们已经悄悄提高了这两个限制：

  * 对于付费用户，Worker 脚本大小（压缩后）从 [_1 MB 增加到 5 MB_](https://github.com/cloudflare/cloudflare-docs/pull/6613)，然后再次从 [_5 MB 增加到 10 MB_](https://github.com/cloudflare/cloudflare-docs/pull/9083)。
  * 对于免费用户，Worker 脚本大小（压缩后）从 [_1 MB 增加到 3 MB_](https://github.com/cloudflare/cloudflare-docs/pull/18400)。
  * 启动 CPU 时间从 [_200 毫秒增加到 400 毫秒_](https://github.com/cloudflare/cloudflare-docs/pull/9154)。



我们放宽了这些限制，因为我们的用户希望在我们的平台上部署越来越复杂的应用程序。他们也确实这样做了！但这些增加是有代价的：

  * 增加脚本大小会增加我们必须从脚本存储传输到 Workers 运行时的数据量。
  * 增加脚本大小也会增加脚本编译阶段的脚本编译时间复杂度。
  * 增加启动 CPU 时间限制会增加最大顶层执行时间。



综合来看，复杂应用程序的冷启动开始在 TLS 握手竞赛中落败。

### 将请求路由到现有 Worker

由于脚本大小和启动时间限制放宽，直接优化冷启动时间收效甚微。因此，我们需要找到减少冷启动绝对 _次数_ 的方法，从而降低请求发生冷启动的概率。

一种方法是将请求路由到现有的 Worker 实例，而以前我们可能会选择启动一个新实例。

之前，我们不太擅长将请求路由到现有的 Worker 实例。如果请求恰好落在已经运行着 Worker 的机器上，我们可以轻松地将请求合并到同一个 Worker 实例，因为在这种情况下，这不是分布式系统的问题。但是，如果我们的数据中心里另一台服务器上已经存在一个 Worker，而另一台服务器收到了对该 Worker 的请求呢？我们总是会选择在收到请求的机器上冷启动一个新的 Worker，而不是将请求转发到已经运行着 Worker 的机器上，即使转发请求可以避免冷启动。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47HJDB1527GM95E8PJ0X9F.png&w=715&h=410&f=webp&fit=cover&position=center)

为了更清楚地说明这一点：假设一位访客每分钟向一个拥有 300 台服务器的数据中心发送一个请求，并且流量在所有服务器上均匀分配。平均而言，每台服务器每五小时会收到一个请求。在特别繁忙的数据中心，这个时间间隔可能足够长，以至于我们需要将 Worker 进程驱逐出去以重新利用其资源，从而导致 100% 的冷启动率。这对访客来说体验非常糟糕。

因此，我们不得不向那些在应用原型测试阶段遇到高延迟的用户解释，一旦他们向我们的网络发送足够的流量，延迟反而会 _降低_ ，这与他们的直觉相悖。这凸显了我们最初简单设计的低效之处。

如果将这些请求合并到一台服务器上，我们将看到诸多好处。该 Worker 每分钟会收到一个请求，如此短的时间几乎可以保证它不会被驱逐。这意味着访客可能只会经历一次冷启动，之后便能享受 100% 的“热请求率”。同时，我们还能节省 99.7% (299/300) 的内存来处理这些流量。这为其他 Worker 腾出了空间，降低了它们的驱逐率，并提高了 _它们的_ 热请求率，从而形成良性循环！

不过，将请求合并到单个实例上也是有代价的，对吧？毕竟，如果我们需要将请求代理到数据中心的另一台服务器上，就会增加请求的延迟。

实际上，增加的首字节时间不到一毫秒，我们的进程间通信 (IPC) 和性能团队一直在持续优化这一指标。一毫秒远小于典型的冷启动时间，这意味着无论从哪个方面衡量，将请求代理到已启动的 Worker 都比冷启动一个新的 Worker 要好。

### 一致性哈希环

解决这个问题的方法正是我们许多产品的核心，包括我们最古老的功能之一：我们[ _内容分发网络_](https://www.cloudflare.com/application-services/products/cdn/)中的 HTTP 缓存。

当访客通过 Cloudflare 请求可缓存的 Web 资源时，该请求会经过一系列代理服务器。其中一个代理服务器是缓存代理，它会将资源存储起来以供后续使用，这样我们无需再次从源服务器请求资源，就可将其提供给未来的请求。

Worker 的冷启动类似于 HTTP 缓存未命中，因为向一个已启动的 Worker 发出的请求就像 HTTP 缓存命中一样。

当我们的标准 HTTP 代理管道将请求路由到缓存层时，它会根据请求的缓存键选择一个缓存服务器，以优化 HTTP 缓存命中率。[ _缓存键是请求的 URL 加上一些其他信息_](https://developers.cloudflare.com/cache/how-to/cache-keys/)。这种技术通常被称为“分片”。服务器被视为一个更大的逻辑系统（在本例中是数据中心的 HTTP 缓存）的各个分片。因此，我们可以这样说：“每个数据中心包含一个逻辑 HTTP 缓存，并且该缓存分片分布在数据中心的每个服务器上。”

直到最近，我们还无法对数据中心中的 Worker 集合做出同样的论断。过去，每台服务器都包含其自身独立的 Worker 集合，它们很容易重复执行任务。

我们借鉴了缓存的技巧来解决这个问题。实际上，我们甚至使用了与 HTTP 缓存相同的数据结构来选择服务器：一个[ _一致性哈希环_](https://en.wikipedia.org/wiki/Consistent_hashing)。一个简单的分片实现可能会使用经典的哈希表，将 Worker 脚本 ID 映射到服务器地址。对于一组永不改变的服务器来说，这当然没问题。但服务器实际上是短暂的，它们有自己的生命周期。它们可能会崩溃、重启、维护或退役。新的服务器也会上线。当这些事件发生时，哈希表的大小会发生变化，需要重新对整个表进行哈希处理。每个 Worker 的“主服务器”都会改变，所有分片的 Worker 都需要重新冷启动！

使用一致性哈希环可以显著改善这种情况。我们不再直接建立脚本 ID 和服务器地址之间的对应关系，而是将它们映射到一条首尾相连的数轴上，也就是一个环。要查找 Worker 的根服务器，首先对其脚本进行哈希运算，然后找到它在环上的位置。接下来，我们找到环上该位置之后或紧邻的服务器地址，并将其视为该 Worker 的根服务器。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4627CWMGKN1YPQKJVDNZNB.png&w=715&h=440&f=webp&fit=cover&position=center)

如果出于某种原因新增了一台服务器，那么哈希环上位于该服务器之前的所有 Worker 都会被重新分配（即迁移到新的目标服务器），但其他 Worker 不受影响。同样地，如果某台服务器下线，哈希环上位于该服务器之前的所有 Worker 也会被重新分配。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VWG7EBY9N9BNGFTWT2S7.png&w=715&h=440&f=webp&fit=cover&position=center)

我们将 Worker 的归属服务器称为“分片服务器”。在涉及分片的请求流程中，还存在一个“分片客户端”。它同样是一台服务器！分片客户端首先接收到请求，然后利用其一致性哈希环查找应将请求发送至哪个分片服务器。在本文后续内容中，我将使用“分片客户端”和“分片服务器”这两个术语。

### 处理过载

HTTP 资源的特性使其非常适合进行分片处理。如果这些资源可缓存，那么至少在其缓存[ _生存时间 (TTL)_](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/) 期间，它们是静态的。因此，对这些资源的处理所需的时间复杂度和空间复杂度与其大小呈线性关系。

但 Worker 并非 JPEG 图片那样的静态资源。它们是实时运行的计算单元，每个请求最多可使用五分钟的 CPU 时间。其时间和空间复杂度并不一定与输入数据量成正比，甚至可能远超我们为提供缓存中的超大文件所需投入的计算资源量。

这意味着，当单个 Worker 接收到足够大的流量时，很容易出现过载的情况。因此，无论我们采取何种措施，都必须牢记：系统必须具备无限扩容的能力。我们永远无法保证某个数据中心中只运行一个 Worker 实例，并且必须随时能够快速实现水平扩展，以应对突发流量。理想情况下，这一切都应该在不产生任何错误的前提下完成。

这意味着，分片服务器必须具备拒绝在其上调度 Worker 请求的能力，同时分片客户端也必须始终能够优雅地处理此类情况。

### 两种负载削减方案

我了解到有两种通用的解决方案，可以在避免返回错误的前提下，优雅地实现负载削减。

在第一种解决方案中，客户端会礼貌地询问是否可以发出请求。如果收到肯定响应，它便会发送该请求；反之，若收到“请勿访问”（即拒绝）响应，则会采用其他方式处理该请求，例如在本地提供服务。在 HTTP 协议中，这种模式体现在 [_Expect: 100-continue 语义_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/100)里。该方案的主要缺点在于，为了在发送请求前确认能否成功（即设置成功预期），会额外引入一次往返延迟。（请注意，一种常见的简单做法是直接重试请求。这种方法对某些类型的请求虽能奏效，但并非通用解决方案，因为请求可能携带任意大小的请求体。）

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46WHBSXKWD989MKXFD5CGB.png&w=715&h=323&f=webp&fit=cover&position=center)

第二种常见解决方案是：客户端直接发送请求，而不事先确认服务器是否能够处理该请求，之后再依赖服务器在必要时将请求转发至其他地方进行处理。这甚至可能将请求转发回客户端自身。这种方式避免了第一种方案所引入的往返延迟，但也存在权衡考量：它会使分片服务器介入请求路径，从而将数据字节回传给客户端。幸运的是，我们有一项技巧能够最大程度地减少以这种方式实际需要回传的字节数量，我将在下一节中详细介绍该技巧。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CAGN975G6WHWYMEYY1N2.png&w=715&h=317&f=webp&fit=cover&position=center)

### 乐观式分片请求发送

我们选择不经许可就乐观式发送分片请求，主要基于以下几点原因。

首要原因是，在实际应用中，我们预计这类被拒绝的请求极少出现。原因很简单：如果分片客户端收到某个 Worker 的拒绝响应，那么它就必须在本地冷启动该 Worker。如此一来，后续所有请求都可在本地处理，无需再次经历冷启动过程。所以，在经历一次拒绝后，分片客户端就不会再对该 Worker 进行分片处理了（至少在针对该 Worker 的流量减少到足以触发驱逐之前不会）。

通常情况下，这意味着我们预期如果请求被分片到不同的服务器，分片服务器很可能会接受该请求并执行调用。由于我们预期请求会成功，因此将整个请求乐观地发送到分片服务器比先建立权限而产生往返开销要合理得多。

第二个原因是，正如我上面提到的，我们有一个技巧可以避免为将请求代理回客户端支付过高的费用。

我们在 Workers 运行时中通过 [_Cap’n Proto RPC_](https://capnproto.org/) 实现跨实例通信，其分布式对象模型支持一些卓越的功能，例如 [_JavaScript 原生 RPC_](https://blog.cloudflare.com/javascript-native-rpc/)。它也是刚刚发布的 [_Cap’n Web_](https://blog.cloudflare.com/capnweb-javascript-rpc-library/) 的前辈，可谓精神上的“兄弟项目”。

对于分片，Cap’n Proto 使得实现最优的请求拒绝机制变得非常简单。当分片客户端组装分片请求时，它会包含一个句柄（在 Cap’n Proto 中[ _称为 _“能力_ ”_](https://capnproto.org/rpc.html#distributed-objects)），指向一个延迟加载的本地 Worker 实例。这个延迟加载的实例[ _与任何其他通过 RPC 公开的 Worker 具有完全相同的接口_](https://github.com/cloudflare/workerd/blob/f93fd2625f8d4131d9d50762c09deddb01bb4c70/src/workerd/io/worker-interface.capnp#L582)。区别仅在于它是延迟加载的——它直到被调用才会冷启动。如果分片服务器决定拒绝该请求，它不会返回“请勿访问”响应，而是返回分片客户端自身的延迟加载能力！

分片客户端的应用程序代码只能看到它从分片服务器接收到了一个能力，但并不知道这个能力实际实现在哪里。然而，分片客户端的 _RPC 系统_ 却知道这个能力的所在位置！具体来说，它识别出返回的能力实际上是一个本地能力——正是它传递给分片服务器的那个。一旦意识到这一点，它也就明白，继续向分片服务器发送任何请求字节都会导致循环。因此，它会停止发送更多的请求字节，等待从分片服务器接收所有已发送的字节，并尽快缩短请求路径。这样就完全将分片服务器从循环中移除，从而避免了“长号效应”。

### Workers 调用 Workers

在确定了负载削减策略后，我们原以为最难的部分已经过去了。

当然，Worker 可以调用其他 Worker。这可以通过多种方式实现，最显而易见的是通过[ _服务绑定_](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)。不太明显的是，我们许多喜爱的功能，例如 [_Workers KV_](https://developers.cloudflare.com/kv/)，实际上也是跨 Worker 调用。但有一个产品因其强大的调用其他 Worker 的能力而格外突出：[ _Workers for Platforms_](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)。

Workers for Platforms 允许您在 Cloudflare 基础设施上运行您自己的函数即服务。要使用该产品，您需要部署三种特殊类型的 Workers：

  * 一个动态分派 Worker
  * 任意数量的用户 Worker
  * 可选的参数化 [_Outbound Workers_](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/)



Workers for Platforms 的典型请求流程如下：首先，系统会调用动态分发 Worker；接着，动态分发 Worker 会选择并调用一个用户 Worker；随后，该用户 Worker 会调用 Outbound Worker 来拦截其子请求。需要注意的是，动态分发 Worker 在调用用户 Worker 之前，就已经选定了 Outbound Worker 的参数。

为了增加趣味性，动态分发 Worker 可以附加一个 [_Tail Worker_](https://developers.cloudflare.com/workers/observability/logs/tail-workers/)。这个 Tail Worker 需要使用与之前所有调用相关的跟踪信息进行调用。需要注意的是，它应该仅被调用一次，并且传入与该请求流相关的所有事件，而不是针对请求流的不同片段多次调用。

您可能还会问：Workers for Platforms 可以嵌套吗？我不知道官方答案，但我可以告诉您，代码路径确实存在，而且它们确实会被执行。

为了支持这种嵌套式的 Workers，我们在调用期间维护一个上下文栈。该上下文包含所有权覆盖、资源限制覆盖、信任级别、Tail Worker 配置、Outbound Worker 配置、功能标志等信息。当所有操作都在单个线程上执行时，这个上下文栈还算易于管理。但是，为了真正发挥分片的作用，我们需要能够将这个上下文栈迁移到其他机器上。

我们选择 Cap’n Proto RPC 作为主要通信媒介，这有助于我们理解整个流程。为了在调用栈深处对 Workers 进行分片，我们将上下文栈序列化为 Cap’n Proto 数据结构，并将其发送到分片服务器。分片服务器将其反序列化为原生对象，并从中断处继续执行。

和负载削减的解决方案一样，Cap’n Proto 的分布式对象模型也为我们原本棘手的问题提供了简单的答案。就拿 Tail Worker 的问题来说，当调用请求被分散到任意数量的其他服务器上时，我们该如何将这些调用产生的追踪数据汇总到一个地方呢？很简单：在动态分发 Worker 的归属服务器上为 reportTraces() 回调函数创建一个能力（一个实时 Cap’n Proto 对象），然后把这个能力放入序列化的上下文栈中。现在，这个上下文栈可以随意传递。它最终会出现在多个地方：至少会出现在用户 Worker 的分片服务器和 Outbound Worker 的分片服务器上。如果这些 Worker 中的任何一个调用了服务绑定，它还可能传播到其他分片服务器上！每个分片服务器都可以调用 reportTraces() 回调函数，并且可以放心，这些数据一定会回到正确的地方——动态分发 Worker 的归属服务器。而且，这些分片服务器都不需要确切知道归属服务器的 _位置_ 。呼，问题解决啦！

### 驱逐率下降，热请求率上升

推出此类功能总是令人欣喜，因为它们会生成图表，显示效率大幅提升。

全面部署后，企业流量中只有约 4% 的请求最终进行了分片。换句话说，96% 的企业请求都发送到负载过重的 Worker，以至于我们 _必须_ 在数据中心运行多个 Worker 实例。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VC8RT4YQ1XP5CEPW7NTN.png&w=715&h=322&f=webp&fit=cover&position=center)

尽管分片总率很低，但我们的全局 Worker 驱逐率降低了 10 倍。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XNXQK9WT7W2A7MF8ND8F.png&w=715&h=323&f=webp&fit=cover&position=center)

我们的驱逐率衡量的是系统内存压力。您可以将其理解为宏观层面的垃圾回收，其意义也相同。驱逐次数越少，意味着系统内存使用效率越高。这带来的一个好处是，用于清理内存的 CPU 资源消耗更少。对于 Workers 用户而言，效率的提升意味着我们可以让 Workers 在内存中停留更长时间，从而提高其热请求率并降低延迟。

我们所展现出的显著成效——仅需对 4% 的流量进行分片处理，就能将内存效率提升 10 倍——这一结果源于互联网流量遵循幂律分布的特性。

[ _幂律分布_](https://en.wikipedia.org/wiki/Power_law)是一种在许多科学领域都存在的现象，包括语言学、社会学、物理学，当然还有计算机科学。遵循幂律分布的事件通常表现为：大量数据集中在少数几个“区间”内，其余数据则分散在许多其他“区间”中。词频就是一个经典的例子：像“the”、“and”和“it”这样的少数几个词在文本中出现的频率极高，而像“eviction”或“trombone”这样的词可能在文本中只出现一两次。

在我们的案例中，绝大多数 Workers 请求都分配给了少数几个高流量 Worker，而极少数请求则分配给了数量庞大的低流量 Worker。被分片的 4% 请求全部分配给了低流量 Worker，这些 Worker 正是分片的最大受益者。

那么，我们真的消除冷启动问题了吗？还是说，未来我们还会迎来 _《消除冷启动 3》_ 呢？

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2971 image 11](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46E3SVPQQECYDMP7BRCX56.png&w=715&h=320&f=webp&fit=cover&position=center)

对于企业流量，我们的热请求率从 99.9% 提升至 99.99%——也就是从三个 9 提升至四个 9。反过来，这意味着冷启动率从 0.1% 降至 0.01%，下降了 10 倍。稍加思考，您就会发现这与我上面分享的驱逐率图表相符：随着时间的推移，我们销毁的 Worker 数量减少了 10 倍，这意味着我们最初创建的 Worker 数量也减少了 10 倍。

与此同时，我们的热请求率在一天中波动性降低。

嗯。

虽然我不愿意承认这一点，但我仍然注意到图表顶部还有一点空白。😟

[ _您能帮助我们达到五个 9 的目标吗？_](https://www.cloudflare.com/careers/)

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Feliminating-cold-starts-2-shard-and-conquer%2F&t=%E6%B6%88%E9%99%A4%E5%86%B7%E5%90%AF%E5%8A%A8%E9%97%AE%E9%A2%98%202%EF%BC%9A%E5%88%86%E7%89%87%E6%94%BB%E5%85%8B%E6%B3%95)[](https://x.com/intent/post?text=%E6%B6%88%E9%99%A4%E5%86%B7%E5%90%AF%E5%8A%A8%E9%97%AE%E9%A2%98+2%EF%BC%9A%E5%88%86%E7%89%87%E6%94%BB%E5%85%8B%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Feliminating-cold-starts-2-shard-and-conquer%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Feliminating-cold-starts-2-shard-and-conquer%2F)[](https://bsky.app/intent/compose?text=%E6%B6%88%E9%99%A4%E5%86%B7%E5%90%AF%E5%8A%A8%E9%97%AE%E9%A2%98+2%EF%BC%9A%E5%88%86%E7%89%87%E6%94%BB%E5%85%8B%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Feliminating-cold-starts-2-shard-and-conquer%2F)[](https://mastodonshare.com/?text=%E6%B6%88%E9%99%A4%E5%86%B7%E5%90%AF%E5%8A%A8%E9%97%AE%E9%A2%98+2%EF%BC%9A%E5%88%86%E7%89%87%E6%94%BB%E5%85%8B%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Feliminating-cold-starts-2-shard-and-conquer%2F)[](https://www.threads.net/intent/post?text=%E6%B6%88%E9%99%A4%E5%86%B7%E5%90%AF%E5%8A%A8%E9%97%AE%E9%A2%98+2%EF%BC%9A%E5%88%86%E7%89%87%E6%94%BB%E5%85%8B%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Feliminating-cold-starts-2-shard-and-conquer%2F)

## 相关标签

[Cap'n Proto](https://blog.cloudflare.com/zh-cn/tag/capn-proto/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[TLS](https://blog.cloudflare.com/zh-cn/tag/tls/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[生日周](https://blog.cloudflare.com/zh-cn/tag/birthday-week/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
