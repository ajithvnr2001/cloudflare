---
url: https://blog.cloudflare.com/zh-cn/tag/reliability/
title: \u6807\u7b7e\u4e3a\"\u53ef\u9760\u6027\"\u7684\u6587\u7ae0 \u2014 Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:11:32.581256+00:00
---

# 标签为"可靠性"的文章 — Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/tag/reliability/

标签

# 可靠性

[订阅 可靠性 RSS 源](https://blog.cloudflare.com/zh-cn/tag/reliability/rss)

2026年4月22日## [提高 Rust Workers 可靠性：wasm-bindgen 中的 panic 错误与中止恢复机制](https://blog.cloudflare.com/zh-cn/making-rust-workers-reliable/)

过去，Rust Workers 中的 panic 会产生致命影响，污染整个实例。通过 wasm-bindgen 项目方面的上游合作，Rust Workers 现在支持韧性关键错误恢复，包括使用 WebAssembly Exception Handling 进行 panic unwind 处理。

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/zh-cn/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/zh-cn/author/hood/)和[Logan Gatlin](https://blog.cloudflare.com/zh-cn/author/logan-gatlin/)

2025年12月22日## [Workers 如何为我们的内部维护调度流程提供支持](https://blog.cloudflare.com/zh-cn/building-our-maintenance-scheduler-on-workers/)

在全球网络上，物理数据中心的维护工作充满风险。为此，我们在 Workers 上构建了一个维护调度器，用以安全地规划具有破坏性的操作；同时，通过在多个数据源与指标管道之上引入图接口来洞察基础设施的整体状态，从而解决了扩展过程中遇到的种种挑战。

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/zh-cn/author/kevin-deems/)和[Michael Hoffmann](https://blog.cloudflare.com/zh-cn/author/michael-hoffmann/)

2024年3月4日## [利用 CISA 的 Secure by Design 原则进行行业变革](https://blog.cloudflare.com/zh-cn/secure-by-design-principles/)

安全考量应当是软件设计过程中不可分割的一部分，而不应当是事后的想法。了解 Cloudflare 如何遵守 CISA 的 Secure by Design 原则以推进行业变革

![Kristina Galicova](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SE6FVY39NNKJ8GYZXBZN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Edo Royker](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NPG0HKPB45GKW757SAW2.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kristina Galicova](https://blog.cloudflare.com/zh-cn/author/kristina-galicova/)和[Edo Royker](https://blog.cloudflare.com/zh-cn/author/edo-royker/)

2018年9月24日## [不加密，无隐私：加密SNI工作原理](https://blog.cloudflare.com/zh-cn/encrypted-sni/)

今天，我们发布了加密SNI支持，这是TLS 1.3协议的扩展，它通过防止路径上的观察者（包括互联网服务提供商，咖啡店所有者和防火墙）拦截TLS服务器名称指示（SNI）扩展，并使用它来确定用户正在访问哪些网站，从而提高互联网用户的隐私。

![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alessandro Ghedini](https://blog.cloudflare.com/zh-cn/author/alessandro-ghedini/)

2018年9月24日## [加密SNI：修复其中一个核心Internet漏洞](https://blog.cloudflare.com/zh-cn/esni/)

Cloudflare于2010年9月27日推出。从那时起，我们就把9月27日定为我们的生日。这个星期四是我们的8岁生日。 从我们的第一个生日开始，我们就利用这个机会推出新产品或服务。多年来，我们得出的结论是，庆祝我们生日的正确方式，与其推出我们可以从中赚钱的产品，不如做一些回馈用户和整个互联网的礼物。我的联合创始人米歇尔昨天在一篇很棒的博客文章中提到了这一传统。

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/zh-cn/author/matthew-prince/)

2018年7月6日## [如何每秒丢弃1000万个数据包](https://blog.cloudflare.com/zh-cn/how-to-drop-10-million-packets/)

在公司内部，我们的DDoS缓解团队有时被称为“丢包者”。其他团队在构建令人兴奋的产品来处理通过我们网络的流量，而我们却乐于发现丢弃这些流量的新方法。

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/zh-cn/author/marek-majkowski/)

2018年2月27日## [Memcrashed - 来自UDP端口11211的主要放大攻击](https://blog.cloudflare.com/zh-cn/memcrashed-major-amplification-attacks-from-port-11211/)

在过去的几天里，我们观察到隐蔽的放大攻击向量的频次大幅增加，这些放大攻击使用了来自UDP端口11211 的memcached协议。之前我们已经谈论过很多关于互联网上放大攻击的话题。我们最近关于这个主题的两篇博文是：

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/zh-cn/author/marek-majkowski/)

2017年9月25日## [不计量缓解：无限的 DDoS 防护](https://blog.cloudflare.com/zh-cn/unmetered-mitigation/)

本周是 Cloudflare 的七周年生日周。按照惯例，我们会在本周的每一天宣布推出一系列产品并为客户带来重大的新权益。我们先来介绍我特别自豪的一款产品：Unmetered Mitigation

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/zh-cn/author/matthew-prince/)
