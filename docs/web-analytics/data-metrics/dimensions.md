---
url: https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/
title: Dimensions \u00b7 Cloudflare Web Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:53.437883+00:00
---

# Dimensions · Cloudflare Web Analytics docs

> Source: https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)
  3. /[Data and metrics](https://developers.cloudflare.com/web-analytics/data-metrics/)
  4. /Dimensions



# Dimensions

Last updated Aug 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNavigation types

Dimensions are the labels used to describe different types of metrics or data. For example, **Referer** is the data collected from external links referring visits to a page, while **Browser** shows which browsers accessed your website.

Below you can find a list of the different dimensions you can use to filter Web Analytics:

  * **Country** : The visitor's country.
  * **Host** : The domain of the site's URL.
  * **Path** : The links within your site referring visits to a page.
  * **Referer** : The external links referring visits to a page. You can access `referer host` data on the dashboard. Additionally, you can access data for the `referer path` from the GraphQL API.
  * **Device type** : The device visitors use to access a page (for example, desktop, mobile, or tablet).
  * **Browser** : The web browser (for example, Chrome, Safari) visitors use to access your website.
  * **Operating system** : The operating system visitors use to access a page.
  * **Site** : The website's domain name. Used for high-level segmentation of data. For example, you can use it for a particular zone or gray-clouded website.
  * **Exclude Bots** : Exclude bot traffic from the dataset. With this dimension set to `Yes`, the resulting dataset will be a closer representation of real user traffic.
  * **Navigation type** : Which method was used to load the HTML document. Refer to Navigation types for a breakdown.

![Web Analytics dimensions page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=982,height=694,format=webp/_astro/dash-web_analytics-dimensions.DqK_-eil.png)

## Navigation types

Type | Cache hit? | Explanation  
---|---|---  
Navigate | ❌ | The visitor clicked a link or submitted a form but the document was either not found or stale in the browsers HTTP cache, so a network request was made to load the document.  
Navigate Cache | ✅ | The visitor clicked a link or submitted a form and the document was found and fresh within the browsers HTTP cache, so no network request was necessary for the document.  
Navigate Prefetch Cache | ✅ | The visitor clicked a link or submitted a form and the document has been prefetched into the browsers HTTP cache, so no network request was necessary for the document.  
Prerender | ✅ | The visitor clicked a link or submitted a form but the browser had already prerendered the page, so no network request was necessary for the document.  
Reload | ❌ | The visitor reloaded the page but the document was either not found or stale in the browsers HTTP cache, so a network request was made to load the document.  
Reload Cache | ✅ | The visitor reloaded the page and the document was found and fresh within the browsers HTTP cache, so no network request was necessary for the document.  
Back-forward | ❌ | The visitor used the back/forward buttons/gestures in their browser but the previously-loaded document either not found or stale in the browsers HTTP cache OR a feature was used which prevents using the cache (refer to the explanation in [Back/forward cache ↗︎](https://web.dev/articles/bfcache)), so a network request was made to load the document.  
Back-forward Cache | ✅ | The visitor used the back/forward buttons/gestures in their browser and the document was found and fresh within the browsers HTTP cache, so no network request was necessary for the document.  
Restore | ✅ | The browser was able to restore this page, for example when a tab has been paused due to inactivity.  
Soft Navigation | N/A | The visitor clicked a link or submitted a form but JavaScript intercepted the navigation and made a client-side update instead. Measured via [the native Soft Navigation API ↗︎](https://developer.chrome.com/docs/web-platform/soft-navigations).  
Routing APIs | N/A | The visitor clicked a link or submitted a form but JavaScript intercepted the navigation and made a client-side update instead. Measured via [the Navigation API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API) or [the History API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/History_API) when the Soft Navigation API is not supported.  
  
[PreviousCore Web Vitals](https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/)[NextData origin and collection](https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web-analytics/data-metrics/dimensions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
