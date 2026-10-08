---
url: https://blog.cloudflare.com/tag/deep-dive/
title: Posts tagged \"Deep Dive\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:46.220451+00:00
---

# Posts tagged "Deep Dive" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/deep-dive/

TAG

# Deep Dive

[Subscribe to Deep Dive RSS feed](https://blog.cloudflare.com/tag/deep-dive/rss)

September 29, 2026## [We tested our own WAF with frontier AI models. Here’s what we found](https://blog.cloudflare.com/adaptive-ai-waf-testing/)

We built a WAF tester that adapted each request based on what the WAF blocked or passed. This helped us explore variations that a fixed test might miss. We ran it across six attack categories on an authorized staging environment and discovered detection gaps worth fixing. Here’s how the loop worked, what got through, and what we did about it. 

![Vikram Grover](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KXRZQ9V87C8WK94DX4J9EPSD.webp&w=64&h=64&f=webp&fit=cover&position=center)![Daniele Molteni](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464793D50Z8QJQK451PK2A.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Kuber Nandwani](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KXRZS93GCE4CXP81WJ1TX25Y.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Vikram Grover](https://blog.cloudflare.com/author/vikram-grover/), [Daniele Molteni](https://blog.cloudflare.com/author/daniele/), and [Kuber Nandwani](https://blog.cloudflare.com/author/kuber-nandwani/)

September 18, 2026## [Saving another 100TB of RAM with math (and Rust)](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)

Cloudflare's global network is immense but not limitless. As we look for small ways to trim our resource usage, we sometimes get lucky and we can cut significantly more. Here’s how we reduced one of our Pingora-based service's RAM usage with statistics.

![Kevin Guthrie](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VQ8K1T55ANDEX70V1EEQ.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Mariia Iurchenko](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M2PGX99HXQ1AJD4D0GYQ6PZ7.01M2PGXACVX3VE6FGB02AYFXX5.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Zaidoon Abd Al Hadi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VAC8T0NPDPFZ06GAZW3H.png&w=64&h=64&f=webp&fit=cover&position=center)![Ivan Babrou](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW459B6P3WP5JXFP7X1NGXQY.png&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Guthrie](https://blog.cloudflare.com/author/kevin-guthrie/), [Mariia Iurchenko](https://blog.cloudflare.com/author/mariia-iurchenko/), [Zaidoon Abd Al Hadi](https://blog.cloudflare.com/author/zaidoon/), and [Ivan Babrou](https://blog.cloudflare.com/author/ivan/)

August 27, 2026## [How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/)

Five Rust-level memory optimizations to the DNS cache layout of Big Pineapple cut per-entry memory by 56%, freeing approximately 100 TB of memory across Cloudflare's fleet.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

October 21, 2025## [A deep dive into BPF LPM trie performance and optimization](https://blog.cloudflare.com/a-deep-dive-into-bpf-lpm-trie-performance-and-optimization/)

This post explores the performance of BPF LPM tries, a critical data structure used for IP matching. 

![Matt Fleming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469GS9NZP4VYY003HA8XEA.webp&w=64&h=64&f=webp&fit=cover&position=center)![Jesper Brouer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW499RS2WW80VBYFGEW0TADD.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Fleming](https://blog.cloudflare.com/author/matt-fleming/) and [Jesper Brouer](https://blog.cloudflare.com/author/jesper-brouer/)

October 16, 2025## [Improving the trustworthiness of Javascript on the Web](https://blog.cloudflare.com/improving-the-trustworthiness-of-javascript-on-the-web/)

There's no way to audit a site’s client-side code as it changes, making it hard to trust sites that use cryptography. We preview a specification we co-authored that adds auditability to the web.

![Michael Rosenberg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47X0RA8J05R35F2H1JAJ8R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michael Rosenberg](https://blog.cloudflare.com/author/michael-rosenberg/)

October 8, 2025## [How we found a bug in Go's arm64 compiler](https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/)

84 million requests a second means even rare bugs appear often. We'll reveal how we discovered a race condition in the Go arm64 compiler and got it fixed.

![Thea Heinen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CYSDFZQ7AE7FQYJ5JVNT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Thea Heinen](https://blog.cloudflare.com/author/thea-heinen/)

September 26, 2025## [Cloudflare just got faster and more secure, powered by Rust](https://blog.cloudflare.com/20-percent-internet-upgrade/)

We’ve replaced the original core system in Cloudflare with a new modular Rust-based proxy, replacing NGINX. 

![Richard Boulton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WPC6H4PY51ETZPAGBKZ9.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Steve Goldsmith](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497YX7768BEJGS24P0FMX8.png&w=64&h=64&f=webp&fit=cover&position=center)![Maurizio Abba](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45R40JSMY4JX26YZV11150.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Matthew Bullock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ABWPJWE9RP8CPZF1G4F5.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Richard Boulton](https://blog.cloudflare.com/author/richard/), [Steve Goldsmith](https://blog.cloudflare.com/author/steve-goldsmith/), [Maurizio Abba](https://blog.cloudflare.com/author/maurizio-abba/), and [Matthew Bullock](https://blog.cloudflare.com/author/matthew-bullock/)

September 25, 2025## [R2 SQL: a deep dive into our new distributed query engine](https://blog.cloudflare.com/r2-sql-deep-dive/)

R2 SQL provides a built-in, serverless way to run ad-hoc analytic queries against your R2 Data Catalog. This post dives deep under the Iceberg into how we built this distributed engine.

![Yevgen Safronov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW467KVZ9QVG0BC5FVHJWW7W.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)

[Yevgen Safronov](https://blog.cloudflare.com/author/yevgen/), [Nikita Lapkov](https://blog.cloudflare.com/author/nikita-lapkov/), and [Jérôme Schneider](https://blog.cloudflare.com/author/jerome/)

April 10, 2025## [Sequential consistency without borders: how D1 implements global read replication](https://blog.cloudflare.com/d1-read-replication-beta/)

D1, Cloudflare’s managed SQL database, announces read replication beta. Here's a deep dive of the read replication implementation and how your queries can remain consistent across all regions.

![Justin Mazzola Paluska](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462TBPQQQGVSNE4R1Q55M1.png&w=64&h=64&f=webp&fit=cover&position=center)![Lambros Petrou](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47WA9G46YD5HZY63QTNT9A.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Justin Mazzola Paluska](https://blog.cloudflare.com/author/justin-mazzola-paluska/) and [Lambros Petrou](https://blog.cloudflare.com/author/lambros-petrou/)

April 8, 2025## [Pools across the sea: how Hyperdrive speeds up access to databases and why we’re making it free](https://blog.cloudflare.com/how-hyperdrive-speeds-up-database-access/)

Hyperdrive, Cloudflare's global connection pooler, relies on some key innovations to make your database connections work. Let's dive deeper, in celebration of its availability for Free Plan customers.

![Andrew Repp](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SY3XJK8CSZZFSD0TQ47A.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Matt Alonso](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW452FJYAB1W8XF6QXGGKSVK.png&w=64&h=64&f=webp&fit=cover&position=center)

[Andrew Repp](https://blog.cloudflare.com/author/andrew-repp/) and [Matt Alonso](https://blog.cloudflare.com/author/matt-alonso/)

April 2, 2025## [A steam locomotive from 1993 broke my yarn test](https://blog.cloudflare.com/yarn-test-suffers-strange-derailment/)

Yarn tests fail consistently at the 27-second mark. The usual suspects are swiftly eliminated. A deep dive is taken to comb through traces, only to be derailed into an unexpected crash investigation.

![Yew Leong](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47WY2V47FRVMZG9QW45ZVB.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yew Leong](https://blog.cloudflare.com/author/yew-leong/)

February 14, 2025## [Searching for the cause of hung tasks in the Linux kernel](https://blog.cloudflare.com/searching-for-the-cause-of-hung-tasks-in-the-linux-kernel/)

The Linux kernel can produce a hung task warning. Searching the Internet and the kernel docs, you can find a brief explanation that the process is stuck in the uninterruptible state.

![Oxana Kharitonova](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462M0EFJXTMW95T83V5454.png&w=64&h=64&f=webp&fit=cover&position=center)![Jesper Brouer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW499RS2WW80VBYFGEW0TADD.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Oxana Kharitonova](https://blog.cloudflare.com/author/oxana/) and [Jesper Brouer](https://blog.cloudflare.com/author/jesper-brouer/)

January 27, 2025## [Over 700 million events/second: How we make sense of too much data](https://blog.cloudflare.com/how-we-make-sense-of-too-much-data/)

Here we explain how we made our data pipeline scale to 700 million events per second while becoming more resilient than ever before. We share some math behind the approach and some of the designs.

![Constantin Pan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4569HHEF9XM981Y3Q8T9FF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jim Hawkridge](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455228FF3J2XW973RTKHR2.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Constantin Pan](https://blog.cloudflare.com/author/constantin-pan/) and [Jim Hawkridge](https://blog.cloudflare.com/author/jim-hawkridge/)

January 3, 2025## [Multi-Path TCP: revolutionizing connectivity, one path at a time](https://blog.cloudflare.com/multi-path-tcp-revolutionizing-connectivity-one-path-at-a-time/)

Multi-Path TCP (MPTCP) leverages multiple network interfaces, like Wi-Fi and cellular, to provide seamless mobility for more reliable connectivity. While promising, MPTCP is still in its early stages,

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/author/marek-majkowski/)

October 25, 2024## [Elephants in tunnels: how Hyperdrive connects to databases inside your VPC networks](https://blog.cloudflare.com/elephants-in-tunnels-how-hyperdrive-connects-to-databases-inside-your-vpc-networks/)

Hyperdrive (Cloudflare’s globally distributed SQL connection pooler and cache) recently added support for directing database traffic from Workers across Cloudflare Tunnels.

![Andrew Repp](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SY3XJK8CSZZFSD0TQ47A.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Emilio Assunção](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BHFV47MQQ1Z1KF20NQG6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Abhishek Chanda](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4603PGXXYDV5YED6Q6MKQB.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Andrew Repp](https://blog.cloudflare.com/author/andrew-repp/), [Emilio Assunção](https://blog.cloudflare.com/author/emilio-assuncao/), and [Abhishek Chanda](https://blog.cloudflare.com/author/abhishek-chanda/)

October 23, 2024## [Training a million models per day to save customers of all sizes from DDoS attacks](https://blog.cloudflare.com/training-a-million-models-per-day-to-save-customers-of-all-sizes-from-ddos/)

In this post we will describe how we use anomaly detection to watch for novel DDoS attacks. We’ll provide an overview of how we build models which flag unusual traffic and keep our customers safe.

![Nick Wood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490CQBGG1HX5RJ9S0NQYZE.png&w=64&h=64&f=webp&fit=cover&position=center)![Manish Arora](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW472P0T2N5TT53DVJYPJWAK.png&w=64&h=64&f=webp&fit=cover&position=center)

[Nick Wood](https://blog.cloudflare.com/author/nick-wood/) and [Manish Arora](https://blog.cloudflare.com/author/manish/)

October 22, 2024## [Building Vectorize, a distributed vector database, on Cloudflare’s Developer Platform](https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/)

Cloudflare's Vectorize is now generally available, offering faster responses, lower pricing, a free tier, and supporting up to 5 million vectors.

![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)![Alex Graham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48RGYX3NYXWZKRVZM74ZV1.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Jérôme Schneider](https://blog.cloudflare.com/author/jerome/) and [Alex Graham](https://blog.cloudflare.com/author/alex-graham/)

April 12, 2024## [How we ensure Cloudflare customers aren't affected by Let's Encrypt's certificate chain change](https://blog.cloudflare.com/shortening-lets-encrypt-change-of-trust-no-impact-to-cloudflare-customers/)

Let’s Encrypt’s cross-signed chain will be expiring in September. This will affect legacy devices with outdated trust stores (Android versions 7.1.1 or older). To prevent this change from impacting customers, Cloudflare will shift Let’s Encrypt certificates upon renewal to use a different CA

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/author/dina/)

Load more
