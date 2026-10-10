---
url: https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/
title: Hyperdrive exposes database connection pool size metrics \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.089038+00:00
---

# Hyperdrive exposes database connection pool size metrics · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 15, 2026

## Hyperdrive exposes database connection pool size metrics

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the `hyperdrivePoolSizesAdaptiveGroups` dataset in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/), you can see `waitingClients`, `currentPoolSize`, `availablePoolSlots`, and `maxPoolSize` for each of your configurations.

A new **Pool connections** chart has been added to the **Metrics** tab of each Hyperdrive configuration in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com). You can use the location selector to drill down into specific locations hosting your connection pool by airport code.

![Hyperdrive pool size metrics chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2604,height=890,format=webp/_astro/hyperdrive-pool-size-metrics-chart.DZxLTFgB.png)

The chart shows:

  * **Waiting clients** : Client requests waiting for an available connection.
  * **Open connections** : Active connections to your database.
  * **Pool size maximum** : Your configured origin connection limit.



Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to [increase your Hyperdrive connection limit](https://developers.cloudflare.com/hyperdrive/platform/limits/#request-a-limit-increase).

#### Pool size metrics

The `hyperdrivePoolSizesAdaptiveGroups` dataset in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/getting-started/) exposes the following key connection pool metrics for each Hyperdrive configuration:

Under `avg`:

  * **`currentPoolSize`** — Average number of connections currently open in the pool.
  * **`availablePoolSlots`** — Average number of pool connections available for checkout.
  * **`waitingClients`** — Average number of clients waiting for a connection from the pool.



Under `max`:

  * **`maxPoolSize`** — Configured maximum size of the connection pool.
  * **`currentPoolSize`** — Peak number of connections open in the pool.
  * **`waitingClients`** — Peak number of clients waiting for a connection from the pool.



For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/hyperdrive/observability/metrics/) and [Connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).
