---
url: https://blog.cloudflare.com/tag/dns/
title: Posts tagged \"DNS\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:49.649405+00:00
---

# Posts tagged "DNS" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/dns/

TAG

# DNS

[Subscribe to DNS RSS feed](https://blog.cloudflare.com/tag/dns/rss)

October 6, 2026## [The keys to the Internet change on October 11. Are you ready?](https://blog.cloudflare.com/root-ksk-2024-rollover/)

On October 11, 2026, the DNS root switches to a new key-signing key (KSK-2024). Learn what this means for you, and how RFC 8509 trust anchor sentinels allow you to test whether your DNS resolver is ready for the rollover.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)![James Godlewski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M48ZN7537R9D7AB9PWK3P0Q9.01M48ZN84M75FBR63MKDCQTCED.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/) and [James Godlewski](https://blog.cloudflare.com/author/james-godlewski/)

September 10, 2026## [1.1.1.1 now supports post-quantum DNSSEC, all 2,420 bytes of it](https://blog.cloudflare.com/post-quantum-dnssec-1111/)

1.1.1.1 now validates DNSSEC signatures using NIST’s post-quantum ML-DSA-44 algorithm. Here is how we manage 2,420-byte signatures and downgrade risks at scale.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)![Bas Westerbaan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46N3BWJ6WS6790KRRJ4RWD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/) and [Bas Westerbaan](https://blog.cloudflare.com/author/bas/)

August 27, 2026## [How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/)

Five Rust-level memory optimizations to the DNS cache layout of Big Pineapple cut per-entry memory by 56%, freeing approximately 100 TB of memory across Cloudflare's fleet.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

July 20, 2026## [Cloudflare Internal DNS is now generally available](https://blog.cloudflare.com/internal-dns/)

Cloudflare Internal DNS brings authoritative and recursive DNS for private networks to the same global network and control plane that runs Cloudflare's Zero Trust, networking, and public DNS.

![Enrique Somoza](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KY0CFW3DJ9J69XDCMWR1NNSG.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Hannes Gerhart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P53YA8A3G53W0H9FH0TT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Enrique Somoza](https://blog.cloudflare.com/author/enrique-somoza/) and [Hannes Gerhart](https://blog.cloudflare.com/author/hannes/)

July 14, 2026## [A broken DNSSEC rollover took down .al. Now 1.1.1.1 tells you when validation is bypassed](https://blog.cloudflare.com/dnssec-nta-ede-33/)

When a failed DNSSEC key rollover took down the .al TLD, we deployed a Negative Trust Anchor to restore resolution. This time, though, clients didn't have to take our word for it: 1.1.1.1 returned EDE 33, a new DNS error code that signals directly in the response that DNSSEC validation was bypassed.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

June 10, 2026## [Route public traffic to private applications with Cloudflare](https://blog.cloudflare.com/private-origins-dns-routing/)

Application Services for Private Origins is available now in closed beta. Route public hostnames to private IP origins over your existing IPsec, GRE, CNI, or Cloudflare Mesh paths. No public IPs or extra connector software required.

![Enrique Somoza](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KY0CFW3DJ9J69XDCMWR1NNSG.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Steve Welham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW451R06ENST8DGAV3F7RKS1.png&w=64&h=64&f=webp&fit=cover&position=center)![Shruti Mittal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49HBW40EJGDC404YV6193A.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Enrique Somoza](https://blog.cloudflare.com/author/enrique-somoza/), [Steve Welham](https://blog.cloudflare.com/author/steve-welham/), and [Shruti Mittal](https://blog.cloudflare.com/author/shruti-mittal/)

May 27, 2026## [Iran's Internet is partially restored, Cloudflare Radar data shows](https://blog.cloudflare.com/iran-internet-partially-restored-may-2026/)

Cloudflare Radar data confirms early indications of a partial Internet restoration in Iran, nearly three months after the shutdown began. Traffic spikes and DNS queries have risen, but network activity is currently just 40% of pre-shutdown levels.

![Lai Yi Ohlsen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DGMNXAW2CZQQAX92W97V.png&w=64&h=64&f=webp&fit=cover&position=center)![Sabina Zejnilovic](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49B114HP8HRQ7MA3FAFRSN.JPG&w=64&h=64&f=webp&fit=cover&position=center)

[Lai Yi Ohlsen](https://blog.cloudflare.com/author/lai-yi-ohlsen/) and [Sabina Zejnilovic](https://blog.cloudflare.com/author/sabina/)

May 6, 2026## [When DNSSEC goes wrong: how we responded to the .de TLD outage](https://blog.cloudflare.com/de-tld-outage-dnssec/)

On May 5, 2026, DENIC published broken DNSSEC signatures for the .de TLD, making millions of domains unreachable. Here's what 1.1.1.1 saw, how serve stale cushioned the impact, and how we restored resolution.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)![Christian Elmerot](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW474H2CPWRSBJ9DXXAEA3KM.png&w=64&h=64&f=webp&fit=cover&position=center)![Max Worsley](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46G5JWQ32WMKW8WD2K1HGX.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/), [Christian Elmerot](https://blog.cloudflare.com/author/christian-elmerot/), and [Max Worsley](https://blog.cloudflare.com/author/max-worsley/)

April 1, 2026## [Our ongoing commitment to privacy for the 1.1.1.1 public DNS resolver](https://blog.cloudflare.com/1111-privacy-examination-2026/)

Eight years ago, we launched 1.1.1.1 to build a faster, more private Internet. Today, we’re sharing the results of our latest independent examination. The result: our privacy protections are working exactly as promised.

![Rory Malone](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45DQQRE3PNN0KFRQ3SBGZJ.png&w=64&h=64&f=webp&fit=cover&position=center)![Hannes Gerhart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P53YA8A3G53W0H9FH0TT.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Leah Romm](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469TWJ112ZTRE0C6FEXRAR.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Rory Malone](https://blog.cloudflare.com/author/rory/), [Hannes Gerhart](https://blog.cloudflare.com/author/hannes/), and [Leah Romm](https://blog.cloudflare.com/author/leah-romm/)

January 14, 2026## [What came first: the CNAME or the A record?](https://blog.cloudflare.com/cname-a-record-order-dns-standards/)

A recent change to 1.1.1.1 accidentally altered the order of CNAME records in DNS responses, breaking resolution for some clients. This post explores the technical root cause, examines the source code of affected resolvers, and dives into the inherent ambiguities of the DNS RFCs.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

December 15, 2025## [ChatGPT's rivals, Kwai's quiet rise: the top Internet services of 2025](https://blog.cloudflare.com/radar-2025-year-in-review-internet-services/)

AI competition intensified in 2025 as ChatGPT gained strong challengers. Instagram climbed, X declined, and platforms like Shopee, Temu, and Kwai reshaped global Internet usage. Our 2025 DNS data shows how Internet patterns evolved.

![João Tomé](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497RTGEQ58P8N9RFTT4A4M.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[João Tomé](https://blog.cloudflare.com/author/joao-tome/)

October 27, 2025## [From .com to .anything: introducing Top-Level Domain (TLD) insights on Cloudflare Radar](https://blog.cloudflare.com/introducing-tld-insights-on-cloudflare-radar/)

Cloudflare Radar has launched a new Top-Level Domain (TLD) page, providing insights into TLD popularity, traffic, and security. The top-ranking TLD may come as a surprise.

![André Jesus](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48SMWWWW1RG87RNZQH78V5.webp&w=64&h=64&f=webp&fit=cover&position=center)![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[André Jesus](https://blog.cloudflare.com/author/andre-jesus/) and [David Belson](https://blog.cloudflare.com/author/david-belson/)

September 4, 2025## [Addressing the unauthorized issuance of multiple TLS certificates for 1.1.1.1](https://blog.cloudflare.com/unauthorized-issuance-of-certificates-for-1-1-1-1/)

Unauthorized TLS certificates were issued for 1.1.1.1 by a Certification Authority without permission from Cloudflare. These rogue certificates have now been revoked.

![Joe Abley](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MP3XA34VR71FH9QWVDS5.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Thibault Meunier](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CG4C7M8Y2P7VRAYHW2RV.png&w=64&h=64&f=webp&fit=cover&position=center)![Vicky Shrestha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QW01XDQ9HR53EG76H0K6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bas Westerbaan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46N3BWJ6WS6790KRRJ4RWD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Joe Abley](https://blog.cloudflare.com/author/joe-abley/), [Thibault Meunier](https://blog.cloudflare.com/author/thibault/), [Vicky Shrestha](https://blog.cloudflare.com/author/vicky/), and [Bas Westerbaan](https://blog.cloudflare.com/author/bas/)

February 27, 2025## [Some TXT about, and A PTR to, new DNS insights on Cloudflare Radar](https://blog.cloudflare.com/new-dns-section-on-cloudflare-radar/)

The new Cloudflare Radar DNS page provides increased visibility into aggregate traffic and usage trends seen by our 1.1.1.1 resolver

![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Carlos Rodrigues](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P9VMTDZ2R4BDYEPSPMX4.png&w=64&h=64&f=webp&fit=cover&position=center)![Vicky Shrestha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QW01XDQ9HR53EG76H0K6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Hannes Gerhart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P53YA8A3G53W0H9FH0TT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[David Belson](https://blog.cloudflare.com/author/david-belson/), [Carlos Rodrigues](https://blog.cloudflare.com/author/carlos-rodrigues/), [Vicky Shrestha](https://blog.cloudflare.com/author/vicky/), and [Hannes Gerhart](https://blog.cloudflare.com/author/hannes/)

November 8, 2024## [How we prevent conflicts in authoritative DNS configuration using formal verification](https://blog.cloudflare.com/topaz-policy-engine-design/)

We describe how Cloudflare uses a custom Lisp-like programming language and formal verifier (written in Racket and Rosette) to prevent logical contradictions in our authoritative DNS nameserver’s behavior.

![James Larisch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44C9J5HQA4MAD7AN1K285E.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Marwan Fayed](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4975XAXEZ77Q31PP9FF3ME.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[James Larisch](https://blog.cloudflare.com/author/james-larisch/), [Suleman Ahmad](https://blog.cloudflare.com/author/suleman/), and [Marwan Fayed](https://blog.cloudflare.com/author/marwan/)

October 29, 2024## [Migrating billions of records: moving our active DNS database while it’s in use](https://blog.cloudflare.com/migrating-billions-of-records-moving-our-active-dns-database-while-in-use/)

DNS records have moved to a new database, bringing improved performance and reliability to all customers.

![Alex Fattouche](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H0J66VY9AP4Y8GXCS4RZ.png&w=64&h=64&f=webp&fit=cover&position=center)![Corey Horton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455RXC9SP67GW0ZACX19AQ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Fattouche](https://blog.cloudflare.com/author/alex-fattouche/) and [Corey Horton](https://blog.cloudflare.com/author/corey-horton/)

September 24, 2024## [Cloudflare partners with Internet Service Providers and network equipment providers to deliver a safer browsing experience to millions of homes](https://blog.cloudflare.com/safer-resolver/)

Cloudflare is extending the use of our public DNS resolver through partnering with ISPs and network providers to deliver a safer browsing experience directly to families. Join us in protecting every Internet user from unsafe content with the click of a button, powered by 1.1.1.1 for Families.

![Kelly May Johnston](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46WM5TMV3Y8S91FG1PQJ01.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Morgan Steffen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW489Z1BSN8HPMPKAR5PP1AF.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kelly May Johnston](https://blog.cloudflare.com/author/kelly-may-johnston/) and [Morgan Steffen](https://blog.cloudflare.com/author/morgan-steffen/)

September 23, 2024## [Making zone management more efficient with batch DNS record updates](https://blog.cloudflare.com/batched-dns-changes/)

In response to customer demand, we now support the ability to DELETE, PATCH, PUT and POST multiple DNS records in a single API call, enabling more efficient and reliable zone management. 

![Alex Fattouche](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H0J66VY9AP4Y8GXCS4RZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Fattouche](https://blog.cloudflare.com/author/alex-fattouche/)

Load more
