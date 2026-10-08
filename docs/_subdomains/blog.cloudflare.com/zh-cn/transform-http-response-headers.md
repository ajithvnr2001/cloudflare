---
url: https://blog.cloudflare.com/zh-cn/transform-http-response-headers/
title: \u4f7f\u7528 Transform Rules \u4fee\u6539 HTTP \u54cd\u5e94\u6807\u5934\uff0c\u73b0\u5df2\u63a8\u51fa\uff01 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:50:52.438162+00:00
---

# 使用 Transform Rules 修改 HTTP 响应标头，现已推出！ | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/transform-http-response-headers/

[博客](https://blog.cloudflare.com/zh-cn/)

[Full Stack Week](https://blog.cloudflare.com/zh-cn/tag/full-stack-week/)[Transform Rules](https://blog.cloudflare.com/zh-cn/tag/transform-rules/)

2 个标签显示 2 个标签

  * 文章标签
  *   * 全部标签
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



[Full Stack Week](https://blog.cloudflare.com/zh-cn/tag/full-stack-week/)[Transform Rules](https://blog.cloudflare.com/zh-cn/tag/transform-rules/)

2021年11月18日

# 使用 Transform Rules 修改 HTTP 响应标头，现已推出！

![Sam Marsh](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47NXPW1KFG006NK565ZPD7.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sam Marsh](https://blog.cloudflare.com/zh-cn/author/sam-marsh/)

阅读时间：5 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/transform-http-response-headers/)和[日本語](https://blog.cloudflare.com/ja-jp/transform-http-response-headers/).

![Modifying HTTP response headers with Transform Rules](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW460CHW4699R5GMMBMY7NP5.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f//8vLw7Onm7urn8fDt8PHv6ezs////////8/Hu6+Xg7ebf8uzn8e/s7O3s////////9fHs6+Pb7ePZ8+ri9O/q8O/t////////+PTv7uXc8OXa9+3k+fPt9PPx/////////fr29Ozk9u3k/fXt//r1+fn3///////////++/Xx/vjy///7/////v/+//////////////37///+////////////////////////////////////////////)

HTTP 标头对于 Web 的运作至关重要。它们用于在客户端和服务器之间传递额外信息，例如要应用的安全权限，以及有关客户端的信息，以允许提供正确的内容。

今天，我们宣布转换规则中的第三个操作“HTTP 响应标头修改”即刻推出，适用于所有 Cloudflare 服务套餐。利用这个新功能，Cloudflare 用户能够在流量通过 Cloudflare 返回到客户端时设置或删除 HTTP 响应标头。这样一来，客户可以在响应中扩充有关其请求处理方式的信息、调试信息，甚至是[招聘消息](https://frenxi.com/http-headers-you-dont-expect/)。

之前，HTTP 响应标头修改是使用 [Cloudflare Worker](https://workers.cloudflare.com/) 执行的。现在我们引入了更轻松的做法，无需编写哪怕一行代码。

### 万维网的行李标签

可以将 HTTP 标头视为您在机场办理登机手续时贴到提包上的“行李标签”。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-795 Embedded Image - vpvzfq](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW448A3BS01NBT7S1NKB6TW6.png&w=715&h=473&f=webp&fit=cover&position=center)

一般来说，您无需知道这些数字和词语的含义。您只需知道，要将您的手提箱从登机台运送到正确的飞机，再运送到目的地的正确行李传送带，这些信息非常重要。

这些标签包含有关手提箱重量、目的地机场代码、行李标签号、航空公司、海关处理信息等的信息。这些属性都至关重要，不仅可确保行李到达正确的目的地，而且能以最安全、最高效的方式完成此过程。

HTTP 标头是互联网的行李标签。它们非常重要，可确保来自您浏览器的请求到达正确的目的地，并且该流量使用正确的设置以最安全、最高效的方式返回到您的浏览器。

### HTTP 响应标头的使用方式是怎样的？

HTTP 标头在“request”和“response”交互中设置；“request”是指客户端要求提供文件，“response”是指服务器作为结果返回的内容。今天宣布的功能专门与 HTTP _response_ 标头相关。

HTTP 响应标头用于确保向浏览器返回正确的数据，以及帮助浏览器正确处理数据的信息。常见响应标头包括“Content-Type”，用于告知浏览器所返回内容的类型，例如“Content-Type: text/html” or “Content-Type: image/png”。另一个常见标头是“Server:”，其中包含有关用于处理 HTTP 请求的软件的信息，例如“Server: cloudflare”。

在基本 HTTP 流量处理之外，这些响应标头还有其他许多用途。一个此类示例是提高_安全性_。内容安全策略 (CSP)、跨域资源共享 (CORS) 和 HTTP 严格传输安全 (HSTS) 等安全机制全部实现为响应标头，以便为网站访问者提高并加强安全性。

例如，CSP 的主要目标是缓解和报告跨站点脚本 (XSS) 攻击。XSS 攻击是指在可信网站中注入了恶意脚本的情况，此时攻击者可以使用应用程序将浏览器端脚本之类的恶意代码发送给其他最终用户。接着，该脚本可以用于泄露最终用户与网站或应用程序的交互，将密码等敏感信息透露给第三方。

为防止这种情况，网站管理员将 CSP 添加为 HTTP 响应标头。CSP 响应标头指定了浏览器应该视为可执行脚本的有效源的域。然后，[兼容 CSP 的浏览器](https://content-security-policy.com/)将仅执行从这些允许的域接收的文件中加载的脚本，而忽略其他所有脚本。

通过设置“Content-Security-Policy”标头以及值中包含的策略，将 CSP 添加到 HTTP 响应。例如，使用 NGINX 这一[热门](https://w3techs.com/technologies/overview/web_server)的 Web 服务器时，管理员会在配置中包含类似于以下内容的一行代码：

`add_header Content-Security-Policy "default-src 'self';" always;`
    
    
    add_header Content-Security-Policy "default-src 'self';" always;

使用 [Cloudflare Workers](https://workers.cloudflare.com/) 时，代码会类似于：
    
    
    response.headers.set("Content-Security-Policy": "default-src 'self' example.com *.example.com",)

`response.headers.set("Content-Security-Policy":"default-src 'self' example.com *.example.com",)`

现在，当浏览器收到 HTTP 响应时，会检测是否存在 Content-Security-Policy 标头，并相应采取行动。

## 动态修改 HTTP 响应标头

负责确保 HTTP 响应中存在这些标头的通常是反向代理， 这是位于客户端和服务器之间的一种服务器，其职责之一是扩充返回给客户端的 HTTP 响应数据。

“HTTP 响应标头修改”现在可在所有 Cloudflare 服务套餐的转换规则中使用。它可用于修改 HTTP 响应标头，然后将其返回给访问者，这一切都在 Cloudflare 中进行。当响应来自管理员没有完全控制的源（例如 SaaS 提供商或其他第三方服务）时，这尤其重要。

转换规则允许用户使用以下三个选项之一，针对每个规则修改最多 10 个 HTTP 响应标头：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-795 Embedded Image - cmor6v](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW452RKBK4Z5XMBE44VPHM8J.png&w=715&h=221&f=webp&fit=cover&position=center)

当需要对每个 HTTP 响应动态填充 HTTP 响应标头的值时，应该使用“Set dynamic”。示例包括将 Cloudflare Bot Management“bot score”添加到每个 HTTP 响应，或访问者的国家/地区：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-507 Embedded Image - Cp9kzR](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45M2F60H96KZYWDPF4QES9.png&w=715&h=70&f=webp&fit=cover&position=center)

注意：这些值是使用相应 HTTP 请求计算的，意味着响应标头中返回的机器人分数将基于 HTTP 请求来计算。类似地，ip.src.country 值将为网站访问者的国家/地区，而不是从中发送响应的源。

“Set static”应该用于使用静态文本字符串填充标头的值。该选项应该用于简单的标头创建，例如设置 CORS 或 CSP 策略：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-795 Embedded Image - ZFpVPJ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48Z1BWM1TZA3BXAZEGNWDE.png&w=715&h=63&f=webp&fit=cover&position=center)

在两种“set”示例中，如果 HTTP 响应中已存在具有指定名称的标头 ，其值将被删除并替换为给定值。

“Remove”是最后的选项，应该用于删除具有指定名称的所有 HTTP 响应标头。例如，如果您想确保删除了“Link”HTTP 响应标头，您可使用类似于以下内容的规则：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-795 Embedded Image - 5eoqiO](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KZHK9X9QTX3XWZSS23T2.png&w=715&h=91&f=webp&fit=cover&position=center)

Cloudflare [函数](https://developers.cloudflare.com/firewall/cf-firewall-language/functions)可以在“set dynamic”标头修改中使用。这些函数包括：

  * concat()
  * regex_replace()
  * to_string()
  * lower()



通常使用函数的示例是，使用 concat() 和 to_string() 来接收不同数据类型的列表并连接在一起以构成单个标头值。例如，`concat(“score=”,to_string(cf.bot_management.score))`会生成 `score=85` 这样的标头值。

注意：正则表达式函数仅可用于使用 Business 和 Enterprise 服务套餐的客户。

## 针对您的网站进行优化

将 HTTP 响应标头修改移入 Cloudflare 中的另一个巨大优势是规则构建器中提供的过滤级别。通常，CORS 和 CSP 等技术在整个网站上（或最佳情况下）会被逐个目录设置为响应标头。

利用转换规则，管理员可以基于一些参数设置标头，包括访问者的所在国家/地区、机器人分数、用户代理、请求的文件名/文件扩展名、请求方法，[等等](https://developers.cloudflare.com/firewall/cf-firewall-language/fields)。

这样一来，管理员能够实施一些设置，例如，相比未验证的机器人/低机器人分数流量，对[已验证](https://developers.cloudflare.com/bots/get-started/bm-subscription#verified-bots)的机器人设置更严格的内容安全策略。

## 马上试试吧

HTTP 响应标头修改可用于改进操作、删除敏感数据、提高安全性，以及其他许多用例。立即亲自试用最新的[转换规则](https://dash.cloudflare.com/)。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftransform-http-response-headers%2F&t=%E4%BD%BF%E7%94%A8%20Transform%20Rules%20%E4%BF%AE%E6%94%B9%20HTTP%20%E5%93%8D%E5%BA%94%E6%A0%87%E5%A4%B4%EF%BC%8C%E7%8E%B0%E5%B7%B2%E6%8E%A8%E5%87%BA%EF%BC%81)[](https://x.com/intent/post?text=%E4%BD%BF%E7%94%A8+Transform+Rules+%E4%BF%AE%E6%94%B9+HTTP+%E5%93%8D%E5%BA%94%E6%A0%87%E5%A4%B4%EF%BC%8C%E7%8E%B0%E5%B7%B2%E6%8E%A8%E5%87%BA%EF%BC%81&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftransform-http-response-headers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftransform-http-response-headers%2F)[](https://bsky.app/intent/compose?text=%E4%BD%BF%E7%94%A8+Transform+Rules+%E4%BF%AE%E6%94%B9+HTTP+%E5%93%8D%E5%BA%94%E6%A0%87%E5%A4%B4%EF%BC%8C%E7%8E%B0%E5%B7%B2%E6%8E%A8%E5%87%BA%EF%BC%81+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftransform-http-response-headers%2F)[](https://mastodonshare.com/?text=%E4%BD%BF%E7%94%A8+Transform+Rules+%E4%BF%AE%E6%94%B9+HTTP+%E5%93%8D%E5%BA%94%E6%A0%87%E5%A4%B4%EF%BC%8C%E7%8E%B0%E5%B7%B2%E6%8E%A8%E5%87%BA%EF%BC%81&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftransform-http-response-headers%2F)[](https://www.threads.net/intent/post?text=%E4%BD%BF%E7%94%A8+Transform+Rules+%E4%BF%AE%E6%94%B9+HTTP+%E5%93%8D%E5%BA%94%E6%A0%87%E5%A4%B4%EF%BC%8C%E7%8E%B0%E5%B7%B2%E6%8E%A8%E5%87%BA%EF%BC%81+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Ftransform-http-response-headers%2F)

## 相关标签

[Full Stack Week](https://blog.cloudflare.com/zh-cn/tag/full-stack-week/)[Transform Rules](https://blog.cloudflare.com/zh-cn/tag/transform-rules/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
