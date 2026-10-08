---
url: https://blog.cloudflare.com/zh-cn/tag/engineering/
title: \u6807\u7b7e\u4e3a\"\u5de5\u7a0b\"\u7684\u6587\u7ae0 \u2014 Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:11:17.778097+00:00
---

# 标签为"工程"的文章 — Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/tag/engineering/

标签

# 工程

[订阅 工程 RSS 源](https://blog.cloudflare.com/zh-cn/tag/engineering/rss)

2026年8月6日## [推出 Billable Usage API：Cloudflare 的程序化成本可见性](https://blog.cloudflare.com/zh-cn/billable-usage-api/)

Cloudflare 推出了全新的账户级 Billable Usage API，通过单一端点为开发者和 FinOps 团队提供程序化的成本与使用量可见性，覆盖所有自助服务产品。该 API 围绕 FOCUS 规范构建，使您能够将 Cloudflare 支出与云技术栈中其他服务的支出无缝整合，实现统一追踪。

![Ryan Noel](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KZ1X993V2NQBSHZCEDTSYH99.webp&w=64&h=64&f=webp&fit=cover&position=center)![Zunayed Ali](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KZ1X7VHNGDVK1WPDK7WS7DWR.webp&w=64&h=64&f=webp&fit=cover&position=center)![Filipa Nóbrega](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KZ1X62NSE3TRWSABF7J6JR84.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Ryan Noel](https://blog.cloudflare.com/zh-cn/author/ryan-noel/)、[Zunayed Ali](https://blog.cloudflare.com/zh-cn/author/zunayed-ali/)和[Filipa Nóbrega](https://blog.cloudflare.com/zh-cn/author/filipa-nobrega/)

2026年5月18日## [Project Glasswing：Mythos 为我们揭示的发现](https://blog.cloudflare.com/zh-cn/cyber-frontier-models/)

最近几周，我们将 Mythos 及其他专注于安全的 LLM 对我们基础设施中关键部分的实际运行代码进行扫描。我们将分享观测结果、模型的优势和局限，以及在规模化应用前需要进行的相关工作。

![Grant Bourzikas](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SJJRBDYVMHZKVGKTMJ08.png&w=64&h=64&f=webp&fit=cover&position=center)

[Grant Bourzikas](https://blog.cloudflare.com/zh-cn/author/grant/)

2026年5月14日## [我们的计费流程管道突然变慢了。问题的起因在于 ClickHouse 中隐藏的瓶颈](https://blog.cloudflare.com/zh-cn/clickhouse-query-plan-contention/)

当我们对 PB 级 ClickHouse 集群进行分区更改而导致重要的计费任务停滞时，标准指标未显示明显错误。本文概述了我们如何识别 ClickHouse 查询规划器中存在的严重锁争用问题，以及构建了哪些上游补丁来解决问题。

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/zh-cn/author/james-morrison/)和[Christian Endres](https://blog.cloudflare.com/zh-cn/author/christian-endres/)

2026年4月22日## [提高 Rust Workers 可靠性：wasm-bindgen 中的 panic 错误与中止恢复机制](https://blog.cloudflare.com/zh-cn/making-rust-workers-reliable/)

过去，Rust Workers 中的 panic 会产生致命影响，污染整个实例。通过 wasm-bindgen 项目方面的上游合作，Rust Workers 现在支持韧性关键错误恢复，包括使用 WebAssembly Exception Handling 进行 panic unwind 处理。

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/zh-cn/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/zh-cn/author/hood/)和[Logan Gatlin](https://blog.cloudflare.com/zh-cn/author/logan-gatlin/)

2026年2月27日## [互联网上最常见的用户界面是什么？重新设计 Turnstile 与质询页面](https://blog.cloudflare.com/zh-cn/the-most-seen-ui-on-the-internet-redesigning-turnstile-and-challenge-pages/)

我们每天处理 76 亿次质询。以下将介绍我们如何运用研究成果、AAA 级无障碍标准以及统一的信息架构，重新设计互联网上最常见的用户界面。

![Leo Bacevicius](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW493S0ZBT0BV1Y08GV76K24.png&w=64&h=64&f=webp&fit=cover&position=center)![Ana Foppa](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KTZRPFJSPXK2FK8H5CSH.png&w=64&h=64&f=webp&fit=cover&position=center)![Marina Elmore](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW477HVM8X1SKDG8ADKQJ9T3.png&w=64&h=64&f=webp&fit=cover&position=center)

[Leo Bacevicius](https://blog.cloudflare.com/zh-cn/author/leo-bacevicius/)、[Ana Foppa](https://blog.cloudflare.com/zh-cn/author/ana-foppa/)和[Marina Elmore](https://blog.cloudflare.com/zh-cn/author/marina-elmore/)

2025年9月26日## [Rust 助力 Cloudflare 变得更快、更安全](https://blog.cloudflare.com/zh-cn/20-percent-internet-upgrade/)

我们用基于 Rust 的新模块化代理替换了 Cloudflare 中原有的核心系统，从而取代了 NGINX。 

![Richard Boulton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WPC6H4PY51ETZPAGBKZ9.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Steve Goldsmith](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497YX7768BEJGS24P0FMX8.png&w=64&h=64&f=webp&fit=cover&position=center)![Maurizio Abba](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45R40JSMY4JX26YZV11150.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Matthew Bullock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ABWPJWE9RP8CPZF1G4F5.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Richard Boulton](https://blog.cloudflare.com/zh-cn/author/richard/)、[Steve Goldsmith](https://blog.cloudflare.com/zh-cn/author/steve-goldsmith/)、[Maurizio Abba](https://blog.cloudflare.com/zh-cn/author/maurizio-abba/)和[Matthew Bullock](https://blog.cloudflare.com/zh-cn/author/matthew-bullock/)

2025年9月26日## [消除冷启动问题 2：分片攻克法](https://blog.cloudflare.com/zh-cn/eliminating-cold-starts-2-shard-and-conquer/)

我们通过乐观地将请求路由到已加载 Workers 的服务器，将 Cloudflare Workers 的冷启动时间减少了 10 倍。在这里了解我们是如何做到的。

![Harris Hancock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H05HT7CQGVFMPCZBNF6H.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Harris Hancock](https://blog.cloudflare.com/zh-cn/author/harris-hancock/)

2025年9月25日## [沙箱安全：Cloudflare Workers 的安全加固](https://blog.cloudflare.com/zh-cn/safe-in-the-sandbox-security-hardening-for-cloudflare-workers/)

我们正通过运用最新的软件和硬件特性，持续强化 Cloudflare Workers。我们使用纵深防御措施，包括 V8 沙箱和 CPU 的内存保护密钥，确保您的数据安全。

![Erik Corry](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AASRAFXFDH6FXBW7Q2FY&w=64&h=64&fit=cover&position=center)![Ketan Gupta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46M1KQ1E9BDY0G700HZFHF.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Erik Corry](https://blog.cloudflare.com/zh-cn/author/erik-corry/)和[Ketan Gupta](https://blog.cloudflare.com/zh-cn/author/ketan-gupta/)

2025年7月23日## [构建 Jetflow：Cloudflare 实现灵活、高性能数据管道的框架](https://blog.cloudflare.com/zh-cn/building-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare/)

面对大规模数据摄取的挑战，Cloudflare 的商业智能团队构建了一个名为 Jetflow 的新框架。

![Harry Hough](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47C0JMBM7Y7F2GNX2R8X3Q.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Rebecca Walton-Jones](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47P62GPSPWQJMX49XBJ9PK.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andy Fan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WD6HZHWZDZ6D51EB2YHJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Ricardo Margalhau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4692VQ40ERSW2HS1VWGJ06.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Uday Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45ZJ46DGX82MAJPNK0SWE0.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Harry Hough](https://blog.cloudflare.com/zh-cn/author/harry-hough/)、[Rebecca Walton-Jones](https://blog.cloudflare.com/zh-cn/author/rebecca-walton-jones/)、[Andy Fan](https://blog.cloudflare.com/zh-cn/author/andy-fan/)、[Ricardo Margalhau](https://blog.cloudflare.com/zh-cn/author/ricardo-margalhau/)和[Uday Sharma](https://blog.cloudflare.com/zh-cn/author/uday-sharma/)
