---
url: https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/
title: Data origin and collection \u00b7 Cloudflare Web Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:53.353835+00:00
---

# Data origin and collection · Cloudflare Web Analytics docs

> Source: https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)
  3. /[Data and metrics](https://developers.cloudflare.com/web-analytics/data-metrics/)
  4. /Data origin and collection



# Data origin and collection

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewData collection and reporting

Web Analytics relies on the `performance.getEntriesByType('navigation')` object to collect metrics about page load performance. If Navigation Timing Level 2 is not supported, then [`performance.timing` (Level 1) ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Performance/timing) is used.

Refer to the [W3C Processing Model ↗︎](https://www.w3.org/TR/navigation-timing-2/#processing-model) for a visual depiction of the sequence of timing events for web page loads.

## Data collection and reporting

Web Analytics collects the minimum amount of information - timing metrics - to show customers how their websites perform. Cloudflare does not track individual end users across our customers’ Internet properties.

The Web Analytics performance beacon loads from `https://static.cloudflareinsights.com/beacon.min.js`. You may need to update your [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) settings to load this script.

Beacon data is sent to `https://<yourdomainname>/cdn-cgi/rum` for sites proxied through Cloudflare or `https://cloudflareinsights.com/cdn-cgi/rum` for sites not proxied through Cloudflare. Core Web Vital metrics are reported when the `visibilityState` is hidden for the first time after the page load event is triggered.

[PreviousDimensions](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/)[NextLimits](https://developers.cloudflare.com/web-analytics/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web-analytics/data-metrics/data-origin-and-collection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
