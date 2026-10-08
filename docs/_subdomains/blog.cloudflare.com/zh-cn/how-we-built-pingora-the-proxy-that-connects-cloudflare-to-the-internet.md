---
url: https://blog.cloudflare.com/zh-cn/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/
title: \u5c06 Cloudflare \u8fde\u63a5\u5230\u4e92\u8054\u7f51\u7684\u4ee3\u7406\u2014\u2014Pingora \u7684\u6784\u5efa\u65b9\u5f0f | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:50:31.479262+00:00
---

# 将 Cloudflare 连接到互联网的代理——Pingora 的构建方式 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/

[博客](https://blog.cloudflare.com/zh-cn/)

[NGINX](https://blog.cloudflare.com/zh-cn/tag/nginx/)[Pingora](https://blog.cloudflare.com/zh-cn/tag/pingora/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)+1再显示 1 个标签

4 个标签显示 4 个标签

  * 文章标签
  * [NGINX](https://blog.cloudflare.com/zh-cn/tag/nginx/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[性能](https://blog.cloudflare.com/zh-cn/tag/performance/)
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



[性能](https://blog.cloudflare.com/zh-cn/tag/performance/)

[NGINX](https://blog.cloudflare.com/zh-cn/tag/nginx/)[Pingora](https://blog.cloudflare.com/zh-cn/tag/pingora/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[性能](https://blog.cloudflare.com/zh-cn/tag/performance/)

2022年9月14日

# 将 Cloudflare 连接到互联网的代理——Pingora 的构建方式

![Yuchen Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CEA1K0ZA59ZK5J7QNRVF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yuchen Wu](https://blog.cloudflare.com/zh-cn/author/yuchen/)和[Andrew Hauck](https://blog.cloudflare.com/zh-cn/author/andrew-hauck/)

阅读时间：10 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/)和[繁體中文](https://blog.cloudflare.com/zh-tw/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/).

![How we built Pingora, the proxy that connects Cloudflare to the Internet](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45YKTPTHGN3EXA0YGTQDVW.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAfgAAfgAAfwAAfQAAdgAAbAAAXwAAVAAAm2A/nFxBn1pJoWFXn21hlm5fhlpJdScSvJZ0vZN1wJB5xJeFxaOQvaSOrJB5l2pT2byR2bmQ27WT37qd4cWo28eny7WTt5Vx79ed7tOd7s6e8NCl8tmu7tyt4s6e0bWE/+ig/eSf+t2e+d2i+uOn+ean8d2e5c2Q//Gd/+2c/+Wa/OKa/eac/uqd+eWa8tuW//Sb//Ca/+iY/eSW/ueX/+qY/OiY9uCX)

## 简介

今天，我们很高兴有机会在此介绍 Pingora，这是我们使用 [Rust](https://www.rust-lang.org/) 在内部构建的新 HTTP 代理，它每天处理超过 1 万亿个请求，提高了我们的性能，并为 Cloudflare 客户带来了许多新功能，同时只需要我们以前代理基础架构的三分之一的 CPU 和内存资源。

随着 Cloudflare 规模的扩大，我们已经超越了 NGINX 的处理能力。多年来它一直运作良好，但随着时间的推移，它在我们规模上的局限性意味着我们有必要构建一些新的东西。我们无法再获得我们所需要的性能，NGINX 也没有我们在非常复杂的环境中所需要的功能。

许多 Cloudflare 客户和用户使用 Cloudflare 全球网络作为 HTTP 客户端（例如 Web 浏览器、应用程序、物联网设备等）和服务器之间的代理。过去，对于浏览器和其他用户代理如何连接到我们的网络，我们已进行过许多讨论，我们开发了很多技术并实施了新协议（参见 [QUIC](https://blog.cloudflare.com/the-road-to-quic/) 和 [http2 优化](https://blog.cloudflare.com/delivering-http-2-upload-speed-improvements/)）来使这段连接更高效。

今天，我们将关注这个等式的另一部分：代理我们的网络和互联网上服务器之间的流量的服务。这个代理服务为我们的 CDN、Workers fetch、Tunnel、Stream、R2 以及许多其他功能和产品提供了动力。

让我们研究为什么我们选择取代我们的旧版服务以及 Pingora 的开发过程，这是我们专门为 Cloudflare 的客户用例和规模而设计的新系统。

## 为什么要再建一个代理

这些年来，我们对 NGINX 的使用遇到了限制。对于部分限制，我们进行了优化或选择绕过它们。但另一些限制则更难克服。

### 架构的限制损害了性能

NGINX [worker（进程）架构](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)对于我们的用例而言存在操作缺陷，这会损害我们的性能和效率。

首先，在 NGINX 中，每个请求只能由单个 worker 处理。这会导致[所有 CPU 内核之间的负载不平衡](https://blog.cloudflare.com/the-sad-state-of-linux-socket-balancing/)，从而[导致速度变慢](https://blog.cloudflare.com/keepalives-considered-harmful/)。

由于这种请求进程锁定效应，执行 [CPU 繁重](https://blog.cloudflare.com/the-problem-with-event-loops/)或[阻止 IO 任务](https://blog.cloudflare.com/how-we-scaled-nginx-and-saved-the-world-54-years-every-day/)的请求可能会减慢其他请求的速度。正如这些博客文章所表明的那样，我们已经花了很多时间来解决这些问题。

对于我们的用例来说，最关键的问题是糟糕的连接重用。我们的机器与原始服务器建立 TCP 连接，以代理 HTTP 请求。连接重用通过重用之前从连接池建立的连接，跳过新连接所需的 TCP 和 TLS 握手，来加快请求的 TTFB（首字节时间）。

但是，[NGINX 连接池](https://www.nginx.com/blog/load-balancing-with-nginx-plus-part-2/)与单个 worker 相对应。当请求到达某个 worker 时，它只能重用该 worker 内的连接。当我们添加更多 NGINX worker 以进行扩展时，我们的连接重用率会变得更差，因为连接分散在所有进程的更多孤立的池中。这导致更慢的 TTFB 以及需要维护更多连接，进而消耗我们和客户的资源（和金钱）。

正如在过去的博客文章中所提到的，我们为其中一些问题提供了解决方法。但如果我们能够解决根本问题：worker/进程模型，我们将自然而然地解决所有这些问题。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1310 Embedded Image - NQxBHe](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464BC4Q68PMNGE1GG5MDZ7.png&w=715&h=304&f=webp&fit=cover&position=center)

**有些类型的功能难以添加**

NGINX 是一个非常好的 Web 服务器、负载均衡器或简单的网关。但 Cloudflare 的作用远不止于此。我们过去常常围绕 NGINX 构建我们需要的所有功能，但要尽量避免与 NGINX 上游代码库有太多分歧，这并不容易。

例如，当[重试请求/请求失败](https://blog.cloudflare.com/new-tools-to-monitor-your-server-and-avoid-downtime/)时，有时我们希望将请求发送到具有不同请求标头集的不同源服务器。但 NGINX 并不允许执行此操作。在这种情况下，我们需要花费时间和精力来解决 NGINX 的限制。

同时，我们被迫使用的编程语言并没有帮助缓解这些困难。NGINX 纯粹是用 C 语言编写的，这在设计上不是内存安全的。使用这样的第 3 方代码库非常容易出错。即使对于经验丰富的工程师来说，也很容易陷入[内存安全问题](https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/)，我们希望尽可能避免这些问题。

我们用来补充 C 语言的另一种语言是 Lua。它的风险较小，但性能也较差。此外，在处理复杂的 Lua 代码和业务逻辑时，我们经常发现自己缺少[静态类型](https://en.wikipedia.org/wiki/Type_system#Static_type_checking)。

而且 NGINX 社区也不是很活跃，开发往往是[“闭门造车”](https://dropbox.tech/infrastructure/how-we-migrated-dropbox-from-nginx-to-envoy)。

**选择建立我们自己的**

在过去的几年里，随着我们的客户群和功能集的持续增长，我们持续评估了三种选择：

  1. 继续投资 NGINX，向其付款进行定制，使其 100% 满足我们的需求。我们拥有所需的专业知识，但鉴于上述架构限制，需要付出大量努力才能以完全支持我们需求的方式重建它。
  2. 迁移到另一个第三方代理代码库。肯定有好的项目，比如 [envoy](https://dropbox.tech/infrastructure/how-we-migrated-dropbox-from-nginx-to-envoy) 和[其他一些](https://linkerd.io/2020/12/03/why-linkerd-doesnt-use-envoy/)。但这条道路意味着在几年内可能会重复同样的循环。
  3. 从头开始建立一个内部平台和框架。这一选择需要在工程方面进行最大的前期投资。



在过去的几年中，我们每个季度都会对这些选项进行评估。没有明显的公式来判断哪种选择是最好的。在几年的时间里，我们继续走阻力最小的道路，继续增强 NGINX。然而，在某些情况下，建立自有代理的投资回报率似乎更值得。我们呼吁从头开始建立一个代理，并开始设计我们梦想中的代理应用程序。

## Pingora 项目

### 设计决定

为了打造一个每秒提供数百万次请求且快速、高效和安全的代理，我们必须首先做出一些重要的设计决定。

我们选择 [Rust](https://www.rust-lang.org/) 作为项目的语言，因为它可以在不影响性能的情况下以内存安全的方式完成 C 语言可以做的事情。

尽管有一些很棒的现成第 3 方 HTTP 库，例如 [hyper](https://github.com/hyperium/hyper)，我们选择构建自己的库是因为我们希望最大限度地提高处理 HTTP 流量的灵活性，并确保我们可以按照自己的节奏进行创新。

在 Cloudflare，我们处理整个互联网的流量。我们必须支持许多奇怪且不符合 RFC 的 HTTP 流量案例。这是 HTTP 社区和 Web 中的一个常见困境，在严格遵循 HTTP 规范，和适应潜在遗留客户端或服务器的广泛生态系统的细微差别之间存在矛盾和冲突，需要在其中作出艰难抉择。

HTTP 状态码在 [RFC 9110 中定义为一个三位整数](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes)，通常预期在 100 到 599 的范围内。Hyper 就是这样一种实现。但是，许多服务器支持使用 599 到 999 之间的状态代码。我们为此功能创建了一个[问题](https://github.com/hyperium/http/issues/144)，探讨了争论的各个方面。虽然 hyper 团队最终确实接受了这一更改，但他们有充分的理由拒绝这样的要求，而这只是我们需要支持的众多不合规行为案例之一。

为了满足 Cloudflare 在 HTTP 生态系统中的地位要求，我们需要一个稳健、宽容、可定制的 HTTP 库，该库可以在互联网的各种风险环境中生存，并支持各种不合规的用例。保证这一点的最佳方法就是实施我们自己的架构。

下一个设计决策关于我们的工作负载调度系统。我们选择多线程而不是[多处理](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/#Inside-the-NGINX-Worker-Process)，以便轻松共享资源，尤其是连接池。我们认为还需要实施[工作窃取](https://en.wikipedia.org/wiki/Work_stealing)来避免上面提到的某些类别的性能问题。Tokio 异步运行时结果[非常适合](https://tokio.rs/blog/2019-10-scheduler)我们的需求。

最后，我们希望我们的项目直观且对开发人员友好。我们构建的不是最终产品，而是应该可以作为一个平台进行扩展，因为在它之上构建了更多的功能。我们决定实施一个[类似于 NGINX/OpenResty](https://openresty-reference.readthedocs.io/en/latest/Directives/) 的基于“请求生命周期”事件的可编程接口。例如，“请求过滤器”阶段允许开发人员在收到请求标头时运行代码来修改或拒绝请求。通过这种设计，我们可以清晰地分离我们的业务逻辑和通用代理逻辑。之前从事 NGINX 工作的开发人员可以轻松切换到 Pingora 并迅速提高工作效率。

## Pingora 在生产中更快

让我们快进到现在。Pingora 处理几乎所有需要与源服务器交互的 HTTP 请求（例如缓存未命中），我们在此过程中收集了很多性能数据。

首先，让我们看看 Pingora 如何加快我们客户的流量。Pingora 上的总体流量显示，TTFB 中位数减少了 5 毫秒，第 95 个百分位数减少了 80 毫秒。这不是因为我们运行代码更快。甚至我们的旧服务也可以处理亚毫秒范围内的请求。

时间节省来自我们的新架构，它可以跨所有线程共享连接。这意味着更好的连接重用率，在 TCP 和 TLS 握手上花费的时间更少。

在所有客户中，与旧服务相比，Pingora 每秒的新连接数只有三分之一。对于一个主要客户，它将连接重用率从 87.1% 提高到 99.92%，这将新连接减少了 160 倍。更直观地说，通过切换到 Pingora，我们每天为客户和用户节省了 434 年的握手时间。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1310 Embedded Image - lT30Sj](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TZVYQ0EY0S9MQ582DT7F.png&w=715&h=304&f=webp&fit=cover&position=center)

### 更多功能

拥有工程师熟悉的开发人员友好界面，同时消除以前的限制，让我们能够更快地开发更多功能。像新协议这样的核心功能充当我们为客户提供更多产品的基石。

例如，我们能够在没有重大障碍的情况下向 Pingora 添加 HTTP/2 上游支持。这使我们能够在不久之后向我们的客户提供 [gRPC](https://blog.cloudflare.com/road-to-grpc/)。将相同的功能添加到 NGINX 将需要[更多的工程工作，并且可能无法实现](https://mailman.nginx.org/pipermail/nginx-devel/2017-July/010357.html)。

最近，我们宣布推出了 [Cache Reserve](https://blog.cloudflare.com/introducing-cache-reserve/)，其中 Pingora 使用 R2 存储作为缓存层。随着我们向 Pingora 添加更多功能，我们能够提供以前不可行的新产品。

### 更高效

在生产环境中，与我们的旧服务相比，Pingora 在相同流量负载的情况下，消耗的 CPU 和内存减少了约 70% 和 67%。节省来自几个因素。

与旧的 [Lua 代码](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/lua.html)相比，我们的 Rust 代码运行[效率更高](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust.html)。最重要的是，它们的架构也存在效率差异。例如，在 NGINX/OpenResty 中，当 Lua 代码想要访问 HTTP 头时，它必须从 NGINX C 结构中读取它，分配一个 Lua 字符串，然后将其复制到 Lua 字符串中。之后，Lua 还对其新字符串进行垃圾回收。在 Pingora 中，它只是一个直接的字符串访问。

多线程模型还使得跨请求共享数据更加高效。NGINX 也有共享内存，但由于实施限制，每次共享内存访问都必须使用互斥锁，并且只能将字符串和数字放入共享内存。在 Pingora 中，大多数共享项目可以通过[原子引用计数器](https://doc.rust-lang.org/std/sync/struct.Arc.html)后面的共享引用直接访问。

如上所述，CPU 节省的另一个重要部分是减少了新的连接。与仅通过已建立的连接发送和接收数据相比，TLS 握手成本显然更为高昂。

### 更安全

在我们这样的规模下，快速安全地发布功能十分困难。很难预测在每秒处理数百万个请求的分布式环境中可能发生的每个边缘情况。模糊测试和静态分析只能缓解这么多。Rust 的内存安全语义保护我们免受未定义行为的影响，并让我们相信我们的服务将正确运行。

有了这些保证，我们可以更多地关注我们的服务更改将如何与其他服务或客户来源进行交互。我们能够以更高的节奏开发功能，而不用背负内存安全和难以诊断崩溃的问题。

当崩溃确实发生时，工程师需要花时间来诊断它是如何发生的以及是什么原因造成的。自 Pingora 创立以来，我们已经处理了数百万亿个请求，至今尚未因为我们的服务代码而崩溃。

事实上，Pingora 崩溃是如此罕见，当我们遇到一个问题时，我们通常会发现不相关的问题。最近，我们的服务开始崩溃后不久，我们发现了[一个内核错误](https://lkml.org/lkml/2022/3/15/6)。我们还在一些机器上发现了硬件问题，过去排除了由我们的软件引起的罕见内存错误，即使在几乎不可能进行重大调试之后也是如此。

## 总结

总而言之，我们已经建立了一个更快、更高效、更通用的内部代理，作为我们当前和未来产品的平台。

我们之后将介绍有关我们面临的问题和应用优化的更多技术细节，以及我们从构建 Pingora 并将其推出以支持互联网的重要部分的经验教训。同时还将介绍我们的开源计划。

Pingora 是我们重写系统的最新尝试，但它不会是我们的最后一次。它也只是我们系统重新架构的基石之一。有兴趣加入我们，帮助建立一个更好的互联网？[我们的工程团队正在招聘](https://www.cloudflare.com/zh-cn/careers/jobs/?department=Engineering)。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet%2F&t=%E5%B0%86%20Cloudflare%20%E8%BF%9E%E6%8E%A5%E5%88%B0%E4%BA%92%E8%81%94%E7%BD%91%E7%9A%84%E4%BB%A3%E7%90%86%E2%80%94%E2%80%94Pingora%20%E7%9A%84%E6%9E%84%E5%BB%BA%E6%96%B9%E5%BC%8F)[](https://x.com/intent/post?text=%E5%B0%86+Cloudflare+%E8%BF%9E%E6%8E%A5%E5%88%B0%E4%BA%92%E8%81%94%E7%BD%91%E7%9A%84%E4%BB%A3%E7%90%86%E2%80%94%E2%80%94Pingora+%E7%9A%84%E6%9E%84%E5%BB%BA%E6%96%B9%E5%BC%8F&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet%2F)[](https://bsky.app/intent/compose?text=%E5%B0%86+Cloudflare+%E8%BF%9E%E6%8E%A5%E5%88%B0%E4%BA%92%E8%81%94%E7%BD%91%E7%9A%84%E4%BB%A3%E7%90%86%E2%80%94%E2%80%94Pingora+%E7%9A%84%E6%9E%84%E5%BB%BA%E6%96%B9%E5%BC%8F+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet%2F)[](https://mastodonshare.com/?text=%E5%B0%86+Cloudflare+%E8%BF%9E%E6%8E%A5%E5%88%B0%E4%BA%92%E8%81%94%E7%BD%91%E7%9A%84%E4%BB%A3%E7%90%86%E2%80%94%E2%80%94Pingora+%E7%9A%84%E6%9E%84%E5%BB%BA%E6%96%B9%E5%BC%8F&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet%2F)[](https://www.threads.net/intent/post?text=%E5%B0%86+Cloudflare+%E8%BF%9E%E6%8E%A5%E5%88%B0%E4%BA%92%E8%81%94%E7%BD%91%E7%9A%84%E4%BB%A3%E7%90%86%E2%80%94%E2%80%94Pingora+%E7%9A%84%E6%9E%84%E5%BB%BA%E6%96%B9%E5%BC%8F+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fhow-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet%2F)

## 相关标签

[NGINX](https://blog.cloudflare.com/zh-cn/tag/nginx/)[Pingora](https://blog.cloudflare.com/zh-cn/tag/pingora/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[性能](https://blog.cloudflare.com/zh-cn/tag/performance/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
