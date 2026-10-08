---
url: https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/
title: TLD Insights in Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:27.368460+00:00
---

# TLD Insights in Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 27, 2025

## TLD Insights in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-27-radar-tld-insights/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now introduces Top-Level Domain (TLD) insights, providing visibility into popularity based on the DNS magnitude metric, detailed TLD information including its type, manager, DNSSEC support, RDAP support, and WHOIS data, and trends such as DNS query volume and geographic distribution observed by the [1.1.1.1](https://developers.cloudflare.com/1.1.1.1/) DNS resolver.

The following dimensions were added to the Radar DNS API, specifically, to the [`/dns/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) and [`/dns/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries_groups_v2/) endpoints:

  * `tld`: Top-level domain extracted from DNS queries; can also be used as a filter.
  * `tld_dns_magnitude`: Top-level domain ranking by [DNS magnitude](https://developers.cloudflare.com/radar/glossary#dns-magnitude).



And the following endpoints were added:

  * [`/tlds`](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/methods/list/) \- Lists all TLDs.
  * [`/tlds/{tld}`](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/methods/get/) \- Retrieves information about a specific TLD.

![Screenshot of the TLD ranking by DNS magnitude](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=2344,format=webp/_astro/tld-ranking-by-dns-magnitude.DbmrooPK.png)

Learn more about the new Radar DNS insights in our [blog post ↗︎](https://blog.cloudflare.com/introducing-tld-insights-on-cloudflare-radar/), and check out the [new Radar page ↗︎](https://radar.cloudflare.com/tlds).
