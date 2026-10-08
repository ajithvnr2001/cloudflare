---
url: https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/
title: Time to Live (TTL) \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:59.500954+00:00
---

# Time to Live (TTL) · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)

  4. /Reference
  5. /Time to Live (TTL)



# Time to Live (TTL)

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProxied recordsUnproxied recordsNameserver TTL

**Time to Live (TTL)** is a field on [DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) that controls how long each record is cached and — as a result — how long it takes for record updates to reach your end users.

Longer TTLs speed up [DNS lookups ↗︎](https://www.cloudflare.com/learning/dns/what-is-dns/) by increasing the chance of cached results, but a longer TTL also means that updates to your records take longer to go into effect.

## Proxied records

By default, all [proxied records](https://developers.cloudflare.com/dns/proxy-status/) have a TTL of **Auto** , which is set to 300 seconds. This value cannot be edited.

Since only [records used for IP address resolution](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/#ip-address-resolution) can be proxied, this setting ensures that potential changes to the assigned [anycast IP address](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/) will take effect quickly, as recursive resolvers will not cache them for longer than 300 seconds (five minutes).

Note

It may take longer than 5 minutes for you to actually experience record changes, as your local DNS cache may take longer to update.

## Unproxied records

For **DNS only** records, you can choose a TTL between **30 seconds** (Enterprise) or **60 seconds** (non-Enterprise) and **1 day**.

A TTL of **Auto** is set to 300 seconds (five minutes).

## Nameserver TTL

[Nameserver TTL](https://developers.cloudflare.com/dns/nameservers/nameserver-options/#nameserver-ttl) is a separate feature and only affects Cloudflare nameservers and custom nameservers. For other [NS records](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/#ns) on your DNS records table, TTL is controlled by their respective TTL fields.

[PreviousDNS record types](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/)[NextRecord attributes](https://developers.cloudflare.com/dns/manage-dns-records/reference/record-attributes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/manage-dns-records/reference/ttl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
