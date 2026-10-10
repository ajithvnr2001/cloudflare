---
url: https://developers.cloudflare.com/changelog/post/2026-08-20-durable-objects-deployments-tab/
title: View deployments for Durable Objects in the dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.670552+00:00
---

# View deployments for Durable Objects in the dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-20-durable-objects-deployments-tab/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 20, 2026

## View deployments for Durable Objects in the dashboard

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Object namespaces now have a **Deployments** tab in the Cloudflare dashboard, showing the [versions](https://developers.cloudflare.com/workers/versions-and-deployments/#versions) of the backing Worker that are currently live and the traffic split between them.

![The Deployments tab for a Durable Object namespace, showing two versions with their traffic %, requests/sec, error rate, and median wall time](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2508,height=654,format=webp/_astro/durable-objects-deployments-tab.ZJc93gIt.png)[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

A Durable Object namespace is backed by a Worker script, so its deployments are the same as that Worker's deployments. Previously, checking on a [gradual deployment](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/) in progress for a Durable Object meant navigating to the backing Worker. The new tab surfaces that information directly on the namespace, alongside the metrics that matter for it: requests, error rate, and wall time per version.

The tab is read-only — promoting, rolling back, or splitting traffic on a deployment is still managed from the backing Worker's Deployments tab.

#### Actual vs. configured traffic split

The **Traffic %** column, for both Workers and Durable Objects, now shows the actual, observed traffic share for each version next to the percentage you configured. Previously, this column only showed the configured percentage. If you moved a deployment from 50/50 to 100% on a new version, the configured number updated immediately, but requests take time to catch up, and there was no way to tell how far along that shift was without checking metrics elsewhere.

The configured split assigns Worker versions to individual Durable Objects, not to individual requests. Because [each Durable Object is pinned to the version it started on until you create a new deployment](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/with-durable-objects/) and some objects naturally receive more traffic than others, the observed split can differ from the configured one for as long as multiple versions are active.

Actual traffic share is calculated from the same [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) data that powers other Workers and Durable Objects metrics, so standard ingestion delay and [sampling](https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/) apply. Durable Objects analytics can lag Workers analytics by several minutes, so a version's actual share may take a little longer to catch up after a change.

To view this, go to **Workers & Pages** > **Durable Objects** , select a namespace, then select the **Deployments** tab. For more on how gradual deployments work, refer to [Gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/).
