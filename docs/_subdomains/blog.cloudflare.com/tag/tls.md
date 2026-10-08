---
url: https://blog.cloudflare.com/tag/tls/
title: Posts tagged \"TLS\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:20:10.217532+00:00
---

# Posts tagged "TLS" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/tls/

TAG

# TLS

[Subscribe to TLS RSS feed](https://blog.cloudflare.com/tag/tls/rss)

September 29, 2026## [Building a certificate authority for the whole Internet](https://blog.cloudflare.com/cloudflare-certificate-authority/)

Twelve years after launching Universal SSL, Cloudflare is applying to become a certificate authority. By combining an established root, an ACME-first approach, and Merkle Tree Certificates, we are building a post-quantum CA for the open web.

![Steve Goldsmith](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497YX7768BEJGS24P0FMX8.png&w=64&h=64&f=webp&fit=cover&position=center)

[Steve Goldsmith](https://blog.cloudflare.com/author/steve-goldsmith/)

September 29, 2026## [Building a post-quantum certificate authority with Merkle Tree Certificates](https://blog.cloudflare.com/pq-ca-with-mtcs/)

As post-quantum signatures threaten to inflate TLS handshakes and certificate transparency logs, Merkle Tree Certificates offer a path to compact, auditable authentication. Cloudflare’s new certificate authority will support MTC issuance at scale.

![Mari Galicer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW481GPW34N2TYBX476WQC8S.png&w=64&h=64&f=webp&fit=cover&position=center)

[Mari Galicer](https://blog.cloudflare.com/author/mari/)

September 8, 2026## [Automatic Key Exchange: faster, post-quantum secure origin handshakes for 45 billion daily connections (and counting)](https://blog.cloudflare.com/automatic-key-exchange-for-origins/)

Automatic Key Exchange probes TLS 1.3-capable customer origins to learn which key agreement algorithms they support. We then lead with the most secure algorithm when connecting to the origin, preferring post-quantum connections wherever the origin supports it. 

![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Yawar Jamal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1PVVBNHNQWX6D1BK30VQW4X.01M1PVVCG30FCBAY7PS1R17190.png&w=64&h=64&f=webp&fit=cover&position=center)![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Suleman Ahmad](https://blog.cloudflare.com/author/suleman/), [Yawar Jamal](https://blog.cloudflare.com/author/yawar/), and [Alex Krivit](https://blog.cloudflare.com/author/alex/)

August 13, 2026## [Certificate Transparency Monitoring is now generally available](https://blog.cloudflare.com/certificate-transparency-monitoring-ga/)

Cloudflare's Certificate Transparency Monitoring is now generally available. The biggest change: we no longer email you about certificates Cloudflare issued for your domain, so when an alert lands in your inbox, it's worth a look.

![Jenny Yang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KZQQ26VN8E4P561X998FKQ9H.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Pravallika Nakarikanti](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KZQQ34PPYQF64Q3WFAPX7W5S.png&w=64&h=64&f=webp&fit=cover&position=center)

[Jenny Yang](https://blog.cloudflare.com/author/jenny-yang/) and [Pravallika Nakarikanti](https://blog.cloudflare.com/author/pravallika-nakarikanti/)

July 29, 2026## [Post-quantum authentication to origins is now supported](https://blog.cloudflare.com/post-quantum-authentication-to-origins/)

Cloudflare now supports post-quantum (PQ) authentication when connecting to customer origin servers via Authenticated Origin Pulls and Custom Origin Trust Store. This is the first step towards providing PQ authentication for all Cloudflare products.

![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Kevin Guthrie](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VQ8K1T55ANDEX70V1EEQ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Luke Valenta](https://blog.cloudflare.com/author/luke/) and [Kevin Guthrie](https://blog.cloudflare.com/author/kevin-guthrie/)

October 28, 2025## [Keeping the Internet fast and secure: introducing Merkle Tree Certificates](https://blog.cloudflare.com/bootstrap-mtc/)

Cloudflare is launching an experiment with Chrome to evaluate fast, scalable, and quantum-ready Merkle Tree Certificates, all without degrading performance or changing WebPKI trust relationships.

![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Christopher Patton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471WT491ZC11M0S5HA34X3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Vânia Gonçalves](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48DQDQ26SRVKPGYTBWBHMD.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bas Westerbaan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46N3BWJ6WS6790KRRJ4RWD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Luke Valenta](https://blog.cloudflare.com/author/luke/), [Christopher Patton](https://blog.cloudflare.com/author/christopher-patton/), [Vânia Gonçalves](https://blog.cloudflare.com/author/vania/), and [Bas Westerbaan](https://blog.cloudflare.com/author/bas/)

September 26, 2025## [Eliminating Cold Starts 2: shard and conquer](https://blog.cloudflare.com/eliminating-cold-starts-2-shard-and-conquer/)

We reduced Cloudflare Workers cold starts by 10x by optimistically routing to servers with already-loaded Workers. Learn how we did it here.

![Harris Hancock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H05HT7CQGVFMPCZBNF6H.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Harris Hancock](https://blog.cloudflare.com/author/harris-hancock/)

September 24, 2025## [Automatically Secure: how we upgraded 6,000,000 domains by default to get ready for the Quantum Future](https://blog.cloudflare.com/automatically-secure/)

After a year since we started enabling Automatic SSL/TLS, we want to talk about these results, why they matter, and how we’re preparing for the next leap in Internet security.

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Yawar Jamal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1PVVBNHNQWX6D1BK30VQW4X.01M1PVVCG30FCBAY7PS1R17190.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/), [Suleman Ahmad](https://blog.cloudflare.com/author/suleman/), and [Yawar Jamal](https://blog.cloudflare.com/author/yawar/)

September 4, 2025## [Addressing the unauthorized issuance of multiple TLS certificates for 1.1.1.1](https://blog.cloudflare.com/unauthorized-issuance-of-certificates-for-1-1-1-1/)

Unauthorized TLS certificates were issued for 1.1.1.1 by a Certification Authority without permission from Cloudflare. These rogue certificates have now been revoked.

![Joe Abley](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MP3XA34VR71FH9QWVDS5.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Thibault Meunier](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CG4C7M8Y2P7VRAYHW2RV.png&w=64&h=64&f=webp&fit=cover&position=center)![Vicky Shrestha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QW01XDQ9HR53EG76H0K6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bas Westerbaan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46N3BWJ6WS6790KRRJ4RWD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Joe Abley](https://blog.cloudflare.com/author/joe-abley/), [Thibault Meunier](https://blog.cloudflare.com/author/thibault/), [Vicky Shrestha](https://blog.cloudflare.com/author/vicky/), and [Bas Westerbaan](https://blog.cloudflare.com/author/bas/)

February 7, 2025## [Resolving a Mutual TLS session resumption vulnerability](https://blog.cloudflare.com/resolving-a-mutual-tls-session-resumption-vulnerability/)

Cloudflare patched a Mutual TLS (mTLS) vulnerability (CVE-2025-23419) reported via its Bug Bounty Program. The flaw in session resumption allowed client certificates to authenticate across different

![Matt Bullock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW466BA2DF5DM17JT5M31SWH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Rushil Mehra](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3J65XQ6KWWMTYQHZMX9VC2Q.01M3J65YDX7BCSBDQXBR3P2B20.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Bullock](https://blog.cloudflare.com/author/matt-bullock/), [Rushil Mehra](https://blog.cloudflare.com/author/rushil-mehra/), and [Alessandro Ghedini](https://blog.cloudflare.com/author/alessandro-ghedini/)

November 7, 2024## [A look at the latest post-quantum signature standardization candidates](https://blog.cloudflare.com/another-look-at-pq-signatures/)

NIST has standardized four post-quantum signature schemes so far, and they’re not done yet: there are fourteen new candidates in the running for standardization.

![Bas Westerbaan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46N3BWJ6WS6790KRRJ4RWD.png&w=64&h=64&f=webp&fit=cover&position=center)![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Bas Westerbaan](https://blog.cloudflare.com/author/bas/) and [Luke Valenta](https://blog.cloudflare.com/author/luke/)

September 25, 2024## [New standards for a faster and more private Internet](https://blog.cloudflare.com/new-standards/)

Cloudflare's customers can now take advantage of Zstandard (zstd) compression, offering 42% faster compression than Brotli and 11.3% more efficiency than GZIP. We're further optimizing performance for our customers with HTTP/3 prioritization and BBR congestion control, and enhancing privacy through Encrypted Client Hello (ECH).

![Matt Bullock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW466BA2DF5DM17JT5M31SWH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Maciej Lechowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46AHNEHP1J791334DRJQ7M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Rushil Mehra](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3J65XQ6KWWMTYQHZMX9VC2Q.01M3J65YDX7BCSBDQXBR3P2B20.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Bullock](https://blog.cloudflare.com/author/matt-bullock/), [Maciej Lechowski](https://blog.cloudflare.com/author/maciej/), and [Rushil Mehra](https://blog.cloudflare.com/author/rushil-mehra/)

August 8, 2024## [Introducing Automatic SSL/TLS: securing and simplifying origin connectivity](https://blog.cloudflare.com/introducing-automatic-ssl-tls-securing-and-simplifying-origin-connectivity/)

This new Automatic SSL/TLS setting will maximize and simplify the encryption modes Cloudflare uses to communicate with origin servers by using the SSL/TLS Recommender.

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![J Evans](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ZE25220R6CASCHHEWHJ1.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Yawar Jamal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1PVVBNHNQWX6D1BK30VQW4X.01M1PVVCG30FCBAY7PS1R17190.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/), [Suleman Ahmad](https://blog.cloudflare.com/author/suleman/), [J Evans](https://blog.cloudflare.com/author/jayeve/), and [Yawar Jamal](https://blog.cloudflare.com/author/yawar/)

July 29, 2024## [Avoiding downtime: modern alternatives to outdated certificate pinning practices](https://blog.cloudflare.com/why-certificate-pinning-is-outdated/)

Outages caused by certificate pinning is increasing. Learn why certificate pinning hasn’t kept up with modern standards and find alternatives to improve security while reducing management overhead

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/author/dina/)

April 12, 2024## [How we ensure Cloudflare customers aren't affected by Let's Encrypt's certificate chain change](https://blog.cloudflare.com/shortening-lets-encrypt-change-of-trust-no-impact-to-cloudflare-customers/)

Let’s Encrypt’s cross-signed chain will be expiring in September. This will affect legacy devices with outdated trust stores (Android versions 7.1.1 or older). To prevent this change from impacting customers, Cloudflare will shift Let’s Encrypt certificates upon renewal to use a different CA

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/author/dina/)

March 14, 2024## [Upcoming Let’s Encrypt certificate chain change and impact for Cloudflare customers](https://blog.cloudflare.com/upcoming-lets-encrypt-certificate-chain-change-and-impact-for-cloudflare-customers/)

Let’s Encrypt’s cross-signed chain will be expiring. To prepare for, Cloudflare will issue certs from Let’s Encrypt’s ISRG X1 chain. This change impacts legacy devices with outdated trust stores.

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/author/dina/)

September 4, 2023## [Connection coalescing with ORIGIN Frames: fewer DNS queries, fewer connections](https://blog.cloudflare.com/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)

In this blog we’re going to take a closer look at “connection coalescing”, with specific focus on manage it at a large scale

![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Suleman Ahmad](https://blog.cloudflare.com/author/suleman/), [Jonathan Hoyland](https://blog.cloudflare.com/author/jonathan-hoyland/), and [Sudheesh Singanamalla](https://blog.cloudflare.com/author/sudheesh/)

August 9, 2023## [Introducing per hostname TLS settings — security fit to your needs](https://blog.cloudflare.com/introducing-per-hostname-tls-settings/)

Starting today, customers that use Cloudflare’s Advanced Certificate Manager can configure TLS settings on individual hostnames within a domain

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/author/dina/)

Load more
