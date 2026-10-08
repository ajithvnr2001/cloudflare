---
url: https://blog.cloudflare.com/tag/congestion-control/
title: Posts tagged \"Congestion Control\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:38.783590+00:00
---

# Posts tagged "Congestion Control" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/congestion-control/

TAG

# Congestion Control

[Subscribe to Congestion Control RSS feed](https://blog.cloudflare.com/tag/congestion-control/rss)

May 12, 2026## [When "idle" isn't idle: how a Linux kernel optimization became a QUIC bug](https://blog.cloudflare.com/quic-death-spiral-fix/)

We investigated a bug where CUBIC's congestion window became pinned at its minimum floor, causing a performance to plummet. The fix involved correctly measuring idle periods to distinguish RTT wait times from actual application idleness.

![Esteban Carisimo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VSSKPEBK3K5ND6JZ67YP.webp&w=64&h=64&f=webp&fit=cover&position=center)![Antonio Vicente](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487NFE7AY4B70WNGYX9WZ9.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Esteban Carisimo](https://blog.cloudflare.com/author/esteban-carisimo/) and [Antonio Vicente](https://blog.cloudflare.com/author/antonio-vicente/)
