---
url: https://blog.cloudflare.com/zh-cn/making-rust-workers-reliable/
title: \u63d0\u9ad8 Rust Workers \u53ef\u9760\u6027\uff1awasm-bindgen \u4e2d\u7684 panic \u9519\u8bef\u4e0e\u4e2d\u6b62\u6062\u590d\u673a\u5236 | Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:34:39.830431+00:00
---

# 提高 Rust Workers 可靠性：wasm-bindgen 中的 panic 错误与中止恢复机制 | Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/making-rust-workers-reliable/

[博客](https://blog.cloudflare.com/zh-cn/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Internship Experience](https://blog.cloudflare.com/zh-cn/tag/internship-experience/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)+8再显示 8 个标签

11 个标签显示 11 个标签

  * 文章标签
  * [Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[Rust Workers](https://blog.cloudflare.com/zh-cn/tag/rust-workers/)[WASM](https://blog.cloudflare.com/zh-cn/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/zh-cn/tag/webassembly/)[可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)
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



[Rust Workers](https://blog.cloudflare.com/zh-cn/tag/rust-workers/)[WASM](https://blog.cloudflare.com/zh-cn/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/zh-cn/tag/webassembly/)[可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Internship Experience](https://blog.cloudflare.com/zh-cn/tag/internship-experience/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[Rust Workers](https://blog.cloudflare.com/zh-cn/tag/rust-workers/)[WASM](https://blog.cloudflare.com/zh-cn/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/zh-cn/tag/webassembly/)[可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)

2026年4月22日

# 提高 Rust Workers 可靠性：wasm-bindgen 中的 panic 错误与中止恢复机制

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/zh-cn/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/zh-cn/author/hood/)和[Logan Gatlin](https://blog.cloudflare.com/zh-cn/author/logan-gatlin/)

阅读时间：9 分钟

复制 URL

本文另有 [English](https://blog.cloudflare.com/making-rust-workers-reliable/)、[日本語](https://blog.cloudflare.com/ja-jp/making-rust-workers-reliable/)、[한국어](https://blog.cloudflare.com/ko-kr/making-rust-workers-reliable/)和[繁體中文](https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/).

![BLOG-3145 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HQEZP84STFXFD0H3EBY7.png&w=2048&h=1152&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88O7x3uLt3eXz6e758/L19u/r//////7+5Ofzx9XuxNb01uP66ez38u7t//////7/2OH2rsjwqMj2w9j93+f77+3x////////1eL6psf0nsX6vdf/3uj/8PD2////////4Oz/t9T6sdT/y+P/5/H/9/f7////////8fr/1en/0ur/5Pb/9v7/////////////////7fr/7Pz/+P//////////////////////9///9v//////////////)

[_Rust Workers_](https://developers.cloudflare.com/workers/languages/rust/) 是 Cloudflare Workers 平台上运行的一个工具，它将 Rust 代码编译为 WebAssembly 格式，但我们发现 WebAssembly 存在一些缺陷。当出现 panic 错误或意外中止时，运行时可能处于未定义状态。对于 Rust Workers 用户而言，panic 往往会产生致命影响：不仅污染实例，甚至可能导致 Worker 在一段时间内无法响应。

虽然我们能够检测并缓解这些问题，但 Rust Worker 仍然有可能意外失败，并导致其他请求也随之失败。Worker 中未处理的 Rust 中止会影响单个请求，可能升级为影响同级请求的更大故障，甚至持续影响新的传入请求。问题的根源在于 wasm-bindgen，这是生成 Rust worker 所依赖的 Rust-to-JavaScript 绑定的核心项目，而 wasm-bindgen 缺乏内置的恢复机制。

在这篇文章中，我们将分享最新版 Rust Workers 如何处理全面的 Wasm 错误恢复，以解决这种由中止引起的沙箱污染问题。作为我们[ _去年在 wasm-bindgen 组织内部_](https://github.com/wasm-bindgen/wasm-bindgen)合作的一部分，我们已将这项工作贡献融入 [_wasm-bindgen_](https://blog.rust-lang.org/inside-rust/2025/07/21/sunsetting-the-rustwasm-github-org/)。首先，我们添加了 `panic=unwind` 支持，确保单个失败的请求不会影响其他请求；其次，我们添加了中止恢复机制，保证 Wasm 中的 Rust 代码在中止后绝不会再次执行。 

## 初始恢复缓解措施

我们最开始尝试解决这方面的可靠性问题时，侧重于理解和控制生产环境中的 Rust Worker 因 Rust panic 和中止引起的故障。我们引入了自定义 Rust panic 处理程序来跟踪 Worker 中的故障状态，并在处理后续请求之前触发了完整的应用重新初始化。在 JavaScript 端，这需要使用基于代理的间接寻址来封装 Rust-JavaScript 调用边界，以确保以一致的方式封装所有入口点。我们还对生成的绑定进行了针对性修改，以便在故障发生后正确地重新初始化 WebAssembly 模块。

虽然这种方法依赖于自定义 JavaScript 逻辑，但它证明了可靠的恢复是可以实现的，并且排除了我们在实践中遇到的持续性故障模式。从 0.6 版本开始，此解决方案已默认提供给所有 workers-rs 用户，并为下文所述的更普遍的、上游中止恢复机制奠定了基础。

## 使用 WebAssembly Exception Handling，实施 `panic=unwind`

上文描述的中止恢复机制可确保 Worker 能够在出现故障时继续运行，但这些机制是通过重新初始化整个应用来实现这个目标。对于无状态请求处理程序来说，这没有问题。但对于在内存中保存有意义状态的工作负载（例如 Durable Objects）来说，重新初始化意味着完全丢失该状态。一个请求中的单个 panic 可能会清除其他并发请求正在使用的内存状态。

在大多数原生 Rust 环境中，可以进行 panic unwind 处理，从而允许析构函数运行，程序在不丢失状态的情况下恢复。在 WebAssembly 中，情况历来截然不同。通过 `wasm32-unknown-unknown` 编译成 Wasm 的 Rust 默认使用 `panic=abort`，因此，Rust Worker 内部的 panic 会突然生成 `unreachable` 指令，导致 Wasm 退出执行并抛出 `WebAssembly.RuntimeError` 错误给 JS。

为了从 panic 中恢复且不丢弃实例状态，我们需要 wasm-bindgen 中对 `wasm32-unknown-unknown` 的 `panic=unwind` 支持。WebAssembly Exception Handling 提案使这成为可能，该提案在 2023 年获得了广泛的引擎支持。

我们首先使用 `RUSTFLAGS='-Cpanic=unwind' cargo build -Zbuild-std` 进行编译，这重新构建支持 unwind 的标准库，并生成具备适当 panic unwind 处理策略的代码。例如：
    
    
    struct HasDropA;
    struct HasDropB;
    extern "C" {
        fn imported_func();
    }
    
    fn some_func() {
        let a = HasDropA;
        let b = HasDropB;
        imported_func();
    }

编译为 WebAssembly 格式的代码如下：
    
    
    try
      call <imported_func>
    catch_all
      call <drop_b>
      call <drop_a>
      rethrow
    end
    call <drop_b>
    call <drop_a>

这可确保即使 `imported_func()` panic 错误，析构函数仍然会运行。类似地，`std::panic::catch_unwind(|| some_func())` 编译后的格式为：
    
    
    try
      call <some_func>
      ;; set result to Ok(return value)
    catch
      try
        call <std::panicking::catch_unwind::cleanup>
        ;; set result to Err(panic payload)
      catch_all
        call <core::panicking::cannot_unwind>
        unreachable
      end
    end

要使这种编译方式能够端到端正常发挥作用，我们对 wasm-bindgen 工具链进行了一些更改。WebAssembly 解析器 Walrus 无法处理 try/catch 指令，因此，我们添加了对它们的支持。描述符解释器还需要学会如何评估包含异常处理块的代码。就在这时，可以使用 `panic=unwind` 构建完整的应用。

最后一步是修改 wasm-bindgen 生成的导出，以便在 Rust-JavaScript 边界处捕获 panic，并将其显示为 JavaScript `PanicError` 异常。需要注意的一点是：Rust 会捕获外部异常，并在通过 `extern "C"` 函数进行 unwind 时终止，因此，需要将导出标记为 `extern "C-unwind"`，以明确支持跨边界进行 unwind 处理。如果使用 futures 库，panic 会拒绝 JavaScript `Promise`，并抛出 `PanicError`。

闭包问题需要特别注意，确保通过新的` MaybeUnwindSafe` trait 来正确检查 unwind 安全性，该 trait 仅在使用 `panic=unwind` 进行构建时才会检查 `UnwindSafe`。但这很快暴露了一个问题：许多闭包捕获了 unwind 处理后仍然存在的引用，这使得它们本质上不安全。为避免出现用户错误地将闭包包装在 `AssertUnwindSafe` 中只为满足编译器要求这种情况，我们添加了 `Closure::new_aborting` 变体，在无法保证 unwind 安全性的情况下，这些变体会在发生 panic 时终止程序，而不是进行 unwind 处理。

启用 panic unwind 时：

  * wasm-bindgen 会捕获已导出 Rust 函数中的 panic
  * panic 会作为 PanicError 异常抛给 JavaScript
  * 异步导出会拒绝其返回的 Promise，并抛出 PanicError
  * Rust 析构函数正常运行
  * WebAssembly 实例仍然有效且可重用



有关这种方法的详细信息以及在 wasm-bindgen 中的使用方式，请参阅 [_Wasm Bindgen：捕获 panic_](https://wasm-bindgen.github.io/wasm-bindgen/reference/catch-unwind.html) 最新指南页面。

## 中止恢复

即便启用 `panic=unwind` 支持，也仍然会出现中止，而内存溢出错误是常见原因之一。由于无法对中止进行 unwind 处理，因此完全无法恢复状态，但我们至少可以检测中止并从中恢复，以执行后续操作，避免无效状态导致后续请求出错。

Panic unwind 支持为中止恢复引入了新问题。当我们收到源自 Wasm 的错误时，我们无法确定它是源自 `extern “C-unwind”`的错误，还是真正的中止。WebAssembly 中的中止可能以多种形式出现。

有两种技术方案来解决这个问题：标记所有明确的中止错误，或者标记所有明确的 unwind 错误。两种方案都可行，但我们选择了后者。由于我们的外部异常处理已直接使用原始的 WAT 级 Exception Handling （WebAssembly 文本格式）指令，因此，我们发现可以更轻松地为外部异常添加异常标记，将它们与中止 non-unwind-safe 异常区分开来。

借助 WebAssembly Exception Handling 中的 `Exception.Tag` 特性，我们能够清楚地区分可恢复错误与不可恢复错误，然后集成新的中止处理程序以及中止重入防护。  
  
新的中止 hook `set_on_abort` 可用于在初始化时附加处理程序，该处理程序会根据平台嵌入的需求进行相应的恢复。

强化 panic 和中止处理是避免无效执行状态的关键。WebAssembly 支持调用栈深度交错，也就是说，Wasm 可以调用 JavaScript，JavaScript 可以重新进入 Wasm，无论嵌套调用有多深；除此之外，多个任务可以在同一个 WebAssembly 实例中运行。之前，某个任务或嵌套栈中发生的中止并不一定能通过 JS 导致更高层级的栈失效，从而引发未定义的行为。我们需要谨慎地确保执行模型的可靠性，并且这方面的工作仍在持续进行。

虽然中止并非理想情况，故障后重新初始化更是极端情况，但将关键错误恢复作为最后一道安全防线可确保执行正确无误，以及后续操作能够成功。无效状态不会持续存在，从而确保单个故障不会引发多个故障。

## 扩展：wasm-bindgen 库的中止后重新初始化

在开发过程中，我们意识到这是使用 wasm-bindgen 构建 JS 库的常见问题，以及添加一个中止处理程序进行恢复，也会让这些库从中受益。

但是，当以 ES 模块的形式构建 Wasm 并直接导入（例如，使用 `import { func } from ‘wasm-dep’`）时，如果用户 JS 应用中已链接并初始化的库在调用 `func()` 函数时发生 Wasm 中止，尚不清楚其恢复机制是什么。

虽然这并非严格意义上的 Rust Workers 用例，但我们团队也支持基于 JS 的 Workers 用户，此类用户运行 Rust 支持的 Wasm 库依赖项。如果我们能够同时解决这个问题，可能会间接推动 Cloudflare Workers 平台上的 Wasm 使用。

为了支持 Wasm 库用例的自动化中止恢复，我们在 wasm - bindgen 中添加了试验性重新初始化机制 `--reset-state-function` 支持。该机制提供一个函数，让 Rust 应用能够有效地请求将其内部 Wasm 实例重置回初始状态以备下一次调用，而无需生成的绑定的用户重新导入或重新创建实例。旧实例中的类实例会抛出异常，因为其句柄已变为孤立类，但此后可以构造新的类。使用 Wasm 库的 JS 应用会出现错误，但不是完全无响应。

有关此项功能的完整技术详情以及在 wasm-bindgen 中的使用方式，请参阅新的 wasm-bindgen 指南中的 [_Wasm Bindgen：处理中止_](https://wasm-bindgen.github.io/wasm-bindgen/reference/handling-aborts.html)部分。

## 完善 Rust Wasm Exception Handling 生态系统

对这项工作的上游贡献并不仅限于 wasm-bindgen 项目。使用 `panic=unwind` 进行 Wasm 构建仍然需要采用试验性 Nightly Rust 目标，因此，我们也一直在努力推进 Rust Wasm 对 WebAssembly Exception Handling 的支持，以便将其引入稳定的 Rust 版本。

在开发 WebAssembly Exception Handling 功能的过程中，后期规范变更导致了两种变体：[ _传统异常处理_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/legacy/Exceptions.md)以及最终的[ _现代异常处理（使用 exnref）_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md)。目前，Rust 的 WebAssembly 目标仍然会默认生成传统异常处理的代码。虽然传统异常处理仍然得到广泛支持，但它如今已被弃用。

以下 JS 平台版本开始支持现代 WebAssembly Exception Handling：

运行时| 版本| 发布日期  
---|---|---  
v8| 13.8.1| 2025 年 4 月 28 日  
workerd| v1.20250620.0| 2025 年 6 月 19 日  
Chrome| 138| 2025 年 6 月 28 日  
Firefox| 131| 2024 年 10 月 1 日  
Safari| 18.4| 2025 年 3 月 31 日  
Node.js| 25.0.0| 2025 年 10 月 15 日  
  
在调查支持矩阵的过程中，我们发现最大的问题是 Node.js 24 LTS 的发布计划，这将导致整个生态系统只能继续使用旧版 WebAssembly Exception Handling 直至 2028 年 4 月。

发现这一差异后，我们成功地将现代异常处理机制移植到 Node.js 24 版本，甚至还移植了必要的修复程序，使其能够在 Node.js 22 系列版本上运行，以确保支持这个目标。如此一来，现代异常处理提案应该在明年会成为默认目标。

在未来几个月，我们将努力让最终用户顺畅地过渡到稳定的 `panic=unwind` 支持和现代异常处理机制。

虽然对完善生态系统的这些长期投入需要时间才能见效，但它们有助于为整个 Rust WebAssembly 社区奠定更坚实的基础，Cloudflare 很高兴能够为这些改进贡献一份力量。

## 在 Rust Workers 中使用 panic unwind

从 Rust Workers 0.8.0 版本开始，我们新增了一个 `--panic-unwind` 标志，用户可以按照[ _此处的说明_](https://github.com/cloudflare/workers-rs?tab=readme-ov-file#panic-recovery-with---panic-unwind)将其添加到 build 命令中。

使用该标志，可以完全恢复 panic 错误，中止恢复机制将使用新的中止分类和恢复 hook 机制。我们强烈建议用户升级并试用新版本，获得更稳定的 Rust Workers 体验；另外，我们还计划在后续版本中将 `panic=unwind` 设置为默认值。继续使用 `panic=abort` 方法的用户，将继续受益于 0.6.0 版本中之前的自定义恢复封装器处理功能。

## 确保 Rust Workers 的稳定性

这项工作是我们持续努力的一部分，旨在推出稳定版 Rust Workers。Cloudflare 通过从根本上解决 Wasm 平台基础架构中的这些棘手问题，并在适当的时候回馈生态系统，我们不仅为自己的平台，也为整个 Rust、JS 和 Wasm 生态系统构建了更坚实的基础。

我们计划对 Rust Workers 进行一系列改进，并很快分享这项额外工作的最新进展，包括 wasm-bindgen 泛型和自动化 bindgen。上个月，我们团队的 Guy Bedford 在 [_Wasm.io 大会上关于 Rust 与 JS 互操作性_](https://www.youtube.com/watch?v=zlSJY8Qv5XI)的一场演讲中预告了这方面的信息。

请关注我们在 [_Cloudflare Discord_](https://discord.com/invite/cloudflaredev) 的 **#rust‑on‑workers** 频道。我们也欢迎用户提供反馈并展开讨论，尤其是所有新加入 [_workers-rs_](https://github.com/cloudflare/workers-rs) 和 [_wasm-bindgen_](https://github.com/wasm-bindgen/wasm-bindgen) GitHub 项目的贡献者。

本页内容

在线讨论

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-rust-workers-reliable%2F&t=%E6%8F%90%E9%AB%98%20Rust%20Workers%20%E5%8F%AF%E9%9D%A0%E6%80%A7%EF%BC%9Awasm-bindgen%20%E4%B8%AD%E7%9A%84%20panic%20%E9%94%99%E8%AF%AF%E4%B8%8E%E4%B8%AD%E6%AD%A2%E6%81%A2%E5%A4%8D%E6%9C%BA%E5%88%B6)[](https://x.com/intent/post?text=%E6%8F%90%E9%AB%98+Rust+Workers+%E5%8F%AF%E9%9D%A0%E6%80%A7%EF%BC%9Awasm-bindgen+%E4%B8%AD%E7%9A%84+panic+%E9%94%99%E8%AF%AF%E4%B8%8E%E4%B8%AD%E6%AD%A2%E6%81%A2%E5%A4%8D%E6%9C%BA%E5%88%B6&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-rust-workers-reliable%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-rust-workers-reliable%2F)[](https://bsky.app/intent/compose?text=%E6%8F%90%E9%AB%98+Rust+Workers+%E5%8F%AF%E9%9D%A0%E6%80%A7%EF%BC%9Awasm-bindgen+%E4%B8%AD%E7%9A%84+panic+%E9%94%99%E8%AF%AF%E4%B8%8E%E4%B8%AD%E6%AD%A2%E6%81%A2%E5%A4%8D%E6%9C%BA%E5%88%B6+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-rust-workers-reliable%2F)[](https://mastodonshare.com/?text=%E6%8F%90%E9%AB%98+Rust+Workers+%E5%8F%AF%E9%9D%A0%E6%80%A7%EF%BC%9Awasm-bindgen+%E4%B8%AD%E7%9A%84+panic+%E9%94%99%E8%AF%AF%E4%B8%8E%E4%B8%AD%E6%AD%A2%E6%81%A2%E5%A4%8D%E6%9C%BA%E5%88%B6&url=https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-rust-workers-reliable%2F)[](https://www.threads.net/intent/post?text=%E6%8F%90%E9%AB%98+Rust+Workers+%E5%8F%AF%E9%9D%A0%E6%80%A7%EF%BC%9Awasm-bindgen+%E4%B8%AD%E7%9A%84+panic+%E9%94%99%E8%AF%AF%E4%B8%8E%E4%B8%AD%E6%AD%A2%E6%81%A2%E5%A4%8D%E6%9C%BA%E5%88%B6+https%3A%2F%2Fblog.cloudflare.com%2Fzh-cn%2Fmaking-rust-workers-reliable%2F)

## 相关标签

[Cloudflare Workers](https://blog.cloudflare.com/zh-cn/tag/workers/)[Internship Experience](https://blog.cloudflare.com/zh-cn/tag/internship-experience/)[Rust](https://blog.cloudflare.com/zh-cn/tag/rust/)[Rust Workers](https://blog.cloudflare.com/zh-cn/tag/rust-workers/)[WASM](https://blog.cloudflare.com/zh-cn/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/zh-cn/tag/webassembly/)[可靠性](https://blog.cloudflare.com/zh-cn/tag/reliability/)[工程](https://blog.cloudflare.com/zh-cn/tag/engineering/)[开发人员](https://blog.cloudflare.com/zh-cn/tag/developers/)[开发人员平台](https://blog.cloudflare.com/zh-cn/tag/developer-platform/)[开源](https://blog.cloudflare.com/zh-cn/tag/open-source/)

关注社交媒体

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 订阅以接收新文章通知

电子邮件地址

我们绝不会分享您的电子邮件地址。

订阅

感谢订阅！请查看您的收件箱以确认。
