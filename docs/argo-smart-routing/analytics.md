---
url: https://developers.cloudflare.com/argo-smart-routing/analytics/
title: Analytics \u00b7 Cloudflare Argo Smart Routing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:19.660063+00:00
---

# Analytics · Cloudflare Argo Smart Routing docs

> Source: https://developers.cloudflare.com/argo-smart-routing/analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Argo Smart Routing](https://developers.cloudflare.com/argo-smart-routing/)
  3. /Analytics



# Analytics

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/argo-smart-routing/analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksTypes of analytics

Cloudflare provides analytics to show the performance benefits of Argo Smart Routing.

You can access Argo analytics for your domain in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) at **Analytics** > **Performance**. For information on all analytics in the dashboard, refer to [Analytics](https://developers.cloudflare.com/analytics/).

## How it works

Analytics collects data based on the time-to-first-byte (TTFB) from your origin to the Cloudflare network. TTFB is the delay between when Cloudflare sends a request to your server and when it receives the first byte in response. Argo Smart Routing optimizes your server's network transit time to minimize this delay.

Note

Detailed performance data within **Origin Performance (Argo)** will only display if Argo has routed at least 500 origin requests within the last 48 hours.

## Types of analytics

The dashboard displays two different views for performance data:

  * **Origin Response Time** : A histogram shows response time from your origin to the Cloudflare network. The blue bars show time-to-first-byte (TTFB) without Argo, while the orange bars show TTFB where Argo found a Smart Route.

  * **Geography** : A map shows the improvement in response time at each Cloudflare data center.

    * A negative value indicates that requests from that location would not have benefited from Argo Smart Routing, so instead would have been routed directly.



[PreviousGet started](https://developers.cloudflare.com/argo-smart-routing/get-started/)[NextArgo for Packets](https://developers.cloudflare.com/argo-smart-routing/argo-for-packets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/argo-smart-routing/analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
