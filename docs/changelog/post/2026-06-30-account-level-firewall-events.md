---
url: https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/
title: Account-scoped firewall events dataset in Logpush \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.851038+00:00
---

# Account-scoped firewall events dataset in Logpush · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 30, 2026

## Account-scoped firewall events dataset in Logpush

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush now supports [firewall events as an account-scoped dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/). Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone.

The dataset includes a new [`ZoneName`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/#zonename) field so you can identify which zone each event came from when consuming logs in your downstream pipeline.

#### What's available

  * A new account-scoped `firewall_events` dataset, configurable via the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/) or the Cloudflare dashboard.
  * The same fields and filter expressions supported by the existing [zone-scoped firewall events dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/), plus the new `ZoneName` field.
  * Support for all existing Logpush destinations.


