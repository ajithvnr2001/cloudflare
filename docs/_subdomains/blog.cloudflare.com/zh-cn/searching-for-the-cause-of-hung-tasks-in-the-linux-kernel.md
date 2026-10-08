---
url: https://blog.cloudflare.com/zh-cn/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/
title: \u5bfb\u627e Linux \u5185\u6838\u4e2d\u4efb\u52a1\u6302\u8d77\u7684\u539f\u56e0 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:50:05.786051+00:00
---

# 寻找 Linux 内核中任务挂起的原因 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/

[博客](https://blog.cloudflare.com/zh-cn/)

[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[内核](https://blog.cloudflare.com/zh-cn/tag/kernel/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)+1再显示 1 个标签

4 个标签显示 4 个标签

  * 文章标签
  * [Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[内核](https://blog.cloudflare.com/zh-cn/tag/kernel/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)[监控](https://blog.cloudflare.com/zh-cn/tag/monitoring/)
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



[监控](https://blog.cloudflare.com/zh-cn/tag/monitoring/)

[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[内核](https://blog.cloudflare.com/zh-cn/tag/kernel/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)[监控](https://blog.cloudflare.com/zh-cn/tag/monitoring/)

2025年2月14日

# 寻找 Linux 内核中任务挂起的原因

![Oxana Kharitonova](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462M0EFJXTMW95T83V5454.png&w=64&h=64&f=webp&fit=cover&position=center)![Jesper Brouer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW499RS2WW80VBYFGEW0TADD.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Oxana Kharitonova](https://blog.cloudflare.com/zh-cn/author/oxana/)和[Jesper Brouer](https://blog.cloudflare.com/zh-cn/author/jesper-brouer/)

阅读时间：8 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/)和[繁體中文](https://blog.cloudflare.com/zh-tw/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/).

![BLOG-2660 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46Y20YJ525ZDYYEE488MY4.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vv+193owMvdzNfl5ezy7/Lz6unq/////f7/29/rxMzez9jm5uzz8fP17Ozt////////4eTuytDh1Nro6u/19Pb48fDx////////6er00tbn2uDu7/P6+fv99vb3////////8PL829/w4uj29fr//v//+/v8////////9vn/4un56fH++///////////////////+/7/6O//7vf//////////////////////P//6vL/8Pr/////////////)

根据您的配置，Linux 内核可能在其日志中生成挂起任务警告消息。搜索互联网和内核文档，您可以找到一个简短的解释，即内核进程卡在不可中断状态，并且在意外长的时间内没有被调度到 CPU 上运行。这解释了警告的含义，但没有提供它发生的原因。在这篇博文中，我们将探讨挂起任务警告的工作原理、它为什么会发生、这是 Linux 内核还是应用程序本身的错误，以及是否值得对其进行监控。

### INFO：任务 XXX:1495882 已被阻止超过 YYY 秒。

内核日志中的挂起任务消息如下所示：
    
    
    INFO: task XXX:1495882 blocked for more than YYY seconds.
         Tainted: G          O       6.6.39-cloudflare-2024.7.3 #1
    "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
    task:XXX         state:D stack:0     pid:1495882 ppid:1      flags:0x00004002
    . . .

Linux 中的进程可以处于不同的状态。一些进程正在运行或准备在 CPU 上运行——它们处于 [`_TASK_RUNNING_`](https://elixir.bootlin.com/linux/v6.12.6/source/include/linux/sched.h#L99) 状态。另一些进程正在等待某些信号或事件发生，例如网络数据包到达或来自用户的终端输入。它们处于 `TASK_INTERRUPTIBLE` 状态，并且可以在此状态下停留任意长的时间，直到被信号唤醒。关于这些状态，最重要的一点是它们仍然可以接收信号，并被信号终止。相比之下，处于 `TASK_UNINTERRUPTIBLE` 状态的进程只等待某些特殊类型的事件将其唤醒，并且不能被信号中断。直到进程退出此状态后，才会发送信号，只有系统重新启动才能清除进程。在上面显示的日志中，它用字母 `D` 标记。

如果这个唤醒事件没有发生或者发生时有显著延迟，会怎么样？（“显著延迟”可能是几秒或几分钟，具体取决于系统。）那么我们的依赖进程就会以这个状态挂起。如果这个依赖进程持有某个锁并阻止其他进程获取该锁，会怎么样？或者如果我们看到许多进程处于 D 状态，又会怎么样？它可能会告诉我们，一些系统资源不堪重负或无法正常工作。同时，这种状态非常有价值，特别是当我们想保留进程内存时。如果部分数据写入磁盘，而另一部分仍在进程内存中，这种状态就很有用——我们不希望磁盘上的数据不一致。或者，当出现错误时，我们可能想要进程内存的快照。为了保留此行为，但使其更受控制，内核中引入了一种新状态：[` _TASK_KILLABLE_`](https://lwn.net/Articles/288056/)——它仍然保护进程，但允许使用致命信号终止进程。

### Linux 如何识别挂起的进程

Linux 内核有一个特殊的线程，称为 `khungtaskd`。它会根据设置定期运行，迭代所有处于 `D` 状态的进程。如果一个进程处于这种状态超过 YYY 秒，我们将在内核日志中看到一条消息。您可以根据意愿对这个后台程序的一些设置进行更改：
    
    
    $ sudo sysctl -a --pattern hung
    kernel.hung_task_all_cpu_backtrace = 0
    kernel.hung_task_check_count = 4194304
    kernel.hung_task_check_interval_secs = 0
    kernel.hung_task_panic = 0
    kernel.hung_task_timeout_secs = 10
    kernel.hung_task_warnings = 200

在 Cloudflare，我们将通知阈值 `kernel.hung_task_timeout_secs` 从默认的 120 秒更改为 10 秒。您可以根据配置以及此延迟对您的重要性来调整系统的值。如果进程在 D 状态下停留的时间超过 `hung_task_timeout_secs` 秒，则会写入日志条目，并且我们的内部监控系统会根据此日志发出警报。这里的另一个重要设置是 `kernel.hung_task_warnings`：将发送到日志的消息总数。我们将其限制为 200 条消息，并每 15 分钟重置一次。这让我们不会被同一个问题所困扰，同时不会让我们的监控停止太久。您可以通过[ _将值设置为“-1”_](https://docs.kernel.org/admin-guide/sysctl/kernel.html#hung-task-warnings)来使其无限制。

为了更好地理解挂起任务的根本原因以及系统会受到怎样的影响，我们来看几个更详细的示例。

### 示例 1：XFS

通常，日志中会显示一个有意义的进程或应用程序名称，但有时您可能会看到这样的内容：
    
    
    INFO: task kworker/13:0:834409 blocked for more than 11 seconds.
     	Tainted: G      	O   	6.6.39-cloudflare-2024.7.3 #1
    "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
    task:kworker/13:0	state:D stack:0 	pid:834409 ppid:2   flags:0x00004000
    Workqueue: xfs-sync/dm-6 xfs_log_worker

在这条日志中，`kworker` 是内核线程。它用作一种推迟机制，即某项工作将安排在未来执行。在 `kworker` 下，工作是从不同的任务中汇总而来的，这使得很难判断哪个应用程序正在经历延迟。幸运的是，`kworker` 会伴随着 [`_Workqueue_`](https://docs.kernel.org/core-api/workqueue.html) 行出现。`Workqueue` 是一个链接列表，通常在内核中预定义，这些工作将由 `kworker` 添加到队列中并按照添加顺序执行。`Workqueue` 名称 `xfs-sync` 及[ _其指向的函数_](https://elixir.bootlin.com/linux/v6.12.6/source/kernel/workqueue.c#L6096)`xfs_log_worker`，可能提供了很好的线索。在这里，我们可以假设 [_XFS_](https://en.wikipedia.org/wiki/XFS) 承受压力并检查相关指标。它帮助我们发现，由于某些配置更改，我们忘记了前段时间为[ _加快 Linux 磁盘加密速度_](https://blog.cloudflare.com/speeding-up-linux-disk-encryption/)而引入的 `no_read_workqueue`/`no_write_workqueue` 标志。

 _总结_ ：这种情况下，系统没有发生任何严重的问题，但是挂起任务警告提醒我们，文件系统的速度已经变慢。

### 示例 2：Coredump

我们来看看下一个挂起任务日志及其解码的堆栈跟踪：
    
    
    INFO: task test:964 blocked for more than 5 seconds.
          Not tainted 6.6.72-cloudflare-2025.1.7 #1
    "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
    task:test            state:D stack:0     pid:964   ppid:916    flags:0x00004000
    Call Trace:
    <TASK>
    __schedule (linux/kernel/sched/core.c:5378 linux/kernel/sched/core.c:6697) 
    schedule (linux/arch/x86/include/asm/preempt.h:85 (discriminator 13) linux/kernel/sched/core.c:6772 (discriminator 13)) 
    [do_exit (linux/kernel/exit.c:433 (discriminator 4) linux/kernel/exit.c:825 (discriminator 4)) 
    ? finish_task_switch.isra.0 (linux/arch/x86/include/asm/irqflags.h:42 linux/arch/x86/include/asm/irqflags.h:77 linux/kernel/sched/sched.h:1385 linux/kernel/sched/core.c:5132 linux/kernel/sched/core.c:5250) 
    do_group_exit (linux/kernel/exit.c:1005) 
    get_signal (linux/kernel/signal.c:2869) 
    ? srso_return_thunk (linux/arch/x86/lib/retpoline.S:217) 
    ? hrtimer_try_to_cancel.part.0 (linux/kernel/time/hrtimer.c:1347) 
    arch_do_signal_or_restart (linux/arch/x86/kernel/signal.c:310) 
    ? srso_return_thunk (linux/arch/x86/lib/retpoline.S:217) 
    ? hrtimer_nanosleep (linux/kernel/time/hrtimer.c:2105) 
    exit_to_user_mode_prepare (linux/kernel/entry/common.c:176 linux/kernel/entry/common.c:210) 
    syscall_exit_to_user_mode (linux/arch/x86/include/asm/entry-common.h:91 linux/kernel/entry/common.c:141 linux/kernel/entry/common.c:304) 
    ? srso_return_thunk (linux/arch/x86/lib/retpoline.S:217) 
    do_syscall_64 (linux/arch/x86/entry/common.c:88) 
    entry_SYSCALL_64_after_hwframe (linux/arch/x86/entry/entry_64.S:121) 
    </TASK>

堆栈跟踪显示进程或应用程序 `test` 被阻止 `for more than 5 seconds`。我们可以通过名称认出这个用户空间应用程序，但它为什么被阻止了？在查找原因时，检查堆栈跟踪总是有帮助的。这里最值得注意的一行是 `do_exit (linux/kernel/exit.c:433 (discriminator 4) linux/kernel/exit.c:825 (discriminator 4))`。[ _源代码_](https://elixir.bootlin.com/linux/v6.6.67/source/kernel/exit.c#L825)指向 `coredump_task_exit` 函数。此外，检查进程指标发现，应用程序在日志中出现警告消息时崩溃。当进程基于某些信号集（异常）终止时，[ _Linux 内核可以提供核心转储文件_](https://man7.org/linux/man-pages/man5/core.5.html)（如果启用）。“当进程终止时，内核会在退出之前为进程内存创建快照，并将其写入文件或通过套接字发送到另一个处理程序”——这样的机制可以是 [_systemd-coredump_](https://systemd.io/COREDUMP/) 或由您自定义。发生这种情况时，内核会将进程移至 `D` 状态以保留其内存并提前终止。进程内存使用率越高，获取核心转储文件所需的时间就越长，并且收到挂起任务警告的可能性就越高。

让我们用一个小型 Go 程序来触发它，以验证我们的假设。我们将使用默认的 Linux coredump 处理程序，并将挂起任务阈值降低至 1 秒。

Coredump 设置：
    
    
    $ sudo sysctl -a --pattern kernel.core
    kernel.core_pattern = core
    kernel.core_pipe_limit = 16
    kernel.core_uses_pid = 1

您可以对 [_sysctl_](https://man7.org/linux/man-pages/man8/sysctl.8.html) 进行更改：
    
    
    $ sudo sysctl -w kernel.core_uses_pid=1

挂起任务设置：
    
    
    $ sudo sysctl -a --pattern hung
    kernel.hung_task_all_cpu_backtrace = 0
    kernel.hung_task_check_count = 4194304
    kernel.hung_task_check_interval_secs = 0
    kernel.hung_task_panic = 0
    kernel.hung_task_timeout_secs = 1
    kernel.hung_task_warnings = -1

Go 程序：
    
    
    $ cat main.go
    package main
    
    import (
    	"os"
    	"time"
    )
    
    func main() {
    	_, err := os.ReadFile("test.file")
    	if err != nil {
    		panic(err)
    	}
    	time.Sleep(8 * time.Minute) 
    }

该程序将一个 10 GB 的文件读入进程内存。让我们来创建文件：
    
    
    $ yes this is 10GB file | head -c 10GB > test.file

最后一步是构建 Go 程序，使其崩溃，并观察内核日志：
    
    
    $ go mod init test
    $ go build .
    $ GOTRACEBACK=crash ./test
    $ (Ctrl+\)

太棒了！我们可以看到挂起任务警告：
    
    
    $ sudo dmesg -T | tail -n 31
    INFO: task test:8734 blocked for more than 22 seconds.
          Not tainted 6.6.72-cloudflare-2025.1.7 #1
          Blocked by coredump.
    "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
    task:test            state:D stack:0     pid:8734  ppid:8406   task_flags:0x400448 flags:0x00004000

顺便问一下，您注意到日志中的 `Blocked by coredump.` 行了吗？它最近被添加到[ _上游_](https://git.kernel.org/pub/scm/linux/kernel/git/akpm/mm.git/commit/?h=mm-nonmm-stable&id=23f3f7625cfb55f92e950950e70899312f54afb7)代码中，以提高可见性并消除进程本身的责任。该补丁还添加了 `task_flags` 信息，因为通过标志 [`_PF_POSTCOREDUMP_`](https://elixir.bootlin.com/linux/v6.13.1/source/include/linux/sched.h#L1675) 检测到 `Blocked by coredump`，了解所有任务标志对于进一步分析根本原因很有用。

 _总结_ ：此示例表明，即使所有迹象都表明问题出在应用程序上，但真正的根本原因可能是其他内容——在本例中是 `coredump`。

### 示例 3：rtnl_mutex

这个问题很难调试。通常，警报仅限于一两个不同的进程，这意味着只有特定的应用程序或子系统遇到问题。在这个示例中，我们看到数十个不相关的任务挂起数分钟，而且随着时间的推移并没有任何改进。日志中没有其他内容，大多数系统指标都没有问题，并且现有流量得到服务，但无法通过 ssh 连接到服务器。新的 Kubernetes 容器创建也停滞不前。初始分析不同任务的堆栈跟踪表明，所有跟踪都仅限于三个函数：
    
    
    rtnetlink_rcv_msg+0x9/0x3c0
    dev_ethtool+0xc6/0x2db0 
    bonding_show_bonds+0x20/0xb0

进一步调查显示，所有这些函数都在等待获取 [`_rtnl_lock_`](https://elixir.bootlin.com/linux/v6.6.74/source/net/core/rtnetlink.c#L76)。看起来某个应用程序获取了 `rtnl_mutex` 但没有释放它。所有其他进程都处于 `D` 状态，等待此锁。

RTNL 锁主要由内核网络子系统用于与网络相关的配置，包括写入和读取。RTNL 是一个全局 **mutex** 锁，但正在进行[ _上游工作_](https://lpc.events/event/18/contributions/1959/)来按网络命名空间 (netns) 拆分 RTNL。

从挂起任务报告中，我们可以观察到因等待锁而停滞的“受害者”，但我们如何识别持有此锁时间过长的任务？为了解决这个问题，我们通过 `bpftrace` 脚本利用 `BPF`，因为这使我们能够检查正在运行的内核状态。[ _内核的 mutex 实现_](https://elixir.bootlin.com/linux/v6.6.75/source/include/linux/mutex.h#L67)有一个名为 `owner` 的结构体成员。它包含一个指针，从拥有 mutex 的进程指向 [`_task_struct_`](https://elixir.bootlin.com/linux/v6.6.75/source/include/linux/sched.h#L746)，只不过它被编码为 `atomic_long_t` 类型。这是因为 mutex 实现将一些状态信息存储在此指针的低 3 位（掩码 0x7）中。因此，要读取和取消引用此 `task_struct` 指针，我们必须首先屏蔽低位 (0x7)。

用于确定谁持有 mutex 的 `bpftrace` 脚本如下所示：
    
    
    #!/usr/bin/env bpftrace
    interval:s:10 {
      $rtnl_mutex = (struct mutex *) kaddr("rtnl_mutex");
      $owner = (struct task_struct *) ($rtnl_mutex->owner.counter & ~0x07);
      if ($owner != 0) {
        printf("rtnl_mutex->owner = %u %s\n", $owner->pid, $owner->comm);
      }
    }

在此脚本中，`rtnl_mutex` 锁是一个全局锁，其地址可通过 `/proc/kallsyms` 公开——使用 `bpftrace` 辅助函数 `kaddr()`，我们可以从 `kallsyms` 访问 struct mutex 指针。因此，我们可以定期（通过 `interval:s:10`）检查是否有进程持有此锁。

输出如下：
    
    
    rtnl_mutex->owner = 3895365 calico-node

这使我们能够快速识别出 `calico-node` 是持有 RTNL 锁时间过长的进程。为了快速观察此进程本身停滞的位置，可以通过 `/proc/3895365/stack` 获取调用堆栈。这向我们表明，根本原因是 Wireguard 配置更改，函数 `wg_set_device()` 持有 RTNL 锁，而 `peer_remove_after_dead()` 等待 `napi_disable()` 调用的时间过长。我们继续通过一个名为 [`_drgn_`](https://drgn.readthedocs.io/en/latest/user_guide.html#stack-traces) 的工具进行调试，这是一个可编程的调试器，可以通过类似 Python 的交互式 shell 调试正在运行的内核。我们仍然没有发现 Wireguard 问题的根本原因，并[ _向上游寻求_](https://lore.kernel.org/lkml/CALrw=nGoSW=M-SApcvkP4cfYwWRj=z7WonKi6fEksWjMZTs81A@mail.gmail.com/)帮助，这就是另一个故事了。

 _总结_ ：挂起任务消息是我们在内核日志中唯一拥有的消息。这些消息的每个堆栈跟踪都是唯一的，但通过仔细分析，我们可以发现相似之处，并继续使用其他工具进行调试。

### 结语

您的系统可能有不同的挂起任务警告，我们也有许多其他情况未在此处提及。每种情况都是独一无二的，并没有标准的调试方法。但希望这篇博客文章能帮助您更好地理解为什么需要启用这些警告、它们如何工作，以及它们背后的含义。我们也试图为调试过程提供一些导航指导：

  * 分析堆栈跟踪可能是一个不错的调试起点，即使所有消息看起来都不相关，就像我们在示例 3 中看到的那样
  * 请记住，警报可能会产生误导，指向受害者而不是犯罪者，如示例 2 和示例 3 中所示
  * 如果内核没有将应用程序调度到 CPU 上，而是将其置于 D 状态并发出警告——真正的问题可能存在于应用程序代码中



祝您调试顺利，并希望本文内容将对您有所帮助！

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F&t=%E5%AF%BB%E6%89%BE%20Linux%20%E5%86%85%E6%A0%B8%E4%B8%AD%E4%BB%BB%E5%8A%A1%E6%8C%82%E8%B5%B7%E7%9A%84%E5%8E%9F%E5%9B%A0)[](https://x.com/intent/post?text=%E5%AF%BB%E6%89%BE+Linux+%E5%86%85%E6%A0%B8%E4%B8%AD%E4%BB%BB%E5%8A%A1%E6%8C%82%E8%B5%B7%E7%9A%84%E5%8E%9F%E5%9B%A0&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)[](https://bsky.app/intent/compose?text=%E5%AF%BB%E6%89%BE+Linux+%E5%86%85%E6%A0%B8%E4%B8%AD%E4%BB%BB%E5%8A%A1%E6%8C%82%E8%B5%B7%E7%9A%84%E5%8E%9F%E5%9B%A0+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)[](https://mastodonshare.com/?text=%E5%AF%BB%E6%89%BE+Linux+%E5%86%85%E6%A0%B8%E4%B8%AD%E4%BB%BB%E5%8A%A1%E6%8C%82%E8%B5%B7%E7%9A%84%E5%8E%9F%E5%9B%A0&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)[](https://www.threads.net/intent/post?text=%E5%AF%BB%E6%89%BE+Linux+%E5%86%85%E6%A0%B8%E4%B8%AD%E4%BB%BB%E5%8A%A1%E6%8C%82%E8%B5%B7%E7%9A%84%E5%8E%9F%E5%9B%A0+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fsearching-for-the-cause-of-hung-tasks-in-the-linux-kernel%2F)

## 相关标签

[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[内核](https://blog.cloudflare.com/zh-cn/tag/kernel/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)[监控](https://blog.cloudflare.com/zh-cn/tag/monitoring/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
