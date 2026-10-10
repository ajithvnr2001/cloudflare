---
url: https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/
title: Account-level DNS records quota \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.792383+00:00
---

# Account-level DNS records quota · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 10, 2026

## Account-level DNS records quota

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now enforces DNS records quotas at the account level for Enterprise accounts. Instead of a per-zone limit, these accounts have a quota on the total number of records across all of their zones, letting you distribute records across your zones however you like — regardless of each zone's plan. Public and internal zones are counted separately, each with a default quota of 1,000,000 records.

Accounts without an account-level quota are unaffected: existing per-zone quotas behave exactly as before.

For more details, refer to [DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#dns-records-quota).
