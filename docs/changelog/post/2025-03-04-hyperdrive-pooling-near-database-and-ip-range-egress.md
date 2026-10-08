---
url: https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/
title: Hyperdrive reduces query latency by up to 90% and now supports IP access control lists \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:05.323150+00:00
---

# Hyperdrive reduces query latency by up to 90% and now supports IP access control lists · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 7, 2025

## Hyperdrive reduces query latency by up to 90% and now supports IP access control lists

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now pools database connections in one or more regions close to your database. This means that your uncached queries and new database connections have up to 90% less latency as measured from connection pools.

![Hyperdrive query latency decreases by 90% during Hyperdrive's gradual rollout of regional pooling.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1732,height=836,format=webp/_astro/hyperdrive-regional-pooling-query-latency-improvement.Bzz_xvHZ.png)

By improving placement of Hyperdrive database connection pools, Workers' Smart Placement is now more effective when used with Hyperdrive, ensuring that your Worker can be placed as close to your database as possible.

With this update, Hyperdrive also uses [Cloudflare's standard IP address ranges ↗︎](https://www.cloudflare.com/ips/) to connect to your database. This enables you to configure the firewall policies (IP access control lists) of your database to only allow access from Cloudflare and Hyperdrive.

Refer to [documentation on how Hyperdrive makes connecting to regional databases from Cloudflare Workers fast](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).

This improvement is enabled on all Hyperdrive configurations.
