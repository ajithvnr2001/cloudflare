---
url: https://blog.cloudflare.com/zh-cn/tag/tls/
title: \u6807\u7b7e\u4e3a\"TLS\"\u7684\u6587\u7ae0 \u2014 Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:10:57.714309+00:00
---

# 标签为"TLS"的文章 — Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/tag/tls/

标签

# TLS

[订阅 TLS RSS 源](https://blog.cloudflare.com/zh-cn/tag/tls/rss)

2026年10月8日## [利用 Merkle Tree Certificates 构建后量子证书颁发机构](https://blog.cloudflare.com/zh-cn/pq-ca-with-mtcs/)

随着后量子签名可能导致 TLS 握手和证书透明度日志急剧膨胀，Merkle Tree Certificates 提供了一条通往紧凑、可审计身份验证的路径。Cloudflare 的新证书颁发机构将支持大规模 MTC 颁发。

![Mari Galicer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW481GPW34N2TYBX476WQC8S.png&w=64&h=64&f=webp&fit=cover&position=center)

[Mari Galicer](https://blog.cloudflare.com/zh-cn/author/mari/)

2026年10月8日## [为整个互联网构建证书颁发机构](https://blog.cloudflare.com/zh-cn/cloudflare-certificate-authority/)

在推出 Universal SSL 十二年后，Cloudflare 正式申请成为证书颁发机构。通过将成熟的根证书、ACME 优先方法与 Merkle Tree Certificates 相结合，我们正在为开放网络构建一个后量子 CA。

![Steve Goldsmith](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497YX7768BEJGS24P0FMX8.png&w=64&h=64&f=webp&fit=cover&position=center)

[Steve Goldsmith](https://blog.cloudflare.com/zh-cn/author/steve-goldsmith/)

2025年9月26日## [消除冷启动问题 2：分片攻克法](https://blog.cloudflare.com/zh-cn/eliminating-cold-starts-2-shard-and-conquer/)

我们通过乐观地将请求路由到已加载 Workers 的服务器，将 Cloudflare Workers 的冷启动时间减少了 10 倍。在这里了解我们是如何做到的。

![Harris Hancock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H05HT7CQGVFMPCZBNF6H.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Harris Hancock](https://blog.cloudflare.com/zh-cn/author/harris-hancock/)

2025年9月24日## [自动保护：我们如何为 600 万个域名默认升级安全防护，备战量子计算时代](https://blog.cloudflare.com/zh-cn/automatically-secure/)

在我们开始启用 Automatic SSL/TLS 一年后，我们想谈谈这些结果、它们为何重要，以及我们如何为互联网安全的下一次飞跃做好准备。

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Yawar Jamal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1PVVBNHNQWX6D1BK30VQW4X.01M1PVVCG30FCBAY7PS1R17190.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/zh-cn/author/alex/)、[Suleman Ahmad](https://blog.cloudflare.com/zh-cn/author/suleman/)和[Yawar Jamal](https://blog.cloudflare.com/zh-cn/author/yawar/)

2025年2月7日## [解决 mutual TLS 会话恢复漏洞](https://blog.cloudflare.com/zh-cn/resolving-a-mutual-tls-session-resumption-vulnerability/)

Cloudflare 修补了通过其漏洞悬赏计划报告的一个 mutual TLS (mTLS) 漏洞 (CVE-2025-23419)。会话恢复中的缺陷导致客户端证书无法跨不同区域正确地进行身份验证

![Matt Bullock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW466BA2DF5DM17JT5M31SWH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Rushil Mehra](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3J65XQ6KWWMTYQHZMX9VC2Q.01M3J65YDX7BCSBDQXBR3P2B20.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Bullock](https://blog.cloudflare.com/zh-cn/author/matt-bullock/)、[Rushil Mehra](https://blog.cloudflare.com/zh-cn/author/rushil-mehra/)和[Alessandro Ghedini](https://blog.cloudflare.com/zh-cn/author/alessandro-ghedini/)

2023年9月4日## [使用 ORIGIN Frames 实现连接合并：减少 DNS 查询，减少连接数](https://blog.cloudflare.com/zh-cn/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)

在本博客中，我们将对“连接合并”进行更深入的探讨，并特别关注大规模的管理问题

![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Suleman Ahmad](https://blog.cloudflare.com/zh-cn/author/suleman/)、[Jonathan Hoyland](https://blog.cloudflare.com/zh-cn/author/jonathan-hoyland/)和[Sudheesh Singanamalla](https://blog.cloudflare.com/zh-cn/author/sudheesh/)

2022年12月15日## [可配置、可扩展的新版 Geo Key Manager 现已进入封闭测试阶段](https://blog.cloudflare.com/zh-cn/configurable-and-scalable-geo-key-manager-closed-beta/)

隆重宣布，Geo Key Manager 新版本现已进入封闭测试阶段，该版本允许客户按国家、按地区或按标准（例如，“仅在符合 FIPS 标准的数据中心中存储我的私钥”）定义边界

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/zh-cn/author/dina/)

2022年10月6日## [Total TLS：一键为自己的所有主机名部署 TLS](https://blog.cloudflare.com/zh-cn/total-tls-one-click-tls-for-every-hostname/)

我们今天隆重推出 Total TLS，可一键为客户域的每一个子域颁发单独的 TLS 证书

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/zh-cn/author/dina/)

2022年3月14日## [隆重推出：备份证书](https://blog.cloudflare.com/zh-cn/introducing-backup-certificates/)

Cloudflare 使每一位客户都能为自己的互联网应用程序配置 TLS 证书，而且费用全免，对此我们引以为豪。今天，我们负责管理近 4500 万份证书从颁发到部署到更新的整个生命周期

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/zh-cn/author/dina/)

2021年10月22日## [Cloudflare for SaaS for All，现已全面上市！](https://blog.cloudflare.com/zh-cn/cloudflare-for-saas-for-all-now-generally-available/)

在几个月前的开发者周期间，我们推出了 Cloudflare for SaaS 的测试版： 为 SaaS 提供商提供一站式服务，希望为其客户提供快速的加载时间、无与伦比的冗余和强大的安全性

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/zh-cn/author/dina/)

2019年6月18日## [使用多域控制器验证确保证书颁发安全](https://blog.cloudflare.com/zh-cn/secure-certificate-issuance/)

公众对互联网的信任是以公钥基础设施（PKI）为基础的。PKI通过签发数字证书，授予服务器安全服务网站的能力，为加密和真实的通信提供了基础。

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Gabbi Fisher](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AWARSGXCZQZ5Y1WSQE8K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/zh-cn/author/dina/)和[Gabbi Fisher](https://blog.cloudflare.com/zh-cn/author/gabbi/)

2018年9月24日## [不加密，无隐私：加密SNI工作原理](https://blog.cloudflare.com/zh-cn/encrypted-sni/)

今天，我们发布了加密SNI支持，这是TLS 1.3协议的扩展，它通过防止路径上的观察者（包括互联网服务提供商，咖啡店所有者和防火墙）拦截TLS服务器名称指示（SNI）扩展，并使用它来确定用户正在访问哪些网站，从而提高互联网用户的隐私。

![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alessandro Ghedini](https://blog.cloudflare.com/zh-cn/author/alessandro-ghedini/)

2018年4月24日## [BGP泄漏与加密货币](https://blog.cloudflare.com/zh-cn/bgp-leaks-and-crypto-currencies/)

在过去的几个小时里，已经有十几个新闻报道揭露了有攻击者企图（也许已经完成了）使用BGP泄漏来窃取加密货币。

![Louis Poinsignon](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45XKBQHBMEVSAS1MAW42NT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Louis Poinsignon](https://blog.cloudflare.com/zh-cn/author/louis-poinsignon/)
