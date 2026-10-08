---
url: https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/
title: DNS Insights in Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:05.547164+00:00
---

# DNS Insights in Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 27, 2025

## DNS Insights in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-27-radar-dns-insights/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its DNS insights, providing visibility into aggregated traffic and usage trends observed by our [1.1.1.1](https://developers.cloudflare.com/1.1.1.1/) DNS resolver. In addition to global, location, and ASN traffic trends, we are also providing perspectives on protocol usage, query/response characteristics, and DNSSEC usage.

Previously limited to the [`top`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/top/) locations and ASes endpoints, we have now introduced the following endpoints:

  * [`/dns/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries/): Retrieves DNS query volume over time.
  * [`/dns/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/): Retrieves summaries of DNS query distribution across ten different dimensions.
  * [`/dns/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/): Retrieves timeseries data for DNS query distribution across ten different dimensions.



For the `summary` and `timeseries_groups` endpoints, the following dimensions are available, displaying the distribution of DNS queries based on:

  * `cache_hit`: Cache status (hit vs. miss).
  * `dnsssec`: DNSSEC support status (secure, insecure, invalid or other).
  * `dnsssec_aware`: DNSSEC client awareness (aware vs. not-aware).
  * `dnsssec_e2e`: End-to-end security (secure vs. insecure).
  * `ip_version`: IP version (IPv4 vs. IPv6).
  * `matching_answer`: Matching answer status (match vs. no-match).
  * `protocol`: Transport protocol (UDP, TLS, HTTPS or TCP).
  * `query_type`: Query type (`A`, `AAAA`, `PTR`, etc.).
  * `response_code`: Response code (`NOERROR`, `NXDOMAIN`, `REFUSED`, etc.).
  * `response_ttl`: Response TTL.



Learn more about the new Radar DNS insights in our [blog post ↗︎](https://blog.cloudflare.com/new-dns-section-on-cloudflare-radar/), and check out the [new Radar page ↗︎](https://radar.cloudflare.com/dns).
