---
url: https://developers.cloudflare.com/dns/dns-firewall/
title: DNS Firewall \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:56.113564+00:00
---

# DNS Firewall · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/dns-firewall/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /DNS Firewall



# DNS Firewall

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/dns-firewall/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow DNS Firewall worksBenefits

Speed up and protect entire authoritative nameservers

Enterprise-only paid add-on

Cloudflare DNS Firewall proxies all DNS queries to your nameservers through Cloudflare’s global network. This action protects upstream nameservers from DDoS attacks and reduces load by caching DNS responses.

![Diagram showing protection provided by DNS Firewall. For more details, read further.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1222,height=816,format=webp/_astro/dns-firewall-overview.DCpibQR6.png)

DNS Firewall is for customers who need to speed up and protect entire authoritative nameservers. If you need to speed up and protect individual zones, refer to Cloudflare DNS [Setups](https://developers.cloudflare.com/dns/zone-setups/).

* * *

## How DNS Firewall works

When a DNS query for your domain takes place:

  1. Queries go to the Cloudflare data center that is closest to the website visitor. This is determined by the location of the DNS resolver.
  2. Cloudflare tries to return a DNS response from cache.
  3. If the response is not available in cache, Cloudflare queries the upstream authoritative nameservers.
  4. After returning the response from the nameservers, Cloudflare temporarily caches it for subsequent DNS queries.



* * *

## Benefits

DNS Firewall provides the following benefits while allowing your organization total control over your authoritative nameservers:

  * DDoS mitigation
  * High availability
  * Global distribution
  * Enhanced performance
  * Bandwidth savings
  * [Rate limiting per data center](https://developers.cloudflare.com/dns/dns-firewall/setup/#additional-options)
  * Minimum and maximum cache TTL specification
  * DNS [ANY ↗︎](https://datatracker.ietf.org/doc/html/rfc8482) query type block



[PreviousAnalytics and logs](https://developers.cloudflare.com/dns/internal-dns/analytics/)[NextSetup](https://developers.cloudflare.com/dns/dns-firewall/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/dns-firewall/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
