---
url: https://blog.cloudflare.com/zh-cn/live-patch-security-vulnerabilities-with-ebpf-lsm/
title: \u4f7f\u7528 eBPF Linux \u5b89\u5168\u6a21\u5757\u5b9e\u65f6\u4fee\u8865 Linux \u5185\u6838\u4e2d\u7684\u5b89\u5168\u6f0f\u6d1e | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:50:34.297411+00:00
---

# 使用 eBPF Linux 安全模块实时修补 Linux 内核中的安全漏洞 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/live-patch-security-vulnerabilities-with-ebpf-lsm/

[博客](https://blog.cloudflare.com/zh-cn/)

[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)+1再显示 1 个标签

4 个标签显示 4 个标签

  * 文章标签
  * [Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)
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



[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)

[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)

2022年6月29日

# 使用 eBPF Linux 安全模块实时修补 Linux 内核中的安全漏洞

![Frederick Lawler](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YV7KWFD5VEJ5KEDXS2R1.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Frederick Lawler](https://blog.cloudflare.com/zh-cn/author/frederick/)

阅读时间：6 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/live-patch-security-vulnerabilities-with-ebpf-lsm/)和[繁體中文](https://blog.cloudflare.com/zh-tw/live-patch-security-vulnerabilities-with-ebpf-lsm/).

![Live-patching security vulnerabilities inside the Linux kernel with eBPF Linux Security Module](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BF72JMBAWG18TW78WAGE.png&w=1894&h=947&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA9/j/9PX87+/y7Ozt8O/u8vLy7+/w6Onp+Pr/9fb/7u7z7Ovq7+7r8vHv8PDv6Onr+/3/9/n/8PD07evp8O7p9PLu8fHx6uvv/////P7/9PT58O7t9PHs+Pbx9fX17e/0////////+/v/9/X0+/j0//35+/v88/T5//////////////79///+////////+fr//////////////////////////////v7/////////////////////////////////)

[Linux 安全模块](https://www.kernel.org/doc/html/latest/admin-guide/LSM/index.html) (LSM) 是基于 hook 的框架，用于在 Linux 内核中实现安全策略和强制性访问控制。直到前不久，想要实现安全策略的用户还只有两种选项：配置 AppArmor 或 SELinux 等现有 LSM 模块，或编写自定义内核模块。

[Linux 5.7](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.7) 引入了第三种方式：[LSM 扩充 Berkeley Packet Filter (eBPF)](https://docs.kernel.org/bpf/prog_lsm.html)（简称 LSM BPF）。使用 LSM BPF，开发人员能够在无需配置或加载内核模块的情况下编写精细策略。LSM BPF 程序会在加载时进行验证，然后在调用路径中到达 LSM hook 时执行。

## 让我们解决现实问题

现代操作系统提供了允许“分割”内核资源的设施。例如，FreeBSD 有“jail”，Solaris 有“区域”。Linux 有所不同，它提供一组看起来独立的设施，每个设施允许隔离特定资源。这些称为“命名空间”，多年来一直在内核中增长。它们是 Docker、lxc 或 firejail 等流行工具的基础。许多命名空间都是无争议的，例如 UTS 命名空间，它允许主机系统隐藏其主机名和时间。其他一些命名空间则比较复杂，但直接明了，例如，NET 和 NS (mount) 命名空间就令人难以理解。最后，还有一个非常特殊且稀奇的 USER 命名空间。

USER 命名空间的特殊之处在于，它允许所有者以其中的“根”用户身份操作。具体机制超出了本博客文章的讨论范围，但简单地说，在它的基础上，Docker 等工具才能不以真正的根用户身份操作，并且它还是无根容器等事项的基础。

鉴于其性质，允许无特权的用户访问 USER 命名空间始终会带来极大的安全风险。其中一种风险就是特权提升。

特权提升是操作系统的常见攻击面。用户可以获取特权的一种方式是通过 unshare [syscall](https://en.wikipedia.org/wiki/System_call) 将其命名空间映射到根命名空间，并指定 _CLONE_NEWUSER_ 标志。这会指示 unshare 创建有完整权限的新用户命名空间，并将新用户和组 ID 映射到之前的命名空间。您可以使用 [unshare(1)](https://man7.org/linux/man-pages/man1/unshare.1.html) 程序将根映射到我们的原始命名空间：

在大部分情况下，使用 unshare 没有损害，而且预定以较低特权运行。但是，此 syscall 已被发现用于[提升特权](https://nvd.nist.gov/vuln/detail/CVE-2022-0492)。
    
    
    $ id
    uid=1000(fred) gid=1000(fred) groups=1000(fred) …
    $ unshare -rU
    # id
    uid=0(root) gid=0(root) groups=0(root),65534(nogroup)
    # cat /proc/self/uid_map
             0       1000          1

Syscall _clone_ 和 _clone3_ 值得仔细考虑，因为它们还能够 _CLONE_NEWUSER_ 。但就本文而言，我们将专注于 unshare。

Debian 使用这个[“add sysctl to disallow unprivileged CLONE_NEWUSER by default”](https://sources.debian.org/patches/linux/3.16.56-1+deb8u1/debian/add-sysctl-to-disallow-unprivileged-CLONE_NEWUSER-by-default.patch/)（添加 sysctl 以在默认情况下不允许无特权的 CLONE_NEWUSER）补丁解决了该问题，但这不是主流做法。另一个类似补丁[“sysctl: allow CLONE_NEWUSER to be disabled”](https://lore.kernel.org/all/1453502345-30416-3-git-send-email-keescook@chromium.org/)（sysctl：允许禁用 CLONE_NEWUSER）试图成为主流，但遭到了排挤。一种批评意见是针对特定应用程序[无法切换此功能](https://lore.kernel.org/all/87poq5y0jw.fsf@x220.int.ebiederm.org/)。在文章[《控制对用户命名空间的访问》](https://lwn.net/Articles/673597/)中，作者写道：“...现行补丁似乎很难成为主流。”显然，这些补丁最终并未包含在 vanilla 内核中。

## 我们的解决方案 - LSM BPF

由于限制 USER 命名空间的上游代码似乎行不通，我们决定使用 LSM BPF 来规避这些问题。这样做并不需要修改内核，而且我们可以制定守护访问权限的复杂规则。

### 找到合适的 hook 候选项

首先，让我们找到所需的 syscall。我们可以在 [_include/linux/syscalls.h_](https://elixir.bootlin.com/linux/v5.18/source/include/linux/syscalls.h#L608) 文件中找到原型。这在其中并不太容易查找到，但以下这行：

提供了线索，这样我们就知道接下来要在 [_kernel/fork.c_](https://elixir.bootlin.com/linux/v5.18/source/kernel/fork.c#L3201) 中的什么地方查找。其中发出了对 [_ksys_unshare()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/fork.c#L3082) 的调用。在该函数中深入探查，我们找到对 [_unshare_userns()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/fork.c#L3129) 的调用。此操作有望成功。
    
    
    /* kernel/fork.c */

到目前为止，我们确定了 syscall 实现，但接下来要弄清楚的是，哪些 hook 可供我们使用？因为我们通过[手册页](https://man7.org/linux/man-pages/man2/unshare.2.html)可以知道，unshare 用于改变任务，所以我们来看一下 [_include/linux/lsm_hooks.h_](https://elixir.bootlin.com/linux/v5.18/source/include/linux/lsm_hooks.h#L605) 中基于任务的 hook。早在函数 [_unshare_userns()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/user_namespace.c#L171) 中，我们就看到对 [_prepare_creds()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/cred.c#L252) 的调用。这非常类似于 [_cred_prepare_](https://elixir.bootlin.com/linux/v5.18/source/include/linux/lsm_hooks.h#L624) hook。为了验证我们是否通过 [_prepare_creds()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/cred.c#L291) 获得匹配，我们观察对安全性 hook [_security_prepare_creds()_](https://elixir.bootlin.com/linux/v5.18/source/security/security.c#L1706) 的调用，后者最终会调用该 hook：

不必进一步详细探究细节，我们知道这个 hook 很适合使用，因为 _prepare_creds()_ 刚好就在 _create_user_ns()_ （位于 [_unshare_userns()_](https://elixir.bootlin.com/linux/v5.18/source/kernel/user_namespace.c#L181) 中）之前调用，后者是我们试图阻止的操作。
    
    
    …
    rc = call_int_hook(cred_prepare, 0, new, old, gfp);
    …

### LSM BPF 解决方案

我们打算使用 [eBPF compile once-run everywhere (CO-RE)](https://nakryiko.com/posts/bpf-core-reference-guide/#defining-own-co-re-relocatable-type-definitions) 方法进行编译。这样一来，我们就可以在一个架构上编译，而在另一个架构上加载。但我们打算专门以 x86_64 为目标。适用于 ARM64 的 LSM BPF 仍在开发中，以下代码将无法在该架构上运行。敬请留意 [BPF 邮寄列表](https://lore.kernel.org/bpf/)以关注进展。

测试该解决方案时采用的内核版本不低于 5.15，且配置了以下内容：

启动选项 `lsm=bpf` 在 `CONFIG_LSM` 未在列表中包含“bpf”时可能是必要的。
    
    
    BPF_EVENTS
    BPF_JIT
    BPF_JIT_ALWAYS_ON
    BPF_LSM
    BPF_SYSCALL
    BPF_UNPRIV_DEFAULT_OFF
    DEBUG_INFO_BTF
    DEBUG_INFO_DWARF_TOOLCHAIN_DEFAULT
    DYNAMIC_FTRACE
    FUNCTION_TRACER
    HAVE_DYNAMIC_FTRACE

让我们从序言开始：

 _deny_unshare.bpf.c_ ：

接下来，我们通过以下方式为 CO-RE 调整设置我们的必要结构：
    
    
    #include <linux/bpf.h>
    #include <linux/capability.h>
    #include <linux/errno.h>
    #include <linux/sched.h>
    #include <linux/types.h>
    
    #include <bpf/bpf_tracing.h>
    #include <bpf/bpf_helpers.h>
    #include <bpf/bpf_core_read.h>
    
    #define X86_64_UNSHARE_SYSCALL 272
    #define UNSHARE_SYSCALL X86_64_UNSHARE_SYSCALL

 _deny_unshare.bpf.c_ ：

我们不需要完全充实 struct 的细节，只需提供程序正常运行所需信息的绝对下限。CO-RE 将执行为内核执行调整所需的任何操作。这样就可以很轻松地编写 LSM BPF 程序！
    
    
    …
    
    typedef unsigned int gfp_t;
    
    struct pt_regs {
    	long unsigned int di;
    	long unsigned int orig_ax;
    } __attribute__((preserve_access_index));
    
    typedef struct kernel_cap_struct {
    	__u32 cap[_LINUX_CAPABILITY_U32S_3];
    } __attribute__((preserve_access_index)) kernel_cap_t;
    
    struct cred {
    	kernel_cap_t cap_effective;
    } __attribute__((preserve_access_index));
    
    struct task_struct {
        unsigned int flags;
        const struct cred *cred;
    } __attribute__((preserve_access_index));
    
    char LICENSE[] SEC("license") = "GPL";
    
    …

 _deny_unshare.bpf.c_ ：

第一步是创建程序，第二步是加载程序并附加到我们所需的 hook。有几种方式可实现这一目的：[Cilium ebpf](https://github.com/cilium/ebpf) 项目，[Rust 绑定](https://github.com/libbpf/libbpf-rs)，以及 [ebpf.io](https://ebpf.io/projects/) 项目环境页面上的其他几项。我们打算使用原生 libbpf。
    
    
    SEC("lsm/cred_prepare")
    int BPF_PROG(handle_cred_prepare, struct cred *new, const struct cred *old,
                 gfp_t gfp, int ret)
    {
        struct pt_regs *regs;
        struct task_struct *task;
        kernel_cap_t caps;
        int syscall;
        unsigned long flags;
    
        // If previous hooks already denied, go ahead and deny this one
        if (ret) {
            return ret;
        }
    
        task = bpf_get_current_task_btf();
        regs = (struct pt_regs *) bpf_task_pt_regs(task);
        // In x86_64 orig_ax has the syscall interrupt stored here
        syscall = regs->orig_ax;
        caps = task->cred->cap_effective;
    
        // Only process UNSHARE syscall, ignore all others
        if (syscall != UNSHARE_SYSCALL) {
            return 0;
        }
    
        // PT_REGS_PARM1_CORE pulls the first parameter passed into the unshare syscall
        flags = PT_REGS_PARM1_CORE(regs);
    
        // Ignore any unshare that does not have CLONE_NEWUSER
        if (!(flags & CLONE_NEWUSER)) {
            return 0;
        }
    
        // Allow tasks with CAP_SYS_ADMIN to unshare (already root)
        if (caps.cap[CAP_TO_INDEX(CAP_SYS_ADMIN)] & CAP_TO_MASK(CAP_SYS_ADMIN)) {
            return 0;
        }
    
        return -EPERM;
    }

_deny_unshare.c_ ：

最后，我们使用以下 Makefile 来编译：
    
    
    #include <bpf/libbpf.h>
    #include <unistd.h>
    #include "deny_unshare.skel.h"
    
    static int libbpf_print_fn(enum libbpf_print_level level, const char *format, va_list args)
    {
        return vfprintf(stderr, format, args);
    }
    
    int main(int argc, char *argv[])
    {
        struct deny_unshare_bpf *skel;
        int err;
    
        libbpf_set_strict_mode(LIBBPF_STRICT_ALL);
        libbpf_set_print(libbpf_print_fn);
    
        // Loads and verifies the BPF program
        skel = deny_unshare_bpf__open_and_load();
        if (!skel) {
            fprintf(stderr, "failed to load and verify BPF skeleton\n");
            goto cleanup;
        }
    
        // Attaches the loaded BPF program to the LSM hook
        err = deny_unshare_bpf__attach(skel);
        if (err) {
            fprintf(stderr, "failed to attach BPF skeleton\n");
            goto cleanup;
        }
    
        printf("LSM loaded! ctrl+c to exit.\n");
    
        // The BPF link is not pinned, therefore exiting will remove program
        for (;;) {
            fprintf(stderr, ".");
            sleep(1);
        }
    
    cleanup:
        deny_unshare_bpf__destroy(skel);
        return err;
    }

_Makefile_ ：

### 结果
    
    
    CLANG ?= clang-13
    LLVM_STRIP ?= llvm-strip-13
    ARCH := x86
    INCLUDES := -I/usr/include -I/usr/include/x86_64-linux-gnu
    LIBS_DIR := -L/usr/lib/lib64 -L/usr/lib/x86_64-linux-gnu
    LIBS := -lbpf -lelf
    
    .PHONY: all clean run
    
    all: deny_unshare.skel.h deny_unshare.bpf.o deny_unshare
    
    run: all
    	sudo ./deny_unshare
    
    clean:
    	rm -f *.o
    	rm -f deny_unshare.skel.h
    
    #
    # BPF is kernel code. We need to pass -D__KERNEL__ to refer to fields present
    # in the kernel version of pt_regs struct. uAPI version of pt_regs (from ptrace)
    # has different field naming.
    # See: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=fd56e0058412fb542db0e9556f425747cf3f8366
    #
    deny_unshare.bpf.o: deny_unshare.bpf.c
    	$(CLANG) -g -O2 -Wall -target bpf -D__KERNEL__ -D__TARGET_ARCH_$(ARCH) $(INCLUDES) -c $< -o $@
    	$(LLVM_STRIP) -g $@ # Removes debug information
    
    deny_unshare.skel.h: deny_unshare.bpf.o
    	sudo bpftool gen skeleton $< > $@
    
    deny_unshare: deny_unshare.c deny_unshare.skel.h
    	$(CC) -g -Wall -c $< -o $@.o
    	$(CC) -g -o $@ $(LIBS_DIR) $@.o $(LIBS)
    
    .DELETE_ON_ERROR:

在新的终端窗口中，运行：

在另一个终端窗口中，我们成功被阻止！
    
    
    $ make run
    …
    LSM loaded! ctrl+c to exit.

策略还有一项始终允许特权通过的功能：
    
    
    $ unshare -rU
    unshare: unshare failed: Cannot allocate memory
    $ id
    uid=1000(fred) gid=1000(fred) groups=1000(fred) …

在无特权的情况下，syscall 会及早中止。在有特权的情况下，对性能有何影响？
    
    
    $ sudo unshare -rU
    # id
    uid=0(root) gid=0(root) groups=0(root)

### 测量性能

我们打算使用单行 unshare 来映射用户命名空间，并在其中执行测量的命令：

通过 syscall unshare enter/exit 的 CPU 周期分辨率，我们将以根用户身份测量以下内容：
    
    
    $ unshare -frU --kill-child -- bash -c "exit 0"

  1. 不带策略运行的命令
  2. 带策略运行的命令



我们将使用 [ftrace](https://docs.kernel.org/trace/ftrace.html) 记录测量：

目前，我们专门为 unshare 的 syscall enter 和 exit 启用了跟踪。现在，我们设置 enter/exit 调用的时间分辨率，计算 CPU 周期数量：
    
    
    $ sudo su
    # cd /sys/kernel/debug/tracing
    # echo 1 > events/syscalls/sys_enter_unshare/enable ; echo 1 > events/syscalls/sys_exit_unshare/enable

接下来，我们开始测量：
    
    
    # echo 'x86-tsc' > trace_clock 

在新的终端窗口中运行策略，然后运行下一个 syscall：
    
    
    # unshare -frU --kill-child -- bash -c "exit 0" &
    [1] 92014

现在，我们来比较两个调用：
    
    
    # unshare -frU --kill-child -- bash -c "exit 0" &
    [2] 92019

unshare-92014 使用了 63294 个周期。
    
    
    # cat trace
    # tracer: nop
    #
    # entries-in-buffer/entries-written: 4/4   #P:8
    #
    #                                _-----=> irqs-off
    #                               / _----=> need-resched
    #                              | / _---=> hardirq/softirq
    #                              || / _--=> preempt-depth
    #                              ||| / _-=> migrate-disable
    #                              |||| /     delay
    #           TASK-PID     CPU#  |||||  TIMESTAMP  FUNCTION
    #              | |         |   |||||     |         |
             unshare-92014   [002] ..... 762950852559027: sys_unshare(unshare_flags: 10000000)
             unshare-92014   [002] ..... 762950852622321: sys_unshare -> 0x0
             unshare-92019   [007] ..... 762975980681895: sys_unshare(unshare_flags: 10000000)
             unshare-92019   [007] ..... 762975980752033: sys_unshare -> 0x0
    

unshare-92019 使用了 70138 个周期。

这两个测量之间有 6,844 个（大约 10%）周期的差值。结果还不赖！

这些数字是针对单个 syscall 的情况，调用代码越频繁，这些数字也会相应累加。Unshare 通常在创建任务时调用，而在程序正常执行期间不会重复调用。需要对您的用例进行仔细考虑和测量。

## 结尾

我们大致了解了 LSM BPF 的基本概念，如何使用 unshare 将用户映射到根，以及如何通过在 eBPF 中实现解决方案来解决现实问题。找到合适的 hook 并不容易，需要开展一些试验，还要编写大量内核代码。幸运的是，其他部分都比较简单。由于策略是采用 C 语言编写的，我们可以通过精细调整策略来解决我们的问题。这意味着，可以使用允许列表扩展该策略，允许特定程序或用户继续使用无特权的 unshare。最后，我们考察了该程序的性能影响，并发现阻止攻击手段所需的开销是值得的。

“Cannot allocate memory”（无法分配内存）并不是拒绝权限的明确错误消息。我们提议了一个[补丁](https://lore.kernel.org/all/20220608150942.776446-1-fred@cloudflare.com/)，用于在调用堆栈中从 _cred_prepare_ hook 向上传播错误代码。最终，我们得出结论，新的 hook 更适合解决该问题。敬请关注！

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F&t=%E4%BD%BF%E7%94%A8%20eBPF%20Linux%20%E5%AE%89%E5%85%A8%E6%A8%A1%E5%9D%97%E5%AE%9E%E6%97%B6%E4%BF%AE%E8%A1%A5%20Linux%20%E5%86%85%E6%A0%B8%E4%B8%AD%E7%9A%84%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)[](https://x.com/intent/post?text=%E4%BD%BF%E7%94%A8+eBPF+Linux+%E5%AE%89%E5%85%A8%E6%A8%A1%E5%9D%97%E5%AE%9E%E6%97%B6%E4%BF%AE%E8%A1%A5+Linux+%E5%86%85%E6%A0%B8%E4%B8%AD%E7%9A%84%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)[](https://bsky.app/intent/compose?text=%E4%BD%BF%E7%94%A8+eBPF+Linux+%E5%AE%89%E5%85%A8%E6%A8%A1%E5%9D%97%E5%AE%9E%E6%97%B6%E4%BF%AE%E8%A1%A5+Linux+%E5%86%85%E6%A0%B8%E4%B8%AD%E7%9A%84%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)[](https://mastodonshare.com/?text=%E4%BD%BF%E7%94%A8+eBPF+Linux+%E5%AE%89%E5%85%A8%E6%A8%A1%E5%9D%97%E5%AE%9E%E6%97%B6%E4%BF%AE%E8%A1%A5+Linux+%E5%86%85%E6%A0%B8%E4%B8%AD%E7%9A%84%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)[](https://www.threads.net/intent/post?text=%E4%BD%BF%E7%94%A8+eBPF+Linux+%E5%AE%89%E5%85%A8%E6%A8%A1%E5%9D%97%E5%AE%9E%E6%97%B6%E4%BF%AE%E8%A1%A5+Linux+%E5%86%85%E6%A0%B8%E4%B8%AD%E7%9A%84%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Flive-patch-security-vulnerabilities-with-ebpf-lsm%2F)

## 相关标签

[Linux](https://blog.cloudflare.com/zh-cn/tag/linux/)[Programming](https://blog.cloudflare.com/zh-cn/tag/programming/)[安全](https://blog.cloudflare.com/zh-cn/tag/security/)[深入剖析](https://blog.cloudflare.com/zh-cn/tag/deep-dive/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
