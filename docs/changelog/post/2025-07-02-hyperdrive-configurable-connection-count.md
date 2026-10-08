---
url: https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/
title: Hyperdrive now supports configuring the amount of database connections \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:16.135646+00:00
---

# Hyperdrive now supports configuring the amount of database connections · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 3, 2025

## Hyperdrive now supports configuring the amount of database connections

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.

All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the [Hyperdrive limits of your Workers plan](https://developers.cloudflare.com/hyperdrive/platform/limits/).

This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.

Refer to the [Hyperdrive configuration documentation](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/) for more information.
