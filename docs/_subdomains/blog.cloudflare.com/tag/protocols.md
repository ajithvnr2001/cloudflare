---
url: https://blog.cloudflare.com/tag/protocols/
title: Posts tagged \"Protocols\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:24:59.083961+00:00
---

# Posts tagged "Protocols" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/protocols/

TAG

# Protocols

[Subscribe to Protocols RSS feed](https://blog.cloudflare.com/tag/protocols/rss)

October 2, 2026## [Announcing Cloudflare OHTTP Gateway – expanding access to Cloudflare’s privacy-preserving infrastructure](https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/)

We’re announcing the closed beta of a self-serve Cloudflare OHTTP Gateway. We’re also renaming our Privacy Gateway to Cloudflare OHTTP Relay to better distinguish the two products.

![Lara Schull](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M34Y34B7NA1EXDT3NB44Q1E9.01M34Y34V1QSE5BJE43H5NGG6K.webp&w=64&h=64&f=webp&fit=cover&position=center)![Akshat Mahajan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VR0DYS4EZ818QTQC7Z5F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lara Schull](https://blog.cloudflare.com/author/lara-schull/) and [Akshat Mahajan](https://blog.cloudflare.com/author/akshat-mahajan/)

November 6, 2025## [Async QUIC and HTTP/3 made easy: tokio-quiche is now open-source](https://blog.cloudflare.com/async-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source/)

We’re excited to announce the open sourcing of tokio-quiche, our async QUIC library built on quiche and tokio. Relied upon in our services such as iCloud Private Relay and our next-generation Oxy-based proxies, tokio-quiche handles millions of HTTP/3 requests per second with low latency and high throughput. 

![Pedro Mendes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44728NW455QD7JX15VF2WS.webp&w=64&h=64&f=webp&fit=cover&position=center)![Leo Blöcher](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49579CYY7HBQE8A4NZZ9B2.webp&w=64&h=64&f=webp&fit=cover&position=center)![Evan Rittenhouse](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47GS3RW10ESS21SA5P60SX.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Fisher Darling](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463PVCFZWEEPCE2T84TW2R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Pedro Mendes](https://blog.cloudflare.com/author/mendes/), [Leo Blöcher](https://blog.cloudflare.com/author/leo-bloecher/), [Evan Rittenhouse](https://blog.cloudflare.com/author/evan-rittenhouse/), and [Fisher Darling](https://blog.cloudflare.com/author/fisher/)

October 29, 2025## [Defending QUIC from acknowledgement-based DDoS attacks](https://blog.cloudflare.com/defending-quic-from-acknowledgement-based-ddos-attacks/)

We identified and patched two DDoS vulnerabilities in our QUIC implementation related to packet acknowledgements. Cloudflare customers were not affected. We examine the "Optimistic ACK" attack vector and our solution, which dynamically skips packet numbers to validate client behavior. 

![Apoorv Kothari](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SGJG5SXE4YMV1EXQHRZM.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Louis Navarre](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW451TFKH3TJ9D40EQ8R9B9F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Apoorv Kothari](https://blog.cloudflare.com/author/apoorv-kothari/) and [Louis Navarre](https://blog.cloudflare.com/author/louis-navarre/)

December 30, 2024## [Open sourcing h3i: a command line tool and library for low-level HTTP/3 testing and debugging](https://blog.cloudflare.com/h3i/)

h3i is a command line tool and Rust library designed for low-level testing and debugging of HTTP/3, which runs over QUIC.

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Evan Rittenhouse](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47GS3RW10ESS21SA5P60SX.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/author/lucas/) and [Evan Rittenhouse](https://blog.cloudflare.com/author/evan-rittenhouse/)

February 8, 2024## [connect() - why are you so slow?](https://blog.cloudflare.com/linux-transport-protocol-port-selection-performance/)

This is our story of what we learned about the connect() implementation for TCP in Linux. Both its strong and weak points. How connect() latency changes under pressure, and how to open connection so that the syscall latency is deterministic and time-bound

![Frederick Lawler](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YV7KWFD5VEJ5KEDXS2R1.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Frederick Lawler](https://blog.cloudflare.com/author/frederick/)

March 28, 2023## [Cloudflare’s commitment to the 2023 Summit for Democracy](https://blog.cloudflare.com/cloudflare-commitment-to-the-2023-summit-for-democracy/)

Cloudflare is proud to participate in and contribute commitments to the 2023 Summit Summit for Democracy because we believe that everyone should have access to an Internet that is faster,

![Zaid Zaid](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463DA0PAXJPDTJNGC8FTG1.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Patrick Day](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48TYR5VCZ5TE2F5PZ2Z1X5.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Zaid Zaid](https://blog.cloudflare.com/author/zaid-zaid/) and [Patrick Day](https://blog.cloudflare.com/author/patrick-day/)

October 27, 2022## [Privacy Gateway: a privacy preserving proxy built on Internet standards](https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/)

Privacy Gateway enables privacy-forward applications to use Cloudflare as a trusted Relay, limiting which identifying information, including IP addresses, is visible to their infrastructure

![Mari Galicer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW481GPW34N2TYBX476WQC8S.png&w=64&h=64&f=webp&fit=cover&position=center)![Christopher Wood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495W9WYS29QA8B6X8KQHCZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Mari Galicer](https://blog.cloudflare.com/author/mari/) and [Christopher Wood](https://blog.cloudflare.com/author/christopher/)

October 13, 2021## [Cloudflare and the IETF](https://blog.cloudflare.com/cloudflare-and-the-ietf/)

Cloudflare helps build a better Internet through collaboration on open and interoperable standards. This post will describe how Cloudflare contributes to the standardization process to enable incremental innovation and drive long-term architectural change.

![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Christopher Wood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495W9WYS29QA8B6X8KQHCZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Jonathan Hoyland](https://blog.cloudflare.com/author/jonathan-hoyland/) and [Christopher Wood](https://blog.cloudflare.com/author/christopher/)

October 13, 2021## [Exported Authenticators: The long road to RFC](https://blog.cloudflare.com/exported-authenticators-the-long-road-to-rfc/)

Learn more about Exported Authenticators, a new extension to TLS, currently going through the IETF standardisation process.

![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Jonathan Hoyland](https://blog.cloudflare.com/author/jonathan-hoyland/)

October 12, 2021## [Handshake Encryption: Endgame (an ECH update)](https://blog.cloudflare.com/handshake-encryption-endgame-an-ech-update/)

In this post, we’ll dig into ECH details and describe what this protocol does to move the needle to help build a better Internet.

![Christopher Wood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495W9WYS29QA8B6X8KQHCZ.png&w=64&h=64&f=webp&fit=cover&position=center)![Christopher Patton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471WT491ZC11M0S5HA34X3.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Christopher Wood](https://blog.cloudflare.com/author/christopher/) and [Christopher Patton](https://blog.cloudflare.com/author/christopher-patton/)

December 8, 2020## [Good-bye ESNI, hello ECH!](https://blog.cloudflare.com/encrypted-client-hello/)

A deep dive into the Encrypted Client Hello, a standard that encrypts privacy-sensitive parameters sent by the client, as part of the TLS handshake.

![Christopher Patton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471WT491ZC11M0S5HA34X3.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Christopher Patton](https://blog.cloudflare.com/author/christopher-patton/)

December 8, 2020## [OPAQUE: The Best Passwords Never Leave your Device](https://blog.cloudflare.com/opaque-oblivious-passwords/)

Imagine passwords for online services that never leave your device, encrypted or otherwise. OPAQUE is a new cryptographic protocol that makes this idea possible, giving you and only you full control of your password.

![Tatiana Bradley](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW452V619V5ZY5T4NTYG4MPN.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tatiana Bradley](https://blog.cloudflare.com/author/tatiana/)
