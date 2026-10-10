---
url: https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/
title: Shadowed record warnings are now available for all zones \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.190072+00:00
---

# Shadowed record warnings are now available for all zones · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 14, 2026

## Shadowed record warnings are now available for all zones

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now displays warnings for shadowed records in all zones. A record is shadowed when a subdomain delegation gives authority for its name, or a name below it, to another set of nameservers. The record remains present, but your zone is not authoritative for it thus Cloudflare will not respond with it to matching DNS queries. These warnings help you find records that may no longer resolve from the expected zone.

Shadow metadata is also available in DNS records API responses when you set `include_shadow_metadata=true`. The metadata identifies the delegating `NS` records and, when applicable, whether an `A` or `AAAA` record is glue. For more information, refer to [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records/).
