---
url: https://developers.cloudflare.com/changelog/post/2026-04-28-enforce-dns-only/
title: Account-level enforce DNS-only \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:39.382905+00:00
---

# Account-level enforce DNS-only · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-28-enforce-dns-only/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 28, 2026

## Account-level enforce DNS-only

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now disable Cloudflare's reverse proxy across all zones in your account simultaneously using the new `enforce_dns_only` setting. When enabled, Cloudflare responds to DNS queries for all proxied records with your origin IP addresses instead of Cloudflare's anycast IPs. This account-level kill switch is designed for incident response scenarios where you need to quickly route traffic directly to your origin servers.

Caution

Enabling this setting exposes your origin IP addresses and removes all Cloudflare protections — including DDoS mitigation, WAF, caching, and all other proxy-based features — for every zone in your account. Use with extreme caution and only after proper [preparations](https://developers.cloudflare.com/dns/proxy-status/enforce-dns-only/#preparation).

#### Key characteristics

  * **Account-level** — Affects all zones in the account simultaneously with a single API call.
  * **Non-destructive** — Does not modify your DNS records. Disabling the setting restores normal proxy behavior.
  * **API-only** — Available through the API only, not in the Cloudflare dashboard.



#### What's affected

**Included:** Standard proxied A, AAAA, and CNAME records, Load Balancing records, and records matching Worker routes.

**Excluded:** Spectrum applications, Cloudflare Tunnel CNAMEs, R2 custom domains, Web3 gateways, and Workers custom domains continue to operate normally.

#### Before you enable

  * Verify your origin servers can handle direct traffic without Cloudflare's caching and filtering.
  * Review which origin IPs will become publicly visible through DNS queries.
  * Test the API in a staging account before relying on it for incident response.



#### Availability

Available via API to all Cloudflare customers.

For information on how to use it, refer to [Enforce DNS-only developer documentation](https://developers.cloudflare.com/dns/proxy-status/enforce-dns-only/) .
