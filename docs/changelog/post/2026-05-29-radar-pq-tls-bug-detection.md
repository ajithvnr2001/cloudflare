---
url: https://developers.cloudflare.com/changelog/post/2026-05-29-radar-pq-tls-bug-detection/
title: TLS bug detection in the Cloudflare Radar post-quantum checker \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.501196+00:00
---

# TLS bug detection in the Cloudflare Radar post-quantum checker · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-29-radar-pq-tls-bug-detection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 29, 2026

## TLS bug detection in the Cloudflare Radar post-quantum checker

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [**Radar**](https://developers.cloudflare.com/radar/) [post-quantum TLS support checker ↗︎](https://radar.cloudflare.com/post-quantum#website-support) now also reports TLS bugs detected during the handshake test. When a scanned host exhibits compatibility issues, the results include details on the specific bugs detected, along with guidance on how to investigate and remediate each issue. The bugs section only appears for hosts where issues are found.

The following TLS bugs are detected:

  * **Split ClientHello** — The connection fails with a fragmented post-quantum `ClientHello` but succeeds with classical handshakes. Typically caused by middleboxes or firewalls that cannot reassemble split TLS messages.
  * **HRR Failure** — The server sends a `HelloRetryRequest` but fails to complete the handshake afterward.
  * **Unknown Keyshare** — The server cannot handle unknown key exchange algorithms and fails instead of responding with a `HelloRetryRequest` as required by the TLS 1.3 specification.

![TLS bug detection results in the Radar post-quantum checker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2260,height=1244,format=webp/_astro/pq-tls-bug-detection.BrmsVMno.png)

Bug detection data is available through the existing [`/post_quantum/tls/support`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/) endpoint.

Visit the [Post-Quantum Encryption ↗︎](https://radar.cloudflare.com/post-quantum#website-support) page to test a host.
