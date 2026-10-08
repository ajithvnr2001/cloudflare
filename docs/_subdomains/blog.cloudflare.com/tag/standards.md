---
url: https://blog.cloudflare.com/tag/standards/
title: Posts tagged \"Standards\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:24:58.772667+00:00
---

# Posts tagged "Standards" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/standards/

TAG

# Standards

[Subscribe to Standards RSS feed](https://blog.cloudflare.com/tag/standards/rss)

October 2, 2026## [Announcing Cloudflare OHTTP Gateway – expanding access to Cloudflare’s privacy-preserving infrastructure](https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/)

We’re announcing the closed beta of a self-serve Cloudflare OHTTP Gateway. We’re also renaming our Privacy Gateway to Cloudflare OHTTP Relay to better distinguish the two products.

![Lara Schull](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M34Y34B7NA1EXDT3NB44Q1E9.01M34Y34V1QSE5BJE43H5NGG6K.webp&w=64&h=64&f=webp&fit=cover&position=center)![Akshat Mahajan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VR0DYS4EZ818QTQC7Z5F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lara Schull](https://blog.cloudflare.com/author/lara-schull/) and [Akshat Mahajan](https://blog.cloudflare.com/author/akshat-mahajan/)

September 29, 2026## [Preventing quantum downgrade attacks against IPsec](https://blog.cloudflare.com/ipsec-downgrade-protection/)

A sophisticated attacker with a quantum computer can exploit a protocol design flaw to downgrade post-quantum IPsec tunnels to classical crypto. We helped the IETF develop a transcript authentication extension to prevent these attacks.

![Christopher Patton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471WT491ZC11M0S5HA34X3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Amos Paul](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47FD25GV5MTTPN5NXN79ES.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Lina Baquero](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KXDHSP0NJR8EJ5X72TPSFA2R.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Christopher Patton](https://blog.cloudflare.com/author/christopher-patton/), [Amos Paul](https://blog.cloudflare.com/author/amos-paul/), and [Lina Baquero](https://blog.cloudflare.com/author/lina-baquero/)

July 14, 2026## [A broken DNSSEC rollover took down .al. Now 1.1.1.1 tells you when validation is bypassed](https://blog.cloudflare.com/dnssec-nta-ede-33/)

When a failed DNSSEC key rollover took down the .al TLD, we deployed a Negative Trust Anchor to restore resolution. This time, though, clients didn't have to take our word for it: 1.1.1.1 returned EDE 33, a new DNS error code that signals directly in the response that DNSSEC validation was bypassed.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

April 21, 2026## [Moving past bots vs. humans](https://blog.cloudflare.com/past-bots-and-humans/)

As AI assistants and privacy proxies challenge the capabilities of traditional bot detection, the Web needs new models for accountability. We believe that control should remain with the client, and that an open ecosystem of anonymous credentials is key to preserving user privacy while protecting origins from abuse.

![Thibault Meunier](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CG4C7M8Y2P7VRAYHW2RV.png&w=64&h=64&f=webp&fit=cover&position=center)

[Thibault Meunier](https://blog.cloudflare.com/author/thibault/)

February 27, 2026## [We deserve a better streams API for JavaScript](https://blog.cloudflare.com/a-better-web-streams-api/)

The Web streams API has become ubiquitous in JavaScript runtimes but was designed for a different era. Here's what a modern streaming API could (should?) look like.

![James M Snell](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47K5PBRD0MV43BH5TR121F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[James M Snell](https://blog.cloudflare.com/author/jasnell/)

January 14, 2026## [What came first: the CNAME or the A record?](https://blog.cloudflare.com/cname-a-record-order-dns-standards/)

A recent change to 1.1.1.1 accidentally altered the order of CNAME records in DNS responses, breaking resolution for some clients. This post explores the technical root cause, examines the source code of affected resolvers, and dives into the inherent ambiguities of the DNS RFCs.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

August 22, 2025## [MoQ: Refactoring the Internet's real-time media stack](https://blog.cloudflare.com/moq/)

Media over QUIC (MoQ) is a new IETF standard that resolves this conflict, creating a single foundation for sub-second, interactive streaming at a global scale. 

![Mike English](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456AKXY6NZWXBX72F7RG6T.png&w=64&h=64&f=webp&fit=cover&position=center)![Renan Dincer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW449Z67TCFN30VHF8AAYGZS.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Mike English](https://blog.cloudflare.com/author/mike-english/) and [Renan Dincer](https://blog.cloudflare.com/author/renan/)

March 24, 2025## [New URLPattern API brings improved pattern matching to Node.js and Cloudflare Workers](https://blog.cloudflare.com/improving-web-standards-urlpattern/)

Today we're announcing our latest contribution to Node.js, now available in v23.8.0: URLPattern. 

![Yagiz Nizipli](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49902QMPTX5QJQNJN0SVZ9.jpg&w=64&h=64&f=webp&fit=cover&position=center)![James M Snell](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47K5PBRD0MV43BH5TR121F.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Daniel Lemire](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48X5DN2VNBW1HS6SJCXYTC.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Yagiz Nizipli](https://blog.cloudflare.com/author/yagiz-nizipli/), [James M Snell](https://blog.cloudflare.com/author/jasnell/), and [Daniel Lemire](https://blog.cloudflare.com/author/daniel-lemire/)

October 6, 2024## [Enhance your website's security with Cloudflare’s free security.txt generator](https://blog.cloudflare.com/security-txt/)

Cloudflare’s free security.txt generator lets users create and manage security.txt files. Enhance vulnerability disclosure, align with industry standards, and integrate into the dashboard.

![Alexandra Moraru](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49B8GD6QKS5GZ8V5QVR4GP.png&w=64&h=64&f=webp&fit=cover&position=center)![Sam Khawasé](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW448QFVB1T546KP043SG7BY.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alexandra Moraru](https://blog.cloudflare.com/author/alexandra/) and [Sam Khawasé](https://blog.cloudflare.com/author/sam-khawase/)

September 27, 2023## [You can now use WebGPU in Cloudflare Workers](https://blog.cloudflare.com/webgpu-in-workers/)

Today, we are introducing WebGPU support to Cloudflare Workers. This blog will explain why it's important, why we did it, how you can use it, and what comes next

![André Cruz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FAFHK5DDQ0GQPPQ92C3B.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Celso Martinho](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K1GG0634XMEFX9CSSGM2.png&w=64&h=64&f=webp&fit=cover&position=center)

[André Cruz](https://blog.cloudflare.com/author/andre-cruz/) and [Celso Martinho](https://blog.cloudflare.com/author/celso/)

October 27, 2022## [Privacy Gateway: a privacy preserving proxy built on Internet standards](https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/)

Privacy Gateway enables privacy-forward applications to use Cloudflare as a trusted Relay, limiting which identifying information, including IP addresses, is visible to their infrastructure

![Mari Galicer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW481GPW34N2TYBX476WQC8S.png&w=64&h=64&f=webp&fit=cover&position=center)![Christopher Wood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495W9WYS29QA8B6X8KQHCZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Mari Galicer](https://blog.cloudflare.com/author/mari/) and [Christopher Wood](https://blog.cloudflare.com/author/christopher/)

February 24, 2022## [HPKE: Standardizing public-key encryption (finally!)](https://blog.cloudflare.com/hybrid-public-key-encryption/)

HPKE (RFC 9180) was made to be simple, reusable, and future-proof by building upon knowledge from prior PKE schemes and software implementations. This article provides an overview of this new standard, going back to discuss its motivation, design goals, and development process

![Christopher Wood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495W9WYS29QA8B6X8KQHCZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Christopher Wood](https://blog.cloudflare.com/author/christopher/)

October 13, 2021## [Cloudflare and the IETF](https://blog.cloudflare.com/cloudflare-and-the-ietf/)

Cloudflare helps build a better Internet through collaboration on open and interoperable standards. This post will describe how Cloudflare contributes to the standardization process to enable incremental innovation and drive long-term architectural change.

![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Christopher Wood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495W9WYS29QA8B6X8KQHCZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Jonathan Hoyland](https://blog.cloudflare.com/author/jonathan-hoyland/) and [Christopher Wood](https://blog.cloudflare.com/author/christopher/)
