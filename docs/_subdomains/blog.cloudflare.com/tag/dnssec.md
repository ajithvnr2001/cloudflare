---
url: https://blog.cloudflare.com/tag/dnssec/
title: Posts tagged \"DNSSEC\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:50.790703+00:00
---

# Posts tagged "DNSSEC" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/dnssec/

TAG

# DNSSEC

[Subscribe to DNSSEC RSS feed](https://blog.cloudflare.com/tag/dnssec/rss)

October 6, 2026## [The keys to the Internet change on October 11. Are you ready?](https://blog.cloudflare.com/root-ksk-2024-rollover/)

On October 11, 2026, the DNS root switches to a new key-signing key (KSK-2024). Learn what this means for you, and how RFC 8509 trust anchor sentinels allow you to test whether your DNS resolver is ready for the rollover.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)![James Godlewski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M48ZN7537R9D7AB9PWK3P0Q9.01M48ZN84M75FBR63MKDCQTCED.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/) and [James Godlewski](https://blog.cloudflare.com/author/james-godlewski/)

September 10, 2026## [1.1.1.1 now supports post-quantum DNSSEC, all 2,420 bytes of it](https://blog.cloudflare.com/post-quantum-dnssec-1111/)

1.1.1.1 now validates DNSSEC signatures using NIST’s post-quantum ML-DSA-44 algorithm. Here is how we manage 2,420-byte signatures and downgrade risks at scale.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)![Bas Westerbaan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46N3BWJ6WS6790KRRJ4RWD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/) and [Bas Westerbaan](https://blog.cloudflare.com/author/bas/)

July 14, 2026## [A broken DNSSEC rollover took down .al. Now 1.1.1.1 tells you when validation is bypassed](https://blog.cloudflare.com/dnssec-nta-ede-33/)

When a failed DNSSEC key rollover took down the .al TLD, we deployed a Negative Trust Anchor to restore resolution. This time, though, clients didn't have to take our word for it: 1.1.1.1 returned EDE 33, a new DNS error code that signals directly in the response that DNSSEC validation was bypassed.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

May 6, 2026## [When DNSSEC goes wrong: how we responded to the .de TLD outage](https://blog.cloudflare.com/de-tld-outage-dnssec/)

On May 5, 2026, DENIC published broken DNSSEC signatures for the .de TLD, making millions of domains unreachable. Here's what 1.1.1.1 saw, how serve stale cushioned the impact, and how we restored resolution.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)![Christian Elmerot](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW474H2CPWRSBJ9DXXAEA3KM.png&w=64&h=64&f=webp&fit=cover&position=center)![Max Worsley](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46G5JWQ32WMKW8WD2K1HGX.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/), [Christian Elmerot](https://blog.cloudflare.com/author/christian-elmerot/), and [Max Worsley](https://blog.cloudflare.com/author/max-worsley/)

February 27, 2025## [Some TXT about, and A PTR to, new DNS insights on Cloudflare Radar](https://blog.cloudflare.com/new-dns-section-on-cloudflare-radar/)

The new Cloudflare Radar DNS page provides increased visibility into aggregate traffic and usage trends seen by our 1.1.1.1 resolver

![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Carlos Rodrigues](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P9VMTDZ2R4BDYEPSPMX4.png&w=64&h=64&f=webp&fit=cover&position=center)![Vicky Shrestha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QW01XDQ9HR53EG76H0K6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Hannes Gerhart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P53YA8A3G53W0H9FH0TT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[David Belson](https://blog.cloudflare.com/author/david-belson/), [Carlos Rodrigues](https://blog.cloudflare.com/author/carlos-rodrigues/), [Vicky Shrestha](https://blog.cloudflare.com/author/vicky/), and [Hannes Gerhart](https://blog.cloudflare.com/author/hannes/)

February 29, 2024## [Remediating new DNSSEC resource exhaustion vulnerabilities](https://blog.cloudflare.com/remediating-new-dnssec-resource-exhaustion-vulnerabilities/)

Cloudflare recently fixed two critical DNSSEC vulnerabilities: CVE-2023-50387 and CVE-2023-50868. Both of these vulnerabilities can exhaust computational resources of validating DNS resolvers. These vulnerabilities do not affect our Authoritative DNS or DNS firewall products

![Vicky Shrestha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QW01XDQ9HR53EG76H0K6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Anbang Wen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KFNG572S3BFGS2YK900X.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Vicky Shrestha](https://blog.cloudflare.com/author/vicky/) and [Anbang Wen](https://blog.cloudflare.com/author/anbang/)

July 11, 2023## [Connection errors in Asia Pacific region on July 9, 2023](https://blog.cloudflare.com/connection-errors-in-asia-pacific-region-on-july-9-2023/)

On July 9, 2023, users in the Asia Pacific region experienced connection errors due to origin DNS resolution failures to .com and .net TLD nameservers

![Christian Elmerot](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW474H2CPWRSBJ9DXXAEA3KM.png&w=64&h=64&f=webp&fit=cover&position=center)![Alex Fattouche](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H0J66VY9AP4Y8GXCS4RZ.png&w=64&h=64&f=webp&fit=cover&position=center)![Hannes Gerhart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P53YA8A3G53W0H9FH0TT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Christian Elmerot](https://blog.cloudflare.com/author/christian-elmerot/), [Alex Fattouche](https://blog.cloudflare.com/author/alex-fattouche/), and [Hannes Gerhart](https://blog.cloudflare.com/author/hannes/)

March 9, 2022## [DNSSEC issues take Fiji domains offline](https://blog.cloudflare.com/dnssec-issues-fiji/)

DNSSEC issues with the .fj ccTLD caused problems reaching websites on the island nation

![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[David Belson](https://blog.cloudflare.com/author/david-belson/)

April 17, 2020## [Is BGP Safe Yet? No. But we are tracking it carefully](https://blog.cloudflare.com/is-bgp-safe-yet-rpki-routing-security-initiative/)

BGP leaks and leaks and hijacks have been accepted as an unavoidable part of the Internet for far too long. Today, we are releasing isBGPSafeYet.com, a website to track deployments and filtering of invalid routes by the major networks.

![Louis Poinsignon](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45XKBQHBMEVSAS1MAW42NT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Louis Poinsignon](https://blog.cloudflare.com/author/louis-poinsignon/)

March 15, 2019## [RFC8482 - Saying goodbye to ANY](https://blog.cloudflare.com/rfc8482-saying-goodbye-to-any/)

Ladies and gentlemen, I would like you to welcome the new shiny RFC8482, which effectively deprecates DNS ANY query type. DNS ANY was a "meta-query" - think about it as a similar thing to the common A, AAAA, MX or SRV query types, but unlike these it wasn't a real query type - it was special.

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/author/marek-majkowski/)

February 22, 2019## [Cloudflare Registrar at three months](https://blog.cloudflare.com/registrar-after-three-months/)

We’re excited to make Cloudflare Registrar available to all of our customers and we’d like to share some insights and data about domain registration that we learned during the early access period.

![Sam Rhea](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45B32X8M7A8CXY9C0SX0EQ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sam Rhea](https://blog.cloudflare.com/author/sam/)

January 16, 2019## [One-Click DNSSEC with Cloudflare Registrar](https://blog.cloudflare.com/one-click-dnssec-with-cloudflare-registrar/)

When you launch a domain, you rely on the Domain Name System to direct your users to your site. However, DNS can't guarantee that visitors reach your content because basic DNS lacks authentication.

![Sam Rhea](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45B32X8M7A8CXY9C0SX0EQ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sam Rhea](https://blog.cloudflare.com/author/sam/)

September 18, 2018## [Expanding DNSSEC Adoption](https://blog.cloudflare.com/automatically-provision-and-maintain-dnssec/)

Cloudflare first started talking about DNSSEC in 2014 and at the time, Nick Sullivan wrote: “DNSSEC is a valuable tool for improving the trust and integrity of DNS, the backbone of the modern Internet.”

![Sergi Isasi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GA2M8TX4RHAHVAP55XN1.png&w=64&h=64&f=webp&fit=cover&position=center)![Vicky Shrestha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QW01XDQ9HR53EG76H0K6.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Sergi Isasi](https://blog.cloudflare.com/author/sergi/) and [Vicky Shrestha](https://blog.cloudflare.com/author/vicky/)

September 17, 2018## [End-to-End Integrity with IPFS](https://blog.cloudflare.com/e2e-integrity/)

Use Cloudflare’s IPFS gateway to set up a website which is end-to-end secure, while maintaining the performance and reliability benefits of being served from Cloudflare’s edge network.

![Brendan McMillion](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49JHKGRN1NGXFK2PCA5G2A.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Brendan McMillion](https://blog.cloudflare.com/author/brendan/)

September 17, 2018## [Cloudflare goes InterPlanetary - Introducing Cloudflare’s IPFS Gateway](https://blog.cloudflare.com/distributed-web-gateway/)

Today we’re excited to introduce Cloudflare’s IPFS Gateway, an easy way to access content from the the InterPlanetary File System (IPFS) that doesn’t require installing and running any special software on your computer.

![Andy Parker](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46VGQVK0ZVRDX2MSCKPXV4.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Andy Parker](https://blog.cloudflare.com/author/andy/)

August 6, 2018## [Additional Record Types Available with Cloudflare DNS](https://blog.cloudflare.com/additional-record-types-available-with-cloudflare-dns/)

Cloudflare recently updated the authoritative DNS service to support nine new record types. Since these records are less commonly used than what we previously supported, we thought it would be a good idea to do a brief explanation of each record type and how it is used.

![Sergi Isasi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GA2M8TX4RHAHVAP55XN1.png&w=64&h=64&f=webp&fit=cover&position=center)![Etienne Labaume](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4737Q4D7DYCNK51MG9XFC4.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Sergi Isasi](https://blog.cloudflare.com/author/sergi/) and [Etienne Labaume](https://blog.cloudflare.com/author/etienne-labaume/)

February 6, 2018## [It’s Hard To Change The Keys To The Internet And It Involves Destroying HSM’s](https://blog.cloudflare.com/its-hard-to-change-the-keys-to-the-internet-and-it-involves-destroying-hsms/)

The root of the DNS tree has been using DNSSEC to protect the zone content since 2010. DNSSEC is simply a mechanism to provide cryptographic signatures alongside DNS records that can be validated, i.e. prove the answer is correct and has not been tampered with. 

![Ólafur Guðmundsson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44HAGHBK6S60Z1E6GP861N.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ólafur Guðmundsson](https://blog.cloudflare.com/author/olafur-gudmundsson/)

August 18, 2017## [Broken packets: IP fragmentation is flawed](https://blog.cloudflare.com/ip-fragmentation-is-broken/)

As opposed to the public telephone network, the internet has a Packet Switched design. But just how big can these packets be?

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/author/marek-majkowski/)

Load more
