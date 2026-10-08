---
url: https://blog.cloudflare.com/zh-cn/2022-07-sms-phishing-attacks/
title: \u4e00\u573a\u590d\u6742\u7f51\u7edc\u9493\u9c7c\u9a97\u5c40\u7684\u673a\u5236\u53ca\u6211\u4eec\u5982\u4f55\u6210\u529f\u963b\u6b62\u5b83 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:45:54.017628+00:00
---

# 一场复杂网络钓鱼骗局的机制及我们如何成功阻止它 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/2022-07-sms-phishing-attacks/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Access](https://blog.cloudflare.com/zh-cn/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/zh-cn/tag/gateway/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)+2再显示 2 个标签

5 个标签显示 5 个标签

  * 文章标签
  * [Cloudflare Access](https://blog.cloudflare.com/zh-cn/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/zh-cn/tag/gateway/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[网络钓鱼](https://blog.cloudflare.com/zh-cn/tag/phishing/)
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



[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[网络钓鱼](https://blog.cloudflare.com/zh-cn/tag/phishing/)

[Cloudflare Access](https://blog.cloudflare.com/zh-cn/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/zh-cn/tag/gateway/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[网络钓鱼](https://blog.cloudflare.com/zh-cn/tag/phishing/)

2022年8月9日

# 一场复杂网络钓鱼骗局的机制及我们如何成功阻止它

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Daniel Stinson-Diess](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BSD1SAVED23QC64BJ0XP.png&w=64&h=64&f=webp&fit=cover&position=center)![Sourov Zaman](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PWM9TRAJ8WPBBS7J2SPN.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/zh-cn/author/matthew-prince/)、[Daniel Stinson-Diess](https://blog.cloudflare.com/zh-cn/author/daniel-stinson-diess/)和[Sourov Zaman](https://blog.cloudflare.com/zh-cn/author/sourov/)

阅读时间：9 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/2022-07-sms-phishing-attacks/)、[Español](https://blog.cloudflare.com/es-es/2022-07-sms-phishing-attacks/)、[日本語](https://blog.cloudflare.com/ja-jp/2022-07-sms-phishing-attacks/)、[Русский](https://blog.cloudflare.com/ru-ru/2022-07-sms-phishing-attacks/)和[Polski](https://blog.cloudflare.com/pl-pl/2022-07-sms-phishing-attacks/).

![The mechanics of a sophisticated phishing scam and how we stopped it](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XYVSV0Q80CXCW0QHC2NE.png&w=1600&h=900&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAgwBEiyZHn1JTtnJlxIJ0wX92qGdogjdNiTI+kE5WoXh9tJabvqGnuZifpHuDhlBZjkk2lWZipJOasrG/uLnKsqu8oIuXi2Jjkk8vmG5lp5yjtLrKuMHVsLHFoJCdjmdlkkUtmmRdqpKXua+6vbXEtqa1pIaQj11dkCQvmUlMrXV1v5KQx5mZwI2Oqm9yjURKjgAymA82rkw/xGpLz3VSyW1Rr1FGjBcyjQA0lwAprzAAxlMA0mEAzFwSsUAjiwAj)

2022 年 8 月 9 日，Twilio 宣布 [遭到一次针对性的网络钓鱼攻击](https://www.twilio.com/blog/august-2022-social-engineering-attack)。在Twilio 受到攻击的大约同一时间，我们发现了一次针对 Cloudflare 员工的类似攻击。虽然确实有个别员工上当受骗，然而，通过使用我们自己的 [Cloudflare One 产品](https://www.cloudflare.com/zh-cn/cloudflare-one/)，以及发放给每位员工的物理安全密钥（用于访问我们的所有应用），我们成功防御了这次攻击。

我们确认没有任何 Cloudflare 系统受到入侵。我们的 [Cloudforce One 威胁情报团队](https://blog.cloudflare.com/zh-cn/introducing-cloudforce-one-threat-operations-and-threat-research-zh-cn/) 能够执行额外的分析来进一步剖析攻击的机制，并收集关键的证据来协助追踪攻击者。

这是一次针对员工和系统的复杂攻击，我们认为大多数组织都有可能遭到入侵。鉴于攻击者以多个组织为目标，我们希望分享我们所看到的详细情况，以帮助其他公司识别和缓解这一攻击。

## 针对性的短信

2022 年 7 月 20 日，Cloudflare 安全团队收到报告，称员工收到了看起来合法的短信，指向一个看似是 Cloudflare Okta 登录页面的网址。这些信息开始于 2022 年 7 月 20 日 22:50 UTC。在不到一分钟内，至少 76 位员工在其个人和工作手机上收到了短信。一些员工家属也收到了信息。我们还未能确定攻击者如何收集到这些员工的电话号码，但已经检查过我们员工目录服务的访问日志，没有发现任何入侵的迹象。

Cloudflare 运营一个全天候的安全事件响应团队（SIRT）。Cloudflare 的每位员工都受过向 SIRT 报告任何可疑情况的训练。SIRT 收到的报告中，超过 90% 被确认并非威胁。员工被鼓励报告任何情况，过度举报也没有关系。然而，这次 SIRT 收到的报告是一次真正的威胁。

员工收到的短信如下：

它们来自与 T-Mobile SIM 卡相关联的 3 个电话号码：(754) 268-9387, (205) 946-7573, (754) 364-6683 和 (561)524-5989。它们指向一个看似官方的域：cloudflare-okta.com。该域是通过域名注册服务商 Porkbun 于 2022 年 7 月 20 日 22:13:04 UTC 注册的，距离上述网络钓鱼攻击发动不到 40 分钟。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - mzDQx2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458M23R42VF210NMM8NBN6.png&w=715&h=601&f=webp&fit=cover&position=center)

Cloudflare 构建自己的[安全注册产品](https://www.cloudflare.com/products/registrar/custom-domain-protection/)，部分是为了能够监控使用 Cloudflare 品牌的域名被注册的情况，并及时将其关闭。然而，由于这个域注册时间很短，尚未作为新的 .com 注册发布，以至于我们的系统未能检测到其注册，我们的团队尚未采取行动来将其终止。

一旦点击上述链接，就会进入一个网络钓鱼页面。该钓鱼页面托管于 DigitalOcean，看起来是这样的：

Cloudflare 使用 Okta 作为身份提供商。该钓鱼页面设计成与合法的Okta 登录页面完全相同。该钓鱼页面提示访问页面的人输入用户名和密码。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - 5SXCpt](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45QS52KCAFCN2KSPGK32J4.png&w=715&h=536&f=webp&fit=cover&position=center)

## 实时网络钓鱼

根据员工收到的内容，以及其他受到攻击的公司在VirusTotal 等服务发布的内容，我们得以分析了这次网络钓鱼攻击的有效负载。受害者在钓鱼页面提交后，其凭据被即时通过信息服务 Telegram 转发给攻击者。这个实时转发很重要，因为该钓鱼页面也会提示输入基于时间的一次性密码（TOTP）。

估计攻击者会实时收到凭据，并在受害者公司的实际登录页面输入，而且对很多组织而言，这一操作会生成一个代码并通过短信发送给员工，或显示在密码生成器上。然后员工将在钓鱼站点上输入 TOTP，后者也会被转发给攻击者。随后攻击者会在TOTP 代码过期前使用它来登录该公司的实际登录页面，从而击败大多数双因素身份验证措施。

## 尽管不完美，但仍受到保护

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - y0kAKQ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BDTY0D16K46QEKFRZ8VJ.png&w=715&h=250&f=webp&fit=cover&position=center)

我们证实三位 Cloudflare 员工被钓鱼信息骗到并输入了凭据。然而，Cloudflare 并不使用 TOTP 代码。实际上，Cloudflare 的每一位员工从 YubiKey 这样的供应商获发放一个 FIDO2 兼容的安全密钥。由于该硬件密钥与用户关联，并实施[源绑定](https://www.yubico.com/blog/creating-unphishable-security-key/)，即使这样复杂的实时钓鱼攻击也无法收集到足够的信息来登录到我们的任何系统。虽然攻击者尝试使用泄露的用户名和密码凭据登录我们的系统，但他们无法通过硬件密钥的要求。

但这个钓鱼页面并非只是为了获取登录凭据和TOTP 代码。如果有人通过了这些步骤，钓鱼页面就会开始下载钓鱼有效负载，其中包括 AnyDesk 的远程访问软件。该软件一旦被安装，攻击者就能远程控制受害者的机器。我们确认，我们没有任何团队成员走到了这一步。然而，如果确实到了这一步，我们的端点安全软件也会阻止该远程访问软件的安装。

## 我们如何响应？

我们对该事件采取的主要响应行动如下

### 1\. 用 Cloudflare Gateway 阻止该钓鱼域名。

Cloudflare Gateway 是一个安全 Web 网关解决方案，提供威胁和数据保护，附带 DNS/HTTP 过滤功能，并原生集成 Zero Trust。我们在内部使用这个解决方案，以主动识别恶意域名并予以阻止。我们的团队将该恶意域名加入到Cloudflare Gateway，以阻止所有员工对其进行访问。

Gateway 对恶意域名的自动检测也识别出了该域名并将其屏蔽，但由于该域名注册并发送消息的时间间隔非常短，在一些员工点击这些链接之前，系统尚未自动采取行动。鉴于这次事件，我们正在努力加快识别和阻止恶意域名的速度。我们还实施了对新注册域名的访问控制，这一功能已经向客户提供，但我们内部还没有实施。

### 2\. 识别所有受影响的 Cloudflare 员工，并重置被泄露的凭据

我们对网络钓鱼短信的收件人与登录活动进行比对，识别威胁行为者利用我们员工账户登录的尝试。我们识别了因硬件密钥（U2F）要求而被阻止的登录尝试，其表明已输入正确密码但第二因素未通过验证。对于三位员工已泄露的凭据，我们重置了其凭据和任何活动会话，并对其设备进行扫描。

### 3\. 识别和下线威胁行为者的基础设施

威胁行为者的网络钓鱼域是通过 Porkbun 新注册的，托管在DigitalOcean上。针对 Cloudflare 的钓鱼域是在首轮钓鱼攻击发动前不到一小时内设置的。该站点使用 Nuxt.js 前端，Django 后端。我们与 DigitalOcean 合作关闭了攻击者的服务器。我们还与 Porkbun 合作获得了对该恶意域的控制权。

从失败的登录尝试中，我们能够确定威胁行为者利用了 Mullvad VPN 软件，且显然是在 Windows 10 机器上使用谷歌 Chrome浏览器进行操作。攻击者使用的 VPN IP 地址为 198.54.132.88和198.54.135.222。这些 IP 地址被分配给美国专业服务器提供商Tzulo，该公司网站声称他们的服务器位于洛杉矶和芝加哥。实际上，前者运行于位于多伦多地区的一台服务器上，后者运行在华盛顿特区地区的一台服务器上。我们阻止了这些 IP 地址访问我们的任何服务。

### 4\. 更新检测，以识别任何后续的攻击企图

根据从这一攻击中获得的信息，我们将更多信号加入到原有的检测机制中，以专门识别这一攻击行为者。截至本文撰写时，我们还没有发现任何针对我们员工的更多攻击。然而，来自该服务器的情报显示，攻击者当时还对其他组织发动了攻击，包括 Twilio。我们与这些组织取得联系，并分享了有关攻击的情报。

### 5\. 审计服务访问日志，以确定是否有其他攻击迹象

以上攻击之后，我们筛查所有系统日志，以寻找来自这个特定攻击者的任何额外指纹。鉴于 Cloudflare Access 是所有Cloudflare 应用的中央控制点，我们可以搜索日志以查找攻击者可能破坏了任何系统的任何迹象。鉴于员工的电话成为了目标，我们也仔细检查了员工目录提供商的日志。我们没有发现任何破坏迹象。

## 吸取的教训及正在采取的额外措施

我们从每一个攻击中学习。即使攻击并不成功，我们也正在根据所了解到的情况进行额外的调整。我们正在调整 Cloudflare Gateway 的设置，以限制或隔离对过去 24 小时内注册的域上所运行网站的访问。任何包含“cloudflare”、“okta”、“sso” 和 “2fa” 等术语但不在允许列表中的网站，也将通过我们的浏览器隔离技术运行。我们也越来越多地使用 Cloudflare Area 1 的网络钓鱼识别技术来扫描 Web，寻找任何针对 Cloudflare 的网页。最后，我们正在加强 Access 实施，以防止来自未知 VPN、民用代理和基础设施提供商的任何登录。所有这些都是我们提供给客户的相同产品中的标准功能。

这一攻击还使我们目前做得好的三件事情变得更加重要。第一，要求硬件密钥来访问所有应用。和 [Google](https://krebsonsecurity.com/2018/07/google-security-keys-neutralized-employee-phishing/) 一样，自从推出硬件密钥以来，我们还没有遭遇任何成功的钓鱼攻击。通过像 Cloudflare Access 这样的工具，即使对传统应用使用硬件密钥也变得简单易行。如果您的组织对我们如何推出硬件密钥感兴趣，请联系[cloudforceone-irhelp@cloudflare.com](mailto:cloudforceone-irhelp@cloudflare.com)，我们的安全团队将乐于分享我们在此过程中学到的最佳实践。

第二，使用 Cloudflare 自身技术来保护我们的员工和系统。Cloudflare One 的 Access 和 Gateway 等解决方案对于在这次攻击中保持领先至关重要。我们实施的 Access 要求对每一个应用使用硬件密钥。它还为所有应用的身份验证创建一个中央日志位置。如有必要，我们还可以在这里终止可能受到入侵的员工的会话。Gateway 让我们能够迅速关闭类似这样的恶意网站，并了解哪些员工可能已被攻击所欺骗。这些都是我们作为 Cloudflare One 套件的一部分向Cloudflare 客户提供的功能，这次攻击证明了它们的有效性。

第三，拥有多疑但不责难的文化对安全至关重要。落入网络钓鱼骗局的三名员工没有受到训斥。我们都是人，都会犯错。至关重要的是，如果确实犯错了，就要上报而非隐瞒。这起事件再次证明了为什么安全是 Cloudflare 每个团队成员工作的一部分。

## 事件的时间线

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top}

2022-07-20 22:49 UTC

攻击者向 Cloudflare 员工及其家人发送了100 多条短信。

2022-07-20 22:50 UTC

员工开始向 Cloudflare 安全团队报告短信。

2022-07-20 22:52 UTC

证实攻击者的域在用于企业设备的 Cloudflare Gateway 中被阻止。

2022-07-20 22:58 UTC

通过聊天软件和电子邮件向所有员工发送警告信息。

2022-07-20 22:50 UTC 至2022-07-20 23:26 UTC

监控 Okta 系统日志和 Cloudflare Gateway HTTP 日志中的遥测信息，以定位凭据泄露。在发现后清除登录会话并暂停帐户。

2022-07-20 23:26 UTC

钓鱼网站被托管服务商下线。

2022-07-20 23:37 UTC

重置泄露的员工凭据。

2022-07-21 00:15 UTC

深挖攻击者的基础设施和能力

## 破坏的指标

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-nr0u{border-color:inherit;font-family:inherit;font-size:100%;text-align:left;vertical-align:top} .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}

Value | Type | Context and MITRE Mapping  
---|---|---  
cloudflare-okta[.]com hosted on 147[.]182[.]132[.]52 | Phishing URL | [T1566.002](https://attack.mitre.org/techniques/T1566/002/): Phishing: Spear Phishing Link sent to users.  
64547b7a4a9de8af79ff0eefadde2aed10c17f9d8f9a2465c0110c848d85317a | SHA-256 | [T1219](https://attack.mitre.org/techniques/T1219/): Remote Access Software being distributed by the threat actor  
  
值

类型

上下文和 MITRE 映射

cloudflare-okta[.]com 托管于 147[.]182[.]132[.]52

网络钓鱼 URL

[T1566.002](https://attack.mitre.org/techniques/T1566/002/): 网络钓鱼：发送给用户的鱼叉式网络钓鱼链接。

64547b7a4a9de8af79ff0eefadde2aed10c17f9d8f9a2465c0110c848d85317a

SHA-256

[T1219](https://attack.mitre.org/techniques/T1219/): 威胁者分发的远程访问软件

## 你可以做什么

如果您的环境中发现了类似的攻击，欢迎联系 [cloudforceone-irhelp@cloudflare.com](mailto:cloudforceone-irhelp@cloudflare.com)，我们乐于分享有关保障企业安全的最佳实践。另一方面，如果您有兴趣了解我们如何实施安全密钥的更多信息，请参阅我们的 [博客文章](https://blog.cloudflare.com/zh-cn/how-cloudflare-implemented-fido2-and-zero-trust-zh-cn/)，或发送电邮到 [securitykeys@cloudflare.com](mailto:securitykeys@cloudflare.com)。

最后，如果您想和我们一起检测并缓解下一次的攻击，我们的检测和响应团队正在招贤纳士， [欢迎加入我们](https://www.cloudflare.com/zh-cn/careers/)！

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2F2022-07-sms-phishing-attacks%2F&t=%E4%B8%80%E5%9C%BA%E5%A4%8D%E6%9D%82%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E9%AA%97%E5%B1%80%E7%9A%84%E6%9C%BA%E5%88%B6%E5%8F%8A%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%88%90%E5%8A%9F%E9%98%BB%E6%AD%A2%E5%AE%83)[](https://x.com/intent/post?text=%E4%B8%80%E5%9C%BA%E5%A4%8D%E6%9D%82%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E9%AA%97%E5%B1%80%E7%9A%84%E6%9C%BA%E5%88%B6%E5%8F%8A%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%88%90%E5%8A%9F%E9%98%BB%E6%AD%A2%E5%AE%83&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2F2022-07-sms-phishing-attacks%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2F2022-07-sms-phishing-attacks%2F)[](https://bsky.app/intent/compose?text=%E4%B8%80%E5%9C%BA%E5%A4%8D%E6%9D%82%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E9%AA%97%E5%B1%80%E7%9A%84%E6%9C%BA%E5%88%B6%E5%8F%8A%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%88%90%E5%8A%9F%E9%98%BB%E6%AD%A2%E5%AE%83+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2F2022-07-sms-phishing-attacks%2F)[](https://mastodonshare.com/?text=%E4%B8%80%E5%9C%BA%E5%A4%8D%E6%9D%82%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E9%AA%97%E5%B1%80%E7%9A%84%E6%9C%BA%E5%88%B6%E5%8F%8A%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%88%90%E5%8A%9F%E9%98%BB%E6%AD%A2%E5%AE%83&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2F2022-07-sms-phishing-attacks%2F)[](https://www.threads.net/intent/post?text=%E4%B8%80%E5%9C%BA%E5%A4%8D%E6%9D%82%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC%E9%AA%97%E5%B1%80%E7%9A%84%E6%9C%BA%E5%88%B6%E5%8F%8A%E6%88%91%E4%BB%AC%E5%A6%82%E4%BD%95%E6%88%90%E5%8A%9F%E9%98%BB%E6%AD%A2%E5%AE%83+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2F2022-07-sms-phishing-attacks%2F)

## 相关标签

[Cloudflare Access](https://blog.cloudflare.com/zh-cn/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/zh-cn/tag/gateway/)[事后分析](https://blog.cloudflare.com/zh-cn/tag/post-mortem/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[网络钓鱼](https://blog.cloudflare.com/zh-cn/tag/phishing/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
