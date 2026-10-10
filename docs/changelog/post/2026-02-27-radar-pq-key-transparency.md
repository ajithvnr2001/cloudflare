---
url: https://developers.cloudflare.com/changelog/post/2026-02-27-radar-pq-key-transparency/
title: Post-Quantum Encryption and Key Transparency on Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.928243+00:00
---

# Post-Quantum Encryption and Key Transparency on Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-27-radar-pq-key-transparency/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 27, 2026

## Post-Quantum Encryption and Key Transparency on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now tracks post-quantum encryption support on origin servers, provides a tool to test any host for post-quantum compatibility, and introduces a Key Transparency dashboard for monitoring end-to-end encrypted messaging audit logs.

#### Post-quantum origin support

The new [`Post-Quantum`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/) API provides the following endpoints:

  * [`/post_quantum/tls/support`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/) \- Tests whether a host supports post-quantum TLS key exchange.
  * [`/post_quantum/origin/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/methods/summary/) \- Returns origin post-quantum data summarized by key agreement algorithm.
  * [`/post_quantum/origin/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/methods/timeseries_groups/) \- Returns origin post-quantum timeseries data grouped by key agreement algorithm.



The new [Post-Quantum Encryption ↗︎](https://radar.cloudflare.com/post-quantum) page shows the share of customer origins supporting [X25519MLKEM768](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-support/#x25519mlkem768), derived from daily automated TLS scans of TLS 1.3-compatible origins. The scanner tests for algorithm support rather than the origin server's configured preference.

![Screenshot of the origin post-quantum support graph on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1040,format=webp/_astro/pq-origin-support.Bn5Dw_It.png)

A host test tool allows checking any publicly accessible website for post-quantum encryption compatibility. Enter a hostname and optional port to see whether the server negotiates a post-quantum key exchange algorithm.

![Screenshot of the post-quantum host test tool on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2372,height=566,format=webp/_astro/pq-host-test.dRqwoOvo.png)

#### Key Transparency

A new [Key Transparency ↗︎](https://radar.cloudflare.com/key-transparency) section displays the audit status of Key Transparency logs for end-to-end encrypted messaging services. The page launches with two monitored logs: WhatsApp and Facebook Messenger Transport.

Each log card shows the current status, last signed epoch, last verified epoch, and the root hash of the Auditable Key Directory tree. The data is also available through the [Key Transparency Auditor API](https://developers.cloudflare.com/key-transparency/api/).

![Screenshot of the Key Transparency dashboard on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2454,height=1062,format=webp/_astro/key-transparency-dashboard.DNQgLsb0.png)

Learn more about these features in our [blog post ↗︎](https://blog.cloudflare.com/radar-origin-pq-key-transparency-aspa) and check out the [Post-Quantum Encryption ↗︎](https://radar.cloudflare.com/post-quantum) and [Key Transparency ↗︎](https://radar.cloudflare.com/key-transparency) pages to explore the data.
