---
url: https://blog.cloudflare.com/zh-cn/making-super-slurper-five-times-faster/
title: \u4f7f\u7528 Workers\u3001Durable Objects \u548c Queues \u4f7f Super Slurper \u901f\u5ea6\u63d0\u9ad8 5 \u500d | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:00.369974+00:00
---

# 使用 Workers、Durable Objects 和 Queues 使 Super Slurper 速度提高 5 倍 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/making-super-slurper-five-times-faster/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Queues](https://blog.cloudflare.com/zh-cn/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)+4再显示 4 个标签

7 个标签显示 7 个标签

  * 文章标签
  * [Cloudflare Queues](https://blog.cloudflare.com/zh-cn/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/zh-cn/tag/r2-super-slurper/)[队列](https://blog.cloudflare.com/zh-cn/tag/queues/)
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



[Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/zh-cn/tag/r2-super-slurper/)[队列](https://blog.cloudflare.com/zh-cn/tag/queues/)

[Cloudflare Queues](https://blog.cloudflare.com/zh-cn/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/zh-cn/tag/r2-super-slurper/)[队列](https://blog.cloudflare.com/zh-cn/tag/queues/)

2025年4月10日

# 使用 Workers、Durable Objects 和 Queues 使 Super Slurper 速度提高 5 倍

![Connor Maddox](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GJCDNCNMKRFZB06B4MZ6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Siddhant Sinha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XJ1R2S5DZS8B6TDZBZ25.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Prasanna Sai Puvvada](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SJHBSH635BDQ2W9VQA8G.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Connor Maddox](https://blog.cloudflare.com/zh-cn/author/connor-maddox/)、[Siddhant Sinha](https://blog.cloudflare.com/zh-cn/author/siddhant/)和[Prasanna Sai Puvvada](https://blog.cloudflare.com/zh-cn/author/prasanna-sai-puvvada/)

阅读时间：9 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/making-super-slurper-five-times-faster/)、[Deutsch](https://blog.cloudflare.com/de-de/making-super-slurper-five-times-faster/)、[Español](https://blog.cloudflare.com/es-es/making-super-slurper-five-times-faster/)、[Français](https://blog.cloudflare.com/fr-fr/making-super-slurper-five-times-faster/)、[日本語](https://blog.cloudflare.com/ja-jp/making-super-slurper-five-times-faster/)、[한국어](https://blog.cloudflare.com/ko-kr/making-super-slurper-five-times-faster/)和[繁體中文](https://blog.cloudflare.com/zh-tw/making-super-slurper-five-times-faster/).

![BLOG-2731 Feature Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49756SEE9TPQPR5FT8SAFG.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////85OjwydfryNrx2eb36u308ezr///////+3+byvtHtu9Pz0eL65u338e7t////////3OX2tM7xr8/3yuD+5e378/Hx////////3+n7ttH2sdL8y+P/5/H/9vX2////////6fH/xtz7wt3/1+v/7vf/+/r7////////9fv/3Ov/2ev/6Pb/+P7/////////////////7vf/6/f/9f7/////////////////////9Pv/8vv/+///////////)

[_Super Slurper_](https://developers.cloudflare.com/r2/data-migration/super-slurper/) 是 Cloudflare 打造的数据迁移工具，旨在简化云对象存储提供商和 [_Cloudflare R2_](https://developers.cloudflare.com/r2/) 之间的大规模数据传输。自推出以来，已有数千名开发人员使用 Super Slurper 将 PB 级数据从 AWS S3、Google Cloud Storage 和 [_其他 S3 兼容服务_](https://developers.cloudflare.com/r2/data-migration/super-slurper/#supported-cloud-storage-providers) 迁移至 R2。

但我们看到了进一步提升性能的机会。基于我们的开发人员平台，我们从零开始重新设计了 Super Slurper 的架构，使用 [_Cloudflare Workers_](https://developers.cloudflare.com/workers/)、[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/) 和 [_Queues_](https://developers.cloudflare.com/queues/)，将传输速度提升高达 5 倍。在本文中，我们将深入探讨原始架构、识别的性能瓶颈、解决方案，以及这些改进的实际影响。

## 原有架构与性能瓶颈

Super Slurper 最初与 [_SourcingKit_](https://developers.cloudflare.com/images/upload-images/sourcing-kit/) 共享架构，后者是一个用于将图像从 AWS S3 批量导入到 [_Cloudflare Images_](https://developers.cloudflare.com/images/) 的工具。SourcingKit 部署在 Kubernetes 上，与 [_Images_](https://developers.cloudflare.com/images/) 服务一起运行。在开始构建 Super Slurper 时，我们将其拆分到独立的 Kubernetes 命名空间，并引入了几个新的 API，使其更容易在对象存储应用场景中使用。这一架构配置运行良好，帮助数千名开发人员成功将数据迁移至 R2。

然而，其中并非没有挑战。SourcingKit 并不是为处理大规模 PB 级传输所需的规模而设计的。SourcingKit 乃至 Super Slurper 运行在位于核心数据中心的 Kubernetes 集群上，这意味着它必须与 Cloudflare 的控制平面、分析服务和其他服务共享计算资源和带宽。随着迁移数量的增长，这些资源约束逐渐成为明显的性能瓶颈。

对于在对象存储提供商之间传输数据的服务而言，其工作流程非常简单：列出源存储中的对象，将其复制到目标存储，并重复此过程。这正是原版 Super Slurper 的工作方式。我们列出来自源存储桶的对象，将该列表推送到一个基于 Postgres 的队列（`pg_queue`），然后以稳定的速度从此队列中拉出对象以复制过来。鉴于对象存储迁移的规模，带宽使用量势必居高不下。这使得系统扩展存在挑战性。

为了解决仅在我们的核心数据中心运行的带宽限制，我们引入了 [_Cloudflare Workers_](https://developers.cloudflare.com/workers/)。我们不再在核心数据中心处理数据复制，而是开始调用 Worker 执行实际的复制操作：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44D530YYFHF6VPDT2G2NT5.png&w=715&h=498&f=webp&fit=cover&position=center)

随着 Super Slurper 使用量增加，我们的 Kubernetes 资源消耗也在增加。在数据传输过程中，大量时间都耗费在等待网络 I/O 或存储操作上，而非实际执行计算密集型任务。所以我们不需要更多的内存或更多的 CPU，我们需要更多的并发。

为了跟上需求，我们不断增加副本数量。但最终，我们遇到了瓶颈。我们面临着可扩展性方面的挑战，当运行大约数十个 Pod 时，我们希望将其进一步增加几个数量级。

我们决定从最基本原理重新思考整个方案，而不是依赖已继承的架构。在大约一周的时间里，我们使用 [_Cloudflare Workers_](https://developers.cloudflare.com/workers/)、[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/) 和 [_Queues_](https://developers.cloudflare.com/queues/)构建了一个粗略的概念验证原型。我们列出源存储桶中的对象，将它们推送到队列中，然后使用队列中的消息来启动传输。尽管这听起来与我们最初的实现方案非常相似，但基于 Cloudflare 开发人员平台构建使我们能够自动扩展到比之前高一个数量级的规模。

  * **Cloudflare Queues** ：支持异步对象传输，并可自动扩展以满足迁移对象的数量需求。
  * **Cloudflare Workers** ：运行轻量级计算任务，没有 Kubernetes 的开销，并优化进程每个部分的运行位置，以降低延迟和提高性能。
  * **基于 SQLite 的 Durable Objects (DO)** ：充当一个完全分布式的数据库，消除了单个 PostgreSQL 实例的局限性。
  * **Hyperdrive** ：提供对原始 PostgreSQL 数据库中历史作业数据的快速访问，并保留其作为存档存储。



我们进行了几轮测试，发现对于小规模传输（数百个对象）时，我们的概念验证方案性能低于原始实现，但随着传输规模扩展到数百万个对象时，性能逐渐匹配并最终超越了原始实现。那是我们需要投入时间将概念验证投入生产的信号。

我们移除了概念验证临时方案，专注于稳定性优化，并探索了使传输能够实现更高并发的新方法。经过几次迭代后，我们获得了满意的效果。

## 全新架构： Workers、 Queues 和 Durable Objects

#### 处理层：管理迁移流程

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GAXDNPXMT21H1Q8CNN7M.png&w=715&h=251&f=webp&fit=cover&position=center)

我们处理层的核心是**队列、消费者和 workers** 。其过程如下所示：

#### 启动迁移

当客户端触发迁移时，它首先向我们的 **API Worker** 发送请求。这个 worker 获取迁移的详细信息，存储在数据库中，并向 **List Queue** 添加消息以启动迁移过程。

#### 列出源存储对象

**List Queue** 是事务开始处理的关键环节。它从队列中拉取消息，从源存储桶中检索对象列表，应用任何必要的过滤器，并将重要的元数据存储在数据库中。然后，它通过将对象传输消息排队到 **Transfer Queue** 中来创建新任务。

我们立即将新批次的工作排队，最大程度增加并发。内置的限流机制可以防止我们在发生意外故障时向队列添加更多的消息，例如从属系统宕机。这有助于保持稳定性并防止中断期间过载。

#### 高效的对象传输

**Transfer Queue Consumer** Workers 从队列中提取对象传输消息，通过锁定数据库中的对象键来确保每个对象仅被处理一次。传输完成后，该对象将被解锁。对于大型对象，我们将其拆分为可管理的块，并以分段上传的方式传输。

#### 优雅地处理故障

在任何分布式系统中，故障都是不可避免的，我们必须确保对此做好充分的容错处理。我们实现了暂时性故障的自动重试，确保问题不会打断迁移过程。但是，如果重试无法解决问题，则消息会进入 **Dead Letter Queue (DLQ)** ，并记录下来供以后查看和解决。

#### 作业完成与生命周期管理

一旦所有对象列出且开始传输， **Lifecycle Queue Consumer** 将持续监控整个过程。它会监控传输过程，确保没有对象被遗漏。当所有传输完成后，作业将被标记为已完成，迁移过程随即结束。

### 数据库层：持久化存储和传统数据检索

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46PPCT7KRZD27PS744HKQT.png&w=715&h=479&f=webp&fit=cover&position=center)

在构建新架构时，我们深知需要一个强大的解决方案，既能处理海量数据集，又能确保历史作业数据的检索。这就是我们的 **Durable Objects (DO)** 和 **Hyperdrive** 组合发挥作用的地方。

#### Durable Objects

我们为每个帐户分配一个专用的 Durable Object，专门跟踪迁移作业。每项**作业的 DO** 存储关键的详细信息，例如存储桶名称、用户选项和作业状态。这确保一切都有条不紊且易于管理。为了支持大型迁移，我们还添加了一个 **Batch DO** ，用于管理所有排队等待传输的对象，并存储其传输状态、对象键以及任何额外的元数据。

随着迁移规模扩大到**数十亿个对象** ，我们必须在存储方面发挥创造力。我们实施了分片策略来分散请求负载，既避免了性能瓶颈，又绕过了 **SQLite DO 10 GB** 的存储限制。在对象传输后，我们会清理其详细信息，从而优化存储空间。10 亿个对象键所需的存储空间非常惊人！

#### Hyperdrive

由于我们正在重建一个拥有多年迁移历史的系统，我们需要一种方法来保存和访问每一个历史迁移的详细信息。Hyperdrive 作为连接我们传统系统的桥梁，能够从核心 **PostgreSQL** 数据库无缝检索历史作业数据。这不仅仅是一种数据检索机制，更是复杂迁移场景的归档存储。

## 成果：Super Slurper 现将数据迁移到 R2 的速度提高多达 5 倍

那么，在完成以上所有工作之后，我们是否真正实现了加快传输速度的目标呢？

我们进行了测试，将 75000 个对象从 AWS S3 迁移到 R2。使用原始实现方案时，数据传输耗时 15 分钟 30 秒。经过性能优化后，同样的迁移过程仅耗时 3 分钟 25 秒。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW477CPDAB1K3Y0SNDE0Z0SJ.png&w=715&h=360&f=webp&fit=cover&position=center)

2 月份生产环境迁移正式使用新服务后，我们在某些场景下观察到更显著的性能提升，尤其是在对象大小分布不同的情况下。Super Slurper 已经投入使用 [_大约两年了_](https://blog.cloudflare.com/r2-super-slurper-ga/) 。然而，性能改进使其能够迁移到数据量大幅提升 —— Super Slurper 复制的所有对象中，有 35% 实在最近两个月内发生的。

## 挑战

使用新架构时，我们面临的最大挑战之一是处理重复消息。重复消息可能会以几种方式产生：

  * Queues 提供至少一次交付（At-least-once delivery）机制，这意味着为了确保传输成功，消费者可能会多次接收同一条消息。
  * 失败和重试也可能造成明显的重复。例如，如果对 Durable Object 的请求在对象已完成传输后失败，重试可能会重复处理同一个对象。



如果处理不当，可能会导致同一对象被传输多次。为解决这一问题，我们实施了多项策略，以确保每个对象准确计数并仅传输一次：

  1. 由于列出对象是按顺序进行的（例如，要获取对象 2，您需要从列出对象 1 时获得的继续令牌），我们为每个列出操作分配了一个序列 ID。这使我们能够检测重复的列出操作，并防止多个进程同时启动。这特别有用，因为我们无需等待数据库和队列操作完成，就能列出下一批次。如果列出操作 2 失败，我们可以重试；如果列出操作 3 已经启动，我们可以跳过不必要的重试。
  2. 当每个对象传输开始时都会被锁定，从而防止同一对象的并行传输。对象成功传输后，通过从数据库中删除其键来解锁。如果针对该对象的消息后续重新出现，如果其键不再存在，则我们可以安全地假定该对象已完成传输。
  3. 我们依赖数据库事务来保持计数的准确性。如果一个对象释放失败，其计数保持不变。同样，如果对象键添加到数据库失败，则不会更新计数，并会在稍后重试该操作。
  4. 作为最后的故障保护机制，我们会检查目标存储桶中是否已存在该对象，并验证其发布时间是否晚于我们迁移的起始时间。如果是，则假定该对象是由我们（或另一个）进程传输的，并安全地跳过它。



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44AHGCDWRPKVF577ESK4QA.png&w=715&h=228&f=webp&fit=cover&position=center)

## Super Slurper 的下一步计划是什么？

我们始终在探索优化 Super Slurper 的方法，致力于提升其性能、可扩展性和易用性 ——这仅仅是个开始。

  * 我们最近推出了从任何 [_S3 兼容存储提供商_](https://developers.cloudflare.com/changelog/2025-02-24-r2-super-slurper-s3-compatible-support/)迁移的功能！
  * 目前数据迁移仍被限制为每个账户最多 3 个并发迁移，但我们计划提高这一限制。这将使对象前缀能够拆分为独立的迁移任务以并行执行，显著提高存储桶的迁移速度。欲进一步了解 Super Slurper 和如何从现有对象存储迁移数据到 R2，请参阅我们的[ _文档_](https://developers.cloudflare.com/r2/data-migration/super-slurper/)。



P.S.作为本次更新的一部分，我们使 API 的交互更加简单，因此现在管理迁移能够 [_以编程方式管理_](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/)了！

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-super-slurper-five-times-faster%2F&t=%E4%BD%BF%E7%94%A8%20Workers%E3%80%81Durable%20Objects%20%E5%92%8C%20Queues%20%E4%BD%BF%20Super%20Slurper%20%E9%80%9F%E5%BA%A6%E6%8F%90%E9%AB%98%205%20%E5%80%8D)[](https://x.com/intent/post?text=%E4%BD%BF%E7%94%A8+Workers%E3%80%81Durable+Objects+%E5%92%8C+Queues+%E4%BD%BF+Super+Slurper+%E9%80%9F%E5%BA%A6%E6%8F%90%E9%AB%98+5+%E5%80%8D&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-super-slurper-five-times-faster%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-super-slurper-five-times-faster%2F)[](https://bsky.app/intent/compose?text=%E4%BD%BF%E7%94%A8+Workers%E3%80%81Durable+Objects+%E5%92%8C+Queues+%E4%BD%BF+Super+Slurper+%E9%80%9F%E5%BA%A6%E6%8F%90%E9%AB%98+5+%E5%80%8D+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-super-slurper-five-times-faster%2F)[](https://mastodonshare.com/?text=%E4%BD%BF%E7%94%A8+Workers%E3%80%81Durable+Objects+%E5%92%8C+Queues+%E4%BD%BF+Super+Slurper+%E9%80%9F%E5%BA%A6%E6%8F%90%E9%AB%98+5+%E5%80%8D&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-super-slurper-five-times-faster%2F)[](https://www.threads.net/intent/post?text=%E4%BD%BF%E7%94%A8+Workers%E3%80%81Durable+Objects+%E5%92%8C+Queues+%E4%BD%BF+Super+Slurper+%E9%80%9F%E5%BA%A6%E6%8F%90%E9%AB%98+5+%E5%80%8D+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-super-slurper-five-times-faster%2F)

## 相关标签

[Cloudflare Queues](https://blog.cloudflare.com/zh-cn/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Developer Week](https://blog.cloudflare.com/zh-cn/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/zh-cn/tag/durable-objects/)[R2](https://blog.cloudflare.com/zh-cn/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/zh-cn/tag/r2-super-slurper/)[队列](https://blog.cloudflare.com/zh-cn/tag/queues/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
