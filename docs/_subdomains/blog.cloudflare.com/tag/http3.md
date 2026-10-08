---
url: https://blog.cloudflare.com/tag/http3/
title: Posts tagged \"HTTP3\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:09:10.581803+00:00
---

# Posts tagged "HTTP3" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/http3/

TAG

# HTTP3

[Subscribe to HTTP3 RSS feed](https://blog.cloudflare.com/tag/http3/rss)

July 27, 2026## [We’re open-sourcing our privacy proxy CLI](https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/)

pvcli is a curl-like tool designed to simplify the testing of complex privacy protocols like OHTTP.

![Hannah Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYHF9MV2X49QE0SXTCSPH1N2.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Ben Yang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495TVKCM4J39JXG32VTCNG.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Fisher Darling](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463PVCFZWEEPCE2T84TW2R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Hannah Wang](https://blog.cloudflare.com/author/hannah-wang/), [Ben Yang](https://blog.cloudflare.com/author/ben-yang/), and [Fisher Darling](https://blog.cloudflare.com/author/fisher/)

May 12, 2026## [When "idle" isn't idle: how a Linux kernel optimization became a QUIC bug](https://blog.cloudflare.com/quic-death-spiral-fix/)

We investigated a bug where CUBIC's congestion window became pinned at its minimum floor, causing a performance to plummet. The fix involved correctly measuring idle periods to distinguish RTT wait times from actual application idleness.

![Esteban Carisimo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VSSKPEBK3K5ND6JZ67YP.webp&w=64&h=64&f=webp&fit=cover&position=center)![Antonio Vicente](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487NFE7AY4B70WNGYX9WZ9.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Esteban Carisimo](https://blog.cloudflare.com/author/esteban-carisimo/) and [Antonio Vicente](https://blog.cloudflare.com/author/antonio-vicente/)

February 10, 2025## [QUIC action: patching a broadcast address amplification vulnerability](https://blog.cloudflare.com/mitigating-broadcast-address-attack/)

Cloudflare was recently contacted by researchers who discovered a broadcast amplification vulnerability through their QUIC Internet measurement research. We've implemented a mitigation.

![Josephine Chow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW496EEZSG9EMYJFTHPP2Q8A.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![June Slater](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SCBXA2XSNDDC08ZYCVCS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Josephine Chow](https://blog.cloudflare.com/author/josephine-chow/), [June Slater](https://blog.cloudflare.com/author/june-slater/), [Bryton Herdes](https://blog.cloudflare.com/author/bryton/), and [Lucas Pardue](https://blog.cloudflare.com/author/lucas/)

December 30, 2024## [Open sourcing h3i: a command line tool and library for low-level HTTP/3 testing and debugging](https://blog.cloudflare.com/h3i/)

h3i is a command line tool and Rust library designed for low-level testing and debugging of HTTP/3, which runs over QUIC.

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Evan Rittenhouse](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47GS3RW10ESS21SA5P60SX.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/author/lucas/) and [Evan Rittenhouse](https://blog.cloudflare.com/author/evan-rittenhouse/)

March 6, 2024## [Zero Trust WARP: tunneling with a MASQUE](https://blog.cloudflare.com/zero-trust-warp-with-a-masque/)

This blog discusses the introduction of MASQUE to Zero Trust WARP and how Cloudflare One customers will benefit from this modern protocol

![Dan Hall](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46Z2K75S50M22FWMMB9CAJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dan Hall](https://blog.cloudflare.com/author/dan-hall/)

June 20, 2023## [Introducing HTTP/3 Prioritization](https://blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/)

Today, Cloudflare is very excited to announce full support for HTTP/3 Extensible Priorities, a new standard that speeds the loading of webpages by up to 37%

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Achiel van der Mandele](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46PX2WV5KG8RYPQWH4Q50Q.png&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/author/lucas/) and [Achiel van der Mandele](https://blog.cloudflare.com/author/achiel/)

December 30, 2022## [The state of HTTP in 2022](https://blog.cloudflare.com/the-state-of-http-in-2022/)

So what happened at all of those working group meetings, specification documents, and side events in 2022? What are implementers and deployers of the web’s protocol doing? And what’s coming next?

![Mark Nottingham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44K3PCPNB7HHJRJHCHP6H4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Mark Nottingham](https://blog.cloudflare.com/author/mark-nottingham/)

June 24, 2022## [HTTP/3 inspection on Cloudflare Gateway](https://blog.cloudflare.com/cloudflare-gateway-http3-inspection/)

Today we’re excited to announce the ability for administrators to apply Zero Trust inspection policies to HTTP/3 traffic

![Ankur Aggarwal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47NKH772PAS2QKG6BFKRHR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Ankur Aggarwal](https://blog.cloudflare.com/author/ankur/)

June 6, 2022## [HTTP RFCs have evolved: A Cloudflare view of HTTP usage trends](https://blog.cloudflare.com/cloudflare-view-http3-usage/)

HTTP/3 is now RFC 9114. We explore Cloudflare's view of how it is being used

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/author/lucas/) and [David Belson](https://blog.cloudflare.com/author/david-belson/)

October 22, 2020## [A Last Call for QUIC, a giant leap for the Internet](https://blog.cloudflare.com/last-call-for-quic/)

QUIC and HTTP/3 are open standards that have been under development in the IETF for almost exactly 4 years. On October 21, 2020, following two rounds of Working Group Last Call, draft 32 of the family of documents that describe QUIC and HTTP/3 were put into IETF Last Call.

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/author/lucas/)

September 30, 2020## [Speeding up HTTPS and HTTP/3 negotiation with... DNS](https://blog.cloudflare.com/speeding-up-https-and-http-3-negotiation-with-dns/)

A look at a new DNS resource record intended to speed-up negotiation of HTTP security and performance features and how it will help make the web faster.

![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alessandro Ghedini](https://blog.cloudflare.com/author/alessandro-ghedini/)

June 30, 2020## [How to test HTTP/3 and QUIC with Firefox Nightly](https://blog.cloudflare.com/how-to-test-http-3-and-quic-with-firefox-nightly/)

Now that Firefox Nightly supports HTTP/3 we thought we'd share some instructions to help you enable and test it yourselves.

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/author/lucas/)

April 14, 2020## [Comparing HTTP/3 vs. HTTP/2 Performance](https://blog.cloudflare.com/http-3-vs-http-2/)

We announced support for HTTP/3, the successor to HTTP/2, during Cloudflare’s birthday week last year. Our goal is and has always been to help build a better Internet. Even though HTTP/3 is still in draft status, we've seen a lot of interest from our users.

![Sreeni Tellakula](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463BK5X364DPZP3DD4FQ83.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Sreeni Tellakula](https://blog.cloudflare.com/author/sreeni-tellakula/)

January 14, 2020## [A cost-effective and extensible testbed for transport protocol development](https://blog.cloudflare.com/a-cost-effective-and-extensible-testbed-for-transport-protocol-development/)

At Cloudflare, we develop protocols at multiple layers of the network stack. In the past, we focused on HTTP/1.1, HTTP/2, and TLS 1.3. Now, we are working on QUIC and HTTP/3, which are still in IETF draft, but gaining a lot of interest.

![Lohith Bellad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49NY9WGAQ1TH27ZQSWAWCE.png&w=64&h=64&f=webp&fit=cover&position=center)![Junho Choi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49A9S8PVCT5XTZNVN0K6SP.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lohith Bellad](https://blog.cloudflare.com/author/lohith/) and [Junho Choi](https://blog.cloudflare.com/author/junho/)

January 8, 2020## [Accelerating UDP packet transmission for QUIC](https://blog.cloudflare.com/accelerating-udp-packet-transmission-for-quic/)

Significant work has gone into optimizing TCP, UDP hasn't received as much attention, putting QUIC at a disadvantage. Let's explore a few tricks that help mitigate this.

![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alessandro Ghedini](https://blog.cloudflare.com/author/alessandro-ghedini/)

October 17, 2019## [Experiment with HTTP/3 using NGINX and quiche](https://blog.cloudflare.com/experiment-with-http-3-using-nginx-and-quiche/)

Just a few weeks ago we announced the availability on our edge network of HTTP/3, the new revision of HTTP intended to improve security and performance on the Internet. Everyone can now enable HTTP/3 on their Cloudflare zone

![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alessandro Ghedini](https://blog.cloudflare.com/author/alessandro-ghedini/)

September 27, 2019## [Birthday Week 2019 Wrap-up](https://blog.cloudflare.com/birthday-week-2019-wrap-up/)

This week we celebrated Cloudflare’s 9th birthday by launching a variety of new offerings that support our mission: to help build a better Internet. Below is a summary recap of how we celebrated Birthday Week 2019.

![Jake Anderson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GF4DF0GG3A36F3WNYN2N.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Jake Anderson](https://blog.cloudflare.com/author/jake-anderson/)

September 26, 2019## [HTTP/3: the past, the present, and the future](https://blog.cloudflare.com/http3-the-past-present-and-future/)

We are now happy to announce that QUIC and HTTP/3 support is available on the Cloudflare edge network. We’re excited to be joined in this announcement by Google Chrome and Mozilla Firefox, two of the leading browser vendors and partners in our effort to make the web faster and more reliable for all.

![Alessandro Ghedini](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H2E9D8N6JKPKGJDGCW6M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Rustam Lalkaka](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45YY8QEMHA71G37Y0EH50C.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alessandro Ghedini](https://blog.cloudflare.com/author/alessandro-ghedini/) and [Rustam Lalkaka](https://blog.cloudflare.com/author/rustam/)

Load more
